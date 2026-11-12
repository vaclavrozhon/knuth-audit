"""Complete finite Wang-tile neighborhoods via row transfer and original XCC."""
from collections import defaultdict
from datetime import datetime,timezone
from pathlib import Path
import json
import graph_native
from puzzle_xcc import encode,save

ROOT=graph_native.ROOT;OUT=ROOT/'results/graphs117_120';sha=graph_native.sha

def row_boards(tiles,n):
    rows=[]
    def row(prefix):
        if len(prefix)==n:rows.append(tuple(prefix));return
        for k,t in enumerate(tiles):
            if not prefix or tiles[prefix[-1]][1]==t[3]:row(prefix+[k])
    row([])
    bytop=defaultdict(list)
    for r in rows:bytop[''.join(tiles[t][0] for t in r)].append(r)
    boards=[]
    def visit(prefix):
        if len(prefix)==n:boards.append(tuple(t for r in prefix for t in r));return
        allowed=rows if not prefix else bytop[''.join(tiles[t][2] for t in prefix[-1])]
        for r in allowed:visit(prefix+[r])
    visit([])
    return boards,len(rows)

def encoding(tiles,n):
    primary=[f'p{r}{c}' for r in range(n) for c in range(n)]
    secondary=[f'h{r}{c}' for r in range(n+1) for c in range(n)]
    secondary += [f'v{r}{c}' for r in range(n) for c in range(n+1)]
    colors={c:i+1 for i,c in enumerate('WRBK')};options=[];placements=[]
    for r in range(n):
        for c in range(n):
            for k,t in enumerate(tiles):
                options.append([(f'p{r}{c}',0),(f'h{r}{c}',colors[t[0]]),(f'v{r}{c+1}',colors[t[1]]),
                                (f'h{r+1}{c}',colors[t[2]]),(f'v{r}{c}',colors[t[3]])])
                placements.append((r*n+c,k))
    return encode(primary,secondary,options),placements

def main():
    data=json.loads((OUT/'tetrads120-vectors.json').read_text());results=[]
    graph_native.OUT=OUT
    for letter,tiles in zip('ab',data['families']):
        boards,rowcount=row_boards(tiles,5);assert len(boards)==len(set(boards))
        enc,placements=encoding(tiles,5)
        native=graph_native.run('tetrads120-'+letter,enc)
        assert native['status']=='completed'
        actual=set()
        for model in graph_native.models('tetrads120-'+letter,enc):
            board=[None]*25
            for i in model:
                u,k=placements[i];assert board[u] is None;board[u]=k
            assert None not in board;actual.add(tuple(board))
        assert actual==set(boards) and len(actual)==native['solutions']
        groups=[[b for b in boards if b[12]==k] for k in range(10)]
        forced=[''.join(str(bs[0][u]) if len({b[u] for b in bs})==1 else '?' for u in range(25)) for bs in groups]
        if letter=='a':
            assert list(map(len,groups))==[16,8,19,8,8,8,10,8,16,24]
            assert forced==[g['board'] for g in data['forced_neighborhoods']]
        results.append(dict(family=letter,tiles=tiles,row_patterns=rowcount,boards=sorted(actual),
            counts_by_center=list(map(len,groups)),forced_neighborhoods=forced,
            native_result_sha256=sha(OUT/('tetrads120-'+letter+'.json')),complete_sets_equal=True))
    save(OUT/'tetrads120-finite-checked.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),script_sha256=sha(__file__),
        vectors_sha256=sha(OUT/'tetrads120-vectors.json'),families=results,
        scope='All5x5 neighborhoods and all displayed forced entries; infinite-plane uniqueness needs a separate propagation certificate.'))
    print([(r['family'],r['counts_by_center'],len(r['boards'])) for r in results])

if __name__=='__main__':main()

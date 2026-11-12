#!/usr/bin/env python3
"""DLX72--74: enumerate geometric tilings; independently verify record boards."""
from collections import Counter
from datetime import datetime, timezone
from functools import lru_cache
import gzip
import json
from pathlib import Path
import subprocess
import tempfile
import numpy as np
from dlx1_audit_tools import ROOT, sha, run, input_text

OUT = ROOT/'results/dominosa72'
PAIRS = [(x,y) for x in range(7) for y in range(x,7)]
EDGES = [(8*r+c,8*r+c+1) for r in range(7) for c in range(7)]
EDGES += [(8*r+c,8*r+c+8) for r in range(6) for c in range(8)]
BOARDS = {
 'keller2004': '66110144/26611514/52132140/55322200/53242006/36430565/33643054',
 'gonzalez2023': '06151146/66611014/56132144/55326224/53632022/34300525/33040054',
 'sermulins2005': '13122234/41112342/44010264/40006026/54050361/15553656/52533366',
 'knuth74': '15133034/21446115/22056105/65460423/22465553/61102332/63600044',
}
EXPECTED = dict(keller2004=730924, gonzalez2023=807752, sermulins2005=793648, knuth74=1)


def build():
    manifest = OUT/'build.json'
    if manifest.exists():
        d = json.loads(manifest.read_text())
        assert d['source_sha256'] == sha(ROOT/'dominosa_count.cc')
        assert d['binary_sha256'] == sha(d['binary'])
        return d
    directory = Path(tempfile.mkdtemp(prefix='knuth-vol4b-dominosa-'))
    binary = directory/'dominosa'
    command = ['g++','-O3','-std=c++17',str(ROOT/'dominosa_count.cc'),'-o',str(binary)]
    subprocess.run(command,check=True)
    d = dict(source_sha256=sha(ROOT/'dominosa_count.cc'),binary=str(binary),
             binary_sha256=sha(binary),command=command)
    manifest.write_text(json.dumps(d,indent=2)+'\n')
    return d


def instance(board, cells_first=False):
    names = [f'D{x}{y}' for x,y in PAIRS]+[f'p{r}{c}' for r in range(7) for c in range(8)]
    rows = [[PAIRS.index(tuple(sorted((board[u],board[v]))))+1,u+29,v+29] for u,v in EDGES]
    if cells_first:
        names = names[28:]+names[:28]
        rows = [[i-28 if i>28 else i+56 for i in row] for row in rows]
    return names,rows


def transfer_count(height,width):
    # Independent row-by-row transfer; incoming/outgoing vertical occupancy only.
    @lru_cache(None)
    def transitions(mask):
        output = Counter()
        def fill(pos,occupied,outgoing):
            if pos == width:
                output[outgoing] += 1
            elif occupied>>pos&1:
                fill(pos+1,occupied,outgoing)
            else:
                fill(pos+1,occupied|1<<pos,outgoing|1<<pos)
                if pos+1<width and not occupied>>(pos+1)&1:
                    fill(pos+2,occupied|3<<pos,outgoing)
        fill(0,mask,0)
        return output
    state = {0:1}
    for _ in range(height):
        new = Counter()
        for incoming,count in state.items():
            for outgoing,mult in transitions(incoming).items():
                new[outgoing] += count*mult
        state = new
    return state.get(0,0)


def tilings(build_info):
    path = OUT/'tilings.u8.gz'
    if not path.exists():
        raw = Path(build_info['binary']).parent/'tilings.u8'
        result = subprocess.run([build_info['binary'],'tilings',str(raw)],check=True,capture_output=True,text=True)
        data = raw.read_bytes()
        with gzip.GzipFile(path,'wb',mtime=0) as f: f.write(data)
        (OUT/'tilings-enumeration.json').write_text(json.dumps(json.loads(result.stdout),indent=2)+'\n')
        raw.unlink()
    data = gzip.decompress(path.read_bytes())
    return np.frombuffer(data,dtype=np.uint8).reshape((-1,28))


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    build_info = build()
    tiles = tilings(build_info)
    assert len(tiles) == transfer_count(7,8) == transfer_count(8,7) == 1292697
    # All geometric models are distinct, cover every cell once, and have 28 edges.
    sorted_tiles = np.sort(tiles,axis=1)
    assert len(np.unique(sorted_tiles,axis=0)) == len(tiles)
    cells = np.array(EDGES,dtype=np.uint8)[tiles].reshape((-1,56))
    assert np.all(np.sort(cells,axis=1) == np.arange(56))
    names = [f'p{r}{c}' for r in range(7) for c in range(8)]
    native,_ = run(OUT,'geometric',input_text(names,[[u+1,v+1] for u,v in EDGES]))
    assert native['solutions'] == len(tiles)
    result = dict(source_sha256=sha(__file__),build=build_info,edges=EDGES,
      geometric=dict(count=len(tiles),native=native,transfer_both_orientations=len(tiles),
                     archive_sha256=sha(OUT/'tilings.u8.gz'),all_models_valid_and_distinct=True),cases={})
    inp = '\n'.join(s.replace('/','') for s in BOARDS.values())+'\n'
    detail_run = subprocess.run([build_info['binary'],'details'],input=inp,text=True,
                               capture_output=True,check=True,timeout=600)
    detail = [json.loads(s) for s in detail_run.stdout.splitlines()]
    assert len(detail) == len(BOARDS)
    for (label,text),d in zip(BOARDS.items(),detail):
        board = [int(c) for c in text if c!='/']
        assert Counter(board) == {x:8 for x in range(7)}
        types = np.array([PAIRS.index(tuple(sorted((board[u],board[v])))) for u,v in EDGES],dtype=np.uint32)
        valid = np.bitwise_or.reduce(np.left_shift(np.uint32(1),types[tiles]),axis=1) == (1<<28)-1
        solutions = tiles[valid]
        freq = np.bincount(solutions.ravel(),minlength=97).tolist()
        assert len(solutions) == d['count'] == EXPECTED[label]
        assert freq == d['frequency'] and sum(freq) == 28*len(solutions)
        items,rows = instance(board)
        stats,_ = run(OUT,label,input_text(items,rows),timeout=600)
        assert stats['solutions'] == len(solutions)
        path = OUT/(label+'-models.u8.gz')
        with gzip.GzipFile(path,'wb',mtime=0) as f: f.write(solutions.tobytes())
        zero = [EDGES[i] for i,c in enumerate(freq) if not c]
        r = dict(board=text,solutions=len(solutions),frequency=freq,zero_edges=zero,
                 minimum_positive_frequency=min(x for x in freq if x),
                 direct_cell_search=d,native=stats,all_models_archive_sha256=sha(path),
                 count_and_edge_frequencies_independently_equal=True,
                 candidate_type_frequencies=np.bincount(types,minlength=28).tolist())
        if label == 'keller2004':
            assert zero == [(17,18)] and r['minimum_positive_frequency']==31370
        if label == 'gonzalez2023':
            assert not zero and r['minimum_positive_frequency']==35082
        if label == 'knuth74':
            assert Counter(r['candidate_type_frequencies']) == {3:15,4:13}
            solution = [EDGES[i] for i in solutions[0]]
            owner = {v:i for i,e in enumerate(solution) for v in e}
            tatami = all(len({owner[8*r+c],owner[8*r+c+1],owner[8*r+8+c],owner[8*r+9+c]})<4
                         for r in range(6) for c in range(7))
            r.update(unique_solution=solution,tatami=tatami)
            assert tatami
            cells_items,cells_rows = instance(board,cells_first=True)
            second,_ = run(OUT,label+'-cells-first',input_text(cells_items,cells_rows))
            assert second['solutions']==1
            r['native_cells_first']=second
        result['cases'][label]=r
        print(label,len(solutions),'minimum frequency',r['minimum_positive_frequency'],
              'native nodes',stats['nodes'],flush=True)
    result.update(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat())
    (OUT/'records.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: all geometric tilings; three independent counts per board; two full edge-frequency calculations.')


if __name__=='__main__': main()

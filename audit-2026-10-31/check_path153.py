"""Independent transcription and full enumeration of TAOCP 4B X153(a,c)."""
from collections import Counter,defaultdict
from pathlib import Path
import json,subprocess,time
from pysat.card import CardEnc,EncType
from pysat.solvers import Solver
from check_path_dominoes import placements,boundary,OUT


def normalized(pairs,tip):
    return tuple(sorted(tuple(sorted(p)) for p in pairs)),tip


def turn(piece):
    pairs,tip=piece
    return normalized([((a+3)%6,(b+3)%6) for a,b in pairs],
                      -1 if tip<0 else (tip+3)%6)


def canon(piece):return min(piece,turn(piece))

# Pieces in the question, left to right, all drawn vertically. The last two
# are terminal pieces. Ports use check_path_dominoes.placements convention.
QUESTION=[([(5,1)],-1), ([(5,0)],-1), ([(2,1)],-1), ([(5,2)],-1),
          ([(0,3),(1,4)],-1), ([(3,0),(2,1)],-1),
          ([(4,0)],3), ([(0,2)],1)]
# Printed answer: RIGHT diagram = (a), LEFT diagram = (c).
# Each tuple: first row, first column, orientation, pairs, terminal port.
FIG_A=[(0,0,'V',[(0,2)],1),(0,1,'V',[(1,4),(0,3)],-1),
       (0,2,'H',[(5,4)],-1),(1,2,'H',[(5,4),(0,3)],-1),
       (2,0,'V',[(5,1)],-1),(2,2,'H',[(1,3)],0),
       (3,1,'H',[(5,2)],-1),(3,3,'H',[(0,5)],-1)]
FIG_C=[(1,0,'V',[(0,1)],-1),(1,1,'V',[(1,4),(0,3)],-1),
       (0,2,'V',[(0,3),(1,2)],-1),(2,2,'V',[(5,1)],4),
       (0,3,'H',[(5,3)],4),(1,3,'V',[(0,4),(5,1)],-1),
       (1,4,'V',[(5,4),(3,2)],-1),(3,3,'H',[(1,5)],-1)]


def inventory(fig):return sorted(canon(normalized(pairs,tip)) for r,c,d,pairs,tip in fig)


def options(pieces):
    result=[]
    for place in placements(4,5):
        for i,piece in enumerate(pieces):
            for pairs,tip in sorted({piece,turn(piece)}):
                active={v for pair in pairs for v in pair}
                if tip>=0:active.add(tip)
                if any(boundary(place['ports'][j],4,5) for j in active):continue
                result.append(dict(place,piece=i,pairs=pairs,tip=tip,
                    mask=sum(1<<v for v in active)))
    for r in range(4):
        for c in range(5):
            result.append(dict(cells=((r,c),),orientation='B',piece=-1,
                pairs=(),tip=-1,mask=0,
                ports=((2*r,2*c+1),(2*r+1,2*c+2),(2*r+2,2*c+1),(2*r+1,2*c))))
    return result


def verify(selected,pieces):
    assert Counter(cell for o in selected for cell in o['cells'])==Counter((r,c) for r in range(4) for c in range(5))
    assert Counter(o['piece'] for o in selected if o['piece']>=0)==Counter(range(8))
    edge=defaultdict(list);graph=defaultdict(set)
    for o in selected:
        for j,p in enumerate(o['ports']):edge[p].append(o['mask']>>j&1)
        if o['piece']<0:continue
        assert canon(normalized(o['pairs'],o['tip']))==pieces[o['piece']]
        arcs=[(o['ports'][a],o['ports'][b]) for a,b in o['pairs']]
        if o['tip']>=0:arcs.append((o['ports'][o['tip']],('terminal',o['piece'])))
        for a,b in arcs:graph[a].add(b);graph[b].add(a)
    for p,values in edge.items():
        if boundary(p,4,5):assert values==[0]
        else:assert len(values)==2 and values[0]==values[1]
    assert sorted(map(len,graph.values())).count(1)==2
    assert all(len(v) in (1,2) for v in graph.values())
    unseen=set(graph);comps=[]
    while unseen:
        todo=[unseen.pop()];seen=set(todo)
        while todo:
            for b in graph[todo.pop()]:
                if b not in seen:seen.add(b);unseen.remove(b);todo.append(b)
        comps.append(seen)
    return len(comps)==1


def picture_options(fig,pieces,opts):
    selected=[]
    for r,c,d,pairs,tip in fig:
        piece=canon(normalized(pairs,tip));i=pieces.index(piece)
        matches=[o for o in opts if o['cells'][0]==(r,c) and o['orientation']==d and
                 o['piece']==i and normalized(o['pairs'],o['tip'])==normalized(pairs,tip)]
        assert len(matches)==1,(r,c,d,pairs,tip)
        selected+=matches
    occupied={p for o in selected for p in o['cells']}
    selected += [o for o in opts if o['piece']<0 and o['cells'][0] not in occupied]
    assert verify(selected,pieces)
    return selected


def sig(selected):
    return tuple(sorted((o['cells'],o['piece'],normalized(o['pairs'],o['tip'])) for o in selected))


def transformed(selected,flipr,flipc,opts):
    # Match actual local arcs, not merely port masks, after an isometry.
    point=lambda p:(8-p[0] if flipr else p[0],10-p[1] if flipc else p[1])
    lookup={}
    def key(o,transform=False):
        f=point if transform else lambda p:p
        cells=tuple(sorted((3-r if flipr and transform else r,
                            4-c if flipc and transform else c) for r,c in o['cells']))
        arcs=tuple(sorted(tuple(sorted((f(o['ports'][a]),f(o['ports'][b])))) for a,b in o['pairs']))
        tip=f(o['ports'][o['tip']]) if o['tip']>=0 else (-1,-1)
        return cells,arcs,tip
    for o in opts:lookup[key(o)]=o
    try:return sig([lookup[key(o,True)] for o in selected])
    except KeyError:return None


def run(name,fig):
    start=time.monotonic();pieces=inventory(fig);assert len(set(pieces))==8
    if name=='153a':assert pieces==sorted(canon(normalized(*p)) for p in QUESTION)
    opts=options(pieces);picture=picture_options(fig,pieces,opts)
    by=defaultdict(list);edges=sorted({p for o in opts for p in o['ports'] if not boundary(p,4,5)})
    evars={p:len(opts)+i+1 for i,p in enumerate(edges)};top=len(opts)+len(edges);clauses=[]
    for i,o in enumerate(opts,1):
        for cell in o['cells']:by['cell',cell].append(i)
        if o['piece']>=0:by['piece',o['piece']].append(i)
        for j,p in enumerate(o['ports']):
            if p in evars:clauses.append([-i,evars[p] if o['mask']>>j&1 else -evars[p]])
    for vv in by.values():
        card=CardEnc.equals(vv,bound=1,top_id=top,encoding=EncType.seqcounter)
        top=max(top,card.nv);clauses.extend(card.clauses)
    sols=[];full=set();single=set()
    with Solver(name='g4',bootstrap_with=clauses) as solver:
        while solver.solve():
            ids=[v for v in solver.get_model() if 0<v<=len(opts)]
            selected=[opts[v-1] for v in ids];valid=verify(selected,pieces)
            s=sig(selected);assert s not in full;full.add(s)
            if valid:single.add(s)
            sols.append(dict(ids=ids,single_path=valid))
            solver.add_clause([-i for i in ids])
    assert sig(picture) in single
    orbits={min(t for r in (False,True) for c in (False,True)
                if (t:=transformed([opts[i-1] for i in sol['ids']],r,c,opts)) is not None)
            for sol in sols if sol['single_path']}
    cnames={cell:f'c{cell[0]}{cell[1]}' for kind,cell in by if kind=='cell'}
    enames={p:f'e{p[0]}{p[1]}' for p in edges}
    lines=[' '.join(list(cnames.values())+[f'p{i}' for i in range(8)]+['|']+list(enames.values()))]
    for o in opts:
        row=[cnames[c] for c in o['cells']]
        if o['piece']>=0:row.append(f'p{o["piece"]}')
        row += [f'{enames[p]}:{o["mask"]>>j&1}' for j,p in enumerate(o['ports']) if p in enames]
        lines.append(' '.join(row))
    base=OUT/name;base.with_suffix('.xcc').write_text('\n'.join(lines)+'\n')
    native=subprocess.run(['/tmp/knuth-dlx2','v1','d0','m1'],input='\n'.join(lines)+'\n',text=True,capture_output=True,timeout=300)
    base.with_suffix('.dlx2.txt').write_text(native.stdout+native.stderr)
    import re
    count=int(re.search(r'Altogether (\d+) solution',native.stderr)[1]);assert count==len(full)
    out=dict(name=name,options=len(opts),matching_solutions=len(full),single_path_solutions=len(single),
        symmetry_classes=len(orbits),dlx2_solutions=count,question_inventory_matches=name=='153a',
        printed_figure_single_path=True,pieces=pieces,figure=picture,solutions=sols,seconds=time.monotonic()-start)
    base.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('pieces','figure','solutions')}),flush=True)

if __name__=='__main__':
    run('153a',FIG_A);run('153c',FIG_C)

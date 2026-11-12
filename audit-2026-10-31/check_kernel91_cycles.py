"""Exact word-distinct cycle pruning, with explicit incomplete-search handling."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time

from word_kernel91 import graph, core, components, LEFT36, RIGHT5
from double_word_tools import dictionary, validate

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/stair_kernels'


def cyclic_edges(edges):
    parts=components(edges);owner={v:i for i,part in enumerate(parts) for v in part}
    return [e for e in edges if owner[e[0]]==owner[e[1]]]


def one_cycle(start,adj,limit=None):
    """A simple cycle is sufficient for testing participation in any closed walk."""
    nodes=0;seen={start};path=[]
    def visit(v,used):
        nonlocal nodes
        nodes+=1
        if limit and nodes>limit:raise TimeoutError('node cap, not UNSAT')
        for t,mask,eid in adj[v]:
            if mask&used:continue
            path.append(eid)
            if t==start:return list(path)
            if t not in seen:
                seen.add(t);answer=visit(t,used|mask);seen.remove(t)
                if answer is not None:return answer
            path.pop()
        return None
    try:return visit(start,0),nodes,True
    except TimeoutError:return None,nodes,False


def adjacency(edges):
    words=sorted({w for e in edges for w in e[2:]});number={w:i for i,w in enumerate(words)}
    adj=defaultdict(list)
    for i,(s,t,a,d) in enumerate(edges):
        assert a!=d
        adj[s].append((t,(1<<number[a])|(1<<number[d]),i))
    return adj


def all_closed_walks(edges):
    """Enumerate word-distinct closed walks, allowing repeated intermediate vertices.

    The smallest vertex is the start; revisits of start are allowed to continue,
    so concatenated compatible cycles cannot be missed. Canonicalize arc rotations.
    """
    adj=adjacency(edges);cycles=set();nodes=0
    for start in sorted(adj):
        path=[]
        def visit(v,used):
            nonlocal nodes
            nodes+=1
            for t,mask,eid in adj[v]:
                if t<start or used&mask:continue
                path.append(eid)
                if t==start:
                    cyc=tuple(path)
                    cycles.add(min(cyc[i:]+cyc[:i] for i in range(len(cyc))))
                visit(t,used|mask)
                path.pop()
        visit(start,0)
    return sorted(cycles),nodes


def main(kind,W):
    started=time.monotonic();path=OUT/f'{kind}{W}-distinct-kernels.txt'
    edges=graph(path.read_text().splitlines(),kind)
    reduced=cyclic_edges(core(edges));rounds=[];round_no=0
    while True:
        round_no+=1;adj=adjacency(reduced);removed=[];queries=[]
        for v in sorted(adj):
            if len(adj[v])!=1:continue
            cyc,nodes,complete=one_cycle(v,adj,limit=1000000)
            queries.append(dict(vertex=v,nodes=nodes,complete=complete,
                                cycle=cyc,verdict='SAT' if cyc is not None else 'UNSAT' if complete else 'incomplete'))
            if complete and cyc is None:removed.append(v)
        rounds.append(dict(before_vertices=len(adj),before_edges=len(reduced),queries=queries,removed=removed))
        print(kind,round_no,len(adj),len(reduced),'removed',len(removed),'nodes',sum(q['nodes'] for q in queries),flush=True)
        (OUT/f'{kind}{W}-prune-progress.json').write_text(json.dumps(dict(rounds=rounds,status='running'),indent=2)+'\n')
        if not removed:break
        gone=set(removed)
        reduced=cyclic_edges(core([e for e in reduced if e[0] not in gone and e[1] not in gone]))
    (OUT/f'{kind}{W}-reduced-edges.json').write_text(json.dumps(reduced,indent=2)+'\n')
    print('enumerating final word-distinct closed walks',len(reduced),'edges',flush=True)
    cycles,nodes=all_closed_walks(reduced);hist=Counter(map(len,cycles))
    words=dictionary(5)[:W];models=[]
    for cyc in cycles:
        rows=[reduced[i][2] for i in cyc]
        rank=validate(rows,words,kind)
        models.append(dict(period=len(rows),rows=rows,rank=rank,
                           simple=len({reduced[i][0] for i in cyc})==len(cyc)))
    result=dict(kind=kind,W=W,source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                completed_utc=datetime.now(timezone.utc).isoformat(),rounds=rounds,
                final_vertices=len(adjacency(reduced)),final_edges=len(reduced),
                cycle_histogram=dict(sorted(hist.items())),enumeration_nodes=nodes,models=models,
                maximum_period=max(hist,default=0),seconds=time.monotonic()-started,
                short_periods_note='Eight distinct local slots applies to p>=4; p<4 cannot improve either attained optimum.')
    (OUT/f'{kind}{W}-cycles.json').write_text(json.dumps(result,indent=2)+'\n')
    print({k:v for k,v in result.items() if k not in ['models','rounds']},flush=True)


if __name__=='__main__':
    import sys
    main(sys.argv[1],int(sys.argv[2]))

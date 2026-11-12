"""Independent SAT certificate of every word-cycle pruning deletion.

An edge Boolean selects the whole pair of contributed words. Each active
vertex has exactly one selected incoming and outgoing edge; all word labels
occur at most once. Thus selected edges are disjoint simple directed cycles.
Forcing vertex v is satisfiable iff a word-distinct simple cycle through v
exists. Other cycles can always be discarded, so connectivity is unnecessary.
"""
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import time
from pysat.card import CardEnc, EncType
from pysat.formula import CNF, IDPool
from pysat.solvers import Solver
import pysat
import networkx as nx

from word_kernel91 import graph, core, components

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/stair_kernels'


def main():
    started=time.monotonic();kind='left';W=500
    path=OUT/f'{kind}{W}-distinct-kernels.txt'
    edges=graph(path.read_text().splitlines(),kind)
    # Independent directed-core computation using NetworkX degree views.
    g=nx.DiGraph()
    for s,t,*_ in edges:g.add_edge(s,t)
    while True:
        gone=[v for v in g if g.in_degree(v)==0 or g.out_degree(v)==0]
        if not gone:break
        g.remove_nodes_from(gone)
    expected=core(edges)
    assert set(g.edges)=={e[:2] for e in expected}
    assert {frozenset(s) for s in nx.strongly_connected_components(g)}=={frozenset(s) for s in components(expected)}
    pool=IDPool();cnf=CNF();incoming=defaultdict(list);outgoing=defaultdict(list);words=defaultdict(list)
    for i,(s,t,a,d) in enumerate(expected):
        e=pool.id(('edge',i));outgoing[s].append(e);incoming[t].append(e)
        words[a].append(e);words[d].append(e)
    vertices=sorted(set(incoming)|set(outgoing))
    for v in vertices:
        y=pool.id(('vertex',v))
        for group in [incoming[v],outgoing[v]]:
            cnf.append([-y]+group)
            cnf.extend([[-e,y] for e in group])
            cnf.extend(CardEnc.atmost(group,1,vpool=pool,encoding=EncType.seqcounter).clauses)
    for group in words.values():
        cnf.extend(CardEnc.atmost(group,1,vpool=pool,encoding=EncType.seqcounter).clauses)
    inp=OUT/'left500-prune-proof.cnf';cnf.to_file(str(inp))
    record=json.loads((OUT/'left500-cycles.json').read_text());checks=[]
    with Solver(name='cadical195',bootstrap_with=cnf) as solver:
        for r,round_ in enumerate(record['rounds']):
            count=0
            for v in round_['removed']:
                assert solver.solve(assumptions=[pool.id(('vertex',v))]) is False,v
                count+=1
            checks.append(dict(round=r+1,unsat_vertices=count))
            print('SAT independently verified round',r+1,count,flush=True)
        stats=solver.accum_stats()
    result=dict(complete=True,method='Independent edge-SAT cycle cover with distinct word resources',
                core_vertices=g.number_of_nodes(),core_edges=g.number_of_edges(),
                checked_deletions=sum(c['unsat_vertices'] for c in checks),checks=checks,
                solver='cadical195',pysat_version=pysat.__version__,networkx_version=nx.__version__,
                variables=cnf.nv,clauses=len(cnf.clauses),solver_stats=stats,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                kernels_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                cnf_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),seconds=time.monotonic()-started)
    (OUT/'left500-sat-verified.json').write_text(json.dumps(result,indent=2)+'\n');print(result)


if __name__=='__main__':main()

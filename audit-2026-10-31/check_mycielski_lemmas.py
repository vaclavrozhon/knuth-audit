"""Small counterexamples and exhaustive finite checks supporting general proofs."""
from fractions import Fraction
from itertools import combinations,product
from graph_native import OUT,save,sha
from run_mycielski_counts import mycielski

def coloring(n,edges,d):
    neighbors=[set() for _ in range(n)]
    for u,v in edges:neighbors[u].add(v);neighbors[v].add(u)
    order=sorted(range(n),key=lambda u:(-len(neighbors[u]),u));a=[-1]*n
    def go(t,used):
        if t==n:return a[:]
        u=order[t];bad={a[v] for v in neighbors[u] if a[v]>=0}
        for c in range(min(d,used+1)):
            if c not in bad:
                a[u]=c;r=go(t+1,max(used,c+1))
                if r is not None:return r
        a[u]=-1
        return None
    return go(0,0)
def chromatic(n,e):return next(d for d in range(1,n+1) if coloring(n,e,d) is not None)
def triangles(n,e):
    es=set(e);return [t for t in combinations(range(n),3) if all(tuple(sorted(pair)) in es for pair in combinations(t,2))]
def critical(n,e):
    c=chromatic(n,e);return all(chromatic(n,e[:i]+e[i+1:])<c for i in range(len(e)))

def main():
    # Every small graph checks both triangle-preservation and chi(G)+1.
    cases=[]
    for n in range(1,5):
        poss=list(combinations(range(n),2))
        for mask in range(1<<len(poss)):
            e=[x for i,x in enumerate(poss) if mask>>i&1];nn,ee=mycielski(n,e);c=chromatic(n,e)
            assert chromatic(nn,ee)==c+1
            assert bool(triangles(n,e))==bool(triangles(nn,ee))
            ec=critical(n,e);noisolates=all(any(u in edge for edge in e) for u in range(n))
            if ec and noisolates:assert critical(nn,ee)
            cases.append(dict(n=n,edge_mask=mask,chromatic=c,edge_critical=ec,no_isolated_vertices=noisolates))
    n,e=3,[(0,1)];nn,ee=mycielski(n,e);deleted=(5,6);after=[edge for edge in ee if edge!=deleted]
    assert critical(n,e) and chromatic(nn,ee)==chromatic(nn,after)==3
    oddcycle=[0,1,3,6,4]
    assert all(tuple(sorted((u,v))) in after for u,v in zip(oddcycle,oddcycle[1:]+oddcycle[:1]))
    labels=list(product(range(2),repeat=nn));assert not any(all(a[u]!=a[v] for u,v in after) for a in labels)
    witness=coloring(nn,after,3);assert all(witness[u]!=witness[v] for u,v in after)
    critical_counter=dict(n=n,edges=e,mycielski_n=nn,mycielski_edges=ee,removed_edge=deleted,chromatic_before=3,chromatic_after=3,
        retained_5_cycle=oddcycle,proper_3_coloring=witness,all_128_binary_labelings_rejected=True,
        scope='Counterexample to general edge-criticality statement under edge-deletion-only definition; not to the requested Mc sequence. Conventional stronger definition may exclude isolates.')
    n,e=3,[(0,1),(0,2),(1,2)];nn,ee=mycielski(n,e);t=(0,1,5)
    assert t in triangles(nn,ee) and any(u>=n for u in t)
    triangle_counter=dict(original_edges=e,mycielski_edges=ee,triangle=t,projection=[u if u<n else u-n for u in t],
        scope='Literal containment in G is too strong for arbitrary G. Projection to a G triangle is true; triangle-free induction remains valid.')
    formulas=[];n,e=2,[(0,1)]
    for c in range(2,9):
        assert n==Fraction(3,4)*2**c-1
        assert len(e)==Fraction(7,18)*3**c-Fraction(3,4)*2**c+Fraction(1,2)
        assert not triangles(n,e) if n<=23 else True
        formulas.append(dict(c=c,vertices=n,edges=len(e)));n,e=mycielski(n,e)
    save(OUT/'mycielski-lemmas-checked.json',dict(script_sha256=sha(__file__),small_graphs=len(cases),cases=cases,
        criticality_counterexample=critical_counter,triangle_wording_counterexample=triangle_counter,formulas=formulas,
        general_proofs='GRAPHS115_120_NOTES.md; finite checks are supporting evidence, not substitutes for the all-c proof.'))
    print('116:',len(cases),'small graphs; two scoped counterexamples; all-c proof written separately.')

if __name__=='__main__':main()

"""X262(b): corrected coordinates, independent MacMahon counts and ZDD checks."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from pathlib import Path
import json,subprocess

ROOT=Path(__file__).parent


def region(m,n,printed=False):
    up={(x,y,0) for x in range(n+m) for y in range(2*m)
        if m<=x+y and (printed or x+y<n+2*m)}
    down={(x,y,1) for x in range(n+m) for y in range(2*m)
          if m-1<=x+y<n+2*m-1}
    edges=[frozenset([a,(a[0]-dx,a[1]-dy,1)]) for a in sorted(up)
           for dx,dy in [(0,0),(0,1),(1,0)] if (a[0]-dx,a[1]-dy,1) in down]
    return up,down,edges


def macmahon(a,b,c):
    value=Fraction(1)
    for i,j,k in product(range(1,a+1),range(1,b+1),range(1,c+1)):
        value*=Fraction(i+j+k-1,i+j+k-2)
    assert value.denominator==1
    return int(value)


def explicit(m,n):
    up,down,edges=region(m,n);items=sorted(up|down);indices={p:i for i,p in enumerate(items)}
    edges.sort(key=lambda e:(min(indices[p] for p in e),-max(indices[p] for p in e)))
    def visit(remaining,selected):
        if not remaining:yield frozenset(selected);return
        cell=min(remaining)
        for i,edge in enumerate(edges):
            if cell in edge and edge<=remaining:
                yield from visit(remaining-edge,selected+[i])
    family=frozenset(visit(up|down,[]));nodes={}
    @lru_cache(None)
    def zdd(family):
        if not family:return 0
        if family==frozenset([frozenset()]):return 1
        var=min(v for s in family for v in s)
        lo=zdd(frozenset(s for s in family if var not in s))
        hi=zdd(frozenset(s-{var} for s in family if var in s))
        if not hi:return lo
        key=(var,lo,hi)
        if key not in nodes:nodes[key]=len(nodes)+2
        return nodes[key]
    root=zdd(family)
    # A row-cut count forces the y-decreasing edge multiplicities.
    expected=[min(y,2*m-y) for y in range(1,2*m)]
    for solution in family:
        counts=Counter()
        for j in solution:
            a=next(p for p in edges[j] if p[2]==0);b=next(p for p in edges[j] if p[2]==1)
            if a[1]-b[1]==1:counts[a[1]]+=1
        assert [counts[y] for y in range(1,2*m)]==expected
    return len(family),len(nodes)+2 if root>1 else 1


def run(m,n,prime_first=0):
    return json.loads(subprocess.check_output(['/tmp/knuth-hexagon-zdd',str(m),str(n),str(prime_first)],text=True))


def main():
    small=[]
    for m,n in list(product(range(1,3),range(6)))+[(3,0),(3,1),(3,2)]:
        count,nodes=explicit(m,n);got=run(m,n)
        assert count==macmahon(m,m,n)==int(got['solutions'])
        assert nodes==got['zdd_nodes'],(m,n,nodes,got)
        small.append(dict(m=m,n=n,solutions=count,zdd_nodes=nodes))
    broken=[]
    for n in range(41):
        up,down,edges=region(8,n,True);fixed,_,_=region(8,n)
        touched=set().union(*edges);extra=up-fixed
        assert len(extra)==28 and extra.isdisjoint(touched)
        assert len(up)==16*n+92 and len(down)==len(fixed)==16*n+64
        broken.append(dict(n=n,unprimed=len(up),primed=len(down),isolated_extra_items=len(extra)))
    results=dict(validation=small,printed_coordinate_counterexamples=broken,corrected=[])
    for n in [1,5,6,7,8,9,10,16,20]:
        got=run(8,n);assert int(got['solutions'])==macmahon(8,8,n)
        if n>=7:assert got['zdd_nodes']==257400*n-1210061
        if n==8:assert int(got['solutions'])==5055160684040254910720
        if n==16:assert int(got['solutions'])==2065715788914012182693991725390625
        results['corrected'].append(got)
        (ROOT/'results/hexagon_zdd.json').write_text(json.dumps(results,indent=2)+'\n')
        print(json.dumps(got),flush=True)


if __name__=='__main__':main()

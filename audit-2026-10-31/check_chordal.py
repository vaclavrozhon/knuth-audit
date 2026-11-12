"""Independent finite checks of SAT 346--347, with exact rational arithmetic."""
from itertools import combinations, product, permutations
from fractions import Fraction as Q
from functools import lru_cache
from math import prod
from pathlib import Path
import json
import sympy as s
from check_extreme_distribution import graphs
from check_cographs import scaled_mobius


def chordal_by_cycles(adj):
    # An induced cycle has degree exactly two at each vertex, and is connected.
    n=len(adj)
    for mask in range(1<<n):
        if mask.bit_count()<4:continue
        if any((adj[i]&mask).bit_count()!=2 for i in range(n) if mask>>i&1):continue
        seen=mask&-mask;front=seen
        while front:
            bit=front&-front;front^=bit
            new=adj[bit.bit_length()-1]&mask&~seen
            front|=new;seen|=new
        if seen==mask:return False
    return True


def peo(adj):
    left=(1<<len(adj))-1;order=[]
    while left:
        for i in range(len(adj)):
            if not left>>i&1:continue
            neighbors=adj[i]&left
            if all((neighbors&~(1<<j))&~adj[j]==0 for j in range(len(adj)) if neighbors>>j&1):
                order.append(i);left^=1<<i;break
        else:return None
    return order


def forest_from_peo(adj,order):
    rank={v:k for k,v in enumerate(order)};parent=[None]*len(adj)
    for v in order:
        later=[u for u in order if adj[v]>>u&1 and rank[u]>rank[v]]
        if later:parent[v]=min(later,key=rank.get)
    ancestors=[0]*len(adj)
    for v in reversed(order):
        if parent[v] is not None:ancestors[v]=ancestors[parent[v]]|1<<parent[v]
    # Two defining properties, independently checked on all vertex triples.
    for a,b in combinations(range(len(adj)),2):
        if adj[a]>>b&1:assert (ancestors[a]>>b&1) or (ancestors[b]>>a&1)
    for a,b,c in permutations(range(len(adj)),3):
        if ancestors[b]>>a&1 and ancestors[c]>>b&1 and adj[a]>>c&1:
            assert adj[a]>>b&1
    return ancestors


def theta_test(adj,p,order):
    theta={}
    for v in order:
        denominator=prod(1-theta[u] for u in theta if adj[v]>>u&1)
        value=p[v]/denominator
        if value>=1:return False,None
        assert value>=0
        theta[v]=value
    return True,prod(1-x for x in theta.values())


def recursive_test(adj,p):
    """Direct implementation of 346, with cached induced subgraphs."""
    @lru_cache(None)
    def visit(mask):
        if mask==0:return Q(1)
        bit=mask&-mask;i=bit.bit_length()-1
        rest=mask^bit;den=visit(rest)
        if den is None:return None
        num=visit(rest&~adj[i])
        if num is None:return None
        factor=1-p[i]*num/den
        if factor<=0:return None
        return den*factor
    return visit((1<<len(adj))-1)


def symbolic_examples():
    a,b,c,d,e,f=s.symbols('a b c d e f');p=[a,b,c,d,e,f]
    adj=[0]*6
    for i,j in [(0,1),(0,2),(1,3),(2,3),(2,4),(3,5),(4,5)]:
        adj[i]|=1<<j;adj[j]|=1<<i
    def M(mask):
        total=0
        for I in range(64):
            if I&~mask or any(I>>i&1 and adj[i]&I for i in range(6)):continue
            total+=(-1)**I.bit_count()*prod(p[i] for i in range(6) if I>>i&1)
        return total
    # Transcribe both tables, then compare every auxiliary variable with
    # independently enumerated independent-set polynomials.
    fp=f;epp=e;ep=s.cancel(e/(1-fp))
    dp=s.cancel(d*(1-epp)/((1-ep)*(1-fp)))
    cpp=s.cancel(c/(1-ep));cp=s.cancel(c/((1-dp)*(1-ep)))
    bp=s.cancel(b*(1-cpp)/((1-cp)*(1-dp)));ap=s.cancel(a/((1-bp)*(1-cp)))
    rows=[(0,63,ap),(1,62,bp),(2,60,cp),(2,52,cpp),(3,56,dp),(4,48,ep),(4,16,epp),(5,32,fp)]
    count=0
    for v,mask,value in rows:
        rest=mask^(1<<v)
        assert s.cancel(value-p[v]*M(rest&~adj[v])/M(rest))==0;count+=1
    value=s.Integer(1)
    for x in [ap,bp,cp,dp,ep,fp]:value=s.cancel(value*(1-x))
    assert s.cancel(value-M(63))==0;count+=1
    bp=b;app=a;ap=s.cancel(a/(1-bp))
    dp=s.cancel(d*(1-app)*(1-epp)/((1-ap)*(1-bp)*(1-ep)*(1-fp)))
    cp=s.cancel(c/((1-ap)*(1-dp)*(1-ep)))
    for v,mask,value in [(2,63,cp),(3,59,dp),(0,3,ap),(0,1,app),(1,2,bp)]:
        rest=mask^(1<<v)
        assert s.cancel(value-p[v]*M(rest&~adj[v])/M(rest))==0;count+=1
    value=s.Integer(1)
    for x in [ap,bp,cp,dp,ep,fp]:value=s.cancel(value*(1-x))
    assert s.cancel(value-M(63))==0;count+=1
    return count


def main():
    classified=chordal=forests=vectors=inside=recursive=monotonic=theta_vectors=0
    counts=[]
    for n in range(1,6):
        this=0
        for adj in graphs(n):
            order=peo(adj);is_chordal=chordal_by_cycles(adj)
            assert (order is not None)==is_chordal;classified+=1
            if is_chordal:
                chordal+=1;this+=1;ancestors=forest_from_peo(adj,order);forests+=1
            if n<=4:
                grid=product(range(5),repeat=n)
            elif is_chordal:
                grid=product([0,1,2],repeat=n)
            else:continue
            for nums in grid:
                values=scaled_mobius(adj,nums);truth=all(v>0 for v in values)
                p=[Q(v,4) for v in nums]
                if n<=4:
                    got=recursive_test(adj,p);recursive+=1
                    assert (got is not None)==truth
                    if truth:
                        assert got==Q(values[-1],4**n)
                        for a in range(n):
                            rest=((1<<n)-1)^(1<<a);remote=rest&~adj[a]
                            old=Q(values[remote],4**remote.bit_count())/Q(values[rest],4**rest.bit_count())
                            for j in range(n):
                                if nums[j]==0:continue
                                lower=list(nums);lower[j]-=1;vs=scaled_mobius(adj,lower)
                                new=Q(vs[remote],4**remote.bit_count())/Q(vs[rest],4**rest.bit_count())
                                assert new<=old;monotonic+=1
                if is_chordal:
                    got,value=theta_test(adj,p,order);vectors+=1;inside+=got
                    assert got==truth
                    if got:assert value==Q(values[-1],4**n)
            if is_chordal and n<=4:
                for ts in product([Q(0),Q(1,4),Q(3,4)],repeat=n):
                    p=[ts[v]*prod(1-ts[u] for u in range(n) if adj[v]>>u&1 and ancestors[u]>>v&1) for v in range(n)]
                    ok,value=theta_test(adj,p,order)
                    assert ok and value==prod(1-t for t in ts)
                    assert recursive_test(adj,p)==value;theta_vectors+=1
        counts.append(this)
    symbolic=symbolic_examples()
    # Exact two-vertex example for the reversal in the proof of 346(a).
    assert 1/(1-Q(1,4))==Q(4,3)<Q(2)==1/(1-Q(1,2))
    result=dict(classified_graphs=classified,chordal_graphs=chordal,chordal_counts_by_n=counts,
                tree_orderings=forests,chordal_probability_vectors=vectors,inside_vectors=inside,
                general_recursive_vectors=recursive,monotonic_comparisons=monotonic,
                inverse_theta_vectors=theta_vectors,symbolic_ladder_identities=symbolic,
                F037={'old_p_b':'1/2','old_K':'2','new_p_b':'1/4','new_K':'4/3'})
    Path('results/chordal.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()

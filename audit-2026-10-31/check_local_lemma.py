"""Independent-set enumeration and probability checks for SAT 315-321."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
import random
import sympy as sp


def adjacency(n,edges):
    masks=[0]*n
    for i,j in edges:masks[i]|=1<<j;masks[j]|=1<<i
    return masks


def independent_subsets(adj,allowed=None):
    if allowed is None:allowed=(1<<len(adj))-1
    out=[0]
    for i,neighbors in enumerate(adj):
        if allowed>>i&1:out += [s|1<<i for s in out if not s&neighbors]
    return out


def mobius(adj,p,allowed=None):
    return sum(((-p)**s.bit_count() for s in independent_subsets(adj,allowed)),Q(0))


def coefficients(adj):
    result=[0]*(len(adj)+1)
    for s in independent_subsets(adj):result[s.bit_count()]+=1
    while len(result)>1 and not result[-1]:result.pop()
    return result


def tree(t,h):
    edges=[];frontier=[0];n=1
    for _ in range(h):
        nxt=[]
        for parent in frontier:
            for _ in range(t):
                edges.append((parent,n));nxt.append(n);n+=1
        frontier=nxt
    return adjacency(n,edges)


def poly(coefs,p):return sum((-p)**i*c for i,c in enumerate(coefs))


def main():
    graphs=[]
    for n in range(1,6):
        edges=list(combinations(range(n),2))
        for mask in range(1<<len(edges)):
            graphs.append(adjacency(n,[e for i,e in enumerate(edges) if mask>>i&1]))
    rng=random.Random(317)
    for _ in range(1000):
        n=rng.randrange(6,10)
        graphs.append(adjacency(n,[e for e in combinations(range(n),2) if rng.randrange(2)]))
    low_degree_checks=0
    for adj in graphs:
        d=max(2,max(map(int.bit_count,adj)));p=Q((d-1)**(d-1),d**d);rho=Q(d-1,d)
        mg=mobius(adj,p);assert mg>0
        for v in range(len(adj)):
            if adj[v].bit_count()<d:
                assert mg>rho*mobius(adj,p,((1<<len(adj))-1)^(1<<v))
                low_degree_checks+=1
    p,x=sp.symbols('p x');tree_cases=0;tree_details=[]
    for t,maxh in [(1,6),(2,3),(3,2),(4,2)]:
        fs=[]
        for h in range(maxh+1):
            adj=tree(t,h);counts=coefficients(adj);direct=sp.expand(poly(counts,p))
            recurrence=1-p if h==0 else (1-p)**t-p if h==1 else fs[-1]**t-p*fs[-2]**(t*t)
            assert sp.expand(direct-recurrence)==0
            fs.append(direct);tree_cases+=1;tree_details.append((t,h,len(adj),sum(counts)))
    # Certified outward-rounded rational intervals; fixed denominator prevents
    # the exponential bit growth of the exact rational recurrence.
    D=10**80;lo=hi=851*D//1000;intervals=[]
    def floorq(z):return z.numerator//z.denominator
    def ceilq(z):return -((-z.numerator)//z.denominator)
    for n in range(1,100):
        newlo=floorq(D*(1-Q(149,1000)/Q(lo,D)**2))
        newhi=ceilq(D*(1-Q(149,1000)/Q(hi,D)**2))
        assert newlo<=newhi
        lo,hi=newlo,newhi;intervals.append((n,lo,hi))
        if hi<=0:break
        assert lo>0
    assert n==45 and hi<0
    path_cases=cycle_cases=0
    for n in range(1,17):
        adj=adjacency(n,[(i,i+1) for i in range(n-1)])
        coefs=coefficients(adj)
        lhs=sum((-1)**k*c*(2*x)**(n+1-2*k) for k,c in enumerate(coefs))
        assert sp.expand(lhs-sp.chebyshevu(n+1,x))==0
        path_cases+=1
        if n>=3:
            adj=adjacency(n,[(i,(i+1)%n) for i in range(n)])
            coefs=coefficients(adj)
            lhs=sum((-1)**k*c*(2*x)**(n-2*k) for k,c in enumerate(coefs))
            assert sp.expand(lhs-2*sp.chebyshevt(n,x))==0
            cycle_cases+=1
    # F030: reproduce answer 345's independent OR inflation of the exact
    # boundary measure, without using the displayed six formulas in 321.
    theta=(2-sp.sqrt(2))/2;theta1=sp.simplify(theta*(1-theta));c=sp.symbols('c')
    base={1:theta1,2:theta1,4:theta1,8:theta1,5:theta**2,10:theta**2}
    distribution={s:0 for s in range(16)}
    for initial,weight in base.items():
        for mask in range(16):
            if mask&initial:continue # independent coins only for absent events
            distribution[initial|mask]+=weight*c**mask.bit_count()*(1-c)**(4-initial.bit_count()-mask.bit_count())
    distribution={s:sp.expand(v) for s,v in distribution.items()}
    assert sp.simplify(sum(distribution.values())-1)==0
    finalp=theta+(1-theta)*c
    for i in range(4):
        assert sp.simplify(sum(v for s,v in distribution.items() if s>>i&1)-finalp)==0
    for a,b in [(0,2),(1,3)]:
        assert sp.simplify(sum(v for s,v in distribution.items() if s>>a&1 and s>>b&1)-finalp**2)==0
    correct=[0,theta1*(1-c)**3,2*theta1*(1-c)**2*c,
             theta**2*(1-c)**2+2*theta1*c*(1-c)**2,
             theta**2*(1-c)*c+3*theta1*(1-c)*c**2,
             2*theta**2*c**2+4*theta1*c**3]
    representatives=[0,1,3,5,7,15];multiplicities=[1,4,4,2,4,1]
    for s,v in zip(representatives,correct):assert sp.simplify(distribution[s]-v)==0
    printed=correct.copy();printed[3]=theta**2*(1-c)**2+2*theta1*(1-c)**3
    printed[5]=theta**2*c**2+4*theta1*c**3
    atp03=sp.simplify((Q(3,10)-theta)/(1-theta))
    numeric=lambda z:str(sp.N(sp.sympify(z).subs(c,atp03),18))
    wrongtotal=sp.simplify(sum(m*v for m,v in zip(multiplicities,printed)))
    assert sp.simplify(wrongtotal-1)!=0
    # A simpler exact solution to the actual exercise at p=3/10.
    rational={s:Q(1,5) if s.bit_count()==1 else Q(9,100) if s in (5,10)
              else Q(1,200) if s in (3,6,9,12) else Q(0) for s in range(16)}
    assert sum(rational.values())==1 and rational[0]==0
    for i in range(4):assert sum(v for s,v in rational.items() if s>>i&1)==Q(3,10)
    for a,b in [(0,2),(1,3)]:assert sum(v for s,v in rational.items() if s>>a&1 and s>>b&1)==Q(9,100)
    report={'small_graphs':len(graphs)-1000,'random_graphs':1000,'low_degree_ratio_checks':low_degree_checks,
            'complete_tree_polynomials':tree_cases,'tree_details':tree_details,
            'binary_tree_p_0149_first_nonpositive_height':intervals[-1][0],
            'certified_interval_denominator':str(D),
            'g44_numerators':list(map(str,intervals[43][1:])),
            'g45_numerators':list(map(str,intervals[44][1:])),
            'path_Chebyshev_checks':path_cases,'cycle_Chebyshev_checks':cycle_cases,
            'F030_printed_six_probabilities_at_p03':list(map(numeric,printed)),
            'F030_printed_total_at_p03':numeric(wrongtotal),
            'F030_corrected_six_probabilities_at_p03':list(map(numeric,correct)),
            'F030_exact_rational_alternative':{format(s,'04b'):str(v) for s,v in rational.items()},
            'known_erratum':'Answer 318 decreasing-difference identity, 2024-02-02, applied; not a new finding.',
            'scope':'General proofs in LOCAL_LEMMA_NOTES.md; polynomial and probability checks use exact arithmetic. Height 45 certified by outward-rounded rational intervals.'}
    (Path(__file__).parent/'results/local_lemma.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()

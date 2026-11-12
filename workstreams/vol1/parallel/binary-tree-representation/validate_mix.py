"""Supplementary exhaustive, randomized, boundary and storage-limit MIX runs."""
import sys
sys.dont_write_bytecode=True
from check_mix import *
from itertools import product

def expressions(n):
    if n==1:return [C(0),C(1),V(),V('A')]
    out=[(op,t) for op in ['ln','neg'] for t in expressions(n-1)]
    for k in range(1,n-1):
        out.extend((op,u,v) for op in ['+','-','*','/','^'] for u in expressions(k) for v in expressions(n-1-k))
    return out

def random_tree(rng,n):
    if n==1:return rng.choice([C(-7),C(-1),C(0),C(1),C(2),C(3),V(),V('A')])
    if n==2 or rng.randrange(4)==0:return (rng.choice(['ln','neg']),random_tree(rng,n-1))
    k=rng.randrange(1,n-1)
    return (rng.choice(['+','-','*','/','^']),random_tree(rng,k),random_tree(rng,n-1-k))

def validate():
    rng=random.Random(230232)
    result={'seed':230232,'complete':{},'copies':{},'limits':[],'boundary_own':0,'total_steps':0,'total_time':0}
    small=[t for n in range(1,5) for t in expressions(n)]
    randoms=[random_tree(rng,rng.randrange(5,26)) for _ in range(160)]
    radix_cases=[('/',V(),V()),('^',V(),V()),('^',V(),C(-2)),('*',('ln',V()),('/',C(3),V())),('-',('*',C(3),('ln',('+',V(),C(1)))),('/',V('A'),('^',V(),C(2))))]
    for own in [False,True]:
        name='own' if own else 'book';done=0;copied=0
        for i,(b,t) in enumerate([(64,t) for t in small+randoms]+[(b,t) for b in range(64,101) for t in radix_cases]):
            f=Fixture(t,b,shuffle=i+1,own=own)
            actual,time=f.differentiate()
            assert actual==derivative(t),(name,t,actual,derivative(t))
            result['total_steps']+=f.m.steps;result['total_time']+=time;done+=1
        result['complete'][name]={'exhaustive_size_at_most':4,'exhaustive_count':len(small),'random_count':len(randoms),'all_radix_cases':37*len(radix_cases),'runs':done}
        for i,t in enumerate(randoms+small[::7]):
            b=64+i%37;f=Fixture(t,b,shuffle=10000+i,own=own)
            # Root's external sibling link is immaterial to COPY; corrupt it deliberately.
            w=f.m.mem[f.root];f.m.mem[f.root]=f.word(f.left(f.root),3999,w.digits[2],bool(i%2));f.original[f.root]=f.m.mem[f.root]
            time=f.call('COPY',[(1,f.root),(2,11),(3,22),(4,33),(5,44),(6,55)])
            p=f.m.reg[1].value(b);assert f.decode(p)==t;f.partition(p);f.assert_original()
            for r,v in [(2,11),(3,22),(4,33),(5,44),(6,55)]:assert f.m.reg[r].value(b)==v
            if not own:
                assert time==36*count(t)+17
                n=count(t);a=sum(1 for x in walk(t) if x[0] not in ('c','v'))
                groups=[(64,67,1),(69,69,a),(70,79,a+1),(80,81,n-1),(82,88,n-1-a),(89,94,n),(95,95,n-a),(96,98,n+1),(99,100,n-a),(101,103,1)]
                for lo,hi,c in groups:
                    for line in range(lo,hi+1):assert f.visits[f.a.line_addresses[f'{line:03}']]==c,(line,t,c)
            else:
                a=sum(1 for x in walk(t) if x[0] not in ('c','v'))
                assert time==59*count(t)-2*a+15
            copied+=1;result['total_steps']+=f.m.steps;result['total_time']+=time
        result['copies'][name]=copied
        for b in range(64,101):
            for leaf in [C(-(b**5-1)),C(b**5-1),C(0)]:
                f=Fixture(leaf,b,own=own);f.differentiate()
            # A failed allocation enters the designated OVERFLOW trap; no claim
            # of transactional restoration on failure is made by the book.
            start=2000 if own else 1000
            f=Fixture(V(),b,pool_end=start-2,own=own)
            try:f.differentiate();raise RuntimeError('exhaustion undetected')
            except AssertionError as e:assert e.args[0][0]=='OVERFLOW'
            result['limits'].append({'b':b,'program':name,'empty_pool':'OVERFLOW'})
            if own:
                for t in [('*',C(-(b**5-1)),V()),('*',V(),C(-(b**5-1))),('^',V(),C(-(b**5-2)))]:
                    f=Fixture(t,b,own=True);actual,time=f.differentiate();assert actual==derivative(t);result['boundary_own']+=1
                f=Fixture(('^',V(),C(-(b**5-1))),b,own=True)
                try:f.differentiate();raise RuntimeError('output underflow undetected')
                except AssertionError as e:assert e.args[0][0]=='OVERFLOW'
                result['limits'].append({'b':b,'program':name,'unrepresentable_output_exponent':'OVERFLOW'})
    return result

def walk(t):
    yield t
    if t[0] not in ('c','v'):
        for c in t[1:]:yield from walk(c)

if __name__=='__main__':
    result=validate();(HERE/'results'/'mix-validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

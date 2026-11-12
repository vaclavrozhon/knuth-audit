"""Exact checks for TAOCP 3.5-26,29,30; general proofs are in the note."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter, defaultdict, deque
from itertools import product
from math import comb
import argparse
import json
import sympy as s

P = Path(__file__).resolve().parent
OUT = P / 'results/white-parity.json'
parser = argparse.ArgumentParser()
parser.add_argument('--resume', action='store_true')
args = parser.parse_args()
r = json.loads(OUT.read_text()) if args.resume and OUT.exists() else {}

def save():
    OUT.write_text(json.dumps(r, indent=2) + '\n')

if 'franklin' not in r:
    x, y = s.symbols('x y', real=True)
    half = s.Rational(1, 2)
    regions = [(0, half, 0, x), (0, half, x+half, 1), (half, 1, x-half, x)]
    def integ(f):
        return s.simplify(sum(s.integrate(f, (y, a, b), (x, c, d))
                              for c, d, a, b in regions))
    # Rows and columns of density 2*1_G have mass one.
    rows = [2*(x + 1-x-half), 2*(x-(x-half))]
    cols = [2*((y+half)-y), 2*((1-y)+(y-half))]
    assert all(s.simplify(v)==1 for v in rows+cols)
    moments = {str(f): str(integ(2*f)) for f in [s.S.One, x, y, x*y, x*x, y*y]}
    assert list(moments.values()) == ['1','1/2','1/2','1/4','1/3','1/3']
    within_descent = 2*(s.integrate(x, (x, 0, half)) + s.integrate(half, (x, half, 1)))
    assert within_descent == s.Rational(3, 4)
    total_descent = (within_descent+half)/2
    assert total_descent == s.Rational(5, 8)
    r['franklin'] = dict(moments=moments, within_pair_descent=str(within_descent), all_descent=str(total_descent))
    save(); print('PASS Franklin exact regions', flush=True)

if 'waterman_kernels' not in r:
    cases = 0
    rows = []
    for lag in range(1, 5):
        for H in range(1, 9):
            total = 0
            for y in product((-1,1), repeat=H+lag):
                z = sum(y[j]*y[j+lag] for j in range(H))
                total += z*z
                cases += 1
            mean_square = F(total, 2**(H+lag)*H*H)
            assert mean_square == F(1,H)
            rows.append(dict(lag=lag, window=H, second_moment=str(mean_square)))
    r['waterman_kernels'] = dict(binary_histories=cases, rows=rows)
    save(); print('PASS Waterman local mean-square kernels', cases, flush=True)

if 'parity_extremal' not in r:
    identities=[]
    for k in range(1,65):
        pos=sum((a-b)*comb(k,a)*comb(k,b) for a in range(k+1) for b in range(a))
        assert pos == k*comb(2*k-1,k)
        if k<=8:
            mx=sum(max(a,b)*comb(k,a)*comb(k,b) for a in range(k+1) for b in range(k+1))
            mn=sum(min(a,b)*comb(k,a)*comb(k,b) for a in range(k+1) for b in range(k+1))
            assert mx==k*2**(2*k-1)+pos and mn==k*2**(2*k-1)-pos
        identities.append(dict(k=k, positive_sum=pos))
    graphs=[]
    for k in range(1,9):
        width=2*k-1; mask=(1<<width)-1
        words={v:tuple((v>>j)&1 for j in range(width-1,-1,-1)) for v in range(mask+1)}
        adj=defaultdict(list); rev=defaultdict(list); indeg=Counter(); outdeg=Counter()
        for parity in [0,1]:  # 0 = book E, 1 = book O; first arc E is at position 1.
            for v,w in words.items():
                for b in [0,1]:
                    D=sum(w[::2])-sum(w[1::2])-b
                    sign=(D>0)-(D<0); multiplicity=1+(1 if parity==0 else -1)*sign
                    src=(parity,v); dst=(1-parity,((v<<1)|b)&mask)
                    for _ in range(multiplicity):
                        adj[src].append((dst,b)); rev[dst].append(src)
                        outdeg[src]+=1; indeg[dst]+=1
        nodes=set(outdeg)|set(indeg)
        assert all(indeg[u]==outdeg[u] for u in nodes)
        assert sum(outdeg.values())==2**(2*k+1)
        target=(0,int('10'*(k-1)+'1',2))
        for root,reverse in [(target,False),(target,True)]:
            seen={root};todo=[root]
            while todo:
                u=todo.pop()
                neighbors=rev[u] if reverse else [v for v,b in adj[u]]
                for v in neighbors:
                    if v not in seen:seen.add(v);todo.append(v)
            assert seen==nodes
        # General proof's explicit route: O appends 1; E repeatedly appends 0,1.
        for u in nodes:
            v=u; route=([1] if v[0] else [])+[0,1]*k
            for b in route:
                w=(1-v[0],((v[1]<<1)|b)&mask)
                assert any(z==w and bit==b for z,bit in adj[v])
                v=w
            assert v==target
        # Hierholzer construction, followed by independent cyclic word counting.
        todo=[((0,0),None)]; trail=[]; remaining={u:list(es) for u,es in adj.items()}
        while todo:
            u,b=todo[-1]
            if remaining.get(u):
                v,c=remaining[u].pop();todo.append((v,c))
            else:
                _,bit=todo.pop()
                if bit is not None:trail.append(bit)
        trail.reverse();period=(list(words[0])+trail)[:len(trail)]
        N=len(period);counts=Counter(tuple(period[(i+j)%N] for j in range(2*k)) for i in range(N))
        assert len(counts)==2**(2*k) and set(counts.values())=={2}
        # Stored index 0 is book X_1, so X_(2n) are odd stored indices.
        even_zero=sum(period[i]==0 for i in range(1,N,2))
        expected=F(1,2)+F(comb(2*k-1,k),2**(2*k))
        assert F(even_zero,N//2)==expected
        graphs.append(dict(k=k, active_vertices=len(nodes), arcs=N, even_zero_count=even_zero, even_zero_frequency=str(expected), period=''.join(map(str,period)) if k<=3 else None))
        print('PASS parity graph',k,len(nodes),N,flush=True)
    printed='00001000110010101001101110111110'
    N=len(printed);pc=Counter(''.join(printed[(i+j)%N] for j in range(4)) for i in range(N))
    assert len(pc)==16 and set(pc.values())=={2}
    assert F(sum(printed[i]=='0' for i in range(1,N,2)),N//2)==F(11,16)
    r['parity_extremal']=dict(identities=identities,graphs=graphs,printed_k2_period=printed,printed_even_zero_frequency='11/16')
    save();print('PASS parity identities and printed example',flush=True)

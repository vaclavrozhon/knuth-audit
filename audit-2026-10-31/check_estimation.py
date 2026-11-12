"""Exact independent checks of TAOCP 7.2.2, exercises 49--57.

Enumerate the complete probability space of leaves, then compare with the
recursive moments. Fractions prevent numerical agreement from hiding errors.
"""
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from math import factorial, prod, sqrt
import json, random
import mpmath as mp

OUT = Path(__file__).resolve().parent / 'results/estimation'


def moments(tree, costs, probabilities, v=0):
    kids = tree[v]
    c = costs[v]
    if not kids:
        return c, c, c, c*c
    stats = [moments(tree, costs, probabilities, w) for w in kids]
    ps = probabilities[v]
    # Direct conditioning on the first selected child.
    return (c + min(s[0]/p for s,p in zip(stats,ps)),
            c + max(s[1]/p for s,p in zip(stats,ps)),
            c + sum(s[2] for s in stats),
            c*c + sum(s[3]/p + 2*c*s[2] for s,p in zip(stats,ps)))


def literal_second(tree, costs, v=0, corrected=False):
    if not tree[v]:
        return costs[v], costs[v]**2
    kids = [literal_second(tree,costs,w,corrected) for w in tree[v]]
    cost = sum(c for c,q in kids)
    chat = sum(q for c,q in kids)
    return costs[v]+cost, costs[v]**2+len(kids)*chat+2*(costs[v] if corrected else 1)*cost


def full_distribution(tree, costs, probabilities):
    results=[]
    def visit(v,path,p,s):
        s += costs[v]/p
        if not tree[v]:
            results.append((p,s,path+(v,)))
        else:
            for w,q in zip(tree[v],probabilities[v]): visit(w,path+(v,),p*q,s)
    visit(0,(),F(1),F(0))
    assert sum(p for p,s,path in results)==1
    return results


def tree_total(tree,costs,v):
    return costs[v]+sum(tree_total(tree,costs,w) for w in tree[v])


def check_tree(tree,costs):
    total=sum(costs)
    uniform={v:[F(1,len(kids))]*len(kids) for v,kids in enumerate(tree) if kids}
    biased={v:[F(w+1,sum(k+1 for k in kids)) for w in kids] for v,kids in enumerate(tree) if kids}
    ideal={v:[F(tree_total(tree,costs,w),sum(tree_total(tree,costs,k) for k in kids)) for w in kids]
           for v,kids in enumerate(tree) if kids}
    for name,probabilities in [('uniform',uniform),('biased',biased),('ideal',ideal)]:
        leaves=full_distribution(tree,costs,probabilities)
        expected=sum(p*s for p,s,path in leaves)
        second=sum(p*s*s for p,s,path in leaves)
        assert expected==total
        assert moments(tree,costs,probabilities)==(min(s for p,s,path in leaves),max(s for p,s,path in leaves),expected,second)
        if name=='ideal': assert all(s==total for p,s,path in leaves)
        # Conditional martingale increment: C(v)=c(v)+sum C(children).
        for v,kids in enumerate(tree):
            if kids:
                assert sum(p*(costs[v]+F(tree_total(tree,costs,w),p)) for w,p in zip(kids,probabilities[v]))==tree_total(tree,costs,v)
        if name=='uniform':
            assert literal_second(tree,costs,corrected=True)==(expected,second)
            # Exercise 57, exact product instead of logarithmic floating point.
            assert prod(1/p for p,s,path in leaves)>=len(leaves)**len(leaves)
            profile=Counter()
            reached={}
            def go(v,d,p):
                profile[d]+=1;reached[v]=(d,p)
                for w,q in zip(tree[v],probabilities.get(v,[])): go(w,d+1,p*q)
            go(0,0,F(1))
            est=Counter()
            for p,s,path in leaves:
                for v in path:
                    d,pv=reached[v];est[d]+=p/pv
            assert est==profile


def figure69():
    mp.mp.dps=100
    expected=[([2,5,1,4,7,3,6],10,2129),([6,1,7,5,8,2,4],20,2689),
              ([5,8,2,7,3,1],13,1489),([5,8,6,1,3,7],13,2609)]
    rows=[]
    for (name,real),(board_expected,used,estimate) in zip([('pi',mp.pi),('e',mp.e),('phi',mp.phi),('gamma',mp.euler)],expected):
        y=real-mp.floor(real);bits=''
        for _ in range(100):
            y*=2;b=int(y);bits+=str(b);y-=b
        board=[];degrees=[];blocks=[];position=0
        for r in range(8):
            choices=[c for c in range(8) if all(c!=old and abs(c-old)!=r-j for j,old in enumerate(board))]
            d=len(choices);degrees.append(d)
            if not d:break
            t=(d-1).bit_length()
            while True:
                bit=bits[position:position+t];position+=t
                k=int(bit,2) if bit else 0
                blocks.append({'bits':bit,'accepted':k<d})
                if k<d:break
            board.append(choices[k])
        value=1
        for d in reversed(degrees):value=1+d*value
        assert [c+1 for c in board]==board_expected and position==used and value==estimate
        rows.append({'constant':name,'board':board_expected,'degrees':degrees,'bits':bits[:position],'choices':blocks,'estimate':value})
    return rows


def bit_cost(q):
    # Lower bound: at most floor(2**k/q) length-k prefixes per outcome.
    # Recycling rejection attains all these bounds simultaneously.
    if q==1:return F(0)
    r=1;seen={};terms=[];k=0
    while r not in seen:
        seen[r]=k;terms.append(F(r,2**k));r=2*r%q;k+=1
    if r==0:return sum(terms)
    j=seen[r]
    return sum(terms[:j])+sum(terms[j:])/(1-F(1,2**(k-j)))


def check_coin_generator(q,depth=16):
    # Exhaustive reachable states of recycling algorithm (range,value).
    states=Counter({(1,0):1});emitted=Counter();survival=[]
    for k in range(depth):
        assert sum(states.values())==2**k%q
        survival.append(F(sum(states.values()),2**k))
        nxt=Counter()
        for (v,c),ways in states.items():
            for b in (0,1):
                v2,c2=2*v,2*c+b
                if v2>=q:
                    if c2<q:
                        emitted[c2]+=F(ways,2**(k+1));continue
                    v2-=q;c2-=q
                nxt[v2,c2]+=ways
        states=nxt
    assert len(set(emitted.values()))==1
    assert all(v==F((2**depth)//q,2**depth) for v in emitted.values())
    assert sum(survival)<=bit_cost(q)


def binomial_trees():
    # Bernoulli convolution vs cycle-count/Stirling recurrence.
    probabilities=[F(1)]
    stirling=[1]
    tails={}
    for n in range(1,101):
        new=[F(0)]*(n+1);ss=[0]*(n+1)
        for k in range(n+1):
            if k<n:new[k]+=probabilities[k]*F(n-1,n);ss[k]+=(n-1)*stirling[k]
            if k:new[k]+=probabilities[k-1]*F(1,n);ss[k]+=stirling[k-1]
        probabilities,stirling=new,ss
        assert probabilities==[F(s,factorial(n)) for s in stirling]
        assert sum(k*p for k,p in enumerate(probabilities))==sum(F(1,k) for k in range(1,n+1))
        if n<=12:
            found=Counter()
            def visit(top,path,p):
                if top==1:
                    found[path]=p;return
                for x in range(1,top):visit(x,path+(x,),p*F(1,top-1))
            visit(n+1,(),F(1))
            dist=Counter()
            for path,p in found.items():
                coin=F(1)
                for k in range(1,n+1):coin*=F(1,k) if k in path else F(k-1,k)
                assert coin==p;dist[len(path)]+=p
            assert [dist[k] for k in range(n+1)]==probabilities
        if n==100:tails['level_at_least_20']=str(sum(probabilities[19:]));tails['decimal']=float(sum(probabilities[19:]));tails['level_at_least_21_decimal']=float(sum(probabilities[20:]));tails['printed_level20_decimal']=2.7e-9
    return tails


def main():
    rng=random.Random(20261101053)
    for _ in range(1000):
        n=rng.randrange(1,75);tree=[[] for i in range(n)]
        for i in range(1,n):tree[rng.randrange(i)].append(i)
        costs=[F(rng.randrange(1,10),rng.randrange(1,5)) for i in range(n)]
        check_tree(tree,costs)
    tree=[[1],[]];costs=[F(2),F(2)];bad=literal_second(tree,costs)
    assert bad==(4,12) and bad[1]-bad[0]**2==-4
    for q in range(2,41):check_coin_generator(q)
    assert bit_cost(3)==F(8,3) and bit_cost(5)==F(18,5) and bit_cost(6)==F(11,3)
    out={'random_trees_checked':1000,'F088':{'costs':[2,2],'true_estimate':4,'true_variance':0,'printed_second_moment':12,'printed_variance':-4},
         'figure69':figure69(),'binomial_tree':binomial_trees(),
         'F090':{'q':5,'printed_bits':'10/3','optimal_bits':str(bit_cost(5)),'three_bit_lower_bound':'27/8'},
         'optimal_bits':{q:str(bit_cost(q)) for q in range(1,41)}}
    big=[json.loads(x) for x in (OUT/'queen-moments.jsonl').read_text().splitlines()]
    for r in big:
        assert r['nodes']==r['mean'] and r['second']==r['mean']**2+r['variance']
        r['sd']=sqrt(r['variance'])
    assert big[1]['min']==489 and big[1]['max']==7409 and big[1]['variance']==1146640
    assert big[2]['min']==2597105 and big[2]['max']==131048318769 and round(big[2]['sd'],-6)==1234000000
    out['queens']=big
    (OUT/'exact-verified.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':'pass','trees':1000,'queens':big,'tail100':out['binomial_tree'],'five_way_bits':out['F090']},indent=2))

if __name__=='__main__':main()

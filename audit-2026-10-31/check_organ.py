#!/usr/bin/env python3
"""Exact independent sound-set counting for TAOCP 4B 7.2.2--79.

The independent model enumerates local Boolean output patterns. Each pattern
is labelled by the set of console settings that can produce it. Across pitch
classes, intersect those sets. A sound is playable iff the intersection is
nonempty. This counts distinct sounds, not console/key configurations.
All per-console polynomials are compared with the printed formulas.
"""
from collections import Counter,defaultdict
from math import comb
from pathlib import Path
import json
import random
import time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/organ'


def add(a,b,factor=1):
    c=a.copy()+[0]*max(0,len(b)-len(a))
    for i,x in enumerate(b):c[i]+=factor*x
    while len(c)>1 and c[-1]==0:c.pop()
    return c


def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:c[i+j]+=x*y
    return c


def power(a,n):
    p=[1]
    for _ in range(n):p=mul(p,a)
    return p


def sparse(d):
    a=[0]*(max(d,default=0)+1)
    for i,c in d.items():a[i]+=c
    return a


def binomial_poly(step,n):
    if step==0:return [2**n]
    return sparse({step*k:comb(n,k) for k in range(n+1)})


def f(n):return add(binomial_poly(n,56),[1],-1)
def g(m,n):return mul(binomial_poly(n,12),add(binomial_poly(m,44),[1],-1))


def h(w,z,corrected=True):
    a=Counter({0:1});a[ w+2*z]+=3;a[2*w+3*z]+=2;a[2*w+4*z]+=1;a[3*w+4*z]+=1
    b=Counter({0:1});b[w+2*z]+=2;b[2*w+3*z]+=1
    left,right=power(sparse(a),8),power(sparse(b),4)
    return add(mul(left,right),[1],-1) if corrected else mul(left,add(right,[1],-1))


def q(z):
    a=sparse({0:1,2*z:3,3*z:2,4*z:1})
    b=sparse({0:1,2*z:2,3*z:1})
    c=sparse({0:1,2*z:1})
    return add(add(mul(power(a,8),power(b,4)),mul(power(b,8),power(c,4)),-2),power(c,8))


def book_polynomials(division,corrected=True):
    out=[[1]]
    if division=='G':
        for k in range(1,64):
            c9,c10,c11,c12,c13,c14=[k>>i&1 for i in range(6)]
            if c13*c14:p=[0]
            elif not c10:p=f(c9+c11+c12+c13+3*c14)
            else:p=g(c9+1+c11+c12+c13+3*c14,1+c11+c12+c13+3*c14)
            out.append(p)
    elif division=='S':
        for k in range(1,64):
            c3,c4,c5,c6,c7,c8=[k>>i&1 for i in range(6)]
            if k==32:p=add(binomial_poly(1,44),[1],-1)
            elif c4==c8==0:p=f(c3+c5+c6+c7)
            else:p=g(c3+c4+c5+c6+c7+c8,max(c3,c4)+c5+c6+c7)
            out.append(p)
    else:
        for k in range(1,32):
            c0,c1,c2,c15,c16=[k>>i&1 for i in range(5)]
            if k==31:p=h(1,2,corrected)
            elif c0*c15==c1*c16==0:
                if c0+c1+c2==0:
                    p=add(binomial_poly(c15+c16,32),binomial_poly(c15+c16,20),-1)
                else:p=add(binomial_poly(c0+c1+c2+c15+c16,32),[1],-1)
            elif c0==c15 and c1==c16 and c2==0:p=q(c0+c1)
            else:p=h(c0+c1+c2+c15+c16-2,1,corrected)
            out.append(p)
    return out


def pedal_pattern(k,length,notes):
    c0,c1,c2,c15,c16=[k>>i&1 for i in range(5)]
    p=lambda j: int(0<=j<length and notes>>j&1)
    rows=[]
    for j in range(length+1):
        if (c0 and p(j)) or (c15 and p(j-1)):rows.append(j)
        if (c1 and p(j)) or (c16 and p(j-1)):rows.append(length+1+j)
        if c2 and p(j):rows.append(2*(length+1)+j)
    return sum(1<<x for x in rows)


def manual_pattern(division,k,low):
    c=[k>>i&1 for i in range(6)]
    if division=='S':
        bits=[c[0] or (c[1] and low),c[1] and not low,c[2],c[3],c[4],c[5] and not low]
    else:
        bits=[c[0] or (c[1] and low),c[1] and not low,c[2],c[3],c[4] or c[5],c[5],c[5]]
    return sum(int(b)<<i for i,b in enumerate(bits))


def alphabet(division,kind):
    masks=defaultdict(int)
    for k in range(32 if division=='P' else 64):
        patterns=({pedal_pattern(k,kind,p) for p in range(1<<kind)} if division=='P'
                  else {0,manual_pattern(division,k,kind)})
        for pattern in patterns:masks[pattern] |= 1<<k
    return masks


def independent(division):
    settings=32 if division=='P' else 64
    kinds=[3]*8+[2]*4 if division=='P' else [True]*12+[False]*44
    tables={k:alphabet(division,k) for k in set(kinds)}
    dp={(1<<settings)-1:[1]}
    sizes=[]
    for kind in kinds:
        # Distinct patterns with equal weight/membership have equal effects,
        # but their multiplicities must be retained.
        counts=Counter((mask,p.bit_count()) for p,mask in tables[kind].items())
        nxt={}
        for state,poly in dp.items():
            for (mask,weight),number in counts.items():
                dest=state&mask
                if dest:
                    shifted=[0]*weight+[number*x for x in poly]
                    nxt[dest]=add(nxt.get(dest,[0]),shifted)
        dp=nxt;sizes.append(len(dp))
    canonical=[[0] for _ in range(settings)]
    for state,poly in dp.items():
        k=(state&-state).bit_length()-1
        canonical[k]=add(canonical[k],poly)
    return canonical,{'alphabet_sizes':{str(k):len(v) for k,v in tables.items()},'state_counts':sizes}


def sound(s,g,p,c):
    # Direct literal definitions, including couplers (no generating functions).
    pp=lambda j:j in p if 0<=j<32 else False
    out=set()
    for j in range(56):
        ss=j in s or (17 in c and j in g) or (18 in c and pp(j))
        gg=j in g or (19 in c and pp(j))
        for i in range(16):
            if i in (0,1):b=(i in c and pp(j)) or (i+15 in c and pp(j-12))
            elif i==2:b=2 in c and pp(j)
            elif i==3:b=(3 in c or (4 in c and j<12)) and ss
            elif i in (4,8):b=i in c and j>=12 and ss
            elif i in (5,6,7):b=i in c and ss
            elif i==9:b=(9 in c or (10 in c and j<12)) and gg
            elif i==10:b=10 in c and j>=12 and gg
            elif i in (11,12):b=i in c and gg
            elif i==13:b=(13 in c or 14 in c) and gg
            else:b=14 in c and gg
            if b:out.add((i,j))
    return out


def playable(target):
    # Monotonicity oracle: for each console setting retain exactly those
    # individual keys whose output is a subset of target; union them all.
    # Existence follows iff this largest admissible union equals target.
    divisions=[(range(0,3),[0,1,2,15,16],32),
               (range(3,9),list(range(3,9)),56),
               (range(9,16),list(range(9,15)),56)]
    for part,(ranks,switches,nkeys) in enumerate(divisions):
        want={x for x in target if x[0] in ranks}
        if not want:continue
        found=False
        for mask in range(1<<len(switches)):
            c={x for i,x in enumerate(switches) if mask>>i&1}
            got=set()
            for j in range(nkeys):
                args=[set(),set(),set()]
                args[[2,0,1][part]]={j}
                one=sound(*args,c)
                if one<=want:got |= one
            if got==want:
                found=True;break
        if not found:return False
    return True


def main():
    started=time.time();OUT.mkdir(parents=True,exist_ok=True)
    result={'status':'running','divisions':{}}
    polys={}
    for division in ('P','S','G'):
        actual,stats=independent(division)
        printed=book_polynomials(division)
        assert actual==printed,(division,[i for i,(a,b) in enumerate(zip(actual,printed)) if a!=b])
        total=[0]
        for p in actual:total=add(total,p)
        polys[division]=total
        stats['per_console_polynomials']=actual
        stats['total']=total
        result['divisions'][division]=stats
        print(division,'max_states',max(stats['state_counts']),'degree',len(total)-1,flush=True)
    p,s,g=[polys[k] for k in 'PSG']
    wrong=[0]
    for term in book_polynomials('P',False):wrong=add(wrong,term)
    assert wrong[3]==22704 and p[3]==22848
    assert book_polynomials('P',False)[11][3]==8
    assert book_polynomials('P')[11][3]==32
    result['F099']={'printed_P3':wrong[3],'correct_P3':p[3],
                    'printed_P11_z3':8,'correct_P11_z3':32,
                    'correction':'h(w,z)=A(w,z)^8 B(w,z)^4 - 1, not A(w,z)^8 (B(w,z)^4 - 1)',
                    'printed_P':wrong}
    assert (p[:4],p[10],p[-2:])==([1,120,2336,22848],324113168,[8,1])
    assert (s[:4],s[10],s[308],s[312])==([1,312,9312,155720],180657383126,12,1)
    assert (g[:4],g[10],g[374],g[380])==([1,268,8146,139452],178087336020,12,1)
    assert all(s[n]>g[n] for n in range(1,108))
    assert s[108]<g[108]
    Q=mul(mul(p,s),g)
    assert Q[:11]==[1,700,173010,18838948,1054376915,38386611728,1039287557076,
                    22560539157160,410723052356833,6457608682396156,89490036797524716]
    assert len(Q)==813 and Q[-2:]==[8,1]
    result['F100']={'printed_Q811':12,'correct_Q811':8,
                    'missing_pipe_positions':[[2,j] for j in range(12,20)]}
    result['Q']=Q
    result['ratios']=[Q[n]/comb(812,n) for n in range(2,11)]
    result['first_S_G_crossing']={'n':108,'S':s[108],'G':g[108]}
    full=sound(set(range(56)),set(range(56)),set(range(32)),set(range(20)))
    absent={(i,j) for i in range(16) for j in range(56)}-full
    assert len(full)==812 and absent==({(i,j) for i in (0,1) for j in range(44,56)}
           |{(2,j) for j in range(32,56)}|{(i,j) for i in (4,8,10) for j in range(12)})
    assert sound({33,45},set(),set(),{3,4,5,6})=={(i,j) for i in (3,4,5,6) for j in (33,45)}
    assert sound(set(),set(),{0,12},{0,1,15})=={(0,0),(0,12),(0,24),(1,0),(1,12)}
    assert sound({0,19,28},set(),set(),{3,4})=={(3,0),(3,19),(3,28),(4,19),(4,28)}
    rng=random.Random(79)
    for _ in range(1000):
        args=[{i for i in range(n) if rng.randrange(2)} for n in [56,56,32,20]]
        ss,gg,pp,cc=args
        coupled_s=ss|(gg if 17 in cc else set())|(pp if 18 in cc else set())
        coupled_g=gg|(pp if 19 in cc else set())
        assert sound(*args)==sound(coupled_s,coupled_g,pp,cc-{17,18,19})
        larger=[a|{i for i in range(n) if rng.randrange(2)} for a,n in zip(args,[56,56,32,20])]
        assert sound(*args)<=sound(*larger)
    # Cache each single-key output; avoid repeating the 896 literal tests
    # for every target in the independent monotonicity oracle.
    patterns=[]
    for part,(switches,nkeys) in enumerate([([0,1,2,15,16],32),(list(range(3,9)),56),(list(range(9,15)),56)]):
        settings=[]
        for k in range(1<<len(switches)):
            cs={x for i,x in enumerate(switches) if k>>i&1}
            row=[]
            for j in range(nkeys):
                a=[set(),set(),set()];a[[2,0,1][part]]={j}
                row.append(sound(*a,cs))
            settings.append(row)
        patterns.append(settings)
    def oracle(target):
        for d,ranks in enumerate([range(3),range(3,9),range(9,16)]):
            want={x for x in target if x[0] in ranks}
            if not any(set().union(*(x for x in row if x<=want))==want for row in patterns[d]):return False
        return True
    for i in range(16):
        for j in range(16):
            forbidden=i in (2,14,15) or j in (0,1,2,14,15) or (
                i!=j and (3<=i<=8 and 3<=j<=8 or 9<=i<=15 and 9<=j<=15))
            assert oracle({(i,40),(j,50)})== (not forbidden),(i,j)
    singles=[pipe for pipe in full if oracle({pipe})]
    missing=[pipe for pipe in full if oracle(full-{pipe})]
    assert len(singles)==700
    assert set(missing)=={(2,j) for j in range(12,20)}
    for j in range(12,20):
        assert full-sound(set(range(56)),set(range(56)),set(range(32))-{j},set(range(20)))=={(2,j)}
    for j in range(20,24):
        assert full-sound(set(range(56)),set(range(56)),set(range(32))-{j},set(range(20)))=={(2,j),(0,j+12),(1,j+12)}
    result.update(status='pass',single_pipe_sounds=len(singles),missing_pipe_sounds=sorted(missing),
                  independent_pair_tests=256,random_coupler_monotonicity_tests=1000,
                  elapsed_seconds=time.time()-started)
    (OUT/'verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',flush=True)


if __name__=='__main__':main()

#!/usr/bin/env python3
"""4.3.3E and exercise 11: literal synchronous automata, independent product oracle.
State is (c,x0,y0,x1,y1,x,y,z2,z1,z0); all transitions read the old array.
"""
from pathlib import Path
from itertools import product
import json,random,time
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/fast-automata.json'
ZERO=(0,)*10

def step(state,left,right):
    c,x0,y0,x1,y1,x,y,z2,z1,z0=state
    cl,lx0,ly0,lx1,ly1,lx,ly,lz2,lz1,lz0=left
    polynomial=[lx*ly,x0*ly+lx*y0,x0*ly+x1*y1+lx*y0,
                x0*ly+x1*y+x*y1+lx*y0][c]
    total=right[9]+z1+lz2+polynomial
    assert 0<=total<8
    cp=min(c+1,3) if cl==3 else 0
    xp0,yp0=(lx,ly) if c==0 else (x0,y0)
    xp1,yp1=(lx,ly) if c==1 else (x1,y1)
    xp,yp=(lx,ly) if c>=2 else (x,y)
    return (cp,xp0,yp0,xp1,yp1,xp,yp,total>>2,(total>>1)&1,total&1),polynomial

def simulate(u,v,q,n,width=None,check_mass=False,save=False):
    assert all(0<=x<1<<n for x in [u,v,q])
    if width is None:width=n//2+1
    states=[ZERO]*width;history=[states[:]];output=0;injected=0;largest_active=0
    for t in range(2*n+3):
        left=(3,0,0,0,0,(u>>t)&1,(v>>t)&1,(q>>t)&1,0,0)
        old=states;new=[];terms=[]
        for j in range(width):
            ns,P=step(old[j],left if j==0 else old[j-1],old[j+1] if j+1<width else ZERO)
            new.append(ns);terms.append(P)
            assert ns[0]==min(3,max(0,t+1-3*j))
            if ns[9]:largest_active=max(largest_active,j+1)
        states=new;output|=states[0][9]<<t
        if check_mass:
            # At time t+1, output through time t-1 plus all state mass
            # equals the weighted contribution already introduced.
            injected += ((q>>t)&1)<<t
            injected += sum(P<<(t+j) for j,P in enumerate(terms))
            old_output=output-((states[0][9])<<t)
            mass=sum(((s[7]<<2)+(s[8]<<1)+s[9])<<(t+j) for j,s in enumerate(states))
            assert old_output+mass==injected
            assert output%(1<<(t+1))==(u*v+q)%(1<<(t+1))
            assert injected<=u*v+q
        if save:history.append(states[:])
    return output,dict(largest_active=largest_active,history=history if save else None)

def exhaustive():
    cases=0;pure=0;maximum=0
    for n in range(1,5):
        for u,v,q in product(range(1<<n),repeat=3):
            got,s=simulate(u,v,q,n,check_mass=True);assert got==u*v+q
            cases+=1;maximum=max(maximum,s['largest_active'])
    # Larger pure products, including the n=2 exception if q must be zero.
    for n in [5,6]:
        for u,v in product(range(1<<n),repeat=2):
            got,_=simulate(u,v,0,n);assert got==u*v;pure+=1
    for u,v in product(range(4),repeat=2):
        got,_=simulate(u,v,0,2,width=1,check_mass=True);assert got==u*v
    short,_=simulate(3,3,3,2,width=1)
    full,_=simulate(3,3,3,2,width=2,check_mass=True)
    assert short==4 and full==12
    return dict(three_input_cases=cases,additional_pure_product_cases=pure,
                all_two_bit_pure_products_work_with_one_module=True,
                two_bit_addend_witness=dict(u=3,v=3,q=3,one_module=short,two_modules=full),
                largest_module_in_exhaustive=maximum)

def large():
    rng=random.Random(43357);cases=0;rows=[]
    for n in [5,6,7,8,15,16,31,32,63,64,127]:
        mask=(1<<n)-1;maximum=0
        pairs=[(0,0,0),(mask,mask,mask),(mask,mask,0),(1<<(n-1),1<<(n-1),0)]
        pairs += [(rng.getrandbits(n),rng.getrandbits(n),rng.getrandbits(n)) for _ in range(12)]
        for u,v,q in pairs:
            got,s=simulate(u,v,q,n,check_mass=True);assert got==u*v+q
            maximum=max(maximum,s['largest_active']);cases+=1
        rows.append(dict(n=n,cases=len(pairs),maximum_active_module=maximum,bound=n//2+1))
    sharp=[]
    for n in range(1,65):
        m=n//2+1;u=(1<<n)-1
        for q in [0,u]:
            full,s=simulate(u,u,q,n,check_mass=True);assert full==u*u+q
            short=0 if m==1 else simulate(u,u,q,n,width=m-1)[0]
            needed=(short!=full)
            assert needed or (n==2 and q==0)
            sharp.append(dict(n=n,q_is_zero=q==0,width=m,shorter_fails=needed))
    return dict(cases=cases,seed=43357,rows=rows,sharpness_cases=sharp)

def table2():
    got,s=simulate(23,23,11,5,width=3,check_mass=True,save=True)
    assert got==540
    h=s['history'][:12]
    # Independently transcribed printed table: c,x0y0,x1y1,xy,z2z1z0.
    # Pair fields are encoded as two-bit integers; z field as a three-bit integer.
    expected=[
        [(0,0,0,0,0),(0,0,0,0,0),(0,0,0,0,0)],
        [(1,3,0,0,2),(0,0,0,0,0),(0,0,0,0,0)],
        [(2,3,3,0,4),(0,0,0,0,0),(0,0,0,0,0)],
        [(3,3,3,3,3),(0,0,0,0,1),(0,0,0,0,0)],
        [(3,3,3,0,5),(1,3,0,0,1),(0,0,0,0,0)],
        [(3,3,3,3,3),(2,3,0,0,1),(0,0,0,0,0)],
        [(3,3,3,0,4),(3,3,0,3,2),(0,0,0,0,0)],
        [(3,3,3,0,0),(3,3,0,0,2),(1,3,0,0,1)],
        [(3,3,3,0,0),(3,3,0,0,2),(2,3,0,0,0)],
        [(3,3,3,0,0),(3,3,0,0,1),(3,3,0,0,0)],
        [(3,3,3,0,1),(3,3,0,0,0),(3,3,0,0,0)],
        [(3,3,3,0,0),(3,3,0,0,0),(3,3,0,0,0)]
    ]
    observed=[[(x[0],2*x[1]+x[2],2*x[3]+x[4],2*x[5]+x[6],4*x[7]+2*x[8]+x[9]) for x in row] for row in h]
    mismatches=[dict(time=t,module=j+1,printed=expected[t][j],computed=observed[t][j])
                for t in range(12) for j in range(3) if expected[t][j]!=observed[t][j]]
    # Keep mismatches explicit; a scan transcription is not silently corrected.
    assert not mismatches,mismatches
    return dict(answer=got,output_bits=[row[0][9] for row in h[1:]],rows=observed,table_states_checked=36)

def main():
    d=json.loads(OUT.read_text()) if OUT.exists() else {}
    for name,fn in [('table2',table2),('exhaustive',exhaustive),('large',large)]:
        if name in d:continue
        start=time.monotonic();r=fn();r['seconds']=round(time.monotonic()-start,3)
        d[name]=r;OUT.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'block':name,**r}),flush=True)
if __name__=='__main__':main()

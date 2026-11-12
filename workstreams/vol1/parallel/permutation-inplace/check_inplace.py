"""Actual MIX I/J, printed tables, canonical map and variance; no old checks rerun."""
from pathlib import Path
import sys, json, random
from collections import Counter
from fractions import Fraction as F
from itertools import permutations
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from mix_machine import Machine, number
from mixal import Assembly

HERE = Path(__file__).resolve().parent

def rows(program, n, x=100, start=0):
    prefix = [('N','EQU',str(n)), ('X','EQU',str(x)), ('','ORIG',str(start))]
    if program == 'I':
        body = [('INVERT','ENT1','N'),('','ENT3','-1'),('2H','LD2N','X,1'),
          ('','J2P','5F'),('3H','ST3','X,1'),('','ENN3','0,1'),
          ('','ENN1','0,2'),('','LD2N','X,1'),('4H','J2N','3B'),
          ('','ENN2','0,3'),('5H','ST2','X,1'),('6H','DEC1','1'),('','J1P','2B')]
    else:
        r = '1' if program == 'J-original' else '4'
        body = [('INVERT','ENN'+r,'N'),('','ST'+r,'X+N+1,'+r+'(0:0)'),
          ('','INC'+r,'1'),('','J'+r+'N','*-2'),('','ENT1','N'),
          ('2H','ENN3','0,1'),('','ENN2','0,3'),('','LD3N','X,2'),
          ('','J3N','*-2'),('','LDA','X,3'),('','STA','X,2'),('','ST1','X,3'),
          ('','DEC1','1'),('','J1P','2B')]
    return prefix+body+[('','END','INVERT')]

def inverse(p):
    result=[0]*len(p)
    for i,v in enumerate(p,1): result[v-1]=i
    return tuple(result)

def canonical(p):
    unseen=set(range(1,len(p)+1)); cycles=[]
    while unseen:
        start=min(unseen); c=[]; v=start
        while v in unseen:
            unseen.remove(v); c.append(v); v=p[v-1]
        assert v==start
        cycles.append(c)
    return tuple(v for c in reversed(cycles) for v in c), len(cycles)

def dots(q):
    # A: each index and all following larger entries up to first smaller entry.
    total=0
    for j,v in enumerate(q):
        k=j
        while k<len(q) and q[k]>=v: total+=1; k+=1
    return total

def run_case(p, program, b=64, x=100, start=0, snapshots=False):
    n=len(p); asm=Assembly(rows(program,n,x,start),b); m=Machine(b); asm.load(m)
    code_len=13 if program=='I' else 14
    assert not set(range(start,start+code_len)) & set(range(x+1,x+n+1))
    for i,v in enumerate(p,1): m.mem[x+i]=number(v,b)
    # The algorithms may not depend on the initial values of any registers.
    for r in range(8): m.reg[r]=number((-1)**r*(23+r),b)
    m.overflow=True; m.comparison=-1
    before=list(m.mem); counts=Counter(); trace=[]
    q,C=canonical(inverse(p)); A=dots(q)
    bound=10*n+C+2 if program=='I' else 9*n+3*A+2
    while m.pc!=start+code_len:
        if m.steps>bound: raise AssertionError(('unexpected instruction count',program,p))
        line=m.pc-start+1; counts[line]+=1; m.step()
        if snapshots:
            trace.append({'line':line,'X':[m.mem[x+i].value(b) for i in range(1,n+1)],
                          'r':[w.value(b) for w in m.reg[1:5]],'time':m.time})
    got=tuple(m.mem[x+i].value(b) for i in range(1,n+1))
    assert got==inverse(p),(program,p,got)
    assert all(m.mem[x+i].sign==1 for i in range(1,n+1))
    assert all(before[i]==m.mem[i] for i in range(4000) if not x<i<=x+n)
    expected=({k:(1 if k in (1,2) else C if k==10 else n) for k in range(1,14)}
          if program=='I' else {k:(1 if k in (1,5) else A if k in (7,8,9) else n) for k in range(1,15)})
    assert dict(counts)==expected,(program,p,counts,expected)
    assert m.time==(14*n+C+2 if program=='I' else 13*n+4*A+2)
    assert m.steps==bound,(m.steps,bound)
    assert m.overflow and m.comparison==-1
    return {'program':program,'n':n,'b':b,'x':x,'start':start,'C':C,'A':A,
            'time':m.time,'steps':m.steps, **({'trace':trace} if snapshots else {})}

def moments_recurrence(limit):
    # The minimum splits a random ordering into independent left/right orderings.
    mu=[F(0)]; second=[F(0)]; out=[]
    for n in range(1,limit+1):
        mean=sum(mu[k]+mu[n-1-k]+n-k for k in range(n))/n
        sec=sum(second[k]+second[n-1-k]+2*mu[k]*mu[n-1-k]
            +2*(n-k)*(mu[k]+mu[n-1-k])+(n-k)**2 for k in range(n))/n
        h=sum((F(1,k) for k in range(1,n+1)),F(0)); h2=sum((F(1,k*k) for k in range(1,n+1)),F(0))
        v=2*n*(n+2)-(n+1)*h-(n+1)**2*h2
        assert mean==(n+1)*h-n
        assert sec-mean**2==v
        mu.append(mean);second.append(sec)
        if n<=12: out.append({'n':n,'mean':str(mean),'variance':str(v)})
    return out

def main():
    out={'programs':{},'boundary':[]}
    for program in ['I','J-original','J-2024']:
        count=0
        for n in range(1,8):
            for p in permutations(range(1,n+1)):
                run_case(p,program);count+=1
        out['programs'][program]={'all_permutations_n_1_to_7':count}
        print(program,count,flush=True)
    rng=random.Random(20261101)
    for b in range(64,101):
        for n in [1,2,63,64,65,99,100,101]:
            p=list(range(1,n+1));rng.shuffle(p)
            for program in out['programs']:run_case(p,program,b)
    out['all_radices']={'radices':list(range(64,101)),'sizes':[1,2,63,64,65,99,100,101],'program_runs':888}
    for program in out['programs']:
        size=3987 if program=='I' else 3986
        for b in [64,100]:
            for high in [False,True]:
                x=4000-size-1 if high else -1;start=0 if high else size
                for pattern in ['identity','ascending-cycle']:
                    p=tuple(range(1,size+1)) if pattern=='identity' else tuple(range(2,size+1))+(1,)
                    r=run_case(p,program,b,x,start);r['pattern']=pattern;out['boundary'].append(r)
        # Worst J search path is an increasing canonical inverse.
        p=(128,)+tuple(range(1,128));out['boundary'].append(run_case(p,program))
    out['tables']=[run_case((6,2,1,5,4,3),s,snapshots=True) for s in ['I','J-original']]
    p=(1,3,2,4);orbit=[p]
    while True:
        p=canonical(p)[0];orbit.append(p)
        if p==orbit[0]:break
    assert orbit==[(1,3,2,4),(4,2,3,1),(3,2,1,4),(4,2,1,3),(2,1,4,3),(3,4,1,2),(2,4,1,3),(1,2,4,3),(3,4,2,1),(1,3,2,4)]
    out['exercise16_orbit']=orbit
    out['exercise24_moments']=moments_recurrence(100)
    (HERE/'results'/'inplace.json').write_text(json.dumps(out,indent=2)+'\n')
    print('all checks passed',flush=True)

if __name__=='__main__':main()

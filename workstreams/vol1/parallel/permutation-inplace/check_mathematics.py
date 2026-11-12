"""New checks only: printed tables, canonical bijection, variance, transpose."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
from math import gcd,factorial
from collections import Counter
import json
from check_inplace import canonical,dots,rows,inverse
from mix_machine import Machine,number,instruction
from mixal import Assembly
HERE=Path(__file__).resolve().parent

def decode(q):
    c=[];cycles=[];minimum=float('inf')
    for v in q:
        if v<minimum:
            if c:cycles.append(c)
            c=[];minimum=v
        c.append(v)
    if c:cycles.append(c)
    p=[0]*len(q)
    for c in cycles:
        for v,w in zip(c,c[1:]+c[:1]):p[v-1]=w
    return tuple(p)

def printed_tables():
    traces=json.loads((HERE/'results/inplace.json').read_text())['tables']
    # Rows transcribed manually from original image, not from simulator output.
    t3=[
      [6,6,6,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,3],
      [2,2,2,2,2,2,2,2,2,2,2,2,-4,2,2],
      [1,1,-6,-6,-6,-6,-6,-6,-6,-6,-6,6,6,6,6],
      [5,5,5,5,5,5,5,-5,-5,-5,5,5,5,5,5],
      [4,4,4,4,4,4,-1,-1,4,4,4,4,4,4,4],
      [3,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1],
      [6,3,1,6,6,5,4,5,5,4,4,3,2,2,1],
      [-1,-6,-3,-1,-1,-1,-5,-4,-4,-4,-4,-4,-2,-2,-2],
      [3,1,6,-1,-1,4,5,-1,-4,-5,-5,-6,-4,-2,-3]]
    wanted=list(zip(*t3));cursor=0;found=[]
    for s in traces[0]['trace']:
        if s['line'] not in [3,8,11]:continue
        row=tuple(s['X']+[s['r'][0],s['r'][2],-s['r'][1]])
        if cursor<len(wanted) and row==wanted[cursor]:found.append(s['line']);cursor+=1
    assert cursor==15,(cursor,wanted[cursor:])
    t4=[
      [-6,-6,-6,-6,-6,-6,-6,-6,3,3,3,3,3],
      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,2,2,2],
      [-1,-1,6,6,6,6,6,6,6,6,6,6,6],
      [-5,-5,-5,-5,5,5,5,5,5,5,5,5,5],
      [-4,-4,-4,-4,-5,-5,4,4,4,4,4,4,4],
      [-3,-3,-1,-1,-1,-1,-1,-1,-6,-6,-6,-6,1],
      [6,6,5,5,4,4,3,3,2,2,1,1,0],
      [None,-3,-3,-4,-4,-5,-5,-1,-1,-2,-2,-6,-6],
      [6,6,6,5,5,5,5,6,6,2,2,6,6]]
    wanted=list(zip(*t4));cursor=0
    for s in traces[1]['trace']:
        if s['line'] not in [7,8,13]:continue
        row=tuple(s['X']+[s['r'][0],-s['r'][2],s['r'][1]])
        if cursor<len(wanted) and all(w is None or a==w for a,w in zip(row,wanted[cursor])):cursor+=1
    assert cursor==13,(cursor,wanted[cursor:])
    return {'table3_columns':15,'table4_columns':13,'status':'all cells and named variables agree'}

def transpose():
    cases=0;maxsize=0
    for m in range(1,26):
      for n in range(1,26):
        if m==n:continue
        N=m*n-1; p=tuple((m*x)%N for x in range(N))+(N,)
        exact=tuple(m*(x%n)+x//n for x in range(m*n))
        assert p==exact
        # gcd classes are disjoint; each is partitioned into equal-length orbits.
        classes={}
        unseen=set(range(N))
        while unseen:
            x=min(unseen);c=[];v=x
            while v in unseen:c.append(v);unseen.remove(v);v=p[v]
            assert v==x
            d=gcd(x,N);r=1
            while (pow(m,r,N//d) if N//d>1 else 0)!=(1%(N//d)):r+=1
            assert len(c)==r
            classes.setdefault(d,[]).append(c)
        for d,cs in classes.items():
            phi=sum(gcd(t,N//d)==1 for t in range(N//d))
            assert len(cs)*len(cs[0])==phi
        # The scatter map is p; a gather assignment uses its inverse q.
        q=tuple((n*x)%N for x in range(N))+(N,)
        assert all(q[p[x]]==x for x in range(m*n))
        a=list(range(m*n))
        for x in range(m*n):
            y=q[x]
            while y>x:y=q[y]
            if y!=x:continue
            save=a[x];v=x;w=q[v]
            while w!=x:a[v]=a[w];v=w;w=q[v]
            a[v]=save
        assert a==[(x%m)*n+x//m for x in range(m*n)]
        cases+=1;maxsize=max(maxsize,m*n)
    return {'rectangles':cases,'dimensions':'1..25, m!=n','largest_entries':maxsize}

def canonical_variance():
    out=[]
    for n in range(0,9):
        total=0;squares=0;fixed=[];seen=set()
        for p in permutations(range(1,n+1)):
            q,_=canonical(p);assert decode(q)==p;seen.add(q)
            if p==q:fixed.append(p)
            a=dots(q);total+=a;squares+=a*a
        count=factorial(n);assert len(seen)==count
        assert len(fixed)==(1 if n<=1 else 0)
        mean=F(total,count);var=F(squares,count)-mean**2
        h=sum((F(1,k) for k in range(1,n+1)),F(0));h2=sum((F(1,k*k) for k in range(1,n+1)),F(0))
        assert var==2*n*(n+2)-(n+1)*h-(n+1)**2*h2
        out.append({'n':n,'count':count,'mean':str(mean),'variance':str(var),'fixed_points':fixed})
    return out

def executable_limits():
    out=[]
    for program in ['I','J-original','J-2024']:
        length=13 if program=='I' else 14;n=3999-length;x=length
        for b in [64,100]:
            asm=Assembly(rows(program,n,x,0),b);m=Machine(b);asm.load(m)
            m.mem[length]=instruction(b,'HLT')
            for i in range(1,n+1):m.mem[x+i]=number(i,b)
            m.run(0,limit=50000)
            assert m.halted and m.pc==length+1
            assert [m.mem[x+i].value(b) for i in range(1,n+1)]==list(range(1,n+1))
            assert m.time==(15*n+3 if program=='I' else 17*n+3)
            out.append({'program':program,'n':n,'radix':b,'time_including_halt':m.time})
    return out

def main():
    out={'tables':printed_tables(),'ex12':transpose(),'canonical_and_variance':canonical_variance(),'complete_halted_programs':executable_limits()}
    (HERE/'results/mathematics.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()

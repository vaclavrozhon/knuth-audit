#!/usr/bin/env python3
"""Independent Fraction and allocation-fault checks for linked rationals."""
from fractions import Fraction as F
from math import comb, gcd
from pathlib import Path
import itertools
import json
import random
import sys
import time

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'sources'))
from linked_integer import Pool, Number
from linked_rational import Rational, add, subtract, multiply, divide, compare
OUT = ROOT / 'results/rational-linked.json'


def headers(*rats):
    return [h for x in rats for h in (x.numerator, x.denominator)]


def check_pair(pool, xx, yy, alias=False):
    x = Rational.from_ints(pool, xx.numerator, xx.denominator)
    y = x if alias else Rational.from_ints(pool, yy.numerator, yy.denominator)
    inputs = headers(x) if alias else headers(x,y)
    before = [h.to_int() for h in inputs]
    assert compare(x,y) == ((xx>yy)-(xx<yy))
    for op, oracle in [(add,lambda:xx+yy),(subtract,lambda:xx-yy),
                       (multiply,lambda:xx*yy),(divide,lambda:xx/yy)]:
        if op is divide and yy==0:
            used = pool.used
            try:op(x,y)
            except ZeroDivisionError:pass
            else:raise AssertionError('division by zero accepted')
            assert pool.used==used
            continue
        z=op(x,y);q=oracle()
        assert z.to_pair()==(q.numerator,q.denominator), (op.__name__,xx,yy,z.to_pair(),q)
        pool.check(inputs+headers(z))
        z.close()
        assert [h.to_int() for h in inputs]==before
        pool.check(inputs)
    x.close()
    if not alias:y.close()
    pool.check([])


def arithmetic():
    small=large=aliases=0;rows=[]
    values=sorted({F(u,a) for u in range(-4,5) for a in range(1,5)})
    rng=random.Random(45110)
    for base in [2,3,10,256]:
        pool=Pool(base,12000)
        for x,y in itertools.product(values,repeat=2):
            check_pair(pool,x,y);small+=1
        for _ in range(24):
            bits=rng.randrange(8,257)
            x=F(rng.randrange(-2**bits,2**bits),rng.randrange(1,2**bits))
            y=F(rng.randrange(-2**bits,2**bits),rng.randrange(1,2**bits))
            check_pair(pool,x,y);large+=1
        for x in values:check_pair(pool,x,x,True);aliases+=1
        rows.append({'base':base,'peak_nodes':pool.peak,'stats':pool.stats.copy()})
    pool=Pool(2**32,12000)
    for _ in range(12):
        x=F(rng.randrange(-2**1024,2**1024),rng.randrange(1,2**1024))
        y=F(rng.randrange(-2**1024,2**1024),rng.randrange(1,2**1024))
        check_pair(pool,x,y);large+=1
    rows.append({'base':pool.base,'peak_nodes':pool.peak,'stats':pool.stats.copy()})
    # Normalization with negative denominators and explicit common factors.
    normalize=0
    for u in range(-8,9):
        for a in range(-8,9):
            if not a:continue
            z=Rational.from_ints(pool,u,a);q=F(u,a)
            assert z.to_pair()==(q.numerator,q.denominator)
            z.close();normalize+=1
    pool.check([])
    return {'small_pairs':small,'large_pairs':large,'alias_pairs':aliases,
            'normalizations':normalize,'max_input_bits':1024,'rows':rows}


class FaultPool(Pool):
    def __init__(self,base,capacity):
        super().__init__(base,capacity)
        self.fail_at=None
    def alloc(self,d):
        if self.allocations==self.fail_at:
            raise MemoryError('injected allocation failure')
        return super().alloc(d)


def allocation():
    rows=[]
    for op in [add,subtract,multiply,divide,compare]:
        p=FaultPool(10,1000)
        x=Rational.from_ints(p,7,15);y=Rational.from_ints(p,-10,21)
        before=p.allocations
        z=op(x,y)
        if isinstance(z,Rational):z.close()
        count=p.allocations-before
        x.close();y.close();p.check([])
        for index in range(count):
            p=FaultPool(10,1000)
            x=Rational.from_ints(p,7,15);y=Rational.from_ints(p,-10,21)
            used=p.used;p.fail_at=p.allocations+index
            try:op(x,y)
            except MemoryError:pass
            else:raise AssertionError((op.__name__,index,'failure did not occur'))
            assert p.used==used and x.to_pair()==(7,15) and y.to_pair()==(-10,21)
            p.check(headers(x,y));x.close();y.close();p.check([])
        rows.append([op.__name__,count])
    p=FaultPool(10,1000);z=Rational.from_ints(p,12345,-54321)
    count=p.allocations;z.close();p.check([])
    for i in range(count):
        p=FaultPool(10,1000);p.fail_at=i
        try:Rational.from_ints(p,12345,-54321)
        except MemoryError:pass
        else:raise AssertionError(('construct',i))
        p.check([])
    rows.append(['construct',count])
    # Real exhaustion, in addition to faults at every successful allocation.
    p=Pool(10,40)
    x=Rational.from_ints(p,7,15);y=Rational.from_ints(p,-10,21)
    filler=Number(p)
    while p.free!=-1:filler.push_high(1)
    try:add(x,y)
    except MemoryError:pass
    else:raise AssertionError('full pool unexpectedly accepted addition')
    p.check(headers(x,y)+[filler]);filler.close();x.close();y.close();p.check([])
    # Populate alternating live/free nodes, then perform rational operations.
    p=Pool(10,1000);markers=[Number.from_int(p,1) for _ in range(1000)]
    survivors=[]
    for i,m in enumerate(markers):
        if i%2==0:m.close()
        else:survivors.append(m)
    x=Rational.from_ints(p,12345678901234567890,998877665544332211)
    y=Rational.from_ints(p,-987654321,123456789)
    z=multiply(x,y)
    q=F(12345678901234567890,998877665544332211)*F(-987654321,123456789)
    assert z.to_pair()==(q.numerator,q.denominator)
    jumps=0
    for h in headers(x,y,z):
        k=h.head
        while k!=-1:
            if p.next[k]!=-1 and abs(p.next[k]-k)!=1:jumps+=1
            k=p.next[k]
    assert jumps>0
    p.check(survivors+headers(x,y,z))
    x.close();y.close();z.close()
    for m in survivors:m.close()
    p.check([])
    return {'fault_injections':sum(r[1] for r in rows),'per_operation':rows,
            'real_exhaustion':True,'fragmented_live_digits':500,'nonadjacent_links':jumps}


def matrices():
    rows=[]
    for n in range(1,6):
        p=Pool(256,10000)
        mat=[[Rational.from_ints(p,1,i+j+1) for j in range(n)]+
             [Rational.from_ints(p,int(i==j)) for j in range(n)] for i in range(n)]
        for k in range(n):
            pivot=Rational.from_numbers(mat[k][k].numerator,mat[k][k].denominator)
            for j in range(2*n):
                old=mat[k][j];mat[k][j]=divide(old,pivot);old.close()
            pivot.close()
            for i in range(n):
                if i==k:continue
                factor=Rational.from_numbers(mat[i][k].numerator,mat[i][k].denominator)
                for j in range(2*n):
                    prod=multiply(factor,mat[k][j]);old=mat[i][j]
                    mat[i][j]=subtract(old,prod);old.close();prod.close()
                factor.close()
        for i in range(n):
            for j in range(n):
                assert mat[i][j].to_pair()==(int(i==j),1)
                want=(-1)**(i+j)*(i+j+1)*comb(n+i,n-j-1)*comb(n+j,n-i-1)*comb(i+j,i)**2
                assert mat[i][n+j].to_pair()==(want,1)
        # Independent Fraction multiplication of the original matrix and result.
        inv=[[F(*mat[i][n+j].to_pair()) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):assert sum(F(1,i+k+1)*inv[k][j] for k in range(n))==int(i==j)
        p.check(headers(*[x for row in mat for x in row]))
        rows.append({'order':n,'peak_nodes':p.peak,'inverse_largest_integer':max(abs(x.numerator) for row in inv for x in row)})
        for row in mat:
            for x in row:x.close()
        p.check([])
    return {'hilbert_inversions':rows,'inverse_entries':sum(n*n for n in range(1,6))}


if __name__=='__main__':
    data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
    for name,fn in [('arithmetic',arithmetic),('allocation',allocation),('matrices',matrices)]:
        if name in data:continue
        start=time.monotonic();v=fn();data[name]={'status':'passed','seconds':time.monotonic()-start,'result':v}
        OUT.write_text(json.dumps(data,indent=2)+'\n');print(name,json.dumps(data[name]),flush=True)

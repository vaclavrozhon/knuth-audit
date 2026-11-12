"""Executable word-and-link model for TAOCP 4.3.1-34.
Only from_int/to_int (test adapters) combine all digits into Python integers.
Arithmetic uses one-digit operands and at most two-digit temporaries.
Allocation pops one node from a free chain; free nodes need not be contiguous.
"""
class Pool:
    def __init__(self,base,capacity):
        assert base>=2 and capacity>=0
        self.base=base;self.capacity=capacity
        self.digit=[0]*capacity;self.prev=[-1]*capacity
        self.next=list(range(1,capacity))+[-1] if capacity else []
        self.free=0 if capacity else -1;self.used=0;self.peak=0;self.allocations=0
        self.stats={'word_products':0,'trial_decrements':0,'add_backs':0,'division_steps':0}
    def alloc(self,d):
        assert 0<=d<self.base
        k=self.free
        if k<0:raise MemoryError('node pool exhausted')
        self.free=self.next[k];self.next[k]=self.prev[k]=-1;self.digit[k]=d
        self.used+=1;self.peak=max(self.peak,self.used);self.allocations+=1
        return k
    def release(self,k):
        self.next[k]=self.free;self.prev[k]=-1;self.free=k;self.used-=1
    def check(self,numbers):
        # Independent structural audit, outside arithmetic/allocator complexity.
        seen=set()
        for x in numbers:
            assert x.pool is self
            k=x.head;prev=-1;n=0
            while k!=-1:
                assert 0<=k<self.capacity and k not in seen
                seen.add(k);assert self.prev[k]==prev and 0<=self.digit[k]<self.base
                prev=k;k=self.next[k];n+=1
            assert n==x.length and prev==x.tail
            assert (n==0)==(x.sign==0)
            if n:assert self.digit[x.tail]!=0 and x.sign in (-1,1)
        assert len(seen)==self.used
        k=self.free;free=set()
        while k!=-1:
            assert 0<=k<self.capacity and k not in seen and k not in free
            free.add(k);k=self.next[k]
        assert len(free)+len(seen)==self.capacity

class Number:
    def __init__(self,pool,sign=1):
        self.pool=pool;self.head=self.tail=-1;self.length=0;self.sign=0
        self.preferred_sign=sign
    def push_high(self,d):
        p=self.pool;k=p.alloc(d);p.prev[k]=self.tail
        if self.tail!=-1:p.next[self.tail]=k
        else:self.head=k
        self.tail=k;self.length+=1
        if self.sign==0:self.sign=self.preferred_sign
    def push_low(self,d):
        p=self.pool;k=p.alloc(d);p.next[k]=self.head
        if self.head!=-1:p.prev[self.head]=k
        else:self.tail=k
        self.head=k;self.length+=1
        if self.sign==0:self.sign=self.preferred_sign
    def trim(self):
        p=self.pool
        while self.tail!=-1 and p.digit[self.tail]==0:
            k=self.tail;self.tail=p.prev[k];p.release(k);self.length-=1
            if self.tail!=-1:p.next[self.tail]=-1
            else:self.head=-1;self.sign=0
        return self
    def close(self):
        p=self.pool;k=self.head
        while k!=-1:
            nxt=p.next[k];p.release(k);k=nxt
        self.head=self.tail=-1;self.length=0;self.sign=0
    def digits(self):
        k=self.head
        while k!=-1:
            yield self.pool.digit[k];k=self.pool.next[k]
    @classmethod
    def from_int(cls,pool,n):
        # Test adapter, not an arithmetic implementation.
        x=cls(pool,-1 if n<0 else 1);n=abs(n)
        try:
            while n:n,d=divmod(n,pool.base);x.push_high(d)
            return x
        except BaseException:x.close();raise
    def to_int(self):
        # Independent test adapter.
        n=0;k=self.tail;p=self.pool
        while k!=-1:n=n*p.base+p.digit[k];k=p.prev[k]
        return n*self.sign

class Temps:
    """Exception-safe ownership of the constant number of scratch headers."""
    def __init__(self):self.numbers=[]
    def __enter__(self):return self
    def own(self,x):self.numbers.append(x);return x
    def keep(self,x):self.numbers.remove(x);return x
    def __exit__(self,*unused):
        for x in self.numbers:x.close()

def clone(x):
    with Temps() as t:
        y=t.own(Number(x.pool,x.sign))
        for d in x.digits():y.push_high(d)
        return t.keep(y)

def compare_abs(x,y):
    assert x.pool is y.pool
    if x.length!=y.length:return 1 if x.length>y.length else -1
    p=x.pool;i=x.tail;j=y.tail
    while i!=-1:
        if p.digit[i]!=p.digit[j]:return 1 if p.digit[i]>p.digit[j] else -1
        i=p.prev[i];j=p.prev[j]
    return 0

def add_abs(x,y):
    p=x.pool;b=p.base;assert y.pool is p
    with Temps() as w:
        z=w.own(Number(p));i=x.head;j=y.head;c=0
        while i!=-1 or j!=-1 or c:
            a=p.digit[i] if i!=-1 else 0;d=p.digit[j] if j!=-1 else 0
            c,e=divmod(a+d+c,b);z.push_high(e)
            i=p.next[i] if i!=-1 else -1;j=p.next[j] if j!=-1 else -1
        return w.keep(z.trim())

def sub_abs(x,y):
    assert compare_abs(x,y)>=0
    p=x.pool;b=p.base
    with Temps() as w:
        z=w.own(Number(p));i=x.head;j=y.head;c=0
        while i!=-1:
            a=p.digit[i]-(p.digit[j] if j!=-1 else 0)-c
            c=int(a<0);z.push_high(a+c*b)
            i=p.next[i];j=p.next[j] if j!=-1 else -1
        assert c==0
        return w.keep(z.trim())

def add(x,y,subtract=False):
    sy=-y.sign if subtract else y.sign
    if x.sign==0:
        z=clone(y);z.sign=sy;return z
    if sy==0:return clone(x)
    if x.sign==sy:
        z=add_abs(x,y);z.sign=x.sign;return z
    c=compare_abs(x,y)
    if c==0:return Number(x.pool)
    z=sub_abs(x,y) if c>0 else sub_abs(y,x)
    z.sign=x.sign if c>0 else sy;return z

def subtract(x,y):return add(x,y,True)

def multiply_digit(x,d):
    p=x.pool;b=p.base;assert 0<=d<b
    if d==0 or x.sign==0:return Number(p)
    with Temps() as w:
        z=w.own(Number(p,x.sign));c=0
        for a in x.digits():
            p.stats['word_products']+=1;c,e=divmod(a*d+c,b);z.push_high(e)
        if c:z.push_high(c)
        return w.keep(z.trim())

def multiply(x,y):
    p=x.pool;b=p.base;assert y.pool is p
    if x.sign==0 or y.sign==0:return Number(p)
    with Temps() as w:
        z=w.own(Number(p,x.sign*y.sign))
        for _ in range(x.length+y.length):z.push_high(0)
        row=z.head;j=y.head
        while j!=-1:
            i=x.head;k=row;c=0
            while i!=-1:
                a=p.digit[i]*p.digit[j]+p.digit[k]+c
                assert 0<=a<b*b
                p.stats['word_products']+=1;c,p.digit[k]=divmod(a,b)
                i=p.next[i];k=p.next[k]
            assert p.digit[k]==0;p.digit[k]=c
            row=p.next[row];j=p.next[j]
        return w.keep(z.trim())

def divide_digit(x,d):
    p=x.pool;b=p.base;assert 0<d<b
    with Temps() as w:
        q=w.own(Number(p));r=0;i=x.tail
        while i!=-1:
            a=r*b+p.digit[i];digit,r=divmod(a,d);q.push_low(digit);i=p.prev[i]
        return w.keep(q.trim()),r

def shift_words(x,n):
    assert n>=0
    with Temps() as w:
        z=w.own(clone(x))
        if z.sign:
            for _ in range(n):z.push_low(0)
        return w.keep(z)

def divide_abs(x,y):
    """D on linked magnitudes. Returns 0<=r<abs(y), positive quotient."""
    p=x.pool;b=p.base;assert y.pool is p
    if y.sign==0:raise ZeroDivisionError
    with Temps() as w:
        if compare_abs(x,y)<0:
            q=w.own(Number(p));r=w.own(clone(x));r.sign=1 if r.length else 0
            return w.keep(q),w.keep(r)
        if y.length==1:
            q0,r0=divide_digit(x,p.digit[y.head]);q=w.own(q0)
            r=w.own(Number(p))
            if r0:r.push_high(r0)
            return w.keep(q),w.keep(r)
        n=y.length;m=x.length-n
        factor=b//(p.digit[y.tail]+1)
        u=w.own(multiply_digit(x,factor));v=w.own(multiply_digit(y,factor))
        u.sign=v.sign=1
        assert v.length==n
        while u.length<x.length+1:u.push_high(0)
        q=w.own(Number(p))
        for _ in range(m+1):q.push_high(0)
        high=u.tail;low=u.head
        for _ in range(m):low=p.next[low]
        qpos=q.tail;vtop=p.digit[v.tail];vnext=p.digit[p.prev[v.tail]]
        for j in range(m,-1,-1):
            p.stats['division_steps']+=1
            h1=p.prev[high];h2=p.prev[h1]
            if p.digit[high]==vtop:guess=b-1;rhat=p.digit[h1]+vtop
            else:guess,rhat=divmod(p.digit[high]*b+p.digit[h1],vtop)
            assert 0<=guess<b
            while rhat<b and guess*vnext>b*rhat+p.digit[h2]:
                guess-=1;rhat+=vtop;p.stats['trial_decrements']+=1
            i=v.head;k=low;borrow=0
            while i!=-1:
                a=guess*p.digit[i]+borrow;borrow,d=divmod(a,b)
                p.stats['word_products']+=1
                a=p.digit[k]-d
                if a<0:a+=b;borrow+=1
                p.digit[k]=a;i=p.next[i];k=p.next[k]
            assert k==high
            a=p.digit[high]-borrow;p.digit[high]=a%b
            if a<0:
                guess-=1;p.stats['add_backs']+=1;i=v.head;k=low;carry=0
                while i!=-1:
                    carry,p.digit[k]=divmod(p.digit[k]+p.digit[i]+carry,b)
                    i=p.next[i];k=p.next[k]
                p.digit[high]=(p.digit[high]+carry)%b
            assert p.digit[high]==0
            p.digit[qpos]=guess;qpos=p.prev[qpos]
            high=p.prev[high];low=p.prev[low]
        q.trim();u.trim()
        r0,rem=divide_digit(u,factor);r=w.own(r0);assert rem==0
        return w.keep(q),w.keep(r)

def divmod_trunc(x,y):
    q,r=divide_abs(x,y)
    if q.length:q.sign=x.sign*y.sign
    if r.length:r.sign=x.sign
    return q,r

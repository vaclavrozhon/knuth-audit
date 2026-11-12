#!/usr/bin/env python3
"""4.3.3-12/13: pointer arithmetic/grouping and rectangular multiplication.
Python is a reference simulator, not a compiled seven-instruction machine.
Integer labels are used only by the independent oracle, never by bucket access.
"""
from pathlib import Path
import json, random, time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/fast-models.json'

class Node:
    def __init__(self,label):
        self.label=label
        self.next=self.half=self.double=None
        self.bit=0
        self.head=self.tail=None

def nodes(N):
    """Two linked sweeps; endpoint/double links wrap modulo N."""
    assert N>=2 and N&(N-1)==0
    zero=Node(0);tail=zero
    for label in range(1,N):
        tail.next=Node(label);tail=tail.next
    tail.next=zero
    p=q=zero;parity=0
    while True:
        p.half=q;p.bit=parity
        if parity:q=q.next
        parity^=1;p=p.next
        if p is zero:break
    p=q=zero
    while True:
        p.double=q;q=q.next.next;p=p.next
        if p is zero:break
    return zero

def binary(p,zero):
    out=[]
    while p is not zero:
        out.append(p.bit);p=p.half
    return out

def encode(bits,zero):
    p=zero
    for b in reversed(bits):
        p=p.double
        if b:p=p.next
    return p

def add_bits(a,b):
    carry=0;out=[]
    for i in range(max(len(a),len(b))):
        # A bounded truth table: all inputs are bits.
        t=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)+carry
        out.append(t&1);carry=t>>1
    if carry:out.append(carry)
    return out

def arithmetic(op,p,q,zero,width):
    a=binary(p,zero);b=binary(q,zero)
    if op==0:r=add_bits(a,b)
    else:
        r=[]
        for j,bit in enumerate(b):
            if bit:r=add_bits(r,[0]*j+a)
    return encode(r[:width],zero),encode(r[width:],zero)

class Instruction:
    def __init__(self,op,p,q):
        self.op=op;self.p=p;self.q=q;self.next=None;self.result=None

def stable_pass(head,zero,key):
    while head is not None:
        item=head;head=head.next;bucket=key(item);item.next=None
        if bucket.head is None:bucket.head=item
        else:bucket.tail.next=item
        bucket.tail=item
    out=tail=None;p=zero
    while True:
        if p.head is not None:
            if out is None:out=p.head
            else:tail.next=p.head
            tail=p.tail;p.head=p.tail=None
        p=p.next
        if p is zero:break
    return out

def batch(items,zero,width):
    for x,y in zip(items,items[1:]):x.next=y
    items[-1].next=None
    head=stable_pass(items[0],zero,lambda x:x.q)
    head=stable_pass(head,zero,lambda x:x.p)
    head=stable_pass(head,zero,lambda x:zero if x.op==0 else zero.next)
    previous=None;groups=0
    while head is not None:
        if previous is None or (head.op!=previous.op or head.p is not previous.p or head.q is not previous.q):
            result=arithmetic(head.op,head.p,head.q,zero,width);groups+=1
        head.result=result;previous=head;head=head.next
    return groups

def pointer_tests():
    arithmetic_cases=0;batch_cases=0;rows=[];rng=random.Random(43312)
    for width in range(1,7):
        N=1<<width;zero=nodes(N);table=[];p=zero
        for i in range(N):
            assert p.label==i and p.half.label==i//2 and p.double.label==2*i%N
            assert p.bit==i%2
            table.append(p);p=p.next
        for p in table:
            for q in table:
                for op in [0,1]:
                    lo,hi=arithmetic(op,p,q,zero,width)
                    want=p.label+q.label if op==0 else p.label*q.label
                    assert lo.label+N*hi.label==want;arithmetic_cases+=1
        items=[Instruction(rng.randrange(2),rng.choice(table),rng.choice(table)) for _ in range(8*N+1)]
        # Deliberately repeat operands with distinct output destinations.
        items+= [Instruction(x.op,x.p,x.q) for x in items[:N]]
        groups=batch(items,zero,width)
        oracle_groups=len({(x.op,x.p.label,x.q.label) for x in items})
        assert groups==oracle_groups<=2*N*N
        for x in items:
            want=x.p.label+x.q.label if x.op==0 else x.p.label*x.q.label
            assert x.result[0].label+N*x.result[1].label==want
        batch_cases+=len(items);rows.append(dict(N=N,instructions=len(items),groups=groups))
    return dict(arithmetic_cases=arithmetic_cases,batch_instructions=batch_cases,seed=43312,rows=rows)

def rectangular(u,v,m):
    B=1<<m;mask=B-1;carry=0;digits=[];blocks=0
    while v:
        digit=v&mask;v>>=m
        partial=u*digit+carry
        digits.append(partial&mask);carry=partial>>m;blocks+=1
        assert 0<=carry<B
    if carry:digits.append(carry)
    return sum(x<<(i*m) for i,x in enumerate(digits)),blocks

def rectangular_tests():
    rng=random.Random(43313);cases=0;max_n=0
    for m in [1,2,3,7,8,13,31,64,127,1024]:
        for n in [m,m+1,2*m-1,2*m,7*m+3,101*m+1]:
            for u,v in [(0,(1<<n)-1),((1<<m)-1,(1<<n)-1),
                        (1<<(m-1),1<<(n-1))]+[(rng.getrandbits(m),rng.getrandbits(n)) for _ in range(5)]:
                got,blocks=rectangular(u,v,m)
                assert got==u*v and blocks<=(n+m-1)//m
                cases+=1;max_n=max(max_n,n)
    return dict(cases=cases,max_n_bits=max_n,seed=43313)

def main():
    d=json.loads(OUT.read_text()) if OUT.exists() else {}
    for name,fn in [('pointer',pointer_tests),('rectangular',rectangular_tests)]:
        if name in d:continue
        start=time.monotonic();r=fn();r['seconds']=round(time.monotonic()-start,3)
        d[name]=r;OUT.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'block':name,**r}),flush=True)

if __name__=='__main__':main()

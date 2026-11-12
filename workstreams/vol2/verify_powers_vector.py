#!/usr/bin/env python3
"""Constructive and independent finite checks for TAOCP 4.6.3-36/37/39/40."""
from collections import Counter
from datetime import datetime,timezone
from functools import lru_cache
from itertools import product,combinations_with_replacement
import argparse
import json
from pathlib import Path
import random
import time

BASE=Path(__file__).resolve().parent
RESULT=BASE/'results/powers-vector.json'


class Program:
    def __init__(self,m):
        self.m=m
        self.values=[tuple(int(i==j) for j in range(m)) for i in range(m)]
        self.pairs=[]
        self.lookup={v:i for i,v in enumerate(self.values)}
    def add(self,a,b):
        if a is None:return b
        if b is None:return a
        value=tuple(x+y for x,y in zip(self.values[a],self.values[b]))
        if value not in self.lookup:
            self.lookup[value]=len(self.values);self.values.append(value);self.pairs.append((a,b))
        return self.lookup[value]
    def validate(self):
        for i,(a,b) in enumerate(self.pairs,self.m):
            assert 0<=a<i and 0<=b<i
            assert self.values[i]==tuple(x+y for x,y in zip(self.values[a],self.values[b]))
        assert len(self.values)==self.m+len(self.pairs)


def straus(target,k=1):
    m=len(target);b=1<<k;prog=Program(m)
    zero=(0,)*m;table={zero:None}
    for value in product(range(b),repeat=m):
        if value==zero:continue
        if sum(value)==1:table[value]=value.index(1);continue
        coord=next(i for i,x in enumerate(value) if x)
        previous=tuple(x-int(i==coord) for i,x in enumerate(value))
        table[value]=prog.add(table[previous],coord)
    precompute=len(prog.pairs)
    digits=(max(target).bit_length()-1)//k
    leading=tuple(x>>(k*digits)&(b-1) for x in target)
    current=table[leading]
    for pos in range(digits-1,-1,-1):
        for _ in range(k):current=prog.add(current,current)
        current=prog.add(current,table[tuple(x>>(k*pos)&(b-1) for x in target)])
    prog.validate();assert prog.values[current]==target
    assert precompute==b**m-m-1
    assert len(prog.pairs)<=b**m-m-1+(k+1)*digits
    return prog,current


def straus_block():
    count=0;examples=[]
    for m,limit in ((1,127),(2,24),(3,8),(4,4)):
        for target in product(range(1,limit+1),repeat=m):
            prog,output=straus(target)
            bound=2*(max(target).bit_length()-1)+(1<<m)-m-1
            assert len(prog.pairs)<=bound
            count+=1
    rng=random.Random(46336);large=0
    for m in range(1,6):
        for k in (1,2,3):
            if k*m>12:continue
            for bits in (17,65,257):
                target=tuple(rng.getrandbits(bits)|(1<<(bits-1)) for _ in range(m))
                prog,output=straus(target,k);large+=1
                if bits==257 and k==2:examples.append(dict(m=m,k=k,bits=bits,operations=len(prog.pairs)))
    return dict(binary_targets=count,large_radix_targets=large,max_bits=257,examples=examples)


def yao(targets,k):
    prog=Program(1);top=max(targets).bit_length()-1
    powers=[0]
    for _ in range(top):powers.append(prog.add(powers[-1],powers[-1]))
    outputs=[];detail=[];b=1<<k
    for n in targets:
        start=len(prog.pairs);buckets={};v=n;pos=0
        while v:
            digit=v&(b-1)
            if digit:
                e=(digit&-digit).bit_length()-1;q=digit>>e
                buckets[q]=prog.add(buckets.get(q),powers[k*pos+e])
            pos+=1;v>>=k
        grouping=len(prog.pairs)-start
        assert grouping<=(n.bit_length()-1)//k
        h=None;s=None
        for q in range(b-1,0,-2):
            h=prog.add(h,buckets.get(q))
            if q>=3:s=prog.add(s,h)
        out=prog.add(h,prog.add(s,s));outputs.append(out)
        combine=len(prog.pairs)-start-grouping
        assert combine<=b-1
        assert prog.values[out]==(n,)
        detail.append((grouping,combine))
    prog.validate()
    assert len(prog.pairs)<=top+sum((n.bit_length()-1)//k+b-1 for n in targets)
    # Independent ascending-chain validator after duplicate removal and sorting.
    values=sorted(v[0] for v in prog.values);available={1}
    for value in values[1:]:
        assert any(value-a in available for a in available)
        available.add(value)
    assert all(n in available for n in targets)
    return prog,outputs,detail


def yao_block():
    count=0
    for k in range(1,9):
        for n in range(1,2049):yao([n],k);count+=1
    rng=random.Random(46337);multi=[]
    for bits in (17,65,257,1025):
        for m in (1,2,5,11):
            targets=[rng.getrandbits(bits)|(1<<(bits-1)) for _ in range(m)]
            if m>1:targets[-1]=targets[0] # repeated outputs are intentional
            for k in (2,4,7):
                prog,outputs,detail=yao(targets,k)
                multi.append(dict(bits=bits,m=m,k=k,operations=len(prog.pairs),bound=bits-1+m*((bits-1)//k+(1<<k)-1)))
    return dict(single_targets=count,multiple_target_cases=len(multi),max_bits=1025,cases=multi)


def transpose(prog,outputs):
    # Add distinct zero-cost terminal copies, including repeated/unit outputs.
    original=len(prog.values);size=original+len(outputs)
    edges=[Counter() for _ in range(size)]
    for i,(a,b) in enumerate(prog.pairs,prog.m):edges[a][i]+=1;edges[b][i]+=1
    for j,out in enumerate(outputs):edges[out][original+j]+=1
    live=set(range(original,size))
    for i in range(original-1,-1,-1):
        if any(j in live for j in edges[i]):live.add(i)
    assert set(range(prog.m))<=live,'Only nonzero input rows are transposed.'
    edges=[Counter({j:x for j,x in row.items() if i in live and j in live}) for i,row in enumerate(edges)]
    used=sum(i in live for i in range(prog.m,original))
    reverse=Program(len(outputs));where={original+j:j for j in range(len(outputs))}
    raw_steps=0
    for i in range(original-1,-1,-1):
        if i not in live:continue
        operands=[where[j] for j,x in edges[i].items() for _ in range(x)]
        assert operands
        raw_steps+=len(operands)-1
        current=operands[0]
        for j in operands[1:]:current=reverse.add(current,j)
        where[i]=current
    reverse_outputs=[where[i] for i in range(prog.m)]
    reverse.validate()
    assert raw_steps==used+len(outputs)-prog.m
    assert len(reverse.pairs)<=raw_steps
    for i,node in enumerate(reverse_outputs):
        assert reverse.values[node]==tuple(prog.values[out][i] for out in outputs)
    return reverse,reverse_outputs,dict(original_useful=used,raw_transposed_steps=raw_steps,optimized_transposed_steps=len(reverse.pairs))


@lru_cache(None)
def minimum(targets):
    # BFS over sets of available exponent vectors. No graphical duality used.
    targets=frozenset(targets);dim=len(next(iter(targets)))
    units=frozenset(tuple(int(i==j) for j in range(dim)) for i in range(dim))
    states={units};depth=0;count=0
    while True:
        if any(targets<=s for s in states):return depth,count+len(states)
        next_states=set()
        for state in states:
            values=sorted(state);count+=1
            for i,a in enumerate(values):
                for b in values[:i+1]:
                    value=tuple(x+y for x,y in zip(a,b))
                    if value not in state and any(all(x<=y for x,y in zip(value,t)) for t in targets):
                        next_states.add(state|{value})
        assert next_states
        states=next_states;depth+=1


def canonical_targets(values):return tuple(sorted(set(values)))


def duality_block():
    tested=0;states=0;sample=[]
    for m,p,base in ((1,1,5),(1,2,4),(1,3,3),(2,1,4),(2,2,3),(2,3,2),(3,2,2)):
        for entries in product(range(base),repeat=m*p):
            rows=[tuple(entries[i*p:(i+1)*p]) for i in range(m)]
            cols=[tuple(entries[i*p+j] for i in range(m)) for j in range(p)]
            if any(not any(v) for v in rows+cols):continue
            a,sa=minimum(canonical_targets(cols));b,sb=minimum(canonical_targets(rows))
            assert a==b+m-p,(rows,a,b)
            tested+=1;states+=sa+sb
            if tested<=8:sample.append(dict(matrix=rows,length=a,transpose_length=b))
    # Real algorithm outputs, transposed by an independent graph routine.
    constructions=0
    for targets in ([1],[2],[1,1],[3,5],[1,2,3],[7,11,13],[31,31,47]):
        prog,outs,_=yao(targets,2)
        rev,revouts,costs=transpose(prog,outs)
        assert rev.values[revouts[0]]==tuple(targets)
        constructions+=1
    for target in ((1,1),(3,5),(7,11),(1,1,1),(2,3,4),(5,7,9)):
        prog,out=straus(target)
        rev,revouts,costs=transpose(prog,[out])
        assert [rev.values[i][0] for i in revouts]==list(target)
        constructions+=1
    return dict(matrices=tested,bfs_state_visits_summed_with_repeated_cached_problems=states,
                distinct_bfs_problems=minimum.cache_info().currsize,constructive_transpositions=constructions,examples=sample)


def marked_chains(depth):
    result=[]
    def visit(values,pairs):
        result.append((values,pairs))
        if len(pairs)==depth:return
        for j in range(len(values)):
            for k in range(j+1):
                v=values[j]+values[k]
                if v>values[-1]:visit(values+[v],pairs+[(j,k)])
    visit([1],[])
    return result


def compose(a,apairs,b,bpairs,coeff):
    indices=[(i,j) for i,row in enumerate(coeff) for j,v in enumerate(row) for _ in range(v)]
    assert indices
    original=Program(1)
    # Use the selected scalar representation verbatim, with its original indices.
    original.values=[(x,) for x in b];original.pairs=bpairs;original.lookup={v:i for i,v in enumerate(original.values)}
    monomial,outs,costs=transpose(original,[j for i,j in indices])
    values=a[:];lookup={x:i for i,x in enumerate(values)};pairs=apairs[:]
    where={k:i for k,(i,j) in enumerate(indices)}
    for k,(u,v) in enumerate(monomial.pairs,len(indices)):
        left,right=where[u],where[v];value=values[left]+values[right]
        if value not in lookup:lookup[value]=len(values);values.append(value);pairs.append((left,right))
        where[k]=lookup[value]
    n=values[where[outs[0]]]
    assert n==sum(coeff[i][j]*a[i]*b[j] for i in range(len(a)) for j in range(len(b)))
    assert len(pairs)<=len(apairs)+len(bpairs)+len(indices)-1
    for k,(i,j) in enumerate(pairs,1):assert i<k and j<k and values[k]==values[i]+values[j]
    available={1};normal=sorted(x for x in values if x<=n)
    for x in normal[1:]:assert any(x-y in available for y in available);available.add(x)
    assert normal[-1]==n
    return dict(n=n,operations=len(normal)-1,bound=len(apairs)+len(bpairs)+len(indices)-1)


def composition_block():
    chains=marked_chains(4);rng=random.Random(46340);count=0;examples=[]
    for a,apairs in chains:
        for b,bpairs in chains:
            coeff=[[rng.randrange(3) for _ in b] for _ in a]
            if not any(map(any,coeff)):coeff[0][0]=1
            row=compose(a,apairs,b,bpairs,coeff);count+=1
            if count<=6:examples.append(row)
    return dict(marked_input_chains=len(chains),nonzero_coefficient_matrices=count,examples=examples,
                zero_matrix='Excluded, as required by the known2022-02-22 erratum.')


BLOCKS={'straus':straus_block,'yao':yao_block,'duality':duality_block,'composition':composition_block}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('block',choices=BLOCKS);a=parser.parse_args()
    out=json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{}}
    assert a.block not in out['blocks'],'Do not rerun a completed block without a new concern.'
    start=time.perf_counter();data=BLOCKS[a.block]()
    out['blocks'][a.block]=dict(status='passed',seconds=time.perf_counter()-start,data=data,completed_at_utc=datetime.now(timezone.utc).isoformat())
    RESULT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(a.block,'PASSED',out['blocks'][a.block]['seconds'],flush=True)

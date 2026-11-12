#!/usr/bin/env python3
"""Exact graph, binary-chain, and tree audits for TAOCP 4.6.3-33/34/35."""
from collections import Counter
from datetime import datetime, timezone
from functools import lru_cache
from itertools import combinations
import argparse
import json
from pathlib import Path
import time

BASE=Path(__file__).resolve().parent
RESULT=BASE/'results/powers-graphs.json'


def matrix(pairs):
    size=len(pairs)+1
    a=[[0]*size for _ in range(size)]
    for i,(j,k) in enumerate(pairs,1):
        assert 0<=j<i and 0<=k<i
        a[j][i]+=1;a[k][i]+=1
    return a


def reduce_graph(a):
    # First retain exactly the ancestors of the designated final result.
    size=len(a);live={size-1}
    for i in range(size-1,-1,-1):
        if i in live: live.update(j for j in range(i) if a[j][i])
    assert 0 in live
    nodes=sorted(live)
    b=[[a[i][j] for j in nodes] for i in nodes]
    while True:
        dead=next((i for i in range(1,len(b)-1) if sum(b[i])==1),None)
        if dead is None:break
        out=next(j for j,v in enumerate(b[dead]) if v)
        for i in range(dead):b[i][out]+=b[i][dead]
        b=[[v for j,v in enumerate(row) if j!=dead] for i,row in enumerate(b) if i!=dead]
        nodes.pop(dead)
    return b,nodes,len(live)-1


def labels(a):
    values=[1]+[0]*(len(a)-1)
    for i in range(1,len(a)): values[i]=sum(values[j]*a[j][i] for j in range(i))
    return values


def reversed_graph(a):
    size=len(a)
    return [[a[size-1-j][size-1-i] for j in range(size)] for i in range(size)]


def cost(a):return sum(map(sum,a))-len(a)+1


def signature(a):
    values=labels(a)
    assert len(values)==len(set(values))
    return tuple(values),tuple((values[i],values[j],x) for i,row in enumerate(a) for j,x in enumerate(row) if x)


def expand(a,star=False):
    values=[1];pairs=[];outputs=[0]
    for i in range(1,len(a)):
        operands=[outputs[j] for j in range(i) for _ in range(a[j][i])]
        assert len(operands)>=2
        if star:
            assert a[i-1][i]
            operands.remove(outputs[-1]);operands.insert(0,outputs[-1])
        current=operands[0]
        for other in operands[1:]:
            pairs.append((current,other));values.append(values[current]+values[other]);current=len(values)-1
        outputs.append(current)
    assert len(pairs)==cost(a)
    return values,pairs


def path_matrix(a):
    # Independent finite geometric series I+A+...+A^(v-1).
    size=len(a)
    power=[[int(i==j) for j in range(size)] for i in range(size)]
    total=[row[:] for row in power]
    for _ in range(size-1):
        power=[[sum(power[i][k]*a[k][j] for k in range(size)) for j in range(size)] for i in range(size)]
        total=[[total[i][j]+power[i][j] for j in range(size)] for i in range(size)]
    return total


def graphs_block():
    counts=Counter();duplicate_examples=[];star_choice_example=None
    def visit(values,pairs):
        nonlocal star_choice_example
        counts['pair_labelled_chains']+=1
        a,nodes,useful=reduce_graph(matrix(pairs));p=labels(a)
        assert p==[values[i] for i in nodes]
        assert cost(a)==useful
        assert p==path_matrix(a)[0]
        b=reversed_graph(a);q=labels(b)
        assert q[-1]==p[-1] and cost(b)==cost(a) and reversed_graph(b)==a
        for g in (a,b):
            full,representation=expand(g)
            reduced,_,used=reduce_graph(matrix(representation))
            assert reduced==g and used==len(representation)==cost(g)
            assert full[-1]==values[-1]
            unique=all(g[i-1][i]>0 for i in range(1,len(g)))
            if unique:
                full,representation=expand(g,star=True)
                assert all(x<y for x,y in zip(full,full[1:]))
                assert all(i-1 in pair for i,pair in enumerate(representation,1))
                assert reduce_graph(matrix(representation))[0]==g
                counts['star_reconstructions']+=1
        chosen_star=all(i-1 in pair for i,pair in enumerate(pairs,1))
        unique=all(a[i-1][i]>0 for i in range(1,len(a)))
        if chosen_star:assert unique
        numerical_star=all(values[i]-values[i-1] in values[:i] for i in range(1,len(values)))
        if numerical_star and not unique:
            counts['numerical_star_with_nonstar_representation']+=1
            if star_choice_example is None:star_choice_example=dict(chain=values,pairs=pairs,reduced=a)
        if len(set(q))<len(q):
            counts['dual_repeated_retained_labels']+=1
            if len(duplicate_examples)<4:duplicate_examples.append(dict(chain=values,pairs=pairs,labels=p,dual_labels=q,graph=a))
        if len(pairs)==7:return
        for j in range(len(values)):
            for k in range(j+1):
                value=values[j]+values[k]
                if value>values[-1]:visit(values+[value],pairs+[(j,k)])
    visit([1],[])
    # Explicit n=14 witness with all displayed operations essential.
    values=[1,2,3,4,6,8,14]
    pairs=[(0,0),(1,0),(1,1),(2,2),(3,3),(4,5)]
    a,nodes,useful=reduce_graph(matrix(pairs));dual=labels(reversed_graph(a))
    assert labels(a)==[1,2,3,4,14] and dual==[1,2,2,6,14] and useful==6
    return dict(counts,maximum_length=7,duplicate_examples=duplicate_examples,
                explicit_repeated_dual=dict(chain=values,pairs=pairs,graph=a,dual_labels=dual),
                numerical_star_interpretation_example=star_choice_example,
                scope='Converse and reversal preserve computations with repeated values; strict-chain convention separately discussed.')


def left_binary(n,choices=None):
    values=[1];pairs=[];bit_count=0
    for digit in bin(n)[3:]:
        previous=len(values)-1
        if digit=='1' and values[-1]>1:
            option=0 if choices is None else choices>>bit_count&1
            bit_count+=1
            if option:
                values.append(values[-1]+1);pairs.append((previous,0))
                values.append(values[-1]+values[previous]);pairs.append((len(values)-2,previous))
                continue
        values.append(values[-1]*2);pairs.append((previous,previous))
        if digit=='1':
            pairs.append((len(values)-1,0));values.append(values[-1]+1)
    return values,pairs,bit_count


def right_binary(n):
    powers=[1<<i for i in range(n.bit_length())]
    terms=[x for x in powers if n&x]
    sums=[];current=terms[0];decomp={powers[i]:(powers[i-1],powers[i-1]) for i in range(1,len(powers))}
    for term in terms[1:]:decomp[current+term]=(current,term);current+=term;sums.append(current)
    values=sorted(set(powers+sums));where={x:i for i,x in enumerate(values)}
    return values,[(where[decomp[x][0]],where[decomp[x][1]]) for x in values[1:]]


def binary_block():
    rows=[]
    for n in range(1,16385):
        lv,lp,_=left_binary(n);rv,rp=right_binary(n)
        l,_,_=reduce_graph(matrix(lp));r,_,_=reduce_graph(matrix(rp))
        assert signature(reversed_graph(l))==signature(r)
        m=n.bit_length()-1
        assert labels(l)==[n>>k for k in range(m,-1,-1)]
        assert labels(r)==([1] if m==0 else [1<<k for k in range(m)]+[n])
        assert cost(l)==cost(r)==len(lp)==len(rp)==m+n.bit_count()-1
        if n in (1,2,3,5,13,79):rows.append(dict(n=n,left=lv,right=rv,reduced_left=labels(l),reduced_right=labels(r)))
    return dict(targets=16384,examples=rows,first_erroneous_printed_dual_label=3)


@lru_cache(None)
def trees(leaves):
    # Independent enumeration by all unordered bipartitions of a leaf multiset.
    if len(leaves)==1:return ((leaves[0],),)
    result=set();size=len(leaves)
    for mask in range(1,(1<<size)-1):
        first=tuple(leaves[i] for i in range(size) if mask>>i&1)
        second=tuple(leaves[i] for i in range(size) if not(mask>>i&1))
        if first>second:continue
        for a in trees(first):
            for b in trees(second):result.add(tuple(sorted((a,b),key=repr)))
    return tuple(result)


def tree_values(tree):
    if len(tree)==1:return tree[0],[]
    a,left=tree_values(tree[0]);b,right=tree_values(tree[1])
    return a+b,left+right+[(a+b,a,b)]


def odd_factorial(m):
    out=1
    for x in range(1,2*m,2):out*=x
    return out


def counting_block():
    core=[1,2,3,6,12];chains33=[]
    for tree in trees((3,12,12,12)):
        n,ops=tree_values(tree);assert n==39
        for middle in (40,78):chains33.append(sorted(core+[x for x,_,_ in ops]+[middle,79]))
    assert len(chains33)==len(set(map(tuple,chains33)))==8
    expected=[[0,3,0,0,0,1],[0,0,2,0,1,0],[0,0,0,2,0,0],[0,0,0,0,3,0],[0,0,0,0,0,2],[0,0,0,0,0,0]]
    sample=[(1,2,3,6,12,15,27,39,78,79),(1,2,3,6,12,15,24,39,40,79)]
    for values in chains33:
        # Enumerate all decompositions, independently of the trees, until the graph matches.
        options=[[(j,k) for j in range(i) for k in range(j+1) if values[j]+values[k]==values[i]] for i in range(1,len(values))]
        found=False
        def select(pairs):
            nonlocal found
            if found:return
            if len(pairs)==len(options):
                found=reduce_graph(matrix(pairs))[0]==expected;return
            for pair in options[len(pairs)]:select(pairs+[pair])
        select([]);assert found
    for value in sample:assert list(value) in chains33
    assert labels(expected)==[1,3,6,12,39,79]
    dual=reversed_graph(expected);assert labels(dual)==[1,2,6,12,26,79]
    dual_values=[1,2,4,6,12,24,26,52,78,79]
    dual_pairs=[(0,0),(1,1),(2,1),(3,3),(4,4),(5,1),(6,6),(7,6),(8,0)]
    assert signature(reduce_graph(matrix(dual_pairs))[0])==signature(dual)
    left_cases=right_cases=right_chains=0;rows=[]
    for n in range(2,512):
        lv,lp,bits=left_binary(n)
        variants=set()
        for choice in range(1<<bits):
            values,pairs,_=left_binary(n,choice)
            assert signature(reduce_graph(matrix(pairs))[0])==signature(reduce_graph(matrix(lp))[0])
            variants.add(tuple(values))
        expected_count=1<<(n.bit_count()-1-int(n.bit_count()>1 and bool(n&(1<<(n.bit_length()-2)))))
        assert len(variants)==expected_count;left_cases+=1
        m=n.bit_length()-1
        if n.bit_count()==1 or n&(1<<(m-1)) or n.bit_count()>5:continue
        q=1<<(m-1);leaves=tuple(sorted([q,q]+[1<<i for i in range(m-1) if n>>i&1]))
        tree_set=trees(leaves);t=n.bit_count()-1
        assert len(tree_set)==(odd_factorial(t+1)+odd_factorial(t))//2
        paths=set();base=[1<<i for i in range(m)]
        target=signature(reduce_graph(matrix(right_binary(n)[1]))[0])
        for tree in tree_set:
            value,ops=tree_values(tree);assert value==n
            values=sorted(base+[x for x,_,_ in ops]);assert len(values)==len(set(values))
            where={x:i for i,x in enumerate(values)}
            decomps={base[i]:(base[i-1],base[i-1]) for i in range(1,len(base))}
            decomps.update({x:(a,b) for x,a,b in ops})
            pairs=[tuple(where[y] for y in decomps[x]) for x in values[1:]]
            assert signature(reduce_graph(matrix(pairs))[0])==target
            paths.add(tuple(values));right_chains+=1
        assert len(paths)==len(tree_set);right_cases+=1
    # Abstract leaf-tree orbit counts beyond the numerical exhaustive range.
    for t in range(1,6):
        ts=trees(tuple([1,1]+list(range(2,t+2))))
        count=(odd_factorial(t+1)+odd_factorial(t))//2
        assert len(ts)==count;rows.append(dict(t=t,trees=count))
    return dict(exercise33=chains33,figure52=expected,figure54=dual,dual_example=dual_values,
                left_targets=left_cases,right_targets=right_cases,right_chain_graphs=right_chains,
                abstract_counts=rows)


BLOCKS={'graphs':graphs_block,'binary':binary_block,'counting':counting_block}
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('block',choices=BLOCKS);args=parser.parse_args()
    out=json.loads(RESULT.read_text()) if RESULT.exists() else {'blocks':{}}
    assert args.block not in out['blocks'],'Do not rerun completed blocks without a new concern.'
    start=time.perf_counter();data=BLOCKS[args.block]()
    out['blocks'][args.block]={'status':'passed','seconds':time.perf_counter()-start,'data':data,
                              'completed_at_utc':datetime.now(timezone.utc).isoformat()}
    RESULT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(args.block,'PASSED',out['blocks'][args.block]['seconds'],flush=True)

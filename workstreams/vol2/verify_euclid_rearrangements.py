#!/usr/bin/env python3
"""Block-reversal certificates for continuant extrema, TAOCP 4.5.3-37."""
from itertools import product, permutations
from pathlib import Path
from collections import Counter
import json, os, time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/euclid-rearrangements.json'

def K(a):
    x,y=0,1
    for z in a:x,y=y,z*y+x
    return y

def matching_sum(a):
    # Independent definition: tile a path by monomers and dimers.
    # A monomer at i has weight a_i, a dimer has weight1.
    total=0
    stack=[(0,1)]
    while stack:
        i,w=stack.pop()
        if i==len(a):total+=w;continue
        stack.append((i+1,w*a[i]))
        if i+1<len(a):stack.append((i+2,w))
    return total

def fixed_order(values,minimum):
    s=sorted(values);out=[None]*len(s);lo=0;hi=len(s)-1
    for r in range((len(s)+1)//2):
        positions=(r,len(s)-1-r) if r<len(s)-1-r else (r,)
        low=minimum and r%2==0
        for pos in positions:
            if low:out[pos]=s[lo];lo+=1
            else:out[pos]=s[hi];hi-=1
    return tuple(out)

def move_left(a,r,j,minimum,stats):
    # In this orientation both fixed boundaries have length r.
    # A previous placement at the opposite end may also be fixed.
    A=a[:r];B=a[r:j+1];C=a[j+1:]
    assert len(B)>=2
    QA=K(A[:-1]) if A else 0
    QC=K(C[1:]) if C else 0
    D=K(A)*QC-QA*K(C)
    Q=K(B[:-1])-K(B[1:])
    old=K(a)
    if minimum:
        assert (-1)**r*D>=0
        assert (-1)**r*Q>0
    else:
        assert D>=0 and Q<0
    a[r:j+1]=reversed(B)
    new=K(a)
    assert old-new==D*Q
    assert (new<=old if minimum else new>=old)
    stats['moves']+=1
    stats['equal_moves']+=new==old
    return a

def construct(values,minimum,stats):
    a=list(values);n=len(a)
    for r in range((n+1)//2):
        lo=r;hi=n-r-1
        if lo==hi:break
        low=minimum and r%2==0
        target=(min if low else max)(a[lo:hi+1])
        if a[lo]!=target:
            j=a.index(target,lo,hi+1)
            move_left(a,r,j,minimum,stats)
        # Reverse the entire orientation to apply the same identity at right.
        if lo+1<=hi:
            target=(min if low else max)(a[lo+1:hi+1])
            if a[hi]!=target:
                j=a.index(target,lo+1,hi+1)
                a.reverse();move_left(a,r,n-1-j,minimum,stats);a.reverse()
    assert tuple(a)==fixed_order(values,minimum)
    return tuple(a)

def explicit():
    rows=[]
    for a in range(1,13):
        for b in range(a+1,25):
            prescribed=(b,b,a,b,b);better=(b,a,b,b,b)
            assert K(better)-K(prescribed)==b-a
            assert K(prescribed)==a*(b**4+2*b*b+1)+2*b**3+2*b
            assert K(better)==a*(b**4+2*b*b)+2*b**3+3*b
            if (a,b) in ((1,2),(2,3),(3,10)):
                rows.append({'a':a,'b':b,'prescribed':list(prescribed),'K_prescribed':K(prescribed),'better':list(better),'K_better':K(better)})
    return {'families':210,'selected_examples':rows}

def identities():
    models=0;reversals=0;signs=0
    for n in range(1,8):
        for a in product(range(1,4),repeat=n):
            assert K(a)==matching_sum(a);models+=1
            if n>5:continue
            for i in range(n):
                for j in range(i+1,n):
                    A=a[:i];B=a[i:j+1];C=a[j+1:]
                    D=K(A)*(K(C[1:]) if C else 0)-(K(A[:-1]) if A else 0)*K(C)
                    Q=K(B[:-1])-K(B[1:])
                    assert K(a)-K(A+B[::-1]+C)==D*Q;reversals+=1
                    if B[0]!=B[-1]:assert Q*(B[0]-B[-1])>0;signs+=1
    return {'independent_matching_models':models,'block_reversal_identities':reversals,'different_endpoint_signs':signs}

def minimum_paths():
    stats={'inputs':0,'moves':0,'equal_moves':0}
    for n in range(1,10):
        for a in product(range(1,4),repeat=n):
            construct(a,True,stats);stats['inputs']+=1
    stats['scope']='Every word over {1,2,3}, lengths1..9. Every move and boundary sign checked.'
    return stats

def distinct_maximum_paths():
    stats={'inputs':0,'moves':0,'equal_moves':0}
    for n in range(1,9):
        for a in permutations(range(1,n+1)):
            construct(a,False,stats);stats['inputs']+=1
    # Different spacings test the boundary comparison independently of ranks.
    for vals in ((1,3,7,20,21),(2,4,9,15,100),(1,2,3,4,5,1000)):
        for a in permutations(vals):construct(a,False,stats);stats['inputs']+=1
    stats['scope']='All permutations of1..n for n<=8, plus three nonuniform alphabets.'
    return stats

def main():
    t=time.time();out={'pid':os.getpid(),'status':'running','checkpoints':{}}
    OUT.write_text(json.dumps(out,indent=2)+'\n');print('PID',os.getpid(),flush=True)
    for name,fn in [('counterexamples',explicit),('identities',identities),('minimum_paths',minimum_paths),('distinct_maximum_paths',distinct_maximum_paths)]:
        out['checkpoints'][name]=fn();OUT.write_text(json.dumps(out,indent=2)+'\n');print(name,'PASS',flush=True)
    out['prior_pilots_not_rerun']={
        'maximum_counterexample_search':'All{1,2,3}words of length<=4 passed; stopped at first length5 counterexample(2,1,2,2,2).',
        'minimum_global_comparisons':{'alphabet':[1,2,3],'lengths':'1..11','words':265719,'status':'passed','session_for_lengths9_to11':88913},
        'distinct_minimum_oracle':'All permutations1..n for n<=8; smallest minimizers were used only to check the printed pattern.',
        'rational_pilot':'15 random rational multisets in[1,6] for each n5,6; all permutations passed. Not a proof or claim for arbitrary real entries.'}
    out['status']='passed';out['elapsed_seconds']=time.time()-t
    OUT.write_text(json.dumps(out,indent=2)+'\n');print('PASS',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()

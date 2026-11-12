"""Construct every possible diagonal/central fixed maximum rook cycle on8x8."""
from itertools import permutations,product
from math import factorial
from verify_chess_snakes import OUT,adjacency,classify
import json

def mask(p,q):return sum(1<<(p[j]*8+c) for j in range(8) for c in [q[j],q[(j+1)%8]])

def transform(m,which):
    result=0
    for v in range(64):
        if m>>v&1:
            r,c=divmod(v,8)
            if which=='transpose':r,c=c,r
            else:r,c=7-r,7-c
            result|=1<<(r*8+c)
    return result

def main():
    diagonal=set();central=set()
    for tail in permutations(range(1,8)):
        p=(0,)+tail
        for k in range(8):
            q=tuple(p[(k-j)%8] for j in range(8))
            if q[0]<q[1]:diagonal.add(mask(p,q))
    half_perms=[]
    for pairs in permutations(range(4)):
        for choices in product(range(2),repeat=4):
            first=tuple(7-v if bit else v for v,bit in zip(pairs,choices))
            half_perms.append(first+tuple(7-v for v in first))
    assert len(half_perms)==384
    for p in half_perms:
        if p[0]!=0:continue
        for q in half_perms:
            if q[0]<q[1]:central.add(mask(p,q))
    a=adjacency(8,'rook')
    for m in diagonal:assert m.bit_count()==16 and classify(m,a)=='cycle' and transform(m,'transpose')==m
    for m in central:assert m.bit_count()==16 and classify(m,a)=='cycle' and transform(m,'central')==m
    assert len(diagonal)==20160 and len(central)==9216 and len(diagonal&central)==192
    raw=factorial(8)**2//16;classes=(raw+2*len(diagonal)+len(central))//8
    F=factorial(7)**2;A=factorial(6)**2;B=factorial(6)
    result=dict(cycle_positions=raw,cycle_fixed_diagonal=len(diagonal),cycle_fixed_central=len(central),
                cycle_fixed_both=len(diagonal&central),cycle_classes=classes,
                path_classes_corner=F-(A-B)//2,path_classes_01_no_corner=2*F-9*A+2*B,
                path_positions=factorial(8)**2,path_classes_all=(factorial(8)**2+2*factorial(8))//8)
    assert classes==12706992 and result['path_classes_corner']==25142760 and result['path_classes_01_no_corner']==46139040
    (OUT/'rook-eight.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

if __name__=='__main__':main()

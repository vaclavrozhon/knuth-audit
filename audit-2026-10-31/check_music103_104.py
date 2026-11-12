"""XCC row sets, full small symmetry groups, and perfect-row algebra."""
from itertools import permutations
from math import gcd
import json
from puzzle_xcc import ROOT, OUT, encode, native, read_models, colors_for, save, sha


def instance(n):
    primary=[f'j{j}' for j in range(n)]+[f'p{j}' for j in range(n)]
    primary += [f'd{k}' for k in range(1,n)]+[f'q{k}' for k in range(1,n)]
    rows=[]
    for j in range(n):
        for t in range(n):
            if (j==0 and t!=0) or (j==n-1 and 2*t!=n):continue
            rows.append([(f'j{j}',0),(f'p{t}',0),(f'x{j}',t+1)])
    for k in range(1,n):
        for t in range(1,n):
            for i in range(n):
                rows.append([(f'd{k}',0),(f'q{t}',0),(f'x{t-1}',i+1),(f'x{t}',(i+k)%n+1)])
    return encode(primary,[f'x{j}' for j in range(n)],rows)


def normalize(x):
    n=len(x);return tuple((v-x[0])%n for v in x)


def valid(x):
    n=len(x)
    return sorted(x)==list(range(n)) and { (x[i]-x[i-1])%n for i in range(1,n)}==set(range(1,n))


def qshift(x):
    n=len(x);cut=next(i for i in range(1,n) if (x[i]-x[i-1])%n==n//2)
    return x[cut:]+x[:cut]


def all_transforms(x):
    q=qshift(x);r=x[::-1];qr=q[::-1]
    assert qr==qshift(r)
    n=len(x)
    return {(c,op):normalize(tuple(c*v%n for v in y))
            for c in range(1,n) if gcd(c,n)==1 for op,y in [('id',x),('R',r),('Q',q),('QR',qr)]}


def read_cell_rows(n):
    meta=json.loads((OUT/f'music-{n}.json').read_text())
    assert meta['status']=='completed'
    path=OUT/f'music-{n}.rows.bin';assert sha(path)==meta['rows_sha256']
    data=path.read_bytes();rows={tuple(data[i:i+n]) for i in range(0,len(data),n)}
    assert len(rows)==meta['solutions']
    assert all(x[0]==0 and valid(x) for x in rows)
    return rows


def perfect(x):
    n=len(x);p=n+1
    return all(normalize(tuple(x[(k*r)%p-1] for k in range(1,p)))==x for r in range(1,p))


def perfect_checks():
    output=[]
    primes=[p for p in range(3,102) if all(p%d for d in range(2,int(p**.5)+1))]
    for p in primes:
        n=p-1;constructed=set()
        roots=[]
        for r in range(2,p):
            powers=[pow(r,j,p) for j in range(n)]
            if len(set(powers))!=n:continue
            roots.append(r)
            logs={value:j for j,value in enumerate(powers)}
            x=tuple(logs[k] for k in range(1,p))
            assert valid(x) and perfect(x) and normalize(x[::-1])==x
            constructed.add(x)
        assert len(constructed)==sum(gcd(c,n)==1 for c in range(1,n))
        if n<=6:
            brute={x for tail in permutations(range(1,n)) if perfect(x:=(0,)+tail)}
            assert brute==constructed
        if n<=12:
            from_all={x for x in read_cell_rows(n) if perfect(x)}
            assert from_all==constructed
        output.append(dict(n=n,primitive_roots=roots,perfect_rows=len(constructed)))
    example=(0,1,4,2,9,5,11,3,8,10,7,6)
    assert perfect(example) and valid(example)
    assert tuple((k*5)%13-1 for k in range(1,13))==(4,9,1,6,11,3,8,0,5,10,2,7)
    return output


def main():
    runs=[]
    for n in range(2,13):
        enc=instance(n);label=f'music-xcc-{n}'
        meta=native(label,enc,limit=1200)
        assert meta['status']=='completed'
        models=read_models(label,enc)
        rows=set()
        for model in models:
            colors=colors_for(enc,model)
            rows.add(tuple(colors[f'x{j}']-1 for j in range(n)))
        assert len(rows)==len(models) and rows==read_cell_rows(n)
        orbit_keys=set();symmetric=0;fix=CounterLike()
        for x in rows:
            transforms=all_transforms(x)
            assert all(valid(y) and y in rows for y in transforms.values())
            stabilized=[(c,op) for (c,op),y in transforms.items() if y==x and (c,op)!=(1,'id')]
            if n>4:
                assert len(stabilized)<=1
                for c,op in stabilized:
                    assert (op=='R' and c==1) or (op=='Q' and c==n-1) or (op=='QR' and c==n//2+1 and n%8==4)
            symmetric+=bool(stabilized)
            for c,op in stabilized:fix[f'{c}:{op}']+=1
            orbit_keys.add(min(transforms.values()))
        runs.append(dict(n=n,solutions=len(rows),xcc_nodes=meta['nodes'],
                         initial_mems=meta['initial_mems'],search_mems=meta['net_search_mems'],
                         symmetric_rows=symmetric,full_group_orbits=len(orbit_keys),nonidentity_fixed=dict(fix)))
        print('XCC + independent rows + all symmetries',n,len(rows),flush=True)
    examples=[(8,7,3,0,10,5,11,4,6,9,1,2),(0,1,3,7,2,5,11,10,8,4,9,6),
              (0,3,9,1,2,4,11,8,7,5,10,6),(0,1,4,9,3,11,10,8,5,7,2,6),
              (0,1,8,11,10,3,9,5,7,4,2,6),
              (0,1,3,11,2,19,13,9,12,7,14,18,4,17,16,8,6,15,5,10)]
    for x in examples:assert valid(x)
    assert normalize(examples[0][::-1])==normalize(examples[0])
    assert normalize(tuple(-v%12 for v in qshift(examples[1])))==examples[1]
    for x in examples[2:]:assert all_transforms(x)[len(x)//2+1,'QR']==x
    save(OUT/'music-checked.json',dict(script_sha256=sha(__file__),xcc_runs=runs,
         printed_examples_verified=examples,perfect_rows=perfect_checks(),
         boundary='Part103(a) assumes n>=2; n=1 is the vacuous permutation exception. Part(b) states n>=2 explicitly.'))


from collections import Counter as CounterLike
if __name__=='__main__':main()

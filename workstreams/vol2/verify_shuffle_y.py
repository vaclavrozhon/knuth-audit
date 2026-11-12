"""Independent sparse covering proof for the large example 3.2.2-(13).

Each aligned time block contains every bucket very near its beginning.
This certifies a weak global gap bound without repeating the full census.
"""
from math import gcd
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
M=2**35
A=2718281829
C=3141592653
SEED=1781072418


def state_at(n):
    # Compose affine maps by binary exponentiation, using Python big integers.
    a,c=A,C
    x=SEED
    while n:
        if n&1:x=(a*x+c)%M
        a,c=a*a%M,c*(a+1)%M
        n//=2
    return x


def main():
    census=json.loads((ROOT/'results/shuffle-y-census.json').read_text())
    assert (census['modulus'],census['a'],census['c'],census['seed'])==(M,A,C,SEED)
    assert census['raw_steps']==M and census['filtered_period']==M-1
    assert A%4==1 and C%2==1
    assert 3141592653%4==1 and 2718281829%2==1
    assert state_at(M)==SEED and state_at(M//2)!=SEED
    assert sum(r['count'] for r in census['rows'])==M-1
    witnesses=0
    for j,r in enumerate(census['rows']):
        assert r['bucket']==j and r['count']==2**29-(j==0)
        first,last=r['from_raw'],r['to_raw']
        x=state_at(first)
        assert x and x//2**29==j
        steps=0
        for t in range(first+1,last+1):
            x=(A*x+C)%M
            if x:steps+=1
            if t<last:assert not x or x//2**29!=j
        assert x==state_at(last) and x and x//2**29==j
        assert steps==r['max_gap']
        witnesses+=1

    stride=2**23
    covers=[]
    all_buckets=2**64-1
    for block in range(M//stride):
        start=block*stride
        x=state_at(start)
        mask=0
        for offset in range(4096):
            if x:mask|=1<<(x//2**29)
            if mask==all_buckets:break
            x=(A*x+C)%M
        else:raise AssertionError(('Uncovered block',block))
        covers.append(offset+1)
    bound=stride+max(covers)
    assert bound<M//2
    # The unique bucket of smaller frequency forces the gap-word period M-1.
    assert gcd(M-1,2**29-1)==1
    result=dict(status='passed',method='independent affine jumps and aligned block cover',
                blocks=len(covers),stride=stride,prefix_lengths=covers,
                largest_cover_prefix=max(covers),independent_global_gap_bound=bound,
                census_gap_witnesses=witnesses,
                census_reported_max_gap=max(r['max_gap'] for r in census['rows']),
                gap_word_period=M-1,output_period=M*(M-1),
                scope='All gap witnesses checked; global sufficient bound independently proved. Exact maximum upper bound comes from the census.')
    (ROOT/'results/shuffle-y-validation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='prefix_lengths'},indent=2))


if __name__=='__main__':main()

"""Exact completions of the mod-5 pattern in TAOCP X443, independently via bits."""
from itertools import combinations
from pathlib import Path
import json
from check_hitori import Board
ROOT=Path(__file__).parent

def complete(m,n,offset):
    board=Board(m,n)
    base=sum(1<<(r*n+c) for r in range(m) for c in range(n) if (r+2*c-offset)%5==0)
    assert board.cover(base,False)
    possible=board.full&~(base|board.neighbors(base));bits=[]
    while possible:
        bit=possible&-possible;possible-=bit;bits.append(bit)
    all_valid=[];hist={};checked=0
    for subset in range(1<<len(bits)):
        extra=sum(bit for j,bit in enumerate(bits) if subset>>j&1);black=base|extra
        checked+=1
        if board.cover(black):
            size=black.bit_count();hist[size]=hist.get(size,0)+1
            all_valid.append(black)
    assert all_valid
    best=min(all_valid,key=int.bit_count)
    return dict(m=m,n=n,offset=offset,base_black=base.bit_count(),
        base=[list(divmod(v,n)) for v in range(m*n) if base>>v&1],
        possible_additions=[list(divmod(bit.bit_length()-1,n)) for bit in bits],
        subsets_checked=checked,hitori_completion_histogram=hist,
        minimum_black=best.bit_count(),bound_numerator=m*n+10,bound_denominator=5,
        bound_violated=5*best.bit_count()>m*n+10,
        minimum_witness=[list(divmod(v,n)) for v in range(m*n) if best>>v&1])

if __name__=='__main__':
    cases=[]
    for m in range(2,10):
        for n in range(m,10):
            rows=[complete(m,n,k) for k in range(5)]
            cases.extend(rows)
    failures=[]
    for m in range(2,10):
        for n in range(m,10):
            rows=[c for c in cases if (c['m'],c['n'])==(m,n)]
            if all(c['bound_violated'] for c in rows):
                failures.append(dict(m=m,n=n,minimum_over_offsets=min(c['minimum_black'] for c in rows)))
    out=dict(cases=cases,failures_for_every_offset=failures,
        method='Enumerate every subset outside the closed neighborhood of the required black set; bitboard flood fill and deletion tests verify minimal connected vertex cover.')
    (ROOT/'results/hitori_sparse.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(cases=len(cases),subsets=sum(c['subsets_checked'] for c in cases),failures=failures)),flush=True)

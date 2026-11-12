"""Check the old-clause timestamp filter in answer 376, p.624."""
from itertools import combinations, product
from pathlib import Path
import json
import random
from check_preprocessing import clauses, eliminate, direct_cores


def strengthenings(f):
    return [(a,b,l) for a in f for b in f if a != b for l in a
            if -l in b and a-{l} <= b-{-l}]


def witness():
    rng=random.Random(624)
    core=frozenset((1,2,3))
    sources={frozenset((9,-1,2,4)),frozenset((-9,3))}
    pool=[c for c in clauses(8) if len(c)==4]
    for attempt in range(10000):
        f=set(rng.sample(pool,26))|sources|{core}
        if any(a<b for a in f for b in f) or strengthenings(f):
            continue
        if any(not any(l in c for c in f) for l in range(-9,10) if l):
            continue
        blocked=[]
        for v in range(1,9):
            new,a,b=eliminate(f,v)
            minimal={c for c in new if not any(d<c for d in new)}
            if len(minimal)<=len(f) or direct_cores(f,v) or direct_cores(f,-v):
                break
            blocked.append({'variable':v,'before':len(f),'after_full_resolution_and_subsumption':len(minimal)})
        else:
            new,a,b=eliminate(f,9)
            target=frozenset((-1,2,3,4))
            if any(a<b for a in new for b in new):
                continue
            if set(strengthenings(new)) != {(core,target,1)}:
                continue
            touched=set().union(*a,*b)-{9,-9}
            count=len(core&touched)
            extra=4*count+2*bool(any(-l in touched for l in core))
            assert touched=={-1,2,3,4} and extra==10
            printed=(-1 in touched and count==len(core)-(1 in touched))
            corrected=(-1 in touched and count==len(core)-(1 not in touched))
            assert not printed and corrected
            return {'attempt':attempt,'clauses':[sorted(c) for c in sorted(f,key=lambda c:tuple(sorted(c)))],
                    'variables_not_eliminable_before_9':blocked,
                    'eliminated_variable':9,'old_clause':sorted(core),
                    'new_clause':sorted(target),'touched_literals':sorted(touched),
                    'SIZE':3,'EXTRA':extra,'printed_filter':printed,'corrected_filter':corrected,
                    'only_available_strengthening':[-1, 'is deleted from the new clause']}
    raise AssertionError('No full-round witness found')


def main():
    total=valid=printed_false_negatives=0
    for size in range(2,7):
        core=set(range(1,size+1))
        for pivot in core:
            # All distinct statuses relevant to the test: the core literals
            # and the complement of the pivot. Other timestamps cannot matter.
            labels=tuple(core)+(-pivot,)
            for bits in product((False,True),repeat=len(labels)):
                touched={l for l,b in zip(labels,bits) if b}
                expected=(-pivot in touched and core-{pivot}<=touched)
                count=len(core&touched)
                printed=(-pivot in touched and count==size-(pivot in touched))
                corrected=(-pivot in touched and count==size-(pivot not in touched))
                assert corrected==expected
                if expected:
                    valid+=1
                    assert not printed
                    printed_false_negatives+=1
                total+=1
    out={'status':'all assertions passed','timestamp_cases':total,
         'valid_pivot_cases':valid,'printed_false_negatives':printed_false_negatives,
         'full_round_witness':witness()}
    (Path(__file__).parent/'results/preprocessing_stamps.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='full_round_witness'},indent=2))
    print('Full-round witness:',len(out['full_round_witness']['clauses']),'clauses; attempt',out['full_round_witness']['attempt'])


if __name__=='__main__':
    main()

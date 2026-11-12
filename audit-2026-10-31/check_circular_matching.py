"""Audit exercise 7.2.2.1-201, especially the even-n exception in answer (b)."""
from itertools import permutations
from pathlib import Path
from algorithm_x import DLX
import json
import time


def lucas(n):
    a,b = 2,1
    for _ in range(n):
        a,b = b,a+b
    return a


def allowed(p):
    n = len(p)
    return all((i-j) % n in (0,1,n-1) for i,j in enumerate(p))


def independent_enum(n):
    return {p for p in permutations(range(n)) if allowed(p)}


def circular_transpositions(n):
    """Enumerate matchings of the cycle and swap the matched neighbors."""
    out = set()
    for mask in range(1 << n):
        used = set()
        p = list(range(n))
        for i in range(n):
            if mask >> i & 1:
                j = (i+1) % n
                if i in used or j in used:
                    break
                used.update((i,j))
                p[i],p[j] = p[j],p[i]
        else:
            out.add(tuple(p))
    return out


def main():
    start = time.monotonic()
    enumerated = []
    n4_derangements = None
    for n in range(3,10):
        actual = independent_enum(n)
        deranged = {p for p in actual if all(i != j for i,j in enumerate(p))}
        shifts = {tuple((i+d) % n for i in range(n)) for d in (-1,1)}
        transpositions = circular_transpositions(n)
        assert len(actual) == lucas(n)+2
        assert len(transpositions) == lucas(n)
        assert not shifts & transpositions
        assert actual == shifts | transpositions
        assert len(deranged) == (2 if n % 2 else 4)
        assert len(actual-deranged) == lucas(n)-(0 if n % 2 else 2)
        if n == 4:
            n4_derangements = [[x+1 for x in p] for p in sorted(deranged)]
        enumerated.append({'n':n,'solutions':len(actual),
                           'no_fixed_point':len(deranged),
                           'at_least_one_fixed_point':len(actual-deranged),
                           'Lucas_number':lucas(n)})

    measured = []
    for n in range(3,25):
        items = [(kind,i) for i in range(n) for kind in ('X','Y')]
        options = [(('X',i),('Y',j)) for i in range(n) for j in range(n)
                   if (i-j) % n in (0,1,n-1)]
        run = DLX(items,options).solve(collect=False)
        assert run.solution_count == lucas(n)+2, (n,run.solution_count)
        assert run.updates == 5*lucas(n+2)+10*n-33, (n,run.updates)
        measured.append({'n':n,'solutions':run.solution_count,'updates':run.updates})
    report = {
        'exercise':'7.2.2.1-201',
        'book_pages':[149,471],
        'finding':'The partition in answer (b) is false for every even n>=4; the total L_n+2 is correct.',
        'counterexample':{'n':4,'derangements':n4_derangements,
                          'actual_with_fixed_point':5,'claimed_with_fixed_point':7},
        'correct_partition':'Two cyclic shifts, plus L_n products of disjoint adjacent transpositions, including the empty product.',
        'correct_partition_by_fixed_points':'Odd n: 2 derangements and L_n with a fixed point. Even n: 4 derangements and L_n-2 with a fixed point.',
        'exhaustive_permutation_results':enumerated,
        'part_c_operation_counts':measured,
        'part_c_status':'Printed formula 5 L_(n+2) + 10 n - 33 passes measured Algorithm X for 3<=n<=24; this is not a general proof.',
        'seconds':round(time.monotonic()-start,3),
    }
    (Path(__file__).parent/'results/circular_matching.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()

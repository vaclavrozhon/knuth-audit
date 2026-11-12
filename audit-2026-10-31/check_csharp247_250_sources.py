"""Small new source checks for C$/247--250; consume accepted results once."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
from itertools import combinations_with_replacement, product
from math import inf
import json
import os
import re
import time
from csharp_spacer import CostDLX
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/csharp247_250'


def read(p):
    return json.loads(Path(p).read_text())


def small_columns(columns):
    # Synthetic column lists test answer248 independently of cost taxation.
    q = CostDLX.__new__(CostDLX)
    q.R = [1, 2, 0]
    q.D = [None, 1, 2]
    q.W = [0, 0, 0]
    q.T = [None, len(columns[0]), len(columns[1])]
    q.stats = Counter()
    for i, costs in enumerate(columns, 1):
        last = i
        for cost in costs:
            p = len(q.D)
            q.D[last] = p
            q.D.append(i)
            q.W.append(cost)
            last = p
    return q


def main():
    assert not (OUT/'source-checked.json').exists()
    start = time.monotonic()
    obs = read(ROOT/'sources/csharp247_250/source-observations.json')
    for p,h in (obs['image_hashes'] | obs['text_hashes']).items():
        assert sha(ROOT/p) == h, p
    for q in read(OUT/'errata-search.json')['files']:
        assert sha(ROOT.parent/q['file']) == q['sha256']
    old = read(ROOT/'results/cost_reductions/verified.json')
    assert len(old['random_cases']) == 1000 and old['online_prefix_checks'] == 157497
    new = read(OUT/'spacer-checked.json')
    assert new['case_count'] == 512
    for p,h in new['source_hashes'].items():
        assert sha(ROOT/p) == h
    # Check the printed example, including every repeated cutoff value.
    costs = [3,1,4,1,5,9,2,6,5,3]
    heap_examples = {}
    for k,expected in [(3,[inf,inf,4,3,3,3,2,2,2,2]),
                       (4,[inf,inf,inf,4,4,4,3,3,3,3])]:
        best, cutoffs, accepted = [inf]*k, [], []
        for c in costs:
            if c < best[-1]:
                accepted.append(c)
                best = sorted(best[:-1]+[c])
            cutoffs.append(best[-1])
        assert cutoffs == expected
        if k == 3:
            assert accepted == [3,1,4,1,2]
        heap_examples[k] = dict(cutoffs=['infinity' if t == inf else t for t in cutoffs],
                                accepted=accepted, best=best)
    # Independent declarative rank: exact cheap length through L, otherwise
    # LEN is the stated conservative estimate; larger minimum cost breaks ties.
    choices = [a for n in range(4) for a in combinations_with_replacement([0,1,3], n)]
    choice_checks = 0
    for columns,theta,L in product(product(choices, repeat=2), [1,2,4], [1,2,10]):
        engine = small_columns(columns)
        actual = [sum(c < theta for c in a) for a in columns]
        estimate = [n if n <= L else len(a) for a,n in zip(columns,actual)]
        expected = None if 0 in actual else min(range(2),key=lambda i:(estimate[i],-columns[i][0],i))+1
        assert engine.choose(theta,L) == expected, (columns,theta,L)
        choice_checks += 1
    assert choice_checks == 3600
    # This printed249 sequence was not checked in the old random prefix suite.
    incoming = [3,1,4,1,5,9,2,6,5,3,5,8]
    bounds = [sum(sorted(incoming[:t]+[0]*(12-t))[1::2]) for t in range(13)]
    first = next(t for t,l in enumerate(bounds) if l >= 16)
    assert first == 7 and bounds[6] == 14 and bounds[7] == 16
    # F150 is a one-word source typo, with a local short type witness.
    typo = {}
    for version,name in [('book','original-173'),('draft','draft-95')]:
        text = (ROOT/f'sources/words_primes231_238/{name}.txt').read_text()
        block = text.split('248.',1)[1].split('249.',1)[0]
        assert re.search(r'LEN\(i\)\s+such\s+items',block)
        typo[version] = dict(source=f'sources/words_primes231_238/{name}.txt',
                             source_sha256=sha(ROOT/f'sources/words_primes231_238/{name}.txt'))
    witness_rows = [('a','b'),('a','c'),('a','d')]
    assert sum('a' in row for row in witness_rows) == 3
    # Keep the known 249 correction separate from a new finding.
    err = (ROOT.parent/'errata/originals/err4f5.textxt').read_text()
    assert 'line 3 of answer 249 (20.01.26)' in err
    assert 'line 4 of answer 249 (21.12.08)' in err
    book = (ROOT/'sources/csharp247_250/original-500.txt').read_text().split('249.',1)[1].split('250.',1)[0]
    draft = (ROOT/'sources/csharp247_250/draft-190.txt').read_text().split('249.',1)[1].split('250.',1)[0]
    assert re.search(r'y\s*←\s*0',book) and not re.search(r'y\s*←\s*0',draft)
    accepted = ['colored_dlx.py','DANCING_LINKS_FOUNDATIONS.md','COLORED_BASICS_NOTES.md',
                'COST_REDUCTION_NOTES.md','check_cost_reductions.py','results/cost_reductions/verified.json',
                'sources/knuth-programs/dlx5.w']
    current = ['csharp_spacer.py','check_csharp_spacer.py','results/csharp247_250/spacer-checked.json',
               'sources/csharp247_250/gondran-lauriere1974.pdf',
               'sources/csharp247_250/source-observations.json','results/csharp247_250/errata-search.json']
    report = dict(at_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,
                  nice=os.getpriority(os.PRIO_PROCESS,0),checker_sha256=sha(__file__),
                  heap_examples=heap_examples,choice248_checks=choice_checks,
                  example249=dict(costs=incoming,lower_bounds=bounds,earliest_bad_prefix=first),
                  f150=dict(versions=typo,witness_options=witness_rows,item='a',LEN=3,
                            correction='such items -> such options',severity='low',scope='editorial'),
                  E108='Both published249 corrections applied in book480; missing in draft184.',
                  accepted_old_tests_rerun=False,
                  accepted_hashes={p:sha(ROOT/p) for p in accepted},
                  current_hashes={p:sha(ROOT/p) for p in current})
    save(OUT/'source-checked.json',report)
    print('PASS:3600 heuristic choices; both heap traces; earliest bad249 prefix7; F150/E108 distinguished.')


if __name__ == '__main__':
    main()

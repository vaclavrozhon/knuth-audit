#!/usr/bin/env python3
"""Compare independent CSP with every possible across tuple on tiny inputs."""
from datetime import datetime, timezone
from itertools import product
import hashlib, json, random
from double_word_tools import OUT, ROOT, geometric_models, down_words
from word_domain_csp import WordCSP, SearchIncomplete


def main():
    rng = random.Random(870090)
    cases = []
    digest = hashlib.sha256()
    for kind, n, p in [('square',2,2),('square',3,3),('left',2,1),('left',2,2),
                      ('left',3,2),('left',3,3),('right',2,1),('right',2,2),
                      ('right',3,2),('right',3,3)]:
        universe = [''.join(x) for x in product('ABC' if n==2 else 'AB', repeat=n)]
        dictionaries = [universe] + [rng.sample(universe,rng.randrange(1,len(universe)+1)) for _ in range(25)]
        for words in dictionaries:
            expected = set(geometric_models(words,kind,p))
            ranks = {w:i for i,w in enumerate(words)}
            reduced = {r for r in expected if (ranks[r[0]] < ranks[down_words(r,kind)[0]] if kind=='square'
                else ranks[r[0]] == min(ranks[w] for w in list(r)+down_words(r,kind)))}
            for symmetry in (False,True):
                csp = WordCSP(words,kind,p,symmetry)
                got = csp.solve(timeout=30)
                assert len(got) == len(set(got))
                assert set(got) == (reduced if symmetry else expected), (kind,p,words,symmetry,got,expected)
                digest.update(json.dumps([kind,p,words,symmetry,sorted(got)]).encode())
                cases.append(dict(kind=kind,n=n,p=p,words=len(words),symmetry=symmetry,models=len(got),nodes=csp.nodes))
    try:
        WordCSP(universe,'square').solve(timeout=1e-15)
        raise AssertionError('deadline incorrectly treated as a completed search')
    except SearchIncomplete:
        pass
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),cases=cases,
        runs=len(cases),complete_model_digest=digest.hexdigest(),timeout_is_not_unsat=True,
        source_sha256={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in ['word_domain_csp.py','check_word_domain_csp.py','double_word_tools.py']})
    (OUT/'csp-small-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:',len(cases),'CSP/permutation model-set comparisons; deadline raises')


if __name__ == '__main__': main()

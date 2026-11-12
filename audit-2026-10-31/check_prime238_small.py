"""Complete small n3 case only; no repeated 5x5 or large 3xn optimization."""
from pathlib import Path
from datetime import datetime, timezone
from math import isqrt, prod
import json
import os
import time
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/words_primes231_238'


def main():
    assert not (OUT/'prime238-n3.json').exists()
    assert os.nice(0) >= 15
    start = time.monotonic()
    primes = [p for p in range(100,1000) if all(p%d for d in range(2,isqrt(p)+1))]
    allowed = set(primes)
    assert len(allowed) == 143
    # Every first-row digit starts a three-digit column; every last-row digit
    # ends a prime >5. These are necessary restrictions, not heuristic pruning.
    first = [p for p in primes if '0' not in str(p)]
    last = [p for p in primes if set(str(p)) <= set('1379')]
    digits = {p: list(map(int,str(p))) for p in primes}
    trials = count = 0
    minimum, maximum = 10**30, -1
    lows, highs = [], []
    for a in first:
        for b in primes:
            for c in last:
                trials += 1
                if a == b or a == c or b == c:
                    continue
                cols = [100*digits[a][j]+10*digits[b][j]+digits[c][j] for j in range(3)]
                if not all(p in allowed for p in cols) or len(set([a,b,c]+cols)) != 6:
                    continue
                count += 1
                price = prod([a,b,c]+cols)
                if price < minimum:
                    minimum, lows = price, []
                if price == minimum:
                    lows.append([str(a),str(b),str(c)])
                if price > maximum:
                    maximum, highs = price, []
                if price == maximum:
                    highs.append([str(a),str(b),str(c)])
    prior = ROOT/'results/prime_squares/verified.json'
    accepted = json.loads(prior.read_text())['238_witnesses']
    assert accepted[0]['rows'] in lows and accepted[0]['product'] == minimum
    assert accepted[5]['rows'] in highs and accepted[5]['product'] == maximum
    save(OUT/'prime238-n3.json', dict(at_utc=datetime.now(timezone.utc).isoformat(), checker_sha256=sha(__file__),
        nice=os.nice(0), wall_seconds=time.monotonic()-start, primes=143, first_row_candidates=len(first),
        last_row_candidates=len(last), tested_row_triples=trials, valid_grids=count, minimum=minimum, maximum=maximum,
        minimum_grids=lows, maximum_grids=highs, complete=True, accepted_evidence={str(prior.relative_to(ROOT)):sha(prior)},
        old_searches_repeated=0, global_n4_to_n7_reproved=False))
    print('PASS prime238 n3:',count,'grids;',trials,'triples;',round(time.monotonic()-start,3),'seconds.')


if __name__ == '__main__':
    main()

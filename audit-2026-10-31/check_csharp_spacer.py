"""Bounded new checks of the literal C$ threshold/undo changes.

No accepted native DLX5 or old prefix test is rerun. Every new instance has
at most ten options, so the independent oracle visits at most 1024 subsets.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import json
import os
import random
import time
from csharp_spacer import CostDLX
from colored_dlx import brute
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/csharp247_250'


def main():
    assert not (OUT / 'spacer-checked.json').exists()
    start = time.monotonic()
    rng = random.Random(202611030247)
    cases = []
    # Empty columns, zero cost, duplicate options, repeated compatible colors.
    fixed = [
        (1, 1, [], []),
        (1, 1, [[(1, 0)], [(1, 0)], [(1, 0)]], [0, 0, 0]),
        (3, 2, [[(1, 0), (3, 1)], [(2, 0), (3, 1)],
                [(2, 0), (3, 2)], [(1, 0)]], [9, 7, 1, 10]),
        # Red first gives cutoff5, blue later costs1+2. At the last
        # primary, cost2 equals TH0=2: the chosen row is not hidden.
        (3, 2, [[(1, 0), (3, 1)], [(1, 0), (3, 2)],
                [(2, 0), (3, 1)], [(2, 0), (3, 2)],
                [(2, 0), (3, 3)]], [0, 1, 5, 2, 0]),
    ]
    for n, primary, rows, prices in fixed:
        for k in [1, 2, 5]:
            cases.append((n, primary, rows, prices, k, 1))
    for _ in range(500):
        primary = rng.randrange(1, 6)
        n = primary + rng.randrange(3)
        rows = []
        for j in range(rng.randrange(1, 11)):
            pp = [i for i in range(1, primary+1) if rng.randrange(2)]
            pp = pp or [rng.randrange(1, primary+1)]
            row = [(i, 0) for i in pp]
            row += [(i, rng.randrange(3)) for i in range(primary+1, n+1)
                    if rng.randrange(2)]
            rng.shuffle(row)
            rows.append(row)
        prices = [rng.choice([0, 1, 2, 3, 7, 20]) for row in rows]
        cases.append((n, primary, rows, prices, rng.randrange(1, 6),
                      rng.choice([1, 2, 10])))
    summary, totals = [], Counter()
    for case, (n, primary, rows, prices, k, lookahead) in enumerate(cases):
        assert time.monotonic() - start < 20, 'bounded check exceeded20seconds'
        models = brute(primary, rows)
        oracle = sorted(sum(prices[j] for j in m) for m in models)[:k]
        engine = CostDLX(n, primary, rows, prices).solve_cost(k, lookahead)
        assert engine.best_costs() == oracle, (case, rows, prices, oracle)
        visited = set()
        for model, cost in engine.accepted:
            assert model in models and model not in visited
            visited.add(model)
            assert cost == sum(prices[j] for j in model)
        totals.update(engine.stats)
        summary.append(dict(case=case, n=n, primary=primary, rows=rows,
                            prices=prices, k=k, lookahead=lookahead,
                            oracle_best_costs=oracle, accepted=engine.accepted,
                            stats=dict(engine.stats)))
    required = ['cutoff_decreased_before_undo', 'chosen_row_not_hidden_by_C4',
                'purify_exact_restorations', 'negative_color_nodes_skipped',
                'LEN_estimate', 'C3_backtrack', 'C5_cutoff']
    assert all(totals[k] for k in required), totals
    report = dict(at_utc=datetime.now(timezone.utc).isoformat(),
                  elapsed_seconds=time.monotonic()-start, nice=os.getpriority(os.PRIO_PROCESS, 0),
                  case_count=len(cases), totals=dict(totals), cases=summary,
                  accepted_old_tests_rerun=False,
                  source_hashes={p:sha(ROOT/p) for p in
                                 ['csharp_spacer.py','check_csharp_spacer.py','colored_dlx.py']})
    save(OUT/'spacer-checked.json', report)
    print(json.dumps({k:v for k,v in report.items() if k not in ['cases','source_hashes']}))


if __name__ == '__main__':
    main()

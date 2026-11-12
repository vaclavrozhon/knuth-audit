"""Exact MPR4 certificate: all720 calls and an independent stopping-set sum."""
from collections import Counter, defaultdict
from datetime import datetime, timezone
from itertools import combinations, permutations
from math import factorial
from pathlib import Path
import json
import os
import time

CARDS = {
    "A": ((1, 2), (3, 5)),
    "B": ((2, 3), (4, 6)),
    "C": ((3, 4), (1, 5)),
    "D": ((1, 4), (2, 6)),
}
SIGMA = {1: 2, 2: 3, 3: 4, 4: 1, 5: 6, 6: 5}


def completion_times(order):
    position = {value: i+1 for i, value in enumerate(order)}
    return {name: min(max(position[x] for x in row) for row in rows)
            for name, rows in CARDS.items()}


def ordered_outcomes():
    # Partition every permutation by its first winning call for each player set.
    distributions = defaultdict(Counter)
    by_time = defaultdict(Counter)
    for order in permutations(range(1, 7)):
        times = completion_times(order)
        for size in range(2, 5):
            for players in combinations("ABCD", size):
                stop = min(times[name] for name in players)
                winners = ''.join(name for name in players if times[name] == stop)
                key = ''.join(players)
                distributions[key][winners] += 1
                by_time[key][str(stop)] += 1
    return distributions, by_time


def stopping_set_outcomes():
    # T is the set before the first win; c is the next call.
    # Every such pair represents |T|! (5-|T|)! full permutations.
    row_sets = {name: [set(row) for row in rows] for name, rows in CARDS.items()}
    distributions = defaultdict(Counter)
    for size in range(2, 5):
        for players in combinations("ABCD", size):
            key = ''.join(players)
            for mask in range(64):
                previous = {v for v in range(1, 7) if mask >> (v-1) & 1}
                if any(row <= previous for name in players for row in row_sets[name]):
                    continue
                for called in set(range(1, 7))-previous:
                    current = previous | {called}
                    winners = ''.join(name for name in players
                                      if any(row <= current for row in row_sets[name]))
                    if winners:
                        distributions[key][winners] += factorial(len(previous))*factorial(5-len(previous))
    return distributions


def prefix_status(prefix, players):
    called = set()
    steps = []
    for value in prefix:
        called.add(value)
        winners = ''.join(name for name in players
                          if any(set(row) <= called for row in CARDS[name]))
        steps.append({"called": value, "prefix": sorted(called), "completed_players": winners})
        if winners:
            return {"steps": steps, "first_winners": winners, "stopping_time": len(steps)}
    return {"steps": steps, "first_winners": "", "stopping_time": None}


def main():
    started = time.perf_counter()
    rotations = {}
    for source, target in zip("ABCD", "BCDA"):
        mapped = {frozenset(SIGMA[x] for x in row) for row in CARDS[source]}
        assert mapped == {frozenset(row) for row in CARDS[target]}
        rotations[source] = target
    perm, by_time = ordered_outcomes()
    sets = stopping_set_outcomes()
    assert dict(perm) == dict(sets)
    assert len(perm) == 11
    assert all(sum(distribution.values()) == 720 for distribution in perm.values())
    assert perm['AB'] == Counter({'A': 336, 'B': 312, 'AB': 72})
    assert perm['AC'] == Counter({'A': 288, 'C': 288, 'AC': 144})
    assert perm['ABC'] == Counter({'A': 168, 'B': 216, 'C': 168,
                                  'AB': 48, 'AC': 72, 'BC': 36, 'ABC': 12})
    for winner, expected in [('A', 120), ('AB', 24), ('AC', 48), ('ABC', 12), ('ABCD', 0)]:
        assert perm['ABCD'][winner] == expected
    examples = [prefix_status([6, 2, 5, 1], 'AB'), prefix_status([1, 3, 2], 'AB')]
    assert [x['first_winners'] for x in examples] == ['A', 'AB']
    # Include impossible winner subsets explicitly as0 in the complete output.
    complete = {}
    for players, distribution in sorted(perm.items(), key=lambda x: (len(x[0]), x[0])):
        complete[players] = {''.join(w): distribution[''.join(w)]
                             for size in range(1, len(players)+1)
                             for w in combinations(players, size)}
    result = {
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "cards": CARDS,
        "number_permutation": SIGMA,
        "card_rotation": rotations,
        "denominator": 720,
        "all_player_sets": complete,
        "first_win_time_counts": {k: dict(sorted(v.items())) for k, v in by_time.items()},
        "examples": examples,
        "independent_stopping_set_sum_agrees_for_all11_player_sets": True,
        "elapsed_seconds": time.perf_counter()-started,
        "execution_nice": os.getpriority(os.PRIO_PROCESS, 0),
        "old_tests_repeated": 0,
    }
    root = Path(__file__).resolve().parent
    (root / 'results/sequential/mpr-004-bingo.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['denominator',
        'independent_stopping_set_sum_agrees_for_all11_player_sets', 'elapsed_seconds', 'execution_nice']}))


if __name__ == '__main__':
    main()

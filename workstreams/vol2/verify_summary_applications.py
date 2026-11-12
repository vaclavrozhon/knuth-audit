"""Bounded implementations and exact models for TAOCP2 exercises3.6-1,3,4.

The saved games are reproducible examples, not independence or quality tests
of the Python pseudorandom source. Probability claims use ideal uniform input.
"""
from collections import Counter
from fractions import Fraction
from pathlib import Path
import json
import random
import sympy as sp

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/summary-applications.json'


def digits(x, base, length):
    out = []
    for _ in range(length):
        x, d = divmod(x, base)
        out.append(d)
    return out


def number(word, base):
    x = 0
    for d in reversed(word):
        x = x * base + d
    return x


def multiply(left, right, base):
    out = [0] * 10
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i+j] += x*y
    for i in range(9):
        q, out[i] = divmod(out[i], base)
        out[i+1] += q
    assert out[-1] < base
    return out


def randi(old, k, base, overflow):
    # CON is represented as five radix-base bytes; high digits discarded.
    multiplier = digits(3141592621, base, 5)
    ax = multiply(digits(old, base, 5), multiplier, base)
    carry = 1009
    for i in range(5):
        carry, ax[i] = divmod(ax[i] + carry, base)
    overflow |= bool(carry)
    overflow = False  # JOV next-instruction clears even a pre-existing toggle.
    new = number(ax[:5], base)  # SLAX5 followed by STA XRAND.
    product = multiply(ax[:5], digits(k, base, 5), base)
    result = number(product[5:], base) + 1
    return new, result, overflow


def craps_step(state, dice):
    total = sum(dice)
    if state == 0:
        if total in (7, 11):
            return 'win'
        if total in (2, 3, 12):
            return 'loss'
        return total
    if total == state:
        return 'win'
    if total == 7:
        return 'loss'
    return state


def game(rng):
    state = 0
    rolls = []
    while isinstance(state, int):
        dice = rng.randrange(1, 7), rng.randrange(1, 7)
        state = craps_step(state, dice)
        comment = 'snake eyes' if dice == (1, 1) else 'the hard way' if dice[0] == dice[1] else 'roll'
        rolls.append({'dice': f'{dice[0]}{dice[1]}', 'comment': comment, 'state': state})
    return {'result': state, 'rolls': rolls}


def shuffle(cards, rng):
    cards = list(cards)
    for i in range(len(cards)-1, 0, -1):
        j = rng.randrange(i+1)
        cards[i], cards[j] = cards[j], cards[i]
    return cards


def clock_patience(deck, ranks, copies):
    # Card labels are ranks0..ranks-1; the last rank plays the role of king.
    assert Counter(deck) == Counter({r: copies for r in range(ranks)})
    piles = [list(deck[p*copies:(p+1)*copies]) for p in range(ranks)]
    pile = ranks-1
    played = []
    while piles[pile]:
        card = piles[pile].pop()
        played.append(card)
        pile = card
    assert pile == ranks-1
    assert len(played) + sum(map(len, piles)) == ranks * copies
    return {'moves': len(played), 'won': len(played) == ranks*copies,
            'unseen_per_pile': list(map(len, piles)), 'revealed_ranks': played}


def multiset_words(ranks, copies):
    counts = [copies] * ranks
    word = []
    def walk():
        if len(word) == ranks*copies:
            yield tuple(word)
        else:
            for r in range(ranks):
                if counts[r]:
                    counts[r] -= 1
                    word.append(r)
                    yield from walk()
                    word.pop()
                    counts[r] += 1
    yield from walk()


def main():
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    def save(key, value):
        data[key] = value
        OUT.write_text(json.dumps(data, indent=2) + '\n')
        print('PASS', key, flush=True)
    if 'mix_randi' not in data:
        tests = 0
        for base in (64, 100):
            m = base**5
            a = 3141592621 % m
            assert a % 4 == 1 and (base != 100 or (a-1) % 5 == 0)
            inverse = pow(a, -1, m)
            states = {0, 1, m-1, *(j*m//64 for j in range(64))}
            states |= {inverse*t % m for t in (0, 1, m-1010, m-1009, m-1)}
            for x in states:
                for k in (1, 2, 4095, 4096, 4999):
                    for overflow in (False, True):
                        new, y, ov = randi(x, k, base, overflow)
                        expected = (3141592621*x + 1009) % m
                        assert new == expected and y == 1 + k*expected//m
                        assert 1 <= y <= k and not ov
                        tests += 1
        save('mix_randi', {'byte_models': [64, 100], 'boundary_cases': tests,
                          'scope': 'Instruction arithmetic with the multiplier reduced modulo word size; no claim about a particular MIXAL assembler diagnostics.'})
    if 'craps' not in data:
        states = [0, 4, 5, 6, 8, 9, 10]
        matrix = sp.eye(7)
        win = sp.zeros(7, 1)
        for i, state in enumerate(states):
            for a in range(1, 7):
                for b in range(1, 7):
                    result = craps_step(state, (a, b))
                    if result == 'win':
                        win[i] += sp.Rational(1, 36)
                    elif result != 'loss':
                        matrix[i, states.index(result)] -= sp.Rational(1, 36)
        chances = matrix.inv()*win
        times = matrix.inv()*sp.ones(7, 1)
        assert chances[0] == sp.Rational(244, 495)
        assert times[0] == sp.Rational(557, 165)
        rng = random.Random(20261102)
        games = [game(rng) for _ in range(10)]
        lines = []
        for i, g in enumerate(games, 1):
            lines.append(f'Game {i}')
            lines.extend(f"{r['dice']} {r['comment']}; {r['state']}" for r in g['rolls'])
        (ROOT / 'results/craps-ten-games.txt').write_text('\n'.join(lines) + '\n')
        save('craps', {'ideal_win_probability': str(chances[0]),
                       'ideal_expected_rolls': str(times[0]),
                       'transition_cases': 252, 'sample_games': games})
    if 'clock_patience' not in data:
        rows = []
        for ranks, copies in ((2, 2), (3, 2), (4, 2), (3, 3)):
            census = Counter()
            for word in multiset_words(ranks, copies):
                result = clock_patience(word, ranks, copies)
                census[result['moves']] += 1
            total = sum(census.values())
            n = ranks*copies
            assert Fraction(census[n], total) == Fraction(1, ranks)
            for t in range(copies, n+1):
                assert Fraction(census[t], total) == Fraction(int(sp.binomial(t-1, copies-1)), int(sp.binomial(n, copies)))
            rows.append({'ranks': ranks, 'copies': copies, 'deals': total, 'stopping_time_counts': dict(census)})
        rng = random.Random(20261103)
        histogram = Counter()
        examples = []
        for _ in range(100):
            cards = shuffle(range(52), rng)
            assert sorted(cards) == list(range(52))
            # Each rank appears four times; suits remain distinct in shuffled ids.
            result = clock_patience([x//4 for x in cards], 13, 4)
            histogram[result['moves']] += 1
            if len(examples) < 3:
                examples.append({'deck_card_ids': cards, **result})
        save('clock_patience', {'exact_small_deals': rows, 'ideal_win_probability': '1/13',
                                'sample_games': 100, 'sample_wins': histogram[52],
                                'sample_stopping_time_counts': dict(histogram), 'sample_examples': examples,
                                'scope': 'Finite uniform-deal proof is independent of the pseudorandom sample; no quality claim from100 trials.'})


if __name__ == '__main__':
    main()

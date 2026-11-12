"""Backtrack37: independent checks of the Eastman/Scholtz distinction.

Scholtz is represented by the odd-first Hall order of Perrin--Reutenauer,
Section4. Recursive Hall membership is checked separately from Melancon's
circular merging algorithm. Eastman is the earlier literal Algorithm O.
"""
from functools import lru_cache
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
from check_eastman import eastman, circular_oracle, primitive

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/commafree'


def order(w):
    return (len(w) % 2 == 0, len(w), w)


def melancon(w):
    blocks = list(w)
    history = [blocks.copy()]
    while len(blocks) > 1:
        keys = list(map(order, blocks))
        minimum = min(keys)
        i = next(i for i, k in enumerate(keys)
                 if k == minimum and k < keys[(i+1) % len(keys)])
        if i+1 < len(blocks):
            blocks[i:i+2] = [blocks[i]+blocks[i+1]]
        else:
            blocks = [blocks[-1]+blocks[0]]+blocks[1:-1]
        history.append(blocks.copy())
    return blocks[0], history


@lru_cache(None)
def hall_trees(w):
    """All binary parses satisfying the defining Hall conditions, Section2.1.

No greedy merging, circular word operations, dips, or Eastman code is used.
For a composite (u,v), u<v and v is a letter or left(v)<=u.
"""
    if len(w) == 1:
        return (w,)
    answer = []
    for k in range(1, len(w)):
        u, v = w[:k], w[k:]
        if order(u) >= order(v):
            continue
        for a in hall_trees(u):
            for b in hall_trees(v):
                if isinstance(b, str) or order(foliage(b[0])) <= order(u):
                    answer.append((a, b))
    return tuple(answer)


def foliage(tree):
    return tree if isinstance(tree, str) else foliage(tree[0])+foliage(tree[1])


def main():
    results = []
    examples = [('Perrin-Reutenauer Example17', 'a'*12+'c'+'a'*10+'c'+'aac'+'aab'+'aac', 13),
                ('Additional binary example, standard radix tie order',
                 ('1'*7+'01')*2+'101'+'001'+'101', 9)]
    for name, w, cut in examples:
        assert primitive(w)
        e, eh = eastman(w)
        assert e == w and circular_oracle(w) == (e, eh)
        s, sh = melancon(w)
        assert s == w[cut:]+w[:cut] and s != e
        assert hall_trees(e) == ()
        assert len(hall_trees(s)) == 1
        members = []
        for k in range(len(w)):
            rot = w[k:]+w[:k]
            assert eastman(rot)[0] == e
            assert circular_oracle(rot)[0] == e
            assert melancon(rot)[0] == s
            if hall_trees(rot):
                members.append(rot)
        assert members == [s]
        results.append(dict(name=name, length=len(w), eastman=e, scholtz=s,
                            scholtz_rotation=cut, eastman_boundaries=eh,
                            scholtz_merges=sh, hall_tree=hall_trees(s)[0],
                            all_rotations_checked=len(w)))
    # The construction starts already finished at n=1; the low-level O loop
    # is a nontrivial-case routine. Record the convention, not a new error.
    for letter in ('a', 'b', 'c'):
        assert circular_oracle(letter) == (letter, [])
    files = ['errata/originals/err4b.textxt', 'errata/originals/err4f5.textxt',
             'errata/text/all4b.txt', 'errata/text/all4f5.txt']
    errata = [dict(file=p, sha256=hashlib.sha256((ROOT.parent/p).read_bytes()).hexdigest())
              for p in files]
    result = dict(verified_at_utc=datetime.now(timezone.utc).isoformat(), examples=results,
                  singleton_convention='identity, zero rounds before entering O2',
                  errata_checked=errata,
                  errata_result='No correction to the Scholtz identification. Nearby known changes concern O3/O4/O5 and recurrence37c.',
                  source='arXiv:1609.05438, Sections2.1,4,6,8 and Example17')
    (OUT/'scholtz-verified.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(verified=True, examples=[(r['length'],r['scholtz_rotation']) for r in results])))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""DLX75--76: independent Latin-table and exact-cover enumerations."""
from collections import Counter
from itertools import combinations, permutations, product
from math import comb
import gzip
import hashlib
import json
from dlx1_audit_tools import ROOT, decode_rows, input_text, run, sha

OUT = ROOT/'results/gropes75'
TABLES = [tuple(map(int, s)) for s in [
    '0123103223013210', '0321321021031032', '0132102332102301',
    '0231310213202013', '0312213030211203']]


def valid(t, n):
    assert len(t) == n*n and all(0 <= v < n for v in t)
    assert all(t[x*n+t[y*n+x]] == y for x in range(n) for y in range(n))
    assert all(t[t[x*n+y]*n+x] == y for x in range(n) for y in range(n))
    assert all(len(set(t[x*n:x*n+n])) == n for x in range(n))
    assert all(len({t[y*n+x] for y in range(n)}) == n for x in range(n))


def latin_tables(n):
    """Enumerate row permutations with column uniqueness, not XC options.

    Reject a prefix only when it violates an already fully assigned identity.
    Every Latin table is in this unlabelled-row-free search space.
    """
    perms = list(permutations(range(n)))
    rows, cols, result = [], [set() for _ in range(n)], set()
    def visit():
        r = len(rows)
        if r == n:
            result.add(tuple(v for row in rows for v in row))
            return
        for row in perms:
            if any(v in cols[i] for i, v in enumerate(row)):
                continue
            rows.append(row)
            okay = True
            for x in range(r+1):
                for y in range(r+1):
                    if rows[x][rows[y][x]] != y:
                        okay = False
                        break
                if not okay:
                    break
            if okay:
                for i, v in enumerate(row):
                    cols[i].add(v)
                visit()
                for i, v in enumerate(row):
                    cols[i].remove(v)
            rows.pop()
    visit()
    return result


def model(n, mode):
    if mode == 'commutative':
        pairs = [(x,y) for x in range(n) for y in range(x,n)]
        triples = ([(x,x,x) for x in range(n)] +
                   [(x,x,y) for x in range(n) for y in range(x+1,n)] +
                   [(x,y,y) for x in range(n) for y in range(x+1,n)] +
                   list(combinations(range(n),3)))
    else:
        start = 1 if mode.startswith('loop') else 0
        pairs = [(x,y) for x in range(start,n) for y in range(start,n)
                 if mode not in ('idempotent','loop') or x != y]
        if mode == 'full':
            triples = ([(x,x,x) for x in range(n)] +
                       [(x,x,y) for x in range(n) for y in range(x+1,n)] +
                       [(x,y,z) for x in range(n) for y in range(x+1,n)
                        for z in range(x+1,n)])
        else:
            triples = [(x,y,z) for x in range(start,n) for y in range(x+1,n)
                       for z in range(x+1,n) if y != z]
    indexes = {p:i+1 for i,p in enumerate(pairs)}
    rows = []
    for x,y,z in triples:
        row = {(x,y),(y,z),(z,x)}
        if mode == 'commutative':
            row = {tuple(sorted(p)) for p in row}
        rows.append(tuple(sorted(indexes[p] for p in row)))
    assert len(set(rows)) == len(rows)
    return pairs, rows, triples


def decode_table(n, mode, triples, solution):
    a = [-1]*(n*n)
    def put(x,y,z):
        assert a[n*x+y] in (-1,z)
        a[n*x+y] = z
    if mode == 'idempotent':
        for x in range(n):
            put(x,x,x)
    if mode.startswith('loop'):
        for x in range(n):
            put(0,x,x); put(x,0,x); put(x,x,0)
    for r in solution:
        x,y,z = triples[r]
        for u,v,w in [(x,y,z),(y,z,x),(z,x,y)]:
            put(u,v,w)
            if mode == 'commutative':
                put(v,u,w)
    valid(a,n)
    return tuple(a)


def cover_models(count, rows):
    """Independent immutable bit-mask cover search, no dancing links."""
    masks = [sum(1 << (i-1) for i in row) for row in rows]
    incidence = [[r for r,row in enumerate(rows) if i+1 in row]
                 for i in range(count)]
    result = set()
    def visit(left, chosen):
        if not left:
            result.add(tuple(sorted(chosen)))
            return
        choices = None
        for i in range(count):
            if left >> i & 1:
                eligible = [r for r in incidence[i] if masks[r] & left == masks[r]]
                if choices is None or len(eligible) < len(choices):
                    choices = eligible
                    if not choices:
                        return
        for r in choices:
            visit(left ^ masks[r], chosen+(r,))
    visit((1 << count)-1, ())
    return result


def relabel(t,n,p):
    a = [None]*(n*n)
    for x in range(n):
        for y in range(n):
            a[n*p[x]+p[y]] = p[t[n*x+y]]
    return tuple(a)


def save_tables(name,tables):
    data = json.dumps(sorted(tables), separators=(',',':')).encode()+b'\n'
    path = OUT/(name+'.json.gz')
    path.write_bytes(gzip.compress(data,mtime=0))
    return dict(path=str(path.relative_to(ROOT)),sha256=sha(path),
                table_count=len(tables),uncompressed_sha256=hashlib.sha256(data).hexdigest())


def group_checks():
    records = []
    for size in range(1,7):
        ps = list(permutations(range(size)))
        # S_6 has 76 involutions; all 720^2 pairs for all would be excessive.
        if size > 4:
            break
        ident = tuple(range(size))
        def mul(a,b):
            return tuple(a[b[i]] for i in range(size))
        def inv(a):
            return tuple(a.index(i) for i in range(size))
        tested = 0
        for alpha in ps:
            if mul(alpha,alpha) != ident:
                continue
            def op(x,y):
                return mul(mul(mul(mul(alpha,inv(x)),alpha),inv(y)),alpha)
            for x,y in product(ps,repeat=2):
                assert op(x,op(y,x)) == y
                tested += 1
        records.append(dict(group='S'+str(size),order=len(ps),identity_checks=tested))
    for n in range(1,41):
        for alpha in range(n):
            for x,y in product(range(n),repeat=2):
                op = lambda a,b:(-a-b+alpha)%n
                assert op(x,op(y,x)) == y
    return dict(noncommutative=records,cyclic_groups_all_alpha_up_to=40,
                scope='Finite regression checks supplement the general symbolic proof in GROPES_NOTES.md.')


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    data = dict(source_sha256=sha(__file__),cases=[])
    direct = {}
    for n in range(1,6):
        direct[n] = latin_tables(n)
        for t in direct[n]:
            valid(t,n)
        print('Direct Latin enumeration',n,len(direct[n]),flush=True)
    for t in TABLES:
        valid(t,4)
        assert t in direct[4]
    assert TABLES[0] == tuple(x^y for x,y in product(range(4),repeat=2))
    assert TABLES[1] == tuple((-x-y)%4 for x,y in product(range(4),repeat=2))
    swap12 = (0,2,1,3)
    assert relabel(TABLES[1],4,swap12) == TABLES[2]
    for a,b in combinations(range(4),2):
        p = list(range(4)); p[a],p[b] = p[b],p[a]
        assert relabel(TABLES[3],4,p) == TABLES[4]
    orbits = [{relabel(t,4,p) for p in permutations(range(4))}
              for t in [TABLES[0],TABLES[2],TABLES[4]]]
    assert [len(s) for s in orbits] == [4,12,2]
    assert set.union(*orbits) == direct[4] and sum(map(len,orbits)) == 18
    functions = []
    for t in TABLES[3:]:
        f = t[:4]
        assert t == tuple(x ^ f[x^y] for x,y in product(range(4),repeat=2))
        assert [f[x^f[x]] for x in range(4)] == list(range(4))
        functions.append(dict(f=f,xor_arguments=[x^f[x] for x in range(4)],
          ordinary_arguments=[x+f[x] for x in range(4)],
          mod4_values=[f[(x+f[x])%4] for x in range(4)]))
    data['printed_tables'] = dict(tables=TABLES,isomorphism_class_sizes=[4,12,2],
      all_six_transpositions_swap_last_two=True,functions=functions)
    for n in range(1,7):
        for mode in ['full','idempotent','commutative','loop','loop_literal']:
            pairs, rows, triples = model(n,mode)
            if mode == 'full':
                assert len(rows) == n+(n**3-n)//3
            elif mode == 'idempotent':
                assert len(rows) == 2*comb(n,3) if n >= 3 else not rows
            elif mode.startswith('loop'):
                assert len(rows) == 2*comb(n-1,3) if n >= 4 else not rows
            else:
                assert len(pairs) == comb(n+1,2)
                assert len(rows) == n+2*comb(n,2)+(comb(n,3) if n>=3 else 0)
            solutions = cover_models(len(pairs), rows)
            if pairs:
                names = [f'x{x}y{y}' for x,y in pairs]
                stats, stdout = run(OUT,f'n{n}-{mode}',input_text(names,rows),models=True)
                native = decode_rows(stdout,names,rows)
                assert native == solutions and len(native) == stats['solutions']
            else:
                assert solutions == {()}
                stats = dict(solutions=1,scope='Empty-universe XC has the single empty solution; native DLX1 requires a nonempty header.')
            if mode == 'loop_literal' and n >= 2:
                assert not solutions
                assert all(not any(i+1 in row for row in rows)
                           for i,(x,y) in enumerate(pairs) if x == y)
                tables = set()
            else:
                tables = {decode_table(n,mode,triples,s) for s in solutions}
                assert len(tables) == len(solutions)
                if n in direct:
                    expected = direct[n]
                    if mode == 'idempotent':
                        expected = {t for t in expected if all(t[x*n+x] == x for x in range(n))}
                    elif mode == 'commutative':
                        expected = {t for t in expected if all(t[x*n+y] == t[y*n+x] for x,y in product(range(n),repeat=2))}
                    elif mode.startswith('loop'):
                        expected = {t for t in expected if all(t[x] == t[x*n] == x for x in range(n))}
                    assert tables == expected
                if mode == 'full':
                    spectrum = Counter(sum(t[x*n+x] == x for x in range(n)) for t in tables)
                    expected = {k for k in range(n+1) if (k-n*n)%3 == 0 and (n,k) != (6,6)}
                    assert set(spectrum) == expected
                    data.setdefault('idempotent_spectrum',{})[n] = dict(sorted(spectrum.items()))
            data['cases'].append(dict(n=n,mode=mode,items=len(pairs),options=len(rows),
              native=stats,models=save_tables(f'n{n}-{mode}-tables',tables)))
            print('XC',n,mode,len(solutions),flush=True)
    for n in range(1,101):
        for mode in ['full','idempotent','commutative','loop']:
            # Counting formulas checked without materializing the O(n^3) rows.
            if mode == 'full':
                assert n+comb(n,2)+sum(i*i for i in range(n)) == n+(n**3-n)//3
    data['group_constructions'] = group_checks()
    data['counterexample_76c'] = dict(n=2,table=[0,1,1,0],
      literal_remaining_items=['11'],literal_options=[],corrected_items=[],corrected_options=[])
    data['scope'] = 'Complete labelled table sets through n=5 from independent Latin enumeration, and through n=6 from independent mask and original DLX1 cover searches; general proofs are separate.'
    (OUT/'check.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PASS: all tables, orbit classes, constructions and literal/corrected models',flush=True)


if __name__ == '__main__':
    main()

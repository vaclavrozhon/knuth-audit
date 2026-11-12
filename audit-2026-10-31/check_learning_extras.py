"""Check SAT55,58,60,61 independently of printed learning examples."""
from itertools import product
from pathlib import Path
import json, subprocess
from fractions import Fraction
from itertools import combinations
from pysat.card import CardEnc, EncType
from pysat.solvers import Solver
from check_learning_dnf import encode, decode, sha

ROOT = Path(__file__).parent
OUT = ROOT / 'results/learning_dnf'
CHECKER = '/tmp/knuth-drat-trim/drat-trim'


def certified(name, clauses):
    path = OUT / name
    top = max(abs(lit) for clause in clauses for lit in clause)
    cnf = path.with_suffix('.cnf')
    cnf.write_text(f'p cnf {top} {len(clauses)}\n' +
                   ''.join(' '.join(map(str, c)) + ' 0\n' for c in clauses))
    with Solver(name='g4', bootstrap_with=clauses, with_proof=True) as solver:
        sat = solver.solve()
        out = {'status': 'SAT' if sat else 'UNSAT', 'variables': top,
               'clauses': len(clauses), 'cnf_sha256': sha(cnf)}
        if sat:
            return out, solver.get_model()
        proof = path.with_suffix('.drat')
        proof.write_text('\n'.join(solver.get_proof()) + '\n')
    r = subprocess.run([CHECKER, str(cnf), str(proof)], text=True, capture_output=True)
    path.with_suffix('.verification.txt').write_text(r.stdout + r.stderr)
    assert r.returncode == 0 and 's VERIFIED' in r.stdout, r.stdout + r.stderr
    out.update(proof_sha256=sha(proof), proof_verified=True)
    return out, None


def evaluate(terms, point):
    return any(all(point[abs(v)-1] == int(v > 0) for v in term) for term in terms)


def inclusion_probability(terms):
    """Exact inclusion-exclusion on conjunctions, independent of truth tables."""
    probability = Fraction(0)
    for length in range(1,len(terms)+1):
        for subset in combinations(terms,length):
            literals = {v for term in subset for v in term}
            if literals & {-v for v in literals}: continue
            probability += (-1)**(length+1) * Fraction(1, 2**len(literals))
    return probability


def main():
    data = json.loads((ROOT / 'results/learning_table_data.json').read_text())
    pos = [tuple(map(int,w)) for w in data['positive_words_pi'][:16]]
    neg = [tuple(map(int,w)) for w in data['negative_words_e'][:16]]
    _, clauses, p, q = encode(pos, neg, 4)
    clauses.extend([[-v] for row in q for v in row])
    monotone, model = certified('monotone-increasing-four', clauses)
    assert model is None

    base = data['dnf_witnesses']['eq27']
    examples = {
        '32': [[4,-7,-12],[-6,8,-11,14,20],[-9,-12,18,-19],[-13,-16,-17,19]],
        '64': [[2,-13,-15,19],[-3,-9,-19,-20],[-6,-10,-12],[-8,10,-12]],
    }
    differences = {}
    for name, terms in examples.items():
        support = sorted({abs(v) for t in base + terms for v in t})
        count = 0
        for bits in product((0,1), repeat=len(support)):
            point = [0] * 20
            for j,b in zip(support,bits): point[j-1] = b
            count += evaluate(base,point) != evaluate(terms,point)
        differences[name] = {'support':support, 'differing_assignments':count,
                             'total_assignments': 1 << len(support)}
        left, right = inclusion_probability(base), inclusion_probability(terms)
        intersection = inclusion_probability([a+b for a in base for b in terms])
        exact = left + right - 2*intersection
        assert exact == Fraction(count,1 << len(support))
        differences[name].update(left_probability=str(left),right_probability=str(right),
                                  intersection_probability=str(intersection),xor_probability=str(exact))
    assert differences['32']['differing_assignments'] * (1 << 18) == 102752 * differences['32']['total_assignments']
    assert differences['64']['differing_assignments'] * (1 << 11) == 402 * differences['64']['total_assignments']

    # Every satisfiable term in an equivalent DNF must be an implicant.
    # Enumerate all implicants, including nonprime ones, on the eight variables.
    support = sorted({abs(v) for t in base for v in t})
    points = list(product((0,1), repeat=len(support)))
    assignments = []
    for bits in points:
        point = [0] * 20
        for j,b in zip(support,bits): point[j-1] = b
        assignments.append(point)
    truth = sum(1 << i for i,x in enumerate(assignments) if evaluate(base,x))
    literal_masks = {}
    for j in support:
        for sign in [-1,1]:
            literal_masks[sign*j] = sum(1 << i for i,x in enumerate(assignments)
                                        if x[j-1] == int(sign > 0))
    implicants = []; covers = []
    full = (1 << len(assignments)) - 1
    for cube in product((-1,0,1), repeat=len(support)):
        term = tuple(j * (1 if bit else -1) for j,bit in zip(support,cube) if bit != -1)
        mask = full
        for lit in term: mask &= literal_masks[lit]
        if mask and not mask & ~truth:
            implicants.append(term); covers.append(mask)
    count = len(implicants)
    clauses = [[j+1 for j,c in enumerate(covers) if c >> i & 1]
               for i in range(len(assignments)) if truth >> i & 1]
    clauses.extend(CardEnc.atmost(list(range(1,count+1)), bound=4,
                                 encoding=EncType.seqcounter).clauses)
    original = [implicants.index(tuple(sorted(t, key=abs)))+1 for t in base]
    clauses.append([-i for i in original])
    uniqueness, model = certified('four-term-unique-representation', clauses)
    if model is not None:
        uniqueness['alternative'] = [implicants[i-1] for i in model if 1 <= i <= count]
    assert model is None, uniqueness
    # A private positive point for each original term rules out introducing
    # any of the twelve irrelevant variables after projection to this support.
    private = []
    for term in base:
        others = [t for t in base if t != term]
        witness = next(x for x in assignments if evaluate([term],x) and not evaluate(others,x))
        private.append(''.join(map(str,witness)))
    uniqueness.update(implicants=count, positive_points=truth.bit_count(),
                      support=support, private_witnesses=private)

    # Answer58: raw parameter choices per term are 4**N before, 3**N after.
    ratios = [{'M':m,'N':n,'before':4**(m*n),'after':3**(m*n)}
              for m,n in product(range(1,5),range(1,5))]
    results = {'monotone_increasing_four':monotone, 'answer60':differences,
               'answer61':uniqueness, 'answer58_raw_parameter_counts':ratios}
    (OUT / 'extras.json').write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))


if __name__ == '__main__': main()

"""Check the fixed five-step witness against all original transition clauses."""
import itertools
import json
from pathlib import Path

# Each state is (Alice program counter, Bob program counter, light).
states = [(0, 0, 0), (1, 0, 0), (2, 0, 0), (3, 0, 1), (3, 1, 1), (3, 3, 1)]
bumps = [1, 1, 1, 0, 0]
failures = []
modified_count = 0
for t, (old, new, alice) in enumerate(zip(states, states[1:], bumps)):
    a, b, light = old
    aa, bb, light2 = new
    A = [a == k for k in range(5)]; B = [b == k for k in range(5)]
    AA = [aa == k for k in range(5)]; BB = [bb == k for k in range(5)]
    clauses = []
    for k in range(5):
        clauses += [('hold-A', (bool(alice), not A[k], AA[k])),
                    ('hold-B', (not alice, not B[k], BB[k]))]
    for name, guard, S, SS in [('A', not alice, A, AA), ('B', bool(alice), B, BB)]:
        clauses += [(name+'-maybe', (guard, not S[0], SS[0], SS[1])),
                    (name+'-wait', (guard, not S[1], not light, SS[1])),
                    (name+'-advance', (guard, not S[1], bool(light), SS[2])),
                    (name+'-set1-state', (guard, not S[2], SS[3])),
                    (name+'-set1-value', (guard, not S[2], bool(light2))),
                    (name+'-critical', (guard, not S[3], SS[4])),
                    (name+'-set0-state', (guard, not S[4], SS[0])),
                    (name+'-set0-value', (guard, not S[4], not light2)),
                    (name+'-hold-light-down', (guard, bool(light), S[2], S[4], not light2)),
                    (name+'-hold-light-up', (guard, not light, S[2], S[4], bool(light2)))]
    assert len(clauses) == 30
    for name, lits in clauses:
        if not any(lits): failures.append({'t': t, 'clause': name})
        if name == 'B-wait':
            continue  # precisely the deletion suggested in answer 92
        if name == 'B-maybe':
            lits = (bool(alice), not B[0], BB[1])
        assert any(lits), (t, name)
        modified_count += 1
    # Twenty at-most-one clauses at each new time.
    for S in [AA, BB]:
        assert sum(S) == 1
        for i, j in itertools.combinations(range(5), 2):
            assert not S[i] or not S[j]

assert failures == [{'t': 4, 'clause': 'B-wait'}]
assert len(set(states)) == len(states)
assert states[0] == (0, 0, 0) and states[-1][:2] == (3, 3)
# The retained guard, with only its successor literal removed, rejects the jump.
assert not (bumps[4] or states[4][1] != 1 or not states[4][2])

out = {'states': states, 'alice_bumps': bumps, 'all_states_distinct': True,
       'original_transition_clauses_evaluated': 150,
       'original_unsatisfied_clauses': failures,
       'modified_transition_clauses_satisfied': modified_count,
       'at_most_one_clauses_satisfied': 100,
       'repair': 'Remove B1_(t+1) from the waiting clause, preserving its guard.'}
p = Path(__file__).parent / 'results/bookwise-sat92.json'
p.write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out))

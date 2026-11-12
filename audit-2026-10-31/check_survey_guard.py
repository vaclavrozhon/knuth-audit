"""Literal Algorithm S trace for the legal input (x) AND (not x)."""
from fractions import Fraction as Q
from pathlib import Path
import json

# S1 allows these draws; default N0=5, epsilon=.01. Reinforcement stays0.
eta=[Q(1,2),Q(1,2)];i=0;trace=[]
for _ in range(2):
    # S2 skips S3 while i<N0. S5 computes the two flexibility coefficients.
    assert i<5
    pi=[1-v for v in eta]
    # In S6, each unit clause sends the empty product, equal to1.
    new=[Q(1),Q(1)];delta=max(abs(a-b) for a,b in zip(eta,new));eta=new
    trace.append(dict(i=i,pi=list(map(str,pi)),eta=list(map(str,eta)),delta=str(delta),S3_visited=False))
    if delta>=Q(1,100):i+=1
    else:
        denominator=pi[0]+pi[1]-pi[0]*pi[1]
        assert denominator==0
        trace[-1]['next_step']='S8, with undefined 0/0 field'
        break
else:raise AssertionError('Expected S8 before S3')

# This is an open set of random initial draws, not an isolated event of
# probability zero: if either initial eta<=.99, the first delta>=.01,
# and the next sweep has pi=(0,0),delta=0. All such draws reach S8 at i=1.
checked=0
for a in range(20):
    for b in range(20):
        assert max(1-Q(a,20),1-Q(b,20))>=Q(1,100)
        checked+=1

# The description in answer362 checks new unit clauses but not empty ones.
# Its initial list already contains both literals in this example.
clauses=[{1},{-1}];pending=[1,-1];empty_trace=[]
while pending:
    literal=pending.pop(0);clauses=[C-{ -literal } for C in clauses if literal not in C]
    for C in clauses:
        if len(C)==1:
            l=next(iter(C));assert -l not in pending
            if l not in pending:pending.append(l)
    empty_trace.append(dict(literal=literal,clauses=[sorted(C) for C in clauses],pending=pending.copy()))
assert clauses==[set()]
result=dict(F046='Guard pi_l=pi_not_l=0 must precede S6/S8; the only guard in S3 can be bypassed.',
            algorithm_S_trace=trace,initial_draw_grid=checked,
            answer362_trace=empty_trace,
            proposed_fix='After S5 terminate unsuccessfully if either polarity pair has both flexibilities zero; also reject conflicting initial units in362.')
Path('results/survey_guard.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

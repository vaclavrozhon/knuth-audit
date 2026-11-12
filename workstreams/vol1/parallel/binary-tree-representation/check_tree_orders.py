"""Targeted checks for exercises 6 and 8; the main proofs are structural."""
import sys
sys.dont_write_bytecode=True
from check_trees import *

def ordinary(b):
    return (b[0],tuple(ordinary(c) for c in b[1:] if c is not None))
def binary_key(b):
    return (0,) if b is None else (1,b[0],binary_key(b[1]),binary_key(b[2]))
def assign(t,values):return (next(values),tuple(assign(c,values) for c in t[1]))

if __name__=='__main__':
    n6=0
    for n in range(1,9):
        for s in shapes(n):
            b=label(s);converted=binary((ordinary(b),))
            assert bp(b,'pre')==bp(converted,'pre') and bp(b,'post')==bp(converted,'in');n6+=1
    ts=[]
    for n in range(1,5):
        for s in shapes(n-1):
            base=(0,forest(label(s)))
            ts += [assign(base,iter(values)) for values in product([0,1],repeat=n)]
    for a,b in product(ts,repeat=2):
        assert (a<=b)==(binary_key(binary((a,)))<=binary_key(binary((b,))))
    result={'exercise6_binary_trees':n6,'exercise8_labelled_trees':len(ts),'exercise8_comparisons':len(ts)**2}
    (HERE/'results/tree-orders.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))

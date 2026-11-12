"""Isolated check of the stated positive-tag sentinel contract in answer 27."""
import json
import sys
from pathlib import Path
sys.dont_write_bytecode = True
from buddy import Buddy, memory_of, execute, number, HEAD

results = []
for b in range(64, 101):
    for capacity in (1, 2):
        state = Buddy(capacity)
        while state.reserve(0)[0] is not None:
            pass
        good = memory_of(state, b)
        bad = list(good)
        bad[HEAD+state.m+1] = number(0, b)  # positive TAG; unspecified fields zero
        _, allocated, _, _, _ = execute(bad, 0, b=b, mode='original')
        _, expected, _, _, _ = execute(good, 0, b=b, mode='original')
        assert allocated == 0 and expected is None
        results.append(dict(radix=b, capacity=capacity, already_reserved=sorted(state.used),
                            positive_zero_sentinel_result=allocated,
                            self_linked_sentinel_result=expected))
root = Path(__file__).parent
(root/'results'/'sentinel-minimal.json').write_text(json.dumps(results, indent=2)+'\n')
layers = ['all1-prepre', 'all1-pre', 'all1', 'err1']
terms = ['sentinel', 'TLNKF', 'TLINKF', 'J4NN', 'LD4N', 'zero']
search = []
for layer in layers:
    path = root.parents[3]/'errata'/'text'/(layer+'.txt')
    text = path.read_text()
    # Full term hits are navigation evidence; all entries at 443/611/612 are
    # separately inventoried and their original images have been read.
    lines = text.splitlines()
    for line, value in enumerate(lines):
        if any(term.lower() in value.lower() for term in terms):
            search.append(dict(layer=layer, line=line+1,
                               context='\n'.join(lines[max(0,line-2):line+3])))
(root/'results'/'sentinel-errata-terms.json').write_text(json.dumps(search, indent=2)+'\n')
print(json.dumps(dict(cases=len(results), result='positive-zero sentinel duplicates address zero')))

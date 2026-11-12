#!/usr/bin/env python3
"""Accept the last completed convex count without repeating enumerations."""
from datetime import datetime, timezone
import json
from dlx1_audit_tools import ROOT, sha, statistics, validated_binary


def main():
    out=ROOT/'results/convex68'
    state=json.loads((out/'counts.json').read_text())
    assert state['status']=='verified'
    assert state['source_sha256']==sha(ROOT/'run_convex68_counts.py')
    assert state['cpp_sha256']==sha(ROOT/'jigsaw_count.cc')
    assert state['binary_sha256']==sha(state['binary'])
    assert state['dlx1_sha256']==sha(validated_binary())
    label='n9-no-square';case=state['cases'][label]
    assert case['independent_counts_equal'] and case['expected']==5406376
    for method,record in case['methods'].items():
        assert record['status']=='finished'
        inp=out/(label+('.dlx' if method=='dlx1' else '.masks'))
        assert sha(inp)==record['input_sha256']
        assert sha(out/f'{label}-{method}.out')==record['stdout_sha256']
        assert sha(out/f'{label}-{method}.log')==record['stderr_sha256']
        computed=statistics((out/f'{label}-{method}.log').read_text()) if method=='dlx1' else json.loads((out/f'{label}-{method}.out').read_text())
        assert computed==record['output'] and computed['solutions']==5406376
    answer=case['methods']['dlx1']['output']
    assert sum(answer['profile'])==answer['nodes']==83027265
    for name,other in state['cases'].items():
        assert other['independent_counts_equal'],name
        assert all(m['status']=='finished' and m['output']['solutions']==other['expected'] for m in other['methods'].values()),name
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),status='verified',case=case,
        full_count_state_sha256=sha(out/'counts.json'),source_sha256=sha(__file__),
        original_sources=dict(wrapper=state['source_sha256'],mask_solver=state['cpp_sha256']),
        complete_counts={name:item['expected'] for name,item in state['cases'].items()},
        scope='Last pending independent full count5406376 verified; native83027265 nodes and complete profile. All count jobs terminal. Combine with already checked general proof, full placements, symmetries and bibliography to close exercise68.')
    (out/'final-verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: final n9-no-square count5406376; native83027265 nodes; all convex count jobs complete')


if __name__=='__main__':main()

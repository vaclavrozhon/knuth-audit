#!/usr/bin/env python3
"""Accept the completed n9 count; do not rerun either enumeration."""
from datetime import datetime,timezone
import json
from dlx1_audit_tools import ROOT,sha,statistics,validated_binary


def main():
    out=ROOT/'results/convex68'
    state=json.loads((out/'counts.json').read_text());case=state['cases']['n9']
    assert state['source_sha256']==sha(ROOT/'run_convex68_counts.py')
    assert state['cpp_sha256']==sha(ROOT/'jigsaw_count.cc')
    assert state['binary_sha256']==sha(state['binary'])
    assert state['dlx1_sha256']==sha(validated_binary())
    assert case['independent_counts_equal'] and case['expected']==8113709
    for method,record in case['methods'].items():
        assert record['status']=='finished'
        src=out/('n9.dlx' if method=='dlx1' else 'n9.masks')
        assert sha(src)==record['input_sha256']
        assert sha(out/f'n9-{method}.out')==record['stdout_sha256']
        assert sha(out/f'n9-{method}.log')==record['stderr_sha256']
        computed=statistics((out/f'n9-{method}.log').read_text()) if method=='dlx1' else json.loads((out/f'n9-{method}.out').read_text())
        assert computed==record['output'] and computed['solutions']==8113709
    result=case['methods']['dlx1']['output']
    assert sum(result['profile'])==result['nodes']==111286419
    report=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),status='verified',case=case,
      source_sha256=sha(__file__),cpp_sha256=state['cpp_sha256'],native_sha256=state['dlx1_sha256'],
      scope='Both complete n9 counts8113709 agree. Native111286419 nodes. The separate no-square native count is still pending; this does not close exercise68.')
    (out/'n9-verified.json').write_text(json.dumps(report,indent=2)+'\n')
    print('PASS: n9 complete count8113709; native111286419 nodes; no enumeration repeated')


if __name__=='__main__':main()

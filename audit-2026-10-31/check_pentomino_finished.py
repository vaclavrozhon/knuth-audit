#!/usr/bin/env python3
"""Accept completed large searches without repeating their computation."""
from datetime import datetime, timezone
import json
from dlx1_audit_tools import ROOT, sha, decode_rows, statistics
from prepare_pentomino_main import OUT


def main():
    state = json.loads((OUT/'large-wrapper.json').read_text())
    assert state['status'] == 'verified'
    for key,file in [('source_sha256',ROOT/'run_pentomino_main.py'),
                     ('cpp_sha256',ROOT/'pentomino_mask.cc'),
                     ('instances_sha256',OUT/'instances.json'),
                     ('short_sha256',OUT/'short-check.json')]:
        assert state[key] == sha(file)
    assert sha(state['binary']) == state['binary_sha256']
    for binary in state['native_binaries'].values():
        assert sha(binary['path']) == binary['sha256']
    instances = json.loads((OUT/'instances.json').read_text())['cases']
    short = json.loads((OUT/'short-check.json').read_text())['cases']
    expected = {tuple(m) for m in short['full']['models']}
    accepted = {}
    for label,nodes in [('full-cells-secondary',1086521921),('first-cell-3x20',1528716954)]:
        c = instances[label]
        for method in ['dlx1','mask']:
            key = label+'-'+method; meta = state['cases'][key]
            assert meta['status'] == 'finished'
            assert meta['stdout_sha256'] == sha(OUT/(key+'.out'))
            assert meta['stderr_sha256'] == sha(OUT/(key+'.log'))
            inp = OUT/(label+('.dlx' if method == 'dlx1' else '.masks'))
            assert meta['input_sha256'] == sha(inp)
        native = statistics((OUT/(label+'-dlx1.log')).read_text())
        mask = json.loads((OUT/(label+'-mask.out')).read_text())
        assert native == state['cases'][label+'-dlx1']['output']
        assert mask == state['cases'][label+'-mask']['output']
        assert native['nodes'] == mask['nodes'] == nodes
        assert native['profile'] == mask['profile']
        assert native['solutions'] == mask['solutions'] == 8
        models = decode_rows((OUT/(label+'-dlx1.out')).read_text(),c['names'],c['rows'])
        assert models == expected
        accepted[label] = dict(native=native,mask=mask,all_eight_models_match_independent_short_search=True)
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
      source_sha256=sha(__file__),wrapper_sha256=sha(OUT/'large-wrapper.json'),cases=accepted,
      scope='All large search profiles and complete native model sets verified. Historical memory-accounting differences and named bibliographic gaps remain separate.')
    (OUT/'large-verified.json').write_text(json.dumps(result,indent=2)+'\n')
    (OUT/'large-checkpoint.json').write_bytes((OUT/'large-wrapper.json').read_bytes())
    print('PASS:two complete billion-node profiles and both complete eight-model sets; no search restarted.')


if __name__ == '__main__':
    main()

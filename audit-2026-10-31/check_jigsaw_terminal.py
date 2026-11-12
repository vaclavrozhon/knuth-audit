"""Accept the finished original n7 DLX1 run without repeating enumeration."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
from dlx1_audit_tools import statistics

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/jigsaw/tilings'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    state=json.loads((OUT/'count-wrapper.json').read_text())
    assert state['status']=='verified' and state['active_case'] is None
    assert state['source_sha256']==sha(ROOT/'run_jigsaw_counts.py')
    assert state['cpp_sha256']==sha(ROOT/'jigsaw_count.cc')
    assert state['binary_sha256']==sha(state['binary'])
    assert state['dlx1_sha256']==sha(state['dlx1_binary'])
    accepted=[]
    for label,case in state['cases'].items():
        assert case['independent_counts_equal']
        for method,record in case['methods'].items():
            assert record['status']=='finished'
            prefix=OUT/(label+'-'+method)
            inp=OUT/(label+('.masks' if method=='cell-mask' else '.dlx'))
            stdout=Path(str(prefix)+'.out');stderr=Path(str(prefix)+'.log')
            assert record['input_sha256']==sha(inp)
            assert record['stdout_sha256']==sha(stdout)
            assert record['stderr_sha256']==sha(stderr)
            parsed=json.loads(stdout.read_text()) if method=='cell-mask' else statistics(stderr.read_text())
            assert parsed==record['output'] and parsed['solutions']==case['expected']
            if method=='dlx1':
                assert sum(parsed['profile'])==parsed['nodes']
                assert parsed['profile'][-1]==parsed['solutions'] if parsed['solutions'] else True
        accepted.append(dict(label=label,solutions=case['expected'],
                             native=case['methods']['dlx1']['output']))
    n7=state['cases']['n7']['methods']['dlx1']['output']
    assert n7['solutions']==132418528 and n7['nodes']==983498562
    assert n7['search_mems']==24619131223049 and n7['updates']==1894211822180
    # Book page72 defines Gmu as gigamems. Updates are a separate counter;
    # their 1.894T value must not be passed off as matching the 1.9Tmu claim.
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),status='verified',
        source_sha256=sha(Path(__file__)),wrapper_sha256=sha(OUT/'count-wrapper.json'),
        accepted=accepted,original_wrapper_pid=state['pid'],finished_at_utc=state['finished_at_utc'],
        book_unit='Page72 explicitly defines Gmu as gigamems, not updates.',
        benchmark_gap='Native n7 search24.619T mems; printed1.9Tmu remains unreproduced. Updates1.894T are a different unit.',
        new_searches=0)
    checkpoint=dict(state);checkpoint['accepted_at_utc']=result['checked_at_utc']
    checkpoint['accepted_wrapper_sha256']=result['wrapper_sha256']
    (OUT/'count-checkpoint.json').write_text(json.dumps(checkpoint,indent=2)+'\n')
    (OUT/'terminal-checked.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='verified',cases=len(accepted),n7=n7,benchmark_reproduced=False)))

if __name__=='__main__':main()

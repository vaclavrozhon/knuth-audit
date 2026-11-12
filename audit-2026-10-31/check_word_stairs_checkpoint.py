"""Accept terminal evidence and freeze current progress without repeating search."""
from datetime import datetime,timezone
import hashlib,json,subprocess
from pathlib import Path
from double_word_tools import dictionary
from three_way_stairs import validate

ROOT=Path(__file__).resolve().parent;K=ROOT/'results/stair_kernels';T=ROOT/'results/three_way_stairs'

def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    out=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),graphs=[],native_left_pending=True)
    small=read(K/'small-checked.json');assert small['comparisons']==96 and small['models']==57789
    for kind,W,count,vertices,cv,ce,maximum in [('left',500,136771,74568,6280,12269,36),('right',1000,180524,96677,30,34,5)]:
        prefix=f'{kind}{W}';meta=read(K/(prefix+'-distinct.json'));cycles=read(K/(prefix+'-cycles.json'))
        path=K/(prefix+'-distinct-kernels.txt');digest=sha(path)
        assert digest==meta['sha256']==cycles['source_sha256']
        assert (meta['kernels'],meta['vertices'],meta['core_vertices'],meta['core_edges'])==(count,vertices,cv,ce)
        scan=read(K/(prefix+'-scan-core.json'));assert (scan['core_vertices'],scan['core_edges'])==(cv,ce)
        assert cycles['maximum_period']==maximum and max(m['period'] for m in cycles['models'])==maximum
        assert all(q['complete'] for r in cycles['rounds'] for q in r['queries'])
        progress_path=K/(prefix+'-prune-progress.json')
        progress=read(progress_path)
        assert progress['rounds']==cycles['rounds']
        if progress['status']=='running':
            progress.update(status='completed',finished_utc=cycles['completed_utc'],
                            accepted_result_sha256=sha(K/(prefix+'-cycles.json')))
            progress_path.write_text(json.dumps(progress,indent=2)+'\n')
        out['graphs'].append(dict(kind=kind,W=W,kernels=count,vertices=vertices,core_vertices=cv,core_edges=ce,
            maximum_period=maximum,closed_walks=len(cycles['models']),kernels_sha256=digest,
            witnesses_sha256=sha(K/(prefix+'-distinct-witnesses.txt')),cycle_result_sha256=sha(K/(prefix+'-cycles.json'))))
    sat=read(K/'left500-sat-verified.json')
    assert sat['complete'] and sat['core_edges']==12269 and sat['checked_deletions']==3798
    assert sat['kernels_sha256']==sha(K/'left500-distinct-kernels.txt')
    assert sat['cnf_sha256']==sha(K/'left500-prune-proof.cnf')
    out['sat_pruning_deletions_verified']=3798
    native=K/'left500-native.json'
    if native.exists():
        n=read(native)
        assert n['status']=='completed' and n['returncode']==0 and n['complete_sets_equal']
        assert n['kernels']==136771 and n['join_set_sha256']==sha(K/'left500-distinct-kernels.txt')
        assert n['input_sha256']==sha(K/'left500-native.dlx') and n['stderr_sha256']==sha(K/'left500-native.log')
        assert n['script_sha256']==sha(ROOT/'run_kernel91_native.py') and n['kernel_module_sha256']==sha(ROOT/'word_kernel91.py')
        out.update(native_left_pending=False,native_left_solutions=n['solutions'],native_left_result_sha256=sha(native))
    else:
        run=read(K/'left500-native-run.json')
        out['native_left_live_ps']=subprocess.run(['ps','-p',str(run['wrapper_pid']),str(run['pid']),'-o','pid,ppid,etime,stat,args'],capture_output=True,text=True,check=True).stdout
    (K/'checkpoint.json').write_text(json.dumps(out,indent=2)+'\n')
    checked=read(T/'checked.json');assert checked['comparisons']==39 and checked['total_small_models']==230
    current=dict(checked_at_utc=out['checked_at_utc'],accepted=[],pending=[],small_comparisons=39,printed_examples=17)
    words=dictionary(5)
    for example in checked['examples']:
        label=f"{example['kind']}-{example['p']}";path=T/(label+'.json')
        if not path.exists():current['pending'].append(label);continue
        result=read(path)
        if result['status']!='proved':current['pending'].append(label);continue
        assert result['module_sha256']==sha(ROOT/'three_way_stairs.py')
        assert result['wordlist_sha256']==sha(ROOT/'sources/wordlists/words5-from-sgb')
        assert validate(result['best_rows'],words,result['kind'])==result['best_rank']
        last=result['attempts'][-1]
        assert last['complete'] and last['sat'] is False and last['threshold']==result['best_rank']-1
        for a in result['attempts'][:-1]:
            assert a['complete'] and a['sat']
            assert validate(a['witness'],words,result['kind'])<=a['threshold']
        current['accepted'].append(dict(label=label,printed_rank=result['printed_rank'],proved_rank=result['best_rank'],
            nodes=sum(a['nodes'] for a in result['attempts']),sha256=sha(path)))
    current['all_17_proved']=len(current['accepted'])==17
    (T/'checkpoint.json').write_text(json.dumps(current,indent=2)+'\n')
    print(json.dumps(dict(kernel_native_pending=out['native_left_pending'],kernel_maxima=[g['maximum_period'] for g in out['graphs']],
                         three_way_proved=len(current['accepted']),three_way_pending=current['pending'])))

if __name__=='__main__':main()

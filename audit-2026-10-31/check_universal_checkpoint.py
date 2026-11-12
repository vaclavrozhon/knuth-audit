"""Accept terminal benchmarks and freeze process observations; no new search."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,re,subprocess

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/universal_cycles'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    results=[]
    for p,q,want in [(0,3,137216),(3,4,41280)]:
        cases=[]
        for variant in ['primary','b-secondary']:
            label=f'native95-7-{p}-{q}-{variant}'
            path=OUT/(label+'.json');r=json.loads(path.read_text())
            assert r['status']=='completed' and r['returncode']==0 and r['solutions']==want
            for key,suffix in [('stderr_sha256','.log'),('stdout_sha256','.out.gz'),('input_sha256','.dlx')]:
                assert r[key]==sha(OUT/(label+suffix))
            assert r['module_sha256']==sha(ROOT/'universal_cycles.py')
            assert r['script_sha256']==sha(ROOT/'run_universal_native.py')
            log=(OUT/(label+'.log')).read_text()
            profile={int(k):int(v) for k,v in re.findall(r'^\s*(\d+): (\d+)$',log,re.M)}
            assert sum(profile.values())==r['nodes'] and profile[max(profile)]==want
            cases.append(dict(label=label,solutions=want,nodes=r['nodes'],net_search_mems=r['net_search_mems'],
                              profile=profile,result_sha256=sha(path)))
        assert cases[1]['nodes']>cases[0]['nodes']
        assert cases[1]['net_search_mems']<cases[0]['net_search_mems']
        results.append(cases)
    slow=json.loads((OUT/'native95-7-0-3-a-secondary-run.json').read_text())
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),script_sha256=sha(Path(__file__)),
                accepted=results,slow_status=slow['status'])
    if slow['status']=='running':
        observed=subprocess.run(['ps','-p',str(slow['wrapper_pid'])+','+str(slow['pid']),
                                 '-o','pid,ppid,etime,stat,args'],capture_output=True,text=True,check=True)
        assert len(observed.stdout.splitlines())==3
        result['live_ps']=observed.stdout
        result['slow_live_source_hashes']={name:sha(ROOT/name) for name in
            ['run_universal95_slow.py','run_universal_native.py','universal_cycles.py']}
        assert slow['script_sha256']==result['slow_live_source_hashes']['run_universal_native.py']
        assert slow['module_sha256']==result['slow_live_source_hashes']['universal_cycles.py']
    else:
        result['slow_terminal']=slow
    (OUT/'benchmarks-checked.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(fast_cases=4,slow_status=result['slow_status'],
                         net_gigamems=[[r['net_search_mems']/1e9 for r in pair] for pair in results])))

if __name__=='__main__':main()

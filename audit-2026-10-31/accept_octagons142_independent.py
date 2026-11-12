"""Accept the completed ten-case CSP queue; retain exact full/sample scopes."""
from datetime import datetime, timezone
import gzip
import hashlib
import json
import subprocess
import octagons142 as h
from octagons142_jobs import JOBS
from accept_octagons142_cases import checker


def read(path):
    return json.loads(path.read_text())


def main():
    base=h.OUT/'independent';queue=read(base/'queue.json')
    assert queue['status']=='completed' and len(queue['done'])==10
    for name,digest in queue['source_sha256'].items():
        assert h.sha(h.ROOT/name)==digest,name
    assert h.sha(h.OUT/'small/checked.json')==queue['small_check_sha256']
    ps=subprocess.run(['ps','-p',str(queue['wrapper_pid']),'-o','pid=,args='],capture_output=True,text=True)
    assert ps.returncode==1 and not ps.stdout
    records={};artifacts={};new_models=0
    for job in JOBS:
        label=job['label'];path=base/(label+'.json');meta=read(path)
        done=next(r for r in queue['done'] if r['label']==label)
        assert h.sha(path)==done['terminal_sha256'] and meta['solutions']==done['solutions']
        assert meta['status']=='completed' and meta['returncode']==0
        assert meta['source_sha256']==queue['source_sha256'] and meta['job']==job
        assert h.sha(meta['command'][2])==meta['binary_sha256']
        for suffix,key in [('.case','input_sha256'),('.out.gz','stdout_sha256'),('.log','stderr_sha256')]:
            target=base/(label+suffix);assert h.sha(target)==meta[key];artifacts[str(target.relative_to(h.ROOT))]=meta[key]
        artifacts[str(path.relative_to(h.ROOT))]=h.sha(path)
        layout=h.modes(job['case']);contract=h.contracted(layout,job['periodic'])
        assert (base/(label+'.case')).read_text()==h.independent_case(label,layout,every=job['every'],periodic=job['periodic'])
        paired=h.OUT/'accepted'/(label+'.json')
        if paired.exists():
            previous=read(paired)
            assert previous['terminal_sha256']['independent']==h.sha(path)
            assert previous['checker_sha256']==h.sha(h.ROOT/'accept_octagons142_cases.py')
            assert previous['independent_direct_models']==meta['solutions'] and previous['complete_sets_equal']
            artifacts[str(paired.relative_to(h.ROOT))]=h.sha(paired)
            count=meta['solutions'];scope='Previously accepted full paired model sets; no repeated validation.'
        else:
            validate=checker(layout,job['periodic']);seen=set();ordinals=[];terminal=None;raw_hash=hashlib.sha256()
            histogram=dict(tb=0,lr=0,both=0)
            with gzip.open(base/(label+'.out.gz'),'rb') as inp:
                for raw in inp:
                    raw_hash.update(raw);parts=raw.decode().split()
                    if parts[0]=='M':
                        assert terminal is None and len(parts)==4 and parts[1]==label
                        word=parts[3]
                        assert len(word)==contract['variables'] and set(word)<=set('abc') and h.color_key(word)==word
                        key,matches=validate([''.join(word[j] for j in ids) for ids in contract['sectors']])
                        assert key not in seen;seen.add(key);ordinals.append(int(parts[2]))
                        histogram['tb']+=matches['tb'];histogram['lr']+=matches['lr'];histogram['both']+=matches['tb'] and matches['lr']
                    else:
                        assert parts[:2]==['C',label] and terminal is None and len(parts)==8
                        terminal=list(map(int,parts[2:]))
            assert raw_hash.hexdigest()==meta['raw_stdout_sha256']
            assert terminal==[meta[k] for k in ['solutions','nodes','tb','lr','both','emitted']]
            expected=list(range(job['every'],meta['solutions']+1,job['every']))
            if job['every']>1 and meta['solutions']:
                expected=[1]+expected
            assert ordinals==expected and len(seen)==meta['emitted']
            if job['every']==1:
                assert len(seen)==meta['solutions'] and histogram=={k:meta[k] for k in histogram}
            log=(base/(label+'.log')).read_text().splitlines()
            assert log[-2:]==['COMPLETED '+label+' '+' '.join(map(str,terminal)),'ALL_COMPLETED 1']
            count=len(seen);new_models+=count
            scope='Every complete model directly validated.' if job['every']==1 else 'All saved samples validated; no archive of all models.'
        records[label]=dict(solutions=meta['solutions'],validated_models=count,output_period=job['every'],
            tb=meta['tb'],lr=meta['lr'],both=meta['both'],scope=scope,
            terminal_sha256=h.sha(path),matches_book=None if job['expected'] is None else meta['solutions']==job['expected'])
        print('ACCEPTED independent',label,meta['solutions'],'checked',count,flush=True)
    assert [records[k]['solutions'] for k in ['i','ii','iii']]==[264093722,3317206,239198]
    for case in ['i','ii','iii']:
        for axis in ['tb','lr']:
            assert records[case][axis]==records[case+'-'+axis]['solutions']
    assert records['i']['both']==records['i-both']['solutions']==192
    assert records['ii']['lr']==111960 and records['ii']['tb']==records['ii']['both']==0
    assert records['iii']['tb']==records['iii']['lr']==records['iii']['both']==0
    artifacts['results/octagons142/independent/queue.json']=h.sha(base/'queue.json')
    h.save(h.OUT/'independent-accepted.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),
        checker_sha256=h.sha(__file__),geometry_sha256=h.sha(h.__file__),model_checker_sha256=h.sha(h.ROOT/'accept_octagons142_cases.py'),
        queue_sha256=h.sha(base/'queue.json'),wrapper_pid=queue['wrapper_pid'],finished_at_utc=queue['finished_at_utc'],
        wrapper_absent=True,all_ten_cases_completed=True,all_main_counts_match_book=True,
        all_cylinder_counts_match_separate_constrained_censuses=True,
        f136_reproduced_in_unrestricted_ii=True,newly_validated_saved_models=new_models,
        cases=records,artifacts=artifacts,native_remaining_pending=True,
        full_i_ii_sets_archived=False,whole_exercise_status='partial'))
    print('PASS full independent queue; main counts match, F136 corroborated by unrestricted(ii). No search restarted.')


if __name__=='__main__':
    main()

"""Accept127–128 immutable evidence and its exact coverage, without searches."""
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
import gzip,hashlib,json,re,subprocess,sys
import borders127_128 as b
from macmahon126 import sha,save


def read(p):return json.loads(p.read_text())


def main():
    out=b.OUT;root=b.ROOT;repo=root.parent
    accepted=[]
    paths=list((out/'native').glob('*.json'))+list((out/'counts-native').glob('small-*.json'))+list((out/'counts-native').glob('wide-*.json'))
    for path in sorted(paths):
        if path.name.endswith('-run.json'):continue
        m=read(path);assert m['status']=='completed' and m['returncode']==0
        assert read(path.with_name(path.stem+'-run.json'))==m
        for suffix,key in [('.dlx','input_sha256'),('.log','stderr_sha256'),('.out.gz','stdout_sha256')]:
            assert sha(path.with_name(path.stem+suffix))==m[key]
        assert sha(m['command'][2])==m['binary_sha256'] and sha(m['source'])==m['source_sha256']
        assert sha(root/'graph_native.py')==m['runner_sha256']
        with gzip.open(path.with_name(path.stem+'.out.gz'),'rb') as f:assert hashlib.file_digest(f,'sha256').hexdigest()==m['raw_stdout_sha256']
        match=re.search(r'Altogether (\d+) solutions?, (\d+)\+(\d+)(?:-(\d+))? mems, .*?, (\d+) nodes',path.with_suffix('.log').read_text())
        assert match and tuple(int(x or 0) for x in match.groups())==tuple(m[k] for k in ['solutions','initial_mems','search_mems','unmems','nodes'])
        accepted.append(dict(name=path.stem,solutions=m['solutions'],metadata_sha256=sha(path)))
    assert len(accepted)==29,len(accepted)
    for name in ['supertiles128-bitset.json','wide-0-bitset.json','wide-1-bitset.json','border-witness127-run.json']:
        m=read(out/name);assert m['status']=='completed' and m['returncode']==0
        for f,h in m['files'].items():assert sha(out/f)==h
        assert sha(m['command'][2])==m['binary_sha256']
        assert sha(root/'borders127_128.py')==m['model_sha256']
    orbits=read(out/'orbits127-checked.json');witness=read(out/'border-witness127-checked.json')
    assert orbits['source_sha256']==sha(root/'border_orbits127.py')
    assert orbits['labeled_even_borders']==2099200
    assert orbits['groups']['abstract_D12']['orbits']==4054 and orbits['groups']['geometric_D6']['orbits']==7889
    for group in orbits['groups'].values():assert sha(out/group['representatives_file'])==group['representatives_sha256']
    assert witness['geometrically_validated_witnesses']==7889 and witness['covered_labeled_even_borders']==2099200
    assert witness['run_sha256']==sha(out/'border-witness127-run.json')
    assert witness['census_sha256']==sha(out/'orbits127-checked.json')
    assert witness['validator_sha256']==sha(root/'check_border_witness127.py')
    for file,script in [('supertiles128-checked.json','check_supertiles128.py'),('supertiles128-figures-checked.json','extract_supertiles128.py'),
                        ('counts127-small-checked.json','run_border_counts127.py'),('counts127-wide-checked.json','check_border_threshold127.py')]:
        assert read(out/file)['source_sha256']==sha(root/script)
    result128=read(out/'supertiles128-checked.json')
    assert result128['labeled_solutions']==6192 and result128['color_orbits']==1032 and result128['all_models_equal']
    assert sha(out/result128['all_models'])==result128['all_models_sha256']
    assert result128['independent_sha256']==sha(out/'supertiles128-bitset.json')
    assert result128['native_sha256']==sha(out/'native/supertiles128.json')
    assert len(result128['periodic_plane_proof']['triangle_cosets'])==22 and len(result128['periodic_plane_proof']['edge_cosets'])==33
    figures=read(out/'supertiles128-figures-checked.json');assert figures['total_original_wedges']==1055
    assert figures['trace_sha256']==sha(out/'page448-trace.xml') and len(figures['large']['wedges'])==1022
    assert len(read(out/'counts127-small-checked.json')['cases'])==12
    assert len(read(out/'counts127-wide-checked.json')['cases'])==2
    errata=read(out/'errata-check.json')
    for f,h in errata['local_files'].items():assert sha(repo/f)==h
    assert len(errata['local_files'])==6 and len(errata['remote_files'])==4 and all(x['unchanged'] for x in errata['remote_files'])
    assert sha(out/'errata-contexts.json')==errata['contexts_sha256']
    ledger=read(root/'ledger.json');items={x['id']:x for x in ledger['items']}
    assert len(items)==len(ledger['items'])==490
    assert items['X127']['status']=='partial' and items['X128']['status']=='checked'
    for id in ['X127','X128']:
        for f in items[id]['evidence']:assert (root/f).is_file(),(id,f)
    full=read(root/'full-review.json');reviews={x['id']:x for x in full['exercises']}
    assert len(reviews)==1202 and len(full['pages'])==734
    assert Counter(x['status'] for x in full['exercises'])=={'reviewed':137,'partial':70,'pending':995}
    assert reviews['DLX:128']['status']=='reviewed' and reviews['DLX:127']['status']=='partial'
    baseline=Path(sys.argv[1]);previous=read(baseline/'ledger.json')
    assert all(items[x['id']]==x for x in previous['items'] if x['id']!='X089'), 'Unrelated prior evidence must remain unchanged.'
    old89=next(x for x in previous['items'] if x['id']=='X089')
    assert set(old89['evidence'])<=set(items['X089']['evidence']) and items['X089']['status']=='partial'
    ospd6=root/'results/double_words/ospd6-terminal-checked.json';six=read(ospd6)
    assert six['script_sha256']==sha(root/'accept_ospd6_terminal.py')
    assert six['source_metadata_sha256']==sha(root/'results/double_words/cell-ospd6-run.json')
    assert six['source_result_sha256']==sha(root/'results/double_words/cell-ospd6.json')
    assert six['complete_squares']==2038753 and six['stored_double_models']==389514
    assert sha(repo/'review-ui/curation.json')==sha(baseline/'curation.json')
    queue=read(out/'counts127-queue.json')
    process=None
    if queue['status']=='running':
        process=subprocess.check_output(['ps','-p',str(queue['wrapper_pid']),'-o','pid=,stat=,etime=,args='],text=True).strip()
        assert 'run_border_counts127.py' in process
    save(out/'checkpoint-checked.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
         source_sha256=sha(__file__),completed_native_cases=accepted,validated_border_witnesses=7889,
         labeled128models=6192,color128orbits=1032,original_wedges=1055,all487_unrelated_previous_ledger_items_unchanged=True,
         X089_prior_evidence_preserved=True,ospd6_accepted_metadata_sha256=sha(ospd6),
         ledger_counts=dict(Counter(x['status'] for x in ledger['items'])),review_counts=dict(Counter(x['status'] for x in full['exercises'])),
         count_queue_status=queue['status'],live_observation=process,
         remaining_gaps=['127:Full counts for side/corner/separated boundaries','127:Meaning of576 symmetries for completion counts','127:Global order and statistical estimates','Other pending/partial content prevents whole-volume completion.']))
    print('PASS:29 native terminals;128 complete,127 partial;OSPD6 terminal accepted;487 unrelated ledger items unchanged,X089 prior evidence preserved.')


if __name__=='__main__':main()

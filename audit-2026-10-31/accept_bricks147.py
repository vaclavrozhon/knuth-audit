"""Bind the completed147 catalogue and standalone F138 certificate to inputs."""
from datetime import datetime,timezone
from pathlib import Path
import json
import bricks147 as h


def read(p):return json.loads(Path(p).read_text())


def main():
    bounded=h.OUT/'bounded';follow=h.OUT/'followup'
    batch=read(bounded/'batch-status.json');assert batch['interrupted'] is None and len(batch['completed'])==13
    cases={};models=orbits=0
    for folder,labels in [(bounded,batch['completed']),(follow,['2x2x6','2x2x7'])]:
        for label in labels:
            run=read(folder/f'{label}-run.json');checked=read(folder/f'{label}-checked.json')
            assert run['status']=='completed' and run['returncode']==0
            for suffix,key in [('.case','input_sha256'),('.out','stdout_sha256'),('.log','stderr_sha256')]:assert h.sha(folder/(label+suffix))==run[key]
            models+=checked['models'];orbits+=len(checked['orbits'])
            cases[label]=dict(normalized_models=checked['models'],orbits=len(checked['orbits']),elapsed_seconds=run['elapsed_seconds'])
    assert models==1190 and orbits==206
    for label in ['native-2x2x4','native-3x3x3']:
        r=read(follow/f'{label}-accepted.json');assert r['full_sets_equal'] and r['all_models_directly_valid']
        assert r['native_terminal_sha256']==h.sha(follow/f'{label}.json')
        assert r['checker_sha256']==h.sha(h.ROOT/'followup_bricks147.py')
    for label,n in [('without-corner',26),('without-middle-and-above',25)]:
        r=read(follow/f'{label}-witness.json')
        assert len(r['model'])==n and r['complete_census'] is False and r['first_solution_only']
        assert r['native_terminal_sha256']==h.sha(follow/f'{label}.json')
    fig=read(h.OUT/'figures-checked.json')
    assert fig['checker_sha256']==h.sha(h.ROOT/'extract_bricks147.py')
    assert fig['geometry_sha256']==h.sha(h.__file__) and fig['cube_geometry_sha256']==h.sha(h.cubes.__file__)
    for p,d in fig['trace_hashes'].items():assert h.sha(h.ROOT/p)==d
    small=fig['figures']['small']['model']
    op=next(g for g in h.group((1,2,2)) if g[0]==(0,1,2) and g[1]==(1,-1,1))
    assert tuple(w.translate(str.maketrans('de','ed')) for w in h.transform((1,2,2),small,op))==tuple(small)
    claims=read(h.OUT/'claims-checked.json');assert claims['checker_sha256']==h.sha(h.ROOT/'check_bricks147_claims.py')
    assert len(claims['differences'])==4 and claims['all_other_histograms_agree']
    source=read(h.OUT/'sources-checked.json');assert source['checker_sha256']==h.sha(h.ROOT/'check_bricks147_sources.py')
    for p,d in source['source_hashes'].items():assert h.sha(h.ROOT/p)==d,p
    for label in ['native-2x2x4','native-3x3x3','without-corner','without-middle-and-above']:
        run=read(follow/f'{label}.json')
        for suffix,key in [('.dlx','input_sha256'),('.out.gz','stdout_sha256'),('.log','stderr_sha256')]:assert h.sha(follow/(label+suffix))==run[key]
        assert h.sha(run['source'])==run['source_sha256']
    assert read(bounded/'started.json')['source_sha256']==h.sha(h.ROOT/'check_bricks147.py')
    assert read(bounded/'build.json')['source_sha256']==h.sha(h.ROOT/'count_bricks147.cpp')
    assert 'PASS: five valid' in (h.OUT/'f138-standalone.log').read_text()
    artifacts=[p for folder in [bounded,follow] for p in folder.rglob('*') if p.is_file() and p.suffix!='.lock']
    artifacts += [h.OUT/p for p in ['figures-checked.json','claims-checked.json','sources-checked.json','errata-check.json','f138-standalone.log']]
    artifacts += [h.ROOT/p for p in ['bricks147.py','extract_bricks147.py','count_bricks147.cpp','check_bricks147.py',
        'followup_bricks147.py','check_bricks147_claims.py','check_bricks147_sources.py','verify_f138.py',
        'BRICKS147_NOTES.md','F138_BRICK_HISTOGRAMS.md']]
    h.save(h.OUT/'accepted.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),acceptor_sha256=h.sha(__file__),
        cases=cases,total_normalized_models=models,total_orbits=orbits,all_mathematical_claims_reviewed=True,
        f138=claims['differences'],known_errata=['E074','E075'],omissions=[],
        independent_whole_sets_equal={'2x2x4':244,'3x3x3':0},standalone_five_class_certificate=True,
        cavity_witnesses_only=[26,25],pending_history=source['pending_history'],
        artifacts={str(p.relative_to(h.ROOT)):h.sha(p) for p in artifacts}))
    print('PASS147 acceptance:1190 models/206 classes; four erroneous histogram entries; independent244/0; direct26/25 witnesses; no expensive-count omissions.')


if __name__=='__main__':main()

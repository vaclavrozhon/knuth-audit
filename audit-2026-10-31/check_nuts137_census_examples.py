"""Original DLX2 verifies every encountered stabilizer order and the reported maximum."""
from datetime import datetime,timezone
import gzip
import json
import re
import nuts137 as n
import graph_native as native


def main():
    out=n.OUT/'census'
    assert not (out/'examples-checked.json').exists()
    run=json.loads((out/'run.json').read_text())
    assert run['status']=='completed' and run['returncode']==0
    assert n.sha(out/'census.tsv.gz')==run['census_gzip_sha256']
    summary=json.loads((out/'stdout.json').read_text())
    maximum=max(q for q,amount in summary['histogram'] if amount)
    selected={}
    with gzip.open(out/'census.tsv.gz','rt') as f:
        next(f)
        for line in f:
            key,count,h,q,weight=map(int,line.split())
            selected.setdefault('h'+str(h),(key,count,h,q,weight))
            if q==maximum: selected.setdefault('maximum',(key,count,h,q,weight))
    build=json.loads((n.ROOT/'results/symmetry121_123/native/build.json').read_text())
    binary=build['binaries']['original']['binary']
    assert n.sha(binary)==build['binaries']['original']['sha256']
    native.OUT=out/'native-examples';native.OUT.mkdir(exist_ok=True)
    checks=[]
    for label,(key,count,h,q,weight) in selected.items():
        ids=[0]*7;tmp=key
        for i in range(6,0,-1): ids[i]=tmp&127;tmp>>=7
        assert tmp==0
        nuts=[n.TYPES[i] for i in ids]
        enc=n.problem(nuts,'equal')
        result=native.run(label,n.native_text(enc),binary=binary,limit=120)
        assert result['status']=='completed' and result['returncode']==0
        lookup={tuple(sorted(row)):k for k,row in enumerate(enc['rows'])}
        chosen=[];models=[]
        def accept():
            assert len(chosen)==7
            words=['']*7
            for k in chosen:
                p,w=enc['placements'][k];assert not words[p];words[p]=w
            n.validate(words,nuts,'equal');assert words[0][0]=='1'
            return '/'.join(words)
        with gzip.open(native.OUT/(label+'.out.gz'),'rt') as f:
            for line in f:
                if re.fullmatch(r'\d+:\s*',line):
                    if chosen: models.append(accept());chosen=[]
                elif line.strip():
                    row=re.sub(r'\s*\(\d+ of \d+\)\s*$','',line).split()
                    chosen.append(lookup[tuple(sorted(row))])
        if chosen: models.append(accept())
        independent,_=n.ring_search(nuts,'equal')
        assert sorted(models)==independent and len(models)==q==result['solutions']
        checks.append(dict(label=label,key=key,nuts=nuts,stabilizer=h,solutions=q,
                           models=independent,full_set_equality=True,
                           native_metadata_sha256=n.sha(native.OUT/(label+'.json'))))
    n.save(out/'examples-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=n.sha(__file__),geometry_sha256=n.sha(n.__file__),
        census_metadata_sha256=n.sha(out/'run.json'),cases=checks,
        scope='Existence and exact counts for representative examples; completeness of the global histogram is a separate verifier.'))
    print('PASS137 census examples:',[(x['label'],x['solutions']) for x in checks],flush=True)


if __name__=='__main__': main()

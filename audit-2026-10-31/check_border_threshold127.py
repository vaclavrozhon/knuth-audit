"""Nontrivial boundary-domain cross-checks: original C, threshold C and bitsets."""
from datetime import datetime,timezone
import json,random,subprocess,os
import borders127_128 as b
import run_border_counts127 as run
from macmahon126 import build,text,save,sha


def main():
    rng=random.Random(710127);built=build();reports=[]
    for case,word in enumerate(['000000000011','000000000101']):
        base=b.problem127(word);allowed={}
        for p in base['placements'][:-1]:
            t=tuple(p['cell']);key=(t,run.orbit(p['colors']))
            if key not in allowed:allowed[key]=rng.random()<.7
        ids=[i for i,p in enumerate(base['placements']) if p is None or allowed[(tuple(p['cell']),run.orbit(p['colors']))]]
        enc=dict(base,rows=[base['rows'][i] for i in ids],placements=[base['placements'][i] for i in ids])
        full=[];orbits=[]
        for threshold in (False,True):
            label=f'wide-{case}-'+('C' if threshold else 'original')
            meta=run.native(label,enc,threshold);assert meta['status']=='completed'
            vectors=run.validate_samples(label,enc);assert len(vectors)==meta['solutions']
            if threshold:orbits=vectors
            else:full=vectors
        assert len(full)==2*len(orbits) and len(full)>2
        assert set(map(run.orbit,full))==set(map(run.orbit,orbits))
        label=f'wide-{case}-bitset';end=b.OUT/(label+'.json');raw=b.OUT/(label+'.models.txt')
        if end.exists():
            meta=json.loads(end.read_text());assert meta['status']=='completed'
            for f,h in meta['files'].items():assert sha(b.OUT/f)==h
        else:
            state=b.OUT/(label+'-run.json');assert not state.exists()
            inp=b.OUT/(label+'.xcc');inp.write_text(text(enc));stdout=b.OUT/(label+'.stdout');stderr=b.OUT/(label+'.stderr')
            cmd=['timeout','1800',built['binaries']['bitset']['path'],str(raw),'42']
            meta=dict(status='running',command=cmd,wrapper_pid=os.getpid(),started_at_utc=datetime.now(timezone.utc).isoformat(),
                      source_sha256=sha(__file__),model_sha256=sha(b.__file__),binary_sha256=built['binaries']['bitset']['sha256'])
            with inp.open('rb') as fin,stdout.open('wb') as fout,stderr.open('wb') as ferr:
                p=subprocess.Popen(cmd,stdin=fin,stdout=fout,stderr=ferr);meta['pid']=p.pid;save(state,meta);rc=p.wait()
            meta.update(status='completed' if rc==0 else 'incomplete',returncode=rc,
                        finished_at_utc=datetime.now(timezone.utc).isoformat(),files={p.name:sha(p) for p in [inp,stdout,stderr,raw]})
            save(end,meta);save(state,meta);assert rc==0
        independent=raw.read_text().splitlines();assert len(independent)==len(full) and set(independent)==set(full)
        for cs in independent:b.validate127(cs,enc)
        reports.append(dict(word=word,options=len(ids),labeled_solutions=len(full),color_orbits=len(orbits),
                            all_sets_equal=True,independent_metadata_sha256=sha(end)))
    save(b.OUT/'counts127-wide-checked.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
         source_sha256=sha(__file__),model_sha256=sha(b.__file__),cases=reports))
    print('PASS127 wide:',reports)


if __name__=='__main__':main()

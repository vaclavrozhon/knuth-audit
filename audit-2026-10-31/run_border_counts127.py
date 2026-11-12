"""Recorded two-color boundary counts; one queue, no implicit restarts."""
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
import fcntl,json,os,random,sys
import borders127_128 as b
import graph_native
from macmahon126 import build,text,save,sha

CASES=[('side11','000000000011'),('corner11','100000000001'),('separated101','000000000101')]


def orbit(cs):
    swapped=cs.translate(str.maketrans('cd','dc'))
    return min(cs,swapped)


def native(label,enc,threshold,every=1):
    built=build();out=b.OUT/'counts-native';out.mkdir(exist_ok=True);graph_native.OUT=out
    variant='threshold' if threshold else 'original'
    source=b.ROOT/'results/triangles124_126/native/dlx2-macmahon126.w' if threshold else b.ROOT/'sources/knuth-programs/dlx2.w'
    return graph_native.run(label,text(enc),binary=built['binaries'][variant]['path'],source=source,
                            every=every,extra=('y99','W2') if threshold else ())


def validate_samples(label,enc):
    vectors=[]
    for chosen in b.selected_models(b.OUT/'counts-native'/(label+'.out.gz'),enc):
        colors=b.geometric_colors(chosen,enc);cs=''.join(colors[e] for e in enc['edges'])
        b.validate127(cs,enc);vectors.append(cs)
    assert len(vectors)==len(set(vectors));return vectors


def small():
    witnesses={w:cs for w,cs,n in (s.split() for s in (b.OUT/'border-witness127.models.txt').read_text().splitlines())}
    results=[];rng=random.Random(127)
    for index,(w,vector) in enumerate((w,witnesses[w]) for w in ['000000000011','000000000101']):
        base=b.problem127(w);colors=dict(zip(base['edges'],vector))
        for size in [0,10,30,80,150,250]:
            selected={}
            for t in b.g.TRIANGLES:
                cs=''.join(colors[e] for e in b.g.edges(t))
                selected[t]={cs,cs.translate(str.maketrans('cd','dc'))}
            for i in rng.sample(range(len(base['rows'])-1),size):
                p=base['placements'][i];cs=p['colors'];selected[tuple(p['cell'])].update([cs,cs.translate(str.maketrans('cd','dc'))])
            ids=[i for i,p in enumerate(base['placements']) if p is None or p['colors'] in selected[tuple(p['cell'])]]
            enc=dict(base,rows=[base['rows'][i] for i in ids],placements=[base['placements'][i] for i in ids])
            sets=[];counts=[]
            for threshold in (False,True):
                label=f'small-{index}-{size}-'+('C' if threshold else 'original')
                m=native(label,enc,threshold);assert m['status']=='completed'
                cs=validate_samples(label,enc);assert len(cs)==m['solutions']
                sets.append(set(map(orbit,cs)));counts.append(len(cs))
            assert counts[0]==2*counts[1] and sets[0]==sets[1]
            results.append(dict(word=w,added_choices=size,original=counts[0],color_orbits=counts[1],equal_orbit_sets=True))
    save(b.OUT/'counts127-small-checked.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
         source_sha256=sha(__file__),model_sha256=sha(b.__file__),cases=results,
         scope='Twelve invariant restricted instances compare complete original and threshold model sets, with independent geometric validation. The c/d permutation acts freely.'))
    print('PASS127:',len(results),'complete restricted-instance comparisons',flush=True)


def main():
    if len(sys.argv)>1 and sys.argv[1]=='small':small();return
    assert (b.OUT/'counts127-small-checked.json').exists()
    lock=(b.OUT/'counts127-queue.lock').open('w');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    path=b.OUT/'counts127-queue.json';assert not path.exists(),'No implicit queue restart.'
    state=dict(status='running',wrapper_pid=os.getpid(),started_at_utc=datetime.now(timezone.utc).isoformat(),
               runner_sha256=sha(__file__),model_sha256=sha(b.__file__),done=[],timeout_seconds_per_case=172800)
    save(path,state)
    for label,word in CASES:
        state['current']=dict(label=label,word=word);save(path,state)
        enc=b.problem127(word);m=native(label,enc,True,100000)
        if m['status']!='completed':
            state.update(status='incomplete',finished_at_utc=datetime.now(timezone.utc).isoformat());save(path,state);return
        samples=validate_samples(label,enc);assert len(samples)==m['solutions']//100000
        record=dict(label=label,word=word,status='completed',color_orbits=m['solutions'],labeled_solutions=2*m['solutions'],
                    validated_samples=len(samples),native_sha256=sha(b.OUT/'counts-native'/(label+'.json')),
                    model_sha256=sha(b.__file__),runner_sha256=sha(__file__),free_color_symmetry_factor=2)
        save(b.OUT/(label+'-count-checked.json'),record);state['done'].append(record);save(path,state)
        print(json.dumps(record),flush=True)
    state.update(status='completed',current=None,finished_at_utc=datetime.now(timezone.utc).isoformat());save(path,state)


if __name__=='__main__':main()

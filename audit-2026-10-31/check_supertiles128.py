"""Two complete6192-model censuses,1032 color orbits and periodic proof."""
from collections import Counter
from datetime import datetime,timezone
import gzip,json,os,subprocess
import borders127_128 as b
import graph_native
from macmahon126 import build,text,save,sha


def main():
    out=b.OUT;out.mkdir(exist_ok=True)
    enc=b.problem128();built=build();native=out/'native';native.mkdir(exist_ok=True)
    graph_native.OUT=native
    result=graph_native.run('supertiles128',text(enc),binary=built['binaries']['original']['path'])
    assert result['status']=='completed' and result['solutions']==6192
    native_set=set()
    for selected in b.selected_models(native/'supertiles128.out.gz',enc):
        colors=b.geometric_colors(selected,enc)
        assert all(colors[a]==colors[c] for a,c in b.PAIRS128)
        cs=''.join(colors[e] for e in enc['representatives']);b.validate128(cs,enc)
        assert cs not in native_set;native_set.add(cs)
    assert len(native_set)==6192
    bitset=out/'supertiles128-bitset.json';raw=out/'supertiles128-bitset.models.txt'
    if bitset.exists():
        other=json.loads(bitset.read_text())
        assert other['status']=='completed'
        for f,h in other['files'].items():assert sha(out/f)==h
    else:
        state=out/'supertiles128-bitset-run.json';assert not state.exists(),'No implicit restart.'
        cmd=['timeout','600',built['binaries']['bitset']['path'],str(raw),'18']
        meta=dict(status='running',wrapper_pid=os.getpid(),command=cmd,started_at_utc=datetime.now(timezone.utc).isoformat(),
                  binary_sha256=built['binaries']['bitset']['sha256'],source_sha256=sha(b.ROOT/'xcc_bitset.cpp'),
                  runner_sha256=sha(__file__),model_sha256=sha(b.__file__))
        stdout=out/'supertiles128-bitset.stdout';stderr=out/'supertiles128-bitset.stderr'
        with (native/'supertiles128.dlx').open('rb') as fin,stdout.open('wb') as fout,stderr.open('wb') as ferr:
            proc=subprocess.Popen(cmd,stdin=fin,stdout=fout,stderr=ferr);meta['pid']=proc.pid;save(state,meta);rc=proc.wait()
        assert rc==0,rc
        other=dict(meta,status='completed',returncode=rc,finished_at_utc=datetime.now(timezone.utc).isoformat(),
                   statistics=json.loads(stdout.read_text()),files={p.name:sha(p) for p in [raw,stdout,stderr]})
        save(bitset,other);save(state,other)
    independent=raw.read_text().splitlines();assert len(independent)==6192 and len(set(independent))==6192
    for cs in independent:b.validate128(cs,enc)
    assert set(independent)==native_set
    from border_orbits127 import normalize
    color_orbits=Counter(normalize(cs) for cs in independent)
    assert len(color_orbits)==1032 and set(color_orbits.values())=={6}
    proof=b.plane_quotient128()
    canonical=out/'supertiles128-models.txt';canonical.write_text('\n'.join(sorted(native_set))+'\n')
    save(out/'supertiles128-checked.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
         source_sha256=sha(__file__),model_sha256=sha(b.__file__),labeled_solutions=6192,
         color_orbits=1032,color_orbit_size=6,primary=22,secondary=18,options=297,
         native_sha256=sha(native/'supertiles128.json'),independent_sha256=sha(bitset),
         all_models_sha256=sha(canonical),all_models=canonical.name,all_models_equal=True,
         periodic_plane_proof=proof,
         interpretation='The printed1032 counts modulo the six global color permutations; without that normalization there are6192. No automatic erratum inferred from an implicit symmetry convention.',
         scope='Full model sets and general plane-cover proof. Original printed figures are checked separately.'))
    print('PASS128:6192 complete models agree,1032 color orbits;22 triangle cosets and33 edge cosets prove plane cover.')


if __name__=='__main__':main()

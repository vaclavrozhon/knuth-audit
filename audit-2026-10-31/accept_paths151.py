"""Accept prior6420 certificates and new original figures, with no search reruns."""
from collections import Counter
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import gzip, hashlib, json
import paths151 as h

def read(p):return json.loads(p.read_text())
def digest(b):return hashlib.sha256(b).hexdigest()

def main():
    old=h.ROOT/'results/path_dominoes';summary=read(old/'geometries/summary.json')
    assert [summary[k] for k in ['geometries','orbits','verified_models','completed','exhausted','weighted_models']]==[625,169,6420,169,169,6420]
    def orbit(cs):return {tuple(cs),tuple(reversed(cs)),tuple(8-c for c in cs),tuple(8-c for c in reversed(cs))}
    reps={min(orbit(cs)) for cs in product(range(0,9,2),repeat=4)}
    assert reps=={tuple(r['columns']) for r in summary['results']}
    assert sum(len(orbit(r['columns'])) for r in summary['results'])==625
    hashes={};proofs=[]
    for r in summary['results']:
        label='-'.join(map(str,r['columns']));p=old/'geometries'/label
        assert read(p.with_suffix('.json'))==r and r['proof_verified'] and r['status']=='EXHAUSTED'
        assert len(orbit(r['columns']))==r['orbit_size']
        for ext in ['cnf','drat']:
            f=p.with_suffix('.'+ext+'.gz');assert digest(gzip.decompress(f.read_bytes()))==r[ext+'_sha256']
            hashes[str(f.relative_to(h.ROOT))]=h.sha(f)
        log=p.with_suffix('.verification.txt');assert 's VERIFIED' in log.read_text()
        hashes[str(log.relative_to(h.ROOT))]=h.sha(log);hashes[str(p.with_suffix('.json').relative_to(h.ROOT))]=h.sha(p.with_suffix('.json'))
        proofs.append(dict(columns=r['columns'],known_models=r['known_models'],orbit_size=r['orbit_size']))
    assert sum(p['known_models']*p['orbit_size'] for p in proofs)==6420
    models=[tuple(sorted(json.loads(line))) for line in (old/'max36.models.jsonl').read_text().splitlines()]
    assert len(models)==len(set(models))==6420
    # Relate the newly decoded printed maximum witness to the saved factored
    # census. Constructing options is finite; do not call encode/solve/main.
    from check_path_dominoes import options_for,key
    counts=Counter()
    for k in [1,2]:
        for p in h.catalogue(k)[1]:counts[key(sum(1<<x for x in h.mask(p)))]+=1
    opts=options_for(8,9,counts)
    lookup={(tuple(o['cells']),o['mask']):i+1 for i,o in enumerate(opts)}
    figs=read(h.OUT/'figures-checked.json');witness=[]
    for p in figs['figures']['original-b']['pieces']:
        a,b,c,d=p['bounds'];cells=tuple((y,x) for y in range(c,d) for x in range(a,b))
        witness.append(lookup[cells,sum(1<<x for x in h.mask(p['pattern']))])
    assert tuple(sorted(witness)) in set(models)
    for filename in ['max36.models.jsonl','max36.json','geometries/summary.json','catalog.json','balanced36.loop.json','max36-witness.loop.json']:
        hashes[str((old/filename).relative_to(h.ROOT))]=h.sha(old/filename)
    for script in ['check_path_dominoes.py','check_path_geometries.py','check_path_loops.py']:
        hashes[script]=h.sha(h.ROOT/script)
    claims=read(h.OUT/'claims-checked.json')
    assert claims['checker_sha256']==h.sha(h.ROOT/'check_paths151_claims.py')
    for key_,filename in [('catalogue_sha256','catalogue-checked.json'),('figures_sha256','figures-checked.json'),('errata_sha256','errata-check.json')]:assert claims[key_]==h.sha(h.OUT/filename)
    # claims-checked recorded only the new work. Its proposed6420 omission is
    # superseded here by the previously completed and accepted certificate set.
    omissions=[dict(r) for r in claims['omissions']]
    omissions[0].update(id='DLX151-balanced-census',claim='Millions of factored solutions in151(a)',
        evidence='General MCC correspondence and direct18H/18V printed witness. The separate6420 count in151(b) is already verified by prior169 certificates.',
        reason='User permits omitting expensive additional complete censuses. No new census launched; prior6420 evidence retained.')
    h.save(h.OUT/'accepted.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=h.sha(__file__),
        previous_6420_accepted=True,prior_certificate_groups=169,prior_geometries=625,prior_models=6420,
        no_prior_solver_or_proof_verifier_restarted=True,prior_model_validation_retained=True,printed_maximum_in_prior_model_set=True,
        prior_hashes=hashes,new_claims_sha256=h.sha(h.OUT/'claims-checked.json'),new_figures_sha256=h.sha(h.OUT/'figures-checked.json'),
        new_geometry_and_catalogue_sha256={p:h.sha(h.ROOT/p) for p in ['paths151.py','extract_paths151.py','check_paths151_claims.py']},
        supersedes='The6420 omission proposed in claims-checked.json is withdrawn: old completed evidence already verifies it. All48 witness gap is now closed by the original diagram.',
        exercise151_status='partial',exercise151_open='Precise1999 source chronology and first-solution priority.',exercise152_status='reviewed',
        omissions=omissions,new_findings=[],known_errata=['E076','E077'],new_placement_searches=0))
    print('PASS:prior6420/169proofs/625geometries accepted by hashes and verification logs; printed maximum belongs to saved set. New48-piece witness closes old gap. No searches.')

if __name__=='__main__':main()

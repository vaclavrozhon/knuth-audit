"""Accept the exact histogram only after ALL orbit counts and total completeness agree."""
from collections import Counter
from datetime import datetime,timezone
from fractions import Fraction
import gzip
import hashlib
import json
import nuts137 as n
from accept_nuts137 import check_native


def read(p): return json.loads(p.read_text())


def main():
    out=n.OUT/'census'
    for name,cpp,runner in [('run.json','census_nuts137.cpp','run_nuts137_census.py'),
                             ('verifier-run.json','verify_nuts137_census.cpp','run_nuts137_census_verifier.py')]:
        m=read(out/name)
        assert m['status']=='completed' and m['returncode']==0,name
        assert n.sha(n.ROOT/cpp)==m['source_sha256'] and n.sha(n.ROOT/runner)==m['runner_sha256']
    run=read(out/'run.json');verify=read(out/'verifier-run.json')
    assert verify['census_metadata_sha256']==n.sha(out/'run.json')
    assert verify['census_sha256']==run['census_sha256']
    assert verify['stdout_sha256']==n.sha(out/'verifier-stdout.json')
    assert verify['stderr_sha256']==n.sha(out/'verifier-progress.log')
    assert run['stdout_sha256']==n.sha(out/'stdout.json')
    assert run['census_gzip_sha256']==n.sha(out/'census.tsv.gz')
    raw_digest=hashlib.sha256();hist=Counter();rows=0;anchored=0
    with gzip.open(out/'census.tsv.gz','rb') as f:
        raw_digest.update(next(f))
        for line in f:
            raw_digest.update(line)
            key,c,h,q,weight=map(int,line.split())
            assert h in (1,2,3,6) and weight==720//h and c*h==6*q
            hist[q]+=weight;rows+=1;anchored+=c
    assert raw_digest.hexdigest()==run['census_sha256']
    total=59487568920
    hist[0]=total-sum(hist.values())
    native=read(out/'stdout.json');independent=read(out/'verifier-stdout.json')
    assert sorted(map(list,hist.items()))==native['histogram']==independent['histogram']
    assert rows==native['orbits']==independent['orbits_verified']==5623238
    assert anchored==native['anchored_models']==independent['independent_anchored_models']==43500008
    assert sum(q*amount for q,amount in hist.items())==native['total_solutions']==independent['weighted_models']==5220000960
    examples=read(out/'examples-checked.json')
    assert examples['source_sha256']==n.sha(n.ROOT/'check_nuts137_census_examples.py')
    assert examples['geometry_sha256']==n.sha(n.__file__)
    for case in examples['cases']:
        meta,sha=check_native(case['label'],lambda p:(out/'native-examples'/p).read_bytes())
        assert sha==case['native_metadata_sha256'] and meta['solutions']==case['solutions']
        assert case['full_set_equality']
    preflight=read(out/'preflight-checked.json')
    assert preflight['all_86400_rename_entries_equal'] and preflight['direct_all720_permutations_agree']
    assert preflight['source_sha256']==n.sha(n.ROOT/'run_nuts137_census.py')
    grouped=[hist[0],hist[1],hist[2],sum(amount for q,amount in hist.items() if q>=3)]
    ratios=[Fraction(amount,total) for amount in grouped]
    artifacts=[p for p in out.iterdir() if p.is_file() and p.name not in ('census.tsv','accepted.json')]
    artifacts+=list((out/'native-examples').glob('*'))
    artifacts=[p for p in artifacts if p.suffix!='.lock']
    n.save(out/'accepted.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=n.sha(__file__),total_type_sets=total,nonempty_orbits=rows,
        independently_verified_orbits=rows,anchored_solutions=anchored,
        total_solutions_across_all_sets=5220000960,
        histogram=sorted(map(list,hist.items())),grouped_0_1_2_3plus=grouped,
        exact_probabilities=[dict(numerator=p.numerator,denominator=p.denominator,
                                  percent=float(100*p)) for p in ratios],
        maximum_solutions=max(hist),sets_at_maximum=hist[max(hist)],
        all_orbits_canonical_and_stabilizers_checked=True,
        all_orbits_exact_solution_count_checked=True,
        global_completeness_independently_checked=True,
        proof='Every solution orbit can be relabeled to center123456. For a type-set orbit '
          'with stabilizer h and q solutions per set, uniformity among120 center types gives '
          'c=6q/h anchored solutions and720/h distinct sets. A separate shared-edge-label '
          'enumeration supplies the total43,500,008 anchored solutions. The verifier checks '
          'all720 relabelings and the complete fixed-set solution count for EVERY reported '
          'representative, and their weighted total equals120 times that independent total. '
          'Any missing nonempty orbit would contribute a positive additional count. Zeros '
          'are the complement in120 choose7. No claim of an exact sum7/joint histogram.',
        candidate=f'C032: {float(100*ratios[3]):.10f}% versus the coarse remaining1%; '
          'whether this warrants an erratum remains an editorial interpretation, not a counting uncertainty.',
        artifacts={str(p.relative_to(out)):n.sha(p) for p in sorted(artifacts)},
        dependencies={p:n.sha(n.ROOT/p) for p in ['census_nuts137.cpp','run_nuts137_census.py',
            'verify_nuts137_census.cpp','run_nuts137_census_verifier.py',
            'check_nuts137_census_examples.py','accept_nuts137.py','nuts137.py','graph_native.py']}))
    print('PASS137 exact census:',grouped,'out of',total,flush=True)


if __name__=='__main__': main()

#!/usr/bin/env python3
"""Reconcile completed symmetry counts and visually transcribed illustrations."""
from datetime import datetime, timezone
from fractions import Fraction
import json

from dlx1_audit_tools import ROOT, sha
from check_queen_rotations import problem, valid
from check_queen_pair_symmetry import oriented

OUT=ROOT/'results/queen_symmetry'


def main():
    val=json.loads((OUT/'validation.json').read_text())
    large=json.loads((OUT/'large-wrapper.json').read_text());assert large['status']=='finished'
    counts={v['n']:v for v in val['cases']}
    for c in large['cases']:
        path=OUT/(c['label']+'.json');assert sha(path)==c['result_sha256']
        counts[c['n']]=json.loads(path.read_text())
    rotations=json.loads((ROOT/'results/queen_rotations/verified.json').read_text())
    for n in range(4,18):
        r180=next(v for v in rotations['table_cases'] if v['n']==n and v['turn_degrees']==180 and v['rule']=='none')
        r90=next(v for v in rotations['table_cases'] if v['n']==n and v['turn_degrees']==90 and v['rule']=='none')
        assert counts[n]['half']==r180['solutions'] and counts[n]['quarter']==r90['solutions']
        assert counts[n]['total']==8*counts[n]['Qa']+4*counts[n]['Qs']+2*counts[n]['Qd']
    figures={'a':[5,3,6,9,2,8,1,4,7],'b':[1,4,6,3,9,2,8,5,7],'c':[1,8,4,2,7,9,6,3,5]}
    for case,p in figures.items():assert valid(list(enumerate(p,1)),9) and oriented(p,case)
    printed={
        (4,2):[[(1,2),(4,3)],[(1,3),(4,2)],[(2,1),(3,4)],[(2,4),(3,1)]],
        (4,1):[[(1,2),(2,4),(4,3),(3,1)],[(2,1),(3,4),(1,3),(4,2)]],
        (5,2):[[(1,2),(5,4)],[(1,4),(5,2)],[(2,1),(4,5)],[(2,5),(4,1)],[(3,3)]],
        (5,1):[[(1,2),(2,5),(5,4),(4,1)],[(2,1),(1,4),(4,5),(5,2)],[(3,3)]]}
    for (n,turn),groups in printed.items():
        assert {tuple(sorted(g)) for g in groups}==set(problem(n,turn)[2])
    c16=counts[16]['cases']['23a'];c17=counts[17]['cases']['23b']
    canon=(c16['total']+c16['half']+2*c16['quarter'])//8
    assert (c16['total'],c16['weak'],c16['stronger'],canon)==(454376,64374,59648,57188)
    assert (c17['total'],c17['weak'])==(4067152,577732)
    forced=(counts[16]['total']-c16['total']-8*counts[16]['cases']['22b']['oriented'])//8
    assert forced==1220918
    assert round(Fraction(43,12),2)==Fraction(358,100)
    report=dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
        table24=[{k:counts[n][k] for k in ['n','total','half','quarter','Qa','Qs','Qd']} for n in range(4,18)],
        figures22=figures,printed_option_groups24={f'n{n}-r{90*t}':g for (n,t),g in printed.items()},
        boundary_n16=dict(total=c16['total'],weak=c16['weak'],stronger=c16['stronger'],canonical=canon),
        boundary_n17=dict(total=c17['total'],weak=c17['weak']),
        ratios=dict(n16=float(Fraction(c16['total'],c16['weak'])),n17=float(Fraction(c17['total'],c17['weak'])),known_ratio_correction=str(Fraction(43,12))),
        answer22c_forced_by_partition=forced,
        input_hashes={str(p.relative_to(ROOT)):sha(p) for p in [OUT/'validation.json',OUT/'large-wrapper.json',ROOT/'results/queen_rotations/verified.json']})
    (OUT/'claims-verified.json').write_text(json.dumps(report,indent=2)+'\n')
    print('verified42 table entries,3 diagrams,4 option lists,23(a,b) counts, and the n16 partition identity')


if __name__=='__main__':main()

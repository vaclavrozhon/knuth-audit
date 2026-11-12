#!/usr/bin/env python3
"""Measure DLX24's specified rotational reductions under explicit orders."""
from datetime import datetime, timezone
import json

from dlx1_audit_tools import input_text, run, sha
from check_queen_rotations import problem, OUT


def main():
    cases=[]
    for n,turn,rule,expected in [(16,2,'half-corrected',1500),(16,1,'deduplicate',4),(32,1,'deduplicate',1589)]:
        names,rows,_=problem(n,turn,rule)
        for order in ['alternating','organ-pipe']:
            numbers=list(range(1,n+1)) if order=='alternating' else sorted(range(1,n+1),key=lambda i:(abs(2*i-n-1),-i))
            header=[v for i in numbers for v in [f'r{i}',f'c{i}']]
            data=input_text(names,rows,2*n).splitlines();data[0]=' '.join(header+['|']+names[2*n:])
            stats,_=run(OUT,f'n{n}-r{90*turn}-{rule}-{order}','\n'.join(data)+'\n')
            assert stats['solutions']==expected
            cases.append(dict(n=n,turn_degrees=90*turn,rule=rule,order=order,**stats))
    report=dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),cases=cases,
                scope='Explicit item orders for the correct geometric half cut or duplicate-row quarter reduction. No claim that these reconstruct the unpublished book inputs.')
    (OUT/'cost-comparison.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps([dict(label=x['label'],mems=x['search_mems']) for x in cases],indent=2))


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Check completed Langford measurements without rerunning their searches."""
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/langford_mems'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    validation=json.loads((OUT/'validation.json').read_text())
    assert validation['status']=='verified'
    assert validation['source_sha256']==sha(ROOT/'langford_mems.cpp')
    raw=json.loads((OUT/'loose15.json').read_text())
    assert raw['nodes']==396535288 and raw['representatives']==0
    literal=raw['mems_without_cached_L5_read']
    assert literal==raw['mems']+raw['nodes']-1
    # For n15 the symmetry label is the largest, 15, at position h=4.
    # The repaired L4 can skip one redundant p[15] read for each failing
    # prefix of length three. There are at most 15^3 such prefixes. The
    # simultaneous-forcing repair cannot fire because h=4<ceil(15/2)=8.
    guard_read_bound=15**3
    assert 9925000000<=literal<=literal+guard_read_bound<9935000000
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
        loose15=dict(verified=True,result_sha256=sha(OUT/'loose15.json'),
            nodes=raw['nodes'],mems_with_cached_L5_read=raw['mems'],
            uncached_mems_with_repaired_L4=literal,
            extra_reads_bound_for_original_L4=guard_read_bound,
            original_uncached_mems_interval=[literal,literal+guard_read_bound],
            rounded_book_gigamems='9.93'),large_cases=[])
    expected={
        'L21':dict(nodes_interval=[155000000000,165000000000],mems_interval=[3935000000000,3945000000000],per_node='24.6'),
        'L20':dict(nodes_interval=[325000000000,335000000000],mems_interval=[8050000000000,8150000000000],per_node='24.4'),
        'L':dict(nodes_interval=[1285000000000,1295000000000],mems_interval=[24950000000000,25050000000000],per_node='19.4'),
    }
    for mode,printed in expected.items():
        meta_path=OUT/f'n17-{mode}-run.json'
        meta=json.loads(meta_path.read_text()) if meta_path.exists() else {}
        entry=dict(mode=mode,status=meta.get('status','pending'),printed_rounding_intervals=printed)
        if meta.get('status')=='finished':
            path=OUT/f'n17-{mode}.json';assert sha(path)==meta['result_sha256']
            assert meta['source_sha256']==validation['source_sha256']
            value=json.loads(path.read_text());nodes=value['nodes'];mems=value['mems_without_cached_L5_read']
            assert value['representatives']==0 and nodes==sum(value['profile'])
            ratio=Fraction(mems,nodes);center=Fraction(printed['per_node'])
            entry.update(nodes=nodes,uncached_mems=mems,cached_mems=value['mems'],
                exact_uncached_mems_per_node=str(ratio),
                nodes_match_printed_rounding=printed['nodes_interval'][0]<=nodes<printed['nodes_interval'][1],
                mems_match_printed_rounding=printed['mems_interval'][0]<=mems<printed['mems_interval'][1],
                per_node_matches_printed_rounding=center-Fraction(1,20)<=ratio<center+Fraction(1,20))
        result['large_cases'].append(entry)
    result['all_large_cases_finished']=all(x['status']=='finished' for x in result['large_cases'])
    (OUT/'claims-checked.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()

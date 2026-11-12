#!/usr/bin/env python3
"""DLX63: every rainbow packing, with two explicit fault-line validators."""
from collections import Counter
from datetime import datetime,timezone
import gzip
import json
from dlx1_audit_tools import ROOT,sha,statistics
from check_sudoku_trios57 import bitset_covers

OUT=ROOT/'results/jigsaw/tilings'


def cuts_crossed(tile,n):
    rs=[v//n for v in tile];cs=[v%n for v in tile]
    return sum(1<<k for k in range(min(rs),max(rs)))|sum(1<<(n-1+k) for k in range(min(cs),max(cs)))


def explicit_faults(tiles,n):
    labels=[None]*(n*n)
    for i,tile in enumerate(tiles):
        for v in tile:assert labels[v] is None;labels[v]=i
    assert None not in labels
    h=[r for r in range(n-1) if all(labels[r*n+c]!=labels[(r+1)*n+c] for c in range(n))]
    v=[c for c in range(n-1) if all(labels[r*n+c]!=labels[r*n+c+1] for r in range(n))]
    return h,v


def main():
    raw=json.loads(gzip.decompress((OUT/'rainbow.json.gz').read_bytes()))
    rows=[[v+1 for v in r] for r in raw]
    models,profile=bitset_covers(rows,81)
    native=statistics((OUT/'rainbow-dlx1.log').read_text())
    assert len(models)==native['solutions']==98556
    assert native['profile']==[profile.get(i,0) for i in range(len(native['profile']))]
    diagrams=json.loads((ROOT/'results/jigsaw/pdf-diagrams.json').read_text())['sources']
    reference=diagrams['35c']['cells']
    square={tuple(9*(3*a+r)+3*b+c for r in range(3) for c in range(3)) for a in range(3) for b in range(3)}
    is_square=[tuple(row) in square for row in raw]
    crossed=[cuts_crossed(t,9) for t in raw]
    histogram=Counter();filtered=[];faultfree=[]
    for model in models:
        tiles=[raw[i] for i in model]
        assert len(tiles)==9
        assert all({reference[v] for v in t}==set('123456789') for t in tiles)
        faults=explicit_faults(tiles,9)
        crossing=0
        for i in model:crossing|=crossed[i]
        assert (not any(faults))==(crossing==(1<<16)-1)
        ordinary=sum(is_square[i] for i in model);histogram[ordinary]+=1
        if ordinary==0:
            filtered.append(model)
            if not any(faults):faultfree.append(model)
    assert len(filtered)==42669 and len(faultfree)==24533
    native_filtered=statistics((OUT/'rainbow-no-sudoku-dlx1.log').read_text())
    assert native_filtered['solutions']==len(filtered)
    printed=tuple(sorted(map(tuple,diagrams['63']['regions'])))
    lookup={tuple(t):i for i,t in enumerate(raw)}
    printed_model=tuple(sorted(lookup[t] for t in printed))
    assert printed_model in set(faultfree)
    with gzip.open(OUT/'rainbow-models.json.gz','wt') as f:json.dump(sorted(models),f)
    with gzip.open(OUT/'rainbow-faultfree-no-sudoku.json.gz','wt') as f:json.dump(sorted(faultfree),f)
    result=dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
                source_sha256=sha(__file__),helper_sha256=sha(ROOT/'check_sudoku_trios57.py'),
                options_sha256=sha(OUT/'rainbow.json.gz'),complete_packings=len(models),
                profile=profile,native=native,native_filtered=native_filtered,
                standard_box_histogram=dict(sorted(histogram.items())),without_standard_boxes=len(filtered),
                faultfree_without_standard_boxes=len(faultfree),printed_model=printed_model,
                models_sha256=sha(OUT/'rainbow-models.json.gz'),
                faultfree_sha256=sha(OUT/'rainbow-faultfree-no-sudoku.json.gz'))
    (OUT/'rainbow-verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS',len(models),len(filtered),len(faultfree),histogram,flush=True)


if __name__=='__main__':main()

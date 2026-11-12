#!/usr/bin/env python3
"""DLX23(a): audit the seven displayed boundary options and a full witness."""
from datetime import datetime, timezone
import json
import subprocess

from dlx1_audit_tools import ROOT, sha, input_text, decode_rows, validated_binary
from check_dlx_ordering import pair_lists
from check_queen_rotations import valid

OUT=ROOT/'results/queen_symmetry'


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    n=16
    # Coordinates transcribed from PDF420 and author PS124.
    printed=[(1,2),(2,16),(15,16),(16,2),(16,14),(2,1),(15,1)]
    corrected=[(1,2),(2,16),(15,16),(16,2),(16,15),(2,1),(15,1)]
    assert printed[0][1]==2  # The text's a is the actual column, not an option index.
    assert (1,1)[0]==(1,1)[1]  # a=1 would be a forbidden main-diagonal corner.
    beta0=set(pair_lists(7,0)[1]);beta1=set(pair_lists(7,1)[1])
    assert beta0=={1,2,4} and beta1=={2,4}
    for r,c in corrected[1:]:
        distance=min(r,n+1-r) if c in (1,n) else min(c,n+1-c)
        assert distance==2
    assert min(14,17-14)==3
    # Top-column3 and bottom-column14 have equal distance3, hence are allowed.
    # The printed extra y1 rejects that pair.
    alpha1=set(pair_lists(7,1)[0]);assert alpha1=={1}
    assert not alpha1 & beta1 and alpha1 & beta0=={1}
    names=[f'r{i}' for i in range(1,n+1)]+[f'c{j}' for j in range(1,n+1)]
    names += [f'a{s}' for s in range(2,2*n+1)]+[f'b{d}' for d in range(1-n,n)]
    index={name:i+1 for i,name in enumerate(names)}
    points=[];rows=[]
    for r in range(1,n+1):
        for c in range(1,n+1):
            if r==c or r+c==n+1:continue
            if r==1 and c!=3:continue
            if r==n and c!=14:continue
            if c==n and not 3<=r<14:continue
            if c==1 and not 3<=n+1-r<14:continue
            points.append((r,c));rows.append(tuple(index[name] for name in [f'r{r}',f'c{c}',f'a{r+c}',f'b{r-c}']))
    data=input_text(names,rows,2*n);inp=OUT/'answer23-witness.dlx';inp.write_text(data)
    command=[validated_binary(),'v129','m1','t1']
    run=subprocess.run(command,input=data,text=True,capture_output=True,check=True,timeout=120)
    (OUT/'answer23-witness.log').write_text(run.stderr)
    (OUT/'answer23-witness.out').write_text(run.stdout)
    models=decode_rows(run.stdout,names,rows);assert len(models)==1
    board=sorted(points[r] for r in next(iter(models)))
    assert valid(board,n) and all(r!=c and r+c!=n+1 for r,c in board)
    p=[c for r,c in board];a=p[0];b=p.index(n)+1;c=n+1-p[-1];d=n-p.index(1)
    assert a==c==3 and all(a<=x<n+1-a for x in [b,c,d])
    report=dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
        source_sha256=sha(__file__),printed_coordinates=printed,corrected_coordinates=corrected,
        corrected_a=2,printed_beta_for_16_14=sorted(beta0),correct_beta_for_16_14=sorted(beta1),
        wrong_option_replacement='r16 c15 a31 b1 y1 y2 y4',
        valid_full_witness=p,boundary_tuple=[a,b,c,d],
        command=command,binary_sha256=sha(command[0]),input_sha256=sha(inp),
        scope='The run stops after one witness; no total count is inferred. '
              'Every queen and the full weak boundary ordering are checked directly. '
              'For the distance2 group use a=2 and bottom-column15. If column14 is retained, '
              'its correct comparison items are y2,y4 instead of y1,y2,y4.')
    (OUT/'example23-verified.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__=='__main__':main()

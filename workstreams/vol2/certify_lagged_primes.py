"""Generate (not independently validate) ECPP certificates for p.550.

Usage: python3 certify_lagged_primes.py /path/to/gp
Each target has its own 1800 s timeout; completed certificates are resumable.
The separate verify_ecpp.py checks their mathematical content in Python.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
# k, l, coefficient of b^l, constant, author's mixing classification.
TABLE = [
    (57,17,-1,-1,'preferred'), (73,17,-1,-1,'preferred'),
    (86,62,-1,-1,'preferred'), (88,52,-1,-1,'preferred'),
    (95,61,-1,-1,'preferred'),
    (58,33,-1,1,'preferred'), (62,17,-1,1,'preferred'),
    (69,24,-1,1,'preferred'), (70,57,-1,1,'preferred'),
    (87,24,-1,1,'preferred'),
    (56,22,1,-1,'preferred'), (61,44,1,-1,'preferred'),
    (74,27,1,-1,'preferred'), (90,65,1,-1,'preferred'),
    (56,5,-1,-1,'less desirable'), (56,32,-1,-1,'less desirable'),
    (66,57,-1,-1,'less desirable'), (76,15,-1,-1,'less desirable'),
    (84,26,-1,-1,'less desirable'), (90,42,-1,-1,'less desirable'),
    (93,18,-1,-1,'less desirable'),
    (52,8,-1,1,'less desirable'), (60,12,-1,1,'less desirable'),
    (67,8,-1,1,'less desirable'), (67,63,-1,1,'less desirable'),
    (83,14,-1,1,'less desirable'),
    (65,2,1,-1,'less desirable'), (76,11,1,-1,'less desirable'),
    (88,30,1,-1,'less desirable'), (92,48,1,-1,'less desirable'),
]


def targets():
    b=2**32
    result=[dict(id=f'p550-{i:02}',base=b,k=k,l=l,lag_sign=s,
                 constant=t,mixing=c,value=b**k+s*b**l+t)
            for i,(k,l,s,t,c) in enumerate(TABLE,1)]
    b-=5
    result.append(dict(id='marsaglia-zaman-43-22',base=b,k=43,l=22,
                       lag_sign=-1,constant=1,value=b**43-b**22+1))
    return result


def main():
    gp=str(Path(sys.argv[1]).resolve())
    out=ROOT/'results/lagged-prime-certificates'
    out.mkdir(exist_ok=True)
    version=subprocess.run([gp,'--version'],capture_output=True,text=True,check=True)
    print(f'runner pid={os.getpid()}, GP={gp}',flush=True)
    manifest=dict(generator='PARI/GP primecert (ECPP)',
                  version=(version.stdout+version.stderr).strip(),
                  gp_sha256=hashlib.sha256(Path(gp).read_bytes()).hexdigest(),
                  started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                  per_target_timeout_seconds=1800,nbthreads=1,runner_pid=os.getpid(),targets=[])
    for target in targets():
        ident=target['id']; path=out/f'{ident}.json'
        if path.exists():
            row=json.loads(path.read_text())
            assert row['target']==target and row['certificate']
            print(f'{ident}: existing certificate',flush=True)
        else:
            print(f'{ident}: start, {target["value"].bit_length()} bits',flush=True)
            # Changing the maximum stack abandons the rest of its input line.
            code=('default(parisizemax,1073741824);\ndefault(nbthreads,1);\n'
                  f'c=primecert({target["value"]});print(c);quit;\n')
            start=time.monotonic()
            try:
                run=subprocess.run([gp,'-fq','-s','134217728'],input=code,
                                   text=True,capture_output=True,timeout=1800)
            except subprocess.TimeoutExpired as e:
                row=dict(target=target,status='timeout',elapsed_seconds=time.monotonic()-start)
                print(f'{ident}: timeout',flush=True)
            else:
                cert=json.loads(run.stdout.strip()) if run.returncode==0 and run.stdout.strip() else None
                row=dict(target=target,status='generated' if cert else 'failed',
                         elapsed_seconds=time.monotonic()-start,certificate=cert,
                         returncode=run.returncode,stderr=run.stderr)
                if cert:
                    path.write_text(json.dumps(row,indent=2)+'\n')
                print(f'{ident}: {row["status"]}, {row["elapsed_seconds"]:.2f}s',flush=True)
        manifest['targets'].append({k:v for k,v in row.items() if k!='certificate'})
        (ROOT/'results/lagged-primes-generation.json').write_text(json.dumps(manifest,indent=2)+'\n')
    assert all(r['status']=='generated' for r in manifest['targets'])
    print('ALL CERTIFICATES GENERATED; independent validation still required',flush=True)


if __name__=='__main__':
    main()

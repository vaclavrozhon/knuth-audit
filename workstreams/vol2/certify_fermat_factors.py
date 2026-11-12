"""Propose reproducible ECPP certificates for the factors on TAOCP 2 p.403.

The independent validator is verify_fermat_factors.py. Completed certificates
are reused; a failed or timed-out proposal is never a primality conclusion.
"""
from pathlib import Path
from math import prod
import datetime
import hashlib
import json
import os
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
KNOWN = {
    9: [2424833, 7455602825647884208337395736200454918783366342657],
    10: [45592577, 6487031809, 4659775785220018543264560743076778192897],
    11: [319489, 974849, 167988556341760475137, 3560841906445833920513],
    12: [114689, 26017793, 63766529, 190274191361, 1256132134125569],
    13: [2710954639361, 2663848877152141313, 3603109844542291969,
         319546020820551643220672513],
}


def targets():
    result = []
    for m, factors in KNOWN.items():
        N = (1 << (1 << m)) + 1
        cofactor, remainder = divmod(N, prod(factors))
        assert remainder == 0 and cofactor > 1
        values = factors + ([cofactor] if m <= 11 else [])
        for i, value in enumerate(values, 1):
            result.append(dict(id=f'F{m}-{i}', fermat_index=m, value=value))
    return result


def save(path, value):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value, indent=2) + '\n')
    temporary.replace(path)


def main():
    gp = str(Path(sys.argv[1]).resolve())
    timeout = 1800
    out = ROOT / 'results/fermat-factor-certificates'
    out.mkdir(exist_ok=True)
    version = subprocess.run([gp, '--version'], capture_output=True,
                             text=True, check=True)
    print(f'runner pid={os.getpid()}, GP={gp}', flush=True)
    manifest = dict(generator='PARI/GP primecert (ECPP)',
                    version=(version.stdout + version.stderr).strip(),
                    gp_sha256=hashlib.sha256(Path(gp).read_bytes()).hexdigest(),
                    started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    per_target_timeout_seconds=timeout, nbthreads=1,
                    runner_pid=os.getpid(), targets=[])
    for target in targets():
        ident = target['id']
        path = out / f'{ident}.json'
        if path.exists():
            row = json.loads(path.read_text())
            assert row['target'] == target and row['certificate']
            print(f'{ident}: existing certificate', flush=True)
        else:
            print(f'{ident}: start, {len(str(target["value"]))} digits', flush=True)
            code = ('default(parisizemax,1073741824);\n'
                    'default(nbthreads,1);\n'
                    f'c=primecert({target["value"]});print(c);quit;\n')
            start = time.monotonic()
            process = subprocess.Popen([gp, '-fq', '-s', '134217728'],
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, text=True)
            print(f'{ident}: GP pid={process.pid}, timeout={timeout}s', flush=True)
            try:
                stdout, stderr = process.communicate(code, timeout=timeout)
            except subprocess.TimeoutExpired:
                process.kill()
                stdout, stderr = process.communicate()
                row = dict(target=target, status='timeout', gp_pid=process.pid,
                           elapsed_seconds=time.monotonic()-start, stderr=stderr)
            else:
                try:
                    cert = json.loads(stdout.strip()) if process.returncode == 0 else None
                except json.JSONDecodeError:
                    cert = None
                row = dict(target=target, status='generated' if cert else 'failed',
                           elapsed_seconds=time.monotonic()-start, gp_pid=process.pid,
                           certificate=cert, returncode=process.returncode, stderr=stderr)
                if cert:
                    save(path, row)
            manifest['targets'].append({k: v for k, v in row.items() if k != 'certificate'})
            save(ROOT / 'results/fermat-factors-generation.json', manifest)
            print(f'{ident}: {row["status"]}, {row["elapsed_seconds"]:.2f}s', flush=True)
            continue
        manifest['targets'].append({k: v for k, v in row.items() if k != 'certificate'})
        save(ROOT / 'results/fermat-factors-generation.json', manifest)
    assert all(r['status'] == 'generated' for r in manifest['targets'])
    print('ALL CERTIFICATES GENERATED; independent validation still required', flush=True)


if __name__ == '__main__':
    main()

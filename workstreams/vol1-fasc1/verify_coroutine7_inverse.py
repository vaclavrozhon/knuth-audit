#!/usr/bin/env python3
"""First runs of the newly completed inverse translator; never repeat old tests."""
from pathlib import Path
from itertools import groupby
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import tarfile
import tempfile
import time

BASE = Path(__file__).resolve().parent
SOURCES = BASE / 'sources'
RESULTS = BASE / 'results'


def reference(raw):
    end = raw.index(b'.') + 1
    consumed = raw[:end]
    target = bytes(c for c in consumed if c > 32)
    assert target[-1:] == b'.'
    runs = [(c, len(list(g))) for c, g in groupby(target[:-1])]
    encoded = []
    L = 1  # Terminal single-character token.
    U = 0  # Count-one digit tokens.
    F = sum(n // 10 for c, n in runs)
    H = int(bool(runs) and runs[-1][1] % 10 != 0)
    D = sum(n % 10 != 0 for c, n in runs[:-1])
    starts = sum((n + 9) // 10 for c, n in runs)
    Z = starts - D
    S = sum(n for c, n in runs) - starts
    minimum = 1
    for c, n in runs:
        q, r = divmod(n, 10)
        digit = 48 <= c <= 57
        minimum += 2 * ((n + 9) // 10) if digit else 2*q + min(r, 2)
        encoded.extend(bytes([57, c, 10]) for _ in range(q))
        if r:
            if r == 1 and not digit:
                encoded.append(bytes([c, 10]))
                L += 1
            else:
                encoded.append(bytes([47 + r, c, 10]))
                U += int(r == 1)
    encoded.append(b'.\n')
    output = b''.join(encoded)
    T = len(encoded)
    W = sum(c <= 32 for c in consumed)
    N = len(target)
    R = len(consumed)
    # Separate direct decoder, stopping at the first produced period.
    code = bytes(c for c in output if c > 32)
    decoded = bytearray()
    i = 0
    while True:
        c = code[i]
        i += 1
        if 48 <= c <= 57:
            copies = c - 47
            c = code[i]
            i += 1
        else:
            copies = 1
        if c == 46:
            decoded.append(c)
            break
        decoded.extend([c] * copies)
    assert bytes(decoded) == target
    assert len(code) == minimum
    return output, {'consumed_bytes': R, 'whitespace_bytes': W,
                    'significant_characters_including_period': N,
                    'runs': [[c, n] for c, n in runs], 'full_tens': F,
                    'residual_at_period': H, 'changed_run_flushes': D,
                    'empty_run_starts': Z, 'same_run_characters': S,
                    'tokens_including_period': T, 'single_tokens': L,
                    'count_one_digit_tokens': U,
                    'minimum_non_newline_characters': minimum,
                    'output_bytes': len(output),
                    'expected_mems': R + 2*T - L,
                    'expected_oops': 12*W + 16*N + 6*Z + 9*D + 8*S + 7*F + H + 15 + 17*T + 3*U}


def cases():
    edge = b'!' + b'A'*9 + b'B'*10 + b'C'*11 + b'0' + b'1'*9 + b'2'*10 + b'3'*11 + bytes([255])*21 + b'.'
    # Includes all whitespace byte values, both sides of the ten-character
    # boundary, count-one digits, and the largest byte value.
    edge = bytes(range(33)) + b'\x00\t\r\n '.join(bytes([c]) for c in edge) + b'IGNORED'
    return {'empty': b'.\n',
            'book-example': b'abb bee eee e44 446 66f gzy w22 220 0pq 999 999 999 r.\n',
            'boundaries': edge}


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, 'Run with nice -n15.'
    start = time.monotonic()
    logs = []
    result = {'checked_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'scope': 'First native runs of one new complete MMIX inverse translator on three targeted cases. No old decoder or SAVE proof/checker is rerun.',
              'source_sha256': hashlib.sha256((SOURCES/'coroutine7-inverse.mms').read_bytes()).hexdigest(),
              'runs': {}}

    def checkpoint():
        (RESULTS/'coroutine7-inverse-build-and-run.json').write_text(json.dumps(logs, indent=2)+'\n')
        (RESULTS/'coroutine7-inverse-program.json').write_text(json.dumps(result, indent=2)+'\n')

    def run(command, cwd, timeout=30):
        tick = time.monotonic()
        p = subprocess.run(command, cwd=cwd, capture_output=True, timeout=timeout)
        logs.append({'command': command, 'returncode': p.returncode,
                     'stdout': p.stdout.decode('utf-8', 'backslashreplace'),
                     'stderr': p.stderr.decode('utf-8', 'backslashreplace'),
                     'elapsed_seconds': time.monotonic()-tick})
        checkpoint()
        p.check_returncode()
        return p

    with tempfile.TemporaryDirectory(prefix='coroutine7-first-build-', dir=RESULTS) as tmp:
        build = Path(tmp)
        with tarfile.open(SOURCES/'mmix-20250620.tar.gz') as archive:
            for name in ['Makefile', 'mmixal.w', 'mmix-arith.w', 'mmix-io.w', 'mmix-sim.w', 'abstime.w', 'boilerplate.w']:
                (build/name).write_bytes(archive.extractfile(name).read())
        run(['make', 'basic', 'CFLAGS=-O0'], build)
        shutil.copyfile(SOURCES/'coroutine7-inverse.mms', build/'inverse.mms')
        run([str(build/'mmixal'), '-b250', '-l', 'inverse.lst', '-o', 'inverse.mmo', 'inverse.mms'], build)
        (RESULTS/'coroutine7-inverse-listing.txt').write_text((build/'inverse.lst').read_text())
        result['object_sha256'] = hashlib.sha256((build/'inverse.mmo').read_bytes()).hexdigest()
        for name, raw in cases().items():
            expected, ref = reference(raw)
            input_path = RESULTS/('coroutine7-'+name+'-input.bin')
            input_path.write_bytes(raw)
            (RESULTS/('coroutine7-'+name+'-expected.bin')).write_bytes(expected)
            p = run([str(build/'mmix'), '-q', '-P', '-f'+str(input_path), 'inverse.mmo'], build, timeout=10)
            (RESULTS/('coroutine7-'+name+'-profile.bin')).write_bytes(p.stdout)
            ref['every_output_byte_agrees'] = p.stdout.startswith(expected)
            ref['input_sha256'] = hashlib.sha256(raw).hexdigest()
            result['runs'][name] = ref
            stats = re.findall(rb'(\d+) instructions?, (\d+) mems?, (\d+) oops?;', p.stdout)
            checkpoint()
            assert len(stats) == 1, (name, stats)
            ref['instructions'], ref['mems'], ref['oops'] = map(int, stats[0])
            checkpoint()
            assert ref['every_output_byte_agrees'], name
            assert (ref['mems'], ref['oops']) == (ref['expected_mems'], ref['expected_oops']), (name, ref)
        result['elapsed_seconds'] = time.monotonic()-start
        checkpoint()
    print(json.dumps({'runs': {name: {k: v for k, v in r.items() if k != 'runs'} for name, r in result['runs'].items()},
                      'elapsed_seconds': result['elapsed_seconds']}, indent=2))


if __name__ == '__main__':
    main()

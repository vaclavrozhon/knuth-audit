#!/usr/bin/env python3
"""Losslessly archive a finished, independently verified binary DRAT proof.

The raw proof is removed only after a complete decompression reproduces its
SHA256 and byte count, and the archive metadata has been written atomically.
This does not rerun the SAT solver or the proof checker.
"""
from datetime import datetime, timezone
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import os
import sys


def digest_file(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            digest.update(block)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run_json', type=Path)
    args = parser.parse_args()
    path = args.run_json.resolve()
    result = json.loads(path.read_text())
    if (result.get('status') != 'UNSAT' or result.get('proof_check') != 'verified'
            or result.get('proof_returncode') != 0):
        raise ValueError('Only a completed, independently verified proof may be archived.')
    raw = path.parent / result['proof_file']
    archive = raw.with_suffix(raw.suffix + '.gz')
    temporary = archive.with_suffix(archive.suffix + '.partial')
    if archive.exists():
        raise FileExistsError(archive)
    before = raw.stat()
    digest = hashlib.sha256()
    length = 0
    with raw.open('rb') as source, temporary.open('xb') as target:
        with gzip.GzipFile(filename='', mode='wb', compresslevel=6,
                           fileobj=target, mtime=0) as compressed:
            for block in iter(lambda: source.read(1024 * 1024), b''):
                digest.update(block)
                length += len(block)
                compressed.write(block)
        target.flush()
        os.fsync(target.fileno())
    after = raw.stat()
    if (before.st_ino, before.st_size, before.st_mtime_ns) != (
            after.st_ino, after.st_size, after.st_mtime_ns):
        raise ValueError('The raw proof changed during compression.')
    if length != result['proof_bytes']:
        raise ValueError('Raw proof size differs from the completed run metadata.')
    decoded = hashlib.sha256()
    decoded_length = 0
    with gzip.open(temporary, 'rb') as source:
        for block in iter(lambda: source.read(1024 * 1024), b''):
            decoded.update(block)
            decoded_length += len(block)
    if (decoded.hexdigest(), decoded_length) != (digest.hexdigest(), length):
        raise ValueError('The decoded archive does not reproduce the original proof.')
    temporary.replace(archive)
    result.update(
        proof_archive=archive.name,
        proof_sha256=digest.hexdigest(),
        proof_archive_sha256=digest_file(archive),
        proof_archive_bytes=archive.stat().st_size,
        proof_archive_verified_at_utc=datetime.now(timezone.utc).isoformat(),
        proof_archive_command=[sys.executable, str(Path(__file__).resolve()), str(path)],
        proof_archive_script_sha256=digest_file(Path(__file__)),
        proof_reproduction='Decompress gzip to the original .drat path before invoking '
                           'the recorded drat-trim command.')
    new_metadata = path.with_suffix('.json.partial')
    with new_metadata.open('x') as target:
        json.dump(result, target, indent=2)
        target.write('\n')
        target.flush()
        os.fsync(target.fileno())
    new_metadata.replace(path)
    raw.unlink()
    print(json.dumps({key: value for key, value in result.items()
                      if key.startswith('proof_')}, indent=2), flush=True)


if __name__ == '__main__':
    main()

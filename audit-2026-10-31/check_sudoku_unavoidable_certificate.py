#!/usr/bin/env python3
"""Replay trade witnesses, antichain property, and checked proof identities."""
from collections import Counter
from datetime import datetime, timezone
import gzip
import hashlib
import json
from dlx1_audit_tools import ROOT, sha

OUT = ROOT/'results/sudoku_variants/unavoidable55'


def clauses(path):
    return [[int(x) for x in line.split()[:-1]] for line in path.read_text().splitlines()
            if line and not line.startswith(('p','c'))]


def main():
    meta = json.loads((OUT/'run.json').read_text())
    assert meta['status'] == 'verified'
    trades = json.loads((OUT/'trades.json').read_text())
    board = json.loads((ROOT/'results/sudoku_basics/pdf-grids.json').read_text())['sources']['28b']['board']
    masks = []
    for trade in trades:
        s = trade['alternative']
        assert len(s) == 81
        assert all(set(s[9*i:9*i+9]) == set(range(1,10)) and
                   {s[9*j+i] for j in range(9)} == set(range(1,10)) for i in range(9))
        assert all({s[9*(3*b+i)+3*c+j] for i in range(3) for j in range(3)} == set(range(1,10))
                   for b in range(3) for c in range(3))
        differences = [v for v in range(81) if board[v] != s[v]]
        assert differences == trade['positions'] and 0<len(differences)<=18
        masks.append(sum(1<<v for v in differences))
    assert len(masks) == len(set(masks)) == 2043
    assert all(a&b not in (a,b) for i,a in enumerate(masks) for b in masks[i+1:])
    enumeration = clauses(OUT/'enumeration-exhaustive.cnf')
    hitting = clauses(OUT/'no19clues.cnf')
    assert enumeration[-len(trades):] == [[9*v+board[v] for v in t['positions']] for t in trades]
    assert hitting[:len(trades)] == [[v+1 for v in t['positions']] for t in trades]
    for label,key in [('enumeration-exhaustive','enumeration_certificate'),('no19clues','no19_certificate')]:
        proof = meta[key]
        assert sha(OUT/(label+'.cnf')) == proof['cnf_sha256']
        assert sha(OUT/(label+'.drat.gz')) == proof['compressed_proof_sha256']
        with gzip.open(OUT/(label+'.drat.gz'),'rb') as stream:
            assert hashlib.file_digest(stream,'sha256').hexdigest() == proof['proof_sha256']
        assert 's VERIFIED' in (OUT/(label+'-verify.log')).read_text()
    result = dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
                  trades_sha256=sha(OUT/'trades.json'),proof_manifest_sha256=sha(OUT/'run.json'),
                  trade_count=len(trades),size_distribution=dict(Counter(t.bit_count() for t in masks)),
                  pairwise_antichain_checks=len(masks)*(len(masks)-1)//2,
                  argument='All2043 sets have valid alternative-grid witnesses and are an antichain. '
                           'The independently checked exhaustive DRAT proof says every alternative changing at most18 cells '
                           'contains one listed set. Hence every listed set is minimal: a smaller alternative would contain '
                           'another listed set, contradicting the antichain. The second checked DRAT proof excludes '
                           'a hitting set of at most19 clues, using independently proved two-per-critical-group constraints.',
                  scope='Replays witness data and proof hashes; does not repeat the already successful DRAT verifier runs.')
    (OUT/'certificate-replay.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Verified2043 witnesses,2085903 antichain pairs, bothCNF boundaries and both checked DRAT archives.')


if __name__ == '__main__':
    main()

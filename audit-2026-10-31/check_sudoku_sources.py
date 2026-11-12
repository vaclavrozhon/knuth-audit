#!/usr/bin/env python3
"""Recheck the archived primary-source grids from de Ruiter and Boyer."""
from datetime import datetime, timezone
import json
import re
from check_sudoku_basics import OUT, UNITS, DIGITS, all_solutions
from dlx1_audit_tools import ROOT, sha


def main():
    sources = json.loads((OUT/'pdf-grids.json').read_text())['sources']
    p = ROOT/'sources/sudoku/puzzle346.json'; d = json.loads(p.read_text())
    grid = d['puzcode'].split('grid 9 9',1)[1].split('{',1)[1].split('}',1)[0]
    tokens = re.findall(r'\br([f1-9])\b',grid); assert len(tokens) == 81
    board = [0 if t == 'f' else int(t) for t in tokens]
    digits = ''.join(str(k) for k in board if k)
    assert digits == json.loads((OUT/'pi.json').read_text())['first_33_digits'][:32]
    models = all_solutions(board); assert len(models) == 1
    assert board != sources['29a']['board']
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=sha(__file__),
                  helper_sha256=sha(ROOT/'check_sudoku_basics.py'), puzzle_record_sha256=sha(p),
                  published_at=d['publishedAt'], author_username=d['authorUsername'],
                  board=board, clue_digits=digits, solution=models[0],
                  assessment='Primary record confirms July7 2007 and32 pi digits. This is a different grid '
                  'from29a; the book does not claim they are identical. Global historical priority not established.')
    (OUT/'de-ruiter.json').write_text(json.dumps(result,indent=2)+'\n')
    # All81 values manually read from the embedded original newspaper photograph.
    rows = ['789123456','312645978','564897231','897231564','123456789',
            '645978312','978312645','231564897','456789123']
    board = [int(c) for row in rows for c in row]
    assert all({board[v] for v in unit} == DIGITS for unit in UNITS)
    order = [4,2,6,5,0,7,3,1,8]
    assert [board[9*r+c] for r in order for c in range(9)] == sources['28c']['board']
    image_path = ROOT/'images/boyer-la-france-1895-solution.jpg'
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=sha(__file__),
                  primary_pdf_sha256=sha(ROOT/'sources/sudoku/boyer-solutions.pdf'),
                  image_path=str(image_path.relative_to(ROOT)), image_sha256=sha(image_path),
                  board=board, row_permutation_to28c=order, units_checked=27,
                  assessment='All81 digits transcribed from the original La France solution reproduced by Boyer. '
                  'A row permutation gives28c exactly. Original question asks for line and diagonal sums, '
                  'without3x3 box conditions. English2007 metadata verified; exact page63 not accessed.')
    (OUT/'boyer-pattern.json').write_text(json.dumps(result,indent=2)+'\n')
    print('de Ruiter: one complete solution; Boyer:81 digits and27 units, exact row permutation to28c.')


if __name__ == '__main__':
    main()

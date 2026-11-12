"""Reproduce the fixed L3 missing-backup witness using the archived author source.

The first variant only logs; the second inserts the book's conditional save
and guards unsaved reads. No assertion about an unguarded wrong SAT answer.
"""
from pathlib import Path
import subprocess, tempfile, shutil, json
base = Path(__file__).resolve().parent
out = base / 'results/bookwise-sat-l3'
with tempfile.TemporaryDirectory(prefix='bookwise-sat-l3-') as tmp:
    work = Path(tmp)
    for name in ['gb_flip.w', 'boilerplate.w']:
        shutil.copy(base / 'sources/knuth-programs' / name, work / name)
    subprocess.run(['ctangle', 'gb_flip.w'], cwd=work, check=True,
                   stdout=subprocess.DEVNULL, timeout=20)
    results = []
    for stem, expected in [('sat11-instrumented', 0), ('sat11-book-l3-guarded', 91)]:
        shutil.copy(out / (stem + '.w'), work / (stem + '.w'))
        subprocess.run(['ctangle', stem + '.w'], cwd=work, check=True,
                       stdout=subprocess.DEVNULL, timeout=20)
        subprocess.run(['gcc', '-O2', '-w', stem + '.c', 'gb_flip.c', '-o', stem],
                       cwd=work, check=True, timeout=20)
        run = subprocess.run(['nice', '-n', '15', str(work / stem), 'v3', 'm20',
                              'T10000000'], input=(out / 'witness.sat').read_text(),
                             text=True, capture_output=True, timeout=5)
        assert run.returncode == expected, run.stderr
        marker = 'F207_BRANCHLESS_READ' if expected == 0 else 'BOOK_L3_UNSAVED_BACKF'
        events = [s for s in run.stderr.splitlines() if s.startswith(marker)]
        assert events
        results.append({'variant': stem, 'returncode': run.returncode, 'events': events})
    print(json.dumps(results, indent=2))

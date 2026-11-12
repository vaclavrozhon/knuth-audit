"""Short source-level checks for162; no queen-placement census."""
from datetime import datetime, timezone
from pathlib import Path
import json
from check_nested_queens import valid, occurrences, orbit
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/nested162'


def main():
    assert not (OUT / 'claims-checked.json').exists()
    # Direct transcription of Ahrens, Fig24, printed258, in the1921 anastatic edition.
    p = (5, 7, 4, 6, 14, 16, 13, 15, 8, 1, 3, 0, 2, 10, 12, 9, 11)
    assert valid(list(enumerate(p))) and p[8] == 8
    blocks = occurrences(p, 4)
    assert blocks == [(0, 4), (4, 13), (9, 0), (13, 9)]
    queens = set(enumerate(p))
    assert {(c, 16-r) for r, c in queens} == queens
    archive = ROOT / 'results/nested_queens/independent-n17-q4-t4.jsonl'
    models = [tuple(json.loads(line)) for line in archive.read_text().splitlines()]
    assert p in models
    overlap = json.loads((ROOT / 'results/nested_queens/overlap.json').read_text())
    assert [len(row['patterns']) for row in overlap] == [2, 10, 4]
    five = next(row['patterns'] for row in overlap if row['k'] == 5)
    # Read the accepted ten small patterns to classify the wording in the question.
    q5_with_q4 = [q for q in five if occurrences(q, 4)]
    assert len(q5_with_q4) == 8
    native_small = json.loads((ROOT / 'results/nested_queens/n5-q4-t1.json').read_text())
    assert native_small['complete'] and native_small['distinct_models'] == 8
    offsets = [(0, 1), (1, 3), (2, 0), (3, 2)]
    assert valid(offsets)
    correct_diagonals = [(r+c, r-c) for r, c in offsets]
    assert correct_diagonals == [(1, -1), (4, -2), (2, 2), (5, 1)]
    printed_diagonals = [(1, -1), (3, -3), (2, 2), (5, 1)]
    assert [i for i in range(4) if correct_diagonals[i] != printed_diagonals[i]] == [1]
    classification = json.loads((ROOT / 'results/nested_queens/classification.json').read_text())
    assert [(x['positions'], x['D4_classes'], x['collapsed_positions'], x['collapsed_D4_classes']) for x in classification] == [
        (144, 19, 36, 5), (288, 42, 18, 4), (896, 116, 224, 30)]
    sources = ['check_nested_queens.py', 'results/nested_queens/overlap.json', 'results/nested_queens/n5-q4-t1.json',
        'results/nested_queens/classification.json', str(archive.relative_to(ROOT)), 'images/nested162-ahrens-pdf271.png']
    save(OUT / 'claims-checked.json', dict(at_utc=datetime.now(timezone.utc).isoformat(), checker_sha256=sha(__file__),
        source_hashes={p: sha(ROOT / p) for p in sources},
        ahrens=dict(edition=3, year=1921, printed_page=258, pdf_page=271, figure=24, columns=p,
                    Q4_blocks=blocks, central_queen=[8, 8], quarter_turn_invariant=True, accepted_archive_line=models.index(p)+1),
        question_Q5_patterns=10, containing_Q4=8, printed_diagonal_offsets=printed_diagonals,
        corrected_diagonal_offsets=correct_diagonals, all_census_results_preserved=True, new_placement_searches=0))
    print('PASS162 claims: Ahrens Fig24 is archived Q17 pinwheel;8 of10 Q5 patterns containQ4; known diagonal correction confirmed. No search.')


if __name__ == '__main__':
    main()

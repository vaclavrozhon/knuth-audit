"""Verify the saved F068 counterexample directly, without any solver or search."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def main():
    path = ROOT / 'results/partridge_rectangles/n6-better-witness.json'
    witness = json.loads(path.read_text())
    height, width = witness['rows'], witness['columns']
    assert (height, width) == (16, 28)
    assert set(witness['piece_positions']) == set(map(str, range(1, 7)))
    occupied = set()
    for side in range(1, 7):
        positions = witness['piece_positions'][str(side)]
        assert len(positions) == side
        for row, column in positions:
            assert 0 <= row <= height-side and 0 <= column <= width-side
            square = {(r, c) for r in range(row, row+side) for c in range(column, column+side)}
            assert not occupied & square
            occupied |= square
    blank = {(r, c) for r in range(height) for c in range(width)} - occupied
    assert blank == set(map(tuple, witness['empty_cells']))
    assert len(occupied) == 441 and len(blank) == 7
    assert width*height == 448 < 30*15 == 450
    print(json.dumps(dict(valid=True, pieces=21, covered=441, empty=7, witness_area=448,
        printed_rectangle_area=450, smaller_by=2, search_calls=0,
        witness_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()), indent=2))


if __name__ == '__main__':
    main()

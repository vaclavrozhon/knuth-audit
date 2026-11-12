"""Check archived denominators and short witnesses, without rerunning searches."""

import datetime
from fractions import Fraction
import gzip
import hashlib
import json
from math import gcd
from pathlib import Path
import struct
import time

ROOT = Path(__file__).resolve().parent


def fraction(digits):
    value = Fraction(0)
    for digit in reversed(digits):
        assert digit >= 1
        value = 1 / (digit + value)
    return value


def main():
    started = time.monotonic()
    archive = json.loads((ROOT / "results/continuants.json").read_text())
    arrays = []
    for alphabet in (2, 3):
        census = archive[f"census{alphabet}"]
        limit = census["limit"]
        for convention, saved in census["conventions"].items():
            data = gzip.decompress((ROOT / saved["compressed_array"]).read_bytes())
            digest = hashlib.sha256(data).hexdigest()
            assert digest == saved["raw_sha256"]
            assert len(data) == 4 * (limit + 1)
            positive = 0
            missing = []
            blocks = [0] * 64
            for denominator, (numerator,) in enumerate(struct.iter_unpack("<I", data)):
                if denominator < 2:
                    assert numerator == 0
                    continue
                if numerator:
                    assert 0 < numerator < denominator
                    positive += 1
                    if alphabet == 2:
                        blocks[(denominator - 1) // 16384] += 1
                elif alphabet == 3:
                    missing.append(denominator)
            assert positive == saved["witnesses_checked"]
            result = dict(alphabet=alphabet, convention=convention, limit=limit,
                          raw_sha256=digest, positive_denominators_from_2=positive)
            if alphabet == 3:
                assert missing == saved["missing"]
                witnesses = saved["exact_minima_for_missing"]
                assert [row["m"] for row in witnesses] == missing
                for row in witnesses:
                    assert max(row["digits"]) == row["bound"]
                    assert fraction(row["digits"]) == Fraction(row["numerator"], row["m"])
                    assert gcd(row["numerator"], row["m"]) == 1
                result["missing"] = missing
                result["exception_witnesses_checked"] = len(witnesses)
            else:
                blocks[0] += 1  # denominator 1, represented by the word (1)
                assert blocks == saved["block_counts"]
                assert str(Fraction(min(blocks), 16384)) == saved["min_density"]
                assert str(Fraction(max(blocks), 16384)) == saved["max_density"]
                result["block_counts"] = blocks
            arrays.append(result)

    powers = []
    for exponent in range(25, 36):
        row = archive[f"power{exponent}"]
        digits = row["witness_digits"]
        numerator = row.get("witness_numerator", row["solutions"][0] if row["solutions"] else None)
        assert row["m"] == 2 ** exponent
        assert max(digits) <= 2
        assert gcd(numerator, row["m"]) == 1
        assert fraction(digits) == Fraction(numerator, row["m"])
        powers.append(dict(exponent=exponent, numerator=numerator,
                           denominator=row["m"], digits=digits,
                           canonical_terminal_digit=digits[-1] >= 2))

    result = dict(
        checked_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        seconds=time.monotonic() - started,
        scope="Archive integrity/counts and 65 exception plus 11 power witnesses. "
              "No word census, all-numerator search, or full positive-witness validation rerun. "
              "Exception minimality and completeness rely on the separately reviewed original programs and logs.",
        arrays=arrays, powers=powers,
    )
    destination = ROOT / "results/sequential-continuant-certificates.json"
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(dict(result=str(destination), arrays=len(arrays),
                          exception_witnesses=65, power_witnesses=len(powers),
                          seconds=result["seconds"])))


if __name__ == "__main__":
    main()

"""Check completed word-rectangle runs and independently bound their mem costs.

This does not repeat the large enumerations. The bound uses only the printed
profiles/rounded averages and the explicit per-step accesses of answer 25 /
BACK-MXN-WORDS-NEW. See WORD_RECTANGLE_NOTES.md, finding F102.
"""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction
import hashlib
import json
import math
import re

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/word_rectangles'
SOURCE = ROOT/'sources/knuth-programs/back-mxn-words-new.w'

EXPECTED = {
    '5x6': dict(m=5, profile=[1, 5757, 2458830, 360728099, 579940198, 29621728, 625415],
                averages=['5757.0', '1697.9', '844.1', '273.5', '153.5', '100.8'],
                printed_teramems='1.15'),
    '6x5': dict(m=6, profile=[1, 15727, 8072679, 630967290, 90962081, 625415],
                averages=['15727.0', '4321.6', '1749.7', '450.4', '286.0'],
                printed_teramems='18.3'),
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    source_metadata = json.loads(SOURCE.with_suffix('.w.json').read_text())
    assert sha(SOURCE) == source_metadata['sha256']
    certificate = dict(status='pass', checked_at_utc=datetime.now(timezone.utc).isoformat(),
                       source=str(SOURCE.relative_to(ROOT)), source_sha256=sha(SOURCE),
                       source_last_modified=source_metadata['last_modified'], cases=[])
    for dimensions, expected in EXPECTED.items():
        label = 'column-'+dimensions
        path = OUT/(label+'.json')
        got = json.loads(path.read_text())
        cell = json.loads((OUT/('cell-'+dimensions+'.json')).read_text())
        meta = json.loads((OUT/(label+'-run.json')).read_text())
        logpath = OUT/(label+'.log')
        log = logpath.read_text()
        assert got['verified'] and meta['returncode'] == 0
        assert got['profile'] == expected['profile']
        assert got['weights'][:-1] == [float(x) for x in expected['averages']]
        assert got['weights'][-1] == 0
        assert got['count'] == meta['validated_solutions'] == 625415
        assert got['repeated_words'] == 1618
        # Two algorithms already validate every model and reject duplicates.
        # These fingerprints supplement that validation; they are not a proof
        # that two arbitrary sets are equal.
        compared = ['count', 'repeated_words', 'sha256_xor', 'sha256_sum']
        assert all(got[k] == cell[k] for k in compared)
        match = re.search(r'Altogether (\d+) solutions \((\d+) mems\)', log)
        assert match and [int(x) for x in match.groups()] == [got['count'], got['mems']]
        initialization = int(re.search(r'\((\d+) mems to initialize', log)[1])
        m = expected['m']
        nonterminal = sum(expected['profile'][:-1])
        edges = sum(expected['profile'][1:])
        # A rounded one-decimal average w is at most w+0.05. Use ceil rather
        # than any floating-point operation; retaining the endpoint is safe.
        trial_upper = sum(math.ceil(count*(Fraction(average)+Fraction(1, 20)))
                          for count, average in zip(expected['profile'][:-1],
                                                    expected['averages']))
        # At a node: m*(2 pointer/signature loads + <=26 list sizes), then
        # <=26 head loads. At a trial: word load + <=m*(2 reads+1 write)
        # + next-link load. At a successful edge: 3 saves + 4 restores.
        # Initialization includes dictionary construction; another m stores
        # initialize the zero-depth row pointers.
        node_cost = 28*m+26
        trial_cost = 3*m+2
        edge_cost = 7
        upper = initialization+m+node_cost*nonterminal+trial_cost*trial_upper+edge_cost*edges
        assert got['mems'] <= upper
        printed = Fraction(expected['printed_teramems'])*10**12
        certificate['cases'].append(dict(
            dimensions=dimensions, result=path.name, result_sha256=sha(path),
            run_metadata_sha256=sha(OUT/(label+'-run.json')), log_sha256=sha(logpath),
            matches_profile_and_averages=True, cell_fingerprint_fields=compared,
            mems=got['mems'], initialization_mems=initialization,
            nonterminal_nodes=nonterminal, successful_edges=edges,
            trial_upper_from_printed_rounding=trial_upper,
            node_cost_bound=node_cost, trial_cost_bound=trial_cost, edge_cost=edge_cost,
            search_and_initialization_upper_bound=upper,
            printed_teramems=expected['printed_teramems'],
            printed_value_exceeds_upper_bound=printed>upper))
    five, six = certificate['cases']
    assert not five['printed_value_exceeds_upper_bound']
    assert six['printed_value_exceeds_upper_bound']
    assert Fraction(1145, 1000) <= Fraction(five['mems'], 10**12) < Fraction(1155, 1000)
    assert Fraction(1825, 1000) <= Fraction(six['mems'], 10**12) < Fraction(1835, 1000)
    certificate['correction'] = 'Answer 27: 18.3 teramems -> 1.83 teramems.'
    (OUT/'costs-verified.json').write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(certificate, indent=2))


if __name__ == '__main__':
    main()

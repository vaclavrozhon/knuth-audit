"""One new exact counterexample; never reruns the archived MIX census."""
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path

from mix_float_machine import Machine


def main():
    root = Path(__file__).resolve().parent
    output = root / 'results/C0251-sticky-overflow.json'
    if output.exists():
        raise SystemExit('Saved witness already exists; do not rerun it.')
    radix, precision, excess = 100, 4, 50
    u, v = (50, 99999950, 1), (48, 50000001, 1)
    machine = Machine(radix)
    machine.load_float(u, location='ACC')
    machine.load_float(v, reg='A')
    snapshots = []
    wanted = {'A22', 'A23', 'A24', 'A49', 'A50', 'A51',
              'A52', 'A55', 'A57', 'A58', 'A62', 'A66'}

    def observe(state, row):
        if row in wanted:
            snapshots.append({
                'before_row': row,
                'A': [state.reg['A'].sign, state.reg['A'].mag],
                'X': [state.reg['X'].sign, state.reg['X'].mag],
                'I2': state.reg['2'].val,
                'overflow': state.ov,
            })

    machine.observer = observe
    machine.execute('FADD')
    # Independent rational value and the two adjacent output candidates.
    exact_u = Fraction(u[1], radix**precision)
    exact_v = Fraction(v[1], radix**(precision + 2))
    exact_sum = exact_u + exact_v
    lower = Fraction(1000049, radix**precision) * radix
    upper = Fraction(1000050, radix**precision) * radix
    midpoint = (lower + upper) / 2
    got = machine.output_float()
    assert machine.halt is None
    assert got == (51, 1000049, 1)
    assert machine.memory[machine.symbols['ACC']] == machine.reg['A']
    assert lower < exact_sum < upper
    assert exact_sum - midpoint == Fraction(1, 10**12)
    assert upper - exact_sum < exact_sum - lower
    assert snapshots[3]['before_row'] == 'A49'
    assert snapshots[3]['X'][1] == 100000000
    assert any(s['before_row'] == 'A52' and s['X'][1] == 0 for s in snapshots)
    result = {
        'checked_at_utc': datetime.now(timezone.utc).isoformat(),
        'new_targeted_machine_executions': 1,
        'archived_census_rerun': False,
        'radix': radix, 'precision': precision, 'excess': excess,
        'u': u, 'v': v, 'actual': got, 'nearest': [51, 1000050, 1],
        'exact_sum': str(exact_sum),
        'lower': str(lower), 'upper': str(upper),
        'distance_lower': str(exact_sum - lower),
        'distance_upper': str(upper - exact_sum),
        'above_midpoint': str(exact_sum - midpoint),
        'snapshots': snapshots, 'executed_rows': machine.trace,
        'source_sha256': {
            path: sha256((root / path).read_bytes()).hexdigest()
            for path in ['sources/single-precision.mix', 'mix_float_machine.py']
        },
        'scope': '2002-corrected transcription; exact arithmetic proves upper neighbor is closer. The N4 instructions are unchanged from the original printing.',
    }
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in
                      ['new_targeted_machine_executions', 'actual', 'nearest',
                       'distance_lower', 'distance_upper', 'above_midpoint']}))


if __name__ == '__main__':
    main()

"""New signed-zero boundary of the2018 answer; no old test suite is rerun."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1]))
from mix_machine import Machine, Word, number

ROWS = [('ENT1', 45), ('SLA', 1), ('ST1', 3003, 0, (4, 4)),
        ('ADD', 200), ('DEC1', 9), ('J1P', 3001), ('HLT', 0)]
cases = []
for radix in range(64, 101):
    for initial_sign, value, fix in [(-1, 0, False), (1, 0, False),
                                    (-1, 1, False), (-1, 0, True)]:
        m = Machine(radix)
        m.reg[0] = number(0, radix, initial_sign)
        m.reg[7] = Word(-1, (radix-1,)*5)
        for j in range(1, 7):
            m.reg[j] = number(-(radix**2-1), radix)
        m.mem[200] = number(value, radix)
        m.program(3000, ROWS)
        if fix:
            m.program(2999, [('ENTA', 0)])
        m.pc = 2999 if fix else 3000
        trace = []
        while not m.halted:
            pc = m.pc
            m.step()
            if pc in (3001, 3003):
                trace.append({'pc': pc, 'A_sign': m.reg[0].sign,
                              'A_digits': m.reg[0].digits,
                              'I1': m.reg[1].value(radix)})
        expected_digits = tuple(reversed(number(value, radix).digits))
        assert m.reg[0].digits == expected_digits
        expected_sign = -1 if initial_sign == -1 and value == 0 and not fix else 1
        assert m.reg[0].sign == expected_sign
        cases.append({'b': radix, 'initial_A_sign': initial_sign,
                      'input': value, 'ENTA_fix': fix,
                      'actual_sign': m.reg[0].sign,
                      'actual_digits': m.reg[0].digits,
                      'required_sign': 1, 'time_with_HLT': m.time,
                      'matches_word_contract': m.reg[0].sign == 1,
                      'trace': trace})
result = {'scope': 'Previously untested -0 boundary of the stated rA>=0 condition',
          'checks': len(cases), 'all_expected_outcomes_reproduced': True,
          'counterexamples': sum(not x['matches_word_contract'] for x in cases),
          'cases': cases}
(HERE/'results/wahid-zero.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k: v for k, v in result.items() if k != 'cases'}))

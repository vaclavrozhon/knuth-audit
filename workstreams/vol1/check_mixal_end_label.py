"""Regression for MIXAL END LOC definitions; hand-calculated addresses."""
from pathlib import Path
import json
from mixal import Assembly
from mix_machine import instruction, number

checks = 0
for b in range(64, 101):
    rows = [('', 'ORIG', '100'), ('START', 'LDA', 'FINISH'),
            ('', 'LDA', 'UNDEF'), ('', 'LDX', '=7='), ('', 'HLT', ''),
            ('FINISH', 'END', 'START')]
    for reverse in [False, True]:
        a = Assembly(rows, b, reverse_literals=reverse)
        # Four instructions, one undefined CON0, one literal CON7; END
        # itself allocates no word, and its label denotes address106.
        assert a.start == 100 and a.pc == 106
        assert a.symbols['FINISH'] == number(106, b)
        assert a.symbols['UNDEF'] == number(104, b)
        assert a.memory[100] == instruction(b, 'LDA', 106)
        assert a.memory[104] == number(0, b)
        assert a.memory[105] == number(7, b)
        assert 106 not in a.memory
        checks += 7
    # Removing the label must retain allocation for an undefined symbol.
    a = Assembly([('', 'ORIG', '100'), ('START', 'LDA', 'FINISH'),
                  ('', 'END', 'START')], b)
    assert a.symbols['FINISH'] == number(101, b)
    assert a.memory[101] == number(0, b) and a.pc == 102
    checks += 2
    # Local forward labels obey the same LOC rule after normalization.
    a = Assembly([('', 'ORIG', '100'), ('START', 'JMP', '1F'),
                  ('1H', 'END', 'START')], b)
    assert a.memory[100] == instruction(b, 'JMP', 101)
    assert a.pc == 101 and 101 not in a.memory
    checks += 2
    # END's ADDRESS may refer to its own, now-defined LOC.
    a = Assembly([('', 'ORIG', '100'), ('', 'JMP', 'FINISH'),
                  ('FINISH', 'END', 'FINISH')], b)
    assert a.start == 101 and a.pc == 101
    checks += 1
    try:
        Assembly([('FINISH', 'CON', '0'), ('FINISH', 'END', '0')], b)
    except ValueError as err:
        assert 'duplicate symbol' in str(err)
    else:
        raise AssertionError('duplicate LOC accepted')
    checks += 1
result = dict(status='passed', checks=checks, radices=list(range(64,101)),
              scope='END label, implicit zero and literal words, local LOC, duplicate definition')
Path(__file__).with_name('results').joinpath('mixal-end-label.json').write_text(
    json.dumps(result, indent=2)+'\n')
print(json.dumps(result))

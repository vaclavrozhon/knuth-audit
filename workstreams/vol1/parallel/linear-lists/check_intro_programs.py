"""Focused execution of original TAOCP 1 section 2.1 programs.

Imports the already audited assembler/CPU/I/O model without editing it.
Independent expected lists and output strings supplement general proofs.
All newly generated files stay beside this script under results/.
"""
from pathlib import Path
import itertools
import json
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parents[1]))
from mix_machine import Machine, Word, number
from mixal import Assembly, CHARACTERS, CHAR_CODE
from mix_io import IOMachine

checks = 0
profiles = []


def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


PREFIX = [('NEXT', 'EQU', '4:5'), ('TAG', 'EQU', '1:1'),
          ('TOP', 'EQU', '20'), ('NEWCARD', 'EQU', '21'),
          ('', 'ORIG', '3000')]
A = PREFIX + [('START', 'LD1', 'NEWCARD'), ('', 'LDA', 'TOP'),
              ('', 'STA', '0,1(NEXT)'), ('', 'ST1', 'TOP'),
              ('', 'STZ', '0,1(TAG)'), ('', 'HLT', ''),
              ('', 'END', 'START')]
B = PREFIX + [('START', 'ENTA', '0'), ('', 'LD1', 'TOP'),
              ('', 'J1Z', '*+4'), ('', 'INCA', '1'),
              ('', 'LD1', '0,1(NEXT)'), ('', 'J1NZ', '*-2'),
              ('', 'HLT', ''), ('', 'END', 'START')]
PRINT = [('TOP', 'EQU', '20'), ('PRINTER', 'EQU', '18'),
         ('TAG', 'EQU', '1:1'), ('NEXT', 'EQU', '4:5'),
         ('NAME', 'EQU', '0:5'), ('', 'ORIG', '2000'),
         ('PBUF', 'ALF', 'PILE '), ('', 'ALF', 'EMPTY'),
         ('', 'ORIG', 'PBUF+24'), ('BEGIN', 'LD2', 'TOP'),
         ('', 'J2Z', '2F'), ('1H', 'LDA', '0,2(TAG)'),
         ('', 'ENT1', 'PBUF'), ('', 'JBUS', '*(PRINTER)'),
         ('', 'JAZ', '*+3'), ('', 'MOVE', 'PAREN(3)'),
         ('', 'JMP', '*+2'), ('', 'MOVE', 'BLANKS(3)'),
         ('', 'LDA', '1,2(NAME)'), ('', 'STA', 'PBUF+1'),
         ('', 'LD2', '0,2(NEXT)'), ('2H', 'OUT', 'PBUF(PRINTER)'),
         ('', 'J2NZ', '1B'), ('DONE', 'HLT', ''),
         ('PAREN', 'ALF', '    ('), ('BLANKS', 'ALF', '     '),
         ('', 'ALF', ')    '), ('', 'ALF', '     '),
         ('', 'END', 'BEGIN')]


def alphabetic(s):
    assert len(s) == 5
    return Word(1, tuple(CHAR_CODE[c] for c in s))


def install_pile(machine, addresses, tags):
    titles = []
    for i, (address, tag) in enumerate(zip(addresses, tags)):
        suit, rank = i % 4 + 1, i % 13 + 1
        following = addresses[i+1] if i+1 < len(addresses) else 0
        machine.mem[address] = Word(1, (tag, suit, rank,
                                               following//machine.b, following % machine.b))
        title = f'{rank:3d} {"CDHS"[suit-1]}'
        titles.append(title)
        machine.mem[address+1] = alphabetic(title)
    machine.mem[20] = number(addresses[0] if addresses else 0, machine.b)
    return titles


# Every allowed byte radix, both empty/nonempty insertion and count cases.
for radix in range(64, 101):
    for length in [0, 1, 2, 7, 52]:
        addresses = [100+2*((37*i) % 900) for i in range(length)]
        tags = [i % 2 for i in range(length)]
        assembly = Assembly(A, radix)
        machine = Machine(radix)
        assembly.load(machine)
        install_pile(machine, addresses, tags)
        old_top = machine.mem[20]
        fresh = 3998
        machine.mem[21] = number(fresh, radix)
        machine.mem[fresh] = Word(1, (1, 4, 13, 17, 19))
        machine.mem[fresh+1] = alphabetic('  K S')
        before = list(machine.mem)
        machine.run(assembly.start)
        check(machine.mem[20].value(radix) == fresh, ('A top', radix, length))
        check(machine.mem[fresh] == Word(1, (0, 4, 13, *old_top.digits[-2:])),
              ('A fields', radix, length))
        check(all(machine.mem[i] == before[i] for i in range(4000)
                  if i not in [20, fresh]), ('A locality', radix, length))

        assembly = Assembly(B, radix)
        machine = Machine(radix)
        assembly.load(machine)
        install_pile(machine, addresses, tags)
        before = list(machine.mem)
        machine.reg[0] = number(-7, radix)
        machine.reg[1] = number(-11, radix)
        machine.run(assembly.start)
        check(machine.reg[0].value(radix) == length, ('B count', radix, length))
        check(machine.reg[1].value(radix) == 0, ('B exhausted', radix, length))
        check(machine.mem == before, ('B no mutation', radix, length))

# Long non-contiguous and boundary-address chains; no new general proof is inferred.
for radix in [64, 100]:
    addresses = list(reversed(range(100, 2100, 2))) + [3998]
    assembly = Assembly(B, radix)
    machine = Machine(radix)
    assembly.load(machine)
    install_pile(machine, addresses, [1]*len(addresses))
    machine.run(assembly.start)
    check(machine.reg[0].value(radix) == len(addresses), ('B long', radix))

# Printed field indirection in exercise7: exactly two loads are necessary.
for radix in [64, 100]:
    for correct in [False, True]:
        rows = PREFIX + ([('START', 'LD1', 'TOP'), ('', 'LDA', '0,1(NEXT)')]
                         if correct else [('START', 'LDA', 'TOP(NEXT)')])
        rows += [('', 'HLT', ''), ('', 'END', 'START')]
        assembly = Assembly(rows, radix)
        machine = Machine(radix)
        assembly.load(machine)
        install_pile(machine, [242, 386, 100], [0, 0, 1])
        machine.run(assembly.start)
        check(machine.reg[0].value(radix) == (386 if correct else 242),
              ('exercise7', radix, correct))

# Device delay exercises actual buffer ownership across asynchronous OUT calls.
tag_cases = [[], [0], [1], [0, 1], [1, 0], [1]*5, [0]*5,
             [i % 2 for i in range(52)]]
for radix, delay, tags in itertools.product([64, 100], [0, 1, 97], tag_cases):
    assembly = Assembly(PRINT, radix)
    machine = IOMachine(radix, delay)
    assembly.load(machine)
    addresses = [100+2*((37*i) % 900) for i in range(len(tags))]
    titles = install_pile(machine, addresses, tags)
    before = {i: machine.mem[i] for a in addresses for i in [a, a+1]}
    machine.run(assembly.start, limit=100000)
    machine.finish_io()
    lines = [''.join(CHARACTERS[c] for w in row for c in w.digits)
             for row in machine.outputs[18]]
    expected = [('    ('+name+')    ' if tag else '     '+name+'     ').ljust(120)
                for name, tag in zip(titles, tags)] if tags else ['PILE EMPTY'.ljust(120)]
    check(lines == expected, ('printed lines', radix, delay, tags))
    check(all(machine.mem[i] == w for i, w in before.items()),
          ('printer preserves nodes', radix, delay, len(tags)))
    check(machine.mem[20].value(radix) == (addresses[0] if addresses else 0),
          ('printer preserves top', radix, delay, len(tags)))
    profiles.append(dict(radix=radix, delay=delay, cards=len(tags),
                         output_lines=len(lines), steps=machine.steps))

result = dict(status='passed', checks=checks, printer_profiles=profiles,
              scope='section2.1 original programA, answer8, answer9, field indirection7',
              conventions='nonoverlapping valid nodes, null link0, zero-initialized reserved output buffer',
              proof='notes/intro-proofs.md; tests supplement general invariants')
(ROOT/'results/intro-programs.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'status':result['status'], 'checks':checks,
                  'printer_cases':len(profiles)}))

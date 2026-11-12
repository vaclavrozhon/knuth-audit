"""Structured transcriptions from pp.145,148–149,157,512.

The prime-table base is selectable to compare the 1997 text with the 2022
correction. The instruction validator includes the 2002 and 2008 errata.
"""


MAXIMUM = [
    ('X', 'EQU', '1000'), ('', 'ORIG', '3000'),
    ('MAXIMUM', 'STJ', 'EXIT'), ('INIT', 'ENT3', '0,1'),
    ('', 'JMP', 'CHANGEM'), ('LOOP', 'CMPA', 'X,3'),
    ('', 'JGE', '*+3'), ('CHANGEM', 'ENT2', '0,3'),
    ('', 'LDA', 'X,3'), ('', 'DEC3', '1'), ('', 'J3P', 'LOOP'),
    ('EXIT', 'JMP', '*')]

SORT = MAXIMUM + [
    ('', 'ORIG', '200'), ('START', 'IN', 'X+1(0)'),
    ('', 'JBUS', '*(0)'), ('', 'ENT1', '100'),
    ('1H', 'JMP', 'MAXIMUM'), ('', 'LDX', 'X,1'),
    ('', 'STA', 'X,1'), ('', 'STX', 'X,2'), ('', 'DEC1', '1'),
    ('', 'J1P', '1B'), ('', 'OUT', 'X+1(1)'),
    ('', 'HLT', ''), ('', 'END', 'START')]


def prime_program(base=99):
    return [
        ('L', 'EQU', '500'), ('PRINTER', 'EQU', '18'),
        ('PRIME', 'EQU', str(base)), ('BUF0', 'EQU', '2000'),
        ('BUF1', 'EQU', 'BUF0+25'), ('', 'ORIG', '3000'),
        ('START', 'IOC', '0(PRINTER)'), ('', 'LD1', '=1-L='),
        ('', 'LD2', '=3='), ('2H', 'INC1', '1'),
        ('', 'ST2', 'PRIME+L,1'), ('', 'J1Z', '2F'),
        ('4H', 'INC2', '2'), ('', 'ENT3', '2'),
        ('6H', 'ENTA', '0'), ('', 'ENTX', '0,2'),
        ('', 'DIV', 'PRIME,3'), ('', 'JXZ', '4B'),
        ('', 'CMPA', 'PRIME,3'), ('', 'INC3', '1'),
        ('', 'JG', '6B'), ('', 'JMP', '2B'),
        ('2H', 'OUT', 'TITLE(PRINTER)'), ('', 'ENT4', 'BUF1+10'),
        ('', 'ENT5', '-50'), ('2H', 'INC5', 'L+1'),
        ('4H', 'LDA', 'PRIME,5'), ('', 'CHAR', ''),
        ('', 'STX', '0,4(1:4)'), ('', 'DEC4', '1'),
        ('', 'DEC5', '50'), ('', 'J5P', '4B'),
        ('', 'OUT', '0,4(PRINTER)'), ('', 'LD4', '24,4'),
        ('', 'J5N', '2B'), ('', 'HLT', ''),
        ('', 'ORIG', 'PRIME+1'), ('', 'CON', '2'),
        ('', 'ORIG', 'BUF0-5'), ('TITLE', 'ALF', 'FIRST'),
        ('', 'ALF', ' FIVE'), ('', 'ALF', ' HUND'),
        ('', 'ALF', 'RED P'), ('', 'ALF', 'RIMES'),
        ('', 'ORIG', 'BUF0+24'), ('', 'CON', 'BUF1+10'),
        ('', 'ORIG', 'BUF1+24'), ('', 'CON', 'BUF0+10'),
        ('', 'END', 'START')]


def validator_program():
    from mix_machine import OPS
    names = ['NOP', 'ADD', 'SUB', 'MUL', 'DIV', 'HLT', 'SRC', 'MOVE']
    names += ['LD'+r for r in ['A', '1', '2', '3', '4', '5', '6', 'X']]
    names += ['LD'+r+'N' for r in ['A', '1', '2', '3', '4', '5', '6', 'X']]
    names += ['ST'+r for r in ['A', '1', '2', '3', '4', '5', '6', 'X']]
    names += ['STJ', 'STZ', 'JBUS', 'IOC', 'IN', 'OUT', 'JRED', 'JLE']
    names += ['J'+r+'NP' for r in ['A', '1', '2', '3', '4', '5', '6', 'X']]
    names += ['ENN'+r for r in ['A', '1', '2', '3', '4', '5', '6', 'X']]
    names += ['CMP'+r for r in ['A', '1', '2', '3', '4', '5', '6', 'X']]
    rows = [('B', 'EQU', '1(4:4)'), ('BMAX', 'EQU', 'B-1'),
            ('UMAX', 'EQU', '20'), ('INST', 'EQU', '50'),
            ('GOOD', 'EQU', '10'), ('BAD', 'EQU', '11'), ('', 'ORIG', '100')]
    for c, name in enumerate(names):
        assert OPS[name][0] == c
        if c == 0:
            a = 'GOOD(BMAX)'
        elif c in (1, 2, 3, 4, 56):
            a = 'FLOAT(5:5)'
        elif c in (5, 6) or 48 <= c <= 55:
            a = 'GOOD'
        elif c == 7:
            a = 'MEMORY(BMAX)'
        elif 8 <= c <= 33 or 57 <= c <= 63:
            a = 'FIELD(5:5)'
        elif 34 <= c <= 38:
            a = ('GOOD' if c == 35 else 'MEMORY')+'(UMAX)'
        else:
            a = 'MEMORY'
        rows.append(('TABLE' if c == 0 else '', name, a))
    rows += [
        ('BEGIN', 'LDA', 'INST'), ('', 'CMPA', 'VALID(3:3)'),
        ('', 'JG', 'BAD'), ('', 'LD1', 'INST(5:5)'),
        ('', 'DEC1', '64'), ('', 'J1NN', 'BAD'),
        ('', 'CMPA', 'TABLE+64,1(4:4)'), ('', 'JG', 'BAD'),
        ('', 'LD1', 'TABLE+64,1(1:2)'), ('', 'JMP', '0,1'),
        ('FLOAT', 'CMPA', 'VALID(4:4)'), ('', 'JE', 'MEMORY'),
        ('FIELD', 'ENTA', '0'), ('', 'LDX', 'INST(4:4)'),
        ('', 'DIV', '=9='), ('', 'STX', '*+1(0:2)'),
        ('', 'INCA', '0'), ('', 'DECA', '5'), ('', 'JAP', 'BAD'),
        ('MEMORY', 'LDX', 'INST(3:3)'), ('', 'JXNZ', 'GOOD'),
        ('', 'LDX', 'INST(0:2)'), ('', 'JXN', 'BAD'),
        ('', 'DECX', '3999'), ('', 'JXNP', 'GOOD'),
        ('', 'JMP', 'BAD'), ('VALID', 'CMPX', '3999,6(6)'),
        ('', 'END', 'BEGIN')]
    return rows

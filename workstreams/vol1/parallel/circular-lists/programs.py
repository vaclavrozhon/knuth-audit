"""Literal MIX listings, checked against original printed pp277--278,552--553.

Only address placement and descriptive labels replace the book's local labels.
The returned row triples are assembled by the existing, unchanged audit model.
"""
import sys
from pathlib import Path
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from mixal import Assembly
from mix_machine import Machine, Word, number, field, instruction, Undefined


def rows(text):
    ans = []
    for line in text.strip().splitlines():
        label, op, operand = line.strip().split('|')
        ans.append((label, op, operand))
    return ans


ADD = rows('''
ADD|STJ|ARETURN
AINIT|ENT3|0,2
|LD2|1,3(LINK)
ANEXT|LD1|1,1(LINK)
SW1|LDA|1,1
ACOMP|CMPA|1,2(ABC)
|JE|ARETURN
|JG|AINSERT
|ENT3|0,2
|LD2|1,3(LINK)
|JMP|ACOMP
ARETURN|JAN|*
SW2|LDA|0,1
|ADD|0,2
|STA|0,2
|JANZ|AINIT
|ENT6|0,2
|LD2|1,2(LINK)
|LDX|AVAIL
|STX|1,6(LINK)
|ST6|AVAIL
|ST2|1,3(LINK)
|JMP|ANEXT
AINSERT|LD6|AVAIL
|J6Z|OVERFLOW
|LDX|1,6(LINK)
|STX|AVAIL
|STA|1,6
SW3|LDA|0,1
|STA|0,6
|ST2|1,6(LINK)
|ST6|1,3(LINK)
|ENT3|0,6
|JMP|ANEXT
''')

COPY = rows('''
COPY|STJ|CRETURN
|ENT3|CRETURN
|LDA|1,1
CLOOP|LD6|AVAIL
|J6Z|OVERFLOW
|LDX|1,6(LINK)
|STX|AVAIL
|STA|1,6
|LDA|0,1
|STA|0,6
|ST6|1,3(LINK)
|ENT3|0,6
|LD1|1,1(LINK)
|LDA|1,1
|JANN|CLOOP
|LD2|CDUMMY(LINK)
|ST2|1,3(LINK)
CRETURN|JMP|*
CDUMMY|CON|0
''')

ERASE = rows('''
ERASE|STJ|ERETURN
|LDX|AVAIL
|LDA|1,1(LINK)
|STA|AVAIL
|STX|1,1(LINK)
ERETURN|JMP|*
''')

ZERO = rows('''
ZERO|STJ|ZRETURN
|LD1|AVAIL
|J1Z|OVERFLOW
|LDX|1,1(LINK)
|STX|AVAIL
|ENT2|0,1
|MOVE|ZMODEL(2)
|ST2|1,2(LINK)
ZRETURN|JMP|*
ZMODEL|CON|0
|CON|-1(ABC)
''')

MULT = rows('''
MULT|STJ|MRETURN
|LDA|MSW1
|STA|SW1
|LDA|MSW2
|STA|SW2
|STA|SW3
|JMP|*+2
MCYCLE|JMP|ADD
MNEXT|LD4|1,4(LINK)
|LDA|1,4
|JANN|MCYCLE
|LDA|MOLD1
|STA|SW1
|LDA|MOLD2
|STA|SW2
|STA|SW3
MRETURN|JMP|*
MSW1|JMP|*+1
|LDA|0,1
|MUL|0,4
|LDA|1,1(ABC)
|JAN|*+2
|ADD|1,4(ABC)
|SLA|2
|STX|MPROD
|JMP|SW1+1
MSW2|LDA|MPROD
MOLD1|LDA|1,1
MOLD2|LDA|0,1
MPROD|CON|0
''')


def assembly(b=64, overflow='halt', extra=()):
    # Code below 500, data/allocation test pools start at 1000.
    base = rows('''
LINK|EQU|4:5
ABC|EQU|0:3
AVAIL|EQU|50
RESERVE|EQU|51
|ORIG|100
''')
    allrows = base + ADD + COPY + ERASE + ZERO + MULT + list(extra)
    if overflow == 'halt':
        allrows += [('OVERFLOW','HLT','')]
    elif overflow == 'refill':
        # One explicitly reserved chain is supplied without register changes.
        # AVAIL/RESERVE are data cells; MOVE temporarily uses and restores I1.
        allrows += rows('''
OVERFLOW|STJ|ORET
|ST1|OSAVE
|ENT1|AVAIL
|MOVE|RESERVE(1)
|LD1|OSAVE
|STZ|RESERVE
ORET|JMP|*-2
OSAVE|CON|0
''')
        # STJ patches ORET to incoming rJ, hence encode the -2 in the address
        # calculation explicitly, preserving A and all index registers.
        allrows[-2:-1] = rows('''
ORET|ENT1|*
|DEC1|2
|ST1|OJUMP(0:2)
|LD1|OSAVE
OJUMP|JMP|*
''')
    else:
        raise ValueError(overflow)
    allrows += [('','END','ADD')]
    result=Assembly(allrows,b)
    result.audit_rows=allrows
    return result


def symbols(a):
    return {k:v.value(a.b) for k,v in a.symbols.items()}


if __name__ == '__main__':
    import json
    p=Path(__file__).resolve().parent/'results'
    for b in (64,100):
        a=assembly(b)
        (p/f'book-programs-{b}.json').write_text(json.dumps({
            'radix':b,'symbols':symbols(a),
            'words':{str(k):[v.sign,*v.digits] for k,v in a.memory.items()}
        },indent=2)+'\n')
    print('Assembled all five book routines for b=64,100')

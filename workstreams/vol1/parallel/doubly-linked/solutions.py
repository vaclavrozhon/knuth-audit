"""Independent actual MIX solutions for exercises8 and9."""

DECISION='''
DECISION|STJ|DRETURN
|J5NZ|DRETURN
|LDA|ELEV1+2(NEXTINST)
|DECA|E1
|STA|DACTIVE
|JANZ|DSCAN
|LDA|CALL+2
|JANZ|DOPEN
DSCAN|ENT1|0
DLOOP|ENTA|0,1
|DECA|0,4
|JAZ|DNEXT
|LDA|CALL,1
|JANZ|DCHOOSE
DNEXT|INC1|1
|CMP1|=5=
|JL|DLOOP
|LDA|DRETURN(0:2)
|DECA|E6B
|JANZ|DRETURN
|ENT1|2
DCHOOSE|ENT5|0,1
|DEC5|0,4
|J5Z|DRETURN
|LDA|DACTIVE
|JANZ|DRETURN
|ENT3|E6
|JMP|DSCHED
DOPEN|ENT3|E3
DSCHED|ST6|DSAVED
|ENT6|ELEV1
|ST3|2,6(NEXTINST)
|ENTA|20
|JMP|HOLD
|LD6|DSAVED
DRETURN|JMP|*
DACTIVE|CON|0
DSAVED|CON|0
'''

E8='''
E8|DEC4|1
|ENTA|61
|JMP|HOLDC
|LDA|CALL,4(3:5)
|JAP|ESTOP
|ENT1|-2,4
|J1Z|ESCAN
|LDA|CALL,4(1:1)
|JAZ|E8
ESCAN|ENT1|0,4
ECHECK|DEC1|1
|J1N|ESTOP
|LDA|CALL,1
|JANZ|E8
|JMP|ECHECK
ESTOP|ENTA|23
|JMP|E2A
'''

def numbered(text,prefix):
    return [(f'{prefix}{i:02}',tuple(row.split('|'))) for i,row in enumerate(text.strip().splitlines(),1)]

OWN_DECISION=numbered(DECISION,'OD')
OWN_E8=numbered(E8,'OE')

if __name__=='__main__':
    from pathlib import Path
    from book_program import assemble
    a=assemble(decision=OWN_DECISION,e8=OWN_E8)
    p=Path(__file__).resolve().parent/'results'/'own-solutions-complete.mixal'
    p.write_text('\n'.join(f'{l:12} {o:6} {x}' for l,o,x in a.audit_rows)+'\n')
    print('own actual MIX E8 and DECISION assembled:',p.name)

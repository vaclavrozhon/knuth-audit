"""Own complete MIX subroutines for1.3.3-36, with runtime lengths l,m,n.

I1,I2,I3 are input lengths; DATA is fixed at1000. The cycle method uses
word arithmetic for virtual indices, which can exceed the index-register range.
"""
def program(method,l,m,n):
    rows=[('DATA','EQU','1000'),('','ORIG','0'),('EXCHANGE','STJ','BACK'),
          ('','ST1','LLEN'),('','ST2','MLEN'),('','ST3','NLEN')]
    if method=='cycles':
        rows += [('','LDA','LLEN'),('','ADD','MLEN'),('','STA','SHIFT'),('','ADD','NLEN'),('','STA','TOTAL'),('','JAZ','BACK'),
                 ('','ADD','MLEN'),('','STA','VIRT'),('','LDA','MLEN'),('','ADD','NLEN'),('','STA','V'),('','LDA','SHIFT'),('','STA','U'),
                 ('GCD','LDA','V'),('','JAZ','READY'),('','ENTA','0'),('','LDX','U'),('','DIV','V'),
                 ('','LDA','V'),('','STA','U'),('','STX','V'),('','JMP','GCD'),
                 ('READY','ENT1','0'),('OUTER','ST1','START'),('','LDX','DATA,1'),('','ENT2','0,1'),
                 ('STEP','ENTA','0,2'),('','ADD','SHIFT'),('','CMPA','VIRT'),('','JL','INSIDE'),('','SUB','VIRT'),
                 ('INSIDE','CMPA','TOTAL'),('','JL','NEXT'),('','ADD','SHIFT'),('','CMPA','VIRT'),('','JL','NEXT'),('','SUB','VIRT'),
                 ('NEXT','CMPA','START'),('','JE','CLOSE'),('','STA','SUCC'),('','LD3','SUCC'),
                 ('','LDA','DATA,3'),('','STA','DATA,2'),('','ENT2','0,3'),('','JMP','STEP'),
                 ('CLOSE','STX','DATA,2'),('','INC1','1'),('','CMP1','U'),('','JL','OUTER'),('BACK','JMP','*')]
    elif method=='reversals':
        rows += [('','LDA','LLEN'),('','ADD','MLEN'),('','ADD','NLEN'),('','STA','TOTAL'),
                 ('','ENT1','0'),('','LD2','TOTAL'),('','JMP','REV'),
                 ('','ENT1','0'),('','LD2','NLEN'),('','JMP','REV'),
                 ('','LD1','NLEN'),('','LDA','NLEN'),('','ADD','MLEN'),('','STA','CUT'),('','LD2','CUT'),('','JMP','REV'),
                 ('','LD1','CUT'),('','LD2','TOTAL'),('','JMP','REV'),('BACK','JMP','*'),
                 ('REV','STJ','RBACK'),('RLOOP','ENT3','-1,2'),('','DEC3','0,1'),('','J3NP','RBACK'),
                 ('','DEC2','1'),('','LDA','DATA,1'),('','LDX','DATA,2'),('','STX','DATA,1'),('','STA','DATA,2'),
                 ('','INC1','1'),('','JMP','RLOOP'),('RBACK','JMP','*')]
    else:raise ValueError(method)
    rows += [(x,'CON','0') for x in ['LLEN','MLEN','NLEN','TOTAL','VIRT','SHIFT','U','V','START','SUCC','CUT']]
    rows += [('','ORIG','300'),('CALL','ENT1',str(l)),('','ENT2',str(m)),('','ENT3',str(n)),('','JMP','EXCHANGE'),('STOP','HLT',''),('','END','CALL')]
    return rows

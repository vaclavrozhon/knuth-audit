"""Farey subroutine, §1.3.2-18, pp.519–520, plus an explicit caller."""

def program(n,handle_one=False):
    rows=[('X','EQU','400'),('Y','EQU','2200'),('','ORIG','100'),
        ('FAREY','STJ','9F'),('','STZ','X'),('','ENTX','1'),('','STX','Y'),
        ('','STX','X+1'),('','ST1','Y+1'),('','ENT2','0'),
        ('1H','LDX','Y,2'),('','INCX','0,1'),('','ENTA','0'),('','DIV','Y+1,2'),
        ('','STA','TEMP'),('','MUL','Y+1,2'),('','SLAX','5'),('','SUB','Y,2'),
        ('','STA','Y+2,2'),('','LDA','TEMP'),('','MUL','X+1,2'),('','SLAX','5'),
        ('','SUB','X,2'),('','STA','X+2,2'),('','CMPA','Y+2,2'),('','INC2','1'),
        ('','JL','1B'),('9H','JMP','*'),('BEGIN','ENT1',str(n)),('','JMP','FAREY'),
        ('','HLT',''),('','END','BEGIN')]
    if handle_one:
        at=rows.index(('','ENT2','0'))+1
        rows[at:at]=[('','CMP1','=1='),('','JE','9F')]
    return rows

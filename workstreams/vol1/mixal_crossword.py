"""Our complete MIX solution of §1.3.2-23; the book supplies no answer.

Read n cards (n=23 requested), flood the black exterior, number white starts,
and print the prescribed 5-column by3-line tiles, with the outer top/left edge.
Numbers use at least two decimal digits, and three when necessary.
"""
def program(n=23):
    assert 1<=n<=23
    stride=n+2;size=stride*stride;first=stride+1;last=n*stride+n
    rows=[('N','EQU',str(n)),('S','EQU',str(stride)),('SIZE','EQU',str(size)),
        ('FIRST','EQU',str(first)),('STOP','EQU',str(last+1)),
        ('X','EQU','500'),('LABELS','EQU','1200'),('BUF','EQU','2200'),
        ('B1','EQU','2224'),('B2','EQU','2248'),('INPUT','EQU','2300'),
        ('','ORIG','100'),('START','ENTA','-1'),('','ENT1','SIZE-1'),
        ('INIT','STA','X,1'),('','STZ','LABELS,1'),('','DEC1','1'),('','J1NN','INIT'),
        ('','ENT1','FIRST'),('','ENT2','N'),('READ','IN','INPUT(16)'),('','JBUS','*(16)')]
    for col in range(n):
        word,byte=divmod(col,5);byte+=1
        rows += [('','LDA',f'INPUT+{word}({byte}:{byte})'),('','SUB','THIRTY'),
                 ('','STA','X,1'),('','INC1','1')]
    rows += [('','INC1','2'),('','DEC2','1'),('','J2P','READ'),
        ('PASS','ENT2','0'),('','ENT1','FIRST'),('SCAN','LDA','X,1'),
        ('','CMPA','ONE'),('','JNE','NEXT'),('','LDA','X-1,1'),('','JAN','FILL'),
        ('','LDA','X+1,1'),('','JAN','FILL'),('','LDA','X-S,1'),('','JAN','FILL'),
        ('','LDA','X+S,1'),('','JANN','NEXT'),
        ('FILL','ENTA','-1'),('','STA','X,1'),('','ENT2','1'),
        ('NEXT','INC1','1'),('','CMP1','=STOP='),('','JL','SCAN'),('','J2P','PASS'),
        ('','STZ','LAST'),('','ENT1','FIRST'),('','ENT2','0'),
        ('NUMBER','LDA','X,1'),('','JAN','ADVANCE'),('','ST1','LAST'),('','JAP','ADVANCE'),
        ('','LDA','X+S,1'),('','JANZ','ACROSS'),('','LDA','X-S,1'),('','JANZ','ASSIGN'),
        ('ACROSS','LDA','X+1,1'),('','JANZ','ADVANCE'),('','LDA','X-1,1'),('','JAZ','ADVANCE'),
        ('ASSIGN','INC2','1'),('','ST2','LABELS,1'),
        ('ADVANCE','INC1','1'),('','CMP1','=STOP='),('','JL','NUMBER'),
        ('','LDX','LAST'),('','JXZ','DONE'),('','ENTA','0'),('','DIV','=S='),('','STA','MAXROW'),
        ('','ENT5','0'),('','ENT6','0'),
        ('ROW','JBUS','*(18)'),('','ENT3','71'),('CLEAR','STZ','BUF,3'),('','DEC3','1'),('','J3NN','CLEAR'),
        ('','ENT2','0'),('CELL','ENT1','0,6'),('','INC1','0,2'),('','LDA','X,1'),
        ('','JAN','OUTSIDE'),('','JAP','BLACK'),
        ('','LDA','VERTICAL'),('','STA','BUF,2'),('','STA','B1,2'),
        ('','LDA','SOLID'),('','STA','B2,2'),('','LDA','LABELS,1'),('','JAZ','NEXTCELL'),
        ('','CMPA','HUNDRED'),('','CHAR',''),('','JGE','THREE'),
        ('','STX','BUF,2(1:2)'),('','JMP','NEXTCELL'),('THREE','STX','BUF,2(1:3)'),('','JMP','NEXTCELL'),
        ('BLACK','LDA','SOLID'),('','STA','BUF,2'),('','STA','B1,2'),('','STA','B2,2'),('','JMP','NEXTCELL'),
        ('OUTSIDE','LDA','X+1,1'),('','JAN','BELOW'),('','LDA','VERTICAL'),
        ('','STA','BUF,2'),('','STA','B1,2'),('','STA','B2,2'),
        ('BELOW','LDA','X+S,1'),('','JAN','DIAGONAL'),('','LDA','SOLID'),('','STA','B2,2'),('','JMP','NEXTCELL'),
        ('DIAGONAL','LDA','X+S+1,1'),('','JAN','NEXTCELL'),('','LDA','VERTICAL'),('','STA','B2,2'),
        ('NEXTCELL','INC2','1'),('','CMP2','=N='),('','JLE','CELL'),
        ('','J5Z','BOTTOM'),('','OUT','BUF(18)'),('','JBUS','*(18)'),('','OUT','B1(18)'),('','JBUS','*(18)'),
        ('BOTTOM','OUT','B2(18)'),('','INC5','1'),('','INC6','S'),('','CMP5','MAXROW'),('','JLE','ROW'),
        ('DONE','HLT',''),('LAST','CON','0'),('MAXROW','CON','0'),
        ('THIRTY','CON','30'),('ONE','CON','1'),('HUNDRED','CON','100'),
        ('VERTICAL','ALF','    +'),('SOLID','ALF','+++++'),('','END','START')]
    return rows

"""Printed Program B pp174-175; optional published ENT3 correction (2000)."""
from mixal_permutation_a import LINES as A_LINES

LINES={
1:('MAXWDS','EQU','1200'),2:('X','ORIG','*+MAXWDS'),3:('T','ORIG','*+MAXWDS'),
4:('PERM','ORIG','*+MAXWDS'),5:('ANS','EQU','PERM'),6:('OUTBUF','ORIG','*+24'),
**{k+2:A_LINES[k] for k in range(5,23)},
25:('1H','INC2','15'),26:('','ENT3','1'),27:('RIGHT','ENTX','0'),
28:('SCAN','DEC2','1'),29:('','LDA','PERM,2'),30:('','JAZ','CYCLE'),
31:('','CMPA','RPREN'),32:('','JE','RIGHT'),33:('','CMPA','LPREN'),34:('','JE','LEFT'),
35:('','ENT4','1,3'),36:('','STA','X'),37:('2H','DEC4','1'),38:('','CMPA','X,4'),39:('','JNE','2B'),
40:('','J4P','FOUND'),41:('','INC3','1'),42:('','STA','X,3'),43:('','ST3','T,3'),44:('','ENT4','0,3'),
45:('FOUND','LDA','T,4'),46:('','STX','T,4'),47:('','SRC','5'),48:('','JANZ','SCAN'),
49:('','ENT1','0,4'),50:('','JMP','SCAN'),51:('LEFT','STX','T,1'),52:('CYCLE','J2P','SCAN'),
54:('OUTPUT','ENT1','ANS'),55:('','J3Z','DONE'),56:('1H','LDAN','X,3'),57:('','JAP','SKIP'),
58:('','CMP3','T,3'),59:('','JE','SKIP'),60:('','MOVE','LPREN'),61:('2H','MOVE','X,3'),
62:('','STA','X,3'),63:('','LD3','T,3'),64:('','LDAN','X,3'),65:('','JAN','2B'),
66:('','MOVE','RPREN'),67:('SKIP','DEC3','1'),68:('','J3P','1B'),
**{k+22:A_LINES[k] for k in range(48,63) if k in A_LINES},85:('','END','BEGIN')}


def program(corrected=True,max_words=1200,expanded_answer=False):
    rows=[]
    for line,row in sorted(LINES.items()):
        if line==1:row=('MAXWDS','EQU',str(max_words))
        if line==26 and corrected:row=('','ENT3','0')
        if line==4 and expanded_answer:row=('PERM','ORIG','*+MAXANS')
        rows.append(row)
        if line==1 and expanded_answer:rows.append(('MAXANS','EQU','2*MAXWDS+23'))
    return rows

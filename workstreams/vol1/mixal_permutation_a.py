"""Exact printed Program A, Volume1 pp168-169, with original line numbers."""
from mix_machine import Word
from mixal import CHARACTERS

LINES={
1:('MAXWDS','EQU','1200'),2:('PERM','ORIG','*+MAXWDS'),3:('ANS','ORIG','*+MAXWDS'),
4:('OUTBUF','ORIG','*+24'),5:('CARDS','EQU','16'),6:('PRINTER','EQU','18'),
7:('BEGIN','IN','PERM(CARDS)'),8:('','ENT2','0'),9:('','LDA','EQUALS'),
10:('1H','JBUS','*(CARDS)'),11:('','CMPA','PERM+15,2'),12:('','JE','*+2'),
13:('','IN','PERM+16,2(CARDS)'),14:('','ENT1','OUTBUF'),15:('','JBUS','*(PRINTER)'),
16:('','MOVE','PERM,2(16)'),17:('','OUT','OUTBUF(PRINTER)'),18:('','JE','1F'),
19:('','INC2','16'),20:('','CMP2','=MAXWDS-16='),21:('','JLE','1B'),22:('','HLT','666'),
23:('1H','INC2','15'),24:('','ST2','SIZE'),25:('','ENT3','0'),
26:('2H','LDAN','PERM,3'),27:('','CMPA','LPREN(1:5)'),28:('','JNE','1F'),
29:('','STA','PERM,3'),30:('','INC3','1'),31:('','LDXN','PERM,3'),32:('','JXZ','*-2'),
33:('1H','CMPA','RPREN(1:5)'),34:('','JNE','*+2'),35:('','STX','PERM,3'),
36:('','INC3','1'),37:('','CMP3','SIZE'),38:('','JL','2B'),
39:('','LDA','LPREN'),40:('','ENT1','ANS'),41:('OPEN','ENT3','0'),
42:('1H','LDXN','PERM,3'),43:('','JXN','GO'),44:('','INC3','1'),45:('','CMP3','SIZE'),46:('','JL','1B'),
48:('DONE','CMP1','=ANS='),49:('','JNE','*+2'),50:('','MOVE','LPREN(2)'),
51:('','MOVE','=0='),52:('','MOVE','-1,1(22)'),53:('','ENT3','0'),
54:('','OUT','ANS,3(PRINTER)'),55:('','INC3','24'),56:('','LDX','ANS,3'),57:('','JXNZ','*-3'),58:('','HLT',''),
60:('LPREN','ALF','    ('),61:('RPREN','ALF',')    '),62:('EQUALS','ALF','    ='),
64:('GO','MOVE','LPREN'),65:('','MOVE','PERM,3'),66:('','STX','START'),67:('SUCC','STX','PERM,3'),
68:('','INC3','1'),69:('','LDXN','PERM,3(1:5)'),70:('','JXN','1F'),71:('','JMP','*-3'),
72:('5H','STX','0,1'),73:('','INC1','1'),74:('','ENT3','0'),75:('4H','CMPX','PERM,3(1:5)'),
76:('','JE','SUCC'),77:('1H','INC3','1'),78:('','CMP3','SIZE'),79:('','JL','4B'),
80:('','CMPX','START(1:5)'),81:('','JNE','5B'),82:('CLOSE','MOVE','RPREN'),
83:('','CMPA','-3,1'),84:('','JNE','OPEN'),85:('','INC1','-3'),86:('','JMP','OPEN'),87:('','END','BEGIN')}


def program(expanded_answer=False):
    rows=[LINES[k] for k in sorted(LINES)]
    if expanded_answer:
        rows[2]=('ANS','ORIG','*+MAXANS')
        rows.insert(1,('MAXANS','EQU','2*MAXWDS+23'))
    return rows


def name_word(s):
    assert len(s)==5
    return Word(1,tuple(CHARACTERS.index(ch) for ch in s))


def cards_from_tokens(tokens):
    """Tokens are complete five-character fields; final equals uses the last field."""
    tokens=list(tokens)
    while len(tokens)%16!=15:tokens.append('     ')
    tokens.append('    =')
    return [[name_word(s) for s in tokens[i:i+16]] for i in range(0,len(tokens),16)]


def cycle_tokens(cycles):
    return [field for cycle in cycles for field in ['    (',*cycle,')    ']]

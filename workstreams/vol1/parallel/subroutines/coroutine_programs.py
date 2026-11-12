"""Original p.195-197 program and independent solution of exercise1.4.2-7."""

NEXTCHAR = [
    ('NEXTCHAR','STJ','9F'), ('','JXNZ','3F'), ('1H','J6N','2F'),
    ('','IN','INPUT(READER)'), ('','JBUS','*(READER)'), ('','ENN6','16'),
    ('2H','LDX','INPUT+16,6'), ('','INC6','1'), ('3H','ENTA','0'),
    ('','SLAX','1'), ('9H','JANZ','*'), ('','JMP','NEXTCHAR+1')]


def decoder(variant='original'):
    """The five blanks in line32 are made explicit as in the 2018 erratum."""
    rows = [('', 'ORIG','100'), ('READER','EQU','16'), ('INPUT','ORIG','*+16')]
    rows += NEXTCHAR
    rows += [('2H','INCA','30'), ('','JMP','OUT'), ('IN1','JMP','NEXTCHAR'),
             ('','DECA','30'), ('','JAN','2B'), ('','CMPA','=10='),
             ('','JGE','2B'), ('','STA','*+1(0:2)'), ('','ENT5','*'),
             ('','JMP','NEXTCHAR')]
    if variant == 'corrected_comparison':
        rows += [('', 'CMPA','PERIOD')]
    rows += [('', 'JMP','OUT'), ('','DEC5','1'), ('','J5NN','*-2'),
             ('','JMP','IN1'), ('','ALF','     '), ('OUTPUT','ORIG','*+16'),
             ('PUNCH','EQU','17'), ('OUT1','ENT4','-16'), ('','ENT1','OUTPUT'),
             ('','MOVE','-1,1(16)')]
    for field in (1,2,3):
        rows += [('1H' if field==1 else '', 'JMP','IN'),
                 ('','STA',f'OUTPUT+16,4({field}:{field})')]
        if variant not in ('omit_comparisons','corrected_comparison'):
            rows += [('', 'CMPA','PERIOD')]
        rows += [('', 'JE','9F')]
    rows += [('', 'INC4','1'), ('','J4N','1B'), ('9H','OUT','OUTPUT(PUNCH)'),
             ('','JBUS','*(PUNCH)'), ('','JNE','OUT1'), ('','HLT',''),
             ('PERIOD','ALF','    .'), ('START','ENT6','0'), ('','ENTX','0')]
    if variant == 'corrected_comparison':
        rows += [('', 'CMPX','PERIOD')]
    rows += [('', 'JMP','IN1' if variant=='start_in' else 'OUT1'),
             ('OUT','STJ','INX'), ('OUTX','JMP','OUT1'),
             ('IN','STJ','OUTX'), ('INX','JMP','IN1'), ('','END','START')]
    return rows


ENCODER = [
    ('READER','EQU','16'), ('PUNCH','EQU','17'), ('INPUT','EQU','200'),
    ('OUTPUT','EQU','100'), ('','ORIG','1000')]
ENCODER += NEXTCHAR
ENCODER += [
    ('START','ENT6','0'), ('','ENTX','0'), ('','ENT4','-16'), ('','ENT2','9'),
    ('','STZ','OUTPUT-1'), ('','ENT1','OUTPUT'), ('','MOVE','-1,1(16)'),
    ('','JMP','NEXTCHAR'),
    ('NEW','CMPA','PERIOD'), ('','JE','LAST'), ('','STA','CCHAR'),
    ('','ENT5','1'),
    ('READMORE','JMP','NEXTCHAR'), ('','CMPA','CCHAR'), ('','JNE','FLUSH'),
    ('','INC5','1'), ('','CMP5','=10='), ('','JL','READMORE'),
    ('','JMP','EMITRUN'), ('','JMP','NEXTCHAR'), ('','JMP','NEW'),
    ('FLUSH','STA','LOOKAHEAD'), ('','JMP','EMITRUN'),
    ('','LDA','LOOKAHEAD'), ('','JMP','NEW'),
    ('LAST','JMP','PUTCHAR'), ('','CMP4','=-16='), ('','JNE','FINALOUT'),
    ('','CMP2','=9='), ('','JE','STOP'),
    ('FINALOUT','OUT','OUTPUT(PUNCH)'), ('','JBUS','*(PUNCH)'), ('STOP','HLT',''),
    ('EMITRUN','STJ','RRET'), ('','CMP5','=1='), ('','JNE','PREFIX'),
    ('','LDA','CCHAR'), ('','CMPA','=30='), ('','JL','DIRECT'),
    ('','CMPA','=40='), ('','JGE','DIRECT'),
    ('PREFIX','ENTA','29,5'), ('','JMP','PUTCHAR'),
    ('DIRECT','LDA','CCHAR'), ('','JMP','PUTCHAR'), ('RRET','JMP','*'),
    ('PUTCHAR','STJ','PRET'), ('','ST2','*+1(4:4)'),
    ('','STA','OUTPUT+16,4(1:1)'), ('','INC2','9'), ('','CMP2','=45='),
    ('','JLE','PRET'), ('','ENT2','9'), ('','INC4','1'), ('','J4N','PRET'),
    ('','OUT','OUTPUT(PUNCH)'), ('','JBUS','*(PUNCH)'), ('','ENT4','-16'),
    ('','STZ','OUTPUT-1'), ('','ENT1','OUTPUT'), ('','MOVE','-1,1(16)'),
    ('PRET','JMP','*'), ('CCHAR','CON','0'), ('LOOKAHEAD','CON','0'),
    ('PERIOD','ALF','    .'), ('','END','START')]


THREE_LINK = [('', 'ORIG','3000'),
    ('AB','STJ','AX'), ('BX','JMP','B1'), ('CB','STJ','CX'), ('','JMP','BX'),
    ('BC','STJ','BX'), ('CX','JMP','C1'), ('AC','STJ','AX'), ('','JMP','CX'),
    ('CA','STJ','CX'), ('AX','JMP','A1'), ('BA','STJ','BX'), ('','JMP','AX'),
    ('A1','EQU','100'), ('B1','EQU','200'), ('C1','EQU','300')]

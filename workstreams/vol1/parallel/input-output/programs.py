"""Structured MIXAL rows for TAOCP 1.4.4; shared assembler is unchanged."""


def wordin_sentinel():
    return [
        ('U','EQU','5'), ('SENTINEL','EQU','-1'), ('','ORIG','100'),
        ('WORDIN','STJ','1F'), ('','INC6','1'), ('2H','LDA','0,6'),
        ('','CMPA','=SENTINEL='), ('1H','JNE','*'), ('','IN','-100,6(U)'),
        ('','LD6','1,6'), ('','JMP','2B'), ('','ORIG','1000'),
        ('INBUF1','ORIG','*+100'), ('','CON','SENTINEL'), ('','CON','*+1'),
        ('INBUF2','ORIG','*+100'), ('','CON','SENTINEL'), ('','CON','INBUF1'),
        ('','ORIG','3000'), ('START','IN','INBUF1(U)'),
        ('','ENT6','INBUF2+99'), ('CALL','JMP','WORDIN'), ('RETURN','NOP',''),
        ('','END','START')]


def wordin_coroutine():
    """Printed answer7 with the analogous initial IN from exercise6 supplied."""
    return [
        ('U','EQU','5'), ('','ORIG','1000'),
        ('INBUF1','ORIG','*+100'), ('INBUF2','ORIG','*+100'),
        ('','ORIG','100'),
        ('1H','LDA','INBUF2+100,6'), ('','JMP','MAIN'),
        ('','INC6','1'), ('','J6N','1B'),
        ('WORDIN1','IN','INBUF2(U)'), ('','ENN6','100'),
        ('2H','LDA','INBUF1+100,6'), ('','JMP','MAIN'),
        ('','INC6','1'), ('','J6N','2B'), ('','IN','INBUF1(U)'),
        ('','ENN6','100'), ('','JMP','1B'),
        ('WORDIN','STJ','MAINX'), ('WORDINX','JMP','WORDIN1'),
        ('MAIN','STJ','WORDINX'), ('MAINX','JMP','*'),
        ('','ORIG','3000'), ('START','IN','INBUF1(U)'),
        ('CALL','JMP','WORDIN'), ('RETURN','NOP',''), ('','END','START')]


def wordin_fast():
    """Independent no-sentinel solution: seven u on an ordinary word call."""
    return [
        ('U','EQU','5'), ('BUF1','EQU','1000'), ('BUF2','EQU','1101'),
        ('','ORIG','100'),
        ('WORDIN','STJ','RETURNIN'), ('','INC6','1'), ('','J6N','LOADWORD'),
        ('REFILL','IN','BUF1(U)'), ('LINK','LDA','BUF1+100'),
        ('','STA','LOADWORD(0:2)'), ('','STA','LINK(0:2)'),
        ('','SUB','=100='), ('','STA','REFILL(0:2)'), ('','ENN6','100'),
        ('LOADWORD','LDA','BUF1+100,6'), ('RETURNIN','JMP','*'),
        ('','ORIG','BUF1+100'), ('','CON','BUF2+100'),
        ('','ORIG','BUF2+100'), ('','CON','BUF1+100'),
        ('','ORIG','3000'), ('START','IN','BUF1(U)'), ('','IN','BUF2(U)'),
        ('','ENN6','101'), ('CALL','JMP','WORDIN'), ('RETURN','NOP',''),
        ('','END','START')]


def wordout(corrected=True):
    rows=[('V','EQU','1'), ('','ORIG','100'),
          ('WORDOUT','STJ','1F'), ('','STA','0,5'), ('','INC5','1'),
          ('2H','CMP5','BUFMAX'), ('1H','JNE','*'),
          ('','OUT','-100,5(V)'), ('','LD5','0,5'), ('','ST5','BUFMAX'),
          ('','DEC5','100'), ('','JMP','2B')]
    if corrected:
        rows += [('', 'ORIG','1000'), ('OUTBUF1','ORIG','*+100'),
                 ('ENDBUF1','CON','*+101'), ('OUTBUF2','ORIG','*+100'),
                 ('ENDBUF2','CON','ENDBUF1'), ('BUFMAX','CON','ENDBUF1')]
    else:
        # The original has inadmissible forward references in CON W-values.
        rows += [('BUFMAX','CON','ENDBUF1'), ('','ORIG','1000'),
                 ('OUTBUF1','ORIG','*+100'), ('ENDBUF1','CON','ENDBUF2'),
                 ('OUTBUF2','ORIG','*+100'), ('ENDBUF2','CON','ENDBUF1')]
    rows += [('', 'ORIG','3000'), ('START','ENT5','OUTBUF1'),
             ('CALL','JMP','WORDOUT'), ('RETURN','NOP',''),
             ('FINISH','LDA','BUFMAX'), ('','DECA','100,5'), ('','JAZ','*+6'),
             ('','STZ','0,5'), ('','INC5','1'), ('','CMP5','BUFMAX'),
             ('','JNE','*-3'), ('','OUT','-100,5(V)'), ('STOP','HLT',''),
             ('','END','START')]
    return rows


def tape_copy(corrected=True, unrolled=False):
    rows=[('U','EQU','0'), ('V','EQU','1'), ('','ORIG','1000'),
          ('BUF1','ORIG','*+100'), ('BUF2','ORIG','*+100'),
          ('BUF3','ORIG','*+100'), ('','ORIG','100'),
          ('TAPECPY','IN','BUF1(U)')]
    if unrolled:
        for k in range(1,100):
            rows += [('', 'IN',f'BUF{k%3+1}(U)'),
                     ('', 'OUT',f'BUF{(k-1)%3+1}(V)')]
    else:
        rows += [('', 'ENT1','99'), ('1H','IN','BUF2(U)'),
                 ('','OUT','BUF1(V)'), ('','IN','BUF3(U)'),
                 ('','OUT','BUF2(V)'), ('','IN','BUF1(U)'),
                 ('','OUT','BUF3(V)'), ('','DEC1','3'), ('','J1P','1B')]
    if corrected: rows += [('', 'JBUS','*(U)')]
    rows += [('', 'OUT','BUF1(V)'), ('','HLT',''), ('','END','TAPECPY')]
    return rows


def ring_routines(n=2, unit=16, termination='none'):
    """Printed Programs A/R/B; input termination is original answer12 or CI repair."""
    length=16 if unit==16 else 100
    rows=[('N','EQU',str(n)),('U','EQU',str(unit))]
    for i in range(n):rows += [(f'BUF{i+1}','EQU',str(1000+i*(length+1)))]
    for i in range(n):rows += [('', 'ORIG',f'BUF{i+1}-1'),
                             ('','CON',f'BUF{(i+1)%n+1}')]
    rows += [('', 'ORIG','100'),
             ('ASSIGN','STJ','9F'),('1H','JRED','CONTROL(U)'),
             ('','CMP6','=N='),('','JE','1B'),('','LD4','NEXTG'),
             ('','LDX','-1,4'),('','STX','NEXTG'),('9H','JMP','*'),
             ('RELEASE','INC6','1'),('','JRED','CONTROL(U)'),
             ('','JMP','RELEASERET'),
             ('CONT1','JMP','COMPUTE'), ('1H','J6Z','*-1'),
             ('','IN','0,5(U)'), ('','JMP','COMPUTE')]
    if termination=='none':
        rows += [('DONEIO','LD5','-1,5'),('','DEC6','1'),('','JMP','1B')]
    elif termination=='printed':
        rows += [('DONEIO','STA','2F'),('','LDA','3F'),
                 ('','CMPA','15,5(5:5)'),('','LDA','2F'),
                 ('','LD5','-1,5'),('','DEC6','1'),('','JNE','1B'),
                 ('','JMP','COMPUTE'),('','JMP','*-1'),
                 ('2H','CON','0'),('3H','ALF','    .')]
    elif termination=='preserve_ci':
        restore=[('', 'LDA','CISAVE'),('','CMPA','=0='),('','LDA','ASAVE')]
        rows += [('DONEIO','STA','ASAVE'),('','ENTA','-1'),('','JL','SAVECI'),
                 ('','ENTA','1'),('','JG','SAVECI'),('','ENTA','0'),
                 ('SAVECI','STA','CISAVE'),('','LDA','PERIOD'),
                 ('','CMPA','15,5(5:5)'),('','LD5','-1,5'),('','DEC6','1'),
                 ('','JE','ENDINPUT')]
        rows += restore+[('', 'JMP','1B')]
        rows += [('ENDINPUT','NOP','')]+restore
        rows += [('', 'JMP','COMPUTE'),('','JMP','*-1'),
                 ('ASAVE','CON','0'),('CISAVE','CON','0'),('PERIOD','ALF','    .')]
    else:raise ValueError(termination)
    rows += [('CONTROL','STJ','COMPUTEX'),('CONTROLX','JMP','CONT1'),
             ('COMPUTE','STJ','CONTROLX'),('COMPUTEX','JMP','COMP1'),
             ('NEXTG','CON','BUF1')]
    return rows


def comparison_example(termination='printed', ci=-1):
    rows=ring_routines(termination=termination)
    rows += [('', 'ORIG','500'),('START','ENT5','BUF1'),('','ENT6','N'),
             ('COMP1','JMP','ASSIGN'),('','JBUS','*(U)'),
             ('','ENTA','0'),('','CMPA',f'={-ci}='),('','JRED','CONTROL(U)'),
             ('',{-1:'JL',0:'JE',1:'JG'}[ci],'SUCCESS'),('FAIL','HLT',''),('SUCCESS','HLT',''),
             ('RELEASERET','EQU','SUCCESS'),('','END','START')]
    return rows


def ring_workload(n, mode, blocks, before=0, after=0):
    """Complete test application of the printed circle algorithm.

    Input uses the CI-preserving termination repair; output uses the original
    CONTROL with OUT substituted for IN and the answer13 final drain.
    """
    unit=16 if mode=='input' else 1
    length=16 if mode=='input' else 100
    rows=ring_routines(n,unit,'preserve_ci' if mode=='input' else 'none')
    if mode=='output':
        rows=[(l,'OUT' if o=='IN' and a=='0,5(U)' else o,a) for l,o,a in rows]
    rows += [('DATA','EQU','2000'),('RESULTS','EQU','2700'),
             ('','ORIG','500'),('START','ENT5','BUF1'),
             ('','ENT6','N' if mode=='input' else '0'),('','ENT2','0'),
             ('COMP1','JMP','ASSIGN')]
    if mode=='input':
        rows += [('ASSIGNED','ENT1','RESULTS,2'),('','MOVE','0,4(16)')]
    else:
        rows += [('ASSIGNED','ENT1','0,4'),('','MOVE','DATA,2(50)'),
                 ('','MOVE','DATA+50,2(50)')]
    rows += [('', 'INC2',str(length)),('','ENT3',str(before)),
             ('PAUSEA','J3Z','RELEASEINLINE'),('','JRED','CONTROL(U)'),
             ('','DEC3','1'),('','JMP','PAUSEA'),
             ('RELEASEINLINE','INC6','1'),('','JRED','CONTROL(U)'),
             ('','ENT3',str(after)),('PAUSEB','J3Z','NEXTBLOCK'),
             ('','JRED','CONTROL(U)'),('','DEC3','1'),('','JMP','PAUSEB'),
             ('NEXTBLOCK','CMP2',f'={blocks*length}='),('','JL','COMP1')]
    if mode=='output':
        rows += [('DRAIN','JRED','CONTROL(U)'),('','J6NZ','DRAIN')]
    rows += [('STOP','HLT',''),('RELEASERET','EQU','STOP'),('','END','START')]
    return rows

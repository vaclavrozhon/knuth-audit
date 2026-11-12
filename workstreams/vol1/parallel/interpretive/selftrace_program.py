"""An actual MIX self-interpreter with disjoint logical memory at every level.

Physical layout: dictionary pairs0..1999; immutable ROM image2000..2999;
executing interpreter3000..3999. The logical machine has the same layout.
The ROM image is data in the load image, not an execution hook. Every step
after loading is performed by the ordinary unmodified MIX emulator.
"""
from programs import SIM_HEAD,SIM_BODY,SHIFT,MOVE,SPEC,parse
from mixal import Assembly
from mix_machine import OPS,number


MEMORY = parse('''
001|USED|CON|0
002|VREAD|STJ|READRET
003||ST1|READREST(0:2)
004||J5N|MEMERROR
005||CMP5|=4000=
006||JGE|MEMERROR
007||ENT1|0
008|1H|CMP1|USED
009||JGE|READMISS
010||CMP5|0,1
011||JE|READHIT
012||INC1|2
013||JMP|1B
014|READHIT|LDA|1,1
015||JMP|READREST
016|READMISS|CMP5|=2000=
017||JL|READZERO
018||ENT1|0,5
019||CMP5|=3000=
020||JL|*+2
021||DEC1|1000
022||LDA|0,1
023||JMP|READREST
024|READZERO|ENTA|0
025|READREST|ENT1|0
026|READRET|JMP|*
027|VWRITE|STJ|WRITERET
028||ST1|WRITEREST(0:2)
029||J5N|MEMERROR
030||CMP5|=4000=
031||JGE|MEMERROR
032||ENT1|0
033|1H|CMP1|USED
034||JGE|WRITENEW
035||CMP5|0,1
036||JE|WRITEHIT
037||INC1|2
038||JMP|1B
039|WRITENEW|CMP1|=CAPACITY=
040||JGE|MEMFULL
041||ST5|0,1
042||LDA|USED
043||INCA|2
044||STA|USED
045|WRITEHIT|STX|1,1
046|WRITEREST|ENT1|0
047|WRITERET|JMP|*
''')


PRINT = parse('''
001|LOG|STJ|LOGRET
002||ENTA|0
003||CHAR|0
004||STA|LOGBUF
005||STX|LOGBUF+1
006||ENTA|0,6
007||CHAR|0
008||STA|LOGBUF+2
009||STX|LOGBUF+3
010||LDA|INST
011||CHAR|0
012||STA|LOGBUF+4
013||STX|LOGBUF+5
014||LDA|PLUS
015||LDX|INST
016||JXNN|*+2
017||LDA|MINUS
018||STA|LOGBUF+6
019||OUT|LOGBUF(18)
020||JBUS|*(18)
021|LOGRET|JMP|*
022|PLUS|ALF|+    
023|MINUS|ALF|-    
''')


OUTPUT = parse('''
001|OUT|CMP3|=18=
002||JNE|FERROR
003||J5N|MEMERROR
004||CMP5|=3976=
005||JG|MEMERROR
006||ENT1|0
007|1H|JMP|VREAD
008||STA|OUTBUF,1
009||INC5|1
010||INC1|1
011||CMP1|=24=
012||JL|1B
013||LDA|OUTBUF
014||LDX|OUTBUF+1
015||NUM|0
016||INCA|1
017||CHAR|0
018||STA|OUTBUF
019||STX|OUTBUF+1
020||OUT|OUTBUF(18)
021||JBUS|*(18)
022||JMP|CYCLE
023|JBUS|CMP3|=18=
024||JNE|FERROR
025||JMP|CYCLE
026|JRED|CMP3|=18=
027||JNE|FERROR
028||JMP|JMP
029|IN|JMP|FERROR
030|IOC|JMP|FERROR
''')


def assembly(b=64,capacity=2000):
    assert 0<capacity<=2000 and capacity%2==0
    numbered=[]
    for n,r in SIM_HEAD:
        if n==2:
            r=('', 'ORIG','3000')
        elif n==6:r=('', 'ENT6','BEGIN')
        elif n==10:
            numbered += [(9.1,('', 'ENT5','0,6'))]
            r=('', 'JMP','VREAD')
        numbered.append((n,r))
        if n==11:
            numbered += [(11.1,('', 'JMP','LOG')),(11.2,('', 'LDA','INST'))]
    names={v[0]:k for k,v in OPS.items()}
    for c in range(64):
        dest=({0:'CYCLE',1:'ADD',2:'SUB',3:'MUL',4:'DIV',5:'SPEC',6:'SHIFT',7:'MOVE',
               34:'JBUS',35:'IOC',36:'IN',37:'OUT',38:'JRED',39:'JUMP'}.get(c)
              or ('LOAD' if c<16 else 'LOADN' if c<24 else 'STORE' if c<34 else
                  'REGJUMP' if c<48 else 'ADDROP' if c<56 else 'COMPARE'))
        cost=10 if c in (3,5) else 12 if c==4 else 2 if c in (1,2,6) or 8<=c<34 or c>=56 else 1
        index=',1' if 9<=c<=14 or 17<=c<=22 or 49<=c<=54 else ''
        numbered.append((37+c,('OPTABLE' if c==63 else '', names[c],f'{dest}{index}({cost})')))
    for n,r in SIM_BODY:
        if n==128:r=('', 'CMP5','=4000=')
        if n==130:
            numbered += [(129.1,('', 'JMP','VREAD')),(129.2,('', 'STA','SAVEWORD'))]
            r=('', 'LDX','SAVEWORD')
        if n==133:r=('', 'LDA','SAVEWORD(1:5)')
        if n==218:r=('', 'JMP','VREAD')
        if n==221:r=('', 'JMP','VWRITE')
        numbered.append((n,r))
    rows=[('CAPACITY','EQU',str(capacity))]+[r for _,r in numbered]
    rows += [r for _,r in SHIFT]
    for n,r in MOVE:
        if n==9:r=('', 'CMP1','=4000=')
        if n==11:
            rows += [('', 'ST5','SAVESRC'),('', 'ENT5','0,1'),('', 'JMP','VWRITE'),('', 'LD5','SAVESRC')]
        else:rows.append(r)
    rows += [r for _,r in SPEC]
    rows += [r for _,r in MEMORY]
    rows += [('LOGBUF','CON','0')]+[('','CON','0')]*23
    rows += [('OUTBUF','CON','0')]+[('','CON','0')]*23
    # parse() strips operand whitespace, so pad the two ALF operands explicitly.
    rows += [(lab,op,arg.ljust(5) if op=='ALF' else arg) for _,(lab,op,arg) in PRINT]
    rows += [r for _,r in OUTPUT]
    rows += [(name,'HLT','0') for name in ('INDEXERROR','ADDRERROR','OPERROR','MEMERROR','FERROR','SIZEERROR','MEMFULL')]
    rows += [('', 'END','BEGIN')]
    asm=Assembly(rows,b)
    assert min(asm.memory)==3000 and max(asm.memory)<4000
    # Immutable original source image, also present in every logical machine.
    for m in range(1000):asm.memory[2000+m]=asm.memory.get(3000+m,number(0,b))
    return asm


if __name__=='__main__':
    for b in (64,100):
        a=assembly(b)
        print({'b':b,'first':min(a.memory),'last':max(a.memory),'entry':a.start,
               'MEMFULL':a.symbols['MEMFULL'].value(b),'code_words':sum(m>=3000 for m in a.memory)})

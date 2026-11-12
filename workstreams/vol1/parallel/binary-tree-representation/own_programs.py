"""Independent actual MIX answers 13, 15, 16.

COPY uses a breadth-first queue of source/destination pairs, not the book's
thread traversal. DIV/PWR are emitted from explicitly named tree values.
The source generator only emits ordinary MIX instructions: no host callbacks.
Queue workspace 1500..1999 has capacity 250 source nodes; it is private.
"""

def rows():
    out=[]
    def e(op,x='',label=''):out.append((label,op,x))
    for name,value in [('OSRC',1500),('ODST',1750),('OCAP',250)]:e('EQU',str(value),name)
    e('STJ','OCRET','OCOPY')
    for i in range(2,7):e('ST'+str(i),'OCS'+str(i))
    e('ENT6','0,1');e('JMP','OALLOC');e('ST1','OCROOT')
    e('ENT2','0');e('ENT3','1');e('ST6','OSRC');e('ST1','ODST')
    e('ST3','OCTAIL','OCLOOP');e('CMP2','OCTAIL');e('JE','OCDONE')
    e('LD4','OSRC,2');e('LD5','ODST,2');e('INC2','1');e('LD6','0,4(LLINK)');e('J6Z','OCLOOP');e('STZ','OCPREV')
    e('JMP','OALLOC','OCCHILD');e('ENNA','0,5');e('STA','0,1(RLINKT)')
    e('LD4','OCPREV');e('J4Z','OCFIRST');e('ST1','0,4(RLINKT)');e('JMP','OCAPPEND')
    e('ST1','0,5(LLINK)','OCFIRST')
    e('ST1','OCPREV','OCAPPEND');e('CMP3','OCLIMIT');e('JGE','OVERFLOW')
    e('ST6','OSRC,3');e('ST1','ODST,3');e('INC3','1')
    e('LDA','0,6');e('JAN','OCLOOP');e('LD6','0,6(RLINK)');e('JMP','OCCHILD')
    e('LD1','OCROOT','OCDONE')
    for i in range(2,7):e('LD'+str(i),'OCS'+str(i))
    e('JMP','*','OCRET')
    e('STJ','OARET','OALLOC');e('LD1','AVAIL');e('J1Z','OVERFLOW')
    e('LDX','0,1(LLINK)');e('STX','AVAIL');e('STZ','0,1')
    e('LDA','0,6(TYPE)');e('STA','0,1(TYPE)');e('LDA','1,6');e('STA','1,1');e('JMP','*','OARET')

    def start(label):
        e('ST2','OSAV2',label);e('ST3','OV');e('ST4','OU');e('ST5','ODV');e('ST6','ODU')
    def copy(src,dst):e('LD1',src);e('JMP','COPY');e('ST1',dst)
    def tree(label,children,dst):
        if len(children)==2:e('LDX',children[0])
        if children:e('LD1',children[-1])
        e('ENTA',label);e('JMP','TREE'+str(len(children)));e('ST1',dst)
    def mul(u,v,dst):e('LDA',u);e('LD1',v);e('JMP','MULT');e('ST1',dst)
    def finish(target):
        e('LD2','OSAV2');e('LD3','OV');e('LD4','OU');e('LD5','ODV');e('LD6','ODU');e('JMP',target)
    def zero(slot,target):e('LD1',slot);e('LDA','1,1');e('JAZ',target)

    start('ODIV');zero('ODU','ODRIGHT')
    copy('OV','OT1');tree('SLASH',['ODU','OT1'],'ODU')
    e('NOP','','ODRIGHT');zero('ODV','ODEND')
    copy('OV','OT1');tree('CON2',[],'OT2');tree('UPARROW',['OT1','OT2'],'OT3')
    copy('OU','OT1');mul('OT1','ODV','OT2');tree('SLASH',['OT2','OT3'],'ODV')
    e('NOP','','ODEND');finish('SUB')

    start('OPWR');zero('ODU','OPRIGHT')
    copy('OU','OR');e('LD1','OV');e('LDA','0,1(TYPE)');e('JANZ','OPVAR')
    e('LDA','1,1');e('CMPA','CON2+1');e('JE','OPCOEF')
    e('JOV','*+1');e('DECA','1');e('JOV','OVERFLOW')
    e('STA','CON0+1');tree('CON0',[],'OT1');e('STZ','CON0+1');e('JMP','OPRAISE')
    e('NOP','','OPVAR');copy('OV','OT2');tree('CON1',[],'OT3');tree('MINUS',['OT2','OT3'],'OT1')
    e('NOP','','OPRAISE');tree('UPARROW',['OR','OT1'],'OR')
    e('NOP','','OPCOEF');copy('OV','OT1');mul('OT1','OR','OT2');mul('ODU','OT2','ODU')
    e('NOP','','OPRIGHT');zero('ODV','OPEND')
    copy('OU','OT1');tree('LOG',['OT1'],'OT2');mul('OT2','ODV','OT3')
    copy('OU','OT1');copy('OV','OT2');tree('UPARROW',['OT1','OT2'],'OT4');tree('TIMES',['OT3','OT4'],'ODV')
    e('NOP','','OPEND');finish('ADD')
    names=['OCROOT','OCTAIL','OCPREV']+['OCS'+str(i) for i in range(2,7)]+['OSAV2','OU','OV','ODU','ODV','OT1','OT2','OT3','OT4','OR']
    for name in names:e('CON','0',name)
    e('CON','OCAP','OCLIMIT')
    return out

REDIRECT={'COPY':'OCOPY','DIV':'ODIV','PWR':'OPWR'}

if __name__=='__main__':
    import sys
    sys.dont_write_bytecode=True
    from pathlib import Path
    from programs import assemble
    a=assemble(64,True,rows(),REDIRECT)
    path=Path(__file__).resolve().parent/'results'/'own-complete.mixal'
    path.write_text('\n'.join(f'{l:12} {op:7} {x}' for l,op,x in a.audit_rows)+'\n')
    print('Independent COPY/DIV/PWR integrated; highest code/data address',max(a.memory))

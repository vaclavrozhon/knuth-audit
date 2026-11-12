"""Transcriptions of §1.3.2-10, pp.513–514, with 1999/2013 corrections.

m,n parameterize the displayed 9-by-8 layouts for boundary checks only.
The program begins at 200; scratch words precede the matrix at 1000+n+1.
"""
from mixal import Assembly
from mix_machine import Machine, number


def solution1(m=9, n=8):
    return [
        ('A10','EQU',str(1000+n)), ('LIST','EQU','1000'), ('','ORIG','200'),
        ('START','ENT1',str(m*n)), ('ROWMIN','ENT2',str(n)),
        ('2H','LDX','A10,1'), ('','ENT3','0'), ('4H','INC3','1'),
        ('','ST2','LIST,3'), ('1H','DEC1','1'), ('','DEC2','1'),
        ('','J2Z','COLMAX'), ('3H','CMPX','A10,1'), ('','JL','1B'),
        ('','JG','2B'), ('','JMP','4B'), ('COLMAX','LD2','LIST,3'),
        ('','INC2',str(m*n-n)), ('1H','CMPX','A10,2'), ('','JL','NO'),
        ('','DEC2',str(n)), ('','J2P','1B'), ('YES','INC1','A10+'+str(n)+',2'),
        ('','HLT',''), ('NO','DEC3','1'), ('','J3P','COLMAX'),
        ('','J1P','ROWMIN'), ('','HLT',''), ('','END','START')]


def solution2(m=9,n=8,fix1999=True,fix2013=True):
    tail=[('NO','DEC3',str(n)), ('','J3P','3B'), ('','ENT1','0'), ('','HLT','')]
    if not fix1999:tail[1:3]=tail[2:3]+tail[1:2]
    return [
        ('CMAX','EQU','1000'), ('A10','EQU','CMAX+'+str(n)), ('','ORIG','200'),
        ('PHASE1','ENT1',str(n)), ('3H','ENT2',str(m*n-n)+',1'), ('','JMP','2F'),
        ('1H','CMPX','A10,2'), ('','JGE','*+2'), ('2H','LDX','A10,2'),
        ('','DEC2',str(n)), ('','J2P','1B'), ('','STX','CMAX+'+str(n)+',2'),
        ('','J2Z','1F'), ('','CMPA','CMAX+'+str(n)+',2'), ('','JLE','*+2'),
        ('1H','LDA','CMAX+'+str(n)+',2'), ('','DEC1','1'), ('','J1P','3B'),
        ('PHASE2','ENT3',str(m*n if fix2013 else m*n-n)),
        ('3H','ENT2',('0' if fix2013 else str(n))+',3'), ('','ENT4',str(n)),
        ('1H','CMPA','A10,2'), ('','JG','NO'), ('','JL','2F'),
        ('','CMPA','CMAX,4'), ('','JNE','2F'), ('','ENT1','A10,2'),
        ('2H','DEC4','1'), ('','DEC2','1'), ('','J4P','1B'), ('','HLT','')
    ]+tail+[('','END','PHASE1')]


def saddles(a):
    m,n=len(a),len(a[0])
    lo=[min(row) for row in a]
    hi=[max(a[i][j] for i in range(m)) for j in range(n)]
    return {1000+n+n*i+j+1 for i in range(m) for j in range(n)
            if lo[i]==a[i][j]==hi[j]}


def scalar1(a):
    """Grouped instruction costs, independent of machine decoding; includes HLT."""
    m,n=len(a),len(a[0]);time=1
    for i in reversed(range(m)):
        row=a[i];v=row[-1];candidates=[n-1];time+=10
        for j in reversed(range(n-1)):
            if row[j]>v:time+=6
            elif row[j]<v:v=row[j];candidates=[j];time+=13
            else:candidates.append(j);time+=11
        for j in reversed(candidates):
            k=next((k for k in range(m) if a[m-1-k][j]>v),m)
            if k==m:return 1000+n+n*i+j+1,time+5*m+5
            time+=5*(k+1)+3
        time+=1
    return 0,time+1


def scalar2(a):
    """Grouped instruction costs, independent of machine decoding; includes HLT."""
    m,n=len(a),len(a[0]);hi=[max(row[j] for row in a) for j in range(n)]
    records=0
    for j in range(n):
        v=a[-1][j]
        for i in reversed(range(m-1)):
            if a[i][j]>v:records+=1;v=a[i][j]
    v=hi[-1];minrecords=0
    for c in reversed(hi[:-1]):
        if c<v:minrecords+=1;v=c
    time=5*m*n+9*n+2*records+2*minrecords
    phase1=time;time+=1
    for i in reversed(range(m)):
        time+=2;answer=0
        for j in reversed(range(n)):
            if a[i][j]<v:time+=5;break
            time+=7
            if a[i][j]==v:
                time+=3
                if hi[j]==v:answer=1000+n+n*i+j+1;time+=1
        else:return answer,time+1,phase1
    return 0,time+2,phase1


def execute(a,which,b=64,**kwargs):
    m,n=len(a),len(a[0]);rows=solution1(m,n) if which==1 else solution2(m,n,**kwargs)
    asm=Assembly(rows,b);machine=Machine(b);asm.load(machine)
    for i,row in enumerate(a):
        for j,x in enumerate(row):machine.mem[1000+n+n*i+j+1]=number(x,b)
    machine.run(asm.start,limit=50000)
    return machine.reg[1].value(b),machine.time


def solution3_distinct(m=9,n=8):
    """One concrete implementation of the third hint, for distinct entries only.

    I5 remembers the current column maximum's offset. On a new minimum of
    column maxima, I6 remembers that row's right boundary and I3 its address.
    Repeated values require retaining all candidate rows, which this omits.
    """
    rows=[]
    for label,op,addr in solution2(m,n):
        if label=='PHASE2':break
        if op=='JGE' and addr=='*+2':addr='*+3'
        if op=='JLE' and addr=='*+2':addr='*+5'
        rows.append((label,op,addr))
        if label=='2H' and op=='LDX':rows.append(('','ENT5','0,2'))
        if label=='1H' and op=='LDA':
            rows += [('','ENT6',str(n)+',5'),('','DEC6','0,1'),('','ENT3','A10,5')]
    return rows+[
        ('PHASE2','ENT1','0,3'),('','ENT2','0,6'),('','ENT4',str(n)),
        ('1H','CMPA','A10,2'),('','JG','NO'),('','DEC2','1'),
        ('','DEC4','1'),('','J4P','1B'),('','HLT',''),
        ('NO','ENT1','0'),('','HLT',''),('','END','PHASE1')]

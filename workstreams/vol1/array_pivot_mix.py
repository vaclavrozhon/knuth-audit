"""Literal p557–559 MIX pivot code; exact normalized floating attachment.

The attachment rejects inexact arithmetic rather than silently substituting
Python float. Tests use representable operations; the linked invariant proves
control correctness for the exercise's specified zero-on-cancellation contract.
"""
from fractions import Fraction as Q
from mix_machine import Machine,Word,number,Undefined
from mixal import Assembly

SOURCE='''ROW|EQU|0:3
UP|EQU|4:5
COL|EQU|0:3
LEFT|EQU|4:5
PTR|EQU|1:3
BROW|EQU|499
BCOL|EQU|599
|ORIG|100
PIVOTSTEP|STJ|9F
S1|LD2|0,1(ROW)
|ST2|I0
|LD3|1,1(COL)
|ST3|J0
|LDA|FONE
|FDIV|2,1
|STA|ALPHA
|LDA|FONE
|STA|2,1
|ENT2|BROW,2
|ENT3|BCOL,3
|JMP|S2
2H|ENTA|BCOL,1
|STA|BCOL,1(PTR)
|LDA|2,2
|FMUL|ALPHA
|STA|2,2
S2|LD2|1,2(LEFT)
|LD1|1,2(COL)
|J1NN|2B
S3|LD3|0,3(UP)
|LD4|0,3(ROW)
9H|J4N|*
|CMP4|I0
|JE|S3
|ST4|I(ROW)
|ENT4|BROW,4
S4A|LD5|1,4(LEFT)
S4|LD2|1,2(LEFT)
|LD1|1,2(COL)
|CMP1|J0
|JE|S4
|ENTA|0,1
|SLA|2
|J1NN|S5
|LDAN|2,3
|FMUL|ALPHA
|STA|2,3
|JMP|S3
1H|ENT4|0,5
|LD5|1,4(LEFT)
S5|CMPA|1,5(COL)
|JL|1B
|JE|S7
S6|LD5|BCOL,1(PTR)
|LDA|I
2H|ENT6|0,5
|LD5|0,6(UP)
|CMPA|0,5(ROW)
|JL|2B
|LD5|AVAIL
|J5Z|OVERFLOW
|LDA|0,5(UP)
|STA|AVAIL
|LDA|0,6(UP)
|STA|0,5(UP)
|LDA|1,4(LEFT)
|STA|1,5(LEFT)
|ST1|1,5(COL)
|LDA|I(ROW)
|STA|0,5(ROW)
|STZ|2,5
|ST5|1,4(LEFT)
|ST5|0,6(UP)
S7|LDAN|2,3
|FMUL|2,2
|FADD|2,5
|JAZ|S8
|STA|2,5
|ST5|BCOL,1(PTR)
|ENT4|0,5
|JMP|S4A
S8|LD6|BCOL,1(PTR)
|JMP|*+2
|LD6|0,6(UP)
|LDA|0,6(UP)
|DECA|0,5
|JANZ|*-3
|LDA|0,5(UP)
|STA|0,6(UP)
|LDA|1,5(LEFT)
|STA|1,4(LEFT)
|LDA|AVAIL
|STA|0,5(UP)
|ST5|AVAIL
|JMP|S4A
RETURN|HLT|
OVERFLOW|HLT|
FONE|CON|0
|END|PIVOTSTEP'''
ROWS=[tuple(line.split('|')) for line in SOURCE.splitlines()]


def decode(w,b):
    e,*ds=w.digits;v=0
    for d in ds:v=v*b+d
    return Q(w.sign*v)*Q(b)**(e-b//2-4)


def encode(x,b):
    x=Q(x)
    if not x:return number(0,b)
    sign=1 if x>0 else -1;y=abs(x);e=b//2
    while y>=1:y/=b;e+=1
    while y<Q(1,b):y*=b;e-=1
    if not 0<=e<b:raise Undefined('floating exponent range')
    mant=y*b**4
    if mant.denominator!=1:raise Undefined(('inexact floating operation',str(x),b))
    word=number(sign*int(mant),b)
    return Word(sign,(e,)+word.digits[1:])

class ExactFloatMachine(Machine):
    def __init__(self,b):
        super().__init__(b);self.floating_ops=0;self.visits={}
    def step(self):
        self.visits[self.pc]=self.visits.get(self.pc,0)+1
        w=self.read(self.pc);a,z,i,f,c=w.digits
        if f!=6 or c not in [1,2,3,4]:return super().step()
        if self.halted:raise Undefined('step after halt')
        if not 0<=i<=6:raise Undefined('index selector')
        m=w.sign*(a*self.b+z)+(self.reg[i].value(self.b) if i else 0)
        u,v=decode(self.reg[0],self.b),decode(self.read(m),self.b)
        if c==1:y=u+v
        elif c==2:y=u-v
        elif c==3:y=u*v
        else:
            if not v:raise Undefined('floating division by zero')
            y=u/v
        self.reg[0]=encode(y,self.b)
        self.pc+=1;self.steps+=1;self.floating_ops+=1
        self.time+={1:4,2:4,3:9,4:11}[c]


def run_pivot(a,pi,pj,b=64,node_addresses=None,free_count=None):
    ass=Assembly(ROWS,b);m=ExactFloatMachine(b)
    for p,w in ass.memory.items():m.mem[p]=w
    sym={k:v.value(b) for k,v in ass.symbols.items()}
    m.mem[sym['FONE']]=encode(1,b)
    rows,cols=len(a),len(a[0]);nonzero=sum(bool(x) for row in a for x in row)
    if free_count is None:free_count=rows*cols+3
    count=nonzero+free_count
    if node_addresses is None:node_addresses=[1000+3*t for t in range(count)]
    assert len(node_addresses)>=count and len(set(node_addresses[:count]))==count
    assert all(0<=p<=3997 for p in node_addresses[:count])
    used={};at=0
    for i,row in enumerate(a,1):
        for j,v in enumerate(row,1):
            if v:used[i,j]=node_addresses[at];at+=1
    def rh(i):return sym['BROW']+i
    def ch(j):return sym['BCOL']+j
    for i in range(1,rows+1):
        chain=[used[i,j] for j in range(cols,0,-1) if (i,j) in used]
        m.mem[rh(i)+1]=number(-(b*b+(chain[0] if chain else rh(i))),b)
        for k,p in enumerate(chain):
            j=next(j for j in range(1,cols+1) if used.get((i,j))==p)
            m.mem[p+1]=number(j*b*b+(chain[k+1] if k+1<len(chain) else rh(i)),b)
            m.mem[p+2]=encode(a[i-1][j-1],b)
    for j in range(1,cols+1):
        chain=[used[i,j] for i in range(rows,0,-1) if (i,j) in used]
        m.mem[ch(j)]=number(-(b*b+(chain[0] if chain else ch(j))),b)
        for k,p in enumerate(chain):
            i=next(i for i in range(1,rows+1) if used.get((i,j))==p)
            m.mem[p]=number(i*b*b+(chain[k+1] if k+1<len(chain) else ch(j)),b)
    free=node_addresses[at:count]
    for k,p in enumerate(free):m.mem[p]=number(free[k+1] if k+1<len(free) else 0,b)
    m.mem[sym['AVAIL']]=number(free[0] if free else 0,b)
    pivot=used[pi+1,pj+1];m.reg[1]=number(pivot,b);m.reg[7]=number(-987654,b)
    m.j=sym['RETURN'];m.run(sym['PIVOTSTEP'],limit=100000)
    assert m.reg[7]==number(-987654,b)
    if m.pc==sym['OVERFLOW']+1:return {'overflow':True,'steps':m.steps}
    assert m.pc==sym['RETURN']+1
    def lo(p):return m.mem[p].magnitude(b)%(b*b)
    def hi(p):return m.mem[p].sign*(m.mem[p].magnitude(b)//(b*b))
    out=[[Q(0) for _ in range(cols)] for _ in range(rows)]
    row_nodes=set();col_nodes=set();free_nodes=set()
    for i in range(1,rows+1):
        assert hi(rh(i)+1)<0
        p=lo(rh(i)+1);prev=cols+1
        while p!=rh(i):
            assert p not in row_nodes and p in node_addresses[:count]
            j=hi(p+1);assert 0<j<prev and hi(p)==i
            v=decode(m.mem[p+2],b);assert v
            out[i-1][j-1]=v;row_nodes.add(p);prev=j;p=lo(p+1)
    for j in range(1,cols+1):
        assert hi(ch(j))<0
        p=lo(ch(j));prev=rows+1
        while p!=ch(j):
            assert p not in col_nodes and p in row_nodes
            i=hi(p);assert 0<i<prev and hi(p+1)==j
            col_nodes.add(p);prev=i;p=lo(p)
    p=m.mem[sym['AVAIL']].value(b)
    while p:
        assert p not in free_nodes and p not in row_nodes
        free_nodes.add(p);p=lo(p)
    assert row_nodes==col_nodes
    assert row_nodes|free_nodes==set(node_addresses[:count])
    return {'overflow':False,'matrix':out,'steps':m.steps,'floating_ops':m.floating_ops,
            's6':m.visits.get(sym['S6'],0),'s8':m.visits.get(sym['S8'],0),
            'live_nodes':len(row_nodes),'free_nodes':len(free_nodes)}

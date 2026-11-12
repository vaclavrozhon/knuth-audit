"""Buddy R/S: abstract allocator, actual MIX, local specified XOR extension."""
from pathlib import Path
import sys,copy
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from mix_machine import Machine,Word,number,field,Undefined
from mixal import Assembly,put

FWD,BWD,KVAL,TAG,TFWD=10,28,45,0,2
HEAD,TWO,K,L,TEMP=3000,3100,3200,3201,3202


class Buddy:
    def __init__(self,capacity):
        assert capacity>=1
        self.capacity=capacity
        self.m=capacity.bit_length()-1
        self.free=[[] for _ in range(self.m+1)]
        self.used={}
        p=0
        for k in range(self.m,-1,-1):
            if capacity-p >= 1<<k:
                self.free[k].append(p)
                p+=1<<k
        assert p==capacity

    def reserve(self,k,front=False):
        assert 0<=k<=self.m
        for j in range(k,self.m+1):
            if self.free[j]:break
        else:return None,0
        p=self.free[j].pop(0 if front else -1)
        splits=j-k
        while j>k:
            j-=1
            assert not self.free[j]
            self.free[j].append(p+(1<<j))
        self.used[p]=k
        return p,splits

    def liberate(self,p,printed_nonpower_guard=False):
        k=self.used.pop(p)
        merges=0
        while k<self.m:
            q=p^(1<<k)
            if printed_nonpower_guard and q>=self.capacity-(1<<k):break
            if q not in self.free[k]:break
            self.free[k].remove(q)
            p=min(p,q);k+=1;merges+=1
        self.free[k].insert(0,p)
        return p,k,merges

    def key(self):
        return tuple(tuple(row) for row in self.free),tuple(sorted(self.used.items()))

    def validate(self,coalesced=True):
        cells=[None]*self.capacity
        for kind,blocks in [('free',[(p,k) for k,row in enumerate(self.free) for p in row]),('used',self.used.items())]:
            for p,k in blocks:
                assert p%(1<<k)==0 and 0<=p<p+(1<<k)<=self.capacity
                for i in range(p,p+(1<<k)):
                    assert cells[i] is None
                    cells[i]=kind
                if kind=='free' and coalesced:assert p^(1<<k) not in self.free[k]
        assert None not in cells
        return cells


def get(mem,p,f,b):return field(mem[p],f).value(b)
def setf(mem,p,f,v,b):mem[p]=put(mem[p],number(v,b),f)


def memory_of(state,b=64):
    assert state.capacity==1<<state.m and state.m<=11
    mem=[number(0,b)]*4000
    for k,row in enumerate(state.free):
        h=HEAD+k
        mem[h]=number(0,b,-1)
        chain=[h]+row+[h]
        for i,p in enumerate(chain[:-1]):
            setf(mem,p,FWD,chain[i+1],b)
            setf(mem,chain[i+1],BWD,p,b)
        for p in row:
            mem[p]=Word(-1,mem[p].digits)
            setf(mem,p,KVAL,k,b)
        mem[TWO+k]=number(1<<k,b)
    # Positive list sentinel; m+1 is never an allocation size.
    mem[HEAD+state.m+1]=number(1,b)
    # A nonzero forward address lets LD4N distinguish the sentinel from -0.
    setf(mem,HEAD+state.m+1,FWD,HEAD+state.m+1,b)
    mem[state.capacity]=number(0,b)
    return mem


def check_memory(mem,state,b=64):
    for k,expected in enumerate(state.free):
        h=HEAD+k
        actual=[];p=get(mem,h,FWD,b);prev=h
        while p!=h:
            assert p not in actual and 0<=p<state.capacity,(k,actual,p)
            actual.append(p)
            assert mem[p].sign==-1 and get(mem,p,KVAL,b)==k
            assert get(mem,p,BWD,b)==prev,(k,p,'back')
            prev,p=p,get(mem,p,FWD,b)
        assert get(mem,h,BWD,b)==prev
        assert actual==expected,(k,actual,expected)
    for p in state.used:assert mem[p].sign==1,(p,'reserved tag')


class XORMachine(Machine):
    """Only the binary MIX C=5,F=5 extension explicitly requested in ex28."""
    def step(self):
        word=self.read(self.pc)
        a,z,i,f,c=word.digits
        if (c,f)!=(5,5):return super().step()
        if self.b!=64 or self.halted or i>6:raise Undefined('XOR requires binary MIX')
        addr=word.sign*(a*self.b+z)+(self.reg[i].value(self.b) if i else 0)
        if abs(addr)>=self.b*self.b:raise Undefined('XOR effective address')
        value=self.reg[0].magnitude(self.b)^self.read(addr).magnitude(self.b)
        sign=self.reg[0].sign
        self.reg[0]=number(sign*value,self.b,sign)
        self.pc+=1;self.steps+=1;self.time+=2


def rows_r(mode='repaired'):
    """mode=original, published-2006, or repaired FIFO selection."""
    r=[('LINKF','EQU','1:2'),('LINKB','EQU','3:4'),('KVAL','EQU','5:5'),
       ('TAG','EQU','0:0'),('TLINKF','EQU','0:2'),('AVAIL','EQU',str(HEAD)),
       ('TWO','EQU',str(TWO)),('K','EQU',str(K)),('','ORIG','3300'),
       ('R1','LD1','K'),('','ENT2','0,1'),('','ENT3','0'),
       ('','LD4','AVAIL,2(LINKF)'),('SEARCH','ENT5','AVAIL,2'),
       ('','DEC5','0,4'),('','J5NZ','R2'),('','INC2','1'),('','INC3','1'),
       ('','LD4N','AVAIL,2(TLINKF)'),('','J4NN','SEARCH'),('','JMP','OVERFLOW'),
       ('R2','LD5','0,4(LINKF)'),('','ST5','AVAIL,2(LINKF)'),
       ('','ENTA','AVAIL,2'),('','STA','0,5(LINKB)'),('','STZ','0,4(TAG)'),
       ('R3','J3Z','DONE'),('R4','DEC3','1'),('','DEC2','1'),
       ('','LD5','TWO,2'),('','INC5','0,4'),('','ENNA','AVAIL,2'),
       ('','STA','0,5(TLINKF)'),('','STA','0,5(LINKB)'),
       ('','ST5','AVAIL,2(LINKF)'),('','ST5','AVAIL,2(LINKB)'),
       ('','ST2','0,5(KVAL)'),('','J3P','R4'),('DONE','HLT','0'),
       ('OVERFLOW','HLT','1'),('','END','R1')]
    if mode!='original':
        # Exactly the code-field changes in the 6 November 2006 erratum.
        ix=r.index(('R2','LD5','0,4(LINKF)'))
        r[ix]=('R2','LD5','0,4(LINKB)')
        r[ix+1]=('','ST5','AVAIL,2(LINKB)')
        r[ix+3]=('','STA','0,5(LINKF)')
        if mode=='repaired':
            r[ix]=('','LD5','0,4(LINKB)')
            r.insert(ix,('R2','LD4','AVAIL,2(LINKB)'))
    return r


def rows_s():
    return [('LINKF','EQU','1:2'),('LINKB','EQU','3:4'),('KVAL','EQU','5:5'),
       ('AVAIL','EQU',str(HEAD)),('TWO','EQU',str(TWO)),('K','EQU',str(K)),
       ('L','EQU',str(L)),('TEMP','EQU',str(TEMP)),('','ORIG','3400'),
       ('S1','LD4','L'),('','LD1','K'),('LOOP','ENTA','0,4'),
       # NUM with F=5 encodes the specified new XOR opcode without core edits.
       ('','NUM','TWO,1(5)'),('','STA','TEMP'),('','LD5','TEMP'),
       ('','LDA','0,5'),('','JANN','S3'),('','CMP1','0,5(KVAL)'),('','JNE','S3'),
       # Known September 2003 correction: backward first, forward second.
       ('S2','LD2','0,5(LINKB)'),('','LD3','0,5(LINKF)'),
       ('','ST3','0,2(LINKF)'),('','ST2','0,3(LINKB)'),('','INC1','1'),
       ('','CMP4','TEMP'),('','JL','LOOP'),('','ENT4','0,5'),('','JMP','LOOP'),
       ('S3','LD2','AVAIL,1(LINKF)'),('','ENNA','AVAIL,1'),
       ('','STA','0,4(0:4)'),('','ST2','0,4(LINKF)'),('','ST1','0,4(KVAL)'),
       ('','ST4','0,2(LINKB)'),('','ST4','AVAIL,1(LINKF)'),
       ('DONE','HLT','0'),('','END','S1')]


_assembly={}
def execute(mem,k,l=None,b=64,mode='repaired'):
    key=(b,mode) if l is None else (b,'S')
    if key not in _assembly:_assembly[key]=Assembly(rows_r(mode) if l is None else rows_s(),b)
    a=_assembly[key]
    machine=XORMachine(b) if l is not None else Machine(b)
    machine.mem=list(mem);a.load(machine)
    machine.mem[K]=number(k,b)
    if l is not None:machine.mem[L]=number(l,b)
    done=a.symbols['DONE'].value(b)
    overflow=a.symbols['OVERFLOW'].value(b) if l is None else -1
    machine.pc=a.symbols['R1' if l is None else 'S1'].value(b)
    visits={}
    for _ in range(10000):
        if machine.pc in (done,overflow):break
        visits[machine.pc]=visits.get(machine.pc,0)+1
        machine.step()
    else:raise RuntimeError('finite test instruction bound')
    return machine.mem,None if machine.pc==overflow else machine.reg[4].value(b),machine.time,visits,a

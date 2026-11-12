"""Small instruction interpreter for the transcribed 4.2.1 MIX routines.

Signed zeros, independent register signs during shifts, field positioning,
self-modified signs/return addresses, overflow, and instruction costs are kept.
This is not a general MIX assembler. The instruction source is inspected text,
not executable input received from an external service.
"""
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
import re

SOURCE=Path(__file__).resolve().parent/'sources/single-precision.mix'

@dataclass(frozen=True)
class Word:
    sign:int=1
    mag:int=0
    @property
    def val(self):return self.sign*self.mag


def word(n,zero_sign=1):return Word(-1 if n<0 else 1 if n>0 else zero_sign,abs(n))


class Machine:
    def __init__(self,b,original=False,source=SOURCE):
        assert b>=64 and b%4==0
        self.b=b;self.w=b**5;self.ww=b**10
        self.rows=[];self.symbols={};self.memory={};self.code_sign={};self.code_addr={}
        rows=[]
        for line in Path(source).read_text().splitlines():
            if not line or line.startswith('#'):continue
            src,label,op,arg=line.split()
            rows.append([src,label,op,arg])
        if original:
            start=next(i for i,r in enumerate(rows) if r[0]=='A26')
            end=next(i for i,r in enumerate(rows) if r[0]=='A32')
            rows[start:end]=[['A26-old','-','CMPA','=0=(1:1)'],['A27-old','-','JNE','N5'],['A28-old','COMPLEMENT','SRC','5']]
            for r in rows:
                if r[0]=='A38':r[3]='4'
                if r[0]=='A39':r[3]='N3A'
                if r[0]=='A47':r[1]='N3A'
        self.rows=rows
        for pc,(src,label,op,arg) in enumerate(rows):
            if label!='-':assert label not in self.symbols;self.symbols[label]=pc
        for pc,(src,label,op,arg) in enumerate(rows):
            if op=='CON':self.memory[pc]=word(self.constant(arg))
        self.reg={k:Word() for k in ['A','X','1','2','3','4','5','6']}
        self.ret=min(4000,b*b-1);self.j=self.ret;self.ov=False;self.cmp=0
        self.pc=0;self.time=0;self.visits=Counter();self.trace=[];self.halt=None
        self.attrs={}

    def constant(self,s):
        if s in ['HALFWORD','1//2']:return self.w//2
        if s=='WORDMINUS1':return self.w-1
        if s=='BYTE/2':return self.b//2
        if s=='BYTE':return self.b
        if s=='Q':return self.b//2
        if s=='QQ':return self.b*self.b//2
        if s=='BYTE2':return self.b*self.b
        return int(s)

    def expression(self,s,pc):
        terms=re.findall(r'[+-]?[^+-]+',s);total=0
        for t in terms:
            sign=-1 if t.startswith('-') else 1
            t=t.lstrip('+-')
            val=pc if t=='*' else self.symbols[t] if t in self.symbols else self.constant(t)
            total+=sign*val
        return total

    def operand(self,arg,pc,default=(0,5)):
        field=default
        if arg.endswith(')'):
            arg,f=arg.rsplit('(',1);f=f[:-1]
            aliases={'EXP':(1,1),'EXPD':(1,2),'ABS':(1,5),'SIGN':(0,0)}
            field=aliases[f] if f in aliases else (int(f)//8,int(f)%8) if f.isdigit() else tuple(map(int,f.split(':')))
        idx=0
        if ',' in arg:arg,k=arg.split(',');idx=self.reg[k].val
        if arg.startswith('='):
            assert idx==0 and arg.endswith('=')
            return word(self.constant(arg[1:-1])),field
        if pc in self.code_addr:
            addr=self.code_addr[pc]
        else:
            addr=self.expression(arg,pc)
            if pc in self.code_sign:addr=abs(addr)*self.code_sign[pc]
        return addr+idx,field

    def extract(self,w,field):
        l,r=field;assert 0<=l<=r<=5
        n=r-max(l,1)+1
        mag=0 if n<=0 else (w.mag//self.b**(5-r))%self.b**n
        return Word(w.sign if l==0 else 1,mag)

    def fetch(self,operand,field):
        w=operand if isinstance(operand,Word) else self.memory[operand]
        return self.extract(w,field)

    def store(self,addr,field,w):
        if self.rows[addr][2]!='CON':
            if field==(0,0):self.code_sign[addr]=w.sign;return
            if field==(0,2):self.code_addr[addr]=w.mag%(self.b*self.b);return
            raise AssertionError(('unsupported self modification',addr,field))
        old=self.memory[addr];l,r=field;n=r-max(l,1)+1
        mag=old.mag
        if n>0:
            factor=self.b**(5-r);mask=self.b**n
            mag+=(w.mag%mask-(mag//factor)%mask)*factor
        self.memory[addr]=Word(w.sign if l==0 else old.sign,mag)

    def plus(self,reg,v):
        old=self.reg[reg];n=old.val+v.val
        cap=self.w if reg in ['A','X'] else self.b*self.b
        if abs(n)>=cap:
            assert reg in ['A','X'];self.ov=True
        s=word(n,old.sign).sign
        self.reg[reg]=Word(s,abs(n)%cap)

    def load_float(self,u,reg=None,location=None):
        e,F,sign=u
        w=Word(sign,e*self.b**4+abs(F))
        if reg:self.reg[reg]=w
        else:self.memory[self.symbols[location]]=w

    def output_float(self):
        w=self.reg['A'];e,F=divmod(w.mag,self.b**4)
        return e,w.sign*F,w.sign

    def execute(self,entry):
        self.pc=self.symbols[entry]
        for step in range(getattr(self,'max_steps',1000)):
            if self.pc==self.ret:return self
            pc=self.pc;src,label,op,arg=self.rows[pc]
            assert op!='CON',(entry,pc,src)
            observer=getattr(self,'observer',None)
            if observer is not None:observer(self,src)
            self.visits[src]+=1;self.trace.append(src);self.pc+=1
            cost=10 if op=='MUL' else 12 if op=='DIV' else 2 if op.startswith(('LD','ST','CMP')) or op in ['ADD','SUB','SLA','SRA','SLAX','SRAX','SLC','SRC','SLB','SRB'] else 1
            self.time+=cost
            operand,field=self.operand(arg,pc,(0,2) if op=='STJ' else (0,5))
            if op=='MOVE':self.time+=2*(8*field[0]+field[1])
            if label=='N5' and 'first_round' not in self.attrs:
                self.attrs['first_round']={'digit_half':self.reg['A'].mag%self.b==self.b//2,
                                           'tail_half':self.reg['A'].mag%self.b==self.b//2 and not self.reg['X'].mag}
            if src=='A24':self.attrs['fraction_overflow']=self.ov
            if src=='A25':self.attrs['X']=bool(self.reg['X'].mag)
            if src=='A60':self.attrs['round_up']=True
            if src=='A61' and self.ov:self.attrs['round_overflow']=True
            if op=='MOVE':
                count=8*field[0]+field[1]
                for k in range(count):self.store(self.reg['1'].mag+k,(0,5),self.memory[operand+k])
                self.plus('1',word(count))
            elif op.startswith('LD'):
                suffix=op[2:];negative=suffix.endswith('N');reg=suffix[:-1] if negative else suffix
                v=self.fetch(operand,field)
                if negative:v=Word(-v.sign,v.mag)
                if reg not in ['A','X']:assert v.mag<self.b*self.b
                self.reg[reg]=v
            elif op.startswith('ST'):
                reg=op[2:];v=word(self.j) if reg=='J' else Word() if reg=='Z' else self.reg[reg]
                self.store(operand,field,v)
            elif op.startswith('CMP'):
                a=self.extract(self.reg[op[3:]],field).val;v=self.fetch(operand,field).val
                self.cmp=(a>v)-(a<v)
            elif op in ['ADD','SUB']:
                v=self.fetch(operand,field)
                if op=='SUB':v=Word(-v.sign,v.mag)
                self.plus('A',v)
            elif op in ['MUL','DIV']:
                a=self.reg['A'];x=self.reg['X'];v=self.fetch(operand,field)
                if op=='MUL':
                    hi,lo=divmod(a.mag*v.mag,self.w);self.reg['A']=Word(a.sign*v.sign,hi);self.reg['X']=Word(a.sign*v.sign,lo)
                elif a.mag>=v.mag:
                    self.ov=True;self.reg['A']=Word();self.reg['X']=Word()
                else:
                    hi,lo=divmod(a.mag*self.w+x.mag,v.mag);self.reg['A']=Word(a.sign*v.sign,hi);self.reg['X']=Word(a.sign,lo)
            elif op.startswith(('ENT','ENN','INC','DEC')):
                prefix,reg=op[:3],op[3:]
                ins_sign=self.code_sign.get(pc,-1 if arg.startswith('-') else 1)
                v=word(operand,ins_sign)
                if prefix=='ENN':v=Word(-v.sign,v.mag)
                if prefix in ['ENT','ENN']:self.reg[reg]=v
                else:self.plus(reg,v if prefix=='INC' else Word(-v.sign,v.mag))
            elif op in ['SLA','SRA','SLAX','SRAX','SLC','SRC','SLB','SRB']:
                n=operand;assert n>=0
                a,x=self.reg['A'],self.reg['X'];v=a.mag*self.w+x.mag
                if op=='SLA':am=a.mag*self.b**min(n,5)%self.w;xm=x.mag
                elif op=='SRA':am=a.mag//self.b**min(n,5);xm=x.mag
                elif op=='SLAX':am,xm=divmod(v*self.b**min(n,10)%self.ww,self.w)
                elif op=='SRAX':am,xm=divmod(v//self.b**min(n,10),self.w)
                elif op=='SLB':am,xm=divmod((v<<n)%self.ww,self.w)
                elif op=='SRB':am,xm=divmod(v>>n,self.w)
                else:
                    n%=10
                    if op=='SLC':n=(-n)%10
                    split=self.b**n;v=v//split+(v%split)*(self.ww//split);am,xm=divmod(v,self.w)
                self.reg['A']=Word(a.sign,am);self.reg['X']=Word(x.sign,xm)
            elif op.startswith('J'):
                if op in ['JMP','JSJ']:jump=True
                elif op in ['JOV','JNOV']:
                    jump=self.ov if op=='JOV' else not self.ov;self.ov=False
                elif op in ['JL','JE','JG','JGE','JNE','JLE']:
                    jump={'JL':self.cmp<0,'JE':self.cmp==0,'JG':self.cmp>0,'JGE':self.cmp>=0,'JNE':self.cmp!=0,'JLE':self.cmp<=0}[op]
                else:
                    reg=op[1];cond=op[2:];v=self.reg[reg].val
                    jump={'N':v<0,'Z':v==0,'P':v>0,'NN':v>=0,'NZ':v!=0,'NP':v<=0,'O':abs(v)%2==1,'E':abs(v)%2==0}[cond]
                if jump:
                    if op!='JSJ':self.j=pc+1
                    self.pc=operand
            elif op=='HLT':self.halt=operand;return self
            else:raise AssertionError(op)
        raise AssertionError(('nontermination',entry,self.trace[-15:]))

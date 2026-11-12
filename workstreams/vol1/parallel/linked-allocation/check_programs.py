"""Execute original section2.2.3 code plus explicitly identified errata.

General proofs are in notes/. This verifies transcription, fields, branches,
returned data, asynchronous buffers, timing and finite printed examples.
"""
from pathlib import Path
import collections
import itertools
import json
import random
import sys
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parents[1]))
from mix_machine import Machine,Word,number,field
from mixal import Assembly,CHARACTERS
from mix_io import IOMachine
from programs import *

checks=0
profiles=[]
def check(ok,label):
    global checks
    if not ok: raise AssertionError(label)
    checks+=1

def sym(a,name):return a.symbols[name].value(a.b)
def value(m,address):return m.mem[address].value(m.b)
def link(m,address):return field(m.mem[address],37).value(m.b)
def info(m,address):return field(m.mem[address],3).value(m.b)
def install(m,addresses,data):
    for i,(p,y) in enumerate(zip(addresses,data)):
        q=addresses[i+1] if i+1<len(addresses) else 0
        d=number(y,m.b)
        m.mem[p]=Word(d.sign,(*d.digits[-3:],q//m.b,q%m.b))
def chain(m,p):
    out=[]
    while p:
        if p in out:raise AssertionError(('cycle in chain',out,p))
        out.append(p);p=link(m,p)
    return out

def assembly(source,b):
    # Exact expansion of END's implicit words under MIXAL rules11(f),13.
    # Avoid the shared assembler's forward-END-label limitation without edits.
    source=list(source)
    if source[-1][0]=='X' and source[-1][1]=='END':
        tail=[]
        if any(row[2]=='NO' for row in source):tail.append(('NO','CON','0'))
        tail += [('X','EQU','*'),('', 'END',source[-1][2])]
        source=source[:-1]+tail
    return Assembly(source,b)

# Stack and subroutine versions, including both failure exits and sign limits.
for b,length,free_count in itertools.product([64,67,100],[0,1,2,7],[0,1,4]):
    old=[100+11*i for i in range(length)]
    free=[500+13*i for i in range(free_count)]
    data=[(-1)**i*(b**3-1-i) for i in range(length)]
    for name,code in [('push',PUSH),('pop',POP),('insert',INSERT),('delete',DELETE)]:
        a=assembly(LINK_DEFS+code,b);m=Machine(b);a.load(m)
        install(m,old,data);install(m,free,[18]*len(free))
        m.mem[20]=number(old[0] if old else 0,b)
        m.mem[21]=number(free[0] if free else 0,b)
        m.mem[22]=number(-(b**3-1),b)
        for r in range(8):m.reg[r]=number(30+r,b)
        m.reg[0]=m.mem[22];saved=m.reg.copy()
        m.run(a.start)
        insertion=name in ('push','insert')
        succeeded=bool(free if insertion else old)
        expected_head=([free[0]]+old if insertion else old[1:]) if succeeded else old
        expected_free=free[1:] if insertion and succeeded else ([old[0]]+free if succeeded else free)
        check(chain(m,value(m,20))==expected_head,(name,b,length,free_count,'stack'))
        check(chain(m,value(m,21))==expected_free,(name,b,length,free_count,'free'))
        check(m.pc-1==sym(a,'DONE' if succeeded else ('OVERFLOW' if insertion else 'UNDERFLOW')),
              (name,b,length,free_count,'exit'))
        if succeeded:
            if insertion:check(info(m,free[0])==-(b**3-1),(name,'data',b))
            else:check((m.reg[0].value(b) if name=='delete' else value(m,22))==data[0],(name,'returned',b))
            if name in ('push','pop'):check(m.time-1==17,(name,'17u',b,m.time))
            if name in ('insert','delete'):check(m.reg[1].value(b)==(expected_head[0] if expected_head else 0),(name,'I1'))
        if name in ('insert','delete'):
            check(all(m.reg[r]==saved[r] for r in [4,5,6,7]),(name,'preserved registers'))
            if name=='insert':check(m.reg[0]==saved[0],('insert A preserved'))

# Overflow recovery: positive/negative/signed-zero I1 and exact boundary.
for b,old_i1,gap in itertools.product([64,100],[-19,-1,0,19],[2,3,7]):
    a=assembly(LINK_DEFS+OVERFLOW,b);m=Machine(b);a.load(m)
    for r in range(8):m.reg[r]=number(r*2-7,b)
    m.reg[1]=number(old_i1,b,-1 if old_i1==0 else 1)
    saved=m.reg.copy();m.mem[24]=number(1500,b);m.mem[25]=number(1500+gap,b)
    m.mem[21]=number(0,b);m.mem[1500]=Word(-1,(2,3,4,8,9));m.j=1002
    m.run(a.start,stop=1000)
    check(value(m,24)==1503 and value(m,21)==1500,('overflow pool',b,gap))
    if gap<3:check(m.halted and m.pc-1==sym(a,'TOOBAD'),('overflow rejected',b))
    else:
        check(m.pc==1000 and not m.halted,('overflow returned',b,gap))
        check(m.reg==saved,('overflow preserves all data registers',b,old_i1))
        check(m.mem[1500]==Word(-1,(2,3,4,0,0)),('overflow fields',b))

for b,length in itertools.product([64,67,100],[0,1,2,3,4,5,7,99,501]):
    addresses=[100+3*((97*i)%800) for i in range(length)]
    data=[(-1)**i*(i+5) for i in range(length)]
    for name,code in [('book',REVERSE),('unrolled',FAST_REVERSE)]:
        a=assembly(LINK_DEFS+code,b);m=Machine(b);a.load(m)
        install(m,addresses,data);m.mem[23]=number(addresses[0] if addresses else 0,b)
        m.run(a.start)
        check(chain(m,value(m,23))==list(reversed(addresses)),('reverse',name,b,length))
        check([info(m,p) for p in addresses]==data,('reverse data',name,b,length))
        check(m.time-1==(7*length+6 if name=='book' else 5*length+6+(length%3!=2)),
              ('reverse time',name,b,length,m.time))

class TapeMachine(IOMachine):
    """Local extension: 100-word tapes0..7 and IOC0 rewind, with busy ownership."""
    LENGTH=dict(IOMachine.LENGTH,**{})
    LENGTH.update({k:100 for k in range(8)})
    def __init__(self,b,delay):
        super().__init__(b,delay);self.cpu_time=0;self.io_issues=0;self.visits=collections.Counter()
    def step(self):
        self._finish_input();w=self.read(self.pc);code=w.digits[4];unit=w.digits[3]
        self.visits[self.pc]+=1
        if code in (35,36,37):self.io_issues+=1
        if code==35 and unit in range(8):
            a,z,i,_,_=w.digits
            adr=w.sign*(a*self.b+z)+(self.reg[i].value(self.b) if i else 0)
            if adr!=0:raise ValueError('only tape rewind needed')
            if unit in self.devices:
                self.time=max(self.time,self.devices[unit][0]);self._finish_input()
            delay=self.delay(unit,code) if callable(self.delay) else self.delay
            self.devices[unit]=(self.time+1+delay,code,0,())
            self.pc+=1;self.time+=1;self.steps+=1
            return
        before=self.time
        super().step()
        if not 34<=code<=38:self.cpu_time+=self.time-before

def expected_topo(n,edges,descending=True):
    succ=[[] for _ in range(n+1)];deg=[0]*(n+1)
    for j,k in edges:succ[j].insert(0,k);deg[k]+=1
    q=collections.deque(j for j in (range(n,0,-1) if descending else range(1,n+1)) if deg[j]==0)
    out=[]
    while q:
        j=q.popleft();out.append(j)
        for k in succ[j]:
            deg[k]-=1
            if deg[k]==0:q.append(k)
    return out

book_edges=[(9,2),(3,7),(7,5),(5,8),(8,6),(4,6),(1,3),(7,4),(9,5),(2,8)]
check(expected_topo(9,book_edges,False)==list(map(int,'193274586')),('answer17 ascending'))
check(expected_topo(9,book_edges)==list(map(int,'912374586')),('answer17 descending'))
cases=[('book',9,book_edges),('bookcycle',9,book_edges+[(9,1),(6,9)])]
for n in [1,2,49,50,51,98,99,100,101,199,200,201]:
    cases.append(('chain'+str(n),n,[(j,j+1) for j in range(1,n)]))
    if n in [1,2,99,100,101]:cases.append(('empty'+str(n),n,[]))
for mcount in [47,48,49,50,98,99,100,148,149,150]:
    cases.append(('duplicates'+str(mcount),2,[(1,2)]*mcount))
cases += [('loop',1,[(1,1)]),('isolatedcycle',4,[(2,3),(3,2)]),('cycleandtail',5,[(1,2),(2,3),(3,1),(3,4),(4,5)])]
rng=random.Random(223)
for trial in range(24):
    n=rng.randrange(2,31);labels=list(range(1,n+1));rng.shuffle(labels)
    edges=[(labels[i],labels[j]) for i in range(n) for j in range(i+1,n) if rng.random()<.15]
    rng.shuffle(edges)
    if trial%3==0:edges += [(labels[-1],labels[0])]
    cases.append(('random'+str(trial),n,edges))
for name,n,edges in cases:
  expected=expected_topo(n,edges)
  for extension,b,delay in itertools.product([False,True],[64,100],[0,97]):
    a=assembly(with_cycles() if extension else TOPO,b);m=TapeMachine(b,delay);a.load(m)
    raw=[0,n]+[v for edge in edges for v in edge]+[0,0]
    raw += [0]*((-len(raw))%100)
    for offset in range(0,len(raw),100):m.inputs[1].append([number(v,b) for v in raw[offset:offset+100]])
    m.run(a.start,limit=1000000);m.finish_io()
    out=[w.value(b) for block in m.outputs[2] for w in block]
    end=out.index(0)
    check(out[:end]==expected,(name,extension,b,delay,'output',out[:end],expected))
    check(len(m.outputs[2])==(len(expected)+1+99)//100,(name,'output records'))
    check(len(expected)==len(set(expected)),(name,'no duplicate vertices'))
    pos={v:i for i,v in enumerate(expected)}
    check(all(k not in pos or (j in pos and pos[j]<pos[k]) for j,k in edges),(name,'precedence'))
    remaining=set(range(1,n+1))-set(expected)
    check(all(any(j in remaining and k==v for j,k in edges) for v in remaining),(name,'residual cycle certificate'))
    if not extension:
        check(m.reg[6].value(b)==len(remaining),(name,'N'))
        x=sym(a,'X');ptr=field(m.mem[x],19).value(b);linked=[]
        while ptr and ptr not in linked:
            linked.append(ptr);ptr=field(m.mem[x+ptr],19).value(b)
        check(linked==expected and ptr==0,(name,'retained QLINK list'))
        if not remaining:
            target=32*len(edges)+24*n+7*((len(edges)+2+49)//50)+2*((n+1+99)//100)+16
            book_time=m.cpu_time-1+m.io_issues
            check(book_time==target,(name,'exact time',book_time,target))
    else:
        lines=[''.join(CHARACTERS[c] for w in row for c in w.digits) for row in m.outputs[18]]
        if not remaining:check(not lines,(name,'no cycle output'))
        else:
            check(lines[0].startswith('LOOP DETECTED IN INPUT:'),(name,'cycle title'))
            cycle=[int(s.strip()) for s in lines[1:]]
            check(len(cycle)>=2 and cycle[0]==cycle[-1] and len(set(cycle[:-1]))==len(cycle)-1,
                  (name,'simple cycle',cycle))
            check(all((y,x) in edges for x,y in zip(cycle,cycle[1:])),(name,'backwards cycle edges',cycle))
            if name=='bookcycle':check(cycle==[1,9,6,4,7,3,1],('answer24 actual cycle',cycle))
    profiles.append(dict(name=name,n=n,m=len(edges),extension=extension,radix=b,delay=delay,
                         outputs=len(expected),cpu_time=m.cpu_time,io_issue_count=m.io_issues))

# General dependency graphs: cycles, shared dependencies, repeated requested roots,
# empty directory/list, zero-length routines, tape order differing from addresses.
allocator_profiles=[]
for trial in range(80):
    count=trial%17
    addresses=[1000+12*i for i in range(count)]
    tape=list(addresses);rng.shuffle(tape)
    deps={p:rng.sample(addresses,rng.randrange(min(count,8)+1)) for p in addresses}
    sizes={p:rng.randrange(0,101) for p in addresses}
    requested=[rng.choice(addresses) for _ in range(trial%9)] if addresses else []
    reachable=set(requested);front=list(requested)
    while front:
        for q in deps[front.pop()]:
            if q not in reachable:reachable.add(q);front.append(q)
    for b in [64,100]:
        a=assembly(ALLOC_DEFS+allocator_fixed(),b);m=Machine(b);a.load(m)
        m.reg[1]=number(13,b) # known 2008 bug is not hidden by initial zero registers
        m.mem[20]=number(len(requested),b);m.mem[21]=number(400,b)
        m.mem[30]=number(tape[0] if tape else 0,b)
        for i,p in enumerate(tape):
            q=tape[i+1] if i+1<len(tape) else 0;d=deps[p]
            m.mem[p]=Word(1 if d else -1,(0 if d else 1,sizes[p]//b,sizes[p]%b,q//b,q%b))
            for j in range(0,len(d),2):
                u=d[j];v=d[j+1] if j+1<len(d) else 0;last=j+2>=len(d)
                m.mem[p+1+j//2]=Word(-1 if last else 1,(1 if last else 0,u//b,u%b,v//b,v%b))
        for i,p in enumerate(requested,1):m.mem[2000+i]=number(p,b)
        m.run(a.start,limit=100000)
        expected_rows=[];base=400
        for p in tape:
            if p in reachable:expected_rows.append((base,p));base+=sizes[p]
        expected_rows.append((base,0))
        actual=[(field(m.mem[2001+i],3).value(b),link(m,2001+i)) for i in range(len(expected_rows))]
        check(actual==expected_rows,('allocator',trial,b,actual,expected_rows))
        check(all(field(m.mem[p],1).value(b)>0 if p in reachable else field(m.mem[p],1).value(b)<=0 for p in addresses),
              ('allocator marks exact closure',trial,b))
        allocator_profiles.append(dict(trial=trial,radix=b,routines=count,requested=len(requested),selected=len(reachable)))

# A direct reproducer of the already published 2008 correction, without directory data.
for corrected in [False,True]:
    a=assembly(ALLOC_DEFS+(allocator_fixed() if corrected else ALLOC),64)
    m=Machine(64);a.load(m);m.reg[1]=number(7,64);m.mem[20]=number(0,64);m.mem[21]=number(400,64)
    m.mem[30]=number(0,64);m.run(a.start)
    check(field(m.mem[2001 if corrected else 2008],3).value(64)==400,('known N=0 erratum',corrected))

result=dict(status='passed',checks=checks,topological_cases=len(profiles),allocator_cases=len(allocator_profiles),
            topological_profiles=profiles,allocator_profiles=allocator_profiles,
            known_errata=['2008-02-26 answer27 N=0 branch'],
            scope=['main push/pop','answers2,3,4,8','own5n+O(1) reversal','ProgramT exact timing and I/O','answer24 cycle printing','answer27 allocator'],
            helper_limitations=['Local tape IOC0 and unit2 extension; no tape seek semantics beyond rewind',
                                'END expansion avoids shared assembler forward-END-label issue'],
            general_proofs=['notes/linked-primitives.md','notes/topological-sort.md','notes/subroutine-allocation.md'])
(ROOT/'results/programs.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','checks','topological_cases','allocator_cases']}))

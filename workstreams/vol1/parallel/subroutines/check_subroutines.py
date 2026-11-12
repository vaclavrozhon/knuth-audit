"""Focused checks of TAOCP 1 section 1.4.1, original pp.186-193,527-528.

The independent expectations below supplement the general proofs in notes/.
This imports the shared, previously validated MIX model without modifying it.
Run from any directory; writes only results/subroutines.json alongside this file.
"""
from pathlib import Path
import itertools
import json
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parents[1]))
from mix_machine import Machine, Word, number, instruction, Undefined
from mixal import Assembly
from mixal_examples import MAXIMUM

checks = 0
cases = {}
findings = []


def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


BODY = [('1H', 'CMPA', 'X,3'), ('', 'JGE', '*+3'),
        ('2H', 'ENT2', '0,3'), ('', 'LDA', 'X,3'),
        ('', 'DEC3', '1'), ('', 'J3P', '1B')]


def max_rows(kind):
    rows = [('X', 'EQU', '1000'), ('', 'ORIG', '3000')]
    if kind == 'saved_i3':
        rows += [('MAX100', 'STJ', 'EXIT'), ('', 'ST3', '3F(0:2)'),
                 ('', 'ENT3', '100'), ('', 'JMP', '2F')]
    elif kind == 'no_j':
        rows += [('MAX100', 'STA', 'EXIT(0:2)'), ('', 'ENT3', '100'),
                 ('', 'JMP', '2F')]
    elif kind == 'inline':
        rows += [('MAXN', 'STJ', '*+1'), ('', 'ENT1', '*'),
                 ('', 'LD3', '0,1'), ('', 'JMP', '2F')]
    elif kind in ('stride', 'stride_one'):
        rows += [('SMAX1', 'ENT1', '1'), ('SMAX', 'STJ', 'EXIT'),
                 ('', 'JMP', '2F')]
    else:
        if kind == 'max50':
            rows += [('MAX50', 'ENT3', '50'), ('', 'JSJ', 'MAXN')]
        elif kind == 'max50_without_jsj':
            rows += [('MAX50', 'STJ', 'EXIT'), ('', 'ENT3', '50'),
                     ('', 'JMP', '2F')]
        rows += [('MAX100', 'ENT3', '100'), ('MAXN', 'STJ', 'EXIT'),
                 ('', 'JMP', '2F')]
    rows += [((l, o, '0,1') if kind.startswith('stride') and o == 'DEC3'
              else (l, o, a)) for l, o, a in BODY]
    if kind == 'two_exit':
        rows += [('', 'JANP', 'EXIT'), ('', 'STX', 'TEMP'),
                 ('', 'CMPA', 'TEMP'), ('', 'JGE', 'EXIT'), ('', 'ENT3', '1')]
    if kind == 'saved_i3':
        rows += [('3H', 'ENT3', '*')]
    rows += [('EXIT', 'JMP', '1,1' if kind == 'inline' else '*,3'
             if kind == 'two_exit' else '*')]
    if kind == 'two_exit':
        rows += [('TEMP', 'CON', '0')]
    return rows


def run_max(kind, values, b=64, n=None, stride=1, old_i1=17, old_i3=-23,
            bound=7, initial_ci=0):
    n = len(values) if n is None else n
    asm = Assembly(max_rows(kind), b)
    machine = Machine(b)
    asm.load(machine)
    for k, value in enumerate(values, 1):
        machine.mem[1000+k] = number(value, b)
    machine.reg = [number(-109,b),number(old_i1,b),number(-24,b),number(old_i3,b),
                   number(31,b),number(-32,b),number(33,b),number(bound,b)]
    machine.comparison = initial_ci
    machine.overflow = True
    if kind in ('stride','stride_one'):
        machine.reg[3] = number(n,b)
        if kind == 'stride':
            machine.reg[1] = number(stride,b)
        entry = 'SMAX1' if kind == 'stride_one' else 'SMAX'
    elif kind == 'inline':
        entry = 'MAXN'
        machine.mem[201] = number(n,b)
    elif kind == 'two_exit' or kind == 'general':
        machine.reg[3] = number(n,b)
        entry = 'MAXN'
    else:
        entry = 'MAX50' if kind.startswith('max50') else 'MAX100'
    machine.mem[200] = instruction(b,'JMP',asm.symbols[entry].value(b))
    if kind == 'no_j':
        machine.reg[0] = number(201,b)  # ENTA *+2 in the calling sequence.
    old = machine.reg.copy()
    machine.run(200,stop=202 if kind == 'inline' else
                202 if kind == 'two_exit' and 0 < max(values[:n]) < bound else 201)
    wanted_indices = list(range(n,0,-stride)) if kind == 'stride' else list(range(n,0,-1))
    maximum = max(values[k-1] for k in wanted_indices)
    winner = max(k for k in wanted_indices if values[k-1] == maximum)
    check(machine.reg[0].value(b) == maximum,(kind,'maximum',b,n,stride))
    check(machine.reg[2].value(b) == winner,(kind,'rightmost maximum',b,n,stride))
    check(machine.overflow and machine.reg[4:] == old[4:],(kind,'preserved flags/registers'))
    return machine, asm, old


for b in (64,100):
    values = [((17*k)%23)-11 for k in range(1,101)]
    for kind in ['general','saved_i3','max50','max50_without_jsj','inline','no_j']:
        n = 50 if kind.startswith('max50') else 100
        m,a,old = run_max(kind,values,b,n)
        expected_i1 = 201 if kind == 'inline' else old[1].value(b)
        check(m.reg[1].value(b)==expected_i1,(kind,'I1'))
        check(m.reg[3] == (old[3] if kind=='saved_i3' else number(0,b)),(kind,'I3'))
        cases[kind] = cases.get(kind,0)+1
    for n in range(1,5):
        for vals in itertools.product([-1,0,1],repeat=n):
            for bound in (-2,0,1,2):
                m,a,old=run_max('two_exit',vals,b,bound=bound)
                check(m.reg[3].value(b)==int(0<max(vals)<bound),'two exits')
                cases['two_exit']=cases.get('two_exit',0)+1
    for n in range(1,11):
        for stride in range(1,13):
            m,a,old=run_max('stride',values,b,n,stride)
            check(m.reg[3].value(b)==-((-n)%stride),'stride residue')
            check(m.reg[1]==old[1],'stride preserves I1')
            cases['stride']=cases.get('stride',0)+1
    m,a,old=run_max('stride_one',[1],b,old_i1=2)
    check(m.reg[1].value(b)==1,'SMAX1 changes I1')
    findings.append({'label':'SMAX1-unlisted-I1','b':b,'input_I1':2,
                     'output_I1':m.reg[1].value(b),'n':1})

# Exercise 3 newly requests exact CI and behavior outside n>=1.
for b in (64,100):
    a=Assembly(MAXIMUM,b)
    for n in range(1,5):
        for values in itertools.product([-1,0,1],repeat=n):
            for ci in (-1,0,1):
                m=Machine(b); a.load(m)
                for k,v in enumerate(values,1): m.mem[1000+k]=number(v,b)
                m.reg[1]=number(n,b); m.j=200; m.comparison=ci
                m.run(3000,stop=200)
                winner=max(k for k,v in enumerate(values,1) if v==max(values))
                expected=ci if n==1 else 1 if max(values)>values[0] else 0 if winner>1 else -1
                check(m.comparison==expected,'exercise 3 comparison')
                check(m.j==3010,'exercise 3 J')
                cases['ex3_positive_CI']=cases.get('ex3_positive_CI',0)+1
    for n in (0,-1,-1000):
        m=Machine(b); a.load(m)
        m.reg[1]=number(n,b); m.j=200; m.comparison=1
        m.mem[1000+n]=number(5,b); m.mem[1001]=number(7,b)
        m.run(3000,stop=200)
        check([m.reg[r].value(b) for r in (0,2,3)]==[5,n,n-1],'ex3 nonpositive')
        check(m.comparison==1 and m.j==3010,'ex3 nonpositive unchanged comparison')
        findings.append({'label':'MAXIMUM-nonpositive-input','b':b,'input_I1':n,
                         'Xn':5,'X1':7,'actual_A_I2_I3':[5,n,n-1],
                         'printed_A_I2_I3':[7,1,n]})

MOVE_ROWS=[('', 'ORIG','3000'),('MOVE','STJ','3F'),('', 'STA','4F'),
 ('','ST2','5F(0:2)'),('','LD2','3F(0:2)'),('','LDA','0,2(0:3)'),
 ('','STA','*+2(0:3)'),('','LD2','5F(0:2)'),('','ENTA','*'),
 ('','LD2','3F(0:2)'),('','LD2N','0,2(4:4)'),('','J2Z','1F'),
 ('','DECA','0,2'),('','STA','2F(0:2)'),('','DEC1','0,2'),
 ('','ST1','6F(0:2)'),('2H','LDA','*,2'),('6H','STA','*,2'),
 ('','INC2','1'),('','J2N','2B'),('1H','LDA','4F'),('5H','ENT2','*'),
 ('3H','JMP','*'),('4H','CON','0')]

for b in (64,100):
    a=Assembly(MOVE_ROWS,b)
    for f in range(b):
        for index in range(7):
            for distance in (-1,0,1,150):
                source=1000; dest=source+distance
                m=Machine(b); a.load(m)
                m.reg=[number(-93,b),number(dest,b),number(-31,b),
                       number(39,b),number(-43,b),number(47,b),number(51,b),number(-73,b)]
                # Restoration must also preserve the sign of zero.
                if f%2==0: m.reg[2]=number(0,b,-1)
                for k in range(850,1250):
                    m.mem[k]=number(((k*31)%173)-86,b,-1 if k%3==0 else 1)
                address=source-(m.reg[index].value(b) if index else 0)
                m.mem[200]=instruction(b,'JMP',3000)
                m.mem[201]=instruction(b,'NOP',address,index,f)
                oldregs=m.reg.copy(); expected=m.mem.copy()
                for k in range(f): expected[dest+k]=expected[source+k]
                m.comparison=-1; m.overflow=True
                m.run(200,stop=202)
                check(m.mem[850:1250]==expected[850:1250],('MOVE memory',b,f,index,distance))
                check(m.reg[0]==oldregs[0] and m.reg[2:]==oldregs[2:],'MOVE restored registers')
                check(m.reg[1].value(b)==dest+f,'MOVE I1')
                check(m.comparison==-1 and m.overflow,'MOVE flags')
                check(m.writes <= set(range(dest,dest+f)) | set(a.memory),'MOVE writes')
                cases['MOVE']=cases.get('MOVE',0)+1

result={'checks':checks,'cases':cases,'findings':findings,
        'method':'Original-page transcription; invariant proofs in notes; independent mathematical expectations, no second simulator claimed.',
        'limits':'MIX data/calling code/routine storage are disjoint; valid source and destination ranges; finite checks supplement general proofs.'}
(ROOT/'results'/'subroutines.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'checks':checks,'cases':cases,'finding_labels':sorted(set(f['label'] for f in findings))},indent=2))

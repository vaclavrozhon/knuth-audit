"""Independent expectations for MIXAL syntax, M/P, sorting and validator.

Exercise 8 is proved by hand in the notes and deliberately not executed here.
"""
from collections import Counter
from pathlib import Path
import itertools
import json
from mix_machine import Machine, Word, number, instruction, Undefined
from mixal import Assembly, CHARACTERS
from mix_io import IOMachine
from mixal_examples import MAXIMUM, SORT, prime_program, validator_program

ROOT = Path(__file__).resolve().parent
checks = 0


def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def decode(words):
    return ''.join(CHARACTERS[d] for word in words for d in word.digits)


# Directly transcribed signed address, index, F, C fields from answer 4, p.511.
PRINTED = [
    (0, 0, 18, 35), (2051, 0, 5, 9), (2050, 0, 5, 10),
    (1, 0, 0, 49), (499, 1, 5, 26), (3016, 0, 1, 41),
    (2, 0, 0, 50), (2, 0, 2, 51), (0, 0, 2, 48),
    (0, 2, 2, 55), (-1, 3, 5, 4), (3006, 0, 1, 47),
    (-1, 3, 5, 56), (1, 0, 0, 51), (3008, 0, 6, 39),
    (3003, 0, 0, 39), (1995, 0, 18, 37), (2035, 0, 2, 52),
    (-50, 0, 2, 53), (501, 0, 0, 53), (-1, 5, 5, 8),
    (0, 0, 1, 5), (0, 4, 12, 31), (1, 0, 1, 52),
    (50, 0, 1, 53), (3020, 0, 2, 45), (0, 4, 18, 37),
    (24, 4, 5, 12), (3019, 0, 0, 45), (0, 0, 2, 5)]


def raw(b, a, i, f, c, zero_sign=1):
    return Word(-1 if a < 0 else 1 if a > 0 else zero_sign,
                (abs(a)//b, abs(a) % b, i, f, c))


# An independent sieve supplies all primes and every displayed table entry.
sieve = [True]*4000
sieve[0:2] = [False, False]
for p in range(2, 64):
    if sieve[p]:
        for k in range(p*p, 4000, p):
            sieve[k] = False
primes = [p for p in range(4000) if sieve[p]][:500]
expected_lines = ['FIRST FIVE HUNDRED PRIMES'.ljust(120)]
expected_lines += [(' '*5+' '.join(f'{primes[r+50*c]:04}' for c in range(10))+' ').ljust(120)
                   for r in range(50)]
shown = [[2,233,547,877,1229,1597,1993,2371,2749,3187],
         [3,239,557,881,1231,1601,1997,2377,2753,3191],
         [5,241,563,883,1237,1607,1999,2381,2767,3203],
         [7,251,569,887,1249,1609,2003,2383,2777,3209],
         [11,257,571,907,1259,1613,2011,2389,2789,3217],
         [229,541,863,1223,1583,1987,2357,2741,3181,3571]]
for row, values in zip([0,1,2,3,4,49], shown):
    check(values == [primes[row+50*c] for c in range(10)], ('printed table', row))

for b in range(64, 101):
    a = Assembly([], b)
    for text, expected in [('-1+5',4),('-1+5*20/6',13),('1//3',b**5//3),('1:3',11)]:
        check(a.expression(text).value(b) == expected, ('expression',b,text))
    check(a.expression('-0').sign == -1, ('negative zero',b))
    check(a.wvalue('1,-1000(0:2)') == Word(-1,(1000//b,1000 % b,0,0,1)), ('W order',b))
    check(a.wvalue('-1000(0:2),1') == number(1,b), ('W overwrite',b))
    check(a.wvalue('1(4:4)').value(b) == b, ('BYTESIZE',b))
    local = Assembly([('', 'ORIG','100'),('2H','EQU','10'),('2H','MOVE','2F(2B)'),
                      ('2H','EQU','2B-3')], b)
    check(local.memory[100] == instruction(b,'MOVE',97,0,10), ('local symbols',b))
    old = Assembly(prime_program(-1), b, reverse_literals=True)
    new = Assembly(prime_program(99), b, reverse_literals=True)
    for k, row in enumerate(PRINTED):
        check(old.memory[3000+k] == raw(b,*row), ('printed assembly',b,k))
    check(old.memory[0] == number(2,b), ('first prime old',b))
    check(old.memory[2050] == number(3,b) and old.memory[2051] == number(-499,b), ('literals',b))
    check(decode([old.memory[k] for k in range(1995,2000)]) == 'FIRST FIVE HUNDRED PRIMES', ('title',b))
    changed = {k for k in set(old.memory)|set(new.memory) if old.memory.get(k) != new.memory.get(k)}
    check(changed == {0,100,3004,3010,3012,3020}, ('2022 relocation impact',b,changed))
    mcode = Assembly(MAXIMUM, b)
    inputs = [[0],[-5], [1,1,1], [1,2,3,4], [4,3,2,1],[-9,-1,-2],
              [-b**5+1,0,b**5-1], [b**5-1,-b**5+1], [0]*100]
    for xs in inputs:
        m = Machine(b);mcode.load(m);m.reg[1]=number(len(xs),b);m.j=2000
        for k,x in enumerate(xs,1001):m.mem[k]=number(x,b)
        records=0;maximum=xs[-1]
        for x in reversed(xs[:-1]):
            if x>maximum:records+=1;maximum=x
        m.run(3000,stop=2000)
        check(m.reg[0].value(b)==max(xs),('maximum',b,xs))
        check(m.reg[2].value(b)==max(k+1 for k,x in enumerate(xs) if x==max(xs)),('rightmost maximum',b))
        check(m.time==5+5*len(xs)+3*records,('maximum time',b,m.time))

profiles=[]
for b,base,delay in itertools.product([64,100],[-1,99],[0,50000]):
    a=Assembly(prime_program(base),b,reverse_literals=True)
    m=IOMachine(b,delay);a.load(m);profile=Counter();start_time=end_time=None
    for _ in range(200000):
        if m.halted:break
        if m.pc==3001:start_time=m.time
        if m.pc==3016:end_time=m.time
        profile[m.pc]+=1;m.step()
    else:raise AssertionError('prime execution limit')
    check(profile[3010]==9538,('division count',b,base,delay))
    check(end_time-start_time==182144,('prime computation time',b,base,delay,end_time-start_time))
    check([m.mem[base+k].value(b) for k in range(1,501)]==primes,('prime memory',b,base))
    m.finish_io()
    check([decode(line) for line in m.outputs[18]]==expected_lines,('printed primes',b,base,delay))
    check(m.controls==[(18,0)],('page advance',b,base))
    profiles.append({'b':b,'base':base,'io_delay':delay,'division_count':profile[3010],
                     'computation_time':end_time-start_time})

for b,delay in itertools.product([64,100],[0,31]):
    a=Assembly(SORT,b);m=IOMachine(b,delay);a.load(m)
    xs=[(k*43 % 101)-50 for k in range(100)]
    m.inputs[0].append([number(x,b) for x in xs])
    m.run(a.start,limit=50000);m.finish_io()
    check([w.value(b) for w in m.outputs[1][0]]==sorted(xs),('selection sort',b,delay))


def valid(c, f, i, addr):
    if c>63 or i>6:return False
    field_ok = f in {8*l+r for l in range(6) for r in range(l,6)}
    if c==0 or c==7: f_ok=True
    elif c in (1,2,3,4,56):f_ok=field_ok or f==6
    elif c==5:f_ok=f<=2
    elif c==6:f_ok=f<=5
    elif 8<=c<=33 or 57<=c<=63:f_ok=field_ok
    elif 34<=c<=38:f_ok=f<=20
    elif c==39:f_ok=f<=9
    elif 40<=c<=47:f_ok=f<=5
    else:f_ok=f<=3
    requires_memory = c in range(1,5) or 7<=c<=34 or 36<=c<=47 or 56<=c<=63
    return f_ok and (not requires_memory or i!=0 or 0<=addr<=3999)


validator_cases=0
for b in [64,100]:
    a=Assembly(validator_program(),b);m=Machine(b);a.load(m)
    def run_case(c,f,i,addr,zero_sign=1):
        global validator_cases
        m.mem[50]=raw(b,addr,i,f,c,zero_sign);m.pc=a.start
        for _ in range(40):
            if m.pc in (10,11):break
            m.step()
        else:raise AssertionError('validator execution limit')
        check((m.pc==10)==valid(c,f,i,addr),('instruction validation',b,c,f,i,addr))
        validator_cases+=1
    for c in range(b):
        for f in range(b):run_case(c,f,0,1000)
    for c in range(b):
        for f in [0,5,6,9,20,45,b-1]:
            for i in [0,1,6,7,b-1]:
                for addr in [-b*b+1,-1,0,3999,4000,b*b-1]:run_case(c,f,i,addr)
            run_case(c,f,0,0,-1)

result={'checks':checks,'assembly_radices':list(range(64,101)),
        'execution_radices':[64,100],'prime_profiles':profiles,
        'validator_cases':validator_cases,
        'scope':'MIXAL examples, full prime output with two I/O delays, maximum, sorting and instruction validation.',
        'limitations':['Structured rows, not a card/terminal parser.','No execution of mystery exercise 8.',
                       'Finite execution cases supplement the general invariants in notes.',
                       'Assembler rejects literals containing *; disk and tape motion are not implemented.']}
(ROOT/'results/mixal-basics.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':checks,'validator_cases':validator_cases,'status':'passed'}))

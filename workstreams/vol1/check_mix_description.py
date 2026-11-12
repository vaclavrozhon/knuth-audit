"""Execute the scanned MIX examples against separately derived results.

This checks every allowed byte radix. It does not claim exhaustive coverage of
all register states or prove unrestricted shortest-program lower bounds.
"""
import itertools
import json
from pathlib import Path
from mix_machine import Machine, Word, number, instruction, OPS

ROOT = Path(__file__).resolve().parent
checks = 0


def check(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def machine(b):
    m = Machine(b)
    m.mem = [number(-12345, b)]*4000
    m.reg = [number(-37, b)]*8
    m.j, m.comparison = 19, -1
    return m


def run(m, rows, start=1000):
    m.program(start, rows)
    m.run(start, stop=start+len(rows))
    return m


clear100 = [('STZ', 0), ('ENT1', 1), ('MOVE', 0, 0, 49), ('MOVE', 0, 0, 50)]
clear_short = [('STZ', 0, 2), ('DEC2', 1), ('J2NN', 3000)]
clear_fast = [('STZ', 0), ('ENT1', 1), ('JMP', 3004), ('MOVE', 0, 0, 63),
              ('DEC2', 63), ('J2P', 3003), ('INC2', 63), ('ST2', 3008, 0, (4, 4)), ('MOVE', 0)]
clear_unrolled = [('JMP', 3995)] + [('STZ', j, 2) for j in range(1, 994)] + [
    ('J2N', 3999), ('DEC2', 993), ('J2NN', 3001), ('ENN1', 0, 2), ('JMP', 3000, 1)]
number_one = [('STZ', 1), ('ENNX', 1), ('STX', 1, 0, (0, 1)), ('SLAX', 1),
              ('ENNA', 1), ('INCX', 1), ('ENT1', 1), ('SRC', 1), ('ADD', 1),
              ('DEC1', -1), ('STZ', 1), ('CMPA', 1), ('MOVE', -1, 1, 1),
              ('NUM', 1), ('CHAR', 1), ('HLT', 1)]
halt_fill = [('ENT1', 0), ('MOVE', 3995), ('MOVE', 0, 0, 43), ('JMP', 3993), ('HLT', 0)]
set_j = [('LDA', -1, 4), ('LDX', 3004), ('STX', -1, 4), ('JMP', -1, 4),
         ('JMP', 3005), ('STA', -1, 4)]
patt = [('LDA', 2000), ('MUL', 2000, 0, (1, 5)), ('STX', 3500, 0, (1, 1)),
        ('SRC', 1), ('MUL', 3500), ('STA', 3501), ('ADD', 2000),
        ('MUL', 3501, 0, (1, 5)), ('STX', 3501), ('MUL', 3501, 0, (1, 5)),
        ('SLAX', 1), ('HLT', 0)]
power_short = [('ENT4', 12), ('LDA', 2000), ('MUL', 2000), ('SLAX', 5),
               ('DEC4', 1), ('J4P', 3002), ('HLT', 0)]
power_table = [('LD1', 2000), ('LDA', 3500, 1), ('HLT', 0)]
dixon = [('ENT1', 4), ('LDA', 200), ('SRA', 0, 1), ('SRAX', 1),
         ('DEC1', 1), ('J1NN', 3001), ('SLAX', 5), ('HLT', 0)]
wahid = [('ENT1', 45), ('SLA', 1), ('ST1', 3003, 0, (4, 4)), ('ADD', 200),
         ('DEC1', 9), ('J1P', 3001), ('HLT', 0)]
loader = [('IN', 16, 0, 16), ('IN', 29, 0, 16), ('LD1', 0, 0, (0, 0)),
          ('JBUS', 3, 0, 16), ('LDA', 30), ('SLA', 1), ('SRAX', 6),
          ('NUM', 30), ('STA', 0), ('LDA', 30, 0, (1, 1)), ('SUB', 7, 0, (0, 2)),
          ('LD3', 0), ('JAZ', 0, 3), ('STA', 29), ('LDA', 0), ('ADD', 5, 0, (0, 2)),
          ('STA', 0), ('LDA', 32, 1, (5, 5)), ('SUB', 22, 0, (0, 2)),
          ('STA', 0, 3, (0, 0)), ('LDA', 31, 1), ('LDX', 32, 1), ('NUM', 25),
          ('STA', 0, 3, (1, 5)), ('MOVE', 0, 1, 2), ('LDA', 29),
          ('SUB', 5, 0, (0, 2)), ('JAP', 11), ('JMP', 1)]

# Direct transcription of the punched characters on p.510, with the two
# documented corrections: line 03 uses O, and line 27 includes J.
alphabet = ' ABCDEFGHIΔJKLMNOPQRΣΠSTUVWXYZ0123456789.,()+-*/=$<>@;:\''
punched = [' O O6', ' Z O6', '    I', ' C O4', ' 0 EH', ' A  F', ' F CF',
           ' 0  E', '   EU', ' 0 IH', ' G BB', '   EJ', '  CA.', ' Z EU',
           '   EH', ' E BA', '   EU', ' 2A-H', ' S BB', '  C U', ' 1AEH',
           ' 2AEN', ' V  E', '  CLU', '  ABG', ' Z EH', ' E BB', ' J B.', ' A  9']


def card(words):
    return words+[Word(1, (0,)*5)]*(16-len(words))


def data_card(address, values):
    # Each value is (sign, magnitude), so negative zero is representable.
    digits = [1, 2, 3, 4, 5] + [30+len(values)] + [30+int(d) for d in f'{address:04d}']
    for sign, mag in values:
        word = [30+int(d) for d in f'{mag:010d}']
        if sign < 0:
            word[-1] -= 20
        digits.extend(word)
    digits.extend([0]*(80-len(digits)))
    return [Word(1, tuple(digits[k:k+5])) for k in range(0, 80, 5)]


check(sum([360,650,709,7070,3,80,1107,1604,20,220,2000,920,601,800,4,2])//16 == 1009, 'name average')
check([64**j-1 for j in range(2,6)] == [4095,262143,16777215,1073741823], 'capacities')
check(len(OPS) == 144, '144 integer operator names; plus five floating operators')
check(len(alphabet) == 56, 'character table')

for b in range(64, 101):
    # Original field-loading and storing examples; 80 occupies two bytes.
    source = number(-(80*b**3+3*b*b+5*b+4), b)
    for f, sign, magnitude in [(5,-1,80*b**3+3*b*b+5*b+4), (13,1,80*b**3+3*b*b+5*b+4),
                              (29,1,3*b*b+5*b+4), (3,-1,80*b+3), (36,1,5), (0,-1,0), (9,1,80//b)]:
        m = machine(b); m.mem[2000] = source
        run(m, [('LDA', 2000, 0, f)])
        check(m.reg[0] == number(sign*magnitude,b,sign), ('load example',b,f))
    for f, result in [(5,(1,(6,7,8,9,0))), (13,(-1,(6,7,8,9,0))), (45,(-1,(1,2,3,4,0))),
                      (18,(-1,(1,0,3,4,5))), (19,(-1,(1,9,0,4,5))), (1,(1,(0,2,3,4,5)))]:
        m = machine(b); m.mem[2000]=Word(-1,(1,2,3,4,5));m.reg[0]=Word(1,(6,7,8,9,0))
        run(m,[('STA',2000,0,f)])
        check(m.mem[2000] == Word(*result), ('store example',b,f))
    arithmetic = [
        ('ADD', 1234*b**3+b*b+150, 100*b**3+5*b*b+50, 1334*b**3+6*b*b+200, None),
        ('SUB', -(1234*b**3+9), -(2000*b**3+150*b), 766*b**3+149*b+(b-9), None),
        ('MUL', sum(b**k for k in range(5)), sum(b**k for k in range(5)),
         b**3+2*b*b+3*b+4, 5*b**4+4*b**3+3*b*b+2*b+1),
        ('MUL', -(50*b**4+112*b+4), -2*b**4, 100*b**3+224, 8*b**4)]
    for op, a, v, expected_a, expected_x in arithmetic:
        m=machine(b);m.reg[0]=number(a,b);m.mem[2000]=number(v,b)
        run(m,[(op,2000)])
        check(m.reg[0].value(b)==expected_a and (expected_x is None or m.reg[7].value(b)==expected_x),('arithmetic',b,op,a))
    for top in [1234,1235]:
        m=machine(b);m.reg[0]=number(0,b,-1);m.reg[7]=number(-(top*b**3+3*b+1),b);m.mem[2000]=number(-2*b,b)
        run(m,[('DIV',2000)])
        q,r=divmod(top*b**3+3*b+1,2*b)
        check(m.reg[0]==number(q,b) and m.reg[7]==number(-r,b,-1),('division',b,top))
        if top==1234:check(q==617*b*b+1 and r==b+1,('exercise8',b))
    m=machine(b);m.reg[0]=Word(1,(1,2,3,4,5));m.reg[7]=Word(-1,(6,7,8,9,10))
    run(m,[('SRAX',1),('SLA',2),('SRC',4),('SRA',2),('SLC',501)])
    check(m.reg[0]==Word(1,(0,6,7,8,3)) and m.reg[7]==Word(-1,(4,0,0,5,0)),('shifts',b))
    m=machine(b);m.reg[0]=Word(-1,(0,0,31,32,39));m.reg[7]=Word(1,(37,57,47,30,30))
    run(m,[('NUM',0),('INCA',1),('CHAR',0)])
    check(m.reg[0]==Word(-1,(30,30,31,32,39)) and m.reg[7]==Word(1,(37,37,36,39,39)),('conversion',b))
    m=machine(b);run(m,clear100)
    check(m.mem[:100]==[m.zero]*100 and m.writes==set(range(100)) and m.time==203,('clear100',b))
    for n in [0,1,62,63,64,992,993,994,1985,1986,2978,2979,2999]:
        for rows,stop,expected_time in [
            (clear_short,3003,4*(n+1)),
            (clear_fast,3009,2*n+3*(max(0,n-1)//63)+10),
            (clear_unrolled,3999,2*n+3*(n//993)+8)]:
            m=machine(b);m.reg[2]=number(n,b);m.program(3000,rows);next_word=m.mem[n+1];m.run(3000,stop)
            check(m.mem[:n+1]==[m.zero]*(n+1) and m.mem[n+1]==next_word and m.time==expected_time,
                  ('clearN',b,n,len(rows),m.time,expected_time))
    for start in [1,2,1000]:
        m=machine(b);run(m,number_one,start)
        check(m.overflow and m.comparison==0 and m.reg[0]==Word(-1,(30,)*5)
              and m.reg[7]==Word(-1,(31,30,30,30,30)) and m.reg[1]==number(3,b)
              and m.mem[1:3]==[m.zero]*2 and m.time-1==42,('number one',b,start))
    m=machine(b);m.program(3991,halt_fill);m.run(3991)
    check(m.mem==[instruction(b,'HLT')]*4000 and m.pc==3995 and m.reg[1]==number(4000,b),('halt fill',b))
    for n in [1,2,100,2999]:
        m=machine(b);m.reg[4]=number(n,b);m.program(3000,set_j);before=m.mem[:];m.run(3000,3006)
        check(m.j==n and m.mem==before,('set J restore memory',b,n))
    for x in range(-5,6):
        if abs(x**13)>=b**5:continue
        for rows,t in [(patt,54),(power_short,171),(power_table,4)]:
            m=machine(b);m.mem[2000]=number(x,b)
            m.mem[3500]=m.mem[3501]=m.zero
            if rows is power_table:
                for y in range(-5,6):
                    if abs(y**13)<b**5:m.mem[3500+y]=number(y**13,b)
            run(m,rows,3000)
            check(m.reg[0].value(b)==x**13 and m.time-1==t,('power13',b,x,t))
    for digits in [(0,)*5,(b-1,)*5,(1,2,3,4,5),(b-1,0,1,0,b-2)]:
        for rows in [dixon,wahid]:
            m=machine(b);m.reg[0]=number(b**5-1,b)  # Wahid's explicit nonnegative premise
            m.mem[200]=Word(1,digits);run(m,rows,3000)
            check(m.reg[0]==Word(1,digits[::-1]),('reflection',b,digits,len(rows)))
    m=machine(b);m.reg[0]=Word(1,(0,1,2,3,4));m.reg[7]=Word(1,(5,6,7,8,9));m.mem[3500]=number(b**4,b)
    run(m,[('DIV',3500)])
    check(m.reg[0]==Word(1,(1,2,3,4,5)) and m.reg[7]==Word(1,(0,6,7,8,9)),('exercise24 division',b))
    words=[Word(1,tuple(alphabet.index(c) for c in s)) for s in punched]
    check(words==[instruction(b,*r) for r in loader],('punched loader',b))
    check(all(d<48 and d not in (20,21) for w in words for d in w.digits),('reader alphabet',b))
    for delay in [0,17,100]:
        m=machine(b);m.card_delay=delay
        values=[(1,0),(-1,0),(1,b**5-1),(-1,b**5-1),(1,1),(-1,100),(1,123456789)]
        m.cards=[card(words[:16]),card(words[16:]),data_card(100,values),
                 data_card(3999,[(1,17)]),data_card(1000,[(1,123456789),(1,1),(-1,100)]),data_card(1000,[])]
        m.go();m.run(0,1000)
        check(m.mem[100:107]==[number(s*v,b,s) for s,v in values] and m.mem[3999]==number(17,b)
              and m.mem[1000:1003]==[number(123456789,b),number(1,b),number(-100,b)] and not m.cards
              and m.pending is None and m.j==13,('loader result and synchronization',b,delay))

# Independent symbolic positions prove that two shift instructions cannot do
# exercise24(b). Entries are symbols, so this is not a numerical sample.
initial=tuple('0abcdefghi');target=tuple('abcde0fghi')
def shift_symbols(a, f, k):
    n=5 if f<2 else 10
    v=list(a[:n]);tail=list(a[n:])
    if f>=4:
        k=(k if f==4 else -k)%n;v=v[k:]+v[:k]
    else:
        k=min(k,n);v=v[k:]+['0']*k if f%2==0 else ['0']*k+v[:n-k]
    return tuple(v+tail)
shifts=list(itertools.product(range(6),range(11)))
check(all(shift_symbols(shift_symbols(initial,*s),*t)!=target for s in shifts for t in shifts),'no two-shift solution')
v=initial
for s in [(5,4),(1,1),(4,5)]:v=shift_symbols(v,*s)
check(v==target,'three shifts exercise24')

result={'checks':checks,'byte_radices':list(range(64,101)),
        'scope':'Printed integer examples, exercise programs 16–24 and corrected punched-card loader 26; selected boundary states, all byte radices.',
        'limitations':['Not an independent formal verification of the interpreter.',
                       'Program correctness also has algebraic/invariant proofs in notes.',
                       'No unrestricted shortest-program proof for exercises16,17,22,23.',
                       'Two-shift lower bound is exhaustive only within the shift instruction class.',
                       'Only asynchronous card-reader input is implemented; other devices and floating operations raise.'],
        'card_delays':[0,17,100],'integer_operator_names':len(OPS)}
(ROOT/'results/mix-description.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':checks,'status':'passed'}))

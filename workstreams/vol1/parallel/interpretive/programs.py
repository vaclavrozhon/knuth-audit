"""Manual transcriptions checked against original pp.204-214,530-531.

Printed simulator line numbers are retained; no core emulator changes.
The omitted error handlers are separate HLT sentinels, never an assumed fix.
"""
from pathlib import Path
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from mixal import Assembly


def parse(source):
    result = []
    for line in source.strip().splitlines():
        fields = line.split('|')
        assert len(fields) == 4, line
        number, label, op, operand = [f.strip() for f in fields]
        result.append((int(number), (label, op, operand)))
    return result


SIM_HEAD = parse('''
002||ORIG|3500
003|BEGIN|STZ|TIME(0:2)
004||STZ|OVTOG
005||STZ|COMPI
006||ENT6|0
007|CYCLE|LDA|CLOCK
008|TIME|INCA|0
009||STA|CLOCK
010||LDA|0,6
011||STA|INST
012||INC6|1
013||LDX|INST(1:2)
014||SLAX|5
015||STA|M
016||LD2|INST(3:3)
017||J2Z|1F
018||DEC2|6
019||J2P|INDEXERROR
020||LDA|SIGN6,2
021||LDX|I6REG,2
022||SLAX|5
023||ADD|M
024||CMPA|ZERO(1:3)
025||JNE|ADDRERROR
026||STA|M
027|1H|LD3|INST(4:4)
028||LD5|M
029||LD4|INST(5:5)
030||DEC4|63
031||J4P|OPERROR
032||LDA|OPTABLE,4(4:4)
033||STA|TIME(0:2)
034||LD2|OPTABLE,4(0:2)
035||JNOV|0,2
036||JMP|0,2
''')


SIM_BODY = parse('''
101|AREG|CON|0
102|I1REG|CON|0
103|I2REG|CON|0
104|I3REG|CON|0
105|I4REG|CON|0
106|I5REG|CON|0
107|I6REG|CON|0
108|XREG|CON|0
109|JREG|CON|0
110|ZERO|CON|0
111|SIGNA|CON|1
112|SIGN1|CON|1
113|SIGN2|CON|1
114|SIGN3|CON|1
115|SIGN4|CON|1
116|SIGN5|CON|1
117|SIGN6|CON|1
118|SIGNX|CON|1
119|SIGNJ|CON|1
120|SIGNZ|CON|1
121|INST|CON|0
122|COMPI|CON|0
123|OVTOG|CON|0
124|CLOCK|CON|0
126|MEMORY|STJ|9F
127||J5N|MEMERROR
128||CMP5|=BEGIN=
129||JGE|MEMERROR
130||LDX|0,5
131||ENTA|1
132||SRAX|5
133||LDA|0,5(1:5)
134|9H|JMP|*
135|FCHECK|STJ|9F
136||ENTA|0
137||ENTX|0,3
138||DIV|=8=
139||CMPX|=5=
140||JG|FERROR
141||STX|R
142||STA|L
143||LD1|L
144||CMPA|R
145|9H|JLE|*
146||JMP|FERROR
147|GETAV|STJ|9F
148||JMP|1F
149|GETV|STJ|9F
150||JMP|FCHECK
151||JMP|MEMORY
152|1H|J1Z|2F
153||ENTX|1
154||SLA|-1,1
155||SRA|-1,1
156|2H|LD2N|R
157||SRA|5,2
158|9H|JMP|*
160|ADD|JMP|GETV
161||ENT1|0
162||JMP|INC
163|SUB|JMP|GETV
164||ENT1|0
165||JMP|DEC
167|MUL|JMP|GETV
168||CMPX|SIGNA
169||ENTX|1
170||JE|*+2
171||ENNX|1
172||STX|SIGNA
173||STX|SIGNX
174||MUL|AREG
175||JMP|STOREAX
177|DIV|LDA|SIGNA
178||STA|SIGNX
179||JMP|GETV
180||CMPX|SIGNA
181||ENTX|1
182||JE|*+2
183||ENNX|1
184||STX|SIGNA
185||STA|TEMP
186||LDA|AREG
187||LDX|XREG
188||DIV|TEMP
189|STOREAX|STA|AREG
190||STX|XREG
191|OVCHECK|JNOV|CYCLE
192||ENTX|1
193||STX|OVTOG
194||JMP|CYCLE
196|LOADN|JMP|GETV
197||ENT1|47,4
198|LOADN1|STX|TEMP
199||LDXN|TEMP
200||JMP|LOAD1
201|LOAD|JMP|GETV
202||ENT1|55,4
203|LOAD1|STA|AREG,1
204||STX|SIGNA,1
205||JMP|SIZECHK
207|STORE|JMP|FCHECK
208||JMP|MEMORY
209||J1P|1F
210||ENT1|1
211||LDX|SIGNA+39,4
212|1H|LD2N|R
213||SRAX|5,2
214||LDA|AREG+39,4
215||SLAX|5,2
216||ENN2|0,1
217||SRAX|6,2
218||LDA|0,5
219||SRA|6,2
220||SRAX|-1,1
221||STX|0,5
222||JMP|CYCLE
224|JUMP|DEC3|9
225||J3P|FERROR
226||LDA|COMPI
227||JMP|JTABLE,3
228|JMP|ST6|JREG
229||JMP|JSJ
230||JMP|JOV
231||JMP|JNOV
232||JMP|LS
233||JMP|EQ
234||JMP|GR
235||JMP|GE
236||JMP|NE
237|JTABLE|JMP|LE
238|JOV|LDX|OVTOG
239||JMP|*+3
240|JNOV|LDX|OVTOG
241||DECX|1
242||STZ|OVTOG
243||JXNZ|JMP
244||JMP|CYCLE
245|LE|JAZ|JMP
246|LS|JAN|JMP
247||JMP|CYCLE
248|NE|JAN|JMP
249|GR|JAP|JMP
250||JMP|CYCLE
251|GE|JAP|JMP
252|EQ|JAZ|JMP
253||JMP|CYCLE
254|JSJ|JMP|MEMORY
255||ENT6|0,5
256||JMP|CYCLE
258|REGJUMP|LDA|AREG+23,4
259||JAZ|*+2
260||LDA|SIGNA+23,4
261||DEC3|5
262||J3NP|JTABLE,3
263||JMP|FERROR
265|ADDROP|DEC3|3
266||J3P|FERROR
267||ENTX|0,5
268||JXNZ|*+2
269||LDX|INST
270||ENTA|1
271||SRAX|5
272||LDA|M(1:5)
273||ENT1|15,4
274||JMP|1F,3
275||JMP|INC
276||JMP|DEC
277||JMP|LOAD1
278|1H|JMP|LOADN1
279|DEC|STX|TEMP
280||LDXN|TEMP
281|INC|CMPX|SIGNA,1
282||JE|1F
283||SUB|AREG,1
284||JANP|2F
285||STX|SIGNA,1
286||JMP|2F
287|1H|ADD|AREG,1
288|2H|STA|AREG,1(1:5)
289|SIZECHK|LD1|OPTABLE,4(3:3)
290||J1Z|OVCHECK
291||CMPA|ZERO(1:3)
292||JE|CYCLE
293||JMP|SIZEERROR
295|COMPARE|JMP|GETV
296||SRAX|5
297||STX|V
298||LDA|XREG,4
299||LDX|SIGNX,4
300||JMP|GETAV
301||SRAX|5
302||CMPX|V
303||STZ|COMPI
304||JE|CYCLE
305||ENTA|1
306||JG|*+2
307||ENNA|1
308||STA|COMPI
309||JMP|CYCLE
''')


SHIFT = parse('''
1|SHIFT|J5N|ADDRERROR
2||DEC3|5
3||J3P|FERROR
4||LDA|AREG
5||LDX|XREG
6||LD1|1F,3(4:5)
7||ST1|2F(4:5)
8||J5Z|CYCLE
9|2H|SLA|1
10||DEC5|1
11||J5P|2B
12||JMP|STOREAX
13||SLA|1
14||SRA|1
15||SLAX|1
16||SRAX|1
17||SLC|1
18|1H|SRC|1
''')
MOVE = parse('''
1|MOVE|J3Z|CYCLE
2||JMP|MEMORY
3||SRAX|5
4||LD1|I1REG
5||LDA|SIGN1
6||JAP|*+3
7||J1NZ|MEMERROR
8||STZ|SIGN1(0:0)
9||CMP1|=BEGIN=
10||JGE|MEMERROR
11||STX|0,1
12||LDA|CLOCK
13||INCA|2
14||STA|CLOCK
15||INC1|1
16||ST1|I1REG
17||INC5|1
18||DEC3|1
19||JMP|MOVE
''')


# An audit solution of the 2025 exercise, not a transcription of a printed answer.
SPEC = parse('''
1|SPEC|DEC3|2
2||J3P|FERROR
3||J3Z|HALTED
4||LDA|AREG
5||LDX|XREG
6||J3NN|FERROR
7||INC3|1
8||J3Z|1F
9||NUM|0
10||JMP|STOREAX
11|1H|CHAR|0
12||JMP|STOREAX
13|HALTED|LDA|CLOCK
14||INCA|1
15||STA|CLOCK
16||STZ|TIME(0:2)
17||HLT|0
18||JMP|CYCLE
''')


def simulator(b=64, extensions=True, extra_io=None):
    table = []
    from mix_machine import OPS
    names = {v[0]: k for k,v in OPS.items()}
    for c in range(64):
        dest = ({0:'CYCLE',1:'ADD',2:'SUB',3:'MUL',4:'DIV',5:'SPEC',
                 6:'SHIFT',7:'MOVE',34:'JBUS',35:'IOC',36:'IN',37:'OUT',
                 38:'JRED',39:'JUMP'}.get(c)
                or ('LOAD' if c<16 else 'LOADN' if c<24 else 'STORE' if c<34
                    else 'REGJUMP' if c<48 else 'ADDROP' if c<56 else 'COMPARE'))
        cost = 10 if c in (3,5) else 12 if c==4 else 2 if c in (1,2,6) or 8<=c<34 or c>=56 else 1
        index = ',1' if 9<=c<=14 or 17<=c<=22 or 49<=c<=54 else ''
        table.append((37+c, ('OPTABLE' if c==63 else '', names[c], f'{dest}{index}({cost})')))
    head = SIM_HEAD[:]
    if extra_io is not None:
        at=next(k for k,(n,_) in enumerate(head) if n==9)
        head.insert(at+1,(9.1,('','JMP','TICK')))
    numbered = head+table+SIM_BODY
    rows = [r for _,r in numbered]
    if extensions:
        rows += [r for _,r in SHIFT+MOVE]
        rows += [r for _,r in (SPEC if extra_io is None else extra_io[0])]
    elif extra_io is None:
        rows += [(n,'HLT','0') for n in ('SHIFT','MOVE','SPEC')]
    else:
        rows += [(n,'HLT','0') for n in ('SHIFT','MOVE')]
        rows += [r for _,r in extra_io[0]]
    if extra_io is not None:
        rows += [r for _,r in extra_io[1]]
    else:
        rows += [(n,'HLT','0') for n in ('JBUS','IOC','IN','OUT','JRED')]
    rows += [(n,'HLT','0') for n in ('INDEXERROR',
                                  'ADDRERROR','OPERROR','MEMERROR','FERROR','SIZEERROR')]
    rows += [('', 'END', 'BEGIN')]
    asm = Assembly(rows,b)
    lines = {n: asm.locations[k] for k,(n,_) in enumerate(numbered)}
    return asm, lines


TRACE = parse('''
02|ENTER|STX|TEST(0:2)
03||STX|LEAVEX(0:2)
04||STA|AREG
05||STJ|JREG
06||LDA|JREG(0:2)
07|CYCLE|STA|PREG(0:2)
08|TEST|DECA|*
09||JAZ|LEAVE
10|PREG|LDA|*
11||STA|INST
12||SRA|2
13||STA|INST1(0:3)
14||LDA|INST(5:5)
15||DECA|38
16||JANN|1F
17||INCA|6
18||JANZ|2F
19||LDA|INST(0:4)
20||STA|*+2(0:4)
21|JREG|ENTA|*
22||STA|*
23||JMP|INCP
24|2H|DECA|2
25||JANZ|2F
26||JMP|3F
27|1H|DECA|9
28||JAP|2F
29|3H|LDA|8F(0:3)
30||STA|INST(0:3)
31|2H|LDA|AREG
34|INST|NOP|*
35||STA|AREG
36|INCP|LDA|PREG(0:2)
37||INCA|1
38||JMP|CYCLE
39|8H|JSJ|JUMP
40|JUMP|LDA|8B(4:5)
41||SUB|INST(4:5)
42||JAZ|*+4
43||LDA|PREG(0:2)
44||INCA|1
45||STA|JREG(0:2)
46|INST1|ENTA|*
47||JMP|CYCLE
48|LEAVE|LDA|AREG
49|LEAVEX|JMP|*
50|AREG|CON|0
''')

RESTORE_J = parse('''
1|XREG|ORIG|*+2
2|LEAVE|STX|XREG
3||ST1|XREG+1
4||LD1|JREG(0:2)
5||LDA|-1,1
6||LDX|1F
7||STX|-1,1
8||JMP|-1,1
9|1H|JMP|*+1
10||STA|-1,1
11||LD1|XREG+1
12||LDX|XREG
13||LDA|AREG
14|LEAVEX|JSJ|*
''')


def tracer(b=64, origin=3500, restore_j=False, tape=False, original_erratum=False):
    rows = [('', 'ORIG', str(origin))]
    if tape:
        rows += [('', 'ORIG', '*+99'), ('BUF','CON','0')]
    for n,r in TRACE:
        if restore_j and n==48:
            rows += [x for _,x in RESTORE_J]
        if not restore_j or n not in (48,49):
            rows.append(r)
        if not tape:
            continue
        if n==4: rows += [('', 'ST1','I1REG')]
        if n==7:
            rows += [('PTR','ENT1','-100'), ('','JBUS','*(0)'), ('','STA','BUF+1,1(0:2)')]
        if n==11: rows += [('', 'STA','BUF+2,1')]
        if n==13:
            rows += [('','LDA','AREG'), ('','STA','BUF+3,1'), ('','LDA','I1REG'), ('','STA','BUF+4,1')]
            rows += [('',f'ST{i}', f'BUF+{i+3},1') for i in range(2,7)]
            rows += [('','STX','BUF+10,1'), ('','LDA','JREG(0:2)'), ('','STA','BUF+1,1(4:5)'),
                     ('','ENTA','8'), ('','JNOV','1F'), ('','ADD','BIG'), ('1H','JL','1F'),
                     ('','INCA','1'), ('','JE','1F'), ('','INCA','1'), ('1H','STA','BUF+1,1(3:3)'),
                     ('','INC1','10'), ('','J1N','1F'), ('','OUT','BUF-99(0)'), ('','ENT1','-100'),
                     ('1H','ST1','PTR(0:2)')]
            if not original_erratum: rows += [('', 'LD1','I1REG')]
        if n==31 and original_erratum: rows += [('', 'LD1','I1REG')]
        if n==35: rows += [('', 'ST1','I1REG')]
        if n==48: rows += [('', 'LD1','I1REG')]
    if tape:
        rows += [('B4','EQU','1(1:1)'), ('BIG','CON','B4-8,B4-1(1:1)')]
    rows += [('', 'END','ENTER')]
    return Assembly(rows,b)

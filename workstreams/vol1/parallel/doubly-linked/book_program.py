"""Full literal elevator MIX, printed pp289--296, answers554--555.

Printed line numbers are retained separately from addresses. Known 1998
POOLMAX amendments are applied by default. Omitted symmetric lines190--195
are supplied. E8 and DECISION are the printed answers. A real, table-driven
VALUES completes the runnable program; it is not a host execution hook.
"""
import sys
from pathlib import Path
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from mix_machine import Machine,Word,number,instruction,field,Undefined
from mixal import Assembly


TEXT='''
002|IN|EQU|1:1
003|LLINK1|EQU|2:3
004|RLINK1|EQU|4:5
005|NEXTINST|EQU|0:2
006|OUT|EQU|1:1
007|LLINK2|EQU|2:3
008|RLINK2|EQU|4:5
010|WAIT|CON|*+2(LLINK1),*+2(RLINK1)
011||CON|0
012|USER1|CON|*-2(LLINK1),*-2(RLINK1)
013||CON|0
014||JMP|U1
015|ELEV1|CON|0
016||CON|0
017||JMP|E1
018|ELEV2|CON|0
019||CON|0
020||JMP|E5
021|ELEV3|CON|0
022||CON|0
023||JMP|E9
024|AVAIL|CON|0
025|TIME|CON|0
026|QUEUE|EQU|*-3
027||CON|*-3(LLINK2),*-3(RLINK2)
028||CON|*-3(LLINK2),*-3(RLINK2)
029||CON|*-3(LLINK2),*-3(RLINK2)
030||CON|*-3(LLINK2),*-3(RLINK2)
031||CON|*-3(LLINK2),*-3(RLINK2)
032|ELEVATOR|EQU|*-3
033||CON|*-3(LLINK2),*-3(RLINK2)
034||CON|0
035||CON|0
036||CON|0
037||CON|0
038|CALL|CON|0
039||CON|0
040||CON|0
041||CON|0
042||CON|0
043||CON|0
044||CON|0
045||CON|0
046||CON|0
047|D1|CON|0
048|D2|CON|0
049|D3|CON|0
051|INSERT|STJ|9F
052||LD2|3,1(LLINK2)
053||ST2|3,6(LLINK2)
054||ST6|3,1(LLINK2)
055||ST6|3,2(RLINK2)
056||ST1|3,6(RLINK2)
057|9H|JMP|*
058|DELETE|STJ|9F
059||LD1|3,6(LLINK2)
060||LD2|3,6(RLINK2)
061||ST1|3,2(LLINK2)
062||ST2|3,1(RLINK2)
063|9H|JMP|*
064|IMMED|STJ|9F
065||LDA|TIME
066||STA|1,6
067||ENT1|WAIT
068||JMP|2F
069|HOLD|ADD|TIME
070|SORTIN|STJ|9F
071||STA|1,6
072||ENT1|WAIT
073||LD1|0,1(LLINK1)
074||CMPA|1,1
075||JL|*-2
076|2H|LD2|0,1(RLINK1)
077||ST2|0,6(RLINK1)
078||ST1|0,6(LLINK1)
079||ST6|0,1(RLINK1)
080||ST6|0,2(LLINK1)
081|9H|JMP|*
082|DELETEW|STJ|9F
083||LD1|0,6(LLINK1)
084||LD2|0,6(RLINK1)
085||ST1|0,2(LLINK1)
086||ST2|0,1(RLINK1)
087|9H|JMP|*
088|CYCLE1|STJ|2,6(NEXTINST)
089||JMP|CYCLE
090|HOLDC|STJ|2,6(NEXTINST)
091||JMP|HOLD
092|CYCLE|LD6|WAIT(RLINK1)
093||LDA|1,6
094||STA|TIME
095||JMP|DELETEW
096||JMP|2,6
098|U1|JMP|VALUES
099||LDA|INTERTIME
100||JMP|HOLD
101||LD6|AVAIL
102||J6P|1F
103||LD6|POOLMAX(0:2)
104||INC6|4
105||ST6|POOLMAX(0:2)
106||JMP|*+3
107|1H|LDA|0,6(RLINK1)
108||STA|AVAIL
109||LD1|INFLOOR
110||ST1|0,6(IN)
111||LD2|OUTFLOOR
112||ST2|3,6(OUT)
113||ENTA|39
114||STA|2,6
115|U2|ENTA|0,4
116||DECA|0,1
117||ST6|TEMP
118||JANZ|2F
119||ENT6|ELEV1
120||LDA|2,6(NEXTINST)
121||DECA|E6
122||JANZ|3F
123||ENTA|E3
124||STA|2,6(NEXTINST)
125||JMP|DELETEW
126||JMP|4F
127|3H|LDA|D3
128||JAZ|2F
129||ST6|D1
130||STZ|D3
131|4H|JMP|IMMED
132||JMP|U3
133|2H|DEC2|0,1
134||ENTA|1
135||J2P|*+3
136||STA|CALL,1(5:5)
137||JMP|*+2
138||STA|CALL,1(1:1)
139||LDA|D2
140||JAZ|*+3
141||LDA|ELEV1+2(NEXTINST)
142||DECA|E1
143||JAZ|DECISION
144|U3|LD6|TEMP
145||LD1|0,6(IN)
146||ENT1|QUEUE,1
147||JMP|INSERT
148|U4A|LDA|GIVEUPTIME
149||JMP|HOLDC
150|U4|LDA|0,6(IN)
151||DECA|0,4
152||JANZ|*+3
153||LDA|D1
154||JANZ|U4A
155|U6|JMP|DELETE
156||LDA|AVAIL
157||STA|0,6(RLINK1)
158||ST6|AVAIL
159||JMP|CYCLE
160|U5|JMP|DELETE
161||ENT1|ELEVATOR
162||JMP|INSERT
163||ENTA|1
164||LD2|3,6(OUT)
165||STA|CALL,2(3:3)
166||J5NZ|CYCLE
167||DEC2|0,4
168||ENT5|0,2
169||ENT6|ELEV2
170||JMP|DELETEW
171||ENTA|25
172||JMP|E5A
174|E1A|JMP|CYCLE1
175|E1|EQU|*
176|E2A|JMP|HOLDC
177|E2|J5N|1F
178||LDA|CALL+1,4
179||ADD|CALL+2,4
180||ADD|CALL+3,4
181||ADD|CALL+4,4
182||JAP|E3
183||LDA|CALL-1,4(3:3)
184||ADD|CALL-2,4(3:3)
185||ADD|CALL-3,4(3:3)
186||ADD|CALL-4,4(3:3)
187||JMP|2F
188|1H|LDA|CALL-1,4
189||ADD|CALL-2,4
190||ADD|CALL-3,4
191||ADD|CALL-4,4
192||JAP|E3
193||LDA|CALL+1,4(3:3)
194||ADD|CALL+2,4(3:3)
195||ADD|CALL+3,4(3:3)
196||ADD|CALL+4,4(3:3)
197|2H|ENN5|0,5
198||STZ|CALL,4
199||JANZ|E3
200||ENT5|0
201|E3|ENT6|ELEV3
202||LDA|0,6
203||JANZ|DELETEW
204||ENTA|300
205||JMP|HOLD
206||ENT6|ELEV2
207||ENTA|76
208||JMP|HOLD
209||ST6|D2
210||ST6|D1
211||ENTA|20
212|E4A|ENT6|ELEV1
213||JMP|HOLDC
214|E4|ENTA|0,4
215||SLA|4
216||ENT6|ELEVATOR
217|1H|LD6|3,6(LLINK2)
218||CMP6|=ELEVATOR=
219||JE|1F
220||CMPA|3,6(OUT)
221||JNE|1B
222||ENTA|U6
223||JMP|2F
224|1H|LD6|QUEUE+3,4(RLINK2)
225||CMP6|3,6(RLINK2)
226||JE|1F
227||JMP|DELETEW
228||ENTA|U5
229|2H|STA|2,6(NEXTINST)
230||JMP|IMMED
231||ENTA|25
232||JMP|E4A
233|1H|STZ|D1
234||ST6|D3
235||JMP|CYCLE
236|E5A|JMP|HOLDC
237|E5|LDA|D1
238||JAZ|*+3
239||ENTA|40
240||JMP|E5A
241||STZ|D3
242||ENT6|ELEV1
243||ENTA|20
244||JMP|HOLDC
245|E6|J5N|*+2
246||STZ|CALL,4(1:3)
247||J5P|*+2
248||STZ|CALL,4(3:5)
249||J5Z|DECISION
250|E6B|J5Z|E1A
251||LDA|D2
252||JAZ|*+4
253||ENT6|ELEV3
254||JMP|DELETEW
255||STZ|ELEV3
256||ENT6|ELEV1
257||ENTA|15
258||J5N|E8A
259|E7A|JMP|HOLDC
260|E7|INC4|1
261||ENTA|51
262||JMP|HOLDC
263||LDA|CALL,4(1:3)
264||JAP|1F
265||ENT1|-2,4
266||J1Z|2F
267||LDA|CALL,4(5:5)
268||JAZ|E7
269|2H|LDA|CALL+1,4
270||ADD|CALL+2,4
271||ADD|CALL+3,4
272||ADD|CALL+4,4
273||JANZ|E7
274|1H|ENTA|14
275||JMP|E2A
276|E8A|JMP|HOLDC
277|E8|DEC4|1
278||ENTA|61
279||JMP|HOLDC
280||LDA|CALL,4(3:5)
281||JAP|1F
282||ENT1|-2,4
283||J1Z|2F
284||LDA|CALL,4(1:1)
285||JAZ|E8
286|2H|LDA|CALL-1,4
287||ADD|CALL-2,4
288||ADD|CALL-3,4
289||ADD|CALL-4,4
290||JANZ|E8
291|1H|ENTA|23
292||JMP|E2A
293|E9|STZ|0,6
294||STZ|D2
295||JMP|DECISION
296||JMP|CYCLE
D01|DECISION|STJ|9F
D02||J5NZ|9F
D03||LDX|ELEV1+2(NEXTINST)
D04||DECX|E1
D05||JXNZ|1F
D06||LDA|CALL+2
D07||ENT3|E3
D08||JANZ|8F
D09|1H|ENT1|-4
D10||LDA|CALL+4,1
D11||JANZ|2F
D12|1H|INC1|1
D13||J1NP|*-3
D14||LDA|9F(0:2)
D15||DECA|E6B
D16||JANZ|9F
D17||ENT1|-2
D18|2H|ENT5|4,1
D19||DEC5|0,4
D20||J5NZ|*+2
D21||JANZ|1B
D22||JXNZ|9F
D23||J5Z|9F
D24||ENT3|E6
D25|8H|ENTA|20
D26||ST6|8F(0:2)
D27||ENT6|ELEV1
D28||ST3|2,6(NEXTINST)
D29||JMP|HOLD
D30|8H|ENT6|*
D31|9H|JMP|*
'''


def source():
    return [(n,(label,op,operand)) for n,label,op,operand in
            (line.split('|') for line in TEXT.strip().splitlines())]


def assemble(b=64,original_pool=False,bug_u4=False,extra=(),decision=None,e8=None,no_e9=False):
    numbered=source()
    if bug_u4:numbered=[(n,(l,o,'CYCLE' if n=='154' else x)) for n,(l,o,x) in numbered]
    if no_e9:
        changes={'201':('E3','JMP','NOTIMER3'),'206':('NOTIMER3','ENT6','ELEV2'),
                 '251':('','JMP','NOTIMER6'),'256':('NOTIMER6','ENT6','ELEV1')}
        numbered=[(n,changes.get(n,row)) for n,row in numbered]
    if decision is not None:
        numbered=[(n,row) for n,row in numbered if not n.startswith('D')]+list(decision)
    if e8 is not None:
        i=next(i for i,(n,_) in enumerate(numbered) if n=='277')
        numbered[i:i+16]=list(e8)
    prefix=[('POOL','EQU','900'),('INPUT','EQU','3000'),('','ORIG','100')]
    rows=prefix+[row for n,row in numbered]+list(extra)
    # Four input words per user: floor in, floor out, patience, interarrival.
    # All input tables and termination horizons are set by the caller before
    # execution; VALUES itself runs wholly as MIX instructions.
    aux='''
VALUES|STJ|VRET
|LD3|VPTR
|CMP3|VEND
|JE|FINISH
|LDA|0,3
|STA|INFLOOR
|LDA|1,3
|STA|OUTFLOOR
|LDA|2,3
|STA|GIVEUPTIME
|LDA|3,3
|STA|INTERTIME
|INC3|4
|ST3|VPTR
VRET|JMP|*
FINISH|HLT|
VPTR|CON|INPUT
VEND|CON|INPUT
INFLOOR|CON|0
OUTFLOOR|CON|0
GIVEUPTIME|CON|0
INTERTIME|CON|0
TEMP|CON|0
BEGIN|ENT4|2
|ENT5|0
|JMP|CYCLE
POOLMAX|NOP|POOL
|END|BEGIN
'''
    rows += [tuple(line.split('|')) for line in aux.strip().splitlines()]
    a=Assembly(rows,b);a.line_addresses={n:a.locations[len(prefix)+i] for i,(n,row) in enumerate(numbered)}
    a.audit_rows=rows
    if original_pool:
        s={k:w.value(b) for k,w in a.symbols.items()}
        a.memory[s['POOLMAX']]=number(s['POOL'],b)
        for n in ['103','105']:
            addr=a.line_addresses[n];w=a.memory[addr]
            a.memory[addr]=Word(w.sign,w.digits[:3]+(5,w.digits[4]))
    return a


if __name__=='__main__':
    import json
    out=Path(__file__).resolve().parent/'results'
    for b in [64,100]:
        a=assemble(b)
        (out/f'book-{b}.json').write_text(json.dumps({'symbols':{k:w.value(b) for k,w in a.symbols.items()},'line_addresses':a.line_addresses,'words':{k:[w.sign,*w.digits] for k,w in a.memory.items()}},indent=2)+'\n')
    (out/'book-complete.mixal').write_text('\n'.join(f'{l:12} {o:6} {x}' for l,o,x in a.audit_rows)+'\n')
    print('Complete elevator assembled; code high address',max(a.memory),'pool starts at900; input at3000')

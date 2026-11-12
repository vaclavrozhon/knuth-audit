"""General invariant proofs are in notes/coroutines.md; this is finite evidence."""
from pathlib import Path
import itertools
import json
import random
import sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parents[1]))
from mix_machine import Machine, Word, number, instruction
from mix_io import IOMachine
from mixal import Assembly, CHAR_CODE, CHARACTERS
from coroutine_programs import decoder, ENCODER, THREE_LINK

checks=0
counts={}


def check(ok,label):
    global checks
    if not ok: raise AssertionError(label)
    checks+=1


def card_words(text):
    text=text.ljust(80)
    assert len(text)==80
    return tuple(Word(1,tuple(CHAR_CODE[c] for c in text[k:k+5])) for k in range(0,80,5))


def reference_decode(text):
    chars=iter(text.replace(' ','')); out=[]
    for c in chars:
        if c.isascii() and c.isdigit():
            f=int(c)+1; c=next(chars)
        else: f=1
        if c=='.': return ''.join(out)+'.'
        out.extend(c*f)
    raise ValueError('unterminated input')


def grouped_cards(text):
    groups=[text[k:k+3].ljust(5) for k in range(0,len(text),3)]
    return [''.join(groups[k:k+16]).ljust(80) for k in range(0,len(groups),16)]


def read_output(m):
    return [''.join(CHARACTERS[d] for w in card for d in w.digits) for card in m.outputs[17]]


def execute(rows,text,b=64,delay=0,ci=0,monitor=False):
    a=Assembly(rows,b);m=IOMachine(b,delay=delay);a.load(m)
    m.comparison=ci
    m.reg[2]=number(-27,b);m.reg[3]=number(29,b)
    for k in range(0,len(text),80):m.inputs[16].append(card_words(text[k:k+80]))
    in_entry=out_entry=None
    while not m.halted:
        if m.steps>=300000:raise RuntimeError('finite execution limit')
        if monitor and m.pc==a.symbols['IN'].value(b):
            if out_entry is not None:
                check([m.reg[r] for r in (0,7,5,6)]==out_entry,'OUT preserves IN state')
            in_entry=m.reg[4]
        if monitor and m.pc==a.symbols['OUT'].value(b):
            check(m.reg[4]==in_entry,'IN preserves OUT pointer')
            out_entry=[m.reg[r] for r in (0,7,5,6)]
        m.step()
    m.finish_io()
    return m,a,read_output(m)


sample='A2B5E3426FG0ZYW3210PQ89R.'
sample_expected='ABB BEE EEE E44 446 66F GZY W22 220 0PQ 999 999 999 R.'.replace(' ','')
check(reference_decode(sample)==sample_expected,'printed example(2)->(3)')
inputs=[sample,'.','1.','0.A.','A.','9A.','9 9 .',' '*80+'A.',
        'A'*79+'9'+'B.','A'*80+'.','9A'*20+'.','0A'*81+'.',
        'A'*47+'.','A'*48+'.','A'*49+'.','A'*95+'.','A'*96+'.']
inputs += [c+'.' for c in CHARACTERS[1:] if c not in '0123456789.']
inputs += [str(d)+c+'.' for d in range(10) for c in 'AZ09.']
for b,delay in [(64,0),(100,73)]:
    for text in inputs:
        wanted=grouped_cards(reference_decode(text))
        m,a,out=execute(decoder(),text,b,delay,monitor=True)
        check(out==wanted,('original decoder',b,text))
        check([m.reg[2].value(b),m.reg[3].value(b)]==[-27,29],'decoder untouched I2,I3')
        counts['original_decoder']=counts.get('original_decoder',0)+1
        # Corrected 2006 answer3 optimization adds both missing comparisons.
        m,a,out=execute(decoder('corrected_comparison'),text,b,delay,ci=0)
        check(out==wanted,('2006 corrected answer3',b,text))
        counts['corrected_comparison']=counts.get('corrected_comparison',0)+1

known_examples=[]
for text,ci in [('A.',0),('0.A.',-1)]:
    m,a,out=execute(decoder('omit_comparisons'),text,ci=ci)
    obtained=''.join(out).replace(' ','')
    check(obtained!=reference_decode(text),'known comparison counterexample')
    known_examples.append({'input':text,'initial_CI':ci,'actual':obtained,
                           'expected':reference_decode(text)})
for text in ('AB.','2A.','0A.'):
    m,a,out=execute(decoder('start_in'),text)
    check(out==grouped_cards(reference_decode(text)[1:]),'answer2 first character lost')
    counts['start_in']=counts.get('start_in',0)+1


def reference_encode(text):
    out=[]
    for c,g in itertools.groupby(text.split('.')[0]):
        n=len(list(g));q,r=divmod(n,10)
        out += ['9'+c]*q
        if r:
            out.append(c if r==1 and c not in '0123456789' else str(r-1)+c)
    return ''.join(out)+'.'


def optimum_length(text):
    """Dynamic program over every permissible token; independent of the greedy code."""
    text=text.split('.')[0];n=len(text);dp=[10**9]*(n+1);dp[n]=1
    for i in range(n-1,-1,-1):
        if text[i] not in '0123456789':dp[i]=1+dp[i+1]
        for k in range(1,min(10,n-i)+1):
            if text[i+k-1]!=text[i]:break
            dp[i]=min(dp[i],2+dp[i+k])
    return dp[0]


plain=[''.join(p)+'.' for n in range(5) for p in itertools.product('AB09',repeat=n)]
plain += [c*n+'.' for c in 'A09' for n in range(1,42)]
plain += [sample_expected, 'AB'*39+'A.', 'AB'*40+'.', 'AB'*41+'.',
          'AB'*79+'A.', 'A'*1000+'.','0'*1000+'.','9'*1000+'.',
          'A'*10+'0'*11+'B'*12+'9'*21+'.']
rng=random.Random(141142)
plain += [''.join(rng.choice('AB09')*rng.randrange(1,25) for _ in range(20))+'.' for _ in range(30)]
for b,delay in [(64,0),(100,41)]:
    for text in plain:
        # Actual input uses the three-character card layout of(3).
        input_text=''.join(grouped_cards(text))
        m,a,out=execute(ENCODER,input_text,b,delay)
        obtained=''.join(out).rstrip(' ')
        wanted=reference_encode(text)
        check(obtained==wanted,('inverse encoder',b,text,obtained,wanted))
        check(reference_decode(obtained)==text,'inverse roundtrip')
        check(len(obtained)==optimum_length(text),'minimum number of characters')
        check(len(out)==(len(obtained)+79)//80,'no extra blank final card')
        counts['inverse_encoder']=counts.get('inverse_encoder',0)+1

# Answer6: every directed transfer updates exactly the leaving continuation.
a=Assembly(THREE_LINK,64)
for trace in [('A','B','C','A','C','B','A'),('C','A','B','C','B','A','C')]:
    m=Machine();a.load(m)
    saved={'A':100,'B':200,'C':300}
    current=trace[0]
    for step,target in enumerate(trace[1:]):
        call=500+10*step
        m.mem[call]=instruction(64,'JMP',a.symbols[current+target].value(64))
        m.run(call,stop=saved[target],limit=5)
        saved[current]=call+1
        for name in 'ABC':
            word=m.mem[a.symbols[name+'X'].value(64)]
            check(word.digits[0]*64+word.digits[1]==saved[name],'three-coroutine continuation')
        current=target
        counts['three_link_transfers']=counts.get('three_link_transfers',0)+1

result={'checks':checks,'cases':counts,'known_comparison_counterexamples':known_examples,
        'sample_shortest_encoding':reference_encode(sample_expected),
        'scope':'Original program incl. asynchronous I/O and contracts; 2006 comparison correction; first-character loss; independently written minimum-length inverse encoder; three-coroutine linkage.',
        'limits':'Finite checks supplement general proofs. Historical IBM/CDC instruction semantics are checked separately against primary manuals.'}
(ROOT/'results'/'coroutines.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

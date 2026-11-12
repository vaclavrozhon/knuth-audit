"""Rounded harmonic sums by term, value groups, layers, and original MIX."""
from pathlib import Path
from collections import Counter
import json,math
from mixal_rounded_harmonic import program,rounded_sum,layer_sum
from mixal import Assembly,CHARACTERS
from mix_io import IOMachine

ROOT=Path(__file__).resolve().parent
checks=0

def check(ok,label):
    global checks
    if not ok:raise AssertionError(label)
    checks+=1


for M in range(1,501):
    direct=sum((2*M+m)//(2*m) for m in range(1,2*M+1))
    check(direct==rounded_sum(M)[0]==layer_sum(M)[0],('three scalar sums',M))
    for r in range(1,M+1):
        lo=2*M//(2*r+1)+1;hi=2*M//(2*r-1)
        if lo<=hi:
            check((2*M+lo)//(2*lo)==r and (2*M+hi)//(2*hi)==r,('group endpoints',M,r))
            check(lo==1 or (2*M+lo-1)//(2*(lo-1))>r,('previous group',M,r))
            check((2*M+hi+1)//(2*(hi+1))<r,('next group',M,r))

published=[39,616,8449,107509,1305363,15356262,176588276,1996140690,22263991779,245665766353]
values=[]
for n,answer in enumerate(published,1):
    M=10**n;a,g=rounded_sum(M);b,l=layer_sum(M)
    check(a==b==answer,('published number',n,a,b))
    if n<=5:
        check(a==sum((2*M+m)//(2*m) for m in range(1,2*M+1)),('direct term sum',n))
    asym=n*math.log(10)+2*0.5772156649015328606-1+2*math.log(2)
    values.append({'n':n,'scaled_sum':a,'groups_after_first':g,'layer_blocks':l,'asymptotic':asym,'error':a/M-asym})

# Number of nonempty rounded-value intervals, independently of the group walk.
groups=[]
for n in range(2,6):
    M=10**n
    g=sum(2*M//(2*r-1)>2*M//(2*r+1) for r in range(1,M+1))-1
    groups.append(g)
check(groups==[18,61,198,630],'independent group counts')
expected=''
for n in range(2,6):
    M=10**n;s=published[n-1]
    expected+=(f'{s//M:04}.'+f'{s%M:0{n}}').ljust(15)
expected=expected.ljust(120)

rows=program();profiles=[]
for b in range(64,101):
    a=Assembly(rows,b);m=IOMachine(b,500);a.load(m);m.pc=a.start
    counts=Counter();times=Counter()
    while not m.halted:
        pc=m.pc;t=m.time;m.step();counts[pc]+=1;times[pc]+=m.time-t
    cpu=m.time;m.finish_io()
    lines=[''.join(CHARACTERS[d] for w in block for d in w.digits) for block in m.outputs[18]]
    check(lines==[expected],('MIX full output',b))
    check(cpu==3+4*(26+29+26)+72*sum(groups)+2==65633,('instruction time',b,cpu))
    check(not m.overflow,('no overflow',b))
    check(m.steps==21877,('instruction count',b))
    if b==64:
        for row,pc in zip(rows,a.locations):
            if row[1] not in ('ORIG','END'):
                profiles.append({'address':pc,'row':row,'executions':counts[pc],'time':times[pc]})

check(abs(values[-1]['asymptotic']-24.566576621)<5e-10,'printed S10 approximation')
result={'checks':checks,'radices':list(range(64,101)),'io_delay':500,
        'values':values,'groups_n2_to5':groups,'cpu_time_including_out_and_hlt':65633,
        'time_before_out':65631,'printed_time':65595,'instructions':21877,
        'output':expected,'profile_radix64':profiles,
        'scope':'Complete MIX output and timing; exact scalar sums through n10 and general proofs in notes. Published asymptotic typo already in1999 errata.'}
(ROOT/'results/rounded-harmonic.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('profile_radix64','radices')},indent=2))

"""Full MIX block interchange, signed data, runtime lengths, and closed time sums."""
from pathlib import Path
from itertools import product
from math import gcd
import json,random,time
from mixal import Assembly
from mix_machine import Machine,number
from mixal_block_interchange import program
ROOT=Path(__file__).resolve().parent
checks=0;started=time.monotonic();runs=[]
def check(x,info=None):
    global checks
    assert x,info
    checks+=1

def run(l,m,n,method,b=64):
    size=l+m+n;check(size<=3000)
    a=Assembly(program(method,l,m,n),b);machine=Machine(b);a.load(machine)
    data=[number((-1 if i%2 else 1)*(i+1),b) for i in range(size)]
    if size:data[size//2]=number(0,b,sign_zero=-1)
    machine.mem[1000:1000+size]=data
    machine.overflow=True;machine.comparison=-1
    for r in [0,4,5,6,7]:machine.reg[r]=number(-17-r,b)
    before=list(machine.mem);machine.run(a.start,limit=300000)
    expected=data[l+m:]+data[l:l+m]+data[:l]
    check(machine.mem[1000:1000+size]==expected,(method,l,m,n,b))
    local_names=['LLEN','MLEN','NLEN','TOTAL','VIRT','SHIFT','U','V','START','SUCC','CUT','BACK']
    if method=='reversals':local_names+=['RBACK']
    allowed={a.symbols[x].value(b) for x in local_names}|set(range(1000,1000+size))
    check(all(before[i]==machine.mem[i] for i in range(4000) if i not in allowed))
    check(all(machine.reg[r].value(b)==-17-r for r in [4,5,6]))
    check(machine.overflow)
    if method=='cycles':
        u,v=l+m,m+n;g=0
        while v:u,v=v,u%v;g+=1
        expected_time=38+25*g+24*l+29*m+22*n+gcd(l+m,m+n) if size else 20
    else:
        exchanges=size//2+l//2+m//2+n//2
        expected_time=65+14*exchanges
    # Wrapper:3 parameter assignments, one call, and one final HLT, each1u.
    core=machine.time-5;check(core==expected_time,(method,l,m,n,b,core,expected_time))
    rec=dict(method=method,l=l,m=m,n=n,radix=b,core_time=core,instructions=machine.steps)
    runs.append(rec);return rec

for l,m,n in product(range(9),repeat=3):
    for method in ['cycles','reversals']:run(l,m,n,method)
for b in range(64,101):
    for method in ['cycles','reversals']:run(3,4,5,method,b)
for l,m,n in [(0,3000,0),(250,1300,1450),(1500,0,1500),(0,0,3000),(3000,0,0)]:
    for b in (64,100):
        for method in ['cycles','reversals']:run(l,m,n,method,b)
result=dict(checks=checks,runs=len(runs),elapsed_seconds=time.monotonic()-started,details=runs)
(ROOT/'results/block-interchange.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='details'}))

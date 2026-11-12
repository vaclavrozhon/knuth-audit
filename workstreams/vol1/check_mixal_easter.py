"""Independent absolute-day, reduced-period histogram, and MIX Easter checks."""
from collections import Counter
from pathlib import Path
import json,math,random,time
from mixal_easter import algorithm,reingold,fixed_march0,program,search_program
from mixal import Assembly,CHARACTERS
from mix_io import IOMachine
from mix_machine import number

ROOT=Path(__file__).resolve().parent
checks=0

def check(ok,label):
    global checks
    if not ok:raise AssertionError(label)
    checks+=1


def line(y):
    n=reingold(y)
    return (' '*5+f'{n if n<=31 else n-31:02}   '
            +('MARCH' if n<=31 else 'APRIL')+',    '+f'{y:05}').ljust(120)


def decode(m):
    return [''.join(CHARACTERS[d] for w in block for d in w.digits) for block in m.outputs[18]]


def one_year(y,b):
    rows=program();start=rows.index(('BEGIN','ENTX','1950'))
    rows=rows[:start]+[('BEGIN','LDX','INPUT'),('','JMP','EASTER'),
                       ('','HLT',''),('INPUT','CON',str(y)),('','END','BEGIN')]
    a=Assembly(rows,b);m=IOMachine(b,43);a.load(m)
    m.run(a.start,limit=10000);m.finish_io()
    check(decode(m)==[line(y)],('MIX subroutine',y,b,decode(m),line(y)))

start=time.monotonic()
rng=random.Random(13214)
# Every epact/exception branch represented, plus century and range boundaries.
reps={}
for y in range(1583,100000):
    g=y%19+1;c=y//100+1;e=(11*g+27+(8*c+5)//25-3*c//4)%30
    reps.setdefault((e,g>11),y)
check(len(reps)==60,'all epact/golden-number branch combinations')
years=sorted(set(reps.values())|{1583,1599,1600,1699,1700,1899,1900,1999,2000,
                               2099,2100,99998,99999,10317,14250}|
             set(rng.sample(range(1583,100000),50)))
for b in range(64,101):
    for y in years:one_year(y,b)
    B=b**5
    for num,den,vmax in [(1,100,99999),(3,4,1060),(8,25,1060),(1,4,99999)]:
        check(den*vmax<B,('reciprocal lemma bound',b,num,den,vmax))
        for v in [0,1,den-1,den,vmax]:
            check((v*(num*B//den+1))//B==num*v//den,('reciprocal sample',b,num,den,v))

for b in (64,100):
    for delay in (0,1200):
        a=Assembly(program(),b);m=IOMachine(b,delay);a.load(m)
        m.run(a.start,limit=200000);m.finish_io()
        check(decode(m)==[line(y) for y in range(1950,2001)],('whole driver',b,delay))

first=next(y for y in range(1583,100000) if algorithm(y)!=algorithm(y,True))
check(first==10317,'first signed-remainder failure')
check(algorithm(first)==25 and algorithm(first,True)==53,'first dates')
check(algorithm(14250)==45 and algorithm(14250,True)==73,'14250 example')
near=[10108+19*k for k in range(11)]
weekday=[]
for y in near:
    c=y//100+1;x=3*c//4-12;d=5*y//4-x-10
    weekday.append((d+50)%7)
    check(algorithm(y)==algorithm(y,True),('near miss',y))
check(weekday==[4,6,2,5,1,2,5,1,4,6,2],'near-miss Sunday residues')
search_runs=[]
for b in (64,100):
    a=Assembly(search_program(),b);m=IOMachine(b,1200);a.load(m)
    m.run(a.start,limit=1500000);m.finish_io()
    check(m.mem[a.symbols['YEARCOUNT'].value(b)].value(b)==first,('MIX first failure',b))
    check(decode(m)==[str(first).ljust(120)],('MIX search output',b,decode(m)))
    search_runs.append({'radix':b,'steps':m.steps,'time_including_io':m.time})

period=5700000
hist=Counter()
for y in range(1583,1583+period):
    n=algorithm(y)
    check(n==reingold(y),('absolute-day model',y))
    check(22<=n<=56,('date range',y))
    hist[n]+=1
check(sum(hist.values())==period and len(hist)==35,'full-period histogram size')
witnesses=[]
for prime in (2,3,5,19):
    q=period//prime;y=1583
    check(algorithm(y)!=algorithm(y+q),('minimal-period witness',prime))
    witnesses.append({'prime':prime,'candidate_period':q,'year':y,
                      'date1':algorithm(y),'date2':algorithm(y+q)})
# Independent CRT factorization of all years, giving a proof of divisibility.
small=Counter()
for t in range(4):
    for within_century in range(100):
        d=125*t-3*(t+1)//4+5*within_century//4+2
        for g in range(1,20):
            for raw_epact in range(30):
                e=raw_epact+int(raw_epact==24 or raw_epact==25 and g>11)
                moon=21+(23-e)%30
                sunday=moon+7-(d+moon)%7
                small[sunday]+=1
check(hist==Counter({n:25*v for n,v in small.items()}),'CRT factorization of histogram')
check(hist[50]==220400 and hist[22]==27550 and hist[56]==42000,'published frequencies')
check(max(hist,key=hist.get)==50 and sorted(hist,key=hist.get)[:2]==[22,56],'published extrema')
check(all(v%25==0 for v in hist.values()),'frequency divisibility')
result={'checks':checks,'subroutine_runs':len(years)*37,'driver_runs':4,
        'years_sampled_all_radices':years,'radices':list(range(64,101)),
        'first_wrong_year':first,'near_misses':near,'near_miss_weekday_residues':weekday,
        'search_runs':search_runs,'period':period,'period_witnesses':witnesses,
        'full_period':{'start':1583,'end_inclusive':1583+period-1,'years':period},
        'histogram_march_day':dict(sorted(hist.items())),
        'reduced_histogram_size':sum(small.values()),'elapsed_seconds':time.monotonic()-start,
        'scope':'General proofs in notes; finite checks are corroboration, including every year of one full Easter period.'}
(ROOT/'results/mixal-easter.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))

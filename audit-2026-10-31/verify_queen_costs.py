"""Permutation oracle, symmetry checks, exact costs and original DLX5."""
from pathlib import Path
from itertools import permutations
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal,localcontext
from fractions import Fraction
import json,subprocess,math,time
ROOT=Path(__file__).parent;OUT=ROOT/'results/queen_costs';OUT.mkdir(exist_ok=True)

def orbit(q):
    n=len(q);cells=list(enumerate(x-1 for x in q));out=set()
    for reflect in range(2):
        cc=[(r,n-1-c if reflect else c) for r,c in cells]
        for _ in range(4):
            v=[0]*n
            for r,c in cc:v[r]=c+1
            out.add(tuple(v));cc=[(c,n-1-r) for r,c in cc]
    return out

def valid(q):
    n=len(q)
    return sorted(q)==list(range(1,n+1)) and len({i+x for i,x in enumerate(q)})==n and len({i-x for i,x in enumerate(q)})==n

def norms(q):
    n=len(q);return [(2*i+1-n)**2+(2*x-1-n)**2 for i,x in enumerate(q)]

def small():
    reports=[]
    for n in range(4,10):
        data=json.loads(subprocess.check_output(['/tmp/knuth-queen-costs',str(n)],text=True))
        (OUT/f'n{n}.json').write_text(json.dumps(data,indent=2)+'\n')
        qs=[q for q in permutations(range(1,n+1)) if valid(q)]
        assert len(qs)==data['solutions']
        values={q:norms(q) for q in qs}
        functions={
          'distance_min':(lambda a:sum(math.sqrt(v)/2 for v in a),min),
          'distance_max':(lambda a:sum(math.sqrt(v)/2 for v in a),max),
          'floor_min':(lambda a:sum(math.isqrt(v)//2 for v in a),min),
          'norm_squared_min':(lambda a:sum(v*v for v in a),min),
          'norm_squared_max':(lambda a:sum(v*v for v in a),max),
          'product_norm_min':(math.prod,min),'product_norm_max':(math.prod,max),
          'power20_min':(lambda a:sum(v**10 for v in a),min),
          'power21_min':(lambda a:sum(v**10.5 for v in a),min),
          'ultimate':(lambda a:tuple(sorted(a,reverse=True)),min)}
        for name,(f,ext) in functions.items():
            vv={q:f(v) for q,v in values.items()};best=ext(vv.values())
            if name in ('distance_min','distance_max','power21_min'):
                models={q for q,v in vv.items() if abs(v-best)<1e-10*max(1,abs(best))}
            else:models={q for q,v in vv.items() if v==best}
            assert models==set(map(tuple,data[name]['models'])),(n,name)
        reports.append(dict(n=n,solutions=len(qs),criteria=10))
    (OUT/'small-verified.json').write_text(json.dumps(reports,indent=2)+'\n');print('All permutation oracles n=4,...,9 agree.',flush=True)

def big():
    d=json.loads((OUT/'n16.json').read_text());assert d['solutions']==14772512
    report={}
    for name,v in d.items():
        if not isinstance(v,dict):continue
        models=set(map(tuple,v['models']));assert len(models)==len(v['models'])
        assert all(valid(q) for q in models)
        assert set().union(*(orbit(q) for q in models))==models
        reps={min(orbit(q)) for q in models}
        report[name]=dict(count=len(models),classes=len(reps),orbit_histogram=dict(Counter(len(orbit(q)) for q in reps)),representatives=sorted(reps))
    assert set(map(tuple,d['distance_min']['models']))==set(map(tuple,d['product_norm_min']['models']))
    assert set(map(tuple,d['distance_max']['models']))==set(map(tuple,d['product_norm_max']['models']))
    assert d['floor_min']['value']==84 and len(d['floor_min']['models'])==96
    assert {sum(math.isqrt(w)//2 for w in norms(q)) for q in d['distance_min']['models']}=={86}
    assert d['norm_squared_min']['value']//4==127760 and d['norm_squared_max']['value']//4==187760
    assert set(map(tuple,d['power21_min']['models']))==set(map(tuple,d['ultimate']['models']))
    printed=[8,11,4,7,5,12,1,16,14,2,15,10,3,13,6,9]
    assert printed in d['power20_min']['models']
    costs=[]
    for q in [printed,d['ultimate']['models'][0]]:
        w=norms(q);exact=sum(Fraction(v,4)**10 for v in w)
        costs.append(dict(permutation=q,norm_histogram=dict(Counter(w)),exact=str(exact),decimal=float(exact),times1024=str(exact*1024)))
    report['printed_N20_costs']=costs
    report['N2_constant']=16*(16*16-1)//6
    (OUT/'verified-summary.json').write_text(json.dumps(report,indent=2)+'\n')
    print('All n16 models, orbits and exact polynomial/product costs checked.',flush=True)

def weighted(name,k):
    n=16;ww={};scale=2**32
    with localcontext() as ctx:
        ctx.prec=90
        for r in range(n):
            for c in range(n):
                w=(2*r+1-n)**2+(2*c+1-n)**2
                if name.startswith('distance'):v=math.isqrt(w<<62)
                elif name.startswith('product'):v=int((Decimal(w)/2).ln()*Decimal(scale)/2)
                elif name.startswith('quartic'):v=w*w//4
                else:v=math.isqrt(w)//2
                ww[r,c]=v
    maximum=max(ww.values())
    if name.endswith('max'):ww={p:maximum-v for p,v in ww.items()}
    header=' '.join([f'r{i}' for i in range(n)]+[f'c{i}' for i in range(n)])+' | '+' '.join([f'a{i}' for i in range(2*n-1)]+[f'b{i}' for i in range(2*n-1)])
    text=header+'\n'+'\n'.join(f'r{r} c{c} a{r+c} b{r-c+n-1} |{ww[r,c]}' for r in range(n) for c in range(n))+'\n'
    (OUT/f'{name}.xcc').write_text(text)
    start=time.monotonic()
    p=subprocess.run(['/tmp/knuth-dlx5',f'k{k}','v17','m1','d0'],input=text,text=True,capture_output=True,timeout=900)
    (OUT/f'{name}.out').write_text(p.stdout);(OUT/f'{name}.log').write_text(p.stderr)
    result=dict(name=name,k=k,seconds=time.monotonic()-start,returncode=p.returncode,complement_constant=maximum if name.endswith('max') else None,weights=ww)
    result['weights']={f'{r},{c}':v for (r,c),v in ww.items()}
    (OUT/f'{name}.json').write_text(json.dumps(result,indent=2)+'\n')
    assert 'The optimum cost' in p.stderr and 'TIMEOUT' not in p.stderr
    print(name,round(result['seconds'],2),'seconds',p.stderr[-400:],flush=True)
    return result

def original():
    with ThreadPoolExecutor(max_workers=2) as ex:
        tasks=[('distance_min',9),('distance_max',9),('quartic_min',17),('quartic_max',9),('floor_min',97),('product_min',9),('product_max',9)]
        list(ex.map(lambda t:weighted(*t),tasks))

if __name__=='__main__':
    small();big();original()

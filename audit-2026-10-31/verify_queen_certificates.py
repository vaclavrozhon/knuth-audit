"""Check saved DLX models, figure coordinates, and the exponent certificate."""
from pathlib import Path
import re,json,math
from verify_queen_costs import valid,norms
ROOT=Path(__file__).parent;OUT=ROOT/'results/queen_costs'

def original_outputs():
    native=json.loads((OUT/'n16.json').read_text());report={}
    for name,key in [('distance_min','distance_min'),('distance_max','distance_max'),('quartic_min','norm_squared_min'),('quartic_max','norm_squared_max'),('floor_min','floor_min'),('product_min','product_norm_min'),('product_max','product_norm_max')]:
        ww=json.loads((OUT/(name+'.json')).read_text())['weights']
        blocks=re.split(r'^\d+: \(total cost \$(\d+)\)\n',(OUT/(name+'.out')).read_text(),flags=re.M);bycost={}
        for cost,body in zip(blocks[1::2],blocks[2::2]):
            rows=body.strip().splitlines();q=[0]*16;assert len(rows)==16
            for row in rows:
                rr=int(re.search(r'\br(\d+)\b',row)[1]);cc=int(re.search(r'\bc(\d+)\b',row)[1]);q[rr]=cc+1
            assert valid(q);cost=int(cost);assert sum(ww[f'{i},{x-1}'] for i,x in enumerate(q))==cost
            bycost.setdefault(cost,set()).add(tuple(q))
        best=min(bycost);expected=set(map(tuple,native[key]['models']));assert bycost[best]==expected
        for q in expected:
            if name.startswith('product'):assert math.prod(norms(q))==int(native[key]['value'])
            if name.startswith('quartic'):assert sum(w*w for w in norms(q))==native[key]['value']
        second=sorted(bycost)[1]
        matches=re.findall(r'\$(\d+)(?: \(repeated (\d+) times\))?',(OUT/(name+'.log')).read_text().split('The optimum cost')[-1])
        assert int(matches[0][0])==best and int(matches[1][0])==second
        report[name]=dict(best=best,next=second,gap=second-best,models=len(expected),improvements=sum(map(len,bycost.values())))
        if name.startswith(('distance','product')):assert second-best>16
    (OUT/'dlx5-verified.json').write_text(json.dumps(report,indent=2)+'\n')
    models=[]
    for block in re.split(r'^\d+:\n',(OUT/'ultimate.out').read_text(),flags=re.M)[1:]:
        q=[0]*16
        for line in block.strip().splitlines():
            a=re.search(r'\br(\d+)\b',line);b=re.search(r'\bc(\d+)\b',line)
            if a and b:q[int(a[1])]=int(b[1])+1
        assert valid(q);models.append(q)
    assert set(map(tuple,models))==set(map(tuple,native['ultimate']['models']))
    (OUT/'ultimate-verified.json').write_text(json.dumps(dict(models=models,all_match=True),indent=2)+'\n')

def figures():
    data=json.loads((OUT/'n16.json').read_text());report={}
    for page,limit,groups,keys in [(112,1000,3,['distance_min','distance_max','distance_max']),(152,1000,1,['ultimate']),(477,240,3,['norm_squared_min','norm_squared_min','norm_squared_max'])]:
        a=re.findall(r'<word xMin="(.*?)" yMin="(.*?)" xMax="(.*?)" yMax="(.*?)">(.*?)</word>',(OUT/f'page{page}-bbox.html').read_text())
        coords=sorted((float(w[0]),float(w[1])) for w in a if w[4]=='\x05' and float(w[1])<limit)
        assert len(coords)==16*groups;records=[]
        for k in range(groups):
            group=coords[16*k:16*(k+1)];xs=sorted(x for x,y in group);ys=sorted(y for x,y in group);q=[0]*16
            for x,y in group:q[ys.index(y)]=xs.index(x)+1
            assert valid(q) and q in data[keys[k]]['models'];records.append(q)
        report[str(page)]=records
    (OUT/'figures-verified.json').write_text(json.dumps(report,indent=2)+'\n')

def endpoints():
    d=json.loads((OUT/'n16.json').read_text());u=d['ultimate']['models'][0];a=d['power20_min']['models'][0];b=d['distance_min']['models'][0];res=[];C=2**56
    for n in range(1,21):
        if n==2:continue
        q=b if n==1 else a;ww=norms(q);uu=norms(u);v=max(ww+uu)
        floor=lambda w:math.isqrt((C*C*w**n)//v**n)
        delta=sum(map(floor,uu))-sum(map(floor,ww));assert delta>16
        res.append(dict(N=n,witness=q,normalized_scale=C,reference_norm=v,scaled_ultimate_minus_witness=delta))
    assert 16*113**80<117**80
    proof=json.loads((OUT/'power-threshold.json').read_text())
    assert proof['half_board_solutions']*2==14772512 and proof['classes']==1846955 and proof['ultimate_classes']==8
    assert [x['N'] for x in proof['margins']]==list(range(21,160))
    assert all(x['minimum_scaled_margin']>16 and x['comparisons']==1846947 for x in proof['margins'])
    out=dict(small_exponents=res,constant_N2=680,large_bound=dict(N0=160,numerator=113,denominator=117,coefficient=16,exact_inequality=True,ratio=float(16*113**80/117**80)))
    (OUT/'power-threshold-endpoints.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    original_outputs();figures();endpoints();print('All saved queen certificates and extracted figures agree.')

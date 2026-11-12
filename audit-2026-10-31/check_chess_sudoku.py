"""Read numerical clues at exact PDF grid coordinates; verify via SAT and MCC."""
from pathlib import Path
from collections import Counter
import json,re,subprocess,xml.etree.ElementTree as ET
from pysat.card import CardEnc,EncType
from pysat.solvers import Solver
ROOT=Path(__file__).parent;OUT=ROOT/'results/chess_sudoku';OUT.mkdir(exist_ok=True)

def words(page):
    path=OUT/f'page{page}-bbox.html'
    if not path.exists():subprocess.run(['pdftotext','-f',str(page+20),'-l',str(page+20),'-bbox',str(ROOT.parent/'books/taocp-vol4b-ed1-print2-2022.pdf'),str(path)],check=True)
    s=re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]',' ',path.read_text());root=ET.fromstring(s)
    return [dict(text=w.text,x=(float(w.get('xMin'))+float(w.get('xMax')))/2,y=float(w.get('yMin')))
            for w in root.iter() if w.tag.endswith('word') and (w.text or '').isdigit()]

def extract(ws,bases,y0,step):
    grids=[[] for x in bases]
    for w in ws:
        r=round((w['y']-y0)/step)
        if not 0<=r<9 or abs(w['y']-y0-r*step)>.01:continue
        for z,x in enumerate(bases):
            c=round((w['x']-x)/step)
            if 0<=c<9 and abs(w['x']-x-c*step)<.01:grids[z].append([r,c,int(w['text'])])
    return [sorted(g) for g in grids]

def adjacent(v,w,piece):
    r,c=divmod(v,9);s,t=divmod(w,9);a,b=abs(r-s),abs(c-t)
    return a*b==2 if piece=='knight' else a==b and a>0

def verify(model,clues,piece):
    assert len(model)==27
    assert all(sum(v//9==r for v in model)==3 for r in range(9))
    assert all(sum(v%9==c for v in model)==3 for c in range(9))
    assert all(sum((v//9//3)*3+(v%9//3)==b for v in model)==3 for b in range(9))
    for r,c,label in clues:
        v=9*r+c;assert v in model and sum(adjacent(v,w,piece) for w in model)==label

def sat(clues,piece):
    cnf=[];top=81
    def equal(vs,bound):
        nonlocal top
        q=CardEnc.equals(lits=[v+1 for v in vs],bound=bound,top_id=top,encoding=EncType.seqcounter);cnf.extend(q.clauses);top=max(top,q.nv)
    for r in range(9):equal([9*r+c for c in range(9)],3)
    for c in range(9):equal([9*r+c for r in range(9)],3)
    for r in [0,3,6]:
        for c in [0,3,6]:equal([9*i+j for i in range(r,r+3) for j in range(c,c+3)],3)
    for r,c,label in clues:
        v=9*r+c;cnf.append([v+1]);equal([w for w in range(81) if adjacent(v,w,piece)],label)
    models=[]
    with Solver(name='g4',bootstrap_with=cnf) as solver:
        while len(models)<2 and solver.solve():
            model={i-1 for i in solver.get_model() if 1<=i<=81};verify(model,clues,piece);models.append(sorted(model))
            solver.add_clause([-(v+1) if v in model else v+1 for v in range(81)])
    return models

def mcc(clues,piece,name):
    fixed={9*r+c for r,c,_ in clues};quotas={};scopes={}
    for r in range(9):scopes[f'r{r}']={9*r+c for c in range(9)}
    for c in range(9):scopes[f'c{c}']={9*r+c for r in range(9)}
    for b in range(9):scopes[f'b{b}']={9*r+c for r in range(9) for c in range(9) if 3*(r//3)+c//3==b}
    for key,scope in scopes.items():quotas[key]=3-len(scope&fixed)
    for z,(r,c,label) in enumerate(clues):
        key=f'p{z}';scopes[key]={w for w in range(81) if adjacent(9*r+c,w,piece)};quotas[key]=label-len(scopes[key]&fixed)
    assert min(quotas.values())>=0
    forbidden=fixed|set().union(*(scopes[key] for key,q in quotas.items() if q==0))
    options={v:[key for key,scope in scopes.items() if v in scope] for v in range(81) if v not in forbidden}
    text=' '.join(f'{q}|{key}' for key,q in quotas.items() if q)+'\n'+'\n'.join(' '.join(items) for items in options.values())+'\n'
    base=OUT/name;base.with_suffix('.mcc').write_text(text)
    p=subprocess.run(['/tmp/knuth-dlx3','v1','d0','m1','t2'],input=text,text=True,capture_output=True,timeout=120)
    base.with_suffix('.log').write_text(p.stderr);base.with_suffix('.out').write_text(p.stdout)
    match=re.search(r'Altogether (\d+) solution',p.stderr);assert match,p.stderr
    models=[];model=None
    for line in p.stdout.splitlines()+['END']:
        if re.match(r'^\d+:$',line) or line=='END':
            if model is not None:verify(model,clues,piece);models.append(sorted(model))
            model=set(fixed)
        elif line.strip():
            parts=line.split(' (')[0].split();r=int(next(x[1:] for x in parts if x.startswith('r')));c=int(next(x[1:] for x in parts if x.startswith('c')));model.add(9*r+c)
    assert len(models)==int(match[1]);return models

def main():
    w146=words(146);bases=[123.149461,219.149461,319.769461,415.769461]
    first=extract(w146,bases,224.306157,9.5534);second=extract(w146,bases,343.046157,9.5534)
    assert list(map(len,first))==[27,8,27,9];assert list(map(len,second))==[5,4,3,3]
    w466=words(466);x0=[]
    for lo,hi in [(132,135),(222,226),(318,322),(408,412)]:x0.append(next(w['x'] for w in w466 if lo<w['x']<hi and 580<w['y']<610))
    step=8.9584;y0=next(w['y'] for w in w466 if 132<w['x']<135 and 580<w['y']<590)-step
    last=extract(w466,x0,y0,step);assert list(map(len,last))==[9,9,10,10]
    assert last[0]==last[1] and last[2]==last[3]
    for z,piece in [(0,'knight'),(2,'bishop')]:verify({9*r+c for r,c,_ in first[z]},first[z],piece)
    cases=[('173-example-knight','knight',first[1]),('173-example-bishop','bishop',first[3])]
    cases += [(f'173b-{z+1}', 'knight' if z<2 else 'bishop',clues) for z,clues in enumerate(second)]
    cases += [(f'174-{z+1}','knight' if z%2==0 else 'bishop',clues) for z,clues in enumerate(last)]
    cases += [('173d-three-clues','knight',[[3,3,6],[4,4,8],[5,5,6]])]
    results=[]
    for name,piece,clues in cases:
        a=sat(clues,piece);b=mcc(clues,piece,name);assert a==b and len(a)==1,(name,a,b)
        if name=='173-example-knight':assert set(a[0])=={9*r+c for r,c,_ in first[0]}
        if name=='173-example-bishop':assert set(a[0])=={9*r+c for r,c,_ in first[2]}
        result=dict(name=name,piece=piece,clues=clues,models=a,unique=True);results.append(result);print(name,'unique',len(clues),'clues',flush=True)
    (OUT/'verified.json').write_text(json.dumps(dict(complete_diagrams=first[::2],cases=results),indent=2)+'\n')

if __name__=='__main__':main()

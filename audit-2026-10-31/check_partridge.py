"""Direct model verification and DLX3 cross-checks of square-multiset packing."""
from pathlib import Path
from collections import Counter
import json,re,subprocess
ROOT=Path(__file__).parent;OUT=ROOT/'results/partridge'


def verify(side,counts,path):
    signatures=set();orbits=set();hist=Counter();orbit_hist=Counter();diag=0
    for line in path.read_text().splitlines():
        d=json.loads(line);tiles=d['tiles'];assert Counter(k for r,c,k in tiles)==Counter({i+1:x for i,x in enumerate(counts) if x})
        cells={}
        for tid,(r,c,k) in enumerate(tiles):
            assert 0<=r<=side-k and 0<=c<=side-k
            for i in range(r,r+k):
                for j in range(c,c+k):assert (i,j) not in cells;cells[i,j]=(tid,k)
        assert len(cells)==side*side
        sig=tuple(sorted(map(tuple,tiles)));assert sig not in signatures;signatures.add(sig)
        images=set()
        for a in range(2):
            for b in range(2):
                for swap in range(2):
                    image=[]
                    for r,c,k in tiles:
                        if swap:r,c=c,r
                        if a:r=side-r-k
                        if b:c=side-c-k
                        image.append((r,c,k))
                    images.add(tuple(sorted(image)))
        assert len(images)==d['orbit_size'];orbit_hist[len(images)]+=1;orbits.add(min(images))
        affinity=sum(cells[r,c][1]==cells[s,t][1] and cells[r,c][0]!=cells[s,t][0]
                     for r in range(side) for c in range(side)
                     for s,t in [(r+1,c),(r,c+1)] if (s,t) in cells)
        hist[affinity]+=1
        if d['affinity']:assert affinity==d['affinity']
        if counts[0]==1:
            r,c,k=next(t for t in tiles if t[2]==1);diag+=r+c==side-1
    return dict(models=len(signatures),symmetry_classes=len(orbits),affinity_histogram=dict(hist),orbit_sizes=dict(orbit_hist),unit_on_antidiagonal=diag)


def inventories(side):
    def visit(k,area,counts):
        if k>side:
            yield [side*side-area]+counts;return
        for n in range((side*side-area)//(k*k)+1):yield from visit(k+1,area+n*k*k,counts+[n])
    yield from visit(2,0,[])


def xcc(side,counts):
    header=[f'c{r}{c}' for r in range(side) for c in range(side)]
    header += [f'{count}|s{k}' for k,count in enumerate(counts,1) if count]
    lines=[' '.join(header)]
    for k,count in enumerate(counts,1):
        if not count:continue
        for r in range(side-k+1):
            for c in range(side-k+1):lines.append(' '.join([f's{k}']+[f'c{i}{j}' for i in range(r,r+k) for j in range(c,c+k)]))
    return '\n'.join(lines)+'\n'


def validate():
    cases=[]
    for side in range(1,6):
        for i,counts in enumerate(inventories(side)):
            path=Path('/tmp/partridge-validation.models.jsonl')
            a=subprocess.run(['/tmp/knuth-partridge',str(side),','.join(map(str,counts)),str(path),'affinity'],capture_output=True,text=True,check=True)
            actual=json.loads(a.stdout);models=verify(side,counts,path)
            p=subprocess.run(['/tmp/knuth-dlx3','v1','d0'],input=xcc(side,counts),text=True,capture_output=True)
            expected=int(re.search(r'Altogether (\d+) solution',p.stderr)[1]);assert actual['solutions']==models['models']==expected
            assert actual['symmetry_classes']==models['symmetry_classes']
            assert {int(k):v for k,v in actual['affinity_histogram'].items()}==models['affinity_histogram']
            cases.append(dict(side=side,counts=counts,solutions=expected,nodes=actual['nodes']))
    (OUT/'validation.json').write_text(json.dumps(cases,indent=2)+'\n')
    print(json.dumps(dict(cases=len(cases),models=sum(c['solutions'] for c in cases))))

if __name__=='__main__':validate()

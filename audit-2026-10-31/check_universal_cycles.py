"""Full 16-bit census and independent exact Euler-tour counts for DLX94--95."""
from datetime import datetime,timezone
from itertools import product
from pathlib import Path
import hashlib,json,re
from colored_dlx import ColoredDLX
from universal_cycles import binary94,cycle95,words95,euler_count95

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/universal_cycles'


class NoEvents(list):
    def append(self,value):pass


def solve(enc):
    s=ColoredDLX(len(enc['names']),enc['primary'],enc['rows'])
    s.events=NoEvents()
    return s.solve().solutions


def decode(enc,model):
    cells={}
    for ri in model:
        for i,c in enc['rows'][ri]:
            name=enc['names'][i-1]
            if name.startswith('x'):
                assert i not in cells or cells[i]==c-1
                cells[i]=c-1
    return tuple(cells[i] for i in sorted(cells))


def rotate_canonical(bits):
    return min(bits[k:]+bits[:k] for k in range(len(bits)))


def direct95(n,p,q):
    allowed=set(words95(n,p,q));m=len(allowed)
    assert m<=16
    cycles=set()
    for bits in product(range(2),repeat=m):
        found={tuple(bits[(j+k)%m] for k in range(n)) for j in range(m)}
        if found==allowed:cycles.add(rotate_canonical(bits))
    return cycles


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    valid=set()
    for bits in product(range(2),repeat=16):
        if len({tuple(bits[(k+d)%16] for d in (0,1,3,4)) for k in range(16)})==16:
            valid.add(bits)
    enc=binary94(); xcc={decode(enc,model) for model in solve(enc)}
    assert xcc==valid
    printed=tuple(map(int,'0000011010111011'))
    orbit=set()
    for rev,comp in product(range(2),repeat=2):
        bits=printed[::-1] if rev else printed
        bits=tuple(b^comp for b in bits)
        orbit.update(bits[k:]+bits[:k] for k in range(16))
    assert orbit==valid
    (OUT/'binary94-models.txt').write_text(''.join(''.join(map(str,b))+'\n' for b in sorted(valid)))
    checks=[]
    for n in range(1,5):
        for p in range(n):
            for q in range(p+1,n+1):
                direct=direct95(n,p,q); determinant=euler_count95(n,p,q)
                assert determinant['cycles']==len(direct)
                counts=[]
                for variant in ('primary','b-secondary','a-secondary','omit-a'):
                    enc=cycle95(n,p,q,variant)
                    models=solve(enc)
                    decoded={rotate_canonical(decode(enc,m)) for m in models}
                    assert len(models)==len(decoded) and decoded==direct,(n,p,q,variant)
                    counts.append(len(models))
                checks.append(dict(n=n,p=p,q=q,cycles=len(direct),four_variants=counts))
    large=[]
    text=(ROOT.parent/'text/vol4b.txt').read_text().split('\f')[153]
    printed95=re.findall(r'\(([01]{30,})\)',text)
    for (p,q,want),bits in zip([(0,3,137216),(3,4,41280)],printed95):
        words=set(words95(7,p,q));m=len(words)
        assert len(bits)==m
        windows={tuple(int(bits[(j+k)%m]) for k in range(7)) for j in range(m)}
        assert windows==words
        result=euler_count95(7,p,q)
        assert result['cycles']==want
        # Independent determinant implementation, applied to the same graph.
        import sympy
        assert int(sympy.Matrix(result['laplacian_minor']).det(method='domain-ge'))==want
        result['printed_cycle']=bits
        large.append(result)
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        module_sha256=hashlib.sha256((ROOT/'universal_cycles.py').read_bytes()).hexdigest(),
        binary94=dict(assignments_examined=65536,solutions=len(valid),
                      rotation_classes=len({rotate_canonical(b) for b in valid}),
                      dihedral_complement_classes=1,complete_xcc_set_equal=True),
        small95=checks,large95=large)
    (OUT/'cycles-checked.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(binary94=result['binary94'],small95=len(checks),
                         large95=[{k:r[k] for k in ('edges','vertices','cycles')} for r in large])))


if __name__=='__main__':main()

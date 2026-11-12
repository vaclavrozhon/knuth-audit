"""Resolve the p111 forcing witness under the printed orientation item order."""
from pathlib import Path
from datetime import datetime,timezone
import ast,json,os,subprocess,time
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/preprocess225'


def main():
    assert os.nice(0)>=15 and not (OUT/'y-order.json').exists()
    source=ROOT/'check_y208_bounded.py';tree=ast.parse(source.read_text())
    S=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='S' for t in n.targets))
    digits='0123456789abcde';cells=[digits[r]+digits[c] for r in range(15) for c in range(15)];rows=[]
    for shape in S:
        coords=[(int(s[0]),int(s[1])) for s in shape]
        for r in range(15):
            for c in range(15):
                shifted=[(r+x,c+y) for x,y in coords]
                if any(x>=15 or y>=15 for x,y in shifted):continue
                rows.append([digits[x]+digits[y] for x,y in shifted])
    old=(OUT/'y15x15.xcc').read_text().splitlines();assert len(rows)==1344
    assert {frozenset(row) for row in rows}=={frozenset(s.split()) for s in old[1:]}
    text=' '.join(cells)+'\n'+'\n'.join(' '.join(row) for row in rows)+'\n';inp=OUT/'y15x15-printed-order.xcc';inp.write_text(text)
    build=json.loads((OUT/'build.json').read_text());assert sha(build['binary'])==build['binary_sha256'];start=time.monotonic()
    p=subprocess.run([build['binary'],'v15','d0'],input=text,text=True,capture_output=True,timeout=5)
    (OUT/'y15x15-printed-order.out').write_text(p.stdout);(OUT/'y15x15-printed-order.log').write_text(p.stderr)
    assert p.returncode==0
    save(OUT/'y-order.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),orientation_source_sha256=sha(source),
        same1344_unordered_options=True,changed='Only option ordering and order of cells within each option now follow the printed S0–S7 list.',
        wall_seconds=time.monotonic()-start,nice=os.nice(0),returncode=p.returncode,timeout_seconds=5,
        hashes={str((OUT/('y15x15-printed-order'+suffix)).relative_to(ROOT)):sha(OUT/('y15x15-printed-order'+suffix)) for suffix in ['.xcc','.out','.log']}))
    print('\n'.join(s for s in p.stderr.splitlines() if s.startswith('Beginning round') or s.startswith('Deleting item 00') or s.startswith('Deleting item 20') or '61 blocked by 50 51 52 53 62' in s or s.startswith('Removed')))


if __name__=='__main__':main()

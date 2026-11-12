"""A checked five-cell universal window on the quotient by (4,4),(4,-4)."""
from datetime import datetime,timezone
from itertools import product
from pathlib import Path
import hashlib,json,re,subprocess
from universal_cycles import instance,native_text

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/universal_cycles'
BIN=Path('/tmp/knuth-vol4b-colored-4ulh1ceo/dlx2-original')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def reduce_cell(x,y):
    quotient,remainder=divmod(y,4)
    return (x-4*quotient)%8,remainder

def main():
    offsets=[(0,0),(1,0),(0,1),(-1,0),(0,-1)]
    positions=list(product(range(8),range(4)))
    # Verify the two lattice generators and the absence of collisions in each cross.
    for x,y in positions:
        assert reduce_cell(x+4,y+4)==reduce_cell(x,y)==reduce_cell(x+4,y-4)
        assert len({reduce_cell(x+dx,y+dy) for dx,dy in offsets})==5
    prim=[f't{i}' for i in range(32)]+[f'p{i}' for i in range(32)]
    sec=[f'd{x}.{y}' for x,y in positions]
    rows=[];info=[]
    for j,bits in enumerate(product(range(2),repeat=5)):
        for k,(x,y) in enumerate(positions):
            if (j==0)!=(k==0):continue
            row=[(f't{j}',0),(f'p{k}',0)]
            for (dx,dy),b in zip(offsets,bits):
                xx,yy=reduce_cell(x+dx,y+dy);row.append((f'd{xx}.{yy}',b+1))
            rows.append(row);info.append((j,k))
    enc=instance(prim,sec,rows,info)
    path=OUT/'cross96.dlx';path.write_text(native_text(enc))
    cmd=[str(BIN),'v129','m1','t1']
    with path.open() as fin:
        completed=subprocess.run(cmd,stdin=fin,capture_output=True,text=True,timeout=60,check=True)
    (OUT/'cross96.out').write_text(completed.stdout);(OUT/'cross96.log').write_text(completed.stderr)
    values={}
    for x,y,b in re.findall(r'd(\d+)\.(\d+):([01])',completed.stdout):
        xy=int(x),int(y)
        assert xy not in values or values[xy]==int(b)
        values[xy]=int(b)
    assert len(values)==32
    patterns={tuple(values[reduce_cell(x+dx,y+dy)] for dx,dy in offsets) for x,y in positions}
    assert patterns==set(product(range(2),repeat=5))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),command=cmd,
        script_sha256=sha(Path(__file__)),input_sha256=sha(path),binary_sha256=sha(BIN),
        source_sha256=sha(ROOT/'sources/knuth-programs/dlx2.w'),
        conclusion='One valid witness, independently checked. t1 stops after one; no total-count claim.',
        offsets=offsets,generators=[[4,4],[4,-4]],rows=[[values[x,y] for x in range(8)] for y in range(4)],
        patterns=32)
    (OUT/'cross96.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()

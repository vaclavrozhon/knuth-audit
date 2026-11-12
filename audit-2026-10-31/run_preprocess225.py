"""Short AlgorithmP reductions only; no exact-cover solution enumeration."""
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
import json,os,shutil,subprocess,tempfile,time
from check_pentomino_bipairs import SHAPES,orientations,normalized,transform
from sudoku_automorphisms114 import instance as sudoku
from puzzle_xcc import save,sha,native_text

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/preprocess225';DIGITS='0123456789abcde'


def pentomino(h,w,onesided):
    shapes={}
    for name,base in SHAPES.items():
        rotation={normalized(transform(base,g)) for g in range(4)}
        all_orientations=orientations(base)
        shapes[name]=rotation if onesided else all_orientations
        if onesided and rotation!=all_orientations:shapes[name.lower()]=all_orientations-rotation
    cells=[DIGITS[r]+DIGITS[c] for r in range(h) for c in range(w)]
    rows=[];xcenters=[]
    for name,shapeset in shapes.items():
        for s in sorted(shapeset):
            for r in range(h-max(x for x,y in s)):
                for c in range(w-max(y for x,y in s)):
                    positions=sorted((r+x,c+y) for x,y in s)
                    if name=='X':
                        rr,cc=positions[2]
                        assert sum(x for x,y in positions)==5*rr and sum(y for x,y in positions)==5*cc
                        if not(rr<h/2 and cc<=(w-1)/2):continue
                        xcenters.append([rr,cc])
                    rows.append([name]+[DIGITS[x]+DIGITS[y] for x,y in positions])
    return ' '.join(list(shapes)+cells)+'\n'+'\n'.join(' '.join(row) for row in rows)+'\n',dict(h=h,w=w,onesided=onesided,pieces=list(shapes),options=len(rows),xcenters=xcenters)


def build():
    dest=Path(tempfile.mkdtemp(prefix='knuth-vol4b-preprocess225-compiler-'))
    source=ROOT/'sources/knuth-programs/dlx-pre.w';header=Path('/tmp/knuth-program-build/gb_flip.h')
    shutil.copyfile(source,dest/'dlx-pre.w');shutil.copyfile(header,dest/'gb_flip.h');logs=[]
    for command in [['ctangle','dlx-pre.w'],['gcc','-O2','-Wno-implicit-int','-Wno-implicit-function-declaration','dlx-pre.c','-o','dlx-pre']]:
        p=subprocess.run(command,cwd=dest,capture_output=True,text=True,timeout=20);logs.append(dict(command=command,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0
    binary=dest/'dlx-pre';save(OUT/'build.json',dict(source=str(source),source_sha256=sha(source),include=str(header),include_sha256=sha(header),commands=logs,binary=str(binary),binary_sha256=sha(binary),generated_c_sha256=sha(dest/'dlx-pre.c')))
    return binary


def main():
    assert os.nice(0)>=15 and not (OUT/'runs.json').exists();binary=build();cases=[]
    for h,w,one in [(6,10,False),(6,15,True)]:
        text,meta=pentomino(h,w,one);assert meta['options']==(2032 if w==10 else 3308)
        cases.append((f'pentomino-{h}x{w}',text,meta))
    for label,source in [('pentomino3x20',ROOT/'results/pentomino_main/full.dlx'),('macmahon126',ROOT/'results/triangles124_126/native/full-original.dlx')]:
        cases.append((label,source.read_text(),dict(accepted_input=str(source.relative_to(ROOT)),input_sha256=sha(source))))
    enc,info=sudoku(3,False);text=native_text(enc);assert len(enc['rows'])==5410
    cases.append(('sudoku114-original',text,dict(primary=enc['primary'],secondary=len(enc['names'])-enc['primary'],options=len(enc['rows']),generator_sha256=sha(ROOT/'sudoku_automorphisms114.py'))))
    # Figure73 before center/H restrictions: all1344 geometric Y placements.
    cells=[DIGITS[r]+DIGITS[c] for r in range(15) for c in range(15)];rows=[]
    for s in sorted(orientations(SHAPES['Y'])):
        for r in range(15-max(x for x,y in s)):
            for c in range(15-max(y for x,y in s)):
                rows.append([DIGITS[r+x]+DIGITS[c+y] for x,y in sorted(s)])
    assert len(rows)==1344;cases.append(('y15x15',' '.join(cells)+'\n'+'\n'.join(' '.join(r) for r in rows)+'\n',dict(options=len(rows),center_or_H_restrictions=False)))
    results=[]
    for label,text,meta in cases:
        inp=OUT/(label+'.xcc');inp.write_text(text);start=time.monotonic()
        command=[str(binary),'v15','d0'];record=dict(label=label,command=command,timeout_seconds=30,input_sha256=sha(inp),metadata=meta,nice=os.nice(0))
        try:
            p=subprocess.run(command,input=text,capture_output=True,text=True,timeout=30)
            (OUT/(label+'.out')).write_text(p.stdout);(OUT/(label+'.log')).write_text(p.stderr)
            record.update(status='completed' if p.returncode==0 else 'failed',returncode=p.returncode,stdout_sha256=sha(OUT/(label+'.out')),stderr_sha256=sha(OUT/(label+'.log')))
        except subprocess.TimeoutExpired as e:
            (OUT/(label+'.out')).write_bytes(e.stdout or b'');(OUT/(label+'.log')).write_bytes(e.stderr or b'')
            record.update(status='timeout',returncode=None)
        record['wall_seconds']=time.monotonic()-start;results.append(record);save(OUT/'runs-progress.json',results)
        print(label,record['status'],round(record['wall_seconds'],3),flush=True)
    save(OUT/'runs.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),runner_sha256=sha(__file__),binary_sha256=sha(binary),runs=results,full_solution_searches=0))


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Author cutoff implementation (one @x context update); native DLX86 costs."""
from datetime import datetime, timezone
from pathlib import Path
import json,random,re,shutil,subprocess,tempfile,urllib.request
from colored_dlx import brute
from dlx1_audit_tools import ROOT,sha

OUT=ROOT/'results/minimax_mc'
SOURCE=ROOT/'sources/minimax_mc'


def build():
    SOURCE.mkdir(parents=True,exist_ok=True)
    metadata=[]
    for name in ('dlx2-cutoff.ch','dance-random.ch'):
        url='https://www-cs-faculty.stanford.edu/~knuth/programs/'+name
        path=SOURCE/name
        if not path.exists():
            with urllib.request.urlopen(url,timeout=45) as r:data=r.read()
            assert data.startswith(b'@x'),name
            path.write_bytes(data)
        metadata.append(dict(path=str(path.relative_to(ROOT)),url=url,sha256=sha(path),bytes=path.stat().st_size))
    manifest=OUT/'native-build.json'
    if manifest.exists():
        data=json.loads(manifest.read_text())
        assert sha(data['binary'])==data['binary_sha256']
        assert data['official_change_files']==metadata
        return data
    directory=Path(tempfile.mkdtemp(prefix='knuth-vol4b-minimax-'))
    source=ROOT/'sources/knuth-programs'
    for name in ('dlx2.w','gb_flip.w','gb_flip.ch','boilerplate.w'):
        shutil.copy2(source/name,directory/name)
    original=(SOURCE/'dlx2-cutoff.ch').read_text()
    base=(source/'dlx2.w').read_text()
    needle='            nn=dd;@+continue;\n          }'
    start=base.index('void unpurify(int p) {')
    stop=base.index(needle,start)+len(needle)
    # Current DLX2 added a diagnostic and replaced an unreachable rr!=p guard.
    # Only the OLD match side changes; every author-supplied @y replacement is exact.
    patched=re.sub(r'@x\nvoid unpurify\(int p\) \{.*?\n@y',
                   lambda _: '@x\n'+base[start:stop]+'\n@y',original,flags=re.S)
    assert patched!=original
    assert re.findall(r'@y\n(.*?)\n@z',original,re.S)==re.findall(r'@y\n(.*?)\n@z',patched,re.S)
    (directory/'dlx2-cutoff.ch').write_text(patched)
    (OUT/'dlx2-cutoff-context.ch').write_text(patched)
    commands=[['ctangle','gb_flip.w','gb_flip.ch'],['ctangle','dlx2.w','dlx2-cutoff.ch'],
              ['cc','-O2','-Wno-implicit-int','-Wno-implicit-function-declaration','dlx2.c','gb_flip.c','-o','dlx2-cutoff']]
    OUT.mkdir(parents=True,exist_ok=True)
    if (OUT/'native-build.log').exists() and not (OUT/'native-build-original.log').exists():
        shutil.copy2(OUT/'native-build.log',OUT/'native-build-original.log')
    with (OUT/'native-build.log').open('w') as log:
        for cmd in commands:subprocess.run(cmd,cwd=directory,stdout=log,stderr=subprocess.STDOUT,check=True)
    data=dict(built_at_utc=datetime.now(timezone.utc).isoformat(),commands=commands,
        official_change_files=metadata,binary=str(directory/'dlx2-cutoff'),binary_sha256=sha(directory/'dlx2-cutoff'),
        other_sources={n:sha(source/n) for n in ('dlx2.w','gb_flip.w','gb_flip.ch','boilerplate.w')},
        adapted_change_sha256=sha(OUT/'dlx2-cutoff-context.ch'),
        scope='Official DLX2 plus official dlx2-cutoff.ch with only the old @x context of unpurify updated to match current DLX2. Every @y replacement is unchanged and programmatically checked. Original source and failed initial build log retained. dance-random.ch is archived for source comparison only, not compiled.')
    manifest.write_text(json.dumps(data,indent=2)+'\n')
    return data


def token(i,c):return 'i'+str(i)+(':'+chr(64+c) if c else '')


def input_text(n,primary,rows):
    return ' '.join(['i'+str(i) for i in range(1,primary+1)]+['|']+
                    ['i'+str(i) for i in range(primary+1,n+1)])+'\n'+''.join(
                    ' '.join(token(i,c) for i,c in row)+'\n' for row in rows)


def run(binary,n,primary,rows):
    data=input_text(n,primary,rows)
    command=[binary,'v9','m1']
    p=subprocess.run(command,input=data,text=True,capture_output=True,timeout=10)
    assert p.returncode==0,p.stderr
    match=re.search(r'Altogether (\d+) solution.*?(\d+) updates, (\d+) cleansings,',p.stderr,re.S)
    assert match,p.stderr
    table={frozenset(token(i,c) for i,c in row):r for r,row in enumerate(rows)}
    assert len(table)==len(rows)
    models=[]; model=[]
    for line in p.stdout.splitlines():
        if re.fullmatch(r'\d+:',line):
            if model:models.append(tuple(sorted(model)))
            model=[]
        elif line.strip():
            key=frozenset(line.split(' (',1)[0].split())
            assert key in table,(line,table)
            model.append(table[key])
    if model:models.append(tuple(sorted(model)))
    assert len(models)==int(match[1])
    return dict(n=n,primary=primary,rows=rows,command=command,input=data,stdout=p.stdout,stderr=p.stderr,
                solutions=int(match[1]),updates=int(match[2]),cleansings=int(match[3]),models=models)


def main():
    built=build()
    rng=random.Random(840086)
    matrices=[]
    universe=[((1,0),),((2,0),),((1,0),(2,0)),
              ((1,0),(3,0)),((1,0),(3,1)),((1,0),(3,2)),
              ((2,0),(3,0)),((2,0),(3,1)),((2,0),(3,2)),
              ((1,0),(2,0),(3,1)),((1,0),(2,0),(3,2))]
    for _ in range(100):matrices.append((3,2,rng.sample(universe,rng.randrange(10))))
    cases=[]
    for n,primary,rows in matrices:
        result=run(built['binary'],n,primary,rows)
        expected=brute(primary,rows)
        if expected:
            optimum=min(map(max,expected))
            wanted={m for m in expected if max(m)==optimum}
            got={m for m in result['models'] if max(m)==optimum}
            assert got==wanted,(result,wanted)
            assert all(m in expected for m in result['models'])
            assert all(max(a)>=max(b) for a,b in zip(result['models'],result['models'][1:]))
        else:assert result['models']==[]
        cases.append(result)
    original=json.loads((ROOT/'results/colored_basics/native/build.json').read_text())['binaries']['original']
    assert sha(original['binary'])==original['sha256']
    witness_data=json.loads((OUT/'monte-carlo.json').read_text())['witnesses']
    costs={}
    for name,witness in witness_data.items():
        result=run(original['binary'],witness['n'],witness['primary'],witness['rows'])
        for k in ('solutions','updates','cleansings'):assert result[k]==witness[k],(name,k,result,witness)
        costs[name]=result
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
                native_cutoff_cases=cases,native_cost_witnesses=costs,original_binary=original,
                all_complete_optimal_model_sets_match=True,all_original_costs_match=True)
    (OUT/'native-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:100 original native cutoff cases;4 original cost witnesses')


if __name__=='__main__':main()

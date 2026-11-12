"""Compile original CWEB programs and record complete original runs.

A separate launcher discards the unspecified return value of old-style main.
The archived source and its algorithm are unchanged.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json
import re
import subprocess
import tempfile
import time

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'sources/questionnaires'
OUT=ROOT/'results/questionnaires'


def build():
    directory=Path(tempfile.mkdtemp(prefix='knuth-vol4b-questionnaires-'))
    launcher=directory/'launcher.c'
    launcher.write_text('extern int knuth_main(int, char **);\n'
                        'int main(int argc, char **argv) { knuth_main(argc, argv); return 0; }\n')
    commands=[]
    for name,source,change in [
        ('base','back-20q.w',None),
        ('modified','back-20q.w','back-20q-backmod9,15.ch'),
        ('indeterminate','back-20q.w','back-20q-backmod9,15-indet.ch'),
        ('pi-day','back-pi-day.w',None)]:
        cmds=[['ctangle',str(SRC/source),str(SRC/change) if change else '-',str(directory/(name+'.c'))],
              ['gcc','-std=gnu89','-O2','-include','stdlib.h','-Dmain=knuth_main','-c',
               str(directory/(name+'.c')),'-o',str(directory/(name+'.o'))],
              ['gcc','-O2',str(launcher),str(directory/(name+'.o')),'-o',str(directory/name)]]
        for cmd in cmds:
            p=subprocess.run(cmd,capture_output=True,text=True)
            assert p.returncode==0,(cmd,p.stdout,p.stderr)
            commands.append(cmd)
    (OUT/'build-normalized.json').write_text(json.dumps(dict(directory=str(directory),
        commands=commands,source_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest()
                                      for p in SRC.iterdir() if p.suffix in ['.w','.ch']}),indent=2)+'\n')
    return directory


def main():
    OUT.mkdir(exist_ok=True)
    directory=build()
    all_runs=[]
    for name in ['base','modified','indeterminate']:
        for false in range(21):
            start=time.monotonic()
            command=[str(directory/name),str(false),'0']
            p=subprocess.run(command,capture_output=True,text=True,timeout=300)
            assert p.returncode==0,(command,p.returncode,p.stderr)
            match=re.search(r'Altogether (\d+) solutions \((\d+) mems, (\d+) nodes\)',p.stderr)
            assert match,p.stderr
            solutions=re.findall(r'^\d+: ([A-Ea-e]{20})$',p.stdout,re.M)
            count,mems,nodes=map(int,match.groups())
            assert count==len(solutions)
            result=dict(variant=name,false=false,count=count,mems=mems,nodes=nodes,
                        solutions=solutions,returncode=p.returncode,elapsed_seconds=time.monotonic()-start)
            all_runs.append(result)
            (OUT/'original-runs.json').write_text(json.dumps(all_runs,indent=2)+'\n')
            print(name,false,count,mems,nodes,flush=True)
    start=time.monotonic()
    with (OUT/'pi-day-normalized.out').open('w') as stdout,(OUT/'pi-day-normalized.log').open('w') as stderr:
        p=subprocess.run([str(directory/'pi-day')],stdout=stdout,stderr=stderr,timeout=60)
    assert p.returncode==0
    log=(OUT/'pi-day-normalized.log').read_text()
    match=re.search(r'Stability achieved after (\d+) tests, (\d+) rounds, (\d+) mems',log)
    assert match
    stats=list(map(int,match.groups()))
    assert stats[:2]==[301,6]
    raw=(OUT/'pi-day-normalized.out').read_text()
    solution={int(i):int(d) for i,d in re.findall(r'(\d{2})\((\d)\)',raw)}
    assert len(solution)==100
    independent=json.loads((ROOT/'results/factor_puzzles/arrows-verified.json').read_text())
    assert [solution[i] for i in range(100)]==independent['printed_solution']
    source=(SRC/'back-pi-day.w').read_text().split('char johan[10][10]=',1)[1].split(';',1)[0]
    clues=re.findall(r'([NSEW])\+(\d)',source)
    assert len(clues)==100
    directions={'N':(0,-1),'S':(0,1),'E':(1,0),'W':(-1,0)}
    extracted=json.loads((ROOT/'results/factor_puzzles/arrows-extracted.json').read_text())
    # The PDF trace is authoritative for the data, independent of CWEB literals.
    board=extracted[0] if isinstance(extracted,list) else extracted['boards'][0]
    assert [list(directions[d]) for d,c in clues]==board['directions_xy']
    assert [int(c) if int(c) else None for d,c in clues]==board['digits']
    result=dict(status='pass',refinements=stats[0],rounds=stats[1],mems=stats[2],
                returncode=0,solution=solution,elapsed_seconds=time.monotonic()-start,
                checked_against='independent PDF extraction and all 100 equations')
    (OUT/'pi-day-verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS pi-day',stats,flush=True)


if __name__=='__main__':
    main()

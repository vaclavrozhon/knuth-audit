"""Reproduce F097 in the current official BACK-20Q source and check a fix."""
from pathlib import Path
import json,re,subprocess,time
import z3 as z
from check_questionnaires import model,literal_grade
from run_questionnaires import build

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/questionnaires'


def main():
    solver,a,x=model(False,18)
    grades=[j not in (17,19) for j in range(20)]
    for v,b in zip(x,grades):solver.add(v==b)
    expected=[]
    while True:
        status=solver.check()
        if status==z.unsat:break
        assert status==z.sat
        sol=solver.model();values=[sol.eval(v).as_long() for v in a]
        answer=''.join('ABCDE'[v] for v in values)
        # The witness also has these grades with the actual maximum 19.
        assert literal_grade(answer,grades,False,19)==grades
        expected.append(''.join(c if good else c.lower() for c,good in zip(answer,grades)))
        solver.add(z.Or([v!=value for v,value in zip(a,values)]))
    assert expected==['AEBCDBCBCABECACDDbEc']
    metadata=OUT/'build-normalized.json'
    directory=Path(json.loads(metadata.read_text())['directory']) if metadata.exists() else None
    if directory is None or not (directory/'base').exists():directory=build()
    cmds=[['ctangle',str(ROOT/'sources/questionnaires/back-20q.w'),
           str(ROOT/'back-20q-fix18.ch'),str(directory/'fixed18.c')],
          ['gcc','-std=gnu89','-O2','-include','stdlib.h','-Dmain=knuth_main','-c',
           str(directory/'fixed18.c'),'-o',str(directory/'fixed18.o')],
          ['gcc','-O2',str(directory/'launcher.c'),str(directory/'fixed18.o'),
           '-o',str(directory/'fixed18')]]
    for cmd in cmds:
        p=subprocess.run(cmd,capture_output=True,text=True)
        assert p.returncode==0,(cmd,p.stdout,p.stderr)
    runs=[]
    for binary,expected_count in [('base',0),('fixed18',1)]:
        command=[str(directory/binary),'18','20'];start=time.monotonic()
        p=subprocess.run(command,capture_output=True,text=True,timeout=60)
        assert p.returncode==0
        solutions=re.findall(r'^\d+: ([A-Ea-e]{20})$',p.stdout,re.M)
        count,mems,nodes=map(int,re.search(r'Altogether (\d+) solutions \((\d+) mems, (\d+) nodes\)',p.stderr).groups())
        assert len(solutions)==count==expected_count
        if binary=='fixed18':assert solutions==expected
        runs.append(dict(command=command,count=count,solutions=solutions,mems=mems,
                         nodes=nodes,returncode=0,elapsed_seconds=time.monotonic()-start))
    out=dict(status='pass',independent_solutions=expected,commands=cmds,runs=runs)
    (OUT/'back20q-bug-verified.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS F097: original 0, fixed 1, independent 1')


if __name__=='__main__':main()

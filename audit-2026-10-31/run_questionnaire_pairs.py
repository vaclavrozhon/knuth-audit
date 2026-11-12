"""All original modified-questionnaire runs with exactly two incorrect answers."""
from pathlib import Path
from itertools import combinations
import json,re,subprocess,time,os

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/questionnaires'


def main():
    binary=Path(json.loads((OUT/'build-normalized.json').read_text())['directory'])/'modified'
    rows=[];start=time.monotonic()
    for a,b in combinations(range(1,21),2):
        p=subprocess.run([str(binary),str(a),str(b)],capture_output=True,text=True,timeout=300)
        assert p.returncode==0,(a,b,p.returncode,p.stderr)
        match=re.search(r'Altogether (\d+) solutions \((\d+) mems, (\d+) nodes\)',p.stderr)
        assert match
        solutions=re.findall(r'^\d+: ([A-Ea-e]{20})$',p.stdout,re.M)
        count,mems,nodes=map(int,match.groups());assert count==len(solutions)
        rows.append(dict(false=[a,b],count=count,mems=mems,nodes=nodes,solutions=solutions))
        data=dict(status='running',pid=os.getpid(),rows=rows,elapsed_seconds=time.monotonic()-start)
        (OUT/'original-pairs.json').write_text(json.dumps(data,indent=2)+'\n')
        if len(rows)%10==0:print('pairs',len(rows),'seconds',data['elapsed_seconds'],flush=True)
    for last in ['A','c']:
        actual=sorted(s for row in rows for s in row['solutions'] if s[-1]==last)
        expected=json.loads((OUT/f'modified-18-{last.upper()}.json').read_text())['solutions']
        assert actual==expected,(last,len(actual),len(expected))
    data['status']='pass';(OUT/'original-pairs.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PASS 190 patterns; 48 final-A and 2 final-c solutions',flush=True)


if __name__=='__main__':main()

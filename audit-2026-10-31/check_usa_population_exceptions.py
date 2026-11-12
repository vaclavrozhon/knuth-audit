"""Investigate34111 with the two NY exceptions, preserving the accepted census."""
from pathlib import Path
from datetime import datetime, timezone
import json
import os
import subprocess
import tempfile
import time
from puzzle_xcc import save, sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/usa239_246'


def main():
    assert os.nice(0)>=15 and not (OUT/'ny-exception-run.json').exists()
    original=ROOT/'usa_population_options.cpp'
    accepted=json.loads((OUT/'population-runs.json').read_text())
    assert sha(original)==accepted['source_sha256']
    names=accepted['cases'][0]['states'];index={s:i for i,s in enumerate(names)}
    data=json.loads((OUT/'figures.json').read_text())['data']
    sets=[['NY','ME','NH','VT','MA','CT','RI'],['NY','ME','NH','VT','MA','CT','RI','NJ']]
    exceptions=[dict(mask=sum(1<<index[s] for s in group),population=sum(data['population'][s] for s in group),states=group) for group in sets]
    before='if(total<low*((total+high-2)/(high-1))) return false;'
    checks=['possible(total)']+[f'((component & {e["mask"]}ULL)=={e["mask"]}ULL && possible(total-{e["population"]}LL))' for e in exceptions]
    after='auto possible = [&](long long t) { return t>=0 && t>=low*((t+high-2)/(high-1)); };\n    if(!('+' || '.join(checks)+')) return false;'
    code=original.read_text();assert code.count(before)==1
    temp=Path(tempfile.mkdtemp(prefix='knuth-vol4b-usa-exceptions-'))
    changed=temp/'with-ny.cpp';changed.write_text(code.replace(before,after));binary=temp/'with-ny'
    subprocess.run(['g++','-O3','-std=c++17',str(changed),'-o',str(binary)],check=True)
    inp=OUT/'pop38.input';dest=OUT/'pop38-with-ny.out';log=OUT/'pop38-with-ny.log';t=time.monotonic()
    with inp.open() as i,dest.open('w') as o,log.open('w') as e:
        child=subprocess.Popen([str(binary)],stdin=i,stdout=o,stderr=e)
        try:child.wait(timeout=20);status='complete' if child.returncode==0 else 'error'
        except subprocess.TimeoutExpired:child.terminate();child.wait();status='timeout_incomplete_not_unsat'
    report=dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),source_sha256=sha(original),
                derived_source_sha256=sha(changed),binary_sha256=sha(binary),replacement=dict(before=before,after=after),exceptions=exceptions,
                temp=str(temp),nice=os.nice(0),limit_seconds=20,pid=child.pid,returncode=child.returncode,status=status,
                seconds=time.monotonic()-t,input_sha256=sha(inp),output_sha256=sha(dest),log_sha256=sha(log),
                reason='New residual feasibility convention, motivated by the unresolved34111 discrepancy; no accepted cover optimization repeated.')
    if status=='complete':
        terminal=json.loads(log.read_text());masks=list(map(int,dest.read_text().split()))
        assert len(masks)==len(set(masks))==terminal['reduced_count']
        report.update(terminal=terminal,all_output_masks_unique=True)
    save(OUT/'ny-exception-run.json',report)
    print(status,report.get('terminal'),report['seconds'])


if __name__=='__main__':main()

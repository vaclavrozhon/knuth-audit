"""Durable sequential original-DLX2 jobs for exercises94--97.

Frozen while the queue is live. Individual terminal JSON files are accepted
separately; timeout never implies exhaustion of the search tree.
"""
from datetime import datetime,timezone
from pathlib import Path
import gzip,hashlib,json,os,re,subprocess,time
from universal_cycles import binary94,cycle95,torus96,torus97,native_text

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/universal_cycles'
NATIVE=Path('/tmp/knuth-vol4b-colored-4ulh1ceo/dlx2-original')
LIMIT=172800

def now():return datetime.now(timezone.utc).isoformat()
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def save(path,data):
    temp=path.with_suffix(path.suffix+'.tmp')
    temp.write_text(json.dumps(data,indent=2)+'\n');temp.replace(path)


def run(label,enc,models):
    terminal=OUT/(label+'.json')
    assert not terminal.exists(),label
    inp=OUT/(label+'.dlx');inp.write_text(native_text(enc))
    command=['timeout',str(LIMIT),str(NATIVE),'v129','m1' if models else 'm0']
    start=time.monotonic()
    meta=dict(label=label,status='running',started_utc=now(),wrapper_pid=os.getpid(),
        command=command,timeout_seconds=LIMIT,input_sha256=sha(inp),
        binary_sha256=sha(NATIVE),source_sha256=sha(ROOT/'sources/knuth-programs/dlx2.w'),
        script_sha256=sha(Path(__file__)),module_sha256=sha(ROOT/'universal_cycles.py'),
        primary=enc['primary'],items=len(enc['names']),options=len(enc['rows']))
    with inp.open('rb') as fin,(OUT/(label+'.log')).open('wb') as err:
        p=subprocess.Popen(command,stdin=fin,stdout=subprocess.PIPE,stderr=err)
        meta['pid']=p.pid;save(OUT/(label+'-run.json'),meta)
        with gzip.open(OUT/(label+'.out.gz'),'wb') as compressed:
            for block in iter(lambda:p.stdout.read(65536),b''):compressed.write(block)
        rc=p.wait()
    log=(OUT/(label+'.log')).read_text()
    count=re.search(r'Altogether (\d+) solutions, (\d+)\+(\d+)-(\d+) mems, .*?, (\d+) nodes',log)
    complete=rc==0 and count is not None
    meta.update(status='completed' if complete else 'incomplete',returncode=rc,
                finished_utc=now(),elapsed_seconds=time.monotonic()-start,
                stderr_sha256=sha(OUT/(label+'.log')),stdout_sha256=sha(OUT/(label+'.out.gz')))
    if count:
        s,init,mem,unmem,nodes=map(int,count.groups())
        meta.update(solutions=s,initial_mems=init,search_mems=mem,unmems=unmem,
                    net_search_mems=mem-unmem,nodes=nodes)
    save(terminal,meta);save(OUT/(label+'-run.json'),meta)
    print(label,meta['status'],meta.get('solutions'),flush=True)
    return meta


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    jobs=[('native94',binary94(),True),('native96',torus96(),True),('native97',torus97(),True)]
    for variant in ['primary','b-secondary']:
        for p,q in [(0,3),(3,4)]:
            jobs.append((f'native95-7-{p}-{q}-{variant}',cycle95(7,p,q,variant),False))
    state=dict(wrapper_pid=os.getpid(),status='running',started_utc=now(),jobs=[x[0] for x in jobs],done=[])
    save(OUT/'native-queue.json',state)
    for label,enc,models in jobs:
        if (OUT/(label+'.json')).exists():
            previous=json.loads((OUT/(label+'.json')).read_text())
            assert previous['status']=='completed',label
            state['done'].append(label);continue
        state['current']=label;save(OUT/'native-queue.json',state)
        result=run(label,enc,models)
        state['done'].append(label)
        if result['status']!='completed':break
    state.update(status='completed' if len(state['done'])==len(jobs) else 'incomplete',finished_utc=now())
    save(OUT/'native-queue.json',state)


if __name__=='__main__':main()

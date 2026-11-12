"""Recorded native runs for115--120; direct files preserve output if a wrapper dies."""
from datetime import datetime,timezone
from pathlib import Path
import fcntl,gzip,hashlib,json,os,re,shutil,subprocess,time
from puzzle_xcc import encode,native_text,save

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/graphs115_120'
NATIVE=Path('/tmp/knuth-vol4b-colored-4ulh1ceo/dlx2-original')


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for block in iter(lambda:f.read(1<<20),b''):h.update(block)
    return h.hexdigest()


def run(label,enc,*,binary=NATIVE,source=None,every=1,limit=172800,extra=()):
    lock=(OUT/(label+'.lock')).open('w');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    text=native_text(enc) if isinstance(enc,dict) else enc
    inp=OUT/(label+'.dlx');end=OUT/(label+'.json')
    if end.exists():
        m=json.loads(end.read_text());assert m['status']=='completed' and m['returncode']==0
        assert inp.read_text()==text and sha(inp)==m['input_sha256']
        assert sha(OUT/(label+'.out.gz'))==m['stdout_sha256'] and sha(OUT/(label+'.log'))==m['stderr_sha256']
        return m
    assert not (OUT/(label+'-run.json')).exists(),'Inspect previous evidence; never restart implicitly.'
    inp.write_text(text);source=source or ROOT/'sources/knuth-programs/dlx2.w'
    command=['timeout',str(limit),str(binary),'v129','m'+str(every),*extra]
    m=dict(status='running',wrapper_pid=os.getpid(),command=command,started_utc=datetime.now(timezone.utc).isoformat(),
        timeout_seconds=limit,input_sha256=sha(inp),binary_sha256=sha(binary),source=str(source),source_sha256=sha(source),
        runner_sha256=sha(__file__),model_output_period=every)
    if isinstance(enc,dict):m.update(primary=enc['primary'],items=len(enc['names']),options=len(enc['rows']))
    raw=OUT/(label+'.stdout');start=time.monotonic()
    with inp.open('rb') as fin,raw.open('wb') as fout,(OUT/(label+'.log')).open('wb') as ferr:
        p=subprocess.Popen(command,stdin=fin,stdout=fout,stderr=ferr);m['pid']=p.pid
        save(OUT/(label+'-run.json'),m);rc=p.wait()
    log=(OUT/(label+'.log')).read_text()
    match=re.search(r'Altogether (\d+) solutions?, (\d+)\+(\d+)(?:-(\d+))? mems, .*?, (\d+) nodes',log)
    m.update(status='completed' if rc==0 and match else 'incomplete',returncode=rc,
        finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,
        raw_stdout_sha256=sha(raw),stderr_sha256=sha(OUT/(label+'.log')))
    with raw.open('rb') as fin,gzip.open(OUT/(label+'.out.gz'),'wb') as fout:shutil.copyfileobj(fin,fout)
    m['stdout_sha256']=sha(OUT/(label+'.out.gz'))
    if match:
        count,init,mem,unmem,nodes=(int(x or 0) for x in match.groups())
        m.update(solutions=count,initial_mems=init,search_mems=mem,unmems=unmem,net_search_mems=mem-unmem,nodes=nodes)
    save(end,m);save(OUT/(label+'-run.json'),m)
    # The compressed copy is complete and its original-byte hash is recorded.
    if m['status']=='completed':raw.unlink()
    return m


def models(label,enc):
    lookup={tuple(sorted(line.split())):i for i,line in enumerate(native_text(enc).splitlines()[1:])}
    assert len(lookup)==len(enc['rows']);model=None
    with gzip.open(OUT/(label+'.out.gz'),'rt') as f:
        for line in f:
            if re.fullmatch(r'\d+:\s*',line):
                if model is not None:yield tuple(sorted(model))
                model=[]
            elif line.strip():
                tokens=re.sub(r'\s*\(\d+ of \d+\)\s*$','',line).split()
                assert model is not None;model.append(lookup[tuple(sorted(tokens))])
    if model is not None:yield tuple(sorted(model))

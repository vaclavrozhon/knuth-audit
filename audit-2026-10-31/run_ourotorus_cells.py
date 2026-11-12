"""Compile and run the independent cell enumeration; durable terminal records."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,os,subprocess,tempfile,time

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/universal_cycles'

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def now():return datetime.now(timezone.utc).isoformat()
def save(path,data):
    temp=path.with_suffix(path.suffix+'.tmp');temp.write_text(json.dumps(data,indent=2)+'\n');temp.replace(path)


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    build=Path(tempfile.mkdtemp(prefix='knuth-vol4b-ourotorus-'))
    source=ROOT/'enumerate_ourotorus.cpp';binary=build/'enumerate'
    command=['g++','-O3','-std=c++17','-Wall','-Wextra',str(source),'-o',str(binary)]
    built=subprocess.run(command,capture_output=True,text=True,check=True)
    metadata=dict(compile_command=command,source_sha256=sha(source),binary=str(binary),binary_sha256=sha(binary),
                  compiler=subprocess.check_output(['g++','--version'],text=True).splitlines()[0],stderr=built.stderr)
    save(OUT/'cell-build.json',metadata)
    for exercise in [96,97]:
        label=f'cell{exercise}'
        assert not (OUT/(label+'.json')).exists(),label
        start=time.monotonic()
        cmd=['timeout','172800',str(binary),str(exercise)]
        run=dict(status='running',exercise=exercise,command=cmd,wrapper_pid=os.getpid(),
                 started_utc=now(),timeout_seconds=172800,script_sha256=sha(Path(__file__)),**metadata)
        run['command']=cmd
        with (OUT/(label+'-models.txt')).open('wb') as fout,(OUT/(label+'.log')).open('wb') as err:
            p=subprocess.Popen(cmd,stdout=fout,stderr=err);run['pid']=p.pid
            save(OUT/(label+'-run.json'),run);rc=p.wait()
        log=(OUT/(label+'.log')).read_text()
        import re
        done=re.search(r'COMPLETED (\d+) (\d+) nodes (\d+) solutions',log)
        run.update(status='completed' if rc==0 and done else 'incomplete',returncode=rc,
                   finished_utc=now(),elapsed_seconds=time.monotonic()-start,
                   models_sha256=sha(OUT/(label+'-models.txt')),stderr_sha256=sha(OUT/(label+'.log')))
        if done:
            ex,nodes,count=map(int,done.groups());assert ex==exercise
            run.update(nodes=nodes,solutions=count)
        save(OUT/(label+'.json'),run);save(OUT/(label+'-run.json'),run)
        print(label,run['status'],run.get('solutions'),flush=True)
        if run['status']!='completed':break


if __name__=='__main__':main()

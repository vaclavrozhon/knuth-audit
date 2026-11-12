"""Persistent exact optimum checks; timeout is recorded, never called UNSAT."""
from datetime import datetime,timezone
import fcntl,hashlib,json,os,time,traceback
from pathlib import Path
from double_word_tools import dictionary
from three_way_stairs import ThreeWayCSP,IncompleteSearch,validate

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/three_way_stairs'

def now():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(path,data):
    tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(data,indent=2)+'\n');tmp.replace(path)

def main():
    with (OUT/'queue.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        checked=json.loads((OUT/'checked.json').read_text())
        jobs=sorted(checked['examples'],key=lambda x:(x['kind']=='two-way',x['p']))
        state=dict(pid=os.getpid(),status='running',started_utc=now(),timeout_per_case_seconds=172800,
            script_sha256=sha(__file__),module_sha256=sha(ROOT/'three_way_stairs.py'),
            wordlist_sha256=sha(ROOT/'sources/wordlists/words5-from-sgb'),
            jobs=[f"{j['kind']}-{j['p']}" for j in jobs],completed=[])
        words=dictionary(5);statepath=OUT/'queue.json'
        for job in jobs:
            label=f"{job['kind']}-{job['p']}";path=OUT/(label+'.json')
            if path.exists():
                old=json.loads(path.read_text());assert old.get('status')=='proved',label
                state['completed'].append(label);continue
            state.update(active=label,active_started_utc=now());save(statepath,state)
            result=dict(kind=job['kind'],p=job['p'],printed_rank=job['rank'],printed_rows=job['rows'],
                best_rank=job['rank'],best_rows=job['rows'],attempts=[],started_utc=now(),status='running',
                module_sha256=state['module_sha256'],wordlist_sha256=state['wordlist_sha256'])
            deadline=time.monotonic()+state['timeout_per_case_seconds']
            try:
                while True:
                    B=result['best_rank']-1;state['active_threshold']=B;save(statepath,state)
                    csp=ThreeWayCSP(words[:B],job['p'],job['kind'])
                    try:sol=csp.solve(first=True,timeout=max(.001,deadline-time.monotonic()))
                    except IncompleteSearch:
                        result['status']='incomplete';result['attempts'].append(dict(threshold=B,complete=False,nodes=csp.nodes,seconds=csp.seconds));break
                    attempt=dict(threshold=B,complete=True,sat=bool(sol),nodes=csp.nodes,seconds=csp.seconds,cache=csp.cache)
                    result['attempts'].append(attempt)
                    if not sol:
                        result['status']='proved';break
                    rows=list(sol[0]);rank=validate(rows,words,job['kind']);assert rank<=B
                    result.update(best_rank=rank,best_rows=rows);attempt['witness']=rows
                    save(OUT/(label+'-progress.json'),result)
                result['finished_utc']=now();save(path,result);state['completed'].append(label)
                print(label,result['status'],result['best_rank'],'nodes',sum(a['nodes'] for a in result['attempts']),flush=True)
            except BaseException as e:
                result.update(status='failed',error=repr(e),traceback=traceback.format_exc());save(path,result)
                state.update(status='failed',error=repr(e));save(statepath,state);raise
        state.update(status='finished',active=None,finished_utc=now());save(statepath,state)

if __name__=='__main__':main()

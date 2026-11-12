"""Additional independence check: all original domains, no CSP pruning."""
from check_anacrostic import load,sat_solve,validate,OUT
import hashlib,json,os,time
from datetime import datetime,timezone

started=time.time()
meta={'pid':os.getpid(),'started_at_utc':datetime.now(timezone.utc).isoformat(),
      'status':'running','reason':'Remove shared initial arc-consistency pruning from the independent SAT count.'}
(OUT/'full-sat-run.json').write_text(json.dumps(meta,indent=2)+'\n')
_,domains,positions=load()
solutions,stats=sat_solve(domains,positions,support_encoding=True)
decoded=sorted(tuple(domains[i][k] for i,k in enumerate(s)) for s in solutions)
expected=sorted(tuple(s) for s in json.loads((OUT/'solutions.json').read_text()))
for s in decoded:validate(s,positions)
assert decoded==expected and len(decoded)==720
meta.update(status='pass',count=720,elapsed_seconds=time.time()-started,
            finished_at_utc=datetime.now(timezone.utc).isoformat(),independent_sat=stats,
            solutions_sha256=hashlib.sha256(json.dumps(decoded,separators=(',',':')).encode()).hexdigest())
(OUT/'full-sat-run.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta,indent=2),flush=True)

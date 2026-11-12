"""Small isolated examples; does not repeat the exhaustive buddy audit."""
import json,copy,sys
from pathlib import Path
sys.dont_write_bytecode=True
from buddy import Buddy,memory_of,execute,get,HEAD,FWD,BWD

s=Buddy(4)
for _ in range(4):s.reserve(0)
s.liberate(2);s.liberate(0)
mem,p,t,_,_=execute(memory_of(s),0,mode='published-2006')
_,next_p,_,_,_=execute(mem,0,mode='published-2006')
fixed,fp,_,_,_=execute(memory_of(s),0)
_,fn,_,_,_=execute(fixed,0)
assert (p,next_p,fp,fn)==(0,None,2,0)
out={'published_2006':dict(free_before=s.free,allocated=p,
    head_forward=get(mem,HEAD,FWD,64),head_backward=get(mem,HEAD,BWD,64),
    next_request=next_p,repaired_allocations=[fp,fn])}
s=Buddy(6)
s.reserve(2);s.reserve(0);s.reserve(0)
t=copy.deepcopy(s)
for p in (5,4):s.liberate(p,True);t.liberate(p)
before=copy.deepcopy(s.free);right=copy.deepcopy(t.free)
bad=s.reserve(1)[0];good=t.reserve(1)[0]
assert bad is None and good==4
out['nonpower_endpoint']=dict(M=6,printed_free=before,repaired_free=right,
                              printed_request=bad,repaired_request=good)
(Path(__file__).parent/'results'/'buddy-minimal.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

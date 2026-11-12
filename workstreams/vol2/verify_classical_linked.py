#!/usr/bin/env python3
"""Independent exact and allocation checks for the linked-word subroutines."""
from pathlib import Path
import json,random,sys,time
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'sources'))
from linked_integer import Pool,Number,add,subtract,multiply,divmod_trunc
OUT=ROOT/'results/classical-linked.json'
data=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
def save(k,v):
    data[k]=v;OUT.write_text(json.dumps(data,indent=2)+'\n');print(k,v,flush=True)

def check_pair(p,a,b,structural=False):
    u=Number.from_int(p,a);v=Number.from_int(p,b);out=[]
    try:
        for fn,expected in [(add,a+b),(subtract,a-b),(multiply,a*b)]:
            z=fn(u,v);out.append(z);assert z.to_int()==expected,(p.base,fn.__name__,a,b,z.to_int(),expected)
        if b:
            q,r=divmod_trunc(u,v);out.extend((q,r))
            expected=abs(a)//abs(b)*(1 if a*b>=0 else -1)
            assert q.to_int()==expected and r.to_int()==a-b*expected,(p.base,a,b,q.to_int(),r.to_int())
        else:
            try:divmod_trunc(u,v)
            except ZeroDivisionError:pass
            else:raise AssertionError('zero divisor accepted')
        assert u.to_int()==a and v.to_int()==b
        if structural:p.check([u,v]+out)
    finally:
        for x in out+[u,v]:x.close()
    assert p.used==0

def small():
    count=0;stats=[]
    for base in [2,3,10,256]:
        p=Pool(base,512)
        for a in range(-24,25):
            for b in range(-24,25):
                check_pair(p,a,b,structural=(count%97==0));count+=1
        p.check([]);stats.append({'base':base,'peak_nodes':p.peak,'allocations':p.allocations,**p.stats})
    assert sum(x['add_backs'] for x in stats)>0
    return {'complete_pairs':count,'bases':[2,3,10,256],'stats':stats}

def larger():
    rng=random.Random(43134);count=0;stats=[];aliases=0
    for base in [2,3,10,256,65536,2**32]:
        p=Pool(base,4096)
        for _ in range(120):
            n=rng.randrange(1,101);m=rng.randrange(1,101)
            a=rng.randrange(base**n);b=rng.randrange(base**m)
            a*=rng.choice([-1,1]);b*=rng.choice([-1,1])
            check_pair(p,a,b,structural=True);count+=1
        for _ in range(20):
            a=rng.randrange(1,base**12)*rng.choice([-1,1]);u=Number.from_int(p,a)
            z=add(u,u);w=multiply(u,u);q,r=divmod_trunc(u,u)
            assert [x.to_int() for x in [z,w,q,r]]==[2*a,a*a,1,0]
            p.check([u,z,w,q,r])
            for x in [u,z,w,q,r]:x.close()
            aliases+=1
        p.check([]);stats.append({'base':base,'peak_nodes':p.peak,**p.stats})
    return {'random_pairs':count,'input_alias_cases':aliases,'max_operand_words':100,'stats':stats}

def allocation():
    p=Pool(256,80);live=[]
    for n in range(1,13):live.append(Number.from_int(p,256**(n%6)+n))
    for i in range(0,12,2):live[i].close()
    live=[x for x in live if x.length]
    p.check(live);free=p.capacity-p.used
    large=Number.from_int(p,256**(free-1));p.check(live+[large]);assert p.used==p.capacity
    try:Number.from_int(p,1)
    except MemoryError:pass
    else:raise AssertionError('overfull allocation succeeded')
    p.check(live+[large])
    for x in live+[large]:x.close()
    p.check([])
    failures=0
    for fn in [add,subtract,multiply,divmod_trunc]:
        q=Pool(10,20);u=Number.from_int(q,98765432);v=Number.from_int(q,12345678)
        before=q.used
        try:fn(u,v)
        except MemoryError:failures+=1
        else:raise AssertionError(('expected no space',fn.__name__))
        assert q.used==before and u.to_int()==98765432 and v.to_int()==12345678
        q.check([u,v]);u.close();v.close();q.check([])
    return {'fragmented_free_nodes_reused':free,'filled_capacity':80,
            'failed_operation_cleanup_cases':failures,'out_of_space_allocator_check':True}

if __name__=='__main__':
    for k,fn in [('small',small),('larger',larger),('allocation',allocation)]:
        if k not in data:
            t=time.monotonic();v=fn();v['elapsed_seconds']=time.monotonic()-t;save(k,v)
    print('ALL CHECKPOINTS PASSED',flush=True)

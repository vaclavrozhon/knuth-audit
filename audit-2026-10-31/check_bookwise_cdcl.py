"""Fixed local witnesses for specific printed CDCL omissions; no SAT census."""
import itertools,json
from pathlib import Path
out={}
#260: one unit, literal encoding2 for x1.
def init_unit(fixed):
    trail=[None]; val={1:-1}; F=0; l=2
    val[1]=l&1; tloc={1:F}
    if fixed: trail[F]=l
    F+=1
    return dict(trail=trail,val=val,tloc=tloc,F=F)
assert init_unit(False)['trail']==[None] and init_unit(True)['trail']==[2]
out['F215']={'printed':init_unit(False),'corrected':init_unit(True)}
#261: c=3 watches a true literal and the newly false literal; next link0.
def cursor(fixed):
    c=3;q=0;link=0;steps=[]
    for _ in range(3):
        if c==0: break
        nxt=link
        if q: link=c
        q=c
        steps.append(dict(c=c,q=q,next=nxt,link=link))
        if fixed:c=nxt
    return dict(c=c,steps=steps,terminated=c==0)
assert not cursor(False)['terminated'] and cursor(True)['terminated']
out['F216']={'printed':cursor(False),'corrected':cursor(True)}
#262: a forced variable may remain in heap; initial activities are all zero.
def bump(fixed):
    heap=[1,2];act={1:0.,2:0.};alpha=act[2];act[2]=alpha+1
    if fixed:alpha=act[2]
    if act[heap[0]]<alpha:heap=[2,1]
    return dict(heap=heap,activity=act,invariant=act[heap[0]]>=act[heap[1]])
assert not bump(False)['invariant'] and bump(True)['invariant']
out['F217']={'printed':bump(False),'corrected':bump(True)}
#265: clause(-x1 or x2 or x3), watches(-x1,x2), decisions(-x1,-x2,-x3).
out['F218']={'clause':[-1,2,3],'watches':[-1,2],'trail':[-1,-2,-3],
             'levels':[1,2,3],'false_watch_level':2,'maximum_clause_level':3,
             'reason_watch_is_retained':'Other watch -x1 is true when x2 becomes false.'}
#267: binary clauses can be represented only in BIMP.
cnf=[[1],[-2],[-1,2]]
def sat_clause(c,v):return any(v[abs(l)]==(l>0) for l in c)
assert not any(all(sat_clause(c,dict(zip([1,2],bits))) for c in cnf)
               for bits in itertools.product([False,True],repeat=2))
def propagate_binary(fixed):
    trail=[2,5];val={1:0,2:1};bimp={2:[4],5:[3]};checked=[]
    for l in trail:
        source=l if fixed else l^1;checked.append(source)
        for t in bimp.get(source,[]):
            if val[t>>1]!=(t&1):return dict(outcome='UNSAT',checked=checked)
    return dict(outcome='SAT',checked=checked)
assert propagate_binary(False)['outcome']=='SAT'
assert propagate_binary(True)['outcome']=='UNSAT'
out['F219']={'cnf_signed':cnf,'printed':propagate_binary(False),'corrected':propagate_binary(True)}
#267: unit b forced by a ternary clause; outer trigger is s, then b implies c.
f=[[-1,-2,3],[-3,4]];model={1:False,2:True,3:False,4:False}
assert all(sat_clause(c,model) for c in f) and not sat_clause([-2,4],model)
out['F220']={'cnf_signed':f,'outer_trigger':2,'binary_source':3,'forced':4,
             'printed_reason_clause':[-2,4],'correct_reason_clause':[-3,4],
             'countermodel_to_printed_reason':model}
#270: the book's own R6 example, encoded as(6,-5,-4,-1).
mem=[12,11,9,3];val={1:2,2:4,3:4,4:4,5:4,6:4};d=2;k=3
bad=next(j for j in range(k,0,-1) if val[mem[j]]>=2*d)
good=next(j for j in range(k,0,-1) if val[mem[j]>>1]>=2*d)
assert bad==3 and good==2
out['F221']={'mem_literals':mem,'values':val,'printed_index':bad,'corrected_index':good,
             'printed_watch':mem[bad],'corrected_watch':mem[good]}
#272: a reflection-invariant formula on six variables, i maps to7-i.
f=[[1,2,3],[1,2,-3],[6,5,4],[6,5,-4]]
reflection=lambda l:(1 if l>0 else -1)*(7-abs(l))
assert {frozenset(c) for c in f}=={frozenset(map(reflection,c)) for c in f}
def run_decisions(ds):
    v={};trail=[];levels={};conflict=None
    for level,l in enumerate(ds,1):
        assert abs(l) not in v
        v[abs(l)]=l>0;levels[abs(l)]=level;trail.append(l)
        while True:
            progress=False
            for c in f:
                if any(abs(t) in v and v[abs(t)]==(t>0) for t in c):continue
                free=[t for t in c if abs(t) not in v]
                if not free:return dict(trail=trail,levels=levels,conflict=c)
                if len(free)==1:
                    t=free[0];v[abs(t)]=t>0;levels[abs(t)]=level;trail.append(t);progress=True
            if not progress:break
    return dict(trail=trail,levels=levels,conflict=conflict)
a=run_decisions([-1,-2]);b=run_decisions([-6,-1,-2])
assert a['conflict']==[1,2,-3] and b['conflict']==[1,2,-3]
assert (set(a['conflict'])|set(f[0]))-{3,-3}=={1,2}
#After learning(1 or2), C8/C9 set d=d'=1. Both reflected literals are free.
out['F222']={'formula':f,'trace':a,'learned':[1,2],'reflected':[6,5],
             'backjump_trail':[-1,2],'d':1,'d_prime':1,'printed_ranks':[1,1],
             'printed_action':'C7 on a clause with two free literals',
             'correct_action':'Store and watch; no conflict or propagation.'}
#Second trace retains -6 at level1. Reflection backjumps from2 to1 and appends5.
val5=-1;appended_trail=[-6,5];correct_val5=2
assert val5<0 and correct_val5==2*1+(10&1)
out['F223']={'formula':f,'trace':b,'learned':[1,2],'reflected':[6,5],
             'ranks_before_extra_backjump':{'5':2,'6':1},'trail_after_append':appended_trail,
             'printed_VAL5':val5,'correct_VAL5':correct_val5}
Path('audit-2026-10-31/results/bookwise-cdcl-fixed-witnesses.json').write_text(json.dumps(out,indent=2)+'\n')
print('Nine fixed local witnesses checked; no full solver or general census was run.')

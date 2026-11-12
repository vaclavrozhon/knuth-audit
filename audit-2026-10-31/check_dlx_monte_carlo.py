#!/usr/bin/env python3
"""DLX86: exact path expectations, independent set costs, and literal C1--C8.

No sampling error: every possible random path is enumerated with Fraction
probabilities. The set model copies state and never uses dancing links.
"""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path
import hashlib, json, random
from colored_dlx import ColoredDLX, brute

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/minimax_mc'


class MeasuredDLX(ColoredDLX):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.updates = self.cleansings = 0

    def hide(self, p, undo=False):
        before = sum(self.T[1:self.n+1])
        super().hide(p,undo)
        if not undo:
            self.updates += before-sum(self.T[1:self.n+1])

    def cover(self, i, undo=False):
        if not undo:
            self.updates += 1  # The LLINK(r) assignment, including an empty column.
        return super().cover(i,undo)

    def purify(self, p, undo=False):
        if not undo:
            self.cleansings += 1  # commit calls purify.
            c,i = self.C[p],self.T[p]
            q = self.D[i]
            while q != i:
                self.cleansings += self.C[q]==c
                q = self.D[q]
        return super().purify(p,undo)


def set_tree(n, primary, rows, mrv):
    """Declarative remaining-row model; cover/purify costs counted combinatorially."""
    rowdict = list(map(dict,rows))

    def visit(available, pending, purified, chosen):
        node = dict(depth=len(chosen), children=[], updates4=0, theta=0, solution=not pending)
        if not pending:
            node['model'] = tuple(sorted(chosen))
            return node
        i = min(pending,key=lambda j:(sum(j in rowdict[r] for r in available),j)) if mrv else min(pending)
        choices = sorted(r for r in available if i in rowdict[r])
        node['theta'] = len(choices)

        def cover(active, item, pure):
            removed = {r for r in active if item in rowdict[r]}
            updates = 1+sum(sum(j!=item and j not in pure for j in rowdict[r]) for r in removed)
            return active-removed,updates

        left, node['updates4'] = cover(available,i,purified)
        for r in choices:
            active, remaining, pure = set(left), pending-{i}, dict(purified)
            u = c = 0
            k = next(k for k,(j,_) in enumerate(rows[r]) if j==i)
            ordered = rows[r][k+1:]+rows[r][:k]
            for j,color in ordered:
                if j in pure:
                    assert color==pure[j]
                elif color==0:
                    active, extra = cover(active,j,pure)
                    u += extra
                    remaining.discard(j)
                else:
                    containing = {s for s in active if j in rowdict[s]}
                    matching = {s for s in containing if rowdict[s][j]==color}
                    bad = containing-matching
                    c += 1+len(matching)
                    u += sum(sum(t!=j and t not in pure for t in rowdict[s]) for s in bad)
                    active -= bad
                    pure[j] = color
            node['children'].append(dict(updates5=u,cleansings5=c,
                tree=visit(active,remaining,pure,chosen+(r,))))
        return node

    return visit(set(range(len(rows))),set(range(1,primary+1)),{},())


def tree_summary(tree):
    profile, models = Counter(),set()
    update_profile, cleansing_profile = Counter(),Counter()
    updates = cleansings = 0
    paths = []

    def walk(node,path,probability):
        nonlocal updates,cleansings
        profile[node['depth']] += 1
        updates += node['updates4']
        update_profile[node['depth']] += node['updates4']
        if node['solution']:
            models.add(node['model'])
        if not node['children']:
            paths.append((path,probability))
        for k,edge in enumerate(node['children']):
            updates += edge['updates5']
            cleansings += edge['cleansings5']
            update_profile[node['depth']] += edge['updates5']
            cleansing_profile[node['depth']] += edge['cleansings5']
            walk(edge['tree'],path+(k,),probability/node['theta'])

    walk(tree,(),Fraction(1))
    assert sum(p for _,p in paths)==1
    return dict(profile=profile,models=models,updates=updates,cleansings=cleansings,paths=paths,
                update_profile=update_profile,cleansing_profile=cleansing_profile)


def snapshot_diff(a,b,n):
    # Header color fields are optional caches, deliberately not restored by ordinary C.
    return {key:[dict(address=i,before=x,after=y) for i,(x,y) in enumerate(zip(a[key],b[key]))
                 if x!=y and not (key=='C' and 1<=i<=n)]
            for key in a if any(x!=y and not (key=='C' and 1<=i<=n)
                for i,(x,y) in enumerate(zip(a[key],b[key])))}


def trial(run, path, *, mrv=True, repair_return=True, repair_weight=True, repair_dead=True):
    """Explicit step machine; choices supplied in place of uniformly random integers."""
    before = run.snapshot()
    weight,level,step,pos = 1,0,'C2',0
    nodes = {}
    profile,updates,cleansings = Counter(),Counter(),Counter()
    solutions = 0
    trace = []
    while True:
        trace.append(dict(step=step,level=level,i=locals().get('i'),weight=weight))
        assert len(trace)<1000
        if step=='C2':
            profile[level] += weight
            if run.R[0]==0:
                solutions += weight
                step='C8'
            else:
                step='C3'
        elif step=='C3':
            active=[]
            i=run.R[0]
            while i:
                assert i not in active
                active.append(i)
                i=run.R[i]
            i=min(active,key=lambda j:run.T[j]) if mrv else active[0]
            theta=run.T[i]
            step='C4' if theta or repair_dead else 'C7'
        elif step=='C4':
            u0=run.updates
            run.cover(i)
            updates4=run.updates-u0
            nodes[level]=run.D[i]
            if theta==0:
                updates[level] += weight*updates4
                step='C7'
                continue
            k=path[pos];pos+=1
            assert 0<=k<theta
            for _ in range(k): nodes[level]=run.D[nodes[level]]
            step='C5'
        elif step=='C5':
            x=nodes[level]
            assert x!=i
            u0,c0=run.updates,run.cleansings
            p=x+1
            while p!=x:
                if run.T[p]<=0: p=run.U[p]
                else: run.commit(p);p+=1
            u,c=run.updates-u0,run.cleansings-c0
            updates[level] += weight*(updates4+theta*u)
            cleansings[level] += weight*(theta if repair_weight else 1)*c
            weight*=theta
            level+=1
            step='C2'
        elif step=='C6':
            if repair_return:
                x=nodes[level]
                p=x-1
                while p!=x:
                    if run.T[p]<=0: p=run.D[p]
                    else: run.commit(p,True);p-=1
                i=run.T[x]
            step='C7'  # Literal "nothing" falls through; repair also ends here.
        elif step=='C7':
            run.cover(i,True)
            step='C8'
        else:
            assert step=='C8'
            if level==0: break
            level-=1
            step='C6'
    assert pos==len(path)
    after=run.snapshot()
    return dict(profile=profile,solutions=solutions,updates=updates,cleansings=cleansings,
                trace=trace,difference=snapshot_diff(before,after,run.n))


def exact_case(n,primary,rows,mrv=True,details=False):
    rows=tuple(tuple(r) for r in rows)
    tree=set_tree(n,primary,rows,mrv)
    full=tree_summary(tree)
    measured=MeasuredDLX(n,primary,rows).solve(mrv=mrv)
    assert measured.solutions==full['models']==brute(primary,rows)
    assert measured.profile==full['profile']
    assert measured.updates==full['updates'] and measured.cleansings==full['cleansings']
    means={k:Counter() for k in ('profile','updates','cleansings')}
    solutions=Fraction(0)
    samples=[]
    shared=MeasuredDLX(n,primary,rows)
    for path,probability in full['paths']:
        got=trial(shared,path,mrv=mrv)
        assert not got['difference'],(rows,path,got['difference'])
        for k in means:
            for depth,value in got[k].items(): means[k][depth]+=probability*value
        solutions+=probability*got['solutions']
        if details:
            printed=trial(MeasuredDLX(n,primary,rows),path,mrv=mrv,
                          repair_weight=False,repair_dead=False)
            samples.append(dict(path=path,probability=str(probability),
                repaired={k:got[k] for k in ('profile','solutions','updates','cleansings')},
                printed_costs_with_only_return_repaired={k:printed[k] for k in ('updates','cleansings')}))
    assert means['profile']==full['profile'] and solutions==len(full['models'])
    assert sum(means['updates'].values())==full['updates']
    assert sum(means['cleansings'].values())==full['cleansings']
    assert means['updates']==full['update_profile']
    assert means['cleansings']==full['cleansing_profile']
    result=dict(n=n,primary=primary,rows=rows,profile=full['profile'],solutions=len(full['models']),
                updates=full['updates'],cleansings=full['cleansings'],paths=len(full['paths']),
                update_profile=full['update_profile'],cleansing_profile=full['cleansing_profile'])
    if details: result.update(samples=samples,tree=tree)
    return result


def main():
    examples={
        'cleansing_minimal':(2,1,[((1,0),(2,1)),((1,0),(2,2))]),
        'cleansing_markers':(3,2,[((1,0),(3,1)),((1,0),(3,2)),((2,0),(3,1)),((2,0),(3,2))]),
        'dead_empty_root':(1,1,[]),
        'dead_nonempty':(3,2,[((1,0),(3,0)),((2,0),(3,0))]),
    }
    witnesses={name:exact_case(*args,details=True) for name,args in examples.items()}
    assert witnesses['cleansing_minimal']['cleansings']==2
    assert all(sum(s['printed_costs_with_only_return_repaired']['cleansings'].values())==1
               for s in witnesses['cleansing_minimal']['samples'])
    assert witnesses['dead_empty_root']['updates']==1
    assert witnesses['dead_nonempty']['updates']==5
    assert sum(witnesses['dead_nonempty']['samples'][0]['printed_costs_with_only_return_repaired']['updates'].values())==4
    bad_returns={}
    for name,args,path in [('stale_i',(2,2,[((1,0),),((2,0),)]),(0,0)),
                           ('missing_uncommit',(2,2,[((1,0),(2,0))]),(0,))]:
        run=MeasuredDLX(*args)
        initial=run.snapshot()
        bad=trial(run,path,repair_return=False)
        assert bad['difference']
        bad_returns[name]=dict(n=args[0],primary=args[1],rows=args[2],path=path,
            initial=initial,final=run.snapshot(),trial=bad,
            repaired=trial(MeasuredDLX(*args),path))
        assert not bad_returns[name]['repaired']['difference']
        if name=='stale_i':
            second=trial(run,(0,),repair_return=False)
            assert sum(bad['profile'].values())==3 and sum(second['profile'].values())==2
            bad_returns[name]['second_trial_on_corrupted_state']=second
    universe=[tuple([(i,0) for i in (1,2) if mask>>(i-1)&1]+
                    ([] if c is None else [(3,c)]))
              for mask,c in product(range(1,4),(None,0,1,2))]
    cases=[(3,2,rows) for size in range(5) for rows in combinations(universe,size)]
    rng=random.Random(860086)
    for _ in range(1000):
        p=rng.randrange(1,5);n=p+rng.randrange(4)
        rows=[]
        for __ in range(rng.randrange(10)):
            items=rng.sample(range(1,n+1),rng.randrange(1,n+1))
            if not any(i<=p for i in items):items.append(rng.randrange(1,p+1))
            rows.append(tuple((i,0 if i<=p else rng.randrange(3)) for i in items))
        cases.append((n,p,rows))
    cases.append((0,0,[]))
    digest=hashlib.sha256(); paths=0
    for args in cases:
        for mrv in (False,True):
            result=exact_case(*args,mrv=mrv)
            paths+=result['paths']
            digest.update(json.dumps([mrv,result],sort_keys=True).encode())
    data=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),matrices=len(cases),
        policies=2,runs=len(cases)*2,exact_random_paths=paths,validation_digest=digest.hexdigest(),
        witnesses=witnesses,literal_return_counterexamples=bad_returns,
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
          for p in ('check_dlx_monte_carlo.py','colored_dlx.py')})
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'monte-carlo.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k not in ('witnesses','literal_return_counterexamples','source_sha256')}))


if __name__=='__main__':main()

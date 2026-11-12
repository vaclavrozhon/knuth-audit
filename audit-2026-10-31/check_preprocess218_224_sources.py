"""New literal stack/output checks; old random suites and chain runs are read only."""
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
import json,os,time
from check_exact_preprocessing import P,solutions,reductions,compatible
from verify_f145 import verify
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent; OUT=ROOT/'results/preprocess218_224'


class Literal(P):
    """Keep the accepted data layout, but use the source stack and output loops.

    P3/P5/(103)/(105), header initialization, and F145 are corrected explicitly.
    Early abort unwinds from the current nested-loop coordinates, not a log.
    """
    def __init__(self,*args,early=False):
        super().__init__(*args); self.early=early; self.stats=Counter(); self.events=[]

    def restore_node(self,q):
        j=self.top[q];u,d=self.up[q],self.down[q]
        self.down[u]=self.up[d]=q;self.length[j]+=1

    def uncommit(self,p):
        j,c=self.top[p],self.color[p]
        for q in self.column(j,True):
            if not (c>0 and self.color[q]==c):self.unhide(q)

    def blocking(self,x):
        before=(self.up[:],self.down[:],self.length[:]); nodes=self.row(x)
        for p in nodes:self.color[self.top[p]]=x
        blocked=0; self.stats['blocking_tests']+=1
        for pos,p in enumerate(nodes):
            j,c=self.top[p],self.color[p]
            for q in self.column(j):
                if c>0 and self.color[q]==c:continue
                inner=self.row(q)
                for at,u in enumerate(inner):
                    item=self.top[u]
                    hit=item<=self.np and self.length[item]==1 and self.color[item]!=x
                    if hit and self.early:
                        # Current u has not been unlinked yet (native goto midst).
                        for v in reversed(inner[:at]):self.restore_node(v)
                        previous=self.up[q]
                        while previous!=j:
                            if not(c>0 and self.color[previous]==c):self.unhide(previous)
                            previous=self.up[previous]
                        for pp in reversed(nodes[:pos]):self.uncommit(pp)
                        assert before==(self.up,self.down,self.length)
                        self.stats['early_aborts']+=1
                        return item
                    self.unlink(u)
                    if hit:blocked=item
        for p in reversed(nodes):self.uncommit(p)
        assert before==(self.up,self.down,self.length)
        return blocked

    def delete_cycle(self,q,stop,include_start):
        # Answer222 uses while q!=p. Answer221 needs the post-test F145 fix.
        first=True
        while (first or q>stop) if include_start else q!=stop:
            first=False;j=self.top[q]
            if j<=0:q=self.up[q]
            elif j<=self.np and self.length[j]==1:
                self.collapsed=True;return
            else:self.unlink(q);q+=1

    def output(self):
        output={};printed=[]
        for i in range(1,self.n+1):
            if not self.length[i]:continue
            p=self.down[i]
            while p!=i:
                q=p-1
                while self.down[q]==q-1:q-=1
                if self.top[q]<=0:
                    q+=1;row={};skipped=0
                    while self.top[q]>=0:
                        if self.top[q]>0:row[self.top[q]]=self.color[q]
                        else:
                            skipped+=1;assert self.color[q]==0
                        q+=1
                    rid=-self.top[q];assert rid not in output
                    assert row and any(j<=self.np for j in row)
                    output[rid]=row;printed.append(rid);self.stats['output_spacers_skipped']+=skipped
                p=self.down[p]
        self.stats['output_rows']=len(printed)
        return {i for i in range(1,self.np+1) if self.length[i]},output

    def run(self):
        if any(not self.length[i] for i in range(1,self.np+1)):
            self.collapsed=True;return {1},{}
        changed=True
        while changed:
            self.rounds+=1; assert self.rounds<=20;changed=False
            for i in range(1,self.n+1):
                if not self.length[i]:continue
                self.sanity();S=self.cover(i)
                if S:
                    self.uncover(i);p=self.down[i]
                    while p!=i:
                        following=self.down[p];q=p+1
                        while q!=p:
                            j=self.top[q]
                            if j<=0:q=self.up[q]
                            elif j==S:break
                            else:q+=1
                        if q!=p:
                            self.up[p]=p+1;self.down[p]=p-1;self.top[p]=0
                            self.stats['shortened_nodes']+=1
                        else:self.delete_cycle(p+1,p,False)
                        if self.collapsed:return {1},{}
                        p=following
                    self.up[i]=self.down[i]=i;self.length[i]=0;changed=True
                else:
                    count=0
                    for x in self.column(i):
                        if self.is_first(x) and self.color[x]==0 and self.blocking(x):
                            self.top[x]=S;S=x;count+=1
                    self.stats['max_stack']=max(self.stats['max_stack'],count)
                    self.uncover(i)
                    while S>0:
                        x=S;S=self.top[x];self.top[x]=i
                        self.stats['popped_rows']+=1
                        self.delete_cycle(x,x,True);changed=True
                        if self.collapsed:return {1},{}
                self.sanity()
        return self.output()


def main():
    assert not (OUT/'source-checked.json').exists();assert os.nice(0)>=15;start=time.monotonic()
    f145=verify();save(OUT/'f145-witness.json',f145)
    # Deliberately tiny new cases target TOP overwrites, prefix/interior null
    # spacers, colored compatibility, duplicate identities, and P9 collapse.
    cases=[
      ('two_stacked',2,2,[[(1,0),(3,1),(4,1)],[(1,0),(3,1),(4,2)],[(1,0)],[(2,0),(3,2)]]),
      ('adjacent_prefix_spacers',2,3,[[(3,0),(4,0),(1,0),(5,1)],[(3,0),(4,0),(1,0),(5,2)],[(2,0)]]),
      ('interior_spacers',2,3,[[(3,0),(1,0),(4,0),(5,1)],[(3,0),(1,0),(4,0),(5,2)],[(2,0)]]),
      ('duplicate_rows',2,2,[[(1,0),(3,1),(4,1)],[(1,0),(3,1),(4,1)],[(2,0),(3,1),(4,1)]]),
      ('collapse',3,0,[[(1,0),(2,0)],[(1,0),(3,0)],[(2,0),(3,0)]]),
      ('multiple_commits',3,3,[[(1,0),(4,1),(5,1)],[(1,0)],[(2,0),(4,1),(6,1)],[(2,0),(4,2),(6,1)],[(3,0),(5,2),(6,2)],[(3,0)]])]
    checks=[]
    for name,np,ns,rows in cases:
        expected=solutions(set(range(1,np+1)),{r:dict(row) for r,row in enumerate(rows,1)})
        runs=[]
        for early in [False,True]:
            p=Literal(np,ns,rows,early=early);primary,output=p.run()
            assert solutions(primary,output)==expected,(name,early,output,expected)
            runs.append(dict(early_abort=early,primary=sorted(primary),output=output,rounds=p.rounds,collapsed=p.collapsed,stats=dict(p.stats)))
        for field in ['primary','output','rounds','collapsed']:assert runs[0][field]==runs[1][field],(name,field)
        checks.append(dict(name=name,np=np,ns=ns,rows=rows,models=sorted(expected),runs=runs))
    assert checks[0]['runs'][0]['stats']['max_stack']==2
    assert checks[1]['runs'][0]['stats']['shortened_nodes']>=4
    assert checks[2]['runs'][0]['stats']['output_spacers_skipped']>=2
    assert checks[4]['runs'][0]['collapsed']
    assert sum(q['runs'][1]['stats'].get('early_aborts',0) for q in checks)>=3
    # The (6) example: remove d and its row without a; preserve row identities.
    original={k+1:{j:0 for j in s} for k,s in enumerate(['ce','adg','bcf','adf','bg','deg'])}
    assert not any('a' in row and compatible(original[6],row) for row in original.values())
    reduced={k:{j:0 for j in row if j!='d'} for k,row in original.items() if k!=6}
    assert set(reduced[2])==set('ag') and set(reduced[4])==set('af')
    assert solutions(set('abcdefg'),original)==solutions(set('abcefg'),reduced)=={(1,4,5)}
    # The three named Langford n3 eliminations on p109.
    lang={str((i,j)):{str(i):0,'s'+str(j):0,'s'+str(j+i+1):0} for i in range(1,4) for j in range(1,6-i)}
    deletions=[]
    for key,blocked in [(str((1,4)),'s3'),(str((1,1)),'s4'),(str((2,2)),'s4')]:
        row=lang[key];assert blocked not in row
        assert not any(blocked in r and compatible(row,r) for r in lang.values())
        deletions.append(dict(option=sorted(row),blocked=blocked));del lang[key]
    # 218 and219 short semantic witnesses; identity of duplicate rows retained.
    colored={1:{'p':0,'i':1},2:{'p':0,'i':2},3:{'q':0,'i':1}}
    assert solutions({'p','q'},colored)=={(1,3)}
    assert solutions({'p','q'},{k:{j:c for j,c in r.items() if j!='i'} for k,r in colored.items()})=={(1,3),(2,3)}
    pairs={1:dict(p=0,i=0),2:dict(p=0,j=0),3:dict(q=0,i=0),4:dict(q=0,j=0)}
    assert solutions({'p','q'},pairs)=={(1,4),(2,3)}
    assert len(solutions({'p','q'},{k:{j:c for j,c in r.items() if j in 'pq'} for k,r in pairs.items()}))==4
    accepted=['random.json','chains224.json','replacement224.json','replacement224-uncolored.json','header-initialization.json','chain6.xcc','chain6.log']
    old=[ROOT/'results/exact_preprocessing'/p for p in accepted]
    random=json.loads(old[0].read_text());assert len(random)==1500 and sum(q['solutions']>0 for q in random)==1212
    chains=json.loads(old[1].read_text());assert all(q['rounds']==min(q['n'],4) for q in chains)
    for p in old[2:4]:assert all(q['rounds']==q['n'] for q in json.loads(p.read_text()))
    src=list((ROOT/'sources/preprocess218_224').glob('*.txt'))+list(OUT.glob('*.xml'))
    save(OUT/'source-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),nice=os.nice(0),
        wall_seconds=time.monotonic()-start,dependencies={p:sha(ROOT/p) for p in ['verify_f145.py','check_exact_preprocessing.py','puzzle_xcc.py']},
        source_hashes={str(p.relative_to(ROOT)):sha(p) for p in src},accepted_data_hashes={str(p.relative_to(ROOT)):sha(p) for p in old},
        literal_cases=checks,named_langford_deletions=deletions,example6_shortening_preserves_solution=True,
        old_random_suite_rerun=False,old_chain_runs_repeated=False,new_solver_searches=0,
        f145='Printed221 falsely collapses the satisfiable three-row input; post-test loop restores the exact solution.'))
    print('PASS: F145 standalone witness; 6 targeted cases in both full/early-abort modes; 1500 old inputs and224 families read only.')


if __name__=='__main__':main()

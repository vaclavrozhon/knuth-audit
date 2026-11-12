"""Literal corrected Algorithm P and answers 220--223; independent solution sets.

Header COLOR is initialized to zero here. Inputs normally put a primary first.
All solutions are sets of original row numbers, preserving duplicate rows.
"""
from pathlib import Path
from itertools import combinations
import random,json,subprocess,re

ROOT=Path(__file__).parent;OUT=ROOT/'results/exact_preprocessing';OUT.mkdir(exist_ok=True)

def compatible(a,b):
    return all(c and b[i] and c==b[i] for i,c in a.items() if i in b)

def solutions(primary,rows):
    result=set();ids=list(rows)
    for bits in range(1<<len(ids)):
        chosen=[ids[j] for j in range(len(ids)) if bits>>j&1]
        if any(sum(i in rows[r] for r in chosen)!=1 for i in primary):continue
        if all(compatible(rows[a],rows[b]) for a,b in combinations(chosen,2)):
            result.add(tuple(sorted(chosen)))
    return result

def reductions(primary,rows):
    blocked=[];forced=[]
    for r,a in rows.items():
        for p in primary-a.keys():
            if not any(p in b and compatible(a,b) for s,b in rows.items() if s!=r):
                blocked.append((r,p));break
    for p in primary:
        options=[r for r in rows.values() if p in r]
        if not options:continue
        for i in set.intersection(*(set(r) for r in options))-{p}:
            if all(r[i]==0 for r in options):forced.append((p,i))
    return blocked,forced

class P:
    def __init__(self,np,ns,rows):
        self.np=np;self.n=np+ns;self.top=list(range(self.n+1));self.up=list(range(self.n+1));self.down=self.up[:];self.color=[0]*(self.n+1);self.length=[0]*(self.n+1)
        self.rows=rows;self.original={};self.trace=[];self.rounds=0;self.collapsed=False
        def alloc(t=0,c=0):
            k=len(self.top);self.top.append(t);self.up.append(0);self.down.append(0);self.color.append(c);return k
        left=alloc()
        for rowid,row in enumerate(rows,1):
            for i,c in row:
                k=alloc(i,c);self.original[k]=rowid
                u=self.up[i];self.down[u]=k;self.up[i]=k;self.up[k]=u;self.down[k]=i;self.length[i]+=1
            self.down[left]=len(self.top)-1
            right=alloc(-rowid);self.up[right]=left+1;left=right

    def column(self,i,reverse=False):
        link=self.up if reverse else self.down;p=link[i];out=[]
        while p!=i:
            assert p not in out,('cycle',i,p,out)
            out.append(p);p=link[p]
        return out

    def row(self,x,reverse=False):
        p=x-1 if reverse else x+1;out=[]
        while p!=x:
            if self.top[p]<=0:p=self.down[p] if reverse else self.up[p]
            else:
                out.append(p);p+=-1 if reverse else 1
        return out

    def unlink(self,p):
        i=self.top[p];u=self.up[p];d=self.down[p]
        self.down[u]=d;self.up[d]=u;self.length[i]-=1
        return i

    def hide(self,x,marker=None):
        blocked=0
        for p in self.row(x):
            i=self.unlink(p)
            if i<=self.np and self.length[i]==0 and (marker is None or self.color[i]!=marker):blocked=i
        return blocked

    def unhide(self,x):
        for p in self.row(x,True):
            i=self.top[p];u=self.up[p];d=self.down[p]
            self.down[u]=self.up[d]=p;self.length[i]+=1

    def cover(self,i):
        blocked=0
        for p in self.column(i):
            if not self.color[p]:blocked=self.hide(p) or blocked
        return blocked

    def uncover(self,i):
        for p in self.column(i,True):
            if not self.color[p]:self.unhide(p)

    def is_first(self,x):
        p=x-1
        while self.down[p]==p-1:p-=1
        return self.top[p]<=0

    def blocking(self,x):
        # Answer220: mark all remaining items, then commit, then reverse.
        nodes=self.row(x)
        for p in nodes:self.color[self.top[p]]=x
        blocked=0;history=[]
        for p in nodes:
            i=self.top[p];c=self.color[p]
            for q in self.column(i):
                if c>0 and self.color[q]==c:continue
                blocked=self.hide(q,x) or blocked;history.append(q)
        for q in reversed(history):self.unhide(q)
        return blocked

    def delete(self,x,include_start):
        for p in ([x]+self.row(x) if include_start else self.row(x)):
            i=self.unlink(p)
            if i<=self.np and self.length[i]==0:self.collapsed=True

    def sanity(self):
        for i in range(1,self.n+1):
            col=self.column(i)
            assert len(col)==self.length[i],(i,col,self.length[i])
            last=i
            for p in col:
                assert self.top[p]==i and self.up[p]==last,(i,p,last)
                last=p
            assert self.up[i]==last

    def run(self):
        if any(self.length[i]==0 for i in range(1,self.np+1)):self.collapsed=True;return set([1]),{}
        change=True
        while change:
            self.rounds+=1;change=False
            for i in range(1,self.n+1):
                if not self.length[i]:continue
                self.sanity();S=self.cover(i)
                if S:
                    self.uncover(i)
                    for p in self.column(i):
                        if any(self.top[q]==S for q in self.row(p)):
                            self.up[p]=p+1;self.down[p]=p-1;self.top[p]=0
                        else:self.delete(p,False)
                    self.up[i]=self.down[i]=i;self.length[i]=0;change=True
                    self.trace.append(('force',self.rounds,S,i))
                else:
                    stack=[]
                    for x in self.column(i):
                        if self.is_first(x) and self.color[x]==0 and self.blocking(x):stack.append(x)
                    self.uncover(i)
                    for x in reversed(stack):
                        self.delete(x,True);change=True;self.trace.append(('block',self.rounds,self.original[x]))
                if self.collapsed:return set([1]),{}
            self.sanity()
        # Answer223, preserving original option numbers.
        output={}
        for i in range(1,self.n+1):
            for x in self.column(i):
                if self.is_first(x):
                    row={self.top[p]:self.color[p] for p in [x]+self.row(x)}
                    output[self.original[x]]=row
        return {i for i in range(1,self.np+1) if self.length[i]},output

def data(np,ns,rows):
    header=' '.join('p'+str(i) for i in range(1,np+1))
    if ns:header+=' | '+' '.join('p'+str(i) for i in range(np+1,np+ns+1))
    return header+'\n'+'\n'.join(' '.join('p'+str(i)+((':'+str(c)) if c else '') for i,c in row) for row in rows)+'\n'

def native(np,ns,rows):
    text=data(np,ns,rows)
    p=subprocess.run(['/tmp/knuth-dlx-pre','v15','d0'],input=text,text=True,capture_output=True,timeout=10)
    assert p.returncode==0,(p.returncode,p.stderr)
    lines=p.stdout.splitlines();header=lines[0].split();primary=set();output={};mode=True;pending=None
    for s in header:
        if s=='|':mode=False
        elif mode:primary.add(int(s[1:]))
    for line in lines[1:]:
        if line.startswith('| (from '):output[int(line[8:-1])]=pending
        elif line.strip():
            pending={}
            for token in line.split():
                a,sep,c=token.partition(':');pending[int(a[1:])]=int(c) if sep else 0
    return primary,output,p.stdout,p.stderr

def main():
    rng=random.Random(220);report=[]
    for case in range(1500):
        np=rng.randrange(1,5);ns=rng.randrange(4);rows=[]
        for _ in range(rng.randrange(1,11)):
            prim=[i for i in range(1,np+1) if rng.randrange(2)] or [rng.randrange(1,np+1)]
            sec=[(i,rng.randrange(3)) for i in range(np+1,np+ns+1) if rng.randrange(2)]
            rng.shuffle(prim);rng.shuffle(sec)
            row=[(i,0) for i in prim]+sec
            # Half retain primary-first; half allow arbitrary order.
            if case%2:rng.shuffle(row)
            rows.append(row)
        a=P(np,ns,rows);primary,output=a.run()
        bprimary,boutput,stdout,stderr=native(np,ns,rows)
        before=solutions(set(range(1,np+1)),{r:dict(row) for r,row in enumerate(rows,1)})
        after=solutions(primary,output);bafter=solutions(bprimary,boutput)
        if before!=after or before!=bafter:
            (OUT/'failure.json').write_text(json.dumps(dict(case=case,np=np,ns=ns,rows=rows,output=output,native=boutput,stderr=stderr),indent=2))
            raise AssertionError(('models',case,before,after,bafter))
        blocked,forced=reductions(primary,output)
        if case%2==0:assert not blocked and not forced,(case,rows,output,blocked,forced)
        report.append(dict(case=case,solutions=len(before),rounds=a.rounds,blocked_remaining=len(blocked),forced_remaining=len(forced),same_output=primary==bprimary and output==boutput))
    (OUT/'random.json').write_text(json.dumps(report,indent=2)+'\n')
    print('1500 inputs preserve exact original solution sets; primary-first outputs are irreducible.',flush=True)
    print('Different reduced representations:',sum(not x['same_output'] for x in report))
    chains=[]
    for n in range(2,31):
        names=[f'{x}{k}' for k in range(1,n) for x in 'pxi'];index={s:i+1 for i,s in enumerate(names)};rr=[]
        for k in range(1,n-1):
            rr.extend([[f'i{n-k}',f'p{k}',f'x{k}'],[f'i{n-k}',f'p{k}',f'x{k+1}'],[f'i{n-k}',f'x{k}'],[f'i{n-k}',f'p{k+1}']])
        rr.extend([['i1',f'p{n-1}',f'x{n-1}'],['i1',f'x{n-1}']])
        rows=[[(index[s],0) for s in row] for row in rr];a=P(len(names),0,rows);a.run()
        bp,bo,stdout,stderr=native(len(names),0,rows)
        r=int(re.search(r'(\d+) rounds',stderr).group(1))
        assert a.rounds==r==min(n,4),(n,a.rounds,r)
        chains.append(dict(n=n,rounds=r,trace=a.trace))
        if n==5:
            (OUT/'chain5.xcc').write_text(data(len(names),0,rows))
            (OUT/'chain5.log').write_text(stdout+stderr)
            (OUT/'chain5-names.json').write_text(json.dumps(dict(enumerate(names,1)),indent=2)+'\n')
    (OUT/'chains224.json').write_text(json.dumps(chains,indent=2)+'\n')
    print('Printed exercise224 gives min(n,4) rounds for n=2,...,30.')

def replacement():
    report=[]
    for n in range(2,31):
        # Items P_{n-1},...,P_0 are primary; E_0,...,E_{n-2} secondary.
        rows=[]
        for k in range(n):
            for c in ([1] if k==0 else [1,2]):
                row=[(n-k,0)]
                if k>0:row.append((n+k,c))
                if k<n-1:row.append((n+k+1,c))
                rows.append(row)
        a=P(n,n-1,rows);a.run();bp,bo,stdout,stderr=native(n,n-1,rows)
        r=int(re.search(r'(\d+) rounds',stderr).group(1))
        assert a.rounds==r==n,(n,a.rounds,r)
        report.append(dict(n=n,rounds=r,trace=a.trace))
    (OUT/'replacement224.json').write_text(json.dumps(report,indent=2)+'\n')
    print('Colored equality chain gives exactly n rounds for n=2,...,30.')

def uncolored_replacement():
    report=[]
    for n in range(2,31):
        z=2*n-2
        def edge(k,c):return z+2*(z-2-k)+1+c
        rows=[]
        for k in range(z):
            for c in ([0] if k==0 else [0,1]):
                row=[(z-k,0)]
                if k>0:row.append((edge(k-1,1-c),0))
                if k<z-1:row.append((edge(k,c),0))
                rows.append(row)
        a=P(z,2*(z-1),rows);a.run();bp,bo,stdout,stderr=native(z,2*(z-1),rows)
        r=int(re.search(r'(\d+) rounds',stderr).group(1))
        assert a.rounds==r==n,(n,a.rounds,r)
        report.append(dict(n=n,primary=z,secondary=2*(z-1),options=len(rows),rounds=r,trace=a.trace))
    (OUT/'replacement224-uncolored.json').write_text(json.dumps(report,indent=2)+'\n')
    print('Uncolored equality chain gives exactly n rounds for n=2,...,30.')

def small_examples():
    rows=[[(1,0),(3,1)],[(1,0)],[(2,0),(3,2)]]
    outputs=[]
    for initial in [0,5]:
        a=P(2,1,rows);a.color[2]=initial;primary,reduced=a.run()
        outputs.append(dict(initial_COLOR_b=initial,first_row_node=5,output=reduced,remaining=reductions(primary,reduced),trace=a.trace))
    (OUT/'header-initialization.json').write_text(json.dumps(outputs,indent=2)+'\n')
    rows[0].reverse()
    p,r,out,log=native(2,1,rows)
    (OUT/'colored-first.xcc').write_text(data(2,1,rows));(OUT/'colored-first.log').write_text(out+log)
    # Human-readable n=6 instance and author log, retaining the book's names.
    n=6;names=[f'{x}{k}' for k in range(1,n) for x in 'pxi'];rr=[]
    for k in range(1,n-1):
        rr.extend([[f'i{n-k}',f'p{k}',f'x{k}'],[f'i{n-k}',f'p{k}',f'x{k+1}'],[f'i{n-k}',f'x{k}'],[f'i{n-k}',f'p{k+1}']])
    rr.extend([['i1',f'p{n-1}',f'x{n-1}'],['i1',f'x{n-1}']])
    text=' '.join(names)+'\n'+'\n'.join(' '.join(row) for row in rr)+'\n'
    result=subprocess.run(['/tmp/knuth-dlx-pre','v15','d0'],input=text,text=True,capture_output=True,timeout=10)
    (OUT/'chain6.xcc').write_text(text);(OUT/'chain6.log').write_text(result.stdout+result.stderr)

if __name__=='__main__':
    main()
    replacement()
    uncolored_replacement()
    small_examples()


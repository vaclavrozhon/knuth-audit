"""Literal spacer layout and steps X1–X8, for DLX6–13 auditing.

This is separate from algorithm_x.py, which uses explicit horizontal row
links. Assertions check every undo, every residual problem, and row output.
Primary items precede secondary items; every option has a primary item.
"""
from collections import Counter


class SpacerX:
    def __init__(self, names, rows, primary=None):
        self.names=['—']+list(names)
        assert len(set(names))==len(names)
        self.N=len(names)
        if primary is None:primary=self.N
        assert 0<=primary<=self.N
        self.rows=[tuple(row) for row in rows]
        for row in rows:
            assert len(set(row))==len(row) and all(1<=i<=self.N for i in row)
            assert any(i<=primary for i in row)
        self.L=[0]*(self.N+2);self.R=[0]*(self.N+2)
        # I1–I2, including the separate secondary-list head N+1.
        n1=-1
        for i in range(1,self.N+1):
            self.L[i]=i-1;self.R[i-1]=i
            if i==primary+1:n1=i-1
        if n1<0:n1=self.N
        assert n1==primary
        self.primary=n1
        self.L[self.N+1]=self.N;self.R[self.N]=self.N+1
        self.L[n1+1]=self.N+1;self.R[self.N+1]=n1+1
        self.L[0]=n1;self.R[n1]=0
        # I3; T is the shared TOP/LEN field. Index zero is unused.
        self.T=[None]+[0]*self.N+[0]
        self.U=[None]+list(range(1,self.N+1))+[None]
        self.D=[None]+list(range(1,self.N+1))+[None]
        p=self.N+1
        for m,row in enumerate(rows,1):
            k=len(row)
            self.T.extend([None]*(k+1));self.U.extend([None]*(k+1));self.D.extend([None]*(k+1))
            for j,i in enumerate(row,1):
                self.T[i]+=1;q=self.U[i]
                self.U[p+j]=q;self.D[q]=p+j;self.D[p+j]=i
                self.U[i]=p+j;self.T[p+j]=i
            self.D[p]=p+k;p+=k+1;self.T[p]=-m;self.U[p]=p-k
        self.M=len(rows);self.Z=p
        assert self.Z==self.N+self.M+sum(map(len,rows))+1
        self.undo=[]
        self.checks=Counter()

    def snapshot(self):
        return tuple(tuple(v) for v in (self.L,self.R,self.T,self.U,self.D))

    def cover(self,i):
        self.undo.append((i,self.snapshot()))
        p=self.D[i]
        while p!=i:
            q=p+1
            while q!=p:
                x,u,d=self.T[q],self.U[q],self.D[q]
                if x<=0:q=u
                else:
                    self.D[u]=d;self.U[d]=u;self.T[x]-=1;q+=1
            p=self.D[p]
        l,r=self.L[i],self.R[i];self.R[l]=r;self.L[r]=l

    def uncover(self,i):
        l,r=self.L[i],self.R[i];self.R[l]=i;self.L[r]=i
        p=self.U[i]
        while p!=i:
            q=p-1
            while q!=p:
                x,u,d=self.T[q],self.U[q],self.D[q]
                if x<=0:q=d
                else:
                    self.D[u]=q;self.U[d]=q;self.T[x]+=1;q-=1
            p=self.U[p]
        previous_i,previous=self.undo.pop()
        assert previous_i==i and self.snapshot()==previous
        self.checks['exact_cover_uncover_restorations']+=1

    def row_of(self,x):
        r=x
        while self.T[r]>=0:r+=1
        return -self.T[r]-1,self.U[r]

    def column(self,i):
        out=[];q=self.D[i]
        while q!=i:
            assert q not in out and self.T[q]==i
            assert self.D[self.U[q]]==q and self.U[self.D[q]]==q
            out.append(q);q=self.D[q]
        assert len(out)==self.T[i]
        return out

    def describe(self,x,colors=None):
        # Answer12, including the not-in-list case.
        if x<=self.N or x>self.Z or self.T[x]<=0:return None
        q=x;parts=[]
        while True:
            part=self.names[self.T[q]]
            if colors is not None and colors[q]!=0:
                c=colors[q] if colors[q]>0 else colors[self.T[q]]
                part+=':'+str(c)
            parts.append(part);q+=1
            if self.T[q]<=0:q=self.U[q]
            if q==x:break
        i=self.T[x];q=self.D[i];k=1
        while q!=x and q!=i:q=self.D[q];k+=1
        return parts,(k,self.T[i]) if q!=i else None

    def validate_state(self,chosen):
        row_indices=[self.row_of(x)[0] for x in chosen]
        counts=Counter(i for r in row_indices for i in self.rows[r])
        assert max(counts.values(),default=0)<=1
        used=set(counts)
        actual=[];i=self.R[0]
        while i:
            assert i not in actual and self.R[self.L[i]]==i
            actual.append(i);i=self.R[i]
        assert actual==[i for i in range(1,self.primary+1) if i not in used]
        for i in range(1,self.N+1):
            if i not in used:
                expected=[r for r,row in enumerate(self.rows) if i in row and not used.intersection(row)]
                assert [self.row_of(x)[0] for x in self.column(i)]==expected
                self.checks['residual_columns']+=1
        for x in range(self.N+1,self.Z+1):
            if self.T[x]<=0:
                assert self.describe(x) is None
                continue
            parts,position=self.describe(x)
            r,start=self.row_of(x)
            offset=x-start;row=self.rows[r]
            assert parts==[self.names[i] for i in row[offset:]+row[:offset]]
            col=self.column(self.T[x])
            assert position==((col.index(x)+1,len(col)) if x in col else None)
            self.checks['row_descriptions']+=1
        self.checks['X2_states']+=1

    def choose(self,policy):
        p=self.R[0]
        if policy=='first':return p
        theta=float('inf');i=None;active=[]
        while p:
            active.append(p);score=self.T[p]
            if policy=='sharp' and score>1 and not self.names[p].startswith('#'):
                score+=self.M
            if score<theta:theta=score;i=p
            p=self.R[p]
        if policy=='mrv':expected=min(active,key=lambda p:(self.T[p],p))
        else:expected=min(active,key=lambda p:(self.T[p]>1 and not self.names[p].startswith('#'),self.T[p],p))
        assert i==expected
        self.checks['branch_priority_checks']+=1
        return i

    def solve(self,policy='mrv',observer=None):
        assert policy in ('mrv','first','sharp')
        original=self.snapshot();self.solutions=set();self.profile=Counter()
        x=[None]*(self.primary+1);level=0;step=2
        while True:
            if step==2:
                self.profile[level]+=1;self.validate_state(x[:level])
                if self.R[0]==0:
                    solution=tuple(sorted(self.row_of(q)[0] for q in x[:level]))
                    assert solution not in self.solutions
                    self.solutions.add(solution);step=8
                else:step=3
            elif step==3:i=self.choose(policy);step=4
            elif step==4:self.cover(i);x[level]=self.D[i];step=5
            elif step==5:
                if x[level]==i:step=7
                else:
                    p=x[level]+1
                    while p!=x[level]:
                        j=self.T[p]
                        if j<=0:p=self.U[p]
                        else:self.cover(j);p+=1
                    level+=1;step=2
            elif step==6:
                p=x[level]-1
                while p!=x[level]:
                    j=self.T[p]
                    if j<=0:p=self.D[p]
                    else:self.uncover(j);p-=1
                i=self.T[x[level]];x[level]=self.D[x[level]];step=5
            elif step==7:
                if observer is not None:observer(self,level,i,x[:level])
                self.uncover(i);step=8
            elif step==8:
                if level==0:break
                level-=1;step=6
        assert self.snapshot()==original and not self.undo
        return self

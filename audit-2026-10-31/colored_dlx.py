"""Literal spacer representation of TAOCP 4B Algorithm C, pp. 68--69, 90.

Independent audit interpreter, not a replacement for the author's DLX2.
Item numbers are 1-based; an option is a tuple of (item, color), color 0
meaning an uncolored occurrence. Positive colors are explicit secondary colors.
"""
from collections import Counter
from itertools import combinations


class ColoredDLX:
    def __init__(self, n, primary, rows, *, colored=True, secondary_lengths=True):
        self.n, self.primary = n, primary
        self.rows = tuple(tuple(row) for row in rows)
        self.colored, self.secondary_lengths = colored, secondary_lengths
        self.L, self.R = list(range(n+2)), list(range(n+2))
        for cycle in ([0]+list(range(1,primary+1)),
                      [n+1]+list(range(primary+1,n+1))):
            for k,i in enumerate(cycle):
                self.L[i], self.R[i] = cycle[k-1], cycle[(k+1)%len(cycle)]
        self.T = [None]+[0]*n+[0]
        self.U = [None]+list(range(1,n+1))+[None]
        self.D = [None]+list(range(1,n+1))+[None]
        self.C = [None]*(n+1)+[0]
        self.owner, self.ends = {}, {}
        spacer = n+1
        for ri,row in enumerate(self.rows):
            assert any(i<=primary for i,c in row)
            assert len(set(i for i,c in row))==len(row)
            assert all(1<=i<=n and c>=0 and (i>primary or c==0) for i,c in row)
            first = len(self.T)
            for i,c in row:
                q = len(self.T)
                self.T.append(i); self.U.append(self.U[i]); self.D.append(i); self.C.append(c)
                self.D[self.U[i]] = q; self.U[i] = q; self.T[i] += 1
                self.owner[q] = ri
            last = len(self.T)-1
            self.D[spacer] = last
            spacer = len(self.T)
            self.T.append(-ri-1); self.U.append(first); self.D.append(None); self.C.append(0)
            for q in range(first,last+1):
                self.ends[q] = last
        self.events = []

    def snapshot(self):
        return {name:list(getattr(self,name)) for name in ('L','R','T','U','D','C')}

    def hide(self,p,undo=False):
        step = -1 if undo else 1
        q = p+step
        while q!=p:
            if self.colored and self.C[q]<0:
                q += step
                continue
            x,u,d = self.T[q],self.U[q],self.D[q]
            if x<=0:
                q = d if undo else u
            else:
                self.D[u],self.U[d] = (q,q) if undo else (d,u)
                if self.secondary_lengths or x<=self.primary:
                    self.T[x] += 1 if undo else -1
                q += step

    def cover(self,i,undo=False):
        self.events.append(('uncover' if undo else 'cover',i))
        l,r = self.L[i],self.R[i]
        if undo:
            self.R[l],self.L[r] = i,i
        p = self.U[i] if undo else self.D[i]
        while p!=i:
            self.hide(p,undo)
            p = self.U[p] if undo else self.D[p]
        if not undo:
            self.R[l],self.L[r] = r,l

    def purify(self,p,undo=False):
        self.events.append(('unpurify' if undo else 'purify',p))
        c,i = self.C[p],self.T[p]
        if not undo:
            self.C[i] = c
        q = self.U[i] if undo else self.D[i]
        while q!=i:
            if (self.C[q]<0) if undo else (self.C[q]==c):
                self.C[q] = c if undo else -1
            else:
                self.hide(q,undo)
            q = self.U[q] if undo else self.D[q]

    def commit(self,p,undo=False):
        if not self.colored or self.C[p]==0:
            self.cover(self.T[p],undo)
        elif self.C[p]>0:
            self.purify(p,undo)

    def solve(self, *, mrv=True, root=None, prefix83=False):
        before = self.snapshot()
        self.solutions, self.first, self.profile = set(), None, Counter()
        chosen = []
        def visit(depth):
            self.profile[depth] += 1
            if self.R[0]==0:
                model = tuple(sorted(self.owner[q] for q in chosen))
                assert model not in self.solutions
                self.solutions.add(model)
                if self.first is None:
                    self.first = dict(nodes=list(chosen),model=model,memory=self.snapshot(),events=list(self.events))
                return
            active=[]; i=self.R[0]
            while i:
                active.append(i); i=self.R[i]
            i = root if root is not None and depth==0 else (min(active,key=lambda x:self.T[x]) if mrv else active[0])
            assert i in active
            self.events.append(('choose',depth,i))
            self.cover(i)
            x = self.D[i]
            while x!=i:
                self.events.append(('try',depth,x))
                p = x+1
                while p!=x:
                    if self.T[p]<=0: p=self.U[p]
                    else: self.commit(p); p+=1
                chosen.append(x); visit(depth+1); chosen.pop()
                p = x-1
                while p!=x:
                    if self.T[p]<=0: p=self.D[p]
                    else: self.commit(p,True); p-=1
                if prefix83 and depth==0:
                    tail=self.ends[x]; j=self.T[tail]
                    if j>self.primary and self.C[tail]==0:
                        self.cover(j)
                x = self.D[x]
            self.cover(i,True)
        visit(0)
        if not prefix83:
            after=self.snapshot()
            # Header colors are printout caches, never reset by unpurify.
            before['C'][1:self.n+1]=after['C'][1:self.n+1]
            assert before==after
        return self


def brute(primary,rows):
    """Every subset, with explicit occurrence-unique colors for uncolored items."""
    result=set()
    for size in range(len(rows)+1):
        for chosen in combinations(range(len(rows)),size):
            counts=Counter(); colors={}; valid=True
            for ri in chosen:
                for i,c in rows[ri]:
                    if i<=primary: counts[i]+=1
                    else:
                        value=('explicit',c) if c else ('unique',ri)
                        if i in colors and colors[i]!=value: valid=False
                        colors[i]=value
            if valid and counts==Counter(range(1,primary+1)):
                result.add(chosen)
    return result

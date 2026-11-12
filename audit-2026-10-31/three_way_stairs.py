"""Literal XCC and independent physical geometry for DLX92--93."""
from collections import defaultdict
from functools import lru_cache
import time

TWO_WAY={
2:'SPEND SPIES',3:'WAVES LINED LEPER',4:'LOOPS POUTS TROTS TOONS',
5:'SPOOL STROP STAID SNORT SNOOT',6:'DIMES MULES RIPER SIRED AIDED FINED',
7:'MILES LINTS CARES LAMED PIPED SANER LIVER',
8:'SUPER ROVED TILED LICIT CODED ROPED TIMED DOMED',
9:'FORTH LURES MIRES POLLS SLATS SPOTS SOAPS PLOTS LOOTS',
10:'TIMES FUROR RUNES MIMED CAPED PACED LAVER FINES LIMED MIRES'}
DIAGONAL={
3:'MILES GALLS BULLS',4:'FIRES PONDS WALKS LOCKS',5:'LIVES FIRED DIKES WAVED TIRES',
6:'BIRDS MARKS POLES WAVES WINES FONTS',7:'LIKED WARES MINES WINDS MALES LOVES FIVES',
8:'WAXES SITES MINED BOXES CAVES TALES WIRED MALES',
9:'CENTS HOLDS BOILS BALLS MALES WINES FINDS LORDS CARES',
10:'LOOKS ROADS BEATS BEADS HOLDS COOLS FOLKS WINES GASES BOLTS'}


def physical_cells(n,p,kind):
    slots=[[(i,j) for j in range(n)] for i in range(p)]
    slots += [[((i+j)%p,j) for j in range(n)] for i in range(p)]
    if kind=='two-way':
        slots += [[((i+j)%p,n-1-j) for j in range(n)] for i in range(p)]
    elif kind=='diagonal':
        slots += [[((i-j)%p,j) for j in range(n)] for i in range(p)]
    else:raise ValueError(kind)
    return slots


def all_words(rows,kind):
    return [''.join(rows[i][j] for i,j in slot) for slot in physical_cells(len(rows[0]),len(rows),kind)]


def validate(rows,words,kind):
    rank={w:i+1 for i,w in enumerate(words)};formed=all_words(rows,kind)
    assert len(set(formed))==3*len(rows),(kind,rows,formed)
    assert all(w in rank for w in formed),(kind,rows,formed)
    return max(rank[w] for w in formed)


def encoding(words,p,kind,printed92=False):
    """Transcribe 92 directly; fix only +j to -j in the di row if requested."""
    n=len(words[0]);primary=[f'{group}{i}' for group in 'abd' for i in range(p)]
    names=primary+[f'{i}.{j}' for i in range(p) for j in range(n)]+list(words)+[w+'@' for w in words]
    number={s:i+1 for i,s in enumerate(names)};rows=[];info=[]
    for rank,w in enumerate(words):
        for slot in range(3*p):
            i=slot%p;family=slot//p;row=[(slot+1,0)]
            for j in range(n):
                if family==0:r=i;c=w[j]
                elif family==1:r=(i+j)%p;c=w[j]
                elif kind=='two-way':r=(i+j if printed92 else i-j)%p;c=w[n-1-j]
                else:r=(i-j)%p;c=w[j]
                row.append((number[f'{r}.{j}'],ord(c)))
            row.append((number[w],0))
            if family==0:row.append((number[w+'@'],0))
            rows.append(tuple(row));info.append((slot,rank))
    return dict(names=names,primary=3*p,rows=rows,info=info,words=words)


class IncompleteSearch(Exception):pass


class ThreeWayCSP:
    """Word domains and actual physical crossings; no XCC options or links."""
    def __init__(self,words,p,kind,symmetry=True):
        self.words,self.p,self.kind=words,p,kind
        self.n=len(words[0]);self.nvars=3*p;self.symmetry=symmetry
        self.full=(1<<len(words))-1
        alphabet=sorted(set(''.join(words)))
        self.masks=[]
        for j in range(self.n):
            values={c:0 for c in alphabet}
            for rank,w in enumerate(words):values[w[j]]|=1<<rank
            self.masks.append(tuple(values[c] for c in alphabet))
        incidence=defaultdict(list);self.neighbors=[[] for _ in range(self.nvars)]
        for v,slot in enumerate(physical_cells(self.n,p,kind)):
            for j,cell in enumerate(slot):incidence[cell].append((v,j))
        for entries in incidence.values():
            for v,j in entries:
                for u,k in entries:
                    if u!=v:self.neighbors[v].append((u,j,k))

    def solve(self,first=False,timeout=None):
        start=time.monotonic();deadline=start+timeout if timeout else float('inf')
        self.nodes=self.failures=0;self.solutions=[]
        @lru_cache(maxsize=100000)
        def support(domain,j,k):
            out=0
            for a,b in zip(self.masks[j],self.masks[k]):
                if domain&a:out|=b
            return out
        def propagate(domains):
            queue=list(range(self.nvars));queued=set(queue)
            def narrow(v,d):
                if not d:return False
                if domains[v]!=d:
                    domains[v]=d
                    if v not in queued:queue.append(v);queued.add(v)
                return True
            while queue:
                if time.monotonic()>=deadline:raise IncompleteSearch('timeout, not UNSAT')
                v=queue.pop();queued.remove(v);d=domains[v]
                if not d&(d-1):
                    for u in range(self.nvars):
                        if u!=v and not narrow(u,domains[u]&~d):return False
                for u,j,k in self.neighbors[v]:
                    if not narrow(u,domains[u]&support(d,j,k)):return False
                if self.symmetry:
                    for u in range(1,self.p):
                        minimum=(domains[0]&-domains[0]).bit_length()-1
                        if not narrow(u,domains[u]&~((1<<(minimum+1))-1)):return False
                        maximum=domains[u].bit_length()-1
                        if not narrow(0,domains[0]&((1<<maximum)-1)):return False
            return True
        def visit(domains):
            self.nodes+=1
            if not propagate(domains):self.failures+=1;return False
            choice=[(d.bit_count(),v) for v,d in enumerate(domains) if d&(d-1)]
            if not choice:
                ranks=[d.bit_length()-1 for d in domains]
                assert len(set(ranks))==self.nvars
                rows=tuple(self.words[r] for r in ranks[:self.p]);validate(list(rows),self.words,self.kind)
                self.solutions.append(rows);return first
            _,v=min(choice);rest=domains[v]
            while rest:
                bit=rest&-rest;rest-=bit;child=domains.copy();child[v]=bit
                if visit(child):return True
            return False
        try:visit([self.full]*self.nvars)
        finally:
            self.seconds=time.monotonic()-start;self.cache=support.cache_info()._asdict();support.cache_clear()
        return self.solutions

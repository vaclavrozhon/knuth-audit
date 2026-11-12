"""Kernel projection and directed graph for answer91, independently by joins."""
from collections import defaultdict, deque
from functools import lru_cache

# Positive c1..c14; negative x1..x12. Across words reflect for left stairs.
PATTERNS = [(-3,-4,-5,2,3),(4,5,6,7,8),(9,10,11,12,-6),
            (13,14,-7,-8,-9),(-1,-2,-5,5,9),(1,2,6,10,13),
            (3,7,11,14,-10),(8,12,-7,-11,-12)]
SOURCE = (0,1,2,3,4,5,6,8,9)
TARGET = (2,6,7,8,9,10,11,12,13)


def kernel_set(words, kind):
    across = words if kind == 'right' else [w[::-1] for w in words]
    down = words
    amiddle, dmiddle = defaultdict(list), defaultdict(list)
    aprefix, dprefix = defaultdict(set), defaultdict(set)
    athird, dthird = defaultdict(set), defaultdict(set)
    for word in across:
        amiddle[word[2]].append(word)
        aprefix[word[:2]].add(word[2:4])
        athird[word[:2]].add(word[2])
    for word in down:
        dmiddle[word[2]].append(word)
        dprefix[word[:3]].add(word[3])
        dthird[word[:2]].add(word[2])
    upper = defaultdict(set)
    for c, rows in amiddle.items():
        for a in rows:
            for d in dmiddle[c]:
                upper[a[3]+d[3]].add((a[4],d[4]))
    kernels = set()
    for c, rows in amiddle.items():
        for a in rows:
            for d in dmiddle[c]:
                for c3,c9 in upper[d[1]+a[1]]:
                    for c11,c12 in aprefix[c9+d[3]]:
                        for c14 in dprefix[c3+a[3]+c11]:
                            if athird[d[4]+c14] & dthird[a[4]+c12]:
                                k=d[:2]+c3+a+c9+d[3]+c11+c12+d[4]+c14
                                assert len(k)==14
                                kernels.add(k)
    return kernels


def edge(kernel, kind):
    s=''.join(kernel[i] for i in SOURCE)
    t=''.join(kernel[i] for i in TARGET)
    a=kernel[3:8]
    if kind=='left':a=a[::-1]
    d=''.join(kernel[i] for i in (0,1,5,9,12))
    return s,t,a,d


def graph(kernels, kind):
    edges=[edge(k,kind) for k in sorted(kernels)]
    assert len({(s,t) for s,t,_,_ in edges})==len(edges)
    return edges


class DistinctWitness:
    """Complete 8-word feasibility for a fixed kernel, by disjoint word masks.

    Four groups remain after the two central words are fixed: the coupled
    upper pair, the coupled lower pair, and two single words with four fixed
    letters. Shared x5/x7 are respected inside pairs; all other x's are private.
    """
    def __init__(self, words, kind):
        self.words, self.kind = list(words), kind
        self.number = {w:i for i,w in enumerate(words)}
        self.aprefix, self.dprefix = defaultdict(list), defaultdict(list)
        self.apre2, self.dpre2 = defaultdict(list), defaultdict(list)
        self.asuffix, self.dsuffix = defaultdict(list), defaultdict(list)
        for i,w in enumerate(words):
            a=w if kind=='right' else w[::-1]
            self.aprefix[a[:4]].append(i);self.dprefix[w[:4]].append(i)
            self.apre2[a[:2]].append((i,a[2]));self.dpre2[w[:2]].append((i,w[2]))
            self.asuffix[a[3:]].append((i,a[2]));self.dsuffix[w[3:]].append((i,w[2]))

    @lru_cache(maxsize=None)
    def pairs(self, top, a, d):
        aa,dd=(self.asuffix,self.dsuffix) if top else (self.apre2,self.dpre2)
        return tuple(((1<<i)|(1<<j),i,j) for i,x in aa[a] for j,y in dd[d] if i!=j and x==y)

    def witness(self,k):
        _,_,a,d=edge(k,self.kind)
        if a==d:return None
        ia,id_=self.number[a],self.number[d]
        used=(1<<ia)|(1<<id_)
        groups=[(0,self.pairs(True,k[1:3],k[4]+k[8])),
                (3,self.pairs(False,k[12:14],k[7]+k[11])),
                (2,tuple((1<<i,i) for i in self.aprefix[k[8:12]])),
                (6,tuple((1<<i,i) for i in self.dprefix[k[2]+k[6]+k[10]+k[13]]))]
        groups=[(g,[v for v in values if not v[0]&used]) for g,values in groups]
        if any(not values for _,values in groups):return None
        groups.sort(key=lambda v:len(v[1]))
        selected={1:(ia,),5:(id_,)}
        def visit(j,mask):
            if j==4:return True
            g,values=groups[j]
            for v in values:
                if not mask&v[0]:
                    selected[g]=v[1:]
                    if visit(j+1,mask|v[0]):return True
            return False
        if not visit(0,used):return None
        ids=[selected[0][0],ia,selected[2][0],selected[3][0],selected[0][1],id_,selected[6][0],selected[3][1]]
        assert len(set(ids))==8
        return tuple(self.words[i] for i in ids)


def literal_encoding(words,kind,distinct):
    """Directly transcribed eight printed word patterns, independent of join."""
    names=[f'p{i}' for i in range(8)]+[f'c{i}' for i in range(1,15)]+[f'x{i}' for i in range(1,13)]
    if distinct:names+=list(words)
    number={name:i+1 for i,name in enumerate(names)}
    rows=[];info=[]
    for slot,pattern in enumerate(PATTERNS):
        for rank,w in enumerate(words):
            oriented=w[::-1] if kind=='left' and slot<4 else w
            row=[(slot+1,0)]
            row += [(number[f'c{v}' if v>0 else f'x{-v}'],ord(c)) for v,c in zip(pattern,oriented)]
            if distinct:row.append((number[w],0))
            rows.append(tuple(row));info.append((slot,rank))
    return dict(names=names,primary=8,rows=rows,info=info,words=words)


def validate_completion(words8,kind,distinct=False):
    """Replay all 26 letter variables and return the 14 printed c's."""
    assert len(words8)==8
    if distinct:assert len(set(words8))==8
    letters={}
    for i,(w,pattern) in enumerate(zip(words8,PATTERNS)):
        oriented=w[::-1] if kind=='left' and i<4 else w
        for var,c in zip(pattern,oriented):
            assert letters.get(var,c)==c,(words8,var)
            letters[var]=c
    return ''.join(letters[i] for i in range(1,15))


def core(edges):
    """Largest induced subgraph with strictly positive in/out degrees."""
    incoming,outgoing=defaultdict(set),defaultdict(set)
    for i,(s,t,*_) in enumerate(edges):
        outgoing[s].add(i);incoming[t].add(i)
    vertices=set(incoming)|set(outgoing)
    queue=deque(v for v in vertices if not incoming[v] or not outgoing[v])
    active=set(range(len(edges)))
    while queue:
        v=queue.popleft()
        if v not in vertices:continue
        vertices.remove(v)
        for i in list(incoming[v]|outgoing[v]):
            if i not in active:continue
            active.remove(i);s,t,*_=edges[i]
            outgoing[s].remove(i);incoming[t].remove(i)
            for u in (s,t):
                if u in vertices and (not incoming[u] or not outgoing[u]):queue.append(u)
    return [edges[i] for i in sorted(active)]


def components(edges):
    """Iterative Kosaraju; return vertex sets in decreasing size."""
    adj,rev=defaultdict(list),defaultdict(list)
    for s,t,*_ in edges:adj[s].append(t);rev[t].append(s)
    seen=set();order=[]
    for start in sorted(set(adj)|set(rev)):
        if start in seen:continue
        stack=[(start,False)]
        while stack:
            v,done=stack.pop()
            if done:order.append(v);continue
            if v in seen:continue
            seen.add(v);stack.append((v,True))
            stack.extend((w,False) for w in reversed(adj[v]) if w not in seen)
    seen=set();parts=[]
    for start in reversed(order):
        if start in seen:continue
        part=set();stack=[start];seen.add(start)
        while stack:
            v=stack.pop();part.add(v)
            for w in rev[v]:
                if w not in seen:seen.add(w);stack.append(w)
        parts.append(part)
    return sorted(parts,key=lambda s:(-len(s),min(s)))


def stair_kernels(rows,kind):
    """Physical sliding window, independent of the eight-word join loops."""
    a=list(rows) if kind=='right' else [w[::-1] for w in rows]
    p=len(a)
    return [a[(t-2)%p][4]+a[(t-1)%p][3:]+a[t]+a[(t+1)%p][:4]+a[(t+2)%p][:2] for t in range(p)]


LEFT36='SHARE SPENT SPEED WHEAT THANK CHILD SHELL SHORE STORE STOOD CHART GLORY FLOWS CLASS NOISE GAMES TIMES MOVES BONES WAVES GASES FIXED TIRED FEELS WALLS WORLD ROOMS WORDS DOORS PARTY WANTS WHICH WHERE SHOES STILL STATE'.split()
RIGHT5='YEARS STEAM SALES MARKS DRIED'.split()

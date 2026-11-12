"""Independent finite checks supplementing the structural proofs in PROOFS.md.

Ordered tree: (label, tuple(children)); forest: tuple(trees).
Binary tree: None or (label, left, right). Labels in generated trees are unique.
"""
import sys
sys.dont_write_bytecode=True
from functools import lru_cache,cmp_to_key
from itertools import permutations,combinations,product
from pathlib import Path
import json,random
HERE=Path(__file__).resolve().parent

@lru_cache(None)
def shapes(n):
    if not n:return (None,)
    return tuple((a,b) for k in range(n) for a in shapes(k) for b in shapes(n-1-k))
def label(s):
    ids=iter(range(1,10000))
    def f(s):return None if s is None else (next(ids),f(s[0]),f(s[1]))
    return f(s)
def forest(b):return () if b is None else ((b[0],forest(b[1])),)+forest(b[2])
def binary(f):return None if not f else (f[0][0],binary(f[0][1]),binary(f[1:]))
def alternative(f):return None if not f else (f[-1][0],alternative(f[:-1]),alternative(f[-1][1]))
def bp(b,order):
    if b is None:return []
    v,l,r=b;a=bp(l,order);c=bp(r,order)
    return [v]+a+c if order=='pre' else a+[v]+c if order=='in' else a+c+[v]
def fp(f,order):
    out=[]
    for v,c in f:
        if order=='pre':out.append(v)
        out+=fp(c,order)
        if order=='post':out.append(v)
    return out
def nodes(f,prefix=()):
    for i,(v,c) in enumerate(f,1):
        path=prefix+(i,)
        yield v,c,path
        yield from nodes(c,path)
def degree_decode(seq):
    pos=0
    def one():
        nonlocal pos
        assert pos<len(seq)
        v,d=seq[pos];pos+=1
        return (v,tuple(one() for _ in range(d)))
    f=[]
    while pos<len(seq):f.append(one())
    return tuple(f)
def dc_compare(x,y):
    k=0
    while k<min(len(x),len(y)) and x[k]==y[k]:k+=1
    if k==min(len(x),len(y)):return (len(y)>len(x))-(len(y)<len(x))
    return (x[k]>y[k])-(x[k]<y[k])
def parent_splice(parent):
    n=len(parent)-1;l=list(range(n+1));r=l.copy();root=0
    for j in range(n,0,-1):
        k=parent[j]
        if not k:root=j;continue
        a=r[k];i=l[j];l[j]=k;r[k]=j;l[a]=i;r[i]=a
    return root,l,r
def parent_oracle(parent):
    def walk(v):return [v]+[z for w in range(1,len(parent)) if parent[w]==v for z in walk(w)]
    root=parent.index(0,1);return walk(root)
def embedded(t,u):
    a=fp((t,),'pre');ap=fp((t,),'post');b=fp((u,),'pre');bp_=fp((u,),'post');rank={x:i for i,x in enumerate(bp_)}
    for selected in combinations(b,len(a)):
        f=dict(zip(a,selected))
        if all(rank[f[x]]<rank[f[y]] for x,y in zip(ap,ap[1:])):return True
    return False
def sufficient(t,u):
    if not t[1]:return True
    if not u[1]:return False
    lt=t[1][0];rt=(t[0],t[1][1:]);lu=u[1][0];ru=(u[0],u[1][1:])
    return embedded(t,lu) or embedded(t,ru) or (embedded(lt,lu) and embedded(rt,ru))

def validate():
    result={'forests':0,'ordered_pairs_ancestry':0,'parent_arrays':0,'embedding_pairs':0}
    degree_shapes={}
    for n in range(9):
        for s in shapes(n):
            b=label(s);f=forest(b);assert binary(f)==b
            pre=fp(f,'pre');post=fp(f,'post');ns=list(nodes(f));paths={v:p for v,c,p in ns}
            assert pre==bp(b,'pre') and post==bp(b,'in')
            alt=alternative(f);assert pre==bp(alt,'in') and post==bp(alt,'post')
            leaves={v for v,c,p in ns if not c};assert [v for v in pre if v in leaves]==[v for v in post if v in leaves]
            assert pre==sorted(pre,key=paths.get);assert post==sorted(pre,key=cmp_to_key(lambda x,y:dc_compare(paths[x],paths[y])))
            seq=[(v,len(c)) for v,c,p in ns];assert degree_decode(seq)==f
            ds=tuple(d for v,d in seq);assert ds not in degree_shapes or degree_shapes[ds]==s;degree_shapes[ds]=s
            def bpaths(t,p='1'):
                if t is None:return {}
                return {t[0]:p}|bpaths(t[1],p+'0')|bpaths(t[2],p+'1')
            actual=bpaths(b)
            for v,c,p in ns:
                code='1'*p[0]+''.join('0'+'1'*(k-1) for k in p[1:]);assert actual[v]==code
            if n:
                def nullr(t):return 0 if t is None else int(t[2] is None)+nullr(t[1])+nullr(t[2])
                assert nullr(b)==sum(bool(c) for v,c,p in ns)+1
            pr={x:i for i,x in enumerate(pre)};po={x:i for i,x in enumerate(post)}
            for x,y in product(pre,repeat=2):
                anc=len(paths[x])<len(paths[y]) and paths[y][:len(paths[x])]==paths[x]
                assert anc==(pr[x]<pr[y] and po[x]>po[y]);result['ordered_pairs_ancestry']+=1
            result['forests']+=1
    # Every labelled tree through six nodes, arbitrary root and parent indices.
    for n in range(1,7):
        for s in shapes(n-1):
            f=((0,forest(label(s))),)
            ns=list(nodes(f));vs=[v for v,c,p in ns]
            for perm in permutations(range(1,n+1)):
                rename=dict(zip(vs,perm));parent=[0]*(n+1)
                for v,c,p in ns:
                    for w,_ in c:parent[rename[w]]=rename[v]
                root,l,r=parent_splice(parent);expected=parent_oracle(parent)
                actual=[];v=root
                for _ in range(n):actual.append(v);assert r[l[v]]==v and l[r[v]]==v;v=r[v]
                assert v==root and actual==expected;result['parent_arrays']+=1
    example=[0,3,8,4,0,4,8,3,4];root,l,r=parent_splice(example)
    assert (root,l[1:],r[1:])==(4,[3,8,4,6,7,2,1,5],[7,6,1,3,8,4,5,2])
    result['exercise18_example']={'root':root,'left':l[1:],'right':r[1:]}
    trees=[(0,forest(label(s))) for n in range(1,7) for s in shapes(n-1)]
    for t,u in product(trees,repeat=2):
        if sufficient(t,u):assert embedded(t,u)
        result['embedding_pairs']+=1
    t=(0,((1,()),(2,()),(3,())))
    u=(0,((1,((2,()),(3,()))),(4,())))
    assert embedded(t,u) and not sufficient(t,u)
    result['exercise22_counterexample']={'T':t,'Tprime':u,'mapping':{'0':0,'1':2,'2':3,'3':4}}
    return result

if __name__=='__main__':
    data=validate();(HERE/'results/trees.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))

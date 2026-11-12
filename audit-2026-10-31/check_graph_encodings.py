"""Independent SAT and graph oracles for exercises 387--390."""
from collections import Counter, deque
from itertools import combinations, permutations, product
from pathlib import Path
import json
from check_preprocessing import clauses, models


def satisfiable(formula):
    f={frozenset(c) for c in formula if not any(-l in c for l in c)}
    while f:
        if frozenset() in f:
            return False
        units={next(iter(c)) for c in f if len(c)==1}
        if any(-l in units for l in units):
            return False
        if not units:
            literals=set().union(*f)
            units={l for l in literals if -l not in literals}
        if not units:
            pivot=min(min(f,key=lambda c:(len(c),tuple(sorted(c)))),key=lambda l:(abs(l),l))
            return satisfiable(f|{frozenset((pivot,))}) or satisfiable(f|{frozenset((-pivot,))})
        f={frozenset(l for l in c if -l not in units) for c in f if not c&units}
    return True


def graphs(n):
    edges=list(combinations(range(n),2))
    for mask in range(1<<len(edges)):
        adjacency=[set() for _ in range(n)]
        for j,(u,v) in enumerate(edges):
            if mask>>j&1:
                adjacency[u].add(v);adjacency[v].add(u)
        yield adjacency


def distances(g,s):
    distance=[len(g)+1]*len(g);distance[s]=0;queue=deque((s,))
    while queue:
        u=queue.popleft()
        for v in g[u]:
            if distance[v]>len(g):
                distance[v]=distance[u]+1;queue.append(v)
    return distance


def paths_formula(g,s,t,k,kind,corrected=False):
    n=len(g)
    x=lambda v,j: j*n+v+1
    if kind in ('a','c'):
        f=[(x(s,0),)]
        for v in range(n):
            if v==s:
                continue
            f.append((-x(v,0),))
            f += [tuple([-x(v,j+1)]+[x(w,j) for w in sorted(g[v])]) for j in range(k)]
        if kind=='a':f.append((x(t,k),))
        else:f += [(x(v,k),) for v in range(n) if v!=s]
    elif kind=='d':
        f=[(x(s,j),) for j in (range(k+1) if corrected else (0,))]
        f += [(-x(v,j),x(w,j+1)) for j in range(k) for v in range(n) for w in g[v]]
        f.append((-x(t,k),))
    elif kind in ('e','f'):
        f=[(s+1,)]+[(-v-1,w+1) for v in range(n) for w in g[v]]
        f.append((-t-1,) if kind=='e' else tuple(-v-1 for v in range(n) if v!=s))
    elif kind=='b':
        f=[(s+1,),(t+1,)]
        for v in range(n):
            neighbors=sorted(g[v]);required=2-(v==s)-(v==t)
            # Direct truth table of the local constraint, without auxiliaries.
            for bits in product((0,1),repeat=len(neighbors)):
                if sum(bits)!=required:
                    f.append(tuple([-v-1]+[-w-1 if bit else w+1 for w,bit in zip(neighbors,bits)]))
    else:raise ValueError(kind)
    return f


def audit_paths(counts):
    first=None
    for n in range(1,6):
        for g in graphs(n):
            for s in range(n):
                dist=distances(g,s)
                connected=max(dist)<n
                assert satisfiable(paths_formula(g,s,0,n-1,'c'))==connected
                assert satisfiable(paths_formula(g,s,0,0,'f'))!=connected
                counts['connectivity_encodings']+=2
                exact={s}
                exact_by_length=[exact]
                for _ in range(n+1):
                    exact=set().union(*(g[v] for v in exact)) if exact else set()
                    exact_by_length.append(exact)
                for t in range(n):
                    reachable=dist[t]<=n-1
                    assert satisfiable(paths_formula(g,s,t,0,'b'))==reachable
                    assert satisfiable(paths_formula(g,s,t,0,'e'))!=reachable
                    counts['unbounded_path_encodings']+=2
                    for k in range(n+2):
                        nearby=dist[t]<=k and dist[t]<=n-1
                        assert satisfiable(paths_formula(g,s,t,k,'a'))==nearby
                        assert satisfiable(paths_formula(g,s,t,k,'d',True))!=nearby
                        printed=satisfiable(paths_formula(g,s,t,k,'d'))
                        assert printed==(t not in exact_by_length[k])
                        if printed==nearby:
                            counts['printed_390d_mismatches']+=1
                            if first is None and s!=t:
                                first={'n':n,'edges':[[u,v] for u in range(n) for v in g[u] if u<v],
                                       's':s,'t':t,'k':k,'distance':dist[t],
                                       'printed_clauses':paths_formula(g,s,t,k,'d')}
                        counts['bounded_path_encodings']+=3
        print('Paths complete through n=',n,dict(counts),flush=True)
    return first


def embedding_oracle(g,h):
    return any(all(mapping[v] in h[mapping[u]] for u in range(len(g)) for v in g[u])
               for mapping in permutations(range(len(h)),len(g)))


def embedding_formula(g,h,degree_filter=True):
    n,m=len(g),len(h)
    x=lambda u,v: u*m+v+1
    allowed={(u,v) for u in range(n) for v in range(m)
             if not degree_filter or len(g[u])<=len(h[v])}
    f=[]
    for u,v in combinations(range(n),2):
        for w in range(m):
            if (u,w) in allowed and (v,w) in allowed:
                f.append((-x(u,w),-x(v,w)))
    for u in range(n):
        for v,w in combinations(range(m),2):
            if (u,v) in allowed and (u,w) in allowed:
                f.append((-x(u,v),-x(u,w)))
    next_variable=n*m
    for u in range(n):
        for v in sorted(g[u]):
            if u>=v:continue
            options=[]
            # Both orientations of each target edge are required and allowed:
            # unlike source edges, the book does not impose u'<v' here.
            for a in range(m):
                for b in sorted(h[a]):
                    if (u,a) not in allowed or (v,b) not in allowed:continue
                    next_variable+=1;options.append(next_variable)
                    f += [(-next_variable,x(u,a)),(-next_variable,x(v,b))]
            f.append(tuple(options))
    return f


def remove_isolates(g):
    kept=[u for u,neighbors in enumerate(g) if neighbors]
    index={u:j for j,u in enumerate(kept)}
    return [{index[v] for v in g[u]} for u in kept]


def audit_embeddings(counts):
    collection=[g for n in range(5) for g in graphs(n)]
    for g in collection:
        for h in collection:
            expected=embedding_oracle(g,h)
            if len(g)>len(h):
                actual=False
            else:
                coreg,coreh=remove_isolates(g),remove_isolates(h)
                actual=satisfiable(embedding_formula(coreg,coreh))
                if all(g) and all(h):
                    assert satisfiable(embedding_formula(g,h,False))==expected
                    counts['unfiltered_embedding_pairs']+=1
            assert actual==expected
            counts['embedding_pairs_with_isolate_preprocessing']+=1


def audit_sinz(counts):
    # Formula (18)--(19), with the source's indices j and k kept distinct.
    for n in range(2,9):
        r=2;counter={(j,k):n+(j-1)*r+k for j in range(1,n-r+1) for k in range(1,r+1)}
        f=[]
        for j in range(1,n-r):
            for k in range(1,r+1):f.append((-counter[j,k],counter[j+1,k]))
        for j in range(1,n-r+1):
            for k in range(r+1):
                clause=[-(j+k)]
                if k:clause.append(-counter[j,k])
                if k<r:clause.append(counter[j,k+1])
                f.append(tuple(clause))
        assert len(counter)==2*(n-2)
        for bits in product((0,1),repeat=n):
            fixed=[((j+1) if bit else -(j+1),) for j,bit in enumerate(bits)]
            assert satisfiable(f+fixed)==(sum(bits)<=2)
            counts['sinz_at_most_two_assignments']+=1


def main():
    counts=Counter()
    pool=[frozenset()]+clauses(2)
    for mask in range(1<<len(pool)):
        f=[c for j,c in enumerate(pool) if mask>>j&1]
        assert satisfiable(f)==bool(models(f,2))
        counts['SAT_oracle_truth_table_checks']+=1
    audit_embeddings(counts)
    audit_sinz(counts)
    first=audit_paths(counts)
    out={'status':'all corrected assertions passed','counts':dict(counts),
         '390d_first_distinct_endpoint_counterexample':first,
         '390b_auxiliary_variables_for_degree_4':4,
         'scope':'All graphs through five vertices for path/connectivity encodings; embedding pairs through four vertices; Sinz r=2 through eight inputs.'}
    (Path(__file__).parent/'results/graph_encodings.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':
    main()

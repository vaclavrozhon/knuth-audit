"""Literal linked stacks of answer 7.2.2--58, with 2025 errata.
The star marker is optionally placed literally before the initialization.
Compare every result with a fresh independent BFS after vertex deletion.
"""
from collections import deque
from itertools import combinations
from pathlib import Path
import json,random

class BadMarker(Exception):pass


def bfs(adj,target,removed):
    inf=len(adj);dist=[inf+1 if v in removed else inf for v in range(inf)]
    if target in removed:return dist
    dist[target]=0;q=deque([target])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if dist[w]==inf:dist[w]=dist[v]+1;q.append(w)
    return dist


def axe(adj,dist,v,link,stamp,correct_marker=True):
    """Apply documented Feb 2025 d++ fix in either marker mode."""
    inf=len(adj);d=dist[v];dist[v]=inf+1
    R=None;T=v;link[v]=None;RT=None
    while T is not None:
        u=T;T=S=None;SB=None
        while u is not None:
            for w in adj[u]:
                if dist[w]<d or dist[w]>=inf:continue
                if dist[w]==d:
                    if u!=v and stamp[w]!=v:
                        stamp[w]=v
                        if R is None:R=RT=w
                        else:link[RT]=w;RT=w
                else:
                    assert dist[w]==d+1,(v,u,w,d,dist)
                    if not any(dist[z]==d for z in adj[w]):
                        link[w]=T;dist[w]=inf;T=w
                    elif u!=v and stamp[w]!=v:
                        stamp[w]=v
                        if S is None:S=SB=w
                        else:link[w]=S;S=w
            u=link[u]
            if u is not None and not correct_marker:
                # The printed return to (*) resets u,T,S again, not merely
                # restarting the neighbor loop for the just-selected u.
                u=T;T=S=None;SB=None
                if u is None:raise BadMarker({'deleted':v,'d':d,'next_u':None,'dist':dist.copy()})
        if S is not None:
            if R is None:R=S;RT=SB
            else:link[RT]=S;RT=SB
        d+=1
    if R is None:return
    link[RT]=None;S=None
    while R is not None or S is not None:
        def update(u):
            nonlocal S
            for w in adj[u]:
                if dist[w]==inf:
                    dist[w]=d+1;stamp[w]=v;link[w]=S;S=w
        if S is None:d=dist[R]
        else:
            u=S;d=dist[u];S=None
            while u is not None:
                update(u);u=link[u]
        while R is not None and dist[R]==d:
            u=R;R=link[u];update(u)


def main():
    counter=[[1],[0,2,3],[1],[1]]
    try:axe(counter,bfs(counter,0,set()),1,[None]*4,[None]*4,False)
    except BadMarker as e:bad=e.args[0]
    else:raise AssertionError('literal marker did not fail')
    instances=0
    for n in range(2,7):
        edges=list(combinations(range(n),2))
        for mask in range(1<<len(edges)):
            adj=[[] for i in range(n)]
            for k,(a,b) in enumerate(edges):
                if mask>>k&1:adj[a].append(b);adj[b].append(a)
            dist=bfs(adj,0,set())
            for v in range(1,n):
                if dist[v]==n:continue
                got=dist.copy();axe(adj,got,v,[None]*n,[None]*n)
                want=bfs(adj,0,{v});assert got==want,(adj,v,got,want)
                instances+=1
    rng=random.Random(20261101058)
    for trial in range(300):
        n=rng.randrange(8,65);adj=[[] for _ in range(n)]
        for a,b in combinations(range(n),2):
            if rng.random()<.15:adj[a].append(b);adj[b].append(a)
        dist=bfs(adj,0,set());link=[None]*n;stamp=[None]*n;removed=set()
        while True:
            eligible=[v for v in range(1,n) if dist[v]<n]
            if not eligible:break
            v=rng.choice(eligible);removed.add(v);axe(adj,dist,v,link,stamp)
            assert dist==bfs(adj,0,removed),(trial,removed,dist,bfs(adj,0,removed))
            instances+=1
    out={'status':'pass','marker_counterexample':{'adjacency':counter,'target':0,'removed':1,'failure':bad},'corrected_BFS_comparisons':instances,'all_simple_graphs_up_to':6,'random_sequential_deletion_graphs':300}
    dest=Path(__file__).resolve().parent/'results/estimation/dynamic-distances-verified.json';dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()

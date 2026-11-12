"""Geometric Torto paths, independent of the XCC representation."""
from itertools import product


def neighbors(m=6,n=3):
    return {r*n+c:[rr*n+cc for rr,cc in product(range(max(0,r-1),min(m,r+2)),
                range(max(0,c-1),min(n,c+2))) if (rr,cc)!=(r,c)] for r,c in product(range(m),range(n))}


def crossing_bit(u,v,n=3):
    r,c=divmod(u,n);rr,cc=divmod(v,n)
    return 1<<(min(r,rr)*(n-1)+min(c,cc)) if r!=rr and c!=cc else 0


def paths(board,word,m=6,n=3,wild=False):
    adjacent=neighbors(m,n);result=[]
    def rec(path,used,diagonals):
        if len(path)==len(word):
            result.append(tuple(path));return
        for v in adjacent[path[-1]]:
            if used>>v&1:continue
            if board[v]!=word[len(path)] and not (wild and board[v]=='.'):continue
            bit=crossing_bit(path[-1],v,n)
            if bit&diagonals:continue
            rec(path+[v],used|(1<<v),diagonals|bit)
    for u,c in enumerate(board):
        if c==word[0] or (wild and c=='.'):rec([u],1<<u,0)
    return result


def validate_path(board,word,path,m=6,n=3):
    assert len(path)==len(word) and len(set(path))==len(path)
    assert ''.join(board[u] for u in path)==word
    diagonals=0
    for u,v in zip(path,path[1:]):
        r,c=divmod(u,n);rr,cc=divmod(v,n)
        assert max(abs(r-rr),abs(c-cc))==1
        bit=crossing_bit(u,v,n);assert not bit&diagonals;diagonals|=bit


def canonical(board,m=6,n=3):
    return min(''.join(board[(m-1-r if flipr else r)*n+(n-1-c if flipc else c)]
               for r,c in product(range(m),range(n))) for flipr,flipc in product([False,True],repeat=2))

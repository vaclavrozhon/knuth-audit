"""Standalone counterexample to the printed loop in answer 7.2.2.1--221.

No DLX implementation, external solver, or third-party package is imported.
The table is the ordinary C1 layout immediately after uncovering item a.
"""
from copy import deepcopy
from itertools import combinations


def witness():
    # Headers 1=a, 2=b, 3=s; spacer4; row1 nodes5,6; spacer7;
    # row2 node8; spacer9; row3 nodes10,11; spacer12.
    return dict(
        top=[0, 1, 2, 3, 0, 1, 3, -1, 1, -2, 2, 3, -3],
        up=[0, 8, 10, 11, 0, 1, 3, 5, 5, 8, 2, 6, 10],
        down=[0, 5, 10, 6, 6, 8, 11, 8, 1, 11, 2, 3, 0],
        length=[0, 2, 1, 2],
        rows=[{1: 0, 3: 1}, {1: 0}, {2: 0, 3: 2}],
    )


def models(rows):
    result=[]
    for mask in range(1 << len(rows)):
        ids=[k for k in range(len(rows)) if mask >> k & 1]
        if any(sum(p in rows[k] for k in ids) != 1 for p in (1, 2)):
            continue
        if all(all(rows[a][j] > 0 and rows[a][j] == rows[b][j]
                   for j in rows[a].keys() & rows[b].keys())
               for a, b in combinations(ids, 2)):
            result.append([k+1 for k in ids])
    return result


def delete_221(corrected=False):
    m=deepcopy(witness()); top,up,down,length=[m[k] for k in ('top','up','down','length')]
    # P5 has placed the blocked row on an initially empty stack.
    x=5; top[x]=0; stack=x
    x=stack; stack=top[x]; top[x]=1
    assert stack == 0
    trace=[]; q=x; first=True
    # Corrected version tests q<=x after the first execution of the body.
    while q >= x if not corrected else first or q > x:
        first=False; j=top[q]
        if j <= 0:
            trace.append(dict(q=q,top=j,action='wrap',next=up[q])); q=up[q]
        elif j <= 2 and length[j] == 1:
            trace.append(dict(q=q,top=j,length=length[j],action='P9: collapse'))
            return dict(collapsed=True,trace=trace,memory=m)
        else:
            trace.append(dict(q=q,top=j,length_before=length[j],action='unlink'))
            u,d=up[q],down[q]; up[d]=u; down[u]=d; length[j]-=1; q+=1
        assert len(trace)<10, 'The tiny witness must terminate or collapse immediately.'
    for j,expected in [(1,[8]),(2,[10]),(3,[11])]:
        p=down[j]; seen=[]
        while p != j:
            seen.append(p); assert len(seen)<4; p=down[p]
        assert seen == expected and length[j] == len(seen)
    return dict(collapsed=False,trace=trace,memory=m)


def verify():
    m=witness(); assert models(m['rows']) == [[2,3]]
    # Row1 conflicts with the only b row, so P5 correctly schedules it.
    assert m['rows'][0][3] != m['rows'][2][3]
    bad,good=delete_221(),delete_221(True)
    assert [q['q'] for q in bad['trace']] == [5,6,7,5]
    assert bad['collapsed'] and not good['collapsed']
    return dict(input='a b | s\na s:1\na\nb s:2\n',solutions=[[2,3]],
                memory_before=m,printed=bad,corrected=good)


if __name__ == '__main__':
    import json
    print(json.dumps(verify(),indent=2))

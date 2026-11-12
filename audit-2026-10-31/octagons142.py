"""DLX142: mixed edge/corner matching, modeled with eight boundary half edges."""
from collections import defaultdict
from itertools import product
from pathlib import Path
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/octagons142'
CASES = ['i','ii','iii']


def tile(word):
    return min(word[i:]+word[:i] for i in range(4))


def inventory(palette='abc'):
    words = [''.join(w) for w in product(palette,repeat=4)]
    return words,sorted({tile(w) for w in words})


def color_key(word):
    labels = {}
    return ''.join(labels.setdefault(c,chr(97+len(labels))) for c in word)


def modes(label,width=6,height=4):
    assert label in CASES
    return {(x,y): ('V' if (x<width//2 if label=='i' else y<height//2 if label=='ii'
                            else (x<width//2)==(y>=height//2)) else 'E')
            for x in range(width) for y in range(height)}


def half_edges(cell):
    x,y = cell
    return [('h',x,y,0),('h',x,y,1),('v',x+1,y,0),('v',x+1,y,1),
            ('h',x,y+1,0),('h',x,y+1,1),('v',x,y,0),('v',x,y,1)]


def sector_indices(mode):
    # V: LL,LR,UR,UL. E: bottom,right,top,left. Each list is cyclic.
    return [0,1,1,2,3,2,0,3] if mode=='V' else [0,0,1,1,2,2,3,3]


def boundary_pairs(layout):
    width=max(x for x,y in layout)+1;height=max(y for x,y in layout)+1
    return dict(tb=[(('h',x,0,k),('h',x,height,k)) for x in range(width) for k in range(2)],
                lr=[(('v',0,y,k),('v',width,y,k)) for y in range(height) for k in range(2)])


def validate(layout,placements,palette='abc',complete=True):
    assert set(placements)==set(layout)
    values={};types=[]
    for cell,word in placements.items():
        assert len(word)==4 and set(word)<=set(palette)
        types.append(tile(word))
        for edge,sector in zip(half_edges(cell),sector_indices(layout[cell])):
            c=word[sector]
            assert edge not in values or values[edge]==c,(cell,edge,c,values.get(edge))
            values[edge]=c
    assert len(set(types))==len(types)
    if complete:
        assert sorted(types)==inventory(palette)[1]
    return values


def problem(layout,palette='abc',complete=True,periodic=()):
    words,types=inventory(palette);board=sorted(layout)
    all_edges=sorted({e for cell in board for e in half_edges(cell)})
    names={e:e for e in all_edges}
    # Optional identified boundaries count cylinders without emitting all models.
    for axis in periodic:
        for a,b in boundary_pairs(layout)[axis]:
            assert a in names and b in names
            names[b]=names[a]
    edge_name=lambda e:e[0]+str(e[1])+'_'+str(e[2])+'_'+str(e[3])
    position=lambda c:'p'+str(c[0])+'_'+str(c[1])
    primary=[position(c) for c in board]+(types if complete else [])
    secondary=([] if complete else types)+[edge_name(e) for e in sorted(set(names.values()))]
    rows=[];placements=[]
    for cell in board:
        for word in words:
            assigned={};valid=True
            for edge,sector in zip(half_edges(cell),sector_indices(layout[cell])):
                name=edge_name(names[edge]);color=word[sector]
                if name in assigned and assigned[name]!=color:
                    valid=False;break
                assigned[name]=color
            if valid:
                rows.append([position(cell),tile(word)]+[name+':'+c for name,c in assigned.items()])
                placements.append(dict(cell=cell,word=word))
    return dict(header=primary+['|']+secondary,rows=rows,placements=placements,
                cells=board,modes=[layout[c] for c in board],palette=palette,complete=complete,
                periodic=list(periodic))


def native_text(enc):
    return ' '.join(enc['header'])+'\n'+''.join(' '.join(row)+'\n' for row in enc['rows'])


def contracted(layout,periodic=()):
    """Independent variable model: union equal sectors across shared half edges."""
    board=sorted(layout);parent=list(range(4*len(board)));incidence=defaultdict(list)
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    def union(x,y):
        a,b=find(x),find(y)
        if a!=b:
            parent[max(a,b)]=min(a,b)
    for i,cell in enumerate(board):
        for edge,sector in zip(half_edges(cell),sector_indices(layout[cell])):
            incidence[edge].append(4*i+sector)
    for occurrences in incidence.values():
        for other in occurrences[1:]:
            union(occurrences[0],other)
    for axis in periodic:
        for a,b in boundary_pairs(layout)[axis]:
            union(incidence[a][0],incidence[b][0])
    roots=sorted({find(v) for v in parent});index={r:i for i,r in enumerate(roots)}
    sectors=[[index[find(4*i+j)] for j in range(4)] for i in range(len(board))]
    edge_variables={e:index[find(v[0])] for e,v in incidence.items()}
    pairs={axis:[(edge_variables[a],edge_variables[b]) for a,b in bb]
           for axis,bb in boundary_pairs(layout).items()}
    return dict(cells=board,sectors=sectors,variables=len(roots),boundary_pairs=pairs,
                half_edges=sorted(edge_variables),half_edge_variables=[edge_variables[e] for e in sorted(edge_variables)])


def independent_case(label,layout,palette='abc',complete=True,every=1,periodic=()):
    enc=contracted(layout,periodic)
    result=f'{label} {len(palette)} {enc["variables"]} {len(layout)} {int(complete)} {every}\n'
    result+=''.join(' '.join(map(str,ids))+'\n' for ids in enc['sectors'])
    for axis in ['tb','lr']:
        pairs=enc['boundary_pairs'][axis]
        result+=str(len(pairs))+'\n'+''.join(f'{a} {b}\n' for a,b in pairs)
    return result

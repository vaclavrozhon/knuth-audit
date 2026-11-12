"""Decode printed path and tiling figures from vector strokes, without search."""
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict, Counter
import json
import math
import os
import time
import xml.etree.ElementTree as ET
from extract_chain150 import points
from extract_jigsaw import transform
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/zdd261_264'


def source(name):
    t=ET.parse(OUT/(name+'.xml'))
    strokes=[]
    for p in t.iter('stroke_path'):
        seq=[];segments=[];first=last=None
        for q in p:
            ps=points(p,q)
            if q.tag=='moveto':first=last=ps[0];seq.append(last)
            elif q.tag=='lineto':segments.append((last,ps[0]));last=ps[0];seq.append(last)
            elif q.tag=='closepath':segments.append((last,first));last=first
            else:assert q.tag!='curveto'
        if seq:strokes.append(dict(color=p.get('color'),points=seq,segments=segments))
    return t,strokes


def select(strokes,box,color='0 0 0'):
    x0,x1,y0,y1=box
    return [p for p in strokes if p['color']==color and all(x0<x<x1 and y0<y<y1 for x,y in p['points'])]


def bounds(strokes):
    ps=[p for s in strokes for p in s['points']]
    return min(x for x,y in ps),max(x for x,y in ps),min(y for x,y in ps),max(y for x,y in ps)


def edge(a,b):return tuple(sorted((a,b)))


def grid_edges(strokes,convert):
    edges=set()
    for s in strokes:
        for a,b in s['segments']:
            u,v=convert(a),convert(b)
            dx,dy=v[0]-u[0],v[1]-u[1]
            length=max(abs(dx),abs(dy))
            assert length and (dx==0 or dy==0 or dx==-dy),(u,v)
            step=(dx//length,dy//length)
            for j in range(length):
                x=(u[0]+j*step[0],u[1]+j*step[1]);y=(x[0]+step[0],x[1]+step[1])
                edges.add(edge(x,y))
    return edges


def rectangular(strokes,n,h):
    x0,x1,y0,y1=bounds(strokes);ux=(x1-x0)/n;uy=(y1-y0)/h
    assert abs(ux/uy-1)<.002
    def convert(p):
        x,y=(p[0]-x0)/ux,(p[1]-y0)/uy
        assert max(abs(x-round(x)),abs(y-round(y)))<.025,(p,x,y)
        return round(x),round(y)
    return grid_edges(strokes,convert),(x0,y0,ux,uy)


def dominoes(strokes,n):
    edges,geometry=rectangular(strokes,n,16)
    cells={(x,y) for y in range(16) for x in range(max(0,7-y,y-8),n-max(0,7-y,y-8))}
    sides=defaultdict(list)
    for x,y in cells:
        for a,b in [((x,y),(x+1,y)),((x+1,y),(x+1,y+1)),((x,y+1),(x+1,y+1)),((x,y),(x,y+1))]:sides[edge(a,b)].append((x,y))
    assert edges<=sides.keys()
    tiles=[]
    for e,adj in sides.items():
        if len(adj)==1:assert e in edges
        elif e not in edges:tiles.append(tuple(sorted(adj)))
    assert Counter(c for tile in tiles for c in tile)==Counter({c:1 for c in cells})
    assert len(tiles)==8*n-56
    return dict(n=n,tiles=sorted(tiles),cells=len(cells),edges=len(edges),geometry=geometry)


def lozenges(strokes,n):
    x0,x1,y0,y1=bounds(strokes);a=(x1-x0)/(n+8);b=(y1-y0)/16
    assert abs(b/a-math.sqrt(3)/2)<.002
    def convert(p):
        r=(p[1]-y0)/b;q=(p[0]-x0)/a-r/2
        assert max(abs(q-round(q)),abs(r-round(r)))<.025,(p,q,r)
        return round(q),round(r)
    edges=grid_edges(strokes,convert)
    polygon=[(4,0),(4+n,0),(4+n,8),(n-4,16),(-4,16),(-4,8)]
    def inside(t):
        q=sum(p[0] for p in t)/3;r=sum(p[1] for p in t)/3
        return all((v[0]-u[0])*(r-u[1])-(v[1]-u[1])*(q-u[0])>0 for u,v in zip(polygon,polygon[1:]+polygon[:1]))
    triangles=[];sides=defaultdict(list)
    for q in range(-12,n+13):
        for r in range(16):
            for t in [((q,r),(q+1,r),(q,r+1)),((q+1,r),(q,r+1),(q+1,r+1))]:
                if inside(t):
                    i=len(triangles);triangles.append(t)
                    for u,v in zip(t,t[1:]+t[:1]):sides[edge(u,v)].append(i)
    assert edges<=sides.keys(),(len(edges-sides.keys()),sorted(edges-sides.keys())[:8])
    tiles=[];vertical=[]
    for e,adj in sides.items():
        if len(adj)==1:assert e in edges
        elif e not in edges:
            tiles.append(tuple(sorted(adj)))
            if e[0][1]==e[1][1]:vertical.append(e[0])
    assert Counter(c for tile in tiles for c in tile)==Counter(range(len(triangles)))
    assert len(tiles)==16*n+64
    assert Counter(r for q,r in vertical)==Counter({r:min(r,16-r) for r in range(1,16)})
    return dict(n=n,triangles=triangles,tiles=sorted(tiles),vertical_left_vertices=sorted(vertical),edges=len(edges),geometry=(x0,y0,a,b))


def square_paths(strokes):
    edges,geometry=rectangular(strokes,16,16)
    boundary={e for e in edges if any(e[0][k]==e[1][k] and e[0][k] in [0,16] for k in [0,1])}
    graph=defaultdict(set)
    for a,b in edges-boundary:graph[a].add(b);graph[b].add(a)
    assert all(len(v) in [1,2] for v in graph.values())
    sources=[v for v in graph if len(graph[v])==1 and (v[1]==0 or v[0]==16)]
    paths=[]
    for v in sorted(sources):
        path=[v];previous=None
        while True:
            choices=graph[v]-({previous} if previous is not None else set())
            if not choices:break
            assert len(choices)==1
            w=next(iter(choices));assert (w[0]-v[0],w[1]-v[1]) in [(-1,0),(0,1)]
            path.append(w);previous,v=v,w
        assert (v[0]==0 or v[1]==16)
        assert sum(x==y for x,y in path)==1
        paths.append(path)
    assert len(paths)==15
    assert Counter(v for p in paths for v in p)==Counter({v:1 for v in graph})
    return dict(paths=paths,geometry=geometry,edges=len(edges-boundary),boundary_edges=len(boundary))


def knight_digits(tree,dx=0,dy=0):
    glyphs=[]
    for t in tree.iter('fill_text'):
        for sp in t:
            for g in sp:
                x,y=transform(t,float(g.get('x')),float(g.get('y')))
                if 260+dx<x<305+dx and 139+dy<y<184+dy and g.get('unicode','') in '0123456789':glyphs.append((x,y,g.get('unicode')))
    assert len(glyphs)==64,len(glyphs)
    glyphs.sort(key=lambda p:p[1]);rows=[]
    for i in range(8):rows.append(''.join(p[2] for p in sorted(glyphs[8*i:8*i+8])))
    expected=['12345678','34120856','12385607','48523700','51486237','00014762','05876143','87654321']
    assert rows==expected,rows
    paths=[]
    for k in range(1,9):
        path=[(r,c) for r,row in enumerate(rows) for c,d in enumerate(row) if d==str(k)]
        assert path[0]==(0,k-1) and path[-1]==(7,8-k)
        assert all((v[0]-u[0],abs(v[1]-u[1])) in [(1,2),(2,1)] for u,v in zip(path,path[1:]))
        paths.append(path)
    return dict(rows=rows,paths=paths,occupied=sum(len(p) for p in paths))


def randall(strokes,dx=0,dy=0):
    tile_sets=[dominoes(select(strokes,(50+dx,175+dx,187+dy,268+dy)),24),dominoes(select(strokes,(180+dx,305+dx,187+dy,268+dy)),24)]
    assert tile_sets[0]['tiles']==tile_sets[1]['tiles']
    colors={}
    for k,(color,tile) in enumerate(zip(['0 0 1','1 0 0'],tile_sets)):
        x0,y0,ux,uy=tile['geometry']
        lines=[]
        for p in strokes:
            if p['color']==color:
                lines.append([((x-x0)/ux,(y-y0)/uy) for x,y in p['points']])
        assert len(lines)==12
        colors[color]=lines
    def hits(color,p):
        found=[]
        for index,line in enumerate(colors[color]):
            for a,b in zip(line,line[1:]):
                d=(b[0]-a[0],b[1]-a[1]);norm=d[0]**2+d[1]**2
                t=((p[0]-a[0])*d[0]+(p[1]-a[1])*d[1])/norm
                if -.01<=t<=1.01 and abs((p[0]-a[0])*d[1]-(p[1]-a[1])*d[0])/math.sqrt(norm)<.02:found.append((index,d))
        return found
    counts=Counter();errors=[]
    for a,b in tile_sets[0]['tiles']:
        p=((a[0]+b[0])/2+.5,(a[1]+b[1])/2+.5)
        blue,red=hits('0 0 1',p),hits('1 0 0',p)
        if a[0]==b[0]:
            if not (bool(blue)!=bool(red) and all(abs(d[0])<.02 for _,d in blue+red)):
                errors.append(dict(tile=(a,b),kind='vertical',blue=blue,red=red))
            counts['vertical_blue' if blue else 'vertical_red']+=1
        else:
            if not (blue and red and all(d[0]*d[1]*e[0]*e[1]<0 for _,d in blue for _,e in red)):
                errors.append(dict(tile=(a,b),kind='horizontal',blue=blue,red=red))
            counts['horizontal_crossed']+=1
    return dict(tiles=tile_sets[0]['tiles'],path_counts={c:len(q) for c,q in colors.items()},motifs=counts,paths=colors,errors=errors)


def main():
    assert not (OUT/'figures-checked.json').exists()
    started=time.monotonic();result={}
    for label,question,answer,dx,dy in [('original','original-175','original-503',0,0),('draft','draft-97','draft-193',22.08,108.66)]:
        tree,strokes=source(question)
        boxes=[(40,125,270,352),(125,250,270,352),(250,405,270,352)]
        dom=[dominoes(select(strokes,(a+dx,b+dx,c+dy,d+dy)),n) for (a,b,c,d),n in zip(boxes,[16,24,32])]
        boxes=[(40,145,390,475),(145,260,390,475),(260,405,390,475)]
        hexa=[lozenges(select(strokes,(a+dx,b+dx,c+dy,d+dy)),n) for (a,b,c,d),n in zip(boxes,[8,12,16])]
        paths=square_paths(select(strokes,(160+dx,210+dx,137+dy,184+dy)))
        knight=knight_digits(tree,dx,dy)
        _,answer_strokes=source(answer)
        rr=randall(answer_strokes,dx+(14.04 if label=='draft' else 0),dy-(.12 if label=='draft' else 0))
        assert len(rr['errors'])==1 and rr['errors'][0]['tile']==((12,1),(13,1)),(label,rr['errors'])
        assert rr['errors'][0]['blue']==[] and len(rr['errors'][0]['red'])==1
        assert rr['tiles']==dom[1]['tiles']
        data=dict(dominoes=dom,hexagons=hexa,square=paths,knights=knight,randall=rr)
        save(OUT/(label+'-figures.json'),data);result[label]=data
    for k in ['dominoes','hexagons']:
        for a,b in zip(result['original'][k],result['draft'][k]):
            assert {k:v for k,v in a.items() if k!='geometry'}=={k:v for k,v in b.items() if k!='geometry'}
    assert result['original']['square']['paths']==result['draft']['square']['paths']
    assert result['original']['knights']==result['draft']['knights']
    # Recover the correspondence of the 64 vertical lozenges with the printed array.
    array=[[int(c,16) for c in row] for row in ['00012457','1134569c','12368abc','25789bbc','4578accc','459aaccc','569aaccc','bbbbcccc']]
    assert all(array[i][j]<=array[i+1][j] for i in range(7) for j in range(8))
    assert all(array[i][j]<=array[i][j+1] for i in range(8) for j in range(7))
    actual=set(map(tuple,result['original']['hexagons'][1]['vertical_left_vertices']))
    decoded=[[None]*8 for _ in range(8)]
    for r in range(1,16):
        indices=[(i,j) for i in range(8) for j in range(8) if 8+i-j==r]
        qs=sorted(q for q,s in actual if s==r)
        assert len(qs)==len(indices)
        for (i,j),q in zip(indices,qs):decoded[i][j]=q+4-j
    differences=[(i,j,array[i][j],decoded[i][j]) for i in range(8) for j in range(8) if array[i][j]!=decoded[i][j]]
    assert differences==[(3,0,2,3),(4,0,4,5),(5,0,4,5),(6,0,5,6)],differences
    assert all(decoded[i][j]<=decoded[i+1][j] for i in range(7) for j in range(8))
    assert all(decoded[i][j]<=decoded[i][j+1] for i in range(8) for j in range(7))
    save(OUT/'reverse-plane-partition.json',dict(array=array,decoded_array=decoded,differences=differences,formula='(q,r)=(-4+j+value,8+i-j); (q,r) is the left endpoint of the removed horizontal edge'))
    files=[OUT/(x+'.xml') for x in ['original-175','original-503','draft-97','draft-193']]+[OUT/(x+'-figures.json') for x in ['original','draft']]+[OUT/'reverse-plane-partition.json']
    save(OUT/'figures-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),elapsed_seconds=time.monotonic()-started,nice=os.getpriority(os.PRIO_PROCESS,0),artifact_hashes={str(p.relative_to(ROOT)):sha(p) for p in files},summary='Both complete source figures:15 paths,64 knight digits,3 domino tilings,3 lozenge tilings,24 Randall paths and64 reverse-plane entries. One identical Randall horizontal domino lacks its blue diagonal; all other135 motifs pass. Four reverse-plane entries disagree with the picture. Exact between-version match of tilings and paths.'))
    print(json.dumps(dict(elapsed_seconds=time.monotonic()-started,dominoes=[len(q['tiles']) for q in result['original']['dominoes']],lozenges=[len(q['tiles']) for q in result['original']['hexagons']],randall=result['original']['randall']['motifs'],array_differences=differences),indent=2))


if __name__=='__main__':main()

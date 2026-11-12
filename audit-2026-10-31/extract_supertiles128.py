"""Check every colored wedge in both original128 illustrations, including clips."""
from collections import Counter,defaultdict
from datetime import datetime,timezone
from math import sqrt
import extract_jigsaw as ex
import borders127_128 as b
from macmahon126 import save,sha

PALETTE={'1 1 1':'a','1 .75 .75':'b','.5 .5 1':'c'}


def extract(part,scale,x0,y0):
    tiles=defaultdict(dict);max_error=0;records=[]
    for index,p in enumerate(part):
        paths=ex.paths(p);assert len(paths)==1 and len(paths[0])==3
        center,a,c=paths[0];coords=[]
        for X,Y in (a,c):
            y=(y0-Y)/(scale*sqrt(3)/2);x=(X-x0)/scale-y/2
            max_error=max(max_error,abs(x-round(x)),abs(y-round(y)));assert max_error<.0003
            coords.append((round(x),round(y)))
        X,Y=center;y=(y0-Y)/(scale*sqrt(3)/2);x=(X-x0)/scale-y/2
        possible=[]
        for z in (0,1):
            xx=x-(1+z)/3;yy=y-(1+z)/3
            if abs(xx-round(xx))<.0003 and abs(yy-round(yy))<.0003:possible.append((round(xx),round(yy),z))
        assert len(possible)==1,(center,x,y,possible)
        t=possible[0];edge=next(e for e in b.g.edges(t) if b.endpoints(e)==frozenset(coords));k=edge[0]
        assert k not in tiles[t];color=PALETTE[p.get('color')];tiles[t][k]=color
        records.append(dict(index=index,cell=t,edge=edge,color=color))
    return tiles,dict(scale=scale,x0=x0,y0=y0,max_lattice_rounding_error=max_error,wedges=records)


def main():
    ex.OUT=b.OUT;tree=ex.trace(448)
    fills=[p for p in tree.iter('fill_path') if p.get('colorspace')=='DeviceRGB'];assert len(fills)==1055
    # The source shows two rows of triangles, hence height2 triangular units.
    vs=[v for p in fills[:33] for v in ex.paths(p)[0][1:]]
    scale=(max(y for x,y in vs)-min(y for x,y in vs))/sqrt(3)
    small,small_data=extract(fills[:33],scale,min(x for x,y in vs),max(y for x,y in vs))
    assert set(small)==set(b.CELLS128) and all(len(cs)==3 for cs in small.values())
    enc=b.problem128();edges={};piece_positions=[]
    for t,cs in small.items():
        colors=''.join(cs[k] for k in ['-','/','\\']);piece_positions.append(dict(cell=t,colors=colors,piece=b.g.piece(colors)))
        for e,c in zip(b.g.edges(t),colors):assert e not in edges or edges[e]==c;edges[e]=c
    assert all(edges[a]==edges[c] for a,c in b.PAIRS128)
    vector=''.join(edges[e] for e in enc['representatives']);b.validate128(vector,enc)
    assert vector in (b.OUT/'supertiles128-models.txt').read_text().splitlines()
    # Six rows, with the upper and lower triangles giving twelve center heights.
    part=fills[33:];vs=[v for p in part for v in ex.paths(p)[0][1:]]
    heights={round(ex.paths(p)[0][0][1],2) for p in part};assert len(heights)==12
    scale=(max(y for x,y in vs)-min(y for x,y in vs))/(6*sqrt(3)/2)
    big,big_data=extract(part,scale,min(x for x,y in vs)-scale/2,max(y for x,y in vs))
    base={}
    for t,colors in small.items():
        for u in [t,(2-t[0],-1-t[1],1-t[2])]:
            key=((u[0]-8*u[1])%11,u[2]);assert key not in base;base[key]=colors
    phases=[]
    for shift in range(11):
        if all(all(base[((t[0]-8*t[1]+shift)%11,t[2])][e]==c for e,c in cs.items()) for t,cs in big.items()):phases.append(shift)
    assert len(phases)==1,phases
    # Check visible shared edges independently of the periodic match.
    visible={}
    for t,cs in big.items():
        for e in b.g.edges(t):
            if e[0] in cs:
                assert e not in visible or visible[e]==cs[e[0]];visible[e]=cs[e[0]]
    save(b.OUT/'supertiles128-figures-checked.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
         source_sha256=sha(__file__),trace_sha256=sha(b.OUT/'page448-trace.xml'),total_original_wedges=1055,
         small=dict(**small_data,tiles=piece_positions,edge_vector=vector,belongs_to_complete_model_set=True),
         large=dict(**big_data,triangle_count=len(big),visible_wedges_per_triangle=dict(Counter(map(len,big.values()))),
                    lattice_phase=phases[0],all1022_visible_wedges_match_periodic_extension=True),
         scope='All33 wedges in the11-tile example and all1022 drawn wedges in the cropped plane pattern match the proven periodic extension; undrawn clipped wedges are not asserted to be visible.'))
    print('PASS:33 small and1022 large original wedges;',len(big),'large triangles;',Counter(map(len,big.values())),'phase',phases)


if __name__=='__main__':main()

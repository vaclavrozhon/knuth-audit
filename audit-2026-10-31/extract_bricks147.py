"""Extract every tensor character from the original PDF and2019 author draft."""
from datetime import datetime,timezone
from pathlib import Path
import xml.etree.ElementTree as ET
from extract_jigsaw import transform
import bricks147 as h


def glyphs(path):
    result=[]
    for t in ET.parse(path).getroot().iter('fill_text'):
        for span in t:
            for g in span:
                if g.get('unicode') in '.abcdef':
                    x,y=transform(t,float(g.get('x')),float(g.get('y')))
                    result.append((x,y,g.get('unicode')))
    return result


def tensor(gs,dims,x0,step,y0,dx,dy):
    nx,ny,nz=[2*d+1 for d in dims];out=[[['?']*nz for _ in range(ny)] for _ in range(nx)]
    for i in range(nx):
        start=x0+i*step
        selected=[(x,y,c) for x,y,c in gs if start-.3<x<start+(nz-1)*dx+.3 and y0-.3<y<y0+(ny-1)*dy+.3]
        assert len(selected)==ny*nz,(i,dims,len(selected))
        for x,y,c in selected:
            j=round((y-y0)/dy);k=round((x-start)/dx)
            assert abs(x-start-k*dx)<.3 and abs(y-y0-j*dy)<.3
            assert out[i][j][k]=='?';out[i][j][k]=c
    return [[''.join(row) for row in plane] for plane in out]


def main():
    specs={
        'small':dict(dims=(1,2,2),page=476,x0=171.49,step=49.66,y0=345.0,dx=4.68,dy=8.96),
        'magnificent':dict(dims=(2,3,5),page=476,x0=72.49,step=68.67,y0=453.55,dx=4.68,dy=8.96),
        'macmahon':dict(dims=(2,2,2),page=477,x0=60.98,step=32.35,y0=388.25,dx=3.745,dy=7.18),
        'kowalewski':dict(dims=(2,2,2),page=477,x0=234.8,step=32.34,y0=388.25,dx=3.745,dy=7.18),
        'winter':dict(dims=(2,2,2),page=477,x0=60.98,step=32.35,y0=444.6,dx=3.745,dy=7.18),
        'fourth':dict(dims=(2,2,2),page=477,x0=234.8,step=32.34,y0=444.65,dx=3.745,dy=7.18)}
    results={};traces={}
    for key,spec in specs.items():
        args=dict(spec);page=args.pop('page');a=h.OUT/f'original-{page}.xml';b=h.OUT/f'draft-{page-310}.xml'
        original=tensor(glyphs(a),**args)
        draft_args=dict(args)
        draft_args['x0']+=9.59 if page==476 else 22.06
        draft_args['y0']+=108.65
        draft=tensor(glyphs(b),**draft_args)
        assert original==draft,key
        result=h.decode_tensor(spec['dims'],original);result.update(tensor=original)
        normalized=h.cubes.normalize(result['model']);acted=h.orbit(spec['dims'],normalized)
        result.update(automorphisms=acted.count(normalized),spatial_group_size=len(acted))
        expected={'small':8,'magnificent':2,'macmahon':24,'kowalewski':8,'winter':4,'fourth':8}[key]
        assert result['automorphisms']==expected,(key,result['automorphisms'])
        results[key]=result;traces.update({str(p.relative_to(h.ROOT)):h.sha(p) for p in [a,b]})
    assert results['small']['names']==['abcedf','abcefd','abcdfe','abcdef']
    big=results['magnificent'];assert sorted(big['names'])==h.cubes.TYPES
    colors=dict(zip(h.positions((2,3,5)),big['model']));assert h.cubes.NAME[colors[(0,1,2)]]=='acbefd'
    # Tensor axes are front/back, top/bottom, left/right; the book lists
    # the three opposite pairs without imposing this coordinate order.
    assert big['boundary']==list('aaccbb')
    # The explicit nontrivial symmetry swaps front/back, top/bottom, e/f.
    op=next(g for g in h.group((2,3,5)) if g[0]==(0,1,2) and g[1]==(-1,-1,1))
    changed=h.transform((2,3,5),big['model'],op)
    assert tuple(w.translate(str.maketrans('ef','fe')) for w in changed)==tuple(big['model'])
    h.save(h.OUT/'figures-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),
        checker_sha256=h.sha(__file__),geometry_sha256=h.sha(h.__file__),cube_geometry_sha256=h.sha(h.cubes.__file__),
        trace_hashes=traces,figures=results,all_original_and_draft_characters_equal=True,
        total_characters=sum(r['characters'] for r in results.values()),all_cubes_contacts_and_boundaries_valid=True))
    print('PASS147 tensors:960 characters,285 facets; six valid figures; all named cubes and automorphisms; original/draft identical.')


if __name__=='__main__':main()

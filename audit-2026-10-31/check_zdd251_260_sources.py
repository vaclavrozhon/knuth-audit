"""Read vector figures and accepted new results; no solver or census is run."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
from decimal import Decimal, localcontext
from math import comb, factorial
import json
import time
import xml.etree.ElementTree as ET
from extract_jigsaw import transform
from extract_chain150 import points
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/zdd251_260'


def read(p):
    return json.loads(Path(p).read_text())


def figure(file, width, dx=0, dy=0):
    tree = ET.parse(OUT / file)
    labels = {}
    for t in tree.iter('fill_text'):
        for sp in t:
            s = ''.join(g.get('unicode','') for g in sp)
            if len(s) != width or not set(s) <= {'0','1'}:
                continue
            coords = [transform(t,float(g.get('x')),float(g.get('y'))) for g in sp]
            x,y = coords[0]
            # Exclude the prose example repeated below figure (123).
            if width == 8 and y > 595 + dy:
                continue
            advance = coords[1][0] - x
            labels[int(s,2)] = (x + advance*width/2, y-1.605)
    assert len(labels) == (33 if width == 8 else 8)
    # The rectangular success terminal is the only five-command stroke in
    # the main figure's bounds (the legend in (123) is farther to the right).
    rects = []
    for t in tree.iter('stroke_path'):
        ps = [p for q in t for p in points(t,q)]
        if len(t) == 5 and ps:
            x = (min(p[0] for p in ps)+max(p[0] for p in ps))/2
            y = (min(p[1] for p in ps)+max(p[1] for p in ps))/2
            if width == 8 and 250+dx < x < 275+dx and 490+dy < y < 512+dy:
                rects.append((x,y))
            if width == 4 and 285+dx < x < 310+dx and 397+dy < y < 418+dy:
                rects.append((x,y))
    assert len(rects) == 1, (file,rects)
    labels[0] = rects[0]
    edges = set()
    physical = 0
    for t in tree.iter('stroke_path'):
        if [q.tag for q in t] not in [['moveto','lineto'],['moveto','curveto'],['moveto','curveto','curveto']]:
            continue
        ps = [p for q in t for p in points(t,q)]
        a,b = ps[0],ps[-1]
        def near(p):
            return [s for s,(x,y) in labels.items() if abs(y-p[1]) < .15 and abs(x-p[0]) < 11]
        aa,bb = near(a),near(b)
        if not aa or not bb:
            continue
        assert len(aa) == len(bb) == 1
        physical += 1
        chain = [aa[0],bb[0]]
        if [q.tag for q in t] == ['moveto','curveto','curveto']:
            mid = near(points(t,t[1])[-1])
            assert len(mid) <= 1
            if mid:
                chain = [aa[0],mid[0],bb[0]]
        if len(ps) == 2:
            vx,vy = b[0]-a[0],b[1]-a[1]
            norm = vx*vx+vy*vy
            inside = []
            for s,(x,y) in labels.items():
                z = ((x-a[0])*vx+(y-a[1])*vy)/norm
                if .02 < z < .98 and abs((x-a[0])*vy-(y-a[1])*vx)/norm**.5 < .15:
                    if s not in chain:
                        inside.append((z,s))
            chain = [aa[0]] + [s for _,s in sorted(inside)] + [bb[0]]
        for u,v in zip(chain,chain[1:]):
            assert (u,v) not in edges, (file,u,v)
            edges.add((u,v))
    expected = set()
    for s in labels:
        if not s:
            continue
        i = s.bit_length()-1
        if width == 8:
            expected |= {(s,s^(1<<i)^(1<<j)) for j in range(i) if s>>j&1}
        else:
            rest=s^(1<<i)
            expected |= {(s,t) for t in range(rest+1) if t&rest==t}
    missing, extra = expected-edges, edges-expected
    if width == 8:
        # Both source figures send 01111011 to 00101101 instead of 00101011.
        assert missing == {(123,43)} and extra == {(123,45)}, (file,missing,extra)
    else:
        assert not missing and not extra, (file,missing,extra)
    assert len(edges) == (97 if width == 8 else 21)
    return dict(labels={format(s,f'0{width}b'):xy for s,xy in labels.items()},
                edges=sorted((format(u,f'0{width}b'),format(v,f'0{width}b')) for u,v in edges),
                semantic_arcs=len(edges),physical_source_strokes=physical,
                missing=sorted((format(u,f'0{width}b'),format(v,f'0{width}b')) for u,v in missing),
                extra=sorted((format(u,f'0{width}b'),format(v,f'0{width}b')) for u,v in extra))


def circular_families(n):
    def mask(xs,ys):
        return sum(1<<(2*(i-1)) for i in xs)+sum(1<<(2*(i-1)+1) for i in ys)
    groups={}
    def put(kind,xs,ys,pivot,updates,branches):
        s=mask(xs,ys)
        v=dict(pivot=pivot,updates=updates,branches=branches)
        if s in groups:
            assert groups[s]['expected'] == v
            groups[s]['families'].append(kind)
        else:
            groups[s]=dict(families=[kind],expected=v)
    put('root',range(1,n+1),range(1,n+1),0,13,3)
    put('B+',range(2,n+1),[1]+list(range(3,n+1)),1,7 if n==3 else 8,2)
    put('B-',range(2,n+1),range(1,n),1,7 if n==3 else 8,2)
    for b in [n,n-1]:
        for a in range(2,b+1):
            m=b-a+1
            put(f'P({a},{b})',range(a,b+1),range(a,b+1),2*(a-1),3 if m==1 else 7 if m==2 else 8,1 if m==1 else 2)
        for a in range(2,b):
            m=b-a
            put(f'Q({a},{b})',range(a+1,b+1),[a]+list(range(a+2,b+1)),2*a-1,3 if m==1 else 4,1)
    for a in range(2,n):
        m=n-a
        cost=3 if m==1 else 4 if m==2 else 5
        put(f'A+({a})',range(a,n),range(a+1,n+1),2*(a-1),cost,1)
        put(f'A-({a})',range(a+1,n+1),range(a,n),2*a-1,cost,1)
    return groups


def main():
    assert not (OUT/'source-checked.json').exists()
    start=time.monotonic()
    cases=read(OUT/'cases-checked.json')
    assert sha(ROOT/'check_zdd251_260_cases.py') == cases['checker_sha256']
    for p,h in cases['artifact_hashes'].items():
        assert sha(ROOT/p)==h,p
    figures={v:figure(v+'.xml',w,dx,dy) for v,w,dx,dy in [
        ('original-141',8,0,0),('draft-63',8,22.08,108.66),
        ('original-501',4,0,0),('draft-191',4,22.08,108.66)]}
    families=[]
    for n in range(3,25):
        accepted=read(OUT/f'circular260-{n}.json')['model']
        expected=circular_families(n)
        actual={int(s):v for s,v in accepted['states'].items()}
        assert set(expected)==set(actual),(n,set(expected)-set(actual),set(actual)-set(expected))
        for s,v in actual.items():
            assert expected[s]['expected']==dict(pivot=v['pivot'],updates=v['updates'],branches=len(v['branches'])),(n,s)
        stats=accepted['stats']
        assert stats['signatures']==6*n-9 and stats['nodes']==8*n-9
        assert stats['updates']==(46 if n==3 else 34*n-58)
        families.append(dict(n=n,nonzero_states=len(expected),family_memberships=sum(len(v['families']) for v in expected.values()),
                             repeated_state='Q(n-1,n)=A-(n-1)',stats=stats))
    f=[0,1]
    for _ in range(1001):
        f.append(f[-1]+f[-2])
    def v(n): return ((n-5)*f[n+1]+2*(n+1)*f[n])//5
    def w(n): return ((5*n*n+7*n+25)*f[n+1]-6*(n+1)*f[n])//25
    bizarre=[]
    for q in cases['cases']:
        if not q['case'].startswith('bizarre'):
            continue
        a,b=q['q'],q['r'];k=min(2*a+1,2*b-1)
        expected=dict(count=factorial(2*a)*factorial(2*b)//(2**(a+b)*factorial(a)*factorial(b)),
                      nodes=(v(2*a)+3)+(v(2*b)+3)-1,
                      signatures=f[2*a+1]+f[2*b+1]+f[k+1],
                      updates=(w(2*a)-1)+(w(2*b)-1)+w(k)+(2*a+2*b+4))
        assert expected==q['stats'],q
        bizarre.append(dict(q=a,r=b,stats=expected,printed_composed_size=v(2*a)+v(2*b)+6))
    asym=[]
    with localcontext() as c:
        c.prec=50
        for n in [100,1000]:
            exact=v(n)+3
            asym.append(dict(n=n,exact_nodes=str(exact),printed=str(Decimal(n)*f[n+1]/5),
                             correct_asymptotic=str(Decimal(n)*f[n+1]/Decimal(5).sqrt()),
                             ratio_to_printed=str(Decimal(exact)/(Decimal(n)*f[n+1]/5))))
    assert factorial(16)//(2**8*factorial(8))==2027025
    assert factorial(32)//(2**16*factorial(16))==191898783962510625
    numeric=dict(matchings16=2027025,matchings32=191898783962510625,zdd16=v(16)+3,zdd32=v(32)+3)
    assert numeric['zdd16']==10228 and round(numeric['zdd32']/1000000)==48
    accepted=['results/zdd_counts/formulas.json','results/zdd_counts/colored-random.json',
              'results/zdd_counts/algebra.json','check_zdd_counts.py','ZDD_COUNT_NOTES.md',
              'MATCHING199_201_SOURCE_NOTES.md','results/circular_matching.json']
    assert len(read(ROOT/accepted[0]))==48 and len(read(ROOT/accepted[1]))==300
    save(OUT/'source-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),
         elapsed_seconds=time.monotonic()-start,figures=figures,circular_families=families,bizarre=bizarre,
         asymptotic=asym,numeric_examples=numeric,new_solver_calls=0,old_censuses_repeated=0,
         accepted_hashes={p:sha(ROOT/p) for p in accepted},
         current_hashes={str(p.relative_to(ROOT)):sha(p) for p in OUT.glob('*.xml')} |
                       {str((OUT/'cases-checked.json').relative_to(ROOT)):sha(OUT/'cases-checked.json')}))
    print('PASS source figures:97+21 semantic arcs per version; general families match22 saved circular cases.')
    print(numeric)


if __name__=='__main__':
    main()

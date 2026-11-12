"""Independent enumeration by touching disjoint tiles, without delta matching."""
from check_pentomino_bipairs import *

def freeze(v):return tuple(freeze(x) for x in v) if isinstance(v,list) else v

def main():
    prior=json.loads((OUT/'catalog.json').read_text());expected={tuple(x['pieces'])+(freeze(x['covers']),) for x in prior['catalog']}
    expected_holes={tuple(x['pieces'])+(freeze(x['covers']),) for x in prior['excluded_with_holes']}
    actual=set();holed=set();placements=0;regions_count=0
    for a,b in combinations(SHAPES,2):
        regions=defaultdict(set)
        for aa,bb in product(orientations(SHAPES[a]),orientations(SHAPES[b])):
            A=set(aa)
            offsets={(r-u+dr,c-v+dc) for r,c in aa for u,v in bb for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]}
            for dr,dc in offsets:
                B={(r+dr,c+dc) for r,c in bb}
                if A&B:continue
                region=A|B;r0=min(r for r,c in region);c0=min(c for r,c in region)
                region=tuple(sorted(shift(region,r0,c0)));cover=(tuple(sorted(shift(A,r0,c0))),tuple(sorted(shift(B,r0,c0))))
                regions[region].add(cover);placements+=1
        regions_count+=len(regions)
        for region,covers in regions.items():
            for first,second in combinations(covers,2):
                key=(a,b,canonical_pair(set(first[0]),set(first[1]),set(second[0]),set(second[1])))
                (actual if hole_free(set(region)) else holed).add(key)
    assert actual==expected and holed==expected_holes
    classes=Counter();participants=set();symmetries=[]
    for a,b,pair in sorted(actual):
        participants|={a,b};region=set(pair[0][0])|set(pair[0][1]);normal=normalized(region)
        symmetry=[g for g in range(8) if normalized(transform(region,g))==normal]
        kind='axial' if any(g in symmetry for g in [4,6]) else 'diagonal' if any(g in symmetry for g in [5,7]) else 'asymmetric'
        if kind=='asymmetric':assert symmetry==[0]
        classes[kind]+=1;symmetries.append(dict(pieces=[a,b],region_symmetry=symmetry,kind=kind))
    assert participants==set(SHAPES) and classes==dict(axial=18,diagonal=14,asymmetric=2)
    result=dict(disjoint_touching_placements=placements,translated_regions=regions_count,catalog_count=len(actual),excluded_holes=len(holed),
                exact_catalog_agreement=True,symmetry_classes=dict(classes),entries=symmetries)
    (OUT/'independent.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='entries'}))
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1150" viewBox="0 0 1200 1150">','<rect width="1200" height="1150" fill="white"/>',
         '<text x="20" y="28" font-family="sans-serif" font-size="21">All 34 hole-free exchanges of two distinct pentominoes</text>']
    for z,(a,b,pair) in enumerate(sorted(actual)):
        x=15+(z%5)*240;y=55+(z//5)*155
        region=set(pair[0][0])|set(pair[0][1]);H=max(r for r,c in region)+1;W=max(c for r,c in region)+1;s=min(16,98/max(H,W))
        svg.append(f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="14">{z+1}: {a} / {b}</text>')
        for h,cover in enumerate(pair):
            for color,tile in zip(['#9dc9ec','#edb482'],cover):
                for r,c in tile:svg.append(f'<rect x="{x+h*118+c*s}" y="{y+15+r*s}" width="{s}" height="{s}" fill="{color}" stroke="#333" stroke-width=".6"/>')
    svg.append('</svg>');(OUT/'catalog.svg').write_text('\n'.join(svg)+'\n')

if __name__=='__main__':main()

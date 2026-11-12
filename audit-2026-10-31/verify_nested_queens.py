"""Recheck archived witnesses and classify both queens and collapsed blocks."""
from check_nested_queens import *

def signature(p,k,resources=True):
    blocks=occurrences(p,k);rows={i for r,c in blocks for i in range(r,r+k)}
    b=tuple((r,c,tuple(sorted(i+p[i] for i in range(r,r+k))),tuple(sorted(i-p[i] for i in range(r,r+k)))) for r,c in blocks) if resources else tuple(blocks)
    return b,tuple((r,c) for r,c in enumerate(p) if r not in rows)

def main():
    results=[];witnesses=[]
    for n,k,t in [(16,5,2),(20,5,4),(22,6,2)]:
        base=OUT/f'independent-n{n}-q{k}-t{t}'
        qs=set(tuple(json.loads(line)) for line in base.with_suffix('.jsonl').read_text().splitlines())
        for q in qs:assert len(q)==n and valid(list(enumerate(q))) and len(occurrences(q,k))==t and orbit(q)<=qs
        representatives=sorted({min(orbit(q)) for q in qs})
        resources={signature(q,k) for q in qs};resource_reps={min(signature(a,k) for a in orbit(q)) for q in qs}
        layouts={signature(q,k,False) for q in qs};layout_reps={min(signature(a,k,False) for a in orbit(q)) for q in qs}
        result=dict(n=n,k=k,t=t,positions=len(qs),D4_classes=len(representatives),
                    D4_orbit_size_histogram=dict(Counter(len(orbit(q)) for q in representatives)),
                    collapsed_positions=len(resources),collapsed_D4_classes=len(resource_reps),
                    layouts=len(layouts),layout_D4_classes=len(layout_reps),representatives=representatives)
        results.append(result)
        if n==16:
            bylayout={}
            for q in sorted(qs):bylayout.setdefault(min(signature(a,k,False) for a in orbit(q)),q)
            assert len(bylayout)==5
            for q in bylayout.values():witnesses.append(dict(columns_1based=[c+1 for c in q],blocks_top_left_1based=[(r+1,c+1) for r,c in occurrences(q,k)]))
    (OUT/'classification.json').write_text(json.dumps(results,indent=2)+'\n')
    (OUT/'five-distinct-layouts.json').write_text(json.dumps(witnesses,indent=2)+'\n')
    # A small independently inspectable counterexample: even after forgetting
    # all internal block patterns, these five configurations are inequivalent.
    for a in witnesses:
        for b in witnesses:
            if a is b:continue
            pa=tuple(c-1 for c in a['columns_1based']);pb=tuple(c-1 for c in b['columns_1based'])
            assert signature(pa,5,False) not in {signature(q,5,False) for q in orbit(pb)}
    svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1050" height="750" viewBox="0 0 1050 750">',
         '<rect width="1050" height="750" fill="white"/>',
         '<text x="24" y="30" font-family="sans-serif" font-size="20">Five inequivalent Q16 layouts, each containing two Q5 blocks</text>']
    for z,w in enumerate(witnesses):
        x=25+(z%3)*345;y=65+(z//3)*345;s=18
        svg.append(f'<text x="{x}" y="{y-10}" font-family="sans-serif" font-size="17">{chr(65+z)}</text>')
        for r,c in w['blocks_top_left_1based']:svg.append(f'<rect x="{x+(c-1)*s}" y="{y+(r-1)*s}" width="{5*s}" height="{5*s}" fill="#dceafa"/>')
        for i in range(17):
            svg.append(f'<path d="M{x+i*s},{y}v{16*s} M{x},{y+i*s}h{16*s}" stroke="#777" stroke-width="0.6"/>')
        for r,c in enumerate(w['columns_1based']):svg.append(f'<circle cx="{x+(c-.5)*s}" cy="{y+(r+.5)*s}" r="4.5" fill="#16344c"/>')
    svg.append('</svg>');(OUT/'five-distinct-layouts.svg').write_text('\n'.join(svg)+'\n')
    print(json.dumps([{k:v for k,v in d.items() if k!='representatives'} for d in results],indent=2))

if __name__=='__main__':main()

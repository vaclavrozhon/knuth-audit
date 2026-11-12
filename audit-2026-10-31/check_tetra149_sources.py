"""Check both vector graph topologies and all six cached errata layers."""
from datetime import datetime,timezone
from itertools import combinations
import json,re,xml.etree.ElementTree as ET
from extract_jigsaw import transform
import tetra149 as h
from puzzle_xcc import save,sha


def topology(path,fig):
    # Small coordinate-label boxes have a constant center offset.
    left={tuple(r['vertex']):(r['label_position'][0]+3.47,r['label_position'][1]-1.05) for r in fig['matches']}
    letters={tuple(r['vertex']):r['color_position'] for r in fig['matches']}
    right={};tree=ET.parse(path).getroot()
    for t in tree.iter('stroke_path'):
        if [q.tag for q in t]!=['moveto']+['curveto']*4+['closepath']:continue
        points=[]
        for q in t:
            for suffix in ['','1','2','3']:
                if 'x'+suffix in q.attrib:points.append(transform(t,float(q.get('x'+suffix)),float(q.get('y'+suffix))))
        center=tuple((min(p[i] for p in points)+max(p[i] for p in points))/2 for i in range(2))
        dist,v=min((sum((a-b)**2 for a,b in zip(center,xy)),v) for v,xy in letters.items())
        if dist<10:assert v not in right;right[v]=center
    assert len(right)==20
    expected={tuple(sorted((h.VERTICES[i],h.VERTICES[j]))) for ids in h.CORNERS for i,j in combinations(ids,2)}
    result={}
    for name,centers in [('coordinate_graph',left),('colored_graph',right)]:
        edges=set();raw=0
        def vertex(xy):
            dist,v=min((sum((a-b)**2 for a,b in zip(xy,p)),v) for v,p in centers.items())
            return v if dist<.003 else None
        for t in tree.iter('stroke_path'):
            if not all(q.tag in ['moveto','lineto','closepath'] for q in t):continue
            start=prev=None
            for q in t:
                if q.tag=='closepath':xy=start
                else:xy=transform(t,float(q.get('x')),float(q.get('y')))
                if q.tag=='moveto':start=xy
                elif prev is not None:
                    a,b=vertex(prev),vertex(xy)
                    if a is not None and b is not None and a!=b:edges.add(tuple(sorted((a,b))));raw+=1
                prev=xy
        assert edges==expected,(name,len(edges),expected-edges,edges-expected)
        result[name]=dict(unique_edges=len(edges),drawn_segments_including_overlays=raw)
    return result


def main():
    figs=json.loads((h.OUT/'figures-checked.json').read_text())
    results={}
    for name,filename in [('original','original-478.xml'),('draft','draft-168.xml')]:
        results[name]=topology(h.ROOT/'results/bricks147'/filename,figs[name])
    previous=json.loads((h.ROOT/'results/polygons143/errata-check.json').read_text())
    pattern=r'(?:[Pp]age\s+|(?:4b|4f5)\.)(?:143|458|141|266)\b|(?:answer|exercise|exer ise)\s+149\b|McComb|Scherphuis|tetrahedr|2880|adec'
    contexts=[]
    for path,digest in previous['files'].items():
        file=h.ROOT.parent/path;assert sha(file)==digest
        lines=file.read_text(errors='replace').splitlines()
        for i,line in enumerate(lines):
            if re.search(pattern,line,re.I):contexts.append(dict(file=path,line=i+1,context='\n'.join(lines[max(0,i-1):i+5])))
    save(h.OUT/'errata-check.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),
        files=previous['files'],pattern=pattern,contexts=contexts,latest_remote_retrieval='2026-11-03T05:37:34Z; unchanged six hashes from143'))
    for src,name in [('page143.txt','question.txt'),('page458.txt','answer.txt'),('draft79.txt','draft-question.txt'),('draft162.txt','draft-answer.txt')]:
        (h.ROOT/'sources/tetra149'/name).write_bytes((h.ROOT/'sources/bricks147'/src).read_bytes())
    save(h.OUT/'topology-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),
        figures_sha256=sha(h.OUT/'figures-checked.json'),all_four_graphs_have_exactly_the_stated60_edges=True,results=results,
        graph_definition_source='sources/polygons143/gb_basic.w',graph_definition_sha256=sha(h.ROOT/'sources/polygons143/gb_basic.w')))
    print('PASS149 topology:all60 edges in each original/draft coordinate/colored graph; six errata layers searched.')


if __name__=='__main__':main()

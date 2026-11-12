"""Short new wording witnesses and arithmetic bounds; no accepted searches rerun."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import json
import os
import time
from check_zdd261_265_cases import path_family
from puzzle_xcc import save, sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/zdd261_264'


def read(p):return json.loads(Path(p).read_text())


def main():
    assert not (OUT/'claims-checked.json').exists()
    started=time.monotonic();accepted={}
    for name,program in [('cases','check_zdd261_265_cases.py'),('figures','check_zdd261_262_figures.py')]:
        data=read(OUT/(name+'-checked.json'))
        assert data['checker_sha256']==sha(ROOT/program)
        for p,h in data['artifact_hashes'].items():assert sha(ROOT/p)==h,p
        accepted[str((OUT/(name+'-checked.json')).relative_to(ROOT))]=sha(OUT/(name+'-checked.json'))
    # Distinguish the literal digraph with boundary arcs from actual source vertices.
    literal=read(OUT/'literal-boundary-paths.json')['cases'] if (OUT/'literal-boundary-paths.json').exists() else []
    for n in ([] if literal else [3,4]):
        vertices=[(i,j) for i in range(n+1) for j in range(i,n+1) if (i,j) not in [(0,0),(0,n),(n,n)]]
        sources=[(0,j) for j in range(1,n)]+[(i,n) for i in range(1,n)]
        sinks=[(i,i) for i in range(1,n)]
        edges=[(u,v) for u in vertices for v in [(u[0]+1,u[1]),(u[0],u[1]-1)] if v in vertices]
        family=path_family(vertices,edges,sources,sinks,n-1)
        literal.append(dict(n=n,count=len(family),incoming_source_arcs=[(u,v) for u,v in edges if v in sources],arc_families=sorted(family)))
    save(OUT/'literal-boundary-paths.json',dict(cases=literal,intended_counts_from_previously_accepted_cases=[5,16],interpretation='Allow a path to start at any S vertex and to pass through another S vertex; terminal diagonal vertices are all used. These are not sources in the literal digraph.'))
    # No enumeration is needed for the two paths through a three-vertex DAG.
    save(OUT/'main-options-witness.json',dict(vertices=['s','v','t'],arcs=[['s','t'],['s','v'],['v','t']],
         primary=['s+','v-','v+','t-'],arc_options=[['s+','t-','s:1','t:1'],['s+','v-','s:1','v:1'],['v+','t-','v:1','t:1']],
         needed_slack=[['v-','v:0'],['v+','v:0']],all_paths=[['s','t'],['s','v','t']],
         arc_only_paths=[['s','v','t']],reason='The direct path leaves v- and v+ uncovered. Literal color 0 is a matchable color, not an uncolored occurrence.'))
    # A conservative bound from actual DLX2 structs, and the <=10 occurrences
    # in every option of answer430(d): cell rows have5, absorption rows<=10.
    bounds=[]
    for label,p,s,o,printed in [('unmodified',1165,66,4889,509),('modified',1187,66,5143,537)]:
        upper=16*(11*o+2*(p+s+2))+4*p+128
        assert upper<1000000 and upper<printed*1000000
        bounds.append(dict(case=label,primary=p,secondary=s,options=o,maximum_occurrences_per_option=10,
                           conservative_bytes_upper_bound=upper,printed_megabytes=printed,
                           correction='MB to KB; exact rounded KB figure has not been independently reproduced'))
    save(OUT/'kakuro-memory-bound.json',dict(cases=bounds,formula='16*(11*options+2*(items+2))+4*primary+128',source='sources/knuth-programs/dlx2.w, bytes calculation and 16-byte item/node structures; answer430(d)',searches_run=0))
    original=read(OUT/'original-figures.json');draft=read(OUT/'draft-figures.json')
    # Exact proposed repair: one bend (13.5,1) should be (13.5,2).
    repairs=[]
    normalized={}
    for label,data in [('original',original),('draft',draft)]:
        def quantize(p):
            q=tuple(round(x*2)/2 for x in p)
            assert max(abs(x-y) for x,y in zip(p,q))<.025
            return q
        def canonical(path):
            q=[]
            for p in map(quantize,path):
                while len(q)>=2 and (q[-1][0]-q[-2][0])*(p[1]-q[-1][1])==(q[-1][1]-q[-2][1])*(p[0]-q[-1][0]):q.pop()
                q.append(p)
            return min(tuple(q),tuple(reversed(q)))
        normalized[label]={c:sorted(canonical(p) for p in paths) for c,paths in data['randall']['paths'].items()}
        matches=[]
        for index,p in enumerate(data['randall']['paths']['0 0 1']):
            for j in range(1,len(p)-1):
                if quantize(p[j])==(13.5,1) and {quantize(p[j-1]),quantize(p[j+1])}=={(13.5,4),(12.5,1)}:
                    matches.append((index,j,p[j]))
        assert len(matches)==1,matches
        index,j,point=matches[0]
        # After the replacement, the horizontal tile centre (13,1.5)
        # lies halfway on its blue segment; the adjoining vertical segment remains.
        repaired=[(12.5,1),(13.5,2),(13.5,4)]
        assert tuple((x+y)/2 for x,y in zip(repaired[0],repaired[1]))==(13,1.5)
        repairs.append(dict(version=label,path_index_zero_based=index,bend_index_zero_based=j,old=point,correct=(13.5,2),local_correct_polyline=repaired))
    assert normalized['original']==normalized['draft']
    save(OUT/'randall-repair.json',dict(repairs=repairs))
    old_files=['TILING_ZDD_NOTES.md','results/aztec_zdd_validation.json','results/aztec_zdd.json','results/aztec_linearity.json','results/hexagon_zdd.json','results/hexagon_linearity.json','results/rectangle_asymptotic.json',
      'QUEEN230_236_SOURCE_NOTES.md','TRIANGLES124_126_NOTES.md','UNIVERSAL_CYCLES_NOTES.md','sources/knuth-programs/dlx2.w','sources/knuth-programs/dlx3.w','sources/knuth-programs/dlx6.w']
    for p in old_files:
        if (ROOT/p).exists():accepted[p]=sha(ROOT/p)
    files=[OUT/p for p in ['literal-boundary-paths.json','main-options-witness.json','kakuro-memory-bound.json','randall-repair.json']]
    save(OUT/'claims-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),elapsed_seconds=time.monotonic()-started,nice=os.getpriority(os.PRIO_PROCESS,0),accepted_hashes=accepted,artifact_hashes={str(p.relative_to(ROOT)):sha(p) for p in files},old_searches_repeated=0))
    print(json.dumps(dict(literal_counts=[(q['n'],q['count']) for q in literal],memory_bounds=bounds,elapsed_seconds=time.monotonic()-started),indent=2))


if __name__=='__main__':main()

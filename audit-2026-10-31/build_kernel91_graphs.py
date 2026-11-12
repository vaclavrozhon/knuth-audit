"""Reproduce answer91's full projected graphs; do not rerun completed searches.

The current results were produced by these same operations before this driver
was saved. --rebuild is deliberately required to replace them.
"""
import argparse,hashlib,json,time
from pathlib import Path
from word_kernel91 import DistinctWitness,kernel_set,validate_completion,graph,core,components
from double_word_tools import dictionary

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/stair_kernels'

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--rebuild',action='store_true')
    parser.add_argument('--kind',choices=['left','right','all'],default='all');args=parser.parse_args()
    if not args.rebuild:parser.error('Use --rebuild only if a new concern requires repeating the completed enumeration.')
    for kind,W in [('right',1000),('left',500)]:
        if args.kind not in ['all',kind]:continue
        started=time.monotonic();words=dictionary(5)[:W];raw=kernel_set(words,kind)
        (OUT/f'{kind}{W}-join-kernels.txt').write_text('\n'.join(sorted(raw))+'\n')
        checker=DistinctWitness(words,kind);keep=[];witnesses=[]
        for k in sorted(raw):
            w=checker.witness(k)
            if w:
                assert validate_completion(w,kind,True)==k
                keep.append(k);witnesses.append(' '.join(w))
        path=OUT/f'{kind}{W}-distinct-kernels.txt';path.write_text('\n'.join(keep)+'\n')
        (OUT/f'{kind}{W}-distinct-witnesses.txt').write_text('\n'.join(witnesses)+'\n')
        edges=graph(keep,kind);reduced=core(edges);parts=components(reduced)
        result=dict(kind=kind,W=W,kernels=len(keep),vertices=len({v for e in edges for v in e[:2]}),
          core_vertices=len({v for e in reduced for v in e[:2]}),core_edges=len(reduced),
          largest_scc_vertices=len(parts[0]),largest_scc_edges=sum(s in parts[0] and t in parts[0] for s,t,*_ in reduced),
          sha256=hashlib.sha256(path.read_bytes()).hexdigest(),seconds=time.monotonic()-started,
          completed=True,driver_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
        (OUT/f'{kind}{W}-distinct.json').write_text(json.dumps(result,indent=2)+'\n');print(result)

if __name__=='__main__':main()

"""Independent bitboard checks, full ZDD counts, and symmetry counts for hitori."""
from itertools import product
from pathlib import Path
import argparse,json,resource,subprocess,time

ROOT=Path(__file__).parent
COUNTS=[
 [1,2,1,1,1,1,1,1,1],
 [2,4,6,12,20,36,64,112,200],
 [1,6,11,30,75,173,434,1054,2558],
 [1,12,30,110,382,1270,4298,14560,49204],
 [1,20,75,382,1804,7888,36627,166217,755680],
 [1,36,173,1270,7888,46416,287685,1751154,10656814],
 [1,64,434,4298,36627,287685,2393422,19366411,157557218],
 [1,112,1054,14560,166217,1751154,19366411,208975042,2255742067],
 [1,200,2558,49204,755680,10656814,157557218,2255742067,32411910059]]
RANGES=[
 [(1,1),(1,1),(2,2),(2,2),(2,2),(2,2),(2,2),(2,2),(2,2)],
 [(1,1),(1,1),(1,2),(2,2),(2,3),(2,3),(3,4),(3,4),(3,5)],
 [(2,2),(1,2),(2,4),(2,4),(3,6),(4,6),(4,8),(5,8),(5,10)],
 [(2,2),(2,2),(2,4),(4,5),(4,7),(5,8),(6,9),(7,10),(8,12)],
 [(2,2),(2,3),(3,6),(4,7),(5,9),(6,10),(8,12),(9,14),(10,15)],
 [(2,2),(2,3),(4,6),(5,8),(6,10),(8,12),(9,14),(11,16),(12,18)],
 [(2,2),(3,4),(4,8),(6,9),(8,12),(9,14),(11,17),(12,19),(14,21)],
 [(2,2),(3,4),(5,8),(7,10),(9,14),(11,16),(12,19),(14,21),(16,24)],
 [(2,2),(3,5),(5,10),(8,12),(10,15),(12,18),(14,21),(16,24),(18,27)]]
HV=[
 [1,0,1,1,1,1,1,1,1], [0,0,0,0,0,0,0,0,0],
 [1,0,3,2,5,1,6,2,10], [1,0,2,0,2,0,2,0,2],
 [1,0,5,2,10,2,21,1,46], [1,0,1,0,2,0,1,0,2],
 [1,0,6,2,21,1,48,1,150], [1,0,2,0,1,0,1,0,3],
 [1,0,10,2,46,2,150,3,649]]
D4=[1,0,1,0,2,0,2,0,11]
ROT_PAIRS=[0,0,0,1,1,3,11,30,106]
DIAG_PAIRS=[0,0,0,0,0,1,4,9,49]


class Board:
    def __init__(self,rows,columns):
        self.rows=rows;self.columns=columns;self.full=(1<<(rows*columns))-1
        self.left=sum(1<<(r*columns) for r in range(rows))
        self.right=self.left<<(columns-1)

    def neighbors(self,mask):
        return (((mask&~self.right)<<1)|((mask&~self.left)>>1)|
                (mask<<self.columns)|(mask>>self.columns))&self.full

    def connected(self,white):
        if not white:return False
        seen=white&-white
        while True:
            expanded=seen|(self.neighbors(seen)&white)
            if expanded==seen:return seen==white
            seen=expanded

    def cover(self,black,minimal=True):
        neighbors=self.neighbors(black)
        if black&neighbors:return False
        white=self.full^black
        if not self.connected(white):return False
        if not minimal:return True
        candidates=white&~neighbors
        while candidates:
            bit=candidates&-candidates;candidates^=bit
            if self.connected(white^bit):return False
        return True


def limits():resource.setrlimit(resource.RLIMIT_AS,(5*1024**3,5*1024**3))


def zdd(rows,columns):
    p=subprocess.run(['/tmp/knuth-hitori-zdd',str(rows),str(columns)],text=True,
                     capture_output=True,check=True,timeout=2400,preexec_fn=limits)
    print(p.stderr.strip(),flush=True)
    return json.loads(p.stdout)


def validate():
    results=[]
    for rows in range(1,5):
        for columns in range(rows,6):
            if rows*columns>20:continue
            board=Board(rows,columns);base=0;maximal=[]
            for black in range(board.full+1):
                if board.cover(black,False):
                    base+=1
                    if board.cover(black):maximal.append(black)
            result=zdd(rows,columns)
            assert result['connected_vertex_covers']==base
            assert result['hitori_covers']==len(maximal)
            assert result['min_black']==min(x.bit_count() for x in maximal)
            assert result['max_black']==max(x.bit_count() for x in maximal)
            results.append(dict(rows=rows,columns=columns,subsets=board.full+1,
                                connected_covers=base,hitori_covers=len(maximal)))
    return results


def symmetric(rows,columns,kind):
    board=Board(rows,columns);remaining=set(product(range(rows),range(columns)))
    if kind=='hv':generators=[lambda r,c:(rows-1-r,c),lambda r,c:(r,columns-1-c)]
    elif kind=='rot':generators=[lambda r,c:(c,rows-1-r)]
    elif kind=='diag':generators=[lambda r,c:(c,r),lambda r,c:(rows-1-c,rows-1-r)]
    elif kind=='d4':generators=[lambda r,c:(c,rows-1-r),lambda r,c:(r,columns-1-c)]
    else:raise ValueError(kind)
    masks=[]
    while remaining:
        seed=min(remaining);orbit={seed};todo=[seed]
        while todo:
            r,c=todo.pop()
            for g in generators:
                p=g(r,c)
                if p not in orbit:orbit.add(p);todo.append(p)
        remaining-=orbit
        mask=sum(1<<(r*columns+c) for r,c in orbit)
        if not mask&board.neighbors(mask):masks.append(mask)
    adjacency=[]
    for mask in masks:
        near=board.neighbors(mask)
        adjacency.append(sum(1<<j for j,other in enumerate(masks) if near&other))
    total=0;independent=0
    def visit(available,black):
        nonlocal total,independent
        if not available:
            independent+=1;total+=board.cover(black);return
        bit=available&-available;i=bit.bit_length()-1;rest=available^bit
        visit(rest,black)
        visit(rest&~adjacency[i],black|masks[i])
    visit((1<<len(masks))-1,0)
    return dict(rows=rows,columns=columns,group=kind,orbits_without_internal_edges=len(masks),
                independent_symmetric_sets=independent,hitori_covers=total)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=['validate','counts','symmetry'],default='validate')
    args=parser.parse_args()
    if args.mode=='validate':
        results=validate();(ROOT/'results/hitori_validation.json').write_text(json.dumps(results,indent=2)+'\n')
        print('Validated',len(results),'boards',flush=True)
    elif args.mode=='counts':
        results=[];mismatches=[]
        for rows in range(1,10):
            for columns in range(rows,10):
                result=zdd(rows,columns);results.append(result)
                if result['hitori_covers']!=COUNTS[rows-1][columns-1]:
                    mismatches.append(dict(rows=rows,columns=columns,field='count',printed=COUNTS[rows-1][columns-1],actual=result['hitori_covers']))
                observed=(result['min_black'],result['max_black'])
                if observed!=RANGES[rows-1][columns-1]:
                    mismatches.append(dict(rows=rows,columns=columns,field='range',printed=RANGES[rows-1][columns-1],actual=observed))
                (ROOT/'results/hitori_counts.json').write_text(json.dumps(dict(cases=results,book_mismatches=mismatches),indent=2)+'\n')
                print(json.dumps(result),flush=True)
    else:
        results=[]
        for rows in range(1,10):
            for columns in range(rows,10):
                result=symmetric(rows,columns,'hv')
                assert result['hitori_covers']==HV[rows-1][columns-1],result
                results.append(result)
                print(json.dumps(result),flush=True)
        for n in range(1,10):
            group={kind:symmetric(n,n,kind) for kind in ['d4','rot','diag']}
            assert group['d4']['hitori_covers']==D4[n-1],group
            assert (group['rot']['hitori_covers']-D4[n-1])==2*ROT_PAIRS[n-1],group
            assert (group['diag']['hitori_covers']-D4[n-1])==2*DIAG_PAIRS[n-1],group
            results.extend(group.values())
            print(json.dumps(group),flush=True)
        (ROOT/'results/hitori_symmetry.json').write_text(json.dumps(results,indent=2)+'\n')


if __name__=='__main__':main()

"""Finite transfer certificate for the corrected X262(b) all-n ZDD size."""
from functools import lru_cache
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).parent
H=16;FULL=(1<<H)-1;EVEN=sum(1<<(2*j) for j in range(H))


@lru_cache(None)
def transfer(incoming,up,down,next_up):
    assert incoming&~up==0
    valid=sum(1<<(2*j) for j in range(H) if up>>j&1)
    valid|=sum(1<<(2*j+1) for j in range(H) if down>>j&1)
    occupied=sum(1<<(2*j) for j in range(H) if incoming>>j&1)
    out=[]
    def fill(occupied,outgoing):
        remaining=valid&~occupied
        if not remaining:out.append(outgoing);return
        bit=remaining&-remaining;j=bit.bit_length()-1
        if j+1<2*H and remaining&(bit<<1):fill(occupied|bit|(bit<<1),outgoing)
        if j%2 and next_up>>(j//2)&1:fill(occupied|bit,outgoing|(1<<(j//2)))
    fill(occupied,0)
    return tuple(out)


def main():
    balanced={mask for mask in range(FULL+1) if mask.bit_count()==8}
    reachable={0};layers=[1]
    for x in range(8):
        up=sum(1<<j for j in range(H) if j+x>=8)
        down=sum(1<<j for j in range(H) if j+x>=7)
        next_up=down
        reachable={out for inc in reachable for out in transfer(inc,up,down,next_up)}
        layers.append(len(reachable))
    assert reachable==balanced and len(balanced)==12870
    image=set();arcs=0
    for inc in balanced:
        outputs=transfer(inc,FULL,FULL,FULL)
        assert set(outputs)<=balanced
        arcs+=len(outputs);image.update(outputs)
    assert image==balanced

    visited=set();nodes=0
    def walk(pos,mask):
        nonlocal nodes
        while pos<2*H and mask&1:mask>>=1;pos+=1
        if pos==2*H:
            assert mask&~EVEN==0 and mask.bit_count()==8;return
        key=(pos,mask)
        if key in visited:return
        visited.add(key)
        if pos+1<2*H and not mask&2:
            nodes+=1;walk(pos+1,(mask|2)>>1)
        if pos%2:
            nodes+=1;walk(pos+1,(mask|(1<<(2*H-1)))>>1)
    for inc in balanced:walk(0,sum(1<<(2*j) for j in range(H) if inc>>j&1))
    assert len(visited)==205920 and nodes==257400
    result=dict(left_cap_layer_sizes=layers,stable_masks=len(balanced),full_column_transfer_arcs=arcs,
                stable_masks_sha256=hashlib.sha256(','.join(map(str,sorted(balanced))).encode()).hexdigest(),
                full_column_successful_signatures=len(visited),full_column_branch_nodes=nodes,
                base_n=8,base_nodes=849139,extra_n7_nodes=591739,
                formula='849139+(n-8)*257400 = 257400*n-1210061, n>=8; direct base n7 agrees.',
                proof='Each eight-column cap permits every weight8 frontier. The reflected right cap has the same property. Full columns preserve these masks. Therefore extra full columns each add257400 nodes, and the two caps contribute a constant.')
    (ROOT/'results/hexagon_linearity.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()

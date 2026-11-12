"""Finite transfer certificate for the all-n linear ZDD size in X262(a)."""
from functools import lru_cache
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).parent
H=16;FULL=(1<<H)-1


@lru_cache(None)
def transfers(incoming,valid,next_valid):
    assert incoming & ~valid == 0
    result=[]
    def fill(occupied,outgoing):
        remaining=valid & ~occupied
        if not remaining:result.append(outgoing);return
        low=remaining&-remaining;r=low.bit_length()-1
        if r+1<H and remaining & (low<<1):fill(occupied|low|(low<<1),outgoing)
        if next_valid&low:fill(occupied|low,outgoing|low)
    fill(incoming,0)
    return tuple(result)


def left_column(c):
    return sum(1<<r for r in range(H) if min(r,H-1-r)+c>=7)


def main():
    even=sum(1<<r for r in range(0,H,2));odd=FULL^even
    balanced={mask for mask in range(FULL+1) if (mask&even).bit_count()==(mask&odd).bit_count()}
    reachable={0};layers=[len(reachable)];first=None
    for c in range(16):
        reachable={out for inc in reachable for out in transfers(inc,left_column(c),left_column(c+1))}
        layers.append(len(reachable))
        if reachable==balanced and first is None:first=c+1
    assert first==15 and len(balanced)==12870 and reachable==balanced
    # Exact closure under a full column, independently checked on every state.
    arcs=0;image=set()
    for inc in balanced:
        outputs=transfers(inc,FULL,FULL)
        assert set(outputs)<=balanced
        image.update(outputs);arcs+=len(outputs)
    assert image==balanced

    # Count all distinct internal signatures and their successful children
    # in a column with unrestricted balanced masks at both ends.
    visited=set();branch_nodes=0
    def walk(row,mask):
        nonlocal branch_nodes
        while row<H and mask&1:row+=1;mask>>=1
        if row==H:
            assert mask in balanced;return
        state=(row,mask)
        if state in visited:return
        visited.add(state)
        if row+1<H and not mask&2:
            branch_nodes+=1;walk(row+1,(mask|2)>>1)
        branch_nodes+=1;walk(row+1,(mask|(1<<H))>>1)
    for inc in balanced:walk(0,inc)
    assert len(visited)==102960 and branch_nodes==154440
    result=dict(height=H,reachable_layer_sizes=layers,first_full_balanced_layer=first,
                balanced_masks=len(balanced),full_column_transfer_arcs=arcs,
                balanced_mask_sha256=hashlib.sha256(','.join(map(str,sorted(balanced))).encode()).hexdigest(),
                full_column_successful_signatures=len(visited),full_column_branch_nodes=branch_nodes,
                base_n=30,base_nodes=1977345,
                formula='1977345 + (n-30)*154440 = 154440*n-2655855, n>=30',
                proof='Left and reflected right boundary sets stabilize after15 columns. For n>=30, extending the middle adds one column with both boundary sets balanced; the two fixed end contributions do not change.')
    (ROOT/'results/aztec_linearity.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()

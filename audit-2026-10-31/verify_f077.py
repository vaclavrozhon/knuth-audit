"""Standalone short witness: the printed Langford sequence is not lex-max."""
import json
PRINTED=(16,14,15,9,6,13,5,7,12,10,11,6,5,9,8,7,14,16,15,13,10,12,11,8,4,1,3,1,2,4,3,2)
LARGER=(16,14,15,11,9,7,13,4,2,12,10,2,4,7,9,11,14,16,15,8,13,10,12,5,6,1,3,1,8,5,3,6)
def validate(a):
    assert len(a)==32
    pairs={i:[j+1 for j,v in enumerate(a) if v==i] for i in range(1,17)}
    assert all(len(p)==2 and p[1]-p[0]==i+1 for i,p in pairs.items())
    return pairs
def verify():
    p,q=validate(PRINTED),validate(LARGER)
    assert LARGER>PRINTED and LARGER[:3]==PRINTED[:3] and (LARGER[3],PRINTED[3])==(11,9)
    return dict(printed=PRINTED,larger=LARGER,printed_pairs=p,larger_pairs=q,first_difference_one_based=4,
        proves_printed_not_maximal=True,claims_new_global_maximum_without_previous_evidence=False)
if __name__=='__main__':print(json.dumps(verify(),indent=2))


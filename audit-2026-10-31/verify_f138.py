"""Standalone F138 certificate: five inequivalent2x2x4 bricks, all six outer colors.

Uses only the Python standard library, no solver, input files or search for
bricks. Positions are lexicographic(x,y,z), dimensions(2,2,4); face order
U,D,F,B,L,R. Only finite cube/box symmetry operations are enumerated.
"""
from collections import Counter
from itertools import permutations,product

COLORS='abcdef'
SIZE=(2,2,4)
DIR=((0,-1,0),(0,1,0),(-1,0,0),(1,0,0),(0,0,-1),(0,0,1))
POS=list(product(range(2),range(2),range(4)))
WITNESSES=[s.split() for s in [
    'abcdef abcefd aecbdf aecdfb bdcaef bdcefa edcbaf edcafb abdfec abefcd acbfde acdfeb bdafec bdefca cdbfae cdafeb',
    'abcdef abcefd aecbdf aecdfb bdcaef bdcefa edcbaf edcafb abdfec abefcd aebfdc aedfcb bdafec bdefca edbfac edafcb',
    'abcdef abcefd aecfdb aecdbf bdcaef bdcefa edcfab edcabf acdbef acebfd aefbdc aedbcf cdabef cdebfa edfbac edabcf',
    'abcdef abcefd aecfdb aecdbf bdcaef bdcefa edcfab edcabf afdbec afebcd acfbde acdbef fdabec fdebca cdfbae cdabef',
    'abcdef abcefd afcedb aecdbf bdcaef bdcefa fdceab edcabf acdbef acebfd afebdc aedbcf cdabef cdebfa fdebac edabcf']]


def operations():
    result=[]
    for p in permutations(range(3)):
        parity=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        for signs in product([-1,1],repeat=3):
            f=tuple(DIR.index(tuple(signs[j]*d[p[j]] for j in range(3))) for d in DIR)
            result.append((p,signs,f,parity*signs[0]*signs[1]*signs[2]))
    return result


OPS=operations()
ROT=[f for p,s,f,d in OPS if d==1]
BOX=[g for g in OPS if all(SIZE[i]==SIZE[g[0][i]] for i in range(3))]


def turn(w,perm):
    r=['?']*6
    for i,j in enumerate(perm):r[j]=w[i]
    return ''.join(r)


def cube_type(w):return min(turn(w,f) for f in ROT)


def normalize(row):
    rename=dict(zip(row[0],COLORS))
    return tuple(''.join(rename[c] for c in w) for w in row)


def action(row,op):
    p,signs,faces,det=op;transformed={}
    for xyz,w in zip(POS,row):
        target=tuple(xyz[p[i]] if signs[i]>0 else SIZE[i]-1-xyz[p[i]] for i in range(3))
        transformed[target]=turn(w,faces)
    return normalize([transformed[pos] for pos in POS])


def check(row):
    assert len(row)==16
    assert all(sorted(w)==list(COLORS) for w in row)
    assert len({cube_type(w) for w in row})==16,'A physical cube type was reused'
    cells=dict(zip(POS,row));outer={}
    for xyz,w in cells.items():
        for face,delta in enumerate(DIR):
            neighbor=tuple(a+b for a,b in zip(xyz,delta))
            if neighbor in cells:assert w[face]==cells[neighbor][face^1],'Mismatched contact'
            else:
                if face in outer:assert outer[face]==w[face],'Nonsolid exterior face'
                outer[face]=w[face]
    assert len(outer)==len(set(outer.values()))==6,'Exterior colors must all differ'
    images=[action(row,g) for g in BOX]
    return min(images),images.count(normalize(row))


def main():
    assert len(ROT)==24 and len(BOX)==16
    results=[check(row) for row in WITNESSES]
    # For each spatial operation exactly one global color permutation makes
    # the first cube abcdef. Thus these keys test every allowed equivalence,
    # without needing to loop over720 arbitrary color names.
    assert len({key for key,aut in results})==5
    hist=Counter(aut for key,aut in results)
    assert hist=={2:1,4:3,8:1},hist
    print('PASS: five valid pairwise inequivalent2x2x4 bricks with six distinct exterior colors.')
    print('Automorphism histogram(1,2,4,8):',(hist[1],hist[2],hist[4],hist[8]))
    print('The printed histogram(0,1,1,1) accounts for only three such classes.')


if __name__=='__main__':main()

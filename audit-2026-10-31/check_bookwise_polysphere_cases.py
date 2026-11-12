"""Small exact checks for the two specific suspected errors on pp.515/517.

This is not a polysphere census. Roof searches stop at the first witness.
"""
from fractions import Fraction as F
from itertools import permutations
import json


def matrix(rows, denominator=1):
    return [[F(x, denominator) for x in row] for row in rows]


I = matrix([[int(i == j) for j in range(4)] for i in range(4)])
T = matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]])
R = matrix([[1, -1, 1, 1], [1, 1, 1, -1], [-1, 1, 1, 1], [1, 1, -1, 1]], 2)
H = matrix([[5, -1, -1, 3], [-1, -1, 5, 3], [-1, 5, -1, 3], [3, 3, 3, -3]], 6)


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def product(*args):
    a = I
    for b in args:
        a = mul(a, b)
    return a


def image(a, i, j):
    return [a[k][i-1] - a[k][j-1] for k in range(4)]


def parity(p):
    return (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4))


def determinant(a):
    result = F(0)
    for p in permutations(range(4)):
        term = parity(p)
        for i in range(4):
            term *= a[i][p[i]]
        result += term
    return result


for a in (T, R, H):
    assert mul(a, list(zip(*a))) == I
    assert determinant(a) == 1 and all(sum(row) == 1 for row in a)
cases = {}
for name, a in [('TH', product(T,H)), ('HT2', product(H,T,T)),
                ('T2RT', product(T,T,R,T)), ('THR3T2', product(T,H,R,R,R,T,T)),
                ('HR', product(H,R)), ('TR', product(T,R))]:
    cases[name] = {f'e{i}{j}': image(a,i,j) for i,j in [(1,2),(1,3),(1,4),(3,4)]}
assert cases['TR']['e12'] == [1,-1,0,0]
assert cases['TR']['e13'] == [0,-1,1,0]
assert cases['TR']['e14'] == [0,-1,0,1]
assert cases['T2RT']['e12'] == [0,0,1,-1]


def roof(m, n, stretched):
    return frozenset((x+m-1-y,y+k,y) if stretched else (x,y+k,m-1-y)
                     for k in range(min(m,n)) for x in range(n-k) for y in range(m-k))


pieces = {'i': ['000','001','002','003'], 'j': ['000','001','002','012'],
          'n': ['000','001','011','012'], 'o': ['000','001','010','011'],
          'p': ['000','001','002','010']}


def placements(name, board):
    cells = [tuple(map(int,s)) for s in pieces[name]]
    cells = [(-sum(c),)+c for c in cells]
    result = set()
    # All pieces here are planar: reflected images also have proper-rotation realizations.
    for perm in permutations(range(4)):
        for sign in (-1,1):
            orient = [tuple(sign*c[perm[j]] for j in range(1,4)) for c in cells]
            for b in board:
                delta = tuple(b[j]-orient[0][j] for j in range(3))
                placed = frozenset(tuple(c[j]+delta[j] for j in range(3)) for c in orient)
                if placed <= board:
                    result.add(placed)
    return result


def one_witness(board):
    opts = {name: sorted(placements(name,board),key=lambda p:sorted(p)) for name in pieces}
    def search(uncovered, remaining):
        if not remaining:
            return {} if not uncovered else None
        choices = min(([ (name,p) for name in remaining for p in opts[name]
                        if cell in p and p <= uncovered ] for cell in sorted(uncovered)),key=len)
        for name,p in choices:
            tail = search(uncovered-p,remaining-{name})
            if tail is not None:
                return {name: sorted(p),**tail}
        return None
    return search(board,frozenset(pieces))


bad_roof = roof(7,2,True)
assert len(bad_roof) == 20 and not placements('i',bad_roof)
witnesses = {label: one_witness(board) for label,board in
             [('R2x7',roof(2,7,False)),('S2x7',roof(2,7,True))]}
assert all(witnesses.values())
print(json.dumps({'rotation_cases':cases,'S7x2_i_placements':0,
                  'corrected_roof_witnesses':witnesses},indent=2,default=str))

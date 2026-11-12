#!/usr/bin/env python3
"""Exact width≤10 column DP for62, with local triangle certificates.

Maximum512 boundary states; each transfer entry is a product of2x2
matrices. No enumeration of the2^85 or2^261 full edge assignments.
"""
from itertools import product
from decimal import Decimal,localcontext
from fractions import Fraction as F
import hashlib,json
from check_clasp_projection import ROOT
from check_polyhedra_fixed import clip


def local_tables():
    matrices={};rows=[]
    for x,y in product((0,1),repeat=2):
        k=[]
        for before in (0,1):
            row=[]
            for after in (0,1):
                allowed=[d for d in (0,1) if x+after+1-d in (1,2) and before+y+1-d in (1,2)]
                row.append(len(allowed));rows.append({'old_vertical':x,'new_vertical':y,'horizontal_before':before,
                                                    'horizontal_after':after,'allowed_diagonals':allowed})
            k.append(row)
        matrices[x,y]=k
    assert matrices=={(0,0):[[1,1],[1,2]],(0,1):[[1,2],[0,1]],(1,0):[[1,0],[2,1]],(1,1):[[2,1],[1,1]]}
    return matrices,rows


def transfer(m,ks):
    size=1<<(m-1);matrix=[[0]*size for _ in range(size)]
    # Carry the row vector(1,1) through the small matrices. Sharing equal
    # prefixes avoids recomputing them for each completed pair of bit words.
    def visit(depth,x,y,a,b):
        if depth==m-1:matrix[y][x]=a+b;return
        for xb,yb in product((0,1),repeat=2):
            k=ks[xb,yb]
            visit(depth+1,2*x+xb,2*y+yb,a*k[0][0]+b*k[1][0],a*k[0][1]+b*k[1][1])
    visit(0,0,0,1,1)
    mask=size-1
    assert all(matrix[y][x]==matrix[mask-y][mask-x] for y in range(size) for x in range(size))
    assert all(0<=v<=1<<(2*m-1) for row in matrix for v in row)
    return matrix


def rounding_certificates(t6,t10):
    dlo,dhi=F(4011234,100000),F(4011235,100000)
    assert dlo*dlo<1609<dhi*dhi
    assert F(81111,2000)<(41+dlo)/2<(41+dhi)/2<F(81113,2000)
    assert F(1969,20000)<(1+31/dhi)/18<(1+31/dlo)/18<F(1971,20000)
    for value,lo,hi in [(t6,12855,12857),(t10,38777,38779)]:
        assert 2**lo<value**200<2**hi
    return {'sqrt1609_strict_rational_bounds':[str(dlo),str(dhi)],
            'r_rounds_to_40.556_by_exact_square_bounds':True,'c_rounds_to_0.0985_by_exact_monotone_bounds':True,
            'log2_rounding_exact_integer_power_tests':[
                {'value':'t6,6','power':200,'strict_lower_power_of2':12855,'strict_upper_power_of2':12857},
                {'value':'t10,10','power':200,'strict_lower_power_of2':38777,'strict_upper_power_of2':38779}]}


def triple_overlap_certificates():
    H=[tuple(map(F,p)) for p in [(0,-4),(4,0),(4,4),(0,4),(-4,0),(-4,-4)]]
    rows=[]
    for centers,wanted in [([(0,0),(-6,-1),(-1,5)],[(-2,2),(-3,1),(-2,1)]),
                           ([(0,0),(5,6),(-1,5)],[(2,4),(1,4),(1,3)])]:
        polygon=H
        for c in centers[1:]:polygon=clip(polygon,[(a+c[0],b+c[1]) for a,b in H])
        assert set(polygon)==set(wanted)
        rows.append({'centers':centers,'common_triangle':[[int(a),int(b)] for a,b in polygon]})
    return rows


def main():
    ks,local=local_tables();out=[];totals={};m3=None
    for m in range(1,11):
        matrix=transfer(m,ks);size=len(matrix);c=[1]*size;seq=[];vectors=[]
        for n in range(1,11):
            assert c==c[::-1]
            totals[m,n]=sum(c);seq.append(sum(c))
            if m==3:vectors.append(c[:])
            if n<10:
                if size==1:c=[2*c[0]]
                else:
                    first=[sum(a*b for a,b in zip(row,c)) for row in matrix[:size//2]]
                    c=first+first[::-1]
        row={'m':m,'boundary_states':size,'transfer_sha256':hashlib.sha256(json.dumps(matrix,separators=(',',':')).encode()).hexdigest(),
             'totals_for_n1_through10':seq,'final_complement_symmetry_checked':True}
        if m==3:row['transfer_matrix']=matrix;row['all_count_vectors']=vectors;m3=row
        out.append(row);print('m',m,'diagonal',seq[m-1],flush=True)
    assert all(totals[m,n]==totals[n,m] for m in range(1,11) for n in range(1,11))
    assert all(totals[1,n]==2**(n-1) for n in range(1,11))
    assert all(totals[2,n]==2*9**(n-1) for n in range(1,11))
    assert m3['transfer_matrix']==[[13,11,9,6],[9,12,10,11],[11,10,12,9],[6,9,11,13]]
    assert m3['totals_for_n1_through10'][:3]==[4,162,6570]
    for n in range(1,9):assert totals[3,n+2]==41*totals[3,n+1]-18*totals[3,n]
    assert totals[6,6]==22406540276117433798
    assert str(totals[10,10]).startswith('2333623171515704644702') and str(totals[10,10]).endswith('99558')
    with localcontext() as ctx:
        ctx.prec=60;d=Decimal(1609).sqrt();r=(41+d)/2;s=(41-d)/2;c=(1609+31*d)/Decimal(28962)
        logs={str(m):str(Decimal(totals[m,m]).ln()/Decimal(2).ln()) for m in (6,10)}
        approximations={'r':str(r),'other_root':str(s),'asymptotic_coefficient_c':str(c),'log2_diagonal_totals':logs}
    result={'local_triangle_tables':local,'matrices':{''.join(map(str,k)):v for k,v in ks.items()},'width_results':out,
            'requested_upper_triangle':[{'m':m,'n':n,'count':totals[m,n]} for m in range(1,11) for n in range(m,11)],
            'all100_rotation_symmetry_checks':True,'approximations':approximations,
            'exact_rounding_certificates':rounding_certificates(totals[6,6],totals[10,10]),
            'two_elementary_triple_overlap_regions':triple_overlap_certificates(),
            'scope':'Exact column DP with maximum512 boundary states and262144 coefficients; no full-order brute-force enumeration.'}
    (ROOT/'results/overlap-orders62.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'t6_6':totals[6,6],'t10_10':totals[10,10],'approximations':approximations}))


if __name__=='__main__':main()

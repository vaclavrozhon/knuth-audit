"""Exact Gaussian-integer checks for TAOCP2 section4.1 exercises16–18/28.

Coordinates are integer pairs. The note supplies general contraction/compactness
proofs; the small-state lists below complete finite cases in those proofs.
"""
from pathlib import Path
from itertools import product
from functools import lru_cache
from fractions import Fraction as F
import json
import sympy as sp

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/complex-radices.json'


def add(z,w):return z[0]+w[0],z[1]+w[1]
def sub(z,w):return z[0]-w[0],z[1]-w[1]
def mul(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def power(z,n):
    out=(1,0)
    while n:
        if n&1:out=mul(out,z)
        z=mul(z,z);n//=2
    return out

def div_exact(z,w):
    den=w[0]*w[0]+w[1]*w[1]
    a=z[0]*w[0]+z[1]*w[1];b=z[1]*w[0]-z[0]*w[1]
    assert a%den==b%den==0,(z,w)
    return a//den,b//den

def value(word,base=(-1,1)):
    z=(0,0)
    for bit in word:z=add(mul(z,base),(int(bit),0))
    return z


def quotient(z,base=(-1,1)):
    d=(z[0]+z[1])%2
    return div_exact(sub(z,(d,0)),base),d


def expand(z,base=(-1,1)):
    ds=[];seen=set()
    while z!=(0,0):
        assert z not in seen,z
        seen.add(z);z,d=quotient(z,base);ds.append(str(d))
    return ''.join(reversed(ds))


@lru_cache(None)
def printed_step(word,op):
    word=word.lstrip('0')
    if not word:return {'P':'1','M':'11101','Q':'11','N':'111'}[op]
    if op=='P':
        if word[-1]=='0':return word[:-1]+'1'
        padded=word if len(word)>=2 else '0'+word
        return printed_step(padded[:-2],'Q')+padded[-2]+'0'
    if op=='M':
        if word[-1]=='1':return word[:-1]+'0'
        padded=word if len(word)>=2 else '0'+word
        return printed_step(padded[:-2],'N')+padded[-2]+'1'
    if op=='Q':
        return printed_step(word[:-1],'P' if word[-1]=='0' else 'N')+('1' if word[-1]=='0' else '0')
    return printed_step(word[:-1],'Q' if word[-1]=='0' else 'M')+('1' if word[-1]=='0' else '0')


def revolving_step(z):
    if (z[0]+z[1])%2==0:return div_exact(z,(1,1)),0
    return div_exact(sub(z,(1,0)),(-1,1)),1


def revolving(z):
    if z==(0,0):return []
    child,first=revolving_step(z)
    tail=[e+1 for e in revolving(child)]
    return ([0]+tail) if first else tail


def trajectory(z,step):
    path=[z];seen=set()
    while z!=(0,0):
        assert z not in seen,z
        seen.add(z);z=step(z)[0];path.append(z)
    return path


def main():
    data=json.loads(OUT.read_text()) if OUT.exists() else {}
    def save(key,result):
        data[key]=result;OUT.write_text(json.dumps(data,indent=2)+'\n');print('PASS',key,flush=True)
    if 'integer_and_revolving' not in data:
        small=sorted((x,y) for x,y in product(range(-2,3),repeat=2) if x*x+y*y<=5)
        assert len(small)==21
        rows=[]
        for z in small:
            p=trajectory(z,quotient);r=trajectory(z,revolving_step)
            assert all(x*x+y*y<=5 for x,y in p+r)
            rows.append({'z':list(z),'negative_base_path':p,'revolving_path':r})
        ordinary=revolves=0
        for z in product(range(-32,33),repeat=2):
            word=expand(z);assert value(word)==z;ordinary+=1
            es=revolving(z)
            assert all(a<b for a,b in zip(es,es[1:]))
            total=(0,0)
            for j,e in enumerate(es):total=add(total,mul(power((0,1),j),power((1,1),e)))
            assert total==z
            revolves+=1
        save('integer_and_revolving',{'small_disk_complete_states':21,'small_state_paths':rows,
                                      'negative_base_integers':ordinary,'revolving_integers':revolves})
    if 'printed_transducers' not in data:
        count=0
        changes={'P':(1,0),'M':(-1,0),'Q':(0,1),'N':(0,-1)}
        for length in range(13):
            for word in product('01',repeat=length):
                word=''.join(word);z=value(word)
                for op,delta in changes.items():
                    got=printed_step(word,op);expected=add(z,delta)
                    assert value(got)==expected
                    assert got.lstrip('0')==expand(expected)
                    count+=1
        # The naive rewrite 2 -> 1100 moves a carry without terminating on -1+1.
        assert value('1100')==(2,0) and value('11101')==(-1,0)
        save('printed_transducers',{'all_word_operation_cases':count,'zero_outputs':{k:printed_step('',k) for k in changes},
                                   'independent_validator':'forced-digit Gaussian division, distinct from recursive suffix rules'})
    if 'fraction_regions' not in data:
        rows=[]
        for base,expected in [((-1,1),[-13,7,-14,11]),((1,1),[-10,10,-20,5])]:
            powers=[power(base,j) for j in range(8)]
            points={value(ds,base) for ds in product('01',repeat=8)}
            bounds=[sum(min(0,z[0]) for z in powers),sum(max(0,z[0]) for z in powers),
                    sum(min(0,z[1]) for z in powers),sum(max(0,z[1]) for z in powers)]
            assert bounds==expected
            assert [min(x for x,y in points),max(x for x,y in points),min(y for x,y in points),max(y for x,y in points)]==bounds
            assert power(base,8)==(16,0) and len(points)==256
            rows.append({'base':base,'block_points':len(points),'powers':powers,'integer_block_bounds':bounds,
                         'fraction_bounds':[str(F(a,15)) for a in bounds]})
        plus_paths={}
        for start in [(-1,0),(-1,1),(0,1)]:
            z=start;path=[]
            while z not in path:
                path.append(z);z=quotient(z,(1,1))[0]
            plus_paths[str(start)]={'path':path,'cycle_start':list(z)}
            assert z==(0,1)
        assert div_exact((1,0),(0,1))==(0,-1) # sum_(k>=1) beta^-k=1/(beta-1).
        # Figure1: all16-digit fractional truncations, with two leading-digit halves.
        points=[value(format(n,'016b')) for n in range(1<<16)]
        assert len(set(points))==1<<16
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig,ax=plt.subplots(figsize=(6,6))
        for lo,hi,color in [(0,1<<15,'#b7b7b7'),(1<<15,1<<16,'#222222')]:
            ax.scatter([z[0]/256 for z in points[lo:hi]],[z[1]/256 for z in points[lo:hi]],s=.45,c=color,linewidths=0,rasterized=True)
        ax.axhline(0,c='black',lw=.5);ax.axvline(0,c='black',lw=.5)
        ax.set(xlim=(-1,1),ylim=(-1,1),aspect='equal',xlabel='Real part',ylabel='Imaginary part',title='Base -1+i: all 16-digit fractional truncations')
        fig.tight_layout();fig.savefig(ROOT/'results/twindragon-truncations.png',dpi=180);plt.close(fig)
        save('fraction_regions',{'blocks':rows,'plus_base_nontermination':plus_paths,
                                  'certified_origin_open_square':'(-1/15,1/15) x (-1/15,1/15)',
                                  'figure_points':len(points),'scope':'The neighborhood follows from a general closedness/lattice argument, not from the finite picture.'})
    if 'contact_matrix' not in data:
        # Duvall–Keesling–Vince Algorithm1, computed directly rather than copied.
        base=(-1,1);N={(0,0),(1,0),(-1,0),(0,1),(0,-1)}
        iterations=0
        while True:
            new=N|{quotient(add(z,(d,0)),base)[0] for z in N for d in (0,1)}
            iterations+=1
            if new==N:break
            N=new
        vertices=sorted(N-{(0,0)})
        C=sp.zeros(len(vertices))
        for i,z in enumerate(vertices):
            for d in (0,1):
                child=quotient(add(z,(d,0)),base)[0]
                if child!=(0,0):C[i,vertices.index(child)]+=1
        t=sp.Symbol('t');polynomial=sp.factor(C.charpoly(t).as_expr())
        expected=(t-1)*(t*t+2*t+2)*(t**3-t*t-2)
        assert sp.expand(polynomial-expected)==0,polynomial
        lo,hi=F(3,2),F(2)
        def cubic(x):return x**3-x*x-2
        for _ in range(80):
            mid=(lo+hi)/2
            if cubic(mid)<0:lo=mid
            else:hi=mid
        assert cubic(lo)<0<cubic(hi)
        # All other eigenvalues have modulus<=sqrt2 or1, so this is the Perron root.
        import mpmath as mp
        mp.mp.dps=60
        root=mp.findroot(lambda x:x**3-x*x-2,mp.mpf('1.7'))
        dimension=2*mp.log(root,2)
        save('contact_matrix',{'neighborhood':vertices,'closure_iterations':iterations,'matrix':[[int(x) for x in C.row(i)] for i in range(C.rows)],
                               'characteristic_polynomial':str(polynomial),'Perron_root_rational_bracket':[str(lo),str(hi)],
                               'Perron_root':str(root),'boundary_dimension':str(dimension),
                               'scope':'Dimension uses the stated primary-source theorem after checking its matrix/radix hypotheses.'})

if __name__=='__main__':main()

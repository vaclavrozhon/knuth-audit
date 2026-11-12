"""Global interval check of Leva's primary Algorithm712 and log-call area.

All published decimal coefficients are exact rationals. A Taylor enclosure
covers the entire transformed boundary, including an explicit infinite tail.
Ellipse areas are evaluated by interval elementary primitives and independently
by high-precision quadrature. No finite grid is used as a global proof.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import sys
import time
import mpmath as mp

mp.mp.dps=80;mp.iv.dps=70;I=mp.iv
ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/leva.json'

def iq(q):
    q=Q(q);return I.mpf(q.numerator)/q.denominator

def endpoints(v):
    return tuple(mp.mp.make_mpf(t) for t in v._mpi_)

def fraction_endpoint(t):
    sign,mantissa,exponent,_=t
    return (-1)**sign*Q(mantissa)*Q(2)**exponent

def fixed_decimal(integer,places=60):
    sign='-' if integer<0 else '';integer=abs(integer);scale=10**places
    return f'{sign}{integer//scale}.{integer%scale:0{places}d}'

def serial(v):
    lo,hi=map(fraction_endpoint,v._mpi_);scale=10**60
    return [fixed_decimal((lo.numerator*scale)//lo.denominator),
            fixed_decimal(-((-hi.numerator*scale)//hi.denominator))]

S,T,A,B=map(iq,['.449871','-.386595','.19600','.25472'])
R1,R2=map(iq,['.27597','.27846']);H=iq('.8578')

def form(u,v):
    x=u-S;y=v-T
    return x*x+y*(A*y-B*x)

def boundary(t):
    u=I.exp(-t*t);v=2*t*u
    return form(u,v)

def derivative(t):
    u=I.exp(-t*t);v=2*t*u;x=u-S;y=v-T
    du=-2*t*u;dv=2*u*(1-2*t*t)
    return (2*x-B*y)*du+(2*A*y-B*x)*dv

def certify_boundary():
    # dQ/dv is positive throughout 0<=u<=1, v>=0.
    lower=2*A*(-T)-B*(1-S)
    assert endpoints(lower)[0]>0
    stack=[(0.0,8.0,0)];leaves=[];maxdepth=0
    while stack:
        lo,hi,depth=stack.pop();mid=(lo+hi)/2;r=(hi-lo)/2
        whole=I.mpf([lo,hi]);direct=boundary(whole)
        taylor=boundary(I.mpf(mid))+derivative(whole)*I.mpf([-r,r])
        low=max(endpoints(direct)[0],endpoints(taylor)[0])
        high=min(endpoints(direct)[1],endpoints(taylor)[1])
        if low>endpoints(R1)[1] and high<endpoints(R2)[0]:
            leaves.append((lo,hi,low,high));maxdepth=max(maxdepth,depth)
        else:
            assert depth<40,(lo,hi,low,high)
            stack.extend([(mid,hi,depth+1),(lo,mid,depth+1)])
    leaves.sort()
    assert leaves[0][0]==0 and leaves[-1][1]==8
    assert all(a[1]==b[0] for a,b in zip(leaves,leaves[1:]))
    # For t>=8 both exp(-t^2) and 2t exp(-t^2) decrease.
    tail=form(I.mpf([0,1])*I.exp(-64),I.mpf([0,1])*16*I.exp(-64))
    assert endpoints(tail)[0]>endpoints(R1)[1] and endpoints(tail)[1]<endpoints(R2)[0]
    return dict(certified_intervals=len(leaves),maximum_bisection_depth=maxdepth,
                finite_t_range=[0,8],boundary_lower_bound=mp.nstr(min(x[2] for x in leaves),60),
                boundary_upper_bound=mp.nstr(max(x[3] for x in leaves),60),
                infinite_tail=serial(tail),positive_vertical_derivative_lower_bound=serial(lower),
                constants='Exact decimals from Netlib TOMS712; t=sqrt(-log u), v=2t exp(-t^2).')

def inverse_sine(z):
    return I.atan2(z,I.sqrt(1-z*z))

def area(r):
    delta=4*A-B*B
    points=[I.mpf(0),I.mpf(1)]
    for v in [I.mpf(0),H]:
        y=v-T;disc=B*B*y*y-4*(A*y*y-r)
        if endpoints(disc)[1]<0:continue
        assert endpoints(disc)[0]>0
        for sign in [-1,1]:
            x=S+(B*y+sign*I.sqrt(disc))/2
            if endpoints(x)[0]>0 and endpoints(x)[1]<1:points.append(x)
            else:assert endpoints(x)[1]<0 or endpoints(x)[0]>1
    points.sort(key=lambda z:sum(endpoints(z))/2)
    assert all(endpoints(x)[1]<endpoints(y)[0] for x,y in zip(points,points[1:]))
    def primitive(u):
        x=u-S;rr=4*A*r
        return T*u+B*x*x/(4*A)+(x*I.sqrt(rr-delta*x*x)+rr/I.sqrt(delta)*inverse_sine(x*I.sqrt(delta/rr)))/(4*A)
    total=I.mpf(0);numeric=mp.mpf(0);parts=[]
    aa=mp.mpf('.196');bb=mp.mpf('.25472');ss=mp.mpf('.449871');tt=mp.mpf('-.386595')
    rr=sum(endpoints(r))/2
    for left,right in zip(points,points[1:]):
        mid=(endpoints(left)[1]+endpoints(right)[0])/2
        q0=form(I.mpf(mid),I.mpf(0));qh=form(I.mpf(mid),H)
        lo=sum(endpoints(left))/2;hi=sum(endpoints(right))/2
        if endpoints(q0)[0]>endpoints(r)[1]:
            value=I.mpf(0);kind='empty'
        elif endpoints(qh)[1]<endpoints(r)[0]:
            value=H*(right-left);kind='full';numeric+=mp.mpf('.8578')*(hi-lo)
        else:
            assert endpoints(q0)[1]<endpoints(r)[0] and endpoints(qh)[0]>endpoints(r)[1]
            value=primitive(right)-primitive(left);kind='ellipse'
            numeric+=mp.quad(lambda u:tt+(bb*(u-ss)+mp.sqrt(4*aa*rr-(4*aa-bb*bb)*(u-ss)**2))/(2*aa),[lo,hi])
        total+=value;parts.append(dict(left=serial(left),right=serial(right),kind=kind))
    assert endpoints(total)[0]-mp.mpf('1e-65')<numeric<endpoints(total)[1]+mp.mpf('1e-65')
    return total,parts,numeric

def log_cost():
    assert endpoints(H-I.sqrt(2/I.e))[0]>0
    inner,p1,n1=area(R1);outer,p2,n2=area(R2)
    normal_area=I.sqrt(I.pi/2)
    logs=2*(outer-inner)/normal_area
    assert endpoints(logs)[0]>mp.mpf('.0115') and endpoints(logs)[1]<mp.mpf('.0125')
    return dict(inner_half_area=serial(inner),outer_half_area=serial(outer),
                logarithms_per_normal=serial(logs),independent_quadrature=mp.nstr(2*(n2-n1)/mp.sqrt(mp.pi/2),65),
                printed_rounding='0.012',inner_parts=p1,outer_parts=p2)

result=json.loads(OUT.read_text()) if '--resume' in sys.argv and OUT.exists() else {}
for name,fn in [('global_bounds',certify_boundary),('logarithm_cost',log_cost)]:
    if name in result:continue
    t=time.monotonic();r=fn();r['elapsed_seconds']=time.monotonic()-t;result[name]=r
    OUT.write_text(json.dumps(result,indent=2)+'\n');print('PASS',name,flush=True)

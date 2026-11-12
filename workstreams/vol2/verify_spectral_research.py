"""Exact certificates for the constructions in spectral exercise23."""
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parent
C=s.Matrix([[0,1,1,1,1,1], [1,0,1,-1,-1,1],
            [1,1,0,1,-1,-1], [1,-1,1,0,1,-1],
            [1,-1,-1,1,0,1], [1,1,-1,-1,1,0]])
assert C.T==C and C*C==5*s.eye(6)

alexeev=[]
for t in range(1,13):
    U=s.eye(t)
    for i in range(1,t):U[i,0]=s.Rational(1,2);U[i,i]=s.sqrt(3)/2
    V=U.inv().T;G=s.simplify(U*U.T);H=s.simplify(V*V.T)
    assert U*V.T==s.eye(t) and H[0,0]==s.Rational(t+2,3)
    assert all(G[i,i]==1 for i in range(t))
    assert all(2*abs(G[i,j])<=1 and 2*abs(H[i,j])<=H[j,j]
               for i in range(t) for j in range(t) if i!=j)
    alexeev.append(dict(t=t,squared=str(H[0,0])))

# An independent symbolic Gram-matrix route certifies the whole family.
r=s.symbols('r');G=s.eye(6)+r*C
assert s.simplify(G*(s.eye(6)-r*C))==(1-5*r*r)*s.eye(6)
# For 0<r<1/sqrt(5), G is positive definite; its inverse has
# constant diagonal 1/(1-5*r*r) and off-diagonal ratio abs(r)<1/2.

pell=[];p,q=1,0
for n in range(1,6):
    p,q=9*p+20*q,4*p+9*q
    assert p*p-5*q*q==1
    N=p*p+5*q*q;A=p*s.eye(6)+q*C;B=p*s.eye(6)-q*C
    assert A*B==s.eye(6)
    assert A*A.T==N*s.eye(6)+2*p*q*C
    assert B*B.T==N*s.eye(6)-2*p*q*C
    assert N-4*p*q==(p-2*q)**2+q*q>0
    # U=A/sqrt(N), V=sqrt(N)*B. Direct integer products prove
    # duality, unit U rows, strict pairwise reducedness, ||V_i||^2=N^2.
    assert (A*A.T/N).inv()==N*B*B.T
    pell.append(dict(n=n,p=p,q=q,normalizing_squared=N,dual_squared=N*N,
                     twice_off_diagonal_ratio=f'{4*p*q}/{N}'))

out=dict(C=[list(map(int,C.row(i))) for i in range(6)],alexeev=alexeev,
         pell=pell,symbolic_gram='(I+rC)^(-1)=(I-rC)/(1-5r^2)',
         conclusion='Unbounded for every t>=6 by an identity block extension. No optimum for t=3,4,5 is claimed. Not classified as a book error; priority unverified.')
(ROOT/'results/spectral-research.json').write_text(json.dumps(out,indent=2)+'\n')
print('Alexeev constructions:12; symbolic Gram identity:passed; Pell certificates:5')

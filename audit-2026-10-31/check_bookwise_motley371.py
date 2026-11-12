"""Only the explicit rotation and reflection cases in answer371; no census."""
import json

def rotate(q,n):
 a,b,c,d=q
 return c,d,n-b,n-a

def diagonal(q):
 a,b,c,d=q
 return c,d,a,b

def antidiagonal(q,n):
 a,b,c,d=q
 return n-d,n-c,n-b,n-a

def cells(q):
 a,b,c,d=q
 return {(i,j) for i in range(a,b) for j in range(c,d)}

q=(0,1,2,4); orbit=[q]
for k in range(3):orbit.append(rotate(orbit[-1],4))
assert rotate(orbit[-1],4)==q
assert orbit==[(0,1,2,4),(2,4,3,4),(3,4,0,2),(0,2,0,1)]
n=4;q=(0,1,3,4);a,b,c,d=q
images=sorted({q,diagonal(q),antidiagonal(q,n),diagonal(antidiagonal(q,n))})
assert images==[(0,1,3,4),(3,4,0,1)]
assert not cells(images[0]) & cells(images[1])
assert len({v[:2] for v in images})==len(images)==len({v[2:] for v in images})
assert not (a==n-1 and c+d>n or c==n-1 and a+b>n or b==1 and c+d<n or d==1 and a+b<n)
assert q==min(images) and not (a==c==n-d==n-b)
assert b>n-d and q==antidiagonal(q,n)
print(json.dumps({'quarter_turn_example':orbit,'bidiagonal_example':images,
 'literal_rejection':'b > n-d (1 > 0), although antidiagonal image is itself',
 'correct_secondary_tokens':{'371a_third_component':'x34 y02','371b_third_example_first_component':'x01 y23'}},indent=2))

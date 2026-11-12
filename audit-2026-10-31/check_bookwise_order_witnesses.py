"""Bounded checks for suspected errors406(a),410 and414; no parameter search."""
import json, math
from itertools import product
from pathlib import Path
from check_graph_encodings import satisfiable
root=Path(__file__).resolve().parent
# One nondegenerate product witness with both printed conjunctions nonempty.
d,a,x,y=5,7,3,3
q=a+1;lo=(q+d-2)//(d-1);floor=math.isqrt(q);ceil=floor+(floor*floor<q)
def prod_encoding(first_hi):
 terms=[]
 for j in range(lo,first_hi+1):
  k=(q+j-1)//j;terms.append({'x_threshold':j,'y_threshold':k,'value':x<j or y<k})
 for j in range(lo,ceil):
  k=(q+j-1)//j;terms.append({'x_threshold':k,'y_threshold':j,'value':x<k or y<j})
 return terms
printed=prod_encoding(floor);fixed=prod_encoding(ceil)
assert printed and all(t['value']for t in printed) and x*y>a
assert not all(t['value']for t in fixed)
# The printed full-adder relaxation allows 111 -> 10.
local={'t':1,'u':1,'v':1,'s':1,'p':1,'q':1,'c':1,'z':0}
checks=[local['s']>=(local['t']^local['u']),local['p']>=(local['t']&local['u']),local['z']>=(local['v']^local['s']),local['q']>=(local['v']&local['s']),local['c']>=(local['p']|local['q'])]
assert all(checks) and 2*local['c']+local['z']<local['t']+local['u']+local['v']
# Test the particular six-input circuit in410, to distinguish the bad local
# transformation from the behavior of that one numerical example.
ids={};cnf=[]
def v(name):
 if name not in ids:ids[name]=len(ids)+1
 return ids[name]
def ge_xor(z,u,w):cnf.extend([(z,-u,w),(z,u,-w)])
def ge_and(z,u,w):cnf.append((z,-u,-w))
def ge_or(z,u,w):cnf.extend([(z,-u),(z,-w)])
def half(i,u,w):ge_xor(v('z'+str(i)),u,w);ge_and(v('c'+str(i)),u,w)
def full(i,t,u,w):
 s,p,q=[v(k+str(i))for k in ['s','p','q']]
 ge_xor(s,t,u);ge_and(p,t,u);ge_xor(v('z'+str(i)),w,s);ge_and(q,w,s);ge_or(v('c'+str(i)),p,q)
xs=[v('x'+str(i))for i in range(3)];ys=[v('y'+str(i))for i in range(3)]
half(0,xs[0],xs[2]);full(1,xs[0],xs[1],-ys[0]);half(2,v('c0'),v('z1'));full(3,xs[1],xs[2],-ys[1]);full(4,v('c1'),v('c2'),v('z3'));full(5,xs[2],-ys[2],v('c3'));half(6,v('c4'),v('z5'));half(7,v('c5'),v('c6'))
assert len(cnf)==44
intermediate={**{f'x{i}':1 for i in range(3)},**{f'y{i}':0 for i in range(3)}}
for i,(carry,summation) in enumerate([(1,0),(1,0),(0,1),(1,0),(0,1),(1,0),(0,0),(0,1)]):
 intermediate['c'+str(i)]=carry;intermediate['z'+str(i)]=summation
for i in [1,3,5]:
 for letter in ['s','p','q']:intermediate[letter+str(i)]=1
intermediate.update(s4=1,p4=0,q4=0)
def satisfied(f,values,names):
 inverse={number:name for name,number in names.items()}
 return all(any(bool(values[inverse[abs(l)]])==(l>0) for l in c)for c in f)
assert satisfied(cnf,intermediate,ids)
word_names=['x0','x1','z0','z2','z4','z6','z7','c7']
intermediate_word=sum(intermediate[k]<<i for i,k in enumerate(word_names))
assert intermediate_word==91 and intermediate_word<13*7+8*7
cnf.extend([(-v('c7'),),(-v('z7'),)])
comparisons=[]
for xx,yy in product(range(8),repeat=2):
 units=[(s if value>>j&1 else -s,) for value,ss in [(xx,xs),(yy,ys)]for j,s in enumerate(ss)]
 got=satisfiable(cnf+units);want=13*xx-8*yy<=7
 comparisons.append({'x':xx,'y':yy,'arithmetic':want,'printed_cnf':got})
mismatches=[row for row in comparisons if row['arithmetic']!=row['printed_cnf']]
circuit_record={'clauses':cnf,'variable_names':ids,'comparisons':comparisons,'mismatches':mismatches,'intermediate_assignment':intermediate,'intermediate_word':intermediate_word,'true_sum':147}
# Fixed 3-by-3 FIFO multiplication, x=y=7. This is the bin reduction
# described in41, with every gate relaxed in the direction prescribed in410.
ids={};cnf=[]
xs=[v('x'+str(i))for i in range(3)];ys=[v('y'+str(i))for i in range(3)]
bins=[[]for _ in range(7)];assignment={**{f'x{i}':1 for i in range(3)},**{f'y{i}':1 for i in range(3)}}
for i,j in product(range(3),repeat=2):
 name=f'b{i}{j}';bit=v(name);ge_and(bit,xs[i],ys[j]);assignment[name]=1;bins[i+j].append(bit)
ops=[];outputs=[];gate_index=0
for column in range(6):
 queue=bins[column]
 while len(queue)>1:
  inputs=queue[:3];del queue[:len(inputs)]
  names={number:name for name,number in ids.items()};bits=[assignment[names[t]]for t in inputs]
  i=gate_index;gate_index+=1
  if len(inputs)==3:
   full(i,*inputs)
   # Use the erroneous 111->10 option only where it occurs naturally.
   ss=1 if bits==[1,1,1] else bits[0]^bits[1]
   pp=bits[0]&bits[1];qq=bits[2]&ss;zz=bits[2]^ss;cc=pp|qq
   assignment.update({f's{i}':ss,f'p{i}':pp,f'q{i}':qq})
  else:
   half(i,*inputs);cc=bits[0]&bits[1];zz=bits[0]^bits[1]
  assignment.update({f'c{i}':cc,f'z{i}':zz})
  ops.append({'column_weight':2**column,'inputs':bits,'carry':cc,'sum':zz,'kind':'full'if len(inputs)==3 else'half'})
  queue.append(v('z'+str(i)));bins[column+1].append(v('c'+str(i)))
 assert len(queue)==1
 outputs.append(queue[0])
names={number:name for name,number in ids.items()}
product_word=sum(assignment[names[t]]<<i for i,t in enumerate(outputs))
assert satisfied(cnf,assignment,ids) and product_word<49
multiplier_record={'x':7,'y':7,'true_product':49,'relaxed_product':product_word,'z':product_word,'assignment':assignment,'variable_names':ids,'clauses':cnf,'operations':ops,'output_bits_low_to_high':[names[t]for t in outputs]}
# Direct resolution for the n=2 strict comparator.
# x1=1,y1=2,x2=3,y2=4,a1=5.
f={frozenset(c)for c in [(-1,2),(-1,5),(2,5),(-3,-5),(4,-5)]}
pos=[c-{5}for c in f if 5 in c];neg=[c-{-5}for c in f if -5 in c]
res={c for c in f if 5 not in c and -5 not in c}
res|={a|b for a in pos for b in neg if not any(-l in a|b for l in a|b)}
assert len(res)==5
clause_count,aux_count=24,0;count_rows=[]
for t in range(2,9):
 if t>2:clause_count,aux_count=2*clause_count+3*(2**t-1),2*aux_count+2**(t+1)-2
 assert aux_count==2*t*2**t-9*2**(t-1)+2
 count_rows.append({'t':t,'d':2**t+1,'clauses':clause_count,'auxiliary_bits':aux_count})
aux_record={'base':'Use original encoding for d<=5; recurse for d=2^t+1, t>=3.','recurrence':'B_t=2B_(t-1)+2^(t+1)-2, B_2=0','exact':'B_t=2t*2^t-9*2^(t-1)+2','leading':'2d lg d + O(d)','sample_counts':count_rows}
out={'product406':{'d':d,'a':a,'x':x,'y':y,'printed_terms':printed,'corrected_terms':fixed},'local_full_adder410':{'assignment':local,'printed_inequalities':checks,'output':2,'input_sum':3},'circuit410':circuit_record,'multiplier411':multiplier_record,'strict414':{'n':2,'resolvents':sorted([sorted(c)for c in res]),'actual_count':5,'printed_count':7,'corrected_general_count':'2^n+2^(n-1)-1'},'auxiliary_count407':aux_record}
(root/'results/bookwise-order-fixed-witnesses.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'406_printed_accepts_bad_product':True,'410_local_underestimate':True,'410_example_mismatches':mismatches,'411_false_product':product_word,'414_resolvents':len(res)}))

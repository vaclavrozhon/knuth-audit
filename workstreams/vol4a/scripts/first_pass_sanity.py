"""Krátké přímé kontroly vytištěných svědků; žádné hledání ani census."""
from collections import Counter
from itertools import permutations
from pathlib import Path
import json

root=Path(__file__).resolve().parents[3]
out={}
out['word_counts_preface_v']={str(n):sum(n**k for k in range(1,n+1)) for n in (5,10,24)}
assert list(out['word_counts_preface_v'].values())==[3905,11111111110,1391724288887252999425128493402200]
a=[16,6,9,15,2,3,8,2,6,3,13,10,9,12,14,8,11,16,1,15,1,5,10,7,13,4,12,5,11,14,4,7]
b=[2,3,4,2,1,3,1,4,16,13,15,5,14,7,9,6,11,5,12,10,8,7,6,13,9,16,15,14,11,8,10,12]
def langford(a):
 n=len(a)//2
 assert Counter(a)==Counter({k:2 for k in range(1,n+1)})
 assert all(a.index(k)+k+1==len(a)-1-a[::-1].index(k) for k in range(1,n+1))
 return {'weighted_sum':sum((i+1)*x for i,x in enumerate(a)), 'left_sum':sum(a[:n]),'right_sum':sum(a[n:]), 'doubled_torque':sum((2*i+1-len(a))*x for i,x in enumerate(a)), 'width':max(sum(v==1 for v in Counter(a[:i]).values()) for i in range(len(a)+1))}
out['langford_display_2']=langford(a)
out['langford_display_3']=langford(b)
assert out['langford_display_2']['doubled_torque']==0
assert out['langford_display_2']['left_sum']==out['langford_display_2']['right_sum']==136
assert out['langford_display_2']['width']==7
assert out['langford_display_3']['weighted_sum']==5268
L=[[int(c) for c in s] for s in ['0123456789','1832547690','2956308471','3709861524','4675290813','5094783162','6547132908','7418029356','8360915247','9281674035']]
M=[[int(c) for c in s] for s in ['0285947361','1749365028','2564870193','3690458217','4817536902','5178029436','6902713845','7351204689','8023691754','9436182570']]
def latin(A):
 n=len(A)
 return all(set(x)==set(range(n)) for x in A) and all(set(x)==set(range(n)) for x in zip(*A))
assert latin(L) and latin(M)
assert len({(L[i][j],M[i][j]) for i in range(10) for j in range(10)})==100
out['latin_display_7']='Both squares are Latin and all 100 ordered pairs are distinct; uniqueness and 808 transversals not recomputed.'
R=[[ord(c)-97 for c in s] for s in ['dabc','cbad','adcb','bcda']]
S=[[ord(c)-97 for c in s] for s in ['cdba','bacd','abdc','dcab']]
assert latin(R) and latin(S)
assert len({(R[i][j],S[i][j]) for i in range(4) for j in range(4)})==16
assert all(len({A[i][i] for i in range(4)})==4 and len({A[i][3-i] for i in range(4)})==4 for A in (R,S))
out['latin_display_5']='Latin, orthogonal, and both principal diagonals valid in both squares.'
words=(root/'audit-2026-10-31/sources/sgb-words.txt').read_text().splitlines()
rank={w:i+1 for i,w in enumerate(words)}
assert len(words)==5757
assert [words[i-1] for i in (1000,2000,3000,4000,5000)]==['ditch','galls','visas','faker','pismo']
out['wordlist_examples']={'size':len(words),'first':words[0],'last':words[-1],'ranks':{str(i):words[i-1] for i in (1000,2000,3000,4000,5000)}}
out['yucca_abuzz_squared_distance']=sum((ord(x)-ord(y))**2 for x,y in zip('yucca','abuzz'))
assert out['yucca_abuzz_squared_distance']==2415
cover=['third flock began jumps','becks fjord glitz nymph squaw','waqfs gyved bronx chimp klutz']
out['letter_cover_sizes']=[len(set(s.replace(' ',''))) for s in cover]
assert out['letter_cover_sizes']==[20,24,25]
assert set(cover[0].replace(' ',''))<=set('abcdefghijklmnopqrstu')
square='class light agree sheep steps'.split()
assert all(square[i][j]==square[j][i] for i in range(5) for j in range(5))
assert max(rank[w] for w in square)<=400
cube=[s.split() for s in ['types yeast pasta ester start','yeast earth armor stove three','pasta armor smoke token arena','ester stove token event rents','start three arena rents tease']]
assert all(cube[i][j][k]==cube[p[0]][p[1]][p[2]] for i in range(5) for j in range(5) for k in range(5) for p in permutations((i,j,k)))
out['word_square_max_rank']=max(rank[w] for w in square)
out['word_cube_max_rank']=max(rank[w] for row in cube for w in row)
assert out['word_cube_max_rank']<=3000
A=[[2,1,0],[1,0,2],[0,2,4]]
def mul(A,B): return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
A2=mul(A,A); A3=mul(A2,A)
assert A2==[[5,2,2],[2,5,8],[2,8,20]]
assert A3==[[12,9,12],[9,18,42],[12,42,96]]
out['matrix_powers']={'A2':A2,'A3':A3}
assert len({tuple(A[i][j] for i in p for j in p) for p in permutations(range(3))})==6
out['mate_address_cases']={str(a):a-20+(40&((a&4)-1)) for a in (0,20,40,60)}
assert list(out['mate_address_cases'].values())==[20,0,60,40]
out['scope']='Fixed examples only. No optimality, uniqueness, large enumeration, benchmark, or external historical-source verification.'
print(json.dumps(out,ensure_ascii=False,indent=2))

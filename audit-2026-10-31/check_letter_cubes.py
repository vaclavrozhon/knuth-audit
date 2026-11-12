"""Fold the printed nets in 3D, enumerate proper cube rotations, and read words."""
from pathlib import Path
from itertools import product, permutations
import json, time

R = Path(__file__).resolve().parent
POSITIONS = [(0,0),(1,0),(2,0),(2,1),(3,1),(4,1)]
# Clockwise quarter-turns in the printed net, confirmed by MuPDF trace matrices.
NETS = [[('P',0),('O',0),('E',0),('Z',0),('G',1),('H',0)],
        [('S',0),('G',0),('S',0),('U',2),('R',1),('Z',0)],
        [('A',0),('R',0),('T',0),('H',0),('I',0),('Z',0)],
        [('D',0),('T',0),('E',0),('U',0),('W',1),('C',0)],
        [('U',0),('Y',0),('L',0),('Z',0),('O',0),('H',0)]]

def neg(v): return tuple(-a for a in v)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def transform(m,v):return tuple(dot(row,v) for row in m)
def compose(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))

def rotations():
    result=[]
    for p in permutations(range(3)):
        for s in product([-1,1],repeat=3):
            m=tuple(tuple(s[i] if j==p[i] else 0 for j in range(3)) for i in range(3))
            if dot(m[0],cross(m[1],m[2]))==1:result.append(m)
    assert len(result)==24
    return result

def fold(net):
    frames={POSITIONS[0]:((1,0,0),(0,1,0),(0,0,1))};queue=[POSITIONS[0]]
    for x,y in queue:
        right,up,normal=frames[x,y]
        for delta,frame in [((1,0),(neg(normal),up,right)),((-1,0),(normal,up,neg(right))),
                            ((0,1),(right,normal,neg(up))),((0,-1),(right,neg(normal),up))]:
            p=(x+delta[0],y+delta[1])
            if p not in POSITIONS:continue
            if p in frames:assert frames[p]==frame
            else:frames[p]=frame;queue.append(p)
    assert len({f[2] for f in frames.values()})==6
    return [(frames[p][2],(frames[p][1],frames[p][0],neg(frames[p][1]),neg(frames[p][0]))[turn],letter)
            for p,(letter,turn) in zip(POSITIONS,net)]

def glyph(letter,q):
    # q is counterclockwise rotation relative to the reader.
    if q==0:return letter
    if letter in 'OX':return letter
    if letter in 'HINZ':return letter if q==2 else {'H':'I','I':'H','N':'Z','Z':'N'}[letter]
    if letter=='S' and q==2:return 'S'
    if letter=='C' and q==1:return 'U'
    if letter=='U' and q==3:return 'C'
    # The printed M and W are different glyphs, not half-turn counterparts.
    return None

SIDES=[(0,1,0),(0,0,1),(0,-1,0),(0,0,-1)]
def read_placement(folded,m):
    placed={transform(m,n):(transform(m,u),c) for n,u,c in folded};out=[]
    for n in SIDES:
        u,c=placed[n];right=(1,0,0);up=cross(n,right)
        q=[up,neg(right),neg(up),right].index(u)
        options={sense:glyph(c,(q-2*sense)%4) for sense in [0,1]}
        options={k:v for k,v in options.items() if v is not None}
        if not options:return None
        out.append(options)
    return out

def main():
    started=time.monotonic();rots=rotations();folded=[fold(net) for net in NETS]
    choices=[[(m,read_placement(f,m)) for m in rots if read_placement(f,m)] for f in folded]
    print('valid placements',list(map(len,choices)),flush=True)
    assert list(map(len,choices))==[16]*5
    # Overall rotations preserving the row axis, including reversal of its ends.
    group=[m for m in rots if transform(m,(1,0,0)) in [(1,0,0),(-1,0,0)]]
    first=[(m,p) for m,p in choices[0] if m==min(compose(g,m) for g in group)]
    assert len(first)==2
    compatible=[]
    for combo in product(first,*choices[1:]):
        p=[x[1] for x in combo];senses=[]
        for face in range(4):
            allowed=set.intersection(*(set(x[face]) for x in p));senses.append(allowed)
        if all(senses):compatible.append((combo,senses))
    print('compatible',len(compatible),flush=True);assert len(compatible)==6144
    words=set((R/'sources/wordlists/words5-from-sgb').read_text().upper().splitlines())
    solutions={};best={2:set(),3:set(),4:set()};perms=list(permutations(range(5)))
    partial_examples={'UNTIL_adjacent_HOURS':[],'SYRUP_opposite_ECHOS':[]}
    for combo,senses in compatible:
        p=[x[1] for x in combo]
        for perm in perms:
            face_words=[]
            for face in range(4):
                options=[]
                for sense in senses[face]:
                    order=perm if sense==0 else perm[::-1]
                    w=''.join(p[i][face][sense] for i in order)
                    if w in words:options.append((sense,w))
                face_words.append(options)
            count=sum(bool(w) for w in face_words)
            if count>=2:
                key=(tuple(m for m,_ in combo),perm)
                best[count].add(key)
                on_face={word:face for face,options in enumerate(face_words) for sense,word in options}
                for label,w1,w2,separation in [('UNTIL_adjacent_HOURS','UNTIL','HOURS',1),
                                                ('SYRUP_opposite_ECHOS','SYRUP','ECHOS',2)]:
                    if w1 in on_face and w2 in on_face:
                        distance=(on_face[w1]-on_face[w2])%4
                        if distance==separation or (separation==1 and distance==3):
                            partial_examples[label].append({'words':face_words,'permutation':perm,'rotations':[m for m,_ in combo]})
                if count==4:
                    solutions[str(key)]={'words':face_words,'permutation_zero_based':perm,'rotations':[m for m,_ in combo]}
    assert all(partial_examples.values())
    # Each of these glyphs is readable at every quarter-turn, choosing its
    # upright/downward word direction independently on each visible side.
    universal='CHINOUXZ'
    assert all(any(glyph(c,(q-2*s)%4) is not None for s in [0,1]) for c in universal for q in range(4))
    bad_net=[('B',0),('A',1),('D',0),('O',0),('O',0),('O',0)]
    bad_fold=fold(bad_net)
    valid_bad=[{'rotation':m,'visible_letters':read_placement(bad_fold,m)} for m in rots if read_placement(bad_fold,m)]
    identity=((1,0,0),(0,1,0),(0,0,1))
    assert len(valid_bad)==8 and read_placement(bad_fold,identity) is not None
    repaired_net=bad_net.copy();repaired_net[2]=('D',1)
    assert not any(read_placement(fold(repaired_net),m) for m in rots)
    out={'status':'pass','valid_placements_per_cube':list(map(len,choices)),'first_cube_representatives':len(first),
         'all_placements':2*16**4,'compatible_placements':len(compatible),'dictionary':'words5-from-sgb',
         'placements_by_number_of_valid_words':{k:len(v) for k,v in best.items()},'four_word_solutions':list(solutions.values()),
         'partial_examples':partial_examples,'all_24_placements_glyphs':universal,
         'impossible_pattern_counterexample':{'net':bad_net,'folded_faces':bad_fold,'valid_placements':valid_bad,
             'identity_placement':read_placement(bad_fold,identity),'repair':'Turn the D face by 90 degrees in the printed net.'},
         'nets':NETS,'elapsed_seconds':time.monotonic()-started}
    (R/'results/factor_puzzles/letter-cubes.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()

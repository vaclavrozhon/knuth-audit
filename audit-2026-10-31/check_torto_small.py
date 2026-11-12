"""Compare the position/inverse/diagonal reduction with all direct king paths."""
from itertools import product
from colored_dlx import ColoredDLX
from layout_native import OUT,encode,save,sha
from torto112 import neighbors,crossing_bit,paths


class NoEvents:
    def append(self,event):pass
    def __iter__(self):return iter(())


def instance(board,words,m,n):
    primary=[f'W{k}_{j}' for k,w in enumerate(words) for j in range(1,len(w))]
    secondary=[f'X{u}' for u in range(m*n)]
    secondary += [f'P{k}_{j}' for k,w in enumerate(words) for j in range(len(w))]
    secondary += [f'Q{k}_{u}' for k,w in enumerate(words) for u in range(m*n)]
    secondary += [f'D{k}_{d}' for k,w in enumerate(words) for d in range((m-1)*(n-1))]
    rows=[];info=[]
    for k,w in enumerate(words):
        for j in range(1,len(w)):
            for u,adj in neighbors(m,n).items():
                for v in adj:
                    if (board[u],board[v])!=(w[j-1],w[j]):continue
                    row=[(f'W{k}_{j}',0),(f'X{u}',ord(w[j-1])-64),(f'X{v}',ord(w[j])-64),
                         (f'P{k}_{j-1}',u+1),(f'P{k}_{j}',v+1),(f'Q{k}_{u}',j),(f'Q{k}_{v}',j+1)]
                    bit=crossing_bit(u,v,n)
                    if bit:row.append((f'D{k}_{bit.bit_length()-1}',0))
                    rows.append(row);info.append((k,j,u,v))
    return encode(primary,secondary,rows),info


def main():
    cases=models=0
    for m,n,lengths in [(2,2,[2,3,4]),(2,3,[2,3])]:
        for letters in product('AB',repeat=m*n):
            board=''.join(letters)
            words=[[''.join(w)] for length in lengths for w in product('AB',repeat=length)]
            if n==2:words += [['AA','ABA'],['AB','BA'],['AAA','BBB']]
            for ws in words:
                enc,info=instance(board,ws,m,n)
                solver=ColoredDLX(len(enc['names']),enc['primary'],enc['rows']);solver.events=NoEvents();solver.solve()
                actual=set()
                for model in solver.solutions:
                    selected=[[-1]*len(w) for w in ws]
                    for i in model:
                        k,j,u,v=info[i]
                        for pos,value in [(j-1,u),(j,v)]:
                            assert selected[k][pos] in [-1,value];selected[k][pos]=value
                    actual.add(tuple(map(tuple,selected)))
                expected=set(product(*(paths(board,w,m,n) for w in ws)))
                assert actual==expected and len(actual)==len(solver.solutions),(board,ws)
                cases+=1;models+=len(actual)
    adj=neighbors();all_edges=[(u,v) for u,vs in adj.items() for v in vs]
    restricted=[(u,v) for u,v in all_edges if u//3<3 and u%3<2 and v%3<2]
    assert len(all_edges)==94 and len(restricted)==26
    for u,v in all_edges:
        orbit=[]
        for fr,fc in product([False,True],repeat=2):
            def transform(x):
                r,c=divmod(x,3);return (5-r if fr else r)*3+(2-c if fc else c)
            orbit.append((transform(u),transform(v)))
        assert set(orbit)&set(restricted)
    save(OUT/'torto-small-checked.json',dict(script_sha256=sha(__file__),instances=cases,models=models,
        complete_path_sets_equal=True,full_directed_edges=94,restricted_edges=26,every_reflection_orbit_represented=True))
    print('Torto',cases,'complete tiny instances,',models,'models;94/26 edges and orbit coverage.')


if __name__=='__main__':main()

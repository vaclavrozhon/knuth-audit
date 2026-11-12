"""Independent row-permutation validation, clue symmetries, and forced digits."""
from collections import Counter,defaultdict
from itertools import permutations,product,combinations
from pathlib import Path
import json
ROOT=Path(__file__).parent;OUT=ROOT/'results/kakuro'


def cells(shape):return [(r,c) for r in range(3) for c in range(3) if shape=='b' or (r,c) not in [(0,2),(2,0)]]


def load(shape,q):
    result={}
    for line in (OUT/f'{shape}{q}-unique.jsonl').read_text().splitlines():
        d=json.loads(line);key=tuple(d['sums']);assert key not in result;result[key]=tuple(d['digits'])
    return result


def independent(shape,q):
    positions=cells(shape);lengths=[sum(r==i for r,c in positions) for i in range(3)]
    fills=defaultdict(list)
    for rows in product(*(permutations(range(1,q+1),length) for length in lengths)):
        values=sum((tuple(row) for row in rows),());grid=dict(zip(positions,values));cols=[]
        for c in range(3):
            col=[grid[r,c] for r in range(3) if (r,c) in grid]
            if len(col)!=len(set(col)):break
            cols.append(sum(col))
        else:fills[tuple(sum(row) for row in rows)+tuple(cols)].append(values)
    unique={key:values[0] for key,values in fills.items() if len(values)==1}
    assert unique==load(shape,q)
    counts=json.loads((OUT/f'{shape}{q}-counts.json').read_text())
    assert counts['fillings']==sum(map(len,fills.values()))
    assert counts['distinct_sum_sequences']==len(fills)
    return dict(shape=shape,alphabet=q,fillings=counts['fillings'],unique=len(unique))


def orbit(shape,key):
    variants=set();rows=key[:3];cols=key[3:];lengths=[3,3,3] if shape=='b' else [2,3,2]
    for transpose in (False,True):
        row,col=(cols,rows) if transpose else (rows,cols)
        arrangements=product(permutations(range(3)),repeat=2) if shape=='b' else [((0,1,2),(0,1,2)),((2,1,0),(2,1,0))]
        for rp,cp in arrangements:
            values=tuple(row[i] for i in rp)+tuple(col[i] for i in cp)
            variants.add(values)
            variants.add(tuple(10*lengths[i%3]-value for i,value in enumerate(values)))
    return variants


def xcc_forced(positions,lengths,key,combos):
    """Initial singleton primary items in the exact encoding430(d)."""
    options=defaultdict(set)
    for r,c in positions:
        for p,xset in enumerate(combos[lengths[r],key[r]]):
            for q,yset in enumerate(combos[lengths[c],key[3+c]]):
                for x in set(xset)&set(yset):
                    option=('cell',r,c,p,q,x)
                    for item in [('cell',r,c),('h',r,p,x),('v',c,q,x)]:options[item].add(option)
    for direction,offset in [('h',0),('v',3)]:
        for block in range(3):
            choices=combos[lengths[block],key[offset+block]]
            for p,choice in enumerate(choices):
                for other in range(len(choices)):
                    if p==other:continue
                    option=('absorb',direction,block,p,other)
                    for x in choice:options[direction,block,p,x].add(option)
    singles=[next(iter(values)) for values in options.values() if len(values)==1]
    return len(set(singles)),len(singles)


def main():
    validations=[independent(shape,q) for shape in ['a','b'] for q in [3,4]]
    combos=defaultdict(list);unions={}
    for k in [2,3]:
        for choice in combinations(range(1,10),k):combos[k,sum(choice)].append(choice)
    for key,choices in combos.items():unions[key]=set().union(*map(set,choices))
    result={}
    for shape in ['a','b']:
        counts=json.loads((OUT/f'{shape}9-counts.json').read_text());records=load(shape,9)
        assert len(records)==counts['unique_puzzles']
        def falling(k):
            value=1
            for j in range(k):value*=9-j
            return value
        assert sum(count*falling(k) for k,count in enumerate(counts['rgs_counts']))==counts['fillings']
        seen=set();classes=[];positions=cells(shape);lengths=[3,3,3] if shape=='b' else [2,3,2]
        for key in sorted(records):
            if key in seen:continue
            members=orbit(shape,key);assert members<=records.keys();seen.update(members)
            forced=0
            for (r,c),digit in zip(positions,records[key]):
                domain=unions[lengths[r],key[r]]&unions[lengths[c],key[3+c]]
                assert digit in domain
                if len(domain)==1:forced+=1
            magic=sum(len(combos[lengths[i%3],s])==1 for i,s in enumerate(key))
            forced_moves,singleton_items=xcc_forced(positions,lengths,key,combos)
            classes.append(dict(representative=key,orbit_size=len(members),forced_cells=forced,
                                forced_moves=forced_moves,singleton_items=singleton_items,magic_blocks=magic))
        histogram=Counter(x['orbit_size'] for x in classes)
        if shape=='a':
            assert histogram=={2:1,4:190,8:9741}
            no_forced=[x for x in classes if x['orbit_size']==8 and x['forced_cells']==0]
            no_magic=[x for x in no_forced if x['magic_blocks']==0]
            assert (6,15,14,14,15,6) in records and len(orbit(shape,(6,15,14,14,15,6)))==2
            forced4=[x for x in classes if x['forced_cells']==4]
            expected={min(orbit(shape,k)) for k in [(4,15,12,12,15,4),(4,15,16,12,15,8)]}
            printed_hard=(6,19,6,8,11,10)
            assert sum(printed_hard[:3])==31 and sum(printed_hard[3:])==29
            assert printed_hard not in records
            hard=min(orbit(shape,(6,19,6,8,13,10)))
            assert hard in {tuple(x['representative']) for x in no_magic}
            result['a_extra']=dict(asymmetric_without_forced=len(no_forced),also_without_magic=len(no_magic),
                                   classes_with_four_forced=forced4,
                                   printed_without_forced=4011,printed_also_without_magic=570,
                                   xcc_without_forced=sum(x['orbit_size']==8 and x['forced_moves']==0 for x in classes),
                                   xcc_also_without_magic=sum(x['orbit_size']==8 and x['forced_moves']==0 and x['magic_blocks']==0 for x in classes),
                                   printed_four_forced=[x for x in classes if tuple(x['representative']) in expected],
                                   printed_hard=printed_hard,printed_row_total=31,printed_column_total=29,
                                   proposed_hard_repair=(6,19,6,8,13,10),
                                   caution='The meaning of forced move is unresolved; these discrepancies are not confirmed book errors.',
                                   hardest_claim='Printed example impossible by unequal totals. The proposed13-for11 repair belongs to the claimed class;79-node count not yet reproduced.')
        else:
            assert histogram=={72:3,144:46}
            expected={min(orbit(shape,k)) for k in [(7,11,20,7,11,20),(7,19,20,7,19,20),(7,15,23,10,15,20)]}
            assert {tuple(x['representative']) for x in classes if x['orbit_size']==72}==expected
            assert all(x['forced_cells']>=1 for x in classes)
            assert all(any((r,c) in {(7,20),(20,7),(23,10),(10,23)}
                           for r in x['representative'][:3] for c in x['representative'][3:]) for x in classes)
        result[shape]=dict(classes=len(classes),orbit_histogram=dict(histogram),
                           forced_histogram=dict(Counter(x['forced_cells'] for x in classes)),
                           all_classes=classes)
        print(shape,{k:v for k,v in result[shape].items() if k!='all_classes'},flush=True)
    result['validation']=validations
    (OUT/'symmetries.json').write_text(json.dumps(result,indent=2)+'\n')
    print('All filling counts, unique-puzzle counts and symmetry classes agree. Forced-move statistics remain unresolved.')

if __name__=='__main__':main()

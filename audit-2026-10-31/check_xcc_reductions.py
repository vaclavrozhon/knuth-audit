"""Independent finite relations and SAT assignments versus DLX98--100 reductions."""
from datetime import datetime,timezone
from itertools import combinations,combinations_with_replacement,product
from pathlib import Path
import hashlib,json,random
from colored_dlx import ColoredDLX,brute

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/universal_cycles'

class NoEvents(list):
    def append(self,value):pass

def solve(n,p,rows):
    s=ColoredDLX(n,p,rows);s.events=NoEvents();return s.solve().solutions


def from_sat(n,clauses):
    """The corrected six-options-per-clause construction, not literal labels."""
    rows=[];p=3*len(clauses)
    for i,clause in enumerate(clauses):
        ids=[3*i+j+1 for j in range(3)]
        rows += [((ids[j],0),(ids[(j+1)%3],0)) for j in range(3)]
        rows += [((ids[j],0),(p+abs(lit),2 if lit>0 else 1))
                 for j,lit in enumerate(clause)]
    return p+n,p,rows


def assignment_extensions(n,p,rows,models):
    assignments=set()
    for model in models:
        fixed={}
        for ri in model:
            for item,color in rows[ri]:
                if item>p:
                    assert item-p-1 not in fixed or fixed[item-p-1]==color-1
                    fixed[item-p-1]=color-1
        free=[i for i in range(n) if i not in fixed]
        for values in product(range(2),repeat=len(free)):
            a=dict(fixed);a.update(zip(free,values))
            assignments.add(tuple(a[i] for i in range(n)))
    return assignments


def ordinary(n,p,rows):
    """Replace each incompatible occurrence pair by its private secondary item.

    Page88 explicitly treats an uncolored occurrence as an occurrence-private
    color. Its numeric COLOR=0 is not a shared mathematical color.
    """
    converted=[[(item,0) for item,c in row if item<=p] for row in rows]
    next_item=p
    for item in range(p+1,n+1):
        occurrences=[(ri,c) for ri,row in enumerate(rows) for i,c in row if i==item]
        for (ri,c),(rj,d) in combinations(occurrences,2):
            if c==d and c!=0:continue
            next_item+=1
            converted[ri].append((next_item,0));converted[rj].append((next_item,0))
    return next_item,p,converted


def from_csp(n,relations,add_free_domains=None):
    relations=list(relations)
    used={i for scope,allowed in relations for i in scope}
    if add_free_domains is not None:
        relations += [((i,),[(v,) for v in add_free_domains[i]]) for i in range(n) if i not in used]
    p=len(relations);rows=[]
    for j,(scope,allowed) in enumerate(relations):
        assert scope and len(set(scope))==len(scope)
        for values in sorted(set(allowed)):
            assert len(values)==len(scope)
            rows.append(tuple([(j+1,0)]+[(p+i+1,v+1) for i,v in zip(scope,values)]))
    return p+n,p,rows


def decoded_csp(n,p,rows,models):
    result=set()
    for model in models:
        values={}
        for ri in model:
            for i,c in rows[ri]:
                if i>p:
                    assert i not in values or values[i]==c-1
                    values[i]=c-1
        result.add(tuple(values.get(p+i+1) for i in range(n)))
    assert len(result)==len(models)
    return result


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    sat_cases=0;sat_models=0;sat_unsat=0
    for n,max_m in [(1,4),(2,3)]:
        clauses=list(combinations_with_replacement(tuple(range(1,n+1))+tuple(range(-n,0)),3))
        for m in range(max_m+1):
            for cs in combinations_with_replacement(clauses,m):
                dim,p,rows=from_sat(n,cs);models=solve(dim,p,rows)
                truth={bits for bits in product(range(2),repeat=n)
                       if all(any(bits[abs(l)-1]==(l>0) for l in c) for c in cs)}
                assert assignment_extensions(n,p,rows,models)==truth
                assert len(rows)==6*m and all(len(row)==2 for row in rows)
                sat_cases+=1;sat_models+=len(models);sat_unsat+=not truth
    # All 256 subformulas of the eight distinct-variable 3-literal clauses.
    clauses=list(product(*[(i,-i) for i in range(1,4)]))
    for mask in range(256):
        cs=[c for i,c in enumerate(clauses) if mask>>i&1]
        dim,p,rows=from_sat(3,cs);models=solve(dim,p,rows)
        truth={bits for bits in product(range(2),repeat=3)
               if all(any(bits[abs(l)-1]==(l>0) for l in c) for c in cs)}
        assert assignment_extensions(3,p,rows,models)==truth
        sat_cases+=1;sat_models+=len(models);sat_unsat+=not truth
    # Exhaustive option families for two primary items and one secondary.
    possibilities=[]
    for prim in [(1,),(2,),(1,2)]:
        for secondary in [None,0,1,2]:
            possibilities.append(tuple([(i,0) for i in prim]+([] if secondary is None else [(3,secondary)])))
    families=[(3,2,rows) for m in range(6) for rows in combinations(possibilities,m)]
    rng=random.Random(99100)
    for _ in range(1000):
        rows=[]
        for __ in range(rng.randrange(1,9)):
            prim=rng.choice([(1,),(2,),(1,2)])
            row=[(i,0) for i in prim]
            for i in [3,4]:
                c=rng.choice([None,0,1,2])
                if c is not None:row.append((i,c))
            rows.append(tuple(row))
        families.append((4,2,rows))
    reduction_models=0
    for n,p,rows in families:
        original=brute(p,rows);nn,pp,converted=ordinary(n,p,rows)
        assert len(rows)==len(converted)
        assert original==brute(pp,converted)==solve(nn,pp,converted)
        reduction_models+=len(original)
    binary=[(a,b) for a,b in product(range(3),repeat=2) if a<=b]
    ternary=[a for a in product(range(3),repeat=3) if sum(a)==3]
    relations=[((j,j+1),binary) for j in range(4)]+[((0,2,4),ternary)]
    dim,p,rows=from_csp(5,relations)
    found=decoded_csp(5,p,rows,solve(dim,p,rows))
    direct={a for a in product(range(3),repeat=5) if list(a)==sorted(a) and sum(a[::2])==3}
    expected={tuple(map(int,s)) for s in ['00112','00122','01112','01122','11111']}
    assert found==direct==expected and len(rows)==31 and len(ternary)==7
    csp_cases=0;free_cases=0;domain_cases=0
    for _ in range(1000):
        n=rng.randrange(1,5);domains=[range(rng.randrange(1,4)) for i in range(n)]
        relations=[]
        for __ in range(rng.randrange(1,6)):
            scope=tuple(sorted(rng.sample(range(n),rng.randrange(1,n+1))))
            allowed=[t for t in product(*(domains[i] for i in scope)) if rng.randrange(2)]
            relations.append((scope,allowed))
        direct={a for a in product(*domains) if all(tuple(a[i] for i in scope) in allowed for scope,allowed in relations)}
        used={i for scope,allowed in relations for i in scope}
        dim,p,rows=from_csp(n,relations,domains)
        found=decoded_csp(n,p,rows,solve(dim,p,rows))
        assert found==direct
        csp_cases+=1;free_cases+=len(used)<n;domain_cases+=sum(i not in used for i in range(n))
    # Precisely expose what the written construction leaves unspecified.
    relations=[((0,),[(0,)])]
    dim,p,rows=from_csp(2,relations)
    unspecified=decoded_csp(2,p,rows,solve(dim,p,rows))
    assert unspecified=={(0,None)}
    dim,p,rows=from_csp(2,relations,[range(2),range(2)])
    expanded=decoded_csp(2,p,rows,solve(dim,p,rows))
    assert expanded=={(0,0),(0,1)}
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        sat98=dict(cases=sat_cases,models=sat_models,unsatisfiable=sat_unsat,
                   corrected_labels_from='errata/originals/err4b.textxt, 2025-01-02'),
        transform99=dict(cases=len(families),models=reduction_models,all_option_index_sets_equal=True,
                         uncolored_convention='Page88: each uncolored occurrence has its own implicit color.'),
        csp100=dict(printed_solutions=[''.join(map(str,s)) for s in sorted(expected)],printed_options=31,random_cases=csp_cases,
                   cases_with_unused_variables=free_cases,added_unary_domains=domain_cases,
                   unused_variable_example=dict(written_construction=sorted(unspecified),with_domain_constraint=sorted(expanded))))
    (OUT/'reductions-checked.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()

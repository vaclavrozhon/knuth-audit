#!/usr/bin/env python3
"""All restricted local tables and their complete Boolean2-CNF projections.

Reuses the proved32 visible octant cases, without rerunning the octant
classification or any scene search. Every possible endpoint marginal is
included, not merely the domains seen in a sample drawing.
"""
import json
from itertools import product,combinations
from collections import defaultdict,Counter
from check_clasp_projection import ROOT,cross2

RAYS=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
PLUS={4:0,2:4,1:2}
FLIP={'+':'+','-':'-','I':'O','O':'I'}
ORDER='+-IO'


def main():
    source=json.loads((ROOT/'results/cubie-junctions.json').read_text())
    groups=defaultdict(set);witnesses=defaultdict(list);v_angles=[]
    for row in source['cases']:
        ds=sorted(((PLUS[e['axis_bit']]+3*e['negative'])%6,e['label']) for e in row['edges'] if e['visible'])
        key=(row['type'],tuple(d for d,s in ds));word=''.join(s for d,s in ds)
        groups[key].add(word);witnesses[key].append(row['printed_label'])
        if row['type']=='V':
            a,b=(d for d,s in ds);distance=min((a-b)%6,(b-a)%6);angle=60*distance
            assert angle==(60 if '+' in word else 120)
            v_angles.append({'octants':row['printed_label'],'directions':[a,b],'word':word,'angle_degrees':angle})
    # Generic orthogonal T junctions: three choices of bar axis and four
    # choices of a noncollinear stem. Material lies opposite the stem side.
    for d in range(3):
        for stem in range(6):
            if stem in(d,d+3):continue
            dirs=tuple(sorted((d,d+3,stem)))
            for s in ORDER:
                word=''.join(s if k==stem else('O' if cross2(RAYS[k],RAYS[stem])>0 else'I') for k in dirs)
                groups['T',dirs].add(word)
            witnesses['T',dirs].append({'bar':[d,d+3],'stem':stem})
    tables=[]
    for k,rows in sorted(groups.items()):
        kind,dirs=k;rows=sorted(rows)
        domains=[set(r[i] for r in rows) for i in range(len(dirs))]
        tables.append({'kind':kind,'directions':dirs,'rows':rows,'domains':domains,'witnesses':witnesses[k]})
    endpoint_domains={d:set() for d in range(6)}
    endpoint_origins=defaultdict(list)
    for t in tables:
        for i,d in enumerate(t['directions']):
            fs=frozenset(FLIP[s] for s in t['domains'][i])
            endpoint_domains[(d+3)%6].add(fs)
            endpoint_origins[(d+3)%6,fs].append({'kind':t['kind'],'directions':t['directions'],'port':i})
    certificates=[];counts=Counter()
    for ti,t in enumerate(tables):
        choices=[sorted({frozenset(own&other) for other in endpoint_domains[d]},key=lambda a:''.join(s for s in ORDER if s in a))
                 for d,own in zip(t['directions'],t['domains'])]
        for domains in product(*choices):
            if any(not d for d in domains):counts['empty_endpoint_intersection']+=1;continue
            free=[];binary=[];fixed=[]
            for i,ds in enumerate(domains):
                if len(ds)>=3:
                    assert t['kind'] in('T','Y')
                    if t['kind']=='Y':
                        assert set(ds)==set('-IO')
                        possible=[q for D in endpoint_domains[t['directions'][i]] if ds<=D for q in endpoint_origins[t['directions'][i],D]]
                        assert possible and all(q['kind']=='T' for q in possible)
                    free.append(i)
                elif len(ds)==2:
                    assert '-' in ds and len(ds&set('IO'))==1
                    binary.append(i)
                else:fixed.append(i)
            live=[r for r in t['rows'] if all(s in ds for s,ds in zip(r,domains))]
            relation=sorted({tuple(int(r[i]!='-') for i in binary) for r in live})
            # A clause is stored as its forbidden partial assignment.
            # A missing projection to one/two variables supplies such a clause.
            clauses=[]
            if not relation:clauses=[[]]
            else:
                for arity in(1,2):
                    for ports in combinations(range(len(binary)),arity):
                        projected={tuple(r[i] for i in ports) for r in relation}
                        for bits in product((0,1),repeat=arity):
                            if bits not in projected:clauses.append(list(zip(ports,bits)))
            satisfying=[r for r in product((0,1),repeat=len(binary))
                        if all(any(r[i]!=b for i,b in clause) for clause in clauses)]
            assert satisfying==relation,(ti,domains,relation,clauses,satisfying)
            extension={''.join(map(str,r)):next(w for w in live if tuple(int(w[i]!='-') for i in binary)==r) for r in relation}
            certificates.append({'table':ti,'domains':[''.join(s for s in ORDER if s in ds) for ds in domains],
                'free_ports':free,'binary_ports':binary,'fixed_ports':fixed,'Boolean_relation':relation,
                'clauses_as_forbidden_partial_assignments':clauses,'extension_witnesses':extension})
            counts['complete_local_domain_cases']+=1
    # All inverted Ys use only odd directions. The opposite ray is even,
    # so two inverted Ys cannot be endpoints of one straight segment.
    ambiguous_y=[t for t in tables if t['kind']=='Y' and len(t['rows'])>1]
    assert len(ambiguous_y)==1 and set(ambiguous_y[0]['directions'])=={1,3,5}
    result={'canonical_rays':RAYS,'positive_axis_directions':PLUS,
            'tables':[{**t,'domains':[''.join(s for s in ORDER if s in ds) for ds in t['domains']]} for t in tables],
            'all_V_angle_checks':v_angles,'every_endpoint_marginal_domain_case':certificates,'counts':counts,
            'scope':'One globally oriented orthogonal-axis catalog. Its180degree screen rotation gives the other global parity. These catalogs must not be mixed locally.'}
    (ROOT/'results/orthohedral65.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'geometric_tables':len(tables),'V_cases':len(v_angles),'domain_cases':dict(counts)}))


if __name__=='__main__':main()

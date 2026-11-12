"""Confirm the printed fixed USA filtering states; no embedding search/census."""
from pathlib import Path
import json
import time

root = Path(__file__).resolve().parent
started = time.perf_counter()
H = {}
for line in (root/'sources/contiguous-usa-2026-11-07.dat').read_text().splitlines():
    u, v = line.split()
    H.setdefault(u, set()).add(v)
    H.setdefault(v, set()).add(u)
G = {(i,j): {(a,b) for a,b in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
              if 0 <= a < 4 and 0 <= b < 5} for i in range(4) for j in range(5)}

def matched(domains):
    mate = {}
    def augment(u, seen):
        for v in sorted(domains[u]):
            if v in seen:
                continue
            seen.add(v)
            if v not in mate or augment(mate[v], seen):
                mate[v] = u
                return True
        return False
    return all(augment(u, set()) for u in domains)

def lad(D):
    D = {u: set(vs) for u,vs in D.items()}
    changed = True
    while changed:
        changed = False
        # A forced assignment has the same global all-different propagation
        # as an explicit branch assignment (the rule stated on printed33).
        fixed = {}
        for u,vs in D.items():
            if len(vs)==1:
                v=next(iter(vs))
                if v in fixed:
                    D[u].clear()
                    return D
                fixed[v]=u
        for u in D:
            remove={v for v,w in fixed.items() if w != u} & D[u]
            if remove:
                D[u]-=remove
                changed=True
            if not D[u]: return D
        for u in G:
            for v in sorted(D[u]):
                if not matched({w: D[w] & H[v] for w in G[u]}):
                    D[u].remove(v)
                    changed = True
            if not D[u]:
                return D
    return D

def gad(D):
    return {u: {v for v in vs if matched({w: ws-{v} for w,ws in D.items() if w != u})}
            for u,vs in D.items()}

def assign(D, u, v):
    assert v in D[u]
    return {w: ({v} if w == u else vs-{v}) for w,vs in D.items()}

def row_table(groups):
    rows = ['iedei','hbabh','gcbcg','jgf gj'.replace(' ','')]
    return {(i,j): groups[c] for i,row in enumerate(rows) for j,c in enumerate(row)}

def words(s):
    return set(s.split())

initial = lad({u:set(H) for u in G})
az = lad(assign(initial,(1,2),'AZ'))
ar = lad(assign(initial,(1,2),'AR'))
a,b,c = words('AR'),words('MO OK TN'),words('KS KY MO')
d=b|words('LA MS TX'); e=b|c|words('AL MS NM TX'); f=b|c|words('CO IA IL NE VA')
g=f|words('IN WV');h=f|words('NC NM');i=e|g|h|words('GA');j=g|h|words('MD OH SD WI WY')
expected56=row_table(dict(a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h,i=i,j=j))
assert ar == expected56
ar_gad=gad(ar)
a,b,c = words('AR'),words('MO OK TN'),words('KS KY')
d=words('LA MS TX');e=words('AL MS NM TX');f=words('CO IA IL NE VA')
g=f|words('IN WV');h=f|words('NC NM');i=e|g|h|words('GA');j=g|h|words('MD OH SD WI WY')
expected58=row_table(dict(a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h,i=i,j=j))
assert ar_gad == expected58
ar_failed=lad(ar_gad)
assert any(not vs for vs in az.values()) and any(not vs for vs in ar_failed.values())
co=lad(assign(initial,(1,2),'CO'))
x=words('NE OK WY'); y=words('CA NM OR');a=words('CO');c=x|words('AZ ID MO SD TX')
d=x|words('KS NM UT');b=d;e=c|words('KS');h=e|words('AR IA MT NV UT');f=h
i=(h-words('AZ'))|y|words('IL LA MN ND TN');g=i;j=i|words('AZ KY MS WA WI')
expected59=row_table(dict(a=a,b=b,c=c,d=d,e=e,f=f,g=g,h=h,i=i,j=j))
assert co == expected59 and gad(co)==co
ok=lad(assign(co,(1,1),'OK'))
expected60=[['LA','TX','NM','AZ','CA NV'],['AR','OK','CO','UT','ID NV'],
            ['TN','MO','NE','WY','ID MT'],['KY','IL','IA','SD','MT ND']]
expected60={(i,j):words(s) for i,row in enumerate(expected60) for j,s in enumerate(row)}
if ok != expected60:
    difference={str(u):{'actual':sorted(ok[u]),'printed':sorted(vs)} for u,vs in expected60.items() if ok[u]!=vs}
    (root/'results/half-usa-filters-doubt.json').write_text(json.dumps(difference,indent=2)+'\n')
    print(json.dumps(difference))
assert ok == expected60
ca=lad(assign(ok,(0,4),'CA'))
fig112=[['LA','TX','NM','AZ','CA'],['AR','OK','CO','UT','NV'],
        ['TN','MO','NE','WY','ID'],['KY','IL','IA','SD','MT']]
assert ca == {(i,j):{s} for i,row in enumerate(fig112) for j,s in enumerate(row)}
for rows in [fig112, ['CA OR ID WY NE IA WI MI OH WV PA NJ'.split(),
                    'AZ NV UT CO KS MO IL IN KY VA MD DE'.split()],
             ['OR ID WY NE IA IL'.split(),'NV UT CO KS MO KY'.split(),'CA AZ NM OK AR TN'.split()]]:
    assert len(set(sum(rows,[])))==len(sum(rows,[]))
    for i,row in enumerate(rows):
        for j,v in enumerate(row):
            if i: assert v in H[rows[i-1][j]]
            if j: assert v in H[row[j-1]]
out={'scope':'Fixed propagation states56/58/59/60, Fig112, two181 witnesses. No search for all embeddings.',
     'initial_middle_domain':sorted(initial[1,2]),
     'AR_LAD':{str(u):sorted(vs) for u,vs in ar.items()},
     'AR_GAD':{str(u):sorted(vs) for u,vs in ar_gad.items()},
     'CO_LAD':{str(u):sorted(vs) for u,vs in co.items()},
     'CO_OK_LAD':{str(u):sorted(vs) for u,vs in ok.items()},
     'AZ_and_AR_contradictions':True,'three_fixed_grid_witnesses_valid':True,
     'elapsed_seconds':time.perf_counter()-started}
(root/'results/half-usa-filters.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'middle_domain_size':len(initial[1,2]),'printed_tables_match':True,
                  'fixed_witnesses':3,'elapsed_seconds':out['elapsed_seconds']}))

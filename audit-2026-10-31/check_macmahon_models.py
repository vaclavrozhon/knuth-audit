#!/usr/bin/env python3
"""Validate every exported LR model geometrically and explicitly quotient symmetries."""
import gzip
import itertools as it
import json
import operator
from collections import Counter
from check_macmahon import OUT,TRIANGLES,EDGE_TRIANGLES,PIECES,edges,piece,patchmask,reflect,opposite

ES=sorted(EDGE_TRIANGLES)
EI={e:i for i,e in enumerate(ES)}
TI={t:i for i,t in enumerate(TRIANGLES)}
ET=[tuple(EI[e] for e in edges(t)) for t in TRIANGLES]
PID={p:i for i,p in enumerate(PIECES)}
types=[];patch=[];mirror=[]
for cs in it.product('abcd',repeat=3):
    types.append(PID[piece(cs)])
    patch.append(patchmask(cs))
    mirror.append(patchmask((cs[0],cs[2],cs[1])))
PAIR=[(TI[t],TI[reflect(t,'lr')]) for t in TRIANGLES if t<=reflect(t,'lr')]

def transform_data(mono):
    data=[]
    funcs=[lambda t:t,lambda t:reflect(t,'lr'),lambda t:reflect(t,'tb'),opposite]
    for n,g in enumerate(funcs):
        side=(0,2,1) if n in (1,2) else (0,1,2)
        perm={}
        for t in TRIANGLES:
            for i,e in enumerate(edges(t)):
                f=edges(g(t))[side[i]]
                assert e not in perm or perm[e]==f
                perm[e]=f
        assert set(perm.values())==set(ES)
        inverse=[None]*42
        for e,f in perm.items():inverse[EI[f]]=EI[e]
        color={old:new for new,(_,old) in enumerate(sorted((g(tuple(t)),old) for old,t in enumerate(mono)))}
        trans=bytes.maketrans(b'abcd',bytes(97+color[i] for i in range(4)))
        data.append((operator.itemgetter(*inverse),trans))
    return data

def main():
    meta=json.loads((OUT/'lr/metadata.json').read_text());freq=Counter();raw=0;seen=set()
    for d in meta:
        if d['fixed']:continue
        f=OUT/'lr'/f'{d["index"]:03d}.models.txt.gz'
        tr=transform_data(d['mono']);local=0
        with gzip.open(f,'rb') as inp:
            for line in inp:
                cs=line.rstrip(b'\n');assert len(cs)==42 and set(cs)<=set(b'abcd')
                assert cs not in seen;seen.add(cs)
                colors=[((cs[a]-97)*4+(cs[b]-97))*4+cs[c]-97 for a,b,c in ET]
                pieces=[types[c] for c in colors]
                assert len(set(pieces))==24
                assert all(patch[colors[a]]==mirror[colors[b]] for a,b in PAIR)
                for c,t in enumerate(d['mono']):assert colors[TI[tuple(t)]]==21*c
                canonical=min(bytes(get(cs)).translate(trans) for get,trans in tr)
                freq[canonical]+=1;raw+=1;local+=1
        print('validated',d['index'],local,'total',raw,flush=True)
    histogram=Counter(freq.values())
    assert set(histogram)<={2,4},histogram
    result=dict(raw_models=raw,canonical_patterns=len(freq),orbit_sizes=dict(histogram),
                strong_rotational=histogram[2],weak_not_strong=histogram[4],
                claim='Every exported model checked for all 24 pieces and weak reflection; explicit four-element spatial quotient after color normalization.')
    (OUT/'lr-canonical-models.json').write_text(json.dumps(result,indent=2)+'\n')
    with gzip.open(OUT/'lr-canonical-colors.txt.gz','wb') as z:
        for cs in sorted(freq):z.write(cs+b'\n')
    print(result,flush=True)

if __name__=='__main__':main()

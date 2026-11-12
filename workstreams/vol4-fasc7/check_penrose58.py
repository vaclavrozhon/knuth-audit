#!/usr/bin/env python3
"""Every native Penrose picture; exact ordered network and small count witnesses.

The symbolic all-n proofs are in notes/hc-penrose-031-058.md. This is not a
search for a three-dimensional realization or a census over 4^(5n) labels.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json
import xml.etree.ElementTree as ET
from check_clasp_projection import ROOT, sub, dot, cross2
from check_cubie_junctions import path_points
from check_hc_drawings26_27 import network
from check_line_csp22 import TABLE, global_symbol, ORDER, propagate
from check_polyhedra_fixed import encode


def name(kind, k, n):
    return kind + str(k % n)


def expected(n):
    ans = {}
    for k in range(n):
        for kind, neighbors in [
            ('t', [('t', k-1), ('t', k+1), ('u', k)]),
            ('u', [('w', k+1), ('t', k)]),
            ('v', [('w', k), ('w', k-1)]),
            ('w', [('v', k+1), ('u', k-1), ('v', k)]),
        ]:
            ans[name(kind, k, n)] = {'type': {'t':'T','u':'V','v':'V','w':'W'}[kind],
                                   'neighbors': [name(a,b,n) for a,b in neighbors]}
    return ans


def cyclic(seq):
    return min(tuple(seq[k:] + seq[:k]) for k in range(len(seq)))


def reconstruct(paths, tag, n, words):
    occurrences = defaultdict(list)
    for pi, word in words.items():
        ps = path_points(paths[pi])
        assert len(ps) == len(word)
        for j,p in zip(word,ps): occurrences[j].append(p)
    points = {j:tuple(sum(p[k] for p in ps)/len(ps) for k in (0,1)) for j,ps in occurrences.items()}
    # The first endpoint t's are exact native points. Enforce the intended
    # T incidence by orthogonally projecting each rounded u onto its bar.
    # No noncollinear junction or crossing is silently snapped.
    extensions = {}
    for k in range(n):
        a,b,c = [points[name(kind,i,n)] for kind,i in [('t',k-1),('t',k),('u',k)]]
        d = sub(b,a); r = dot(sub(c,a),d)/dot(d,d)
        assert r>1
        points[name('u',k,n)] = tuple(a[i]+r*d[i] for i in (0,1))
        extensions[name('u',k,n)] = r-1
    residuals = [sum((p[k]-points[j][k])**2 for k in (0,1))
                 for j,ps in occurrences.items() for p in ps]
    assert max(residuals)<F(1,10000), (tag,float(max(residuals)))
    mapped = {pi:[points[j] for j in word] for pi,word in words.items()}
    pp,ns,rs,lines,faces,boundary = network(mapped,paths)
    assert len(pp)==4*n
    inverse = {p:j for j,p in points.items()}; ren = {j:inverse[p] for j,p in pp.items()}
    actual = {ren[j]:{'type':v['type'],'neighbors':[ren[k] for k in v['neighbors']]} for j,v in ns.items()}
    assert actual==expected(n), (tag,actual,expected(n))
    facewords = [[ren[j] for j in f['walk']] for f in faces]
    central = [name('t',-k,n) for k in range(n)]
    outer = [name(a,k,n) for k in range(n) for a in ['v','w']]
    ring = [[name(a,b,n) for a,b in [('w',k),('u',k-1),('t',k-1),('t',k),('u',k),('w',k+1),('v',k+1)]] for k in range(n)]
    assert {cyclic(f) for f in facewords}=={cyclic(f) for f in [central,outer]+ring}
    assert cyclic([ren[j] for j in boundary])==cyclic(outer)
    # Every central side has all other t vertices strictly to its right.
    for k in range(n):
        a,b=points[name('t',k,n)],points[name('t',k+1,n)]
        assert all(cross2(sub(b,a),sub(points[name('t',j,n)],a))>0
                   for j in range(n) if j not in (k,(k+1)%n))
    center = tuple(sum(points[name('t',k,n)][i] for k in range(n))/n for i in (0,1))
    sides = []
    for k in range(n):
        a,b = points[name('u',k-1,n)],points[name('w',k,n)]
        margins=[cross2(sub(b,a),sub(points[name('t',j,n)],a)) for j in range(n)]
        assert min(margins)>0
        sides.append({'crease':[name('u',k-1,n),name('w',k,n)],'central_vertex_side_determinants':margins})
    out = {'picture':tag,'n':n,'native_paths':words,'points':points,
           'maximum_source_residual_squared':max(residuals),'T_bar_extensions':extensions,
           'junctions':actual,'line_count':len(lines),'faces':facewords,'outer_boundary':outer,
           'center':center,'crease_center_sides':sides}
    if n==3:
        carriers=[]
        for k in range(n):
            a,b=points[name('u',k-1,n)],points[name('w',k,n)]
            carriers.append([a[1]-b[1],b[0]-a[0],cross2(a,b)])
        x,y,z=carriers
        determinant=sum(x[i]*(y[(i+1)%3]*z[(i+2)%3]-y[(i+2)%3]*z[(i+1)%3]) for i in range(3))
        assert determinant
        out['three_crease_carriers']=carriers
        out['native_crease_nonconcurrency_determinant']=determinant
    return out


def labels(n):
    ns=expected(n);relations={}
    for j,v in ns.items():
        variables=['_'.join(sorted((j,k))) for k in v['neighbors']]
        rows=[''.join(global_symbol(s,j,k) for s,k in zip(row,v['neighbors'])) for row in TABLE[v['type']]]
        relations[j]=(variables,rows)
    edges=sorted({e for vs,rs in relations.values() for e in vs})
    assert len(edges)==5*n
    domains,trace=propagate(relations,{e:set(ORDER) for e in edges})
    assert domains is not None
    assignments=[]
    for word in product('>-',repeat=n):
        if any(word[k]==word[(k+1)%n]=='-' for k in range(n)):continue
        values={}
        def set_edge(a,b,s):
            e='_'.join(sorted((a,b)))
            value=global_symbol(s,a,b)
            assert e not in values or values[e]==value
            values[e]=value
        for k in range(n):
            set_edge(name('t',k,n),name('t',k-1,n),'O')
            set_edge(name('u',k,n),name('t',k,n),'O')
            set_edge(name('u',k,n),name('w',k+1,n),'+')
            s='O' if word[k]=='>' else '-'
            set_edge(name('v',k,n),name('w',k,n),s)
            set_edge(name('w',k,n),name('v',k+1,n),s)
        assert len(values)==5*n
        assert all(''.join(values[e] for e in es) in rows for es,rows in relations.values())
        assignments.append({'boundary_W_states':''.join(word),'all_line_labels':values})
    return {'n':n,'all_small_cyclic_words':assignments,'count':len(assignments),
            'unrestricted_GAC_domains':{e:''.join(s for s in ORDER if s in d) for e,d in domains.items()},
            'unrestricted_GAC_trace':trace}


def main():
    paths134=[p.attrib for p in ET.parse(ROOT/'sources/file-134.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    pics=[]
    for n,start in [(3,19),(4,22),(5,26),(6,31)]:
        words={start+i:[name(a,b,n) for a,b in [('t',-i),('u',-i+1),('w',-i+2),('v',-i+2),('w',-i+1)]] for i in range(n)}
        pics.append(reconstruct(paths134,'58-n%d'%n,n,words))
    paths30=[p.attrib for p in ET.parse(ROOT/'sources/file-030.svg').findall('.//{http://www.w3.org/2000/svg}path')]
    words={58:['w0','v0','w2','v2','w1','v1','w0'],59:['w0','u2','t1'],60:['w2','u1','t0'],61:['w1','u0','t2']}
    pics.append(reconstruct(paths30,'31-main-Penrose-triangle',3,words))
    small=[labels(n) for n in range(3,7)]
    assert [r['count'] for r in small]==[4,7,11,18]
    out={'known_correction':'err4f7 TeX26.09.06: w_k=W(v_(k+1),u_(k-1),v_k)',
         'pictures':pics,'small_count_certificates':small,
         'scope':'Every original path and local order; all-n deductions are separately proved in notes/hc-penrose-031-058.md.'}
    (ROOT/'results/penrose58.json').write_text(json.dumps(out,indent=2,default=encode)+'\n')
    print(json.dumps([{'picture':p['picture'],'junctions':len(p['junctions']),'lines':p['line_count'],
                       'max_residual_squared':str(p['maximum_source_residual_squared'])} for p in pics]))
    print('cyclic counts',[(x['n'],x['count']) for x in small])


if __name__=='__main__':main()

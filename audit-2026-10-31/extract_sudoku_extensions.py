#!/usr/bin/env python3
"""Original vector diagrams for DLX64--67; reuse the archived geometry reader."""
import json
import math
import extract_jigsaw as geometry
from dlx1_audit_tools import ROOT,sha

OUT=ROOT/'results/sudoku_extensions'


def extract_layers(page,n,x0,y0,step,alphabet,ignore_shading=False):
    """Keep conflicting glyph provenance; expose the last painted layer.

    No original PDF or trace file is changed. The ordinary reader deliberately
    rejects conflicting duplicate glyphs. Here both layers remain documented.
    """
    original=geometry.trace;tree=original(page);bycell={}
    for text in tree.iter('fill_text'):
        for span in text:
            for g in span:
                ch=g.get('unicode','')
                if len(ch)!=1 or ch not in alphabet:continue
                x,y=geometry.transform(text,float(g.get('x')),float(g.get('y')))
                c,r=math.floor((x-x0)/step),math.floor((y-y0)/step)
                if 0<=r<n and 0<=c<n:
                    bycell.setdefault(r*n+c,[]).append((span,g,dict(text=ch,origin=[x,y],font=span.get('font'))))
    conflicts=[]
    for v,entries in bycell.items():
        if len({g.get('unicode')for _,g,_ in entries})<2:continue
        conflicts.append(dict(cell=v,row=v//n+1,column=v%n+1,paint_order=[s for _,_,s in entries]))
        last=entries[-1][1].get('unicode')
        for span,g,_ in entries:
            if g.get('unicode')!=last:span.remove(g)
    shading=[]
    if ignore_shading:
        for parent in tree.iter():
            for p in list(parent):
                if p.tag=='fill_path' and p.get('colorspace')=='DeviceRGB':
                    shading.append(dict(color=p.get('color'),polygons=geometry.paths(p)))
                    parent.remove(p)
    try:
        geometry.trace=lambda p:tree
        result=geometry.extract(page,n,n,x0,y0,step,alphabet)
    finally:geometry.trace=original
    result['conflicting_glyph_layers']=conflicts
    if ignore_shading:result['separate_shading']=shading
    return result


def main():
    OUT.mkdir(exist_ok=True);geometry.OUT=OUT
    d={}
    d['64']=geometry.extract(130,6,6,354.059,85.91895,53.702/6,'ABCDEF')
    d['64-proof']=geometry.extract(429,7,7,341.639,451.97898,62.701/7,'1234567abcdefghijkl')
    specs=[('DANCING',7,52.829,174.38898,44.401,40.409,555.449),
           ('LINKS',5,107.429,180.729,31.702,95.009,561.78897),
           ('COMPUTER',8,149.37,171.16999,50.8,136.95,552.23),
           ('ALGORITHM',9,210.32999,167.98999,57.101,197.91,549.11),
           ('SOLVING',7,277.589,174.38898,44.401,265.169,555.449),
           ('SUDOKU',6,332.19,177.50995,38.1,319.77,558.56997),
           ('PUZZLE',6,380.49,177.50995,38.1,368.07,558.56997)]
    for word,n,x,y,width,xx,yy in specs:
        for label,page,px,py,alphabet in [('q',130,x,y,word),('a',429,xx,yy,word+'.')]:
            s=extract_layers(page,n,px,py,width/n,alphabet)
            assert len(s['regions'])==n and all(len(r)==n for r in s['regions']),(word,label,s['regions'])
            d['65'+label+'-'+word]=s
        assert d['65q-'+word]['regions']==d['65a-'+word]['regions'],word
    for row,y in [('i',258.978),('ii',291.678)]:
        for k,x in enumerate([81.898,117.658,153.418,189.238,224.998,260.758,296.578,332.338,368.098],1):
            s=geometry.extract(130,3,3,x,y,26.804/3,'123456789')
            assert len(s['glyphs'])==4 and [i for i,v in enumerate(s['cells'])if v!='.']==[0,4,6,8]
            d[f'66-{row}-{k}']=s
    for label,x in [('i',137.519),('ii',260.399)]:
        d['67q-'+label]=extract_layers(130,9,x,359.739,80.601/9,'123456789',True)
    for label,x,alphabet in [('boxes',90.179,'abcde'),('i',194.099,'123456789'),('ii',300.539,'123456789')]:
        d['67a-'+label]=extract_layers(430,9,x,275.799,80.601/9,alphabet,True)
    for k,s in d.items():print(k,'/'.join(s['rows']),len(s['glyphs']),list(map(len,s['regions'])))
    result=dict(book_sha256=sha(geometry.BOOK),source_sha256=sha(__file__),helper_sha256=sha(ROOT/'extract_jigsaw.py'),
                trace_sha256={str(p):sha(OUT/f'page{p}-trace.xml')for p in [130,429,430]},sources=d)
    (OUT/'pdf-diagrams.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()

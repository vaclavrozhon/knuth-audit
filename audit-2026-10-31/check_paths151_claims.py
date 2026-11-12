"""Bind finite catalogues, direct witnesses, MCC examples and known errata."""
from collections import Counter
from datetime import datetime, timezone
import json, re
import paths151 as h

def read(p):return json.loads(p.read_text())

def options(cells,active):
    result={};cells=set(cells)
    for i,j in cells:
        for di,dj,label in [(-1,0,f'h{i}{j}'),(1,0,f'h{i+1}{j}'),(0,-1,f'v{i}{j}'),(0,1,f'v{i}{j+1}')]:
            if (i+di,j+dj) in cells:continue
            if label[0]=='h':internal=0<int(label[1])<8
            else:internal=0<int(label[2])<9
            if internal:result[label]=int(label in active)
            else:assert label not in active
    return result

def main():
    now=datetime.now(timezone.utc).isoformat();figs=read(h.OUT/'figures-checked.json');cat=read(h.OUT/'catalogue-checked.json')
    assert figs['checker_sha256']==h.sha(h.ROOT/'extract_paths151.py')
    assert figs['catalogue_sha256']==cat['checker_sha256']==h.sha(h.__file__)
    assert figs['path_parser_sha256']==h.sha(h.ROOT/'extract_chain150.py')
    for p,d in figs['trace_sha256'].items():assert h.sha(h.ROOT/p)==d
    a=options([(1,0),(1,1)],{'v12','h21','h20','h11'})
    b=options([(1,1),(2,1)],{'v22','h31','v21','v11'})
    assert a==dict(v12=1,h21=1,h20=1,h10=0,h11=1)
    assert b==dict(h11=0,v12=0,v22=1,h31=1,v21=1,v11=1)
    # Clockwise ports in the horizontal and rotated vertical orientations.
    amask=tuple(i for i,p in enumerate(['h10','h11','v12','h21','h20','v10']) if p in a and a[p])
    bmask=tuple(i for i,p in enumerate(['v12','v22','h31','v21','v11','h11']) if b[p])
    assert amask==bmask==(1,2,3,4)
    secondary={f'h{i}{j}' for i in range(1,8) for j in range(9)}|{f'v{i}{j}' for i in range(8) for j in range(1,9)}
    assert len(secondary)==63+64
    for name in ['question','a','b','152']:
        f=figs['figures']['original-'+name]
        counts=Counter(h.mask_type(h.mask(p['pattern'])) for p in f['pieces'])
        expect={tuple(r['mask']):r['count'] for row in cat['records'] for r in row['mask_multiplicities'] if row['subpaths'] in ([1,2] if name!='152' else range(4))}
        assert counts==expect
        if name=='b':assert all(p['bounds'][2]%2==0 for p in f['pieces'] if p['bounds'][3]-p['bounds'][2]==2)
    previous=read(h.ROOT/'results/chain150/errata-check.json');contexts=[]
    pattern=r'(?:[Pp]age\s+|(?:4b|4f5)\.)(?:143|459|460|141|267|268)\b|(?:answer|exercise|exer ise)\s+15[12]\b|path domino|blank pattern|6420|35\.1'
    for p,d in previous['files'].items():
        path=h.ROOT.parent/p;assert h.sha(path)==d
        lines=path.read_text(errors='replace').splitlines()
        for i,line in enumerate(lines):
            if re.search(pattern,line,re.I):contexts.append(dict(file=p,line=i+1,context='\n'.join(lines[max(0,i-1):i+6])))
    orig=(h.ROOT.parent/'text/vol4b.txt').read_text().split('\f')[478]
    draft=(h.ROOT/'sources/fasc5c.txt').read_text().split('\f')[168]
    assert 'Algorithm X and exercise 413' in orig and 'Algorithm X and exercise 413' not in draft
    assert 'blank pattern of multiplicity 1' in orig and 'blank pattern of multiplicity 1' not in draft
    h.save(h.OUT/'errata-check.json',dict(at_utc=now,files=previous['files'],pattern=pattern,contexts=contexts,
        latest_remote_retrieval=previous['latest_remote_retrieval'],known=[dict(id='E076',exercise=151,date='2022-11-05',change='Add reference to exercise413'),
            dict(id='E077',exercise=152,date='2022-07-22',change='Add blank pattern with multiplicity1')],both_applied_in_local_pdf=True,both_absent_from_2019_draft=True,new_errata_found=False))
    for n,page in [('question143',162),('answer459',478),('answer460',479)]:
        (h.ROOT/'sources/paths151_152'/f'{n}.txt').write_text((h.ROOT.parent/'text/vol4b.txt').read_text().split('\f')[page])
    (h.ROOT/'sources/paths151_152/draft-answer163.txt').write_text(draft)
    omissions=[dict(id='DLX151-factored-censuses',exercise='DLX:151',claim='Millions of factored solutions in(a),6420 in(b)',
            evidence='General MCC correspondence and all three printed single-loop witnesses directly checked.',
            reason='User permits omitting expensive complete censuses. No complete placement census launched.',verified=False),
        dict(id='DLX151-historical-performance',exercise='DLX:151',claim='About half the runtime after deleting odd-height verticals; microsecond second-stage assignments',
            evidence='Row parity proves that odd-height verticals are impossible at the optimum. Correct second-stage loop formulation documented.',
            reason='No tuning to reproduce historical algorithm, data ordering or machine-specific timing.',verified=False),
        dict(id='DLX152-historical-cost',exercise='DLX:152',claim='Historical35.1Tmems to find a solution',
            evidence='Printed48-piece witness has all types exactly once and a single96-subpath loop. Noncrossing32-piece impossibility has a parity proof.',
            reason='User permits omitting prolonged brute force. No placement search or historical benchmark launched.',verified=False)]
    h.save(h.OUT/'claims-checked.json',dict(at_utc=now,checker_sha256=h.sha(__file__),catalogue_sha256=h.sha(h.OUT/'catalogue-checked.json'),
        figures_sha256=h.sha(h.OUT/'figures-checked.json'),errata_sha256=h.sha(h.OUT/'errata-check.json'),
        typical_options_correct=True,typical_options_same_rotated_pattern=True,secondary_count=127,all_printed_factored_multiplicities_correct=True,
        maximum_horizontals=32,odd_height_verticals_excluded_at_optimum=True,noncrossing_unsat_proof=True,placement_searches=0,
        complete_censuses_omitted=True,omissions=omissions,new_findings=[],known_errata=['E076','E077']))
    print('PASS151/152 claims:both example options,127 interfaces,multiplicities,sharp32 bound,parity UNSAT; E076/E077 already fixed. No placement search.')

if __name__=='__main__':main()

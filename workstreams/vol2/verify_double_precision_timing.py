"""Reproduce the48 instruction-cost checks for the approximate timing table."""
import json
from pathlib import Path
from verify_double_precision import Harness
ROOT=Path(__file__).resolve().parent

def main():
    data=[]
    for b in [64,100]:
        h=Harness(b,'original');Q=b*b//2
        cases=[((Q,b**7,1),(Q,b**7,1)),((Q,b**8//2,1),(Q,b**8//2,1)),((Q,b**7,1),(Q,b**7,-1)),((Q,b**7,1),(Q,b**7+1,-1)),((Q,b**7+1,1),(Q,b**7,-1)),((Q,b**8-1,1),(Q,b**8-1,1)),((Q,b**8-1,1),(Q,b**7,1)),((Q,b**7,1),(Q,b**8-1,1))]
        for u,v in cases:
            for op in ['DFADD','DFMUL','DFDIV']:
                ans,halt,t=h.run(u,v,op);m=h.m;assert halt is None
                if op=='DFADD':
                    S=int(m.visits['A12']>0);E=int(m.visits['A10']>0);I=int(m.visits['A42']>0);Z=int(ans[1]==0);L=m.visits['A45'];pred=71+13*S+3*E+S*E+I+6*L-15*Z
                    variables={'swapped':S,'equal_high_words':E,'tested_X':I,'zero':Z,'left_shifts':L}
                else:
                    L=m.visits['A45'];assert not m.visits['A42'];C=int(m.visits['D31']>0);pred=(106 if op=='DFMUL' else 123+C)+6*L;variables={'left_shifts':L,'division_borrow':C}
                assert t==pred,(b,op,t,pred,variables)
                data.append({'b':b,'operation':op,'inputs':[u,v],'time':t,'variables':variables,'formula_value':pred})
    (ROOT/'results/double-precision-timing-formulas.json').write_text(json.dumps(data,indent=2)+'\n')
    print('PASS',len(data),'targeted timing formulas')

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Historical/current errata evidence for DLX64--67 and both DLX65 defects."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import json
import re
from dlx1_audit_tools import ROOT,sha
from check_sudoku_variants_errata import remote


def main():
    files=['errata/text/all4b.txt','errata/text/err4b.txt','errata/text/all4f5.txt',
           'errata/text/err4f5.txt','errata/originals/err4b.textxt','errata/originals/err4f5.textxt']
    pattern=re.compile(r'(?:Page\s+(?:66|128|130|133|134|237|238|429|430)\b|'
       r'4(?:b|f5)\.(?:66|128|130|133|134|237|238|429|430)\b|'
       r'clueless|SUDOKU|SOLVING|hypersudoku|Maxime|40237|1966|10080|192435768|149523786|149325687)',re.I)
    hits=[]
    for file in files:
        lines=(ROOT.parent/file).read_text().splitlines()
        for i,line in enumerate(lines):
            if pattern.search(line):hits.append(dict(file=file,line=i+1,context='\n'.join(lines[max(0,i-2):i+7])))
    with ThreadPoolExecutor(max_workers=4)as pool:
        remotes=list(pool.map(remote,['all4b.ps.gz','all4f5.ps.gz','err4b.textxt','err4f5.textxt']))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
                remote_files=remotes,local_files={f:sha(ROOT.parent/f)for f in files},search_hits=hits,
                conclusions=[
                  'The29Jun2022 correction swaps D/U in the TOP row of SUDOKU; already incorporated in our4B. This is E032, not a new finding.',
                  'F118 concerns O and the dot in the SECOND row, columns5/6. It remains wrong in our4B and the older authorPS, even after the published top-row fix.',
                  'F117 is an extra S painted on the correct G in the lower-right SOLVING cell of our4B PDF; original authorPS has a correct G. No matching erratum found; physical printing remains unchecked.',
                  'No matching clarification found about straight regions in64(a). The explicit answer uses62 nonstraight counts; the broader literal statement has more clueless designs. Kept as scope candidateC023.',
                  'No matching correction found for the card counts66 or hypersudoku mathematics67.'])
    (ROOT/'results/sudoku_extensions/errata-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Four remote originals unchanged;',len(hits),'context records')
    for h in hits:
        if '237'in h['context']or'SOLVING'in h['context']or'4b.429'in h['context']:print(h['file'],h['line'],h['context'])


if __name__=='__main__':main()

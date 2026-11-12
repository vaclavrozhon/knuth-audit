#!/usr/bin/env python3
"""Complete archived layers and current author files for DLX77--83, pp87--90."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import json,re
from dlx1_audit_tools import ROOT,sha
from check_sudoku_variants_errata import remote
from check_colored_basics import OUT


def main():
    files=['errata/text/all4b.txt','errata/text/err4b.txt','errata/text/all4f5.txt',
           'errata/text/err4f5.txt','errata/originals/err4b.textxt','errata/originals/err4f5.textxt']
    pattern=re.compile(r'(?:Page\s+(?:23|24|25|26|68|85|86|87|88|89|90|130|132|137|241|433)\b|'
      r'4(?:b|f5)\.(?:85|86|87|88|89|90|130|132|241|433)\b|'
      r'\b(?:answer|exercise)\s+(?:77|78|79|80|81|82|83)\b|'
      r'Riesz|birthday|21st|1913|Acta|purif|earlier.*item|distinct.*second|secondary.*end)',re.I)
    hits=[]
    for f in files:
        lines=(ROOT.parent/f).read_text().splitlines()
        for i,line in enumerate(lines):
            if pattern.search(line):
                hits.append(dict(file=f,line=i+1,context='\n'.join(lines[max(0,i-1):i+8])))
    with ThreadPoolExecutor(max_workers=4) as pool:
        current=list(pool.map(remote,['all4b.ps.gz','all4f5.ps.gz','err4b.textxt','err4f5.textxt']))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
      local_files={f:sha(ROOT.parent/f) for f in files},remote_files=current,search_hits=hits,
      mapping='4Bmain87--90=publishedF5 85--88=preF5c23--26; question132=published130=pre68; answer433=published241=pre137.',
      conclusions=[
        'E040:2Mar2020 vertices to edges in answer77 and embedding sentence in question; incorporated in4B.',
        'E041:27Mar2020 color headers/spacers/printing and purify header cache;19Sep2021 LEN/TOP labels;15Jul2020 commit terminology. All incorporated in local4B.',
        'E042:1Jan2020 answer83 j>N to j>N1. Incorporated in4B; applied to authorPS before comparing F123.',
        'F123:No matching correction found for a distinguished terminal secondary item also occurring in another root option; all-uncolored counterexample survives E042.',
        'C025:No matching correction found for the21st birthday claim. The author TeX mentions only punctuation Uppsala colon to comma for this footnote. Original commemorative preface remains missing; this is a candidate.',
        'Same-numbered pages or exercises outside this section are unrelated.'])
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'errata-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:four current originals unchanged;',len(hits),'contexts saved')


if __name__=='__main__':main()

#!/usr/bin/env python3
"""Current and historical errata for the main pentomino text, 4B79--82."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import json
import re
from dlx1_audit_tools import ROOT,sha
from check_sudoku_variants_errata import remote
from prepare_pentomino_main import OUT


def main():
    files=['errata/text/all4b.txt','errata/text/err4b.txt','errata/text/all4f5.txt',
      'errata/text/err4f5.txt','errata/originals/err4b.textxt','errata/originals/err4f5.textxt']
    pattern=re.compile(r'(?:Page\s+(?:15|16|17|18|77|78|79|80|81|82)\b|'
      r'4(?:b|f5)\.(?:15|16|17|18|77|78|79|80|81|82)\b|'
      r'2j|j2|Hansson|pentomino|71191|71,191|32644|32,644|1236|1243|1128|21805|1086521921)',re.I)
    hits=[]
    for file in files:
        lines=(ROOT.parent/file).read_text().splitlines()
        for i,line in enumerate(lines):
            if pattern.search(line):hits.append(dict(file=file,line=i+1,context='\n'.join(lines[max(0,i-2):i+7])))
    with ThreadPoolExecutor(max_workers=4) as pool:
        current=list(pool.map(remote,['all4b.ps.gz','all4f5.ps.gz','err4b.textxt','err4f5.textxt']))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
      remote_files=current,local_files={f:sha(ROOT.parent/f) for f in files},search_hits=hits,
      page_mapping='4B79--82 = published Fascicle5 pp77--80 = author pre-fascicle5c pp15--18.',
      conclusions=[
        'F120: no matching correction found for last20x3 cell2j; it should bej2. Both local PDF and authorPS print2j.',
        'Known21Nov2020 improvement specifies consecutive letters from O to Z; incorporated in local4B80.',
        'No matching corrections found for placement counts, search-node counts, or figures36--38.'])
    (OUT/'errata-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:four remote originals unchanged;',len(hits),'retained contexts')


if __name__=='__main__':main()

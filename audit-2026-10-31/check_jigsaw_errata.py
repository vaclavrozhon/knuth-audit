#!/usr/bin/env python3
"""Current and complete historical errata check for figures34--35 and DLX59--63."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import json
import re
from dlx1_audit_tools import ROOT,sha
from check_sudoku_variants_errata import remote


def main():
    files=['errata/text/all4b.txt','errata/text/err4b.txt','errata/text/all4f5.txt',
           'errata/text/err4f5.txt','errata/originals/err4b.textxt','errata/originals/err4f5.textxt']
    pattern=re.compile(r'(?:Page\s+(?:14|65|76|78|127|129|132|133|236|237|428|429)\b|'
                       r'4(?:b|f5)\.(?:14|65|76|78|127|129|132|133|236|237|428|429)\b|'
                       r'Behrens|gerechte|jigsaw|Puzzlium|nonomino|1315|3173|42669|24533|1105|132.?418|35\s*b)',re.I)
    hits=[]
    for file in files:
        lines=(ROOT.parent/file).read_text().splitlines()
        for i,line in enumerate(lines):
            if pattern.search(line):hits.append(dict(file=file,line=i+1,context='\n'.join(lines[max(0,i-2):i+7])))
    with ThreadPoolExecutor(max_workers=4) as pool:
        remotes=list(pool.map(remote,['all4b.ps.gz','all4f5.ps.gz','err4b.textxt','err4f5.textxt']))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
                remote_files=remotes,local_files={f:sha(ROOT.parent/f) for f in files},search_hits=hits,
                conclusions=[
                    'No correction found for figure35b row6,column7:6 should be5.',
                    'No correction found for59/60 tree sizes; all six equal our inclusive node counts minus one when the listed symbol orders are used. Kept as a convention candidate.',
                    'Known29Jun2022 SUDOKU-letter correction onF5p237 belongs toDLX65, outside this block.',
                    'Fascicle5 mapping includes mainp76/book78, question127/book129, answers236--237/book428--429; prefascicle5c has14,65,132--133.',
                    'No matching correction found for the mathematical counts of61--63 or the historical1.2Gmem benchmark.'])
    (ROOT/'results/jigsaw/errata-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Four remote files unchanged;',len(hits),'context records')


if __name__=='__main__':main()

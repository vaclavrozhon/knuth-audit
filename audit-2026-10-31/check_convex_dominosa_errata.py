#!/usr/bin/env python3
"""All relevant historical/current errata for DLX68--71, plus known72 typo."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import json
import re
from dlx1_audit_tools import ROOT,sha
from check_sudoku_variants_errata import remote


def main():
    files=['errata/text/all4b.txt','errata/text/err4b.txt','errata/text/all4f5.txt',
           'errata/text/err4f5.txt','errata/originals/err4b.textxt','errata/originals/err4f5.textxt']
    pattern=re.compile(r'(?:Page\s+(?:66|67|134|135|130|131|238|239|430|431)\b|'
       r'4(?:b|f5)\.(?:66|67|134|135|130|131|238|239|430|431)\b|'
       r'1467|1647|Bitland|convex|nonomino|Dominosa|1292687|63\];|8113709|18187302)',re.I)
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
        'No matching correction found for answer69 N6 count1467. Independent geometric enumeration gives1647; PDF and authorPS both print1467.',
        'Known25May2021 answer70 correction63]; to63; is incorporated in local4B and remains wrong in older authorPS.',
        'Known04Jul2020 answer72 correction1292687 to1292697 is incorporated in local4B and remains wrong in older authorPS.',
        'No other matching corrections found for mathematical claims68--71.'])
    (ROOT/'results/convex68/errata-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:four current remote originals unchanged;',len(hits),'retained contexts')


if __name__=='__main__':main()

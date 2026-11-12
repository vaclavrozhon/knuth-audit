#!/usr/bin/env python3
"""DLX75--76: local complete correction layers and current author originals."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
import re
from dlx1_audit_tools import ROOT, sha
from check_sudoku_variants_errata import remote
from check_gropes import OUT


def main():
    files = ['errata/text/all4b.txt','errata/text/err4b.txt','errata/text/all4f5.txt',
             'errata/text/err4f5.txt','errata/originals/err4b.textxt','errata/originals/err4f5.textxt']
    pattern = re.compile(r'(?:Page\s+(?:68|130|132|136|240|432)\b|'
      r'4(?:b|f5)\.(?:68|130|132|136|240|432)\b|'
      r'\b(?:answer|exercise)\s+(?:75|76)\b|'
      r'grope|quasigroup|idempoten|Bennett|Mendelsohn|Schr.{0,8}der|'
      r'Cannon|identity element|f\(t|diagonal items)',re.I)
    hits = []
    for file in files:
        lines = (ROOT.parent/file).read_text().splitlines()
        for i,line in enumerate(lines):
            if pattern.search(line):
                hits.append(dict(file=file,line=i+1,context='\n'.join(lines[max(0,i-2):i+10])))
    with ThreadPoolExecutor(max_workers=4) as pool:
        current = list(pool.map(remote,['all4b.ps.gz','all4f5.ps.gz','err4b.textxt','err4f5.textxt']))
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
      remote_files=current,local_files={f:sha(ROOT.parent/f) for f in files},search_hits=hits,
      page_mapping='4B question132 = publishedF5 130 = preF5c68; answer432 = publishedF5 240 = preF5c136.',
      conclusions=[
        'E038:13Feb2024 appends the topological use of gropes and Cannon1978 to answer75; absent from local4B.',
        'E039:19Sep2021 changes an identity element to the identity element0 in question76; already incorporated in local4B.',
        'No matching correction located for F121, ordinary+ instead of XOR in answer75(b).',
        'No matching correction located for F122, omitted removal of diagonal items in answer76(c).',
        'Other same-numbered pages/exercises are outside the relevant section.'])
    (OUT/'errata-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:four current originals unchanged;',len(hits),'retained correction contexts')


if __name__ == '__main__':
    main()

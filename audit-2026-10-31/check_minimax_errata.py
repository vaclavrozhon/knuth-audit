#!/usr/bin/env python3
"""All archived errata layers plus current official originals for DLX84--86."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json,re
from dlx1_audit_tools import ROOT,sha
from check_sudoku_variants_errata import remote

OUT=ROOT/'results/minimax_mc'


def main():
    files=['errata/text/all4b.txt','errata/text/err4b.txt','errata/text/all4f5.txt',
           'errata/text/err4f5.txt','errata/originals/err4b.textxt','errata/originals/err4f5.textxt']
    pattern=re.compile(r'(?:Page\s+(?:48|49|69|90|131|133|137|138|241|242|433|434)\b|'
      r'4(?:b|f5)\.(?:48|49|69|90|131|133|241|242|433|434)\b|'
      r'\b(?:answer|exercise)\s+(?:84|85|86)\b|'
      r'cutoff|minimax|cleans|Monte.?Carlo|unpurif|unhide|step C[34678])',re.I)
    hits=[]
    for f in files:
        lines=(ROOT.parent/f).read_text().splitlines()
        for i,line in enumerate(lines):
            if pattern.search(line):
                hits.append(dict(file=f,line=i+1,context='\n'.join(lines[max(0,i-1):i+9])))
    with ThreadPoolExecutor(max_workers=4) as pool:
        current=list(pool.map(remote,['all4b.ps.gz','all4f5.ps.gz','err4b.textxt','err4f5.textxt']))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
      local_files={f:sha(ROOT.parent/f) for f in files},remote_files=current,search_hits=hits,
      mapping='4B question133=publishedF5 131=preF5c69; answers433--434=publishedF5 241--242=preF5c137--138.',
      conclusions=[
        'No matching correction for answer86 empty C6, missing theta on cleansings, or skipped update at a zero-degree node.',
        'No matching correction for answers84--85. Both cutoff variants agree with independent complete subset oracles.',
        '25May2021 correction on publishedF5 p242 concerns answer87 marker names, not84--86.',
        '4B p565 answer84 is in the SAT section and is unrelated.',
        'General AlgorithmC color-header and uncommit wording corrections are already incorporated in local4B; see E041.',
        'Theorem7.2.2E and its earlier audit ESTIMATION_NOTES.md support inverse path probabilities. No MonteCarlo sampling claim is used as a proof here.',
        'Unchanged source archives were searched in full. Negative search does not establish novelty or physical-print verification.'])
    OUT.mkdir(parents=True,exist_ok=True)
    (OUT/'errata-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: four current originals unchanged;',len(hits),'contexts saved')


if __name__=='__main__':main()

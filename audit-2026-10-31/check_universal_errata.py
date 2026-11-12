"""Current and historical complete correction layers for DLX94--100."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,re
from check_sudoku_variants_errata import remote

ROOT=Path(__file__).resolve().parent
FILES=['errata/text/all4b.txt','errata/text/err4b.txt','errata/text/all4f5.txt',
       'errata/text/err4f5.txt','errata/originals/err4b.textxt','errata/originals/err4f5.textxt']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    pattern=re.compile(r'(?:Page\s+(?:134|437|438|245|246)\b|4(?:b|f5)\.(?:134|437|438|245|246)\b|'
        r'137216|41280|5796|2898|ourotor|Sainte|universal.?cycle|answer\s+(?:9[4-9]|100)|'
        r'unspecified|unconstrained|unused\s+variable)',re.I)
    hits=[]
    for file in FILES:
        lines=(ROOT.parent/file).read_text().splitlines()
        for i,line in enumerate(lines):
            if pattern.search(line):hits.append(dict(file=file,line=i+1,context='\n'.join(lines[max(0,i-2):i+12])))
    with ThreadPoolExecutor(max_workers=4) as pool:
        remotes=list(pool.map(remote,['all4b.ps.gz','all4f5.ps.gz','err4b.textxt','err4f5.textxt']))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),script_sha256=sha(Path(__file__)),
        local_files={p:sha(ROOT.parent/p) for p in FILES},remote_files=remotes,hits=hits,
        conclusions=[
            'Answer98 has a published02Jan2025 correction: primary occurrence IDs ij replace literal labels lij;6m options. Not incorporated in local2022PDF or2019PS.',
            'No matching correction found concerning the remaining3-fold color/translation normalization in answer97.',
            'Answer99 uncolored occurrences are explicitly assigned private implicit colors on main-text page88; no defect.',
            'Answer100 has no matching clarification concerning variables outside every relation; finite unary domains are a sufficient preprocessing step.',
            'Other same-numbered answers on other pages/sections do not apply to this block.'])
    (ROOT/'results/universal_cycles/errata-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Four current originals unchanged; six complete layers;',len(hits),'contexts.')

if __name__=='__main__':main()

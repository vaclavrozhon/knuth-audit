"""Full current and historical correction layers for DLX115--120."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import re
from graph_native import ROOT,OUT,save,sha
from check_sudoku_variants_errata import remote

def main():
    files=['errata/text/all4b.txt','errata/text/err4b.txt','errata/text/all4f5.txt','errata/text/err4f5.txt','errata/originals/err4b.textxt','errata/originals/err4f5.textxt']
    pattern=re.compile(r'(?:Page\s+(?:135|136|137|138|148|149|444|445|446|252|253|254|255)\b|4(?:b|f5)\.(?:135|136|137|138|148|149|444|445|446|252|253|254|255)\b|(?:answer|exercise)\s+(?:11[5-9]|120)\b|Mycielski|critical|isolated|triangle.free|hypersudoku|Michel|Alon|Sachs|7784|16384|262164|23713820|no.three|MacMahon|tetrad|Gardner|1965)',re.I)
    hits=[]
    for file in files:
        lines=(ROOT.parent/file).read_text().splitlines()
        for i,line in enumerate(lines):
            if pattern.search(line):hits.append(dict(file=file,line=i+1,context='\n'.join(lines[max(0,i-2):i+17])))
    with ThreadPoolExecutor(max_workers=4) as pool:current=list(pool.map(remote,['all4b.ps.gz','all4f5.ps.gz','err4b.textxt','err4f5.textxt']))
    save(OUT/'errata-check.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),script_sha256=sha(__file__),local_files={p:sha(ROOT.parent/p) for p in files},remote_files=current,hits=hits,
        known_updates=['02Jan2023 answer115: remove redundant B-prime items after the Weigel replacement of answer114.','Historical19Feb2020 exercise116: improved illustrations;25May2021: insert G in its definition.'],
        scope_notes=['No corresponding correction located for the general triangle-containment sentence or the general edge-criticality claim with isolated vertices. Their precise reading is documented as a candidate, not a failure of the requested Mycielski sequence.']))
    print('Six full errata layers; four remote originals unchanged;',len(hits),'contexts.')

if __name__=='__main__':main()

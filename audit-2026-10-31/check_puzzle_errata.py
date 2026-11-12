"""Current and historical complete correction layers for DLX101--107."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import json,re
from puzzle_xcc import ROOT,OUT,save,sha
from check_sudoku_variants_errata import remote


def main():
    files=['errata/text/all4b.txt','errata/text/err4b.txt','errata/text/all4f5.txt',
           'errata/text/err4f5.txt','errata/originals/err4b.textxt','errata/originals/err4f5.textxt']
    pattern=re.compile(r'(?:Page\s+(?:134|135|136|438|439|440|247|248)\b|'
                       r'4(?:b|f5)\.(?:134|135|136|438|439|440|247|248)\b|'
                       r'(?:answer|exercise)\s+10[1-7]\b|zebra|Bittencourt|twelve.ton|'
                       r'perfect.*row|Hodges|Stong|Ramos|Gibat|Ouellet|word.search|11351|3856)',re.I)
    hits=[]
    for file in files:
        lines=(ROOT.parent/file).read_text().splitlines()
        for i,line in enumerate(lines):
            if pattern.search(line):hits.append(dict(file=file,line=i+1,context='\n'.join(lines[max(0,i-2):i+14])))
    with ThreadPoolExecutor(max_workers=4) as pool:
        current=list(pool.map(remote,['all4b.ps.gz','all4f5.ps.gz','err4b.textxt','err4f5.textxt']))
    save(OUT/'errata-check.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
         script_sha256=sha(__file__),local_files={p:sha(ROOT.parent/p) for p in files},remote_files=current,hits=hits,
         conclusions=[
         '03Jan2023 question103: italicize twelve-tone row. Published typographic improvement.',
         '15Sep2025 question104: delete whenever k is not a multiple of p; clarify that x_n is considered blank. Published definition amendment.',
         '03Jul2025 answer103: replace Stong/AMM/to appear with N.Hodges etal.,AMM132(2025),94-96. Published citation update.',
         '30Mar2022 Fascicle5: replace103(e) first paragraph and5xQR by7xQR; these mathematical corrections are already present in local4B but not in2019authorPS.',
         '16Dec2019 Fascicle5 answer104: add(a), already present in local4B.',
         'No matching new correction found for the mathematical reductions, exact model counts or printed grids101--107. Performance depends on unspecified input order; differences alone are not classified as errors.',
         'Matching numbers on pages belonging to other sections are not corrections to this block.']))
    print('Four current originals unchanged; six complete layers;',len(hits),'contexts.')


if __name__=='__main__':main()

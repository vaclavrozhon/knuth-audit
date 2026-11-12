"""Complete correction layers for DLX108--114, including shifted fascicle pages."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
import re
from layout_native import ROOT,OUT,save,sha
from check_sudoku_variants_errata import remote


def main():
    files=['errata/text/all4b.txt','errata/text/err4b.txt','errata/text/all4f5.txt',
           'errata/text/err4f5.txt','errata/originals/err4b.textxt','errata/originals/err4f5.textxt']
    pattern=re.compile(r'(?:Page\s+(?:136|137|440|441|442|443|444|248|249|250|251|252)\b|'
        r'4(?:b|f5)\.(?:136|137|440|441|442|443|444|248|249|250|251|252)\b|'
        r'(?:answer|exercise)\s+(?:10[89]|11[0-4])\b|H00|H20|V30|wordcross|word.cross|'
        r'presiden|McDonald|Gordon|Torto|Rieksti|Castawords|18486|403357|30258432|'
        r'blank.regions|minimum.rectangle|smallest.rectangle|transposition)',re.I)
    hits=[]
    for file in files:
        lines=(ROOT.parent/file).read_text().splitlines()
        for i,line in enumerate(lines):
            if pattern.search(line):hits.append(dict(file=file,line=i+1,context='\n'.join(lines[max(0,i-2):i+17])))
    with ThreadPoolExecutor(max_workers=4) as pool:
        current=list(pool.map(remote,['all4b.ps.gz','all4f5.ps.gz','err4b.textxt','err4f5.textxt']))
    save(OUT/'errata-check.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
        script_sha256=sha(__file__),local_files={p:sha(ROOT.parent/p) for p in files},remote_files=current,hits=hits,
        known_updates=[
            '30Mar2023 question111: add explanation of black/white crossword diagrams and reference1.3.2–23.',
            '19Dec2022 answer109: found in20G becomes23G. Local PDF/authorPS actually have29G; current benchmark matches23G.',
            '04Nov2023 answer111(a):591G becomes550G.',
            '08Apr2023 answer112(c):140 becomes416; rightmost first rowETV becomesYTE.',
            '07Jan2023 answer113:225G becomes202G; blockCETRUY becomesCEIRUY.',
            '02Jan2023 answer114: Weigel replacement removes redundant permuted-grid primary items and propagates normalized first row;30,258,432 in171G.',
            'Historical25May2021 quotation marks in109 and16Sep2021 Windsor empty-cell bound already present in local4B.'
        ],
        absent_matches=[
            'No matching correction located for the zero-based H00,H20,V30 labels in the one-based109 construction.',
            'No matching correction or explicit exclusion of one-row rectangles located for the5x11 minimum-area claim under(i),(ii).'
        ]))
    print('Errata:6 full layers,4 current originals,',len(hits),'contexts.')


if __name__=='__main__':main()

"""Source/errata scope for147 and the exact printed F138 histogram entries."""
from datetime import datetime,timezone
from pathlib import Path
import json,re
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/bricks147'
SRC=ROOT/'sources/bricks147'


def main():
    previous=json.loads((ROOT/'results/polygons143/errata-check.json').read_text())
    pattern=r'(?:[Pp]age\s+|(?:4b|4f5)\.)(?:143|456|457|458|141|264|265|266)\b|(?:answer|exercise|exer ise)\s+147\b|11\s*,\s*14\s*,\s*2|Mac.?Mahon|Kowalewski|Winter|8275|Mayblox'
    contexts=[]
    for name,digest in previous['files'].items():
        path=ROOT.parent/name;assert sha(path)==digest
        lines=path.read_text(errors='replace').splitlines()
        for i,line in enumerate(lines):
            if re.search(pattern,line,re.I):contexts.append(dict(file=name,line=i+1,context='\n'.join(lines[max(0,i-1):i+5])))
    tex=(ROOT.parent/'errata/originals/err4b.textxt').read_text()
    corrections=[]
    for id,date,label,old,new in [('E074','2026-04-07','4b.457 line 22 (26.04.07)','(1893)','(1892)'),
                                 ('E075','2023-06-19','4b.457 line 22 (23.06.19)','8-cube','eight-cube')]:
        block=next(b.strip() for b in tex.split('\\endchange') if label in b)
        assert old in block and new in block
        corrections.append(dict(id=id,date=date,context=block,status_in_local_book='not incorporated',status_in_draft2019='not incorporated'))
    segments={}
    for name in ['page457.txt','draft161.txt']:
        text=re.sub(r'\s+',' ',(SRC/name).read_text())
        segment=text.split('Case 2 × 2 × 4:')[1].split('Case 2 × 2 × 5:')[0]
        for phrase in ['(0, 0, 1, 0)','(0, 3, 4, 2)','(0, 11, 14, 2)','(0, 2, 2, 3)','(0, 1, 1, 1)']:assert phrase in segment,phrase
        assert '(1893)' in text and '8-cube' in text
        segments[name]=segment
    assert segments['page457.txt']==segments['draft161.txt']
    save(OUT/'errata-check.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),
        files=previous['files'],pattern=pattern,contexts=contexts,relevant_corrections=corrections,
        latest_remote_retrieval='2026-11-03T05:37:34Z; six hashes reused unchanged from143',
        conclusion='No correction to the2x2x4 histograms found in these layers. E074/E075 concern citation year and spelling only.',
        mapping=dict(question4B=143,answer4B=[456,457,458],questionDraft=79,answerDraft=[160,161,162],answerFascicle5=[264,265,266])))
    history=dict(recorded_at_utc=datetime.now(timezone.utc).isoformat(),
        queries=['MacMahon Jocelyn1892 8275 coloured cubes patent','"On the Thirty Cubes" "1892" MacMahon',
            '"GB189208275"','"Mac Mahons Problem" Winter1933 pdf','"Alte und neue mathematische Spiele"1930 pdf Kowalewski',
            '"On the thirty cubes" pdf MacMahon145','"8275" "MacMahon" "patent"'],
        primary_metadata=[
            dict(url='https://doi.org/10.1112/plms/s1-24.1.145',result='Publisher records nominal volume year1892. Metadata gives145–156 and received21March1893; historical volume index lists145–155, so no new end-page error inferred. DOI open returned403; article body not obtained.'),
            dict(url='https://ndlsearch.ndl.go.jp/books/R100000002-I000006498029',result='National Diet Library catalog: Kowalewski,Alte und neue mathematische Spiele,Teubner,1930,145pages. Does not prove the specific pages14–19 construction.'),
            dict(url='https://ci.nii.ac.jp/ncid/BB17224590',result='CiNii university-library catalog: FerdinandWinter,Mac Mahons Problem,Teubner1933,122pages,doctoral thesis. Does not prove the construction on67–87.')],
        unavailable_originals=['https://patents.google.com/patent/GB189208275A/en'],
        reused_local_sources=['sources/cubes146/sciam1978-09-pdf28.txt','sources/triangles124_126/garcia-macmahon-thesis.txt'],
        supporting_scope='Gardner1978 and Garcia collection description corroborate the Mayblox product name. Historical patent body, original1892/93 article, Kowalewski1930 and Winter1933 construction pages remain open. Secondary literature used only as leads for unavailable originals.',
        no_worldwide_novelty_claim=True)
    save(SRC/'history-search.json',history)
    files=[p for p in SRC.iterdir() if p.is_file()]
    files += [ROOT/'images'/n for n in ['vol4b-p143-cubes146.png','vol4b-p456-cubes146.png',
        'bricks147-original-477.png','bricks147-original-478.png','fasc5c-p160-cubes146.png','bricks147-draft-167.png','bricks147-draft-168.png']]
    save(OUT/'sources-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),
        source_hashes={str(p.relative_to(ROOT)):sha(p) for p in files},printed_2x2x4_segments=segments,
        same_four_histogram_discrepancies_in_original_and_author_draft=True,original457_and_draft161_visually_inspected=True,
        pending_history=['UK8275of1892 patent body','Original MacMahon article body and precise discovery attribution',
            'Kowalewski1930 pages14–19 construction','Winter1933 pages67–87 construction'],
        physical_copy_and_latest_complete_digital_release_unverified=True))
    print('PASS147 sources: original/draft table identical; six errata layers; knownE074/E075 only; four historical-source gaps explicit.')


if __name__=='__main__':main()

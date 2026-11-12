"""Pin six errata layers, the original figures, and the limits of historical sources."""
from datetime import datetime, timezone
from pathlib import Path
from bs4 import BeautifulSoup
import json
import re
import nuts137 as n


def main():
    previous = json.loads((n.ROOT / 'results/borders127_128/errata-check.json').read_text())
    fresh = json.loads((n.OUT / 'errata-remote-check.json').read_text())
    assert len(fresh['files']) == 4 and all(x['unchanged'] for x in fresh['files'])
    for entry in fresh['files']:
        assert n.sha(n.ROOT.parent / 'errata/originals' / entry['file']) == entry['sha256']
    patterns = [r'(?:Page|page)\s+(?:140|452|138|260|76|156)\b',
                r'(?:4b|4f5)\.(?:140|452|138|260)\b',
                r'(?:answer|exercise)\s+137\b',
                r'Drive.?Ya.?Nuts|hex nuts|Super.?Dom|Hydes|Whitehouse|Haswell|93\\?%|0[.]4\\?%']
    contexts = []
    for path, digest in previous['local_files'].items():
        p = n.ROOT.parent / path
        assert n.sha(p) == digest
        lines = p.read_text().splitlines()
        for i, line in enumerate(lines):
            if any(re.search(pattern, line, re.I) for pattern in patterns):
                contexts.append(dict(file=path, line=i+1, matched_line=line,
                                     context='\n'.join(lines[max(0,i-2):i+13])))
    assert len(contexts) == 6
    assert all(('121' in x['matched_line'] or '138' in x['matched_line']) for x in contexts)
    n.save(n.OUT / 'errata-contexts.json', contexts)
    n.save(n.OUT / 'errata-check.json', dict(
        checked_at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=n.sha(__file__),
        local_files=previous['local_files'], remote_verified_at_utc=fresh['checked_at_utc'],
        remote_files=fresh['files'], search_patterns=patterns,
        contexts_sha256=n.sha(n.OUT / 'errata-contexts.json'),
        page_mapping=dict(question4B=140, answer4B=452, questionF5=138,
                          answerF5=260, questionDraft5C=76, answerDraft5C=156),
        correction137_found=False,
        conclusion='All six contexts concern other exercises:121 on4B p138 or138 onF5 p260. '
                   'No published correction found for137 or its probability distribution.'))
    source_dir = n.ROOT / 'sources/nuts137'
    retrievals = []
    for name in ['retrieval.json', 'retrieval-followup.json']:
        for rec in json.loads((source_dir / name).read_text()):
            if rec.get('status') == 200:
                path = rec.get('file') or rec.get('path')
                assert path and n.sha(n.ROOT / path) == rec['sha256'], rec
            retrievals.append(rec)
    patents = []
    for stem, date, required in [
        ('gb149473', '1920-08-19', ['Hydes, H.', 'nineteen', 'is seven']),
        ('gb173588', '1921-12-29', ['Hydes, H., and Whitehouse, F. R. B.', 'nineteen', 'same colour']),
    ]:
        soup = BeautifulSoup((source_dir / (stem + '.html')).read_text(), 'html.parser')
        dates = [m.get('content') for m in soup.find_all('meta', attrs={'name':'DC.date'})]
        abstract = soup.select_one('[itemprop="abstract"]').get_text(' ', strip=True)
        assert date in dates and all(s in abstract for s in required)
        patents.append(dict(patent=stem, publication_date=date, abstract_checked=True,
                            original_full_specification_obtained=False))
    us = (source_dir / 'us1558165.txt').read_text()
    assert '1925' in us and 'HASWELL' in us and 'nineteen' in us
    assert '1 with' in us and '6, 2 with 5, and 3 with 4, to add 7.' in us
    # Independent manual transcription from the manufacturer image, CCW from north.
    manufacturer = ['135426', '264153', '561234', '246135', '432165', '125634', '356142']
    book = json.loads((n.OUT / 'book-cases-checked.json').read_text())
    n.validate(manufacturer, book['cases'][0]['nuts'], 'equal')
    assert '/'.join(n.normalize(manufacturer)) in book['cases'][0]['models']
    paper_clockwise = ['162453','146235','165324','143652','123456','164253','165432']
    rob_clockwise = ['165432','143652','164253','162453','165324','146235','123456']
    for words in [paper_clockwise, rob_clockwise]:
        assert sorted(n.canonical(w[::-1]) for w in words) == book['cases'][0]['nuts']
    draft = (source_dir / 'fasc5c-answer137.txt').read_text()
    for phrase in ['Thousands of random trials', 'remaining 1%', 'About 0.4%']:
        assert phrase in draft
    files = [str(p.relative_to(n.ROOT)) for p in sorted(source_dir.iterdir()) if p.is_file()]
    files += ['images/vol4b-p140.png', 'images/vol4b-p452.png',
              'images/hasbro-solution-1.png', 'images/us1558165-2.png',
              'images/fasc5c-p156-nuts137.png']
    n.save(n.OUT / 'source-status.json', dict(
        at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=n.sha(__file__),
        files={p:n.sha(n.ROOT/p) for p in files}, patents=patents,
        us1558165=dict(original_pdf_obtained=True, page2_visually_read=True,
                       inventor='George Henry Haswell', date='1925-10-20',
                       supported=['7,19,37 hexagon layouts', 'six distinct side labels',
                                  'equality and complementary sum7 matching']),
        manufacturer=dict(url='https://www.hasbro.com/common/instruct/DriveYaNuts.PDF',
                          copyright_year_visually_read=1987, digits_manually_transcribed=42,
                          words=manufacturer, equals_unique_book_solution=True),
        original_research=dict(
            paper='Marshall Zarecky and Adam Parker: Describing a Combinatorics Problem with a System of Polynomial Equations',
            paper_url='https://www.wittenberg.edu/sites/default/files/media/computer_science/forms/sumInSMC.pdf',
            paper_scope='Seven printed clockwise types match the book after reversing the direction convention; no independent audit of every polynomial in this paper.',
            rob_url='https://robspuzzlepage.com/pattern.htm',
            rob_scope='Original author describes a hand table-elimination proof and the same seven nuts. Our separately generated certificate replays every deletion geometrically.'),
        draft2019=dict(file='sources/fasc5c.pdf', sha256=n.sha(n.ROOT/'sources/fasc5c.pdf'),
                       printed_page=156, same_probability_wording=True),
        historical_limits=[
            'Exact1970 introduction and forgotten inventor: repeated in secondary accounts, but original1970 catalog/record not yet obtained; manufacturer sheet is1987.',
            'British patent abstracts corroborate authors, dates,19-piece sets and the two matching rules; full original specifications unavailable through the tried route.',
            'The name Super Dom is absent from the obtained primary patent material.',
            'The precise15-node hand-search convention is not reconstructed; a different elementary deletion certificate establishes hand-solvability.'],
        inaccessible_routes='ToyTales403, Espacenet403, USPTO API401 are recorded; no protected access was bypassed.'))
    print('PASS137: six errata layers; manufacturer42 digits; patent metadata and US original; historical limits retained.')


if __name__ == '__main__':
    main()

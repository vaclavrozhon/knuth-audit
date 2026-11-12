"""Content checks and explicit limits for the primary historical sources."""
from datetime import datetime,timezone
import html,json,re
from layout_native import ROOT,save,sha
from check_layout_figures import PRESIDENTS


def main():
    directory=ROOT/'sources/layouts108_114'
    source=directory/'presidents-obama-archive.html'
    found=[html.unescape(re.sub('<[^>]+>','',label)).strip()
           for url,label in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',source.read_text(),re.S)
           if '1600/presidents/' in url]
    assert [int(n.split('.')[0]) for n in found]==list(range(1,45))
    surnames=['VANBUREN' if n.endswith('Van Buren') else n.split()[-1].upper() for n in found]
    assert len(set(surnames))==38 and set(surnames)==set(PRESIDENTS)
    torto=directory/'ricbit-torto.pro';text=torto.read_text()
    assert '% Ricardo Bittencourt 2011' in text
    assert 'wordlist(Grid, [Word | WordList])' in text and 'validBlock' in text
    # The code itself verifies the described grid-construction idea. It does
    # not verify the magazine/trademark history or the blog publication date.
    metadata={p.name:json.loads(p.read_text()) for p in directory.glob('*.source.json')}
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),script_sha256=sha(__file__),
        presidents=dict(source_sha256=sha(source),numbered_entries=44,distinct_surnames=38,
                        exact_book_set_equal=True,entries=found),
        torto=dict(source_sha256=sha(torto),author_year_comment='Ricardo Bittencourt 2011',
            content_review='Prolog constructs a6x3 grid from requested words using king steps, visited-cell exclusion and diagonal-midpoint exclusion.',
            unverified=['Coquetel trademark1977','Total issue1 in1977','current magazine frequency','original blog date']),
        source_metadata=metadata,
        queries=['"Word-Search Packing" Eckler Gordon1994','"presidential" "19x19" wordcross',
                 '"Torto reverso" ricbit','TAOCP exercise108 presidential word search minimum15x15 5x43',
                 'McDonald presidential wordcross20x20 2017'],
        current_optimum_search='No primary source proving a better optimum for108 or110 was located in these limited searches; this is not an exhaustive absence claim.',
        unresolved=['Full Word Ways1994 pages63,147,252 unavailable; landing-page metadata/abstracts only.',
                    'McDonald2017 attribution not independently verified from a dated original.',
                    '113 Chapter2 word-frequency aside: OCR/edition and token-boundary semantics unresolved.'])
    save(directory/'history-check.json',result)
    print('44 official presidential entries -> exact38 surnames; Bittencourt2011 source reviewed; access/history limits recorded.')


if __name__=='__main__':main()

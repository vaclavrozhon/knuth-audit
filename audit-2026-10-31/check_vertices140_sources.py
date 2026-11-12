"""Pin primary historical evidence and distinguish metadata from unavailable text."""
from datetime import datetime,timezone
from pathlib import Path
from bs4 import BeautifulSoup
import json,re,subprocess
import xml.etree.ElementTree as ET
import vertices140 as h


def main():
    src=h.ROOT/'sources/vertices140'
    ns={'m':'info:lc/xmlns/marcxchange-v2','s':'http://www.loc.gov/zing/srw/'}
    bnf=ET.parse(src/'bnf-title.xml').getroot()
    assert bnf.find('s:numberOfRecords',ns).text=='1'
    record=bnf.find('.//m:record',ns)
    def field(tag,code):return record.find(f'm:datafield[@tag="{tag}"]/m:subfield[@code="{code}"]',ns).text
    assert record.get('id')=='ark:/12148/cb346060085'
    assert field('200','a')=='Surprenants triangles'
    assert field('200','f')=='M. Odier, Y. Roussel'
    assert field('210','d')=='1976' and field('210','c')=='CEDIC'
    assert field('010','a')=='2-7124-0601-X'
    text={}
    for name,path,page in [('book',h.ROOT.parent/'books/taocp-vol4b-ed1-print2-2022.pdf',474),
                           ('draft',h.ROOT/'sources/fasc5c.pdf',164)]:
        text[name]=subprocess.check_output(['pdftotext','-f',str(page),'-l',str(page),'-layout',str(path),'-'],text=True)
        assert re.search(r'Surprenant\s+Triangles',text[name])
        assert not re.search(r'Surprenants\s+Triangles',text[name])
    patent=(src/'us3608906.txt').read_text()
    assert 'Patented Sept. 28, 1971' in patent and re.search(r'1,?582,023',patent)
    fr=BeautifulSoup((src/'fr1582023.html').read_bytes(),'html.parser').get_text(' ',strip=True)
    assert '1968-01-08' in fr and '1969-09-26' in fr
    # Keep the original request record intact, including its misleading extension.
    retrieval=json.loads((src/'retrieval-history2.json').read_text())
    langford=next(r for r in retrieval if r['file'].endswith('langford1959.pdf'))
    assert langford['is_pdf'] is False and langford['content_type'].startswith('text/html')
    article=BeautifulSoup((src/'langford-cambridge.html').read_bytes(),'html.parser').get_text(' ',strip=True)
    for phrase in ['C. Dudley Langford','May 1959','120 - 122','10.2307/3610194']:
        assert phrase in article,phrase
    gaps=[
        'The original Langford1959 article (Gazette43,120–122) is identified, but its full text remains unavailable locally. The PDF link redirected to an access page; the public preview returned403. The attribution has not been checked against the article content.',
        'The original French patent1582023 text was not obtained. Its1968 filing/1969 publication dates come from the patent index; the retrieved original US patent explicitly attributes the earlier vertex-matching construction to that French patent. The parenthetical1968 is compatible with filing and is not classified as an error.'
    ]
    h.save(h.OUT/'source-status.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=h.sha(__file__),
        files={str(p.relative_to(h.ROOT)):h.sha(p) for p in sorted(src.iterdir()) if p.is_file()},
        bnf=dict(record='https://catalogue.bnf.fr/ark:/12148/cb346060085',title=field('200','a'),authors=field('200','f'),
                 publisher=field('210','c'),year=field('210','d'),isbn=field('010','a')),
        title_typo=dict(printed='Surprenant Triangles',correct='Surprenants triangles',book_and_author_draft=True,
                        original_rulebook_pdf_page3_also_spells_plural=True),
        patent=dict(us='3608906',inventor='Marc Odier',patented='1971-09-28',original_pdf_pages_viewed=[1,5],
                    cites_french_patent='1582023',french_filing_metadata='1968-01-08',french_publication_metadata='1969-09-26'),
        original_rules=dict(pdf='sources/vertices140/trioker-rules.pdf',pdf_pages_viewed=[2,3],
                            corner_matching_rule_verified=True,trioker_name_verified=True,copyright_margin='1968 Odier; Robert Laffont'),
        multimatch=dict(url='https://www.gamepuzzles.com/edgemtch.htm',observed_via='web tool, November2 2026',
                        statement='Manufacturer lists Multimatch IV as24 corner-colored triangular pieces covering all combinations of four colors.',
                        raw_archive_available=False,raw_http_request_status=403),
        langford_metadata=dict(author='C. Dudley Langford',title='2829. Dominoes numbered in the corners',journal='The Mathematical Gazette43(344),May1959,120–122',doi='10.2307/3610194'),
        historical_gaps=gaps,physical_taocp_print_verified=False))
    print('PASS: F135 title in BnF versus original PDF/PS; US patent and rules checked; two historical gaps retained.')


if __name__=='__main__':main()

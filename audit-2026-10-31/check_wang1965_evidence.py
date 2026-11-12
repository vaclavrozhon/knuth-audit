"""Primary citation, original PS types and the incorporated illustration erratum."""
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
import json,xml.etree.ElementTree as ET
from PIL import Image
import extract_tetrads120 as ex
from graph_native import ROOT,sha,save

OUT=ROOT/'results/graphs117_120';SOURCE=ROOT/'sources/graphs117_120'

def main():
    data=json.loads((OUT/'tetrads120-vectors.json').read_text())
    ex.PALETTE['.199951 .199951 .199951']='K'
    ps=ex.tiles(ET.parse(OUT/'fasc5c-p74-trace.xml'))
    assert [t['colors'] for t in ps]==sum(data['families'],[])
    comparison=json.loads((OUT/'tetrads120-illustration-comparison.json').read_text())
    changes=comparison['different_tiles'];assert len(changes)==156 and all(x['row']<6 for x in changes)
    corrected=ex.tiles(ET.parse(OUT/'errata4f5-p14-trace.xml'))
    assert len(corrected)==336 and [t['colors'] for t in corrected]==sum(comparison['main_boards'][:6],[])
    crossref=json.loads((SOURCE/'wang1965-crossref.json').read_text())['message']
    assert crossref['title']==['Games, Logic and Computers']
    assert (crossref['volume'],crossref['issue'],crossref['published']['date-parts'])==('213','5',[[1965,11]])
    html=(SOURCE/'scientific-american-1965-11.html').read_text()
    assert 'Volume 213' in html and '1965' in html
    # Read all72 tiles in the original source's two6x6 blocks. Four interior
    # samples per cell; nine shifted samples must all give the same discrete color.
    im=Image.open(ROOT/'images/wang1965-p106.png');assert im.size==(1035,1500)
    palette={'O':(226,61,15),'P':(219,130,120),'G':(145,146,147),'K':(40,37,37)}
    relabel={'P':'W','K':'R','O':'B','G':'K'};rows=[];samples=[]
    for r in range(12):
        row=[]
        for c in range(6):
            colors=[]
            for dx,dy in [(.5,.2),(.8,.5),(.5,.8),(.2,.5)]:
                x=round(64+(c+dx)*98.3);y=round(52+(r+dy)*97.3);labels=set()
                for xx in (-1,0,1):
                    for yy in (-1,0,1):
                        rgb=im.getpixel((x+xx,y+yy))[:3]
                        labels.add(min(palette,key=lambda k:sum((a-b)**2 for a,b in zip(rgb,palette[k]))))
                assert len(labels)==1;label=labels.pop();colors.append(relabel[label]);samples.append([x,y,label])
            tile=''.join(colors);assert tile in data['families'][0];row.append(tile)
        rows.append(row)
    for r in range(12):
        for c in range(6):
            if r:assert rows[r-1][c][2]==rows[r][c][0]
            if c:assert rows[r][c-1][1]==rows[r][c][3]
    save(OUT/'wang1965-history-checked.json',dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),script_sha256=sha(__file__),
        ps80_type_wedges_match=True,ps_source_sha256=sha(ROOT/'sources/fasc5c.pdf'),
        incorporated_erratum=dict(id='E060',date='2021-10-15',published_page=253,part='120(a)',
            changed_old_PS_tiles=156,corrected336_tiles_equal=True,family_b_unchanged=True,trace_sha256=sha(OUT/'errata4f5-p14-trace.xml')),
        citation=dict(title=crossref['title'][0],volume=213,issue=5,year=1965,month=11,doi=crossref['DOI'],
            crossref_sha256=sha(SOURCE/'wang1965-crossref.json'),publisher_html_sha256=sha(SOURCE/'scientific-american-1965-11.html')),
        original_article=dict(pdf_sha256=sha(SOURCE/'wang-1965.pdf'),viewed_printed_pages=[103,106],
            page103_visual_observation='The ten pictured source types agree with family a after the recorded global palette relabeling.',
            page106_image_sha256=sha(ROOT/'images/wang1965-p106.png'),source_palette_relabel=relabel,
            all72_illustrated_tiles=rows,checked_color_samples=len(samples)*9,samples=samples),
        limitations='The source article is checked only where cited by120. Its other mathematical claims are not audited. The231/213 error is supported independently by the publisher issue page and deposited article metadata.'))
    print('History: publisher213(5), original source103/106, all80 PS type wedges, known corrected336-cell illustration; b unchanged.')

if __name__=='__main__':main()

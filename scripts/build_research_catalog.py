#!/usr/bin/env python3
"""Build the research index and CSV from the reviewed JSON; no book files needed."""
import argparse
from collections import Counter
import csv
import io
import json
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research'
KINDS={'exercise':'Exercise','answer_question':'Question in an answer',
       'text_question':'Question in the main text','replacement_exercise':'Replacement exercise',
       'exercise_note':'Research question in an exercise note'}

def anchor(row):
    return re.sub('[^a-z0-9-]','-',row['id'].lower())

def cell(value):
    return str(value).replace('|','\\|').replace('\n',' ')

def location(row):
    text=f"§{row['section']}"
    if row['exercise'] is not None:
        text+=f", {'answer' if row['kind']=='answer_question' else 'exercise'} {row['exercise']}"
    return text+f", printed p. {row['printed_page']}"

def rating(row):
    a,b=row['original_rating'],row['official_rating']
    if a is None: return f'Replacement [{b}]' if b else 'Unrated passage'
    return f'[{a}]' if a==b else f'[{a}] → [{b}]'

def sort_key(row):
    p=row['printed_page']
    return (int(p) if p.isdigit() else -1,row['section'],row['exercise'] or 0,row['id'])

def load():
    data=json.loads((OUT/'catalog.json').read_text())
    searches=json.loads((OUT/'search-log.json').read_text())['batches']
    reviews=json.loads((OUT/'coverage-review.json').read_text())['records']
    ids=[r['id'] for r in data['items']]
    assert len(ids)==len(set(ids)), 'Duplicate catalogue IDs'
    batches={b['id'] for b in searches}
    volumes={v['id'] for v in data['volumes']}
    for r in data['items']:
        assert r['volume'] in volumes and r['kind'] in KINDS, r['id']
        assert r['status'] in data['status_definitions'], r['id']
        assert all(r[k] for k in ('title','question','section','printed_page','status_note','search_batches')),r['id']
        assert set(r['search_batches'])<=batches, r['id']
        if r['kind']=='exercise':
            ratings=[r['original_rating'],r['official_rating']]+[u['rating'] for u in r['official_updates']]
            assert any(t and 46<=int(re.search(r'\d+',t)[0])<=50 for t in ratings),r['id']
        if r['status'] in ('solved','reported_solution','partial','open_in_source'):
            assert r['sources'] or r['official_updates'], r['id']
        for s in r['sources']+r['official_updates']:
            assert urlparse(s['url']).scheme in ('https','http'), (r['id'],s)
    assert len({(r['pass_name'],r['key']) for r in reviews})==len(reviews)
    for r in reviews:
        assert set(r['catalog_ids'])<=set(ids)
        assert bool(r['catalog_ids'])==(r['decision']=='included')
    for name,n in data['methodology']['language_passes'].items():
        assert sum(r['pass_name']==name for r in reviews)==n
    return data,searches

def volume_document(data,volume):
    rows=sorted([r for r in data['items'] if r['volume']==volume['id']],key=sort_key)
    statuses=data['status_definitions']
    text=[f"# {volume['label']}: {volume['title']}",'',
          f"{volume['edition']}. Literature review as of **{data['as_of']}**.",'',
          f"{len(rows)} entries. [Index and status meanings](README.md) · [Terms and notation](GLOSSARY.md).",'',
          'Page numbers refer to the supplied edition. These short paraphrases locate questions; consult the book for complete hypotheses and algorithm definitions.', '',
          '| Location | Research question | Book rating | Literature assessment |',
          '| --- | --- | --- | --- |']
    for r in rows:
        text.append(f"| {cell(location(r))} | [{cell(r['title'])}](#{anchor(r)}) | {rating(r)} | {statuses[r['status']]['label']} |")
    for r in rows:
        text+=['',f"<a id=\"{anchor(r)}\"></a>",'',f"## {r['title']}",'',
               f"**{location(r)}** · {KINDS[r['kind']]} · {rating(r)} · `{r['id']}`",'',r['question'],'',
               f"**{statuses[r['status']]['label']}.** {r['status_note']}"]
        if r['sources']:
            links=[]
            for s in r['sources']:
                year=f" ({s['year']})" if s.get('year') else ''
                links.append(f"[{s['title']}{year}]({s['url']})")
            text+=['','Evidence: '+'; '.join(links)+'.']
        for s in r['official_updates']:
            text+=['',f"Book amendment, {s['date']}: {s['note']} [Official record]({s['url']})."]
        if r.get('current_research_locator'):
            text+=['',f"Current research locator: {r['current_research_locator']}."]
        if r.get('additional_locations'):
            text+=['','Also discussed at: '+'; '.join(r['additional_locations'])+'.']
        if r.get('related_findings'):
            text+=['','Related audit note: '+', '.join(f'[{i}](../findings/{i}.md)' for i in r['related_findings'])+'.']
        if r.get('prior_review'):
            text+=['',f"[Earlier source review](../{r['prior_review']})."]
        text+=['','[Recorded searches](SEARCHES.md): '+', '.join(f"[S{n:02d}](SEARCHES.md#s{n:02d})" for n in r['search_batches'])+'.']
    return '\n'.join(text).rstrip()+'\n'

def index_document(data,searches):
    rows=data['items'];counts=Counter(r['status'] for r in rows)
    qcount=sum(len(b['queries']) for b in searches)
    exercises=sum(r['kind']=='exercise' for r in rows)
    replacements=sum(r['kind']=='replacement_exercise' for r in rows)
    other=len(rows)-exercises-replacements
    text=['# Research questions in TAOCP','',
          f"**{len(rows)} entries from seven supplied publications** of Donald Knuth’s *The Art of Computer Programming* (TAOCP), with a literature review as of **{data['as_of']}**. This is a separate research catalogue; entries are not error-finding cards.",'',
          f'It includes all {exercises} exercises identified with original or amended ratings of 46–50, {replacements} replacement questions, and {other} additional questions or research notes from the main text and answers. Questions later resolved are retained. Closely related subquestions can share an entry, so the count is not a count of independent conjectures.','',
          f'**The catalogue is not a list of {len(rows)} problems known to be open today.** In particular, “Resolution not located” means the present search did not verify a solution. It must not be cited as evidence of openness. Recent reported resolutions are distinguished from established results.','',
          '[Spreadsheet CSV](catalog.csv) · [Structured JSON](catalog.json) · [Search record](SEARCHES.md) · [Terms and notation](GLOSSARY.md)','',
          '## Browse by publication','',
          '| Publication | Supplied edition | Entries |',
          '| --- | --- | ---: |']
    for v in data['volumes']:
        text.append(f"| [{v['label']}: {v['title']}]({v['id']}.md) | {v['edition']} | {sum(r['volume']==v['id'] for r in rows)} |")
    text+=['','## Reading the assessments','','| Assessment | Entries | Meaning |','| --- | ---: | --- |']
    for k,v in data['status_definitions'].items():
        text.append(f"| {v['label']} | {counts[k]} | {v['meaning']} |")
    text+=['','## Scope and method','',
           'The scope is TAOCP volumes 1, 2, 3, 4A and 4B, the MMIX fascicle, and Fascicle 7, in the editions above. Other books by Knuth and unavailable future volumes are outside this inventory.','',
           'Knuth’s number is an exercise difficulty/research rating. The modern guide treats ratings 46 and above as research problems; [50] alone is too narrow. M marks a mathematical exercise and HM marks one involving higher mathematics. A lower amended rating is preserved alongside the original; it does not erase the historical research question. An ungraded note inherits no invented rating.','',
           'The scan screened exercise-like OCR records, checked 606 potentially high or ambiguous ratings against original page crops (including a second pass through ratings 40–45), and reviewed 403 language hits across three overlapping passes. Each included question was read with its surrounding text or answer. The screening decisions are in [rating-review.json](rating-review.json) and [coverage-review.json](coverage-review.json); private images and book OCR are omitted.','',
           f"The literature pass contains {len(searches)} search batches and {qcount} recorded query strings. It uses book locators, named conjectures, authors, and terminology; result pages were followed to relevant primary sources. Current and historical official amendments were compared; their fingerprints are in the [official-source manifest](../data/official-source-manifest.json). The search log records the questions asked, not a claim that every result or every paper was read in full.",'',
           'The intended coverage is comprehensive for these supplied editions, but prose questions require judgment and omissions remain possible. General encouragement to do research, unknown input values, attribution questions, and historical conjectures already settled in the same discussion are normally excluded. Explicit research exercises and specifically highlighted historical targets are retained even if later solved.','',
           'These are concise original paraphrases for navigation. Mathematical notation is local to each entry; named algorithms, graph families and exact computational models are defined at its book location. The [glossary](GLOSSARY.md) explains recurring terms. In particular, a theorem for a different machine model, asymptotic objective, graph family or probability convention is not silently treated as a solution.','',
           '## Useful starting points','',
           '- [Dynamic optimality of splay trees](vol3.md#v3-t-splay): an unnumbered research question on page 478.',
           '- [Research exercises and questions in Volume 4A](vol4a.md).',
           '- [Questions from Constraint Satisfaction, Fascicle 7](vol4-fasc7.md).','',
           f'For unresolved work, start with entries marked “Open in a cited source” and read the remaining target in “Partial results.” The {counts["no_resolution_located"]} entries marked “Resolution not located” need further literature verification before being advertised as open.','',
           '## Data and reproducibility','',
           '`catalog.json` is the reviewed source. Each entry records its location, original and amended ratings, a short question, an assessment, primary-source links, and search batch IDs. `catalog.csv` contains one row per entry, with source links and amendments in separate columns. `search-log.json` contains only query metadata; no third-party search excerpts or copies of papers are included.','',
           'Regenerate the readable files after editing the JSON:','',
           '```bash','python3 scripts/build_research_catalog.py','python3 scripts/build_research_catalog.py --check','```','',
           'The check validates IDs, assessments, evidence references, source URL structure and consistency of the generated documents. It does not prove the mathematical claims or certify literature completeness. The repository remains private.']
    return '\n'.join(text).rstrip()+'\n'

def search_document(data,searches):
    byid={r['id']:r for r in data['items']}
    text=['# Literature search record','',f"Review cutoff: **{data['as_of']}**.",'',
          'This log contains queries and direct source URLs, with links back to the questions they informed. Searches can be relevant to several entries. Their presence is not evidence that every result was useful or that an unlocated solution does not exist. Primary sources supporting an assessment are linked in the entry itself.','']
    for b in searches:
        text += [f"## S{b['id']:02d}",'']
        for q in b['queries']:text.append('- '+q)
        if b['opened_urls']:
            text+=['','Direct source checks:','']
            for u in b['opened_urls']:text.append(f'- [Source page]({u})')
        if b['referenced_by']:
            text+=['','Used for: '+', '.join(f"[{i}]({byid[i]['volume']}.md#{anchor(byid[i])})" for i in b['referenced_by'])+'.','']
        elif not b['queries'] and not b['opened_urls']:
            text+=['Follow-up access using temporary browser references; durable evidence links appear in the relevant catalogue entries.','']
    return '\n'.join(text).rstrip()+'\n'

def csv_document(data):
    out=io.StringIO(newline='')
    fields=['id','volume','kind','section','exercise','printed_page','original_rating','official_rating','title','question','status','status_note','source_urls','sources','official_updates','search_batches','additional_locations']
    w=csv.DictWriter(out,fieldnames=fields,lineterminator='\n');w.writeheader()
    for r in data['items']:
        x={k:r.get(k,'') for k in fields}
        x['source_urls']=' | '.join(s['url'] for s in r['sources'])
        for k in ('sources','official_updates','search_batches','additional_locations'):
            x[k]=json.dumps(r.get(k,[]),ensure_ascii=False)
        w.writerow(x)
    return out.getvalue()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='Check without modifying generated files')
    args=parser.parse_args()
    data,searches=load()
    docs={f"{v['id']}.md":volume_document(data,v) for v in data['volumes']}
    docs.update({'README.md':index_document(data,searches),'SEARCHES.md':search_document(data,searches),'catalog.csv':csv_document(data)})
    for name,content in docs.items():
        path=OUT/name
        if args.check:
            assert path.read_bytes()==content.encode(),f'Stale generated file: {name}'
        else:path.write_bytes(content.encode())
    print(f"Research catalogue {'verified' if args.check else 'built'}: {len(data['items'])} entries, {len(searches)} search batches, {len(docs)} generated files.")

if __name__=='__main__':main()

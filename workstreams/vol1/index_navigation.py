"""Build a navigation inventory, not an authoritative transcription, of the index."""
from pathlib import Path
import ast
import collections
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'workstreams/vol1/results'
BOOK = ROOT / 'books/taocp-vol1-ed3-print1-1997.djvu'
LINE = re.compile(r'\(line\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+("(?:\\.|[^"\\])*")\s*\)', re.S)
PAGE_TOKEN = r'(?:\d{1,3}|[ivx]+)(?:[-–—](?:\d{1,3}|[ivx]+))?'
REFERENCES = re.compile(r',\s+(' + PAGE_TOKEN + r'(?:,\s*' + PAGE_TOKEN + r')*)(?=[.,;]|\s+(?:see|$)|$)')


def build():
    entries, pages = [], []
    parent = None
    for page in range(628, 651):
        raw = subprocess.run(['djvutxt', f'-page={page + 15}', '-detail=line', str(BOOK)],
                             check=True, capture_output=True, text=True).stdout
        (OUT / f'index-p{page}-lines.sexp').write_text(raw)
        lines = []
        for match in LINE.finditer(raw):
            x1, y1, x2, y2 = map(int, match.group(1, 2, 3, 4))
            text = ast.literal_eval(match[5]).strip()
            if not text or text == str(page) or 'INDEX AND GLOSSARY' in text:
                continue
            if page == 628 and y1 > 2500:
                continue
            if page == 650 and y1 < 2700:
                # Closing quotation and colophon are reviewed separately.
                continue
            lines.append(dict(box=[x1, y1, x2, y2], text=text,
                              column=0 if x1 < 900 else 1))
        bases = {}
        for col in (0, 1):
            starts = [x['box'][0] for x in lines if x['column'] == col]
            bins = collections.Counter(round(x / 10) * 10 for x in starts)
            bases[col] = min(k for k, count in bins.items() if count >= 3)
        begin = len(entries)
        for line in lines:
            delta = line['box'][0] - bases[line['column']]
            if delta >= 72 and entries:
                entries[-1]['ocr_text'] += ' ' + line['text']
                entries[-1]['lines'].append(dict(page=page, **line))
                continue
            kind = 'main' if delta < 28 else 'subentry'
            entry_id = f'index-{len(entries) + 1:04}'
            if kind == 'main':
                parent = entry_id
            entries.append(dict(id=entry_id, index_page=page, kind=kind,
                                parent=parent if kind == 'subentry' else None,
                                ocr_text=line['text'], lines=[dict(page=page, **line)],
                                reference_status='pending'))
        pages.append(dict(page=page, lines=len(lines), entries_started=len(entries)-begin,
                          bases=bases, visual_read_status='pending'))
    for entry in entries:
        refs = []
        for match in REFERENCES.finditer(entry['ocr_text']):
            for token in re.split(r',\s*', match[1]):
                parts = re.split('[-–—]', token)
                if len(parts) == 2 and all(x.isdigit() for x in parts):
                    lo, hi = map(int, parts)
                    if 1 <= lo <= hi <= 627:
                        refs.extend(range(lo, hi + 1))
                    else:
                        refs.append(token)
                elif len(parts) == 1 and token.isdigit():
                    refs.append(int(token))
                else:
                    refs.append(token)
        entry['possible_page_targets'] = refs
    data = dict(scope='OCR and indentation navigation only; originals and errata remain authoritative.',
                pages=pages, entries=entries)
    (OUT / 'index-navigation.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    with (OUT / 'index-navigation.txt').open('w') as f:
        for entry in entries:
            f.write(f"{entry['id']} p{entry['index_page']} {entry['kind']}: {entry['ocr_text']}\n")
    print(json.dumps(dict(pages=len(pages), provisional_entries=len(entries),
                          possible_references=sum(len(e['possible_page_targets']) for e in entries))))


if __name__ == '__main__':
    build()

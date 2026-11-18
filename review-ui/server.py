#!/usr/bin/env python3
"""Local, dependency-free review server. Ledger is read-only; notes use SQLite."""
from pathlib import Path
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs, unquote
from datetime import datetime, timezone
from contextlib import contextmanager
from functools import lru_cache
import argparse
import hashlib
import json
import mimetypes
import os
import re
import sqlite3
import threading
import sys

APP = Path(__file__).resolve().parent
sys.path.insert(0, str(APP))
ROOT = APP.parent
AUDIT = ROOT / 'audit-2026-10-31'
BOOK = ROOT / 'books/taocp-vol4b-ed1-print2-2022.pdf'
DB = Path(os.environ.get('KNUTH_REVIEW_DB', APP/'data/annotations.sqlite3'))
# Published corrections remain in the source ledgers, outside the findings UI.
STATUSES = {'confirmed', 'candidate', 'dismissed'}
SEVERITIES = {'critical', 'high', 'medium', 'low', 'unclassified'}
REVIEWS = {'pending', 'verified', 'rejected', 'followup'}
LOCK = threading.RLock()
CATALOG_LOCK = threading.RLock()


def now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


@contextmanager
def connection():
    DB.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(DB, timeout=10)
    db.row_factory = sqlite3.Row
    db.execute('PRAGMA journal_mode=WAL')
    db.execute('''CREATE TABLE IF NOT EXISTS annotations (
        id TEXT PRIMARY KEY, note TEXT NOT NULL DEFAULT '',
        review TEXT NOT NULL DEFAULT 'pending', starred INTEGER NOT NULL DEFAULT 0,
        severity TEXT, revision INTEGER NOT NULL DEFAULT 0, updated_at TEXT)''')
    db.execute('''CREATE TABLE IF NOT EXISTS annotation_history (
        id TEXT NOT NULL, revision INTEGER NOT NULL, data TEXT NOT NULL,
        PRIMARY KEY (id, revision))''')
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def empty_annotation():
    return dict(note='', review='pending', starred=False, severity=None, revision=0, updated_at=None)


def annotation_dict(row):
    result = dict(row)
    result.pop('id', None)
    result['starred'] = bool(result['starred'])
    return result


def annotations():
    with connection() as db:
        return {row['id']: annotation_dict(row) for row in db.execute('SELECT * FROM annotations')}


def safe_file(path):
    resolved = (ROOT/path).resolve()
    if not resolved.is_relative_to(ROOT) or not resolved.is_file():
        return None
    return resolved


def catalog_fingerprint():
    p = APP / 'catalog.json'
    return (p.stat().st_mtime_ns, p.stat().st_size)


@lru_cache(maxsize=1)
def catalog(fingerprint):
    data = json.loads((APP / 'catalog.json').read_text())
    allowed = set(json.loads((APP / 'evidence-files.json').read_text()))
    return data, allowed


def read_data():
    # Concurrent first requests must share one catalog construction.
    with CATALOG_LOCK:
        data, allowed = catalog(catalog_fingerprint())
    saved = annotations()
    books = {v['book_path']: bool(safe_file(v['book_path'])) for v in data['volumes']}
    allowed = allowed | {p for p, exists in books.items() if exists}
    volumes = [dict(v, book_available=books[v['book_path']]) for v in data['volumes']]
    data = dict(data, volumes=volumes, progress=dict(data['progress'], volumes=volumes))
    # Never cache personal notes or share mutable annotation objects between requests.
    data = dict(data, generated_at=now(), findings=[dict(f,
        book_available=books[f['book_path']], annotation=saved.get(f['id'],empty_annotation())) for f in data['findings']])
    return data, allowed


class Handler(BaseHTTPRequestHandler):
    server_version = 'KnuthReview/1.0'

    def log_message(self, fmt, *args):
        if not args or not str(args[0]).startswith('GET /api/findings'):
            super().log_message(fmt,*args)

    def send_json(self, value, status=200, attachment=False):
        raw = json.dumps(value, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header('Content-Type','application/json; charset=utf-8')
        self.send_header('Content-Length',str(len(raw)))
        self.send_header('Cache-Control','no-store')
        self.send_header('X-Content-Type-Options','nosniff')
        if attachment:
            self.send_header('Content-Disposition','attachment; filename="knuth-review-notes.json"')
        self.end_headers()
        if self.command != 'HEAD':
            self.wfile.write(raw)

    def local_request(self):
        host = self.headers.get('Host','').split(':')[0]
        if host not in {'localhost','127.0.0.1'}:
            self.send_json({'error':'Access is allowed only through localhost.'},403)
            return False
        origin = self.headers.get('Origin')
        if origin and origin != f'http://{self.headers.get("Host")}':
            self.send_json({'error':'This request origin is not allowed.'},403)
            return False
        return True

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        if not self.local_request():
            return
        path = urlparse(self.path)
        if path.path == '/api/findings':
            self.send_json(read_data()[0]); return
        if path.path == '/api/research':
            p = APP/'research.json'
            self.send_json(json.loads(p.read_text()) if p.exists() else {'sources':[]}); return
        if path.path == '/api/export':
            self.send_json(dict(exported_at=now(), annotations=annotations()),attachment=True); return
        if path.path in {'/files','/api/document'}:
            requested = parse_qs(path.query).get('path',[''])[0]
            _, allowed = read_data()
            file = safe_file(requested)
            if requested not in allowed or not file:
                self.send_json({'error':'This file is not part of the audit evidence.'},404); return
            if path.path == '/api/document':
                if file.suffix.lower() not in {'.md','.txt','.json','.py','.c','.cpp','.w','.log'}:
                    self.send_json({'error':'This format cannot be displayed as text.'},400); return
                with file.open('rb') as f:
                    content = f.read(2_000_001)
                self.send_json(dict(text=content[:2_000_000].decode('utf-8',errors='replace'),
                                    truncated=len(content)>2_000_000, name=file.name)); return
            self.send_file(file, trusted=False); return
        if path.path.startswith('/api/'):
            self.send_json({'error':'Unknown endpoint.'},404); return
        base = APP/'dist'
        file = (base/unquote(path.path).lstrip('/')).resolve()
        if not file.is_relative_to(base.resolve()):
            self.send_json({'error':'Invalid path.'},404); return
        if path.path == '/':
            file = base/'index.html'
        if not file.is_file():
            self.send_json({'error':'File not found. Run npm run build first.'},404); return
        self.send_file(file, trusted=True)

    def send_file(self, file, trusted):
        size = file.stat().st_size
        start, end, status = 0, size-1, 200
        byte_range = self.headers.get('Range')
        if byte_range:
            match = re.fullmatch(r'bytes=(\d*)-(\d*)',byte_range)
            if not match or not any(match.groups()):
                self.send_json({'error':'Invalid range.'},416); return
            a,b = match.groups()
            if not a:
                start=max(0,size-int(b))
            else:
                start=int(a);end=min(end,int(b)) if b else end
            if start>end or start>=size:
                self.send_response(416);self.send_header('Content-Range',f'bytes */{size}');self.end_headers();return
            status=206
        self.send_response(status)
        mime=mimetypes.guess_type(file.name)[0] or 'application/octet-stream'
        if not trusted and file.suffix in {'.md','.py','.c','.cpp','.w','.log','.txt'}:
            mime='text/plain; charset=utf-8'
        self.send_header('Content-Type',mime)
        if not trusted and file.suffix.lower() in {'.html','.htm','.svg'}:
            self.send_header('Content-Disposition','attachment')
        self.send_header('X-Content-Type-Options','nosniff')
        self.send_header('Accept-Ranges','bytes')
        self.send_header('Cache-Control','no-cache' if trusted else 'private, max-age=300')
        self.send_header('Content-Length',str(end-start+1))
        if status==206:
            self.send_header('Content-Range',f'bytes {start}-{end}/{size}')
        self.end_headers()
        if self.command=='HEAD':return
        try:
            with file.open('rb') as f:
                f.seek(start);remaining=end-start+1
                while remaining:
                    chunk=f.read(min(128*1024,remaining))
                    if not chunk:break
                    self.wfile.write(chunk);remaining-=len(chunk)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def do_PATCH(self):
        if not self.local_request():return
        match=re.fullmatch(r'/api/annotations/([A-Z0-9-]+)',urlparse(self.path).path)
        if not match:
            self.send_json({'error':'Unknown finding.'},404);return
        ident=match[1]
        if ident not in {x['id'] for x in read_data()[0]['findings']}:
            self.send_json({'error':'Unknown finding.'},404);return
        try:
            length=int(self.headers.get('Content-Length','0'))
            if not 0<length<=600000:raise ValueError('Invalid note size.')
            patch=json.loads(self.rfile.read(length))
            if not isinstance(patch,dict):raise ValueError('Invalid data.')
            revision=patch.pop('revision',None)
            if type(revision) is not int or revision<0:raise ValueError('A valid note revision is required.')
            if set(patch)-{'note','review','starred','severity'}:raise ValueError('Unknown field.')
            if 'note' in patch and (not isinstance(patch['note'],str) or len(patch['note'])>100000):raise ValueError('The note must be text with at most 100,000 characters.')
            if 'review' in patch and patch['review'] not in REVIEWS:raise ValueError('Invalid review status.')
            if 'severity' in patch and patch['severity'] is not None and patch['severity'] not in SEVERITIES:raise ValueError('Invalid severity.')
            if 'starred' in patch and type(patch['starred']) is not bool:raise ValueError('Invalid bookmark value.')
        except (ValueError,TypeError,json.JSONDecodeError) as e:
            self.send_json({'error':str(e)},400);return
        with LOCK, connection() as db:
            db.execute('BEGIN IMMEDIATE')
            row=db.execute('SELECT * FROM annotations WHERE id=?',(ident,)).fetchone()
            current=annotation_dict(row) if row else empty_annotation()
            if current['revision']!=revision:
                self.send_json(dict(error='This note changed in another window. Your draft has been preserved.',current=current),409);return
            if row:
                db.execute('INSERT OR IGNORE INTO annotation_history VALUES (?,?,?)',
                    (ident,current['revision'],json.dumps(current,ensure_ascii=False)))
            current.update(patch)
            current.update(revision=revision+1,updated_at=now())
            db.execute('INSERT OR REPLACE INTO annotations VALUES (?,?,?,?,?,?,?)',
                (ident,current['note'],current['review'],int(current['starred']),current['severity'],current['revision'],current['updated_at']))
            db.execute('INSERT INTO annotation_history VALUES (?,?,?)',
                (ident,current['revision'],json.dumps(current,ensure_ascii=False)))
            db.commit()
        self.send_json(current)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--port',type=int,default=4318)
    args=parser.parse_args()
    with connection():
        pass
    print(f'Knuth review: http://localhost:{args.port}',flush=True)
    print(f'Notes: {DB}',flush=True)
    ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()

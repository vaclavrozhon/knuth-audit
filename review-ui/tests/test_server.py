"""Integration checks for the portable UI; all annotations use temporary storage."""
import importlib.util
import json
from pathlib import Path
import sqlite3
import tempfile
import threading
import unittest
from http.client import HTTPConnection
from urllib.parse import quote

APP = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('portable_review_server', APP / 'server.py')
server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)


class QuietHandler(server.Handler):
    def log_message(self, *args):
        pass


class ServerTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix='knuth-portable-test-')
        self.original_db = server.DB
        server.DB = Path(self.directory.name) / 'notes.sqlite3'
        self.http = server.ThreadingHTTPServer(('127.0.0.1', 0), QuietHandler)
        self.thread = threading.Thread(target=self.http.serve_forever, daemon=True)
        self.thread.start()

    def tearDown(self):
        self.http.shutdown()
        self.http.server_close()
        self.thread.join()
        server.DB = self.original_db
        self.directory.cleanup()

    def request(self, method, path, payload=None, headers=None):
        conn = HTTPConnection('127.0.0.1', self.http.server_port, timeout=15)
        body = json.dumps(payload, ensure_ascii=False).encode() if payload is not None else None
        conn.request(method, path, body=body, headers=headers or {})
        response = conn.getresponse()
        result = response.status, dict(response.getheaders()), response.read()
        conn.close()
        return result

    def patch(self, ident, **fields):
        status, _, body = self.request('PATCH', '/api/annotations/' + ident, fields)
        return status, json.loads(body)

    def test_catalog_and_compiled_frontend_work_without_books(self):
        status, _, body = self.request('GET', '/api/findings')
        self.assertEqual(status, 200)
        data = json.loads(body)
        self.assertEqual(len(data['findings']), 946)
        self.assertEqual(sum(f['status'] == 'confirmed' for f in data['findings']), 817)
        self.assertTrue(all(f['annotation']['revision'] == 0 for f in data['findings']))
        self.assertEqual(self.request('GET', '/')[0], 200)
        for volume in data['volumes']:
            exists = server.safe_file(volume['book_path']) is not None
            self.assertEqual(volume['book_available'], exists)
            if not exists:
                self.assertEqual(self.request('GET', '/files?path=' + quote(volume['book_path']))[0], 404)

    def test_notes_persist_without_colliding_between_volumes(self):
        for ident, note in [('V1-C0002', 'Ověřit ε < 1.\n<b>Plain text</b>'),
                            ('V2-C0002', 'Volume two'), ('F014', 'Volume four B')]:
            status, saved = self.patch(ident, revision=0, note=note)
            self.assertEqual(status, 200)
            self.assertEqual(saved['revision'], 1)
            status, saved = self.patch(ident, revision=1, starred=True, review='verified')
            self.assertEqual(status, 200)
            self.assertEqual(saved['note'], note)
            with sqlite3.connect(server.DB) as db:
                self.assertEqual(db.execute('SELECT count(*) FROM annotation_history WHERE id=?',
                                            (ident,)).fetchone()[0], 2)
        status, headers, body = self.request('GET', '/api/export')
        self.assertEqual(status, 200)
        self.assertIn('attachment', headers['Content-Disposition'])
        notes = json.loads(body)['annotations']
        self.assertEqual(set(notes), {'V1-C0002', 'V2-C0002', 'F014'})
        self.assertEqual(notes, server.annotations())

    def test_stale_window_cannot_overwrite_a_note(self):
        self.assertEqual(self.patch('F014', revision=0, note='First window')[0], 200)
        status, conflict = self.patch('F014', revision=0, note='Stale window')
        self.assertEqual(status, 409)
        self.assertEqual(conflict['current']['note'], 'First window')
        self.assertEqual(server.annotations()['F014']['note'], 'First window')

    def test_invalid_edits_and_remote_origins_are_rejected(self):
        for fields in [dict(note='No revision'), dict(revision=True), dict(revision=0, starred='yes'),
                       dict(revision=0, severity='extreme'), dict(revision=0, note=['not text'])]:
            with self.subTest(fields=fields):
                self.assertEqual(self.patch('F014', **fields)[0], 400)
        self.assertEqual(self.patch('UNKNOWN', revision=0, note='x')[0], 404)
        self.assertEqual(self.request('GET', '/api/findings', headers={'Host': 'other.example'})[0], 403)
        self.assertEqual(self.request('PATCH', '/api/annotations/F014', {'revision': 0, 'note': 'x'},
                                      {'Origin': 'https://other.example'})[0], 403)
        self.assertEqual(server.annotations(), {})

    def test_only_listed_evidence_is_served(self):
        for path in ['../../.ssh/id_rsa', 'review-ui/data/annotations.sqlite3',
                     'review-ui/server.py', 'review-ui/package.json', '.git/config']:
            with self.subTest(path=path):
                self.assertEqual(self.request('GET', '/files?path=' + quote(path))[0], 404)
        self.assertEqual(self.request('GET', '/%2e%2e/server.py')[0], 404)
        status, _, body = self.request('GET', '/api/document?path=findings/F7-C0006.md')
        self.assertEqual(status, 200)
        self.assertIn('F7-C0006', json.loads(body)['text'])
        image = 'workstreams/vol4-fasc7/images/F7-C0008-reflex-W.png'
        status, headers, body = self.request('GET', '/files?path=' + quote(image),
                                             headers={'Range': 'bytes=0-7'})
        self.assertEqual(status, 206)
        self.assertEqual(body, b'\x89PNG\r\n\x1a\n')
        self.assertTrue(headers['Content-Range'].startswith('bytes 0-7/'))
        self.assertEqual(self.request('GET', '/files?path=' + quote(image),
                                      headers={'Range': 'bytes=999999999999-'})[0], 416)

    def test_optional_books_are_detected_without_exposing_other_files(self):
        original_root = server.ROOT
        try:
            server.ROOT = Path(self.directory.name).resolve()
            data, _ = server.read_data()
            volume = data['volumes'][-1]
            path = server.ROOT / volume['book_path']
            path.parent.mkdir(parents=True)
            path.write_bytes(b'%PDF-1.4\nTemporary test fixture, not a book.\n')
            data, allowed = server.read_data()
            self.assertTrue(data['volumes'][-1]['book_available'])
            self.assertIn(volume['book_path'], allowed)
            status, _, body = self.request('GET', '/files?path=' + quote(volume['book_path']),
                                          headers={'Range': 'bytes=0-4'})
            self.assertEqual((status, body), (206, b'%PDF-'))
        finally:
            server.ROOT = original_root

    def test_prior_public_reports_have_no_active_cards_or_page_markers(self):
        hidden = {'V1-C0010', 'V2-C0001', 'F097', 'F101'}
        data, _ = server.read_data()
        self.assertFalse(hidden & {f['id'] for f in data['findings']})
        for volume in data['volumes']:
            for page in volume['page_map']['pages']:
                self.assertFalse(hidden & set(page['errors'] + page['candidates'] + page['related']))
        # Notes made on an older snapshot remain exportable after an assessment changes.
        with server.connection() as db:
            db.execute('INSERT INTO annotations (id, note) VALUES (?, ?)', ('F097', 'Earlier local note'))
        self.assertEqual(json.loads(self.request('GET', '/api/export')[2])['annotations']['F097']['note'],
                         'Earlier local note')


if __name__ == '__main__':
    unittest.main()

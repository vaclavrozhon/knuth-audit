"""Playwright server using disposable notes, never the user's annotation DB."""
import importlib.util
from pathlib import Path
import tempfile

APP = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('browser_review_server', APP / 'server.py')
server = importlib.util.module_from_spec(spec)
spec.loader.exec_module(server)
with tempfile.TemporaryDirectory(prefix='knuth-portable-browser-') as directory:
    server.DB = Path(directory) / 'notes.sqlite3'
    print('Browser test server: http://127.0.0.1:4319', flush=True)
    server.ThreadingHTTPServer(('127.0.0.1', 4319), server.Handler).serve_forever()

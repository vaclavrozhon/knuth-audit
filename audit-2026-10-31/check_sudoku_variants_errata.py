#!/usr/bin/env python3
"""Record the complete current/historical errata check for DLX55--58."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import re
import urllib.request
from dlx1_audit_tools import ROOT, sha

OUT = ROOT/'results/sudoku_variants'


def remote(name):
    url = 'https://www-cs-faculty.stanford.edu/~knuth/'+name
    with urllib.request.urlopen(url,timeout=45) as response:
        data = response.read()
    digest = hashlib.sha256(data).hexdigest()
    assert digest == sha(ROOT.parent/'errata/originals'/name),name
    return dict(file=name,url=url,sha256=digest,unchanged=True)


def main():
    files = ['errata/text/all4b.txt','errata/text/err4b.txt','errata/text/all4f5.txt',
             'errata/text/err4f5.txt','errata/originals/err4b.textxt','errata/originals/err4f5.textxt']
    hits = []
    pattern = re.compile(r'(?:Page\s+(?:127|129|235|236|427|428|671)\b|4(?:b|f5)\.(?:127|129|235|236|427|428|671)\b|\b(?:16417|15681|2043|2592|864)\b|trio|1472|Thoen|Dobrichev)',re.I)
    for file in files:
        lines = (ROOT.parent/file).read_text().splitlines()
        for i,line in enumerate(lines):
            if pattern.search(line):
                hits.append(dict(file=file,line=i+1,context='\n'.join(lines[max(0,i-1):i+6])))
    with ThreadPoolExecutor(max_workers=4) as pool:
        remotes = list(pool.map(remote,['all4b.ps.gz','all4f5.ps.gz','err4b.textxt','err4f5.textxt']))
    result = dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),
                  remote_files=remotes,local_files={file:sha(ROOT.parent/file) for file in files},search_hits=hits,
                  conclusions=['Question57 has the known10Sep2021 correction to at most27, incorporated in4B.',
                               'Answer58 has the known05Feb2021 colored-item and four-solutions correction, incorporated in4B.',
                               'No matching correction found for answer57 normalization/count or the omitted symbol renaming in its isomorphism claim.',
                               'Same-numbered exercises or pages outside the corresponding section are unrelated.'])
    (OUT/'errata-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Four remote files unchanged; six complete errata texts searched;',len(hits),'context records retained.')


if __name__ == '__main__':
    main()

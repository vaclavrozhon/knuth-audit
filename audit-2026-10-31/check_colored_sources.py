#!/usr/bin/env python3
"""Preserve primary evidence for the Acta Mathematica footnote (p87)."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,urllib.request

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'sources/colored_basics'
SOURCES=[
 ('mittag-publications.html','https://www.mittag-leffler.se/publications/',
  'The issuing institute dates the founding of Acta Mathematica to1882.'),
 ('koornwinder1995.html','https://math.nist.gov/opsf/misc/op2616.html',
  'First-person library account: Riesz table published1913, biographies, article lists and portraits.'),
 ('bibliography1913.pdf','https://www.e-periodica.ch/cntmng?bot=1&pid=ens-001%3A1913%3A15%3A%3A304',
  'Contemporary1913 bulletin, printedp528: Riesz supplement has179pages, contents and portraits.'),
 ('domar1982.pdf','https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6309-11511_2006_Article_BF02392722.pdf',
  'History published by Acta Mathematica, printedp8: first issue presented12December1882.')]


def fetch(source):
    name,url,note=source; path=OUT/name
    try:
        if not path.exists():
            with urllib.request.urlopen(url,timeout=45) as r:
                data=r.read(); final=r.url
        else: data=path.read_bytes(); final=url
        valid=data.startswith(b'%PDF') if name.endswith('.pdf') else b'html' in data.lower()[:3000]
        if not valid:
            # Keep an HTTP200 verification page as HTML, never pretend it is
            # the requested PDF or use its contents as bibliographic proof.
            failed=path.with_suffix('.response.html');failed.write_bytes(data)
            if path.exists():path.unlink()
            return dict(url=url,status='unavailable',response_file=str(failed.relative_to(ROOT)),reason='Expected PDF, received HTML verification page')
        path.write_bytes(data)
        return dict(file=str(path.relative_to(ROOT)),url=url,final_url=final,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),scope=note,status='archived')
    except Exception as e:
        return dict(url=url,status='unavailable',reason=str(e),intended_scope=note)


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    with ThreadPoolExecutor(max_workers=4) as pool: records=list(pool.map(fetch,SOURCES))
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),sources=records,
      conclusion='Candidate C025:1882+21=1903, not1913. The cited table covers1882--1912, three decades. Verify its original preface and the commemorative occasion before confirming.',
      limitations='The full Riesz1913 table has not been obtained. The exhaustiveness of the27 names relative to all Acta contributors and TAOCP1--3 indexes remains unverified. NIST was readable through the web tool, but its raw download was403. E-periodica initially returned HTML verification; its publicly linked bot=1 URL subsequently supplied the actual10-page original bulletin, visually checked on printedp528.')
    (OUT/'manifest.json').write_text(json.dumps(result,indent=2)+'\n')
    print(sum(x['status']=='archived' for x in records),'sources archived;',sum(x['status']=='unavailable' for x in records),'unavailable; gaps retained')


if __name__=='__main__':main()

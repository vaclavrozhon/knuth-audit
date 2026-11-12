#!/usr/bin/env python3
"""Build official DLX2 change files and the original cell-by-cell word solver."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json,re,shutil,subprocess,tempfile,urllib.request
from double_word_tools import ROOT,OUT


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def build():
    manifest=OUT/'build.json'
    if manifest.exists():
        data=json.loads(manifest.read_text())
        for x in data['binaries'].values():assert sha(x['path'])==x['sha256']
        for p,h in data['sources'].items():assert sha(ROOT/p)==h
        return data
    OUT.mkdir(parents=True,exist_ok=True);sources=ROOT/'sources/double_words';sources.mkdir(parents=True,exist_ok=True)
    fetched=[]
    for name in ['dlx2-kludge.ch','dlx2-cutoff-kludge.ch']:
        url='https://www-cs-faculty.stanford.edu/~knuth/programs/'+name
        with urllib.request.urlopen(url,timeout=45) as r:raw=r.read()
        assert raw.startswith(b'@x')
        path=sources/name
        if path.exists():assert path.read_bytes()==raw
        else:path.write_bytes(raw)
        fetched.append(dict(path=str(path.relative_to(ROOT)),url=url,sha256=sha(path)))
    directory=Path(tempfile.mkdtemp(prefix='knuth-vol4b-double-'))
    original=ROOT/'sources/knuth-programs'
    for name in ['dlx2.w','gb_flip.w','gb_flip.ch','boilerplate.w','back-mxn-words-mxn.w']:
        shutil.copy2(original/name,directory/name)
    base=(original/'dlx2.w').read_text()
    raw=(sources/'dlx2-cutoff-kludge.ch').read_text()
    marker='            nn=dd;@+continue;\n          }'
    start=base.index('void unpurify(int p) {');stop=base.index(marker,start)+len(marker)
    adapted=re.sub(r'@x\nvoid unpurify\(int p\) \{.*?\n@y',lambda _: '@x\n'+base[start:stop]+'\n@y',raw,flags=re.S)
    assert re.findall(r'@y\n(.*?)\n@z',raw,re.S)==re.findall(r'@y\n(.*?)\n@z',adapted,re.S)
    (OUT/'dlx2-cutoff-kludge-context.ch').write_text(adapted)
    shutil.copy2(sources/'dlx2-kludge.ch',directory/'dlx2-kludge.ch')
    (directory/'dlx2-cutoff-kludge.ch').write_text(adapted)
    commands=[['ctangle','gb_flip.w','gb_flip.ch']]
    for label in ['kludge','cutoff-kludge']:
        commands += [['ctangle','dlx2.w','dlx2-'+label+'.ch','dlx2-'+label+'.c'],
                     ['cc','-O3','-Wno-implicit-int','-Wno-implicit-function-declaration','dlx2-'+label+'.c','gb_flip.c','-o','dlx2-'+label]]
    commands += [['ctangle','back-mxn-words-mxn.w'],['cc','-O3','-std=gnu89','-w','back-mxn-words-mxn.c','-o','cell']]
    with (OUT/'build.log').open('w') as log:
        for command in commands:subprocess.run(command,cwd=directory,stdout=log,stderr=subprocess.STDOUT,check=True)
    paths=[original/n for n in ['dlx2.w','gb_flip.w','gb_flip.ch','boilerplate.w','back-mxn-words-mxn.w']]+[sources/n for n in ['dlx2-kludge.ch','dlx2-cutoff-kludge.ch']]+[OUT/'dlx2-cutoff-kludge-context.ch']
    data=dict(built_at_utc=datetime.now(timezone.utc).isoformat(),directory=str(directory),commands=commands,
        sources={str(p.relative_to(ROOT)):sha(p) for p in paths},fetched=fetched,
        binaries={label:dict(path=str(directory/name),sha256=sha(directory/name)) for label,name in [('all','dlx2-kludge'),('minimax','dlx2-cutoff-kludge'),('cell','cell')]},
        adaptation='Only the old @x context of unpurify is updated. All official @y replacements are unchanged. Original solver logic and mem counters are unchanged.')
    manifest.write_text(json.dumps(data,indent=2)+'\n');return data


if __name__=='__main__':print(json.dumps(build(),indent=2))

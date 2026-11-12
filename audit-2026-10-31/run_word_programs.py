#!/usr/bin/env python3
"""Build archived Knuth sources, validate every emitted rectangle, record runs.

Already completed cases are not rerun. Each case has its own stdout-derived
certificate, stderr log, timeout, PID and start/end metadata. No source edits.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/word_rectangles'
DATA = ROOT/'sources/wordlists'


def stamp():
    return datetime.now(timezone.utc).isoformat()


def save(path, obj):
    path.write_text(json.dumps(obj, indent=2)+'\n')


def build():
    directory = Path(tempfile.mkdtemp(prefix='knuth-vol4b-word-programs-'))
    binaries = {}
    commands = []
    for kind in ['mxn', 'new']:
        name = 'back-mxn-words-'+kind
        source = ROOT/'sources/knuth-programs'/(name+'.w')
        cfile = directory/(name+'.c')
        cmd = ['ctangle', str(source), '-', str(cfile)]
        subprocess.run(cmd, check=True, capture_output=True)
        commands.append(cmd)
        target = directory/name
        cmd = ['gcc', '-O3', '-std=gnu89', '-w', str(cfile), '-o', str(target)]
        subprocess.run(cmd, check=True, capture_output=True)
        commands.append(cmd)
        binaries[kind] = target
    save(OUT/'original-build.json', {'commands':commands, 'directory':str(directory),
                                    'built_at_utc':stamp()})
    return binaries


def words(n):
    return DATA/f'words{n}-from-{"sgb" if n == 5 else "OSPD4"}'


def run(binary, label, mfile, nfile, limit, expected, reverse=False):
    dest = OUT/(label+'.json')
    if dest.exists() and json.loads(dest.read_text()).get('verified'):
        print(label+': already verified; skipped', flush=True)
        return
    if reverse:
        generated = OUT/'inputs'
        generated.mkdir(exist_ok=True)
        files=[]
        for source in [mfile,nfile]:
            target=generated/(source.name+'-reversed')
            target.write_text('\n'.join(w[::-1] for w in source.read_text().splitlines())+'\n')
            files.append(target)
        mfile,nfile=files
    mw=mfile.read_text().splitlines();nw=nfile.read_text().splitlines()
    m,n=len(mw[0]),len(nw[0]);mrank={w:i+1 for i,w in enumerate(mw)};nrank={w:i+1 for i,w in enumerate(nw)}
    command=['timeout',str(limit),str(binary),str(mfile),str(nfile)]
    meta={'command':command,'started_at_utc':stamp(),'timeout_seconds':limit,
          'm':m,'n':n,'reverse':reverse,'expected_count':expected}
    meta_path=OUT/(label+'-run.json');save(meta_path,meta)
    start=time.monotonic();seen=set();repeated=symmetric=total=0
    xor_hash=sum_hash=0; witnesses=[]; best=None;small=[]
    with (OUT/(label+'.log')).open('w') as err:
        proc=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=err,text=True,bufsize=1)
        meta['pid']=proc.pid;save(meta_path,meta)
        try:
            for line in proc.stdout:
                number,tail=line.split(':',1)
                first,stats=tail.split('(',1);columns=first.split()
                assert len(columns)==n and all(w in mrank for w in columns),line
                rows=[''.join(w[i] for w in columns) for i in range(m)]
                assert all(w in nrank for w in rows),line
                total+=1;assert int(number)==total
                p=max(map(mrank.__getitem__,columns));q=max(map(nrank.__getitem__,rows))
                printed=list(map(int,re.findall(r'\d+',stats)))
                assert printed==[p,q,p+q,p*q],(line,p,q)
                flat=''.join(rows);assert flat not in seen;seen.add(flat)
                value=int.from_bytes(hashlib.sha256(flat.encode()).digest(),'big')
                xor_hash ^= value;sum_hash=(sum_hash+value)%(1<<256)
                if len(set(rows+columns))<m+n:repeated+=1
                if m==n and rows==columns:symmetric+=1
                if total<=8:witnesses.append(rows)
                if m==n and max(p,q)<=500:small.append(rows)
                if best is None or max(p,q)<best['rank']:
                    best={'rank':max(p,q),'rows':rows,'column_rank':p,'row_rank':q}
        except BaseException:
            proc.terminate();proc.wait();raise
        returncode=proc.wait()
    meta.update(returncode=returncode,elapsed_seconds=time.monotonic()-start,
                finished_at_utc=stamp(),validated_solutions=total)
    save(meta_path,meta)
    if returncode:
        save(dest,{'verified':False,'reason':'nonzero exit or timeout','validated_solutions':total})
        print(label+f': incomplete (return code {returncode}, {total} validated)',flush=True)
        return
    log=(OUT/(label+'.log')).read_text()
    match=re.search(r'Altogether (\d+) solutions \((\d+) mems\)',log)
    assert match and int(match[1])==total
    assert total==expected,(label,total,expected)
    profile=[];weights=[]
    lines=log[log.index('Profile:'):].splitlines()
    for i,line in enumerate(lines):
        fields=line.replace('Profile:','').split()
        profile.append(int(fields[0]))
        if len(fields)>1:weights.append(float(fields[1]))
    result={'verified':True,'count':total,'repeated_words':repeated,'symmetric':symmetric,
            'mems':int(match[2]),'profile':profile,'weights':weights,'best':best,
            'witnesses':witnesses,'small_squares':small,'sha256_xor':f'{xor_hash:064x}',
            'sha256_sum':f'{sum_hash:064x}'}
    save(dest,result)
    print(label+f': {total} solutions, every model validated; {match[2]} mems',flush=True)


def main():
    OUT.mkdir(exist_ok=True,parents=True)
    bins=build()
    cases=[('mxn','cell-5x5',5,5,1800,1787056,False),
           ('mxn','cell-5x6',5,6,3600,625415,False),
           ('mxn','cell-5x9',5,9,3600,2,False),
           ('mxn','cell-5x10',5,10,3600,0,False),
           ('mxn','cell-6x5',6,5,3600,625415,False),
           ('mxn','cell-6x5-reversed',6,5,3600,625415,True),
           ('new','column-5x6',5,6,7200,625415,False),
           ('new','column-6x5',6,5,14400,625415,False)]
    for kind,label,m,n,limit,expected,reverse in cases:
        run(bins[kind],label,words(m),words(n),limit,expected,reverse)


if __name__=='__main__':main()

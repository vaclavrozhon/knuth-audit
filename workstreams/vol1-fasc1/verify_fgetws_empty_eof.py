#!/usr/bin/env python3
"""Nine bounded real-stream calls per common original and audit correction."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

BASE=Path(__file__).resolve().parent
SOURCES,RESULTS=BASE/'sources',BASE/'results'
# Expected result and memory prefix come directly from the stated wyde contract.
CASES=[
    ('empty-two',2,5,'',-1,None),
    ('empty-block-boundary',128,5,'',-1,None),
    ('empty-high-size',2**32+2,5,'',-1,None),
    ('newline-before-more-data',2,5,'000a0041',1,'000a0000'),
    ('full-two-wyde-quota',3,5,'00010002',2,'000100020000'),
    ('embedded-nul-before-newline',4,5,'0000000a',2,'0000000a0000'),
    ('unit-capacity',1,5,'',0,'0000'),
    ('zero-capacity',0,5,'',-1,None),
    ('wrong-mode',2,2,'',-1,None),
]

def main():
    assert os.getpriority(os.PRIO_PROCESS,0)>=15,'Use nice -n 15.'
    original=SOURCES/'mmix-io-20250620.w'
    assert original.read_bytes()==(SOURCES/'mmix-io-20131017.w').read_bytes()
    env=dict(os.environ);env['CWEBINPUTS']=str(SOURCES)+':'
    rows,logs=[],[]
    result=dict(scope='Empty EOF before the first requested wyde and six controls. Real C temporary binary streams, no wchar_t conversion. EOF after a nonempty unterminated prefix and the interactive stdin adapter remain outside this correction.',
                common_original_sha256=hashlib.sha256(original.read_bytes()).hexdigest(),cases=rows)
    def checkpoint():
        (RESULTS/'fgetws-empty-eof.json').write_text(json.dumps(result,indent=2)+'\n')
        (RESULTS/'fgetws-empty-eof-build.json').write_text(json.dumps(logs,indent=2)+'\n')
    with tempfile.TemporaryDirectory(prefix='fgetws-audit-build-',dir=RESULTS) as tmp:
        build=Path(tmp);shutil.copyfile(SOURCES/'fgetws-empty-eof-driver.c',build/'driver.c')
        for version,change in [('original-2013-and-2025-identical','-'),
                               ('audit-empty-eof',str(SOURCES/'audit-fgetws-empty-eof.ch'))]:
            for cmd in [['ctangle',str(original),change,'mmix-io.c'],
                        ['gcc','-O0','-std=c11','driver.c','-o','driver']]:
                p=subprocess.run(cmd,cwd=build,env=env,text=True,capture_output=True)
                logs.append(dict(version=version,command=cmd,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));checkpoint();p.check_returncode()
            for name,size,mode,data,expected,prefix in CASES:
                p=subprocess.run([str(build/'driver'),str(size),str(mode),data],text=True,capture_output=True,check=True)
                actual,eof,error,pos,calls,stored,memory=p.stdout.split()
                expected_bits=f'{expected%2**64:016x}'
                row=dict(case=name,version=version,size=size,mode=mode,input_hex=data,
                         actual_bits=actual,expected_bits=expected_bits,eof=bool(int(eof)),
                         host_error=bool(int(error)),file_position=int(pos),memory_store_calls=int(calls),
                         stored_bytes=int(stored),memory_hex=memory,expected_memory_prefix=prefix,
                         agrees=actual==expected_bits and (prefix is None or memory.startswith(prefix)))
                rows.append(row);checkpoint()
    assert sum(not r['agrees'] for r in rows if r['version'].startswith('original'))==3
    assert all(r['agrees'] for r in rows if r['version'].startswith('audit'))
    print(json.dumps(dict(calls=len(rows),original_mismatches=3,audit_all_agree=True)))

if __name__=='__main__':main()

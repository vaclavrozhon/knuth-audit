#!/usr/bin/env python3
"""Eight short LP64 host-state-model cases per common original and patch."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
BASE=Path(__file__).resolve().parent
SOURCES,RESULTS=BASE/'sources',BASE/'results'
CASES=[('zero',0,5,0),('signed32-limit',2**31-1,5,0),
       ('low-tetra-limit',2**32-1,5,0),('first-high-tetra',2**32,5,0),
       ('high-and-low',2**32+17,5,0),('signed64-limit',2**63-1,5,0),
       ('host-ftell-error',2**32,5,1),('wrong-mode',2**32,2,0)]
def main():
    assert os.getpriority(os.PRIO_PROCESS,0)>=15,'Use nice -n 15.'
    original=SOURCES/'mmix-io-20250620.w'
    assert original.read_bytes()==(SOURCES/'mmix-io-20131017.w').read_bytes()
    env=dict(os.environ);env['CWEBINPUTS']=str(SOURCES)+':'
    rows,logs=[],[]
    result=dict(scope='Legal LP64 fseek-to-end/ftell state model; no large or sparse file is created, and no large-data I/O occurs. An empty real tmpfile supplies only a valid opaque FILE pointer; modeled position/length do not describe that host file.',
                common_original_sha256=hashlib.sha256(original.read_bytes()).hexdigest(),cases=rows)
    def checkpoint():
        (RESULTS/'ftell-high-tetra.json').write_text(json.dumps(result,indent=2)+'\n')
        (RESULTS/'ftell-high-tetra-build.json').write_text(json.dumps(logs,indent=2)+'\n')
    with tempfile.TemporaryDirectory(prefix='ftell-audit-build-',dir=RESULTS) as tmp:
        build=Path(tmp);shutil.copyfile(SOURCES/'ftell-high-tetra-driver.c',build/'driver.c')
        for version,change in [('original-2013-and-2025-identical','-'),
                               ('audit-preserve-high-tetra',str(SOURCES/'audit-ftell-high-tetra.ch'))]:
            for cmd in [['ctangle',str(original),change,'mmix-io.c'],
                        ['gcc','-O0','-std=c11','driver.c','-o','driver']]:
                p=subprocess.run(cmd,cwd=build,env=env,text=True,capture_output=True)
                logs.append(dict(version=version,command=cmd,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));checkpoint();p.check_returncode()
            for name,length,mode,error in CASES:
                p=subprocess.run([str(build/'driver'),str(length),str(mode),str(error)],text=True,capture_output=True,check=True)
                actual,expected,seek,seek_calls,tell_calls,position=p.stdout.split()
                rows.append(dict(case=name,version=version,mode=mode,modeled_binary_length=length,
                                 modeled_ftell_error=bool(error),actual_bits=actual,expected_bits=expected,
                                 fseek_result=seek,host_seek_calls=int(seek_calls),host_tell_calls=int(tell_calls),
                                 modeled_position_after_seek=int(position),agrees=actual==expected));checkpoint()
    assert sum(not r['agrees'] for r in rows if r['version'].startswith('original'))==3
    assert all(r['agrees'] for r in rows if r['version'].startswith('audit'))
    print(json.dumps(dict(calls=len(rows),original_mismatches=3,audit_all_agree=True)))
if __name__=='__main__':main()

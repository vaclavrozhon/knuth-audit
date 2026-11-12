"""Project every completion of the literal eight-word original-DLX2 model."""
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

from double_word_tools import dictionary, input_text
from word_kernel91 import literal_encoding, validate_completion


ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/stair_kernels'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(kind,W):
    prefix=OUT/f'{kind}{W}-native'
    result=prefix.with_suffix('.json')
    assert not result.exists(), 'Do not repeat a completed native projection.'
    build=json.loads((ROOT/'results/colored_basics/native/build.json').read_text())
    binary=build['binaries']['original']['binary']
    assert sha(binary)==build['binaries']['original']['sha256']
    words=dictionary(5)[:W];enc=literal_encoding(words,kind,True)
    inp=prefix.with_suffix('.dlx');inp.write_text(input_text(enc))
    meta=dict(kind=kind,W=W,wrapper_pid=os.getpid(),started_utc=datetime.now(timezone.utc).isoformat(),
              command=['timeout','4h',binary,'v129','m1'],input=str(inp),input_sha256=sha(inp),
              binary_sha256=sha(binary),script_sha256=sha(__file__),
              kernel_module_sha256=sha(ROOT/'word_kernel91.py'),
              wordlist_sha256=sha(ROOT/'sources/wordlists/words5-from-sgb'),status='running')
    status=prefix.with_name(prefix.name+'-run.json')
    start=time.monotonic();kernels=set();count=0;streamhash=hashlib.sha256();chosen=None;rowcount=0
    with inp.open('rb') as fin, prefix.with_suffix('.log').open('wb') as log:
        proc=subprocess.Popen(meta['command'],stdin=fin,stdout=subprocess.PIPE,stderr=log)
        meta['pid']=proc.pid;status.write_text(json.dumps(meta,indent=2)+'\n')
        print(f'{kind}{W}: native timeout PID {proc.pid}',flush=True)
        for line in proc.stdout:
            streamhash.update(line)
            if re.fullmatch(rb'\d+:\n',line):
                assert chosen is None
                count+=1;assert int(line[:-2])==count
                chosen=[None]*8;rowcount=0
            else:
                tokens=line.decode().split();slot=int(tokens[0][1:]);word=tokens[6]
                assert chosen is not None and chosen[slot] is None and word in enc['words']
                chosen[slot]=word;rowcount+=1
                if rowcount==8:
                    kernels.add(validate_completion(chosen,kind,True));chosen=None
        returncode=proc.wait()
    meta.update(returncode=returncode,finished_utc=datetime.now(timezone.utc).isoformat(),
                seconds=time.monotonic()-start,solutions=count,kernels=len(kernels),
                stdout_sha256=streamhash.hexdigest(),stderr_sha256=sha(prefix.with_suffix('.log')),
                status='completed' if returncode==0 else 'incomplete')
    status.write_text(json.dumps(meta,indent=2)+'\n')
    assert returncode==0 and chosen is None,meta
    summary=re.search(r'Altogether (\d+) solutions?',prefix.with_suffix('.log').read_text())
    assert summary and int(summary[1])==count
    target=OUT/f'{kind}{W}-distinct-kernels.txt'
    assert kernels==set(target.read_text().splitlines())
    meta.update(join_set_sha256=sha(target),complete_sets_equal=True)
    result.write_text(json.dumps(meta,indent=2)+'\n')
    print(json.dumps(meta),flush=True)


if __name__=='__main__':
    run(sys.argv[1],int(sys.argv[2]))

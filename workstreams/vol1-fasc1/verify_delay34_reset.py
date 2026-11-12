#!/usr/bin/env python3
"""Finite timer-breakpoint replay of a permitted reset effect, no real-time wait.

The proof is the invariant, not a timeout: after each expiry the live user
state repeats. MMIX-SIM pauses at rI expiry; debugger assignment models the
specified OS restoring rI before returning. This is not a kernel emulator.
"""
from pathlib import Path
import datetime
import hashlib
import json
import os
import argparse
import subprocess
import tarfile
import tempfile
import time

BASE=Path(__file__).resolve().parent
SOURCES=BASE/'sources';RESULTS=BASE/'results'

def main():
    assert os.getpriority(os.PRIO_PROCESS,0)>=15,'Use nice -n15.'
    parser=argparse.ArgumentParser()
    parser.add_argument('--delta',type=int,choices=[17,18])
    args=parser.parse_args()
    start=time.monotonic();logs=[]
    original=(SOURCES/'delay34-reset.mms').read_text()
    inspect='s\nrI!\n$253!\n$254!\n$255!\n'
    commands='rI=20\nc\n'+inspect+('rI=60\nc\n'+inspect)*3+'q\n'
    (SOURCES/'delay34-reset-debugger.txt').write_text(commands)
    result={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'scope':'Finite native execution of the exact printed Delay at two input boundaries; timer expiry uses the documented debugger breakpoint and resetting rI models only the allowed handler effect. Coinductive proof is separate; no timeout inference.',
            'initial_counter':20,'main_prefix_oops':2,'counter_at_Delay':18,
            'reset_counter':60,'reset_count':3,'runs':{}}
    if args.delta is not None:
        logs=json.loads((RESULTS/'delay34-reset-build-and-run.json').read_text())
        result=json.loads((RESULTS/'delay34-reset.json').read_text())
    def checkpoint():
        (RESULTS/'delay34-reset-build-and-run.json').write_text(json.dumps(logs,indent=2)+'\n')
        (RESULTS/'delay34-reset.json').write_text(json.dumps(result,indent=2)+'\n')
    def run(command,cwd,input=None,timeout=30,allowed_codes=(0,)):
        tick=time.monotonic()
        p=subprocess.run(command,cwd=cwd,input=input,text=True,capture_output=True,timeout=timeout)
        logs.append({'command':command,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'elapsed_seconds':time.monotonic()-tick})
        checkpoint()
        if p.returncode not in allowed_codes:p.check_returncode()
        return p
    with tempfile.TemporaryDirectory(prefix='delay34-new-build-',dir=RESULTS)as tmp:
        build=Path(tmp)
        with tarfile.open(SOURCES/'mmix-20250620.tar.gz')as archive:
            for name in ['Makefile','mmixal.w','mmix-arith.w','mmix-io.w','mmix-sim.w','abstime.w','boilerplate.w']:
                (build/name).write_bytes(archive.extractfile(name).read())
        run(['make','basic','CFLAGS=-O0'],build)
        for delta in ([args.delta]if args.delta is not None else[18,17]):
            name=f'delay34-delta{delta}'
            source=original.replace('GREG    18','GREG    '+str(delta),1)
            (build/(name+'.mms')).write_text(source)
            run([str(build/'mmixal'),'-b250','-o',name+'.mmo','-l',name+'.lst',name+'.mms'],build)
            (RESULTS/(name+'-listing.txt')).write_text((build/(name+'.lst')).read_text())
            # Debugger q terminates the simulator with live$255 as process status.
            # Neither the source Returned label nor a program Halt is reached.
            p=run([str(build/'mmix'),'-q','-i','-P',name+'.mmo'],build,input=commands,timeout=5,
                  allowed_codes=(2 if delta==18 else 1,))
            (RESULTS/(name+'-trace.txt')).write_text(p.stdout)
            result['runs'][str(delta)]={'source_sha256':hashlib.sha256(source.encode()).hexdigest(),
                'object_sha256':hashlib.sha256((build/(name+'.mmo')).read_bytes()).hexdigest(),
                'trace':f'results/{name}-trace.txt','listing':f'results/{name}-listing.txt',
                'process_returncode_from_debugger_quit':p.returncode}
            checkpoint()
    result['elapsed_seconds']=time.monotonic()-start;checkpoint()
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()

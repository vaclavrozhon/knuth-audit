#!/usr/bin/env python3
"""First native runs of two new MMIX programs, never the old MIX/census checks.

The new51-row output is checked by the previously proved shifted-epact/absolute
day formula. The12-candidate search uses the accepted old first-year result.
Both nominal costs are derived separately from all branch paths.
"""
from pathlib import Path
from collections import Counter
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import tarfile
import tempfile
import time

BASE=Path(__file__).resolve().parent
SOURCES=BASE/'sources'; RESULTS=BASE/'results'

def reference_row(y):
    # Dershowitz--Reingold1990,p920; accepted proof: vol1/mixal-easter.md.
    c=y//100+1
    shifted=(14+11*(y%19)-(3*c)//4+(5+8*c)//25+30*c)%30
    adj=shifted+int(shifted==0 or shifted==1 and y%19>10)
    march0=365*y-306+y//4-y//100+y//400
    moon=march0+50-adj
    date=moon+7-(moon+7)%7-march0
    line=f'{date if date<=31 else date-31:02} '+('MARCH' if date<=31 else 'APRIL')+f', {y:05}\n'
    # E0=(shifted-6)mod30 is proved independently of the MMIX source.
    e=(shifted-6)%30; g=y%19+1
    extra=int(e==24)+6*int(e==25 and g<=11)+5*int(e==25 and g>11)+3*int(e>=24)
    return {'year':y,'march_day':date,'E0':e,'G':g,'core_oops':361+extra,'line':line}

def main():
    assert os.getpriority(os.PRIO_PROCESS,0)>=15,'Use nice -n15.'
    start=time.monotonic();logs=[]
    reference=BASE.parent/'vol1/results/mixal-easter.json'
    old=json.loads(reference.read_text())
    assert old['first_wrong_year']==10317 and len(old['near_misses'])==11
    rows=[reference_row(y)for y in range(1950,2001)]
    expected={'easter32-table':''.join(r['line']for r in rows),
              'easter33-search':str(old['first_wrong_year'])+'\n'}
    expected_cost={'easter32-table':(459,sum(r['core_oops']for r in rows)+22143),
                   'easter33-search':(5,11*365+361+12*366+529)}
    core32=(SOURCES/'easter32-table.mms').read_text().split('EasterCore DIV',1)[1]
    core33=(SOURCES/'easter33-search.mms').read_text().split('EasterCore DIV',1)[1]
    assert core32==core33
    result={'checked_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'scope':'First native executions of two new complete MMIX programs.51 independent reference cells and12 analytically filtered search candidates; no old MIX/census checker rerun.',
            'reference':'workstreams/vol1/results/mixal-easter.json',
            'reference_sha256':hashlib.sha256(reference.read_bytes()).hexdigest(),
            'shared_core_sha256':hashlib.sha256(core32.encode()).hexdigest(),
            'table_rows':rows,'table_core_cost_counts':dict(Counter(r['core_oops']for r in rows)),
            'search_candidates':old['near_misses']+[old['first_wrong_year']],
            'runs':{}}
    def checkpoint():
        (RESULTS/'easter32-33-build-and-run.json').write_text(json.dumps(logs,indent=2)+'\n')
        (RESULTS/'easter32-33-programs.json').write_text(json.dumps(result,indent=2)+'\n')
    def run(command,cwd,timeout=30):
        tick=time.monotonic()
        p=subprocess.run(command,cwd=cwd,text=True,capture_output=True,timeout=timeout)
        logs.append({'command':command,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'elapsed_seconds':time.monotonic()-tick})
        checkpoint();p.check_returncode();return p
    with tempfile.TemporaryDirectory(prefix='easter32-33-new-build-',dir=RESULTS)as tmp:
        build=Path(tmp)
        with tarfile.open(SOURCES/'mmix-20250620.tar.gz')as archive:
            for name in ['Makefile','mmixal.w','mmix-arith.w','mmix-io.w','mmix-sim.w','abstime.w','boilerplate.w']:
                (build/name).write_bytes(archive.extractfile(name).read())
        run(['make','basic','CFLAGS=-O0'],build)
        for name in expected:
            source=SOURCES/(name+'.mms');shutil.copyfile(source,build/source.name)
            run([str(build/'mmixal'),'-b250','-o',name+'.mmo','-l',name+'.lst',source.name],build)
            (RESULTS/(name+'-listing.txt')).write_text((build/(name+'.lst')).read_text())
            p=run([str(build/'mmix'),'-q','-P',name+'.mmo'],build,timeout=10)
            (RESULTS/(name+'-profile.txt')).write_text(p.stdout)
            assert p.stdout.startswith(expected[name]),name
            (RESULTS/(name+'-output.txt')).write_text(expected[name])
            stats=re.findall(r'(\d+) instructions?, (\d+) mems?, (\d+) oops?;',p.stdout)
            assert len(stats)==1
            instructions,mems,oops=map(int,stats[0])
            result['runs'][name]={'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                'object_sha256':hashlib.sha256((build/(name+'.mmo')).read_bytes()).hexdigest(),
                'every_output_byte_agrees':True,'output_bytes':len(expected[name]),
                'instructions':instructions,'mems':mems,'oops':oops,
                'expected_mems':expected_cost[name][0],'expected_oops':expected_cost[name][1]}
            checkpoint();assert(mems,oops)==expected_cost[name],(name,mems,oops,expected_cost[name])
    result['elapsed_seconds']=time.monotonic()-start;checkpoint()
    print(json.dumps({'runs':result['runs'],'table_core_cost_counts':result['table_core_cost_counts'],
                      'elapsed_seconds':result['elapsed_seconds']},indent=2))

if __name__=='__main__':main()

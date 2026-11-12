#!/usr/bin/env python3
"""First executions of two new witnesses for the exercise10 SAVE claim.

This does not repeat any existing SAVE/UNSAVE inverse test or printed simulator.
"""
from pathlib import Path
import datetime,hashlib,json,os,re,shutil,subprocess,tarfile,tempfile,time
BASE=Path(__file__).resolve().parent
def main():
    assert os.getpriority(os.PRIO_PROCESS,0)>=15,'Use nice -n15.'
    results=BASE/'results';sources=BASE/'sources';logs=[];start=time.monotonic()
    result=dict(checked_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='First runs of two four-instruction witnesses for the book register-equivalence claim. No existing SAVE inverse test is rerun.',runs={})
    def checkpoint():
        (results/'register-permutation-save-build-and-run.json').write_text(json.dumps(logs,indent=2)+'\n')
        (results/'register-permutation-save.json').write_text(json.dumps(result,indent=2)+'\n')
    def run(command,cwd,expected_returncode=0):
        tick=time.monotonic();p=subprocess.run(command,cwd=cwd,text=True,capture_output=True,timeout=20)
        logs.append(dict(command=command,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr,elapsed_seconds=time.monotonic()-tick));checkpoint()
        assert p.returncode==expected_returncode,logs[-1]
        return p
    with tempfile.TemporaryDirectory(prefix='register-permutation-first-',dir=results)as tmp:
        build=Path(tmp)
        with tarfile.open(sources/'mmix-20250620.tar.gz')as archive:
            for name in ['Makefile','mmixal.w','mmix-arith.w','mmix-io.w','mmix-sim.w','abstime.w','boilerplate.w']:
                (build/name).write_bytes(archive.extractfile(name).read())
        run(['make','basic','CFLAGS=-O0'],build)
        for name,expected in [('local',0),('global',5)]:
            source=sources/('register-permutation-'+name+'.mms');shutil.copyfile(source,build/source.name)
            run([str(build/'mmixal'),'-b250','-l',name+'.lst','-o',name+'.mmo',source.name],build)
            (results/('register-permutation-'+name+'-listing.txt')).write_text((build/(name+'.lst')).read_text())
            p=run([str(build/'mmix'),'-q','-P',name+'.mmo'],build,expected_returncode=expected)
            (results/('register-permutation-'+name+'-profile.txt')).write_text(p.stdout)
            stats=re.findall(r'(\d+) instructions?, (\d+) mems?, (\d+) oops?;',p.stdout);assert len(stats)==1
            ins,mems,oops=map(int,stats[0])
            result['runs'][name]=dict(expected_exit_status=expected,exit_status=p.returncode,instructions=ins,mems=mems,oops=oops,initial_G=254,initial_L=2,SAVE_destination=255,source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),object_sha256=hashlib.sha256((build/(name+'.mmo')).read_bytes()).hexdigest())
            checkpoint();assert ins==4
    result['elapsed_seconds']=time.monotonic()-start;checkpoint();print(json.dumps(result,indent=2))
if __name__=='__main__':main()

#!/usr/bin/env python3
"""Build archived unmodified DLX1 and an explicit first-item adaptation."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import tempfile

ROOT=Path(__file__).resolve().parent


def main():
    source=ROOT/'sources/knuth-programs'
    build=Path(tempfile.mkdtemp(prefix='knuth-vol4b-dlx1-'))
    files={name:source/name for name in ['dlx1.w','gb_flip.w','gb_flip.ch','boilerplate.w']}
    files['dlx1-nomrv.ch']=ROOT/'dlx1-nomrv.ch'
    for name,path in files.items():shutil.copy2(path,build/name)
    commands=[['ctangle','gb_flip.w','gb_flip.ch'],['ctangle','dlx1.w'],
              ['cc','-O2','-Wno-implicit-int','-Wno-implicit-function-declaration','dlx1.c','gb_flip.c','-o','dlx1'],
              ['ctangle','dlx1.w','dlx1-nomrv.ch','dlx1-nomrv.c'],
              ['cc','-O2','-Wno-implicit-int','-Wno-implicit-function-declaration','dlx1-nomrv.c','gb_flip.c','-o','dlx1-nomrv']]
    out=ROOT/'results/dancing_links';out.mkdir(exist_ok=True)
    with (out/'dlx1-build.log').open('w') as log:
        for command in commands:subprocess.run(command,cwd=build,stdout=log,stderr=subprocess.STDOUT,check=True)
    metadata=dict(status='built',built_at_utc=datetime.now(timezone.utc).isoformat(),
        build_directory=str(build),commands=commands,
        sources={name:dict(path=str(path.relative_to(ROOT)),sha256=hashlib.sha256(path.read_bytes()).hexdigest()) for name,path in files.items()},
        binaries={name:dict(path=str(build/name),sha256=hashlib.sha256((build/name).read_bytes()).hexdigest()) for name in ['dlx1','dlx1-nomrv']},
        scope='dlx1 is unmodified author code; dlx1-nomrv changes only branch selection and is an audit adaptation, not an archived original author variant.')
    (out/'dlx1-build.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps(metadata,indent=2))


if __name__=='__main__':main()

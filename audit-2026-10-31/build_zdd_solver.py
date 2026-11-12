"""Rebuild the archived DLX6 and GraphBase support in a fresh directory."""
from pathlib import Path
import json
import shutil
import subprocess
import tempfile


def main():
    source = Path(__file__).resolve().parent / 'sources/knuth-programs'
    build = Path(tempfile.mkdtemp(prefix='knuth-vol4b-zdd-'))
    for name in ('dlx6.w', 'dlx6-small.ch', 'gb_flip.w', 'gb_flip.ch', 'boilerplate.w'):
        shutil.copy2(source / name, build / name)
    commands = [
        ['ctangle', 'gb_flip.w', 'gb_flip.ch'],
        ['ctangle', 'dlx6.w', 'dlx6-small.ch'],
        ['cc', '-O2', '-Wno-implicit-int', '-Wno-implicit-function-declaration',
         'dlx6.c', 'gb_flip.c', '-o', 'dlx6'],
    ]
    with (build / 'build.log').open('w') as log:
        for command in commands:
            subprocess.run(command, cwd=build, stdout=log, stderr=subprocess.STDOUT, check=True)
    result = {'binary': str(build / 'dlx6'), 'build_log': str(build / 'build.log'),
              'commands': commands}
    (build / 'build.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

"""Isolated CWEB implementation of the printed DLX122 modifications.

The author source is never changed. Changes are archived as a unified diff;
the original and the adapted program are built in a new temporary directory.
ASCII colors 1..9 are 49..57; y49 therefore corresponds to book v=1.
"""
from datetime import datetime, timezone
from pathlib import Path
import difflib
import json
import re
import shutil
import subprocess
import tempfile
from dlx1_audit_tools import ROOT, sha

OUT = ROOT / 'results/symmetry121_123'


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def build():
    target = OUT / 'native'
    target.mkdir(parents=True, exist_ok=True)
    manifest = target / 'build.json'
    if manifest.exists():
        result = json.loads(manifest.read_text())
        for item in result['sources'].values():
            assert sha(ROOT / item['path']) == item['sha256']
        for item in result['binaries'].values():
            assert sha(item['binary']) == item['sha256']
        assert sha(target/'builder-at-build.py') == result['builder_sha256']
        return result
    source = ROOT / 'sources/knuth-programs'
    original = (source / 'dlx2.w').read_text()
    changes = [
        ('  int prev,next; /* neighbors of this item */',
         '  int prev,next; /* neighbors of this item */\n  int cth; /* answer122: primary eligibility or secondary undo cache */'),
        ('int level; /* number of choices in current partial solution */',
         'int theta=49; /* answer122: ASCII color threshold, default color 1 */\nint level; /* number of choices in current partial solution */'),
        ("case 'v': k|=", "case 'y': k|=(sscanf(argv[j]+1,\"\"O\"d\",&theta)-1);@+break;\ncase 'v': k|="),
        ('@<Set |best_itm| to the best item for branching@>;\ncover(best_itm);',
         '@<Set |best_itm| to the best item for branching@>;\nif (best_itm==root) goto retreat;\ncover(best_itm);'),
        ('backup: uncover(best_itm);\nif (level==0) goto done;',
         'backup: uncover(best_itm);\nretreat: if (level==0) goto done;'),
        ('    if (!nd[pp].color) cover(cc);',
         '    if (nd[pp].color>theta) goto reject122;\n    if (!nd[pp].color) cover(cc);'),
        ('    else if (nd[pp].color>0) unpurify(pp);\n    pp--;',
         '    else if (nd[pp].color>0) unpurify(pp);\nreject122: pp--;'),
        ('  nd[cc].color=x; /* no mem charged, because this is for |print_option| only */',
         '  o,cl[cc].cth=theta;\n  if (x==theta) theta++;\n  nd[cc].color=x; /* no mem charged, because this is for |print_option| only */'),
        ("  o,cc=nd[p].itm,x=nd[p].color; /* there's no need to clear |nd[cc].color| */",
         "  o,cc=nd[p].itm,x=nd[p].color; /* there's no need to clear |nd[cc].color| */\n  o,theta=cl[cc].cth;"),
        ('t=max_nodes,tmems=mems;', 'best_itm=root;\nt=max_nodes,tmems=mems;'),
        ('for (o,k=cl[root].next;t&&k!=root;o,k=cl[k].next) {',
         'for (o,k=cl[root].next;t&&k!=root;o,k=cl[k].next) {\n  if (o,cl[k].cth>theta) continue;'),
    ]
    modified = original
    for old, new in changes:
        assert modified.count(old) == 1, old
        modified = modified.replace(old, new)
    diff = ''.join(difflib.unified_diff(original.splitlines(True), modified.splitlines(True),
                                       fromfile='dlx2-original.w', tofile='dlx2-symmetry122.w'))
    (target / 'dlx2-symmetry122.patch').write_text(diff)
    directory = Path(tempfile.mkdtemp(prefix='knuth-vol4b-symmetry122-native-'))
    names = ['dlx2.w', 'gb_flip.w', 'gb_flip.ch', 'boilerplate.w']
    for name in names:
        shutil.copy2(source/name, directory/name)
    commands = [['ctangle', 'gb_flip.w', 'gb_flip.ch']]
    variants = {'original': original, 'symmetry122': modified}
    for label, code in variants.items():
        name = 'dlx2-' + label
        (directory/(name+'.w')).write_text(code)
        if label != 'original':
            (target/(name+'.w')).write_text(code)
        commands.extend([['ctangle', name+'.w'],
                         ['cc', '-O2', '-Wno-implicit-int', '-Wno-implicit-function-declaration',
                          name+'.c', 'gb_flip.c', '-o', name]])
    with (target/'build.log').open('w') as log:
        for command in commands:
            subprocess.run(command, cwd=directory, stdout=log,
                           stderr=subprocess.STDOUT, check=True)
    result = dict(built_at_utc=datetime.now(timezone.utc).isoformat(),
                  builder_sha256=sha(__file__), commands=commands,
                  sources={name:dict(path=str((source/name).relative_to(ROOT)),
                                     sha256=sha(source/name)) for name in names},
                  binaries={label:dict(binary=str(directory/('dlx2-'+label)),
                                       sha256=sha(directory/('dlx2-'+label))) for label in variants},
                  patch_sha256=sha(target/'dlx2-symmetry122.patch'),
                  scope='Original DLX2 plus precisely the answer122 threshold/CTH/partial rollback changes. Every primary CTH defaults to zero. No input option reordering.')
    save(manifest, result)
    shutil.copy2(__file__, target/'builder-at-build.py')
    return result


def encode(n, primary, rows):
    names = [None] + [f'p{i}' if i <= primary else f'q{i-primary}' for i in range(1, n+1)]
    lines = [' '.join(names[1:primary+1])+' | '+' '.join(names[primary+1:])]
    for row in rows:
        lines.append(' '.join(names[i]+(':'+chr(48+c) if c else '') for i, c in row))
    return '\n'.join(lines)+'\n'


def run(label, variant, data, *, spacing=1, threshold=49):
    built = build()
    path = OUT/'native'/label
    if path.with_suffix('.json').exists():
        result = json.loads(path.with_suffix('.json').read_text())
        assert path.with_suffix('.dlx').read_text() == data
        for ext, expected in result['files'].items():
            assert sha(path.with_suffix(ext)) == expected
        return result
    assert not path.with_suffix('.stderr').exists(), f'Inspect the prior run before any restart: {label}'
    path.with_suffix('.dlx').write_text(data)
    command = [built['binaries'][variant]['binary'], 'v129', f'm{spacing}']
    if variant == 'symmetry122':
        command.append(f'y{threshold}')
    started = datetime.now(timezone.utc).isoformat()
    with path.with_suffix('.stdout').open('w') as out, path.with_suffix('.stderr').open('w') as err:
        proc = subprocess.run(command, input=data, text=True, stdout=out, stderr=err, timeout=120)
    log = path.with_suffix('.stderr').read_text()
    assert proc.returncode == 0, log
    m = re.search(r'Altogether (\d+) solutions?, (\d+)\+(\d+)-(\d+) mems, .*?, (\d+) nodes', log)
    assert m, log
    result = dict(label=label, variant=variant, command=command, started_at_utc=started,
                  finished_at_utc=datetime.now(timezone.utc).isoformat(), returncode=proc.returncode,
                  solutions=int(m[1]), input_mems=int(m[2]), search_mems=int(m[3]), unmems=int(m[4]),
                  net_search_mems=int(m[3])-int(m[4]), nodes=int(m[5]),
                  files={ext:sha(path.with_suffix(ext)) for ext in ['.dlx', '.stdout', '.stderr']},
                  binary_sha256=sha(command[0]))
    save(path.with_suffix('.json'), result)
    return result

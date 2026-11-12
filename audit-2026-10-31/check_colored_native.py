#!/usr/bin/env python3
"""Cross-check Algorithm C and the printed83 extension in the original DLX2."""
from datetime import datetime,timezone
from pathlib import Path
import json,re,shutil,subprocess,tempfile
from dlx1_audit_tools import ROOT,sha
from check_colored_basics import OUT,TOY


def build():
    target=OUT/'native';target.mkdir(parents=True,exist_ok=True)
    manifest=target/'build.json'
    if manifest.exists():
        data=json.loads(manifest.read_text())
        assert all(sha(x['binary'])==x['sha256'] for x in data['binaries'].values())
        assert all(sha(ROOT/x['path'])==x['sha256'] for x in data['sources'].values())
        return data
    directory=Path(tempfile.mkdtemp(prefix='knuth-vol4b-colored-'))
    source=ROOT/'sources/knuth-programs'
    names=['dlx2.w','gb_flip.w','gb_flip.ch','boilerplate.w']
    for name in names:shutil.copy2(source/name,directory/name)
    original=(source/'dlx2.w').read_text()
    forced=original.replace('@<Set |best_itm| to the best item for branching@>;\ncover(best_itm);',
          '@<Set |best_itm| to the best item for branching@>;\nif (level==0) best_itm=1; /* exercise83 permits choosing p first */\ncover(best_itm);')
    assert forced!=original
    needle='recover: @<Uncover all other items of |cur_node|@>;\noo,cur_node=choice[level]=nd[cur_node].down;'
    replacement='''recover: @<Uncover all other items of |cur_node|@>;
if (level==0) {
  pp=cur_node;
  while (nd[pp+1].itm>0) pp++;
  cc=nd[pp].itm;
  if (cc>=second && !nd[pp].color) cover(cc);
}
oo,cur_node=choice[level]=nd[cur_node].down;'''
    assert needle in forced
    patched=forced.replace(needle,replacement)
    variants={'original':original,'root-p':forced,'printed83':patched}
    commands=[['ctangle','gb_flip.w','gb_flip.ch']]
    for label,code in variants.items():
        name='dlx2-'+label
        (directory/(name+'.w')).write_text(code)
        if label!='original':(target/(name+'.w')).write_text(code)
        commands.extend([['ctangle',name+'.w'],['cc','-O2','-Wno-implicit-int','-Wno-implicit-function-declaration',name+'.c','gb_flip.c','-o',name]])
    with (target/'build.log').open('w') as log:
        for cmd in commands:subprocess.run(cmd,cwd=directory,stdout=log,stderr=subprocess.STDOUT,check=True)
    data=dict(built_at_utc=datetime.now(timezone.utc).isoformat(),commands=commands,
      sources={name:dict(path=str((source/name).relative_to(ROOT)),sha256=sha(source/name)) for name in names},
      binaries={label:dict(binary=str(directory/('dlx2-'+label)),sha256=sha(directory/('dlx2-'+label))) for label in variants},
      scope='Original author DLX2; two explicitly modified variants only force the allowed root item p and insert the printed83 persistent-cover instruction. No other solver changes.')
    manifest.write_text(json.dumps(data,indent=2)+'\n');return data


def run(build,label,variant,data,expected):
    path=OUT/'native'/label
    path.with_suffix('.dlx').write_text(data)
    cmd=[build['binaries'][variant]['binary'],'v3','m1']
    p=subprocess.run(cmd,input=data,text=True,capture_output=True,timeout=15)
    path.with_suffix('.stdout').write_text(p.stdout);path.with_suffix('.stderr').write_text(p.stderr)
    assert p.returncode==0,p.stderr
    m=re.search(r'Altogether (\d+) solution',p.stderr);assert m,p.stderr
    assert int(m[1])==expected,(label,p.stderr)
    return dict(label=label,variant=variant,solutions=int(m[1]),command=cmd,
                files={ext:sha(path.with_suffix(ext)) for ext in ['.dlx','.stdout','.stderr']})


def main():
    build_data=build()
    toy='p q r | x y\np q x y:A\np r x:A y\np x:B\nq x:A\nr y:B\n'
    overlap='p q | a b c\np a\np a b\np c\nq a\n'
    expanded='p q | a b c\np a\np a b\np a b c\nq a\n'
    disjoint='p q | a b c\np a\np b\np c\nq a\n'
    results=[run(build_data,'toy','original',toy,1),run(build_data,'overlap-normal','root-p',overlap,1),
      run(build_data,'overlap-printed83','printed83',overlap,1),run(build_data,'overlap-expanded','root-p',expanded,0),
      run(build_data,'disjoint-printed83','printed83',disjoint,0)]
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),source_sha256=sha(__file__),cases=results,
      conclusion='The independent original DLX2, with only the stated83 extension and forced allowed root choice, returns p c + q a, forbidden by the earlier-a condition. Its explicit expanded problem is UNSAT. The normal disjoint-marker case correctly yields UNSAT.')
    (OUT/'native-check.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS:five nativeDLX2 checks; F123 reproduced independently')


if __name__=='__main__':main()

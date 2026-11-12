"""Small new checks: printed matrices179 and zero-row preprocessing boundary.

Accepted175–178 coefficient calculations are read, never rerun.
"""
from collections import defaultdict
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import json
import re
import subprocess
import time
import xml.etree.ElementTree as ET
from extract_jigsaw import transform
from puzzle_xcc import save, sha

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'results/mcc175_179'


def matrix(path, bounds, shape):
    x0,x1,y0,y1 = bounds
    rows = defaultdict(list)
    for text in ET.parse(path).getroot().find('page'):
        if text.tag != 'fill_text':
            continue
        for span in text:
            for g in span:
                if g.get('unicode') not in ('0','1'):
                    continue
                x,y = transform(text,float(g.get('x')),float(g.get('y')))
                if x0 < x < x1 and y0 < y < y1:
                    rows[round(y,2)].append((x,int(g.get('unicode'))))
    result = [[v for _,v in sorted(row)] for _,row in sorted(rows.items())]
    assert len(result) == shape[0] and all(len(row) == shape[1] for row in result)
    return result


def covers(a):
    return [tuple(i for i in range(len(a)) if mask>>i&1)
            for mask in range(1<<len(a))
            if all(sum(row[j] for i,row in enumerate(a) if mask>>i&1) == 1 for j in range(len(a[0])))]


def native(name, text, expected):
    paths = [OUT/(name+s) for s in ['.mcc','.log','.out']]
    if all(p.exists() for p in paths):
        # Reuse completed development outputs; changing a reporting assertion
        # is not a reason to rerun successful solver checks.
        assert paths[0].read_text() == text
        match = re.search(r'Altogether (\d+) solution',paths[1].read_text())
        assert match and int(match[1]) == expected
        return dict(name=name,solutions=expected,wall_seconds=None,reused_completed_development_output=True,
                    input_sha256=sha(paths[0]),log_sha256=sha(paths[1]),output_sha256=sha(paths[2]))
    assert not any(p.exists() for p in paths)
    start = time.monotonic()
    p = subprocess.run(['/tmp/knuth-dlx3','v1','d0','m1'],input=text,text=True,capture_output=True,timeout=10)
    assert p.returncode == 0,p.stderr
    match = re.search(r'Altogether (\d+) solution',p.stderr)
    assert match and int(match[1]) == expected,(name,p.stderr)
    (OUT/(name+'.mcc')).write_text(text)
    (OUT/(name+'.log')).write_text(p.stderr)
    (OUT/(name+'.out')).write_text(p.stdout)
    return dict(name=name,solutions=expected,wall_seconds=time.monotonic()-start,input_sha256=sha(OUT/(name+'.mcc')))


def main():
    assert not (OUT/'source-checked.json').exists()
    matrices = {}
    for version,page,bounds in [('original',167,[(135,212,90,170),(275,325,100,160)]),
                                ('draft',89,[(158,232,199,279),(297,343,209,269)])]:
        path = OUT/(version+'-'+str(page)+'.xml')
        matrices[version] = [matrix(path,b,shape) for b,shape in zip(bounds,[(9,6),(7,4)])]
    assert matrices['original'] == matrices['draft']
    a,b = matrices['original']
    assert a == [list(map(int,s)) for s in ['100000','011100','110111','011100','000011','000011','101000','010111','111100']]
    assert b == [list(map(int,s)) for s in ['1000','0110','1101','0001','1010','0101','1110']]
    columns = [tuple(row[j] for row in a) for j in range(6)]
    kept_columns = [j for j in range(6) if columns[j] not in columns[:j]]
    assert kept_columns == [0,1,2,4]
    compressed = [tuple(row[j] for j in kept_columns) for row in a]
    unique = list(dict.fromkeys(compressed))
    assert unique == list(map(tuple,b))
    classes = [[i for i,row in enumerate(compressed) if row == value] for value in unique]
    small,large = covers(b),covers(a)
    assert set(small) == {(0,1,3),(3,6),(4,5)} and len(large) == 7
    lifts = {','.join(map(str,c)): sorted(tuple(sorted(q)) for q in product(*(classes[i] for i in c))) for c in small}
    assert sorted(q for group in lifts.values() for q in group) == sorted(large)
    assert {k:len(v) for k,v in lifts.items()} == {'0,1,3':4,'3,6':2,'4,5':1}
    # Each pair differs only in explicit handling of one all-zero row.
    cases = [
        ('175-zero-cap1-literal','A\n\nA\n',1),
        ('175-zero-cap1-tagged','A 0:1|Z\nZ\nA\n',2),
        ('175-zero-cap2-literal','A Q | x\nx\nQ x\nQ\nA\n',2),
        ('175-zero-cap2-tagged','A Q 0:2|Z | x\nZ x\nQ x\nQ Z\nA\n',3),
        ('176-zero-literal','2|A B Q\nA B\n\nQ A\nQ B\n',1),
        ('176-zero-tagged','2|A B Q 0:1|Z\nA B\nZ\nQ A\nQ B\n',2)]
    results = [native(*case) for case in cases]
    oldpath = ROOT/'results/mcc_arithmetic/arithmetic.json'
    old = json.loads(oldpath.read_text())
    q = {(c['s'],c['t']):c['count'] for c in old['partition_cases'] if c['distinct']}
    # A tiny arithmetic certificate read from the accepted table, no new DP.
    assert (q[0,0],q[0,1],q[0,2],q[1,1],q[2,1]) == (1,1,5,3,9)
    assert 2*q[0,2] == q[2,1]+q[1,1]-q[0,0]-q[0,1] == 10
    assert q[2,1]+q[1,1]-q[0,0]-2*q[0,1] == 9
    save(OUT/'source-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),
        dependency_hashes={'extract_jigsaw.py':sha(ROOT/'extract_jigsaw.py')},
        trace_hashes={n:sha(OUT/n) for n in ['original-167.xml','draft-89.xml']},
        matrices=matrices,printed_digits_per_version=82,kept_columns_zero_based=kept_columns,
        original_row_classes_zero_based=classes,small_covers=small,large_covers=large,lifts=lifts,
        total_subsets_checked=128+512,zero_row_checks=results,native_binary_sha256=sha('/tmp/knuth-dlx3'),
        old_arithmetic_sha256=sha(oldpath),old_arithmetic_cases_rerun=0,
        f070_short_certificate=dict(s=0,t=1,left=10,right_with_t=10,right_with_arbitrary_n2=9,
                                   scope='The printed n is undefined; this illustrates that an arbitrary n does not work.')))
    print('PASS175–179:82 matrix digits per version;3 reduced/7 original covers;6 tiny zero-row checks;accepted arithmetic not rerun.')


if __name__ == '__main__':
    main()

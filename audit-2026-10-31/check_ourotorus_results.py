"""Verify complete native model sets against independent cell enumerations."""
from collections import Counter
from datetime import datetime,timezone
from itertools import product
from pathlib import Path
import gzip,hashlib,json,re
from universal_cycles import expand96,expand97,window_set

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/universal_cycles'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def native_models(label,pattern,keys):
    meta=json.loads((OUT/(label+'.json')).read_text())
    assert meta['status']=='completed' and meta['returncode']==0
    for key,suffix in [('stderr_sha256','.log'),('stdout_sha256','.out.gz'),('input_sha256','.dlx')]:
        assert meta[key]==sha(OUT/(label+suffix))
    assert meta['module_sha256']==sha(ROOT/'universal_cycles.py')
    assert meta['script_sha256']==sha(ROOT/'run_universal_native.py')
    models=set();values={};count=0
    with gzip.open(OUT/(label+'.out.gz'),'rt') as stream:
        for line in stream:
            if re.fullmatch(r'\d+:\n',line):
                if count:
                    assert set(values)==set(keys)
                    word=''.join(values[k] for k in keys);assert word not in models;models.add(word)
                count+=1;values={}
            else:
                for item,color in re.findall(pattern,line):
                    assert item not in values or values[item]==color
                    values[item]=color
    if count:
        assert set(values)==set(keys)
        word=''.join(values[k] for k in keys);assert word not in models;models.add(word)
    assert len(models)==count==meta['solutions']
    return models


def main():
    b94=native_models('native94',r'(x\d+):([01])',[f'x{i}' for i in range(16)])
    assert b94==set((OUT/'binary94-models.txt').read_text().splitlines())
    result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(),
                script_sha256=sha(Path(__file__)),native94_complete_set_equal=True)
    for exercise,h,w,radix,window_width in [(96,4,8,2,3),(97,3,9,3,2)]:
        keys=[f'd{r}.{c}' for r in range(h) for c in range(w)]
        models=native_models(f'native{exercise}',r'(d\d+\.\d+):([012])',keys)
        cell=json.loads((OUT/f'cell{exercise}.json').read_text())
        assert cell['status']=='completed' and cell['returncode']==0
        path=OUT/f'cell{exercise}-models.txt'
        assert cell['models_sha256']==sha(path)
        assert cell['source_sha256']==sha(ROOT/'enumerate_ourotorus.cpp')
        assert cell['script_sha256']==sha(ROOT/'run_ourotorus_cells.py')
        zero=path.read_text().splitlines();assert len(set(zero))==len(zero)==cell['solutions']
        independent=set(zero) if exercise==96 else {
            ''.join(str((int(c)+a)%3) for c in word) for a in range(3) for word in zero}
        assert models==independent
        expander=expand96 if exercise==96 else expand97
        expected=set(product(range(radix),repeat=2*window_width))
        transpose_fixed=0;translations=set()
        for word in models:
            board=expander(word)
            assert window_set(board,2,window_width)==expected
            size=len(board)
            if exercise==97:
                assert all(board[(r+3)%9][(c+3)%9]==(board[r][c]+1)%3 for r,c in product(range(9),repeat=2))
                transposed=''.join(str(board[c][r]) for r in range(3) for c in range(9))
                assert transposed in models
                transpose_fixed+=transposed==word
                # Adding 1 is translation by (3,3), and leaves the type at00.
                assert all(board[(r+3)%9][(c+3)%9]==(int(word[9*r+c])+1)%3
                           for r in range(3) for c in range(9))
            if exercise==96:
                for r,c in product(range(size),range(w)):
                    translations.add(''.join(str(board[(r+i)%size][(c+j)%w])
                                             for i in range(h) for j in range(w)))
        if exercise==96:
            assert len(models)==80 and len(translations)==5120
            printed=['00000110','00010111','11001010','10001110',
                     '11111001','11101000','00110101','01110001']
            assert expand96(''.join(printed[:4]))==[list(map(int,row)) for row in printed]
            assert ''.join(printed[:4]) in models
        else:
            assert len(models)==17388 and len(zero)==5796 and transpose_fixed==0
            assert Counter(word[0] for word in models)=={'0':5796,'1':5796,'2':5796}
            # No nontrivial translation fixes an ourotorus: its 2x2 windows
            # are unique. The27 normalized types remove27 choices of origin;
            # the remaining translations(0,0),(3,3),(6,6) cycle the base color.
        result[f'torus{exercise}']=dict(native_models=len(models),cell_models_base_zero=len(zero),
            complete_sets_equal=True,all_windows_checked=True,
            normalized_translation_classes=len(zero),
            labelled_matrices=5120 if exercise==96 else 27*len(models),
            transpose_fixed=transpose_fixed if exercise==97 else None,
            cell_nodes=cell['nodes'],model_set_sha256=hashlib.sha256(('\n'.join(sorted(models))+'\n').encode()).hexdigest())
        (OUT/f'torus{exercise}-models.txt').write_text('\n'.join(sorted(models))+'\n')
    (OUT/'tori-checked.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))


if __name__=='__main__':main()

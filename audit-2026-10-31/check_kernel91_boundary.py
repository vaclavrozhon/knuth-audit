"""The eight-distinct local projection loses the shortest left WORDS(136) stair."""
import hashlib,json,subprocess
from pathlib import Path
from double_word_tools import dictionary,input_text,validate,down_words
from word_kernel91 import literal_encoding,stair_kernels,DistinctWitness

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/stair_kernels'
words=dictionary(5)[:136];rows=['WRITE','WHOLE'];assert validate(rows,words,'left')==136
binary=json.loads((ROOT/'results/colored_basics/native/build.json').read_text())['binaries']['original']
assert hashlib.sha256(Path(binary['binary']).read_bytes()).hexdigest()==binary['sha256']
checks=[]
for index,kernel in enumerate(stair_kernels(rows,'left')):
    assert DistinctWitness(words,'left').witness(kernel) is None
    enc=literal_encoding(words,'left',True)
    enc['rows']=[row for row in enc['rows'] if all(not 9<=item<=22 or chr(color)==kernel[item-9] for item,color in row)]
    prefix=OUT/f'left136-boundary-{index}';inp=prefix.with_suffix('.dlx');inp.write_text(input_text(enc))
    run=subprocess.run([binary['binary'],'v129','m1'],input=inp.read_bytes(),capture_output=True,check=True,timeout=30)
    assert 'Altogether 0 solutions' in run.stderr.decode()
    prefix.with_suffix('.out').write_bytes(run.stdout);prefix.with_suffix('.log').write_bytes(run.stderr)
    checks.append(dict(kernel=kernel,options=len(enc['rows']),native_solutions=0,input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest()))
result=dict(rows=rows,down=down_words(rows,'left'),rank=136,checks=checks,
    native_binary_sha256=binary['sha256'],source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    interpretation='The all-eight-distinct model implicit in the numerical examples needs a p>=4 restriction, or a separate short-period branch. Literal membership-only kernels have no such restriction.')
(OUT/'left136-boundary.json').write_text(json.dumps(result,indent=2)+'\n');print(result)

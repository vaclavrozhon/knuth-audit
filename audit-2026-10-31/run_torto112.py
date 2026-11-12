"""Single sequential queue of original TORTO-DLX cases; no implicit restarts."""
from datetime import datetime,timezone
from pathlib import Path
import fcntl,gzip,json,os,re,shutil,subprocess,tempfile
from layout_native import ROOT,OUT,save,sha,run
from torto112 import canonical,validate_path,paths

CASES=[
    ('torto112-dancing','DANCING LINKS TORTO WORDS SOLVER'.split(),10),
    ('torto112-programming','PROGRAMMING COMPUTER THE ART OF'.split(),1444),
    ('torto112-one-ten','THREE ONE TWO FOUR FIVE SIX SEVEN EIGHT NINE TEN'.split(),416),
    ('torto112-zero-eight','THREE ZERO ONE TWO FOUR FIVE SIX SEVEN EIGHT'.split(),553),
    ('torto112-ordinals','SECOND FIRST THIRD FOURTH FIFTH SIXTH'.split(),72853)
]


def build():
    directory=Path(tempfile.mkdtemp(prefix='knuth-vol4b-torto-',dir='/tmp'))
    source=ROOT/'sources/layouts108_114/torto-dlx.w';shutil.copy2(source,directory/'torto-dlx.w')
    records=[]
    for command in [['ctangle','torto-dlx.w'],['gcc','-O2','-std=gnu99','-Wno-implicit-int','torto-dlx.c','-o','torto-dlx']]:
        p=subprocess.run(command,cwd=directory,capture_output=True,text=True)
        records.append(dict(command=command,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,p.stderr
    binary=directory/'torto-dlx'
    save(OUT/'torto-build.json',dict(commands=records,source_sha256=sha(source),binary=str(binary),binary_sha256=sha(binary)))
    return binary


def models(label):
    current=None
    with gzip.open(OUT/(label+'.out.gz'),'rt') as stream:
        for line in stream:
            if re.fullmatch(r'\d+:\s*',line):
                if current is not None:yield current
                current=[]
            elif line.strip():
                assert current is not None
                current.extend(re.sub(r'\s*\(\d+ of \d+\)\s*$','',line).split())
    if current is not None:yield current


def decode_number(c):
    return '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c)


def validate(label,words,expected):
    classes=set();boards=set();count=0;examples=[]
    for tokens in models(label):
        board=['.']*18;positions={}
        for token in tokens:
            if ':' not in token:continue
            name,color=token.split(':')
            if len(name)==1 and 'a'<=name<='r':
                u=ord(name)-ord('a');assert board[u] in ['.',color];board[u]=color
            elif '>' in name:
                a,b=name.split('>');key=(decode_number(a),decode_number(b));u=decode_number(color)-10
                assert key not in positions or positions[key]==u;positions[key]=u
        board=''.join(board);seen=set();allpaths=[]
        for k,word in enumerate(words):
            path=tuple(positions[k,l] for l in range(len(word)))
            validate_path(board,word,path);seen.update(path);allpaths.append(path)
        assert seen=={u for u,c in enumerate(board) if c!='.'}
        count+=1;boards.add(board);classes.add(canonical(board))
        if len(examples)<8:examples.append(dict(board=board,paths=allpaths))
    terminal=json.loads((OUT/(label+'.json')).read_text())
    assert count==terminal['solutions']
    result=dict(script_sha256=sha(__file__),validator_sha256=sha(ROOT/'torto112.py'),
                words=words,native_path_models=count,distinct_boards=len(boards),
                reflection_classes=len(classes),printed_or_corrected_claim=expected,
                count_matches_claim=len(classes)==expected,canonical_boards=sorted(classes),
                every_selected_path_geometrically_valid=True,examples=examples)
    if label=='torto112-one-ten':
        extensions={b:paths(b,'ELEVEN',wild=True) for b in classes}
        result['eleven_extension_paths']=sum(map(len,extensions.values()))
        result['unused_cells_histogram']={str(k):sum(b.count('.')==k for b in classes) for k in range(19) if any(b.count('.')==k for b in classes)}
    save(OUT/(label+'-checked.json'),result)
    print(label,'models',count,'classes',len(classes),'book',expected,flush=True)


def main():
    lock=(OUT/'torto-queue.lock').open('w');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    assert not (OUT/'torto-queue.json').exists(),'Inspect the existing queue before continuing.'
    binary=build()
    queue=dict(status='running',wrapper_pid=os.getpid(),started_utc=datetime.now(timezone.utc).isoformat(),
               cases=[x[0] for x in CASES],done=[],script_sha256=sha(__file__),timeout_seconds_per_case=172800)
    save(OUT/'torto-queue.json',queue)
    for label,words,expected in CASES:
        queue['current']=label;save(OUT/'torto-queue.json',queue)
        command=[str(binary),*words];p=subprocess.run(command,capture_output=True,text=True)
        save(OUT/(label+'-generation.json'),dict(command=command,returncode=p.returncode,stderr=p.stderr,
             source_sha256=sha(ROOT/'sources/layouts108_114/torto-dlx.w'),generator_sha256=sha(binary)))
        assert p.returncode==0,p.stderr
        result=run(label,p.stdout)
        assert result['status']=='completed',result
        validate(label,words,expected)
        queue['done'].append(label);save(OUT/'torto-queue.json',queue)
    queue.update(status='completed',finished_utc=datetime.now(timezone.utc).isoformat());save(OUT/'torto-queue.json',queue)


if __name__=='__main__':main()

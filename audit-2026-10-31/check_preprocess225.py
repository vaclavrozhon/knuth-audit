"""Independent bit-set replay of all new reductions, without solving any cover."""
from collections import Counter,defaultdict
from datetime import datetime,timezone
from pathlib import Path
import json,os,re,time
from prepare_pentomino_main import connected_components
from verify_f146 import verify as verify_f146
from puzzle_xcc import save,sha

ROOT=Path(__file__).resolve().parent;OUT=ROOT/'results/preprocess225'


def option(line):
    d={}
    for s in line.split():
        i,sep,c=s.partition(':');assert i not in d;d[i]=c if sep else None
    return d


def parse(text,output=False):
    lines=[s.strip() for s in text.splitlines() if s.strip()];header=lines[0].split()
    primary=header[:header.index('|')] if '|' in header else header
    names=[s for s in header if s!='|'];rows={};pending=None
    for s in lines[1:]:
        if s.startswith('|'):
            if output:
                m=re.fullmatch(r'\| \(from (\d+)\)',s)
                if m:assert pending is not None;rows[int(m[1])]=pending;pending=None
            continue
        row=option(s)
        if output:assert pending is None;pending=row
        else:rows[len(rows)+1]=row
    assert pending is None
    return set(primary),set(names),rows


class Replay:
    def __init__(self,primary,names,rows):
        self.primary=set(primary);self.names=set(names);self.rows={r:dict(o) for r,o in rows.items()}
        self.col={i:0 for i in names};self.colors={i:defaultdict(int) for i in names};self.active=0
        for r,o in rows.items():
            bit=1<<(r-1);self.active|=bit
            for i,c in o.items():self.col[i]|=bit;self.colors[i][c]|=bit

    def compatible(self,row):
        conflict=0
        for i,c in row.items():conflict|=self.col[i] if c is None else self.col[i]&~self.colors[i][c]
        return self.active&~conflict

    def remove(self,r):
        bit=1<<(r-1);o=self.rows.pop(r);self.active&=~bit
        for i,c in o.items():self.col[i]&=~bit;self.colors[i][c]&=~bit

    def forced_by(self,i):
        return sorted(p for p in self.primary-{i} if self.col[p] and not self.col[p]&~self.colors[i][None])

    def force(self,i,p):
        assert p in self.forced_by(i),(i,p)
        for r in list(self.rows):
            o=self.rows[r]
            if i in o:
                if p not in o:self.remove(r)
                else:assert o[i] is None;del o[i]
        self.names.remove(i);self.primary.discard(i);del self.col[i];del self.colors[i]


def replay(label):
    primary,names,rows=parse((OUT/(label+'.xcc')).read_text());r=Replay(primary,names,rows);events=[];roundno=None
    for line in (OUT/(label+'.log')).read_text().splitlines():
        m=re.fullmatch(r'Beginning round (\d+):',line)
        if m:roundno=int(m[1]);continue
        m=re.fullmatch(r' (\S+) blocked by (.*) \(option (\d+)\)',line)
        if m:
            p,body,rid=m[1],m[2],int(m[3]);assert r.rows[rid]==option(body)
            assert p in r.primary and p not in r.rows[rid]
            assert not r.col[p]&r.compatible(r.rows[rid]),(label,roundno,rid,p)
            events.append(dict(kind='block',round=roundno,row=rid,blocked=p));r.remove(rid);continue
        m=re.fullmatch(r'Deleting item (\S+), forced by (\S+)',line)
        if m:
            i,p=m.groups();witnesses=r.forced_by(i);assert p in witnesses
            events.append(dict(kind='force',round=roundno,item=i,primary=p,all_primary_witnesses=witnesses));r.force(i,p)
    op,on,orr=parse((OUT/(label+'.out')).read_text(),True)
    assert orr==r.rows,(label,len(orr),len(r.rows))
    assert op=={p for p in r.primary if r.col[p]} and on=={p for p in r.names if r.col[p]}
    assert all(any(p in row for p in op) for row in orr.values())
    return dict(input_options=len(rows),output_options=len(orr),primary_before=len(primary),primary_after=len(op),secondary_before=len(names-primary),secondary_after=len(on-op),events=events),rows,orr


def synchronous_closure(primary,names,rows):
    """No source order or native trace: remove all currently blocked rows together."""
    r=Replay(primary,names,rows);passes=[]
    while True:
        blocked=[]
        for k,row in r.rows.items():
            compatible=r.compatible(row)
            if any(not r.col[p]&compatible for p in primary-row.keys()):blocked.append(k)
        passes.append(len(blocked))
        if not blocked:break
        for k in blocked:r.remove(k)
    return r.rows,passes


def main():
    assert os.nice(0)>=15 and not (OUT/'verified.json').exists();start=time.monotonic()
    runs=json.loads((OUT/'runs.json').read_text());build=json.loads((OUT/'build.json').read_text())
    assert runs['runner_sha256']==sha(ROOT/'run_preprocess225.py') and sha(build['binary'])==build['binary_sha256']==runs['binary_sha256']
    assert sha(build['source'])==build['source_sha256'];reports={};cases={};files=[]
    for q in runs['runs']:
        assert q['status']=='completed' and q['returncode']==0;label=q['label']
        for suffix,key in [('.xcc','input_sha256'),('.out','stdout_sha256'),('.log','stderr_sha256')]:
            p=OUT/(label+suffix);assert sha(p)==q[key];files.append(p)
        report,rows,reduced=replay(label);reports[label]=report;cases[label]=(rows,reduced)
        if label.startswith('pentomino'):
            primary,names,_=parse((OUT/(label+'.xcc')).read_text());closure,passes=synchronous_closure(primary,names,rows)
            assert closure==reduced;report['independent_synchronous_closure']=dict(passes=passes,identical_rows=True)
            assert not any(e['kind']=='force' for e in report['events'])
    assert reports['pentomino-6x10']['output_options']==1797
    assert reports['pentomino-6x15']['output_options']==3157
    assert reports['macmahon126']['input_options']==1537 and reports['macmahon126']['output_options']==961
    s=reports['sudoku114-original'];assert (s['input_options'],s['output_options'],s['primary_before'],s['primary_after'],s['secondary_after'])==(5410,2426,585,506,90)
    # MacMahon's forced border row already removes exactly these576 rows at
    # the first search level. No replay of its millions of full solutions.
    original,reduced=cases['macmahon126'];star=[r for r in original if '*' in original[r]];assert len(star)==1
    p,n,_=parse((OUT/'macmahon126.xcc').read_text());r=Replay(p,n,original);good=r.compatible(original[star[0]])|(1<<(star[0]-1))
    assert set(reduced)=={k for k in original if good>>(k-1)&1}
    examples={}
    for label,w in [('pentomino-6x10',10),('pentomino-6x15',15)]:
        original,reduced=cases[label];small=Counter();corner_o=[];primary,names,_=parse((OUT/(label+'.xcc')).read_text());r=Replay(primary,names,original)
        for rid,row in original.items():
            piece=next(i for i in row if len(i)==1);cells={int(s[0],16)*w+int(s[1],16) for s in row if len(s)==2}
            if any(len(c)<5 for c in connected_components(set(range(6*w))-cells,6,w)):small[piece.upper()]+=1
            if piece=='O':
                corners=['00','0'+format(w-1,'x'),'50','5'+format(w-1,'x')]
                blocked=[p for p in corners if p not in row and not r.col[p]&r.compatible(row)]
                if blocked:corner_o.append(dict(row=rid,blocked=blocked))
        assert len(corner_o)==8
        examples[label]=dict(component_smaller_than_five_by_piece=dict(small),corner_blocking_O=corner_o,
            blocking_primary_histogram=dict(Counter(e['blocked'] for e in reports[label]['events'] if e['kind']=='block')))
    a=examples['pentomino-6x10']['component_smaller_than_five_by_piece'];b=examples['pentomino-6x15']['component_smaller_than_five_by_piece']
    assert {p for p in a.keys()|b.keys() if a.get(p,0)!=b.get(p,0)}=={'U'} and b['U']>a['U']
    assert examples['pentomino-6x15']['blocking_primary_histogram'].get('X',0)==0
    original,reduced=cases['pentomino-6x10'];find=lambda s:next(k for k,v in original.items() if set(v)==set(s.split()))
    ridP=find('P 02 12 13 22 23');ridO=find('O 22 23 24 25 26')
    assert any(e['row']==ridP and e['blocked']=='X' and e['round']==1 for e in reports['pentomino-6x10']['events'])
    assert any(e['row']==ridO and e['blocked']=='X' and e['round']==2 for e in reports['pentomino-6x10']['events'])
    primary,names,_=parse((OUT/'pentomino-6x10.xcc').read_text());r=Replay(primary,names,original)
    allowed=r.col['X']&r.compatible(original[ridO]);assert allowed.bit_count()==1
    xrow=allowed.bit_length();assert set(original[xrow])==set('X 01 10 11 12 21'.split()) and xrow not in reduced
    # Equation38 is geometrically impossible, but survives both fixed points.
    original,reduced=cases['pentomino3x20'];bad=next(k for k,v in original.items() if set(v)==set('V 09 0a 0b 19 29'.split()));assert bad in reduced
    y=reports['y15x15']['events'];assert any(e['kind']=='force' and e['item']=='20' and '10' in e['all_primary_witnesses'] for e in y)
    yy=next(e for e in y if e['kind']=='force' and e['item']=='00' and e['round']==2)
    assert '11' in yy['all_primary_witnesses'] and '22' not in yy['all_primary_witnesses']
    original,reduced=cases['y15x15'];rid=next(k for k,v in original.items() if set(v)==set('50 51 52 53 62'.split()))
    assert all(not {'00','22'}<=row.keys() for row in original.values())
    assert any(e['kind']=='block' and e['row']==rid and e['blocked']=='61' and e['round']==4 for e in y)
    order=json.loads((OUT/'y-order.json').read_text());assert sha(ROOT/'check_y_preprocess_order.py')==order['checker_sha256']
    for p,h in order['hashes'].items():assert sha(ROOT/p)==h;files.append(ROOT/p)
    ordered,orr,red=replay('y15x15-printed-order')
    yy2=next(e for e in ordered['events'] if e['kind']=='force' and e['item']=='00' and e['round']==2)
    assert '11' in yy2['all_primary_witnesses'] and '22' not in yy2['all_primary_witnesses']
    reports['y15x15-printed-order']=ordered
    save(OUT/'f146-witness.json',verify_f146())
    examples['explicit225']=dict(first_round_P=ridP,second_round_O=ridO,unique_initial_X_support=xrow)
    save(OUT/'verified.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=sha(__file__),nice=os.nice(0),wall_seconds=time.monotonic()-start,
        dependencies={p:sha(ROOT/p) for p in ['prepare_pentomino_main.py','puzzle_xcc.py','run_preprocess225.py','check_pentomino_bipairs.py','sudoku_automorphisms114.py','verify_f146.py','check_y_preprocess_order.py']},
        source_hashes={str(p.relative_to(ROOT)):sha(p) for p in files},reports=reports,examples=examples,old_solution_censuses_repeated=0,new_full_solution_searches=0,
        caveats=['Soma main109 example not yet checked.','Full6x10 count2339 and historical solution-search costs not rerun; exact omission record required.']))
    print('PASS: seven reductions replayed; three independent pentomino fixed points;225 examples checked. F146:00 cannot be forced by22; both orders give11.')


if __name__=='__main__':main()

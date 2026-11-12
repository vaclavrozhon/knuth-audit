"""Exact local checks for DLX109 and the independently counted DLX114 symmetry."""
import html,json,re
from layout_native import ROOT,OUT,save,sha
from wordcross109 import WORDS,instance,geometry


def main():
    enc,info=instance(WORDS,8,8,symmetry=False)
    zero=next(i for i,p in enumerate(info) if p.get('word')==0 and p['cells']==(0,8,16,24))
    chosen=dict(enc['rows'][zero]);primary=enc['primary']
    def compatible(row):
        return all(i not in chosen or (i>primary and c==chosen[i]) for i,c in row)
    remaining=[i for i,row in enumerate(enc['rows']) if compatible(row)]
    forced={}
    for name in ['H11','H31','V41']:
        item=enc['names'].index(name)+1
        options=[i for i in remaining if any(j==item for j,c in enc['rows'][i])]
        assert len(options)==1 and 'edge' in info[options[0]],(name,options)
        forced[name]=info[options[0]]
    assert all(name not in enc['names'] for name in ['H00','H20','V30'])
    witness=json.loads((OUT/'wordcross109-line53-witness-decoded.json').read_text())
    assert witness['native_models']==witness['distinct_placements']==1
    p=witness['placements'][0]
    direct=geometry(WORDS,1,53,p['chosen'])
    assert direct['board']=='.'.join(WORDS) and direct['components']==11
    assert len(direct['board'])==sum(map(len,WORDS))+len(WORDS)-1==53<5*11

    source=ROOT/'sources/layouts108_114/sudoku-symmetry.html'
    rows=re.findall(r'<tr\b[^>]*>(.*?)</tr>',source.read_text(),re.S|re.I)
    row=next(r for r in rows if '30258432' in r)
    fields=[html.unescape(re.sub('<[^>]*>','',s)).strip() for s in re.findall(r'<td[^>]*>(.*?)</td>',row,re.S)]
    assert fields[0]=='37' and fields[3]=='30258432'
    alpha=list(range(81))
    for cyc in re.findall(r'\(([^)]+)\)',fields[2]):
        cycle=[int(x)-1 for x in cyc.split()]
        for a,b in zip(cycle,cycle[1:]+cycle[:1]):alpha[a]=b
    # beta(r,c)=(r+3 mod9,c): alpha=beta*transpose*beta^-1.
    formula=[9*((c+3)%9)+(r+6)%9 for r in range(9) for c in range(9)]
    assert alpha==formula
    examples={}
    for name,data in json.loads((ROOT/'results/sudoku_basics/pdf-grids.json').read_text())['sources'].items():
        if name not in ['28a','28b','28c']:continue
        b=data['board'];perm=dict(zip(b[:9],b[::9]))
        bad=[(r+1,c+1,b[9*c+r],perm[b[9*r+c]]) for r in range(9) for c in range(9) if b[9*c+r]!=perm[b[9*r+c]]]
        assert bool(bad)==(name!='28b')
        examples[name]=dict(permutation=perm,violations=bad[:3],is_automorphism=not bad)
    assert examples['28b']['permutation']=={1:1,2:4,3:7,4:2,5:5,6:8,7:3,8:6,9:9}
    terminals=[]
    for n in [4,9]:
        label=f'transpose-cell-n{n}';m=json.loads((OUT/(label+'.json')).read_text())
        assert m['status']=='completed' and m['returncode']==0
        assert m['source_sha256']==sha(ROOT/'enumerate_transpose_sudoku.cpp')
        assert m['script_sha256']==sha(ROOT/'run_transpose_sudoku.py')
        assert m['binary_sha256']==sha(m['command'][2])
        assert m['stdout_sha256']==sha(OUT/(label+'.out')) and m['stderr_sha256']==sha(OUT/(label+'.log'))
        base=2 if n==4 else 3;target=set(range(n))
        for b in m['witnesses']:
            assert b[:n]==list(range(n));pi=b[::n]
            for r in range(n):
                assert set(b[n*r:n*r+n])==set(b[r::n])==target
                for c in range(n):assert b[n*c+r]==pi[b[n*r+c]]
            for br in range(base):
                for bc in range(base):assert {b[n*(base*br+r)+base*bc+c] for r in range(base) for c in range(base)}==target
        native=json.loads((OUT/(f'sudoku114-n{n}-improved.json')).read_text())
        assert m['solutions']==native['solutions']
        terminals.append(dict(n=n,solutions=m['solutions'],witnesses=len(m['witnesses']),nodes=m['nodes'],hashes_verified=True))
    save(OUT/'details-checked.json',dict(script_sha256=sha(__file__),
        F129=dict(selected_zero=info[zero],printed_undefined=['H00','H20','V30'],correct_forced=forced),
        F130=dict(witness=direct,area=53,claimed_minimum_area=55,true_minimum_not_asserted=True),
        sudoku114=dict(source_sha256=sha(source),class_number=37,source_count=30258432,
            conjugacy_all81_cells_verified=True,examples=examples,independent_terminals=terminals)))
    print('109: three correct forced edges;53<55 witness.114: all81 source cells conjugate;28a/b/c and both independent terminals verified.')


if __name__=='__main__':main()

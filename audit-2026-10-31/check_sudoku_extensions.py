#!/usr/bin/env python3
"""DLX64 example, all seven DLX65 solutions, and hypersudoku DLX67."""
from datetime import datetime,timezone
import json
from dlx1_audit_tools import ROOT,sha,run,input_text,decode_rows
from check_jigsaw_small import coordinate_solutions,instance,violations
from check_jigsaw_supplement import exact_cover

OUT=ROOT/'results/sudoku_extensions'


def native(label,d,alphabet,expected):
    names,rows,moves,primary=instance(d,alphabet)
    stats,txt=run(OUT/'native',label,input_text(names,rows,primary),models=True)
    (OUT/'native'/(label+'.models')).write_text(txt)
    actual=[]
    for selected in decode_rows(txt,names,rows):
        b=list(d['cells'])
        for i in selected:v,k=moves[i];assert b[v]=='.';b[v]=k
        assert not violations(d,b);actual.append(''.join(b))
    assert sorted(actual)==expected
    return stats


def hyper_instance(board,extra):
    tau=[3,2,1,0,4,8,7,6,5]
    names=[f'p{r}{c}'for r in range(9)for c in range(9)]
    for prefix in ['r','c','b']:
        names += [f'{prefix}{i}{k}'for i in range(9)for k in '123456789']
    names += [f'h{i}{k}'for i in extra for k in '123456789']
    def option(v,k):
        r,c=divmod(v,9);b=3*(r//3)+c//3;h=3*(tau[r]//3)+tau[c]//3
        return [f'p{r}{c}',f'r{r}{k}',f'c{c}{k}',f'b{b}{k}']+([f'h{h}{k}']if h in extra else [])
    used={s for v,k in enumerate(board)if k!='.' for s in option(v,k)}
    names=[s for s in names if s not in used];ix={s:i+1 for i,s in enumerate(names)}
    rows=[];moves=[]
    for v in range(81):
        for k in '123456789':
            o=option(v,k)
            if not used.intersection(o):rows.append([ix[s]for s in o]);moves.append((v,k))
    return names,rows,moves


def main():
    diagrams=json.loads((OUT/'pdf-diagrams.json').read_text())['sources']
    result=dict(source_sha256=sha(__file__),diagrams_sha256=sha(OUT/'pdf-diagrams.json'),puzzles65={},hyper67={})
    for row in [0,1]:
        d=dict(diagrams['64']);d['cells']=['.']*36;d['cells'][row*6:row*6+6]='ABCDEF'
        sols,nodes=coordinate_solutions(d,'ABCDEF');assert len(sols)==1
        stats=native('64-row'+str(row),d,'ABCDEF',sols)
        result['64-row'+str(row)]=dict(solution=sols[0],coordinate_nodes=nodes,native=stats,book_nodes=[40,215][row])
        print('64 row',row,stats['nodes'],flush=True)
    for word in ['DANCING','LINKS','COMPUTER','ALGORITHM','SOLVING','SUDOKU','PUZZLE']:
        d=diagrams['65q-'+word];n=d['nrows'];alphabet=''.join(dict.fromkeys(word))
        if len(alphabet)<n:alphabet+='0'
        assert len(alphabet)==n
        sols,nodes=coordinate_solutions(d,alphabet);assert len(sols)==1,(word,len(sols))
        stats=native('65-'+word,d,alphabet,sols)
        answer=''.join(diagrams['65a-'+word]['cells']).replace('.','0')
        differences=[dict(cell=v,printed=x,correct=y)for v,(x,y)in enumerate(zip(answer,sols[0]))if x!=y]
        if word=='SOLVING':
            assert differences==[dict(cell=48,printed='S',correct='G')]
            layers=diagrams['65a-'+word]['conflicting_glyph_layers']
            assert len(layers)==1 and [x['text']for x in layers[0]['paint_order']]==['G','S']
        elif word=='SUDOKU':
            assert differences==[dict(cell=10,printed='0',correct='O'),dict(cell=11,printed='O',correct='0')]
            assert not diagrams['65a-'+word]['conflicting_glyph_layers']
        else:assert not differences and not diagrams['65a-'+word]['conflicting_glyph_layers']
        result['puzzles65'][word]=dict(alphabet=alphabet,solution=sols[0],coordinate_nodes=nodes,native=stats,
                         printed_differences=differences,violations_of_last_painted_layer=violations(d,answer),
                         conflicting_glyph_layers=diagrams['65a-'+word]['conflicting_glyph_layers'])
        print('65',word,'unique',differences,flush=True)
    tau=[3,2,1,0,4,8,7,6,5]
    standard=[[9*(3*a+r)+3*b+c for r in range(3)for c in range(3)]for a in range(3)for b in range(3)]
    new=[[v for v in range(81)if 3*(tau[v//9]//3)+tau[v%9]//3==h]for h in range(9)]
    assert all(len(t)==9 for t in new)and len({v for t in new for v in t})==81
    letters=diagrams['67a-boxes']['cells']
    for k,h in zip('abcde',[3,5,1,7,4]):assert [v for v,c in enumerate(letters)if c==k]==new[h]
    # The involution exchanges the two complete partitions of nine boxes.
    change=lambda t:tuple(sorted(9*tau[v//9]+tau[v%9]for v in t))
    assert {change(t)for t in standard}==set(map(tuple,new))
    assert {change(t)for t in new}==set(map(tuple,standard))
    result['hyper67']['partitions']=dict(standard=standard,derived=new,tau=tau,involution_verified=True)
    for label in ['i','ii']:
        q=diagrams['67q-'+label];answer=''.join(diagrams['67a-'+label]['cells'])
        cases={}
        for mode,extra,book in [('four',[0,2,6,8],231 if label=='i' else 708),('nine',list(range(9)),77 if label=='i' else 151)]:
            d=dict(q,regions=standard+[new[h]for h in extra])
            sols,nodes=coordinate_solutions(d,'123456789');assert sols==[answer]
            names,rows,moves=hyper_instance(d['cells'],extra)
            stats,txt=run(OUT/'native','67-'+label+'-'+mode,input_text(names,rows),models=True)
            (OUT/'native'/('67-'+label+'-'+mode+'.models')).write_text(txt)
            models,profile=exact_cover(rows,len(names),len(names))
            native_models=decode_rows(txt,names,rows)
            assert models==native_models and len(models)==1
            assert stats['profile']==[profile.get(i,0)for i in range(len(stats['profile']))]
            b=list(d['cells'])
            for i in next(iter(models)):v,k=moves[i];assert b[v]=='.';b[v]=k
            assert ''.join(b)==answer
            cases[mode]=dict(native=stats,independent_profile=dict(profile),book_nodes=book,coordinate_nodes=nodes,solution=answer)
            print('67',label,mode,stats['nodes'],'book',book,flush=True)
        result['hyper67'][label]=cases
    result.update(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat())
    (OUT/'small-check.json').write_text(json.dumps(result,indent=2)+'\n')


if __name__=='__main__':main()

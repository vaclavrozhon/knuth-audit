"""Read-only acceptance of completed101--107 evidence; no expensive searches."""
from collections import defaultdict
from math import gcd
import json
from puzzle_xcc import ROOT,OUT,save,sha
from check_music103_104 import read_cell_rows
from word_puzzles import placements,orbit


def main():
    expected=[1,2,4,24,288,3856,89328,2755968,103653120]
    r_orbits=[None,None,1,1,6,22,48,232,1872]
    q_orbits=[None,None,0,0,2,15,0,0,1346]
    runs=[]
    queue=json.loads((OUT/'music-queue.json').read_text())
    assert queue['status']=='completed' and queue['done']==list(range(2,19))
    for n in range(2,19):
        meta=json.loads((OUT/f'music-{n}.json').read_text())
        assert meta['status']=='completed' and meta['returncode']==0
        assert meta['source_sha256']==sha(ROOT/'enumerate_musical_rows.cpp')
        assert meta['script_sha256']==sha(ROOT/'run_musical_rows.py')
        assert meta['stdout_sha256']==sha(OUT/f'music-{n}.out')
        assert meta['stderr_sha256']==sha(OUT/f'music-{n}.log')
        raw=json.loads((OUT/f'music-{n}.out').read_text())
        assert all(meta[k]==v for k,v in raw.items())
        assert raw['solutions']==(expected[n//2-1] if n%2==0 else 0)
        if n<=14:assert meta['rows_sha256']==sha(OUT/f'music-{n}.rows.bin')
        if n>=6 and n%2==0:
            phi=sum(gcd(c,n)==1 for c in range(1,n))
            assert raw['reverse_fixed']==2*phi*r_orbits[n//2-1]
            assert raw['negative_q_fixed']==2*phi*q_orbits[n//2-1]
        runs.append({k:meta[k] for k in ['n','solutions','nodes','reverse_fixed','negative_q_fixed','qr_fixed','elapsed_seconds']})
    # The complete n14 list was not checked by the small XCC comparison.
    rows14=read_cell_rows(14);assert len(rows14)==89328
    native_labels=['zebra-direct','zebra-inverse','zebra-inverse-lexical','pi-day-author',
                   'words105','words106','words107-pair','words107-eleven']+[f'music-xcc-{n}' for n in range(2,13)]
    for label in native_labels+['words106-mcc']:
        meta=json.loads((OUT/(label+'.json')).read_text())
        assert meta['status']=='completed' and meta['returncode']==0
        for field,suffix in [('input_sha256','.dlx'),('stdout_sha256','.out.gz'),('stderr_sha256','.log')]:
            assert meta[field]==sha(OUT/(label+suffix)),(label,field)
    figures=json.loads((OUT/'figures-checked.json').read_text())
    assert figures['glyphs']==311 and figures['ovals']==91
    five=figures['grids'][:5];assert len({min(orbit(g['board'],6)) for g in five})==5
    d105=json.loads((OUT/'words105-decoded.json').read_text())
    wanted=[m for m in d105['models'] if m['unused']==1]
    assert len(wanted)==40 and len({m['board'] for m in wanted})==40
    assert {min(orbit(m['board'],6)) for m in wanted}=={min(orbit(g['board'],6)) for g in five}
    assert sorted(m['components'] for m in wanted)==[1]*24+[2]*16
    d106=json.loads((OUT/'words106-decoded.json').read_text())
    def rotations(b,n):
        result=set()
        for _ in range(4):
            result.add(b);b=''.join(b[(n-1-j)*n+i] for i in range(n) for j in range(n))
        return result
    two=figures['grids'][5:7]
    a,b=[rotations(g['board'],5) for g in two]
    assert len(a)==len(b)==4 and not a&b
    assert a|b=={m['board'] for m in d106['models']}
    d107=json.loads((OUT/'words107-eleven-decoded.json').read_text())
    by_board=defaultdict(list)
    for m in d107['models']:by_board[m['board']].append(set(m['chosen']))
    assert len(by_board)==8 and all(len(v)==2 for v in by_board.values())
    catalog=placements(d107['words'],9,False);ambiguous=set()
    for models in by_board.values():
        difference=models[0]^models[1];assert len(difference)==2
        ambiguous.update(d107['words'][catalog[k]['word']] for k in difference)
    pitches=[('F',0,4),('E',0,4),('C',0,5),('A',0,4),('G',0,5),('D',0,5),
             ('A',-1,5),('D',-1,5),('E',-1,5),('G',-1,4),('B',-1,4),('B',0,3)]
    pitch_values=dict(A=0,B=2,C=3,D=5,E=7,F=8,G=10)
    classes=[(pitch_values[name]+accidental)%12 for name,accidental,octave in pitches]
    assert classes==[8,7,3,0,10,5,11,4,6,9,1,2]
    sat={}
    for label in ['words105','words106','words107-pair','words107-eleven']:
        path=OUT/(label+'-sat.json')
        if path.exists():
            meta=json.loads(path.read_text());assert meta['status']=='completed' and meta['exhausted']
            assert meta['formula_sha256']==sha(OUT/(label+'-sat.cnf'))
            sat[label]={k:meta[k] for k in ['status','total_models','requested_models','requested_boards','requested_dihedral_classes']}
        else:sat[label]={'status':'not_accepted_yet'}
    save(OUT/'checkpoint-checked.json',dict(script_sha256=sha(__file__),music_runs=runs,
         new_n14_full_rows_independently_validated=89328,native_finished_runs=len(native_labels)+1,
         figures_glyphs=311,figures_ovals=91,words105_requested_models=40,words105_classes=5,
         words106_boards=8,words107_boards=8,words107_classes=1,words107_ambiguous_word=sorted(ambiguous),
         staff_visually_read=pitches,staff_pitch_classes=classes,sat=sat))
    print('Accepted all music counts through18;311 glyphs/91 ovals;107 ambiguity:',ambiguous,'SAT:',sat)


if __name__=='__main__':main()

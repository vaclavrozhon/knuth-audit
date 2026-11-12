"""Validate all reported models and compare original and independent solvers."""
import json
from pathlib import Path
from check_questionnaires import literal_grade

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/questionnaires'


def main():
    original=json.loads((OUT/'original-runs.json').read_text())
    assert len(original)==63
    for variant,prefix,modified,indeterminate in [
        ('base','base',False,False),('modified','modified',True,False),
        ('indeterminate','indeterminate',True,True)]:
        rows=[r for r in original if r['variant']==variant]
        assert len(rows)==21
        for row in rows:
            for answer in row['solutions']:
                grades=[c.isupper() for c in answer]
                assert literal_grade(answer,grades,modified,sum(grades),indeterminate)==grades
        if not indeterminate:
            assert rows[0]['count']==json.loads((OUT/(prefix+'-20.json')).read_text())['count']
        actual=sorted(answer for row in rows if row['false'] for answer in row['solutions'])
        expected=json.loads((OUT/(prefix+'-19.json')).read_text())['solutions']
        assert actual==expected
    by_false={r['false']:r for r in original if r['variant']=='base'}
    assert (by_false[0]['nodes'],by_false[0]['mems'])==(52859,3355989)
    assert (by_false[15]['nodes'],by_false[15]['mems'])==(56,4902)
    assert (by_false[19]['nodes'],by_false[19]['mems'])==(184770,10799667)
    assert (by_false[20]['nodes'],by_false[20]['mems'])==(130721,7608471)
    printed=[
        ('base-19','D C E A B E B C E A B E A E D B D A b B'),
        ('base-19','A E D C A B C D C A C E D B C A D A A c'),
        ('base-19','D C E A B A D C D A E D A E D B D B E e'),
        ('modified-18-C','B A d A B E D C D A E D A E D E D B E c'),
        ('modified-18-C','A E D C A B C D C A C E D B a C D A A c'),
        ('modified-18-A','D e D A B E D e C A E D A E D B D C C A'),
        ('indeterminate-19','D C E A B E D C E A E B A E D B D A d D')]
    for case,text in printed:
        assert text.replace(' ','') in json.loads((OUT/(case+'.json')).read_text())['solutions']
    assert json.loads((OUT/'modified-18-A.json').read_text())['count']==48
    result=dict(status='pass',original_runs=63,printed_solutions=len(printed),
                exact_program_metrics=True,all_seven_printed_models=True)
    (OUT/'cross-verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print(result)


if __name__=='__main__':main()

"""Verify the remaining explicit geometric assertions and standalone proof."""
from datetime import datetime,timezone
import json,subprocess
import vertices140 as h
import verify_f134 as standalone


def main():
    fig=json.loads((h.OUT/'figures-checked.json').read_text())['figures']
    assert len(h.PIECES)==(4**3+2*4)//3==24
    for label,w,hgt in [('a1',6,2),('a2',4,3)]:
        assert {tuple(t) for t in fig[label]['cells']}=={(x,y,z) for x in range(w) for y in range(hgt) for z in (0,1)}
    triangle={(x,y,z) for x in range(5) for y in range(5) for z in (0,1) if x+y<5-z}
    assert len(triangle)==25
    assert {tuple(t) for t in fig['a3']['cells']}==triangle-{(0,4,0)}
    a2=fig['a2'];half=[g for g in h.symmetries(a2['cells']) if g['halfturn']]
    assert len(half)==1
    moved=h.spatial_word(a2['vertex_colors'],half[0]['perm'])
    assert h.canonical_colors(moved)==h.canonical_colors(a2['vertex_colors'])
    rename={}
    for a,b in zip(a2['vertex_colors'],moved):
        assert a not in rename or rename[a]==b
        rename[a]=b
    assert set(rename)==set(rename.values())==set('abcd')
    # Match the standalone literal transcription with every extracted PDF corner.
    for (cell,word),tri in zip(standalone.TILES,fig['c3']['triangles']):
        assert tuple(tri['cell'])==cell
        colors=dict(zip(map(tuple,tri['vertices']),tri['colors']))
        assert ''.join(colors[v] for v in h.vertices(cell))==word
    p=subprocess.run(['python3',str(h.ROOT/'verify_f134.py')],capture_output=True,text=True)
    assert p.returncode==0,p.stderr
    result=json.loads(p.stdout);assert result['result']=='PASS'
    h.save(h.OUT/'standalone-f134-checked.json',dict(command=['python3','verify_f134.py'],returncode=p.returncode,
        source_sha256=h.sha(h.ROOT/'verify_f134.py'),result=result,all72_transcribed_corners_match_pdf=True))
    h.save(h.OUT/'claims-checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=h.sha(__file__),
        geometry_sha256=h.sha(h.__file__),figures_sha256=h.sha(h.OUT/'figures-checked.json'),
        tile_types=24,parallelograms=[[6,2],[4,3]],truncated_triangle_side=5,
        printed_middle_figure_halfturn_color_permutation=rename,
        standalone_sha256=h.sha(h.OUT/'standalone-f134-checked.json')))
    print('PASS: board dimensions, printed middle half-turn and all 72 standalone certificate corners.',rename)


if __name__=='__main__':main()

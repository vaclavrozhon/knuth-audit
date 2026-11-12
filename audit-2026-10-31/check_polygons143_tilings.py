"""Only the three new 24-cell shapes; reuse the completed140 results for the rest."""
from datetime import datetime, timezone
from pathlib import Path
import gzip
import json
import subprocess
import polygons143 as h
import graph_native as native


def read(path):
    return json.loads(path.read_text())


def main():
    out=h.OUT/'tilings';out.mkdir(exist_ok=True)
    assert not (out/'started.json').exists(),'Do not repeat completed searches.'
    h.save(out/'started.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=h.sha(__file__),
        geometry_sha256=h.sha(h.__file__),triangles_sha256=h.sha(h.triangles.__file__)))
    native_meta=read(h.ROOT/'results/vertices140/native/a1.json')
    binary=Path(native_meta['command'][2]);assert h.sha(binary)==native_meta['binary_sha256']
    source=Path(native_meta['source']);assert h.sha(source)==native_meta['source_sha256']
    build=read(h.ROOT/'results/vertices140/independent-fixed/build.json')
    independent=Path(build['binary']);assert h.sha(independent)==build['binary_sha256']
    assert h.sha(h.ROOT/'count_vertices140.cpp')==build['source_sha256']
    cases=[];lines=[];native.OUT=out
    for index in [0,2,4]:
        label=f'shape{index+1}';cells=h.simplex_graph(h.simplex_parameters(h.SIX24[index]))['cells']
        cells=h.triangles.normalize_shape(cells);enc=h.triangles.problem(cells)
        h.save(out/(label+'-encoding.json'),enc)
        meta=native.run(label,h.triangles.native_text(enc),binary=binary,source=source,every=1,limit=172800)
        assert meta['status']=='completed' and meta['returncode']==0 and meta['solutions']==0
        assert gzip.open(out/(label+'.out.gz'),'rb').read()==b''
        vv=h.triangles.vertex_list(cells);idx={v:i for i,v in enumerate(vv)}
        lines.append(f'{label} {len(vv)}')
        lines.extend(' '.join(str(idx[v]) for v in h.triangles.vertices(t)) for t in cells)
        cases.append(dict(label=label,parameters=h.SIX24[index],cells=cells,
            native_terminal_sha256=h.sha(out/(label+'.json')),native_solutions=0,native_nodes=meta['nodes']))
    text='\n'.join(lines)+'\n';(out/'independent-input.txt').write_text(text)
    command=['timeout','172800',str(independent)]
    with (out/'independent-input.txt').open('rb') as fin,(out/'independent-stdout.txt').open('xb') as fout,(out/'independent-stderr.log').open('xb') as ferr:
        result=subprocess.run(command,stdin=fin,stdout=fout,stderr=ferr)
    terminal=dict(at_utc=datetime.now(timezone.utc).isoformat(),command=command,returncode=result.returncode,
        binary_sha256=h.sha(independent),source_sha256=h.sha(h.ROOT/'count_vertices140.cpp'),
        input_sha256=h.sha(out/'independent-input.txt'),stdout_sha256=h.sha(out/'independent-stdout.txt'),stderr_sha256=h.sha(out/'independent-stderr.log'))
    h.save(out/'independent-terminal.json',terminal);assert result.returncode==0
    output=(out/'independent-stdout.txt').read_text().splitlines();assert len(output)==3
    for line,case in zip(output,cases):
        fields=line.split();assert fields[:3]==['C',case['label'],'0'] and len(fields)==4
        case['independent_solutions']=0;case['independent_nodes']=int(fields[3])
    assert (out/'independent-stderr.log').read_text().splitlines()[-1]=='ALL_COMPLETED 3'
    h.save(out/'checked.json',dict(at_utc=datetime.now(timezone.utc).isoformat(),checker_sha256=h.sha(__file__),
        geometry_sha256=h.sha(h.__file__),cases=cases,both_complete_counts_zero=True,
        independent_terminal_sha256=h.sha(out/'independent-terminal.json'),
        reuse140='Only three new shapes enumerated. The other three are geometrically identical to a1/a2/a3 in the already accepted140 census.'))
    print('PASS143: all three other24-cell shapes have zero tilings in two complete independent censuses.')


if __name__=='__main__':
    main()

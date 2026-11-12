#!/usr/bin/env python3
"""DLX58: queen-pattern clique census versus the author's colored DLX2 model."""
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import json
import re
import shutil
import subprocess
import tempfile
import time
from check_sudoku_basics import UNITS
from dlx1_audit_tools import ROOT, sha

OUT = ROOT/'results/sudoku_variants/queens58'


def valid(board):
    assert len(board) == 81
    assert all({board[v] for v in unit} == set(range(1,10)) for unit in UNITS)
    for k in range(1,8):
        cells = [divmod(v,9) for v,n in enumerate(board) if n == k]
        assert len({i+j for i,j in cells}) == len({i-j for i,j in cells}) == 9


def queen_patterns():
    patterns = []
    def visit(row, cols, diag1, diag2, boxes, selected):
        if row == 9:
            patterns.append(tuple(selected)); return
        for col in range(9):
            b = 3*(row//3)+col//3
            if cols>>col&1 or diag1>>(row+col)&1 or diag2>>(row-col+8)&1 or boxes>>b&1:
                continue
            visit(row+1, cols|1<<col, diag1|1<<(row+col), diag2|1<<(row-col+8),
                  boxes|1<<b, selected+[9*row+col])
    visit(0,0,0,0,0,[])
    return patterns


def normalize(board):
    """Digit normalization only: queens in first-row order; first nonqueen is8."""
    names = [k for k in board[:9] if k <= 7]+[k for k in board[:9] if k >= 8]
    mapping = {k:i+1 for i,k in enumerate(names)}
    return tuple(mapping[k] for k in board)


def independent():
    patterns = queen_patterns()
    masks = [sum(1<<v for v in p) for p in patterns]
    adjacency = [sum(1<<j for j in range(i+1,len(patterns)) if not masks[i]&masks[j])
                 for i in range(len(patterns))]
    profile = [0]*8
    clique_count = 0
    component_counts = Counter()
    models = set()
    def finish(chosen, used):
        nonlocal clique_count
        clique_count += 1
        remaining = {v for v in range(81) if not used>>v&1}
        graph = {v:set() for v in remaining}
        for unit in UNITS:
            a,b = set(unit)&remaining
            graph[a].add(b); graph[b].add(a)
        color, components = {}, []
        for v in sorted(remaining):
            if v in color:
                continue
            color[v] = 0; stack = [v]; component = []
            while stack:
                x = stack.pop(); component.append(x)
                for y in graph[x]:
                    if y in color:
                        if color[y] == color[x]:
                            return
                    else:
                        color[y] = 1-color[x]; stack.append(y)
            components.append(component)
        component_counts[len(components)] += 1
        board = [0]*81
        for k,index in enumerate(sorted(chosen,key=lambda i:patterns[i][0]),1):
            for v in patterns[index]:
                board[v] = k
        # Quotient the global interchange8/9 by fixing the first component.
        for mask in range(1<<(len(components)-1)):
            for i,component in enumerate(components):
                flip = 0 if i == 0 else mask>>(i-1)&1
                for v in component:
                    board[v] = 8+(color[v]^flip)
            model = tuple(board); valid(model)
            assert normalize(model) == model and model not in models
            models.add(model)
    def visit(candidates, chosen, used):
        level = len(chosen); profile[level] += 1
        if level == 7:
            finish(chosen,used); return
        while candidates.bit_count() >= 7-level:
            bit = candidates&-candidates; candidates ^= bit
            i = bit.bit_length()-1
            visit(candidates&adjacency[i], chosen+[i], used|masks[i])
    visit((1<<len(patterns))-1,[],0)
    kept = {s for s in models if s.index(8)+s.index(9)<9}
    return kept, dict(patterns=patterns, profile=profile, seven_pattern_cliques=clique_count,
                      completable_cliques_by_component_count=dict(component_counts),
                      digit_normalized_models=[list(s) for s in sorted(models)],
                      book_normalized_models=[list(s) for s in sorted(kept)])


def build():
    manifest = OUT/'build.json'
    if manifest.exists():
        data = json.loads(manifest.read_text())
        assert sha(data['binary']) == data['binary_sha256']
        assert all(sha(ROOT/v['path']) == v['sha256'] for v in data['sources'].values())
        return data
    source = ROOT/'sources/knuth-programs'
    directory = Path(tempfile.mkdtemp(prefix='knuth-vol4b-sudoku-queens-'))
    names = ['dlx2.w','gb_flip.w','gb_flip.ch','boilerplate.w']
    for name in names:
        shutil.copy2(source/name,directory/name)
    commands = [['ctangle','gb_flip.w','gb_flip.ch'],['ctangle','dlx2.w'],
                ['cc','-O2','-Wno-implicit-int','-Wno-implicit-function-declaration',
                 'dlx2.c','gb_flip.c','-o','dlx2']]
    with (OUT/'build.log').open('w') as log:
        for command in commands:
            subprocess.run(command,cwd=directory,stdout=log,stderr=subprocess.STDOUT,check=True)
    data = dict(built_at_utc=datetime.now(timezone.utc).isoformat(),commands=commands,
                binary=str(directory/'dlx2'),binary_sha256=sha(directory/'dlx2'),
                sources={name:dict(path=str((source/name).relative_to(ROOT)),sha256=sha(source/name)) for name in names},
                scope='Unmodified archived author DLX2, built in an isolated temporary directory.')
    manifest.write_text(json.dumps(data,indent=2)+'\n')
    return data


def native():
    prim = [f'{t}{i}{k}' for t in 'prcb' for i in range(9)
            for k in (range(9) if t == 'p' else range(1,10))]+['*']
    secondary = [f'{t}{d:02}{k}' for t in 'ab' for d in range(17) for k in range(1,8)]
    secondary += [f'*{j}' for j in range(9)]
    options = []
    for i in range(9):
        for j in range(9):
            for k in range(1,10):
                option = [f'p{i}{j}',f'r{i}{k}',f'c{j}{k}',f'b{3*(i//3)+j//3}{k}']
                if k <= 7:
                    option += [f'a{i+j:02}{k}',f'b{i-j+8:02}{k}']
                if i == 0:
                    option += [f'*{j}:{k}']
                options.append(option)
    starts = []
    for p in range(9):
        for q in range(p+1,9):
            if p+q >= 9:
                continue
            first = [8 if j == p else 9 if j == q else 1+j-(j>p)-(j>q) for j in range(9)]
            starts.append(first)
            options.append(['*']+[f'*{j}:{k}' for j,k in enumerate(first)])
    assert len(starts) == 20 and len(options) == 749
    data = '\n'.join([' '.join(prim+['|']+secondary)]+[' '.join(o) for o in options])+'\n'
    (OUT/'58.xcc').write_text(data)
    info = build(); command = [info['binary'],'v129','m1']
    start = time.monotonic()
    with (OUT/'58.models').open('w') as output,(OUT/'58.log').open('w') as log:
        proc = subprocess.Popen(command,stdin=subprocess.PIPE,stdout=output,stderr=log,text=True)
        meta = dict(command=command,pid=proc.pid,started_at_utc=datetime.now(timezone.utc).isoformat(),
                    timeout_seconds=1800,input_sha256=sha(OUT/'58.xcc'),binary_sha256=info['binary_sha256'])
        (OUT/'native-run.json').write_text(json.dumps(meta,indent=2)+'\n')
        try:
            proc.communicate(data,timeout=1800)
        except subprocess.TimeoutExpired:
            proc.kill(); proc.wait(); raise
        assert proc.returncode == 0
    log = (OUT/'58.log').read_text()
    match = re.search(r'Altogether (\d+) solutions?, (\d+)\+(\d+)-(\d+) mems, (\d+) updates, (\d+) cleansings, (\d+) bytes, (\d+) nodes',log)
    assert match,log[-1500:]
    stats = dict(zip(['solutions','initialization_mems','search_mems','removed_mems','updates','cleansings','bytes','nodes'],map(int,match.groups())))
    stats['net_search_mems'] = stats['search_mems']-stats['removed_mems']
    models,board = set(),None
    lookup = {frozenset(o):o for o in options}
    for line in (OUT/'58.models').read_text().splitlines()+['end:']:
        if line == 'end:' or re.fullmatch(r'\d+:',line):
            if board is not None:
                valid(board); assert tuple(board) not in models; models.add(tuple(board))
            board = [0]*81
        elif line.strip():
            match = re.fullmatch(r'\s*(.*?) \(\d+ of \d+\)',line); assert match,line
            words = match[1].split(); assert frozenset(words) in lookup
            cell = next((w for w in words if w.startswith('p')),None)
            if cell is not None:
                i,j = map(int,cell[1:]); k = int(next(w for w in words if w.startswith('r'))[-1])
                assert not board[9*i+j]; board[9*i+j] = k
    assert stats['solutions'] == len(models)
    meta.update(status='finished',elapsed_seconds=time.monotonic()-start,statistics=stats,
                finished_at_utc=datetime.now(timezone.utc).isoformat(),models_sha256=sha(OUT/'58.models'))
    (OUT/'native-run.json').write_text(json.dumps(meta,indent=2)+'\n')
    return models,meta


def main():
    OUT.mkdir(parents=True,exist_ok=True)
    start = time.monotonic()
    expected,independent_result = independent()
    (OUT/'independent.json').write_text(json.dumps(independent_result,indent=2)+'\n')
    print('independent',len(independent_result['patterns']),'patterns,',independent_result['profile'],
          len(independent_result['digit_normalized_models']),'digit-normalized models,',len(expected),'book models',flush=True)
    actual,metadata = native()
    assert actual == expected and len(actual) == 4
    symmetries = []
    for board in sorted(actual):
        rotate = normalize(board[::-1])
        assert rotate == board
        transpose = normalize(tuple(board[9*j+i] for i in range(9) for j in range(9)))
        if transpose.index(8)+transpose.index(9) >= 9:
            transpose = normalize(tuple(transpose[9*i+8-j] for i in range(9) for j in range(9)))
        assert transpose in actual and transpose != board
        symmetries.append(dict(board=list(board),transpose_partner=list(transpose)))
    assert len({min(tuple(s['board']),tuple(s['transpose_partner'])) for s in symmetries}) == 2
    result = dict(status='verified',checked_at_utc=datetime.now(timezone.utc).isoformat(),
                  source_sha256=sha(__file__),independent_sha256=sha(OUT/'independent.json'),
                  native=metadata,central_symmetry_and_transpose=symmetries,
                  elapsed_seconds=time.monotonic()-start,
                  scope='Complete queen-pattern clique census; every remaining8/9 coloring; exact agreement with colored DLX2. Digit permutations and the book first-row reflection restriction are explicit.')
    (OUT/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['status'],native=metadata['statistics'],seconds=result['elapsed_seconds']),indent=2))


if __name__ == '__main__':
    main()

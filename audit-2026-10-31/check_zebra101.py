"""Complete zebra-puzzle XCC models versus independent category permutations."""
from itertools import permutations
from collections import Counter
from colored_dlx import ColoredDLX
from puzzle_xcc import ROOT, OUT, encode, native, read_models, colors_for, save, sha

CATEGORIES = dict(N=['England', 'Japan', 'Norway', 'Spain', 'Ukraine'],
                  J=['painter', 'diplomat', 'violinist', 'sculptor', 'nurse'],
                  P=['dog', 'snails', 'horse', 'fox', 'zebra'],
                  D=['coffee', 'milk', 'orange', 'tea', 'water'],
                  C=['red', 'yellow', 'green', 'white', 'blue'])


def instance(inverses=False, inverse_only=False):
    rows, clue_sizes = [], []
    def clue(*placements):
        k = len(clue_sizes) + 1
        clue_sizes.append(len(placements))
        for assignment in placements:
            row = [(f'c{k}', 0)]
            for category, value, house in assignment:
                color = CATEGORIES[category].index(value) + 1
                if not inverse_only:
                    row.append((f'{category}{house}', color))
                if inverses:
                    row.append((f'{category}i{color}', house + 1))
            rows.append(row)
    def same(c, value, d, other):
        return [[(c, value, j), (d, other, j)] for j in range(5)]
    def nextto(c, value, d, other):
        return [[(c, value, j), (d, other, j + 1)] for j in range(4)] + [
                [(d, other, j), (c, value, j + 1)] for j in range(4)]
    clue(*same('N', 'England', 'C', 'red'))
    clue(*same('J', 'painter', 'N', 'Japan'))
    clue(*same('C', 'yellow', 'J', 'diplomat'))
    clue(*same('D', 'coffee', 'C', 'green'))
    clue([('N', 'Norway', 0)])
    clue(*same('P', 'dog', 'N', 'Spain'))
    clue([('D', 'milk', 2)])
    clue(*same('J', 'violinist', 'D', 'orange'))
    clue(*[[('C', 'white', j), ('C', 'green', j + 1)] for j in range(4)])
    clue(*same('N', 'Ukraine', 'D', 'tea'))
    clue(*nextto('N', 'Norway', 'C', 'blue'))
    clue(*same('J', 'sculptor', 'P', 'snails'))
    clue(*nextto('P', 'horse', 'J', 'diplomat'))
    clue(*nextto('J', 'nurse', 'P', 'fox'))
    clue(*[[('P', 'zebra', j)] for j in range(5)])
    clue(*[[('D', 'water', j)] for j in range(5)])
    assert clue_sizes == [5,5,5,5,1,5,1,5,4,5,8,5,8,8,5,5]
    secondary = [] if inverse_only else [f'{c}{j}' for j in range(5) for c in CATEGORIES]
    if inverses:
        secondary += [f'{c}i{i}' for c in CATEGORIES for i in range(1,6)]
    return encode([f'c{k}' for k in range(1,17)], secondary, rows)


def permutation_oracle():
    """Positions per attribute, all-different by construction; no XCC machinery."""
    solutions = []
    perm = list(permutations(range(5)))
    for red, yellow, green, white, blue in perm:
        if green != white + 1 or blue != 1:
            continue
        for england, japan, norway, spain, ukraine in perm:
            if norway != 0 or england != red:
                continue
            for coffee, milk, orange, tea, water in perm:
                if coffee != green or milk != 2 or tea != ukraine:
                    continue
                for painter, diplomat, violinist, sculptor, nurse in perm:
                    if painter != japan or diplomat != yellow or violinist != orange:
                        continue
                    for dog, snails, horse, fox, zebra in perm:
                        if dog != spain or snails != sculptor or abs(horse-diplomat) != 1 or abs(fox-nurse) != 1:
                            continue
                        categories = [(england,japan,norway,spain,ukraine),
                                      (painter,diplomat,violinist,sculptor,nurse),
                                      (dog,snails,horse,fox,zebra),(coffee,milk,orange,tea,water),
                                      (red,yellow,green,white,blue)]
                        solutions.append(tuple(tuple(values.index(j) for values in categories) for j in range(5)))
    return set(solutions)


class NoEvents(list):
    def append(self, item):
        pass


def main():
    expected = permutation_oracle()
    assert len(expected) == 1
    runs = []
    for inv in [False, True]:
        enc = instance(inv)
        solver = ColoredDLX(len(enc['names']), enc['primary'], enc['rows'])
        solver.events = NoEvents()
        solver.solve()
        label = 'zebra-inverse' if inv else 'zebra-direct'
        result = native(label, enc)
        assert result['status'] == 'completed'
        models = read_models(label, enc)
        assert models == solver.solutions
        actual = set()
        for model in models:
            colors = colors_for(enc, model)
            actual.add(tuple(tuple(colors[f'{c}{j}']-1 for c in CATEGORIES) for j in range(5)))
        assert actual == expected
        assert sum(solver.profile.values()) == result['nodes']
        runs.append(dict(variant=label, options=len(enc['rows']), solutions=len(models),
                         nodes=result['nodes'], profile=dict(solver.profile),
                         initial_mems=result['initial_mems'], search_mems=result['net_search_mems']))
    # Inverses alone allow two nationalities at the same house. An explicit
    # assignment satisfying every clue supplies a short independent witness.
    inv = dict(N=[0,0,0,0,0], J=[0,1,0,0,0], P=[0,0,0,1,0],
               D=[1,2,0,0,0], C=[0,1,1,0,1])
    enc = instance(True, True)
    model = []
    for k in range(1,17):
        options=[]
        for ri,row in enumerate(enc['rows']):
            if row[0][0] != k:
                continue
            if all(inv[enc['names'][i-1][0]][int(enc['names'][i-1][2:])-1]+1 == color for i,color in row[1:]):
                options.append(ri)
        assert len(options)==1,(k,options)
        model.extend(options)
    colors_for(enc,model)
    house_rows = [[CATEGORIES[c][x] for c,x in zip(CATEGORIES,house)] for house in next(iter(expected))]
    result = dict(script_sha256=sha(__file__), runs=runs, categories=list(CATEGORIES),
                  unique_house_rows=house_rows, inverse_only_counterexample=inv,
                  independent_oracle='All category permutations, directly filtered by the fourteen clues; zebra and water in the domains.',
                  counts_match_book=[r['nodes'] for r in runs] == [112,32])
    save(OUT/'zebra-checked.json',result)
    print(result)


if __name__ == '__main__':
    main()

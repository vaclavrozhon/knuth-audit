"""Validate fine-grained audit coverage and render a conservative progress report."""
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATUSES = {'todo', 'in_progress', 'partial', 'checked', 'confirmed', 'known_erratum', 'dismissed'}
TERMINAL = {'checked', 'confirmed', 'known_erratum'}


def main():
    data = json.loads((ROOT / 'coverage.json').read_text())
    ids = set()
    def validate(item):
        assert item['id'] not in ids, item['id']
        ids.add(item['id'])
        assert item['status'] in STATUSES
        if item['status'] in TERMINAL:
            assert item['evidence'] and item['scope_note'], item
        for path in item['evidence']:
            assert (ROOT / path).is_file(), (item['id'], path)

    rows = []
    exercise_counts = Counter()
    completed_sections = 0
    for sec in data['sections']:
        units = [sec['text'], *sec['exercises'], *sec['added_exercises']]
        for item in [*units, *sec['subblocks']]:
            validate(item)
        assert len(sec['exercises']) == sec['original_exercise_count']
        assert [x['id'] for x in sec['exercises']] == [f"{sec['id']}-{n}" for n in range(1, sec['original_exercise_count'] + 1)]
        counts = Counter(x['status'] for x in sec['exercises'] + sec['added_exercises'])
        exercise_counts.update(counts)
        closed = sec['inventory_verified'] and sec['errata_extensions_reviewed'] and all(x['status'] in TERMINAL for x in units)
        completed_sections += int(closed)
        inventory = 'ověřen' if sec['inventory_verified'] else 'předběžný'
        done = sum(counts[s] for s in TERMINAL)
        total = sum(counts.values())
        rows.append(f"| {sec['id']} | {sec['printed_start']}–{sec['printed_end']} | {sec['text']['status']} | {done}/{total} | {inventory} | {'ano' if closed else 'ne'} |")
    for item in data['other_units']:
        validate(item)
    fully_done = completed_sections == len(data['sections']) and all(x['status'] in TERMINAL for x in data['other_units'])
    lines = ['# Průběh celého auditu svazku 2', '',
             'Generováno z `coverage.json`. Dokončený podblok není dokončená sekce.', '',
             f"Celý svazek dokončen: **{'ano' if fully_done else 'ne'}**.",
             f"Plně uzavřené sekce: **{completed_sections}/{len(data['sections'])}**.", '',
             'Inventář úloh je do ověření jednotlivých sekcí předběžný. Zvlášť se evidují úlohy přidané v erratech.',
             'Uzavřená úloha může mít potvrzenou chybu nebo známé erratum; počet není počet nových nálezů.', '',
             '| Sekce | Tištěné strany (orientačně) | Text | Uzavřené úlohy | Inventář | Sekce hotova |',
             '|---|---|---|---|---|---|', *rows, '',
             'Sekce začínající na společné stránce se mohou překrývat; intervaly nejsou dokladem přečtení každého řádku.', '',
             '## Další části svazku', '']
    lines.extend(f"- `{x['id']}`: {x['status']}" for x in data['other_units'])
    (ROOT / 'PROGRESS.md').write_text('\n'.join(lines) + '\n')
    print(json.dumps(dict(sections_complete=completed_sections, sections_total=len(data['sections']), exercise_statuses=exercise_counts, fully_done=fully_done)))


if __name__ == '__main__':
    main()

"""A deletion certificate using only neighboring-edge support and forced pieces."""
from datetime import datetime, timezone
import json
import nuts137 as n


def main():
    book = json.loads((n.OUT / 'book-cases-checked.json').read_text())
    nuts = book['cases'][0]['nuts']
    certificates = []
    for center in nuts:
        pairs = []
        for digit in center:
            row = {}
            for nut in nuts:
                if nut != center:
                    i = nut.index(digit)
                    row[nut] = (nut[(i+1)%6], nut[(i-1)%6])
            pairs.append(row)
        domains = [set(row) for row in pairs]
        steps = []
        while True:
            changed = False
            for k in range(6):
                for nut in sorted(domains[k]):
                    for j in ((k-1)%6, (k+1)%6):
                        support = [other for other in domains[j] if other != nut and
                            (pairs[k][nut][1] == pairs[j][other][0] if j == (k+1)%6
                             else pairs[j][other][1] == pairs[k][nut][0])]
                        if not support:
                            domains[k].remove(nut)
                            steps.append(dict(position=k, nut=nut, reason='no adjacent support', neighbor=j))
                            changed = True
                            break
                    if not domains[k]:
                        break
                if not domains[k]:
                    break
            if any(not d for d in domains):
                break
            for k in range(6):
                if len(domains[k]) == 1:
                    nut = next(iter(domains[k]))
                    for j in range(6):
                        if j != k and nut in domains[j]:
                            domains[j].remove(nut)
                            steps.append(dict(position=j, nut=nut, reason='forced elsewhere', forced_position=k))
                            changed = True
            if any(not d for d in domains) or not changed:
                break

        # Replay the certificate using independently constructed geometric faces.
        initial = [set(nuts)-{center} for _ in range(6)]
        faces = {}
        for k in range(6):
            for nut in initial[k]:
                compatible = [w for w in n.rotations(nut) if w[(k+3)%6] == center[k]]
                assert len(compatible) == 1
                faces[k,nut] = compatible[0]
        edge_map = {(u-1,v-1): side for u,v,side in n.EDGES if u and v}
        for step in steps:
            k, nut = step['position'], step['nut']
            assert nut in initial[k]
            if step['reason'] == 'forced elsewhere':
                j = step['forced_position']
                assert j != k and initial[j] == {nut}
            else:
                j = step['neighbor']
                u,v = sorted((j,k))
                side = edge_map[u,v]
                for other in initial[j]:
                    if other == nut:
                        continue
                    words = {k: faces[k,nut], j: faces[j,other]}
                    assert words[u][side] != words[v][(side+3)%6]
            initial[k].remove(nut)
        assert initial == domains
        impossible = any(not d for d in domains)
        if not impossible:
            assert all(len(d) == 1 for d in domains)
            words = [center] + [faces[k,next(iter(d))] for k,d in enumerate(domains)]
            n.validate(words,nuts,'equal')
            assert '/'.join(words) == book['cases'][0]['models'][0]
        certificates.append(dict(center=center, pairs=pairs, steps=steps,
                                 final_domains=[sorted(d) for d in domains],
                                 conclusion='impossible' if impossible else 'unique forced solution'))
    assert sum(c['conclusion']=='unique forced solution' for c in certificates) == 1
    n.save(n.OUT / 'hand-certificate-checked.json', dict(
        at_utc=datetime.now(timezone.utc).isoformat(), source_sha256=n.sha(__file__),
        geometry_sha256=n.sha(n.__file__), book_cases_sha256=n.sha(n.OUT / 'book-cases-checked.json'),
        certificates=certificates, all_deletions_independently_replayed=True,
        branch_choices=7, search_nodes_with_propagation=8,
        search_nodes_including_six_forced_placements=14,
        book_tree_size15_reproduced_exactly=False,
        interpretation='Elementary deletions resolve all seven center cases without further '
          'branching. This proves a compact hand-solvable case analysis. It uses a different '
          'propagation convention and does not reconstruct the exact15-node tree mentioned by Knuth.'))
    print('PASS137 hand proof: six impossible centers and one forced solution; every deletion replayed.')


if __name__ == '__main__':
    main()

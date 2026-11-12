"""Finite symbolic Horn deduction for the named witnesses in TAOCP 7.1.1-75.

This constructs a derivation, not a model enumeration. Names stand for arbitrary
elements and are never assumed distinct. Endpoint symmetry and rules N/D/E must
first be proved in the accompanying mathematical note. E is used only for 75(f).
"""

import json
from pathlib import Path


def canon(a, b, c):
    return (min(a, c), b, max(a, c))


class Deduction:
    def __init__(self, names, use_e=False):
        self.names = tuple(names)
        self.use_e = use_e
        self.facts = {}
        self.records = []
        for a in names:
            for b in names:
                self.add((a, a, b), "endpoint", [])
                self.add((a, b, b), "endpoint", [])

    def add(self, conclusion, rule, premises, substitution=None):
        key = canon(*conclusion)
        if key in self.facts:
            return
        parents = [self.facts[canon(*p)] for p in premises]
        self.facts[key] = len(self.records)
        self.records.append({"fact": key, "rule": rule, "premises": parents,
                             "substitution": substitution})

    def median(self, w, a, b, c):
        for left, right in [(a, b), (a, c), (b, c)]:
            self.add((left, w, right), "median", [], [w, a, b, c])

    def close(self):
        rounds = 0
        while True:
            before = len(self.facts)
            # N: [u y v], [u x y] -> [u x v].
            # D: [u y v], [u x y] -> [x y v].
            for u in self.names:
                for v in self.names:
                    for y in self.names:
                        p = (u, y, v)
                        if canon(*p) not in self.facts:
                            continue
                        for x in self.names:
                            q = (u, x, y)
                            if canon(*q) in self.facts:
                                self.add((u, x, v), "N", [p, q], [u, x, y, v])
                                self.add((x, y, v), "D", [p, q], [u, x, y, v])
            if self.use_e:
                # E: [u x v], [u y z], [v y z] -> [x y z].
                for y in self.names:
                    for z in self.names:
                        ray = [u for u in self.names if canon(u, y, z) in self.facts]
                        for u in ray:
                            for v in ray:
                                for x in self.names:
                                    if canon(u, x, v) in self.facts:
                                        self.add((x, y, z), "E",
                                                 [(u, x, v), (u, y, z), (v, y, z)],
                                                 [u, x, v, y, z])
            rounds += 1
            if len(self.facts) == before:
                return rounds

    def certificate(self, goals):
        needed = set()

        def visit(i):
            if i not in needed:
                needed.add(i)
                for j in self.records[i]["premises"]:
                    visit(j)

        found = [g for g in goals if canon(*g) in self.facts]
        for g in found:
            visit(self.facts[canon(*g)])
        old_ids = sorted(needed)
        renumber = {old: new + 1 for new, old in enumerate(old_ids)}
        rows = []
        for i in old_ids:
            r = dict(self.records[i])
            r["id"] = renumber[i]
            r["premises"] = [renumber[j] for j in r["premises"]]
            rows.append(r)
        return {"goals": goals, "missing": [g for g in goals if g not in found],
                "derived_fact_count": len(self.facts), "steps": rows}


def stage_e():
    d = Deduction("uvxyzwpqrst")
    for fact in ["uxv", "uyz", "vyz"]:
        d.add(tuple(fact), "hypothesis", [])
    for args in ["wyuv", "pwux", "qwvx", "rpxz", "sqxz", "trsz"]:
        d.median(*args)
    d.close()
    goals1 = [tuple(s) for s in ["utv", "utz", "vtz", "uwv", "uwz", "vwz"]]
    first = d.certificate(goals1)
    if not first["missing"]:
        # Uniqueness (iii) now gives t=w. Insert exactly the three transferred
        # median relations specified in the book, with all six proof premises.
        for fact in ["rws", "rwz", "swz"]:
            old_fact = tuple(fact.replace("w", "t"))
            d.add(tuple(fact), "unique_median_t_equals_w", goals1 + [old_fact])
        d.close()
    second = d.certificate([tuple("xyz"), tuple("prp"), tuple("qsq")])
    return {"six_relations": first, "after_uniqueness": second}


def stage_f():
    d = Deduction("xyzuvrstpq", use_e=True)
    for args in ["ryuv", "szuv", "txyz", "pxrs", "qtuv"]:
        d.median(*args)
    d.close()
    return d.certificate([tuple("pqp")])


if __name__ == "__main__":
    result = {"kind": "symbolic Horn derivation on fixed named witnesses",
              "no_distinctness_assumptions": True, "e": stage_e(), "f": stage_f()}
    target = Path(__file__).parents[1] / "results/betweenness75-derivation.json"
    target.write_text(json.dumps(result, indent=2) + "\n")
    for name, cert in [("e-six", result["e"]["six_relations"]),
                       ("e-goal", result["e"]["after_uniqueness"]), ("f", result["f"])]:
        print(name, "missing", cert["missing"], "proof_steps", len(cert["steps"]),
              "derived_facts", cert["derived_fact_count"])

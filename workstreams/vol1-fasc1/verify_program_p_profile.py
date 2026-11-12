#!/usr/bin/env python3
"""Derive Program P profiles from the saved exact prime certificate.

No MMIX program is executed and no sieve is repeated. For composite n,
the saved least prime divisor decides the stopping point. For prime n,
the proved q<=p condition is n<p*(p+1). Each candidate contributes a
closed-form number of visited divisors and branch outcomes.
"""
import json
import os
from pathlib import Path

BASE = Path(__file__).resolve().parent


def main():
    assert os.getpriority(os.PRIO_PROCESS, 0) >= 15, "Use nice -n 15."
    cert = json.loads((BASE / "results/printed-prime-indices.json").read_text())
    primes = cert["all_primes_through_last_entry"]
    least_divisor = dict(cert["composite_divisor_witnesses"])
    rank = {p: i + 1 for i, p in enumerate(primes)}
    candidates = []
    for n in range(5, primes[-1] + 1, 2):
        if n in least_divisor:
            p = least_divisor[n]
            stop = "zero remainder"
        else:
            p = next(p for p in primes[1:] if n < p * (p + 1))
            stop = "q<=p with nonzero remainder"
        count = rank[p] - 1  # odd prime divisors only
        candidates.append(dict(n=n, stop_divisor=p, tests=count, stop=stop))
    T = sum(x["tests"] for x in candidates)
    C = sum(x["stop"] == "zero remainder" for x in candidates)
    A = len(candidates) - C
    D = sum(len(str(p)) for p in primes)
    assert (len(candidates), T, C, A, D) == (1784, 9538, 1286, 498, 1803)
    rows = []

    def add(line, mnemonic, executions, mems=0, cost=1, mispredictions=0):
        rows.append(dict(line=line, mnemonic=mnemonic, executions=executions,
                         mems=mems * executions,
                         oops=cost * executions + 2 * mispredictions,
                         mispredictions=mispredictions))

    add(19, "SET n,3", 1)
    add(20, "SET jj,j0", 1)
    add(21, "STWU n,ptop,jj", 499, mems=1)
    add(22, "INCL jj,2", 499)
    add(23, "BZ jj,2F", 499, mispredictions=1)
    add(24, "INCL n,2", A + C)
    add(25, "SET kk,j0", A + C)
    add(26, "LDWU pk,ptop,kk", T, mems=1)
    add(27, "DIV q,n,pk", T, cost=60)
    add(28, "GET r,rR", T)
    add(29, "BZ r,4B", T, mispredictions=C)
    add(30, "CMP t,q,pk", T - C)
    add(31, "BNP t,2B", T - C, mispredictions=A)
    add(32, "INCL kk,2", T - C - A)
    add(33, "JMP 6B", T - C - A)
    add(38, "LDA t,Title", 1)
    add(39, "TRAP Fputs title", 1, cost=5)
    add(40, "NEG mm,2", 1)
    add(41, "ADD mm,mm,j0", 50)
    add(42, "LDA t,Blanks", 50)
    add(43, "TRAP Fputs blanks", 50, cost=5)
    add(44, "LDWU pk,ptop,mm", 500, mems=1)
    add(46, "STOU 0B,BUF", 500, mems=1)
    add(47, "LDA t,BUF+4", 500)
    add(48, "DIV pk,pk,10", D, cost=60)
    add(49, "GET r,rR", D)
    add(50, "INCL r,'0'", D)
    add(51, "STBU r,t,0", D, mems=1)
    add(52, "SUB t,t,1", D)
    add(53, "PBNZ pk,1B", D, mispredictions=500)
    add(54, "LDA t,BUF", 500)
    add(55, "TRAP Fputs number", 500, cost=5)
    add(56, "INCL mm,100", 500)
    add(57, "PBN mm,2B", 500, mispredictions=50)
    add(58, "LDA t,NewLn", 50)
    add(59, "TRAP Fputs newline", 50, cost=5)
    add(60, "CMP t,mm,98", 50)
    add(61, "PBNZ t,3B", 50, mispredictions=1)
    add(62, "TRAP Halt", 1, cost=5)
    stages = []
    for low, high, label in [(19, 33, "P1–P8"), (38, 62, "P9–P11")]:
        selected = [r for r in rows if low <= r["line"] <= high]
        stages.append(dict(stage=label, mems=sum(r["mems"] for r in selected),
                           oops=sum(r["oops"] for r in selected)))
    assert [(s["mems"], s["oops"]) for s in stages] == [(10037, 641543), (2803, 124559)]
    result = dict(scope="Exact mathematical profiles of printed Program P under Table 1 costs; excludes operating-system TRAP handler time.",
                  source_certificate="results/printed-prime-indices.json",
                  derivation="notes/MMIX-C0016-program-p-mems.md",
                  division_tests=T, composite_candidates=C, prime_candidates=A,
                  decimal_digits=D, stages=stages, instruction_rows=rows,
                  candidate_stopping_certificates=candidates)
    (BASE / "results/program-p-profile.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"division_tests": T, "decimal_digits": D, "stages": stages}, ensure_ascii=False))


if __name__ == "__main__":
    main()

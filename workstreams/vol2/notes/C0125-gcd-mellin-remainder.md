# V2-C0125 — exponenciální zbytek v odpovědi 28

Stav: **confirmed**. §4.5.2-28, str.644, věta po Mellinově integrálu.
Originály643–644 zobrazeny. Odpověď definuje

```text
tau(n)=sum_{j>=1}4^-j/(exp(n/2^j)-1)
```

a správně uvádí `4tau(2n)-tau(n)=1/(exp(n)-1)>0`.
Následně tvrdí, že integrál pro tau(n) je součtem reziduí, tedy
n^-2 krát periodická funkce log2(n) s periodou1. To nemůže být
přesná rovnost: taková funkce by splňovala `4tau(2n)-tau(n)=0`.
Spor platí pro každé kladné n a nevyžaduje numeriku.

Přesná oprava je

```text
tau(n)=n^-2 Q(log2 n)-R(n),
R(n)=sum_{r>=0}4^r/(exp(2^r n)-1)>0,
Q(t)=pi²/(6ln2)+2 Re sum_{k>=1}
     Gamma(2+2pi i k/ln2)zeta(2+2pi i k/ln2)exp(-2pi i k t)/ln2.
```

Zde Q je právě periodický člen odpovědi a R(n)=O(exp(-n)).
Identitu lze dokázat rozšířením dyadického součtu na všechny
celočíselné j a odečtením členů j<=0; Fourierovy koeficienty
oboustranného součtu jsou uvedené součiny Gamma a zeta.
Doklad všech kroků je v `gcd-model.md`.

Nejmenší textová oprava je změnit přesnou rovnost na asymptotickou
rovnost s chybou O(exp(-n)); pro úplnou přesnost lze uvést -R(n).
Hlavní závěr úlohy, psi_n=Theta(n^-2), i periodický asymptotický
člen zůstávají správné. Tvrzení neposuzujeme jako omyl v samotném
hlavním výsledku, ale jako chybnou přesnou identitu v jeho odvození.

Další odhad pro S_n(m)-T_n(m) na643 není uniformní v m ve své
tištěné podobě. V souvislé poznámce je nahrazen uniformní majorantou,
která rigorózně ospravedlňuje výslednou chybu O(n^-3). Není veden
jako další samostatný nález; výše uvedený škálovací spor stačí.

Čtyři řady errat `all2-prepre`, `all2-pre`, `all2`, `err2`
prohledány2026-11-02 podle stran643/644, čísla úlohy a reziduí;
oprava nenalezena. Fyzický dotisk/priorita neověřeny, neodesláno.

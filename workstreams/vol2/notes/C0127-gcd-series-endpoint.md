# V2-C0127 — poslední rozvoj v odpovědi30 diverguje při x=1

Stav: **confirmed**. §4.5.2-30, str.645, společný obor rozvojů
a čtvrtá řada pro Sigma2(1/x). Originál vizuálně přečten.
Text uvádí 0<=x<=1, ale poslední řada při x=1 nekonverguje
v běžném smyslu. Její členy nejdou k nule.

Z definice bhat(k) na téže straně, po změně indexu r=k-1-j,

```text
-bhat(k)=sum_{r=1}^{k-1}binom(k-1,r)/(1-2^-r)
        =2^(k-1)-1+E_k,
0<=E_k<=2((3/2)^(k-1)-1).
```

Tedy -bhat(k)/(2^(k+1)-1)->1/4. Ostatní neperiodické členy
závorky mají po vydělení 2^(k+1)-1 nulovou limitu. Periodický
člen P_k(t) je rovněž uniformně omezen v k,t: pro w=2pi m/ln2
platí |binom(k-1-iw,k-1)|<=exp(pi*w/2), takže faktor
1/sinh(pi*w) dává sčitatelnou majorantu nezávislou na k.
Podrobné odvození této meze je v `gcd-second.md`.

K-tý člen posledního rozvoje při x=1 je tedy

```text
(-1)^k*(1/4+o(1)).
```

Poslední řadu je nutné omezit na 0<x<1, případně výslovně
označit x=1 jako Abelův limit součtů při přiblížení zleva.
Samotná funkce Sigma2(1/x) má konečný limit a ostatní tři
uvedené řady v x=1 konvergují. C0126 opravuje jinou, nezávislou
vadu bodů derivací; zde divergence trvá i po této opravě.

Přesné binomické meze a numerické hraniční členy k=10..160 jsou
v `results/gcd-second.json`; poslední uvedený člen je
0.250000000000000000003409423011. Potvrzení je založeno na
obecném důkazu, nikoli na konečném experimentu.

Všechny čtyři vrstvy errat prohledány2026-11-02 podle stran,
úlohy30 a oboru rozvojů, oprava nenalezena. Aktuální fyzický
dotisk/prvenství neověřeny. Návrh neodeslán.

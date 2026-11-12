# V2-C0024: nulová mezera se musí přičíst

**Confirmed**, 1.11.2026. §3.3.2-28(c), odpověď str.568,
třetí vydání, první dotisk1997. Původní obraz568 vizuálně
potvrzuje minus před druhým členem vzorce.

p_n(M) je počet particí M na nejvýše n částí; pro M<0 je0.
Narozeninový test rozděluje n označených pozorování do m dnů
a R počítá opakované délky kruhových mezer. Pro R=0 mohou
nastat dvě disjunktní možnosti: žádná nulová mezera nebo právě
jedna nulová mezera. Z28(a,b) proto plyne

```text
Pr(R=0) = n!(n−1)! m^(1−n)
 [p_n(m−binom(n+1,2)) + (1/2)p_(n−1)(m−binom(n,2))].
```

Tištěné minus je nutné změnit na plus. Při n=2,m=3 má všech
devět dvojic buď mezery0,3, nebo1,2. Nikdy se nerovnají, takže
správná pravděpodobnost je1. Tištěný výraz dává
2/3·(1−1/2)=1/3; opravený2/3·(1+1/2)=1.

Obecná bijekce i nezávislá enumerace219456 slov ve42 modelech
jsou v `birthday-spacings.md` a `verify_birthday_spacings.py`.
Číselná tabulka na71 je správná: certifikát pro n512,m2^25
rozděluje její pravděpodobnost R=0 na kladné příspěvky
0.3673609563213909... a0.001440620776529986..., které se sčítají.

Všechny historické a aktuální vrstvy errat i TeX prohledány
1.11.2026 podle568, odpovědi28 a birthday spacings. Oprava
nenalezena. Nejnovější fyzický dotisk ani prvenství neověřeny;
draft neodeslán.

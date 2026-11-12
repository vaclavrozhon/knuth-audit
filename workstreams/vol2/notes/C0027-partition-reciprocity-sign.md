# V2-C0027: v reciprocitě particí chybí faktor závislý na paritě

**Confirmed**, 1.11.2026. §3.3.2-30, str.569, předposlední
odstavec; třetí vydání, první dotisk1997. Původní sazba569
vizuálně potvrzuje q_n(m)=p_n(−m) bez znaménkového faktoru.

p_n(m) počítá partice m na nejvýše n částí, q_n(m) partice
na n různých kladných částí. Hodnota p_n(−m) se podle okolního
textu chápe jako pokračování kvazipolynomu: konečné kombinace
polynomů v m a mocnin kořenů jednotky. Není to kombinatorický
počet rozkladů záporného čísla.

Pro n=2 je toto pokračování přesně

```text
p_2(m) = m/2+3/4+(−1)^m/4.
```

Máme q_2(3)=1 (partice1+2), ale p_2(−3)=−1. Správná identita
pro kladná celá m je

```text
q_n(m) = (−1)^(n−1) p_n(−m).
```

Faktor je již přítomen v bezprostředně předcházející identitě
pro r_n, ale při přechodu na p_n,q_n se ztratil.

## Přímý důkaz

Označme F(z)=prod_(j=1)^n(1−z^j)^(-1), N=n(n+1)/2.
Platí F(1/z)=(−1)^n z^N F(z) a q_n(m)=p_n(m−N).
Rozložme F na parciální zlomky a/(1−z/zeta)^k. Jejich
koeficienty jsou a zeta^(−m) binom(m+k−1,k−1).
Při pokračování na−m používáme

```text
binom(−m+k−1,k−1) = (−1)^(k−1) binom(m−1,k−1).
```

Rozvoj téhož zlomku po substituci1/z má koeficient
a(−1)^k zeta^m binom(m−1,k−1). Pro m>0 je tedy
[z^m]F(1/z)=−p_n(−m)=(−1)^n q_n(m), jak bylo třeba.

`certify_birthday_table.py` ověřil racionální generující identitu
pro n=1..10 a explicitní kvazipolynom pro m=1..49 při n=2.
Obecný důkaz výše na těchto konečných kontrolách nezávisí.
Asymptotická záměna alpha za−alpha v odpovědi30 zůstává správná:
chybějící faktor právě ruší znaménko mocniny(−m)^(n−1).

Všechny vrstvy errat a aktuální TeX prohledány1.11.2026 podle
str.569, duality a odpovědi30. Oprava nenalezena. Nejnovější
fyzický dotisk ani prvenství neověřeny; draft neodeslán.

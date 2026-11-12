# §4.5.4–24, 26, 27: pevné seznamy a částečná faktorizace

> Sekvenční doplnění6.11.2026: celé24 a27 jsou nyní partial kvůli výzkumnému dodatku24 a neprokázané obecné záruce jednoslovního hledání v dodatku27. Hlavní důkazy a certifikáty níže zůstávají uzavřené.

Úlohy **24, 26 a 27 jsou uzavřeny**. V úloze 24 je opraven chybný
mezikrok počítání řádku (**C0156**), závěrečná věta platí. Prothova
formulace v úloze 27 potřebuje výjimku pro prvočíslo 3 (**C0157**).
Všech 57 uvedených prvočísel včetně doplnění 2024 má vlastní certifikát;
úplnost seznamu do 300000 je doložena externím primárním přehledem
Ballingera a Kellera. Rozsah historické kontroly včetně nově získaného
Prothova originálu uvádí [proth-history.md](proth-history.md).

## 1. Úloha 24: jeden seznam pro všechny vstupy do N

Pro liché `n>1` řekneme, že základ `x` projde rozšířeným testem,
pokud `x mod n=0` nebo jeho zbytek přijme silný test P. Nulu kniha
výslovně připouští, aby například testování pevné základny dělitelné
prvočíslem nevedlo k jeho odmítnutí. Zbytek 1 také vždy projde.
Nechť `b(n)` je počet přijímaných **nenulových** zbytků `1<=x<n`.
Pro liché složené `n` již máme obecný důkaz
`b(n)<=(n-1)/4`; viz [úloha 22](primality-probabilistic.md), §2–3.

Matice má řádky odpovídající lichým složeným `n<=N` a sloupce
`x=2,...,N`. Jednička značí odmítnutí, nula přijetí. Každý řádek
má alespoň polovinu jedniček. Je třeba počítat **N-1** sloupců
a nepřidat řádek pro `n=1`, který zadání vylučuje.

Položme `N=qn+r`, `0<=r<n`; pak `q>=1`. V každé úplné periodě
projde `b+1` zbytků včetně nuly. Zbytkový interval `1,...,r`
neobsahuje nulu modulo `n`, takže v něm projde nejvýše `min(b,r)`
základen. Po odstranění sloupce 1 je počet nul `Z` omezen takto:

```
Z <= q(b+1)+min(b,r)-1
  <= qn/3+min(n/4,r)-1
   = N/3+min(n/4-r/3,2r/3)-1
  <= N/3+n/6-1
  <= N/2-1.
```

Druhá nerovnost používá `n>=9`, tedy `(n+3)/4<=n/3`.
Maximum uvedeného minima je `n/6`, dosažené při `r=n/4`.
Řádek tudíž obsahuje alespoň `(N-1)/2` jedniček.

**V tištěném řetězci se ztrácí -1 a zbytkový člen je nadhodnocen
na min(b+1,r).** Pro `n=9,N=12,q=1,r=3,b=2` dává jeden krok
`6<=21/4`, což neplatí. Skutečně projdou jen sloupce 8, 9, 10.
Oprava výše zachovává původní strategii. Viz [C0156](C0156-witness-matrix-bound.md).

Průměrováním přes sloupce existuje sloupec, který odmítne alespoň
polovinu zbývajících řádků. Vybereme jej a tyto řádky odstraníme.
Ve zbývajících řádcích byl vybraný sloupec nula, takže jeho
odstranění nezmenší počet jedniček; vlastnost alespoň polovičního
zastoupení jedniček se zachová. Opakováním tedy po `m` krocích
zbývá nejvýše `R/2^m` řádků, kde počáteční počet `R<N/2`.
Pro `m=floor(lg N)` je `R/2^m<1`, a tedy nezbude žádný řádek.
Prvočísla projdou všemi sloupci. Pro malé `N` bez složeného
lichého vstupu je prázdný seznam postačující.

Tento důkaz ukazuje existenci seznamu, nikoli rychlý algoritmus
jeho nalezení. Právě tak je formulováno zadání. Označení
**neuniformní** znamená, že pro každý horní limit `N` smíme
použít jiný předem připravený seznam.

## 2. Jedna nekonečná rostoucí posloupnost

Dokážeme také doprovodné tvrzení s počtem
`m(n)=floor(lg n)(floor(lg n)-1)/2`. Stejně jako zadání se tento
test týká lichých `n>1`; sudá čísla a číslo 2 se vyřídí přímo.

Pro celé `h>=3` položme `T=2^(h+1)-1` a `L=lcm(1,...,T)`.
Rovnoměrný zbytek modulo `L` je rovnoměrný modulo každý `n<=T`.
Liché složené `n` přijme s pravděpodobností

```
(b(n)+1)/n <= (n+3)/(4n) <= 1/3.
```

Zvolíme-li `h-1` takových nezávislých zbytků, pravděpodobnost,
že některé liché složené `n<=T` projde všemi, je menší než
`2^h/3^(h-1)<1`. Existuje tedy blok `h-1` základen, který vyřídí
celý tento rozsah. Každý základ můžeme zvětšit o vhodný násobek
`L`, aniž změníme jediný test v rozsahu. Tím je každý blok
i celá posloupnost striktně rostoucí, včetně případných původně
opakovaných zbytků.

Začneme libovolným jedním základem pro `h=2` (lichá čísla mezi
4 a 7 jsou prvočísla) a připojujeme bloky pro `h=3,4,...`.
Prvních `1+2+...+(h-1)=h(h-1)/2` základen vyřídí všechna
lichá `n` s `floor(lg n)=h`. Pro `h=1` stačí prázdný seznam.
Velikosti základen tento důkaz neomezuje. Otázka, zda stačí
`m=O(log n)` pro jedinou posloupnost, je v knize výzkumná otázka;
zde ji neřešíme ani netvrdíme její aktuální otevřenost.

## 3. Úloha 26: Pocklingtonovo kritérium

Nechť `N=fr+1`, kde `f,r` jsou kladná celá čísla. Známe
prvočíselné dělitele `p` čísla `f`. Pro každý takový `p` předpokládejme
základ `x_p` splňující

```
x_p^(N-1) = 1 (mod N),
gcd(x_p^((N-1)/p)-1,N) = 1.
```

Pro libovolný prvočinitel `q|N` je `x_p` invertibilní modulo `q`.
Jeho řád dělí `N-1`, ale nedělí `(N-1)/p`; jinak by druhý výraz
měl s `N` společný dělitel `q`. Proto řád obsahuje **celou** mocninu
`p` z `N-1`, zejména alespoň mocninu `p` obsaženou v `f`.
Lagrangeova věta říká, že řád dělí `q-1`; dohromady tedy `f|q-1`
a `q>=f+1`. Není nutné konstruovat jediný společný generátor.

Bylo-li by `N` složené, mělo by prvočinitel `q<=sqrt(N)`. Pro
`r<=f+1` ale

```
N=fr+1 <= f^2+f+1 < (f+1)^2 <= q^2 <= N,
```

což je spor. To je přesně tištěný rozsah `r<=f+1`. Pro `f=1`
je podmínka o prvočinitelích prázdná, ale rozsah dovoluje jen
`N=2,3`, tedy žádný problém s prázdnou množinou svědků nevzniká.
Při opětovném vizuálním čtení str. 414 dne 3. listopadu 2026 byl
opraven náš předchozí přepis `<` místo `<=`; obecný důkaz i všechny
vypočtené případy už neostrou hranici zahrnovaly.

Prvočíslo všechny požadované svědky má: stačí generátor cyklické
grupy modulo `N`. Kritérium proto nepotřebuje kompletní rozklad
`N-1`; stačí vhodně velká známá část. Aplikace na `n_4=1653701519`,
známou část `23*1973=45379` a základ 2 na str. 394 již byla přesně
certifikována v [primality-basic.md](primality-basic.md); úspěšné
numerické kongruence se znovu nepočítaly.

## 4. Úloha 27: Prothův test a malé výjimky

Použijeme `e` pro exponent, aby se nepletl s testovaným číslem:
`N=k*2^e+1`, kde `e>=1`, `k>=1`, `3` nedělí `k` a `k<=2^e+1`.
Pro `N>3` platí

```
N je prvočíslo  <=>  3^(k*2^(e-1)) = -1 (mod N).
```

Zprava doleva: řád základu 3 modulo každý prvočinitel `q|N`
obsahuje alespoň `2^e`; proto `q>=2^e+1`. Složené `N` by mělo
`q<=sqrt(N)`, což odporuje
`N<=2^e(2^e+1)+1<(2^e+1)^2`. Tento argument také pokrývá
kraj `k=2^e+1`, který je zahrnut také v tištěném neostrém
předpokladu úlohy 26, dokázaném v §3.

Zleva doprava: pro `e>=2` je prvočíslo `N>3` rovno 1 modulo 4.
Protože `3` nedělí `k` a `N` není dělitelné 3, musí být
`k*2^e=1 (mod 3)`, tedy `N=5 (mod 12)`. Kvadratická reciprocita
dává `J(3,N)=-1`, a Eulerovo kritérium požadovanou kongruenci.
Pro `e=1` zbývá v uvedeném rozsahu kromě `N=3` jen `k=2,N=5`,
které lze přímo ověřit.

**V knize není výjimka N=3:** povolené `k=1,e=1` dává prvočíslo
3, ale `3^1=0 (mod 3)`, nikoli -1. Nejjednodušší oprava je
přidat `N>3` nebo vyřídit 3 předem. Viz [C0157](C0157-proth-three.md).

Pro původní úkol `5*2^e+1` je kritérium se základem 3 použitelné
pro `e>=2`; hodnotu `e=1`, tedy prvočíslo 11, vyřídíme přímo.
Umocníme nejprve na malý exponent 5 a potom provedeme `e-1`
modulárních čtverců. Počet je tedy `e+O(1)`, jako u Lucasova–
Lehmerova testu. Nejde o tvrzení o shodném naměřeném čase.

Pro `3*2^e+1` lze použít libovolný základ s Jacobiho symbolem -1.
Při hledání je třeba reagovat i na symbol 0: vlastní společný
dělitel už dokazuje složenost. Bez této větve by například pro
`e=4,N=49` hledání záporného Jacobiho symbolu nemohlo skončit.
Pro `e mod 4` rovno 1 nebo 2 funguje základ 5 reciprocitou;
pro zbytek 3 číslo přímo dělí 5 a tentýž kongruenční test je
správně odmítne. Pro zbytek 0 obecně jiný základ potřebujeme.
Záruku existence v předem omezeném jednoslovním rozsahu tento
důkaz nedává; náš ověřovací běh zaznamenává konkrétní svědky.

## 5. Rychlá redukce čtverce

Položme `F=2^e` a pro `0<=x<N=kF+1` pišme `x^2=AF+B`,
`0<=B<F`. Rozložme `A=kt+s`, `0<=s<k`. Protože `kF=-1 (mod N)`,

```
x^2 = B-t+sF (mod N).
```

To je přesně knižní vzorec. Navíc `x<=kF`, tedy `A<=k^2F`,
`t<=kF=N-1`, a výsledné celé číslo `R=B-t+sF` leží v intervalu
`1-N<=R<=N-2`. Stačí tedy jediné přičtení `N`, pokud `R<0`.
Pro pevné malé `k`, zejména 3 a 5, je dělení vysoké části číslem
`k` lineární práce v počtu slov. Vlastní čtverec je dominantní
operace stejně jako u redukce modulo `2^e-1`.

Erratum z 7. 4. 2003 správně mění pouhé jednoslovní `k` na malé
`k` a odkazuje na §4.3.2–14. Nemění modulární identitu.

## 6. Přesné konečné kontroly

[Program](../verify_primality_deterministic.py) má tři samostatné
checkpointy; vše prošlo, PID 1278782, session 70086, limit 180 s,
exit 0. [Výsledek](../results/primality-deterministic.json).

- Úloha 24: 340 složených lichých řádků do 1023, **727824**
  kombinací konce intervalu; opravená mez platí všude. Původní
  mezikrok selže 24krát, poprvé `n=9,N=12`. Pro sedm horních
  limitů do 10000 vytvořeny konkrétní seznamy a nezávisle ověřeny
  přímými mocninami a zkušebním dělením. Pro 4096 a 10000 jsou
  dostačující základy `[2,3]`. Čas 103.023474346 s.
- Úloha 26: **1224** párů `1<=f<=48,1<=r<=f+1`, včetně
  372 prvočíselných párů a 682 přímých svědků. Existence svědků
  byla porovnána s nezávislým zkušebním dělením. 0.991211540 s.
- Úloha 27: **5472** párů parametrů pro `1<=e<=12` porovnáno
  s Eratosthenovým sítem do **16781313**. Jediná výjimka je
  `k=1,e=1,N=3`. Ověřeno také **32827** hraničních redukcí
  čtverce včetně 0 a `N-1`. 0.329171710 s.

Samostatný [program pro seznamy](../verify_proth_listed_primes.py)
dokončil 3. listopadu 2026 všech **57 prvočísel**, tedy **114**
úspěšných kontrol. Kongruence byla v každém případě spočtena přímo
modulární mocninou FLINT a samostatně pomocí opakovaného umocňování
a redukce z §5. Obě metody sdílejí celočíselné násobení FLINT;
jejich exponentiační a redukční postupy jsou odlišné. Pro `N=11`
mimo obecný rozsah parametrů je prvočíselnost ověřena dělením 2 a 3.
Součet zaznamenaných časů obou metod je **6842.685372299 s**.
Výsledky jsou v [JSON](../results/proth-listed-primes.json) a
[logu](../results/proth-listed-primes.log), včetně doplněného
`3*2^54792+1` z errata 2024. Poslední případ `5*2^240937+1`
prošel za 1517.5393 s a 569.3060 s.

Obalový nástroj při závěrečném vyzvednutí relace oznámil kód 143,
ale jeho vlastní výstup uvádí `exit 0`; checkpoint je atomicky
uzavřen jako `passed` a log obsahuje závěrečné potvrzení všech 57.
Výpočet nebyl kvůli tomuto rozdílu v kódu obalu opakován. Tato
ověření **nedokazují nepřítomnost dalších prvočísel** mezi uvedenými
exponenty; historická úplnost seznamu zůstává oddělená.

## 7. Errata a historický rozsah

Vizuálně přečteny strany knihy 414, 663, 664, včetně zvětšené 663.
Všechny čtyři vrstvy errat a aktuální TeX prohledány. PDF strana
41 `all2-prepre` obsahuje přesun místa vydání Proth1878,
zpřesnění malého `k` a Youngovu dokončenou citaci 67 (1998),
1735–1738. PDF strana 10 `err2` doplňuje 29. 7. 2024 exponent
54792 do seznamu pro `k=3`. Žádná oprava C0156/C0157 nalezena nebyla.

Adleman1978: titul a bibliografii potvrzuje autorův index a
indexovaná první strana originálu, FOCS19, 75–83. Citovaná
strana 78 nebyla přímo získána; úplné vlastní důkazy §1–2 na
ní nezávisí. Pocklington1914: bibliografický záznam 18, 29–30
ověřen, originál zatím nečten. Rozsah těchto historických kontrol
nepřevádíme na tvrzení o kompletním přezkoumání původních článků.

Historický blok byl doplněn 3. listopadu 2026 v
[proth-history.md](proth-history.md): Prothova původní strana 926
vizuálně přečtena, stejně jako rozhodné pasáže Robinsonových 673,
674 a 676. Původní Prothova sazba skutečně vynechává `+1`; dřívější
předpoklad pouhé chyby transkripce byl opraven. Úplnost obou seznamů
do 300000 potvrzuje přímý projektový přehled Ballingera a Kellera;
přesné porovnání s našimi 57 certifikáty prošlo. Původní články
Cormack–Williams1980, Dubner–Keller1995 a Young1998 nejsou plně přečteny;
rozsah jejich bibliografické kontroly je výslovně oddělen od důkazu.
Fyzický nejnovější dotisk ani prvenství nálezů nejsou ověřeny;
hlášení zůstávají neodeslaná.

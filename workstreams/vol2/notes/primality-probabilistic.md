# §4.5.4: algoritmus P a úloha 22

Stav 3. listopadu 2026: matematika P na str. 395–396 a odpovědi
661–662 je prověřena. Úloha 22 je uzavřena s nálezem **V2-C0154**
v opravě z roku 2002. Pravděpodobnostní mez v knize platí.
Dodatek AKS a původní odstavce o dalších deterministických metodách
na str. 396 jsou samostatný, dosud otevřený blok.

## 1. Co algoritmus počítá

Vstup je liché celé `n >= 3`. Tuto doménu explicitně doplňuje erratum
z 21. 4. 2002 k zadání na str. 413. Píšeme `n-1 = 2^k q`, kde `q`
je liché. Základna `x` je rovnoměrně vybraná z `2,...,n-1`.

Před každým P3 platí `y = x^(2^j q) mod n`, s `0 <= j < k`.
P přijme právě tehdy, když `x^q = 1 mod n`, nebo když pro některé
`0 <= j < k` platí `x^(2^j q) = -1 mod n`. První možnost se testuje
jen při `j=0`; pozdější dosažení jedničky znamená odmítnutí.
Je-li `gcd(x,n)>1`, žádná z přijímacích kongruencí nemůže platit.

Pro prvočíslo Fermatova věta dává `x^(n-1)=1`. Není-li již první
hodnota jedna, hodnota těsně před prvním dosažením jedničky musí být
minus jedna: nad tělesem jsou jediné kořeny `y^2=1` čísla `+1,-1`.
Proto P přijme každou dovolenou základnu pro prvočíselný vstup.

## 2. Přesný počet přijímaných základen

Definujme `b(n)` jako počet přijímaných základen v `1,...,n-1`, tedy
včetně jedničky. Pro prvočísla to jsou také všechny základny; slovo
„lhář“ používáme pouze při složeném vstupu. Rozklad a další značení:

```
n = product p_i^e_i,  i=1,...,t,  p_i různá lichá prvočísla;
p_i-1 = 2^s_i d_i,  d_i liché;
m = min s_i,  g_i = gcd(q,d_i).
```

Vždy `k >= m`, protože každý prvočinitel je `1 mod 2^m`.
Grupa invertibilních zbytků modulo `p_i^e_i` je cyklická, řádu
`p_i^(e_i-1)(p_i-1)`. Jelikož `p_i` nedělí `n-1`, kongruence
`x^q=1` má v této grupě právě `g_i` řešení. Kongruence
`x^(2^j q)=-1` má `2^j g_i` řešení, je-li `j<s_i`, jinak žádné.
To plyne řešením lineární kongruence pro exponent primitivního kořene.

Čínská věta o zbytcích násobí počty řešení. Přijímací případy jsou
disjunktní: po dosažení minus jedné jsou všechny další čtverce jedna.
Proto i pro čísla s opakovanými prvočiniteli platí přesná formule

```
b(n) = (product g_i) * (1 + sum_{j=0}^{m-1} 2^(jt)).           (1)
```

Je-li `p_n` pravděpodobnost chyby při pevném vstupu, dostáváme

```
p_n = 0                         pro prvočíselné n;
p_n = (b(n)-1)/(n-2)             pro složené n.                (2)
```

Odečtení jedničky je nutné, protože P1 základnu 1 nevybírá.

## 3. Obecný důkaz čtvrtinové meze

Každý přijímaný zbytek splňuje také Fermatovu kongruenci
`x^(n-1)=1 mod n`. Jejích řešení je nejvýše `product (p_i-1)`.
Pokud některé `e_i >= 2`, pak

```
b(n)/n <= product ((p_i-1)/p_i^e_i) <= 2/9.
```

Poslední mez platí, protože pro liché prvočíslo
`(p-1)/p^e <= (p-1)/p^2 <= 2/9`. Takové `n>=9`, a tedy
`2n/9 <= (n-1)/4`.

Zbývá bezčtvercové složené číslo, tedy všechna `e_i=1` a `t>=2`.
Nechť `phi(n)=product(p_i-1)` je počet invertibilních zbytků. Z (1)
plyne

```
b(n)/phi(n) <= H_t(m) / 2^(sum s_i - mt),
H_t(m) = (1 + sum_{j=0}^{m-1} 2^(jt)) / 2^(mt)
       = 1/(2^t-1) + (2^t-2)/((2^t-1)2^(mt))
       <= 2^(1-t).
```

Pro `t>=3` je to nejvýše `1/4`. Pro `t=2` a nestejná `s_i`
je další faktor ve jmenovateli alespoň 2, opět s výsledkem `1/4`.
Pro `t=2` a stejná `s_i` nemohou oba liché díly `d_i` dělit `q`:
součin dvou různých prvočísel není Carmichaelovo číslo, jak je
dokázáno v [primality-basic.md](primality-basic.md), §2.
Alespoň jedno `g_i` je tedy vlastní dělitel lichého `d_i`, takže
`g_i <= d_i/3`. Tím je zde dokonce `b(n)/phi(n) <= 1/6`.

Ve všech případech máme `b(n) <= (n-1)/4`. Pro složené `n` navíc
`b(n)<n-1`, takže

```
p_n = (b(n)-1)/(n-2) < b(n)/(n-1) <= 1/4.                    (3)
```

Pro prvočísla platí `p_n=0<1/4` zvlášť. Důkaz pokrývá i `n=9`.

## 4. Kdy lze být blízko jedné čtvrtině

Knižní formulaci „near 1/4 in only two cases“ lze zpřesnit:
**mimo dva uvedené tvary je vždy `p_n <= 2/9`.**

Čísla s opakovaným prvočinitelem splňují přímo
`p_n <= (2n/9-1)/(n-2) < 2/9`. Pro bezčtvercová čísla:

- `t>=4` dává `b/phi<=1/8`.
- Při `t=3` se `m>=2` dostane `H_3(m)<=H_3(2)=5/32`.
  Pokud `m=1`, ale některé `s_i>1`, mez je `1/8`.
  Pokud všechny `s_i=1`, avšak některé `g_i<d_i`, mez je `1/12`.
  Zůstává právě Carmichaelovo číslo se třemi prvočiniteli `3 mod 4`.
- Při `t=2` a stejných `s_i` již máme `1/6`. Pro nestejná `s_i`
  s rozdílem alespoň 2 máme `1/8`. Při rozdílu 1 a `m>=2` máme
  `H_2(m)/2 <= H_2(2)/2 = 3/16`. Zůstává `s_1,s_2=1,2`.
  Bez plných `g_i=d_i` se mez zmenší ještě nejméně třikrát.
  Podmínky `d_1|n-1` a `d_2|n-1` jsou v tomto posledním případě
  ekvivalentní `d_1|d_2` a `d_2|d_1`. Tedy `d_1=d_2=d` a
  `n=(1+2d)(1+4d)`, kde `d` je liché a oba činitelé jsou prvočísla.

V obou výjimečných tvarech je `b(n)=phi(n)/4`. To samo netvrdí
existenci nekonečné posloupnosti s chybou konvergující k `1/4`.

Přesně ověřené příklady z odpovědi:

| n | b(n) | p_n |
|---|---:|---:|
| `49939*99877 = 4987757503` | 1246901922 | 0.249992490763636… |
| `1667*2143*4523 = 16157879263` | 4034270646 | 0.249678226940181… |

Všech pět uvedených prvočinitelů bylo dokázáno přímým dělením
všemi možnými děliteli do odmocniny. Obě zaokrouhlení v knize souhlasí.

## 5. Opakování a čas

Pro každý pevný složený vstup a 25 nezávislých rovnoměrných voleb
základny je pravděpodobnost chybného přijetí menší než
`4^-25 = 1/1125899906842624 < 10^-15`. Při miliardě testovaných
vstupů je očekávaný počet chyb menší než `10^9/2^50 < 10^-6`.
Stačí linearita střední hodnoty; nezávislost mezi různými vstupy
není potřebná. Je potřebná čerstvá nezávislost 25 voleb pro daný vstup.

Toto je pravděpodobnost chyby postupu při pevném vstupu. Není to
podmíněná pravděpodobnost prvočíselnosti vstupu po jeho přijetí.
Oprava z 18. 12. 1998 správně mění slovní výklad a počet testovaných
čísel. Rabin na str. 129 výslovně vysvětluje tentýž rozdíl.
Knižní srovnání s poruchami hardwaru je ilustrativní; bez modelu
konkrétního hardwaru nejde o další dokázanou pravděpodobnostní mez.

Binární umocňování a následné čtverce potřebují `O(log n)`
modulárních násobení. Klasická aritmetika pro každé potřebuje
`O((log n)^2)` bitových operací. Jeden pokus tedy stojí
`O((log n)^3)`. Přijmeme-li jako externí analytický vstup Bachovu
mez `2(ln n)^2` pod rozšířenou Riemannovou hypotézou, projití všech
takových základen stojí `O((log n)^5)`. Millerova lepší mez pro
optimalizovaný postup s rychlou aritmetikou s tím není v rozporu.

## 6. Výpočet, prameny a přesný rozsah

[Validátor](../verify_primality_probabilistic.py) porovnává přímé P
s nezávislou formulí (1) pro všech 2047 lichých vstupů od 3 do 4095
a všech 4 190 209 dovolených základen. Z toho je 563 prvočíselných
a 1484 složených vstupů. Kontroluje i jednotky, čtvrtinovou mez
a zpřesnění `2/9`. Největší chyba v tomto konečném rozsahu je
`449/1889` při `n=1891`; není to globální maximum.
Oba checkpointy v [JSON](../results/primality-probabilistic.json)
prošly. Běh měl PID 1271960, limit 120 s, návrat 0 a trval 12.184 s.

Původní sazba knihy 395, 396, 413, 661, 662 a opravy na PDF stranách
22 a 41 byly vizuálně kontrolovány. Byly prohledány všechny čtyři
vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální zdroj
`err2.textxt`. Pro C0154 nebyla nalezena následná oprava.

[Rabin 1980](https://math.nyu.edu/~goodman/teaching/Algebra_2_2021/MillerRabinTest.pdf):
text 128–134 a 138 přečten; vizuálně 129, 130, 132, 133 a 138.
Jeho původní test používá i gcd; vlastní důkaz výše se týká přímo P.
Implementační experimenty na dalších stranách nebyly reprodukovány.
[Miller 1976](https://www.cs.cmu.edu/~glmiller/Publications/Papers/Mi76.pdf):
vizuálně 300, 306–307, text 301 a 308–309; zbytek analytického důkazu
a dodatku není zde nově auditován.

[Bach 1990](https://doi.org/10.1090/S0025-5718-1990-1023756-8):
ověřena bibliografie a indexovaný autorský abstrakt; vydavatelské PDF
vrátilo 403. Celý důkaz konstanty 2 nebyl získán ani nahrazen tvrzením
o vlastním důkazu.
[Solovay–Strassen 1977](https://epubs.siam.org/doi/10.1137/0206006)
a [oprava 1978](https://epubs.siam.org/doi/10.1137/0207009):
vydavatelská metadata a abstrakt, nikoli celý původní článek.
Úloha 23 zůstává oddělená. Datum 1974 podpírá také historický úvod
AKS 2004, str. 782; nejranější rukopis nebyl dohledán.
[Arazi 1994](https://academic.oup.com/comjnl/article-abstract/37/3/219/403831):
vydavatelský abstrakt potvrzuje použití Montgomeryho aritmetiky
i odstranění dělení v přípravě. Celý placený článek nebyl čten,
konkrétní zrychlení nebylo měřeno. Montgomeryho metoda je již prověřena
samostatně v §4.3.1-41. Selfridgeova priorita zůstává doložena pouze
autorským erratem z roku 2005; nezískán nezávislý dobový záznam.

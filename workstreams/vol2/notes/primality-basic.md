# Základní testy prvočíselnosti, §4.5.4, strany 391–394

Datum: 3. listopadu 2026. Rozsah: Fermatův test, kritérium řádu,
Selfridgeova varianta, úplný příklad `2^214+1` a úlohy 9, 10, 17
s odpověďmi na 659 a 661. Původní sazba všech těchto míst byla zobrazena.
Rozšířené testy ve střední části 394 a algoritmus P na 395–396 mají
samostatný otevřený blok; zde je ověřen konkrétní příklad částečného
rozkladu na 394 a závěrečný odstavec o pseudoprvočíslech.

Nový nález v tomto bloku nevznikl. Počet 8241 byl úplně přepočten;
prvočíselnost všech faktorů číselného příkladu je doložena rekurzivními
celočíselnými certifikáty. Dolní asymptotická mez počtu Carmichaelových
čísel je výslovně převzatý analytický výsledek, viz §6 níže.

## 1. Značení a Fermatův test

Všude `n >= 2`. Číslo `phi(n)` je počet invertovatelných zbytkových tříd
modulo n, tedy tříd reprezentovaných čísly nesoudělnými s n. Jejich
násobení tvoří konečnou grupu. Řád jednotky x je nejmenší kladné k
s `x^k = 1 (mod n)`; dělí phi(n). Exponent grupy `lambda(n)` je nejmenší
společný násobek řádů všech jednotek. Pro liché n platí z již ověřené
věty 3.2.1.2B

```
lambda(n) = lcm { p^(e-1)*(p-1) : p^e je přesná prvočíselná mocnina v n }.
```

Fermatova věta pro prvočíslo p říká `x^(p-1)=1 (mod p)` pro jednotku x.
Binární umocňování používá nejvýše dvě modulární násobení na bit exponentu,
tedy O(log n) násobení pro exponent n-1. Tento počet není bitová složitost.
U složeného n je libovolný vlastní prvočíselný dělitel x také svědkem
`x^(n-1) != 1 (mod n)`; knižní existenční tvrzení tedy nevyžaduje,
aby byl svědek nesoudělný s n.

Výpočet pro `F5=2^32+1` dává po 32 čtvercích z počátečního čísla 3
zbytek **3029026160**. Prvočíselnost předchozích Fermatových čísel
3, 5, 17, 257, 65537 ověřuje tentýž certifikační validátor jako hlavní příklad.

## 2. Úloha 9 a Korseltovo kritérium

Je-li liché n složené a `lambda(n) | n-1`, nemůže `p^2 | n`:
pak by podle vzorce v §1 bylo `p | lambda(n) | n-1`, spor s `p | n`.
Proto je n součin různých prvočísel. Jediný prvočinitel by znamenal
`lambda(n)=n-1`, což zadání vylučuje. Kdyby `n=pq`, `p<q`, pak
`q-1 | pq-1` implikuje `q-1 | p-1`, opět spor. Je tedy třeba alespoň
tří různých prvočinitelů. Nejmenší z nich je **ostře menší než n^(1/3)**.

Opačný směr je také platný: pokud je n bez čtvercových dělitelů a pro
každý jeho prvočíselný dělitel p platí `p-1 | n-1`, potom Fermatova věta
a čínská věta o zbytcích dávají `a^(n-1)=1 (mod n)` pro každou jednotku a.
Složeným číslům s touto vlastností se říká **Carmichaelova čísla**.
Žádné není sudé: jinak by lichý prvočinitel dával sudý dělitel lichého
n-1; bez takového prvočinitele by zbývalo pouze prvočíslo 2.
To je Korseltovo kritérium, včetně nutnosti a postačitelnosti všech podmínek.

Pět příkladů v odpovědi je správných:

| Prvočinitelé | Číslo |
|---|---:|
| 3, 11, 17 | 561 |
| 5, 13, 17 | 1105 |
| 7, 11, 13, 41 | 41041 |
| 5, 7, 17, 19, 73 | 825265 |
| 5, 7, 17, 73, 89, 107 | 413631505 |

U 561 je `lambda(561)=lcm(2,10,16)=80`. Všech 320 jednotek splňuje
obě kongruence s exponenty 80 a 560. Přímý výčet v §3 zároveň dokazuje,
že 561 je nejmenší Carmichaelovo číslo.

## 3. Úplný výčet pod 10^12 a důkaz jeho úplnosti

Označme mez B=10^12. Zapišme každé hledané číslo jednoznačně jako
`n=p1*...*ps*r=m*r`, kde prvočinitelé rostou a `s>=2`.
Poslední prvočinitel r musí splňovat

```
r > ps,  m*r < B,
r-1 | m-1,
m*r = 1 (mod L),    L=lcm(p1-1,...,ps-1).
```

První dělitelnost plyne redukcí `m*r-1` modulo r-1. Z ní dostáváme
`r<=m`, tedy `r^2<=n<B` a `r<10^6`. Všechny prvočinitele proto lze
zcela rozhodnout Eratosthenovým sítem do 999999.

Program `verify_carmichael_census.cpp` vytváří všechny rostoucí prefixy
prvočinitelů. Při přidávání prvočísla p zachovává součin m a hodnotu L.
Větev lze ukončit, pokud `m*p*p >= B`, protože za p ještě musí následovat
větší prvočíslo. Pro první prvočinitel lze použít silnější `p^3 < B`.
Prefix s `gcd(m,L)>1` není možný: kongruence `m*r=1 (mod L)` nemá řešení.
Žádný prefix skutečného Carmichaelova čísla tedy tyto testy nevyřadí.

Pro každý prefix s alespoň dvěma prvočiniteli program vyčíslí inverzi
`u=m^(-1) mod L` rozšířeným Eukleidovým algoritmem. Pak prochází právě
čísla `r=u+j*L` v intervalu

```
ps < r <= min(m, floor((B-1)/m), 999999).
```

Kandidát projde právě tehdy, když je r prvočíslo a `r-1 | m-1`.
Kongruence modulo L již zajišťuje všechny ostatní podmínky Korseltova
kritéria. Všechny výstupy jsou proto správné a každé hledané n se objeví
přes svůj jediný rostoucí rozklad právě jednou. To je důkaz úplnosti,
nikoli předpoklad založený na shodě s publikovaným počtem.

Součiny při omezení rekurze a kontrole inverze se počítají ve 128 bitech.
Ukládané součiny a moduly nepřevyšují 10^12; výsledek m*r nepřekračuje B.
Žádný pravděpodobnostní test prvočíselnosti není použit.

Celý běh trval 13.1873 s a navštívil **22 487 646 prefixů**, otestoval
**15 113 795 členů aritmetických posloupností** a našel **8241 čísel**.
Podle počtu prvočinitelů:

| Počet prvočinitelů | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|
| Počet čísel | 1000 | 2102 | 3156 | 1714 | 262 | 7 |

Největší výstup je 999629786233. Všech 8241 rozkladů je uloženo v CSV.
Samostatný Python validátor ověřil součiny, různost prvočinitelů,
všechny Korseltovy dělitelnosti a neexistenci duplicit. Jeho prvočíselné
orákulum je **přímé dělení do odmocniny**, nikoli C++ síto: takto dokázal
prvočíselnost všech 2649 různých prvočinitelů ve výstupu.

Nezávisle se rozložilo každé liché celé číslo pod milionem. Výsledných
43 Carmichaelových čísel přesně odpovídá příslušné části CSV. Pro všech
332 lichých složených čísel pod 1000 se navíc přímo rozhodlo, zda Fermatova
kongruence platí pro všechny jednotky (nebo se našel protipříklad), a
výsledek se porovnal s klasifikací podle Korselta.

Použitá myšlenka posledního prvočinitele odpovídá Pinchově metodě;
novější primární výklad je Shallue–Webster, §2.2 a §5.1. Jejich program
jsme nepoužili. Jejich mnohem větší census pod 10^22 se tímto nepovažuje
za náš reprodukovaný výsledek. Pinchův poster potvrzuje všech šest
čísel v uvedeném řádku tabulky.

## 4. Kritérium řádu a Selfridgeova úloha 10

Pro jednotku x modulo n platí `x^s=1` právě tehdy, když její řád d dělí s.
Jestliže `d | n-1`, ale `d` nedělí `(n-1)/p` pro žádné prvočíslo p dělící
n-1, musí mít d u každého p přesně stejný exponent jako n-1. Tedy d=n-1.
Pak `n-1 | phi(n) <= n-1`, což je možné pouze pro prvočíslo n.

V Selfridgeově variantě má každé p vlastního svědka x_p. První kongruence
zaručuje, že jde o jednotku. Označme její řád d_p a jejich nejmenší společný
násobek D. Všechny d_p dělí n-1 a každý prvočinitel p je v alespoň jednom
z nich zastoupen s plným exponentem. Proto D=n-1. Zároveň každé d_p dělí
phi(n), takže D dělí phi(n). Předchozí argument opět dokazuje prvočíselnost.
Není nutné konstruovat společného primitivního kořene.

Pro prvočíslo n existuje primitivní kořen, tj. prvek řádu n-1, a takových
kořenů je phi(n-1). Hledání lze omezit na prvočíselné hodnoty svědků:
rozložíme kladného reprezentanta primitivního kořene na prvočinitele.
Řád jejich součinu dělí nejmenší společný násobek jejich řádů, takže pro
každý p musí alespoň jeden prvočinitel zachovat plnou p-mocninu.
U prvočísla n navíc všechny tyto jednotky splňují Fermatovu kongruenci.

Odhad `n/phi(n-1)=O(log log n)` lze odvodit z Mertensova součinu:
prvočinitelé n-1 nejvýše log n přispějí O(log log n); větších prvočinitelů
je nejvýše `log n/log log n`, a jejich součin faktorů `(1-1/p)^(-1)` je
nejvýše `exp(O(1/log log n))`. Tím je ověřena i knižní poznámka o hustotě
primitivních kořenů. Odhad neříká, že jeden společný kořen musí být prvočíslo.

## 5. Celý příklad 2^214+1 a Prattův strom

Identita (15) plyne z rozdílu čtverců:

```
(2*x^2+1+2*x)*(2*x^2+1-2*x) = 4*x^4+1.
```

Pro x=2^53 dává rozklad na dvě 33místná čísla. Validátor ověřil všechny
rovnosti pro n0,...,n6 na 392–394, všech sedm Fermatových testů se základem 3,
všech devět řádků tabulky (17) i počet desetinných míst 65, 33, 29, 27, 55.
Úplný rozklad je

```
2^214+1 = 5 * 857 * 843589 * 8174912477117 * 23528569104401
          * 37866809061660057264219253397.
```

Certifikáty v `results/primality-certificates.json` obsahují 39 uzlů a
úplné rozklady q-1. Jejich generátor smí používat SymPy; samostatný
validátor důvěřuje jen přesným součinům a modulárním mocninám, vychází
z q=2 a induktivně používá dokázané kritérium z §4. Ověřil 154 kongruencí
dvěma implementacemi modulárního umocňování. Nikde se nespoléhá na
pravděpodobnostní odpověď knihovny. Největší faktor má po rozvinutí
sdílených uzlů certifikační strom se 133 uzly.

Pro `n4=1653701519` je `F=23*1973=45379>sqrt(n4)`. Přesně byly ověřeny
všechny tři podmínky na 394. Jejich postačitelnost má krátký důkaz:
pro každý prvočinitel r čísla n4 má základ 2 modulo r řád dělící n4-1.
Podmínka gcd=1 pro každý z obou prvočinitelů F nutí jeho řád obsahovat
plnou příslušnou mocninu. Proto `F | r-1`, tedy každý r je větší než sqrt(n4).
Složené n4 však má prvočinitel nejvýše sqrt(n4), spor. To dokazuje tento
konkrétní Pocklingtonův certifikát; obecná úloha 26 se uzavře zvlášť.

Pro p=8174912477117 má posloupnost `x0=2, x(i+1)=x(i)^2+1 mod p`
ocas délky 680381 a cyklus délky 2238663. Pro druhý prvočinitel
q=23528569104401 jsou délky 2300986 a 3971912. Floydův detektor cyklu
a přímý dyadický detektor daly postupně první kolize
**6432966** a **8166215**. Podle obecného vzorce již dokázaného
v `factoring-rho.md`, §1, jde o

```
m(p) = 2^ceil(log2(max(mu+1,lambda))) - 1 + lambda,
```

kde mu je délka ocasu a lambda zde znamená délku cyklu, nikoli exponent
grupy z §1 tohoto dokumentu. Při první kolizi používá algoritmus kotvu
x4194303. Python nezávisle rekonstruoval její zbytky i zbytky x6432966
pomocí obou cyklů a čínské věty o zbytcích; jediný přesný gcd pak vydal
8174912477117. Před tímto okamžikem se modulo žádného z obou prvočinitelů
kolize nestala. Tím je prokázán knižní počet iterací, nejen existence
nějakého úspěšného kroku.

Na 394 také správně platí
`(2^28-9)/7=38347921=2341*16381` a `3^38347920=1 (mod 38347921)`.
Oba faktory jsou součástí prvočíselných certifikátů.

V úloze 17 děti uzlu q představují prvočinitele q-1 **s násobnostmi**.
Indukce od listů q=2 dokazuje správnost celého certifikátu pomocí §4.
Je-li T(q) počet uzlů, definujme `f(q)=2*log2(q)-1`.
Pro q=2 a q=3 nerovnost T(q)<=f(q) platí přímo. Pro prvočíslo q>3 má q-1
alespoň dva prvočinitele s násobnostmi, tedy počet dětí t>=2, a

```
T(q) <= 1 + sum_i(2*log2(q_i)-1)
     = 1 + 2*log2(q-1) - t < 2*log2(q)-1.
```

To je obecný důkaz odpovědi, ne experimentální odhad. Nakreslený strom
pro (1009,11) má přesně 13 uzlů; všechny jeho čtyři různé typy uzlů,
jejich svědky a násobnosti validátor zkontroloval. Nerovnost pro všech
39 generovaných certifikátů se ověřila i přesnou celočíselnou podmínkou
`2^(T(q)+1)<=q^2`.

## 6. Analytická mez a hranice kontroly pramenů

Alford–Granville–Pomerance, původní článek 1994, na 704–705 skutečně
uvádějí `C(X)>X^(2/7)` pro všechna dost velká X, kde C(X) počítá
Carmichaelova čísla nejvýše X. Jejich věta 1 má obecnější exponent EB,
kde E vyjadřuje hustotu prvočísel s hladkým p-1 a B uniformitu dolního
odhadu prvočísel v aritmetických posloupnostech; přesné definice jsou
jejich (0.1) a (0.3). Dokázané rozsahy jsou

```
0 < E < 1 - 1/(2*sqrt(e)),   0 < B < 5/12.
```

Například E=69/100 a B=83/200 dávají `EB=5727/20000>2/7`.
První přípustnost plyne již z `e>8/3>2500/961`; druhá je racionální.
Knižní slabší zápis Omega(X^(2/7)), i při použití ostré meze n<X, tedy
odpovídá citovanému výsledku.

Vizuálně byly přečteny původní strany 703–705 a 718–722 včetně závěru
konstrukce a bibliografie. Hlavní analytické lemmaty o nulách L-funkcí
na prostředních stranách **nejsou naším nezávislým důkazem**; větu 1
zde používáme jako explicitní externí vstup. Rozdíl mezi touto závislostí
a úplným vlastním konečným výčtem v §3 je podstatný.

Článek má na první tištěné straně chybnou hlavičku **140**, kterou
přebírají některé další zdroje. Obálka původního JSTOR dokumentu a
oficiální archiv Annals jej řadí do **139 (1994), 703–722**. Knuthova
bibliografie je v tomto bodě správná; nejde o nový nález v knize.

Další zdroje a přesné hranice jejich čtení jsou v
`sources/primality-basic.json`. Historické detaily a samostatně uváděné
nedostupné texty nejsou zaměněny za kompletně přezkoušené originály.

Historické poznámky na 391–392 byly porovnány s těmito texty:

- Fermatovy dopisy v Tanneryho a Henryho vydání z roku 1894, díl II,
  strany 205–206, 209, 212–213, 217. Srpnový dopis Freniclovi uvádí
  posloupnost 3, 5, 17, 257, 65537, 4294967297 a chybějící důkaz;
  dopis Mersennovi z 25.12.1640 opakuje domněnku a žádost o vysvětlení.
  Strana 209 dokládá malou Fermatovu větu v dopise z 18.10.1640.
  Knižní historický odstavec je s těmito prameny slučitelný; není tím
  tvrzeno přečtení veškeré Fermatovy a Mersennovy korespondence.
- Eulerův dopis Goldbachovi z **28.8.1742**, č.54 v edici
  Lemmermeyer–Mattmüller 2016, původní znění na 203–204 a anglický
  překlad na 719–720, obsahuje přesně uvedený rozklad 4x^4+1.
  Odkaz na Fussovu edici 1843, str.145, současně potvrzuje Dickson
  1919 na 381. Samotná strana 145 vydání 1843 nebyla zvlášť zobrazena.
- Dickson 1919, str.59 a 375, doplňuje data dopisů a pozdější Eulerův
  rozklad F5; zde nejde o nezávislý průzkum priority.
- Lehmer 1927, Bull. Amer. Math. Soc. 33, 327–340: bibliografie
  potvrzena také v primární bibliografii Prattova článku na webu SIAM.
  Project Euclid vyžaduje bezpečnostní ověření; celý článek nebyl přečten.
- Brillhart–Selfridge 1967, Math. Comp. 21(97), 87–96: metadata
  potvrzena v akademické bibliografii University of Utah. Jejich úplné
  tabulky nebyly získány ani přepočteny; náš vlastní příklad je ověřen v §5.

## 7. Errata a reprodukce

Prohledány všechny vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` podle
stran i výrazů Fermat, Selfridge, Pratt, Carmichael a čísel příkladu.
PDF all2-prepre, strany 22 a 41, byl zobrazen. Relevantní známé změny:

- 392, řádek -4, 20.7.2000: „is composite“ -> „cannot be prime“;
- 394, řádek -3, 20.6.2000: „is prime“ -> „is nonprime“;
- odpověď 9 na 659, 18.5.2002: oprava vnořených hranatých závorek;
- odpověď 17 na 661, 20.4.2009: **SICOMP 7 -> SICOMP 4**.

První dvě změny se nevyskytují v této přesné chybné podobě v našem
prvním dotisku; matematický význam byl kontrolován přímo podle sazby.
Prattův správný údaj 4(3), 214–220 (1975) potvrzuje primární stránka SIAM.
Celý Prattův článek zde nebyl získán; obecný důkaz úlohy je vlastní §5.

```
g++ -std=c++17 -O3 -Wall -Wextra workstreams/vol2/verify_carmichael_census.cpp -o /tmp/knuth-vol2-or9kgh/carmichael-census
timeout 600 /tmp/knuth-vol2-or9kgh/carmichael-census 1000000000000 workstreams/vol2/results/carmichael-census.csv
g++ -std=c++17 -O3 -Wall -Wextra workstreams/vol2/verify_primality_rho.cpp -o /tmp/knuth-vol2-or9kgh/primality-rho
timeout 120 /tmp/knuth-vol2-or9kgh/primality-rho > workstreams/vol2/results/primality-rho.csv
timeout 90 python3 workstreams/vol2/generate_primality_certificates.py
timeout 120 python3 -u workstreams/vol2/verify_primality_basic.py
```

Výsledek: všechny čtyři kontrolní bloky passed, celkem přibližně 6.68 s
validace. Dokončené kontroly se při přidání dalšího bloku zachovávají
přepínačem `--resume`. Běhy, PID, limity a logy jsou v RUN_STATE.json.

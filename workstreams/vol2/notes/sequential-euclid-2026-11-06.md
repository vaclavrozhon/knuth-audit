# §4.5.3 — analýza Eukleidova algoritmu, souvislé argumenty

6. listopadu 2026, V2-X0144. Původní text 356–379 a odpovědi 647–657
byly přečteny. Odpovědi této sekce končí na 657; stránky 658–662 již
patří faktorizaci a nejsou zahrnuté do tohoto bloku. Přidaná úloha52
se přebírá z archivovaných errat a obecného důkazu.

Mapa každé číslované rovnice, dalších tvrzení, tabulek a všech52 úloh
je v results/sequential-euclid-evidence.json. Odkazy vedou k dříve
uzavřeným vlastním argumentům, nikoli pouze k úspěšnému konečnému testu.
Spektrální, gamma a enumerační výpočty se neopakovaly.

## Rozsah převzatých argumentů

Continuantové identity, konečné a nekonečné rozvoje, kanonický konec,
obě znaménka kvadratických vstupů, periodické cykly a Ostrowského
reprezentace mají obecné důkazy v euclid-basic/quadratic. Konec s1
není kanonický rozvoj; libovolná continuantová slova z §3.3.4−31
proto nejsou totožným inventářem. Tamní výzkumná domněnka zůstává otevřená.

Algoritmus L pro algebraická čísla se používá s opravenou podmínkou
jednoduchého kořene. Průběžný Möbiův převod má invariant, maximální
výstup z otevřeného intervalu i produktivitu. Rychlostní dodatek
výslovně přebírá primární větu Mendèse France; vlastní převod a
nekoneční svědci jsou v euclid-online-rate. Analytické a skládací
rozvoje mají obecné důkazy v euclid-analytic/sign-reversal/folding.

Gaussovy operátory se používají na uvedených prostorech funkcí,
se stejnoměrně konvergentními řadami. W, (40)–(44), singularitní
přenos, úplný spektrální rozvoj, mez ocasu a exponenciální pokles
mají vlastní argumenty v euclid-gauss/spectral/full-spectrum.
Ostré pořadí všech spektrálních modulů je zvlášť označený externí
vstup; samotná samoadjungovanost je nedokazuje. Přesný certifikát
(41) má všech40 desetinných míst a20 podílů, bez nového běhu.

Diskrétní modely, Heilbronnovy reprezentace, váhy odečítacího algoritmu,
Collinsův model průměrování podle délek a gcd jsou odlišeny. (50)/(54)
jsou výslovné heuristiky, (55)/(58) podmíněné důsledky. (60) je externí
Porterova věta s ověřeným posunem konvence o1. Vlastní odvození (62)
z (60) i přepočet Lochs1961 jsou uzavřené; pomocné analytické odhady
Lochsova článku nejsou všechny znovu dokázány.

## Dopředné odkazy a nové doplnění

Strana337: čtvercový průměr je a ln N + D + o(1),
a = 12 ln2/pi², D = 0.0653514…; uvedené 0.842766 a0.06 jsou
zamýšlené hrubé aproximace, nikoli další přesné konstanty.
Strana340: průměrná cena A má koeficient19a ln2 ≈11.0991 a konstantu
19D+6 ≈7.2417. Použití předchozího hrubého D≈0.06 vysvětluje7.1;
nezakládáme chybu běžného zaokrouhlování. Nejhorší koeficient26.8
však odporuje Fibonacciho mezi: nový **C0247 confirmed/low**.

Strana345: v limitním Gaussově modelu je
Pr(A<1000) = 1 − log_2(1001/1000) ≈99.8558 %, tedy99.856 % správně.
Tento údaj není uniformní zárukou pro každý krok každého konečného vstupu.

Pro metrický komentář0.97 v úloze47 byl získán
[Faivre1997,119–120](https://matwbn.icm.edu.pl/ksiazki/aa/aa82/aa8222.pdf).
Autor definuje společný prefix krajů desetinného intervalu a uvádí
skoro jistou limitu6 ln2 ln10/pi². Přebíráme tuto externí větu,
nikoli audit celého článku. Je to jiný Lochsův výsledek než čtvercový
průměr1961. Archivní poznámka euclid-gamma je v tomto odkazu příliš
zkratkovitá. Věta není tvrzením o konkrétní gamma ani jejím důkazem
iracionality; uložený prefix9734 je samostatný konečný certifikát.
Na346 zůstává přesný model reprezentativní desetimístné dávky a
přenos metrické predikce na opakované Lehmerovy dávky výslovnou mezerou.

## Uzavření průměru podílů na89–90

Označme Q(n) součet všech podílů všech m/n, 1<=m<n, a R(n) tentýž
součet jen pro gcd(m,n)=1. Již dokázaná úloha35 dává
Q(n) = c n ln²n + O(n ln n (ln ln n)²), c = 6/pi².
Redukce zlomků dává Q(n)=sum_(d|n) R(d), tedy Möbiovou inverzí
R(n)=sum_(d|n) mu(d)Q(n/d).

Pišme L=ln ln n pro dost velká n. Ze σ_-1(n)=O(L), dokázaného
v euclid-heilbronn, a n/phi(n)<=ζ(2)σ_-1(n) je po vydělení phi(n)
součet chyb O(ln n L^4). Poslední nerovnost plyne rozkladem na prvočísla:
produkt zbývajících faktorů (1−p^(-e−1))^(-1) je nejvýše ζ(2).

Pro P(s)=prod_(p|n)(1−p^(-s)) položme

    A = sum_(p|n) ln p/(p−1),
    B = sum_(p|n) p(ln p)²/(p−1)².

Logaritmické derivování konečného součinu dává přesný hlavní člen

    (1/phi(n)) sum_(d|n) mu(d)(n/d)ln²(n/d)
      = (ln n−A)²−B.

Rozdělení prvočísel v ln n dává A=O(L²), B=O(L³): malé členy
omezíme součtem přes všechna celá čísla; pro velké použijeme
sum_(p|n)ln p<=ln n a klesání ln t/t. Proto

    R(n)/phi(n) = (6/pi²)ln²n + O(ln n (ln ln n)^4),

přesně jako na90. Markovova nerovnost pak dává pro pevné epsilon>0
pravděpodobnost sum a_j > (ln n)^(2+epsilon) rovnou O((ln n)^(-epsilon)),
která jde k nule. Není potřeba další census. Tím se tento dopředný
odkaz z89/90 uzavírá; historické krátké pokusy a ostrá mez úlohy
3.3.3−19 zůstávají oddělenými otevřenými body.

## Zbývající části a nálezy

Úloha35 má dokázané celé hlavní zadání a potvrzenou chybu normalizace
C0134, ale přesná dodatečná normalizovaná domněnka z1988 není dokázána.
Úloha30 má vlastní důkaz změn kroků, optimálních voleb a Gaussova
odhadu30.6 %; silnější tvrzení pro pevný jmenovatel zůstává bez
obecného přenosového argumentu. Úloha41 má dokázané všechny požadované
rozvoje i Liouvilleovu transcendenci; doplňková transcendence prvního
Kempnerova čísla zde nemá nezávislý důkaz ani přečtený původní důkaz.
Úloha46 má vlastní rychlý binární gcd; optimalitní model C0139 a
praktický práh1800 bitů zůstávají otevřené. Tyto čtyři položky jsou
proto v nově vymezeném celém rozsahu partial, nikoli smazané důkazy.
Celkem48/52 uzavřených úloh v evidovaném rozsahu.

C0244 v §3.3.4−30 se nezavírá: nejlepší aproximace z úlohy42
minimalizuje lineární chybu, sama nepřenáší tvrzení na optimalizátor
součinu sinusových vah. Hlavní odhad je již dokázán; slabší tištěný
mezilehlý interval zatím nebyl ani vyvrácen, ani obecně dokázán.

C0132 zůstává závažným matematickým nálezem: téměř jistá asymptotika
je nepravdivá, příslušný poměr má skoro jistě nekonečnou horní limitu.
Vlastní důkaz používá podmíněné hustoty, žádnou domnělou nezávislost.
Ostatní potvrzené nálezy i interpretační kandidáty jsou rozlišeny
v anglických kartách. Známé opravy se nezobrazují jako naše nálezy.
Nedostupná historická bibliografie zůstává výslovně přeskočená.

Další kurzor:379/file391, §4.5.4 Factoring into Primes.

# §4.4–14 až 16: rychlé převody a pole automatů

Kontrola 2. listopadu 2026. Původní zadání 328–329 a odpověď 638
byly vizuálně přečteny. `M(n)` je horní mez času násobení dvou
nbitových celých čísel, s předpokladem `M(2n)>=2M(n)` a běžnou
lineární cenou čtení a zápisu. `K(n)` bude cena převodu n desítkových
číslic spolu s vytvořením binární hodnoty 10^n. V části o automatech
n opět znamená počet vstupních desítkových číslic, ale čas se měří
počtem současných taktů všech buněk, nikoli součtem jejich práce.

## Úloha 14: rozdělení čísla na poloviny

Číslo o 2n desítkových číslicích rozdělíme na dvě n-místné části
U_1,U_0. Rekurze vrátí jejich binární hodnoty a mocninu 10^n.
Potom vytvoříme `U=10^n*U_1+U_0` a `10^(2n)=(10^n)^2`.
Identita dokazuje správnost indukcí; základní jednomístná konverze
je konečná tabulka. Cena splňuje

```text
K(2n) <= 2K(n)+O(M(n)).
```

Převod mezi počtem desítkových číslic a bitů mění délku o pevný
faktor. Není nutné předpokládat nevyřčenou horní podmínku
`M(2n)=O(M(n))`: součin čísel s nejvýše c*n bity pro pevné c
lze rozdělit na konstantně mnoho součinů nbitových bloků a sečíst.
Jeho cena je tedy O(M(n)+n)=O(M(n)). Totéž vysvětluje, proč lze
doplnit délku na nejbližší mocninu dvou a zaplatit jen konstantní
faktor v dostupném algoritmu násobení. Dolní hladkost M zadaná
v úloze slouží naopak k sčítání menších úrovní rekurze.

Pro n=2^h má úroveň j celkem 2^j úloh délky n/2^j a stojí
nejvýše konstantní násobek `2^j*M(n/2^j)<=M(n)`. Je h úrovní
a O(n) koncových operací. Odtud plyne `K(n)=O(M(n)*log n)`.
Zaokrouhlené délky lze zpracovat dvojicemi půlek s rozdílem jedné
číslice nebo výše popsaným doplněním nul.

Pro opačný směr nejprve vytvoříme mocniny `10,10^2,10^4,...`
opakovaným umocňováním na druhou. Součet jejich cen je O(M(n)).
Pro rozpočet 2n desítkových číslic položíme V=10^n, spočteme
`U_1=floor(U/V)` a `U_0=U mod V` a rekurzivně vypíšeme obě poloviny.
Nižší polovina musí mít přesně n číslic, včetně úvodních nul.
Přesné dělení pomocí převrácené hodnoty a konečné opravy podílu
má cenu O(M(n)); obecný důkaz byl proveden v
[fast-reciprocal.md](fast-reciprocal.md). Máme stejnou rekurenci.

Přesná implementace v `verify_radix_fast.py` není časový benchmark:
ověřuje správnost obou rekurzivních směrů, mocnin i doplnění nul.
Prošlo 999 případů, včetně nulových a maximálních hodnot, lichých
délek a délky 8192 desítkových číslic.

## Úloha 15: co plyne a co neplyne o lepší složitosti

Jde o výzkumnou otázku bez tištěné odpovědi. Je nutné určit model
i tvar M; samotný výsledek 14 není dolní mezí.

- Pokud `M(n)=O(n^a)` pro pevné a>1, stejné rozdělení má cenu
  O(n^a), protože ceny úrovní klesají geometricky s poměrem
  `2^(1-a)<1`. Faktor log n v obecné horní mezi zde není nutný.
- V modelu pointer machine z úlohy §4.3.3-12 je doloženo lineární
  násobení, a proto tato konstrukce dává O(n log n). Potřebné
  procházení seznamů a vytváření částí stojí O(n) na úroveň;
  nevzniká další skrytý faktor. Důkaz tohoto modelu je v
  [fast-models.md](fast-models.md).
- Z délky vstupu a výstupu plyne pouze jednoduchá dolní mez
  Omega(n) pro sekvenční model s omezenou šířkou operace. Tato
  mez sama neřeší odstranění logaritmu. Nelze zaměnit následující
  paralelní pole za sekvenční lineární algoritmus.

Primární historický doklad je Brentův článek
[The Complexity of Multiple-Precision Arithmetic](https://maths-people.anu.edu.au/~brent/pd/rpb032-arXiv-v2.pdf),
oddíl Base Conversion, rovnice (6.20)–(6.22), strana 14 reprintu.
Byl vizuálně přečten a obsahuje tutéž horní mez s připsáním Schönhagemu.
[Brent–Zimmermann, Modern Computer Arithmetic](https://members.loria.fr/PZimmermann/mca/mca-cup-0.5.9.pdf),
verze 0.5.9, §1.7, zejména algoritmy 1.25/1.26 na stranách 38–39,
rovněž uvádí O(M(n) log n) pro oba směry; příslušné strany byly přečteny.

Při kontrole současných zdrojů byla nalezena také
[dokumentace FLINT z října 2026](https://fredrikj.net/fdoc/html/algorithms/integers/radix-conversion.html)
s touto horní mezí. Sama upozorňuje, že části nové dokumentace
vytvořil jazykový model. Bereme ji pouze jako doplňující doklad
popisovaného algoritmu, nikoli autoritu pro absenci lepšího výsledku.
Ve zkontrolovaných zdrojích nebyl doložen obecný sekvenční lineární
převod ani ostrá n log n dolní mez; tento omezený rešeršní výsledek
není důkazem, že žádný novější výsledek neexistuje.

Úloha 15 je uzavřena jako audit formulace, existujících horních mezí
a jejich modelových omezení. **Není tvrzeno vyřešení optimální
složitosti ani úplný přehled veškeré literatury.**

## Úloha 16: konkrétní konečné automaty

Použijeme řadu L=4n stejných buněk. Každá má jeden pracovní bit
r, na začátku 0, a několik konečných řídicích stavů. Se sousedy
komunikuje dvěma kanály: doprava jdou desítkové číslice a značka
END, doleva binární číslice a značka DONE. Každý kanál přenáší
nejvýše jeden symbol za takt; prázdný symbol znamená nečinnost.
Krajní buňky mají běžný příznak hranice pole. Nikde není celočíselný
čítač rostoucí s n ani přístup k vzdálené buňce.

Vstupní číslice přicházejí zleva od nejvýznamnější po jedné za takt,
za nimi END. Při číslici d provede každá buňka přechod

```text
q = floor((10*r+d)/2),    r' = (10*r+d) mod 2;
pošli q doprava a ulož r'.
```

Je jen dvacet dvojic (r,d), a proto jde o pevnou konečnou tabulku.
Máme q mezi 0 a 9 a r' mezi 0 a 1. Je to přesně dlouhé dělení
desítkového proudu dvěma. Pro prefix s hodnotou P, dosavadním
podílem Q a zbytkem r platí `P=2Q+r`; po příchodu d je
`10P+d=2*(10Q+q)+r'`. To dokazuje přechod bez znalosti délky.

Buňka j tedy dostává desítkový zápis floor(U/2^j), s úvodními
nulami, a její konečný bit je `floor(U/2^j) mod 2`.
Protože `U<10^n<2^(4n)`, všech L buněk obsahuje úplný binární
výsledek, včetně případných horních nul.

Při příchodu END buňka pošle svůj bit doleva a END doprava.
Poté už pouze předává přicházející bity z pravého souseda doleva.
Poslední buňka místo dalšího END pošle v příštím taktu doleva
DONE. Tato značka se předává stejně jako bity.

Počítáme-li první vstupní takt jako 0, přijde END k buňce j
v taktu n+j. Její bit dorazí na levý výstup v taktu n+2j.
K vlastnímu vyslání bitu a předání pozdějšího bitu z pravé buňky
tedy nikdy nedojde současně; mezi výstupními bity je jeden prázdný
takt. Poslední bit vyjde v n+2L-2 a DONE v n+2L-1.
Celý převod včetně sériového výstupu proto zabere **n+2L=9n taktů**.
Výstup je od nejnižšího bitu; prázdné takty se při čtení vynechávají.

Počet buněk je O(n), čas O(n), ale součet jejich práce není O(n):
už desítkových přechodů je přesně nL=4n^2. To je očekávaná cena
paralelního pole a neslibuje řešení sekvenční otázky 15.
Konstantu 4 lze zmenšit volbou L podle log_2(10), není to nutné
pro zadání. Konstrukce není prohlašována za optimální v počtu buněk.

Simulace používá pouze místní stav a dva příchozí symboly každé
buňky; kontrola velkým celočíselným orákulem je až mimo přechodovou
funkci. Prošlo 1061 vstupů včetně 0,...,1000, úvodních nul,
maximálních hodnot a 256místných čísel. Nejdelší běh měl 2304 taktů.
Celkem bylo ověřeno 2131304 místních číslicových přechodů a přesný
čas každého výstupního bitu i koncové značky.

## Stav a zdroje

Relace 14144 skončila exit 0, oba checkpointy v
`results/radix-fast.json` a `.log`. Primární PDF, texty a jejich
metadata jsou v `sources/radix-fast-manifest.json`. Užitečné stránky
jsou v `images/radix-brent-1976-p14.png` a `radix-mca-054/055.png`.
Čtyři vrstvy errat pro 328/329/638 i související formulace byly
prohledány; k 14–16 nebyla nalezena změna. Nový nález není.
Úlohy 14 a 16 mají vlastní obecné důkazy, 15 výše vymezený audit
výzkumného zadání. Další blok: floating point D/17/18 a kontext F.

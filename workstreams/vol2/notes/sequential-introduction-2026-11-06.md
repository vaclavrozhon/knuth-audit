# Souvislý průchod §3.1: náhodnost a cykly

6. listopadu 2026, V2-X0084. Přímo přečteny původní strany 1–9,
538–542 a část 543 s odpovědí 23. Na 543 zbývají další oddíly.
Všech 23 zadání souhlasí s dřívějším inventářem; nové zadání nepřibylo.
Všechny relevantní položky čtyř řad errat byly přečteny v čerstvě
potvrzených kopiích, včetně přidané odpovědi 19. Přímý obraz
`all2-prepre-p30-direct.png` znovu potvrzuje její sazbu.

## Přijaté matematické důkazy

Byly celé přečteny a porovnány se sazbou poznámky `intro-models.md`,
`intro-cycles.md`, `intro-random-maps.md`, `intro-k-ary.md`,
`intro-k-inversion.md`, `intro-k-census.md` a `intro-foata-fuchs.md`.

| Rozsah | Kontrola |
|---|---|
| text 1–4, úloha 1 | Součinové rozdělení cifer, skutečná nezávislost, Poissonova parita a symetrie deseti čtení. Neznalost vítězného koně není sama důkaz rovnoměrného přiřazení. |
| K, tabulka 1, úlohy 3–5 | Intervaly všech větví, nemožnost nuly při K11, konečnost a všech 45 řádků přepisu tabulky v validátoru. |
| úloha 2 | Multinomický počet a Stirlingova aproximace; uložených 2.5596878645…·10⁻²⁶ odpovídá 2.56·10⁻²⁶. |
| 6–7 | Floyd: první kladný násobek periody alespoň μ. Brent: první vhodný dvojkový blok. Gosper: životnost položky tabulky a přesná délka cyklu. SSY má C0002. |
| 8–10 | Konečný funkční graf, sestup k nule a podmínka prvočíselných dělitelů základu; příklady v textu souhlasí. |
| 11–15 | Rozdělení dvojice (μ,λ), Q(m), determinant lesů, permutace cyklických vrcholů, přesný střední počet cyklů a asymptotické normalizace. |
| 16–18 | Stav je celé k-okno; mez m^k je dosažitelná Eulerovým okruhem grafu slov. Detektor se používá na celé okno. |
| 19 | K-okna netvoří libovolné rovnoměrné zobrazení m^k stavů. Přesný vzorec pro nepřítomnost pevných bodů a rozsah Pemantlových výsledků zůstávají zachovány; C0003 je pouze v erratech. |
| 20–21 | Přesná inverze K a úplný dřívější soupis cyklů; rozsah přijetí níže. |
| 22–23 | Nezávislé hodnoty rovnoměrné funkce pouze na různých vstupech. Foatova–Fuchsova bijekce, inverze, šest vlastností i dva desetiprvkové příklady. |

Rozvoj Q(m) má konstantní člen −1/3; střední délka cyklu je
(Q(m)+1)/2 a ocasu (Q(m)−1)/2. Střední počet cyklů má konstantu
(γ+ln 2)/2 po odečtení (ln m)/2. Důkazy v poznámkách jsou v souladu
s oběma okrajovými případy m=1 a čistým cyklem μ=0. U původního
O(m^(1/2)) v odpovědi 13 jde o slabší, stále platný zbytek, ne
prokázanou nepravdivou rovnost. Nevede se jako nový nález.

Citované hlubší asymptotiky a optimální Brentův parametr jsou přijaty
v rozsahu dřívějšího porovnání primárních článků a jejich modelů.
Nejde o nové kompletní důkazy všech analytických vět. Otevřené části
úlohy 19 zůstávají výzkumné; jejich audit neznamená jejich vyřešení.

## Dřívější výpočty nebyly restartovány

Přečteny výsledky `intro.json`, `intro-extra.json`, `cycle-table.json`,
`random-map-constants.json`, `brent-optimum.json` a oba validační
záznamy úplného soupisu K. Přečten celý `census_algorithm_k.cpp`, celý
`invert_algorithm_k.cpp` a `verify_intro.py`, včetně přepisu tabulky.

Kód soupisu skutečně projde kořeny 0 až 10^10−1, navštíví každý stav
jednou a hledá cykly jednoduššího přechodu g. Každý cyklus f leží na
cyklu g, protože f provádí kladný počet kroků g. Následná mapa skoků
je proto úplná. Uloženo všech 10^10 návštěv, sedm cyklů f a dokončovací
řádek logu; nezávislý validátor ověřil hrany a všech 37 024 cyklických
vrcholů g jiným rozkladem grafu. Vrácený kód staré tool session 143
není převyprávěn jako úspěšný exit 0. Žádný nový soupis neběžel.

Inverze používá úplné celočíselné intervaly kvadratických obrazů,
opravenou celočíselnou odmocninu a všechny větve K2. Přijatá povodí
597 a 128 bodů mají doložené samostatné dopředné kontroly. Samotný
seznam nalezených cyklů by úplnost desetimiliardové domény nedokazoval;
opírá se o dokončený výčet a kontrolu programu.

## Nálezy a jejich umístění

- **C0002, původní 540:** znovu potvrzeno. Pro m=2,g=3 neproběhne
  žádné hledání ani v konstantní posloupnosti. Rovněž g=m nestačí;
  při m=g=2 se hledá v mocninách dvojky a cyklus délky 3 uniká.
  Nutné jsou g<m, počáteční b≥1 a kvalifikace krátkých trajektorií
  v online mezi. Parametrická oblast g<M byla znovu porovnána
  s textem původního SSY článku. Přesná chyba je na 540, ne v zadání 8.
- **C0003, all2-prepre 30:** kladný exponent pravděpodobnosti je
  nemožný již z meze 1 pro pevné k≥1. Chyba se nenachází v původní
  knize, kde odpověď 19 chyběla. Strana 542 je pouze související místo.
- **X0008:** sedm cyklů K je pozdější výsledek řešící původní otázku
  „dokázat, nebo vyvrátit“. Samotná nepravdivá domněnka v takto
  položené úloze není tisková chyba. Poznámka `intro-k-census.md`
  měla tuto hranici formulovanou příliš zkratkovitě; upřesněno.

Nebylo nalezeno další matematické pochybení. Změny pro název Davidovy
knihy a Frobeniovu citaci opravují text přidaný až po roce 1997;
nesmějí samy vybarvit původní strany 3 a 539 jako chybné.

## Rychle dostupná fakta a bibliografické výjimky

[Původní manuál Ferranti Mark 1 v archivu Manchesteru](https://curation.cs.manchester.ac.uk/computer50/www.computer50.org/kgill/mark1/progman.html)
potvrzuje instrukci /W, dvacet nejnižších bitů akumulátoru a zdroj
odporového šumu. To odpovídá technickému popisu na str. 3.
[Vlastní úvod RAND](https://www.rand.org/pubs/monograph_reports/MR1418.html)
potvrzuje elektronický zdroj tabulky milionu cifer; katalogové údaje
reprintu potvrzují původní rok 1955. Není to nový audit milionu cifer.

Další přesná datování a prvenství Tippetta, Kendallova stroje,
instalace Ferranti a doporučení Turinga, literární epigrafy, historické
seedy Forsytha/Metropolise a konkrétní Marsagliův disk jsou výslovně
ponechány bez nové primární kontroly. Totéž platí pro přesnou sazbu
doplňkových bibliografických odkazů, pokud je matematika doložena
vlastním důkazem či dříve přijatým zdrojem. Včetně Peircova epigrafu
538 je tato výjimka zaznamenána i u jednotlivých stránek.

Další kurzor: §3.2 a §3.2.1, původní str. 10–11 a odpovědi 543.

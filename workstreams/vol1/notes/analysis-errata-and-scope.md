# §1.2.10: inventář, errata a rozsah kontroly

Kontrola 1. listopadu 2026. Zobrazen hlavní text s. 96–107 a odpovědi
500–502 (strany souboru = tištěná strana +15). Potvrzeno **23 původních
úloh**, bez nalezeného přidaného cvičení. Matematické části všech úloh
mají obecné důkazy. Historické zbytky níže zůstávají evidovány jako partial.

| Oblast | Doklad |
|---|---|
| Algoritmus M, distribuce rekordů, momenty, úlohy 1,3,7–10,18–20 | `analysis-records.md` |
| PGF, Theorem A, kumulanty, limity, úlohy 2,4–6,11–17 | `analysis-probability.md` |
| Čebyšev, (24)–(25), nezáporné funkce, úlohy 21–23 | `analysis-tails.md` |
| Tři nové nesrovnalosti a opravené důkazy | `analysis-findings.md`, C0013–C0015 |

## Nové nálezy

- **C0013:** odpověď 13 potřebuje násobnou konstantu před exp(−ax).
  Pro n=2,x=1/2 je levá strana 1 a pravá menší než 1.
  Citovaný Flajolet–Soria tuto konstantu skutečně má. Vlastní opravený
  odhad je jednotný pro n≥2,x≥0.
- **C0014:** koeficienty složení PGF jsou obecně nekonečné konvergentní
  součty, nikoli polynomy v koeficientech vstupů. Drobné chybné slovo
  v důkazu; závěr a momentové formule zůstávají správné.
- **C0015:** nový řadový exponenciální odhad z errat 2023 postrádá faktor n
  a ani s n neplatí pro všechna p. Přesná konečná binomická pravděpodobnost
  277/65536 je větší než tvrzených 1/256. Je doložen platný omezený obor.

Všechny tři mají stav confirmed vzhledem k dostupným podkladům;
prvenství ani tištěný exemplář ověřeny nejsou. Návrhy hlášení nebyly odeslány.

## Známé opravy, které kontrola zahrnuje

Prohledány řady all1-prepre, all1-pre, all1, err1 a zdroj err1.textxt podle
stran, čísel úloh, jmen i formulí. Aktualita je doložena dnešním stažením
v `sources/errata-refresh-2026-11-01.json`; výtah je
`sources/analysis-errata-extract.json`. Zobrazeny relevantní stránky
errat včetně all1-prepre 11,34,35; all1-pre 8,15; all1 6,13; err1 12.

| Místo | Oprava |
|---|---|
| 96, Algorithm M | 2024: n>0. |
| 98 | 1997: index n−1 v rekurenci P; 2002: bibliografická poloha Paris. |
| 100 | 2020: čárka v citaci Roes; 2024: nezáporná celočíselná veličina. |
| 101 (17), 102 | 2024: rozsah celých n,k>0; počáteční podmínka G_0=1. |
| 103 | 2024: 1+z; 1997: κ_2 u t²; 2005: Thiele 1889, odkaz na Hald 2000. |
| 104 | 2024: „except possibly“ u kumulantů; 2014/2024: nezáporná celočíselná veličina. |
| 104, obecný odhad | 2007: f nezáporná na celé podpoře; 2012: Bernsteinova citace 1924. |
| 105, úloha 13 | 2006: Pr; 2023: nakladatelské místo Cambridge, Mass. |
| 106, úlohy 14,18,20 | 1998: de Moivre; 2006: values; 2007: krajní faktor a dělení z v PGF; 2001: čárky v zápisu posloupnosti. |
| 106–107, úlohy 21–23 | 2023: q=1−p, p_k∈[0,1]; 2024: p,n>0 a hodnocení HM24. |
| 500, odpověď 6 | 1997: závorka logaritmu; 2002: H'(t); 2021: podoba derivace při B_1=+1/2. |
| 500, odpověď 8 | 1999: odstranění přebytečného (M−n)! ve jmenovateli. |
| 500, odpověď 10 | 2023: −(n−1)/M po změně Bernoulliho konvence. |
| 500–501, odpovědi 11,13–15 | 2024: factor; 1997: závorky odpovědí 13–14; 2001: jmenovatel 2np odpovědi 15. |
| 502, odpověď 21 | 1997: závorka; 1999: chybějící člen ε; 2023: nový řadový odhad, vadný podle C0015. |
| 502, odpověď 22 | 1999: rozsah 493–507 a záporné exponenty; 2023: univerzální odhad s 2+δ a ostrá nerovnost při r>4.32. |
| 502, odpověď 23 | 1998: obor 0≤ε≤p; 2024: zlepšení 6pq na 4pq v horním odhadu. |

## Přesné kontroly a obrázky

`check_analysis_records.py` prošel po opravě vlastní implementační chyby
(prázdný součet s celočíselnou nulou zaváděl float místo racionálního čísla).
Konečný úspěšný běh má **168264** kontrol: algoritmus na všech permutacích
do n=8, úplná slova pro n≤7,M≤4, podmínění počtem různých hodnot,
pevné násobnosti, rekordy inverzí a výběr odčítání s rovnostmi.
Racionální aritmetika ověřuje momenty, Bernoulliho korekci a tři procenta
normálního rozdělení; normální limitu neodvozujeme z konečného testu.

`check_analysis_pgf.py` prošel jednou, **150** kontrol: symbolické derivace,
momenty a kumulanty do řádu 8, koeficientová formule vyšších momentů,
složení a směsi PGF a certifikované číselné prahy 2 a 4.32.
Výsledky jsou v `results/analysis-records.json` a `analysis-pgf.json`.
Žádný starší úspěšný matematický program nebyl znovu spuštěn.

Ve Fig. 10 jsou relativní výšky prvních sloupců přibližně
26.45,79.87,100,69.75,30.48,8.84,1.75 procent maxima; odpovídají skenu.
Ve Fig. 11 jsou sloupce 5–9 relativně 44.44,77.78,100,93.75,62.5 procent
maxima. Jde o kontrolu dat a vizuální shody, ne měření přesných bodů sazby.
Fig. 9 odpovídá rozboru kroků a invariantu v `analysis-records.md`.

## Primární literatura: co bylo skutečně přečteno

Flajolet–Soria 1993: stažené PDF autorů, text §4 a zobrazené strany souboru
6,13–15,18. Definition 4.1 na s. 171 a příklady permutací potvrzují obsah
citace v odpovědi 13 i chybějící násobnou konstantu v knize. Přesnou
číselnou konstantu v jejich Proposition 4.2 nepřebíráme.

Gončarov 1944: stažené PDF z MathNet, skutečně přečtené skeny s. 32–36
(soubor 30–34). §14 uvádí PGF počtu cyklů, §15 momenty a §16 na s. 36
dokazuje normální limitu pomocí Γ. Používá škálování se sqrt(2), proto
limitní charakteristická funkce je exp(−t²/4); po přepočtu je to přesně
knižní standardizace. Atribuce výsledku v odpovědi 13 je doložena.
[Záznam a originál](https://www.mathnet.ru/eng/im3716).

Chernoff: skutečně přečten preprint Stanford Technical Report 6,
9. listopadu 1951, obálka, úvod a s. 5–9 (soubor 1–12).
Theorem 1 a Lemma 5 obsahují exponenciální odhad přes minimum momentové
funkce. Bibliografii publikované verze, *Annals of Mathematical Statistics*
23 (1952), 493–507, potvrzuje [záznam JSTOR](https://www.jstor.org/stable/2236576).
Sken preprintu je z [repozitáře Stanfordu](https://purl.stanford.edu/sw496fn0032).
Publikovaná sazba sama získána nebyla; Project Euclid vrátil pouze iframe.
Pro úplnou shodu citovaného znění proto u úlohy 22 zatím ponecháváme partial.

Hald 2000: záznam Wiley potvrzuje titul a bibliografii, úplný text vrací 403.
Haldův preprint 1979 je indexovaný a ve výtahu zmiňuje Thieleho 1889,
ale stažení i vykreslení potřebných stran skončilo timeoutem. Nepovažujeme
to za přečtení příslušného původního výkladu.
Pokusy, URL a hashe úspěšných stažení jsou v `sources/`.

## Zbývající historické a referenční části

Hlavní text: Bienaymé, Comptes rendus 37 (1853), 309–324;
Roes, CACM 9 (1966), 342; Foster–Stuart, JRSS B16 (1954), 1–22;
Thiele 1889 a obsah Hald 2000; Kolmogorov 1933 a Bernstein 1924.
Matematická tvrzení spojená s těmito odkazy mají výše vlastní důkazy.
Poznámku o rozlišitelných stranách fyzické mince nepovažujeme za empirický
fyzikální model; kontrolovaný binomický model dovoluje každé p∈[0,1].

U úloh zbývá:

- **13:** konkrétní citovaný překlad Gnedenko–Kolmogorov 1954 a tamní
  výklad věty o spojitosti; Gončarov a Flajolet–Soria jsou už ověřeni.
- **14:** historická atribuce de Moivrovi v příslušném původním prameni.
- **22:** uvedená publikovaná verze Chernoff 1952, po již přečteném preprintu.

Proto je hlavní text partial a úlohy **13,14,22** jsou partial;
ostatních 20 je checked. Vnitřní vazby na §1.2.3-(16), §1.2.5-21,
§1.2.6-64, §1.2.7-(7), §1.2.9-(27) souhlasí s již kontrolovanými místy.

## Pomocný Markdown

`md/vol1/12-1.2.10-analysis-of-algorithm.md` má u úlohy 18 doplněn
krajní faktor k_n z/k_n, ale postrádá konečné dělení z z errat 2007.
Výraz tak generuje A+1 místo A. To není nová chyba knihy; návrh opravy
je předán koordinátorovi a sdílený přepis se zde nemění.
Další OCR nedostatky: hodnocení 3=M15,5=M13,11=M15 a neostré nerovnosti
v (24)–(25), úlohách 20–22. U úlohy 23 uchovává inventář původní HM23
i opravené HM24. Checkpoint neukončuje zadání celého svazku.

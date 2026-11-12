# Hlavní text o pentominech, strany 79–82

Kontrola zahájena 1. listopadu 2026 po checkpointu `b96803e`.
Rozsah začíná nadpisem **Polyominoes** na str.79 a končí před nadpisem
**Polycubes** na str.82. Úvod str.79 o Behrensovi zůstává samostatně v D078.
Celý svazek tím není dokončen. Nejsou vytvářeny další návrhy emailů.

## F120: poslední políčko obdélníku 20 × 3

Na str.82, v druhém odstavci, je po zavedení rozměrů `0 ≤ i < 20`,
`0 ≤ j < 3` vytištěno pořadí `00, 01, 02, 10, …, 2j`.
Poslední položka má být **`j2`**. Znak `j` zde podle zavedené číselné
abecedy znamená 19; `2j` tedy znamená souřadnice (2,19), které nejsou
v obdélníku 20 × 3. Poslední řádkově uspořádaná dvojice je (19,2).

`prepare_pentomino_main.py` vypíše všech 60 souřadnic, ověří poslední `j2`
a nepřítomnost `2j`. PDF str.82 i autorův pre-fascicle5c str.18
(souborová str.24) byly zobrazeny; obě obsahují stejný překlep. Fyzický
výtisk dosud neověřen. Jde o lokální překlep, nikoli chybu algoritmu:
správně definovaný obdélník dává právě 71191 uzlů a osm řešení.

Čtyři relevantní vzdálené originály errat se shodují s archivem. Prohledány
byly oba úplné a oba krátké texty 4B/F5 a oba TeX originály, podle slov,
čísel a všech tří číslování stran. Odpovídající oprava nebyla nalezena.
Mapování je 4B79–82 = vydaný F5 77–80 = pre-fascicle5c 15–18.
`results/pentomino_main/errata-check.json` ukládá hashe, datum a 23 kontextů.
Potvrzení v našich zdrojích není tvrzením o prvenství nálezu.

## Úplnost tvarů a modelu

Růst od jedné buňky přidáním souseda vytváří všechny souvislé polyominy.
Úplnost plyne například odebráním listu vhodného kostrového stromu:
každý větší souvislý tvar lze získat z menšího. Normalizace translací
a osmi symetriemi dává pro n=1,…,5 počty 1,1,2,5,12 volných tvarů.
Všech dvanáct pentomin přesně souhlasí s dříve používaným slovníkem O…Z.
Nezaměňujeme volné a jednostranné tvary ani názvy I/L/F/N a O/Q/R/S.

Pro každý tvar jsou vyzkoušeny všechny různé orientace a všechny posuny
v obdélníku. Přiřazení možnosti k pěti buňkám a jednomu názvu dílku je
bijekce mezi geometrickými rozklady a přesnými pokrytími 72 položek.
Přesné pokrytí zaručuje každou buňku i každý dílek právě jednou; geometrický
rozklad naopak vybírá právě odpovídající možnosti.

Při sekundárních názvech dílků pokryjeme 60 buněk dvanácti pětičlennými
dílky bez opakování, takže se všech dvanáct názvů stejně použije. Při
sekundárních buňkách všech dvanáct různých dílků bez překryvu zabere všech
60 buněk. Obě oslabené formulace tedy zachovávají množinu řešení, mění však
strom hledání. Důkaz platí pro tuto konkrétní úlohu, ne pro libovolné XC.

Samostatně jsou uloženy svědecké rozklady 6×10, 5×12 a 4×15. Nejde o
úplné počty jejich řešení. Všechny čtyři vytištěné možnosti v (37) jsou
platné a patří do úplné množiny umístění.

## Počty možností a předzpracování

| Dílek | Všechna umístění | Po odstranění nepřípustných komponent |
|---|---:|---:|
| O | 48 | 48 |
| P | 220 | 156 |
| Q | 136 | 132 |
| R | 144 | 28 |
| S | 136 | 128 |
| T | 72 | 16 |
| U | 110 | 44 |
| V | 72 | 16 |
| W | 72 | 12 |
| X | 18 | 4 |
| Y | 136 | 128 |
| Z | 72 | 16 |
| Celkem | 1236 | 728 |

Každý další dílek je souvislý, takže nemůže překlenout dvě různé komponenty
dosud volných buněk. Každá komponenta doplňku jednoho umístění proto musí
mít velikost dělitelnou pěti. Filtr tím odstraňuje jen nemožné možnosti;
nepředpokládá, že samotná dělitelnost zaručuje doplnitelnost.

V (38) má V buňky 09,0a,0b,19,29; komponenty mají velikosti 27 a28.
Obrázek byl nezávisle načten z barevného vektorového obrysu PDF.
Γ orientace zachová 18 z72 původních V, po předzpracování 4 z16;
celkem tak zbude716 možností. Alternativa s X vlevo a neobráceným Z
má (V,X,Z)=(16,2,8), celkem718 možností. Vše souhlasí s knihou.

Na obdélníku působí čtyřprvková grupa vodorovného a svislého zrcadlení.
V zabírá ve všech orientacích výšku3 a jeho čtyři rohové orientace se
těmito symetriemi permutují jednoduše tranzitivně. Požadavek Γ proto
vybírá právě jednoho reprezentanta. Alternativně střed X nemůže ležet
na ose mezi sloupci9/10, takže poloha vlevo odstraní vodorovné zrcadlení;
svislé zrcadlení poté vymění obě chirality Z. Úplný výčet tento důkaz
potvrzuje: dvě orbity po čtyřech prvcích, v každé právě jeden reprezentant
obou omezení.

## Algoritmy a menší běhy

Původní autorův DLX1 a samostatný výčet s bitovými množinami řádků dávají
**celé stejné množiny řešení a profily po hloubkách**, ne pouze stejné součty.
Třetí implementace `pentomino_mask.cc` používá pouze obsazené buňky a
použité dílky; všech devět malých profilů rovněž souhlasí.

| Varianta | Řešení | Uzly | DLX1 hledání, mems |
|---|---:|---:|---:|
| Původní1236, všechny položky primární | 8 | 32644 | 145079135 |
| Jen Γ orientace V | 2 | 21805 | 102628079 |
|728 bez dalšího omezení symetrií | 8 | 4783 | 13777365 |
|716, Γ orientace V | 2 | 1243 | 4408751 |
|718, X vlevo a Z neobrácené | 2 | 1128 | 3829519 |
|1236, názvy dílků sekundární | 8 | 61851 | 290242299 |
|716, názvy dílků sekundární | 2 | 19306 | 67434465 |
|716, buňky sekundární | 2 | 11656 | 37061735 |
|20×3, první volná buňka bez MRV | 8 | 71191 | 320108294 |

Knižní přesné počty uzlů ve všech těchto případech souhlasí. Hlavička
musí mít buňky před názvy dílků. Při opačném pořadí vzniká jiný strom
(například32978 uzlů pro původní problém); jde o změnu rozhodování při
shodných délkách, nikoli o chybu knihy. Průzkumné vstupy a logy jsou
zachovány pod `explore-full-*`.

Memové počty jsou závislé na implementaci, pořadí a konvenci zahrnutí
inicializace. Archivovaný DLX1 dává uvedené hodnoty hledání a zvlášť
inicializaci v `short-check.json`. Jsou blízké knižním146M/103M/4.5M/4.0M/
291M/68M/37M, ale **všechna historická zaokrouhlení nebyla přesně
reprodukována**. Samotný tento rozdíl neoznačujeme za nový nález.

První buňka00 má29 možností. Po vodorovném O v00…04 má buňka05 dalších49.
Při transpozici všech osm modelů20×3 přesně odpovídá osmi modelům3×20.
Varianta `dlx1-nomrv` je naše dříve ověřená změna výběru větví, nikoli
nezměněný autorův program; mění výběr na první aktivní položku.

Dva velké případy (všech1236 možností, buňky sekundární; a3×20 bez MRV)
mají uložený wrapper `run_pentomino_main.py`, limit24h na běh.
Při pokračování 2. listopadu už obě maskové enumerace dokončily celý strom:
první má přesně **1086521921** uzlů, druhá **1528716954**, tedy knižních
zaokrouhlených1.5 miliardy. Obě mají osm řešení a uložený úplný profil.
Obě druhé enumerace mezitím dokončily také: původníDLX1 skončil
1.11.2026 v23:29:16UTC, varianta bezMRV v23:28:32UTC. Úplné profily
se po všech13 hloubkách shodují s maskovým modelem; obě celé nativní
množiny osmi řešení souhlasí s dřívějším nezávislým krátkým hledáním.
Vyhledávací memové počty jsou2935242344643 a2579381560857, inicializace
395467 v obou případech. Zaznamenané implementační rozdíly u historických
memů zůstávají výše; shoda profilů není automatickým potvrzením jiné
memové konvence.

`check_pentomino_finished.py` bez opakování výpočtů ověřil všechny
zdrojové/vstupní/výstupní hashe, metadata, profily a úplné modely.
Výsledek je v `results/pentomino_main/large-verified.json`.
Wrapper už je terminální (`verified`); uložené dokončené logy lze commitovat.
Žádný z těchto čtyř velkých běhů není potřeba spouštět znovu.

## Původní obrázky a historie

Všechny29 barevné obrysy str.80 a jeden str.81 jsou načteny z PDF,
včetně zaoblených Bézierových rohů. Testované body leží ve středech buněk.
Sedmnáct samostatných ikon se správně identifikuje ve schématech
T…Z, F/I/L/P/N a O/P/Q/R/S. Dvanáct dílků(36) tvoří úplný platný rozklad
a patří mezi dvě Γ řešení. Otočení právě Q,R,S,T,W,Y,Z v centrálně
symetrické35buněčné oblasti dá druhé řešení. DílkyO,P,U,V,X zůstanou na místě.

Přímo od British Chess Problem Society byly získány oba originální skeny:

- [PFCS2, č.12, červen1935](https://www.theproblemist.org/pdf/fcr/vol_2/FCR_031.pdf):
  titulní strana potvrzuje vydání; tištěná128, souborová3, uvádí úlohu1844
  F.Hanssona z Göteborgu: rozdělit3×20 na dvanáct různých pentomin.
- [PFCS2, č.13, srpen1935](https://www.theproblemist.org/pdf/fcr/vol_2/FCR_032.pdf):
  titulní strana potvrzuje vydání; tištěná135, souborová3, obsahuje řešení,
  souřadnice sedmi dílků a citovanou možnost otočit část mezi sloupci b…n.

Souřadnice byly přepsány z obrazu, protože OCR je velmi nepřesné:
`a123bc3; cdef1e2; e3f23g12; i12j23k2; klmn3n2; mnopq1; q2r123s2`.
Zbývající komponenty mají velikost5 a tvoří dílkyZ,T,P,U,S. Celý výsledek
**přesně souhlasí s(36)**, včetně intervalu b…n. Kniha zde cituje správně.
Text původního řešení začíná nejasným „15 by3“; to není údaj převzatý
do kontrolovaného textu4B. Nevyvozujeme z něj chybu knihy.

Golombův článek je ověřen v primárních vydavatelských metadatech:
[Checker Boards and Polyominoes](https://doi.org/10.1080/00029890.1954.11988548),
AMM61(10), prosinec1954,675–682. Plné PDF vydavatele v této relaci
vrátilo403; historické tvrzení, že otázku3×20 položil bez odpovědi,
zatím nebylo ověřeno v celém původním článku.

Stejně byla ověřena Fletcherova bibliografie
[A program to solve the Pentomino problem by the recursive use of macros](https://doi.org/10.1145/365628.365654),
CACM8(10), říjen1965,621–623. Původní PDF i obálka zatím chybějí.
Autorův [původní text Dancing links](https://www-cs-faculty.stanford.edu/~knuth/papers/dancing.tex.gz)
potvrzuje popis makroprogramu a cituje de Bruijnovo sdělení z9.9.1999.
Samotné FGbook465–466 nebyly v této relaci zobrazeny, proto je toto
podpůrný zdroj, nikoli náhrada kontroly stránkového odkazu.

Dudeneyho epigraf se shoduje s textem problému74 v
[Canterbury Puzzles](https://www.gutenberg.org/cache/epub/27635/pg27635-images.html),
str.121 druhého vydání1919. Tiráž uvádí první vydání1907; předmluva říká,
že původní text zachovává a přidává řešení a poznámky. Přímý sken vydání1907
zatím neověřen. Soukromý Golombův dopis z16.2.1994 nebyl získán;
atribuci zachováváme jako zdrojové tvrzení knihy, ne nezávisle doložený citát.

E035 zaznamenává již zapracované upřesnění z21.11.2020:
ve vydaném F5 na str.78 bylo k „consecutive letters“ doplněno „from O to Z“.
To je vydavatelské upřesnění, nikoli náš nový nález.

## Reprodukce a zbývající rozsah

Příprava: `python3 audit-2026-10-31/prepare_pentomino_main.py`.
Malé úplné výčty: `check_pentomino_main.py`.
Obrázky: `extract_pentomino_main.py`.
Původní souřadnice a další obdélníky: `check_pentomino_main_history.py`.
Errata: `check_pentomino_main_errata.py`.
Velký wrapper je dokončen a ověřen; **nespouštět znovu**.

Zbývají přesná konvence historických memových údajů a
výslovně uvedené bibliografické mezery. Polycubes od poloviny str.82
sem nepatří a musí být kontrolovány v dalším bloku. Úlohy266 a268–323
se nestávají dokončenými tím, že je tento hlavní text odkazuje.

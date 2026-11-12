# DLX 115–120: hypersudoku a grafy

Checkpoint 2. listopadu 2026: **115 je úplně prověřena; 116 a 117 částečně.**
V tomto checkpointu úlohy 118–120 čekaly; jejich dokončení je popsáno v
[navazujícím záznamu](GRAPHS117_120_NOTES.md). Odkazy na úlohy zde znamenají
§7.2.2.1. Zdroj je lokální 4B, první vydání, druhý dotisk, listopad 2022.
Kontrolovány byly vykreslené strany 137, 444 a 445 a odpovědi v autorově
PostScriptu, strany 148–149. Fyzický výtisk ověřen není.

## 115: všechny čtyři počty a oba obrázky souhlasí

Počítáme mřížky s prvním řádkem 123456789. Přeznačení devíti číslic působí
volně; bez této normalizace se každý počet násobí 9!. Další geometrické
symetrie se neztotožňují.

| Podmínka | Původní DLX2 | Nezávislé přiřazování orbitám |
|---|---:|---:|
| a: transpozice | 7 784 | 7 784 |
| b: současná permutace řádků i sloupců z 67(d) | 16 384 | 16 384 |
| c: otočení o 90 stupňů | 372 | 372 |
| d: b i c | 32 | 32 |

Shodují se **celé množiny mřížek**, nikoli pouze jejich velikosti. Poslední
řádek je průnik úplných množin b a c; navíc byl nezávisle zkontrolován
testem obou permutací číslic na každé mřížce případu c. Kontrolní součty,
návratové kódy a koncové záznamy jsou v
[hyper115-details-checked.json](results/graphs115_120/hyper115-details-checked.json).
Všechny běhy jsou ukončené; při přijetí se znovu nehledalo.

**Redukce na XCC.** Používáme opravenou konstrukci z 114. Permutaci číslic
vynutí primární položky pro její argumenty a obrazy a barevné položky q.
Každá možnost přiřadí číslici buňce a jejímu obrazu pod alfa; sdílené
barevné položky x vynucují souhlas všech přiřazení téže buňce. Primární
položky hlídají právě jednu hodnotu v každé buňce a právě jeden výskyt
číslice v každé jednotce. Používáme 9 řádků, 9 sloupců, 9 běžných bloků
a 9 odvozených bloků; pět doplňkových bloků je důsledkem čtyř předepsaných
oblastí podle již ověřené 67. Všechny tři permutace zachovávají tuto
rodinu 36 jednotek; ověřeno explicitně na všech jejich obrazech.

První řádek i jeho obrazy jsou filtrovány podle předepsané normalizace.
Z dalších řádků je vyloučena číslice již pevná v témže sloupci. V pevném
bodu alfa musí být předchozí i následná číslice stejná. Tyto filtry
neodstraňují žádné řešení. Každá mřížka určuje permutaci číslic jednoznačně,
protože obsahuje všechny číslice. Tím je dokázána bijekce mezi řešeními
úlohy a modely XCC; nepřidáváme skrytý faktor za pomocné proměnné.

**Nezávislý výčet.** Program C++ prochází všechny permutace číslic, jejichž
řád dělí řád alfa. Pro involuce je jich 2 620; pro řád dělící čtyři 33 616.
Rozloží 81 buněk na orbity alfa. Jediná první číslice určuje celou orbitu;
po jejím oběhu se musí vrátit. Program odmítá opakovanou číslici v jednotce
a konflikty mezi orbitami, ale nepoužívá položky ani taneční vazby XCC.
Volba další orbity podle počtu možností mění jen pořadí úplného prohledání.
Tato úplnost spolu s bijekcí předchozího odstavce dává dvě odlišné kontroly.

**Obrázky.** Z původních PDF vektorů bylo přečteno všech 162 znaků.
Levá mřížka patří do úplné množiny a. Pravá, s původními symboly 0–7 a *,
patří po jednoznačném přeznačení prvního řádku do průniku b a c.
Ověřeny jsou všechny řádky, sloupce, bloky i rovnice pro automorfismy.
[Původní znaky a přeznačení](results/graphs115_120/hyper115-figures.json).

**Historie.** Dohledána a archivována Michelova práce z 5. prosince 2007
v [repozitáři University of Amsterdam](https://pure.uva.nl/ws/files/43012588/sudoku.pdf).
Tabulka na stranách 17–18 uvádí 7 784, 16 384 a 372 v řádcích 31, 22 a 34.
Na straně 16 jsou definovány indexy řádků a sloupců. První dvě permutace
jsou přesně naše a a b. Třetí je konjugovaná k inverznímu čtvrtotočení:
stačí v obou souřadnicích zaměnit sedmou a osmou pozici. Všech 81 buněk
této rovnosti kontroluje skript. Inverze má stejnou množinu pevných tříd.
Zdroj tedy potvrzuje i konkrétní význam počtů a uvedený rok. Nezaměňujeme
to za kontrolu všech ostatních výsledků Michelovy práce.

**E059 je zveřejněná změna, nikoli nový nález.** Oprava z 2. ledna 2023
odstraňuje druhou sadu pomocných blokových položek v návaznosti na Weigelovo
zjednodušení odpovědi 114. Původní dvojitá sada byla nadbytečná, počty
nezkreslovala. Opravený převod dává výše uvedené úplné výsledky.

## 116: obecné důkazy a dvě otázky k formulaci

Má-li G n vrcholů a m hran, konstrukce přidá n klonů, jeden vrchol w,
dvě křížové hrany za každou původní hranu a n hran od w ke klonům.
Tedy n' = 2n+1 a m' = 3m+n. Pro M2 = K2 z těchto rekurencí vychází

    n_c = (3/4) 2^c − 1,
    m_c = (7/18) 3^c − (3/4) 2^c + 1/2.

Vzorce splňují počáteční podmínky i obě rekurence. Jsou tedy platné pro
všechna c, nikoli pouze pro konečný výčet. Doplňkový program ověřil hodnoty
až do c=8. Příklady M2–M5 mají 2, 5, 11, 23 vrcholů a 1, 5, 20, 71 hran.

**Trojúhelníky.** Vrchol w nemůže být v trojúhelníku, neboť jeho sousedé
jsou nezávislí. Trojúhelník obsahuje nejvýše jeden klon. Pokud nemá klon,
leží v G; pokud obsahuje klon z', jeho náhrada původním z dává trojúhelník
v G. Proto μ(G) je bez trojúhelníku právě tehdy, když je bez něj G.
Indukce od K2 dokazuje požadovanou vlastnost všech Mc.

**Chromatičnost.** Z c-barvení G dostaneme (c+1)-barvení μ(G): klonům
dáme barvy jejich originálů a w novou barvu. Naopak předpokládejme
c-barvení μ(G) s barvou c na w. Žádný klon nemá barvu c. U původních
vrcholů s barvou c ji nahradíme barvou jejich klonu. Dva takto měněné
vrcholy nejsou sousední; u hrany s jedním měněným koncem chrání správnost
křížová hrana. Tím by vzniklo (c−1)-barvení G. Pro χ(G)=c je to spor,
takže χ(μ(G))=c+1 a indukcí χ(Mc)=c.

**Kritičnost, bez izolovaných vrcholů.** Nechť G je c-chromatický a
odstranění každé hrany e=uv umožní (c−1)-barvení α. Barvy α(u), α(v)
musí být stejné, jinak by již šlo o barvení G. V μ(G) lze ponechat jediný
konflikt na kterémkoli z následujících tří typů hran:

1. Původní uv: všem klonům dát c a w dát 1.
2. Křížová v–u': klonům nejprve zkopírovat α a potom dát u i w barvu c.
3. Hrana w–u': nejprve dát u i w barvu c a potom zkopírovat barvy klonům.

Pro třetí případ potřebujeme hranu incidentní s u. Podmínka bez izolovaných
vrcholů ji zaručuje. Mc izolované vrcholy nemají: platí to pro K2 a
konstrukce tuto vlastnost zachovává. Proto všechny požadované Mc skutečně
jsou hranově kritické. Odstranění jediné hrany sníží χ nejvýše o jedna:
do barvení grafu bez této hrany lze přidat novou barvu jednomu jejímu konci.

**C029, kandidát s malým dopadem.** Odpověď (a) doslova říká, že každý
trojúhelník v μ(G) musí být v G. Pro libovolné G je to příliš silné:
v μ(K3) tvoří dva původní vrcholy a klon třetího trojúhelník. Správné je
tvrzení o projekci použité výše. Protože jde o zkrácený indukční důkaz
pro bez-trojúhelníkové grafy, nevydáváme tuto formulaci za vyvrácení
úlohy nebo za potvrzený nový nález.

**C030, kandidát závislý na definici.** Obecná věta v odpovědi (c) potřebuje
při definici kritičnosti pouze odstraněním hran vyloučit izolované vrcholy.
Nechť G = K2 sjednoceno s K1. Je hranově kritický a má χ=2. V μ(G) však
po odstranění hrany mezi w a klonem izolovaného vrcholu zůstává C5,
takže χ zůstává 3. Zaznamenán je konkrétní pětiúhelník, tříbarvení
a zamítnutí všech 128 dvoubarevných přiřazení. Běžná silnější definice
kritického grafu může izolované vrcholy vylučovat už sama. Rozsah této
obecné věty proto ponecháváme k posouzení; vlastní závěr o Mc platí.

Obě věty jsou stejné v lokálním PDF i autorově PS. V šesti relevantních
vrstvách errat není nalezena jejich oprava. Dalších 75 malých grafů
ověřuje χ(μ(G))=χ(G)+1, přenos bez-trojúhelníkovosti a kritičnosti při
výslovné podmínce bez izolovaných vrcholů.
[Přesné protipříklady a malé kontroly](results/graphs115_120/mycielski-lemmas-checked.json).

Úloha 116 zůstává **partial**: grafické diagramy zatím nebyly celé
rekonstruovány z vektorů; původní Mycielského a Sachsův text a historický
kontext asymptotických mezí ještě nejsou dořešeny. Údaj 1955 není označen
za chybu: [vydavatel IMPAN jej potvrzuje](https://www.impan.pl/en/publishing-house/journals-and-series/colloquium-mathematicum/all/3/2/94136/sur-le-coloriage-des-graphs),
ačkoli jiný bibliografický katalog uváděl 1954. Opravy zadání z let 2020
a 2021 jsou již v lokálním 4B zahrnuté.

## 117: dokončen nezávislý výčet částí e–g

Samostatný C++ program přiděluje barvy přímo vrcholům. Další vrchol volí
podle počtu sousedních barev a stupně v nezbarvené části. Toto pořadí
nezávisí na jménech barev. Povoluje již použité barvy a nejvýše jednu novou,
takže každé rozdělení vrcholů do barevných tříd projde právě jednou.
Úplný oracle všech grafů s nejvýše čtyřmi vrcholy a 1–4 barvami, celkem
300 instancí, ověřil přepočet na všechna označená barvení.

| Graf | Rozdělení do c barev | Rozdělení do c−1 barev |
|---|---:|---:|
| M2 | 1 | 0 |
| M3 | 5 | 0 |
| M4 | 520 | 0 |
| M5 | 23 713 820 | 0 |

Po odstranění **každé** hrany jsou počty rozdělení do c−1 barev následující:

| Graf | Počet rozdělení : počet hran s tímto výsledkem |
|---|---|
| M2 | 1 : 1 |
| M3 | 1 : 5 |
| M4 | 5 : 15; 7 : 5 |
| M5 | 1432 : 20; 1544 : 10; 1600 : 5; 2200 : 10; 2492 : 10; 2680 : 5; 3744 : 5; 4602 : 5; 6640 : 1 |

Všechny hodnoty souhlasí s odpovědí. Pro označené barvy se první tabulka
násobí c!, druhá (c−1)!. Celkem jde o 105 dokončených samostatných běhů;
jejich vstupy, koncové JSON a kontrolní součty jsou uloženy.
[Výsledek a četnosti](results/graphs115_120/mycielski-counts-checked.json).

Toto **není úplná kontrola 117**. Dosud chybí úplná reprodukce požadovaným
Algoritmem C, 9-barvení Q8, jeho náklady a úprava z 122. Monte Carlo odhad
pro M6 není zaměňován za exaktní počet. Výsledek jiného algoritmu také
neověřuje knižní počet přístupů do paměti.

## Provoz a další práce

Programy a přijaté výsledky jsou oddělené od živých dlouhých úloh.
Dokončené výčty se neopakují. Zdrojový kód použitý běžícími úlohami
108–114 se nemění. Nový terminál sharp varianty 111(a) má celé stejné
čtyři mřížky jako nezávislý výčet; náklad je 507 644 708 130 mems.
Tím ještě nereprodukuje knižních 550 Gμ a mezera zůstává výslovná.

Nově byly přijaty první dvě původní Torto sady: DANCING/LINKS/TORTO/WORDS/SOLVER
má 18 modelů cest a 10 tříd mřížek; PROGRAMMING/COMPUTER/THE/ART/OF má
1 877 modelů cest, 1 540 přímo získaných mřížek a 1 444 tříd po odrazech.
Všechny cesty, zakázané průsečíky a výsledné kanonické mřížky byly zkontrolovány.
Náklady 711.231759119 Gμ a 55.523877046 Gμ nejsou přesnou reprodukcí
knižních 713 Gμ a 126 Gμ. [Přijetí terminálů](results/graphs115_120/torto-new-terminals-checked.json).

Původní řídicí proces 902988 zanikl bez finálního záznamu během třetí
sady ONE–TEN. Časovač/solver 912693/912694 zůstal živý; původní metadata
a částečný výstup jsou zachovány, příčina zániku neznámá. Nejde o dokončený
výčet ani o UNSAT. Dvě následující sady, které ještě spuštěny nebyly,
převzala nová oddělená fronta 918953. Zapisuje stdout přímo do souboru,
aby nezávisel na přežití čtecí roury. Živý ONE–TEN se znovu nespouští.

Další kroky: dokončit 117, rekonstruovat diagramy a dohledat citace 116,
poté přesné počty a obrázky 118–120. Nové terminály Torto a slovních
schodů přijímat jednotlivě, bez restartování hledání. Dřívější SAT výčet
a osiřelý MCC111(b) mají stále přesně popsané omezení důkazní síly.
Žádné nové emailové návrhy ani odesílání zpráv.

# DLX 64–67: clueless jigsaw, písmena, karty a hypersudoku

Kontrola 1. listopadu 2026. Vydání: lokální 4B, první vydání, druhý dotisk
(listopad 2022), SHA256 v `inventory/books.json`. Zadání jsou na tištěné
straně 130 (PDF 150), odpovědi na 429–430 (PDF 449–450). Srovnány také
původní stránky autorova `fasc5c.ps.gz`, datovaného 11. září 2019,
tištěné strany 66 a 133–134. Fyzický výtisk nebyl kontrolován.

**Výsledek:** matematika všech čtyř úloh byla zkontrolována v níže vymezeném
rozsahu. F118 je chybná dvojice buněk odpovědi SUDOKU, doložená v PDF i PS.
F117 je samostatný defekt našeho PDF: přes správné G je přetištěné S.
Autorův PS má správné G; F117 proto není potvrzenou chybou tištěné knihy.
C023 je pouze kandidát na upřesnění rozsahu 64(a). E032 je starší známá
oprava prvního řádku SUDOKU, již zapracovaná v našem PDF.

Úlohy 65 a 66 mají dokončený průchod. U 64 zůstává původní vydání
Maximeho úlohy v ChiMe a bibliografický stav otázky sudé diagonály;
u 67 současný stav přesného minima nápověd. Tyto mezery se neschovávají
za úspěšné výpočty. Úloha 68 a hlavní polyominový text ještě nejsou součástí
tohoto bloku, přestože jejich stránky už máme připravené jako obrázky.

## Původní obrázky a metody

`extract_sudoku_extensions.py` načítá původní vektorové čáry a glyfy,
nikoli OCR. Výstup `results/sudoku_extensions/pdf-diagrams.json` obsahuje
39 diagramů: dva k 64, sedm zadání a sedm odpovědí 65, osmnáct karet 66
a pět diagramů 67. U všech písmenových úloh souhlasí boxy zadání a odpovědi.
Zachovány jsou nezměněné trace XML a hashe PDF, parseru i pomocného kódu.

Původní parser správně odmítl dva různé glyfy v jedné buňce SOLVING.
Nový obal zachovává jejich pořadí i souřadnice; pro samostatnou kontrolu
poslední vrstvy vytvoří pouze dočasný strom v paměti. Původní PDF ani trace
nemění. U hypersudoku samostatně ukládá šedé plochy, které procházejí přes
standardní boxy; jejich barva proto nemůže určovat geometrické boxy.

Souřadnicový řešič používá množiny sousedních buněk a vynucené hodnoty.
Nezávislý původní Knuthův DLX1 řeší přesné pokrytí. Pro barevné položky
66 běží nezměněný DLX2. Úplné modely, vstupy a logy jsou uloženy.
Kontroly 67 porovnávají také celé stromové profily s nezávislým bitovým
modelem, nikoli jen konečný počet řešení.

## 64(a): úplná klasifikace řádů 1–6

Každý souvislý box má n buněk. `clueless_census.cc` nejprve vypíše všechny
rozklady čtverce, kanonizuje je vůči osmi symetriím D4 a přejmenování boxů
podle prvního výskytu. V každé třídě zafixuje první řádek na 1,…,n a hledá
nanejvýš dvě řešení. To stačí ke klasifikaci 0 / 1 / více řešení:
přejmenování symbolů působí volně a každá úplná tabulka má právě jedno
takto normalizované přejmenování. Totéž platí pro libovolný řádek či sloupec.

`run_clueless64.py` samostatně kontroluje každou kanonickou třídu,
souvislost a velikost boxů, stabilizátor a všechna pozitivní svědectví.
Každý případ s n≥2 a nanejvýš jedním řešením je znovu úplně vyřešen původním
DLX1; bylo jich 2201. U ostatních případů jsou uložená dvě různá platná
řešení, která přímo dokazují nejednoznačnost. Součet velikostí orbit
souhlasí s nezávislým úplným počtem rozkladů od DLX1. Doplňková kontrola
ověřuje, že vstup skutečně obsahuje dříve úplně ověřené nepřímé boxy
z 62 plus všechny celé řádky a sloupce.

V tabulce každá trojice znamená **bez řešení / jedno / nejméně dvě**,
po normalizaci symbolů. Počítají se geometrické třídy D4.

| n | Všechny rozklady | Všechny třídy | Bez přímého boxu | Alespoň jeden přímý box |
|---|---:|---:|---|---|
| 1 | 1 | 1 | 0 / 0 / 0 | 0 / 1 / 0 |
| 2 | 2 | 1 | 0 / 0 / 0 | 0 / 1 / 0 |
| 3 | 10 | 2 | 0 / 0 / 0 | 0 / 1 / 1 |
| 4 | 117 | 22 | 1 / 1 / 6 | 0 / 3 / 11 |
| 5 | 4006 | 515 | 8 / 6 / 252 | 0 / 3 / 246 |
| 6 | 451206 | 56734 | 1966 / 28 / 38243 | 180 / 3 / 16314 |

Všechna vytištěná čísla odpovědi jsou tedy správná pro rozklady bez
přímého boxu. Doplňkový skript výslovně přiřazuje všech osm obrázků 62
ke třídám: druhý nemá řešení, pátý má jediné, zbývajících šest má více.
Maximeho šestkový příklad má jediné řešení v obou polohách ABCDEF.
Původní DLX1 přesně reprodukuje 40 uzlů pro první řádek a 215 pro druhý.

### C023: rozsah zadání a přímé boxy

Zadání 64(a) říká najít všechny clueless jigsaw sudoku řádu n≤6, ale
na rozdíl od 62 výslovně nevylučuje přímé boxy. Odpověď odkazuje na 62,
což může zamýšlené omezení naznačovat. Proto jde o kandidáta na upřesnění,
nikoli tvrzení, že všechna čísla odpovědi jsou chybná.

Nejkratší netriviální příklad při širším čtení:

```text
boxy        jediné řešení při prvním řádku 123
AAA         123
BBC         312
BCC         231
```

Má souvislé tříbuněčné boxy, ale A je přímý. Pro n=4 přibývají tři
clueless třídy. Celkové počty clueless tříd při povolení přímých boxů
jsou pro n=1,…,6 postupně 1,1,1,4,9,31. Kompletní svědci jsou v JSONL;
nejde o odhad z náhodného vzorkování.

## 64(b): obecný důkaz Harrisovy konstrukce

Primární zdroj: [Bob Harris, důkaz](https://www.bumblebeagle.org/dusumoh/proof/),
archivovaný HTML a obrázky. Stránka uvádí 9. ledna 2006 a následné doplňky.
Obsahuje také odkaz na starší příklad z roku 2001; nepřisuzujeme tím
Harrisovi prvenství samotné existence. Knižní sedmičkový diagram je
transpozicí této konstrukce; jeho hranice i všechna písmena byly ověřeny.

Indexujme řádky a sloupce od 0, n≥3, a první sloupec zafixujme na
hodnoty 1,…,n. Použijme tyto souvislé oblasti velikosti n:

- A: řádek 0, sloupce 0,…,n−3, a buňky (1,0),(2,0).
- B: buňky (0,n−2),(0,n−1), a řádek 1, sloupce 1,…,n−2.
- C: poslední sloupec, řádky 1,…,n−1, a buňka (n−1,n−2).
- Pro R=4,…,n oblast tvořená řádkem R−2 ve sloupcích R−3,…,n−2
  a řádkem R−1 ve sloupcích 0,…,R−3.

Přímo z intervalů je vidět, že jde o rozklad celé tabulky; dvě části
každé oblasti se dotýkají hranou. Pro n≥4 není žádná oblast přímá.
Tabulka L(r,c)=1+((r−c) mod n) je řešením: v A, B a C obsahují části
právě komplementární množiny hodnot; v oblasti R dolní část obsahuje
3,…,R a horní zbývající hodnoty 1,2,R+1,…,n. Řádky a sloupce jsou
cyklické permutace. Zbývá dokázat jednoznačnost, nikoli jen existenci.

**Základ, hodnota 2.** Porovnání A s řádkem 0 dává v posledních dvou
buňkách řádku 0 množinu {2,3}. Porovnání B s řádkem 1 pak nutí pravou
buňku řádku 1 na 3, protože jeho levá buňka už je 2. Poslední sloupec
tedy nutí horní pravou buňku na 2 a vedlejší na 3. Porovnání C s posledním
sloupcem nutí dolní předposlední buňku na 2.

Nyní postupujeme od řádku r=n−2 do r=2. V oblasti R=r+2 je hodnota 2
ve spodním řádku už mimo její dolní část, na pozici (r+1,r).
Musí tedy být v horní části, v řádku r mezi sloupci r−1 a n−2.
Sloupce r,…,n−2 již mají 2 pod námi; zbývá pouze (r,r−1).
V řádku 1 je tato pozice součástí počátečního sloupce. Tak je umístěna
celá cyklická diagonála dvojek.

**Indukční krok.** Předpokládejme, že hodnoty 2,…,k jsou na svých
cyklických diagonálách, 2≤k≤n−1. Hodnota k+1 už je v (k,0).
Pro r=k+1,…,n−1 použijeme oblast R=r+1. Hodnota k+1 je v předchozím
řádku na (r−1,r−1−k), mimo horní část této oblasti, takže musí ležet
v dolní části, v řádku r. Sloupce 0,…,r−k−1 jsou už obsazeny touto
hodnotou výše; hodnoty 2,…,k v řádku r vylučují všechny zbývající
pozice větší než r−k uvnitř dolní části. Zůstává (r,r−k).

Potom zpracujeme horní řádky r=0,…,k−1. Hodnota k+1 už stojí ve všech
sloupcích menších než n−k+r: nejprve z dolních řádků, pak z předchozích
horních řádků. Ve sloupcích větších než n−k+r má daný řádek hodnoty
2,…,k. Jediná dostupná pozice je (r,n−k+r). Indukce tedy vynutí všechny
hodnoty 2,…,n; zbývající jedničky leží na hlavní diagonále. Řešení je
jediné pro každé n≥3 a požadované nepřímé boxy existují pro každé n≥4.

`check_clueless_proof.py` přehrává tentýž jednotný důkaz pro n=3,…,32
a u každého kroku kontroluje jedinou dostupnou pozici. Tyto konečné
kontroly nenahrazují právě uvedenou indukci. Pro n=3,…,9 jednoznačnost
navíc potvrzuje původní DLX1. Transpozice odpovídá prvnímu řádku knihy:
písmena a–f jsou všechna 3, g–l všechna 4.

Pro liché n můžeme sloupce zrcadlit a přejmenovat hodnoty tak, aby
řešení mělo tvar 1+((r+c) mod n). Jeho hlavní diagonála je permutací
hodnot právě proto, že 2 je invertibilní modulo n. Diagonální nápovědy
proto jednoznačně určí přejmenování už jediné tabulky. Pro sudé n tento
argument neplatí. Knižní příklad COMPUTER řádu 8 je samostatně ověřen;
žádnou obecnou sudou konstrukci zde netvrdíme. Aktuální primární
řešení této navazující výzkumné otázky rešerše nedoložila.

Původní ChiMe MM, 3 (březen 2000), str.15 zatím nemáme. Současný web
Chicago Area Mensa potvrzuje Maximeho autorství jiných jigsaw úloh,
ale sám nedokládá toto přesné datum, stránku ani prvenství. Proto 64
zůstává `partial`, i když matematické části a oba benchmarky jsou hotové.

## 65: všech sedm úplných řešení; F117, F118 a E032

Oba nezávislé řešiče dávají pro každé zadání jediné řešení. Celá tabulka
je porovnána s vektorovými glyfy odpovědi, včetně všech nápověd a boxů.
Opakovaná písmena ve slovech DANCING, SUDOKU a PUZZLE znamenají, že jeden
symbol nemá jméno; tečka v odpovědi zastupuje právě tento další symbol.
Nejde o díry v tabulce. V programu je tento symbol kódován jako `0`.

Pět odpovědí DANCING, LINKS, COMPUTER, ALGORITHM a PUZZLE souhlasí
beze změny. Správná řešení všech sedmi jsou v `small-check.json`.

**F117 — pouze lokální PDF.** V SOLVING, poslední řádek a poslední
sloupec, je nejprve vykresleno správné G a na něm S. Oba glyfy používají
stejný font T23 a téměř stejný počátek: (304.6393,598.7345) a
(304.63529,598.7345) v souřadnicích extrakce. Přesné hodnoty jsou
v `conflicting_glyph_layers`. Zvětšený původní výřez ukazuje překryv.
Samotná poslední vrstva dává řádek OLNISVS; správně je OLNISVG.
Navíc právě G je přímo zadanou nápovědou v dolním pravém rohu.
Starší autorův PS má čisté správné G. Záznam potvrzuje vadné zobrazení
našeho souboru, nikoli původ chyby u autora nebo v tiskárně.

**F118 — PDF i PS.** Ve druhém řádku SUDOKU mají sloupce 5 a 6
prohozené O a tečku. Tisk dává DUSK.O, správně DUSKO. Tečka zde
zastupuje šestý symbol. I bez této interpretace je chyba okamžitě
vidět: poslední sloupec obsahuje O ve druhém i pátém řádku.
Správné celé řešení je:

```text
SKO.UD
DUSKO.
O.DUSK
UDKO.S
.SUDKO
KO.SDU
```

**E032 — odlišná známá oprava.** Erratum z 29. června 2022 přehazuje
D a U v **prvním** řádku SUDOKU. Starší PS má SKO.DU, naše PDF už
správné SKO.UD. Nová F118 se týká druhého řádku a přetrvává i po
provedení zveřejněné opravy.

Citace J. Henleho ověřena u vydavatele: *The Minus and the Plus of
Hi-Tech*, Mathematical Intelligencer 38(1), 2016, str.74–77,
DOI 10.1007/s00283-015-9608-z. Knižní rozsah 76–77 odkazuje na
relevantní část článku; není chybný jen proto, že celý článek začíná na 74.
Na [Henleho vlastním webu](https://www.math.smith.edu/~jhenle/columns/hitech.html)
byl nalezen devítistránkový autorský přetisk. Strany 7–9 skutečně obsahují
Abel, Euler, Newton a Leibniz s písmenovými diagonálami a nepravidelnými
oblastmi. Tím je tvrzení o podobných úlohách doloženo přímo; netvrdíme,
že autorská a časopisecká sazba jsou totožné. Všech devět originálních
PNG je archivováno a zobrazeno. Kvůli chybě místního řetězce certifikátů
byly veřejné autorské stránky získány bez ověření TLS certifikátu;
manifest tuto skutečnost zachovává. Identita článku je zvlášť podpořena
metadaty vydavatele a odkazem z autorova institucionálního webu.

## 66: úplných 10080 uspořádání v obou variantách

Každá z devíti karet má čtyři dané hodnoty. Jejich všech 72 výskytů
pochází z vektorů původní stránky. Otočení karet nejsou dovolena.
Permutace tří pásů a tří sloupcových pásů působí volně na devíti
různých kartách, takže 9!/(3!3!)=10080. Kartu 1 lze dát do slotu 0;
zbývající dvě řádkové a dvě sloupcové volby jednoznačně normalizuje
podmínka c4=min(c4,c5,c7,c8). Transpozice se zde nedělí, protože by
současně transponovala vnitřek karet.

Barevné přesné pokrytí má 729 standardních možností sudoku, osmnáct
primárních položek pro karty a sloty a barevné sekundární položky pro
hodnoty buněk. Každá buňka se vyplní jednou; barvy vynucují shodu
hodnoty s nápovědou položené karty. To dává obousměrnou bijekci mezi
barevnými pokrytími a dvojicemi (uspořádání karet, úplné sudoku).
Všechny tři explicitní možnosti karty 2 v odpovědi byly zvlášť ověřeny.

| Varianta | Neřešitelná uspořádání | Jedno řešení | Více řešení |
|---|---:|---|---|
| i | 10079 | 192435768 | žádné |
| ii | 10078 | 149523786 | 149325687 má deset řešení |

Nezávislý souřadnicový model projde všech 10080 možností každé varianty.
DLX2 má kartu 1 zafixovanou a vrací 4, respektive 44 celých modelů;
zbývající čtyřnásobná symetrie je odstraněna uvedenou normalizací.
Výsledné množiny dvojic se přesně shodují. Každý nativní model je
samostatně geometricky validován včetně shody všech nápověd.

Jediná tabulka varianty i má přesně šest automorfismů ve smyslu 114.
Použit úplný výčet standardních sudoku symetrií s odvozením přejmenování
číslic a zbývající řádkové permutace; všech šest map je uloženo a ověřeno.
V této úloze nezůstává otevřený počet, příklad ani bibliografická mezera.

## 67: obecný důkaz, přesné profily a Brouwerův originál

Indexujme od 0. Položme I={1,2,3}, J={5,6,7}, K={0,4,8}.
Čtyři dodatečné boxy jsou I×I, I×J, J×I a J×J. Pro libovolnou číslici
je v trojici řádků I právě třikrát. Dva boxy I×I a I×J využijí po
jednom výskytu, a proto I×K obsahuje právě jeden. Totéž platí pro
J×K, K×I, K×J. Celá tabulka má devět výskytů každé číslice; osm právě
získaných disjunktních oblastí jich spotřebuje osm, takže i K×K je
duhová. To je obecný důkaz, nikoli úsudek ze dvou řešení.

Pět oblastí a–e z obrázku je přesně K×I,K×J,I×K,J×K,K×K;
porovnáno všech 45 písmen. Permutace τ=(03)(12)(58)(67) dává
y=3 floor(τ(r)/3)+floor(τ(c)/3). Devět takových boxů tvoří rozklad;
čtyři původní odpovídají y∈{0,2,6,8}. Další primární položky b′yk
proto vyjadřují správné omezení. Použití všech devíti nezmění množinu
řešení díky právě uvedenému důkazu.

| Zadání | Pouze čtyři další boxy | Všech devět dalších boxů |
|---|---:|---:|
| i | 231 uzlů | 77 uzlů |
| ii | 708 uzlů | 151 uzlů |

Všechny hodnoty přesně souhlasí s knihou. Nezávislý bitový model navíc
potvrzuje celé profily po hloubkách. Souřadnicové řešení a úplné původní
DLX1 se shodují se všemi 162 vytištěnými číslicemi odpovědí.
Současné použití τ na řádky i sloupce zamění celý standardní a dodatečný
rozklad do devíti boxů. Proto zachovává množinu řešení, jak tvrdí (d).
Geometricky je to právě předepsané otočení rohů a převrácení půlřádků.

Primární [Brouwerova stránka](https://homepages.cwi.nl/~aeb/games/sudoku/nrc.html)
uvádí příklad Ritmeestera z 31.12.2005 a vlastní jedenáctinápovědová
zadání. Její [čtyři příklady](https://homepages.cwi.nl/~aeb/games/sudoku/nrc11.html)
jsou archivovány jako PNG a přepsány po vizuální kontrole. Všechny čtyři
mají právě jedno řešení v obou nezávislých modelech. První dva mají
stejné řešení, jak uvádí zdroj; tvrzení zdroje, že jsou jedinými
jedenáctinápovědovými zadáními tohoto konkrétního řešení, nebylo potřebné
pro knižní úlohu a zde se neoznačuje za zkontrolované.

Knižní ii je přesně varianta souboru `nrc11b.png`:
nová buňka (r,c) odpovídá staré (8−c,r), tedy jde o otočení o 90°.
Přejmenování starých číslic 1,…,9 je (3,1,2,6,9,5,4,8,7).
Tato mapa byla ověřena na všech 81 buňkách zadání i řešení.
Nejde jen o podobnost obrázků nebo stejný počet nápověd.

**Otevřený stav:** jedenáctinápovědové zadání dokazuje horní mez 11;
obecná jednoduchá dolní mez je 8, protože dvě nepoužité číslice lze
zaměnit. To nejsou důkazy přesného minima. Rešerše 1.11.2026 zahrnula
hesla hypersudoku/NRC, minimum, 10/11 clues a původní Brouwerovy stránky;
nepřinesla primární důkaz přesného minima. Starý autorův web sám
nedokládá, že žádný novější důkaz neexistuje. Proto ponecháváme tuto
jedinou ověřovací mezeru výslovně otevřenou a 67 jako `partial`.
Nevydáváme minimální zadání za globálně nejmenší ani neslibujeme
vyřešení výzkumné otázky.

## Errata, vlastní opravy a reprodukce

`check_sudoku_extensions_errata.py` prohledal úplné historické i aktuální
vrstvy `all4b`, `err4b`, `all4f5`, `err4f5`, včetně zdrojových textxt.
Čtyři čerstvě stažené oficiální originály souhlasí s archivem.
Uloženo 35 kontextových zásahů; relevantní je známá oprava E032.
Nenalezena oprava F118, lokálního přetisku F117 ani upřesnění C023.
Absence v těchto souborech není důkazem prvenství nebo autorova souhlasu.

Při vývoji byla opravena vlastní syntaktická chyba `else708` v prvním
skriptu; první kontrola správně zastavila také na dosud nezapsané F118.
Rozšíření parseru řešilo odmítnutý překryv glyfů a nejednotné šedé
vybarvení, nikoli změnu knihy. Pokus použít nedostupný PyMuPDF byl
nahrazen `pdftoppm`; správné výřezy používají cropbox. Neúspěšné kroky
nejsou počítány jako potvrzené výsledky. Konečné úplné běhy prošly.

```bash
python3 audit-2026-10-31/extract_sudoku_extensions.py
# Census build metadata: results/sudoku_extensions/clueless64/build.json
# Vstupy n1..n6.masks jsou úplné a kontroluje je supplement.
python3 audit-2026-10-31/run_clueless64.py
python3 audit-2026-10-31/check_clueless_proof.py
python3 audit-2026-10-31/check_sudoku_extensions.py
python3 audit-2026-10-31/check_sudoku_cards66.py
python3 audit-2026-10-31/check_sudoku_extensions_supplement.py
python3 audit-2026-10-31/check_sudoku_extensions_errata.py
```

Opakování již úspěšných výpočtů není běžnou podmínkou navázání. Nejprve
ověřit uložené výsledky a jejich zdrojové hashe. Census wrapper nyní
odkazuje na izolovanou sestavenou binárku v `/tmp`; při jejím odstranění
je třeba zopakovat zaznamenaný build a aktualizovat metadata před během.
Nevytvářeny žádné nové emailové návrhy ani zprávy Knuthovi.

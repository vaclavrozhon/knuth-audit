# §1.3.2′–35: celý MMIX program a celý grafický výstup

Obnova 7. listopadu 2026. Pokrytí: file58–59 / p50–51, celé zadání35,
oba obrázky18–19 a skutečný program `sources/crossword35.mms`.
Program je naše řešení; kniha nedává hotové MMIX řešení35. Staré
`partial` oprávněně postrádalo úplnou implementaci a její výstup.

Převzat je celý grafový argument z
`../vol1/notes/mixal-crossword.md`: vnější oblast je černá komponenta
dosažitelná přes společné strany z obvodu; začátky slov jsou sjednocení
dvou místních predikátů; pro příklad je níže uvedených14 čísel. Jeho
601 starých MIX běhů, úplné výčty malých matic ani verifier se neopakují.
MMIX má25 řádků místo23 a METAPOST místo textové tiskárny; tyto části
proto vyžadují nový vlastní důkaz, který následuje.

## Přesný vstup, stav a všechny paměťové adresy

Přípustný vstup je25 řádků po25 ASCII znacích `0`/`1` a jednom LF,
tedy650 bajtů. Uvažujeme standardní synchronní MMIX Fread/Fputs,
platně otevřené StdIn/StdOut a úspěšné I/O; nevyžaduje se žádná
předchozí hodnota pracovních lokálních registrů ani pracovních polí.
Další bajty za prvním blokem650 nejsou součástí matice a nečtou se.
V primárním `mmix-io-20250620.w`137–167 vrací Fread počet přečtených
bajtů minus požadovaný počet; při chybě zápornou hodnotu. Test BNZ
tedy pokračuje právě po úplném přečtení650. Neúplný vstup skončí
Halt2 ještě před použitím jeho nevyplněné části.

Označme D=Data_Segment. Fronta obsahuje625 tetrabytů na D…D+2499.
Grid je729 bajtů na D+2500…D+3228, vstup650 bajtů na
D+3232…D+3881. Parametry Fread jsou dvě osmibajtová slova na
D+3888 aD+3896; první obsahuje **adresu D+3232**, ne číslo GREG
pojmenovaného Input. Hlavička a oba formátovací řetězce následují
odD+3904. Řetězce mají výslovné koncové nulové bajty. Žádné oblasti
se nepřekrývají; všechna tetra/octa data mají potřebné zarovnání.

Grid používá index27r+c, 0≤r,c≤26. Celých729 bajtů se před čtením
nastaví na255. Signed LDB tuto značku interpretuje jako−1. Smyčka
začíná idx728, po každém STB snižuje idx a pokračuje při idx≥0;
zapíše tedy každý bajt právě jednou. Vnější obvod zůstane−1.

Při ReadCell platí1≤row,col≤25, idx=27row+col a
inoff=26(row−1)+col−1. LDBU, odečtení `'0'` a unsigned porovnání
s1 přijmou právě znaky0/1, včetně odmítnutí všech znaků pod`'0'`:
jejich záporný rozdíl je unsigned větší než1. Každý další bajt
na konci řádku se výslovně porovná s10. Po25 buňkách idx ukazuje
na pravý pomocný sloupec; přičtení2 přejde na další řádek do sloupce1.
Obě konečné větve row26/col26 jsou zahrnuté. Chybný znak nebo LF
vede do Halt2; žádný grafický výstup ještě nebyl proveden.

Čtyři GREG EnqAddr/EnqRet/EmitAddr/EmitRet se nepřekrývají.
Pomocníci se nevolají rekurzivně ani navzájem. GO ukládá návrat
do příslušného globálního registru; závěrečný GO $255,link,0 vrací
řízení přesně za volání. $255 je volný návratový/I/O registr.
Žádný helper nepřepisuje row,col,head,tail,seq ani návrat druhého
helperu, s výjimkou výslovného appendu Enqueue do tail.

## Fronta: invariant pro libovolnou matici, ne pouze čtyři příklady

Enqueue dostává index vnitřní buňky nebo jejího pomocného souseda.
Je-li hodnota1, nejdřív ji změní na−1 a teprve potom uloží index
na Queue+tail a zvětší tail o4. Jinak nic nezapíše. Označení před
vložením zajišťuje, že žádný index nevstoupí do fronty dvakrát.
Při čtení vstupu se Enqueue volá právě u96 různých obvodových buněk;
zatím neprochází sousedy, takže neovlivní pozdější načítání buněk.

Na začátku každé iterace Flood platí:

* head a tail jsou násobky4, 0≤head≤tail≤2500;
* fronta obsahuje různé původně černé vnitřní buňky, všechny nyní−1;
* každá vložená buňka má černou cestu k obvodu;
* u položek před head už byly zpracovány všechny čtyři strany;
* všechny dosud objevené černé sousední buňky jsou ve frontě.

Načtení položky posune head o4. Čtyři volání Enqueue s indexy
current−27,current+27,current−1,current+1 zachovají invariant.
Vnitřní index je28…700, proto všechna tato čtení leží v0…728.
Při vodorovném posunu z krajního sloupce se načte pomocný sloupec,
nikoli buňka jiného řádku. Obvod−1 se nikdy nevloží. Tail může
dosáhnout2500 až po zápisu posledního tetrabytu naoffset2496;
žádné další úspěšné vložení pak neexistuje.

Každá iterace zvýší head a počet různých vložených buněk je≤625,
tedy nastane head=tail. Zvukovost odstranění dává třetí invariant.
Pro úplnost vezměme nejkratší černou cestu z obvodu k dosažitelné
buňce. První buňka byla vložena při čtení; při zpracování každé
další hrany je následující buňka vložena nebo již byla vložena.
Po vyprázdnění fronty proto nezůstane dosažitelná jednička.
Výsledek je přesně pevný bod knižního opakovaného přeznačování.
Dlouhá cesta, větvení, uzavřený ostrov, nesouměrnost a pouhý
diagonální dotyk tím nejsou zvláštní neprokázané případy.

## Číslování a úplný METAPOST

Renderer prochází vnitřních625 buněk opět po řádcích. Zápornou
buňku přeskočí;1 vydá jako`b(rr,cc);`,0 jako`c(rr,cc);`. U bílé
buňky testuje nejprve below=0 a above≠0. Je-li tato podmínka
pravdivá, přejde přímo k NumberIt. Jinak testuje right=0 aleft≠0.
To je přesně sjednocení začátků maximálních bílých slov délky≥2;
buňka začínající obě slova se očísluje pouze jednou. Žádný test
nemění Grid. Pomocný obvod funguje stejně jako nepřítomný soused.

Seq je počet již vydaných čísel, na začátku0. Každé číslování
jej zvětší o1, a proto1≤seq≤625. Dvě dělení100 a10 rozdělí číslo
na tři desetinné cifry; všechny jsou0…9. Emit podobně rozdělí
row,col∈1…25 na dvě cifry. CellText má10 výstupních bajtů a nulový
terminátor, NumberText14 a terminátor. Emit mění pouze pozice2/3
a5/6 obou šablon, NumberIt pozice8/9/10 číselné šablony. LF,
interpunkce ani NUL se nepřepisují. Čísla typu`001` jsou v jazyce
METAPOST obyčejná čísla; `decimal k` vytvoří popisek`1`.

Hlavička definuje t jako otočení−90° a zvětšení17pt, tedy
(r,c) ↦ (17pt·c,−17pt·r). Řádky jdou dolů, sloupce doprava.
Cellpath(r,c) je uzavřený čtverec s rohy(r,c),(r+1,c),
(r+1,c+1),(r,c+1) po této transformaci. `c` kreslí jeho obvod,
`b` navíc vyplňuje vnitřek černě. Výstup proto obsahuje přesně
sjednocení čtyř hran všech viditelných polí a všechny vnitřní
černé oblasti. Opakované kreslení téže neprůhledné hrany nemění
geometrii; každý obrysový úsek je přítomen. Žádné bílé vnitřní
pole se nevyplňuje. Hranové dotyky sousedních černých polí
neodstraňují žádný potřebný bílý obrys.

`label.lrt(...,(r,c) transformed t)` umísťuje číslo dovnitř
levého horního rohu. Primární `sources/metapost-plain.mp`484–520
dává labeloffset3bp a vektor(.7,−.7), tedy odsazení2.1bp v obou
směrech. Uložený výpis skutečného`cmr8.tfm` dává každé cifře
šířku8·0.531258pt, výšku8·0.644445pt, nulovou hloubku. I tři
cifry mají šířku<12.751pt; s odsazením<2.108pt je to<17pt.
Výška s odsazením je<7.264pt. Žádné číslo≤625 proto nepřesahuje
svoje pole. Font a transformační konvence jsou stejné jako vFig19.

Každý Fputs testuje záporný výsledek a při chybě končí Halt1;
úspěšný běh vydá hlavičku, všechny buňky/popisky, `endfig; end`
a skončí Halt0. Při výstupní chybě může být soubor neúplný a
program to výslovně hlásí nenulovým návratem. Nepředstírá se, že
vadné zařízení vydalo úplný obrázek. Prázdná výsledná matice dává
prázdný beginfig/endfig, nikoli neplatnou syntaxi.

## Všechny náklady

Používáme knižní nominální μ/υ, nikoli skutečný čas hostitelského
I/O. DIV=60υ, GO=3υ, TRAP=5υ; běžné operace1υ. Nevzatá B* nebo
vzatá PB* stojí1υ, opačná predikce3υ. Paměťová instrukce navícμ.
Označme R počet odstraněných černých buněk, K zbývajících černých,
W bílých, L popisků, B původně černých buněk na obvodu. R+K+W=625.

Enqueue stojí8υ+μ při neúspěšném testu a9υ+3μ při vložení.
Inicializace včetně Fread stojí2205υ+729μ. Vstup má625 základů
po5υ+2μ, hraniční testy5908υ,96 volání GO po3υ,
Enqueue celkem(768+B)υ+(96+2B)μ, posuny buněk3175υ
a řádkové hlavičky/LF dohromady227υ+25μ. Tedy
(13491+B)υ+(1371+2B)μ.

Flood mimo pomocníky stojí(21R+4)υ+Rμ; pomocníci se volají4Rkrát
a úspěšně přesněR−Bkrát, tedy(33R−B)υ+(6R−2B)μ.
Celý prefix před rendererem stojí
**(15700+54R)υ+(2100+7R)μ**. Členy B se přesně ruší.

Emit má140υ+4μ včetně návratu. Renderer, jako kdyby každá buňka
byla záporná, má5200υ+625μ: patří sem hlavička, všech25 posledních
sloupcových predikcí, poslední řádková predikce, patička i Halt.
Záměna záporné buňky za černou přidává149υ+5μ, za bílou147υ+5μ,
zatím bez rozhodnutí o čísle. Každé skutečné NumberIt včetně Emit
přidává273υ+7μ.

Zbývající přesné náklady Qυ+Mμ patří testům bílých sousedů:

| Zkoušený soused | Cena při bílé hodnotě | Cena při jiné hodnotě |
|---|---:|---:|
| below |3υ+μ; pokračovat above |5υ+μ; pokračovat right |
| above |3υ+μ; pokračovat right |5υ+μ; očíslovat |
| right |3υ+μ; pokračovat left |5υ+μ; bez čísla |
| left |5υ+μ; bez čísla |3υ+μ; očíslovat |

Každá bílá buňka začne v prvním řádku a skončí přesně v jedné
ukončovací větvi této tabulky. Celý úspěšný program má tedy

**(2725+7R+5(K+W)+M+7L)μ**

**+(20900+54R+149K+147W+Q+273L)υ.**

Procházení i grafová fronta mají počet kroků lineární v počtu
buněk; žádné opakované celé průchody do vzdálenosti dlouhé cesty.
Nepřisuzujeme tomuto vlastnímu programu globální optimálnost.

## Příklady, původní obrázky a skutečné nové běhy

Původní58 a59 byly zobrazeny. V příkladu se odstraňují čtyři
rohy a všechny přidané pravé/spodní jedničky, celkemR593; zbývá
K4,W28. Černé buňky jsou(2,3),(3,5),(4,2),(5,4). Čísla jsou

```
00 01 00 02 03 00
04 00 00 05 00 06
07 00 08 00 00 00
00 00 09 00 10 00
11 12 00 00 13 00
00 14 00 00 00 00
```

Čtrnáct souřadnic vFig19 je právě tento seznam po řádcích. Jeho
sedm vodorovných úseček má na horním/dolním okraji rozsah2…6,
na zbývajících řádcích1…7; sedm svislých úseček má analogické
rozsahy. To je přesně sjednocení hran zde uvedených32 viditelných
buněk. Čtyři black příkazy i všechny popisky souhlasí sFig18.
Změnou seznamu konečných hran, černých buněk a souřadnic popisků
lze stejně reprezentovat libovolný požadovaný konečný diagram.
První vstupní řádek je`100001`+19 jedniček, tedy správně25 číslic.

První vlastní běh odhalil můj chybný parametr Fread: GREG symbol
Input v OCTA znamená číslo registru, nikoli adresu. Vstup proto
přepsal instrukční paměť. Tento neúspěch je uchován ve čtyřech
`crossword35-initial-invalid-pointer-*` souborech a zdroji stejného
jména; nejde o chybu knihy ani simulátoru. Po změně jediného
parametru naD+3232 se opravený program spustil poprvé na každém
ze čtyř níže uvedených případů. Žádný úspěšný běh se neopakoval.

| Vstup | R/K/W/L | M/Q | Bajtů | μ | υ |
|---|---|---|---:|---:|---:|
| knižní příklad |593/4/28/14 |78/298 |879 |7212 |61754 |
| vše bílé |0/0/625/49 |2401/8455 |7299 |8594 |134607 |
| vše černé |625/0/0/0 |0/0 |363 |7100 |54650 |
| jediná dlouhá vnější cesta |288/0/337/15 |1008/4250 |3943 |7539 |94336 |

Poslední vstup má jedinou obvodovou černou buňku(1,2),12 vodorovných
úseků na sudých řádcích2…24 ve sloupcích2…24 a11 střídajících
spojek; vše ostatní je bílé. Fronta musí skutečně dosáhnout konce
celé288buněčné cesty. Nezávislý Python model používá množinu
černých souřadnic, grafové dosažení a oba logické predikáty.
Porovnal **každý výstupní bajt** i celý předem odvozený profil.
Celkem1.497s včetně jediného úspěšného sestavení nástrojů; všechny
nové běhy měly nice15. Výsledky jsou v`results/crossword35-program.json`
a úplné příkazy v`results/crossword35-build-and-run.json`.

Skutečný výstup příkladu prošel METAPOSTem a uložený PNG byl
zobrazen: všech14 čísel a čtyři černé vnitřní buňky souhlasí.
Lokální instalace původně postrádala plain.mp; distribuce
texlive-metapost2023.20240207-1 byla pouze stažena a rozbalena
uvnitř tohoto workstreamu, nikoli instalována. SHA256 balíčku
souhlasí s distribučním indexem. Primární makra i metadata jsou
v`sources/metapost-plain.mp` a`crossword35-metapost-source.json`.
První dva příkazy METAPOSTu skončily před zpracováním obrázku
kvůli chybějícímu preloadu a chybnému předání inicializačního textu.
Následující jediný překlad obrázku uspěl. Pro Ghostscript bylo
nutné doplnit běžný fontový prolog a posunout záporné souřadnice
do výřezu; neúspěšné a prázdné pokusy jsou také zachované. Při
této úpravě zobrazení se MMIX ani úspěšný METAPOST překlad neopakoval.

## Stránkový rozsah a přenos vzorů

Celá59 je uzavřena: lokální predikáty, pevný bod, libovolné cesty,
formát25×25, rozšířený příklad, celýFig19 a úplné řešení. Závěr
§1.3.3′ je příslib budoucích převodů a výzva k účasti, nikoli
tvrzení, že už všechny převody existují; nevzniká nový matematický
důkazní závazek. Stránka58 je celá zmapovaná, ale zůstává partial
pro semafory34 a výslovnou historickou bibliografickou výjimku33.
Úloha35 je nyní argument_recorded; nové knižní zjištění žádné.

Ze vzoru binomických nerovností je převzato přesné vymezení oboru
a hranic625/729/2500, ze SAT vzoru důkaz všech vykonaných větví
a přesného součtu nákladů, z kografového vzoru rozlišení obecného
grafového důkazu od konečných obrazových certifikátů. Čtyři běhy
jsou kontrola implementace; nenahrazují invariant pro všech2^625
vstupních matic.

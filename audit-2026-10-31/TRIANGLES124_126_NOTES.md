# DLX 124–126: souřadnice, zvětšování a MacMahonovy trojúhelníky

Kontrola 2. listopadu 2026, lokální 4B, první vydání, druhý dotisk.
Zadání na str. 138, odpovědi na str. 446–447, související hlavní text
na str. 91. Všechny tyto původní stránky byly zobrazeny. U F063 byl
znovu zobrazen také původní autorův prefascikl 5C, str. 151.

124 a 125 jsou dokončené obecnými důkazy níže. U 125 zůstává dříve
potvrzená chyba F063; její opětovné ověření není nový nález. U 126 jsou
ověřené celé množiny řešení a správnost omezení symetrií. Historické
připsání výpočtu Gottfriedovi v roce 2001 a přesná reprodukce všech
uvedených nákladů jsou samostatné otázky; jejich stav je uveden níže.

## 124: rovinné souřadnice a hrany

Mřížkový vrchol `(u,v)` zobrazíme do eukleidovské roviny jako
`(u+v/2, sqrt(3)*v/2)`. Je to nesingulární lineární zobrazení.
Nečárkovaný trojúhelník `T(x,y,0)` má vrcholy
`(x,y),(x+1,y),(x,y+1)`; čárkovaný `T(x,y,1)` má vrcholy
`(x+1,y),(x,y+1),(x+1,y+1)`. Oba jsou rovnostranné se stranou 1.
Rozdělené jednotkové čtverce před zobrazením pokrývají celou rovinu
bez překryvů vnitřků, takže tyto dvojice souřadnic jednoznačně
popisují všechny elementární trojúhelníky. Obdélník m×n proto dává
rovnoběžník s 2mn trojúhelníky, jak uvádí odpověď.

Označení hrany a její dva vrcholy jsou:

| Hrana | Vrcholy |
|---|---|
| `-xy` | `(x,y),(x+1,y)` |
| `/xy` | `(x,y),(x,y+1)` |
| `\xy` | `(x+1,y),(x,y+1)` |

Nečárkovaná buňka má hrany `-xy,/xy,\xy`; čárkovaná má
`-x(y+1),/(x+1)y,\xy`. V tomto pořadí jsou sousedé nečárkované
buňky `(x,y-1)',(x-1,y)',(x,y)'` a sousedé čárkované buňky
`(x,y+1),(x+1,y),(x,y)`. Jejich společné vrcholy dávají přesně
uvedenou hranu, tedy souřadnice nevytvářejí dvě jména pro jednu hranu.

Původní obrázek 3×2 byl navíc ověřen přímo z PDF: všech 12 názvů,
30 textových znaků, jejich vzájemné polohy a sklon mřížky. Evidence:
`extract_triangles126.py` a `results/triangles124_126/original-figures-checked.json`.

## 124: barycentrická alternativa a dvanáct symetrií

Pro `T(x,y,z)`, kde z je 0 nebo 1, položme
`q=(x,y,2-z-x-y)`. Jeho součet s je 2 nebo 1. Inverzně z=2−s,
tedy jde o bijekci všech trojúhelníků s celočíselnými trojicemi součtu
1 nebo 2. Těžiště trojúhelníku vůči mřížkovému vrcholu `(1,1)`
má v prvních dvou souřadnicích hodnotu `q−(s/3)(1,1,1)`.
Tato projekce na rovinu součtu nula určuje stejnou geometrii:
pro `(u,v,-u-v)` je polovina čtverce normy rovna `u²+uv+v²`.

Každá permutace tří souřadnic je proto izometrie. Zobrazení
`q -> (1,1,1)-q` zaměňuje součty 1 a 2 a na projekci působí jako
násobení −1. Šest permutací a volitelné znaménko dávají 12 různých
izometrií trojúhelníkové mřížky. Jsou to právě rotace a osové
souměrnosti D6 kolem tohoto vrcholu: šest směrů sousedních vrcholů
je zachováno, a těchto 12 různých transformací vyčerpává jejich
dihedrální symetrie. Tím je dokázáno celé barycentrické tvrzení,
nejen jeho ověření pro několik vybraných buněk.

## 124: sudé a liché souřadnice

Trojúhelníku přiřadíme
`O(x,y,z)=(2x-1,2y-1,3-2x-2y-2z)`. Všechny složky jsou liché
a součet je 1 nebo −1. Každá taková trojice má právě jeden původní
trojúhelník, což plyne zpětně z prvních dvou složek a součtu.

Všechny sudé trojice V s `|sum V|≤1` mají součet nula. Vrcholu
přísluší mřížkové souřadnice `(1+V0/2,1+V1/2)`; to je bijekce
s celou vrcholovou mřížkou. Trojice E s právě jednou sudou složkou
má také součet nula. Je-li tato složka j, jsou `E+e_j` a `E-e_j`
liché trojice součtů ±1 a představují sousední trojúhelníky.
Průměr je E a jeho geometrické zobrazení je střed společné hrany.
Obráceně se každé dva sousední trojúhelníky liší o `2e_j`, tedy
takto vznikají právě všechny hrany, každá jednou.

Věta o dvou sudých souřadnicích říká pouze, že by mohly představovat
orientované hrany. Následující explicitní konvence dokazuje možnost.
Má-li Q jedinou lichou souřadnici j a součet s=±1, definujme
`V=Q-s*e_j` a `W=V+2s(e_(j+1)-e_(j+2))`, indexy modulo 3.
V a W jsou sudé trojice součtu nula a zobrazí se na sousední vrcholy;
Q označí orientovanou hranu V→W. Pro každý V dostáváme šest různých
sousedů, tedy všechny orientované hrany právě jednou. Opačná hrana
má kód `W-s*e_j`. Netvrdíme, že kniha tuto konkrétní konvenci předepisuje.

Podpůrná přesná kontrola `check_triangle_coordinates.py` zahrnuje
162 buněk, 486 sousedností a středů hran, 1944 aplikací všech symetrií
a 486 orientovaných hran, včetně záporných souřadnic. Výsledek
`coordinates-checked.json` doplňuje uvedené obecné důkazy.

## 125: obecné dělení a již vedená chyba F063

Zvětšení má kladný celočíselný faktor k. Správné souřadnice malých
trojúhelníků jsou `(kx+p,ky+q)` a `(kx+p',ky+q')'`, nikoli tiskované
`(kx+p,kx+q)` a `(kx+p',kx+q')'`. Už pro k=1 a původní buňku `(0,1)`
tisk buňku posune do `(0,0)`, ačkoli zvětšení faktorem jedna ji musí
zachovat. Původní PDF i autorův PS obsahují tutéž chybu. Je to F063,
které bylo potvrzeno dříve; starý důkaz ani jeho 400 kontrol nemažeme.

Pro nečárkovaný původní trojúhelník je zvětšená oblast určena
`u≥kx`, `v≥ky`, `u+v≤k(x+y+1)`. V rovnoběžníku mají kandidáti
`0≤p,q<k`. Maximum součtu souřadnic nečárkovaného malého trojúhelníku
je `k(x+y)+p+q+1`, čárkovaného `k(x+y)+p+q+2`. Všechny jeho vrcholy
jsou tedy uvnitř právě tehdy, když `p+q<k`, respektive `p+q<k-1`.
Počty těchto dvojic jsou `k(k+1)/2` a `k(k-1)/2`, dohromady k².

Čárkovaný původní trojúhelník zabírá druhou polovinu rovnoběžníku.
Analogická podmínka na minima dává `p+q≥k` pro nečárkované malé
buňky a `p+q≥k-1` pro čárkované. Jsou to právě zbývající možnosti;
počty obou orientací se vymění. Vnitřky se nepřekrývají a hranice
navazují. Lineární zvětšení zachovává tyto vlastnosti také mezi
různými původními buňkami, takže s buněk dává sk² malých buněk.

Nových 882 přesných kontrol používá všechny k=1,…,9, obě orientace
a x,y=−3,…,3. Rozhodnutí podle nerovností souhlasí s vrcholy každého
kandidáta i s oběma binomickými počty. Konečný test sám nenahrazuje
obecný důkaz předchozích odstavců.

## 126: kódování jako barevné pokrytí

Barevný typ je cyklická orbita tří písmen z a,b,c,d, nikoli orbita
se zrcadlením. Burnside dává `(4³+2·4)/3=24` typů. Čtyři jednobarevné
typy mají jednu orientaci, dvacet ostatních tři: dohromady 64 umístění
na libovolnou pozici. V šestiúhelníku je 24 buněk a 42 geometrických
hran, z nich 12 obvodových.

Primární položky jsou 24 pozic, 24 typů a pomocná položka `*`.
Sekundární položky představují 42 hran a barva u jejich výskytu
udává skutečnou barvu hrany. Každá ze 24·64 možností položí jeden
typ na jednu pozici. Poslední, vynucená možnost pokryje `*` a
obarví všech 12 obvodových hran a. Celkem je tedy 49 primárních
položek a 1537 možností. Pokrytí musí použít každý typ a každou
pozici právě jednou; shodné barvy na sdílených hranách a bílý okraj
jsou přesně pravidla hlavolamu. Obrácený převod z libovolného
dláždění je jednoznačný. Tím máme bijekci, nikoli jen podobnost modelů.

Původní autorův `macmahon-triangles-dlx.w` byl samostatně přeložen
a spuštěn s předepsanými argumenty `00+ 10 10+ 01 01+ 11`.
Po cyklické normalizaci názvů dílků produkuje úplně stejných 1537
možností jako náš geometrický generátor. Liší se pořadí položek,
možností a reprezentant některých cyklických názvů. Toto pořadí může
ovlivnit náklad MRV, nikoli množinu řešení; je zachováno v
`author-full.xcc` a porovnání v `author-generator-checked.json`.

Ze stránky 91 bylo vyčteno a zkontrolováno všech 222 barevných výsečí:
24 definičních dílků, dvě úplná dláždění po 24 dílcích a dva chirální
příklady. Obě dláždění obsahují každý typ právě jednou, sdílené hrany
souhlasí a (59b) má celý okraj bílý. Jeho monochromatické buňky jsou
a=20, b=21, c=12, d=22. Dva chirální příklady jsou rozdílné cyklické
typy se stejnou množinou barev. Nejnovější kontrola nenalezla chybu
v žádné z těchto výsečí.

## 126: proč lze dělit dvanácti a šesti

Z hotového důkazu 119 přebíráme, že bílý dílek aaa musí zaujmout jednu
z 12 obvodových pozic. D6 působí na těchto pozicích tranzitivně
a s triviálním stabilizátorem. Žádná netriviální geometrická symetrie
proto nemůže zachovat celé dláždění. Zrcadlení je zde dovoleno jako
transformace celého vzoru: inventář obsahuje obě chirální podoby,
takže vznikne opět přípustné dláždění, ačkoli se jeden fyzický dílek
samostatně nesmí obrátit.

Zvolíme-li aaa na pozici20, získáme právě jeden reprezentant z každé
geometrické orbity. Zbývá volné přejmenování b,c,d: každá z těchto
barev se skutečně vyskytuje, takže žádná netriviální permutace
nezachová označené dláždění. Také kombinovaná akce je volná:
stabilizace nejprve vynucuje pevnou pozici aaa, tím identickou
geometrii a potom identickou permutaci barev. Každá orbita má
12·6=72 prvků. Úplný počet 987816 s aaa=20 tedy dokazuje
11853792 všech označených dláždění a 164636 tříd.

## 126: oprávněnost obou prahů primárních položek

Prahová proměnná Θ začíná na b. V každém okamžiku jsou barvy menší
než Θ již rozlišené; barvy ≥Θ se smějí libovolně permutovat.
Pozice trojúhelníku a položka `*` se při tom nemění. Jméno dílku
se však může změnit, proto nemůže být libovolný takový dílek vždy
bezpečně vybranou primární položkou.

První varianta povolí položky dílků teprve při Θ=e; tehdy je zbývající
barevná grupa triviální. Druhá dovolí dílek hned, jakmile Θ přesáhne
všechny barvy jeho názvu: ty jsou již pevné, takže příslušná primární
položka i její dostupné možnosti jsou invariantní. V každé větvi
zbývají vhodné položky pozic, dokud nejsou všechny buňky obsazené;
nevyrobíme tím neúplný model bez možnosti větvit.

MRV volba v tomto modelu závisí jen na délkách invariantních položek
a pevném pořadí remíz. Pořadí tří hran uvnitř možnosti závisí na
geometrii, nikoli na barvách, a přejmenování je nemění. Máme proto
obvyklou jednoznačnou kanonizaci podle prvního výskytu nepojmenované
barvy. Tím je pro tuto konkrétní aplikaci splněna i podmínka pořadí,
která zůstává interpretační otázkou C031 u obecného zadání122.

Úprava původního DLX2 je izolovaná ve `dlx2-macmahon126.w`; původní
zdroje a další běžící výpočty se nemění. Všech 24 malých nativních
případů dalo stejné celé množiny jako nezávislý úplný oracle;
16 symetrických případů navíc souhlasí s jiným interpreterem.
Vyzkoušena byla obě pořadí primárních položek a čtyři rodiny dílků.

## 126: úplné množiny řešení a rozsah výpočtů

Nezávislý řešič `xcc_bitset.cpp` používá neměnné množiny konfliktů
a bitové operace, nikoli obousměrné seznamy a undo algoritmu C.
Všechny jeho modely prošly kontrolou 42 hran, všech 24 typů,
hranice i fixovaných jednobarevných dílků; žádné dva nejsou totožné.

| Omezení | Původní/odvozený C | Nezávislý výčet | Přímé porovnání |
|---|---:|---:|---|
| aaa=20, tři ne bílé jednobarevné dílky na12,21,22 | 2138 | 2138 | Celé stejné množiny |
| aaa=20, tři ne bílé jednobarevné dílky na11′,21′,12′ | 2670 | 2670 | Celé stejné množiny |
| aaa=20, všechny b,c,d označené | 987816 | 987816 | Všechny nezávislé modely validní; C vypsal 98 vzorků |
| aaa=20, kanonizace b,c,d s dřívějším povolením dílků | 164636 | 164636 orbit | Celé stejné množiny orbit |
| Bez ukotvení aaa, původní C | 11853792 | 12·987816 odvozeno dokázanou symetrií | Úplný počet C, 118 validních vzorků |

Ve třetím řádku nepředstíráme úplný výpis původního C. Úplné
porovnání čtvrtého řádku však dokládá jednu třídu za každých šest
označených modelů nezávislého výčtu; všech 164636 orbit má velikost6.
Naše pojmenování b/c v první centrální variantě je proti (59b)
prohozené; globální přejmenování dává bijekci, a nemění proto2138.

Přijímací porovnání je `compare_macmahon126.py` a
`cross-solver-checked.json`. Jen čte dokončené výsledky, kontroluje
jejich hashe a porovnává celé množiny; nespouští nové hledání.
Přímý původní C bez ukotvení dokončil11853792 dne2.11.2026 v07:28UTC.
Všech118 vypsaných vzorků prošlo geometrickou validací, včetně správného
okraje a jedinečnosti všech24 dílků. Jde o každý stotisící model,
nikoli celý výpis. Terminál a hashe jsou samostatně přijaté; obecné
odvození celkového počtu na tomto běhu nezávisí.

## Paměťové náklady a známé erratum E064

DLX2 zaznamenává hrubé i odečitatelné přístupy, související s údržbou
sekundárních délek. Pro tyto náklady uvádíme obě hodnoty; nejde
o převod sekund nebo uzlů na μ. V našem kanonickém pořadí vstupu:

| Varianta | Hrubé mems | Po odečtu | Údaj v odpovědi126 |
|---|---:|---:|---:|
| Bez ukotvení, původní C | 391671085091 | 339830815607 | 340Gμ |
| aaa=20, původní C | 29052539997 | 25263330905 | 25Gμ |
| Prah všech barev Θ=e | 7844790180 | 6819572032 | 6.9Gμ |
| Prah podle barev dílku | 5149561785 | 4493232397 | 4.5Gμ |

Původní C a rychlá prahová varianta dávají uvedená zaokrouhlení
340G/25G/4.5G. Varianta čekající na všechny barvy dává6.8G,
nikoli6.9G. Samostatné dokončené porovnání ve skutečném pořadí
autorova generátoru dalo6.818661382G a4.492570993G, v obou případech
164636 řešení a164 validních vypsaných vzorků. Pouhá tato změna
pořadí tedy rozdíl6.9G nevysvětlila. Nejde automaticky o chybu knihy:
přesná historická implementace a vstup stále nejsou určeny. Evidence
je v `author-anchored-*-checked.json`; nešlo o opakování nedokončené
fronty a další slepé varianty nespouštíme.

Hlavní text na str.91 má5.2Gμ. Autorovo již zveřejněné erratum
ze17.12.2022, p.91 řádek−6, mění5.2Gμ na4.5Gμ. Odpověď126
na str.447 již4.5Gμ obsahuje. Vedeme to jako **E064 — known_erratum**,
nikoli nový nález. Čtyři aktuální autorovy soubory a šest relevantních
textových/TeX vrstev4B a4F5 byly prohledány; uložených30 kontextů
je v `errata-check.json`. Novější zdrojové soubory měly stejné hashe
jako archiv. Pro F063 ani pro geometrické vzorce124 nebyla oprava
v těchto vrstvách nalezena; není to tvrzení o neexistenci soukromého hlášení.

## Historické originály a zbylé mezery

Stažen původní MacMahonův *New Mathematical Pastimes* (1921),
[sken University of Toronto](https://archive.org/details/newmathematicalp00macmuoft).
Na tištěné str.5 (PDF19) byly zobrazeny oba původní obrazce Fig.5.
Levý má jednobarevný okraj a tři ostatní jednobarevné trojúhelníky
u středu. To potvrzuje přítomnost této konstrukce v originálu;
samotný obrazec neprokazuje autorův úmysl vyjádřený slovem
„specifically“. Přesnou totožnost všech barev s(59b) zatím netvrdíme.

Na tištěné str.113 (PDF127) byla přímo ověřena celá citovaná věta
o černé, bílé, červené a modré a jejich rozlišitelnosti v noci.
Odstavec výslovně mluví o výrobě trojúhelníků první části knihy.
Skeny, OCR, metadata původu a hashe jsou v `sources/triangles124_126/`.

Původní záznam Gottfriedova výpočtu z roku2001 zatím chybí.
Vyhledávání přesných jmen a počtů vrací převážně kopie samotné
Knuthovy odpovědi; ty nejsou nezávislým potvrzením prvenství ani data.
Gottfriedův TriMatch používá barvy vrcholů, takže jej nezaměňujeme
s tímto hlavolamem s barvami hran. Také původní patent3927/1892
MacMahon–Jocelyn ještě nebyl prohlédnut; MacMahonova kniha1921 jej
pro tvrzení o konkrétním patentu nenahrazuje. Proto hlavní str.91
a historický rozsah126 zůstávají částečné.

Doplněna také původní historická disertace Paula Garcii (Open University,
květen2006), stažená z [Rutgers](https://sites.math.rutgers.edu/~zeilberg/akherim/PAM.pdf).
Její str.64–65 popisují patent3927, přihlášku29.2.1892 a udělení28.1.1893,
včetně trojúhelníků a možnosti jednobarevného okraje. To poskytuje
nezávislou historickou podporu, nikoli prohlédnutí samotného patentu
nebo potvrzení totožnosti jeho dvou obrazců. Původní patentová URL
vrátila404; adresář Gottfriedových hlavolamů403. Tyto neúspěchy i
vyhledávací dotazy jsou zaznamenané v `history-search.json`; žádný
z nich nedokazuje, že pramen neexistuje.

Úlohy127–128 a zbytek odpovědní strany447 nejsou tímto blokem
automaticky uzavřeny. Dříve dokončené symetrické výčty129 a jejich
nálezF065 zůstávají zachované; nejsou zde znovu spuštěny.

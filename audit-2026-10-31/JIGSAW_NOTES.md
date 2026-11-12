# Nepravidelná sudoku a rozklady boxů: 7.2.2.1–59 až 63

Kontrola 1. listopadu 2026. Kniha: `taocp-vol4b-ed1-print2-2022.pdf`.
Hlavní text str.78–79, zadání str.129, odpovědi str.428–429.
PDF pořadí je tištěná strana+20. Autorův původní `fasc5c.ps.gz`, převedený
do PDF, má odpovídající strany14,65,132–133; ty byly také zobrazeny.
Vydaný Fascicle5 má hlavní stranu76, zadání127 a odpovědi236–237.
Fyzický výtisk nebyl ověřen.

## F116: jedna chybná číslice v Behrensově obdélníku

**Str.78, obrázek(35b), šestý řádek a sedmý sloupec: `6` má být `5`.**
Zde číslujeme řádky a sloupce od1; v nulových souřadnicích jde o(5,6).

Tištěný řádek `6971426` obsahuje dvakrát6. Poslední sloupec je
`241896673`, opět se dvěma6 a bez5. Příslušný devítipolový box obsahuje
`138769426`, se stejným problémem. Už tyto tři krátké seznamy jsou ručním
důkazem, bez řešiče. Pravidlo na následující straně výslovně zakazuje
opakování v řádku i sloupci, i když obdélník nemá devět sloupců.

Po změně poslední číslice šestého řádku na5 jsou všechny řádky bez
opakování a každý sloupec i box obsahuje právě1–9. Prošli jsme také
všech63×8 změn jediné číslice: tohle je jediná oprava, která napraví
celou tabulku. Neříkáme tím, co bylo v nepřístupném původním článku1956;
chyba je doložená přímo v Knuthově PDF i jeho starším PostScriptu.

Aktuální a úplná historická errata4B/F5 odpovídající opravu neobsahují.
Čtyři vzdálené oficiální originály byly znovu staženy pro kontrolu hashů;
oproti našemu archivu se nezměnily. Přesný záznam:
`results/jigsaw/errata-check.json`. Potvrzení neznamená prvenství ani
slíbenou odměnu. V UI má tento drobný obrázkový překlep nízkou závažnost.

## Podklady: celé diagramy z původních vektorů

`extract_jigsaw.py` čte polohy původních glyphů a silné hranice boxů
z výstupu `mutool draw -F trace`. Ukládá33 diagramů, včetně všech buněk,
hran, souvislých částí, barev a původních souřadnic. Duplicitní vykreslení
téže nápovědy pod hotovým řešením musí mít stejnou hodnotu.

U(34c) je New York záměrně nesouvislý: Long Island je samostatná buňka.
Stejná růžová výplň ji přiřazuje k osmi ostatním buňkám. Není to chyba
velikosti boxu. Všechny tři tvary(34) souhlasí mezi zadáním a řešením;
totéž platí pro tři Puzzlium obrazce a pětiboxový Behrensův příklad.
ObrázekA–2(d) má všech81 číslic shodných s(35c).

U Puzzlium byly otvory zkontrolovány ve vykreslené stránce. A/B mají
30 buněk a pět hexomin, C má24 buněk a čtyři hexomina. Vnitřní bílá
buňka v B se nepočítá jako další box. Žádný diagram nebyl rekonstruován
z pouhého pořadí číslic v OCR.

## 59: tři jednoznačná řešení; C022 vymezuje počítání uzlů

Nezávislý souřadnicový program se sousednostmi a vynucenými hodnotami
a původní nemodifikovaný DLX1 našly přesně tři vytištěné úplné odpovědi,
pro každé zadání jedinou. Všech243 hodnot, všechny nápovědy a všechny
řádkové, sloupcové a boxové podmínky souhlasí.

Pro hlavní text byly zvlášť ověřeny oba jednoduché kroky: v horním
řádku(34a) může být4 jen ve sloupcích7/8 při číslování od0; pro A ve
sloupci2 obrázku(34b) zůstává jen řádek0.

| Příklad | Pořadí symbolů | Kniha | Všechny návštěvy X2 |
|---|---|---:|---:|
| 59a |123456789|1105|1106|
| 59b |GRANDTIME|910|911|
| 59c |AFKLNTVWY|122|123|
| 60a |123456|23|24|
| 60b |123456|26|27|
| 60c |123456|16|17|

U všech šesti případů druhý program s bitovými množinami možností
reprodukuje **celý profil po hloubkách**, nejen součet. Primární položky
jsou v pořadí p,r,c,b, shody MRV se rozhodují jejich pořadím. U59b záleží
také na pořadí symbolů: abecední ADEGIMNRT dává948 uzlů, pořadí uvedené
v textu GRANDTIME dává911. Proto samotný abecední běh nebyl považován
za důkaz chyby čísla910.

**C022 je pouze kandidát nízké závažnosti.** Knižní čísla jsou přesně
počty po vynechání jediného úspěšného listu (u jednoho řešení také stejné
jako vynechání kořene). Doslovný X2 na str.69 vstupuje do kořene i do
hotového řešení; srovnávací89 uzlů sudoku na str.77 již v předchozím
bloku souhlasilo s inkluzivním DLX1. Nejkratší příklad zde je60c:
16 nevyplněných buněk,16 vynucených hran,17 uzlů. Možnou záměrnou
konvenci počítání ponecháváme otevřenou, místo šestinásobného počítání
drobného rozdílu jako šesti potvrzených chyb.

## 60: částečné řádky a sloupce

Každá buňka a každá hodnota v boxu musí být pokryta právě jednou.
Řádek/sloupec kratší než6 pouze zakazuje opakování; jeho hodnotové
položky proto musejí být sekundární. U délky6 různost a šest dostupných
symbolů naopak vynutí každou hodnotu. To dává obecný důkaz modelu(30)
i pro nepravidelný vnější obrys. Oba řešiče potvrdily celé tři odpovědi.

Podařilo se archivovat původní čtyřstránkovou sbírku Puzzlium2014
z `http://www.puzzlium.com/com14/abc.pdf`. Sudoku je na stranách3–4,
první trojice je A/B/C. Původní A má navíc nápovědu3 v posledním řádku,
druhém sloupci. Je redundantní: přidání do knižního zadání ponechává
stejné jediné řešení. B/C a všechny hranice jsme vizuálně porovnali.
Není tedy přesné tvrdit, že knižní A je doslovná kopie všech původních
nápověd; matematickou chybu v této úpravě jsme nenalezli.

PDF potvrzuje rok2014 a souvislost se stoletým výročím Martina Gardnera.
Přesný den prvního oznámení21.10. a individuální autorství obou
Grabarchuků z tohoto podkladu samostatně neplynou; to zůstává
historickou mezerou, vedle konvence C022.

## 61: všech53130 pětinápovědových podmnožin

Původní DLX1 i souřadnicový program daly stejných **1800** úplných
tabulek odpovídajících pěti vytištěným boxům. Pro každou z C(25,5)=53130
podmnožin jsme pak přesně určili, které z těchto1800 tabulek s nápovědami
souhlasí. Referenční(35a) je vždy mezi nimi.

- Přesně **1315** podmnožin připouští jedinou tabulku.
- Přesně **175** z nich používá všech pět číslic.
- Každá z1315 kladných podmnožin prošla také samostatným souřadnicovým
  hledáním; ke každému z ostatních51815 případů je uložen index konkrétní
  druhé tabulky a zkontrolována shoda nápověd.
- ObrázekA–2(a) je lexikograficky první **mezi175** případy se všemi
  číslicemi: nulové pozice0,1,4,6,12. Mezi všemi1315 je první
  0,1,2,12,19. Antecedent věty v knize jsou právě175 případů; nejde
  o nový nález.

Celé tabulky a všechny podmnožiny jsou v `61-models.json` a
`61-subsets.json`. Úloha61 je plně zrevidovaná.

## 62: počty boxů, rozkladů a symetrií

Každou přípustnou souvislou oblast jsme získali dvěma různými cestami:
doslovným Algorithm R s přenášením TAG z dříve prověřené úlohy
7.2.2–76 a růstem všech normalizovaných polyomin přidáváním hraniční
buňky. **Celé množiny umístění**, ne jen jejich počty, se shodují až do n9.

Rovný n-ominový box lze při návštěvě řešení odmítnout z koncových
souřadnic v0 a v[n−1]: stejný řádek/sloupec a vzdálenost n−1. V konečném
n×n čtverci takový nejkratší spoj může mít jen rovný tvar; naopak
kanonické pořadí R pro rovnou oblast končí druhým koncem. Kontrola byla
porovnána s úplnou množinou řádkových/sloupcových souřadnic každého boxu.
Pro n1/n2 jsou všechny tvary rovné, takže žádné přípustné vzory nevznikají.

| n | Nerovné boxové možnosti | Všechny rozklady | Třídy dle počtu symetrií1/2/4/8 |
|---|---:|---:|---|
|3|16|0|žádné|
|4|105|33|2 /3 /2 /1|
|5|561|2082|256 /7 /3 /0|
|6|2804|320098|39791 /439 /7 /0|
|7|13602|132418528|16550986 /2660 /0 /0|
|8|64662|celkový počet zde netvrzen|kontrolovány tři příklady|
|9|302556|celkový počet zde netvrzen|přesně tři vzory se všemi8 symetriemi|

Celkové počty n3–6 potvrdil původní DLX1 a samostatná C++ rekurence
nad maskou zbývajících buněk. Ta používá první volnou buňku, rozklad
na souvislé komponenty a memoizaci, žádné dancing links. Každá další
volba je box obsahující první nepokrytou buňku, takže žádný rozklad
nechybí ani se nezapočítává vícekrát. Komponenty nelze spojit souvislým
boxem; jejich počty se násobí. Omezení počtu uložených stavů mění
jen rychlost, nikoli rekurenci.

Pro n7 tato rekurence skončila za10.389s s132418528 rozklady,19433759
voláními a682771 uloženými stavy. **Původní DLX1 n7 dokončen 2. listopadu
2026 v02:15:29UTC**, po18275s. Potvrdil132418528 řešení,983498562 uzlů a
celý profil. Jeho vstup, výstupy, binárka a původní zdroje prošly hashovou
kontrolou v `check_jigsaw_terminal.py`, bez dalšího hledání. Wrapper789648
je terminální; neregenerovat jej kvůli chybějícímu živémuPID.

Zůstává historický benchmark: původníDLX1 zde spotřeboval24619131223049
mems, tedy24.619T, zatímco kniha uvádí1.9Tμ. Výstup má také1894211822180
updates, což je jiná veličina. Na str.72 je Gμ výslovně definováno jako
**gigamems**; numericky blízkých1.894T updates proto nevydáváme za shodu
s1.9Tμ. Pořadí vstupu a historická implementace stále nejsou doložené.
`results/jigsaw/tilings/terminal-checked.json` přijímá všechny hotové případy
v původním wrapperu. X062 zůstávápartial pouze kvůli benchmarku.

Další nezávislé porovnání poskytují Harrisovy tabulky2010. Z jeho
počtů T(n,m) obdélníků n×m s povolenými rovnými boxy lze pomocí
inkluze-exkluze odečíst rozklady s celým rovným řádkem. Předepsané
řádky oddělí nezávislé obdélníkové mezery; jejich počty se násobí.
Rovný řádek a rovný sloupec nemohou současně patřit jednomu rozkladu,
proto se výsledek odečte dvakrát. Pro n3–7 tato samostatná formule
z původních tabulek dává přesně čísla knihy. Pro n7 je počet s alespoň
jedním rovným řádkem13167643 a158753814−2×13167643=132418528.
Jde o kontrolu vůči publikovanému nezávislému výpočtu, ne o tvrzení,
že jsme znovu spustili celý Harrisův původní program.

Symetrie jsme počítali samostatně. Pro každou neidentickou symetrii D4
seskupíme všechny boxy do orbit. Orbitu s překryvem jejích členů
odmítneme, zbytek tvoří možnosti přesného pokrytí. Invariantní rozklad
je právě sjednocením celých takových orbit. Původní DLX1 a nezávislé
bitové pokrytí souhlasí počty i celými profily; všechny vzniklé rozklady
byly rozvinuty a samostatně validovány.

Pro n7 je10640 symetrických rozkladů,2660 tříd po4 prvcích:
2265 tříd s půlotáčkou,354 s osovým zrcadlením,41 s diagonálním.
Všech osm obrázků n4 a šest obrázků n7/n8 má správné tvary a
vyznačené počty symetrií. Pro n9 pokrytí orbit celé D4 má58 možností,
17 uzlů a právě3 řešení: normální3×3 boxy a přesně dvě vytištěné
alternativy. Tvrzení o dvou dalších vzorech se všemi osmi symetriemi tedy není
odhad založený na náhodném hledání.

## 63: všechny duhové rozklady a faultfree podmnožina

Z úplné množiny302556 nerovných umístění devítimin jsme vybrali
právě3173 s různými číslicemi referenční tabulky. Po odebrání devíti
standardních sudoku boxů zbývá3164. Původní DLX1, nezávislá rekurence
nad zbývajícími buňkami a úplný bitový výčet souhlasí:

| Omezení | Počet |
|---|---:|
|všechny duhové rozklady|98556|
|žádný standardní3×3 box|42669|
|navíc žádná přímá dělicí čára přes celý čtverec|24533|

U všech98556 modelů jsme samostatně ověřili úplné rozdělení81 buněk,
devět duhových boxů a dvě ekvivalentní kontroly faultfree: každá
vodorovná/svislá vnitřní čára musí být překročena nějakým boxem;
nezávisle podél takové čáry musí existovat dvojice sousedních buněk
se stejným boxovým štítkem. ObrázekA–2(d) přímo patří do24533 modelů.

Počty podle počtu standardních boxů0–9 jsou
42669,36771,11466,5919,1023,632,35,40,0,1. Jejich součet je98556.
Celé množiny modelů a celý hloubkový profil jsou archivované.

**Historických1.2Gμ zatím nereprodukujeme.** Původní DLX1 s uvedeným
vstupem má12019710355 hledacích memů, tedy12.020G, a766784 uzlů.
Po odstranění standardních boxů má7.647G a438802 uzlů. Implementace,
pořadí a historický vstup mohou ovlivnit benchmark; rozdíl jsme
nepovýšili na potvrzený překlep desetinné tečky. Úloha63 proto zůstává
částečná pouze v této vymezené části.

## Citace a meze historické kontroly

- [Harris2010, původní rukopis](https://www.bumblebeagle.org/polyominoes/tilingcounting/counting_9x9_tilings.pdf)
  má datum13.3.2010, výslovně G4G9 a tabulky8×8/9×9 s povolenými rovnými
  boxy. Také odkazuje na svůj Grand Time článek2009, str.55–57. Přesné
  znění tohoto druhého článku ještě nemáme archivované.
- [Snyderův vlastní přetisk](https://www.gmpuzzles.com/images/puzzles2025/250809-StatesSudoku-Then.pdf)
  přímo datuje původní puzzle9.6.2006. Všechny nápovědy a regiony byly
  vizuálně porovnány; zvlášť vysvětluje odpojenou buňku New Yorku.
- [Původní Puzzlium ABC](http://www.puzzlium.com/com14/abc.pdf)
  potvrzuje kolekci2014. Rozdíl redundantní nápovědy A je výše.
- Originální Behrensův článek1956, původní časopis Thompson1996
  str.51/67, tvrzení o nejstarší publikaci sudoku a Ragallerova atribuce
  zbývají. Bibliografická shoda v pozdějších článcích není náhradou za
  prohlídku těchto původních stran. Tato mez se týká hlavního textu,
  nikoli platnosti explicitního protipříkladu F116.

## Reprodukce a vlastní implementační opravy

Krátké kontroly: `extract_jigsaw.py`, `check_jigsaw_small.py`,
`check_jigsaw_supplement.py`, `check_jigsaw_errata.py`.
Geometrické možnosti: `prepare_jigsaw_tilings.py`.
Symetrie: `check_jigsaw_symmetry.py`; duhové modely:
`check_jigsaw_rainbow.py`. Dlouhý wrapper `run_jigsaw_counts.py`
už běží; nespouštět duplicitně. Hash zdroje, binárky, vstupu,
výstupů a čas jsou uložené u každého běhu.

Před přijetím výsledků jsme opravili vlastní pomocné kroky:

1. Rozteč malého obrázku61 byla prvně odhadnutá jako38.14/5;
   původní vektorový obrys má38.081/5. Aserce velikostí regionů
   první chybný přepis okamžitě odmítla; konečný výstup už souhlasí
   s nezávisle umístěným(35a).
2. Test rovnosti prvně použil rozdíl plochých indexů, který může
   přetéct přes konec řádku. Správný test používá obě souřadnice.
   Plné porovnání s růstem polyomin bylo provedeno až po opravě.
3. První souřadnicový řešič používal pouze nahé kandidáty a u59b
   byl zbytečně pomalý. Jen tento nový proces byl zastaven; po přidání
   logicky vynucených hidden singles proběhl celý konečný výčet.
4. Generátor orbit původně opakovaně hledal minimum velké množiny,
   což bylo pro302556 možností kvadratické. Jen tento nový proces
   byl zastaven a nahrazen jedním seřazeným průchodem. Konečná
   kompletní kontrola se opakovala s novým hashem zdroje a uspěla.

Nejsou to chyby knihy. Dřívější dlouhé Langfordovy a dámské výpočty
nebyly restartované; totéž platí pro běžící n7 DLX1. Žádné nové
emailové návrhy nevznikly a nic nebylo odesláno.

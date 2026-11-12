# Sudoku 51–54: násobnosti, malé tabulky a minimální nápovědy

Pracovní vydání: 4B, první vydání, druhý dotisk 2022. Zadání na str. 129,
odpovědi na str. 426–427. Zobrazeny všechny tři původní stránky a autorův
PostScript z roku 2019, str. 65, 130–131. Tištěný exemplář nebyl kontrolován.
V tomto bloku není nový potvrzený nález. C021 je drobný, dosud neuzavřený
rozdíl v mezipočtu kandidátů. E028 a E029 jsou známé opravy již zapracované
do našeho vydání.

## 51: dvě nerozlišitelné sedmičky

Každé políčko musí dostat právě jednu hodnotu. Položky pro řádky, sloupce
a boxy mají násobnost dvě pro číslici 7, jedna pro ostatní povolené číslice;
8 se nepoužívá. Jde přesně o bijekci mezi výplněmi požadovaného multisetového
sudoku a řešeními uvedeného vícenásobného pokrytí. Dvě výskyty 7 se tím
neoznačují a nevzniká faktor 2!.

`check_sudoku_multiplicity.py` porovnává celé množiny výsledků dvou postupů:
vlastní hledání podle zbývajících kapacit řádků/sloupců/boxů a nově sestavený,
neupravený autorův DLX3. Oba vracejí přesně šest tabulek. Všech 81 buněk,
původních 16 nápověd a všech 27 multisetů každého výsledku je ověřeno.
Vstup s ponechanými původními nápovědami má 297 položek a 536 možností.

Všech 64 vyplněných buněk obrázku odpovědi souhlasí. Obrázek dokonce přesně
odpovídá průniku šesti řešení, ne pouze nějaké jeho části. Dvě obyčejná řešení
(29c), nezávisle zjištěná v předchozím bloku, po sloučení 8 do 7 dávají tutéž
jednu tabulku z těchto šesti. Obráceně každý úspěšný rozklad sedmiček na
7 a 8 musí dát jedno z obou obyčejných řešení (29c). Proto je rozložitelná
právě jedna z šesti tabulek; má dva rozklady navzájem zaměňující 7 a 8.
Celá úloha je dokončena bez nálezu.

## 52: dohledaná instance a přesně vymezený benchmark

Původní adresa `sites.google.com/site/sudoeleven/` přesměrovává na přihlášení.
Sbírku však s autorovým souhlasem archivuje Denis Berthier:
[Classification-of-TE2-Sudokus](https://github.com/denis-berthier/Classification-of-TE2-Sudokus),
commit `99ee49c8c49fee525049c3e962c9a6338d48ed05`. Staženy jsou původní
seznam, README s vysvětlením původu a autorův dokument *Hardest Sudokus*
datovaný 27. května 2011. Každý soubor má URL, čas a SHA256.

Seznam má přesně 26 370 řádků. Řádek **6539 při číslování od jedničky** je
izomorfní s vytištěným zadáním. `52-isomorphism.json` obsahuje přímo
ověřitelnou transpozici, permutace řádků a sloupců a přejmenování číslic.
Z množiny přípustných geometrických transformací vychází jediná taková mapa.
Sousední řádky 6538 a 6540 při úvodní kontrole nesouhlasily; není posunutý
index seznamu.

Vytištěných 22 nápověd dává jediné řešení jak s původním DLX1, tak s nezávislým
souřadnicovým hledáním alternativy. DLX1 s explicitními semeny 0–999 dává:

| Veličina | Průměr | Výběrová směrodatná odchylka |
|---|---:|---:|
| Počet uzlů | 24 536,968 | 1 845,968 |
| Paměťové operace hledání | 12 205 477,84 | 916 526,12 |
| Inicializační paměťové operace | 186 110,856 | 30,011 |

To je řádově i rozptylem konzistentní s knižními 24 400 ± 1 900 a asi 12 Mμ.
Nejde o reprodukci historické sady semen nebo přesné původní implementace.
Samotnou přednost této instance před všemi ostatními 26 369 zadáními jsme
nepřeměřili. Ani knižní odpověď neprokazuje absolutně nejtěžší sudoku mezi
všemi možnými zadáními. „Kanonický tvar“ zde ověřujeme explicitním
izomorfismem; globální lexikografické minimum všech transformací netvrdíme.
Úloha zůstává částečná v těchto přesně uvedených bodech.

**E028:** F5 str. 234, náhrada odpovědi 52 z **14. prosince 2019**.
Starý autorův PS uvádí třetí instanci a 4 666 ± 550 uzlů. Nové zadání, zdroj
6539 i nové statistiky naše 4B již obsahuje. Datum je 14., nikoli 19. prosince;
ověřeno přímo z originální stránky errat.

## 53: úplný konečný prostor shidoku

Vlastní výčet přípustných řádkových permutací dává všech 288 úplných tabulek.
Celá tato množina se shoduje s původním DLX1 na prázdném zadání 4×4.
Grupa má 128 geometrických prvků a 24 přejmenování číslic. Její orbity
referenčních tabulek A a B jsou disjunktní, mají velikosti 96 a 192 a pokrývají
všech 288 tabulek. Stabilizátory mají přesně 32 a 16 prvků, jak tvrdí odpověď.

Každá ze čtyř oblastí diagramu C je v obou referenčních tabulkách čtyřbuněčná
záměna dvou číslic: jejich výměna pouze v této oblasti dává jinou platnou
tabulku. Bez nápovědy v některé oblasti tedy není řešení jediné. Přenesení
těchto oblastí příslušným izomorfismem dokazuje dolní mez čtyři pro každou
tabulku, nejen pro dvě vytištěné. Právě jednu nápovědu v každé oblasti lze
vybrat 4⁴ = 256 způsoby pro každou referenční tabulku.

Pro A i B je z úplného histogramu shod s ostatními 288 tabulkami spočítán
počet řešení **každé z 65 536 podmnožin**. Supersetová zeta transformace
nevolá žádný sudoku řešič. Minimalita se kontroluje odstraněním každé
jednotlivé nápovědy, následně se masky rozdělují podle všech automorfismů.

| Reference | Minimální 4 / 5 / 6 nápověd před symetriemi | Třídy 4 / 5 / 6 |
|---|---|---|
| A | 12 / 256 / 16 | 2 / 11 / 1 |
| B | 128 / 176 / 0 | 11 / 11 / 0 |
| Dohromady tříd | — | **13 / 22 / 1** |

Každý ze 14 vytištěných písmenových diagramů byl extrahován podle souřadnic
PDF a ověřen jako jednoznačný a minimální. Jejich třídy jsou různé a přesně
pokrývají 13 čtyřnápovědových a jedinou šestinápovědovou třídu. U poslední
je ověřeno i konkrétní tvrzení, že po odstranění kterékoliv nápovědy zůstane
prázdná oblast v C nebo Cᵀ.

**E029:** známé doplnění podmínky jednoznačnosti do otázky 53(b),
F5 str. 127, **21. března 2022**. Ve starém PS podmínka chybí, naše 4B
ji již obsahuje. Všechny matematické a obrázkové části jsou uzavřeny.
Výrok o prvenství Eda Russella v roce 2006 zatím nemá dohledaný nezávislý
primární záznam. Sekundární rozcestník vedl na
`forum.enjoysudoku.com/my-4-year-old-is-doing-sudoku-t30643.html`, ale přístup
selhal timeoutem a následně „No route to host“. Samotný rozcestník není
důkazem historického data. Kvůli tomuto jedinému bodu zůstává plný záznam
úlohy částečný; nejde o podezření na chybnou atribuci.

## 54: všech 777 minimálních podmnožin a úplný certifikát

V popsaném algoritmu zůstává každá známá nezbytná nápověda nezbytná
i v menším jednoznačném zadání, pokud je v něm obsažena. Protipříklad pro
větší zadání po odstranění nápovědy totiž splňuje také slabší menší zadání.
Proto lze množinu W předávat potomkům a sjednocovat ji při opakovaném X.
Každá minimální podmnožina Y ⊆ X musí obsahovat W i všechny nově zjištěné
nezbytné nápovědy. Je-li Y vlastní, některé xᵢ mimo Y lze odstranit a
odpovídající dítě Y stále obsahuje. To dokazuje úplnost sestupného průchodu.

Souřadnicový C++ program hledá alternativu k již známému řešení; nepoužívá
DLX ani jeho datovou strukturu. Každá vrácená alternativa je znovu ověřena
nezávislým Pythonem včetně všech 27 jednotek a všech zbývajících nápověd.
Vzniká 15 442 různých dotazů včetně potvrzení původního plného zadání,
tedy knižních **15 441** po jeho vynechání. Přesně 10 původních nápověd
je nezbytných. Všech 777 minimálních výsledků je poté samostatně předloženo
neupravenému původnímu DLX1; každý má právě jedno řešení.

| Počet nápověd | Minimálních podmnožin | Všech jednoznačných podmnožin |
|---|---:|---:|
| 32 | 0 | 1 |
| 31 | 0 | 22 |
| 30 | 0 | 200 |
| 29 | 0 | 978 |
| 28 | 0 | 2 780 |
| 27 | 8 | 4 609 |
| 26 | 154 | **4 244** |
| 25 | 387 | 1 950 |
| 24 | 206 | 373 |
| 23 | 22 | 22 |

Dodatečný certifikát se vůbec nespoléhá na úplnost C++ hledání ani na
navštívené větve sestupného algoritmu. Používá 777 pozitivních výsledků
ověřených DLX1 a 263 přímo ověřených alternativ pro negativní dotazy.
Podmnožiny postrádající některou z deseti povinných nápověd jsou vyloučeny
příslušným svědkem. Pro zbývajících 2²² masek se vytvoří dvě bitové množiny:
nadmnožiny všech pozitivních minimálních masek a podmnožiny negativních masek.
Jejich průnik je prázdný a sjednocení obsahuje všech 2²² masek. Tím je
certifikováno **všech 2³² = 4 294 967 296 podmnožin** původních 32 nápověd.
Jednoznačných je celkem 15 179. Tato kontrola také potvrzuje minimalitu
všech 777 masek a každý počet v tabulce.

Vytištěný obrázek na str. 427 je skutečně lexikograficky poslední z 22
minimálních zadání s 23 nápovědami, při uspořádání seznamů nápověd podle
řádků. Jeho DLX1 strom má přesně 220 uzlů. Současné odstranění závěrečných
dvou nápověd 9 a 5 původního zadání také zachovává jednoznačnost.

Booleovská formulace je správná: f je monotónní, protože přidání nápověd
nemůže přidat řešení a známá tabulka zůstává přípustná. U monotónní funkce
lze z každého implikantu odstranit negativní literály, proto prvoimplikanty
odpovídají přesně minimálním jednoznačným sadám kladných nápověd.

### C021: 4 249 kandidátních dvojic versus 4 244 různých zadání

PDF i autorův PS tisknou v kole s 26 nápovědami **4 249**. Při slučování
stejných X a jejich W vychází přesně **4 244**; všechny ostatní počty kol
souhlasí. Certifikát výše nezávisle prokazuje, že různých jednoznačných X
této velikosti je opravdu jen 4 244.

Text však výslovně počítá *kandidátní dvojice (W,X)*. Přesná historická
strategie cachování není zadána. Zkusili jsme i doslovnou množinu dvojic,
která slučuje jen stejné W i X: počty dvojic jsou
`1,22,397,2883,10786,22016,23588,11518,1912,72` a různé X mají stále
přesně uvedenou tabulku. Tento druhý průchod vyžádal 47 293 dodatečných
negativních dotazů; všechny mají ověřenou úplnou alternativu, archivovanou
bezeztrátově v `pair-extra-queries.json.gz`.

Ani jedna přirozená politika nedává 4 249. Přesto mohla původní implementace
zpracovat pět opakovaných kandidátů. Proto jde zatím pouze o nízký kandidát
na překlep nebo upřesnění významu počtu. Nevydáváme ho za potvrzenou chybu.
Údaj asi 1,5 Gμ rovněž není reprodukován historicky totožným programem;
nejde o cenu našeho nezávislého C++ programu. Úloha 54 proto zůstává
částečná, přestože všechny její sady, obrázky a logické argumenty jsou uzavřeny.

## Errata, reprodukce a vlastní neúspěšné kontroly

Čtyři oficiální soubory `all4b.ps.gz`, `all4f5.ps.gz`, `err4b.textxt`
a `err4f5.textxt` byly znovu vzdáleně ověřeny; SHA256 odpovídají archivu.
Prohledány současné i historické vrstvy podle čísel úloh, tématu i počtů.
Relevantní jsou pouze uvedené E028/E029; k rozdílu 4 249/4 244 není oprava.
Stejně číslované úlohy jiných sekcí nebyly zaměněny za sudoku.

Reprodukovatelné kroky:

```sh
python3 audit-2026-10-31/extract_sudoku_minimal.py
python3 audit-2026-10-31/check_sudoku_multiplicity.py
python3 audit-2026-10-31/check_shidoku.py
python3 audit-2026-10-31/check_sudoku_minimal.py
python3 audit-2026-10-31/check_sudoku_minimal_certificate.py
python3 audit-2026-10-31/check_sudoku_pair_census.py
python3 audit-2026-10-31/check_sudoku_extreme52.py
```

První běh úlohy 54 zastavila aserce předpokládající shodu všech knižních
mezipočtů. Následná verze rozdíl ukládá jako data; ostatní kontroly zůstaly
přísné. Úvodní pokus přehrát dvojice pouze s cache prvního průchodu selhal,
protože neobsahovala všechny dodatečné negativní dotazy; ty byly potom
skutečně spočítány a všechny jejich modely ověřeny. Žádné z těchto zastavení
se samo o sobě nepočítá za chybu knihy. Původní pracovní ruční přepis spodních
řádků obrázku 51 nebyl použit: rozhodující data jsou přesné souřadnice všech
64 číslic PDF, nikoli odhad z náhledu.

Následuje DLX55–58 a odpovídající hlavní text. Žádný emailový návrh nevznikl.

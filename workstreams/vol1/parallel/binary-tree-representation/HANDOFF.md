# Předání §2.3.2 — Binary Tree Representation of Trees

Technický audit hlavního textu a všech 22 původních úloh je dokončen.
Inventář je potvrzen původními obrazy: hlavní text začíná dole na p. 334
a končí prvním odstavcem p. 346; úlohy 1–12 jsou na 346, 13–19 na 347,
20–22 na 348; odpovědi začínají dole na 571 a končí nahoře na 575.
Žádná doplněná úloha nebyla nalezena. Přibyla odpověď 19 z roku 2024.
Zdroj je třetí vydání, první dotisk 1997; fyzický exemplář není ověřen.

**Strojově čitelný stav jednotlivých jednotek:** `UNIT_STATUS.json`.
U všech úloh jsou obecné důkazy či úplné programové řešení; u úloh 17
a 19 je technický stav oddělen od bibliografických mezer. Všechny
důkazy, definice a přesné předpoklady obsahuje `PROOFS.md`.

## Nálezy a známé zásahy

Root již nezávisle potvrdil a přidělil:

- **V1-C0042:** `reports/mult-overflowing-unity-test.md`. Pro
  c=−(b^5−1) program diferencuje c*x na 1, i když správná konstanta c
  je reprezentovatelná. Přeteče pouze test DECA 1.
- **V1-C0043:** `reports/pwr-overflowing-exponent-test.md`. Pro
  v=−(b^5−2) diferencuje x^v na v*x místo v*x^(v−1). Vstupní v,
  koeficient v i potřebný exponent v−1 se vejdou do slova; přeteče
  jen test v−2. V tomto příkladu se chyba MULT neaktivuje.
- **V1-C0044:** `reports/copy-time-constant.md`. Celý vstup COPY až
  po návrat trvá (36n+17)u, nikoli tištěných (36n+22)u. Volající JMP
  přidá 1u; dvě pomocné vstupní varianty jsou rozebrány zvlášť.

Názvy souborů zůstaly popisné; kořenové reporty a globální status
spravuje root. Zdejší reporty zachovávají původní status kandidáta
před předáním, toto předání zaznamenává výsledek kořenové revize.
Žádná zpráva autorovi nebyla odeslána.

Deset různých známých zásahů ve všech čtyřech vrstvách errat shrnuje
`ERRATA.md`; nejsou započteny jako nové nálezy. Původní relevantní
obrazy všech čtyř vrstev byly zobrazeny a jsou v images/. Živá shoda
snapshotů byla ověřena dříve v téže relaci, viz SOURCES.md.

`TRIAGE.md` navíc zaznamenává implicitní chybějící mez indexu v odpovědi
8. Bez této konvence je krajní případ nedefinovaný, ale není doložen
jednoznačný chybný výsledek. Záměrně to nepočítám jako čtvrtý nový nález.

## Programy a ověření

`programs.py` obsahuje celý skutečný MIX Program D, včetně tištěných
odpovědí COPY, DIV a PWR a známé opravy COPY2→COPYP2. `own_programs.py`
obsahuje vlastní skutečné MIX řešení všech tří podprogramů. Jeho COPY
používá frontu dvojic původních a nových uzlů; DIV/PWR používají
pojmenované mezivýsledky a bezpečná porovnání. Nejde o hostitelské
funkce nahrazující MIX instrukce. Oba úplné výpisy jsou exportovány
do `results/book-complete.mixal` a `results/own-complete.mixal`.

Hlavní validační dávka v `results/mix-validation.json`:

- 965 úplných diferenciací tištěného a 965 vlastního programu:
  v každé skupině všech 620 výrazů do čtyř uzlů nad listy 0,1,x,a,
  160 náhodných výrazů s 5–25 uzly a 185 případů napříč radicy 64–100.
- 249 samostatných COPY pro každý program, s promíchanými adresami,
  oběma kořenovými tagy a nezávislým vnějším kořenovým odkazem 3999.
  Kontrolují se úplné obnovení vstupu, registrové smlouvy, všechna
  vlákna, disjunktnost i zachování všech přidělených a volných uzlů.
- U tištěného COPY souhlasí každý z deseti uvedených řádkových počtů
  a přesný opravený čas. Samostatných 50 kontrol dokládá čas vlastního
  COPY 59n−2a+15 včetně přesměrovacího JSJ, bez volajícího skoku.
- 111 dalších hraničních případů vlastního programu, vyčerpání
  paměti pro všech 37 radiců a zachycení skutečně nereprezentovatelného
  nového exponentu. Tyto testy jsou odděleny od dvou nových chyb testu.
- Základní `mix-smoke.json` uchovává 74 původních chybných případů
  MULT/PWR, každý také po opravě. Nejkratší protipříklady mají tři uzly.

Počet 839 666 instrukcí a čas 1 347 908u v hlavním validačním JSON
zahrnují pouze jeho diferenciace a samostatné kopie; nepřičítají se
k nim neoznačeně další hraniční či vyčerpávací dávky.

Matematické kontroly jsou v `trees.json` a `tree-orders.json`:
2 056 lesů do osmi uzlů, 118 621 dvojic uzlů pro vlastní předky,
32 055 očíslovaných vstupů rodičovského algoritmu, 4 225 dvojic pro
vložení, 2 055 převodů původně binárních stromů a 10 404 porovnání
stromů s INFO v {0,1}. U počtu rodičovských vstupů jde o počet běhů,
nikoli počet různých polí.

Úloha 11 má vlastní diagram SVG i zkontrolovaný PNG a přesnou tabulku
odkazů. `algebra.py` je úplný běžící zjednodušovač požadovaných výrazů
a rozhodovač volných svazů. Rovnice (20) i (21) normalizuje přesně
na (22). Svazový algoritmus byl v 791 případech porovnán s nezávislým
konečným uzávěrem. Z 700 numerických příkladů aritmetiky prošlo 383;
317 s nedefinovanou doménou nebo numerickým rozsahem bylo výslovně
vynecháno. Obecný důkaz zjednodušování je algebraický, nikoli numerický.

## Přesné meze a zbývající prameny

Technická práce v přidělené sekci nemá otevřenou úlohu. Úloha 17 je
otevřený návrhový úkol: dodané řešení splní požadovaný příklad a
uvedenou třídu přepisů, neslibuje úplnost pro všechny elementární
identity. Identita platí na původní doméně, kterou musí volající
uchovat, chce-li zachovat i množinu bodů definovanosti. Vlastní MIX
fronta má kapacitu 250 uzlů; veškerý MIX předpokládá dostatek živé
paměti a reprezentovatelné konstanty. Po chybě OVERFLOW není slíbena
transakční obnova.

Bibliograficky zůstává:

1. **Rok 1952 na p. 338 — partial.** Přímé svědectví Hopperové
   dokládá raný diferenciátor a dokončení Kahrimanianovy práce v
   květnu 1953. Přesné použití už v roce 1952 z dostupného pramene
   neplyne. Potřeba je původní Kahrimanianova práce či zpráva s datem.
2. **Sammetová 1966, odpověď 17 — plný text partial.** Primární
   vydavatelská metadata a bibliografie přes Crossref jsou ověřené,
   PDF endpoint vrací 403.
3. **Whitman 1941/1942, nová odpověď 19 — obsah partial.** Primární
   obsahy obou časopiseckých čísel potvrzují bibliografii a rozsahy;
   články se nezískaly. Skolem 1920 byl naopak získán a jeho relevantní
   §2 přečten včetně původních obrazů. Vlastní důkaz úlohy 19 je úplný.

Attribution Łukasiewicze je ověřena původním článkem z roku 1931,
p. 367 a poznámkou 3. Všechny URL, pokusy a lokální doklady jsou v
`SOURCES.md`; druhotné vyhledávací pomůcky nenahrazují primární důkaz.

## Reprodukce a izolace

Z kořene worktree:

```
python3 -B workstreams/vol1/parallel/binary-tree-representation/programs.py
python3 -B workstreams/vol1/parallel/binary-tree-representation/own_programs.py
python3 -B workstreams/vol1/parallel/binary-tree-representation/check_mix.py
python3 -B workstreams/vol1/parallel/binary-tree-representation/validate_mix.py
python3 -B workstreams/vol1/parallel/binary-tree-representation/check_trees.py
python3 -B workstreams/vol1/parallel/binary-tree-representation/check_tree_orders.py
python3 -B workstreams/vol1/parallel/binary-tree-representation/algebra.py
```

Sdílené simulátory, ledger, scope, RUN_STATE, ostatní pracovní složky
ani commity nebyly měněny. Nová práce začíná až po zmrazení této složky.

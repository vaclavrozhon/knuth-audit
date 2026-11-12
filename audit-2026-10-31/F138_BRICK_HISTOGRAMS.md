# F138 — nesprávné rozdělení kvádrů 2 × 2 × 4

**Potvrzená matematická chyba ve zkoumaných zdrojích, střední závažnost.**
4B, odpověď 7.2.2.1–147(b), str. 457 (PDF 477), tabulka případu
2 × 2 × 4. Stejná čísla má autorův draft z 11. 9. 2019, str. 161 (PDF 167).

Uspořádání šestnácti různých barevných kostek jsou rozdělena do chybných
kategorií podle barev vnějších stěn a počtu automorfismů. Čtyři řádky mají být:

| Barvy protilehlých vnějších stěn | Vytištěno | Správně |
|---|---|---|
| aa × bc × dd | (0, 3, 4, 2) | **(0, 3, 4, 1)** |
| aa × bc × de | (0, 11, 14, 2) | **(0, 11, 12, 2)** |
| ab × cd × ee | (0, 2, 2, 3) | **(0, 2, 2, 4)** |
| ab × cd × ef | (0, 1, 1, 1) | **(0, 1, 3, 1)** |

Čtyři složky označují počty tříd s 1, 2, 4 a 8 automorfismy. První dvě
kategorie 2 × 2 × 4 i všechny tabulky ostatních rozměrů vyšly správně.
Celkový počet **244** řad s fixovanou první kostkou a **48** tříd se nemění:
chyby se při sečtení vzájemně vyruší. Kontrola jen celkového součtu by je přehlédla.

## Nejkratší ověření

```bash
cd audit-2026-10-31
python3 verify_f138.py
```

Skript je samostatný, používá pouze standardní Python, žádné soubory ani
řešič. Přímo obsahuje **pět** konstrukcí s šesti různými vnějšími barvami.
Pro každou ověří všech šest barev na každé kostce, šestnáct různých
fyzických typů, všechny vnitřní kontakty a jednobarevnost vnějších stěn.
Potom ověří, že konstrukce nejsou navzájem ekvivalentní.

Kniha pro tuto kategorii uvádí celkem 0+1+1+1 = **3** třídy. Pět
ověřených příkladů ji vyvrací bez úplného výčtu. Počty symetrií těchto
pěti příkladů dávají (0,1,3,1). Samotný certifikát prokazuje dolní mez;
úplnost přesné opravy je doložená samostatnými výčty níže.

Kostky jsou v certifikátu řazeny podle souřadnic (x,y,z) pro rozměry
(2,2,4). Šest písmen znamená nahoře, dole, vpředu, vzadu, vlevo, vpravo.
Fyzický typ se určí pod 24 vlastními rotacemi kostky, bez ztotožnění
zrcadlových obrazů. Celý kvádr má 16 prostorových rotací/odrazů, které
zachovávají jeho rozměry. Pro každou z nich existuje právě jedno globální
přejmenování barev, které převádí první kostku na abcdef. Porovnání
takto normalizovaných konstrukcí tedy zahrnuje všechny povolené ekvivalence.

## Úplná nezávislá kontrola

Přímý CSP s barevnými proměnnými na stěnách dokončil **244** modelů
po 8 101 uzlech. Původní Knuthův DLX2 s doslovným modelem z knihy
(samostatné proměnné každé stěny a šest voleb vnější barvy) dokončil
stejných **244** modelů po 9 866 uzlech. **Celé množiny se přesně shodují**
a každý model je přímo validovaný. Nejde o dva běhy stejného modelu.
Oba běhy trvaly méně než sekundu, s nízkou prioritou a limitem jedné minuty.

Všech 48 orbit je uchováno v
`results/bricks147/bounded/2x2x4-checked.json`. Srovnání celých množin je
v `results/bricks147/followup/native-2x2x4-accepted.json`, přesné rozdíly
v `results/bricks147/claims-checked.json`. Malý certifikát je v
`verify_f138.py` a výsledek v `results/bricks147/f138-standalone.log`.

## Vydání a errata

Původní PDF druhého dotisku 2022 i autorův draft byly zobrazeny; dotčený
úsek tabulky je v obou totožný. Šest aktuálních a historických vrstev
errat bylo prohledáno podle stránky, úlohy i obsahu. Jejich hashe stále
odpovídají oficiálnímu stažení 3. 11. 2026 v 05:37 UTC. Odpovídající
oprava histogramů nenalezena. E074 a E075 na stejné stránce opravují jen
rok citace a zápis slova eight-cube.

Fyzický výtisk, celé nejnovější digitální vydání ani prvenství nálezu
nejsou ověřeny. Historické prameny ostatních částí úlohy zůstávají
odděleně otevřené a nemění tento konstruktivní protipříklad.

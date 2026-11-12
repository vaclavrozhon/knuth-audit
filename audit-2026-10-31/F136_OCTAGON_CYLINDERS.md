# F136: chybějící číslice v počtu válcových uspořádání

**4B, odpověď 7.2.2.1–142, strana 454, případ (ii), shoda levého a pravého okraje.**
Stav: doloženo v našem PDF i autorově PostScriptu. Střední závažnost.

| Výraz | V knize | Ověřená oprava |
|---|---:|---:|
| Zápis s faktorem 2 | 2 · 5980 | **2 · 55980** |
| Počet po ztotožnění přejmenování barev | 11 960 | **111 960** |
| Po dalším ztotožnění levopravého zrcadlení | 5 980 | **55 980** |

Počítají se uspořádání v pevném obdélníku 6 × 4, se všemi 24 různými
dílky právě jednou. Dolní dvě řady mají čtvrtiny orientované k vrcholům,
horní dvě k hranám. Každá společná půlhrana musí mít stejnou barvu;
stejně tak obě odpovídající půlhrany na levém a pravém okraji.
Barvy se mohou společně přejmenovat. Cyklický posun řezu válcem se zde
navíc neztotožňuje: používáme konvenci počtu v odpovědi s Algorithm C.

**Dva dokončené nezávislé výčty mají celé stejné množiny 111 960 řešení.**
První používá původní Knuthův DLX2 a matici barevného přesného pokrytí.
Druhý přímo přiřazuje barvy spojeným sektorovým proměnným a hlídá
jedinečnost cyklických typů dílků. Každý uložený model obou výčtů prošel
přímou kontrolou všech hran a celé sady. Žádné dvě řešení v téže množině
nejsou totožná po přejmenování barev. Levopravé zrcadlení je rozdělí
na 55 980 dvojic bez pevných bodů.

## Rychlá kontrola bez řešiče

Z kořene repozitáře spusť:

```bash
python3 audit-2026-10-31/verify_f136.py
```

Stačí standardní knihovna Pythonu a přiložený soubor
[f136-5981-classes.txt.gz](results/octagons142/f136-5981-classes.txt.gz),
který má **44 134 bajtů**. Obsahuje 5 981 zástupců různých tříd po
barvách i zrcadlení. Program u každého ověří úplnou sadu, shody hran,
uzavření válce, normalizaci barev a odlišnost od zrcadlového protějšku.
Tím doloží alespoň **11 962** uspořádání v knižní konvenci, tedy více
než uvedených **11 960**. Neprovádí hledání a netvrdí, že malý soubor
obsahuje všechna řešení. Přesnou opravu 111 960 dokládají oba úplné výčty.

Formát každého řádku je 24 čtyřpísmenných slov, sloupec po sloupci
zleva doprava, v každém sloupci zdola nahoru. Pro dolní řady je pořadí
sektorů dolní levý, dolní pravý, horní pravý, horní levý. Pro horní řady
je pořadí dolní, pravý, horní, levý. Písmena a/b/c jsou tři barvy.

- [Samostatný ověřovací program](verify_f136.py) a [výsledek](results/octagons142/f136-certificate-checked.json).
- [Přijetí obou úplných množin](results/octagons142/accepted/ii-lr.json).
- [Všech 111 960 modelů](results/octagons142/accepted/ii-lr-models.txt.gz) a [55 980 zástupců po zrcadlení](results/octagons142/accepted/ii-lr-representatives.txt.gz).
- [Původní stránka 454](images/vol4b-p454-vertices140.png), pořadí 474 v PDF.
- [Autorův draft ze září 2019, strana 158](images/fasc5c-p158-vertices140.png).
- [Kontrola šesti vrstev errat](results/octagons142/errata-check.json).

Čtyři oficiální soubory errat byly naposledy staženy 2. listopadu 2026
v 19:14 UTC a mají stejné otisky jako archiv. Pro tento nález byly
prohledány všechny relevantní současné i historické vrstvy 4B/Fascicle 5,
včetně čísel, textových klíčů a odlišného stránkování. Odpovídající oprava
nebyla nalezena. Jde o první vydání, druhý dotisk našeho PDF; fyzický
výtisk, úplná nejnovější digitální verze a prvenství nálezu nejsou ověřeny.
Celá úloha 142 zůstává částečně prověřená, dokud nedoběhnou hlavní výčty.

# F145: mazací smyčka odpovědi 221 zpracuje první uzel dvakrát

**Potvrzeno v našich zdrojích 3. listopadu 2026.** Sekce 7.2.2.1,
odpověď 221, knižní strana 475 (PDF 495), autorův draft strana 179
(PDF 185). Závažnost: vysoká; řešitelný vstup může být označen za neřešitelný.

Po vyjmutí adresy x ze zásobníku odpověď nastaví q=x a opakuje tělo,
dokud q≥x. U koncového spaceru nastaví q=ULINK(q). Podle (11) na
straně 68 tato hodnota ukazuje na první uzel předcházející možnosti.
Jestliže její začátek nebyl zkrácen, vrátí se tedy přesně na x.
Test q≥x dovolí další smazání téhož uzlu.

Nejkratší použitý svědek má primární položky a,b a sekundární s:

```
a b | s
a s:1
a
b s:2
```

Řádky 2 a 3 tvoří řešení. Řádek 1 je správně určen ke smazání, protože
jeho barva s:1 blokuje jedinou možnost pro b, která má s:2. Všechna známá
errata E011 a nulování značek z C013 zde již předpokládáme opravená.

Při obvyklém uložení mají hlavičky adresy 1–3, první spacer je 4,
první řádek tvoří uzly 5,6 a jeho koncový spacer je 7. Před smazáním
platí LEN(a)=2, LEN(s)=2 a ULINK(7)=5. Doslovná odpověď 221 provede:

| q | Operace | Následek |
|---|---|---|
| 5 | smazání uzlu a | LEN(a)=1 |
| 6 | smazání uzlu s | LEN(s)=1 |
| 7 | přechod přes spacer | q=ULINK(7)=5 |
| 5 | test primární položky s délkou 1 | přechod do P9, chybné zhroucení |

[Samostatný verifier](verify_f145.py) obsahuje explicitní paměťovou tabulku
a kontrolu všech osmi podmnožin tří řádků; neimportuje náš DLX ani solver.
[Výsledek](results/preprocess218_224/f145-witness.json) zachovává všechny
mezistavy. Předběžná nezávislá stopa využívající staré uložení P dala stejné
adresy 5,6,7,5. Nepotřebovali jsme nový výčet nativním DLX-PRE.

Jedna přímá oprava je vykonat tělo jednou a poté pokračovat jen pokud
q>x, tedy ukončit při prvním návratu q≤x. Tím se zahrne první uzel,
ale neopakuje se celý řádek. Vnitřní nulové spacery skáčou doprava;
koncový spacer se vrací na původní začátek, který je nejvýše x.
Ekvivalentně lze začít u x+1, projít zbytek cyklicky a x zpracovat
nakonec, jako to dělá autorův program.

Odpověď 222 používá pro jiný účel podmínku q≠p a není touto chybou
postižena. Autorův `dlx-pre.w` končí mazání po zpracování počátečního
uzlu na konci průchodu; tuto chybu knihy nepřebírá.

Starý `check_exact_preprocessing.py` procházel předem vytvořený seznam
uzlů a zásobník měl jako seznam adres. Jeho 1 500 úspěšných případů
zůstává důkazem správnosti tohoto modelu a nativního programu, **nikoli
doslovné podmínky smyčky 221**. Toto zpřesnění je přidáno do X218;
původní soubory a předchozí závěr zůstávají zachovány.

Nový krátký kontrolní blok testuje opravenou smyčku, dočasné přepsání
TOP, vnitřní i počáteční spacery a výstup 223 na šesti cílených vstupech.
Obě varianty návratu (úplný průchod a předčasný návrat uprostřed smyček)
zachovávají přesné množiny původních řádků. Celý blok trval asi 0,023 s
s nice 15, bez opakování starých výčtů.

Obě zdrojové stránky byly přímo zobrazeny. Šest vrstev úplných/aktuálních
errat 4B a Fascicle 5 včetně původních TeX zdrojů neobsahuje odpovídající
opravu; [záznam hledání](results/preprocess218_224/errata-check.json).
Fyzický výtisk, úplná nejnovější digitální verze a prvenství nálezu nejsou
ověřené. Žádná zpráva autorovi se nevytváří ani neodesílá.

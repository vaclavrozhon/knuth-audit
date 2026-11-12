# F146: políčko 22 nemůže vynucovat 00 u Y pentomin

Potvrzeno v našich zdrojích 3. listopadu 2026. Sekce 7.2.2.1,
hlavní text strana 111 (PDF 131), autorův draft strana 47 (PDF 53).
Závažnost střední: chybný konkrétní příklad předzpracování.

Obě přímo zobrazené verze uvádějí, že v druhém kole políčko 22 vynucuje
políčko 00. To je geometricky nemožné. Každá orientace Y pentomina
má ohraničující obdélník 2×4 nebo 4×2. Políčka 00 a 22 vyžadují alespoň
rozsah 3 v obou souřadnicích. Žádná možnost je tedy nemůže obsahovat obě.

Vynucování znamená, že každá zbývající možnost obsahující primární
položku 22 obsahuje také 00. Sloupec 22 nesmí být prázdný, jinak se
úloha zhroutí. Algorithm P možnosti pouze maže a zkracuje; nikdy do nich
nová políčka nepřidává. Výrok proto nemůže platit v žádném nezkolabovaném
kole, nezávisle na pořadí možností či položek.

[Samostatný verifier](verify_f146.py) kontroluje všech osm orientací
a obecnou invarianci vůči posunutí; neprovádí hledání pokrytí.
[Certifikát](results/preprocess225/f146-witness.json) obsahuje všechna
políčka a rozměry orientací.

Pravděpodobná oprava je **11 místo 22**. Dva krátké běhy původního
`dlx-pre.w`, s odlišným pořadím možností a políček, oba zaznamenaly:

- kolo 1: 20 je vynuceno položkou 10;
- kolo 2: 00 je vynuceno položkou **11**;
- kolo 4: možnost `50 51 52 53 62` blokuje 61.

Každý krok obou běhů byl následně nezávisle přehrán množinovým modelem,
včetně přesných původních identit řádků a zkrácených možností. Oba běhy
odstranily 352 možností a 20 položek. To podporuje navrženou opravu;
samotný důkaz chyby na shodě dvou běhů nezávisí.

První kontrola záměrně porovnávala výstup s knižní hodnotou 22 a selhala.
Následoval jeden odlišný krátký test pořadí a obecný geometrický důkaz.
Nejde o chybu OCR: [kniha](images/preprocess218-224-original-131.png)
i [autorův draft](images/preprocess218-224-draft-53.png) skutečně mají 22.
Šest úplných/aktuálních vrstev errat 4B/Fascicle 5 včetně TeXu neobsahuje
odpovídající opravu; [záznam](results/preprocess225/errata-check.json).
E100 na téže stránce opravuje jiný údaj, počet sudoku.

Fyzický výtisk, úplná nejnovější digitální verze a prvenství nejsou ověřené.

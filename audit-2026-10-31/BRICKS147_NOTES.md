# DLX 147 — barevné kvádry

Kontrola 3. listopadu 2026, 4B str. 143 a 456–458; autorův draft 2019
str. 79 a 160–162. Matematická část je uzavřená, s novým **F138** v tabulce
2 × 2 × 4. Celá položka zůstává partial kvůli konkrétním historickým pramenům.
Nebyl potřeba dlouhý brute force; nejdelší z provedených běhů trval asi
14,3 s, všechny měly nice 15 a pevný limit 60 s.

## Obrázky a reprezentace

Z vektorů původního PDF a draftu vyčteno všech **960 znaků šesti tensorů**,
z toho 285 barevných stěn. Obě verze jsou totožné. Všechny kostky mají
šest různých barev a jejich rotační typy se neopakují; všechny společné
stěny souhlasí, všech šest vnějších ploch je jednobarevných.
Samostatně vyčteno všech **24 označení čtyř kostek v zadání**; přesně
odpovídají malému tensoru i vytištěným jménům.

Souřadnice jsou x vpředu/vzadu, y nahoře/dole, z vlevo/vpravo.
Barvy jsou v bodech s právě dvěma lichými souřadnicemi, viz obecný důkaz
v úloze 145. Šest sousedních barev jednoznačně určuje orientaci kostky.
Všechna ostatní místa tensoru mají tečku; rozměry (2l+1,2m+1,2n+1) sedí.

Velký tensor skutečně používá všech 30 typů. Při tomto pořadí os jsou
jeho protilehlé barvy aa × cc × bb, což je knižní aa × bb × cc po přejmenování
barev. Počáteční chybný požadavek extraktoru na doslovné pořadí barev byl
opraven před přijetím výsledků; nebyla to chyba knihy. Druhá diagnostika
zúžila oblast obrázku v draftu, aby nečetla rejstříková slova na okraji.
Logy obou přípravných diagnostik jsou uchované; dokončené výčty se neopakovaly.

Automorfismy šesti tensorů: malý kvádr **8**, velký **2**, čtyři krychle
MacMahon/Kowalewski/Winter/čtvrtá **24,8,4,8**. Explicitní záměny
front↔back, top↔bottom, e↔f zachovávají velký tensor. Správná je i malá
záměna top↔bottom, d↔e. Příklad možnosti pro buňku135 a všech deset
položek volby horní stěny byly přímo ověřeny.

## Obecné důkazy

Počet pozic je lmn, počet fyzických stěn
lm(n+1)+l(m+1)n+(l+1)mn. Primární pozice vybírají jednu kostku,
sekundární typy zamezují opakování a obarvené stěny vynucují shodu sousedů.
Šest dalších primárních položek, každá se šesti barevnými možnostmi,
vynucuje jednobarevnost vnějších ploch. Každá geometrická konstrukce
tak dává právě jeden exact cover a naopak. Fixování první orientace
odstraní přesně volné působení 720 globálních permutací barev.

Stejná barva může být jen na protilehlých vnějších plochách: kterékoli
dvě sousední plochy se setkávají na kostce, která by jinak měla barvu
dvakrát. Proto se klasifikace vnějších barev redukuje na tři bity shody
protilehlých dvojic, s případnou výměnou stejně dlouhých os.

Kvádr1×m×n používá kostky se stejnou pevnou dvojicí protilehlých barev;
takových fyzických typů je přesně **6**, proto mn≤6. Pro1×1×n jsou čtyři
dlouhé boční barvy pevné, zbývající dvě se musejí v řetězci střídat,
takže třetí kostka by opakovala první typ: n≤2. Kvádr1×1×2 proto tvoří
zrcadlová dvojice.

Pro úplnost katalogu seřadíme l≤m≤n a použijeme lmn≤30. Při l=1 zbývají
jen1×1×1,1×1×2,1×2×2,1×2×3. Při l=2 zbývají2×2×n pro n=2…7
a2×3×n pro n=3…5. Při l=3 zbývá jen3×3×3; l≥4 je objemově nemožné.
Všechny tyto případy byly uzavřeny krátkým úplným výčtem.

## Úplné konečné výčty

Přímý C++ CSP sdílí barevnou proměnnou všech stěn téže vnější plochy,
vybírá nejvíce omezenou dosud neumístěnou kostku a hlídá různorodost
fyzických typů. Každý výstup je poté geometricky validován v Pythonu.
První kostka je abcdef. Stabilizátory a orbity vznikají z doslovných
prostorových symetrií kvádru a globálního přejmenování barev.

| Rozměry | Normalizovaná řešení | Třídy |
|---|---:|---:|
| 1×1×1 | 1 | 1 |
| 1×1×2 | 1 | 1 |
| 1×1×3 | 0 | 0 |
| 1×2×2 | 3 | 2 |
| 1×2×3 | 1 | 1 |
| 2×2×2 | 26 | 4 |
| 2×2×3 | 102 | 22 |
| 2×2×4 | 244 | 48 |
| 2×2×5 | 278 | 45 |
| 2×2×6 | 0 | 0 |
| 2×2×7 | 0 | 0 |
| 2×3×3 | 356 | 42 |
| 2×3×4 | 170 | 38 |
| 2×3×5 | 8 | 2 |
| 3×3×3 | 0 | 0 |

Celkem1190 normalizovaných konstrukcí a206 tříd napříč rozměry.
Pro dotčené2×2×4 má původní DLX2 **celou stejnou množinu244 modelů**
(0,69s). Oba algoritmy také úplně vyloučily3×3×3: přímýCSP0,66s,
DLX2 14,31s. Původní DLX2 používá samostatné položky všech fyzických
stěn a šest barevných selektorů, tedy odlišný model i postup větvení.
Neopakovaly se dokončené běhy.

Čtyři histogramové řádky2×2×4 jsou nesprávné, viz
[F138 a krátký certifikát](F138_BRICK_HISTOGRAMS.md). Celkové počty244/48
se nezmění. **Všechny ostatní vytištěné histogramy souhlasí.**

U2×2×2 s šesti vnějšími barvami byly obě konstrukce přejmenovány na
týž pevný prototyp. Používají stejných osm kostek, nezahrnují prototyp
a propojuje je přesně24 dovolených izomorfismů. Obecný případ libovolného
prototypu plyne z přejmenování barev. U malých kvádrů sedí také3 řešení,
2 třídy a stabilizátory8/16; jediné1×2×3 má stabilizátor8.

Závěrečná existence3×3×3 bez rohu a bez středu s kostkou nad ním je
doložená konkrétními **26- a25-kostkovými svědky**. Hledání skončilo
po prvním řešení (`t1`,0,93/2,98s). Každá stěna, vnější barva a různost
typů přímo prověřeny. Nejsou to úplné výčty obou děravých těles a žádný
jejich celkový počet se netvrdí; kniha požaduje jen existenci.

## Errata a historie

Šest vrstev errat hashem odpovídá oficiálnímu stažení3.11.2026v05:37UTC.
Oprava histogramů F138 nenalezena. **E074** z7.4.2026 opravuje rok citace
1893→1892; **E075** z19.6.2023 mění8-cube→eight-cube. Obě změny v našem
PDF i draftu ještě chybí. Jde o známé opravy, oddělené od F138.

[Vydavatel MacMahonova článku](https://doi.org/10.1112/plms/s1-24.1.145)
uvádí rok svazku1892. Metadata nejsou důkazem přečtení článku, k jehož
tělu se přístup nepodařil; historický rejstřík podporuje knižní rozsah
145–155, i když současná metadata končí156. Z toho další chybu nevyvozujeme.
[NDL](https://ndlsearch.ndl.go.jp/books/R100000002-I000006498029) potvrzuje
Kowalewského knihu1930 a [CiNii](https://ci.nii.ac.jp/ncid/BB17224590)
Winterovu disertaci1933. Jejich uvedené konstrukční stránky zatím nemáme.
Název produktu Mayblox podporuje již uložený Gardner1978 str.26 i popis
fyzických exemplářů v Garcíově vlastní sbírce v jeho disertaci.

Otevřené zůstávají tělo patentu UK8275/1892, původní článek a přesná
atribuce objevu, Kowalewski str.14–19 a Winter str.67–87. Tyto čtyři
historické mezery drží celou úlohu jako partial. Veškerá matematika,
katalog i závěreční svědci jsou hotoví; žádný náročný počet tu nakonec
nebylo nutné vynechat. Fyzický výtisk, úplné nejnovější digitální vydání
a prvenství nálezu nejsou ověřeny.

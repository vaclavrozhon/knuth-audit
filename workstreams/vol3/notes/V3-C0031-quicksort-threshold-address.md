# V3-C0031 — implicitní horní mez prahu v MIX Quicksortu

Candidate, low. Svazek 3, Program Q, tištěná 117 / file128, řádky
25 `DEC4 M,5` a 27 `DEC1 M,2`. Protipříklad k doslovnému rozsahu
N>M je přesný, ale záměr malé hodnoty M může být implicitní konvencí.

Na binárním MIX mají dva bajty rozsah velikostí 0..4095. Svazek 1,
§1.3.1 na 127/file142, výslovně říká, že pokud součet adresy instrukce
a indexového registru není reprezentovatelný ve dvou bajtech, efektivní
adresa je nedefinovaná. Toto platí i u aritmetické instrukce DEC;
není nutné, aby šlo o adresu čtenou z paměti. Originální sazba obou
programových stran a této definice byla zobrazena.

Vezměme N=3000,M=2000, INPUT=0 a klíče

    (3000,1,2,...,2999).

Na 0 a 3001 jsou předepsané nejmenší/největší MIX hodnoty, kód lze
umístit od 3100 a STACK=3200. Všechny vstupní adresy, samotné indexy,
konstanty a kód se vejdou do 4000 paměťových buněk. Zásobník během
první fáze ještě nebyl použit.

Pivot je 3000. Levý scan dospěje k horní zarážce i=3001, pravý se
zastaví po jednom kroku na j=3000. Po pivotové výměně nastaví 24
I4=r=3000, ale 25 vyhodnocuje efektivní adresu M+I5=2000+3000=5000.
Ta je na binárním MIX nedefinovaná; nestačí, že plánovaný konečný
rozdíl r−j−M=−2000 by byl reprezentovatelný.

Dostatečné omezení programu je M+N≤4095 (obecně b²−1 podle báze
bajtu). Druhá možnost: rozdělit oba složené odpočty na odečtení j/l
a M ve dvou instrukcích. Všechny mezivýsledky pak jsou a,b,a−M,b−M
v rozsahu ±N a cena se zvýší o 2A, z 24A na 26A v (16).

Doporučená praktická hodnota M=9 není postižena. Kniha na 115 píše,
že M má být zvoleno podle následujícího textu. Proto ponechávám
nejasnost, zda N>M na 117 zamýšlí celý doslovný parametrický rozsah,
nebo již jen tyto malé praktické prahy. Kandidát se netýká abstraktního
algoritmu Q ani správnosti ceny v definovaném strojovém rozsahu.

Všech pět vrstev je zachyceno v
`sources/quicksort-threshold-address-errata-review.json`.
Žádný výpočtový běh, fyzický výtisk ani prvenství neověřeny.

# DLX154 — původní zdroje a rozsah kontroly

3. listopadu 2026. Matematická klasifikace je již hotová v
[PARTRIDGE_NOTES.md](PARTRIDGE_NOTES.md). Původní test do milionu
a soubor `results/partridge/pell.json` zůstaly beze změny; neopakovaly se.
Celá úloha zůstává **partial** pouze kvůli drobnému redakčnímu kandidátovi C035.
Singletonův podíl i rok1996 potvrzují společně oba citované prameny.

## Matematika a původní znění

Zadání na str.144 a odpověď na str.460 byly znovu přímo přečteny ve
vykresleném PDF i autorově draftu, str.80 a164. Matematické formule
souhlasí. Odlišná současná adresa Friedmanovy stránky je známá oprava E078.

Pro úplnost důkazu není třeba velké hledání. Pro n≥0 je

```
P(n) = n(n+1)^2(n+2)/12.
P(n) je čtverec právě tehdy, když (n+1)^2−3b^2=1.
(a_k,b_k) začíná (1,0) a pokračuje (2a_k+3b_k,a_k+2b_k).
```

Obrácený krok `(a,b) -> (2a−3b,2b−a)` klesá až do `(1,0)`.
Tím je zajištěna úplnost, nikoli jen mnoho nalezených příkladů.
Pro sudý index je `a_(2m)−1=6b_m^2`; pro lichý index je
`a_(2m+1)−1=(a_m+3b_m)^2`. Knižní začátky obou posloupností
jsou správné. Integrální odmocnina je `a_k*b_k/2`; součin je sudý
z Pellovy rovnice modulo4. Případ n=0 je samostatně zahrnutý.

Součet ploch lze ověřit rozdílem sousedních n: jak původní součet,
tak uvedený polynom mají rozdíl `n(n+1)(2n+1)/6` a hodnotu0 v n=0.
Vzorce pro a a b plynou z konjugovaných mocnin `2±√3`.
Perioda řetězového zlomku √3 je `(1,2)`. Odkaz na úlohu4.5.3–42
je správný: ta vyjadřuje vlastnost nejlepších aproximací konvergentů.
Zobrazeno ve svazku2 na tištěné str.378, skutečná stranaDjVu390.
OCR oddělení stránek je o jednu posunuté; nejde o chybu knihy.

## Citované prameny

Nově získaná Wainwrightova kapitola **The Partridge Puzzles**, v
*Puzzlers’ Tribute*, má skutečně str.277–281. Celá byla přečtena
ze skenu, stranyPDF301–305. Na str.280–281 připisuje obrácené
násobnosti Colinu Singletonovi a Donu Knuthovi a uvádí Singletonovy
počáteční příklady a skládačku n=6. Přesný rok jeho dopisu tam není;
rok1996 však výslovně uvádí popisek čtvercové skládačky na druhém
citovaném prameni, Friedmanově stránce. Datování je tím doložené.
Kapitola pomůže také historické kontrole následující úlohy156.

[Friedmanův přehled z června2007](https://erich-friedman.github.io/mathmagic/0607.html)
obsahuje tentýž součet a ekvivalentní posloupnost `a_k−1`. Odkaz funguje
a vede ke správnému tématu. **E078** je již zveřejněná oprava URL
z11.7.2022 pro fascikl5, str.268. V místním PDF je zapracovaná,
v draftu2019 zůstává stará adresa. Není to nový nález.

Šest relevantních vrstev errat má stejné hashe jako při dnešním stažení.
Žádná oprava názvu ptáků ani další oprava matematiky154 v nich není.

## Redakční kandidát a příbuzný projekt

[C035](C035_PARTRIDGE_CAROL.md) se týká názvu druhého daru v koledě.
Jeho závažnost je nízká, výpočty se nemění. Přesná zamýšlená varianta
koledy v knize určena není; kandidáta nepřidáváme k potvrzeným nálezům.

[Munklarův veřejný solver](https://github.com/Munklar/Partridge-Puzzle)
zveřejňuje řešení běžné i obrácené varianty a uvádí úplný počet18656
pro n=8. Jde o samostatný příklad staršího výpočetního zkoumání téhož
hlavolamu. Jeho kód jsme nespouštěli a data jsme v tomto bloku neověřovali;
není to další nezávislý výčet našeho auditu ani soustavný audit celé TAOCP.

Žádný nový brute force. Následuje155: starý počet60568 je hotový,
zbývají mimo jiné původní obrázky a zdroj Reidovy historické poznámky.

Závěrečná kontrola popisku před commitem uzavřela původně zaznamenanou
mezeru v datování. `source-followup-checked.json` a aktuální
`source-observations.json` v tomto bodě nahrazují předběžný checkpoint.

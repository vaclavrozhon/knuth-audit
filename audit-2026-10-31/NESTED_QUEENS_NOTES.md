# Vnořené neútočící dámy, úloha 162

Kontrola 1. 11. 2026. Zadání str. 145, odpověď str. 462; nezávisle
autorův PostScript 5C str. 166. Známá oprava z 13. 10. 2023 mění
diagonální položky druhé dámy, přidává sharp preference a opravuje
počty paměťových operací. Všechna tato upřesnění jsou zapracována.

## Všech devět minim je správně

| Část | Vložené bloky | Minimum n | Úplné polohy v minimu |
|---|---|---:|---:|
| a | 2 Q4 | 15 | 224 |
| b | 3 Q4 | 17 | 32; všechny obsahují dokonce 4 Q4 |
| c | 4 Q4 | 17 | 32 |
| d | 5 Q4 | 22 | 256 |
| e | 2 Q5 | 16 | 144 |
| f | 3 Q5 | 19 | 64 |
| g | 4 Q5 | 20 | 288 |
| h | 2 Q6 | 22 | 896 |
| i | 3 Q6 | 25 | 3 392 |

Každé menší n od kt do minima bylo úplně vyloučeno dvěma programy.
Pro n<kt stačí disjunktnost. Ta nebyla předpokládána: úplný test
všech 2, 10 a 4 vzorů Q4,Q5,Q6 a všech překrývajících se posunů
ukázal, že dva různé bloky nemohou sdílet dámu. Každá přípustná
konfigurace tedy má bloky v disjunktních intervalech řádků i sloupců.

První výpočet používá původní Knuthův DLX3 a jeho
[sharp change file](https://www-cs-faculty.stanford.edu/~knuth/programs/dlx3-sharp.ch).
Druhý, `nested_queens.cpp`, vybírá geometrické bloky ve vzestupném
pořadí řádků, kontroluje sloupce a diagonály bitovými maskami a potom
doplňuje zbývající dámy. Nepoužívá přesné pokrytí. Všechny úplné
seznamy obou programů souhlasí včetně násobností. U d,i dal DLX3
jen prvního svědka; uvedené celkové počty pocházejí z úplného druhého
výpočtu. Část b vybírá tři ze čtyř bloků, tedy každý výsledek čtyřikrát.
U i mají některé polohy čtyři Q6; 3 584 výběrů dává 3 392 poloh.

Také úvodní příklad osmi Q5 obsahujících Q4 souhlasí. Ilustrace
v odpovědi nebyly přepsány a historické počty operací nereprodukujeme.

## F069: počty tříd v částech e,h

Při obvyklé ekvivalenci otočením a zrcadlením celé šachovnice vychází:

| Část | V knize | Správně tříd D4 | Rozklad na orbity |
|---|---:|---:|---|
| e | 4 | 19 | 17×8 + 2×4 = 144 |
| h | 28 | 116 | 108×8 + 8×4 = 896 |

Obě čísla jsou čitelná v PDF i PS. Ve veřejných erratech oprava
počtů není; oprava 2023 na stejné stránce se týká jiných údajů.

Je třeba rozlišovat fyzické polohy od možností přesného pokrytí:
dvojice různých vzorů Qk mohou zabírat přesně stejné řádky, sloupce
a diagonály. Po sloučení takových dvojic je v e pouze 36 možností,
ale i potom **pět**, nikoli čtyři třídy D4. V h je sloučených možností
224 a **30**, nikoli 28 tříd. Takže ani tato širší ekvivalence uvedené
počty nezachrání. Pět explicitních příkladů pro e zůstává různých,
i když se úplně zapomene rozmístění dam uvnitř obou bloků a zachovají
se jen jejich čtverce a zbývající jednotlivé dámy:

![Pět neekvivalentních příkladů](results/nested_queens/five-distinct-layouts.svg)

Souřadnice, úplné seznamy reprezentantů a histogramy jsou v
`results/nested_queens/classification.json` a `five-distinct-layouts.json`.
Kontrola každé polohy i osmi symetrií je v `verify_nested_queens.py`.

Část g vyžaduje opatrnější slovní upřesnění: vytištěných 18 skutečně
odpovídá počtu možností po sloučení identických množin položek.
Každá se rozvine do 16 poloh, celkem 288 a 42 tříd D4. Tento údaj
**nepočítáme jako další chybu**; má smysl jako počet sloučených
řešení Algorithm X. F069 se týká výslovných počtů tříd e,h.

## Vlastní oprava při čtení výstupu

DLX tiskne možnosti cyklicky posunuté podle větvené položky. První
pomocný parser proto nejdříve selhal; následující varianta párovala
množiny položek a nesprávně slučovala právě výše uvedené různé
vzory. Finální parser zachovává cyklické pořadí. Všechny uložené
výstupy byly znovu přečteny, ověřena uzavřenost vůči D4 a porovnány
s nezávislými geometrickými seznamy. Původní chybná mezidata nejsou
použita v závěrech.

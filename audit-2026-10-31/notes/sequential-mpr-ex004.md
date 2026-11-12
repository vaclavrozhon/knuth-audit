# D107 — celá MPR4: NanoBingo

6. listopadu 2026. Celé zadání12–13/file32–33 a odpověď371/file391
přímo zobrazeny; shoda také s autorovým Pre-Fascicle5A,
12–13/file18–19 a28/file34. Zkontrolováno všech16 čísel karet,
obě ukázkové posloupnosti, všechny části(a,b,c) a každý
vytištěný čitatel pravděpodobnosti.

## Pravidla, karty a zastavení

Vylosované pořadí všech šesti různých čísel je rovnoměrné
na6!=720 permutacích. Vyhrávají právě přítomní hráči,
kteří jako první současně dokončí některý vodorovný řádek.
Nezapočítává se dokončení pozdějších řádků po zastavení hry;
sdílená výhra je jediným výsledkem s celou množinou vítězů.

Všechny řádky originálu jsou přesně

| Karta | Horní řádek | Dolní řádek |
|---|---|---|
|A|1,2|3,5|
|B|2,3|4,6|
|C|3,4|1,5|
|D|1,4|2,6|

V každé kartě jsou čtyři různá čísla z předepsané množiny.
Nechť pos(x) je pořadí, ve kterém bylo x oznámeno. Čas dokončení
řádku{x,y} je max(pos(x),pos(y)); čas první výhry jedné karty
je minimum těchto dvou maxim. Pro zvolenou množinu hráčů
je čas konce minimum jejich časů a vítězi jsou právě všichni
s tímto minimálním časem. To přímo odpovídá pravidlu v zadání
a zahrnuje všechny současné výhry.

Pro prefix6,2,5,1 nemá po prvních třech číslech řádek ani A,
ani B. Čtvrté číslo1 dokončí A horní řádek1,2; B stále
postrádá3 nebo4. Proto A vyhraje bez ohledu na pořadí zbytku.
Pro prefix1,3,2 opět není po prvních dvou číslech hotový
řádek; třetí číslo2 současně dokončí A:1,2 a B:2,3.
Výsledkem je remíza A,B. Oba tištěné příklady jsou správné.

## Symetrie a dvě úplné metody počítání

Permutace čísel σ=(1234)(56) posílá řádky postupně takto:

```
A:{12,35} → {23,46}=B,
B:{23,46} → {34,15}=C,
C:{34,15} → {14,26}=D,
D:{14,26} → {12,35}=A.
```

Uvnitř řádku ani mezi řádky pořadí nehraje roli. Aplikace σ
na každé oznamované číslo je bijekce720 stejně pravděpodobných
pořadí; zachová časy a pootočí označení hráčů. Proto jsou
všechny cyklicky přejmenované výsledky stejně pravděpodobné.
Žádná další zrcadlová symetrie není automaticky předpokládána.

`verify_mpr004_bingo.py` nejprve projde každou z720 permutací
a pro všech6 dvojic,4 trojice a jednu čtveřici hráčů použije
přesný vzorec pro časy výše. Každá permutace určí právě jeden
neprázdný výsledek; součet všech čitatelů pro každou sestavu
musí být a také je720.

Druhá metoda počítá stejné výsledky nezávisle pomocí množiny
T čísel oznámených před první výhrou a dalšího čísla c∉T.
Ponechá se právě případ, kdy žádný aktivní řádek neleží v T,
ale alespoň jeden již leží v T∪{c}. Vítězi jsou všichni
aktivní hráči s řádkem v T∪{c}. Takový pár(T,c) odpovídá
přesně

```
|T|! · (5−|T|)!
```

úplným pořadím: libovolné pořadí předchozích čísel T,
potom c, potom libovolné pořadí zbývajících čísel. Žádné
dřívější pořadí v T nemůže vyhrát, protože dokončený řádek
by pak byl i v celé T. Naopak každá úplná permutace má
jediný první vítězný prefix a tedy jediný pár(T,c).
Součet je proto přesnou disjunktní klasifikací720 pořadí.
Projde jen64 možných T a nejvýše6 dalších čísel, bez
pravděpodobnostních aproximací.

Obě metody souhlasí pro každý jednotlivý výsledek všech11
herních sestav. Nejde jen o shodu celkových součtů.
Celá dvojí kontrola trvala0.044753s s nice15. Všechny smyčky
jsou uvedené konečné prostory, počty jsou celá čísla nejvýše720;
žádný starý test ani delší běh nebyl opakován.

## Část(a): všech šest dvojic

Každý údaj v následující tabulce je čitatel se společným
jmenovatelem720. Sloupce odpovídají prvnímu a druhému hráči
v názvu dvojice.

| Hráči | První sám | Druhý sám | Oba současně |
|---|---:|---:|---:|
|A,B|336|312|72|
|A,C|288|288|144|
|A,D|312|336|72|
|B,C|336|312|72|
|B,D|288|288|144|
|C,D|336|312|72|

Tím jsou doloženy i tři čitatele uvedené přímo v zadání.
Cyklicky orientované dvojice A→B→C→D→A mají výhru336/720,
opačnou312/720 a remízu72/720. Obě protilehlé dvojice mají
obě ostré výhry288/720 a remízu144/720, přesně jako odpověď.

## Část(b): všechny čtyři trojice

Stačí reprezentant A,B,C, protože čtyři trojice tvoří jedinou
orbitu pod σ. Úplná distribuce tohoto reprezentanta je

| Vítězové |A|B|C|AB|AC|BC|ABC|
|---|---:|---:|---:|---:|---:|---:|---:|
| Čitatel /720 |168|216|168|48|72|36|12|

Tedy přesně všech sedm čísel odpovědi. Pro úplnost uvádíme
i ostatní sestavy, aby se použitá symetrie dala přímo zkontrolovat:

| Hráči | Samostatní vítězové | Dvojité výhry | Trojitá výhra |
|---|---|---|---|
|A,B,D|A:216, B:168, D:168|AB:36, AD:48, BD:72|ABD:12|
|A,C,D|A:168, C:168, D:216|AC:72, AD:36, CD:48|ACD:12|
|B,C,D|B:168, C:216, D:168|BC:48, BD:72, CD:36|BCD:12|

Všechny čitatele se opět dělí720. Například nestejné48 a36
u sousedních dvojitých výher ukazují, proč by neověřená
zrcadlová symetrie nestačila.

## Část(c): všech patnáct neprázdných výsledků

Všichni čtyři hráči jsou přítomni. V odpovědi jsou vyjmenovány
reprezentanty pěti cyklických tříd A,AB,AC,ABC,ABCD;
nejde o tvrzení, že je to seznam všech jednotlivých výsledků.
Každá třída a všechny její členy mají tyto čitatele /720:

| Typ výsledku | Všechny množiny vítězů | Čitatel pro každou |
|---|---|---:|
|Jediný hráč|A,B,C,D|120|
|Sousední dvojice|AB,BC,CD,AD|24|
|Protilehlá dvojice|AC,BD|48|
|Tři hráči|ABC,ABD,ACD,BCD|12|
|Čtyři hráči|ABCD|0|

Normalizace je4·120+4·24+2·48+4·12+0=720.
Žádný neprázdný podmnožinový výsledek není vynechán:
4+4+2+4+1=15.

Poslední nulu lze navíc dokázat přímo z karet. Při prvním
vítězném tahu musí být právě oznamované číslo součástí
dokončeného řádku každého vítěze, jinak by jeho řádek byl
hotový už předtím. Čísla1,2,3,4 se vyskytují každé jen na
třech kartách;5 a6 každé jen na dvou. Žádné číslo tedy nemůže
současně dokončit řádek všech čtyř karet, takže čtyřnásobná
výhra je nemožná. Důkaz nezávisí na výčtu.

## Errata a uzavřený rozsah

Šest místních vrstev errat a všechny tři dostupné TeXy byly
porovnány. Pro MPR4 není nalezena oprava; sousední změna
zadání5(b) na13 z8.2.2021 ani již evidované doplnění odpovědi2
nejsou změnami této úlohy. MPR4 nemá samostatný bibliografický
odkaz, který by zde vyžadoval vynechání.

D107 uzavírá všechny části4(a,b,c), karty, příklady a celou
odpověď. Tím je uzavřen celý matematický obsah původní
strany12/file32: hlavní text D103 a celé úlohy1–4 v D104–D107.
File33 zůstává partial, protože je zde zatím uzavřena pouze
dokončená MPR4; následují úlohy5–13. File391 zůstává partial
pro odpovědi5 a následující. Žádný nový nález nebo kandidát.

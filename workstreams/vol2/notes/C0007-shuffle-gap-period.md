# V2-C0007: mez periody mezer v poznámce k §3.2.2-15

**Stav: confirmed, 1. listopadu 2026.** Doložený první dotisk, str. 554,
poznámka za odpovědí 15. Hlavní tvrzení a důkaz úlohy jsou správné;
chyba je v dodatečné mezi pro tabulku se dvěma položkami.

## Tvrzení a protipříklad

Algoritmus M používá tabulku délky k. Z pomocné posloupnosti Y_n modulo m
volí index j_n=floor(k Y_n/m). Označme q_n počet kroků od předchozího
výskytu stejného indexu, tedy nejmenší r>0 s j_(n-r)=j_n.
Záporné indexy zde určujeme periodickým prodloužením. Symbol lambda_2
v úloze označuje nejmenší periodu posloupnosti q, nikoli posloupnosti Y.

[Původní poznámka](../images/vol2-p554.png) tvrdí, že při maximální periodě
lineárního kongruenčního Y modulo 2^e je lambda_2 nejvýše 2^(e-2),
pokud je k mocninou dvou. Položme m=16, e=4, k=2 a

```
Y_0=0, Y_(n+1)=(5 Y_n+1) mod 16.
n:   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
Y:   0  1  6 15 12 13  2 11  8  9 14  7  4  5 10  3
j:   0  0  0  1  1  1  0  1  1  1  1  0  0  0  1  0
q:   1  1  1  5  1  1  4  2  1  1  1  5  1  1  4  2
```

Y prochází všemi šestnácti zbytky. Posloupnost q má nejmenší periodu 8:
dvě uvedené poloviny jsou stejné, ale q_2=1 a q_6=4 vylučují periodu 4.
Perioda dělí 8,
takže tím jsou vyloučeni také její menší dělitelé 1 a 2.
Tedy **lambda_2=8>4=2^(e-2)**.

Příklad splňuje i předpoklady [zadání 15](../images/vol2-p038.png).
Pro vstupní X_n=n mod 16 jsou prvky periody různé a lambda_1=16.
Všechny q_n jsou nejvýše 5, tedy přísně menší než lambda_1/2=8.
Není to případ vyřazený podmínkou úlohy. Výstup Algoritmu M má podle
správného hlavního tvrzení periodu lcm(16,8)=16; přímý běh to potvrzuje.

## Platná oprava

Pro e>=2 a k mocninu dvou alespoň 4 je uvedená mez správná.
Pro k=2 ji lze nahradit 2^(e-1). Když k=1, je q_n=1.

Pro důkaz pišme Y_(n+1)=aY_n+c modulo m=2^e. Maximální perioda znamená
a=1 modulo 4 a c liché. Pro h=2^(e-2) platí a^h=1 modulo m
a součet S_h=1+a+...+a^(h-1) má přesně e-2 faktorů 2.
Proto Y_(n+h)-Y_n=c S_h modulo m je pevné liché násobení m/4.
Pokud 4 dělí k, posune se každý index j o stejnou hodnotu k/4
nebo 3k/4 modulo k. Tento posun je permutací indexů, takže všechny
rovnosti j_n=j_(n-r) zachovává. Tudíž q_(n+h)=q_n.

Pro k=2 použijeme analogicky poloviční periodu h=m/2: Y se posune
o m/2 a oba indexy se vymění. To dává správnou mez m/2, ostrou
v uvedeném příkladu.

## Hlavní důkaz úlohy 15

Po naplnění tabulky je výstup Z_n=X_(n+k-q_n). Označme jeho nejmenší
periodu L. Zřejmou periodou je lcm(lambda_1,lambda_2). Různost prvků X
zaručuje q_(n+L)-q_n=L modulo lambda_1. Rozdíl je v otevřeném intervalu
(-lambda_1/2,lambda_1/2), a tudíž je pro všechna dostatečně velká n
touž konstantou c. Opakováním posunu L a omezeností q dostaneme c=0.
Pak lambda_1 i lambda_2 dělí L, což dokazuje tvrzení.

## Doklady a kontrola errat

[Program](../verify_shuffling_boundaries.py) získává Y přímou rekurencí
a nezávisle z celého geometrického součtu (5^n-1)/4. Mezery počítá
jednou mapou posledních výskytů a podruhé hledáním dozadu v cyklu.
Opravené meze navíc kontroluje v 23 664 případech všech plnoperiodických
generátorů se seedem 0 modulo 4,...,128 a mocninových velikostí k až 2m.
Jiné seedy jen posunou celou periodu. Výsledek:
[shuffling-boundaries.json](../results/shuffling-boundaries.json).

Prohledány all2-prepre, all2-pre, all2, err2 i err2.textxt z 1. 11. 2026
podle strany, čísla úlohy a obsahu tvrzení. Oprava str. 554 z 28. 4. 2017
se týká výhradně odpovědi 11 (index n+p lambda), nikoli této poznámky.
Oprava meze nebyla nalezena. Novější fyzický dotisk ani prvenství neověřeny.
[ASCII draft](../reports/C0007-shuffle-gap-period-draft.txt) nebyl odeslán.

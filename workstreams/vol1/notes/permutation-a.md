# §1.3.3: cykly, součin a Program A

Technická kontrola s.164–172, 1. listopadu2026, třetí vydání/první dotisk.
Originální stránky byly zobrazeny; OCR sloužilo jen k navigaci.
Důkaz níže platí pro neprázdné vstupní cykly s různými jmény uvnitř
každého cyklu a při dostatečné kapacitě odpovědi. Přesná kapacitní
chyba C0029 a nevyjasněná prázdná identita C0028 jsou odděleně
v `permutation-a-capacity.md`. Nejsou zakryty úspěšnými malými testy.

## Základní reprezentace a příklady

Permutace je bijekce konečné množiny jmen na sebe. Zápis `(x_1 ... x_k)`
posílá x_i na x_(i+1), poslední na první a ostatní jména nechává pevná.
Dvouřádkový zápis obsahuje vstupní jména nahoře a jejich obrazy dole.
Změna pořadí sloupců proto nic nemění; šest různých horních jmen dává
6!=720 zápisů, po odečtení dvou uvedených zbývá718.

Opakované použití bijekce z x se musí vrátit přímo do x: první opakování
v jiném bodě by mělo dva různé předchůdce. Tím vznikne cyklus. Dva
cykly se buď shodují, nebo jsou disjunktní, protože ze společného bodu
mají tentýž následný postup. Opakováním na zbývajících jménech vznikne
celý rozklad. Jeden pomocný registr stačí k přemístění hodnot podél
každého cyklu; uvedená posloupnost přiřazení na s.165 drží počáteční
hodnotu v t, dokud nepřijde na poslední místo.

Součin používá knižní konvenci zleva doprava. Složení tabulek
`cdfbea` a `bdcafe` na jménech `abcdef` dává `caedfb`, cyklus `(acefb)`;
opačný součin je `dbfcae`, cyklus `(adcfe)`. Rozklad příkladu(6) je
`(adg)(ceb)(f)`, po potlačení pevného bodu f tedy `(adg)(ceb)`.

## Proč A opravdu násobí permutace

Představme si každou vstupní permutaci jako jednu vrstvu: z každého
jména vede hrana k jeho obrazu po této permutaci. Cesta napříč všemi
vrstvami pak představuje aplikaci celého součinu. V každé vrstvě
jsou tyto cesty disjunktní, protože každý částečný součin je bijekce.
Výskyt jména x ve vstupním cyklu představuje konkrétní hranu x na
následující jméno. I singleton představuje jednu takovou hranu x na x.

A1 označí levé závorky a pravé nahradí označenou kopií prvního jména.
Tím je následník posledního jména dostupný stejně jako ostatní
následníci. Prázdná pole nejsou jména a strojový program je přeskakuje.
A3–A4 sledují jednu cestu: po použití výskytu x přejdou na jeho
následníka a pokračují v dalších vstupních cyklech. Kopie na konci
cyklu je pouze následník, nikoli další použitá hrana. Pokud byl
následník uvnitř cyklu, žádný další výskyt téhož jména v tomto cyklu
není; pokud šlo o návrat na první jméno, kurzor už stojí na koncové
kopii. Proto algoritmus týž vstupní cyklus na jedné cestě nepoužije
dvakrát. Tag označuje právě použité hrany těchto cest.

A2 může začít prvním dosud neoznačeným výskytem x. Jeho cesta musí
mít počáteční jméno x: kdyby se jiné počáteční jméno dříve změnilo
na x, musela by mít tato cesta dřívější neoznačenou hranu, což
odporuje volbě první neoznačené pozice. Kdyby ona dřívější hrana
byla označena, celá cesta už byla zpracována a současná hrana by
byla označena také. Počáteční prefix cesty tedy nechával x beze změny.
Stejný argument zaručuje, že x ještě nebylo ve výsledném cyklu.

Po dosažení konce vzorce máme přesně obraz x pod celým součinem.
A5 spustí další takovou cestu z tohoto obrazu. Bijektivita zaručuje,
že se tato posloupnost poprvé uzavře v START. Označily se právě
hrany cest tvořících jeden výsledný cyklus. Následující A2 tedy začne
nový disjunktní cyklus. Každé jméno vyskytující se ve vstupu má na
své cestě alespoň jeden vstupní výskyt: před prvním výskytem ho
žádný faktor nemění. Když už žádný neoznačený výskyt nezbývá, jsou
zpracována všechna jména. To dokazuje úplnost a konečnost.

V MIXu záporné znaménko označuje tag, porovnávání jmen používá pouze
pět bajtů bez znaménka. Vstupní jméno je nenulové slovo odlišné od
obou rezervovaných závorek. Proto test třetího posledního slova
proti levé závorce rozpozná právě singleton `(x)`. Vrácení ukazatele
o tři jej odstraní. Zbylé cykly přesně reprezentují výslednou bijekci.
Při prázdné odpovědi se zvlášť vytiskne `()`.

## Časový rozbor v obecném tvaru

Nechť X je počet karet, Y počet neprázdných vstupních polí bez posledního
ukončovacího znaku, M počet vstupních cyklů a N počet různých jmen.
U je počet výsledných cyklů včetně singletonů, V počet singletonů.
Každá karta obsahuje16 polí, takže zpracovávaný vstup má16X−1 slov.
Písmena A,...,S jsou četnosti instrukcí vyznačené v knize.
Pro začátek předpokládejme prázdná pole jen na pravém konci.

Počítání vstupních polí, hran a výsledných cyklů dává:

```
A = C = 16X−1−M       B = D = M
E = U+1               F = U+G       H = R = U
J = Y−2M              K = L−U
P = N                 Q = N−U       S = V.
```

Poslední nevyčíslené četnosti G a L souvisejí úplnými průchody vstupem.
Průchod začíná řádkem41 nebo74 a končí řádkem80 nebo posledním pádem
z řádku46. Takových průchodů je N+1; každý zvýší I3 přesně16X−1krát.
Zvýšení obstarávají řádky44,68,77 s četnostmi G,J,L. Tedy

```
G+J+L = (16X−1)(N+1).
```

Z cen instrukcí se získá přesně7u za řádky23–25 a39–40 a dále

```
5A+6B+7C+2D+E+3F+4G+8H+6J+3K+4L+3P+4Q+6R+2S
```

jednotek u. Po dosazení je výsledek rovnice(18)

```
112NX+304X−2M−Y+11U+2V−11.
```

I/O část je zde vyloučena přesně jako v textu. Členy3F+4G a3K+4L
dávají společný koeficient7 u G a L; chybné původní vysvětlení je
známé erratum z31.5.2004. Oprava odkazů na řádky v tabulce toku
z30.11.2009 nemění samotné rovnice. Tyto rovnice jsme ověřili jako
obecné zachování počtu příchodů a odchodů, nikoli jen na příkladu.

Pro obecné prázdné výplně označme a počet prázdných polí, jejichž
předchozí neprázdný symbol je levá závorka, a b počet prázdných polí,
jejichž předchozí neprázdný symbol je jméno. Pak A a C klesnou o a,
řádky30–32 mají M+a průchodů. Řádky68–70 mají J+b průchodů a řádek71
se vykoná bkrát. Rovnice úplných průchodů se změní na
`G+J+b+L=(16X−1)(N+1)`. Celkem proti vzorci(18) přibude4a+5b
za smyčky, ale ubude12a+7b za přeskočené běžné kroky. Oprava je
proto **−8a−2b**, ve shodě s erratem odpovědi6 z24.10.2005.
Úvodní mezery a mezery mezi cykly nepřidávají žádnou další korekci.
Změna počtu karet se samozřejmě musí započítat přes X.

## Reprodukce a přesný rozsah

`mixal_permutation_a.py` obsahuje přepis všech tištěných instrukcí,
nikoli novou implementaci algoritmu. `check_permutation_a.py` nezávisle
skládá mapy vstupních cyklů, porovnává každou hotovou cestu, ověřuje
právě jedno označení každého vstupního výskytu jména a parsuje celou
odpověď zpět na bijekci. Kontroluje také kopie vstupních karet,
potlačení singletonů a všechny výše uvedené frekvenční identity.

Prošlo11862 obsahových kontrol ve352 MIX bězích. Součástí jsou všechny
dvojice neprázdných cyklů na třech jménech,37 radixů na knižním
příkladu, všechny jednotlivé polohy trojice prázdných polí ve zvoleném
vzorci,60 různých delších vstupů, netriviální pětiznaková jména,
75karet na horní vstupní mezi a asynchronní I/O.763400 samostatných
kontrol konečného limitu instrukcí není zahrnuto do obsahového počtu.
Knižní příklad dává X=2,Y=29,M=5,N=7,U=3,V=1 a2161u. Výsledky jsou
v `results/permutation-a.json`; úspěšnou sadu není třeba opakovat.

Program používá standardní výchozí nulové neobsazené buňky pro40
prázdných tiskových sloupců za kopií vstupní karty; nezavádíme tvrzení
o libovolném počátečním odpadu v paměti. Odpověď svou výplň inicializuje.
Velký platný případ, který přesáhne tištěnou alokaci, má oddělenou
reprodukci a opravu v C0029. Nejednoznačný vstup `()` zůstává C0028.

## Errata a hranice tohoto bloku

Všechny4 vrstvy byly prohledány podle stránek i tématu. Známé opravy:
A3 „See“ na „Set“19.7.1997; popis symbolu v A1 a řádku30 30.3.1998;
první řádek tabulky1 27.5.1998; upozornění na nevalidovaný vstup24.10.2005;
rovnice/tok výše; typografie a Homo sapiens. Obrázek20 má správné
větvení A1–A6. Tabulka1 po opravě prvního řádku souhlasí s průběhem.

Průměry U=H_N,V=1 budou uzavřeny s následujícím pravděpodobnostním
textem celé sekce. Odkaz na obecné použití toku v2.3.4.1 se uzavírá
s touto cílovou sekcí. Tento záznam necertifikuje Program B/I/J.

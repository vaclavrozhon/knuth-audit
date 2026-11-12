# Odpověď §2.3.4.1-12: opětovné vybrání již připojeného vrcholu

**Stav: confirmed na základě originálu a přesného protipříkladu;
čeká na nezávislou kořenovou revizi.** Bez globálního ID. Tento stav
neznamená prvenství ani kontrolu fyzického tištěného exempláře.

Místo: TAOCP 1, 3. vydání, 1. dotisk (1997), tištěná s. 580,
první odstavec odpovědi §2.3.4.1-12; souborová strana 595.
Originál byl prohlédnut v `../images/vol1-file595-p580.png`.
Jde o chybu první implementační varianty, která používá nekonečno
jako značku vybraného vrcholu. Abstraktní algoritmus úlohy 11
a navržená alternativa se seznamem dosud nevybraných jsou správné.

## Přesný algoritmus a konkrétní chyba

`c(i,j)` je cena hrany mezi terminály `T_i,T_j`; ceny jsou zadány
pro `i<j` a rozšiřují se symetricky. Terminál `T_n` je zvolen na
začátku. `a(i)` je nejlevnější cena spojení `T_i` se zvolenou
množinou a `b(i)` je zvolený soused, který této ceny dosahuje.
Následující pseudokód věrně přepisuje všechny operace prvního
odstavce, včetně obou tištěných mezí a pořadí aktualizací:

```
for 1 <= i < n:
    a(i) <- c(i,n)
    b(i) <- n

repeat n-1 times:
    choose i with a(i) = min_(1 <= j < n) a(j)
    connect T_i to T_(b(i))
    for 1 <= j < n:
        if c(i,j) < a(j):
            a(j) <- c(i,j)
            b(j) <- i
    a(i) <- infinity
```

Rozhodující doslovná mez v originálu je
`for 1 <= j < n if c(i,j) < a(j) set` a následuje přiřazení
obou tabulek; omezení na nevybrané `j` zde není. Značka
`a(j)=infinity` uložená při předchozím výběru tak při dalším kroku
zaručí, že každá konečná cena `c(i,j)` vyvolá přepsání. Vrchol se
znovu stane kandidátem na minimum.

Diagonální ceny `c(i,i)` text nedefinuje. Aby na této samostatné
notační otázce protipříklad nezávisel, stačí porovnání pro `j=i`
ignorovat, ekvivalentně položit `c(i,i)=infinity`. Ani toto
benevolentní doplnění chybu neodstraní. Přiřazení na diagonále
by ostatně bylo hned přepsáno závěrečným `a(i)=infinity`.

## Čtyři terminály, kladné různé ceny

Položme `n=4` a

```
c(1,4)=1,   c(1,2)=2,   c(2,4)=3,
c(3,4)=10,  c(2,3)=20,  c(1,3)=30.
```

Všechny ceny hran jsou kladné, konečné a navzájem různé. Nejsou
zde žádné volby při rovnosti minima.

| Okamžik | `(a(1),a(2),a(3))` | `(b(1),b(2),b(3))` | Právě připojená hrana |
|---|---|---|---|
| Inicializace | `(1,3,10)` | `(4,4,4)` | — |
| Po 1. iteraci | `(infinity,2,10)` | `(4,1,4)` | `T1--T4` |
| Po 2. iteraci | `(2,infinity,10)` | `(2,1,4)` | `T2--T1` |
| Začátek 3. iterace | minimum je znovu `a(1)=2` | `b(1)=2` | `T1--T2` znovu |

Algoritmus provede předepsané tři iterace a skončí. Poslední
hrana pouze opakuje druhé spojení; terminál `T3` je izolovaný.
Výsledek tedy není ani spojovací strom, natož strom nejlevnější.
Platná minimální kostra je například `T1--T4, T2--T1, T3--T4`,
s cenou `1+2+10=13`.

Jde o celou rodinu protipříkladů: libovolné
`0<x<y<z<w<r,s`, přiřazené jako
`c14=x,c12=y,c24=z,c34=w,c23=r,c13=s`, vedou k témuž výběru
`1,2,1`. Pro `n<=3` se tato konkrétní vada ještě nemůže projevit
opětovným výběrem: po první iteraci má jediný vybraný index
hodnotu nekonečno; po druhé iteraci by mohl být obnoven, ale třetí
iterace se pro `n<=3` již nekoná. Protipříklad je tedy v tomto
smyslu nejmenší v počtu terminálů.

## Oprava a obecný důkaz

Vnitřní aktualizaci omezme na dosud nevybrané vrcholy různé od
právě zvoleného `i`. Při zachování místa závěrečného přiřazení
z knihy to lze vyjádřit podmínkou

```
for 1 <= j < n with j != i and a(j) < infinity:
    if c(i,j) < a(j): ...
```

Předpokládáme konečné vstupní ceny. Na začátku každé iterace
platí tento invariant: právě již vybrané indexy `<n` mají
`a(j)=infinity`; pro nevybrané indexy je

```
a(j)=min_(v in S) c(j,v),  b(j) in S,  c(j,b(j))=a(j),
```

kde `S` je dosud vybraná množina, původně `{n}`. Minimum vybírá
nejlevnější hranu mezi `S` a jejím doplňkem. Po přidání `i`
je nové minimum pro každý zbývající vrchol přesně
`min(a(j),c(i,j))`; vybrané značky se nemění. To dokazuje
invariant indukcí a zaručuje právě jedno nové připojení v každé
iteraci.

Minimalita plyne z výměny hrany přes řez: pokud dosavadní vybrané
hrany leží v nějaké minimální kostře a nová nejlevnější hrana
`e` v ní není, přidání `e` vytvoří cyklus. Cesta v původní kostře
mezi konci `e` obsahuje jinou hranu `f` přes stejný řez
`S,V\S`. Proto `cost(e)<=cost(f)`. Nahrazením `f` hranou `e`
získáme kostru nejvýše stejné ceny obsahující rozšířený výběr;
žádná dříve vybraná hrana se neodstraní, protože obě její koncové
vrcholy leží v `S`. Po `n-1` krocích je tak získaná celá kostra
minimální. Dvě lineární prohledání v každém kroku zachovávají
celkový počet operací `O(n^2)`.

## Reprodukovatelná doplňková kontrola

`../check_prim_answer.py` doslovně modeluje první variantu a stejnou
variantu s uvedenou dodatečnou podmínkou. Nezávislý Kruskalův
algoritmus slouží jako kontrola ceny opravených výsledků.
`../results/prim-answer12.json` obsahuje přesný průběh obou
variant pro uvedené ceny a výsledky všech úplných grafů na
`n=1,2,3,4` s cenami hran z `{1,2,3}`. Opravená varianta souhlasí
ve všech `1+3+27+729=760` případech; původní varianta dává
nesouvislý výsledek ve 445 ze 729 případů při `n=4`. Tyto konečné
kontroly doplňují obecný invariant a přesný protipříklad výše.

## Kontrola všech errat

Dne 1. listopadu 2026 byly prohledány `all1-prepre`, `all1-pre`,
`all1` a `err1` podle s. 580 i podle Prim, minimální kostra,
nekonečno, zvolené vrcholy a tabulky `a(i),a(j),b(i)`.
Byly rovněž prohlédnuty následující originální stránky PDF:

| Vrstva | Originální stránka | Nejbližší relevantní položky |
|---|---:|---|
| all1-prepre | 43 | S. 579: citace k odpovědi 8, interpunkce u 11; s. 580: pouze „a free tree“ v odpovědi 13 (23. 10. 2006). |
| all1-pre | 17 | S. 578: aktualizace odkazu u odpovědi 6; s. 579: jednotkový tok v odpovědi 8 (18. 7. 2021); poté s. 587. |
| all1 | 15 | S. 579: citace Jarník1930 a Prim1957 v odpovědi 11 (17. 11. 2023); poté s. 586. |
| err1 | 13 | Tatáž citace u odpovědi 11, poté s. 586. |

Obrazy jsou `../images/{all1-prepre-page43,all1-pre-page17,
all1-page15,err1-page13}.png`. Historická změna terminologie
„path/walk“ na s. 580 se týká odpovědi §2.3.4.2-1, ne zdejší 12.
Žádná nalezená oprava tuto aktualizaci `a(j)` nemění. Aktuálnost
uložených řad errat byla kořenově ověřena novým stažením
1. listopadu 2026; tento nález je vůči těmto verzím.

## English ASCII draft

Volume 1, third edition, page 580, answer 2.3.4.1-12:
The update loop can overwrite a previously chosen vertex's
infinity marker. For n=4, take c14=1, c12=2, c24=3, c34=10,
c23=20, c13=30. Starting at vertex 4, the first two iterations
choose edges 14 and 21. The second update restores a(1)=2 and
b(1)=2, so the last iteration chooses edge 12 again, leaving
vertex 3 disconnected. Restrict the update loop to as-yet
unchosen j (and j != i); with the infinity convention, add
the condition a(j)<infinity. The linked-list alternative in
the next paragraph already avoids this problem.

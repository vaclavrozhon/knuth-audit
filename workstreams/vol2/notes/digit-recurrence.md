# §4.1-33: konečný systém rekurencí pro počet různých hodnot

Kontrola 2. listopadu 2026. Původní strany 213 a 610–611 byly vizuálně
přečteny. Pro konečnou množinu cifer `D` je tvrzení správné pro každý
kladný celočíselný základ `b`. Níže je úplný důkaz a účinně ukončitelný
postup; případ `b=1` je řešen zvlášť. Tištěný Fibonacciho příklad souhlasí.
Možné upřesnění rozsahu zadání a algoritmu je evidováno jako kandidát
**V2-C0081**, nikoli jako potvrzený protipříklad k této konečné větě.

## 1. Počítáme hodnoty, ne slova

Položme `K_0={0}` a `K_n=b K_(n-1)+D`. Množina `K_n` obsahuje hodnoty
všech slov přesně `n` cifer z `D`, včetně počátečních nul, jsou-li
povoleny. `k_n=|K_n|` počítá různé celočíselné hodnoty; různá slova se
mohou slít do stejné hodnoty. Je-li `D` prázdná, je `k_0=1`, ostatní
`k_n=0` a vytvořující funkce je 1. Jednoprvková `D` dává `k_n=1`
pro každé `n` a funkci `1/(1-z)`.

Nyní předpokládejme `D` konečnou neprázdnou a `b>=2`. Pro konečný
neprázdný celočíselný vzor `S` definujme `k_n(S)` jako počet posunů
`t`, pro které `t+S` leží celé v `K_n`. Tento počet se nemění posunem
samotného vzoru, takže můžeme každý vzor normalizovat odečtením jeho
minima. Pro jednoprvkový vzor je `k_n(S)=k_n`.

## 2. Přesná rekurence pomocí průniků

Rozdělme posuny `t` podle `t=bq+j`, kde `0<=j<b`. Pro každý prvek
`s` vzoru musí být zvolena cifra `d_s` s `d_s=s+j (mod b)`. Pro takové
přiřazení cifer `alpha=(d_s : s in S)` zaveďme neprázdný vzor

```
T_alpha = {(s+j-d_s)/b : s in S}.
```

Při tomto přiřazení je `t+S` obsažené v `K_n` právě tehdy, když
`q+T_alpha` leží v `K_(n-1)`. Možná přiřazení sjednocujeme. Průnik
podmínek pro několik přiřazení odpovídá sjednocení jejich vzorů:

```
(q+T_alpha subset K) a (q+T_beta subset K)
    <=> q+(T_alpha union T_beta) subset K.
```

Princip inkluze a exkluze proto dává přesnou celočíselnou lineární
kombinaci `k_n(S)=sum_T c_(S,T) k_(n-1)(T)`. V každém kroku je jen
konečně mnoho přiřazení a průniků. Při jejich výpočtu je třeba zachovat
**absolutní polohy prvků**: normalizovat lze až hotový sjednocený vzor,
ne jednotlivé vzory před jejich sjednocením.

Pro `Delta=max(D)-min(D)` má každý výsledný sjednocený vzor rozpětí
nejvýše `(span(S)+Delta)/b`, kde `span(S)=max(S)-min(S)`.
Zvolme celé `H=ceil(Delta/(b-1))`. Začneme-li vzorem `{0}`, všechny
normalizované výsledné vzory leží v `[0,H]` a obsahují 0, protože
`(H+Delta)/b<=H`. Je jich nejvýše `2^H`. Tím je konečnost rekurence
odůvodněna bez spoléhání na experiment s prvními hodnotami.

## 3. Výpočet vytvořující funkce

Seřaďme konečný seznam vzorů a označme `v_n` sloupcový vektor jejich
počtů. Předchozí část konstruuje celočíselnou matici `M` tak, že
`v_n=M v_(n-1)`. Počáteční vektor má hodnotu 1 u jednoprvkového vzoru
a 0 u ostatních. Pro formální proměnnou `z` tedy

```
V(z) = sum_{n>=0} v_n z^n = (I-z M)^(-1) v_0.
```

Matice `I` je jednotková matice. Inverze existuje jako formální mocninná
řada, neboť konstantní člen `I-zM` je `I`; přes adjungovanou matici
je každá složka racionální funkcí. Hledaná složka má tedy lineární
rekurenci s konstantními koeficienty. Alternativně ji přímo dává
charakteristický polynom `M` a Cayleyho–Hamiltonova identita.

To také doplňuje větu v odpovědi, že koeficienty lze zjistit z prvních
hodnot: samotné empirické odhadnutí rekurence by důkazem nebylo.
Zde jsou koeficienty určeny kombinatoricky; případné řešení z počátečních
vektorů musí být podepřeno známou konečnou dimenzí.

## 4. Vytištěný příklad D={−1,0,3}, b=3

V normalizovaném pořadí vzorů `{0}`, `{0,1}`, `{0,2}`, `{0,1,2}` vychází

```
M = [ 3 -1  0  0 ]
    [ 1  0  0  0 ]
    [ 0  1  1 -1 ]
    [ 0  0  0  0 ],       v_0 = (1,0,0,0)^T.
```

Poslední vzor nikdy nenastane: žádné `K_n` pro `n>=1` neobsahuje číslo
kongruentní s 1 modulo 3, takže nemůže obsahovat tři sousední celá
čísla. Proto je člen `-k_(n-1)({0,1,2})` ve třetí rovnici nulový
 a kniha jej správně vypouští. První čtyři vektory jsou

```
(1,0,0,0), (3,1,0,0), (8,3,1,0), (21,8,4,0).
```

Vytvořující funkce první složky je `1/(1-3z+z^2)`, tedy
`k_n=F_(2n+2)`, kde `F_0=0`, `F_1=1` a `F_(m+2)=F_(m+1)+F_m`.
Pro třetí složku dostaneme `z^2/((1-z)(1-3z+z^2))`, tedy
`k_n({0,2})=F_(2n-1)-1` pro `n>=1`. V `n=0` je hodnota 0;
stejný zápis platí při obvyklém prodloužení rekurence na `F_(-1)=1`.
Žádný numerický nesoulad ani nový nález v příkladu není.

## 5. Základ 1: od jisté chvíle lineární počet

Pro `b=1` je `K_n` množina součtů `n` cifer. Prázdná a jednoprvková
`D` jsou již vyřešeny. Jinak odečtěme nejmenší cifru a vydělme všechny
rozdíly jejich největším společným dělitelem `g`. Tyto operace posunou
a přeškálují `K_n` bijektivně, takže jeho velikost nezmění. Dostaneme
množinu `E` s nejmenším prvkem 0, největším prvkem `h>0` a
`gcd(E)=1`. Nechť `E'=h-E` je její zrcadlená množina.

Pro každou zbytkovou třídu `r modulo h` označme `w_r` nejmenší
nezáporný součet prvků `E`, který do ní patří, a `ell_r` počet sčítanců
v jednom zvoleném takovém zápisu. Tyto hodnoty existují: generované
zbytkové třídy tvoří v konečné cyklické grupě podgrupu a `gcd(E)=1`
zaručuje, že jde o celou grupu. Lze je najít algoritmem nejkratších
cest na `h` vrcholech, kde přičtení cifry `d` má cenu `d`.
Obdobně definujme `w'_s,ell'_s` pro `E'`.

Nyní zvolme efektivní práh

```
N = max_{r mod h} (ell_r + ell'_(−r mod h)).
```

Pro `n>=N` popíšeme přesně součty kongruentní s `r`. Zápis `w_r`
můžeme doplnit ciframi `h` a 0 na `n` míst, takže získáme celou
aritmetickou posloupnost

```
w_r, w_r+h, ..., nh-(h ell_r-w_r).
```

Zrcadlením zápisu `w'_s`, kde `s=-r modulo h`, získáme druhou posloupnost

```
h ell'_s-w'_s, ..., nh-w'_s.
```

Obě mají krok `h` a stejnou zbytkovou třídu. Jejich intervaly se překrývají,
neboť `n>=ell_r+ell'_s`. První má nejnižší možný počátek: každý součet
prvků `E` v této třídě je alespoň `w_r`. Druhá má nejvyšší možný konec:
zrcadlení libovolného `n`ciferného součtu je součet prvků `E'`, a proto
je alespoň `w'_s`. Dostali jsme tedy **všechny** prvky dané třídy mezi
`w_r` a `nh-w'_s`, bez mezer.

Počet nezáporných čísel, která nejsou součty prvků `E`, je konečný a roven
`G=sum_r (w_r-r)/h`. Pro `E'` obdobně `G'`. Sečtení právě odvozených
aritmetických posloupností dává

```
k_n = nh+1-G-G'       pro všechna n>=N.
```

Máme nejen existenci rekurence `k_(n+2)-2k_(n+1)+k_n=0` od konečného
prahu, ale i algoritmus pro celý racionální součet:

```
sum_{n<N} k_n z^n + z^N ((Nh+1-G-G')/(1-z) + h z/(1-z)^2).
```

Konečný prefix se vypočítá přímo ze součtových množin. Formální
vytvořující funkce tak existuje i pro `b=1`, ačkoli ji nelze získat
dosazením do mezí s jmenovatelem `b-1` z tištěného řešení.

## 6. Kandidát V2-C0081: explicitnost rozsahu

V zadání je „any set of integers“ a „any positive integer“. Pro doslova
libovolnou `D` schází konečnost: při `D=Z` je už `K_1=Z` a `k_1`
není konečné celé číslo, které by mohlo být koeficientem uvedené obyčejné
vytvořující funkce. V obvyklém kontextu cifer je konečnost přirozená
implicitní podmínka; právě tento rozdíl mezi doslovným a zamýšleným
čtením je důvod, proč položku vedeme jako **kandidáta upřesnění**, nikoli
jako potvrzenou chybu hlavního matematického výsledku.

Odpověď dále používá konečná `min D,max D` a meze `l,u` z úlohy 19,
obsahující `b-1` ve jmenovateli. Případy `D` prázdná a `b=1` tudíž
nepokrývá uvedený algoritmus. Například při `D={0,1}`, `b=1` máme
`K_n={0,...,n}`, funkci `1/(1-z)^2`, ale meze v odpovědi nejsou definovány.
To nevyvrací obecnou konečnou větu: části 1 a 5 chybějící větve výše
skutečně doplňují.

Přirozené redakční možnosti jsou doplnit „finite“ a samostatné okrajové
větve do odpovědi, nebo vymezit zadání na neprázdnou konečnou `D`
a `b>=2`, což přesně odpovídá vytištěnému algoritmu. [Návrh poznámky](../reports/C0081-digit-recurrence-scope-draft.txt)
je neodeslaný; fyzický nejnovější dotisk ani prvenství nejsou ověřeny.
Všechny čtyři vrstvy errat a aktuální TeX byly prohledány podle stran,
čísla úlohy a jména Klarner; žádná související oprava nebyla nalezena.

## 7. Výpočty a zdrojové omezení

[Ověřovač](../verify_digit_recurrence.py) konstruuje matici inkluzí
 a exkluzí a porovnává ji s nezávislým výčtem součtových množin.
Tištěná matice, čtyři počáteční vektory, racionální funkce a Fibonacciho
hodnoty do `n=10` souhlasí přesně. Dalších 224 kombinací základů 2–5
a cifer z `[-2,3]` pokrývá 7368 hodnot vzorů, dimenze až 32, do `n=5`.

Pro základ 1 ověřeno 224 případů včetně prázdné a jednoprvkových množin;
215 netriviálních případů má nezávislé součtové výčty a kontroly mezer.
Nejvyšší získaný práh byl 60. Příklady s větším rozsahem zahrnují
`{0,6,9,20}`, `{0,4,7,25}`, `{0,17,31}` i posunuté a škálované varianty.
Běh 57961, exit 0; [výsledky](../results/digit-recurrence.json),
[log](../results/digit-recurrence.log). Úspěšné kontroly se neopakovaly.

Bibliografický údaj Klarnerova článku potvrzuje stránka vydavatele:
[An algorithm to determine when certain sets have 0-density](https://www.sciencedirect.com/science/article/abs/pii/0196677481900055),
Journal of Algorithms 2 (1981), 31–43. Úplný článek nebyl získán;
pozdější přímé otevření vrátilo HTTP 403. Důkaz výše vychází z knihy
 a vlastního doplnění, nikoli z předstírané kontroly celého článku.

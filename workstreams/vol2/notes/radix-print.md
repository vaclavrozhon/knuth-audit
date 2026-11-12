# §4.4 E a úloha 13: převod po blocích a tisk 180 číslic

Kontrola 2. listopadu 2026. Text 326, zadání 328 a program
637–638 byly vizuálně přečteny. `w=beta^5` je kapacita slova MIX,
kde beta>=64 je kapacita bajtu. Zvolme `D=10^n<w`; v úloze 13
je D=10^9. Vstupní zlomek s m slovy označujeme `S/w^m`,
`0<=S<w^m`, m>=1. Slova na U+1,...,U+m jsou od nejvyššího řádu.

## Čtyři blokové metody

Pro celé binární číslo dává opakované dělení D číslice v základu
D od nejnižší. Každá taková číslice se vypíše jako n desítkových
číslic, s úvodními nulami kromě nejvyšší skupiny. Je to metoda 1a;
její invariant je totožný s jednotlivými číslicemi.

Pro binární zlomek se násobí D a odděluje celá část, tedy metoda
2a. Protože `0<=r<1`, každý výstupní blok leží v 0,...,D-1.
V opačném směru se desítkové bloky nejprve přečtou do jednoho
slova a pak se použije Hornerův krok `v<-D*v+d` pro celé číslo
nebo zpětný krok `v<-(v+d)/D` pro zlomek. To dokazuje všechny
čtyři body části E. Nezbytné úvodní či koncové nuly poslední
neúplné skupiny jsou pouze umístění číselného bodu; zaokrouhlení
zlomků má stejné požadavky jako základní metoda 2b.

## Aritmetika programu 13

Nechť S_t je celočíselný obsah m pracovních slov po t násobeních
a d_t vydaný blok. Přesný invariant je

```text
S_0*D^t = w^m * (d_1*D^(t-1)+...+d_t) + S_t,
0 <= S_t < w^m,     0 <= d_t < D.
```

V každé vnitřní smyčce se jde od nejnižšího slova k nejvyššímu.
Je-li x aktuální slovo a k přenos, počítá se `D*x+k`, kde
`0<=k<D`. Platí `D*x+k <= D*w-1 < w^2`; vysoká část se proto
vejde do slova a je menší než D. Instrukce MUL, SLC, ADD CARRY
a případné INCX přesně provádějí toto dělení na dvě slova.
JNOV vždy resetuje indikátor přetečení pro další krok.
Konečný rX je d_t; SLAX 5 jej přesune do rA.

CHAR převede d_t na deset desítkových znaků. První je vždy nula,
protože d_t<10^9. STA s polem (2:5) uloží další čtyři znaky,
STX posledních pět. První bajt dvojice slov zůstane tečkou nebo
mezerou. Po dvaceti blocích máme přesně floor(S_0*10^180/w^m),
tedy požadované uříznutí na 180 číslic, nikoli zaokrouhlení.

## Výstupní chyba a oprava

Aritmetika je správná, ale tiskové buffery mají jen 20 slov
na řádek. Skutečný tiskárenský blok má 24 slov. Podrobný doklad,
přesný protipříklad i oprava jsou v
[C0111-radix-printer-buffer.md](C0111-radix-printer-buffer.md).
Opravená varianta používá dva disjunktní bloky po 24 slovech;
čtyři slova na konci každého zůstávají prázdná. Tím lze bezpečně
počítat druhý řádek během tisku prvního.

`verify_radix_print.py` vykonává každou aritmetickou instrukci
dosavadním simulátorem MIX. CHAR a OUT jsou výslovné body
pozastavení s doplněnou sémantikou podle svazku 1, stran 136–138.
Původní čtyři instrukce za BUF+39 jsou pro reprodukci výstupní
vady také uloženy ve formě svých bajtů. U deklarovaných prázdných
částí bufferu předpokládáme nuly; nedostatečná inicializace není
potřeba k protipříkladu a není počítána jako další nález.

Relace 59932 skončila exit 0. Prošlo 270 opravených běhů, m až64,
beta64/128/256, 7354 větví s přenosem. V každém z dvaceti kroků
se porovnává blok i celý zbytek s přímým velkým celočíselným
výpočtem. Oba celé tiskové řádky se ověřují včetně mezer a tečky.
Kromě toho jsou reprodukovány okamžitý a zpožděný tisk původního
programu pro nulový vstup. Doklady jsou v `results/radix-print.json`,
`.log` a `sources/radix-print.mix`.

Část E a úloha 13 jsou uzavřeny, poslední jako confirmed C0111.
Rychlejší konverze 14–16 a floating point D/17/18 jsou další bloky.

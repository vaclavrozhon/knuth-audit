# §4.3.1-1: rané početní postupy

Stav 2. 11. 2026: úloha uzavřena jako historický projekt s přesnými přepisy
vybraných postupů Sun-c’, latinské tradice al-Chvárizmího a Fibonacciho.
Zadání na str. 280–281 uvádí autory jako příklady („say“), ne jako uzavřený
seznam všech povinných pramenů. Níže netvrdíme prostudování al-Uqlīdisīho
ani Recorda. Není zjištěna nová chyba v Knuthově zadání; chyby či neúplnosti
historických textů nejsou automaticky chybami TAOCP.

## Prameny a hranice rekonstrukce

- **Sunzi Suanjing**, první svitek, elektronická edice čínského textu
  [Wikisource, revize 2436749](https://zh.wikisource.org/w/index.php?oldid=2436749&title=%E5%AD%AB%E5%AD%90%E7%AE%97%E7%B6%93).
  Přečteny obecné pokyny pro poziční zápis, násobení a dělení a rozpracované
  příklady 81² a 6561/9. Uložen výběr původního znění v
  `sources/sunzi-selected-original.txt`. Jde o elektronický přepis se
  staršími edičními poznámkami, nikoli o náš přímý průzkum rukopisu.
  Přesnou dataci ani kritickou spolehlivost celé edice zde nerozhodujeme.
  Automatický anglický překlad na Chinese Text Project není podkladem.
- J. N. Crossley a A. S. Henry, **Thus Spake al-Khwārizmī**, *Historia
  Mathematica* 17 (1990), 103–131, odborný překlad Cambridge MS Ii.vi.5.
  [Dostupná anotovaná kopie](https://www.mifami.org/Quad-Sp21/7a-SimTri/Al-Khwarizmi-DixitAlgorizmi-full-NewsomeAnnotated.pdf)
  je uložena jako `sources/khwarizmi-newsome.pdf`. Vizuálně přečteny tištěné
  str. 104, 106 a 114–119 (PDF 3, 5, 13–18); úvodní str. 103–107 rovněž
  textově. Opis latinské adaptace není dochovaný arabský originál; tento
  rozdíl vysvětlují sami překladatelé. Newsomovy dodané poznámky nepovažujeme
  za součást středověkého díla.
- Fibonacci, **Liber abbaci**, kap. II v Boncompagniho vydání (1857).
  Vizuálně přečteny reprodukce latinských odstavců II.2, 8, 19–21, 37–40,
  číslování projektu [Progetto Fibonacci](https://www.progettofibonacci.it/liber/BONCOMPAGNI/trad/txt-trad02B.html).
  Obrázky `images/fibonacci-II-*.png`; tamtéž srovnán odborný italský
  překlad Laury Catastini, revidovaný Sabrinou Rossi a dalšími latinisty.
  Nezaměňujeme jeho odkazy na kritické vydání Giustiho (2020) za přímé
  prostudování tohoto vydání. Bibliografii vydání 1857 potvrzuje
  [ETH, DOI 10.3931/e-rara-34352](https://www.e-rara.ch/zut/content/titleinfo/10607990).

Recorde 1558: získána jen metadata veřejného exempláře Internet Archive;
stažení navigačního OCR i mapy stran skončilo HTTP 500. Jeho text se do
uzavřeného rozsahu nepočítá. Stejně tak nezískané PDF studie o Sun-c’ovi
(HTTP 503) a nezískaný manifest ETH (HTTP 500).

## Společná notace

Číslo U zapisujeme jako součet `sum u_i*10^i`, kde cifry `u_i` jsou 0..9
a místo 0 jsou jednotky. Chybějící vyšší cifry mají hodnotu nula.
Operace `ADD_AT(W,i,t)` přičte celé nezáporné t k místu i pole W:

```
while t > 0:
    append zero places to W when needed
    s = W[i] + t
    W[i] = s mod 10
    t = floor(s/10)
    i = i+1
```

Každý krok zachová číselnou hodnotu, neboť `s = (s mod 10)+10*floor(s/10)`.
Zápis nuly zachovává váhu ostatních míst; není to vymazání a posunutí zápisu.
Všechny následující proměnné jsou celočíselné, není-li řečeno jinak.

## Sun-c’: tři řádky a posouvaný násobitel

Horní řádek obsahuje U, spodní V, prostřední je zpočátku prázdný
(hodnota nula). Jeden věrný aritmetický přepis příkladu 81² je:

```
W = 0
for i = highest position of U down to 0:
    for j = highest position of V down to 0:
        ADD_AT(W, i+j, u_i*v_j)
    remove the processed upper digit u_i
    shift the lower row one position to the right
```

Posun spodního řádku je v indexovaném zápisu vyjádřen snížením i;
neprovádí se ještě druhý číselný posun V. Po každém součinu obsahuje W
součet právě zpracovaných členů `u_i*v_j*10^(i+j)`. Distributivita proto
dokazuje výsledek UV. Pro 81² jsou mezistavy 6400, 6480, 6560, 6561,
přesně jako v původním příkladu. Samotné uspořádání a orientaci počítacích
tyčinek tento číselný model nereprodukuje.

Při dělení je naopak prostřední řádek zbytek R, horní podíl Q. Položíme
R=U, Q=0 a spodní V posuneme k nejvyššímu možnému místu i. Na každém místě
zvolíme největší cifru d z 0..9, pro niž `d*V*10^i <= R`, přičteme
`d*10^i` k Q a odečteme `d*V*10^i` od R; pak snížíme i. Zkoušení nejvýše
devíti násobků je naše přesné doplnění slovního výběru cifry. Invariant je
`U=QV+R`; po kroku na místě i navíc `0<=R<V*10^i`. Konec dává celočíselný
podíl a zbytek. Původní 6561/9 má postupně Q=700,720,729 a R=261,81,0.
Nezpracovaný zbytek se v obecném návodu stává čitatelem zlomku se jmenovatelem V.

## Latinská tradice al-Chvárizmího: destruktivní práce od nejvyšších míst

Str. 115 výslovně začíná sčítání i odčítání nejvyšším místem. Není správné
bez poznámky nahradit tento pokyn dnešními cykly od jednotek.

Pro sčítání kopírujeme U do W a pro místa V od nejvyššího dolů voláme
`ADD_AT(W,i,v_i)`. Přenos se může vrátit do již zpracovaného místa. Po
zpracování míst alespoň i je hodnota W rovna `U+sum_(j>=i) v_j*10^j`.

Pro odčítání předpokládáme U>=V. Opět začneme nejvyšší cifrou V. Je-li
`W[i]<v_i`, najdeme nejbližší nenulové vyšší místo j, snížíme je o 1,
mezilehlé nuly nahradíme devítkami a na místě i přidáme 10. Pak odečteme
v_i. Přeskupení hodnotu nemění. Po kroku je hodnota
`U-sum_(j>=i) v_j*10^j >= U-V >= 0`, takže potřebná zápůjčka existuje.
Toto je přesná rekurzivní realizace půjčování přes nuly v překladu.

Násobení uchovává výsledek v prostoru horního čísla. Vstupní cifry V
neměníme. Na každém i od nejvyššího dolů si podržíme `a=W[i]`. Postupně
zpracujeme cifry V od nejvyššího j k nule; při j>0 přičítáme a*v_j na
místo i+j. **Teprve při j=0 vymažeme staré W[i]** a přičteme a*v_0.
Přenosy zasahují jen již zpracovaná místa, zbývající cifry U pod i nemění.
Po dokončení i platí

```
value(W) = floor(U/10^i)*10^i*V + (U mod 10^i).
```

Tím je zároveň dokázána bezpečnost překryvu vstupu s výstupem. Příklad
2326*214 končí hodnotou 497764. Nulové horní cifry lze přeskočit, jak
text výslovně dovoluje.

Dělení 46468/324 používá stejný horní zbytek a posouvaný spodní řádek,
ale každý vybraný násobek odečítá po cifrách V od nejvyšších. Při přesném
výběru d z výše uvedeného pravidla jsou částečné odčítané součty nejvýše
celý přípustný násobek, proto nemohou vést k zápornému zbytku. Násobky
100,40,3 dávají po řádcích zbytky 14068,1108,136 a výsledek 143+136/324.
Slovní volba zkusmého d v historickém textu není úplným moderním pravidlem
pro opravy nadměrného odhadu; netvrdíme, že samotná nejvyšší cifra vždy
postačí. Náš konečný výběr přes celé V tuto neúplnost výslovně doplňuje.

Půlení naopak začíná jednotkami. Každé původní místo u_i nahradí
`floor(u_i/2)` a je-li u_i liché a i>0, přidá 5 do právě zpracovaného
nižšího místa. Tam dosud leží nejvýše 4, takže přenos nenastane.
Lichá jednotka přidá půl jednotky, v textu 30/60. Identita
`u_i*10^i/2 = floor(u_i/2)*10^i + (u_i mod 2)*5*10^(i-1)`
dokazuje postup i odlišný směr průchodu.

## Fibonacci: diagonály součinu

Odstavce II.2 a II.19 explicitně sdružují součiny, které přispívají ke
stejnému místu výsledku. II.21 a II.37–40 to vysvětlují pomocí proporcí
vah míst. Pro délky m,n a přenos c=0 dostáváme:

```
for k = 0,...,m+n-2:
    t = c + sum_(i+j=k) u_i*v_j
    w_k = t mod 10
    c = floor(t/10)
write the remaining decimal digits of c in higher positions
```

Součet běží pouze přes existující cifry obou čísel. Přenos c **není
omezen na jednu cifru**: příklad II.8 s 98² má t=64,150,96, tedy přenosy
6 a 15 a výsledek 9604. II.20 s 345² dává t=25,42,50,29,11 a výsledek
119025. Obecný invariant po diagonále k je

```
sum_(i+j<=k) u_i*v_j*10^(i+j)
    = sum_(h=0)^k w_h*10^h + c*10^(k+1).
```

Po poslední diagonále na levé straně stojí UV. Důkaz je přímo rozklad t
na jednotky a desítky. Jde o jinou organizaci týchž m*n elementárních
součinů než destruktivní řádkový postup výše.

Zkouška devítkou uvedená v obou tradicích ověřuje jen shodu modulo 9.
Protože 10=1 modulo 9, součet cifer má stejný zbytek jako celé číslo,
a součin zbytků souhlasí se zbytkem správného součinu. Obrácená implikace
neplatí: 497773 projde stejnou zkouškou jako správné 2326*214=497764.
Historické slovní ujištění o správnosti nepřebíráme jako důkaz.

## Kontrola přepisů

`verify_classical_history.py` porovnává uvedené směry průchodu a ukládání
s nezávislou aritmetikou celých čísel: všech 10000 dvojic 0..99, dalších
500 dvojic do 16 cifer a 10000 půlení. U diagonál a destruktivního
násobení ověřuje i uvedené invarianty, u dělení částečné zbytky. Zvlášť
ověřeny původní mezikroky a nedostatečnost zkoušky devítkou.
`results/classical-history.json`, běh 82979, exit 0. Konečné testy podporují
přepis; obecná správnost plyne z invariantů výše. Žádná nová chyba TAOCP.

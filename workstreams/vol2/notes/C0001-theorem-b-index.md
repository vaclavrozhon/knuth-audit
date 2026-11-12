# V2-C0001: chybný index v nové větě B v erratech

**Stav: confirmed, 1. listopadu 2026.** Jde o chybu v aktuálních veřejných
erratech k §4.3.1, nikoli o novou chybu doloženou v našem prvním dotisku.
Identifikátor původního kandidáta ponecháváme. Prvenství není ověřeno.
Fyzický tištěný exemplář ani novější dotisk jsme nekontrolovali.

## Lokace a podklady

Oprava datovaná 14. května 2026, „Page 271 replacement for the bottom eight
lines“, věta B a její důkaz. V dlouhých erratech `all2` jde o stranu 6,
v krátkých `err2` je věta na straně 5 a její důkaz pokračuje na straně 6.
Chybný index byl ověřen v obou sazbách:
[dlouhá](../images/all2-2026-p6.png), [krátká](../images/err2-2026-theorem-b.png).
Nezměněný [TeX zdroj](../sources/err2.textxt), řádky 465–472, obsahuje
**sedm výskytů `v_1`**, které mají být `v_{n-1}`.

Značení určuje původní §4.3.1 na str. 270–271: `b` je základ soustavy,
`v = (v_{n-1} ... v_1 v_0)_b` je kladný n-ciferný dělitel a
`u = (u_n ... u_0)_b` je nezáporný dílčí dělenec splňující `u < b*v`.
Vedoucí cifra je tedy `v_{n-1}`; `v_1` je cifra u mocniny `b^1`.
Nejde o zavedení nového značení. Viz [původní str. 271](../images/vol2-p271.png).

## Přesný protipříklad

Označme `q = floor(u/v)` skutečnou cifru podílu a
`h = floor((u_n*b + u_{n-1})/v_{n-1})` její neuříznutý odhad podle nové
rovnice (2) z roku 2026. Zvolme:

```text
b = 3, n = 3,
u = (1200)_3 = 45,
v =  (121)_3 = 16.

v_{n-1} = v_2 = 1 >= floor(3/2),
u = 45 < 3*16 = 48,
45 = 2*16 + 13,  0 <= 13 < 16,  tedy q = 2,
h = floor((1*3 + 2)/1) = 5 = q + 3.
```

Věta v erratech tvrdí, že při `h = q+3` musí být mimo jiné
`v_1 = (b-1)/2`. Zde ale `v_1 = 2`, zatímco `(b-1)/2 = 1`.
Všechny předpoklady platí a tato nutná podmínka neplatí.
Správná podmínka `v_{n-1} = (b-1)/2` platí.

Chybu nelze obejít pouhým vynecháním podmínky: stejný index je i v důkazu.
Například pro `b=3, n=3, v=(101)_3=10, u=(1000)_3=27` je `q=2` a `v_1=0`.
Tištěný mezikrok `(q+1)*v-1 < (q+1)*(v_1+1)*b^(n-1)` by říkal `29 < 27`
a následující dělení `v_1` by bylo dělením nulou.

## Oprava a obecný důkaz

Ve větě B a jejím důkazu nahradit všech sedm výskytů `v_1` symbolem
`v_{n-1}`. Položme pro přehlednost `a = v_{n-1}`. Potom
`a >= floor(b/2)`, `a >= 1`, `q <= b-1` a `v < (a+1)*b^(n-1)`.
Z definice `q` plyne `u < (q+1)*v`, tedy

```text
h <= u/(a*b^(n-1))
  < (q+1)*(a+1)/a
  = q+1 + (q+1)/a
  <= q+1 + b/a
  <= q+4.
```

Poslední krok používá `b/floor(b/2) <= 3` pro každé celé `b >= 2`.
Celočíselnost dává `h <= q+3`. Je-li `b=2t`, je `a>=t`, takže přísná
mez se zlepší na `h < q+3`. Je-li `b=2t+1`, stejné zlepšení nastane,
pokud `q<b-1` nebo `a>t`. Rovnost `h=q+3` tedy může nastat pouze při
lichém `b`, `q=b-1` a **`a=(b-1)/2`**, jak má správně stát ve větě.

## Kontroly, původ a omezení

[verify_division.py](../verify_division.py) ověřuje certifikát přesnými
celými čísly. Navíc prochází 720 481 přípustných dvojic `(u,v)` v rozsazích
uvedených v [division.json](../results/division.json), včetně 206 případů
`h-q=3`. Opravená věta i její nutná podmínka ve všech těchto případech platí.
Obecný důkaz výše není založen na tomto konečném prohledání.

K 1. listopadu 2026 jsme znovu stáhli `all2-prepre`, `all2-pre`, `all2`,
`err2` a `err2.textxt` z oficiálního webu; soubory se bajtově shodují se
sdíleným archivem. [Manifest](../sources/manifest-2026-11-01.json) obsahuje
URL, časy a kontrolní součty. Všechny tři historické vrstvy byly prohledány
podle stránky, věty a symbolu. Starší vrstvy předcházejí této nové větě;
aktuální krátká i dlouhá errata chybný index přímo obsahují a další opravu
tohoto indexu jsme v nich nenalezli. To nevylučuje dosud nezveřejněné hlášení.

Oficiální zdroje:
[dlouhá errata](https://www-cs-faculty.stanford.edu/~knuth/all2.ps.gz),
[krátká errata](https://www-cs-faculty.stanford.edu/~knuth/err2.ps.gz),
[TeX zdroj](https://www-cs-faculty.stanford.edu/~knuth/err2.textxt).

[Návrh hlášení](../reports/C0001-theorem-b-index-draft.txt) je připraven,
ale nebyl odeslán.

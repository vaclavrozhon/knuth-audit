# V2-X0003 a V2-X0005: §4.3.1, dělení

Uzavřený blok 1. listopadu 2026: důkaz správnosti matematických kroků
algoritmu D na str. 272–273 po relevantních opravách a přesná konečná kontrola
jeho přepisu. Nezahrnuje MIX program, jeho časování ani všechny úlohy §4.3.1.
Nový nález se týká indexu v erratech, viz [V2-C0001](C0001-theorem-b-index.md).

## Značení a verze

Základ poziční soustavy je celé `b>=2`. Dělitel `V` má `n>=2` cifer,
dělenec `U` je nezáporný a vejde se do `m+n` cifer, kde `m>=0`; vedoucí nuly
u `U` jsou dovoleny. Písmena `u,v` níže označují aktuální dílčí dělenec a
normalizovaný dělitel. Cifra `v_i` je koeficient mocniny `b^i` v čísle `v`.
Normalizace znamená, že vedoucí cifra dělitele je alespoň `floor(b/2)`.

Podklady byly zobrazeny: [str. 271](../images/vol2-p271.png),
[272](../images/vol2-p272.png), [273](../images/vol2-p273.png).
Používáme normalizaci opravenou 23. 1. 1998, test D3 opravený 3. 2. 2005
a zvláštní větev D3 z 14. 5. 2026; zdroje viz [mapa](source-map.md).

## V2-X0005: známá chyba normalizace

V prvním dotisku D1 volí `d=floor((b-1)/a)`, kde `a` je vedoucí cifra `V`.
Pro `b=3, n=2, V=(12)_3=5` dostáváme `a=1, d=2`, ale
`d*V=10=(101)_3` má tři cifry. To odporuje požadovanému uložení do dvou
cifer. Je to **known_erratum**, přesně oprava z 23. ledna 1998 v
`all2-prepre`, str. 16, položka pro str. 272 řádky 10 a 23.

Opravené `d=floor(b/(a+1))` je vždy alespoň 1. Z `V<(a+1)*b^(n-1)` plyne
`d*V < b^n`, tedy žádná cifra nepřibude. Dále z definice podlahy
`b < (d+1)*(a+1)` dostáváme `b<=da+d+a`. Protože
`(d-1)*(a-1)>=0`, máme `d+a<=da+1`, a tak `b<=2da+1`.
Odtud `da>=floor(b/2)`, což zaručuje požadovanou vedoucí cifru součinu.
Násobení `U,V` stejným `d` zachovává podíl a násobí zbytek číslem `d`.

## D3 a jedna korekce zbytku

V každém kroku `0<=u<b*v`. Označme `q=floor(u/v)` správnou cifru podílu,
`a=v_{n-1}`, `c=v_{n-2}`, `top=floor(u/b^(n-1))` a
`s=floor(u/b^(n-2)) mod b`. Počáteční odhad je `h=floor(top/a)` a
`r=top-h*a`. Platí `h=floor(u/(a*b^(n-1)))>=q`, protože
`a*b^(n-1)<=v`. Opravená věta B dává `h<=q+3`, přičemž chyba 3
vyžaduje liché `b`, `q=b-1`, `a=(b-1)/2`. Její důkaz je v
[samostatné poznámce](C0001-theorem-b-index.md).

Pro kontrolu druhé cifry položme `A=a*b+c` a
`Q=floor(floor(u/b^(n-2))/A)`. Jde o podíl horních tří cifer dělený
horními dvěma ciframi dělitele. Platí `q<=Q<=q+1`: spodní mez plyne
z `u>=q*v>=q*A*b^(n-2)`; horní z

```text
u < (q+1)*v < (q+1)*(A+1)*b^(n-2),
u/(A*b^(n-2)) < q+1+(q+1)/A <= q+2,
```

kde `A>=b` a `q+1<=b`. To také dokazuje novou rovnici (3) v erratech.

Pokud počáteční `h=b+2` při lichém `b`, z věty B nutně plyne `q=b-1`:
jinak by mez chyby byla nejvýše 2. Nová zvláštní větev tedy nastaví přesné
`h=b-1`. V ostatních případech začne `h<=b+1`.
Test D3 `h*c > b*r+s` je ekvivalentní `h*A > top*b+s`, tedy `h>Q`.
Každé snížení odhadu proto nastává pouze při `h>q` (buď `h>=b`, nebo
`h>Q`); odhad neklesne pod `q`.

Pokud cyklus skončí překročením `r>=b`, potřebujeme také `h<b`.
Jediný problematický případ by byl začátek s `h=b+1` a konec po jednom
snížení. Ale z `top < b*(a+1)` dostáváme `r+a<b`, takže k takovému
ukončení nemůže dojít. Při `h<=b-1` a `r>=b` již druhý test nutně neplatí,
neboť `h*c< b^2<=b*r+s`. Po D3 proto vždy `q<=h<=Q<=q+1` a `h<b`.

D4 odečte `h*v`. Nezáporný výsledek již znamená `h=q`. Záporný výsledek
znamená `h=q+1`, a jediné přičtení `v` v D6, spolu se snížením `h`, dá
správný zbytek. Uložení záporného výsledku modulo `b^(n+1)` a ignorování
přenosu v D6 odpovídá přesně této celočíselné operaci.

Na začátku celé smyčky je okno `floor(d*U/b^m)<d*b^n<=b*v`;
poslední nerovnost používá `V>=b^(n-1)` a `v=d*V`. V dalších krocích
má tvar `b*z+cifra`, kde předchozí zbytek `z<v`. Proto invariant `u<b*v`
platí v každé iteraci. Smyčka provede `m+1` kroků a D8 vydělí zbytek `d`.
Označíme-li vrácený celý podíl `Q_total` a vrácený zbytek `R_total`,
dostáváme `U=Q_total*V+R_total`, `0<=R_total<V`.

## Výpočetní kontrola a její meze

Spuštění z kořene worktree:

```sh
python3 workstreams/vol2/verify_division.py
```

[Výsledky](../results/division.json):

- 720 481 všech přípustných lokálních dvojic: `n=2, b=2..12` nebo
  `n=3, b=2..7`, normalizovaný dělitel `v`, všechny `u=0..b*v-1`.
  Věta B po opravě indexu, rovnice (3) i výstup D3 prošly.
- 278 256 dělitelů: všechny n-ciferné hodnoty pro `n=2,3`, `b=2..32`.
  Opravená normalizace prošla.
- 129 314 úplných dělení: `n=2, b=2..8` nebo `n=3, b=2..5`, `m=1`,
  všechny n-ciferné dělitele a `0<=U<b^(n+1)`.
- 5 000 dalších dělení s pevným seedem 20261101, `n=2..12`, `m=0..12`
  a základy ze seznamu `2,3,5,7,10,16,256`.
- V úplných děleních byla větev přičtení dělitele aktivována 7 096krát,
  nová zvláštní větev 165krát. Test tedy nevynechal vzácné korekce.

Přepis D4/D6 pracuje po cifrách; nezávislým orákulem pro celý výsledek je
vestavěný celočíselný `divmod(U,V)`. Kontroluje se také identita součinu
a zbytku a invariant každého okna. Žádná aritmetika s plovoucí čárkou.

Skript navíc zkouší D3 ve znění 1997 a 2005 při **přesné neomezené
aritmetice**, ovšem s již normalizovaným vstupem. V daném konečném rozsahu
nenašel chybný výstup těchto starších variant; pole
`known_D3_failure_witnesses` je prázdné. Nemáme tedy reprodukci chyby jejich
výsledného podílu. Záznam zveřejněných změn D3 nepoužíváme jako důkaz
takové chyby. Tato kontrola nesimuluje omezenou šířku registrů ani MIX.

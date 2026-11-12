# §3.6: implementace generátorů a úlohy8–13,15

Sazba186–188,193 a599–604 byla přečtena vizuálně, stejně jako náhradní
kód v `all2-prepre`, str.11,34–35. Rozlišujeme původní program1997,
náhradní program2002 a současné soubory autora `rng.c`, `rng-double.c`.
Přesné zdroje a otisky jsou v `sources/summary-generators-sources.json`.
Žádný z autorových stažených souborů není měněn.

## 1. Generování bloku a uchování stavu

Stav `ran_x` obsahuje následujících k=100 hodnot posloupnosti. Kratší
zpoždění je l=37, modul M=2^30. Pole `aa` má délku n>=k a musí mít
odpovídající platnou paměť. Prvních k členů se zkopíruje; zbývající
členy určí rekurence X_j=X_(j−k)−X_(j−l) modulo M.

Po naplnění výstupu je třeba spočítat X_n,...,X_(n+k−1). Pro i<l jsou
oba předchůdci X_(n+i−k),X_(n+i−l) ještě v `aa`. Pro i>=l je druhý
předchůdce již v novém stavu na pozici i−l. To jsou přesně dvě poslední
smyčky. Rozdělení jednoho výstupu na libovolné bloky délky alespoň k
nemění posloupnost ani konečný stav. Délka generovaného posunu je n,
nikoli n+k; k dopředu vypočítaných hodnot je uloženo pro příští volání.

Na dvoukomplementovém stroji `d & (M−1)` dává zbytek modulo M i pro
záporné d. Všechny hodnoty jsou v[0,M), rozdíl v(−M,M), bootstrapový
posun nejvýše2M−4, tedy v rozsahu 32bitového signed long. Předpokládáme
indexy a délky, jejichž mezivýpočty se vejdou do typu int, stejně jako
platně alokované pole. Bitové řešení není přenosné na historické jiné
reprezentace záporných celých čísel; kniha toto omezení výslovně uvádí.

## 2. Polynomový invariant úlohy9

Počítáme v tělese F=GF(2)[z]/(z^100+z^37+1), tedy s koeficienty modulo2
a s redukcí z^100=z^37+1. Primitivita polynomu i řád z rovný
Q=2^100−1 již mají přesný certifikát v `results/binary-polynomials.json`;
tento úspěšný výpočet se neopakoval.

Polynom P_n ze zadání je přeuspořádání spodních bitů bloku100 hodnot:
koeficient X_(n+i) je u z^((i+37) mod100). Přímé odečtení sousedních
polynomů dává

```
z P_(n+1) − P_n = X_(n+63)(z^100+z^37+1) = 0 v F.
```

Tedy P_n=z^(−n)P_0. Bootstrap má jediný lichý koeficient x[1], a proto
reprezentuje z. V původním kódu jsou vysoké liché pozice137,139,...,197
stále sudé; při každém „square“ se vymažou parity všech lichých
pozic1,3,...,135 a zdvojnásobí indexy ostatních. Sestupná redukce tudíž přesně
počítá p(z²)=p(z)² v F. Není to tvrzení o skutečné druhé mocnině
polynomu s koeficienty modulo2^30. Vyšší bity původní program upravuje
záměrně jiným způsobem. Náhradní2002 kód nuluje všechny liché pozice
a redukuje i sudé koeficienty; na paritě je operace stejná.

Násobení z posune koeficienty a přebytečný člen z^100 nahradí
z^37+1. Rotace na konci inicializace je přesně převod koeficientů p
na pořadí X_0,...,X_99 v definici P_0.

Definujme H(s) takto. Začneme celočíselným exponentem1, čteme bity
s od nejnižšího po nejvyšší a za každý bit b nahradíme exponent e
hodnotou2e+b. Nakonec jej vynásobíme2^69. Pro s=0 je H(0)=2^69.
Je-li s=(1 s_j ... s_0)_2>0, dostaneme

```
H(s)=(1 s_0 ... s_j 1)_2 2^69.
```

Zatímco s je nenulové, každá iterace přidá jeden bit; pak proběhne69
samotných druhých mocnin. Původní program má tedy P_n=z^(H(s)−n).

### C0071: chybná vzdálenost v důkazu(c)

Ze shody bloků plyne n−n′≡H(s)−H(s′) modulo Q. Nelze z toho odvodit
vytištěnou mez |n−n′|>=|H(s)−H(s′)|. Konkrétně zvolme

```
s=0, s′=2^29, n=2^99−1, n′=0.
H(s)=2^69, H(s′)=2^99+2^69.
H(s)−n−H(s′)+n′=−Q.
```

Paritní bloky tedy souhlasí, ale |n−n′|=2^99−1<2^99=|H(s)−H(s′)|.
Oba seedy jsou v původním povoleném rozsahu. Jde o lokální chybu
odvození, ne o neplatnost hlavního oddělení proudů.

Oprava: vezmeme vzdálenost na kruhu modulo Q. Hodnoty H jsou různé
liché násobky B=2^69 mezi B a(2^31−1)B. Vnitřní rozestupy jsou
nejméně2B a mezera přes konec kruhu je nejméně2B−1. Proto

```
|n−n′| >= min(d,Q−d) >= 2^70−1,
d=|H(s)−H(s′)|.
```

Rovnost v poslední mezi vyžaduje oba krajní seedy0 a2^30−1. Ten druhý
původní povolený rozsah nezahrnuje, takže tam platí i silnější2^70.
Obecné tvrzení knihy s parametry k,t,e a t+e<=k se dokazuje stejně:
B=2^(t−1), vnitřní mez2^t, krajní nejméně2^t−1.
Rozsah tohoto převzetí upřesněn při obnově X0161: jde o abstraktní
exponenty H a primitivní polynom, s t>=1. Doslovná parametrizace
vytištěného `while(t)` potřebuje TT>=2; při TT=1 nezpracuje ani bity
seedu. Kontextové omezení a úplný malý argument jsou v
`recovery-lagged-initialization-2026-11-06.md`; nejde o nový confirmed.

### C0072: nezapracovaný posun po zahřívání2002

Oprava2002 přidává deset volání `ran_array(x,199)`. Podle části1 je
stav po nich posunut o1990 členů. Nová správná identita je tudíž

```
h(s)=H(s)−1990  modulo Q,
P_n=z^(H(s)−1990−n).
```

Vzorec v odpovědi9(b) na600 zůstal beze změny. Pro seed0 je starý
polynom `0xf85b80e5838f40561323f10da`, ale reálný stav po nové
inicializaci dává `0x756ad685d69f50f0d866a2334`. Každý hexadecimální
bit značí koeficient odpovídající mocniny z. První hodnoty jsou navíc
1028764519 (původní) a58678820 (nová), s opačnou paritou.

Společný posun1990 nemění vzdálenosti mezi seedy ani závěr(c).
Současný autorův zdroj obsahuje stejné zahřívání; tento nález opravuje
návaznost výkladu na nový kód, nikoli samotný generátor.

## 3. FORTRAN, zlomky a 16bitové operace

**Úloha10.** Překlad na jedničkové indexy je správný: C index j odpovídá
FORTRAN indexu j+1; zvláště koeficient2j má index2(j+1)−1. Rozdíl
s následným přičtením M při záporné hodnotě nahrazuje bitovou masku.
Původní i2002 varianty byly porovnány ve všech100 složkách pro132 seedů.
Rozsah zadaný původním textem je0..2^30−3. Pomocná větev pro záporný
seed se nevyužívá k tvrzení, že původní program má bez omezení širší
povolenou doménu; takové rozšíření by vyžadovalo další normalizaci.

**Úloha11.** IEEE binary64 přesně reprezentuje všechna celá čísla do2^53.
Součet dvou zlomků s jmenovatelem2^52 v[0,1) má čitatel menší2^53,
takže součet i odečtení jeho celočíselné části jsou přesné. Odčítací
varianta může obdobně pracovat s jmenovatelem2^53. Bootstrap, zdvojování
a modulo operace mají stejný přesný celočíselný model. Původní pomocné
pole `ul` má hodnoty0 či2^−52 a zaznamenává paritu čitatele. Nové pole
`x` v erratech uchovává stejné bity jako0/1. Tyto operace nemění důkaz
paritního invariantu; zahřívání znovu přidává posun1990.

**C0073: náhradní kód2002 nepřidává deklaraci x.** Retenovaný začátek
odpovědi11 na602 deklaruje `double u[KK+KK-1],ul[KK+KK-1]`. Náhrada
začíná až deklarací `double ss=...`; dále používá `x[j]`, ale žádná
z vrstev errat nedoplňuje deklaraci x. Pouhá změna názvu v próze
„copy in ul“ na „copy in x“ ji nenahrazuje. Přesná rekonstrukce
`repro_errata_ranf.c` se proto nepřeloží: identifikátor x není deklarován.
Po doplnění `int x[KK+KK-1]` se přeloží a oba kontrolní výstupy souhlasí.
Ještě jednodušší oprava odstraní nepotřebné paritní pole a jeho příkazy,
jako to již dělá aktuální autorův `rng-double.c`. Nález se týká
neúplného publikovaného opravného předpisu, ne tohoto samostatného souboru.

**Úloha12.** Při M=2^15 jsou uložené hodnoty0..32767 a jejich rozdíly
v rozsahu signed16. `ss` musí být unsigned, protože zdvojení může
dosáhnout65532. Konstanta `1U<<15` je správná; operace s maskou dává
správný zbytek i po převodu záporného rozdílu na unsigned. Seed do32765
zaručuje bezpečné `seed+2`. Původní kontrolní výstup9387 a aktualizovaný
24130 byly přesně reprodukovány.

Alternativní trojice(a,m)=(157,32363),(146,31727),(142,31657) má skutečně
prvočíselné moduly a primitivní násobitele. Důkaz v programu zkouší
všechny dělitele do odmocniny a všechny prvočinitele m−1. Společná
perioda stavů je lcm(32362,31726,31656)=8125436850168. To samo o sobě
není důkaz kvality libovolné výstupní kombinace.

**Úloha13.** Přeskok na vzdálený stav subtract-with-borrow se redukuje
na modulární mocninu, jak bylo dokázáno v `carry-generators.md` a opravě `C0005-borrow-periodic-extension.md`. Posuny po2^70
zajišťují disjunktní bloky, pokud celkový využitý interval nepřekročí
periodu příslušného cyklu; zcela libovolně mnoho seedů to nezaručuje.
Praktická srovnání rychlosti a kvality jsou historická hodnocení autora,
ne tvrzení o aktuálním nejlepším generátoru. Exponent přibližně1.6
odpovídá násobení s rekurencí T(k)=3T(k/2)+O(k), tedy k^(lg3);
podrobnosti násobení a redukce patří do kapitoly4. V ran_start je
„square“ nad GF(2) nahrazení z za z², s O(k) přesuny a redukcemi,
což není srovnání dvou implementací obecného celočíselného násobení.

## 4. Úloha15: zásobník se značkou konce

Značka−1 je mimo rozsah generovaných hodnot. Po prvním vyvolání cyklu
se vrátí prvek0 a ukazatel přejde na1; při následujících99 voláních se
vydají1..99. Značka na100 vynutí nové generování1009 hodnot. Výstup
je tedy přesně prvních100 hodnot každého bloku1009, se správným pořadím.
Známá oprava2005 nahrazuje100 symbolemKK; známá oprava2002 vyžaduje
reset ukazatele při opakované inicializaci. Aktuální autorův kód také
rozlišuje neprovedenou inicializaci a automaticky použije seed314159.
Obě celočíselné i zlomkové varianty, včetně resetu uprostřed zásobníku,
byly porovnány s nezávislým přímým modelem.

## 5. Kongruenční generátory a úloha8

Pro m=aq+r, 0<=r<q, a0<X<m dává

```
y=a(X mod q)−r floor(X/q) ≡ aX modulo m.
```

První součin je menší m, druhý nepřesáhne ar<m a y leží v(−m,m).
Stačí jediné případné přičtení m. Obě uvedené31bitové dvojice splňují
r<q a přesné konstanty jsou správné. Totéž platí pro trojici úlohy12.

Prvočíselnost a primitivita31bitových násobitelů již byly doloženy v
`spectral-tables.md`. Společná perioda stavů je74382023826798534,
protože gcd(p_1−1,p_2−1)=62. I perioda výstupu Z je celá: při posunu
o periodu druhé složky prochází první složka více než dvěma různými
stavy x. Kdyby další posun d neměl triviální násobitel a_1^d=1, rovnost
rozdílů modulo p_1−1 by vyžadovala, aby (a_1^d−1)x modulo p_1 leželo
v nejvýše dvou hodnotách (dvě celočíselné reprezentace téhož rozdílu).
To nelze. První složka je tedy po d stejná; pak rozdíl druhé složky
má velikost menší p_2−1<p_1−1 a musí být nula. Obě periody d dělí.
Pro původní výstup modulo p_1 je stejný argument ještě přímočařejší.
Známá oprava2010 používá při Z<=0 přírůstek p_1−1 místo p_1; oba
uvedené intervaly výstupů v příslušných verzích odpovídají kódu.

Pro n kroků afinního generátoru je X_n≡a^n X_0+c(1+...+a^(n−1))
modulo m. Při a>1 lze spočítat čitatele

```
A=(a^n((a−1)X_0+c)−c) modulo ((a−1)m)
```

a vrátit A/(a−1). A je dělitelný a−1, takže přesná reprezentace dává
správný výsledek. Případ a=1 se kontroluje přímo X_0+nc modulo m.
Vytištěná mocnina48271^1000000 modulo2147483647=1263606197 souhlasí.
Kontrola vzdáleného stavu je užitečná, ale není úplným důkazem libovolné
implementace; některé chyby se mohou v daném kontrolním bodě kompenzovat.

## 6. Výsledky a errata

`verify_summary_generators.py` má šest checkpointů, všechny prošly.
264 počátečních stavů porovnáno s nezávislou mocninou v GF(2) i
jedničkovým FORTRAN modelem;1848 porovnání rozděleného bloku a celkové
rekurence;60 úplných menších parametrických množin ověřuje kruhovou mez.
Přeložené aktuální zdroje souhlasí v66480 přesných hodnotách, zásobníkové
rozhraní v2504 výstupech. Všech šest starých/nových kontrolních čísel
souhlasí.268234 hraničních Schrageových vstupů a23920 afinních identit
prošlo; nové kompilační erratum a malé prvočíselné certifikáty mají
samostatné checkpointy. Úspěšné první čtyři bloky nebyly při rozšíření
opakovaně spouštěny.

Pro C0071–73 byly prohledány all2-prepre, all2-pre, all2, err2 a uložený
aktuální TeX podle stran, vzorců a názvů proměnných. Opravy těchto tří
problémů nenalezeny; ostatní výše uvedená errata jsou zapracována.
Novější fyzický dotisk ani prvenství nejsou ověřeny; návrhy se neodesílají.

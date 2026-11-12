# §1.3.3: programy I/J a cvičení 12, 15, 16, 24

Kontrola 1. listopadu 2026, třetí vydání, první dotisk (květen 1997).
Nový nález: **žádný**. Matematická a strojová část přiděleného bloku je
ověřena v níže uvedeném rozsahu. Úplné texty některých historických citací
u cvičení 12 nebyly dostupné; tato část bibliografické kontroly zůstává
`partial`, viz poslední oddíl. Fyzický tištěný exemplář nebyl porovnán.

Práce navazuje na [starší důkaz](../../notes/permutation-inversion.md).
Jeho 46 233 kontrol pseudokódu I/J ani nezměněný důkaz průměru nebyly znovu
spouštěny. Zde jsou nové strojové, tabulkové, kanonické a rozptylové kontroly.
Sdílený ledger, mapu rozsahu ani simulátory tento blok nemění.

## Zdroje a errata

Původní obrazy: [176](../../images/vol1-file191-p176.png),
[177](../../images/vol1-file192-p177.png),
[178](../../images/vol1-file193-p178.png), [179](images/vol1-p179.png),
[180](images/vol1-p180.png), [182](images/vol1-p182.png),
[183](images/vol1-p183.png), [184](images/vol1-p184.png),
[523](../../images/vol1-file538-p523.png), [524](images/vol1-p524.png),
[525](images/vol1-p525.png). Strana souboru DjVu je tištěná strana + 15.

Prohledány `all1-prepre`, `all1-pre`, `all1`, `err1`, podle stránek i označení
algoritmů a témat. [Výpis s SHA-256](results/errata-search.json) zachovává
relevantní bloky. Relevantní již publikované změny jsou:

- I5, s. 176: `X[i]` v komentáři se mění na `X[-i]`, 22. 2. 1998,
  [obraz](images/errata-all1-prepre-p15.png). Přiřazení bylo správné již v tisku.
- S. 178, mezera před cyklem, 24. 12. 2001, stejný obraz.
- Program J, s. 178, řádky 01–04 používají rI4 místo rI1, 23. 12. 2024,
  [obraz](images/errata-all1-p8.png). Níže kontrolujeme obě varianty.
- Cvičení 12, s. 182: rozměr výsledku `n x n` se mění na `n x m`, 4. 8. 1997,
  [obraz](images/errata-all1-prepre-p16.png).
- Odpověď 13, s. 523: doplněná podmínka záporné větve invariantu,
  29. 3. 2023; tento známý nález již obsahuje starší důkaz.
- Odpověď 24, s. 525: sazba roku v citaci, 24. 12. 2001,
  [obraz](images/errata-all1-prepre-p38.png). Matematický obsah se nemění.

## Programy I/J: obecný strojový důkaz a čas

Permutace `p` je bijekce množiny `{1,...,n}`; `n>=1`. Pole `X` obsahuje
její původní hodnoty a má skončit jako inverze `p^-1`, tj. `X[p(k)]=k`.
`C` označuje počet cyklů permutace. `A` označuje počet provedení kroku J3,
včetně posledního čtení se záporným výsledkem v každé vnější iteraci.
Jednotka `u` je časová jednotka MIX. Slovo MIX má znaménko a pět bajtů;
indexový registr má znaménko a dva bajty. Báze bajtu `b` může být každé
celé číslo od 64 do 100.

**Program I.** Na hranicích kroků algoritmu je `rI1=m`, `rI2=-i`,
`rI3=j`. `LD2N` přečte zápornou hodnotu pole, podmíněné skoky proto správně
obracejí test znaménka z pseudokódu. Dvojice `ENN3 0,1` a `ENN1 0,2`
realizuje `j=-m` a `m=i`. Při uzavření cyklu `ENN2 0,3` nastaví `-i=-j`.
`ST2 X,1` zapíše `-i`. Každý ostatní řádek je přímo odpovídající operace
pseudokódu; obecný důkaz cyklů ve starších poznámkách se tedy přenáší na
strojový kód. Výchozí hodnoty registrů nejsou předpokladem.

Řádky 01,02 se provedou jednou, řádek 10 právě `C` krát a zbývajících
10 řádků právě `n` krát. Čtyři paměťové instrukce na prvek stojí `2u`,
ostatní `u`, proto počet instrukcí je `10n+C+2` a čas je

```text
T_I = (14n + C + 2)u.
```

**Program J.** Při inicializaci je použitý registr postupně
`-n,-n+1,...,-1`. Adresy `X+n+1+rI` jsou přesně `X+1,...,X+n`.
`STr X+n+1,r(0:0)` zapisuje pouze záporné znaménko, nikoli magnitudu.
Po smyčce `ENT1 N` nastaví `m=n`. To platí jak pro původní `r=1`, tak pro
publikované `r=4`. Obě varianty mají shodný účinek na pole a shodný čas;
původní inicializace není nalezeným protipříkladem správnosti výpočtu.
Varianta 2024 navíc přepisuje rI4; původní jej zachovává. Důvod autorské
změny není v erratech vysvětlen, a zde jej nepředstíráme.

V hlavní smyčce je `rI1=m`, `rI2=j`, `rI3=-i`. Řádek 06 nejprve vloží
`-m` do rI3; řádek 07 z něj vytvoří `j=m`. Při opakování J3 stejný řádek
07 vytváří `j=i` z předchozího záporného rI3. Řádky 10–12 postupně
načtou `X[-i]`, zapíší je do `X[j]` a zapíší `m` do `X[-i]`.
Pořadí je správné i při `j=-i`. Opravený invariant J ve starších poznámkách
proto dokazuje celý strojový program.

Řádky 01,05 mají frekvenci 1; řádky 07–09 frekvenci `A`; ostatních devět
řádků frekvenci `n`. Počet instrukcí je `9n+3A+2` a čas je

```text
T_J = (13n + 4A + 2)u.
E[T_J] = (4(n+1)H_n + 9n + 2)u,
```

kde `H_n=sum(1/k, k=1,...,n)` je harmonické číslo. Použitý průměr
`E[A]=(n+1)H_n-n` již byl obecně dokázán. Platí `A>=n` a `C<=n`,
takže `T_J-T_I=4A-n-C>=2n`: I je rychlejší na **každém** přípustném
vstupu těchto programů, nikoli pouze v průměru. To podporuje text na s. 178.

**Meze MIX.** Předpokládáme, že pole a nepřepisovaný kód leží disjunktně
v adresách 0–3999. Základ pole splňuje `-1<=X` a `X+n<=3999`.
Každá skutečně používaná hodnota indexového registru má velikost nejvýše
`n<=4000`, menší než nejmenší dvoubajtová kapacita `64^2=4096`.
V J může konstantní adresová část `X+n+1` dosáhnout 4000, což je stále
reprezentovatelné; efektivní adresy jsou uvnitř pole. Žádná hodnota pole
není nula, takže záporná nula nemění testy. Nula vzniklá při dokončení
čítače již nevede k dalšímu zápisu do pole.

Pro izolovaný fragment 13 instrukcí I lze disjunktně umístit nejvýše
3987 datových slov, pro 14 instrukcí J nejvýše 3986. Běhy s takovou
kapacitou se zastavují na hranici fragmentu; neposkytují tím místo pro
následující program. Plný program s připojeným `HLT` a nepřekrývajícím se
polem má kapacitu 3986 pro I a 3985 pro J. Tyto úplné programy byly rovněž
provedeny do skutečného zastavení. Kniha žádné číselné kapacitní tvrzení
u I/J neuvádí, takže nejde o erratum.

**Konečná strojová kontrola.** [Přepis a checker](check_inplace.py) používá
sdílené `mix_machine.py` a `mixal.py`; oba byly před použitím přečteny.
Pro každou variantu I, původní J, J-2024 prošlo všech 5913 permutací pro
`1<=n<=7`. Ověřuje se inverze, každý řádkový čítač, přesný čas, zachování
paměti mimo pole a nezávislost na výchozích registrech. Dalších 888 běhů
pokrývá všechny báze 64–100 a velikosti 1,2,63,64,65,99,100,101.
Krajní umístění pole nahoře i dole, obě krajní báze a velké identity/jeden
cyklus prošly. Nejhorší hledání J s `n=128` má `A=8256` a čas `34690u`.
[Výsledky](results/inplace.json) zachovávají přesné parametry.

Tabulka 3 má 15 zobrazených stavů, tabulka 4 má 13. Všechny buňky pole
včetně `m,i,j` byly přepsány ze skenu nezávisle na výpočtu a porovnány s
uloženými strojovými stopami; shodují se. První prázdné `i` v tabulce 4
správně nevyjadřuje požadavek na výchozí registr. Kontrola je v
[check_mathematics.py](check_mathematics.py), [výsledek](results/mathematics.json).

## Kanonický tvar, s. 178–180, cvičení 15 a 16

Kanonický cyklický zápis začíná každý cyklus nejmenším prvkem, zahrnuje
jednoprvkové cykly a řadí cykly podle jejich prvního prvku sestupně.
`F(p)` označuje lineární posloupnost vzniklou odstraněním závorek.
Prvek posloupnosti je **minimum zleva**, je-li menší než všechny prvky
před ním; první prvek má tuto vlastnost automaticky.

Začátky kanonických cyklů jsou přesně minima zleva. Uvnitř cyklu nemůže
vzniknout nové minimum, protože jeho první prvek je menší. Naopak každý
nový cyklus začíná prvkem menším než předchozí začátky, a tedy menším než
všechny dřívější prvky. Rozdělení libovolné lineární permutace těsně před
minimy zleva proto vždy dává právě jeden kanonický cyklický zápis. Tak je
`F` bijekce. Příklady `621543 -> 452163 -> 256314 -> 364125` souhlasí.

Statistika (21) plyne i přímo: při rovnoměrném nezávislém výběru jednoho
z `k` míst vložení nového prvku `k` vzniká nový cyklus s pravděpodobností
`1/k`. Počet cyklů je součet nezávislých indikátorů těchto událostí.
Má minimum 1, maximum n, průměr `H_n` a rozptyl `H_n-H_n^(2)`, kde
`H_n^(2)=sum(1/k^2,k=1,...,n)`. Generující polynom počtu cyklů je
`z(z+1)...(z+n-1)/n!`; jeho koeficienty jsou nezáporná Stirlingova čísla
prvního druhu dělená `n!`. Všechna tvrzení (21) tak souhlasí pro `n>=1`.

Dále mezi všemi `n!` permutacemi existuje
`binom(n,r)*(r-1)!*(n-r)!=n!/r` výskytů cyklů délky `r`, `1<=r<=n`.
To ověřuje počet třícyklů na s. 179 i úvod s. 180. Následující část
s. 180 o pevných bodech a její pokračování patří pracovníkovi statistiky.

**Cvičení 15.** Předpokládejme `F(p)=p` a položme `m=p(1)`.
Je-li `m=1`, pak je `(1)` poslední kanonický cyklus: 1 je současně
poslední symbol `F(p)` a první symbol `p`, což při jedinečnosti symbolů
vynucuje `n=1`. Je-li `m>1`, pak poslední cyklus obsahuje sousední
symboly `1,m`. Ve `F(p)` tedy před m stojí 1, ale v lineárním `p` je m
první. To je spor. Pro `n=0` je prázdná permutace rovněž pevným bodem.
Odpověď na s. 523–524 je správná, včetně dodatku o prázdné permutaci.

**Cvičení 16.** Přímé převody dávají

```text
1324 -> 4231 -> 3214 -> 4213 -> 2143 -> 3412
     -> 2413 -> 1243 -> 3421 -> 1324.
```

Každý přechod byl získán cyklickým rozkladem a odstraněním závorek.
Odpověď na s. 524 je přesná. Dodatečně se pro `0<=n<=8` ověřilo, že
obnova závorek je inverzní k `F` a jedinými pevnými body jsou uvedené
případy `n=0,1`.

## Cvičení 12: obdélníková transpozice

Nechť `m,n` jsou kladné rozměry matice a `m!=n`; položme `N=mn-1>=1`.
Index `x=n(i-1)+(j-1)` označuje původní místo prvku `a[i,j]`, bez
společného základu paměti `L`. Jeho nové místo je
`y=m(j-1)+(i-1)`. Krajní index `x=N` má rovněž `y=N` a zůstává pevný.
Pro `0<=x<N` je `0<=y<N` a

```text
m*x = mn*(i-1) + m*(j-1) = y (mod N),
```

protože `mn=1 (mod N)`. Nové místo je tedy nejmenší nezáporný zbytek
`m*x mod N`, jak tvrdí zadání a odpověď (po známé opravě rozměrů).

Platí `gcd(m,N)=1`, tedy násobení m zachovává třídu danou přesnou
hodnotou `d=gcd(x,N)`. Pišme `x=d*t`, `M=N/d`, `gcd(t,M)=1`.
Návrat do původní pozice po r násobeních je ekvivalentní
`m^r*t=t (mod M)`, a tedy `m^r=1 (mod M)`. Délka každého cyklu této
třídy je nejmenší kladné r s uvedenou vlastností, tzv. multiplikativní
řád m modulo M. V třídě je `phi(M)` prvků, kde `phi` je počet zbytků
nesoudělných s M, a proto přesně `phi(M)/r` cyklů. Pro `M=1` bereme
`phi(1)=1`, r=1; to je pevný prvek x=0. Dále je zvlášť pevný x=N.
Tvrzení odpovědi o délkách a počtech cyklů je správné i na těchto hranicích.

Značkování jedním volným bitem na prvek dovolí projít a přemístit každý
cyklus právě jednou. Nemá-li datové slovo volný bit, lze použít samostatné
bitové pole nebo seznam jednoho zástupce z každého cyklu. Bez takového
pole existuje tento obecný postup s pevným počtem pomocných slov: pro
každý kandidát s opakovaně aplikuj permutaci, dokud nenalezneš prvek
`<=s`; cyklus přemísti právě tehdy, když se vrátíš do s. Každý cyklus se
přemístí pouze při svém nejmenším prvku. Při přesouvání stačí jedna
uložená datová hodnota a indexy. Hledání může být kvadratické, zatímco
značkování je lineární při konstantním čase přístupu k permutaci.

Směr přesunu je podstatný: výše uvedené násobení m je funkce ze starého
místa do nového. Při přiřazování `a[v]=old_a[p(v)]` se má použít její
inverze `p(v)=n*v mod N`, nikoli totéž m. Po obou směrech byl zkontrolován
výsledek 600 obdélníků s rozměry 1–25, včetně jednorozměrných případů;
ověřily se též délky cyklů a počty podle `gcd`. Konečná kontrola doplňuje
obecný důkaz, nepředstavuje jeho náhradu.

## Cvičení 24: obecný důkaz rozptylu

Rozptyl náhodné veličiny Y je `Var(Y)=E[Y^2]-E[Y]^2`. Při rovnoměrně
náhodné vstupní permutaci je i kanonický zápis její inverze bez závorek
rovnoměrně náhodnou lineární permutací q. Předchozí důkaz počtu kroků J
identifikuje A s počtem intervalů `[i,j]`, `i<=j`, v nichž je q[i]
nejmenší prvek. Každý jednoprvkový interval se počítá.

Umístěme nejmenší prvek q na pozici `k+1`, kde `0<=k<n`. Počet intervalů
začínajících v tomto minimu je `n-k`. Interval začínající vlevo od minima
a přesahující do něj se nepočítá. Všechny ostatní počítané intervaly leží
celé vlevo nebo celé vpravo. Relativní pořadí obou částí jsou při daném k
nezávislá rovnoměrná pořadí. S nezávislou kopií označenou čárkou tedy

```text
A_n = A_k + A'_(n-1-k) + n-k,     Pr(k)=1/n,     A_0=0.       (R)
```

Tato rekurence určuje všechny momenty a rozdělení. Pro uzavřený tvar
zaveďme pravděpodobnostní polynom `G_n(t)=E[t^A_n]` a jeho obyčejnou
vytvořující řadu `S(z,t)=sum(G_n(t)*z^n,n>=0)`. Z (R) plyne

```text
n*G_n(t) = sum(t^(n-k)*G_k(t)*G_(n-1-k)(t), k=0,...,n-1),
S_z(z,t) = t*S(z,t)*S(t*z,t),      S(0,t)=1.                 (G)
```

Zápis `S_z` značí derivaci podle z, obdobně `S_t` podle t.
Definujme `M(z)=S_t(z,1)` a `Q(z)=S_tt(z,1)`; jejich koeficienty jsou
`E[A_n]` a `E[A_n(A_n-1)]`. Položme `L=-log(1-z)`.
Protože `S(z,1)=1/(1-z)`, jedna a dvě derivace (G) dávají

```text
M' - 2M/(1-z) = 1/(1-z)^3,
Q' - 2Q/(1-z) = (2L^2 + (4+2z)L + 4z)/(1-z)^4.
```

Nulové konstantní koeficienty určují řešení

```text
M = L/(1-z)^2,
Q = 2(L^2+L+1)/(1-z)^3 - (L^2+4L+2)/(1-z)^2.              (M)
```

Koeficienty se získají jednou a dvěma derivacemi identity
`[z^n](1-z)^(-r)=binom(n+r-1,n)` podle r. Konkrétně koeficient
`L^2/(1-z)^r` je

```text
binom(n+r-1,n) *
((H_(n+r-1)-H_(r-1))^2 - H_(n+r-1)^(2) + H_(r-1)^(2)).
```

Dosazením r=2,3 do (M), přičtením `E[A_n]` k faktoriálnímu druhému
momentu a odečtením čtverce průměru vychází

```text
Var(A_n) = 2n(n+2) - (n+1)H_n - (n+1)^2 H_n^(2).           (V)
```

To je přesně vzorec z Knuthova primárního reportu STAN-CS-71-206,
*Mathematical Analysis of Algorithms*, březen 1971, druhá přednáška,
s. 17 reportu (= strana 26 souboru), viz
[originální obraz](images/knuth1971-file26.png) a
[celý report](sources/knuth1971-analysis.pdf). Článek počítá veličinu
`a=A_n-n`; odečtení konstanty n rozptyl nemění. Primární report také
výslovně propojuje tuto veličinu s algoritmem inverze z TAOCP.
Tím je ověřena věcná použitelnost odkazu v odpovědi 24. Report je preprint
přednášky, nikoli fyzický výtisk sborníku s jeho stránkami 19–27.

Vzorec dále souhlasí s Prodingerovým autorským preprintem
[math/9903149](https://arxiv.org/pdf/math/9903149), s. 9.
Doplňkové nové výpočty ověřily (V) výčtem všech lineárních permutací
`0<=n<=8` a nezávislou momentovou rekurencí (R) pro `n<=100`, vždy s
přesnými racionálními čísly. Pro n=8 je rozptyl `926539/78400`.
U algoritmu J tedy `Var(T_J/u)=16 Var(A_n)`; u I z (21)
`Var(T_I/u)=H_n-H_n^(2)`.

## Historické primární citace: přesný rozsah

[Manifest](sources/coverage.json) rozlišuje dostupný článek, původní
program a pouhá metadata. [Záznam pokusů](sources/publisher-downloads.json)
obsahuje odpovědi 403 pěti vydavatelských PDF. Nejde o důkaz chyby citace.

- **Berman 1958, JACM 5, 383–384:** bibliografické údaje potvrzují
  metadata uložená vydavatelem u Crossref, DOI
  [10.1145/320941.320952](https://doi.org/10.1145/320941.320952).
  Původní celý text nezískán. Matematická správnost značkovacího postupu
  výše je dokázána samostatně; jeho přesnou shodu s Bermanovou variantou
  zde neoznačujeme za ověřenou.
- **Windley 1959, Computer Journal 2, 47–48:**
  [vydavatelský abstrakt](https://academic.oup.com/comjnl/article-pdf/2/1/47/1116824/020047.pdf)
  a metadata potvrzují téma a lokaci. Celý článek nebyl dostupný.
- **Brenner 1973, CACM 16, 692–694:** autorem zveřejněný
  [plný text](https://www.researchgate.net/publication/234810550_Algorithm_467_Matrix_Transposition_in_Place)
  byl přečten v části teorie a algoritmu. Zachovává třídy `gcd`, spojuje
  hledání zástupců s tabulkou značek a dává doporučenou malou pracovní
  tabulku. To potvrzuje konkrétní tvrzení odpovědi 12. Původní program je
  navíc uložen z [Netlib 467](https://www.netlib.org/toms/467.gz).
  Neproběhl audit všech řádků tohoto externího Fortranu.
- **Knuth 1971, IFIP, 1, 19–27:** výše uvedený primární report obsahuje
  přímo obecný postup hledání nejmenšího zástupce cyklu a jeho analýzu;
  [obraz s. 10](images/knuth1971-file19.png). Tím se ověřuje existence
  popsaného obecného postupu s pevným počtem pomocných slov i odkaz 24.
- **Cate–Twigg 1977, TOMS 3, 104–110:** vydavatelská metadata a původní
  [Netlib 513](https://www.netlib.org/toms/513.gz) byly získány. Kód hledá
  cykly a jejich zrcadlové protějšky a používá parametrizovanou tabulku
  `MOVE`. Celý text analýzy nebyl dostupný; externí Fortran nebyl kompletně
  certifikován.
- **Fich–Munro–Poblete 1995, SICOMP 24, 266–278:**
  [primární abstrakt](https://epubs.siam.org/doi/10.1137/S0097539792238649)
  potvrzuje obecné permutování i variantu s konstantním počtem slov při
  dostupnosti permutace a inverze. Bibliografická data souhlasí. Úplný
  důkaz tohoto externího článku nebyl revidován.

Matematické řešení cvičení 12 je tedy `checked` po známé opravě. Přísný
požadavek na přečtení všech šesti citovaných článků je stále `partial`;
zejména Berman a Windley potřebují dostupný plný text. Autorství I u
Huanga bylo dohledáno bibliograficky, ale jeho původní dvoustránkový
článek není v tomto bloku plně porovnán. Tyto hranice se nesmějí při
integraci ztratit.

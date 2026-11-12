# Spektrální test: rozšíření algoritmu a kratší periody

Audit §3.3.4-16–21 a24, tištěné strany116–117 a581–582, první dotisk
třetího vydání, září1997. Původní stránky i kroky S1–S10 na102–103
byly vizuálně přečteny. Jde o sedm uzavřených úloh, nikoli celou sekci.
Všechny výpočty níže jsou přesné; doklady obsahují
`verify_spectral_extensions.py` a `results/spectral-extensions.json`.

## 1. Součet absolutních hodnot: úloha16 a C0044

Řádky U_i tvoří bázi celočíselné mříže dané kongruencí
u_1+a*u_2+...+a^(t-1)*u_t=0 modulo m. Pro souřadnice X v této bázi
označme Y=XU. Norma L1 je součet absolutních hodnot složek; norma
Linf je jejich největší absolutní hodnota. Definujme f(X)=||XU||_1.
Neškálovaná duální báze má matici V=U^(-T), takže x_k=Y·V_k, a tedy

```
|x_k| <= ||Y||_1 ||V_k||_inf = f(X) ||V_k||_inf.
```

**C0044:** v odpovědi je místo f(X) napsáno f(Y). Nejde o obecně platnou
alternativu. Pro U=((1,-1),(0,2)), V=((1,0),(1/2,1/2)), X=(4,3)
je Y=(4,2), f(Y)=4 a tištěná nerovnost pro k=2 tvrdí3<=2.
Tato U skutečně tvoří bázi kongruence u_1+u_2=0 modulo2.

Pro neposunutou mříž z úlohy15 počítáme
g(Y)=||Y||_1-delta(Y), kde delta=1, právě když má Y kladnou i zápornou
složku. Omezení na neposunutou mříž je podstatné: obecné posunutí může
počet rovin změnit, jak ukazuje C0038 v `spectral-foundations.md`.
Je-li k nejmenší nenulová L1 norma, minimum g je k-1, existuje-li
smíšený minimalizující vektor, jinak k. Vektory normy>=k+1 nedají méně.

Konečný soupis pro minimum g lze provést s mezí s na g: každý **striktně
lepší** celočíselný vektor splňuje g(Y)<s, a proto ||Y||_1<=s. V algoritmu
se používá škálovaná dualita UV^T=mI; stačí tedy
z_k=floor(s*max_j|v_kj|/m). Není nutné zvětšovat s na s+1. Vektory
normy s+1 mohou pouze dorovnat dosavadní výsledek, což úloha16 nepožaduje.

Inicializace v dimenzi1 a rozšíření S4 jsou správné. Aktualizace normy
po změně řádku patří do S4 a **S5**, nikoli do vytištěné dvojice S4/S7:
v S4 jde o U_t a v S5 o U_j. S7 žádnou původní aktualizaci s nemá.
Jde o druhou redakční závadu stejné odpovědi. Nepřisuzujeme jí zvlášť
prokázaný chybný číselný výstup: i ponechaná celočíselná kvadratická
norma je horní mez L1 normy. Opravená verze aktualizuje změněný řádek
jeho L1 normou; s se při přechodu dimenzí zachová vložením nulové složky.
Redukce S5 končí ze stejného důvodu jako původní algoritmus.

Nezávislé hledání přímo v souřadnicích Y minimalizovalo L1 a určilo,
zda existuje smíšený minimalizátor. Shodlo se s upraveným algoritmem na
1259 nesoudělných dvojicích a,m, m<=64, celkem5036 minimech v dimenzích2–5.
Tyto testy doplňují důkaz, nenahrazují jej.

## 2. Všechny minimalizátory: úloha17 a C0047

V dimenzích t>=3 je navržené vypisování v S9 správné: konečný kvádr
obsahuje všechny vektory s normou nejvýše počáteční meze. Při rovnosti
se dvojice Y,-Y přidá, při zlepšení se dosavadní seznam zahodí. Projde
se právě jeden reprezentant každé dvojice znamének a žádná minimální
dvojice se neztratí.

**C0047 má dvě části ve stejné odpovědi.** Za prvé úloha výslovně
požaduje i t=2, ale odpověď mění pouze S9. Pro t=2 proběhnou S1–S3;
S4 buď ukončí algoritmus (T=2), nebo t zvětší. S9 se při t=2 nikdy
neprovede. Například a=2,m=5 mají čtyři nejkratší vektory
±(2,-1),±(1,2), všechny čtverce délky5, ale navržená úprava žádný
dvourozměrný vektor nevypíše. Lze po S3 provést S7–S10 i pro t=2,
nebo stejný soupis vyřešit zvlášť z redukované dvourozměrné báze.

Za druhé poznámka o jediné dvojici při přípravě tabulky1 neplatí již
pro její řádek3: a=2^18+1,m=2^35,t=6. Dvě různé minimální dvojice jsou

```
±(1,-1,0,0,-1,1),  ±(1,0,-1,-1,0,1).
```

Obě mají nenulovou první i poslední složku, takže uvedená výjimka
y_1=0 nebo y_t=0 se neuplatní. Položíme-li b=2^18, pak b^2=0 modulo m
a a^j=1+jb modulo m. U obou vektorů je součet koeficientů i součet
j*u_(j+1) nulový. Čtverec normy je4. Menší nemůže být: norma1 je
jednotkový vektor; norma2 by vyžadovala a^i=±a^j pro různé i,j<=5;
norma3 má tři nenulové složky ±1 a lichý součet, který není0 modulo b.
Rozdíl indexů nejvýše5 přitom není dělitelný m/b=2^17. Úplné dřívější
hledání tabulky nezávislou sférou našlo právě tyto čtyři minimalizátory
s nenulovými krajními složkami. Tabulková číselná hodnota4 je správná.

## 3. Špatně redukovaná báze: úloha18 a C0045

Nechť m>1, m=1 modulo3, y=(1-m)/3 a J je matice3x3 samých jedniček.
Položme V=mI+yJ, U=I-yJ. Z J^2=3J plyne UV^T=mI; vlastní hodnoty U
jsou1,1,m, takže det U=m. Každý řádek U má součet m a splňuje kongruenci
pro a=1. Přímým násobením vyjde

```
V_j·V_k = (1-m^2)/3                  (j != k),
V_j·V_j = (2m^2+1)/3,
U_j·U_j = (m^2+2)/3.
```

**C0045:** první výraz je v knize s opačným znaménkem. Například m=64
dává -1365, nikoli1365. Kritérium S5 obsahuje absolutní hodnotu,
takže chyba nepoškozuje hlavní příklad: 2|V_j·V_k|<||V_j||^2,
žádná redukce se neprovede. Počáteční s=(m^2+2)/3 vede k
z_j~sqrt(2)*m/3 a počtu kandidátů řádu m^3. Přesto rozdíly řádků U
mají čtverec normy2; jednotkové vektory kongruenci pro m>1 nesplňují.

Po výměně rolí U,V v S5 je pro j=1 a oba ostatní řádky q=1. Dostaneme
U_2=(-1,1,0),U_3=(-1,0,1),V_1=(1,1,1); ostatní vytištěné řádky zůstávají.
Matice pro m64 i obecné vzorce jsou správné. Příklady m4,7,64,1000
byly kontrolovány přesným násobením; pro m1000 má původní půlkvádr
419280903 kandidátů. Ten se neenumeroval, jeho velikost je spočtena vzorcem.

## 4. Půlčíselné zaokrouhlení: úloha19

Povolíme-li kladnou rovnost 2V_i·V_j=||V_j||^2 s q=1, součet čtverců
délek řádků V stále neroste. Vektory V patří do pevné diskrétní mříže,
v omezené kouli je jich konečně mnoho. Kdyby redukce nikdy neskončila,
po konečně mnoha striktních zkráceních by následovaly pouze rovnosti
a některý stav báze by se opakoval. Odpovídající změny U jsou násobení
elementárními maticemi I+E_ji: mají nezáporné prvky a jedničky na diagonále.
Neprázdný součin nemůže být I, protože přidaný kladný mimodiagonální
prvek nemůže zmizet. Opakování stavu je tedy nemožné. Tištěný argument
je správný, když se doplní tento konečnostní krok.

Při povolení i záporné rovnosti může cyklus vzniknout. Báze s řádky
(1,-1,0),(0,1,-1),(1,1,1) a symetrickým zaokrouhlením půlek od nuly
se po18 krocích indexu j vrací do stejného stavu. V JSON je všech12
provedených transformací. Kladné půlky samotné v tomto příkladu žádnou
transformaci neprovedou a kontrola končí. Příklad ilustruje varování;
obecný důkaz výše není odvozen pouze z testu.

## 5. Skutečná multiplikativní orbita: úloha20 a C0046

Orbita je množina stavů X_n=a^n*X_0 modulo m v jedné periodě.
Zde m=2^e, e>=3, X_0 liché a a=3 nebo5 modulo8. Její délka je m/4.
Pro a=5 modulo8 obsahuje celou jednu zbytkovou třídu modulo4. Se
seedovou třídou tau=X_0 mod4 a substitucí X=4Y+tau dostaneme

```
Y' = (aY + ((a-1)/4)*tau) mod(m/4).
```

Takto opravená první část odpovědi je správná. Faktor tau v přírůstku
doplňují errata25.7.2005; neposuzujeme jeho původní vynechání jako nový nález.

**C0046:** pro a=3 modulo8 nelze stejným způsobem použít jedinou
posunutou mříž modulo m/4. Stavy střídají dvě třídy modulo4. Změna
znamének střídavých souřadnic v každém bodě toto střídání počátečního
stavu mezi body neodstraní. Nejkratší konkrétní doklad používá
m=16,a=3,X_0=1, orbitu1,3,9,11 a body

```
(1,3)/16, (3,9)/16, (9,11)/16, (11,1)/16.
```

Rozdíly od prvního bodu jsou p=(1,3)/8, q=(1,1)/2, r=(5,-1)/8.
Platí q-4p=(0,-1), 8p-3(0,1)=(1,0), r=5p-2(0,1). Jejich celočíselný
obal tedy obsahuje Z^2 a je generován p a (0,1). Normálový vektor
rodiny stejně vzdálených přímek proto musí být celočíselný a splňovat
u+3v=0 modulo8. Nejkratší nenulový vektor je ±(2,2), čtverec délky8.
Všechny možné čtverce menší než8 (1,2,4,5) lze vyloučit přímým dosazením.
Největší rozestup je tudíž1/sqrt(8). Návod s m/4=4 dává ±(1,1),
čtverec2 a chybný rozestup1/sqrt(2). Argument nepotřebuje konvenci
o přidávání celočíselných posunů, neboť ty již leží v obalu rozdílů.

Po reflexi druhé souřadnice vzniknou body
(1,13),(3,7),(9,5),(11,15), dělené16. Náhradní generátor sigma(y)=y-1
modulo4 a konstantní posun(1,1)/16 by místo nich dal
(1,13),(5,1),(9,5),(13,9), dělené16. Oprava2005, která přidává tau
i zde, se pro tau=1 nijak neprojeví a závadu neřeší.

Obecně označme D=gcd(m,{x-X_0: x v orbitě}). První nenulový rozdíl
je (a-1)X_0 modulo m a všechny další jsou jeho násobky; proto
D=gcd(m,a-1). Celočíselná normála u má na celé orbitě konstantní fázi
u·P modulo1 právě tehdy, když

```
sum_(j=0)^(t-1) u_(j+1)*a^j = 0 modulo(m/D).
```

Pro typ5 je D=4, pro typ3 D=2. Toto je přesná charakterizace afinního
mřížového obalu skutečné orbity s celočíselnými posuny; netvrdí, že
orbita typu3 zaplní všechny jeho body v jednotkové krychli. Přímá
kontrola120 orbit a18000 normál v malých dimenzích s ní souhlasí.

**RANDU se číselně nemění.** Jeho tabulková minima pro modulus2^29
mají v každé dimenzi2–9 minimalizátor splňující také silnější kongruenci
modulo2^30. Silnější mříž je podmnožinou slabší, takže stejné horní
a dolní meze dokazují rovnost minim. Svědci jsou uloženi v JSON.

Pro vymezení konvencí byly přečteny §2 a7 článku
[Steele–Vigna](https://arxiv.org/abs/2001.05304), včetně obrazů stran3,14.
Článek zavádí i spektrální veličiny pro všechny počáteční stavy a
rozlišuje orbity typu3 a5; pro vyhledávání multiplikativních generátorů
pak používá typ5. Není to nezávislé potvrzení opravy m/2. Náš nález
se opírá o výše uvedené konkrétní body a doslovné tvrzení odpovědi20
o vzdálenosti rovin pokrývajících skutečnou periodu.

## 6. Vynechávání každého druhého člena čtveřice: úloha21 a C0048

Položme d=gcd(4,m). Má-li generátor plnou periodu m=2^e, podposloupnost
X_(4n) má m/d různých stavů ve třídě X_0 modulo d. Iterace o čtyři
kroky tuto třídu zachovává; uvedený počet plyne z jediné plné periody.
Každý další stav ve třídě změní vybranou trojici modulo1 o násobek
d*(1,a^2,a^3)/m. Konstantní posun pochází ze seedu a přírůstku c:

```
(X_0*(1,a^2,a^3) + c*(0,a+1,a^2+a+1))/m.
```

První bázový vektor tedy je d*(1,a^2,a^3)/m, další dva jsou jednotkové
vektory druhé a třetí souřadnice. Pro e>=2 je d=4 a odpověď správná.
**C0048 je pouze opomenutá malá hranice e=1.** Pro m2,a1,c1,X_0=0
je vybraná trojice stále(0,0,1/2). Její periodické kopie tvoří posun Z^3.
Vytištěná báze má první řádek(2,2,2), determinant2 a neobsahuje(1,0,0).
Správný první řádek je(1,1,1), determinant1. Stačí dodat e>=2 nebo
nahradit4 hodnotou gcd(4,m). Číslo252 přesných modelů v JSON zahrnuje
tuto hranici. Hlavní použití pro velké moduly není zpochybněno.

## 7. Rekurence druhého řádu: úloha24

Pro prvočíslo p a periodu p^2-1 prochází dvojice stavů všemi nenulovými
vektory nad tělesem F_p, tedy aritmetikou modulo p. Každá další složka
je lineární kombinací prvních dvou. Doplňme nulový počáteční stav;
ten nemění příslušné rodiny afinních rovin. Lineární funkce konstantní
na všech nenulových stavech musí mít hodnotu0: pro p>2 porovnáme v a2v;
pro p=2 porovnáme v,w,v+w pro nezávislé v,w.

Matice R uchovává koeficienty dvou posledních členů vzhledem k prvním
dvěma a aktualizuje se R<-R*((0,b),(1,a)) modulo p. Poslední sloupec
(f,g) určuje nový člen. Duální mříž má dvě nezávislé kongruence;
v dimenzi4 přesně u_1+b*u_3+ab*u_4=0 a
u_2+a*u_3+(a^2+b)*u_4=0 modulo p, jak je vytištěno.

Inicializace U=pI_2,V=I_2,R=I_2 zachovává škálovanou dualitu UV^T=pI
a dává nu_2=p. Rozšíření o řádek(-f,-g,0,...,1) zachová obě kongruence.
Nová poslední složka V_i je V_i1*f+V_i2*g; po odečtení q*p z ní musíme
přičíst q*U_i k novému řádku U_t. Přesně to dělá S4'. Nový řádek V_t
je p krát poslední jednotkový vektor. Dualita a determinant mříže p^2
tak zůstávají správné, redukce a konečný soupis S5–S10 se nemění.
Všechny indexy a matice byly ověřeny v původním obrazu582.

Doslovná modifikace S4' souhlasí s nezávislou racionální sférou pro
všech31 primitivních rekurencí nad p2,3,5,7,11 a124 minim v dimenzích2–5.
Samostatné počáteční stavy(1,0),(0,1) kontrolují obě duální kongruence.
Velký vytištěný příklad už byl ověřen v tabulce; nebyl znovu počítán.

## 8. Errata a stav dokladů

Čtyři vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální TeX
prohledány1.11.2026 podle stran116–117,581–582, čísel odpovědí16–24
a výrazů S7, combinatorial, exactly one, hyperplane, non-shortening.
Relevantní oprava20 z25.7.2005 je zapracována výše; oprava26 z6.2.2005
patří do následujícího bloku. Žádná nalezená položka neopravuje C0044–48.
První pětice výpočetních bloků skončila s exit0, session50114.
Dodatečný blok `output_and_boundary` doběhl zvlášť s `--resume` a exit0;
úspěšné bloky se neopakovaly. Zdroj Steele–Vigna a rozsah čtení mají
metadata v `sources/steele-vigna-2022.json`.

Nálezy C0044–48 jsou potvrzené vůči našim zdrojům, s anglickými
neodeslanými návrhy v `reports/`. Nejnovější fyzický dotisk, prvenství
ani nárok na odměnu nejsou ověřeny.

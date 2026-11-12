# §4.6.3: úplný rozbor věty C a úlohy 14

Věta C je správná po známé opravě exponentu na 470 z roku 1998.
Níže rozepisujeme konečné případy, které kniha ponechává čtenáři.
Nejde o nový nález. Obecný důkaz doplňuje nezávislá konečná enumerace
v `results/powers-structure.json`, blok `two_small`.

## 1. Značení a výchozí fakta

Pro kladné celé a je lambda(a)=floor(log2 a) a nu(a) počet jedniček.
Sčítací řetězec 1=a_0<...<a_r má každý další člen součtem dvou dřívějších.
Malý krok nezvyšuje lambda; ostatním zde říkáme velké. Hvězdový krok
používá bezprostředně předchozí člen. Každý krok zvýší lambda o 0 nebo 1,
takže r=lambda(a_r)+s, kde s je počet malých kroků.

Používáme dokázanou klasifikaci jednoho malého kroku z
[poznámky o struktuře, §2](powers-structure.md#2-obecný-důkaz-šesti-typů-b).
Takový řetězec má jen jedno- nebo dvojbitové členy. Jeho dvojbitové členy
se vyskytují pouze v těchto třech rodinách; v zápisech jsou uvedeny jejich
chronologické pořadí a parametry, nikoli případné závěrečné čisté mocniny:

| Rodina | Dvojbitové členy |
|---|---|
| I (typ 1) | U,2U,...,2^C U, kde U=2^A+2^B, A>B>=0, C>=0 |
| II (typ 2) | U,V,2V,...,2^C V, kde U=2^A+2^B, V=2^(A+1)+2^B |
| III (typ 5) | 3*2^(A-1),...,3*2^(A+C-1), poté V,...,2^D V; V=9*2^(A+C-2), A,C>=1, D>=0 |

Typy 3,4,6 končí čistou mocninou dvou, a před ní mají jen úvodní části
těchto rodin. Pro dva sčítance u,v platí
nu(u+v)=nu(u)+nu(v)-c, kde c je celkový počet binárních přenosů, včetně
každé pozice při řetězovém přenosu. Každý přenos nahradí dvě jedničky jednou.

Čtyřbitové číslo s pozicemi A>B>C>D>=0 nazveme speciální, jestliže platí
alespoň jedna z podmínek:

1. A-B=C-D;
2. A-B=C-D+1;
3. A-B=3 a C-D=1;
4. A-B=5 a B-C=C-D=1.

Podle konstrukcí úlohy 13 má speciální číslo řetězec délky A+2.
Klasifikace jediného malého kroku dává současně dolní mez A+2 pro každé
číslo s alespoň třemi jedničkami. Stačí tedy dokázat, že řetězec se dvěma
malými kroky nemůže končit nespeciálním číslem s alespoň čtyřmi jedničkami.

## 2. Druhý malý krok na konci

Připojme k jednosmall řetězci končícímu P malý krok Y. Má-li nu(Y)>=4,
musí mít oba sčítanci dva bity, bez jediného přenosu, takže nu(Y)=4.
Krok musí být hvězdový: jinak lze P vypustit a získat jednosmall řetězec
pro Y, což odporuje jeho čtyřem bitům. Proto Y=P+T s dřívějším T.

V rodině I jde o dvě škálované kopie U. Jejich disjunktní dvojice bitů
tvoří obdélník součtů dvou dvojic exponentů; po seřazení mají krajní
mezery stejnou velikost. Dostáváme případ 1.
V rodině II platí totéž pro dvě kopie V. Pro P=2^C V a T=U mají dvě
krajní mezery rozdíl 1, ať je větší prostřední bit A nebo B+C; jde o
případ 2. Shoda prostředních bitů by byla přenosem a je vyloučena.

V rodině III dávají dvě kopie V opět případ 1. Jinak pišme
P=9*2^h a T=3*2^j. Z časového pořadí plyne j<=h+1.
Při j<=h-2 jsou horní mezera 3 a dolní 1: případ 3.
Pro j=h-1 nebo h se bity překrývají. Pro j=h+1 dostáváme 15*2^h,
tedy čtyři sousední bity a případ 1. Závěrečný malý krok je tím vyřízen.

## 3. Minimální hypotetický protipříklad a úloha 14(a)

Předpokládejme nejkratší protipříklad délky r. Každý jeho kratší prefix
má nejvýše čtyři jedničky a při čtyřech je speciální. Poslední krok není
malý podle §2. Není zdvojením, neboť odstranění zdvojení zachovává počet
malých kroků, počet bitů a nespeciálnost. Je hvězdový: jinak vypuštění
předposledního členu dá jen jeden malý krok pro stejný konec.

Pišme n=y+z, y=a_(r-1), x=a_(r-2), z=a_(r-k), k>=2, a m=lambda(y).
Pak lambda(n)=m+1 a r=m+3.

Kdyby r-1 i r-2 byly malé, krok r-2 by byl první malý krok po čistých
mocninách dvou. y by měl nejvýše tři jedničky. Při jednobitovém z má
velký součet nejvýše tři bity. Jediná dvojbitová možnost z je a_(r-2).
Aby y+z mělo čtyři bity, muselo by y mít tři a vzniknout jen jeden
přenos. Ale tehdy y obsahuje oba bity z, a přenosy jsou alespoň dva.
Poslední dva kroky před n tedy nemohou být oba malé.

Předpokládejme nyní r-1 malý a r-2 velký. Je-li c=1, musí mít z
nejvyšší bit ve stejné pozici jako y, tedy z=x. Z nu(n)>=4 plyne
nu(y)>=3; y musí být hvězdový, jinak jeho kratší řetězec po vypuštění x
má jediný malý krok. Pišme y=x+w. Nahrazení y hodnotou 2x je platné
a zachová konec n=2x+w. Poslední krok je nyní malý, v rozporu s §2.

Je-li c>=2, pak všechny členy před y mají nejvýše dva bity a samotné y
nejvýše čtyři. Rovnost počtů bitů vynucuje
nu(y)=nu(n)=4, nu(z)=2 a c=2. Druhý malý krok y=P+T je opět součtem
disjunktních dvojic z některé rodiny v §1. Případy pro poslední sčítanec z
lze rozepsat takto:

| Rodina prefixu P | Možnosti se dvěma přenosy a čtyřbitovým výsledkem |
|---|---|
| I | z=P dává případ 1; z=P/2 je možný jen při sousedních bitech U a dává případ 3 |
| II | dvě kopie V dávají případ 1; T=U,z=P dává případ 2 |
| III | dvě kopie V dávají případ 1; T je stará sousední dvojice a z=P dává případ 3 |

Pro úplnost, proč jiné řádky nejsou skryté: při z<P musí pro přesně dva
přenosy ležet jeho nejvyšší bit jen o jednu pozici pod nejvyšším bitem y.
V rodině I je proto z=P/2. Pokud horní sousední bit y pochází z T=z,
vznikne přenos i u dolního bitu T, tedy alespoň třetí. Zbývá sousední
horní dvojice P, která dá případ 3. V rodině II není V sousední dvojice;
z=U může být dost vysoké jen při C=0, ale pak P a T nemají disjunktní bity.
V rodině III může staré z dosáhnout potřebné výšky jen jako 6*2^h při
P=9*2^h; pak T=z a součet 15*2^h+6*2^h má tři přenosy. To uzavírá tabulku.
Všechny zbývající výsledky jsou speciální, tedy r-1 není malý.

## 4. Hvězdovost y a vyloučení škálovaného sčítance

Oba poslední kroky jsou velké. Proto c>=2; při c=2 navíc
y>=2^m+2^(m-1), neboť jediné dva přenosy musí projít pozicemi m-1 a m.
Kdyby y nebylo hvězdové, x by bylo malé a vypuštění x dává pro y
jednosmall řetězec. Tedy nu(y)<=2, a poslední součet vynucuje
z=x, nu(x)=4 a c=2. Musí y=3*2^(m-1). Prefix končící a_(r-3) má
jeden malý krok a k dosažení y potřebuje alespoň y/2; maximální
dvojbitová hodnota s jeho nejvyšším bitem je právě 3*2^(m-2).
Je tedy typu 1 a x=3*2^(m-2)+3*2^d. Potom n=9*2^(m-2)+3*2^d
je případ 3. y proto musí být hvězdové.

Uvažujme y=2^t z. Protože c>=2 a nu(n)>=4, je nu(z)>=3.
Oba malé kroky tedy nastaly již nejpozději u z. Všechny kroky od z do y
jsou velké a rovnost y=2^t z vynucuje, že jde právě o t zdvojení;
t=k-1. Je-li nu(z)=3, pak c=2, takže t=1. Dva přenosy nutné k růstu
nejvyššího bitu vyžadují z=2^A+2^(A-1)+2^C s C<=A-3.
Výsledek 3z je případ 3.

Je-li nu(z)=4, je z speciální. Jelikož žádné čtyřbitové z s vedoucím
bitem A nepřesahuje 15*2^(A-3), podmínka
z/2^A >= 2/(1+2^-t) dává t<=3. Tato nerovnost a čtyři speciální vzory
dávají následující úplný seznam, až na společné násobení mocninou dvou:

| t | z | (2^t+1)z |
|---|---|---|
| 3 | 15 | 135, případ 4 |
| 2 | 15 nebo 27 | 75 (případ 3) nebo 135 (případ 4) |
| 1 | 45, 23, 43 | 135 (případ 4), 69 (tři bity), 129 (dva bity) |
| 1 | 3*(2^j+1), j>=2 | 9*(2^j+1): případ 1, kromě j=3, kdy má tři bity |

Úplnost: při t=3 musí být horní tři bity sousední; speciálnost dovolí
jen 15. Při t=2 musí být horní dvojice sousední, takže jde o případ 1,
a mez dovolí dolní dvojici jen v polohách dávajících 15 nebo 27.
Při t=1 je horní mezera nejvýše 2. Mezera 1 dává poslední řádek;
mezera 2 dovolí z případu 1 pouze 45 a z případu 2 pouze 23 nebo 43.
Proto můžeme v protipříkladu škálovaný sčítanec vyloučit.

Pokud k=2, pišme y=x+w. w!=x díky právě provedené redukci.
Nahradíme y hodnotou 2x a poslední krok zapíšeme n=2x+w.
Řetězec zůstává rostoucí, oba poslední kroky velké a nyní k>2.
Kdyby se objevila škálovaná dvojice, použije se už uzavřený rozbor výše.

## 5. Úloha 14(b): nižší nejvyšší bit z

Předpokládejme lambda(z)<m-1. Přenos do nového nejvyššího bitu vyžaduje
c>=3. Proto nu(y)+nu(z)>=7 a oba sčítanci mají alespoň tři bity.
Oba malé kroky leží nejpozději u z, takže lambda(z)=m-k+1.
Přenosy od této pozice do m dávají c>=k. Pro k>=4 tak musí
k=c=4 a nu(y)=nu(z)=4. Nutně y=15*2^(m-3).
Z y<=8z a maximální čtyřbitové hodnoty s lambda(z)=m-3 vyjde y=8z,
což bylo v §4 vyloučeno.

Zbývá k=3. Máme lambda(x)=m-1, lambda(z)=m-2 a y>=3*2^(m-1).
Proto y=2x: jiný hvězdový krok má x+z<3*2^(m-1).
x není zdvojení z podle §4. Také x musí být hvězdové, jinak lze z
vypustit a získat jednosmall řetězec pro x s nu(x)=nu(y)>=3.
Jiný sčítanec než p=a_(r-4) je nejvýše a_(r-5)<=2^(m-2), což spolu
se z<2^(m-1) nestačí k x>=3*2^(m-2). Tedy x=z+p.

Nutně lambda(p)=m-2: s nižším bitem by z+p opět nedosáhlo potřebné meze.
p má právě jeden malý krok. Také z musí být hvězdové: vypuštění p by
jinak dalo jednosmall řetězec pro z s alespoň třemi bity. Proto z=p+v
je druhý malý krok. Jednobitové p by dalo x=2p+v<3p, takže p má dva bity.
Zaveďme L=m-2 a pišme p=2^L+2^(L-delta). Podmínky jsou
v>=2^L-2^(L-delta+1) a v<2^L-2^(L-delta).
Pro delta>=2 dávají rodiny §1 jen následující možnosti; u v tabulce
označuje společný kladný faktor, který je mocninou dvou:

| Možnost | Důvod vyloučení |
|---|---|
| delta=2, v=2^(L-1) | p=5u,v=2u; x=12u má jen dva bity |
| delta=2, v=p/2 | p=10u,v=5u; z=15u,y=50u,n=65u má jen dva bity |
| rodina II, C=0, delta=2, v=U | p=5u,v=3u; z=8u není malý krok |
| rodina III, bez zdvojení za V, v je největší stará dvojice | p=9u,v=6u; x=24u má dva bity |

Proč je seznam úplný: kromě původního U v rodině II a starých sousedních
dvojic v rodině III jsou starší hodnoty nejvýše p/2 nebo čistá mocnina
2^(L-1). Při delta>=3 nedosahují dolní meze pro v. Pro delta=2 zbývají
právě první dva řádky. Původní U dosáhne meze jen při C=0,delta=2.
V rodině III je delta=3 a největší stará dvojice dosáhne meze jen bez
závěrečného zdvojení, jako 6u při p=9u.

Zbývá delta=1, tedy p=3*2^(m-3), což je nutně rodina I.
Jednobitový v dává nu(z)+nu(y)<=6, a proto nestačí. Dvojbitový v má tvar
3*2^d, d<=m-5 (větší by ze z udělal velký krok).
Pak n=15*2^(m-3)+9*2^d. Pro h=m-3-d>=2 máme n/2^d=15*2^h+9.
Pro h=2 jde o 69 se třemi bity, pro h=3 o 129 se dvěma; pro h>=4
se nezvýší nejvyšší bit. To uzavírá úlohu 14(b).

## 6. Poslední větev hlavního důkazu

Nyní lambda(z)=m-1 a k>=3. Počet malých kroků před z je 4-k, takže
k<=4. Pro k=4 je z čistá mocnina dvou a nu(y)+nu(z)-c<=3.
Pro k=3 má z jeden malý krok, x je druhý malý krok a oba poslední kroky
jsou velké. Musí nu(z)=2,nu(y)=nu(n)=4,c=2 a y>=3*2^(m-1).
Je-li y zdvojení x, je nu(x)=4. Jinak y=x+w,w<=z a při této velikosti
vzniknou alespoň dva přenosy, takže rovněž nu(x)=4.

x je speciální, lambda(x)=m-1 a x>=y/2>=3*2^(m-2).
Musí mít sousední horní dvojici, a tedy být případem 1:
x=3H+3u, kde H=2^(m-2), u=2^d<=H/4.
Rozklady x=z+v ze skutečného jednosmall prefixu jsou podle §1–2 přesně:

| Větev | z | v |
|---|---|---|
| a | 3H | 3u |
| b | 2H+2u | H+u |
| c, pouze H=4u | 9u | 6u |

Rodina II by měla nestejné krajní mezery, proto nevystupuje. První dvě
možnosti odpovídají dvěma uspořádáním obdélníku bitů v rodině I.
Rodina III dává stejnou krajní mezeru jen při čtyřech sousedních bitech,
tedy třetí možnost.

Není-li y zdvojení x, vyžaduje y>=6H sčítanec w>=3H-3u.
Ve větvi a musí w=z; každý další starší člen je nejvýše 2H.
Dostáváme n=9H+3u, případ 3. Ve větvi b je dosažení meze možné jen při
H=4u a w=z, ale pak y=25u má tři bity. Ve větvi c může být pouze
w=z, ale y=24u má dva bity.

Při y=2x dává větev a n=9H+6u: buď případ 3, nebo při H=4u jen tři bity.
Větev b dává n=4z se dvěma bity. Větev c dává n=39u, případ 3.
Všechny možnosti pro nejkratší protipříklad byly vyloučeny. Věta C
i obě části úlohy 14 jsou tím dokázány.

## 7. Jemnost knižního zkrácení a kontrolní rozsah

Knižní formulace na 470, že v závěru musí a_(r-3)=3*2^(m-2), nerozepisuje
větev c. Konkrétní řetězec 1,2,3,6,9,15,30,39 má a_(r-3)=9, nikoli 12.
Není protipříkladem věty ani celé hypotézy důkazu: 39 je speciální.
V §6 jsme tuto větev výslovně uzavřeli. Z tohoto místa tedy nevyvozujeme
nový potvrzený nález ani chybu matematického výsledku.

Program generuje všechny rostoucí řetězce do délky 13 s nejvýše dvěma
malými kroky, nezávisle na uvedených rodinách. Kontroluje C, Fibonacciho
mez A, korolár i vztahy hvězdových kroků a shromažďuje doplňkovou větev
39*2^d. Neprohlašujeme tuto konečnou enumeraci za obecný důkaz; tím jsou
předchozí oddíly. Starší tři úspěšné bloky se při doplnění neopakovaly.

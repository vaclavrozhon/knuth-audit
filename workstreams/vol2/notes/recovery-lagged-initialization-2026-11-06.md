# Obnova §3.6: ran_array, ran_start a celá úloha9

Rozsah: hlavní186/file198 od lagged-Fibonacci odstavce, celá187 a188
po kontrolní výstup; zadání9 na193 a odpověď599–600. Originály186,
187,188,193,599,600 a náhradní kód `all2-prepre` str.11 přečteny
vizuálně. Celý `summary-generators.md` a uložený autorův `knuth-rng.c`
přečteny. Staré numerické certifikáty se **nespouštěly**. Tento blok
neuzavírá empirická doporučení ani neprohlašuje všechna zobecnění
parametrů za vlastnosti vytištěného programu.

## Generování a přesný stav

Označme K=100,L=37,M=2^30. Před voláním je `ran_x[i]=X_(r+i)` pro
0≤i<K. Požadujeme n≥K, platné samostatné výstupní pole o n prvcích a
takové n, aby i závěrečný index j=n+K byl reprezentovatelný jako int.
Pole nesmí přepisovat dosud potřebný `ran_x`; běžný samostatný výstupní
buffer tuto podmínku splňuje. Požadavky na paměť a indexy jsou součástí
domény C volání, nikoli záruka pro libovolný integer n.

První smyčka kopíruje X_r až X_(r+K−1). Ve druhé jsou oba indexy
j−K,j−L nezáporné a menší než j; indukce tedy dává správné X_(r+j).
Po ní je j=n. Ve třetí smyčce i<L leží n+i−K i n+i−L v[0,n), takže
oba předchůdci leží v hotovém `aa`. Ve čtvrté i≥L je druhý
předchůdce `ran_x[i−L]` již vypočten, zatímco n+i−K stále leží v aa.
Nový stav je tedy přesně X_(r+n),…,X_(r+n+K−1). Pro n=K druhá
smyčka vynechá tělo; oba závěrečné argumenty zůstávají platné.

Předpočítání K stavových prvků neposouvá výstup o dalších K.
Jedno volání posune stav o n; rozdělení celkového výstupu do bloků
délky alespoň K dává tutéž posloupnost i konečný stav. Kopie celého
`ran_x` proto stačí k pozdějšímu opakování dalších volání `ran_array`.
Případný zásobníkový obal z15 má navíc vlastní ukazatel a buffer;
zde se tvrzení vztahuje právě na vytištěné přímé rozhraní.

Počet kopií/rekurencí je K+(n−K)+K=n+K, tedy Θ(n) pro n≥K; stav
zabírá K slov a výstup n. Rozdíl dvou hodnot v[0,M) leží v(−M,M),
takže 32bitový signed long nepřeteče. Na dvoukomplementovém stroji
`d&(M−1)` vybírá nejnižších30 bitů, tj. zbytek d modulo M i pro d<0.
Makro nemá vedlejší účinky v dodaných argumentech. Obecná historická
přenosnost na jinou reprezentaci záporných čísel se netvrdí.

## Inicializace: každá operace a ukončení

Doména je 0≤s≤M−3, tedy M−2=1073741822 možností. `evenize(s+2)`
leží mezi2 a M−2. Je-li ss=2u, pak 1≤u≤2^29−1. Zdvojení ss a
případné odečtení M−2 odpovídá cyklickému posunu29 bitů u: nejvyšší
bit je přenesen na nejnižší místo. I slovo samých jedniček se zachová.
Největší mezihodnota je2M−4<2^31. Každý ze100 počátečních x[j] je
sudý v[2,M−2]; vysoké pozice100..198 se v původní verzi nulují.
`x[1]++` nevystoupí z[0,M) a právě x[1] je liché. Paritní polynom
p(z)=sum x[j]z^j je proto z.

Při „square“ se postupuje od j=99 dolů: zápis x[2j]=x[j] nezničí
dosud potřebný zdroj, který má menší index. x[0] zůstává. Následující
smyčka přiřadí sudé hodnoty na liché pozice1,3,…,135. Zbývající liché
pozice137,…,197 byly nulové a zůstávají sudé: redukce míří nejvýše na
135 a98 a násobení z nejvýše na100. Modulo2 tudíž opravdu vznikne
p(z²)=p(z)². **Není** to identita druhé mocniny polynomu nad Z/MZ.

Sestupná redukce pro j=198,…,100 při lichém x[j] odečte x[j] od
koeficientů j−63 a j−100. Modulo2 nahrazuje z^j součtem
z^(j−63)+z^(j−100), tedy užívá z^100=z^37+1. Oba cíle jsou nižší než j
a nezáporné. Vysoký x[j] se nemusí nulovat: v tomto průchodu už není
potřebný jako zdroj vyššího stupně a další „square“ přepíše všechny
relevantní sudé pozice a parity lichých. Nízkých100 koeficientů je
správný zbytek.

Je-li ss liché, sestupný posun x[j]=x[j−1] pro100≥j≥1 násobí z;
x[100] je přebytečný koeficient. Přiřazení x[0]=x[100] a odčítání
u x[37] právě zavede z^100=z^37+1 modulo2. Je-li přebytečný koeficient
sudý, jeho nenulová celočíselná velikost nemění tuto paritní identitu.
Všechny redukční operace zachovávají celočíselný rozsah[0,M).

Pro kladný s s bitovou délkou b zpracuje smyčka právě b bitů od
nejnižšího; po každém `ss>>=1`. Poté provede69 samotných druhých
mocnin, protože t začíná69 a klesá jen při ss=0. Pro s=0 provede
právě69 iterací. Celkem nejvýše99 iterací, každá O(K), pomocná paměť
2K−1. V obecném zápisu s TT≥2 je cena O(K(e+TT)) a indexy všech
smyček leží v alokovaném poli. Podmínka TT≥2 je pro tuto přesnou
implementaci důležitá, viz níže.

Začneme exponentem1 a za zpracovaný bit b přejdeme e↦2e+b. Pro
s=(1 s_j…s_0)_2>0 tedy před posledními69 nulovými kroky vznikne
(1 s_0…s_j1)_2. Definujme

```
H(0)=2^69,
H(s)=(1 s_0…s_j1)_2 · 2^69  pro s>0.
```

Závěrečné dvě smyčky mapují koeficient x[j] na pozici j+63 pro j<37
a j−37 jinak. V zadání P_0 má X_i exponent(i+37)mod100, tedy tato
rotace přesně vytvoří P_0=z^H(s).

## Úloha9(a,b): celý tištěný polynomový výpočet

Primitivita f=z^100+z^37+1 a řád z rovný Q=2^100−1 mají archivní
přesný certifikát `results/binary-polynomials.json`; důkaz pomocí
ireducibility a mocnin pro prvočinitele Q je převzat ze
`primitive-polynomials.md`, nyní znovu přečtené celé. V tělese
GF(2)[z]/f je nenulové p=z i jeho
další mocniny nenulové; proto žádný inicializovaný paritní stav není
nulový a exponent je jednoznačný modulo Q.

Doslovné posunutí a odečtení definice P_n dává, ještě před redukcí,

```
z P_(n+1) = P_n − X_n z^37 − X_(n+63)
                 + X_(n+63)z^100 + X_(n+100)z^37.
```

Dosazením X_(n+100)=X_n−X_(n+63) modulo2 dostaneme přesně
`P_n + X_(n+63)(z^100+z^37+1)`. Redukce f dá zP_(n+1)=P_n a
indukcí P_n=z^(H(s)−n). Tím jsou porovnány oba tištěné mezikroky,
nejen finální mocnina. Vzorec pro kladný seed je tištěné9(b); nulu,
která nemá zápis s úvodní1, pokrývá samostatně H(0).

## Úloha9(c): kruhová mez a hranice zobecnění

Celý důkaz a konkrétní rozpor C0071 z `summary-generators.md`§2 se
přebírá, včetně originálu600 a všech čtyř vrstev errat. Shoda bloků
dává pouze n−n′≡H(s)−H(s′)modQ. Pro s=0,s′=2^29,n=2^99−1,n′=0
platí tato kongruence, ale běžná vzdálenost je o1 menší než rozdíl H.
Tištěný mezikrok je chybný; hlavní mez správná.

Pro B=2^69 jsou hodnoty H různé liché násobky B mezi B a
(2^31−1)B. Jednoznačnost plyne ze čtení obráceného binárního zápisu:
vnější1 a délka určují všechny původní bity, s=0 dává samostatný
jednociferný násobek1. Vnitřní rozdíly jsou alespoň2B. Přes konec
kruhu je mezera Q−[(2^31−1)B−B]=2B−1. Vzdálenost n−n′ je alespoň
minimum těchto dvou kruhových vzdáleností. Rovnost2B−1 vyžaduje oba
krajní seedy0 a2^30−1; druhý není v původní doméně. Pro původní
doménu je tudíž dolní mez alespoň2B=2^70, což implikuje zadání9(c).

Abstraktní zobecnění: při primitivním z^k+z^l+1, k>l, semenech
0≤s<2^e, t≥1 a t+e≤k definujme H stejně s B=2^(t−1). Vnitřní
rozestupy jsou≥2B a mezera přes konec je
2^k−1−(2^(e+1)−2)B≥2B−1. Rovnost poslední meze vyžaduje t+e=k
a krajní seedy0,2^e−1. Tím je matematické tvrzení o těchto H uzavřeno.
Primitivita je nutný kontext použití Q=2^k−1; samotné k>l nestačí.

**Kontextová partial pro zobecněný kód:** mechanická změna TT na1
nastaví t=0 a tělo `while(t)` vůbec neproběhne. Všechny seedy pak
mají stejný paritní polynom z. Například k=3,l=1,e=2,t=1,
s=0 a1 jsou v bezpečné původní doméně M=4 a f=z³+z+1 je primitivní
(nemá kořen0 ani1, tedy je ireducibilní; z≠1 má řád7),
ale n=n′=0 dává shodné bloky a poruší požadovanou mez1. To není
rozpor s abstraktní konstrukcí H: ta skutečně zpracuje bity seedu.
Tištěný obecný odstavec lze číst jako zobecnění konstrukce, proto
nejde o nový confirmed. Při použití **tohoto** kódu je třeba TT≥2,
nebo změnit podmínku na `while(ss || t)`. Konkrétní TT70 je v pořádku.
Staré blanketové zobecnění v naší poznámce je proto upřesněno.

## Výkladové důsledky a verze2002

Když 0≤n,n′<2^70, je |n−n′|<2^70. Dva různé původní seedy proto
nemohou dát stejný blok100 ani v paritě, tím méně v celých hodnotách.
To je přesný význam použité nezávislosti; není to důkaz statistické
nezávislosti dvou náhodných proudů ani záruka pro neomezeně dlouhý běh.
I366 dní má31622400·10^9<2^55 nanosekund. M−2>10^9 spočítá počet
povolených seedů, nikoli nezávislých pravděpodobnostních proměnných.
Známá oprava2001 upravuje formulaci „disjoint sets“; není nový nález.

Náhrada lagů z tabulky3.2.2–1 zachová primitivní binární polynom,
což mají všechna tabulková políčka v archivním certifikátu. Stejná
kvantitativní záruka navíc vyžaduje t+e≤k. Menší k=55 či89 se
samotnou náhradou100 a37 tuto podmínku pro70+30 nesplní. Doporučení
nelze číst jako bezpodmínečnou záruku stejného počtu oddělených proudů;
tento rozsah zůstává explicitně partial. Vyšší bity inicializace
a „probably good“ pro t≤100 jsou kvalitativní/heuristické, ne důsledek
paritního důkazu. Srovnání rychlosti platí jako historické hodnocení,
nikoli benchmark nynějších počítačů. Úspora volání při větším n je
viditelná v ceně n+K, ale neprokazuje každé výkonnostní srovnání.

Náhradní kód2002 zapisuje x[2j]=x[j],x[2j−1]=0 pro j=99..1;
všechny vysoké koeficienty jsou tím před čtením definovány, proto lze
odstranit původní úvodní nulovací smyčku. Redukce i oprava x[37] jsou
nepodmíněné. Modulo2 jde o stejné operace, ve vyšších bitech o jinou
posloupnost. Deset následných `ran_array(x,199)` posune stav o1990.
Správný exponent je H(s)−1990modQ; celý již potvrzený C0072 se
přebírá, neodvozuje jako nový nález. Společný posun nemění žádnou
mezi-seedovou vzdálenost. Uložený celý autorův zdroj tuto verzi i
upozornění na nekompatibilitu obsahuje.

## Přenosnost a kontrolní program188

Věty o FORTRAN a zlomcích jsou odkazy na10/11; jejich celý kód bude
posouzen samostatně a zde se nepovažují za uzavřené jen na základě
odkazu. Přenosnost masky a celý rozsah signed long jsou doloženy výše.
Nutnost spolehlivě zaokrouhlené aritmetiky je ve11 součástí zadání.

Dvě kontrolní větve provedou2009·1009 a1009·2009 posunů od stejného
seedu310952. Z invariantu ran_array tedy musejí dát tentýž ran_x[0].
Pole a[2009] v obou případech stačí; loop proměnná m nepřekročí2009.
Archivní přesná reprodukce `results/summary-generators.json` dává
461390032 pro původní a995235265 pro verzi2002. Hodnoty se přebírají
bez nové kompilace či milionového běhu. Známá errata mění `main` na
int a přidávají návrat0, přidávají L k seedům a aktualizují očekávaný
výstup. Formát `%ld` odpovídá long. Ani shoda dvou větví, ani jedna
číselná hodnota nedokazují správnost programu na všech vstupech;
kniha test přiměřeně označuje jako rudimentární.

Brentův článek1992 není v tomto bloku dostupným plným originálem;
historická atribuce inspirace a tvrzení o úplné odlišnosti jeho
algoritmu jsou výslovně **skip bibliography**. Žádný nový nález,
žádný výpočet. Další je188 od Caution,10–15 a zbývající1–7.

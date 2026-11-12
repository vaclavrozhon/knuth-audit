# §3.2.2: primitivní polynomy, tabulka zpoždění a masky

Kontrola 1. listopadu 2026. Tento blok pokrývá algebraická tvrzení
na str.29–32 a úlohy 18,19,20,22; navazuje na
[algoritmy A/M/B](other-algorithms.md) a
[zvedání period a identity 23,30–33](lagged-identities.md).
Celá §3.2.2 tím ještě není uzavřena.

Zde p označuje prvočíslo, F_p těleso zbytků modulo p a k kladný řád
rekurence. Monický polynom má vedoucí koeficient 1. Pro
f(x)=x^k-a_1 x^(k-1)-...-a_k znamená R=F_p[x]/(f) okruh zbytků
polynomů po dělení f; má p^k prvků. Primitivita znamená, že R je
těleso a zbytek x má multiplikativní řád p^k-1. Perioda je vždy
nejmenší délka opakování. Funkce phi(n) počítá čísla mezi 1 a n
nesoudělná s n.

## Kritérium na str.30

Položme r=(p^k-1)/(p-1) a c=(-1)^(k-1)a_k. Kniha požaduje:
c má řád p-1 v F_p, x^r=c v R a pro každý prvočíselný dělitel q|r
není x^(r/q) konstantní. Všechny tři podmínky jsou nutné i postačující.

Pro primitivní f je x generátorem cyklické grupy řádu p^k-1.
Jeho r-tá mocnina má řád p-1 a je normou kořene, tedy součinem
jeho k Frobeniových konjugátů x,x^p,...,x^(p^(k-1)). Součin je
(-1)^k f(0)=(-1)^(k-1)a_k. Nejmenší exponent, který dává konstantu,
je r, takže i třetí podmínka platí.

Obráceně z x^r=c!=0 plyne, že x je jednotka (má inverzi) v R.
Grupa H generovaná x obsahuje všechny nenulové konstanty, protože
c je jejich generátor. Řád x v podílové grupě H/F_p^* je právě r:
dělí r a žádný r/q jej neobsahuje. Proto |H|=r(p-1)=p^k-1.
Jde o všechny nenulové prvky R, takže jsou všechny invertibilní,
R je těleso a f primitivní. Není nutný předem přidaný test ireducibility.

Primitivních monických polynomů stupně k je phi(p^k-1)/k:
v tělese s p^k prvky je phi(p^k-1) generátorů a každý má přesně k
konjugátů. Generátor nemůže ležet ve vlastním podtělese, jehož
multiplikativní grupa by byla menší. Tím je velikost každé třídy k.

Primitivita rovněž dává jediný cyklus všech p^k-1 nenulových stavů
lineární rekurence. Posun stavu je v příslušné bázi násobení kořenem
f v R. To dokazuje periodu pro každý nenulový počáteční vektor,
nejen existenci jedné dlouhé trajektorie.

[Validátor](../verify_primitive_criteria.py) porovnal kritérium s přímými
trajektoriemi pro **2184 polynomů**, p=2,k<=8; p=3,k<=5;
p=5,k<=4; p=7,k<=3; p=11,k<=2, celkem **158349 stavů**.
Souhlasí také přesné počty phi(p^k-1)/k.
[Výsledky](../results/primitive-criteria.json). Přechodné úvody se
rozlišují od cyklů; samotná shoda eventualní délky by nestačila.

## Tabulka 1 na str.29

Všechny dvojice (l,k) byly přepsány z [originálu](../images/vol2-p029.png):
(24,55), (38,89), (37,100), (30,127), (83,258), (107,378),
(273,607), (1029,2281), (576,3217), (4187,9689), (7083,19937),
(9739,23209). Pro každou byl přesně dokázán primitivní trojčlen
x^k+x^l+1 nad F_2. Charakteristický polynom přímo z rekurence
se zpožděními l,k má prostřední exponent k-l; jde o reciproký
polynom, jehož kořeny jsou inverze, takže primitivitu zachovává.

Pro ireducibilitu se ověřilo x^(2^k)=x modulo f a
gcd(x^(2^(k/q))-x,f)=1 pro všechny prvočíselné dělitele q|k.
První identita dovoluje jen ireducibilní faktory se stupněm dělícím k;
gcd testy vyloučí každý vlastní dělitel. Jde o přesné polynomické
identity, nikoli pravděpodobnostní test.

Pro k=55,100,258,378 se navíc ověřil úplný řád M=2^k-1:
x^M=1, x^(M/q)!=1 pro každý prvočíselný faktor q|M. Rozklady byly
získány z primárních [Cunninghamových tabulek](https://homes.cerias.purdue.edu/~ssw/cun/pmain126.txt),
jejich součiny i prvočíselnost faktorů však byly ověřeny samostatně.
Pro ostatních osm k prokázal Lucasův–Lehmerův test prvočíselnost
samotného M; ireducibilní polynom stupně k pak musí mít plný řád,
protože x!=0,1 a M je prvočíslo. Standardní větu o tomto testu zde
znovu nedokazujeme; její knižní důkaz patří do auditu §4.5.4.

[binary-polynomials.json](../results/binary-polynomials.json) obsahuje
všechny zbytky, kontrolní gcd a výsledky Lucasova–Lehmerova testu.
[binary-period-factors.json](../results/binary-period-factors.json)
obsahuje přesné rozklady a **233 rekurzivních Lucasových certifikátů**,
včetně faktorů potřebných pro masky stupňů 2–64.
Samotný generátor rozkladů nerozhoduje o přijetí prvočíselnosti.

Nezávislý publikovaný seznam [R. Brenta](https://maths-people.anu.edu.au/~brent/ftp/trinom/table.txt)
potvrzuje zdejší dvojice s Mersennovými prvočíselnými exponenty.
Lokální kopie a metadata jsou v `sources/brent-trinomial-table.*`;
nejde o kontrolu úplnosti jeho mnohem většího seznamu.

Růst periody na 2^(e-1)(2^k-1) modulo 2^e plyne z důkazu
[úlohy 30](lagged-identities.md), při alespoň jednom lichém počátečním
členu. Samé sudé počáteční hodnoty mají přirozeně kratší periodu;
tato inicializační podmínka je převzata z definice generátoru.

## Úloha 18: proč 35bitová slova neprojdou testem dvojic

Maska A=5 znamená primitivní f=x^35+x²+1. Její primitivita byla
zvlášť ověřena dvěma modely, se všemi faktory 2^35-1. Z úlohy 16
plyne bitová rekurence X_n=X_(n-33)+X_(n-35) modulo 2. Označme
U_n binární zlomek tvořený bity X_(35n),...,X_(35n+34).
Potom **první** bit U_(n+1) je XOR prvního a třetího bitu U_n.
Původní odpověď říká třetí bit; to je již opraveno erratem 3.6.2001,
takže nejde o nový nález.

Dvojice (floor(8U_n),floor(8U_(n+1))) má proto jen 32 možných hodnot
ze 64. Formální lineární formy v počátečních bitech přesně ověřily
všech 32 přípustných párů. Protože gcd(35,2^35-1)=1 a binární
generátor má plný cyklus, vzorkování po 35 krocích projde všechny
nenulové stavy. Každý přípustný pár nastává 2^30krát, kromě (0,0),
který nastává 2^30-1krát kvůli vynechanému nulovému stavu. Polovina
buněk je tedy přesně prázdná i za celou periodu.

Poznámka o kratších blocích a o testu vyšších dimenzí je kvalitativní;
nevydává se za univerzální záruku statistické kvality.

## Úloha 19: 46 konkrétních dvojic koeficientů

Erratum 18.5.2016 správně odkazuje na první **dva** sloupce
[tabulky 4.5.4-2](../images/vol2-p408.png): N a odchylku delta,
tedy prvočíslo p=N-delta. První samotný sloupec N obsahuje mocniny
2 či 10, nikoli hledaná prvočísla. Z tabulky je 38 binárních a 8
desetinných hodnot, dohromady 46. Všechna p mají přesný certifikát;
pro každé celé p<n<N je uložen vlastní dělitel, takže byla ověřena
i maximalita p pod N. Zbylých devět sloupců této tabulky tím
zkontrolováno není.

Pro každé p byly nalezeny konkrétní a_1,a_2 s primitivním
f=x²-a_1x-a_2; a_1 se volí z velkých zbytků mimo ±1. Kritérium
na str.30 bylo ověřeno a nezávisle byl dokázán řád p²-1 matice
posunu T=[[0,1],[a_2,a_1]]: T^(p²-1)=I a žádná mocnina
T^((p²-1)/q) pro prvočíselný faktor q není I.
Výsledné konstanty jsou v oddílu `exercise19` [výsledku](../results/primitive-criteria.json).
Jsou to přesné odpovědi na požadavek periody, nikoli tvrzení o nejlepší
spektrální kvalitě. Ta nemá v úloze daný práh a obecný spektrální test
zůstává předmětem pozdější §3.3.4.

## Úloha 20: vyvážené masky a chyba dodatku

Pro každé 2<=k<=64 byla nalezena maska s počtem jedniček co nejbližším
k/2 mezi kladnými sudými počty. Sudost je nutná: f má navíc vedoucí
jedničku, takže pro ireducibilní f stupně >1 musí být f(1)=1.
Každá ze **63 masek** má přesně ověřený řád 2^k-1 dvěma modely,
bitovou aritmetikou a explicitní konvolucí koeficientů s dělením.
Čísla jsou v oddílu `masks` [výsledku](../results/binary-polynomials.json).

Publikovaná doplňující odpověď z 5.9.2013 však doporučuje masku z
bitů pi, která má lichých 27 jedniček. [C0011](C0011-pi-feedback-mask.md)
dokládá nenulový pevný stav a opravu jediného bitu. Původní selhání
validátoru je zachováno v logu; úspěšná kontrola pokračování není
zaměněna za potvrzení chybné konstanty.

## Úloha 22: součin různých prvočísel

Pro m=p_1...p_t zvolme primitivní polynom stupně k modulo každé p_i.
Čínská věta o zbytcích dává jediné koeficienty a_j modulo m se všemi
těmito lokálními hodnotami. Zvolíme počáteční vektor nenulový modulo
každé p_i, například (0,...,0,1). Perioda jeho složek je p_i^k-1;
perioda vektoru modulo m je přesně lcm_i(p_i^k-1), protože shoda
nastává právě při shodě všech složek. Při nulové počáteční složce
se příslušný faktor periody samozřejmě nemusí objevit.

Ověřeno 12 konkrétních konstrukcí pro m=6,10,15,30 a k=1,2,3,
nezávislým přímým průchodem stavů. Například Fibonacciho rekurence
modulo 6 má při k=2 periodu lcm(3,8)=24. Rozšíření na mocniny
prvočísel odkazuje správně na úlohu 11; netvrdí periodu m^k-1
pro libovolný složený modul.

Relevantní vrstvy all2-prepre, all2-pre, all2, err2 a err2.textxt
prověřeny. Opravy úloh 18 a 19 jsou známé; nový C0011 se týká
samotného dodatku 2013. Historická doporučení statistické kvality
z textu nejsou prezentována jako současná doporučení generátorů.

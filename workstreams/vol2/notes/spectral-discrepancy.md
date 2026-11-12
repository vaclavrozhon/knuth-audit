# Spektrální test a discrepancy: F, úlohy25–30 a32

Původní sazba110–114,117–118,582–584 přečtena vizuálně. Matematická
část F a sedm úloh jsou uzavřeny v níže uvedeném rozsahu. Výzkumná31
a historické atribuce celé sekce zůstávají samostatně otevřeny.
`verify_spectral_discrepancy.py` a `results/spectral-discrepancy.json`
obsahují přesné a intervalové kontroly; obecné důkazy jsou zde.

## 1. Fourierův rozklad počtu bodů

Pro N bodů P_n=(x_n,...,x_(n+t-1)), jejichž souřadnice jsou celá čísla
z rozsahu0,...,m-1, značí D_N^(t) největší rozdíl mezi relativním
počtem bodů v obdélníku R a jeho objemem děleným m^t. Obdélníky
jsou kartézské součiny intervalů [alpha_j,beta_j) s celočíselnými konci.
To je přesně diskrétní definice(42), nikoli maximum přes všechny reálné
hranice. Označme omega=exp(2*pi*i/m), primitivní m-tou odmocninu1.

Součet sum_(u=0)^(m-1) omega^(u*x) je m, pokud m dělí x, a jinak0,
což plyne z konečné geometrické řady. Součin t těchto identit dává
indikátor shody dvou bodů. Sečtení přes n a body R proto dává přesný
rozklad na110. Nulová frekvence u=(0,...,0) je právě očekávaný objem.
Trojúhelníková nerovnost a výměna maxima se součtem dávají(44).

Pro nenulovou jednorozměrnou frekvenci u je absolutní hodnota
normalizované intervalové geometrické řady nejvýše
r_m(u)=1/(m*sin(pi*u/m)); pro u=0 definujeme r_m(0)=1. Součin těchto
vah značí r_m(u_1,...,u_t). Tím dostáváme(45)/(46), bez požadavku
nesoudělnosti u,m. V lineárním kongruenčním generátoru platí modulo m

```
u·P_n = q(u)*x_n + h(u),
q(u) = u_1+a*u_2+...+a^(t-1)*u_t,
```

kde h(u) nezávisí na n. Faktor omega^h má absolutní hodnotu1, a proto
vzorec(47) pro g(u)=|sum_n omega^(q(u)*x_n)|/N je správný. Rovnosti
rozepsaných stavů na111 se zde čtou v exponentu modulo m.

Pro plnou periodu N=m jsou x_n permutací všech zbytků. Proto g(u)=0
pro q(u)!=0 modulo m a g(u)=1 pro duální kongruenci q(u)=0 modulo m.
Označme R(a,m,t) součet r_m(u) přes všechny její nenulové zbytkové
vektory0<=u_j<m a r_max největší z těchto vah. V t>=2 takové vektory
existují; v t=1 je množina prázdná a plná perioda má přímo D_m^(1)=0.

## 2. Součet vah v jedné třídě: úloha25 a C0049

Je-li d dělitel m a0<=q<d, rozdělíme zbytky k=q modulo d na obě
poloviny podle vzdálenosti od0 modulo m. Na každé straně je nanejvýš
jeden nejbližší bod s vahou nejvýše1; další mají vzdálenost alespoň
d,2d,... . Funkce1/sin(pi*x/m) na0<x<=m/2 klesá. Součet je tudíž
nejvýše2*(1+f(m/d)/d), kde

```
f(M) = (1/M) sum_(1<=k<=M/2) csc(pi*k/M).
```

Zde csc(x)=1/sin(x). Pro M>=2 dává obyčejná integrální horní mez

```
f(M) <= 1/(M*sin(pi/M)) + (1/M) integral_1^(M/2) csc(pi*x/M) dx
     <= 1/2 + (1/pi)*ln M.
```

Použili jsme sin(pi/M)>=2/M a cot(pi/(2M))<=2M/pi. Pro M=1 je
f(M)=0. Výsledkem je požadovaná mez (2/(d*pi))*ln(m/d)+O(1),
dokonce s univerzální přidanou konstantou3. Prvotní srovnání součtu
na582 je tedy správné.

**C0049:** následující nahrazení f(M) integrálem s chybou O(1/M)
správné není. Eulerovu konstantu zde definujeme jako
gamma=lim_(n->infty)(H_n-ln n), kde H_n=sum_(k=1)^n1/k.
Odečtěme singularitu pomocí hladké funkce
h(x)=csc(pi*x)-1/(pi*x), rozšířené hodnotou h(0)=0. Riemannův součet
této funkce na[0,1/2] má chybu O(1/M), protože její derivace je omezená.
Její integrál je ln(4/pi)/pi. Proto

```
f(M) = (ln M + gamma + ln(2/pi))/pi + O(1/M).
```

Naproti tomu vytištěný integrál je
-ln(tan(pi/(2M)))/pi=(ln M+ln(2/pi))/pi+O(1/M^2).
Rozdíl tedy jde ke gamma/pi, nikoli k0. Integrální krok lze opravit
buď přidáním gamma/pi, nebo nahrazením zbytku O(1/M) hodnotou O(1).

Stejná odpověď uvádí zpřesněnou formuli pro d=1 s konstantou
1+(2/pi)*ln(2e/pi). Správně má být

```
sum_(0<=k<M) r_M(k)
  = (2/pi)*ln M + 1 + (2/pi)*(gamma+ln(2/pi)) + O(1/M).
```

V argumentu logaritmu tedy patří e^gamma místo e. Součet je přesně
1+2f(M)-[M sudé]/M; poslední korekce ošetřuje dvojí započtení prostředku.
Meze0<gamma<1 plynou již z integrálního srovnání harmonické řady,
takže rozdíl konstant není nulový. Závěr úlohy25 ani hlavní O-odhady F
tato chyba nevyvrací.

Intervalový výpočet ověřil13534 tříd a čtyři velikosti10,100,1000,10000.
Rozdíl součtu a integrálu je větší než0.18 i pro největší velikost;
obecná limita výše je odvozena analyticky, nikoli z těchto čísel.

## 3. Neúplná perioda a úloha26

Pro plnoperiodický generátor s m>1 označme s nejmenší kladný exponent
s a^s=1 modulo m. Po s krocích přibude ke stavu hodnota
b=c*(1+a+...+a^(s-1)) modulo m. Dříve ověřené periodové výsledky
dávají gcd(b,m)=s a b=s*q', kde gcd(q',m)=1. Při a=1 se geometrický
součet stále definuje uvedeným polynomem; není třeba dělit nulou.

Definujme S_(k,l)=sum_(j=0)^(m-1) omega^(x_(j+l)+j*k).
Posun indexu j ukazuje S_(k,l)=omega^(-l*k)S_(k,0). Zprůměrování
|S_(k,l)|^2 přes l a ortogonalita mocnin omega pak vymažou všechny
dvojice indexů j,i kromě j-i dělitelného s. Zůstává

```
|S_(k,0)|^2 = m sum_(j=0)^(m/s-1) omega^(j*(s*k+b)),
|S_(k,0)| = m/sqrt(s), pokud k+q'=0 modulo(m/s), jinak0.
```

To je(51). Přesná Fourierova inverze posloupnosti omega^x_n vede k(49)
a po trojúhelníkové nerovnosti k(52). Použijeme úlohu25 s d=m/s:

```
|sum_(0<=n<N) omega^x_n|
  <= (2/pi)*sqrt(s)*ln s + 3*m/sqrt(s).
```

Pro výpočet discrepancy se tato mez dělí N. Opravy6.2.2005 odstraňují
normalizaci1/N v(49),(52),(53) a v zadání26, rozšiřují sumu k na0<=k<m
a přidávají m>1 do věty N. Jsou zahrnuty; žádná z nich není novým nálezem.

Pro obecnou nenulovou frekvenci q položíme d=gcd(q,m), M=m/d a
q_0=q/d. Posloupnost q_0*x_n modulo M má plnou periodu M, neboť
q_0 je invertibilní. Její násobitel je stále a. Je-li rozklad m na
prvočísla prod p_i^e_i a gcd(a-1,m)=prod p_i^f_i, pak nový řád je
prod p_i^max(0,e_i-f_i-v_(p_i)(d)), přesně jako v odpovědi26.
Z toho plyne s_M<=s i M/sqrt(s_M)<=m/sqrt(s). Horní mez se tudíž
nezvětší. Úplné periody v exponenciálním součtu jsou0, takže N lze
nejprve nahradit N mod M, jak doplňuje stejné erratum. Pokud zbytek
je0, celý součet je0; normalizaci při návratu ke g dělíme původním N.

Přímé skutečné orbity117 modelů poskytly2400 přesně ověřených čtverců
součtů,4800 posunových identit a2283 redukcí modulu. Komplexní hodnoty
se porovnávaly jako celočíselné polynomy modulo cyklotomický polynom,
tedy minimální polynom příslušné primitivní odmocniny1. Nejde o
plovoucí aproximaci nul.

## 4. Dyadické třídy: úloha27

Pro zbytek x definujme rho(x)=min(x,m-x), kromě rho(0)=1, a funkci
rozšiřme periodicky. Kladná třída L(x)=floor(lg x)+1 pro0<x<=m/2
zaznamená počet binárních číslic vzdálenosti; záporná třída používá
záporný počet číslic m-x pro m/2<x<m. Zvlášť L(0)=0. Dále
ell(L)=max(1,2^(|L|-1)). Pak ell(L(x))<=rho(x)<2ell(L(x)). Každá
souřadnicová třída má nejvýše ell(L) prvků a všech tříd v t dimenzích
je nejvýše(2lg m+1)^t.

Nechť P_min je nejmenší součin prod_j rho(u_j) mezi nenulovými
řešeními kongruence q(u)=0. Označme mu=floor(lg P_min). Truncace
vymaže nejnižší bit první souřadnice, jejíž vzdálenost rho přesahuje1;
pokud taková není, nic neudělá. Dvěma vektorům stejné třídy se při
opakování mažou bity ve stejných souřadnicích. Jestliže se po mu
truncacích shodnou, každý rozdíl souřadnic má absolutní hodnotu menší
než2^(počet vymazaných bitů v této souřadnici). Pro dva různé vektory
proto součin rho jejich rozdílu je menší než2^mu<=P_min. Jejich
rozdíl ovšem také splňuje kongruenci; taková dvojice nemůže existovat.
Pro mu=0 je injektivita samozřejmá.

Ve třídě L=(L_1,...,L_t) je B=sum_j log_2 ell(L_j) proměnných bitů.
Po mu truncacích zbývá nejvýše max(1,2^(B-mu)) různých prefixů.
To je horní mez počtu řešení kongruence v dané třídě, i když poslední
třída na hranici m/2 není plná. Pro třídu s jediným řešením je váha
nejvýše r_max<=1/P_min. Při větším počtu je jednotlivá váha nejvýše
2^(-B), takže celková váha nejvýše2^(-mu)<2/P_min. Použili jsme
2rho(x)<=m*sin(pi*x/m)<pi*rho(x) pro x!=0; nulové složky přispívají1.
Vektor dosahující P_min navíc dává1/P_min<=pi^t*r_max. Tedy

```
R(a,m,t) <= 2*(pi+2*pi*lg m)^t*r_max.
```

Výklad i binární příklad na582–583 jsou správné. Přesná kontrola1469
modelů zahrnula119343 nenulových duálních vektorů a81390 tříd;
ověřuje injektivitu konkrétních truncací i všechny počty tříd.

## 5. Věta N a význam hlavního odhadu

Součet všech vah je B_m^t, kde B_m=sum_(0<=u<m)r_m(u)=O(log m)
podle úlohy25. Rozdělíme(44) podle toho, zda platí duální kongruence.
Její část je nejvýše R(a,m,t), část mimo ni nejvýše
B_m^t*((2/pi)*sqrt(s)*ln s+3m/sqrt(s))/N. Úloha27 pak dává přesně
tři O-členy věty N. Pro N=m mimo duální kongruenci nezůstane nic,
takže platí i(55). Konstanty lze vypsat jako funkce t z uvedených
explicitních mezí; běžné O-značení zde chápe dimenzi jako pevnou.

Pro m=2^e,a=5 modulo8 je s=m/4, což plyne z již ověřené periodové
věty. Pro obecný plnoperiodický násobitel s=m/gcd(a-1,m). Výklad
potence na114 tedy odpovídá oběma členům: dobrá kongruenční mříž
sama nezaručuje dobrou krátkou počáteční část periody, když s je malé.

## 6. Prvočíselný multiplikativní generátor: úloha28 a C0050

Nyní m=p je prvočíslo, a je primitivní kořen (jeho mocniny procházejí
všechny nenulové zbytky) a c=0. Délka periody je p-1. Položme
zeta=exp(2*pi*i/(p-1)) a
S_(k,l)=sum_(j=0)^(p-2)omega^(x_(j+l))*zeta^(j*k).
Při k!=0 modulo(p-1) jde o Gaussův součet s netriviálním
multiplikativním charakterem, tj. funkcí chi(a^j)=zeta^(j*k).

Pro úplnost jeho norma plyne z dosazení x=z*y:

```
|sum_(x!=0) chi(x)*omega^x|^2
  = sum_(z!=0) chi(z) sum_(y!=0) omega^((z-1)*y)
  = (p-1) - sum_(z!=1) chi(z) = p.
```

Poslední krok používá sum chi(z)=0 pro netriviální charakter.
**C0050:** pro k=0 tato podmínka neplatí a součet je přímo-1, tedy
|S_(0,0)|=1, nikoli sqrt(p) vytištěné bez výjimky na583. Stačí
doplnit k!=0 a zvlášť hodnotu1. Například p3,a2 dávají pro k0
omega+omega^2=-1. Horní mez sqrt(p) platí pro všechna k, takže
odhad neúplného součtu O(sqrt(p)*log p) zůstává správný.

Pro plnou periodu je g(u)=1 na kongruenci a1/(p-1) mimo ni. Proto

```
D_(p-1)^(t) <= ((p-2)/(p-1))*R(a,p,t) + (B_p^t-1)/(p-1).
```

To souhlasí s přesným rozkladem v odpovědi. Pro t>=2 lze přidaný
člen pohltit do O((log p)^t*r_max): vektor(-a mod p,1,0,...,0)
má váhu větší než1/(pi*p). Pro t=1 se místo prázdného r_max použije
přímo D_(p-1)^(1)=1/p. Také konečný závěr o všech dimenzích včetně1
je správný s tímto odděleným triviálním případem.

Nenulový vektor u představuje nenulový polynom q(a) stupně nejvýše
t-1 nad F_p. Má tedy nanejvýš t-1 kořenů. Sečtení R přes všechny
primitivní kořeny je nejvýše(t-1)(B_p^t-1). Po dělení jejich počtem
phi(p-1) dostáváme požadovaný průměr O(t*(log p)^t/phi(p-1)).
Existence jediného dobrého a pro všechny t<=T nevyžaduje součet
T samostatných výjimek: zvolíme dobré a v dimenzi T a využijeme
D_N^(t)<=D_N^(T), neboť kratší obdélník doplníme plnými intervaly.
Standardní mez n/phi(n)=O(loglog n) pak dává závěr vytištěné poznámky.
Její případ T=1 je přímo vyřešen hodnotou1/p.

Překážka pro složený modul je doložena polynomem(1-a)^3. Modulo2^e
má přesně2^(e-ceil(e/3)) kořenů, protože je třeba v_2(a-1)>=ceil(e/3),
kde v_2 značí exponent2 v rozkladu čísla. Pro e>=4 jsou tyto kořeny
současně násobiteli plnoperiodických smíšených generátorů. Řád velikosti
2^(2e/3) v odpovědi je správný.

Přímé Gaussovy součty14 modelů poskytly111 přesných cyklotomických
kontrol včetně nulové frekvence. Samostatně bylo ověřeno19791
polynomů a jejich kořenových mezí.

## 7. Norma a součin souřadnic: úloha29 a C0051

Zvolme centrované reprezentanty souřadnic duálního vektoru u, takže
nenulové absolutní hodnoty x_j leží mezi1 a m/2. Jejich počet k je
nejméně2: jedna nenulová složka kongruenci při gcd(a,m)=1 nesplní.
Označme v=||u||, takže v^2=sum x_j^2>=k. Platí
prod x_j^2>=sum x_j^2-k+1=v^2-k+1; to se získá opakováním
xy>=x+y-1 pro x,y>=1. Proto

```
r_m(u) <= 1/(2^k*prod x_j)
       <= 1/(2^k*sqrt(v^2-k+1)) <= 1/(sqrt(8)*v).
```

Poslední nerovnost po umocnění plyne z v^2>=k a4^k>=8k pro k>=2.
Jelikož v>=nu_t, dostáváme(56). Pokud všechny souřadnice po centrování
zmizí, šlo o nulový zbytkový vektor, který se v r_max neuvažuje.

**C0051:** poslední odůvodnění na583 má v>=k>=2 místo v^2>=k>=2.
To první neplatí: m2,a1,u=(1,1) dává v=sqrt(2),k=2. Hlavní
nerovnost i výsledná konstanta1/sqrt(8) jsou správné; jde o chybějící
exponent v pomocném argumentu. Celočíselná kontrola tohoto argumentu
je součástí všech119343 vektorů předchozího dyadického bloku.

## 8. Řetězové zlomky: úloha30

Pišme a/m=[0;d_1,...,d_s] v kanonickém tvaru d_s>=2 a A=max d_i.
Konvergenty p_n/q_n jsou zlomky ukončené po n číslicích; začínají
p_0/q_0=0/1. Standardní nejlepší aproximace druhého druhu zde má
krátký důkaz: každý celočíselný pár(p,q) lze vyjádřit jako celočíselnou
kombinaci dvou sousedních konvergentů, neboť determinant je±1. Jejich
chyby a*q-m*p mají opačná znaménka. Při0<q<q_n kombinace s opačnými
znaménky koeficientů chyby sčítá; kombinace s kladnými koeficienty
nemůže použít q_n. Tím |a*q-m*p|>=|a*q_(n-1)-m*p_(n-1)|.
V intervalu q_(n-1)<=q<q_n se proto součin q*|a*q-m*p| nemůže
dostat pod hodnotu předchozího konvergentu.

Kontinuant K(d_1,...,d_n) je jmenovatel konvergentu, definovaný
K_n=d_n*K_(n-1)+K_(n-2), K_0=1,K_(-1)=0. Pro n<s je
|a*q_n-m*p_n| kontinuant posledních s-n-1 číslic. Označme ho r_n.
Rozklad kontinuantu u číslice d_(n+1) dává

```
m/(q_n*r_n) = d_(n+1) + q_(n-1)/q_n + r_(n+1)/r_n.
```

Oba přidané poměry jsou nezáporné a jejich součet menší než2.
Je-li P nejmenší součin q*|a*q-m*p| pro1<=q<m, dostáváme
A<=m/P<A+2. Díky symetrii u a m-u lze P hledat s oběma centrovanými
absolutními složkami. Nerovnosti2u<=m*sin(pi*u/m)<pi*u pak dávají

```
A/(pi^2*m) < r_max <= (A+2)/(4m).
```

Odpověď30 je správná. Nezávislý soupis všech q a výpočet z konvergentů
souhlasí pro7805 nesoudělných dvojic s m<=160. Řádky8 a13 tabulky mají
A=3 a2, jak vyžaduje komentář114. Výrok o O((log m)^2/m) se vztahuje
na rodiny s rovnoměrně omezeným A; jednotlivé konečné příklady samy
o sobě nejsou asymptotickou větou. Citlivost discrepancy na otočení
plyne z definice pomocí souřadnicových obdélníků, zatímco nu_t používá
eukleidovskou normu a na otočení nezávisí.

## 9. Kombinovaný generátor: úloha32

Pro m_1=2^31-1,m_2=2^31-249,m=m_1*m_2 položme
U_n=(X_n/m_1-Y_n/m_2) mod1 a Z_n=(X_n-Y_n) mod m_1. Pak

```
U_n-Z_n/m_1 = (m_2-m_1)*Y_n/m modulo1.
```

Koeficient248/m je přibližně2^(-54), jak kniha uvádí. Rozdíl je ale
po vynásobení Y_n velikosti nejvýše248/m_1, tedy přibližně2^(-23),
a je třeba chápat ho jako vzdálenost na kružnici. Při X_0=Y_0=1 je
Z_0=0 a U_0=1-248/m: obyčejný absolutní rozdíl je blízko1. Přesný
vzorec odpovědi výslovně říká modulo1, takže tento interpretační limit
nevedeme jako další chybu. Nezaručuje shodu všech horních bitů u bodů
ležících na hranici přenosu nebo přetečení.

Číslo a=1431853894371298687 má zbytky48271 a40692 modulo oba moduly.
Proto W_n=(X_n*m_2-Y_n*m_1) mod m splňuje W_(n+1)=a*W_n mod m.
Čínská věta o zbytcích (jednoznačnost při nesoudělných modulech)
ověřuje obě složky a přesnou rovnost U_n=W_n/m. Původní odpověď32
je správná s výše vymezenou kruhovou aproximací. Ověřeno4000 přesných
stavů ze čtyř dvojic seedů; prvočíselnost a periody se nepřepočítávaly,
jsou již certifikovány v `spectral-tables.md`.

## 10. Evidence a zbývající práce

Všechny čtyři vrstvy errat a aktuální TeX prohledány1.11.2026 podle
stran110–118,582–584 a výrazů csc, cosecant, Euler, Gauss, sqrt(m),
Niederreiter, Hlawka a čísel úloh. Obrazy errat stran6/7 a32 ověřují
změny2001/2005. Žádná nalezená oprava se netýká C0049–51. Novější
fyzický dotisk a prvenství neověřeny; všechny návrhy jsou neodeslané.

Pět bloků skončilo exit0 v session44075; nový blok `combined` doběhl
samostatně pomocí --resume, rovněž exit0. Úspěšné bloky se neopakovaly.
Výsledek je obecný audit F a úloh25–30,32. Zůstává31 a primární
historická kontrola atribucí, nikoli neověřená správnost uvedených
hlavních analytických odhadů.

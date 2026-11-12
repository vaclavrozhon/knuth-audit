# §3.4.1 F a zbývající základní distribuční a geometrické úlohy

Stav 1. listopadu 2026. Vizuálně přečteny str.136–142 a587–590.
Uzavřeny matematika F a úlohy17–19,22–23,25–30,32–33.
Úlohy24/31 a historický kontext se evidují samostatně. Nové drobné
nálezy C0056/C0057 jsou uvedeny v §4 a§6. Program
`verify_discrete_distributions.py` má tři checkpointované bloky;
všechny prošly, výsledky v `results/discrete-distributions.json`.

## 1. Geometrické a negativně binomické rozdělení; úlohy17–19

Geometrická veličina N je počet nezávislých pokusů do prvního úspěchu,
včetně tohoto úspěchu; pravděpodobnost úspěchu označujeme p.
Pro 0<p<1, q=1−p, máme Pr(N=n)=p*q^(n−1), n>=1, protože prvních
n−1 pokusů musí selhat. Událost ceil(ln U/ln q)=n je
q^n<=U<q^(n−1), takže(39) má správný zákon. Pro p=1 vrátíme N=1;
p=0 neposkytuje konečný čekací čas. Přesná nula U vyžaduje stejnou
konvenci jako u ostatních logaritmických metod. Při p=1/2 je výsledek
jedna plus počet vedoucích nul nenulového binárního zlomku, i když
U je přesnou mocninou dvou.

Pro x>=0 je distribuční funkce F(x)=1−q^floor(x); pro x<0 je0.
Pravděpodobnostní vytvořující funkce G(z)=E(z^N) je pz/(1−qz).
Derivace v1 dávají E(N)=1/p, Var(N)=q/p² a SD=sqrt(q)/p.
Pomocný výpočet s reciprokou lineární funkcí v odpovědi17 je správný;
v tomto pomocném kroku se používá formální derivace, nikoli tvrzení,
že každý pomocný polynom s případnými zápornými koeficienty je PGF.

Pro úlohu18 součin dvou takových PGF dělený z dává
p²*z/(1−qz)², tedy Pr(N=n)=n*p²*q^(n−1). Proto N=N1+N2−1.
Pro negativně binomickou veličinu řádu t>0 je PGF
(p/(1−qz))^t; koeficient je (t)(t+1)...(t+n−1)*p^t*q^n/n!.
Je-li t celé, jde o součet t geometrických veličin minus t.
Pro libovolné reálné t>0 platí rekurence
p_(n+1)=p_n*q*(t+n)/(n+1), p0=p^t, což dokazuje inverzní
algoritmus N. Opravy29.6.1999 (ukončení a >=) a6.1.2011 (názvy
N1/N2 místo B1/B2) jsou zahrnuty. Kumulativní součet roste k1,
takže ideální U<1 dává skoro jisté ukončení.

Gamma–Poissonova směs v odpovědi19 platí i pro necelé t. Pro
X~gamma(t) a podmíněné N~Poisson(X*q/p) je

```
Pr(N=n) = integral_0^infinity
 x^(t−1)e^(−x)/Gamma(t) * exp(−xq/p)*(xq/p)^n/n! dx
 = Gamma(t+n)/(Gamma(t)n!)*p^t*q^n.
```

Průměr t*q/p tedy také souhlasí. Pro t=p=1/2 je průměr1/2,
proto prostá inverze potřebuje v průměru jen1.5 navštívených hodnot.

## 2. Rekurzivní binomické dělení

Binomický zákon Bin(t,p) počítá úspěchy v t nezávislých pokusech.
Položme a+b−1=t a vyberme X jako a-tou nejmenší z t uniformních
veličin. Podmíněně na X=x jsou zbývající a−1 spodní hodnoty
nezávisle uniformní na(0,x), horních b−1 na(x,1), po zapomenutí pořadí.
Když x>=p, je výsledný počet Bin(a−1,p/x). Když x<p, je jich
nejméně a a zbývající počet je Bin(b−1,(p−x)/(1−x)).
To přesně odpovídá textu. Volbou a=1+floor(t/2) se parametr
v každé větvi zmenší nejvýše na floor(t/2); hloubka je O(log t).

Nezávislá kontrola integruje obě podmíněné pravděpodobnosti proti
beta hustotě X. Pro n<a se integrand zkrátí na konstantu krát
p^n*(x−p)^(a−1−n)*(1−x)^(b−1), x v[p,1]. Pro n>=a je to
konstanta krát x^(a−1)*(p−x)^(n−a)*(1−p)^(t−n), x v[0,p].
Oba integrály dávají binom(t,n)*p^n*(1−p)^(t−n).
Program provedl2184 nezávislých racionálních polynomových integrací
pro všechny dělicí indexy t=1..12 a tři pravděpodobnosti p.

## 3. Poissonovy příchody a rychlejší rekurze

Poissonův zákon s průměrem mu>=0 má hmotnosti e^(−mu)*mu^n/n!.
Pro mu>0 nechť S_m je součet m exponenciálních časů s průměrem1/mu.
Událost, že před časem1 nastane nejvýše n příchodů, je S_(n+1)>=1.
Gamma integrál a integrace per partes dávají rozdíl sousedních ocasů
rovný e^(−mu)*mu^n/n!, tedy(40). Pro n=0 se druhý člen čte jako0:
S0=0 nemůže překročit1. Nejde o potřebu vyčíslovat faktoriál(−1)!.
Nulový parametr mu má deterministický výstup0.

Po sečtení logaritmů je podmínkou zastavení součin U1...Um<=e^(−mu).
Počet vylosovaných čísel je N+1, má tedy průměr mu+1. Uvedená
praktická omezení podtečení a pevné přesnosti zůstávají v platnosti.

Pro m>=1 a X~gamma(m) je přesná rekurze:
X<mu -> m+Poisson(mu−X), X>=mu -> Bin(m−1,mu/X).
Lze ji ověřit přímo bez simulace příchodů. Pro n>=m integrujeme
první větev; exponenciály se zruší na e^(−mu) a zůstane beta
integrál x^(m−1)*(mu−x)^(n−m), x v[0,mu]. Pro n<m integrujeme
druhou větev; zbude posunutý gamma integrál
exp(−x)*(x−mu)^(m−1−n), x v[mu,infinity). Oba dávají přesně
Poissonovu hmotnost, každý ve svém rozsahu.

Společná hustota normalizovaných mezer X_i/S_m, podmíněně na S_m=s,
je konstantní na simplexu; změna na částečné součty má konstantní
Jacobián. Proto S1/S_m,...,S_(m−1)/S_m jsou seřazené uniformní
hodnoty, jak text odvozuje. Pomocné faktory mu*exp(−t/mu) na137
nejsou normalizované hustoty, ale v uvedeném poměru integrálů se
jejich společný faktor úplně zruší. Výsledek tím není chybný.

O(log mu) je očekávaná cena, nikoli deterministická maximální délka.
Pro pevné 0<alpha<1 a dostatečné mu má m=floor(alpha*mu)>=alpha*mu/2.
Z E(X)=m a E(X²)=m²+m plyne
Pr(X>=m/2)>=m²/(4(m²+m))>=1/8 (Cauchyho nerovnost aplikovaná
na X*[X>=m/2]). Takový krok buď skončí binomickou větví, nebo sníží
mu nejméně faktorem1−alpha/4. Počet kroků na konstantní poměrnou
redukci má omezený průměr, proto je celkem O(log mu) gamma kroků.
Binomická větev se provede nejvýše jednou a má tutéž řádovou mez.
Dobovou experimentální optimalizaci alpha=7/8 zde neprohlašujeme
za univerzální optimálnost na všech strojích.

## 4. Přesná oprava aproximovaného kvantilu; úloha22 a C0056

Kvantilem G^(-1)(u) rozumíme inverzi spojité přísně rostoucí CDF G.
Pro mu>0 je G(x)=Gamma(x,mu)/Gamma(x), x>0, kde čitatel je horní
gamma integrál od mu do nekonečna. Tato funkce roste od0 do1:
gamma(x+h) lze vytvořit jako nezávislý gamma(x)+gamma(h).
Integrace per partes dává G(x+1)−G(x)=e^(−mu)*mu^x/Gamma(x+1).
Podlaha veličiny s CDF G má tedy Poissonův zákon.

Nechť Z=G^(-1)(F(X)) je přesný spojitý výstup z normálního X a
Y jeho aproximace s |Z−Y|<epsilon. Pro zamýšlenou malou toleranci
0<epsilon<1/2 položme N=floor Y a M=floor(Y+1/2). Jestliže
|Y−M|>epsilon, interval(Y−epsilon,Y+epsilon) neprotne žádné celé
číslo a floor Z=N. Jinak protne nanejvýš číslo M, a tedy
floor Z=M−[Z<M]. To dokazuje korekční pravidlo. Test Z<M může být
převeden na F(X)<G(M), takže není nutné skutečně invertovat G.
Bez malé tolerance by tento jednoprahový argument neplatil;
tato podmínka je zde vymezena, nikoli převzata jako libovolné epsilon.
Odpověď sama nekonstruuje konkrétní rychlou g s globální chybovou
mezí, pouze popisuje princip pod tímto předpokladem. Normalita v jádru
rozdělení neslibuje uniformní lineární aproximaci v obou nekonečných ocasech.

Pro binomický zákon má být

```
G(x)=Gamma(t+1)/(Gamma(x)Gamma(t+1−x))
     * integral_p^1 u^(x−1)*(1−u)^(t−x) du,  0<x<t+1.     (1)
```

Pro 0<p<1 má G limity0/1 a přísně roste: poměr beta hustot pro dva
parametry x je kladná konstanta krát rostoucí mocnina u/(1−u).
Na celých bodech k=1..t je G(k)=Pr(Bin(t,p)<=k−1); rozdíly tedy
vracejí binomické hmotnosti. Program kontroluje630 takových hodnot
přesnými polynomovými integrály. Degenerované p=0/1 vracejí0/t přímo.

**C0056:** na str.588 v odpovědi22 je v integrandu n−x místo t−x.
Písmeno n v této definici nemá význam a nesouhlasí s parametrem t
v obou gamma faktorech. Například t=1,p=1/2,x=1 musí dát G(1)=1/2.
Kdyby se nezávislé n četlo jako2, tištěný integrál by dal1/8.
Jde o jednoznačnou záměnu písmene; princip korekce kvantilu zůstává
po její opravě platný. Původní str.588/file600 a detail sazby uloženy.

## 5. Úlohy23,25,26

Úloha23: pro0<=x<=1 má sin(pi U/2) CDF (2/pi)arcsin x.
Podmíněně na bod v prvním kvadrantu kruhu je jeho úhel Theta
uniformní na[0,pi/2]. Druhý výstup je |cos(2Theta)|, který má tutéž
CDF symetrií čtyř čtvrtin periody. Dělení nulou v počátku je nulová
událost spojitého modelu, při implementaci se bod odmítne.

Úloha25: nechť q je pravděpodobnost pravé vnořené podformule.
Nezávislý rovnoměrný levý bit mění q při OR na(1+q)/2 a při AND
na q/2. Začínáme q=1/2 v posledním bitu; čteme operátory od konce.
Binární zápis výsledku tak obsahuje zleva1 pro OR,0 pro AND a
poslední1. Daný výraz má0.10101_2=21/32. Program enumeroval všech
126 výrazů s1..6 operátory a jejich10920 pravdivostních řádků.
Známé změny bitových značek19.5.2005 a vysvětlení17.8.2024 zahrnuty.

Úloha26: součin PGF exp(mu1*(z−1))*exp(mu2*(z−1)) dává Poisson(mu1+mu2).
Rozdíl při mu2>0 může být záporný, například při N1=0,N2=1,
což má kladnou pravděpodobnost. Není proto Poissonův; případ mu2=0
je výslovná výjimka. Uvedená konvoluce a oba závěry správné.

## 6. Bitový binomický generátor; úloha27 a C0057

Každá ze t simulovaných uniformních hodnot má nezávislé rovnoměrné
bity. Po j−1 sloupcích známe počet N hodnot menších než p a m dosud
nerozhodnutých, které mají stejný prefix jako p. V dalším sloupci je
počet M odlišných bitů Bin(m,1/2). Pokud je bit p jednička, tyto
odlišné hodnoty jsou menší a přičteme M k N; jinak jsou větší.
V obou případech m zmenšíme o M. Když má p jen nulový zbytek,
žádný zbývající prefix už nemůže dát menší hodnotu. To dokazuje B1–B3.

Racionální model pravděpodobností všech stavů(m,N) ověřil1386
rozdělení pro t=0..10 a všechny končící zlomky s1..6 bity.
Bylo sečteno361812 přechodů; porovnání proti binomickému vzorci
proběhlo pro každou konečnou hmotnost. p=1 lze vrátit přímo nebo
použít nekončící rozvoj0.111..., který také skončí skoro jistě.

Při nekončícím rozvoji p skončíme, až se všech n hodnot odliší.
Počet sloupců je maximum n nezávislých geometrických časů s p=1/2.
Označme jeho průměr A_n. Platí

```
A_0=0,
A_n=1+2^(−n)*sum_(k=0)^n binom(n,k)A_k,              (2)
A_n=sum_(j>=0)(1−(1−2^(−j))^n)
   =1+sum_(k=1)^n binom(n,k)(−1)^(k+1)/(2^k−1).      (3)
```

První řádek je podmínění na první sloupec, druhý součet ocasů
maxima a třetí binomický rozvoj. Vytvořující exponenciální funkce
v knize odpovídá přesně(2). Osmdesát přesných racionálních hodnot
(2) souhlasí s nezávisle vyčísleným konečným součtem(3).

**C0057:** na str.589 je levá strana posledního displeje vytištěna A_m,
ale všechny pravé strany mají index n. Má být A_n. To je i index
v předchozí rekurenci a v definici vytvořující funkce. A_1=2 a A_2=8/3
ukazují, že levý index nemůže být volný. Detail ze souborové strany601
potvrzuje m; nejde o OCR. Oprava nemění vlastní algoritmus ani koeficienty.

Pro jasnou interpretaci periodického členu definujme

```
f0(n)=−(2/ln2)*sum_(k>=1) Re(Gamma(−2*pi*i*k/ln2)
                                  *exp(2*pi*i*k*log2 n)).       (4)
```

Zde i²=−1 a Re je reálná část. Řada konverguje absolutně
exponenciálním poklesem Gamma na svislých přímkách a je periodická
v log2 n s periodou1. Pro poissonizovaný součet
H(n)=sum_(j>=0)(1−exp(−n/2^j)) dává Mellinova inverze integrand
Gamma(s)*n^(−s)/(2^s−1), zpočátku −1<Re(s)<0. Posun přímky doprava
sečte záporné reziduum dvojnásobného pólu v0 a jednoduchých pólů
2*pi*i*k/ln2. Dostaneme log2 n+gamma/ln2+1/2+f0(n)+O(1/n),
kde gamma je Eulerova konstanta. Pro j>=1, q=2^(−j), je

```
0<=exp(−nq)−(1−q)^n<=n*q²*exp(−nq).
```

Součet pravých stran je O(1/n), protože sum_(j>=1)(nq)²exp(−nq)
je omezený po rozdělení u nq=1. Člen j=0 přidá jen exp(−n).
Tím je tentýž rozvoj doložen pro A_n, včetně nenulové malé oscilace.
Čtyři80ciferné nezávislé výpočty ocasového součtu pro n=10³..10⁹
souhlasí; n-násobek zbytku je přibližně0.7213, jak očekává člen O(1/n).

Odkaz na svazek3 byl zkontrolován v dostupném2.vydání1998, původní
str.636/file647: §5.2.2-46/48 používá místo f0 symbol −delta0.
Naše(4) se s touto explicitní definicí shoduje. Původní str.137/file148
navíc definuje V_r=sum_(k>=2)binom(r,k)(−1)^k*k/(2^(k−1)−1);
přeznačení k=j+1 přímo dává A_n=1+V_(n+1)/(n+1). První vydání svazku3,
na které navazoval svazek2 z1997, zde není k dispozici; rozdíl označení
nepřičítáme jako další matematickou chybu. Při prvním renderu byla
použita nesprávná mapa+12; skutečně zobrazená637 byla přejmenována
a636 znovu vykreslena s ověřenou mapou+11. Oba původní snímky zachovány.

## 7. Rovnoměrný povrch elipsoidu; úloha28

Nechť a1>=...>=an>0, A=diag(a1,...,an), a elipsoid je x^T A x=1.
Pro jednotkový směr y položme rho=sqrt(y^T A y) a x=y/rho.
Plošný Jacobián této radiální mapy je

```
J(y)=sqrt(y^T A²y)/rho^(n+1).                         (5)
```

Důkaz: vnější jednotková normála je Ax/||Ax||. Její kosinus se
směrem y je1/(||x||*||Ax||). Plocha radiálního obrazu jednotkového
plošného elementu je ||x||^(n−1) děleno tímto kosinem, tedy(5).
Přijímat směr s pravděpodobností K*J(y) proto dává rovnoměrnou
plošnou míru na elipsoidu. Přesně tento test používá odpověď.

Zbývá ověřit optimální K. Označme m=an, M=a1, w_i=y_i²,
s=sum a_i*w_i, q=sum a_i²*w_i. Máme sum w_i=1 a
q<=(M+m)*s−Mm, protože a_i²<=(M+m)a_i−Mm.
Pro dané s v[m,M] je rovnost dosažitelná směsí obou krajních os.
Minimum1/J² je tedy minimum
s^(n+1)/((M+m)s−Mm). Znaménko jeho derivace určuje
n(M+m)s−(n+1)Mm. Pokud M<=nm, minimum leží v s=m a je m^(n−1).
Jinak leží v s=(n+1)Mm/(n(M+m)) a má hodnotu
((n+1)/(M+m))^(n+1)*(Mm/n)^n. Oba případy přesně souhlasí.
Program ověřil1694 racionálních krajních modelů a dosažitelné váhy;
globální důkaz zajišťuje předchozí sečnová nerovnost.

## 8. Seřazené hodnoty a Poissonovy body; úlohy29–30

Podmíněně na X_(k+1)=v je k-tá seřazená hodnota maximum k
uniformních bodů v[0,v], tedy v*U^(1/k). Součin podmíněných hustot
k*x_k^(k−1)/x_(k+1)^k se zkrátí na n! na simplexu
0<x1<...<xn<1, protože X_(n+1)=1. To je přesně hustota uniformních
pořadových statistik; postup má n kroků. Exponenciální zápis
exp(−Y/k) je totožná inverze. Známé opravy zadání10.11.1997
a jména Seneshal25.3.2006 zahrnuty. Tvrzení o skutečné rychlosti
oproti třídění je strojově závislé, nikoli asymptotická dolní mez.

Úloha30: exponenciální přírůstky vytvářejí Poissonův proces na[0,1].
Podmíněně na počet m je jeho neuspořádaná množina m nezávislých
uniformních bodů. Míru zachovávající rozdělení bitů jednoho uniformního
zlomku do dvou souřadnic dává uniformní bod čtverce. Pro obdélník
plochy a je podmíněný počet Bin(m,a); zprůměrování přes
m~Poisson(mu) dává PGF exp(a*mu*(z−1)), tedy Poisson(a*mu).
Stejný společný PGF dokazuje nezávislost počtů v disjunktních oblastech.

Tištěné rozdělení2r bitů na dva bloky je konečná mřížková aproximace;
obdélníková pravděpodobnost na ní je počet bodů dělený2^(2r), ne
přesná plocha libovolného reálného obdélníku. Ideální prokládání
nekonečných lichých a sudých bitů je přesně míru zachovávající mapa.
Toto rozlišení je společným předpokladem konečných implementací celé
sekce a není vedeno jako nový nález. Výhrada o horších spodních bitech
je věcně správná a neznamená záruku jejich nezávislosti.

## 9. Přeměny exponenciálních dvojic; úloha32

Pro nezávislé Exp(1) vstupy X,Y má součet S=X+Y gamma(2) a
poměr T=X/S je nezávisle uniformní na[0,1]. Mapa(a) zachová S
a pošle T na(T−lambda)mod1, tedy zachová i celý společný zákon.
Indikátor v zadání rozlišuje přesně T<lambda. Hranice jsou nulové.

Mapa(b) dává X'=2min(X,Y), Y'=|X−Y|. Na každé ze dvou polorovin
je prostá a má absolutní Jacobián2, přitom X'+Y'=X+Y.
Oba inverzní příspěvky jsou exp(−x'−y')/2; jejich součet je původní
součinová exponenciální hustota.

Pro(c) lze nezávislost všech binárních cifer dokázat přímo.
Položme K=floor(2^r X), r celé nezáporné, a q=exp(−2^(−r)).
Pak Pr(K=k)=(1−q)q^k, k>=0. Identita
product_(j>=0)(1+q^(2^j))=1/(1−q) ukazuje, že bity K jsou
nezávislé a bit u váhy2^j má pravděpodobnost1 rovnou
q^(2^j)/(1+q^(2^j)). Pro bit X u váhy2^ell je tedy pravděpodobnost
1/(1+exp(2^ell)), nezávislá na zvolené r. Každá konečná množina
cifer je tak nezávislá. Oba vstupy mají stejný produktový zákon;
prohození libovolných shodných bitových pozic mezi nimi jej zachová.
To dokazuje i nekonečné prokládání v zadání.1530 přesných
racionálních modelů podmíněné geometrické veličiny kontroluje
faktorizaci cifer nezávislým součinem pravděpodobností.

## 10. Jeden vstup pro odmítací generátor; úloha33

Tištěná odpověď navrhuje použít U1 jako seed dalšího pseudonáhodného
generátoru. Tím se výstup stane deterministickou funkcí tohoto seedu,
což odpovídá praktickému zadání. Samotná změna násobitele ovšem
není důkaz nezávislosti proudů; tuto záruku zde odpovědi nepřipisujeme.

Pro přesný ideální výklad existuje i čistá konstrukce: u nekonečného
uniformního bitového proudu přidělme do i-tého proudu bity na pozicích
2^(i−1)*(2j−1), j>=1. Tyto množiny rozdělují kladná celá čísla,
proto vznikne spočetně mnoho nezávislých uniformních veličin U_i
z jediného U. Použitím těchto proudů v P/M/F/R se zachová přesný
spojitý důkaz. Na konečném seedu jde opět o aproximaci s konečnou
entropií, nikoli nekonečnou zásobu nezávislých bitů.

## 11. Errata a stav nálezů

C0056: str.588/file600; C0057: str.589/file601,3.vydání/první tisk1997.
Prohledány `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální err2 TeX
podle stran i hesel binomial,continuous Poisson,mean/iterations.
Související historická errata na původních listech33 a8 byla vizuálně
čtena již v normálním bloku. Jediná oprava odpovědi22 je interpunkce
citace, jediná odpovědi29 je jméno; obě záměny indexů opraveny nejsou.
Fyzický nový dotisk a prvenství nejsou ověřeny. Hlášení jsou neodeslaná.

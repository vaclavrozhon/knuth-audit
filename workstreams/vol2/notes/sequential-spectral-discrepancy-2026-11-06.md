# Souvislá revize: diskrepance a spektrální test

**Aktualizace 10. listopadu 2026:** C0244 byl zamítnut po novém čtení
původní sazby. Tištěný interval se týká qq', nikoli uu'; nerovnost
uu' >= qq' je správně použitá. Historická analýza níže je v tomto bodě
překonaná. Viz [opravené posouzení](bookwise-spectral-2026-11-10.md).

6. listopadu 2026. Přečtena původní sazba 109–115, 117–118 a 582–584,
celý `verify_spectral_discrepancy.py`, dokončovací log a všech šest
výsledkových souhrnů. Následující závěry se týkají F a úloh 25–30/32.
Historická část G a výzkumná úloha 31 budou dokončeny samostatně;
jejich staré poznámky byly přečteny pro orientaci, ne znovu celé ověřeny.

## Přezkoumané obecné argumenty

Definice (42) používá obdélníky s celočíselnými hranicemi. Nejde o
nezměněnou definici diskrepance přes všechny reálné hranice. Součin
t geometrických řad dává přesný indikátor shody bodů modulo m;
nulová frekvence po vydělení N*m^t dává objemový člen. Trojúhelníková
nerovnost a výměna maxima se součtem jsou ve správném směru.
Geometrická řada pro nenulové u má normalizovanou normu nejvýše
1/(m*sin(pi*u/m)); nulová souřadnice přispívá nejvýše 1. Tím jsou
(44)–(46) správné bez požadavku gcd(u,m)=1. Rovnosti rozepsaných stavů
na 111 se používají modulo m v exponentu. Konstantní přírůstková fáze
nemění normu, což dokazuje (47)/(48).

Pro plnou periodu smíšeného generátoru jsou stavy permutací zbytků:
g je 1 na duální kongruenci a 0 mimo ni. Pro neúplnou periodu je
Fourierova inverze (49) přesná. Posun indexu dává
S_(k,l)=omega^(-lk)*S_(k,0); zprůměrování čtverce normy přes l
zruší všechny rozdíly indexů, které nejsou násobkem řádu s násobitele.
Je-li b přírůstek po s krocích, zbude

```
|S_(k,0)|² = m * sum_(j=0)^(m/s-1) omega^(j*(s*k+b)).
```

Z dříve doložené plné periody plyne b=s*q', gcd(q',m)=1. To dává
přesně dvě větve (51). Pro a=1 je geometrický podíl definován
polynomem 1+a+...+a^(s-1); při výpočtu se nedělí nulou.
Úloha 25 poskytuje explicitní mez
`|sum omega^x_n| <= (2/pi)*sqrt(s)*ln(s)+3*m/sqrt(s)`.

Pro frekvenci q!=0 modulo m použijeme d=gcd(q,m), M=m/d a
invertibilní q/d. Nová posloupnost modulo M má plnou periodu M.
Prvočíselné exponenty řádu jsou max(0,e_i-f_i-v_p(d)); z nich
po jednotlivých prvočíslech plynou s_M<=s a M/sqrt(s_M)<=m/sqrt(s).
Úplné periody exponenciálního součtu jsou nulové. Lze tedy použít
N mod M, ale při návratu ke g stále dělit původním N.

Dyadický důkaz úlohy 27 je správný. Ve stejné třídě mají vektory
stejná znaménka centrovaných souřadnic a stejné délky binárních zápisů.
Truncace proto odstraňuje bity ve stejných souřadnicích. Pokud by dva
různé duální vektory měly shodný zbytek po mu truncacích, součin rho
jejich rozdílu by byl menší než 2^mu<=P_min. Rozdíl je přitom další
nenulový duální vektor. Injektivita tedy platí; nulové rozdílové
souřadnice mají rho=1 a nejméně jedna jiná dává přísnost. Když se
odstraní všechny proměnné bity dříve, platí týž argument s jejich
menším počtem. Počet prefixů je nejvýše max(1,2^(B-mu)). Jednoprvková
třída se oddělí, ostatní mají celkovou váhu <2/P_min. Odhad počtu
tříd a nerovnosti pro sinus dávají uvedenou konstantu úlohy 27.
Binární příklad na 583 skutečně odstraní pět vyznačených bitů v pořadí.

Součet všech vah je B_m^t s B_m=O(log m). Rozdělení frekvencí na
duální kongruenci a její doplněk dává tři členy (54); při N=m
zůstává jen (55). Konstanty závisejí na pevné dimenzi t.
Použitý rozsah je m>1 a t>=2; v dimenzi 1 je množina nenulových
duálních zbytků prázdná a plná smíšená perioda má přímo D_m^(1)=0.
Nedefinujeme maximum prázdné množiny bez výslovné konvence.
Pro a=5 modulo 8 je s=m/4 a uvedená velikost dostatečného N odpovídá
dosazení. Věta neříká, že vysoké spektrální skóre zaručí dobrou
libovolně krátkou část periody.

## Tři potvrzené závady a jejich dopad

**C0049, původní 582:** nahrazení součtu kosekant integrálem má
nenulový konstantní rozdíl. Odečtením 1/(pi*x) vznikne na [0,1/2]
hladká funkce h s omezenou derivací. Její integrál je ln(4/pi)/pi;
harmonická část dává

```
f(M)=(ln M + gamma + ln(2/pi))/pi + O(1/M).
```

Tištěný integrál má stejný výraz bez gamma. Rozdíl jde ke gamma/pi,
nikoli k 0. V následné konstantě úplného součtu patří e^gamma místo e.
Sudý prostřední člen přispívá korekcí -1/M; liché zaokrouhlení konce
také ovlivní jen O(1/M). Původní logaritmická horní mez je platná:
monotónnost kosekanty dává f(M)<=1/2+ln(M)/pi a součet v jedné třídě
nejvýše 2+2f(M)/d. Konstantní člen lze univerzálně omezit číslem 3.

**C0050, původní 583:** v Gaussově součtu úlohy 28 má nulová
multiplikativní frekvence k=0 hodnotu -1 a normu 1, nikoli sqrt(p).
Pro k!=0 je součet charakteru přes nenulové zbytky 0; dosazení x=z*y
do čtverce normy dává p. Nejkratší příklad výjimky je p=3,a=2.
Horní mez sqrt(p) platí v obou větvích, takže následný odhad
neúplného součtu není chybný. Tento krok se přímo používá pro N
nejvýše délky periody; při delším N se musí oddělit úplné periody,
jejichž součet u multiplikativního generátoru není nulový.

Pro plnou periodu p-1 je g rovno 1 na duální kongruenci a 1/(p-1)
mimo ni, takže rozklad v odpovědi 28 je správný. Pro t>=2 vektor
(-a mod p,1,0,...) dokládá r_max>1/(pi*p), a zbývající člen lze
pohltit do uvedeného O-odhadu. V t=1 se zvlášť použije D_(p-1)=1/p.
Kořenová mez nenulového polynomu stupně nejvýše t-1 dává požadovaný
průměr přes primitivní kořeny. Jedno a pro všechny t<=T získáme
výběrem v dimenzi T a monotónností D^(t)<=D^(T). Standardní použitá
mez n/phi(n)=O(log log n) není nově dokazována. Složený modul
má vytištěnou překážku: (1-a)^3=0 modulo 2^e má přesně
2^(e-ceil(e/3)) řešení; pro e>=4 všechna splňují podmínku a=1 modulo 4.

**C0051, původní 583:** chybí druhá mocnina v podmínce v²>=k>=2.
Vektor (1,1) modulo 2 s a=1 má v=sqrt(2)<k=2. Výsledný odhad je
přesto správný. Pro nenulové centrované souřadnice x_j>=1 platí
`prod x_j² >= sum x_j²-k+1`, opakováním xy>=x+y-1. Potom
`2^k*sqrt(v²-k+1)>=sqrt(8)*v` plyne z v²>=k a 4^k>=8k.
Tento důkaz nepotřebuje dosažitelnost pomocného minimizátoru s
k-1 souřadnicemi rovnými 1: ten by při dodatečné horní hranici m/2
mohl ležet mimo přípustný kvádr. Stačí obecná dolní mez součinu.

## Řetězové zlomky: správný výsledek, otevřený krok výkladu

Pro minimum P součinu q*|aq-mp|, 1<=q<m, platí A<=m/P<A+2.
Důkaz nejlepší aproximace využívá unimodularitu sousedních
konvergentů a opačná znaménka jejich chyb; rozklad kontinuantu dává
m/(q_n*r_n)=d_(n+1)+q_(n-1)/q_n+r_(n+1)/r_n. Oba přidané poměry
mají součet menší než 2. Případ shodných prvních jmenovatelů při
první číslici 1 má prázdný interval a důkaz nenarušuje. Vždy lze
zvolit svědka minima s oběma souřadnicemi centrovanými.

Hlavní výsledek úlohy 30 tedy lze doložit bez ztotožnění optimalizátorů:
každý vektor má součin nejméně P, a proto r<=1/(4P); naopak vektor
dosahující P má r>1/(pi²P). Dostáváme přesně
`A/(pi²*m)<r_max<=(A+2)/(4m)`.

**Nový C0244 je pouze candidate / low.** První odstavec na 584
přenáší rozsah součinu z předchozí minimalizace na vektor zvolený
pro maximum r. Tyto optimalizátory obecně nejsou stejné:
pro m=49,a=15,[0;3,3,1,3] je minimální centrovaný součin 12
(normála (4,3)), zatímco maximum r nastává u ±(1,13), se součinem 13.
Generátor s c=1 skutečně má plnou periodu 49, takže příklad splňuje
i předpoklady smíšeného generátoru. Dvacet čtyři intervalových výpočtů
s 70 desetinnými místy dokládá přísné oddělení obou skupin; výsledek
a program jsou uložené. Dřívější příklad m=29,a=12 dává součiny
10 a 12, ale jeho multiplikátor nemá plnou smíšenou periodu, proto
není použit jako hlavní příklad k textu věty N.
Tento příklad **nevyvrací** slabší tištěný interval A/m<=1/(uu')
ani konečné meze: obojí v něm platí. Otevřený je přesný význam a
odůvodnění přenosu, nikoli dokázaná nesprávnost hlavního odhadu.
Proto má úloha 30 v souvislé revizi stav partial a původní strana
584 zůstává částečná. Při §4.5.3-42 lze tuto otázku znovu prověřit.

Krátký plovoucí průzkum 27397 párů s m<=300 nenašel porušení
slabšího intervalu. Není to přesný ani obecný důkaz. Prvnímu spuštění
nebyl zachycen návratový výstup; opakovaný krátký běh jej zapsal do
`sequential-spectral-product-screen.json` (3.22 s, nice 15). Poté
proběhly jen cílené intervalové kontroly m=29 a m=49 při nice 15.
Krátké nalezení případu s plnou periodou prověřilo 86 modelů přibližně za 0.002 s;
šlo opět pouze o navigaci k následnému přesnému příkladu.
Staré úspěšné soupisy se neopakovaly a žádný dlouhý běh nevznikl.

## Geometrie, kombinace a rozsah zdrojů

Řádky 8 a 13 tabulky mají A=3, respektive A=2; jejich konečné zlomky byly už
uloženým programem porovnány. O((log m)²/m) se týká rodiny s
rovnoměrně omezeným A, nikoli asymptotiky jednoho pevného čísla.
Hermitova horní mez a dolní spektrální mez při omezeném A dávají
šířku mezer mezi rovinami řádu 1/sqrt(m). Uvnitř čtverce z takové
mezery vyřízneme prázdný rovnoběžník s délkou omezenou zdola
kladnou konstantou a s touto šířkou. Jeho plocha má uvedený řád.
Malá odchylka pro souřadnicové obdélníky tomu neodporuje; spektrální
norma je invariantní vůči otočení, třída souřadnicových obdélníků není.

Úloha 32: oba CRT zbytky a přesná rovnost U_n=W_n/(m1*m2) souhlasí.
Chybový koeficient je 248/(m1*m2), přibližně 2^-54, ale násobí se
Y_n; celková kruhová odchylka je nejvýše 248/m1, přibližně 2^-23.
Při X0=Y0=1 přetečení kružnice brání malé obyčejné absolutní
odchylce. Odpověď výslovně pracuje modulo 1, takže to není nový
nález; nevyvozujeme z ní zaručenou rovnost všech vyšších bitů.

Znovu přečteny původní strany 159–162 Niederreiterova článku 1979.
Podporují historické přiřazení exponenciálních metod a jejich vztah
k diskrepanci. Zdroj používá reálné hranice obdélníků, proto má navíc
diskretizační člen s/m; jeho váha je převrácená vůči knize. Nedokazuje
se zde znovu celý článek ani přesná totožnost všech jeho konstant
s knihou. Úplné starší články a historická prvenství zůstávají částí G.

## Errata a přijaté výpočty

Čtyři vrstvy errat i aktuální TeX znovu prohledány podle stran a
výrazů kosekanta/Euler/Gauss/Hlawka/Niederreiter. Obrazy errat 6,7,32
porovnány s OCR. Změna z roku 2005 ruší normalizaci 1/N současně na
obou stranách rovnic, přidává k=0 do pomocné sumy, výslovné m>1 do
věty N a redukci N modulo M do odpovědi 26. Samotné odstranění 1/N
je algebraický přepis, nikoli důkaz chyby původní rovnosti. Zde proto
vzniká záznam kontroly publikované změny, nikoli nová červená karta
za každý přepsaný vzorec. Oprava sazby čísla (44) je rovněž nematematická.

Staré kontroly přijaty po čtení celého kódu a úspěšného logu:
2400 cyklotomických čtverců, 4800 posunů, 2283 redukcí modulu;
13534 intervalových součtů tříd; 119343 duálních vektorů a 81390 tříd;
111 Gaussových součtů, 19791 polynomiálních kořenových mezí;
7805 kontrol součinů z konvergentů; 4000 přesných kombinovaných stavů.
Cyklotomická kontrola používá zbytek celočíselného polynomu, nikoli
plovoucí nulu. Intervalové asymptotické příklady pouze doplňují
analytický důkaz limity. Následný samostatný blok combined má rovněž
úspěšný dokončovací záznam.

Žádná nalezená oprava neřeší C0049–51 ani nepřidává odůvodnění C0244.
Pozdější fyzický dotisk a prvenství nejsou ověřeny. Nic nebylo odesláno.
Další kurzor: výzkumná úloha 31 na 117/584 a historická část G na 114–115.

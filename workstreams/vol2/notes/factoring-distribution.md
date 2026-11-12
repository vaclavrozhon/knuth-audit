# §4.5.4: velikosti a počty prvočinitelů, úloha 18

Kontrola 3. listopadu 2026. Uzavřen spodní Dickmanův odstavec na382,
matematika383–384 a celá odpověď k18 na661. Všechny tyto strany
i zadání413 byly vizuálně přečteny. Vlastní důkazy níže zahrnují
limitní rozdělení, souvislost s permutacemi a normální limitní zákon;
nejde jen o kontrolu čísel. Všech22 kvantilů a40 míst konstanty (9)
je certifikováno. Nová chyba nebyla nalezena.

Prvočíselná věta, Riemannova hypotéza a tabulka počtů prvočísel na382
zůstávají pro pozdější bloky25/41. Dodatečné citace jsou ověřeny
v přesně uvedeném rozsahu v §9; nepřečtené články neoznačujeme za přečtené.

## 1. Značení a konečný rozklad

Nechť X je kladné celé číslo a N je rovnoměrně náhodné číslo z 1,...,X. Jeho prvočinitele
seřadíme sestupně `P_1(N)>=P_2(N)>=...`, **s opakováním**;
chybějící členy položíme rovny1. Knižní p_t je tedy naše P_1.
Pišme `F_k(a)` pro limitní pravděpodobnost `P_k(N)<=X^a`, pokud
existuje. Její existenci i chybu O(1/ln X) pro pevné a>0 dokazuje §2.
Knižní F=F_1, G=F_2 a H=F_3. Logaritmus ln je přirozený.

Číslo je Y-hladké, pokud jsou všechny jeho prvočinitele nejvýše Y.
Jejich počet nejvýše X označme Psi(X,Y). Rozklad podle velkých
prvočinitelů dává přesné identity

```
#{N<=X: P_2(N)<=Y} = Psi(X,Y) + sum_(p>Y) Psi(floor(X/p),Y),
#{N<=X: P_3(N)<=Y} = předchozí počet
                      + sum_(p>=q>Y) Psi(floor(X/(pq)),Y).       (D1)
```

V součtech jsou prvočísla a členy s prázdným rozsahem jsou nula.
Případ p=q je třeba zachovat: faktory se počítají s násobností.
První součet obsahuje právě čísla s jedním velkým faktorem, druhý
právě se dvěma. Nezávislé rozklady celých čísel ověřily obě identity
pro4576 dvojic (X,Y), s X<=2048 a1<=Y<=32.

## 2. Existence limitních rozdělení a vztah k permutacím

Z [factoring-basic.md](factoring-basic.md) už máme elementárně dokázáno

```
sum_(p<=x) 1/p = ln ln x + B + O(1/ln x).                       (D2)
```

Zde B je Mertensova konstanta. Pro pevné a>0 tak míra, která bodu
`ln p/ln X` přiřazuje váhu1/p pro X^a<p<=X, má distribuční funkci
`ln(t/a)+O(1/ln X)` rovnoměrně pro a<=t<=1.
Jejím limitem je míra dt/t na[a,1].

Nechť C_X počítá různé prvočinitele N větší než X^a. Pro každé j
je očekávaná hodnota binom(C_X,j)

```
sum_(p_1<...<p_j, all>X^a, product<=X)
                           floor(X/(p_1...p_j))/floor(X).       (D3)
```

Záměna podlahy za X/(p_1...p_j) má chybu O(1/ln X).
Opravdu, počet příslušných uspořádaných j-tic je O(X/ln X):
fixujeme j-1 faktorů se součinem d, zbývající prvočíslo má nejvýše
X/d možností a leží nad X^a. Odhad pi(y)=O(y/ln y) pak dává
O(X/(d*a*ln X)); součet1/d je omezen pomocí (D2).
Použitý horní odhad pi plyne už z elementárního theta(y)=O(y)
v předchozí poznámce, oddělením prvočísel do sqrt(y) a nad sqrt(y).

Opakovaná prvočísla v pomocných uspořádaných součtech přidávají
jen O(X^(-a)), protože sum_(p>X^a)1/p²=O(X^(-a)). Totéž omezuje
pravděpodobnost, že se nějaký velký prvočinitel N opakuje.
Z (D2–D3) tedy dostáváme limit

```
J_j(a) = 1/j! integral_(t_i>=a, sum t_i<=1)
                                      dt_1...dt_j/(t_1...t_j). (D4)
```

Přechod je i s chybou O(1/ln X). Lze postupovat po jedné proměnné:
pro zbytek simplexu je kumulativní integrál monotónní a omezený.
Integrace per partes proti rozdílu distribučních funkcí z (D2)
proto stojí O(1/ln X), rovnoměrně v horní hranici součtu. Indukce
přes j zachová tento odhad; celková hmotnost míry je omezená.
Počet relevantních j je nejvýše floor(1/a), tedy konečný.

Pro každé nezáporné celé c platí binomická inverze

```
[c<k] = 1 - sum_(j>=k) (-1)^(j-k) binom(j-1,k-1) binom(c,j).   (D5)
```

Hranaté závorky znamenají indikátor. Rovnost plyne například
z Pascalovy identity indukcí podle c. Dosazení (D3–D4) do (D5)
dokazuje existenci F_k(a), včetně chyby O(1/ln X), pro každé pevné a>0.
Pro a=0 je limit 0: pravděpodobnost omezeného počtu faktorů jde k nule
také z limitního zákona v §7. Navíc F_k(a) spojitě klesá k 0 při a->0+.
Opravdu, limitní počet velkých faktorů má průměr m=ln(1/a);
z (D4) je očekávání binom(C_X,2) v limitě nejvýše m²/2, tedy variance
nejvýše m. Pro m>k dává Čebyševova nerovnost
`F_k(a)<=m/(m-k)^2`, což jde k nule. Pro a>=1/k je F_k(a)=1,
neboť k faktorů větších než X^a by mělo součin větší než X.

Nyní vezměme rovnoměrnou permutaci n prvků a C_n počet jejích cyklů
delších než an. Počet způsobů, jak v permutaci vybrat j neoznačených
cyklů délek l_1,...,l_j, dává přesně

```
E binom(C_n,j) = 1/j! sum_(l_i>an, sum l_i<=n) 1/(l_1...l_j).  (D6)
```

Riemannův součet v (D6) konverguje ke stejnému J_j(a). Proto (D5)
dává **stejné limitní rozdělení k-tého nejdelšího cyklu/n** jako
ln(P_k(N))/ln X. Obě veličiny leží v[0,1], takže konvergují i jejich
střední hodnoty, integrací distribučních funkcí.

Přechod od intervalu1,...,2^n k n-bitovým číslům
2^(n-1),...,2^n-1 vznikne rozdílem dvou prefixových počtů; obě
normalizace logaritmu se liší o O(1/n). Počet bitů P_k se od
log2(P_k) liší nejvýše o1. To dokazuje přesnou asymptotickou
formulaci knihy384 pro každé pevné k. Na konečné úrovni bylo
(D5–D6) porovnáno s nezávislou rekurzí podle cyklu obsahujícího
nejmenší prvek:1200 přesných rovností, n<=20, všechna r=1,...,20,
k=1,2,3. Jde o kontrolu konečné identity, nikoli náhradu limitního důkazu.

## 3. Funkcionální rovnice (6), (7) a úloha 18

Definujme `I_j(u)=J_j(1/u)`, tj. integrál (D4) po přenásobení
proměnných u. Jeho oblast je t_i>=1, sum t_i<=u. Pro j=0 položme
I_0(u)=1 pro u>=0, jinak0; pro j>=1 je I_j(u)=0 při u<=j.
Homogenita integrandu, nebo integrace toku vektoru
`(t_1,...,t_j)/(t_1...t_j)` přes hranici simplexu, dává

```
u I_j'(u)=I_(j-1)(u-1).                                      (D7)
```

Na horní stěně je tok u násobek derivace objemového integrálu;
j spodních stěn je po započtení1/j! právě I_(j-1).
Pro j=1 je to jednoduše derivace ln u.

Označme `rho_k(u)=F_k(1/u)` a rho=rho_1. Binomické koeficienty
v (D5), Pascalova identita a (D7) dávají

```
u rho_k'(u)=rho_(k-1)(u-1)-rho_k(u-1),  u>1;
rho_k(u)=1 pro 0<=u<=1,  rho_0=0.                            (D8)
```

Zvláště `u rho'(u)=-rho(u-1)`. Kniha pracuje s převrácenou
proměnnou; po její změně dostáváme

```
F_k'(t) = (F_k(t/(1-t))-F_(k-1)(t/(1-t)))/t.                 (D9)
```

Zde 0<t<1. Integrací od 0 do a, se spojitostí v nule z §2,
jsou to přesně (6), (7) a dodatek pro H na 661.
Řešení je jednoznačné: (D8) je určuje postupně na jednotkových
intervalech z dřívějších hodnot. Heuristické vysvětlení v zadání18
je rozklad N=pm podle jeho k-tého největšího faktoru p;
ve zbytku musí být k-tý faktor nejvýše p a(k-1)-ní větší než p.
Rozdíl obou podmínek dává F_k-F_(k-1). Velké opakované faktory
mají nulovou limitní četnost podle §2.

Pro1<=u<=2 je rho(u)=1-ln u, tedy F(a)=1+ln a pro1/2<=a<=1.
Pravděpodobnost faktoru většího než sqrt(X) je proto ln2.
Z (D1) nebo přímou integrací (D8) také plyne praktický vzorec

```
G(b)=rho(z)+integral_0^(z-1) rho(v)/(z-v) dv,  z=1/b.         (D10)
```

Jeho derivace splňuje(D8): po integraci per partes je
`u(d/du)G(1/u)=-integral_0^(u-2)rho(v)/(u-1-v)dv`.
Pro u<=2 je G(1/u)=1. Tím je (D10) potvrzen i analyticky,
nezávisle na pravděpodobnostním rozkladu.

## 4. Pravděpodobnost z úlohy 18, derivace v nule

Podmínka `P_2<sqrt(P_1)` při P_1 přibližně X^t požaduje,
aby zbytek N/P_1 byl X^(t/2)-hladký. Její limitní pravděpodobnost je

```
integral_0^1 F(t/(2(1-t))) dt/t
  = integral_0^infinity rho(u)/(u+2) du
  = integral_0^infinity rho(u)/(u+1)^2 du =: delta.           (D11)
```

Pro první substituci stačí u=2(1-t)/t. Druhá rovnost plyne
z `rho(u-1)=-u rho'(u)` a integrace per partes; kraj v u=1 je1/2,
stejně jako integral_0^1 du/(u+1)^2. Dále

```
delta = 1 - integral_1^infinity rho(u)/u² du
      = integral_0^1 (1-F(a)) da.                            (D12)
```

Získáme to integrací derivace rho(u)/u. Výraz(D12) je střední
hodnota normalizovaného logaritmu největšího faktoru; §2 jej zároveň
ztotožňuje s relativní střední délkou největšího cyklu permutace.
Jde tedy o Dickmanovu–Golombovu konstantu. Vlastní obaly(D11–D12)
všechny obsahují tutéž hodnotu a certifikují knižní .62433.

Pro normalizaci použijme integrální identitu odvozenou z(D8):

```
u rho(u)=integral_(u-1)^u rho(v)dv,  u>=1.                    (D13)
```

Dokazuje pozitivitu rho: při prvním nulovém bodě by pravá strana
byla kladná. Dává i monotónnost a `rho(u)<=rho(u-1)/u`, tedy
`rho(u)<=1/floor(u)!`. Integrály a následující přechody proto konvergují.

Nechť `R(s)=integral_0^infinity rho(u)exp(-su)du`, s>=0.
Integrace(D8) per partes dává
`s R'(s)=(exp(-s)-1)R(s)`. Tedy

```
R(s)=R(0) exp(-integral_0^s(1-exp(-t))dt/t).
```

Protože rho=1 u nuly, sR(s)->1 pro s->infinity. Integrál
v exponentu je ln s+gamma+o(1); to plyne integrací per partes
a z `gamma=-integral_0^infinity exp(-t)ln t dt`.
Zde gamma je Eulerova konstanta, limita harmonického součtu
`1+1/2+...+1/n-ln n`.
Odtud R(0)=exp(gamma). V(D10) necháme z->infinity:
na v<=z/2 použijeme dominaci2rho(v), zbytek mizí díky faktoriálnímu
ocasu. Dostáváme G(b)/b->exp(gamma). Jelikož G(0)=0,
pravá derivace G'(0) je exp(gamma).

Rovnost(D13) sečtená po celých intervalech zároveň dává

```
R(0)=sum_(n>=1)n rho(n)=F(1)+2F(1/2)+3F(1/3)+... .           (D14)
```

Tištěný integrál na661 je `integral_0^1 F(t/(1-t))*t^(-2)dt`;
substituce u=(1-t)/t jej převádí na R(0). Původní sazba je správná.

Také H'(0)=+infinity v odpovědi je správně. Pro malé b zvažme
čísla se dvěma velkými faktory s exponenty a>=c> b,
kde `2b<=c<=1/4` a `1-b-c<=a<=1-c`. Zbytek je automaticky
X^b-hladký, protože a+c>=1-b. Dvojitý rozklad podle velkých
faktorů dává na tomto podrozsahu příspěvek
`integral integral da dc/(ac)>=b ln(1/(8b))`.
Proto H(b)/b->infinity. Přechod k limitnímu dvojitému integrálu
je tentýž jako v §2; při pevném b jsou hranice od nuly vzdálené.

## 5. Certifikované kvantily a obrázek 12

Program `verify_factoring_distribution.py` užívá síť h=1/16384
na[0,16]. Všechny dolní i horní meze jsou celá čísla v jednotkách
2^(-90); dělení se zaokrouhluje výslovně ven pomocí celočíselných
podlah a stropů. Desetinná čísla v JSON jsou pouze čitelný doplněk,
žádný důkaz na nich nezávisí.

Z(D8),(D13) máme mimo celočíselné body `0<=rho''<=1` pro u>1.
Pro `g(u)=rho(u-1)/u` platí `|g''|<=2`: na(1,2) je g=1/u;
na(2,3) použijeme rho'= -1/u, rho''=1/u² a na vyšších
intervalech přímo(D8). Středový kvadraturní vzorec na kroku h
má tedy chybu nejvýše h³/12. Hodnotu rho ve středu dřívějšího
kroku uzavřeme mezi lineární interpolant a interpolant minus h²/8;
na[0,1] je funkce přesně1. Tak získáme induktivně rigorózní obal
v každém bodě sítě. Navíc jej protínáme s monotónností,
nezáporností a faktoriální horní mezí z(D13).

Pro(D10) je integrand rho(v)/(z-v), v<=z-1. Jeho druhá derivace
má absolutní hodnotu nejvýše5 na každém hladkém dílku. Složené
lichoběžníkové pravidlo včetně posledního kratšího kroku má chybu
nejvýše `5*length*h²/12`. Vnitřní body zlomu jsou body sítě.
Pro tři integrandy v(D11–D12) stačí analogické meze2 nebo11;
pro rho samotné1. Ocas za16 je omezen

```
sum_(n>=16)1/n! <= 17/(16*16!).                              (D15)
```

Distribuční funkce (CDF) udává pravděpodobnost hodnoty nejvýše daný práh.
Pro každý z22 vytištěných kvantilů a_0 jsme **prokázali**,
že horní obal CDF v a_0-0.00005 je menší než cílová pravděpodobnost
a dolní obal v a_0+0.00005 je větší. Monotónnost tak certifikuje
celé čtyřmístné zaokrouhlení. Nejde o dvě shodná numerická řešení.
Dále bylo33 racionálních bodů na[1,2] nezávisle porovnáno
s uzavřeným vzorcem1-ln u v intervalové aritmetice Arb.

Obrázek12 souhlasí s devíti novými certifikovanými body:
například v a=.2 vychází(F,G) přibližně(.0003547,.4632222),
v .3 přibližně(.0236501,.7731918), v .4 přibližně(.1303196,.9533897)
a v .5 přesně F=1-ln2, G=1. Koncové hodnoty i pořadí křivek sedí.

Numerické obaly integrálů jsou mj.

```
delta                    in (0.62432993429,0.62433004444),
P(P_2<sqrt(P_1))          in (0.62432997702,0.62433000232),
integral rho              in (1.78107239891,1.78107245933).
```

Poslední interval obsahuje rigorózní Arb hodnotu exp(gamma).
Rovnosti mezi integrály dokazují §4, nikoli pouhé překrytí obalů.

## 6. Průměr a konstanta počtu faktorů

Označme `Omega(n)` počet prvočinitelů s násobností a `omega(n)`
počet různých prvočinitelů. Přesně platí

```
sum_(n<=X) Omega(n)=sum_(p^a<=X, a>=1)floor(X/p^a).           (D16)
```

Tato identita byla nezávisle ověřena pro všech2048 celých X.
Pro první mocniny je chyba nahrazení floor(X/p)/X číslem1/p
nejvýše pi(X)/X=o(1). Vyšší mocniny přejdou dominovanou konvergencí
na konvergentní součet sum_p1/(p(p-1)). Pomocí(D2) a jeho
již dokázaného výrazu pro B tak dostáváme

```
E Omega(N)=ln ln X + C + o(1),
C=gamma+sum_p(ln(1-1/p)+1/(p-1)).                            (D17)
```

Eulerova funkce phi(n) počítá čísla1,...,n nesoudělná s n.
Z identity sum_(d|n)phi(d)=n a Eulerova součinu pro
`zeta(s)=sum_(n>=1)n^(-s)`, s>1, dostaneme

```
sum_(n>=2) phi(n)ln(zeta(n))/n
 = sum_p sum_(k>=2) (1-1/k)p^(-k)
 = sum_p(ln(1-1/p)+1/(p-1)).                                 (D18)
```

Všechny členy po rozvinutí jsou nezáporné, záměna součtů je přípustná.
To dokazuje oba výrazy(9). Při256 členech je ocas nejvýše3*2^(-256),
protože ln(zeta(n))<=3*2^(-n) a phi(n)/n<=1.
Arb se110 místy tak certifikuje všech40 vytištěných desetinných míst
(zde jde o useknutý rozvoj se znaménkem+, nikoli zaokrouhlení):

```
1.0346538818974379116197942984646382546703+
```

## 7. Normální limitní zákon a variance

Uvádíme vlastní momentový důkaz použití Erdősova–Kacova zákona,
aby závěr(8) nezávisel pouze na nedostupném historickém článku.
Intuice je přesná: malé prvočinitele se v každém pevném počtu
společných momentů chovají jako nezávislé indikátory; větší faktory
a opakování mají po normalizaci zanedbatelný vliv.
Moment r-tého řádu veličiny Y znamená očekávání Y^r.

Položme L=ln ln X, z=X^(1/L²) a
`S(N)=sum_(p<=z)[p|N]`, `mu=sum_(p<=z)1/p=L-2ln L+B+o(1)`.
Pro nezávislé Bernoulliho veličiny B_p s P(B_p=1)=1/p označme
S*=sum B_p. Pro každý pevný r se r-té centrované momenty S a S*
liší nejvýše `O_r(z^r/X)`: rozvineme mocninu, každá r-tice
prvočísel má nejvýše2^r členů a pravděpodobnost dělitelnosti
součinem různých prvočísel se od jeho převrácené hodnoty liší nejvýše1/X.
Počet r-tic je nejvýše z^r. Chyba jde k nule.

Pro S* singletonové bloky v rozvinutí centrovaného momentu mizí
nezávislostí a nulovou střední hodnotou. Každý blok velikosti aspoň2
přispívá v absolutní hodnotě O_r(1/p), tedy po sečtení O_r(L).
Nejvyšší mocninu L dávají pouze párování: normalizované sudé momenty
jsou(2r-1)!!+o(1), liché jdou k nule. Kolize indexů mezi páry
přidávají nižší řád, neboť sum_p1/p² je omezený.
Proto momenty(S-mu)/sqrt(L) konvergují k momentům standardní normální
veličiny, která má střední hodnotu 0 a varianci 1.

Pro úplnost, z druhých momentů plyne těsnost: pravděpodobnost úniku
mimo [-A,A] jde s A k nekonečnu rovnoměrně k nule. Vyšší omezené
momenty zajišťují rovnoměrnou integrovatelnost, tedy zanedbatelný
příspěvek ocasů k nižším momentům, na každé konvergentní podposloupnosti.
Normální momenty určují rozdělení jednoznačně: řada sudých momentů
pro E cosh(tY) se sečte na exp(t²/2), a z ní plyne konečnost
momentové generující funkce a její normální hodnota. Každá limitní
podposloupnost je tedy normální; tím máme konvergenci v rozdělení.

Z(D2) je E(omega(N)-S)=O(ln L), kdežto
E(Omega(N)-omega(N))<=sum_p1/(p(p-1))=O(1).
Markovova nerovnost a ln L/sqrt(L)->0 ukazují, že rozdíl je
po dělení sqrt(L) zanedbatelný v pravděpodobnosti. Také
(mu-L)/sqrt(L)->0. Dostáváme přesně knižní(8).

Samotná konvergence v rozdělení by ještě nedokazovala asymptotiku
variance; tu ověříme zvlášť. V omega oddělme prvočísla p<=X^(1/3).
Součty chyb společných pravděpodobností jsou O(X^(-1/3)), takže
variance této části je sum_(p<=X^(1/3))(1/p-1/p²)+o(1)=L+O(1).
Zbývající část omega je nejvýše2, tedy Cauchyho–Schwarzova nerovnost
dává Var(omega)=L+O(sqrt(L)). Pro R=Omega-omega je E(R²)=O(1):
pro různá p,q dominuje součin konvergentních řad1/(p(p-1));
pro stejné p je součet `sum_(a,b>=2)p^(-max(a,b))=O(p^(-2))`.
Stejný kovarianční odhad proto dává Var(Omega)~L.

Knižní „mean and variance ln ln x“ je tedy hlavní asymptotický člen;
neznamená přesnou rovnost, což ostatně ukazuje následující(9).
Pravděpodobnost vzdálenosti nejvýše3 směrodatné odchylky limitně
činí0.9973002039..., tedy zaokrouhlených99.73 procent; Arb to potvrdil.

## 8. Známá errata a přesný rozsah výpočtu

Všechny čtyři vrstvy all2-prepre/all2-pre/all2/err2 prohledány;
relevantní listy byly už vizuálně přečteny v inventáři.
Na383 jsou známé typografické úpravy2000/2002: aproximační rovnosti
v heuristice a interpunkce u(6). Na384 je známá oprava bibliografie
Erdős–Kac: svazek62, nikoli26; nepřičítá se novým nálezům.
Dodatek2000 přesouvá rozšiřující bibliografii do Selected Papers
on Analysis of Algorithms,329–330 a336–337.

První běh programu, obal PID1263625, Python1263626, session21277,
limit180s, exit0,10.295311132s, dokončil4 bloky. Další běh pouze
přidal obrázek a permutační identity, předchozí výsledky znovu
nepočítal: obal1264333, Python1264334, limit120s, exit0,0.772314529s.
Pět kontrolních bloků je uloženo v `results/factoring-distribution.json`.
Úplná celočíselná síť je vlastní důvěryhodný lokální cache
`results/factoring-dickman-grid.pickle`; lze ji odstranit a znovu
vygenerovat ze zdrojového programu. Čtení cizích pickle souborů
není součástí reprodukce.

## 9. Primární a bibliografické podklady

[Knuth–Trabb Pardo, Stanford CS-TR-76-538](https://ftpmirror.your.org/pub/misc/bitsavers/pdf/stanford/Stanford_CS_TR_Collection_2025-12-12/PDF/1976/CS-TR-76-538.pdf)
byl získán z institucionálního reportu uchovaného v archivu.
Vizuálně přečteny str.7–17,20–22,24,36–37,39–43:
definice a důkaz limitního rozdělení, vztahy integrálů, počátek
asymptotiky druhého faktoru, obraz a aplikace na permutace.
Jeho(4.7) přesně podporuje chybu O(1/ln X), ačkoli vlastní §2
už podává samostatný důkaz potřebného tvrzení.
Celý52stránkový PDF soubor přečten nebyl; původní statistika100 čísel
na39 nebyla přepočítána, protože není tvrzením kontrolované knihy.
Časopiseckou bibliografii TCS3(1976),321–348 potvrzuje
[autorův univerzitní seznam](https://cap.stanford.edu/profiles/frdActionServlet?choiceId=printerprofile&profileId=41803&profileversion=full).

Ramaswami, Bull. AMS55(1949),1122–1127,
DOI10.1090/S0002-9904-1949-09337-0: plný souborAMS vrací403;
nebyl přečten. Preprint1976 odkazuje také na jeho jinou práci
Duke16(1949),99–109. Tyto dva články nezaměňujeme.
Erdős–Kac1940: originál naRényiho serveru403; starší oznámeníPNAS1939
naPMC vyžaduje CAPTCHA, nepřistupováno dále. Knižní opravená bibliografie
je potvrzena institucionálním seznamem Rényi; matematiku zajišťuje §7.

Další údaje byly ověřeny bibliograficky, nikoli čtením celých důkazů:

- [Billingsleyho univerzitní seznam](https://stat.uchicago.edu/people/in-memoriam/billingsley-publications/)
  potvrzuje Periodica Math. Hungarica2(1972),283–289 a Annals of
  Probability2(1974),749–791. Monthly80(1973),1099–1115 potvrzuje
  [záznam časopisu](https://www.jstor.org/pss/2318544).
- [Galambos u vydavatele](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/31/3/101057):
  Acta Arithmetica31(1976),213–218, DOI10.4064/aa-31-3-213-218.
- [Hafner–McCurley u vydavatele](https://www.sciencedirect.com/science/article/abs/pii/0196677489900047):
  Journal of Algorithms10(1989),531–556, DOI10.1016/0196-6774(89)90004-7;
  abstrakt potvrzuje téma druhého největšího faktoru, plný text nepřečten.
- Vershik1987,57–61 je starší rozšiřující citace nahrazená erraty2000;
  doložena bibliografií, nevydávána za vlastní kontrolu celého článku.

Jako doplnění předchozího rho bloku byl získán také
[Arney–Bender1982](https://msp.org/pjm/1982/103-2/pjm-v103-n2-p03-s.pdf).
Vizuálně přečteny269–273: definice modelu, omezení počtů vzorů,
tabulky parametrů a distribucí. Dokládá relevanci doplněné citace385;
jde o náhodný model, nikoli důkaz rychlosti pevného polynomu x²+1.
Zbývající důkazy tohoto článku audit netvrdí jako zkontrolované.

# §1.2.8: základní identity, součty a rekurence

Audit 1. listopadu 2026. Zobrazeny s. 79–86 a odpovědi 493–496.
Definujeme F_0=0,F_1=1,F_(n+2)=F_(n+1)+F_n. Rekurence zpětně
definuje i záporné indexy: F_(−n)=(−1)^(n+1)F_n.
Píšeme phi=(1+sqrt(5))/2, psi=(1−sqrt(5))/2=−1/phi;
oba kořeny splňují x²=x+1. Indexy jsou vždy celé.

## Matice, součet indexů a dělitelnost

Pro Q=[[1,1],[1,0]] platí pro všechna celá n

```text
Q^n=[[F_(n+1),F_n],[F_n,F_(n−1)]].                      (F1)
```

Při n=0 je to jednotková matice díky F_(−1)=1.
Násobení Q posouvá rekurenci a inverze Q je [[0,1],[1,−1]].
To dokazuje (5), úlohu 6 i záporné rozšíření. Determinant
dává F_(n+1)F_(n−1)−F_n²=(−1)^n, Cassiniho identitu.
Z Q^(n+m)=Q^n Q^m plyne

```text
F_(n+m)=F_m F_(n+1)+F_(m−1)F_n.                       (F2)
```

Obě rovnosti platí i se zápornými indexy (úloha 9).
Cassini znamená gcd(F_n,F_(n+1))=1 pro n>=0. Proto
F_(m+n),F_n mají stejné společné dělitele jako F_m,F_n.
Redukce m modulo n a Eukleidův algoritmus dokazují
gcd(F_m,F_n)=F_gcd(m,n) pro m,n>=0. Při m=n=0 se
použije gcd(0,0)=0, nebo se tento případ vynechá.
Dělitelnost F_n | F_(nk), n>=1,k>=0, plyne přímo z (F2).
Oprava F_k na F_n v okolním textu s. 81 je z 1999;
samotné F_k | F_(nk) je ovšem také pravda.

Úloha 7: složené n>4 má vlastní dělitel 2<d<n, tedy
1<F_d<F_n a F_d | F_n. Jediná složená výjimka je
n=4,F_4=3. n=0,1 nedávají prvočíslo F_n.

Opravená mez E2 je k−1 pro kladné vstupy nejvýše F_k,
k>1. Při m>=n a t>=2 děleních jde řetěz kladných
zbytků zpětně nejméně jako 1,2,3,5,...; větší vstup
je tedy aspoň F_(t+2). Při m<n první nulový podíl
přidá jeden krok, takže stačí F_(t+1). Jedno dělení
a vstupy 1,1 se ověří přímo. Tedy t<=k−1. Původní
k+1 bylo slabší pravdivé omezení; Légerova atribuce
zůstává samostatnou historickou otázkou.

## Generující funkce a uzavřený vzorec

Generující funkce je formální řada G(z)=sum_(n>=0)F_n z^n.
Její koeficient z^n uchovává F_n. Rekurence dává
(1−z−z²)G=z a rozklad jmenovatele pak

```text
G(z)=(1/sqrt(5))(1/(1−phi z)−1/(1−psi z)),
F_n=(phi^n−psi^n)/sqrt(5).                             (F3)
```

Formálně jsou jmenovatele invertibilní díky konstantě 1.
Analyticky obě geometrické řady konvergují pro |z|<1/phi;
poloměr je přesný kvůli pólu v 1/phi. Vzorec F_n platí
pro všechna celá n rekurencí v obou směrech.
Pro n>=0 je |psi^n/sqrt(5)|<1/2, takže F_n je nejbližší
celé číslo k phi^n/sqrt(5); tento obor byl doplněn 2021.
Při n=−1 zaokrouhlení dává 0, ale F_(−1)=1. Rozdíl
phi^n/sqrt(5)−F_n má kladné znaménko při sudém n a
záporné při lichém n, i pro záporné n (úloha 10).

Pro oba kořeny x=phi,psi indukcí v celých indexech platí

```text
x^n=F_n x+F_(n−1).                                    (F4)
```

To je úloha 11. Lucasova čísla definujeme
L_n=phi^n+psi^n=F_n+2F_(n−1). Rozklad G² v (16)
a koeficienty (1−xz)^−2 dávají pro n>=0

```text
sum_(k=0)^n F_k F_(n−k)
 = ((n+1)L_n−2F_(n+1))/5
 = ((n−1)F_n+2nF_(n−1))/5.                             (F5)
```

## Úlohy 1–5: počáteční údaje a růst

Po k měsících má popsaný model F_(k+2) párů, tedy
po roce F_14=377. Počet rytmů z délek 1,2 splňuje
rekurenci s hodnotami 1,1 pro délky 0,1, tedy je F_(n+1).
Historický původ modelů se tím neověřuje.
Program úlohy 3 udržuje dvojici (F_n,F_(n+1)) a nahrazuje
ji (F_(n+1),F_n+F_(n+1)). Invariant dokazuje správnost;
celočíselný výstup lze nezávisle porovnat s mocninou Q.
Binární varianta v `fibonacci_tools.py` používá důsledky (F2):
F_(2n)=F_n(2F_(n+1)−F_n), F_(2n+1)=F_n²+F_(n+1)².
Rekurzivní argument se půlí a končí dvojicí (0,1).
Logaritmy v odpovědi 2 a 209 číslic s první číslicí 4
jsou ověřeny zvlášť, bez používání float při generování.
F_n=n má řešení 0,1,5: začátek do 6 je přímý a od
F_6=8>6 zachovává rekurence ostrou nerovnost. F_n=n²
má řešení 0,1,12: začátek do 14 je přímý, F_13>13²
a F_14>14²; dále n²+(n+1)²>(n+2)² pro n>=13 dává indukci.

## Úlohy 12–15 a 39: nehomogenní rekurence

V rekurenci t_(n+2)=t_(n+1)+t_n+u_n je u_n přidaný
vstup v kroku n. Pro t_0=0,t_1=1 platí dosazením

```text
t_n=F_n+sum_(j=0)^(n−2)F_(n−1−j)u_j, n>=1.             (F6)
```

Při u_n=F_n je generující funkce G+zG² a (F5) dává
t_n=((3n+3)F_n−nF_(n+1))/5, včetně n=0. Oprava
značky G v odpovědi 12 je známá z 1998.
Homogenní řešení s a_0=r,a_1=s je rF_(n−1)+sF_n.
Při konstantním vstupu c odstraní posun b_n+c
nehomogenitu: b_n=cF_(n−1)+(c+1)F_n−c (úloha 13).
Linearita (F6) dává úlohu 15 včetně členu (1−x−y)F_n,
který vyrovnává tři počáteční hodnoty 1.

V úloze 14 definujme P_m(n)=sum_(j=0)^m C(n+j,m−j),
kde C je binomický koeficient. Pro n>=0 platí formálně
sum_(m>=0)P_m(n)w^m=(1+w)^n/(1−w−w²). Proto
P_m(n+2)−P_m(n+1)−P_m(n)=−C(n,m),
P_m(0)=F_(m+1),P_m(1)=F_(m+2). Výsledek je

```text
a_n=F_(m+n+1)+F_n−P_m(n).                              (F7)
```

Počáteční podmínky i rekurence jsou dokázány pro n>=0,m>=1.
Oprava 2006 pouze zkracuje původní dvě části pomocí (F2).
V úloze 39 kořeny 3,−2 dávají a_n=(3^n−(−2)^n)/5;
počáteční podmínky a rekurence se ověří dosazením.

## Úlohy 16–24: součty a determinant

Rozklady délky n na díly 1,2 mají při k dvojkách právě
C(n−k,k) pořadí, takže součet je F_(n+1), n>=0 (úloha 16).
Pro nenulová x,y a celé m,n,k platí roznásobením

```text
(x^(n+k)−y^(n+k))(x^(m−k)−y^(m−k))−(x^n−y^n)(x^m−y^m)
 =(xy)^n(x^(m−n−k)−y^(m−n−k))(x^k−y^k).
```

Dosazení phi,psi a dělení 5 dokazuje úlohu 17.
(F2) dává F_n²+F_(n+1)²=F_(2n+1), n>=0 (úloha 18).

Úloha 19: u=cos72°,v=cos36° splňují u=2v²−1,v=1−2u².
Jelikož u+v>0, jejich součet dává v−u=1/2, tedy
4v²−2v−1=0 a v=phi/2. Kladná znaménka sinusů dávají
sin36°=5^(1/4)phi^(−1/2)/2, sin72°=5^(1/4)phi^(1/2)/2.
Dodatek 2007: pro alpha=arctan(phi) z 1+phi²=sqrt(5)phi
plyne sin alpha=5^(−1/4)phi^(1/2), cos alpha=5^(−1/4)phi^(−1/2).
Vzorec dvojnásobného úhlu a správný kvadrant dávají
alpha=pi/4+(1/2)arctan(1/2).

Teleskopování F_k=F_(k+2)−F_(k+1) dává
sum_(k=0)^n F_k=F_(n+2)−1. Polynom S_n(x)=sum_(k=0)^n F_k x^k
splňuje pro n>=0

```text
(x²+x−1)S_n(x)=x^(n+1)F_(n+1)+x^(n+2)F_n−x.          (F8)
```

Při x²+x−1=0 je singularita podílu odstranitelná.
Derivace čitatele dělená 2x+1 je původní odpověď 21;
dosazení x²=1−x ji zjednoduší na opravu z 2004:
S_n(x)=(n+1−x^n F_(n+1))/(2x+1). Jmenovatel je nenulový.

Binomická věta a (F4) dávají pro n>=0 a celá m,t

```text
sum_(k=0)^n C(n,k)F_t^k F_(t−1)^(n−k)F_(m+k)=F_(m+tn).  (F9)
```

Mocnina s nulovým exponentem má polynomiální hodnotu 1
i při nulovém základu. t=2 je úloha 22; omezení n>=0
je právě oprava 2022. Determinant D_n z úlohy 24 splňuje
rozvojem prvního řádku D_n=D_(n−1)+D_(n−2), D_0=D_1=1,
tedy D_n=F_(n+1). Značka det doplněná 2017 je správná.

## Úlohy 25–28,31–33: kongruence a algebraické vztahy

Odečtení binomických rozvojů (1±sqrt(5))^n dává pro n>=0

```text
2^n F_n=2 sum_(1<=k<=n,k odd) C(n,k)5^((k−1)/2).        (F10)
```

Pro liché prvočíslo p zbude modulo p jen k=p;
Fermatova rovnost dává F_p=5^((p−1)/2) modulo p.
Pro p!=5 tedy F_p²=1 a Cassini dává F_(p−1)F_(p+1)=0
modulo p. Oba činitelé nemohou být nulové, protože
jejich rozdíl je F_p. Pro p=2 přímo F_1=1,F_3=2.

Z (F4) plyne F_(n+1)−phi F_n=psi^n. Poznámka odpovědi
28 je konečný součet a_n=sum_(j=0)^(n−1)A^(n−1−j)B^j,
n>=1; při A!=B je (A^n−B^n)/(A−B), jinak nA^(n−1).
a_0=0 se použije zvlášť. Polynomiální součet zahrnuje
i A=B=0 bez umělého dělení nulou.

Úloha 31 nyní plyne ze znaménka a velikosti psi^n:
F_(2n)phi mod 1=1−phi^(−2n),
F_(2n+1)phi mod 1=phi^(−2n−1), n>=0. První rovnost
je při n=0 také správná. x mod 1 znamená x−floor(x).

Pro úlohu 32 stačí n>=1,0<=r<n,m>=0. Modulo F_n je
Q^n=F_(n−1)I a F_(n−1)²=(−1)^n. Tedy
F_(mn+r)=F_(n−1)^m F_r modulo F_n. Dále (F2) dává
F_(n−1)F_r=(−1)^(r+1)F_(n−r) modulo F_n.
Čtyři třídy m modulo 4 jsou přesně čtyři řádky zadání.
Při n=1 je modul 1 a kongruence triviální.

Úloha 33: i²=−1,z=pi/2+i log phi. Z exponenciálních
definic cos z=−i/2,sin z=sqrt(5)/2!=0. Posloupnost
sin(nz)/sin z má hodnoty 0,1 a rekurenci
s_(n+1)=−i s_n−s_(n−1), stejně jako i^(1−n)F_n.
Identita tedy platí pro všechna celá n.

Úlohy 29–30 a 34–42 mají samostatné poznámky.
Historické odkazy nejsou těmito vlastními důkazy uzavřeny.

## Číselné výsledky a certifikát prvočísla

`check_fibonacci_basic.py` prošel jednou: 300 053 přesných
případů, včetně nezávislých maticových mocnin, 229 969
vstupů Eukleidova algoritmu a 492 rekurencí mocnin.
Výstup F_1,...,F_1000 je v `results/fibonacci-1-to-1000.txt`.
Racionální intervaly v `results/fibonacci-basic.json` dávají

```text
ln(phi^1000/sqrt(5)) = 480.4071061033863973104585337577553293154...
log10(F_1000)       = 208.6381552478107243668789586849176633358...
```

Zaokrouhlení knihy 480.40711 a 208.64 tedy souhlasí;
209 číslic a první 4 jsou ověřeny přímo z celého čísla.
Použité intervalové pomocné funkce z `check_gamma_constants.py`
neprovádějí při importu jeho staré testy; ty se neopakovaly.

Tvrzení hlavního textu, že N=2^127−1 je prvočíslo,
má uložen certifikát `results/mersenne127-prime-certificate.json`.
Obsahuje 19 rekurzivních uzlů. Pro každý uzel N>2 je
rozloženo N−1 na mocniny menších prvočísel q a pro každé q
uloženo celé a takové, že

```text
a^(N−1) = 1 (mod N),
gcd(a^((N−1)/q)−1,N)=1.                               (F11)
```

Vysvětlení platnosti certifikátu: pro prvočíselného dělitele
p čísla N je řád a modulo p (nejmenší kladná mocnina dávající 1)
dělitelem N−1 i p−1. Druhá podmínka (F11) vynucuje, aby
řád obsahoval celou q-mocninu z N−1. Platí to pro každé q,
tedy N−1 dělí p−1, což dává p>=N a nutně p=N.
Prvočíselnost menších q se dokazuje týmž postupem až k 2.
SymPy sloužilo pouze k nalezení rozkladů; samostatný validátor
ověřil jejich součiny, rekurzivní uzly, modulární mocniny i gcd
v celočíselné aritmetice. Historická atribuce Lucasovi tím
ověřena není.

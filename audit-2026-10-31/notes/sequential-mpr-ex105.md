# MPR105: náhodná procházka, všechny GF, derivace a Chebyshevův dovětek

7. listopadu 2026. Celé zadání p22/file42 a odpověď p385–386/
files405–406 přímo zobrazeny; autorský PS11.9.2019 p22/file28
a p42/file48 rovněž. Žádná stará kontrola105 se nepřebírá jako
uzavřený důkaz. Všech šest vrstev errat a tři TeX zdroje prohledány:
žádná použitelná oprava105, podrobnosti v manifestu. Změna
Fascicle6 answer304 výslovně používá jiné, vychýlené přechody;
není opravou zdejší férové procházky. Žádný nový výpočet nebo běh.

## Model, ukončení, symetrie a jednoznačnost

Náhodné bity jsou férové, kroky±1 nezávislé. Počet stavů n je
kladný, jak požaduje n-cyklus a operace modulo n; n0 by vůbec
nedefinovalo zadání. Počáteční a je celé,0≤a≤n. Pro a0 nebo n
je první zásah v čase N0. Pro0<a<n lze před prvním zásahem
uvažovat obyčejnou procházku na celých číslech, zastavenou při
dosažení0 nebo n: krok±1 nemůže žádnou z těchto hranic přeskočit.
To je ekvivalentní prvnímu zásahu násobku n na původním cyklu.

Z libovolného vnitřního stavu n po sobě jdoucích kroků−1
zajistí zásah nejpozději během tohoto bloku. Podmíněná
pravděpodobnost takového bloku je2^−n, nezávisle na minulosti.
Proto P(N>kn)≤(1−2^−n)^k. N je konečné skoro jistě a má
exponenciální moment: pro R>1 dost blízké1, aby
R^n(1−2^−n)<1, lze E R^N shora omezit geometrickou řadou
Σ_k≥0 R^((k+1)n)(1−2^−n)^k. PGF g_a(z) je tedy analytická
v okolí z1, nikoli jen formální, a oba momenty lze derivovat.

Záměna všech znamének kroků posílá počáteční a na n−a a
zachovává férový zákon i čas zásahu, tedy g_a=g_(n−a).
Podmínění prvním krokem dává všechny rovnice

```
g_0=g_n=1,
g_a=(z/2)(g_(a−1)+g_(a+1)) pro0<a<n.
```

Tím je doložen i úvod odpovědi na p385. Pro|z|<1 mají rovnice
jediné řešení: rozdíl dvou řešení má nulové hraniční hodnoty;
maximum jeho absolutních hodnot M splňuje M≤|z|M, tedy M0.
Počáteční podmínky, středové symetrie a všechny racionální výrazy
níže proto skutečně určují zákon procházky.

## Sudé n=2m

Položme t_0=t_1=1 a t_(k+1)=2t_k−z²t_(k−1) pro k≥1.
Pro0≤a≤m navrhujeme g_a=z^a t_(m−a)/t_m a pro zbývající
a použijeme symetrii. Máme g0=1 a
g_m=z^m/t_m=z g_(m−1), protože t0=t1=1. To je správná
rovnice uprostřed: oba sousedé m−1,m+1 mají stejnou GF.
Pro0<a<m položme k=m−a. Pak

```
(z/2)(g_(a−1)+g_(a+1))
 = z^a(t_(k+1)+z²t_(k−1))/(2t_m)
 = z^a t_k/t_m = g_a.
```

Všechny rovnice jsou tedy splněny. Pro m≥1 má t_m(0)=2^(m−1),
takže poměr skutečně definuje formální PGF u nuly. Zároveň t_m(1)=1,
jak hned plyne z rekurence s oběma počátečními hodnotami1.
Identita s pravou PGF platí nejprve tam, kde jsou jmenovatele
nenulové, a všude jinde s případnou odstranitelnou singularitou.
V okolí1 je jmenovatel nenulový, takže výpočet momentů je legitimní.

Nechť D=1−2w+z²w². Násobením rekurence w^(k+1) a sečtením
formálních řad vzniká přesně

```
T(w)=Σ_(m≥0)t_m w^m=(1−w)/D.
```

Jde o řadu v w s polynomiálními koeficienty v z; diferenciace po
z a extrakce jednotlivého koeficientu jsou proto přímo oprávněné.
Při z1 platí

```
T(w)=1/(1−w),
T_z(w)=−2w²/(1−w)³,
T_zz(w)=−2w²/(1−w)³+8w⁴/(1−w)⁵.
```

Identita [w^r](1−w)^−s=binom(r+s−1,s−1) plyne například
s−1 derivacemi geometrické řady a platí i s nulovými koeficienty
pro záporné r. Dostáváme pro každé m≥0

```
t_m(1)=1,
t_m′(1)=−2 binom(m,2)=−m(m−1),
t_m″(1)=−2 binom(m,2)+8 binom(m,4)
        =m(m−1)(m²−5m+3)/3.
```

Tím jsou odvozeny oba tištěné výrazy, včetně malých m. Pro libovolný
polynom v s v(1)=1 definujme K(v)=v″(1)+v′(1)−v′(1)².
Dosazením posledních dvou výrazů získáme
K(t_m)=2(m²−m⁴)/3, přesně další tištěný mezikrok.

Logaritmická derivace g_a dává
EN=a+t_(m−a)′(1)−t_m′(1)
=a−(m−a)(m−a−1)+m(m−1)=a(2m−a)=a(n−a).
Pro PGF s g(1)=1 platí VarN=(ln g)″(1)+(ln g)′(1).
Příspěvky a ln z se zde zruší. Proto

```
VarN = K(t_(m−a))−K(t_m)
     = (2/3)((m−a)²−(m−a)⁴−m²+m⁴).
```

Označme k=m−a,b=n−a. Pak ab=m²−k² a
a²+b²=2m²+2k². Poslední výraz tedy je
(2/3)(m²−k²)(m²+k²−1)
=(a²+b²−2)ab/3, přesně tištěná finální variance.

## Liché n=2m−1

Nyní u0=1,u1=z,u_(k+1)=2u_k−z²u_(k−1). Pro0≤a≤m je
g_a=z^a u_(m−a)/u_m; zbytek opět určuje symetrie. Vnitřní
rekurence se ověřuje stejnou výše zapsanou substitucí s u místo t.
Středová podmínka je tentokrát g_m=g_(m−1), protože n−m=m−1.
Skutečně g_m=z^m/u_m a
g_(m−1)=z^(m−1)u1/u_m=z^m/u_m. Rovnice v m−1 a m jsou
tím současně zajištěny; n1 je níže ošetřeno zvlášť.

Pro m≥1 má u_m faktor z a u_m/z má při z0 hodnotu2^(m−1).
To plyne indukcí z rekurence, neboť u1/z=1 a další konstantní
koeficient se vždy zdvojnásobí. Pro a<m se tento faktor ruší
s u_(m−a); pro a=m zůstane z^(m−1)/(u_m/z). Všechny poměry
tedy mají odstranitelnou hodnotu při z0 a určují řádné formální
řady. Ze stejných počátečních hodnot při z1 plyne u_m(1)=1.
Jednoznačnost a analytická argumentace jsou stejné jako v sudém
případě; žádná hodnota PGF není definována dělením0/0.

Sečtení rekurence v w dává

```
U(w)=Σ_(m≥0)u_m w^m=(1+(z−2)w)/D.
```

Nyní derivujeme i čitatel. Při z1 jsou výsledky

```
U(w)=1/(1−w),
U_z(w)=w/(1−w)²−2w²/(1−w)³,
U_zz(w)=−4w³/(1−w)⁴−2w²/(1−w)³+8w⁴/(1−w)⁵.
```

Odtud pro každé m≥0

```
u_m′(1)=m−2 binom(m,2)=−m(m−2),
u_m″(1)=−4 binom(m,3)−2 binom(m,2)+8 binom(m,4)
        =m(m−1)(m²−7m+7)/3.
```

To jsou obě tištěné derivace. Pro úplné doložení následného
„it follows“ vypíšeme i chybějící algebraický krok:

```
K(u_m)=(−2m⁴+4m³−m²−m)/3
      =(2/3)((m−1/2)²−(m−1/2)⁴)−1/8.
```

Průměr z logaritmické derivace je
a−(m−a)(m−a−2)+m(m−2)=a(2m−1−a)=a(n−a).
Pro varianci odečteme K(u_m) od K(u_(m−a)). Položme M=m−1/2,
k=M−a,b=n−a. Konstanty−1/8 se zruší, ab=M²−k² a
a²+b²=2M²+2k². Stejným faktorizováním dostáváme
VarN=(a²+b²−2)ab/3 pro celý lichý případ.

V obou paritách symetrické finální výrazy pokrývají také a>n/2.
Pro a0 či n dávají EN=VarN=0, jak musí. Pro n1 jsou oba přípustné
starty už v nule modulo1; m1,u1=z a oba poměry se ruší na1,
takže N0. Pro n2 a1 je g1=z, N1 deterministicky, EN1,VarN0.
Tím jsou pokryty i nejmenší smysluplné moduly a degenerované starty.

## Každá identita Chebyshevova dovětku

Z kosinového a sinového součtového vzorce plyne, že funkce
T_m(cosθ)=cos(mθ) a U_m(cosθ)=sin((m+1)θ)/sinθ splňují
rekurenci W_(m+1)(x)=2xW_m(x)−W_(m−1)(x).
Počáteční hodnoty jsou T0=U0=1,T1=x,U1=2x. Rekurence proto
definuje polynomy na celém komplexním x; zdánlivé zlomky při
sinθ0 mají tyto polynomiální limitní hodnoty.

Kniha si výslovně zavádí V_m(cosθ)=cos((m−1/2)θ)/cos(θ/2).
Stejný kosinový vzorec dává tutéž rekurenci, s V0=V1=1.
Pro x≠0 výraz
R_m=(2−1/x)T_m+(1/x−1)U_m rovněž splňuje tutéž rekurenci;
R0=1 a R1=(2−1/x)x+(1/x−1)2x=1. Indukcí tedy R_m=V_m.
Proto i tištěná kombinace s1/x má při x0 odstranitelnou
singularitu a hodnotu právě polynomu V_m. Při cos(θ/2)=0
platí stejné polynomiální prodloužení. Žádná konvence běžného
jména V není potřeba: autor jeho indexaci přímo definuje.

Nakonec z_m=z^mT_m(1/z) splňuje
z_(m+1)=2z_m−z²z_(m−1),z_0=z_1=1, a proto z_m=t_m.
Stejně z^mV_m(1/z) má počáteční hodnoty1,z a tutéž rekurenci,
takže je přesně u_m. Obě identity jsou nejprve pro z≠0 a pak
jako polynomiální identity i při z0. Tím je celý dovětek včetně
každého tištěného zlomku a okraje doložen.

Celá105 je checked. Žádný nález, kandidát, nová známá oprava ani
bibliografická výjimka; žádná numerická reprodukce nebo restart.
Stránku406 to samo neuzavírá:106–109 zůstávají samostatnou prací.

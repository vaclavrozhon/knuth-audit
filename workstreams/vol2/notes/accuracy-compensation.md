# §4.2.2-19 a30: kompenzované sčítání a citlivý kalkulační příklad

Původní zadání244–245 a odpověď615–616 byly vizuálně přečteny.
Použity opravy2003,2007 a2021: předmětem meze je skutečný rozdíl
s_n−c_n, nikoli pouze s_n. Závěrečné dodatečné zaokrouhlení tohoto
rozdílu není součástí formulované identity. Všechny čtyři vrstvy errat
jsou zahrnuty. Číselné výpočty používají přesné zlomky.

## 1. Význam chyb a přesná rekurze

Kahanova rekurze je y_k=(x_k−c_(k−1))(1+η_k),
s_k=(s_(k−1)+y_k)(1+σ_k),
c_k=((s_k−s_(k−1))(1+γ_k)−y_k)(1+δ_k), s0=c0=0.
Všechna čtyři řecká písmena značí relativní chyby jednotlivých
operací, v absolutní hodnotě nejvýše ε. Nevyžaduje se konkrétní
pravidlo zaokrouhlování. Po výpočtu chyby zafixujeme; soustava se
pak stává lineární v x_k a lze sledovat koeficient každého vstupu.
Koeficienty samy mohou na daném výpočtu záviset, což požadované
zpětné vyjádření nevylučuje.

Pro jeden již vložený vstup x_j nechť f,g jsou jeho koeficienty
v s−c a c. Následující krok, v němž x_j není přidáván znovu, má tvar

```text
f_new = A f+B g,             g_new = C f+D g,
A = 1−σ(γ+δ+γδ),
B = γ−η+γη+δγ+δγη+δησ+ησγ+δησγ,
C = σ(1+γ)(1+δ),
D = −(1+δ)(γ+γη+ησ+γησ).
```

Při samotném vložení x_j jsou koeficienty

```text
F = (1+η)(1−γ−γδ−γσ−δσ−γδσ),
G = (1+δ)(1+η)(γ+σ+γσ).
```

Přímé dosazení do tří původních rovnic tyto identity dokazuje.
Nezávislé symbolické rozepsání v `verify_accuracy_compensation.py`
ověřilo všech šest polynomů, přesně včetně znamének tištěné odpovědi.
Hlavní rekurze odpovědi je správná.

## 2. Výslovná mez zbytku

Předpokládejme 0<=ε<=1/10. Z předchozích polynomů přímo plyne

```text
|F−(1+η−γ)| <= 5ε²,       |G| <= 3ε,
|A−1| <= 2.1ε²,          |B| <= 2.3ε,
|C| <= 1.21ε,            |D| <= 1.331ε.
```

Například první zbytek je −ηγ−(1+η)(γδ+γσ+δσ+γδσ),
tedy nejvýše (4+4ε+ε²)ε²<=5ε². Ostatní meze jsou součty absolutních
hodnot jednotlivých členů; |D|<=ε(1+ε)^3.

Položme H0=1+2ε+5ε². Při vložení platí |f|<=H0 a |g|<=3εH0.
Pokud |f|<=H a |g|<=3εH, další krok dává

```text
|f_new−f| <= (2.1+3·2.3)ε²H = 9ε²H,
|g_new| <= (1.21+3·1.331ε)εH < 3εH.
```

Indukcí tedy |f|<=H_m=H0(1+9ε²)^m a |g|<=3εH_m po m dalších
krocích. Teleskopováním skutečných změn f dostáváme

```text
|f_final−1| <= 2ε+5ε²+H0((1+9ε²)^m−1),   m=n−j.
```

To je explicitní konečná mez bez skrytého členu. Pokud navíc
(m+1)ε²<=1/100, použijeme H0<=5/4 a
(1+t)^m<=exp(mt)<=1/(1−mt) pro mt<1. Výsledkem je

```text
|f_final−1| <= 2ε+13(m+1)ε².
```

Proto s_n−c_n=Σ_j(1+θ_j)x_j s
|θ_j|<=2ε+O((n+1−j)ε²), a také slabší tištěná mez2ε+O(nε²).
Konstanta i režim platnosti jsou nyní výslovné. Hlavní tvrzení úlohy19
po zapracování známých oprav platí.

## 3. Drobné počítání kvadratických členů

Odpověď615 tvrdí, že rozvoj f_n obsahuje „4n terms of 2nd order“.
Pro n1 skutečně vycházejí čtyři členy. Pro n>=2 je však homogenní
část celkového stupně2 rovna

```text
−η1γ1−γ1δ1−γ1σ1−δ1σ1
+ Σ_(k=2)^n (−γkσk−δkσk+(γk−ηk)σ_(k−1))
+ (γ2−η2)γ1.
```

Po úplném roznásobení jde o4n+2 různých nenulových monomů,
nikoli4n. Už n2 dává deset místo osmi. Poslední dva členy pocházejí
z počátečního g1=γ1+σ1+O(ε²); pro k>=2 už g_k=σ_k+O(ε²).
Přesný symbolický výpočet n1..8 dal počty4,10,14,18,22,26,30,34.
Jde o drobnou chybu doslovného počtu členů, **nikoli o selhání
asymptotické meze nebo Kahanovy metody**. Samostatný záznamC0086.

## 4. Úloha30: význam experimentu

Tištěný polynom má stupeň106 a107 členů:
f(x)=Σ_(k=0)^106 x^k=(1−x^107)/(1−x), pro x≠1.
Jde o exponenty106/107, nikoli o10^6/10^7.
Dosazený argument je

```text
x(y)=(1/3−y²)(3+3.45y²)=1−(37/20)y²−(69/20)y^4.
```

Pro h=x−1 platí f(1+h)=Σ_(k=0)^106 binom(107,k+1)h^k,
protože Σ_(j=k)^106 binom(j,k)=binom(107,k+1).
Rozvoj až do y^6 tak dává přesně všechny čtyři tištěné koeficienty:
107,−10491.35,659749.9625,−30141386.26625. Symbolická kontrola souhlasí.

Experiment provádíme v deklarovaných desetinných modelech s8,10 a12
ciframi, se správným zaokrouhlením každé operace. Nejde o měření
fyzických kalkulaček ani tvrzení o konkrétní dnešní značce.
Pro y=10^(−3),...,10^(−6) se porovnají tři postupy:

- podíl s jednou správně zaokrouhlenou operací x^107;
- stejný podíl, ale mocnina se získá opakovaným čtvercováním
  s odděleně zaokrouhlenými násobeními;
- Hornerova rekurze 106krát h←R(R(hx)+1), počínaje h=1.

Argument x se v každém modelu počítá ze zadaného rozkladu včetně
zaokrouhleného1/3. Přesná reference používá skutečné racionální y
ve skutečném polynomu. Chyba se rozděluje na f(x_rounded)−f(x_exact)
a chybu samotného vyhodnocení při již zaokrouhleném argumentu.
První složka je přibližně f'(1)·chyba(x), kde f'(1)=5671;
malý jmenovatel1−x při podílovém výpočtu naproti tomu zvětšuje
absolutní chybu zaokrouhlené mocniny asi faktorem1/|1−x|.
Je-li zaokrouhlený x=1, podílový zápis vede na0/0, ačkoli polynom
má dobře definovanou hodnotu107. Hornerova rekurze tuto singularitu
zápisu nemá. Vstupní citlivost od následného vyrušení rozlišujeme.

Číselné výsledky a rozklad chyb jsou uložené v JSON. Všech12 experimentů
a oba symbolické bloky dokončeny s exit0. Přehled výsledků:

| Cifer | y | Podíl, přesná mocnina pak R | Podíl, čtvercování | Horner |
|---|---|---|---|---|
| 8 | 0.001 | 106.98936 | 106.99468 | 106.98934 |
| 8 | 0.0001 | 107 | 107 | 106.9998 |
| 8 | 0.00001 | 107 | 107 | 106.99995 |
| 8 | 0.000001 | 107 | 107 | 106.99995 |
| 10 | 0.001 | 106.9895141 | 106.9895141 | 106.9895089 |
| 10 | 0.0001 | 107 | 107 | 106.9998934 |
| 10 | 0.00001 | 107 | 107 | 106.999998 |
| 10 | 0.000001 | 107 | 107 | 106.9999995 |
| 12 | 0.001 | 106.989509212 | 106.989515698 | 106.989509307 |
| 12 | 0.0001 | 106.999891898 | 106.999945949 | 106.99989508 |
| 12 | 0.00001 | 107 | 107 | 106.999998934 |
| 12 | 0.000001 | 107 | 107 | 106.99999998 |

Například při8 cifrách a y=.001 je přesný výsledek106.9895093097...,
ale podíl po čtvercování dává106.99468. Pro y=.0001 a8 cifrách
je výsledek podílu107, zatímco přesná hodnota je106.9998950865... .
Mocnina se při malém1−x zaokrouhlí tak, že její rozdíl od1 přesně
odpovídá107násobku jmenovatele; nelineární korekce se ztratí. Jednotlivé vytištěné desetinné chyby jsou
přibližné reprezentace přesných zlomků, nikoli intervalové certifikáty.

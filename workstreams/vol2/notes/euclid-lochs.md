# §4.5.3: Lochsův čtvercový průměr

Kontrola 3. listopadu 2026. Historický dodatek z 13. ledna 2000
na str. 372 je správný, včetně konstanty a zbytku O(N^(-1/2)).
Původní článek Gustav Lochs, *Statistik der Teilnenner der zu den
echten Brüchen gehörigen regelmäßigen Kettenbrüche*,
Monatshefte für Mathematik 65 (1961), 27–52, byl získán z GDZ
a všech 26 stran bylo vizuálně přečteno. PDF obsahuje navíc
úvodní stránku; jeho textová vrstva není OCR článku.
Původní pramen má několik vlastních tiskových vad, které
nepřičítáme Knuthově knize.

## 1. Přesný převod počítání

Pro kladná celá u,v označuje T(u,v) knižní počet všech dělení,
včetně případného počátečního nulového podílu. Pro 1<=z<n
nechť s(z/n) je počet nenulových podílů v kanonickém rozvoji
[0;a_1,...,a_s] s posledním a_s>=2. Lochsův součet h(N)
zahrnuje všechny dvojice 1<=z<n<=N, i nesoudělné:

```
h(N)=sum_(1<=z<n<=N) s(z/n).
```

Platí T(n,z)=s(z/n), T(z,n)=s(z/n)+1 a T(n,n)=1.
Součet nad celým čtvercem se tedy přesně rovná

```
sum_(1<=u,v<=N) T(u,v)=2h(N)+N(N+1)/2.              (L1)
```

Tentýž součet je Lochsovo H(N): oba konečné zápisy každého
pravého zlomku mají délky s a s+1, navíc jsou zahrnuty
N zápisy [0;1] na diagonále. Například h(4)=8 a H(4)=26,
jak uvádí původní str. 27–28. Není zde podmínka gcd=1.

## 2. Původní asymptotika a její zbytek

Položme zeta(s)=sum_(j>=1)j^(-s) pro s>1; gamma je Eulerova
konstanta a zeta'(2) derivace zeta v bodě 2. Lochsovo k(1)
je rychle konvergentní konstanta definovaná jeho (5.8)/(5.9);
její potřebnou hodnotu odvodíme přesně v oddílu 3.
Jeho (1.5)/(1.7) na str. 29 zní

```
h(N)=(ln2/zeta(2))N^2 ln N+d_0 N^2+O(N^(3/2)),
d_0=-1/2 + { -ln2(ln2+3-4gamma+2zeta'(2)/zeta(2))
              +zeta(2)/2+zeta(3)/4-k(1) }/(2zeta(2)). (L2)
```

Článek odvozuje nejprve počet výskytů jednotlivého podílu b.
Kombinatorický krok převádí oba zápisy na vážené řešení

```
b x u+x v+y u<=N,
x,u>=1, 0<=y<=x, 0<=v<=u, gcd(u,v)=1.
```

Vnitřní volby mají násobnost 2 a krajní 1. Möbiova inverze
v §6 odstraní gcd; §7 spočítá krajní poslední podíly a §8
oddělí kanonické zápisy. Zkontrolováno je zejména, že
L(N,b) počítá poslední podíly **obou** druhů zápisů.
Pro b>1 je H(N,b)=2h(N,b)+L(N,b+1)-L(N,b); při b=1 je
místo rozdílu součet L(N,1)+L(N,2). To vysvětluje dodatečný
člen -N^2/2 v (L2), který by se prostým dělením dvěma ztratil.

Uniformní zbytky (1.2)/(1.3) jsou

```
O(N^(3/2)b^(-5/2)+N ln N),
O(N^2 b^(-3) ln N+N^(4/3)b^(-4/3)).
```

Při součtu přes 1<=b<=N použijeme první odhad do N^(1/3),
druhý nad tímto prahem. První součet je
O(N^(3/2)+N^(4/3)ln N); druhý
O(N^(4/3)ln N+N^(11/9)). Ocas hlavních koeficientů nad N
je O(N ln N). Dohromady tedy O(N^(3/2)), jak žádá (L2).
V sazbě §8 na str. 44 je v jedné pomocné teleskopické rovnosti
obráceno znaménko f(2)-f(1); výsledek (1.5) používá správný
rozdíl f(1)-f(2).

Čtení celého pramene a ověření tohoto převodu není prohlášení,
že každý pomocný analytický odhad článku byl odvozen znovu.
Citovanou původní asymptotiku (L2) používáme jako externí větu;
přesný převod, součet jejích uniformních chyb a identifikace
konstanty zde mají vlastní důkazy. Nepotřebná část §10
o komplexních singularitách k nebyla samostatně auditována.

## 3. Vlastní přesná identita pro k(1)

Lochsův první vzorec §10 na str. 45 dává pro b=1

```
-k(1)+zeta(3)/4 = 4K,
K=sum_(x>=1) { (H_(2x)-H_x-ln2)/x+1/(4x^2) },        (L3)
```

kde H_m=sum_(j=1..m)1/j je harmonické číslo. Člen 1/(4x^2)
pochází z polovičních vah obou krajů y=0 a y=x.

Přesný zbytek střídavé logaritmické řady je

```
ln2-(H_(2x)-H_x)=integral_0^1 t^(2x)/(1+t) dt.
```

Všechny členy napravo jsou nezáporné. Lze proto zaměnit
součet s integrálem a získat

```
sum_(x>=1) (H_(2x)-H_x-ln2)/x
 = integral_0^1 ln(1-t^2)/(1+t) dt
 = -Li_2(1/2)+(ln2)^2/2
 = (ln2)^2-zeta(2)/2.
```

Zde Li_2(z)=sum_(j>=1)z^j/j^2 pro 0<=z<=1. Identitu
Li_2(z)+Li_2(1-z)=zeta(2)-ln z ln(1-z) lze ověřit
derivací na (0,1) a limitou v 0; v bodě 1/2 dává poslední
rovnost. Všechny integrály konvergují, takže (L3) dává přesně

```
k(1)=zeta(2)+zeta(3)/4-4(ln2)^2.                     (L4)
```

Dosazením do (L2) a následně (L1) dostaneme

```
(1/N^2) sum T(u,v) = (12ln2/pi^2)ln N+D+O(N^(-1/2)),
D=2d_0+1/2
 =(6ln2/pi^2)(3ln2+4gamma-12zeta'(2)/pi^2-3)-1.       (L5)
```

Je to přesně knižní (62), nikoli jen číselná shoda. Dřívější
rigorózní certifikát v euclid-discrete.json dává
D=0.0653514259..., tedy d_0=-0.2173242870... .
Lochsovo tištěné -0.21807 v (1.6) je proto nesprávný číselný
přepočet, zatímco jeho analytické (1.5) souhlasí.
Také záporné 2a_2 v tabulce na str. 38 odporuje vlastní
definici (5.8): přímo z (5.3) vyjde
R_2(x)=-(8/15)x^(-5), a_2=(8/15)zeta(5)>0.

Žádný z těchto problémů původního článku není nový nález
v TAOCP. Dodatek2000 s přibližným D=0.065 je správný.
Nebyl spuštěn nový numerický test; argument (L4)/(L5) je přesný
a již hotové číselné certifikáty nebyly opakovány.


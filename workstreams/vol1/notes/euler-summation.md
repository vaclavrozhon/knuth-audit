# §1.2.11.2: Eulerův vzorec, Bernoulliho polynomy a zbytek

Audit 1. listopadu 2026. Zobrazeny s.111–116, odpovědi 503–504
a změny z 21. března 2021. Níže jsou oba významy Bernoulliho čísel
výslovně odděleny. Pracujeme s dostatečně hladkou reálnou funkcí f
na [a,b], kde a<=b jsou celá čísla. Pro vzorec se zbytkem řádu m
stačí, aby f^(m−1) byla absolutně spojitá a f^(m) integrovatelná;
pro jednoduchost lze všude předpokládat spojité potřebné derivace.

## Čísla, polynomy a úlohy 1–2

Definujeme čísla b_j první konvence, současná čísla B_j a stejné
Bernoulliho polynomy P_j(x) jejich exponenciálními generujícími řadami:

```text
z/(exp(z)−1)       = sum b_j z^j/j!,
z/(1−exp(−z))      = sum B_j z^j/j!,
z exp(xz)/(exp(z)−1) = sum P_j(x) z^j/j!.                 (E1)
```

Tyto řady jsou analytické u 0 po odstranění zdánlivé singularity.
Platí B_j=(−1)^j b_j, protože druhá řada je první s argumentem −z.
Jejich rozdíl je z, takže odlišnost nastává jen u indexu 1:
b_1=−1/2,B_1=1/2. Násobení jmenovatelem dává
B_0=1,B_2=1/6,B_3=0,B_4=−1/30. Funkce
`z/(1−exp(−z))−z/2` je sudá, tedy B_(2j+1)=0 pro j>=1.
To dokazuje (4)–(6) v obou konvencích.

Protože `F(z)exp(−z)=F(z)−z` pro F(z)=z/(1−exp(−z)),
porovnání koeficientů dává současnou (7), a tím úlohu 1:

```text
sum_{k=0}^n binom(n,k)(−1)^(n−k) B_k = B_n−[n=1].       (E2)
```

Symbol [n=1] je 1 pro n=1 a 0 jinak. Pro původní b_j
vznikne analogicky `sum binom(n,k)b_k=b_n+[n=1]`.
Z (E1) jsou oba současné zápisy (8) totožné:

```text
P_m(x) = sum binom(m,k) B_k (x−1)^(m−k)
       = sum binom(m,k)(−1)^k B_k x^(m−k).               (E3)
```

Polynomy P_m se přechodem na B_1=+1/2 **nemění**; zejména
P_1(x)=x−1/2, P_m(0)=b_m a P_m(1)=B_m. Přímým derivováním
nebo z (E1) vyjdou pro m>=1 následující rovnosti; symetrie
ve třetím řádku platí také pro m=0:

```text
P'_m=m P_(m−1),
P_m(x+1)−P_m(x)=m x^(m−1),
P_m(1−x)=(−1)^m P_m(x).                                (E4)
```

Pro m>=2 mají P_m(1)=P_m(0), takže funkce P_m({x}) je
spojitá i v celých bodech; {x}=x−floor(x) je zlomková část.
Pro úlohu 2 samotná derivační rekurence nestačí: potřebujeme
P_1=x−1/2 pro počáteční krok a shodu krajních hodnot všech
následujících P_m, aby při integraci po částech nezůstaly
vnitřní hraniční členy. Tyto podmínky určují posloupnost jednoznačně:
P_1 určí počátek a rovnost P_(m+1)(1)=P_(m+1)(0) vynucuje
integrál P_m na [0,1] nulový. Tím se postupně určí integrační
konstanta každého P_m. Dodatek k odpovědi 2 z roku 2024
správně uvádí i nezbytný počáteční polynom.

## Odvození (2)–(3), (9)–(11)

Na každém intervalu [k,k+1] integrace po částech dává

```text
integral_k^(k+1) (x−k−1/2) f'(x) dx
 = (f(k+1)+f(k))/2 − integral_k^(k+1) f(x) dx.           (E5)
```

Hodnota zlomkové části v jednom koncovém bodě nemění integrál;
hraniční hodnoty v (E5) pocházejí ze spojitého polynomu x−k−1/2
na celém daném intervalu. Sečtení (E5) a postupné použití (E4)
dává pro celé m>=1 současnou formu:

```text
sum_{k=a}^b f(k)
 = integral_a^b f(x)dx + f(a)
   + sum_{j=1}^m B_j/j! (f^(j−1)(b)−f^(j−1)(a)) + R_m(a,b),
R_m(a,b) = (−1)^(m+1)/m! integral_a^b P_m({x})f^(m)(x)dx. (E6)
```

Pro m=1 se první dva hraniční členy spojí na (f(a)+f(b))/2,
což je opravená (3). Ve staré konvenci se sečítá a<=k<b
a není samostatné f(a): odečtením f(b) z (E6) se přesně
změní B_1 na b_1. Všechny vyšší členy a zbytek zůstanou stejné.
Tím je ověřena i konzistence změn obrázku 12 a mezí součtu z 2021.

## Velikost a znaménko zbytku, (12)–(13), úloha 3

Fourierova řada periodického polynomu, již odvozená integrací
po částech v [gamma-functions.md](gamma-functions.md), je pro sudé
m=2l>=2 absolutně a stejnoměrně konvergentní:

```text
P_m(t) = (−1)^(l+1) 2m!/(2pi)^m sum_{j>=1} cos(2pi jt)/j^m.
                                                               (E7)
```

Proto |P_m(t)|<=|B_m| a
`|B_m|/m!=2 zeta(m)/(2pi)^m<4/(2pi)^m`.
Zde zeta(m)=sum j^(−m)<2 pro m>=2, například srovnáním
ocasu od j=2 s integrálem x^(−m) na [1,infinity).
To dokazuje celou (12), včetně ostré druhé nerovnosti.

Položme `C_m(a,b)=B_m/m! (f^(m−1)(b)−f^(m−1)(a))`.
Má-li f^(m) konstantní znaménko, z (E6) a (E7) dostaneme

```text
|R_m(a,b)| <= |B_m|/m! integral_a^b |f^(m)(x)|dx
           = |C_m(a,b)|.                               (E8)
```

To je přesná **neostrá** nerovnost úlohy 3. Zahrnuje nulové
derivace i a=b; záměna za ostrou nerovnost v pomocném Markdownu
by byla chybná. Potřebná derivace je m-tá, nikoli (m+1)-ní.

Pro doplňující část odpovědi 3 ověříme maximum rozdílu
`|B_m−P_m(t)|` na [0,1]. Z (E1) plyne
`P_m(1/2)=(2^(1−m)−1)B_m`. Pro m=2 se maximum v 1/2
ověří z P_2(t)=t²−t+1/6. Pro m>=4 má derivace normalizované
řady P_m(t)/B_m na 0<t<1/2 záporné znaménko. Skutečně pro
theta=2pi t a p=m−1>1 je

```text
sum_{j>=1} sin(j theta)/j^p
 = 1/Gamma(p) integral_0^infinity
   u^(p−1) exp(−u) sin(theta)/(1−2exp(−u)cos(theta)+exp(−2u)) du > 0.
                                                               (E9)
```

Záměna řady a integrálu je oprávněna absolutní konvergencí
sum j^(−p). Symetrie z (E4) pokrývá druhou polovinu intervalu.
Tedy poměr `(B_m−P_m(t))/B_m` leží mezi 0 a 2−2^(1−m),
s kladnou hodnotou pro necelé t. Pro m>=4 pak

```text
R_(m−2)=C_m+R_m
 = 1/m! integral_a^b (B_m−P_m({x}))f^(m)(x)dx.           (E10)
```

Při konstantním znaménku f^(m) je R_m/C_m mezi −1 a
1−2^(1−m), pokud C_m!=0; nulový případ plyne přímo.
To dokazuje i silnější neostrý interval z knižní odpovědi.

Konečně nechť m>=2 je sudé, a<b a
`f^(m+2)(x) f^(m+4)(x)>0` pro a<x<b, jak požaduje (13).
Obě derivace mají stejné pevné nenulové znaménko. Z (E10),
jednou s m+2 a podruhé s m+4, mají R_m a R_(m+2) znaménka
C_(m+2), respektive C_(m+4). Ta jsou opačná, protože sousední
sudá Bernoulliho čísla mají opačná znaménka. Současně
R_m=C_(m+2)+R_(m+2). Odtud přesně

```text
R_m = theta C_(m+2),   0<theta<1.                        (E11)
```

Při a=b je rovnost triviální s libovolným theta v (0,1).
Tím je (13) skutečně dokázána; samotné (E8) by nedokazovalo
znaménko ani odhad prvním vynechaným členem. Opravy formulace
z let 2013 a 2024 správně mluví o absolutní hodnotě a prvním
**nenulovém** vynechaném členu.

## Úloha 4: součty mocnin včetně m=0

Po změně 2021 je `S_m(n)=sum_{k=0}^n k^m`, pro celá m,n>=0,
s konvencí 0^0=1. Rozdílová rovnost (E4) teleskopuje na

```text
S_m(n) = (P_(m+1)(n+1)−P_(m+1)(0))/(m+1)
       = (P_(m+1)(n+1)−B_(m+1))/(m+1)+0^m.             (E12)
```

Poslední přepis používá P_(m+1)(0)=B_(m+1)−[m=0].
Z (E3) dále dostaneme
`S_m(n)=n^(m+1)/(m+1)+0^m+sum_{k=1}^m B_k m_[k−1] n^(m−k+1)/k!`,
kde m_[j]=m(m−1)...(m−j+1) je padající mocnina a m_[0]=1.
Pro m=0,1,2 vycházejí n+1, n(n+1)/2 a n(n+1)(2n+1)/6.
Původní součet 0<=k<n má místo n+1 argument n a pracuje
se starým b_(m+1); původní i opravená odpověď jsou ve svých
konvencích správné. Historická atribuce součtů je oddělena od důkazu.

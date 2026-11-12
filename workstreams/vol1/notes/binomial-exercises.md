# §1.2.6: další konečné identity a analytické úlohy

Audit 1. listopadu 2026. Zobrazeno zadání s. 71–74 a odpovědi
487–491. `C(r,k)` znamená padající součin r(r−1)...(r−k+1)/k!
pro celé k>=0 a 0 pro celé k<0. Zobecnění na necelé k
je níže výslovně odděleno. `Gamma` je gama funkce ověřená
v `gamma-functions.md`; `[P]` je indikátor výroku P.

## Multinomické koeficienty (41)–(43)

Pro nezáporná celá k_1,...,k_m se součtem n počítá
`n!/(k_1!...k_m!)` slova délky n, v nichž se písmeno j
objeví k_j-krát: každé slovo odpovídá právě k_1!...k_m!
permutacím n rozlišených objektů. Roznásobení n činitelů
x_1+...+x_m dává (42), neboť každý takový výběr přispěje
stejným monomem x_1^k_1...x_m^k_m. Polynomiální konvence
0^0=1 zahrnuje i nulové proměnné a n=0.

Součin `product_{j=2}^m C(k_1+...+k_j,k_j)` teleskopuje
na stejný faktoriálový podíl; to je (43). Pro m=1 jde
o prázdný součin 1. Ztotožnění dvou stran (20) s trinomiálním
koeficientem používá rozdělení velikostí k,m−k,r−m
v nezáporném celočíselném oboru; obecná polynomiální
identita (20) již byla dokázána nezávisle.

## Úloha 38: filtr pomocí kořenů jedničky

Pro celé m>=1 a 0<=a<m položme omega=exp(2pi i/m).
Konečná geometrická řada dává
`(1/m)sum_{j=0}^{m−1} omega^(j(t−a))=[t≡a mod m]`.
Binomická věta pro celé n>=0 proto dokazuje

```text
sum_{t≡a (mod m)} C(n,t)
 = (1/m)sum_{j=0}^{m−1} omega^(−ja)(1+omega^j)^n
 = (1/m)sum_{j=0}^{m−1} (2cos(pi j/m))^n
                              cos(pi j(n−2a)/m).           (E1)
```

Poslední rovnost je reálná část předchozího výrazu a využívá
`1+omega^j=2cos(pi j/m) exp(pi i j/m)`; n je celé,
takže záporný kosinus nezavádí otázku větve mocniny.
Nulová mocnina při n=0 se vyhodnotí jako 1.
Pro m=3,a=1 se dva netriviální členy rovnají a vzniká
`(2^n+2cos((n−2)pi/3))/3`, přesně jako v příkladu.
Důkaz funguje i pro m>n. Atribuce Ramusovi a oba další odkazy
do CMath byly pramenně uzavřeny2.listopadu2026, viz X0701
a [kořenovou revizi](binomial-primary-root-review.md).

## Beta funkce: úlohy 40–41,43

Pro x,y>0 definujeme
`B(x,y)=integral_0^1 t^(x−1)(1−t)^(y−1)dt`.
Integrál konverguje na obou koncích, neboť x−1,y−1>−1.
Substituce t→1−t dává symetrii B(x,y)=B(y,x).

40(a). Integrace t^(x−1) dává B(x,1)=1/x, a symetrie
dává B(1,x). V (b) se integrandy sčítají, protože
t+(1−t)=1. Integrace po částech, s nulovým okrajovým
členem t^x(1−t)^y, dává `y B(x+1,y)=x B(x,y+1)`.
Spojením s (b) získáme (c),
`B(x,y)=(x+y)B(x,y+1)/y`.

41(a). Iterujeme poslední vztah m+1-krát:

```text
B(x,y) = product_{j=0}^m (x+y+j)/(y+j) * B(x,y+m+1)
       = Gamma_m(y)m^x/Gamma_m(x+y) * B(x,y+m+1),
Gamma_m(v) = m^v m!/[v(v+1)...(v+m)].
```

Pro (b) je `m^x B(x,m+1)→Gamma(x)` i pro reálné m→infinity.
Po substituci u=mt je totiž integrand na [0,m]
`u^(x−1)(1−u/m)^m`, zdola 0 a shora
`u^(x−1)exp(−u)`; po prodloužení nulou mimo [0,m]
platí dominovaná konvergence. Proto také
`m^x B(x,y+m+1)→Gamma(x)`: nahradíme m číslem m+y
a zbylý faktor (m/(m+y))^x jde k 1. Limitou v (a)
dostaneme `B(x,y)=Gamma(x)Gamma(y)/Gamma(x+y)`.

43. Substituce t=u² dává
`B(1/2,1/2)=2 integral_0^1 (1−u²)^−1/2 du=pi`.
Gamma(1/2)>0 z integrální definice, takže její hodnota
je kladná odmocnina pi, nikoli jen neurčené znaménko.

## Úlohy 42,44–46: necelý dolní index a asymptotika

V oboru bez pólů definujeme

```text
C(z,w) = Gamma(z+1)/(Gamma(w+1)Gamma(z−w+1))
       = 1/((z+1)B(w+1,z−w+1)).                            (E2)
```

Druhá podoba zprvu platí pro Re(w)>−1 a Re(z−w)>−1,
potom jako meromorfní identita. Pro hodnoty v pólech odpověď
42 předepisuje iterovanou limitu: nejprve dolní index, poté
horní. Pro celé k>=0 se tak vrátí padající polynom C(z,k),
pro celé k<0 dostaneme 0 i při záporném celém horním indexu.
Když je z záporné celé číslo a w necelé, jde o pól, nikoli
o konečnou hodnotu. Pořadí limit je tedy podstatné.

Mimo tyto výjimky symetrie plyne z (E2). Rekurence (7),(9)
a součinová identita (20) vycházejí po použití
Gamma(v+1)=v Gamma(v); při degeneraci se mohou objevit
neurčité součiny, nikoli oprávnění počítat aritmeticky s 0*infinity.
Reflexní formule Gamma dává uvedenou negaci horního indexu:

```text
C(z,w) = sin(pi(w−z−1))/sin(pi z) * C(w−z−1,w),             (E3)
```

nejprve mimo nuly jmenovatelů a potom pomocí příslušných
limit. Dvě další **bilaterální nekonečné řady** na konci
odpovědi 42 jsou rozebrány v `bilateral-binomial.md` včetně
větví mocnin a konvergence. Obecná konvoluce je vyvrácena
přesným protipříkladem V1-C0007: konečný součet dává 1,
ale iterovaná limita na pravé straně dává 0. Ramshawův
článek IPL 6 (1977), 223–226 dosud nebyl získán v plném textu.

44. Duplikační formule
`Gamma(r+1/2)Gamma(r+1)=2^(−2r)sqrt(pi)Gamma(2r+1)`
z předchozí sekce dává po dosazení do (E2)
`C(r,1/2)=2^(2r+1)/(pi C(2r,r))`. Rozšíření v singulárních
bodech používá stejné pokračování, nikoli přímé dělení nulou.

45. Pro pevné reálné k platí
`Gamma(r+1)/Gamma(r−k+1) ~ r^k`, když r→+infinity.
Lze to získat z již dokázané asymptotiky Gamma: v logaritmu
použijeme `log(1−k/r)=−k/r+O(r^−2)`. Proto
`C(r,k)/r^k→1/Gamma(k+1)`. Pro záporné celé k jsou
obě strany přesně 0 podle limitní konvence; k=0 dává 1.
Knižní mezivýraz s k Gamma(k) je potřeba v těchto bodech
číst po pokračování jako Gamma(k+1).

46. Pro kladné x,y→infinity samostatně dosadíme Stirlingův
vzorec do Gamma podílu a vykrátíme exponenciály:

```text
C(x+y,y) ~ sqrt((1/x+1/y)/(2pi))
               * (1+y/x)^x * (1+x/y)^y.
```

Relativní chyba je `1+O(1/x+1/y)`; není nutné, aby poměr
x/y zůstal omezený. Pro x=y=n vzniká `C(2n,n)~4^n/sqrt(pi n)`.

## Úlohy 47–49

47. Pro k>=0 se sudé a liché činitele v (2r)_[2k]
rozdělí na `4^k r_[k](r−1/2)_[k]`. Vydělení (k!)²
dává obě identity zadání, přičemž druhá používá
`C(2r,k)C(2r−k,k)=C(2r,2k)C(2k,k)`.
Při k<0 jsou všechny tři výrazy 0. Pro r=−1/2 použijeme
C(−1,k)=(−1)^k a dostaneme
`C(−1/2,k)=(−1/4)^k C(2k,k)` pro k>=0;
pro záporné k jsou obě strany opět 0.

48. Pro celé n>=0 a x>0 rozvinutí (1−t)^n pod beta
integrálem dává

```text
sum_{k=0}^n (−1)^k C(n,k)/(x+k)
 = B(x,n+1) = n!/[x(x+1)...(x+n)]
 = 1/(x C(n+x,n)).                                       (E4)
```

Obě strany jsou racionální funkce x; shoda na x>0 je
rozšiřuje na každé x mimo 0,−1,...,−n. Tak jsou zahrnuty
i záporné a komplexní hodnoty x. Pro necelé n lze beta
rozvoj dokázat nejprve při Re(x)>0, Re(n)>−1: integrace
po členech je absolutně oprávněná, protože
`C(n,k)=O(k^(−Re(n)−1))` v absolutní hodnotě a
`1/(x+k)=O(1/k)`. Série je dále holomorfní v x mimo póly
0,−1,..., lokálně stejnoměrnou konvergencí; analytické
pokračování tedy dává i zbývající x mimo tyto póly.
Pro necelé n je Re(n)>−1 také nutná podmínka konvergence:
znaménko (−1)^k se v (−1)^k C(n,k) zruší a členy jsou
nenulová konstanta krát k^(−n−2)(1+O(1/k)). Obvyklá řada
komplexních mocnin k^(−s) konverguje právě pro Re(s)>1,
jak plyne porovnáním jejích součtů s integrálem. Výjimkou
jsou ukončené řady s nezáporným celým n, již ověřené zvlášť.

49. Na |x|<1 můžeme násobit konvergentní binomické řady
v `(1+x)^r=(1−x²)^r(1−x)^−r`. Koeficient x^m dává
`C(r,m)=sum_k (−1)^(m+k)C(r,k)C(−r,m−2k)`.
Pro m>=0 je součet konečný, pro m<0 jsou všechny členy
i levá strana 0. Tím se obejdou krajní body konvergence.

## Úlohy 50–52: další důkazy Abelovy identity

Nechť n>=0 je celé. Abelův polynom je
`sum_{k=0}^n C(n,k)x(x−kz)^(k−1)(y+kz)^(n−k)`;
člen k=0 znamená y^n po zkrácení x. Při y=−x a n>=1
je k-tý člen `C(n,k)(−1)^(n−k)x(x−kz)^(n−1)`.
Součet je n-tá diference polynomu v k stupně n−1,
proto je 0. Pro n=0 dává 1. To dokazuje úlohu 50.

V úloze 51 položíme u=x+y a rozvineme
`(y+kz)^(n−k)=(u−x+kz)^(n−k)` podle mocnin u.
Koeficient u^j po prohození konečných součtů je

```text
C(n,j) sum_{k=0}^{n−j} C(n−j,k)
             x(x−kz)^(k−1)(−x+kz)^(n−j−k).
```

Úloha 50 říká, že je nulový pro j<n a roven 1 pro j=n.
Výsledkem je tedy u^n=(x+y)^n, jak vyžadováno.
Symetrické a Hurwitzovo zobecnění připojené v odpovědi 51
jsou samostatně dokázány v `abel-extensions.md`.

52. Pro n=x=−1,y=z=1 je k-tý člen přesně 1/(k+1)².
Součet je pi²/6, zatímco (x+y)^n=0^−1 není konečný.
To dostačuje jako požadovaný protipříklad. Hodnota pi²/6
plyne též z koeficientu z² v již ověřeném sinusovém součinu
`sin(pi z)/(pi z)=product_{j>=1}(1−z²/j²)`.
Další tvrzení v hranaté poznámce odpovědi 52 o komplexních
parametrech, konvergenci a derivacích jsou prověřena
v `abel-extensions.md`, s výslovným oborem analyticity.
Známé opravy r→n z 26. ledna 1998 jsou zahrnuty.

## Úlohy 53–54,56–57,59–60

53(a). Označme `T_m=(m+1)(n−m)C(r,m+1)C(s,n−m)`.
Pomocí `j C(a,j)=a C(a−1,j−1)` nebo přímo konečných
součinů dostáváme polynomiálně

```text
T_m−T_(m−1) = C(r,m)C(s,n−m)(nr−(r+s)m).
```

Protože T_(−1)=0, teleskopování dokazuje zadání pro m>=0.
Pro m<0 orientovaný součet obsahuje jen nulové koeficienty
a T_m=0; totéž platí při záporném n a m>=0.
V (b) dosadíme r=1/2,s=−1/2 a použijeme (47).
Přepis koeficientu C(1/2,k) obsahuje člen −[k=0],
proto po sečtení vzniká právě `+C(2n,n)/2` na pravé straně.
Výsledný vzorec s dělitelem 2n je tak ověřen pro n>=1,m>=0,
což je přirozený rozsah tohoto prefixového součtu. Mimo něj
by vyžadoval doplnění oboru či indikátoru; nejde o pokračování
na n=0 prostým dosazením do dělení nulou.

Obor části (b) není výslovně uveden, zatímco část (a)
výslovně připouští celá m,n. Kdyby se tento obor přenesl
i do (b), m=−1,n=1 dává levou stranu 0 (prázdný součet)
a pravou 0+C(2,1)/2=1. To nezávisí na sporné konvenci
obrácených mezí: při horní mezi −1 jsou oba obvyklé součty
prázdné. Kandidát **V1-C0009** proto eviduje chybějící
vymezení oboru, s opatrností ohledně implicitního významu
prefixového součtu. Bez upřesnění není celý doslovný obor
této části označen za ověřený. Oprava 53 v prohledaných
pěti vrstvách errat dostupných 1. listopadu 2026 nenalezena.

54. Součin Pascalovy matice C(n,k) s maticí
`(−1)^(n+k)C(n,k)` má (n,m)-tý prvek
`C(n,m)sum_{j=0}^{n−m}(−1)^j C(n−m,j)=[n=m]`.
To dokazuje udaný šachovnicový vzor znamének; každý součet
je konečný, takže i nekonečná trojúhelníková matice je v pořádku.

56. Pro pevné d>=1 se každé N>=0 zapíše jednoznačně jako
`sum_{j=1}^d C(a_j,j)` s celými a_d>...>a_1>=0.
Zvolíme největší a_d s C(a_d,d)<=N. Pascalovo pravidlo
zaručuje, že zbytek je menší než C(a_d,d−1), takže při
rekurzi a_(d−1)<a_d. Indukce současně dokazuje jednoznačnost:
pro pevné a_d dosáhnou nižší místa právě zbytků
0,...,C(a_d,d−1)−1, tedy interval končí v C(a_d+1,d)−1.
Pro d=1 je tvrzení přímo a_1=N.

Opravená odpověď z 31. května 2002 uvádí pořadí a_3,a_2,a_1.
Její posloupnost 210,310,...,543,610 odpovídá požadovaným
N=0,...,20; sken zadání skutečně začíná nulou. Pro d=4 je
počátek 3210,4210,4310,4320,4321,
5210,5310,5320; opět jde o N=0,1,... . Obě reprezentace
v původním a opraveném zápisu jsou ekvivalentní po obrácení
pojmenování indexů.

57. Pro m>=1 je `m!a_m=Delta^m log(n!) při n=0`, jak
bylo dokázáno v §1.2.5. Dosadíme log(j!)=sum_{k=1}^j log k
a prohodíme dva konečné součty. Koeficient log k je

```text
sum_{j=k}^m (−1)^(m−j)C(m,j)
 = (−1)^(m−k)C(m−1,k−1).
```

Po vydělení m! vzniká přesně vzorec zadání. m=1 dává 0;
symbolický nekonečný součet má podporu 1<=k<=m.

59. Kandidát `A(n,k)=(n+1)C(n,k)−C(n,k+1)` má
A(n,0)=1 a A(0,k)=[k=0]. Pascalovo pravidlo dává
`A(n,k)−A(n−1,k)−A(n−1,k−1)=C(n,k)`.
Rekurence jednoznačně určuje všechny hodnoty; odpověď platí
i při k>n, kdy se koeficienty anulují.

60. Neklesající k-tici 1<=a_1<=...<=a_k<=n převedeme na
ostře rostoucí k-tici b_i=a_i+i−1 z {1,...,n+k−1}.
Jde o bijekci, proto počet kombinací s opakováním je
C(n+k−1,k). Pro n=0 je výsledek [k=0] přímo,
a stejný vzorec funguje díky C(−1,0)=1.
Atribuce Scherkovi a Förstemannovi zůstává pramenně otevřena.

## Úlohy 67–68: odhady a absolutní odchylka

67. Pro celá n>=k>0 platí
`C(n,k)<=n^k/k! <= (ne/k)^k/e <= (ne/k)^k`,
díky dolní mezi faktoriálu z §1.2.5-24.
Původní zadání s k>=0 má při k=0 výraz n e/k;
oprava na k>0 z 4. října 2021 je tedy opodstatněná.

Dolní mez v opravené odpovědi z 18. února 2012 je
`C(n,k)>=((n−k+1)e/k)^k/(e k)`; plyne z
n_[k]>=(n−k+1)^k a horní meze k!<=k^(k+1)/e^(k−1).
Jednodušší mez `C(n,k)>=(n/k)^k` plyne z každého
`(n−j)/(k−j)>=n/k`, 0<=j<k. První mez není vždy silnější:
n=k=2 dává e/8<1, zatímco druhá dává přesně 1.
Aktuální oprava ale výslovně říká **often sharper**, tedy
jen často ostřejší, nikoli vždy. Například pro pevné k>=2
a n→infinity poměr obou mezí konverguje k hodnotě e^(k−1)/k>1.
Domnělá chyba v tomto porovnání je proto vyloučena.

68. Pro 0<p<1 a n>=1 položme a=ceil(np) a
`T_k=k C(n,k)p^k(1−p)^(n+1−k)` pro 0<=k<=n+1,
s T_0=T_(n+1)=0. Přímé krácení faktorů dává

```text
T_k−T_(k+1) = C(n,k)p^k(1−p)^(n−k)(k−np).
```

Součet absolutních odchylek se rozdělí na k<a a k>=a;
teleskopováním dostaneme `2T_a`, tedy udaný vzorec.
Je-li np celé, nulový člen na rozhraní nic nemění.
Případy p=0,1 a n=0 dávají 0 přímo, s vynecháním členů
silně nulových koeficientů před zápornými mocninami nuly.
Pro reálné p mimo [0,1] mají všechna k−np stejné znaménko,
takže i algebraicky vážený součet absolutních odchylek je 0
podle binomické věty a její derivace. Pravá strana je také 0
díky a C(n,a)=0. Tvrzení tedy nevyžaduje pravděpodobnostní
interpretaci, pokud p zůstává reálné.

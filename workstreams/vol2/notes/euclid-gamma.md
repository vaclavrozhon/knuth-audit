# §4.5.3-47: zaručený rozvoj Eulerovy konstanty

Zadání na původní straně 379 bylo vizuálně přečteno. Úloha nemá
samostatnou tištěnou odpověď. Eulerova konstanta je
gamma = lim(n→infinity)(H_n-log n), kde H_n=sum(k=1..n)1/k
a H_0=0. Logaritmus je přirozený. Zápis [a_0;a_1,...]
znamená pravidelný řetězový zlomek, jehož podíly a_j pro j>0
jsou kladná celá čísla. Konečný racionální rozvoj volíme kanonicky:
poslední podíl je >1, kromě jednočlenného celočíselného rozvoje.

## Co přesně znamená „co nejvíce podílů“

Vstupem programu je **uzavřený racionální interval [l,u]**,
o němž víme, že obsahuje hledané číslo. Program vrací nejdelší
prefix společný všem reálným číslům tohoto intervalu. Je tedy
uvedeno, jak interpretujeme konečnou přesnost; samotný řetězec
desetinných číslic bez informace o chybě by tento požadavek
neurčoval.

Jsou-li floor(l) a floor(u) různé, nelze vydat další podíl:
již oba přípustné konce jej mají různý. Jinak vydáme společné
a. Pokud l=a, tento přípustný konec rozvoje končí a nelze
zaručit další podíl. Jinak nahradíme interval hodnotami

```text
[l,u] <- [1/(u-a), 1/(l-a)].                            (1)
```

To je přesný obraz dosavadního intervalu, neboť převrácení
kladných čísel obrací pořadí. Indukce proto dokazuje správnost
každého výstupu. Při zastavení existují dvě přípustné možnosti
s různým dalším podílem, nebo jedna končí; důkaz dává také
maximalitu. Je-li l=u, použije se konečný Eukleidův rozvoj.
Konce mohou být záporné: jen první podíl používá obecnou
matematickou podlahu, po (1) je zbývající hodnota kladná.

Tentýž výsledek získáme jako společný prefix obou kanonických
rozvojů konců. Program jej nezávisle ověřuje pomocí Lehmerových
dávek: vezme 60 nejvyšších bitů čitatele a jmenovatele, provede
všechny kroky s jednoznačně určeným malým podílem a společnou
celočíselnou maticí aktualizuje velká čísla. Pokud dávka nedá
žádný podíl, provede plné dělení. Správnost této varianty L
je doložena v `gcd-extensions.md`; zde je zvlášť testován její
výstupní proud podílů. Tvrzení zadání, že plné dělení při
každém kroku není nutné, je tak skutečně využito.

## První analytické sevření: dvě Besselovy řady

Pro celé n>=1 položme t_k=n^(2k)/(k!)² a definujme

```text
I = sum(k>=0) t_k,
S = sum(k>=0) H_k t_k,
K = integral(0..infinity) exp(-2n cosh t) dt.
gamma = S/I - log n - K/I.                             (2)
```

Základní identita (2) je odvozena na stranách 7–8 rozšířeného
anglického znění [Demaillyho článku](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/gamma_gazmath_eng.pdf).
Tyto stránky byly přečteny i vizuálně. Jeho označení I_0(n),
K_0(n) odpovídá obvyklým Besselovým funkcím v argumentu 2n.
Funkce Gamma je zde Gamma(s)=integral(0..infinity)t^(s-1)exp(-t)dt
pro s>0. Definujme I_alpha(n)=sum(k>=0)n^(alpha+2k)/(k!Gamma(alpha+k+1)).
Derivace této řady podle alpha v nule dává
K= S-(log n+gamma)I, protože logaritmická derivace funkce
Gamma v k+1 je H_k-gamma. Integrální vyjádření téhož K
a I=pi^(-1) integral(0..pi) exp(2n cos t) dt jsou na straně 8.

Pro kontrolu chyby nepotřebujeme jemný asymptotický rozvoj.
Nerovnost cosh t>=1+t²/2 dává
K <= exp(-2n) sqrt(pi)/(2sqrt(n)). Na intervalu
0<=t<=1/sqrt(n) platí cos t>=1-t²/2, tedy
I >= exp(2n-1)/(pi sqrt(n)). Proto

```text
0 < K/I < 8 exp(-4n).                                  (3)
```

Konstanta 8 je horní mez e*pi^(3/2)/2; postačí elementární
e<11/4 a pi<22/7. Pro konečné součty do k=N označme
T=t_(N+1) a rho=n²/(N+2)²<1. Poměry dalších členů jsou
nejvýše rho, zatímco H_(N+1+j)<=H_(N+1)+j/(N+2).
Geometrická řada a její derivace proto dávají

```text
0 < I-I_N <= T/(1-rho),
0 < S-S_N <= T*(H_(N+1)/(1-rho)
                  + rho/((N+2)*(1-rho)²)).              (4)
```

Program používá n=6000, N=24000. Oba zbytky (4), korekci
(3) i všechna aritmetická zaokrouhlení zahrnuje do intervalů.
Příspěvek (3) je menší než 6.85·10^(-10423); relativní
zbytky řad jsou menší než 7.36·10^(-13269).

## Druhé sevření: exponenciální integrál

Nezávislý výpočet používá jinou řadu

```text
P(x) = exp(-x) sum(k>=0) H_k x^k/k!,
E_1(x) = integral(x..infinity) exp(-t)/t dt,
gamma = P(x)-log x-E_1(x).                             (5)
```

Souvislost se Sweeneyovým postupem vysvětlují strany 5–7
uvedeného Demaillyho znění. Samotné převedení kladné řady
na integrál ověříme přímo: derivace P je

```text
P'(x) = exp(-x) sum(k>=0)(H_(k+1)-H_k)x^k/k!
      = (1-exp(-x))/x.
```

Proto P(x)=integral(0..x)(1-exp(-t))/t dt; hodnota v nule
je nula. Integrace gamma=-integral(0..infinity)log(t)exp(-t)dt
po částech dává (5). Rovnost Gamma'(1)=-gamma lze nezávisle
vidět z Eulerova limitního součinu
Gamma(1+z)=lim(N→infinity)N^z product(k=1..N)k/(k+z):
logaritmická derivace v nule je lim(log N-H_N)=-gamma.
Všechny zde použité integrály mají exp(-t); dva zjevné
sazební nedostatky na straně 5 Demaillyho překladu (exp(t)
a chybějící exponenciální činitelé v nekonečném součinu)
nepřebíráme. Dále 0<E_1(x)<exp(-x)/x.
Nejde o opakování výpočtu Besselových řad ani o porovnání
dvou zaokrouhlených volání téže konstanty.

Zde jsou x=24000 a N=72000. Pro t_k=x^k/k!,
T=t_(N+1), rho=x/(N+2) platí druhý odhad (4) beze změny.
Program násobí takto sevřenou řadu intervalem exp(-x),
odečte interval log x a zahrne celý zbytek E_1.
Jeho mez je menší než 3.57·10^(-10428); relativní ocas
kladné řady je menší než 2.09·10^(-13510).

## Reprodukovatelnost a rozsah

Obě analytické metody používají `python-flint==0.9.0`
s pracovní přesností 10100 desetinných míst. Typ `arb`
uchovává střed a zaručený poloměr chyby; operace zaokrouhlují
směrem ven. Poloměry se v programu úmyslně rozšiřují o
symetrický interval celého odhadu zbytku. Dolní a horní
konec se ukládají jako přesné dyadické racionální hodnoty.
Dokumentace: [arb](https://python-flint.readthedocs.io/en/stable/arb.html).
Záruka tedy používá intervalovou aritmetiku knihovny; nejde
o formální verifikaci její implementace.

Každá z obou nezávislých analytických metod zvlášť prokazuje,
že gamma leží přísně mezi A/10^10000 a (A+1)/10^10000,
se stejným uloženým celým A. Na tento širší desetinný
interval se pak použije algoritmus (1). Ověřují se také
všechny jeho válcové intervaly: pro konvergenty p_k/q_k
a p_(k-1)/q_(k-1) jsou jejich kraje
p_k/q_k a (p_k+p_(k-1))/(q_k+q_(k-1)). Nezávislá rekurze
těchto čitatelů a jmenovatelů potvrzuje obsahování celého
desetinného intervalu v každém válci.

Nejdříve prošlo 2006 přesných intervalových případů včetně
celých čísel, záporných vstupů a končících krajů; 6000
vnitřních racionálních bodů a 560 samostatných Lehmerových
rozvojů do 4096 bitů. Úplné velké výsledky a poslední
nesouhlasné podíly krajů jsou v `results/euclid-gamma.json`.

Výsledek je **9734 zaručených podílů za a_0=0**, tedy 9735
ověřených válců. Největší podíl je a_5040=11626. Další
podíl dolního desetinného konce je 9, horního 8, takže
maximalita pro zvolený vstupní interval má konkrétní svědky.
Rozvoje začínají

```text
[0;1,1,2,1,2,1,4,3,13,5,1,1,8,1,2,4,1,1,40,...].
```

Pro 10, 100, 1000 a 5000 míst program zaručuje postupně
12, 108, 952 a 4911 podílů za a_0. Lehmerův nezávislý
rozklad obou velkých konců použil 2445 maticových dávek,
38885 podílů v dávkách a jen tři plná dělení po oddělení
celočíselných částí. Oba celé racionální rozvoje jsou delší
než jejich společný prefix; tyto počty nejsou počtem
zaručených podílů gamma.

Relace 25601, PID 1181298, limit 600 sekund, exit 0.
Checkpointy: přesné případy 1.688 s, Bessel 4.526 s,
exponenciální řada 13.270 s a celý prefix s nezávislou
kontrolou 171.491 s. Všechny čtyři prošly.

Hodnota přibližně 0.97 podílu na desetinné místo je metrická
predikce pro téměř všechna čísla. Její konstanta je
6 log(2) log(10)/pi², odvozená z Lochsova výsledku v závěru
hlavního textu; podrobný metrický kontext zůstává v jeho
samostatném auditu. Není to univerzální konečná mez ani
věta o gamma. Konečný certifikovaný prefix také nedokazuje
iracionalitu gamma ani rovnost gamma s některým z konvergentů.

Přesné bibliografické omezení: Sweeneyho původní článek
170–178 se nepodařilo stáhnout (vydavatel 403); jeho obsah
je zde doložen Demaillyho samostatným odvozením. Rozsah
Wrench–Shanks je podezřelý, viz `C0131-wrench-shanks-pages.md`.
Originál tohoto článku zatím chybí, nejde o potvrzenou chybu.

# §1.2.11.3: neúplná gama funkce a Watsonovo lemma

Kontrola hlavního textu s. 116–121 a úloh 1–10, 12, 19–20;
originály s. 116–123 a 504–507 zobrazeny. V této poznámce jsou analytické
důkazy a podmínky zbytků; `check_asymptotic_calculations.py` doplňuje
přesnou kontrolu koeficientů, nikoli náhradu důkazů numerickým odhadem.
Čtyři nalezené nesrovnalosti jsou odděleně v `asymptotic-findings.md`.

## Definice, identity a úlohy 1–3

Pro a>0 a x≥0 je dolní neúplná gama funkce
`γ(a,x)=∫_0^x exp(−t)t^(a−1)dt`; úplná gama funkce Γ(a) má horní mez ∞.
Pro záporné x použité v úlohách 9–10 je exponent a−1 celé nezáporné číslo,
takže integrál po reálné ose zůstává jednoznačný. V obecném reálném
exponentu zde záporný argument nepřipouštíme.

Rovnice (5) je Taylorův vzorec s integrálním zbytkem:
`f(x)=∑_{j=0}^n f^(j)(0)x^j/j! + ∫_0^x t^n f^(n+1)(x−t)dt/n!`.
Pro n=0 je to základní věta integrálního počtu po substituci x−t;
integrace per partes ve zbytku zvýší n o 1. Vyžaduje se příslušná
hladkost f na úsečce mezi 0 a x. Orientovaný integrál dává stejný vzorec
i pro x<0, je-li tam f definována.

Rovnice (7) vzniká integrací exponenciální řady člen po členu:
`γ(a,x)=∑_{k≥0}(−1)^k x^(a+k)/[k!(a+k)]`.
Na každém konečném nezáporném intervalu je po vyjmutí t^(a−1)
exponenciální řada stejnoměrně absolutně konvergentní; a>0 zaručuje
integrabilitu u 0. Pro (8) lze buď vynásobit absolutně konvergentní řady,
nebo použít přímo

`exp(x)γ(a,x)=x^a∫_0^1 exp(x(1−v))v^(a−1)dv`
`=∑_{k≥0}x^(a+k)/[a(a+1)…(a+k)]`.

Poslední rovnost používá beta integrál, odvoditelný k-násobnou integrací
per partes. To také ověřuje binomickou identitu použitou v odpovědi 3.
Jedna integrace per partes dává
`a γ(a,x)=γ(a+1,x)+x^a exp(−x)`.

Pro n≥1 celé definujme Q(n)=∑_{j=1}^n n!/[(n−j)!n^j] a
R(n)=∑_{j≥0}n!n^j/(n+j)!. Rozdělení exponenciální řady v indexu n
dává (4), `Q+R=n!exp(n)/n^n`, bez překryvu či chybějícího členu.
Dosazení a=x=n do (8) dává přesně (9),
`R(n)=[n!exp(n)/n^n] γ(n,n)/(n−1)!`.

## Místní inverze a integrál I_1

Pro velké reálné x>0 a pevné reálné y položme
`I_1=∫_x^∞ exp(−t)t^x dt`, `I_2=∫_x^(x+y) exp(−t)t^x dt`.
Pak `γ(x+1,x+y)/Γ(x+1)=1−I_1/Γ(x+1)+I_2/Γ(x+1)`; pro dost velké x
je x+y kladné i při y<0.
V I_1 substituce t=x(1+u), v=u−ln(1+u) dává

`I_1=exp(−x)x^x ∫_0^∞ x exp(−xv)(1+1/u(v))dv`.             (G1)

Zde u,v≥0 a v je ryze rostoucí pro u>0. Položme w=sqrt(2v).
Funkce w(u)=u sqrt(2(u−ln(1+u))/u²) je analytická u 0 s derivací 1,
takže má analytickou lokální inverzi. Pro tuto kladnou větev platí

```text
w = u − u²/3 + 7u³/36 − 73u⁴/540 + 1331u⁵/12960 + O(u⁶),
u = w + w²/3 + w³/36 − w⁴/270 + w⁵/4320 + O(w⁶),
1+1/u = 1/w + 2/3 + w/12 − 2w²/135 + w³/864 + O(w⁴).
```

Koeficienty poslední řady lze také získat derivací u podle v, protože
du/dv=1+1/u. Existence konvergentní lokální řady zdůvodňuje i derivaci
jejího zbytku; samotné formální derivování libovolného O-členu by nestačilo.
To odpovídá opravě oborů z 30.12.2024 a opravenému odkazu z 29.3.2023.

Pro každý pevný r>0 je 1+1/u(v) na v≥r omezené, takže část (G1) za r
je O(exp(−rx)); viz úloha 4 a drobná oprava V1-C0016. U 0 integrujeme
každý člen pomocí
`∫_0^∞ x exp(−xv)v^α dv=Γ(α+1)x^(−α)`, α>−1.
O(v²) zbytek má po integraci velikost O(x^(−2)); exponenciální ocasy
všech konečně mnoha monomů jsou menší než libovolná záporná mocnina x.
Dostaneme (15):

```text
I_1/[exp(−x)x^x] = sqrt(πx/2) + 2/3 + sqrt(2π)/(24 sqrt x)
                  −4/(135x) + sqrt(2π)/(576 x^(3/2)) + O(x^(−2)).
```

## I_2 a Theorem A

Substituce t=x+u dává
`I_2/[exp(−x)x^x]=∫_0^y exp(−u)(1+u/x)^x du`.
Taylorův rozvoj logaritmu a exponenciály platí rovnoměrně na
**|u|≤|y|**, tedy i na záporné integrační úsečce. Opravy z roku 2024
výslovně připouštějí záporné y; formulaci s jednostranným intervalem
v důkazu doplňujeme tímto oboustranným odhadem. Výsledná rovnost (17) je

`I_2/[exp(−x)x^x]=y−y³/(6x)+(y⁴/12+y⁵/40)/x²+O(x^(−3))`.

Již ověřená Stirlingova formule pro reálné argumenty dává (18)
`exp(−x)x^x/Γ(x+1)=(2π)^(−1/2)(x^(−1/2)−x^(−3/2)/12+x^(−5/2)/288+O(x^(−7/2)))`.
Vynásobením se členy x^(−1) a x^(−2) přesně vyruší; hlavní výsledek je

```text
γ(x+1,x+y)/Γ(x+1) = 1/2 + (y−2/3)/sqrt(2πx)
 + (23/270−y/12−y³/6)/(sqrt(2π) x^(3/2)) + O(x^(−5/2)).  (G2)
```

Součin chyby O(x^(−2)) v (15) s prefaktorem O(x^(−1/2)) vysvětluje
poslední řád; nejde o neopodstatněné vynechání celých mocnin.
Pro y v každém pevném kompaktním intervalu jsou odhady rovnoměrné.

## Úlohy 5–8: změna horní meze

V úloze 5 je f(t)=t^(n+1/2)exp(−t). Eulerův zbytek druhého řádu je
omezen konstantou krát ∫_0^n |f''(t)|dt. Pro velké n má f'' jedinou
nulu v (0,n), a to `r=n+1/2−sqrt(n+1/2)`, s kladným znaménkem před r
a záporným za ním. Integrál absolutní hodnoty je
`2f'(r)−f'(0)−f'(n)`; opačné znaménko této kombinace vytištěné uvnitř
O-notation nemění odhad, který je definován přes absolutní hodnoty.
Platí f'(0)=0, f'(n)=f(n)/(2n) a f'(r)=O(f(n)/sqrt n): poslední vztah
plyne z `r/n=1−n^(−1/2)+O(n^(−1))`, z omezenosti f(r)/f(n) a ze
vzorce `f'(r)/f(r)=(n+1/2)/r−1=O(n^(−1/2))`.
Proto |R|=O(n^n exp(−n)), jak požaduje úloha a rovnice (22).

Úloha 6: pro pevné α,β rozvineme
`(n+β)ln(1+α/n)=α+α(β−α/2)/n+O(n^(−2))`.
Exponenciací dostaneme přesně (23), s kladným základem n+α pro velké n.

V úloze 7 položíme u=x^(1/4)v. Na pevné úsečce mezi 0 a y rozvineme
`exp(−v² x^(−1/2)/2+v³ x^(−5/4)/3−v⁴ x^(−2)/4+…)`
a připojíme jakobián x^(1/4). Zbytek je rovnoměrný pro obě znaménka y.
Po integraci vyjde

```text
y x^(1/4) − y³ x^(−1/4)/6 + y⁵ x^(−3/4)/40 + y⁴ x^(−1)/12
− y⁷ x^(−5/4)/336 − y⁶ x^(−3/2)/36
+ (y⁹/3456−y⁵/20)x^(−7/4) + O(x^(−2)).
```

V úloze 8 je přesný důkaz zbytku po opravě absolutní hodnoty zaznamenán
u V1-C0017. Zvláštní případ r=1/2,s=0,m=2 dává po u=sqrt(2x)t
právě Tricomiho aproximaci s chybou O(1); záporné f(x) používá orientaci
integrálu. Jméno a původ této aproximace jsou samostatná bibliografická kontrola.

## Úlohy 9–10: horní mez px

Parametr p je pevný reálný, x→∞; při p<0 je x kladné celé. Pro p=0
je γ(x+1,0)=0; pro p=1 použijeme (G2) s y=0. Pro p<1,p≠0 substituce
t=px(1−u) převádí integrál na

`p x (px)^x exp(−px) ∫_0^1 exp(x[ln(1−u)+pu])du`.

Platí to i pro p<0: faktor p správně nese orientaci, (px)^x je reálné.
Substituce v=−ln(1−u)−pu je na [0,1) rostoucí do ∞ a její jakobián je
`(1−u)/(1−p+pu)`. U 0 má rozvoj
`(1−p)^(−1)[1−v/(1−p)²+O(v²)]`, jinde je omezený.
Watsonův argument dává odpověď po známé opravě x^z→x^x z 17.10.2007:

`γ(x+1,px)/Γ(x+1) = [p/(1−p)](p exp(1−p))^x`
` · exp(−x)x^x/Γ(x+1) · [1−1/((p−1)²x)+O(x^(−2))]`.       (G3)

Pro p>1 provedeme stejný postup na horním ocasu Γ−γ s t=px(1+u),
v=pu−ln(1+u). Výsledek je 1 plus pravá strana (G3), která je záporná.
Odhady jsou pro pevné p; při p→1 nejsou tvrzeny jako rovnoměrné.

V úloze 10, p≠1, položíme `t=px+pz/(p−1)`. Rozdíl integrálů je přesně

`[p/(p−1)](p exp(1−p))^x exp(−x)x^x`
` · ∫_0^y exp(−z)[1−z²/(2x(p−1)²)+O(x^(−2))]dz`.

Integrace 1 a z² dává závorku odpovědi
`1−exp(−y)−exp(−y)(exp(y)−1−y−y²/2)/(x(p−1)²)+O(x^(−2))`.
Rovnoměrnost na pevné orientované úsečce zaručuje obě znaménka y.
Pro p=0 se původní rozdíl rovná nule přímo, bez dělení p.
Úloha 12 je vyřešena substitucí t²/2 se znaménkem v nálezu V1-C0019.

## Watsonovo lemma, úloha 19

Zde f je lokálně integrovatelná funkce na (0,∞),
`C_n=∫_0^∞ exp(−nt)f(t)dt` existuje pro všechna dost velká n,
a |f(t)|≤M t^α pro 0<t≤r, kde r>0, α>−1. Absolutní konvergence
na nekonečném konci se **nepředpokládá**. Vyberme N s existujícím C_N
a položme `F(t)=∫_r^t exp(−Nu)f(u)du`. Konvergence dává |F(t)|≤K
pro t≥r. Pro n>N integrace per partes a vymizení koncového členu dávají

`|∫_r^∞ exp(−nt)f(t)dt| ≤ (n−N)K∫_r^∞ exp(−(n−N)t)dt`
`=K exp(−(n−N)r)`.

Část u nuly má absolutní hodnotu ≤MΓ(α+1)n^(−α−1).
Exponenciální ocas je menšího řádu, tedy C_n=O(n^(−α−1)).
Přesně tento argument obsahuje odpověď 19. Odkazy Barnes/Watson jsou
historické zdroje; jejich úplná kontrola není nahrazena naším důkazem.

## Úloha 20 a rozvoje Q,R

Úloha 15 dává `Q(n)+1=∫_0^∞ (1+z/n)^n exp(−z)dz` přímým binomickým
rozvojem a integrací z^k. Po z=nx, v=x−ln(1+x) dostaneme
`Q(n)+1=n∫_0^∞ exp(−nv) dx/dv dv`.
Použijeme analytickou inverzi `x=∑_{k≥1}c_k(2v)^(k/2)` z (G1),
takže `dx/dv=∑_{k=1}^{m−1} k c_k(2v)^(k/2−1)+O(v^(m/2−1))`.
Watsonovo lemma platí pro m≥1 a α=m/2−1>−1. Na nekonečném konci
je dx/dv=1+1/x omezené. Dostaneme přesně tvrzený libovolně dlouhý rozvoj

`Q(n)+1=∑_{k=1}^{m−1} k c_k Γ(k/2)(n/2)^(1−k/2)+O(n^(1−m/2))`.

Chybějící faktor k v jedné řádce odpovědi je **známá oprava 1.1.2006**.
Koeficienty c_1,…,c_5 z výše uvedené inverze dávají (25):

`Q(n)=sqrt(πn/2)−1/3+(1/12)sqrt(π/(2n))−4/(135n)`
`     +(1/288)sqrt(π/(2n³))+O(n^(−2))`.

Identita Q+R=n!exp(n)/n^n a Stirlingova řada pak dávají (26) se znaménky
+1/3 a +4/(135n); ostatní zobrazené členy jsou stejné. Z koeficientů
c_6,c_8,… lze pokračovat; již ověřený Ramanujanův certifikát zvlášť
potvrzuje i správné členy `(R−Q)/2=1/3+4/(135n)−8/(2835n²)−16/(8505n³)+…`.
Záměna 1/8505 za 16/8505 na s. 121 je známá oprava 8.2.2000.

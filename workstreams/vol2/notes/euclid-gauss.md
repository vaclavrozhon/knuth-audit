# §4.5.3: Gaussův model a elementární Wirsingovy meze

Audit 2026-11-03. Uzavírá úlohy **19, 20, 21, 23**, matematický
text 362–365, větu W na 366 a odhad (53) na 370. Spektrální tvrzení
(40)–(44), úloha 22 a historické citace zůstávají samostatnou prací.
Níže uvedené důkazy nevyžadují převzetí těchto spektrálních výsledků.

Původní sazba 362–366, 370, 376, 651–652 byla zobrazena. Vrstvy
`all2-prepre`, `all2-pre`, `all2`, `err2` byly prohledány. Jediná
matematická oprava v tomto rozsahu je známé erratum 2000-03-30:
v (25) má člen se zeta(5) obsahovat x^4, nikoli x^5. Oprava citací
na konci 366 patří do dosud neuzavřeného kontextu. Nový nález nevznikl.

## 1. Model, součtový operátor a invariantní rozdělení

Nechť X_0 je rovnoměrně rozděleno v (0,1), X_(n+1) je zlomková
část 1/X_n a F_n(x) = Pr(X_n <= x). Racionální vstupy mají nulovou
pravděpodobnost, takže případ konečného rozvoje zde nevadí.
Píšeme ln pro přirozený logaritmus a lg pro logaritmus o základu 2.
Pro funkci G se spojitou první derivací na [0,1] definujeme

```
(S G)(x) = sum_(k>=1) [G(1/k) - G(1/(k+x))].                 (A1)
```

Rozdělení inverzních větví mapy X -> {1/X} dává F_(n+1) = S F_n
a F_0(x) = x. Pro 0 <= x <= 1 je absolutní hodnota k-tého členu
nejvýše max|G'|/k^2. Také řada derivací stejnoměrně konverguje,
protože její člen je G'(1/(k+x))/(k+x)^2. Tím jsou ospravedlněny
součty, limitní přechody a derivování používané dále; operátor
nepotřebujeme definovat na libovolných nespojitých funkcích.

V úloze 19 vezměme G(x) = log_b(1+x), b > 0, b != 1.
Součet prvních N členů (A1) je přesně

```
log_b((1+x)(N+1)/(N+1+x)).
```

Jeho limita je G(x). Normalizace distribuční funkce G(1) = 1
určuje b = 2. Invariantní distribuční funkce je tedy lg(1+x).

## 2. Vážený operátor a kladný operátor pro derivace

Pro spojitou funkci g na [0,1] definujeme

```
w_k(x) = (1+x)/((k+x)(k+1+x))
       = k/(k+1+x) - (k-1)/(k+x),
(T g)(x) = sum_(k>=1) w_k(x) g(1/(k+x)).                  (A2)
```

Váhy jsou kladné a jejich součet je 1. Jestliže g(x)=(1+x)G'(x),
pak T g = (1+x)(S G)'. Pro spojitou funkci phi definujeme

```
(U phi)(x) = sum_(k>=1) [
  k/(k+1+x)^2 * integral_(1/(k+1+x))^(1/(k+x)) phi(t) dt
  + (1+x)/((k+x)^3 (k+1+x)) * phi(1/(k+x)) ].             (A3)
```

Každý člen je nezáporný pro phi >= 0. Operátor U tedy zachovává
uspořádání funkcí. První část členu má velikost O(k^-3), druhá
O(k^-4), stejnoměrně v x; řada definuje spojitou funkci.
Pro g se spojitou derivací platí

```
(T g)' = -U(g').                                         (A4)
```

Přesný konečný výpočet se součtem do N má na pravé straně
identity -(T_N g)' = U_N(g') navíc člen
N g(1/(N+1+x))/(N+1+x)^2. Ten stejnoměrně mizí. To přímo
ospravedlňuje přeskupení členů v knižním důkazu.

Pro úlohu 20 lze (A1) pomocně definovat pro všechna x >= 0.
Na každém kompaktním intervalu opět platí stejnoměrné odhady.
Teleskopický součet dává

```
S G(x+1) - S G(x) = G(1/(1+x)) - G(0).
```

Po derivování a dosazení g=(1+x)G', h=(1+x)(SG)' dostáváme

```
h(x)/(1+x) - h(x+1)/(2+x)
 = [1/(1+x) - 1/(2+x)] g(1/(1+x)).                       (A5)
```

To je (38); tvar v odpovědi 652 má opačné strany i znaménko
a je s (A5) totožný.

## 3. Celý důkaz věty W a úlohy 23

Zaveďme chybu v logaritmické souřadnici
R_n(y)=F_n(2^y-1)-y pro y v [0,1] a f_n(x)=(1+x)F_n'(x).
Platí f_(n+1)=T f_n, f_0=1+x, a z (A4) plyne

```
f_n' = (-1)^n U^n 1,
f_n(x) = [1 + R_n'(lg(1+x))]/ln 2,
(-1)^n R_n''(lg(1+x)) = (1+x)(ln 2)^2 (U^n 1)(x).        (A6)
```

Symbol 1 v U^n 1 označuje konstantní funkci. Spojitost všech
potřebných derivací plyne indukcí z (A2)–(A4).
Pro g(x)=1+x-1/(1+x) přímé teleskopování (A2) dává

```
T g = 1/(1+x),
phi(x) = g'(x) = 1 + 1/(1+x)^2,
U phi = 1/(1+x)^2.
```

Na [0,1] proto 2 <= phi/Uphi <= 5 a 5/4 <= phi <= 2.
Pozitivita U a indukce dávají 5^-n phi <= U^n phi <= 2^-n phi.
Porovnání s konstantní funkcí 1 pak dává

```
(5/8) 5^-n <= U^n 1 <= (8/5) 2^-n,
(5/8)(ln 2)^2 5^-n <= (-1)^n R_n'' <= (16/5)(ln 2)^2 2^-n.
```

Protože R_n(0)=R_n(1)=0, interpolační zbytek je
R_n(y)=-y(1-y)R_n''(xi)/2 pro vhodné xi v (0,1).
Po návratu k x leží F_n(x)-lg(1+x) mezi

```
(5/16)(-1)^(n+1) 5^-n ln(1+x) ln(2/(1+x)),
(8/5) (-1)^(n+1) 2^-n ln(1+x) ln(2/(1+x)).
```

Pořadí dolní a horní meze se mění s paritou n; knižní formulace
„between“ je správná. V krajích x=0,1 jsou obě strany nulové.
Odhad O(2^-n) je stejnoměrný. To uzavírá větu W.

Pro úlohu 23 označme M_n=max_[0,1]|R_n''|. Z obou nulových
okrajových hodnot plyne identita

```
R_n'(y) = integral_0^y t R_n''(t) dt
          - integral_y^1 (1-t) R_n''(t) dt.
```

Tedy |R_n'(y)| <= M_n[y^2+(1-y)^2]/2 <= M_n/2, i v krajích.
Dosazení do (A6) dokazuje přesně (53), f_n=1/ln 2+O(2^-n).
Také tištěný důkaz přes Taylorův interpolační zbytek je správný:
pro y>0 platí R_n'(y)=R_n(y)/y+(y/2)R_n''(theta), a výše
odvozený odhad R_n(y) obsahuje faktor y, který dovoluje uniformní
odhad při y blízkém nule.

## 4. Úloha 21: parametr a přesné lepší meze

Pro libovolné c>0 definujme na [0,1]

```
g_c(t) = (1+t)/(1+(c-1)t) - 1/(1+ct),
phi_c(t) = g_c'(t)
 = c/(1+ct)^2 + (2-c)/(1+(c-1)t)^2
 = (2+2ct+ct^2)/[(1+ct)^2(1+(c-1)t)^2] > 0.
```

I pro c>2 je poslední výraz kladný. Teleskopický člen (A2) je

```
w_k(x) g_c(1/(k+x))
 = (1+x)[1/((k+x)(k+x+c-1))
          -1/((k+x+1)(k+x+c))].
```

Proto T g_c=1/(x+c), U phi_c=1/(x+c)^2. Definujme poměr

```
R_c(x) = phi_c(x)/(U phi_c)(x)
 = (x+c)^2(2+2cx+cx^2)/[(1+cx)^2(1+(c-1)x)^2].           (A7)
```

Jeho derivace je -2(x+c)P_c(x)/[(1+cx)^3(1+(c-1)x)^3], kde

```
P_c(x) = (c^4-3c^2+c)x^3 + (3c^4-3c^3-3c)x^2
         +(6c^3-6c^2-3c)x + 3c^2-2c-2.
```

Pro 0<c<=1 jsou poslední tři koeficienty záporné. Jestliže první
je kladný, jeho součet s konstantním členem je c^4-c-2<0;
jinak je zápornost P_c okamžitá. R_c tedy roste a jeho minimum
je R_c(0)=2c^2<=2. Pro c>=tau, kde tau=(1+sqrt(5))/2, jsou
všechny koeficienty P_c kladné: v c=tau jsou postupně
tau-1, 3, 3tau, tau+1 a jejich derivace jsou dále kladné.
R_c tedy klesá a minimum je R_c(1)=(3c+2)/c^2<=tau^2.
Obě krajní tvrzení odpovědi souhlasí.

Pro c=65633/50000, tedy přesně 1.31266, program certifikuje

```
29/100 < (U phi_c)(x)/phi_c(x) < 31/100,  0<=x<=1.        (A8)
```

Stejné meze platí i pro jednodušší c=21/16. Nejde o vzorkování:
po odstranění kladných jmenovatelů mají příslušné polynomy
kladné Bernsteinovy koeficienty na uloženém racionálním dělení
[0,1]. Bernsteinovy bázové polynomy jsou
binom(d,j)t^j(1-t)^(d-j), nezáporné a se součtem 1; kladné
koeficienty proto dokazují kladnost na celém intervalu. Program
nezávisle zpětně rekonstruuje původní polynom a ověří, že intervaly
dělení pokrývají [0,1] bez mezer. Všechny koeficienty jsou přesné
racionální hodnoty uložené v výsledku.

Rovnost obou krajních hodnot (A7) vede na 2c^4-3c-2=0,
s kořenem přibližně 1.3126597547. Kniha netvrdí, že při této
volbě leží minimum na kraji; opravdu je uvnitř intervalu.
Z (A8) a pozitivity U plyne přesně knižní mez
(0.29)^n phi_c <= U^n phi_c <= (0.31)^n phi_c.

Poslední poznámku odpovědi o lepších lineárních kombinacích
potvrzuje konkrétní další certifikát. Položme

```
phi = -20 phi_1 + 3410 phi_(3/2) - 1581 phi_2.
```

Stejným racionálním postupem je na celém [0,1] doloženo
phi>0 a 0.30 phi < U phi < 0.305 phi. Tedy také
(0.30)^n phi <= U^n phi <= (0.305)^n phi. Jednotlivé koeficienty
kombinace nemusí být kladné; kladnost výsledné funkce je součástí
certifikátu, nikoli předpoklad podle numerického grafu.

## 5. Nezávislé sevření čtyřicetimístné hodnoty F_2(1/2)

Označme H_x=sum_(k>=1)(1/k-1/(k+x)). Pak F_1(x)=H_x a pro |x|<1
je H_x=sum_(j>=1)(-1)^(j-1)zeta(j+1)x^j, kde
zeta(s)=sum_(k>=1)k^-s pro reálné s>1. Tato přímá geometrická
expanze také potvrzuje známou opravu x^4 u zeta(5).
Separováním členu k=1 v S H dostaneme

```
F_2(1/2) = 1-H_(2/3) + sum_(j>=1) (-1)^(j-1)zeta(j+1)D_j,
D_j = sum_(k>=2) [k^-j - (k+1/2)^-j],
D_1 = 5/3 - 2 ln 2,
D_j = 1+(2/3)^j-(2^j-2)(zeta(j)-1),  j>=2.
```

Součty lze zaměnit absolutně, protože argumenty zbylých H jsou
nejvýše 1/2. Integrál H_x=integral_0^1(1-t^x)/(1-t) dt dává po
substituci t=u^3
H_(2/3)=3/2+pi/(2sqrt(3))-(3/2)ln 3. Pro zbytek po j=J platí

```
|zbytek| <= 2 zeta(2)[2^(-J-1) + 2^-J/J].
```

Důvod: D_j<=sum_(k>=2)k^-j, součet geometrických ocasů je nejvýše
2 sum_(k>=2)k^(-J-1), a poslední součet je nejvýše
2^(-J-1)+integral_2^infinity t^(-J-1)dt.

Arb při 180 desetinných pracovních místech a J=220, s touto
analytickou mezí a řízeným zaokrouhlením, dává

```
F_2(1/2) = 0.57655932769991408418826187212227055924517382452490596764600293209
           s absolutní chybou nejvýše 1.32e-66.
```

Přesné dyadické krajní body jsou uloženy. Tištěná hodnota končící
na 2452 je **správně zaokrouhlena na 40 míst**. První vlastní
assertion chybně předpokládala useknutí; její selhání nebylo
chybou knihy. Po opravě prošel jen tento dosud neuzavřený checkpoint,
bez opakování hotových kontrol. Také F_1(1/2)=2-2ln2 a invariantní
lg(3/2) se správně zaokrouhlují na tištěných 0.61371 a 0.58496.

## 6. Reprodukce a rozsah

Program: `verify_euclid_gauss.py`; výsledek: `results/euclid-gauss.json`.
Závislosti: SymPy a python-flint 0.9.0. V této relaci je druhá
knihovna v `/tmp/knuth-vol2-or9kgh/python-deps`; reprodukční příkaz:

```
PYTHONPATH=/tmp/knuth-vol2-or9kgh/python-deps \
  python3 workstreams/vol2/verify_euclid_gauss.py --resume
```

Checkpointy: 8 symbolických identit, čtyři přesné polynomiální
meze pro dvě volby c, rigorózní F_2 a další pozitivní kombinace.
PID1190631/session49372 skončil 1 na uvedené vlastní chybě
interpretace zaokrouhlení; identity a meze již prošly. PID1192029
skončil 0 po dokončení číslic. PID1192180/session81026 skončil 0
po přidání certifikátu kombinace. Předchozí checkpointy se neopakovaly.

Výše uzavřený rozsah není důkazem spektrálního rozvoje (44), všech
40 číslic lambda v (41), tvrzení o singularitách ani bibliografické
priority. Tyto položky a historický kontext zůstávají otevřené.

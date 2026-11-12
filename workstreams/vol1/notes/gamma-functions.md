# §1.2.5: analytické pokračování faktoriálu

Základní diskrétní definice a číslování úloh jsou v
[factorials.md](factorials.md). Zde `Gamma(z)` označuje knižní gama
funkci a `z!=Gamma(z+1)`. Písmeno z může být komplexní; pro kladné
reálné t definujeme `t^z=exp(z ln t)` s reálným ln t.
Pól znamená izolovanou singularitu s konečnou hlavní částí Laurentovy
řady; meromorfní funkce je holomorfní mimo takové póly. Výrazy
„nekonečno“ v knize odkazují k těmto pólům, ne ke konečné reálné hodnotě.

## Eulerova limita, nulové body a rekurence

Čísla `H_m=sum_{j=1}^m 1/j` splňují, že H_m−ln m klesá a je
kladné, porovnáním součtu s integrálem 1/t. Označme jejich limitu
gamma_E (Eulerova konstanta). Eulerovu aproximaci (15) značíme
`Gamma_m(z)=m^z m!/[z(z+1)...(z+m)]`, kde m>=1.
Její převrácená hodnota je

```text
1/Gamma_m(z) = z exp(z(H_m−ln m))
               product_{j=1}^m (1+z/j)exp(−z/j).
```

Na každé omezené množině z je pro dost velké j
`log(1+z/j)−z/j=O(1/j²)` stejnoměrně. Součin proto konverguje
stejnoměrně na kompaktních množinách a určuje celou funkci

```text
1/Gamma(z)=z exp(gamma_E z) product_{j>=1}(1+z/j)exp(−z/j).  (G1)
```

Mimo 0,−1,−2,... je nenulová: konečné počáteční faktory jsou
nenulové a ocas je exponenciála konvergentní řady. V každém
z uvedených bodů má právě jednoduchou nulu. To současně dokazuje
existenci knižní limity mimo póly, jednoduché póly Gamma a skutečnost,
že Gamma nemá žádné nuly. Žádná volba větve logaritmu pro celý
nekonečný součin není potřeba; logaritmus byl použit jen pro ocas.

Poměr konečných aproximací je
`Gamma_m(z+1)/Gamma_m(z)=zm/(z+m+1)`. Limitou dostáváme
Gamma(z+1)=z Gamma(z), kde obě konečné hodnoty existují, a dále
jako meromorfní identitu. To ověřuje (14), (15) a úlohu 10;
rovnice s nekonečnými hodnotami v pólech není běžná číselná rovnost.

Úloha 8: pro celé n>=0 je aproximace n! rovna
`n! product_{j=1}^n m/(m+j)`, která jde k n!, včetně prázdného
součinu pro n=0. Úloha 9 pak dává Gamma(1/2)=sqrt(pi) a
Gamma(−1/2)=−2sqrt(pi), za použití zadané hodnoty (1/2)!.

## Integrální vyjádření: úlohy 19–20

Pro x>0,m>=0 je integrace po částech v
`B_m(x)=integral_0^1 (1-t)^m t^(x−1) dt` oprávněná; okrajové
členy mizí pro m>=1 a B_0(x)=1/x. Rekurence
`B_m(x)=m B_(m−1)(x+1)/x` dává
`B_m(x)=m!/[x(x+1)...(x+m)]`.
Pro m>=1 změna t=mu tedy dokazuje přesně úlohu 19.

Nerovnost z úlohy 20 lze dokázat bez integrálních limit.
Pro 0<=t<=m dá 1+s<=exp(s), s=±t/m, vztahy

```text
exp(−t) >= (1−t/m)^m
 >= exp(−t)(1−t²/m²)^m
 >= exp(−t)(1−t²/m).
```

Poslední krok je Bernoulliho nerovnost pro argument −t²/m²∈[−1,0].
Tedy rozdíl je mezi 0 a t² exp(−t)/m, včetně krajních bodů.
Po vynásobení t^(x−1) a integraci je rozdíl mezi Gamma_m(x)
a `integral_0^infinity exp(−t)t^(x−1) dt` omezen součtem

```text
integral_m^infinity exp(−t)t^(x−1)dt
 + (1/m) integral_0^infinity exp(−t)t^(x+1)dt.
```

Oba integrály jsou konečné: u nuly x>0, v nekonečnu exponenciála
převáží pevnou mocninu. První ocas i druhý člen jdou k nule.
Eulerův integrál je tím dokázán. Stejná majoranta s Re(z)>0
dokazuje komplexní verzi. Chybějící dt ve staré odpovědi je opraveno
erratem z 2. prosince 1997. Pozdější změna „less than“ na „at most“
(2023) zachovává platný odhad; není to nový nález.

## Součiny a reflexe: úlohy 17,18,23

17. Pro pevné parametry alpha_j,beta_j se stejným součtem
se mocniny m z Eulerových aproximací vykrátí. Zbývající konečný
součin je přesně `product_{n=1}^m product_j(n+alpha_j)/(n+beta_j)`.
Limitou vyjde podíl `product Gamma(1+beta_j)/Gamma(1+alpha_j)`.
Beta nesmí být záporné celé číslo, jinak by konečný součin dělil
nulou. Je-li alpha záporné celé číslo, součin je od jistého místa
nulový a pravou stranu interpretujeme pomocí celé funkce 1/Gamma;
je rovněž nulová. Nejde o neodůvodněné krácení nekonečna.
Pro ostatní alpha lze též přímo sečíst logaritmy faktorů: členy
řádu 1/n se anulují a ocas je O(1/n²).
[DLMF 5.8.4–5](https://dlmf.nist.gov/5.8) potvrzuje tutéž podmínku
po posunu parametrů o 1.

18. Wallisův součin v zadání je
`product_{n>=1} n²/[(n−1/2)(n+1/2)]`.
Předchozí úloha dává Gamma(1/2)Gamma(3/2)=2Gamma(3/2)².
Rovnost s pi/2 a kladnost Gamma(3/2) z Eulerových aproximací dávají
(1/2)!=sqrt(pi)/2. Kladné znaménko odmocniny je zde odůvodněné.
Konvergence Wallisova součinu je také nezávisle dokázána níže.

23. Značme `F_m(w)=m^w m!/product_{j=1}^m(w+j)` konečnou
aproximaci w!. Přímým vynásobením konečných součinů dostaneme
`z F_m(−z) Gamma_m(z)=product_{j=1}^m(1−z²/j²)^(-1)`.
V limitě je tedy z Gamma(1−z) Gamma(z) rovno tomuto nekonečnému
součinu. Na žádném konečném stupni se nezaměňují dvě různě
posunuté aproximace gama funkce.
Z předpokládaného sinusového součinu
`sin(pi z)=pi z product_{n>=1}(1−z²/n²)` plyne
`Gamma(1−z)Gamma(z)=pi/sin(pi z)` pro z necelé.
To je (16), protože (−z)!=Gamma(1−z). Ztracené z před součinem
v navigačním Markdownu není v originálu.

## Hankelova smyčka (17)

Volme větev t^(−z)=exp(−z Log t) s argumentem od −pi do pi.
Dráha jde pod zápornou osou od −nekonečna k −rho, obejde počátek
proti směru hodinových ručiček po kružnici poloměru rho>0 a vrátí
se nad zápornou osou. Hodnota integrálu je nezávislá na rho podle
Cauchyovy věty v rozříznuté rovině. Pro Re(z)<1 lze nechat rho→0;
kružnice přispívá O(rho^(1−Re(z))). Dvě polopřímky dávají

```text
integral_H exp(t)t^(−z)dt
 = (exp(i pi z)−exp(−i pi z)) Gamma(1−z).
```

Po vydělení 2pi i a reflexi je výsledek 1/Gamma(z).
Při pevném rho je levá strana celá funkce z: v nekonečnu je
stejnoměrná exponenciální majoranta, dráha se vyhýbá nule.
Věta o identitě proto rozšíří výsledek na všechna komplexní z.
Původní formule je správná se standardní volbou větve; zmenšení
smyčky na nulu pro Re(z)>=1 by naopak neoprávněně zahodilo člen.
Tvar dráhy a volbu větve výslovně potvrzuje
[DLMF 5.9.2](https://dlmf.nist.gov/5.9.E2).

## Stirlingův odhad (7), chyba a doplnění z 2019

Následující důkaz uzavírá lokální odkaz na asymptotiku, aniž by
prohlašoval celý §1.2.11.2 za prověřený. Pro n>=1 položme
`b_n=ln(n!)−(n+1/2)ln n+n`. S u=1/(2n+1) dostáváme

```text
b_n−b_(n+1) = (n+1/2)ln(1+1/n)−1
             = sum_{j>=1} u^(2j)/(2j+1) = d_n.          (S1)
```

Proto 0<d_n<u²/[3(1−u²)]=1/[12n(n+1)]. Součet d_n konverguje,
takže b_n má konečnou limitu c a
`0<b_n−c<1/(12n)`. Navíc d_n=1/(12n²)+O(n^(−3)), a porovnání
ocasu s integrálem dává `b_n−c=1/(12n)+O(n^(−2))`.

K určení c vezměme `I_r=integral_0^(pi/2) sin(t)^r dt`.
Integrace po částech dává I_r=(r−1)I_(r−2)/r, s I_0=pi/2,I_1=1.
Z I_(2n+1)<=I_(2n)<=I_(2n−1) a
I_(2n+1)/I_(2n−1)=2n/(2n+1) plyne I_(2n+1)/I_(2n)→1.
Explicitní součiny dávají

```text
I_(2n)   = (pi/2) binom(2n,n)/4^n,
I_(2n+1) = 4^n/[(2n+1)binom(2n,n)],
I_(2n) I_(2n+1) = pi/[2(2n+1)].
```

Odtud binom(2n,n)~4^n/sqrt(pi n); stejným výpočtem vznikne
Wallisův součin pi/2. Dosazení definice b_n do logaritmu binomického
koeficientu dává `.5ln2+b_(2n)−2b_n→−.5ln pi`, tedy
c=.5ln(2pi). Proto

```text
n! = sqrt(2pi n)(n/e)^n exp(r_n),
0<r_n<1/(12n),  r_n=1/(12n)+O(n^(−2)).                 (S2)
```

To dokazuje (7), přibližnou relativní chybu 1/(12n) i první
korekci v úloze 5. Číselný příklad 8! a jeho zaokrouhlení jsou
zvlášť kontrolovány intervaly; symbol „přibližně“ není přesná rovnost.
Dodatek 22. ledna 2019 vkládá také
`sqrt(2pi)((n+1/2)/e)^(n+1/2)`. Jeho podíl k původnímu odhadu
je `exp(1/(8n)+O(n^(−2)))`, takže poměr k n! je
`exp(1/(24n)+O(n^(−2)))`. I tento vztah je správné asymptotické
přiblížení; původní vzorec není chybný.

Pro pevné reálné x lze z Eulerovy integrální reprezentace a
logaritmické konvexity Gamma dostat poměrovou limitu úlohy 22.
Konkrétně pro 0<=s<=1 a y>0 platí
`(y/(y+s))^(1−s) <= Gamma(y+s)/(y^s Gamma(y)) <=1`.
Horní mez plyne z Hölderovy nerovnosti mezi Gamma(y) a Gamma(y+1);
dolní z téže horní meze aplikované na y+s a exponent 1−s,
s použitím Gamma(y+1)=y Gamma(y). Obě meze jdou k 1.
Konečně mnoha posuny rekurencí se pokryje libovolné pevné reálné x.

## Konvergentní Newtonova řada (12)

Značme `C(x,m)=x(x−1)...(x−m+1)/m!`. Pro m>=2 jsou koeficienty
z diskrétní poznámky dány Frullaniho integrálem

```text
m! a_m = (−1)^m J_m,
J_m = integral_0^infinity exp(−t)(1−exp(−t))^(m−1)dt/t
    = integral_0^1 (1−u)^(m−1)du/(−ln u).               (N1)
```

Frullaniho vztah `ln b−ln a=integral_0^infinity(e^(−at)−e^(−bt))dt/t`
pro kladná a,b plyne integrací `1/s=integral_0^infinity e^(−st)dt`
přes s od a do b. Aplikace konečné diference ln(n+1) dává (N1).
Z −ln u>=1−u dostáváme 0<J_m<=1/(m−1).
Pro pevné reálné necelé x>-1 je `|C(x,m)|=O(m^(−x−1))`:
po využití rekurence Gamma jde o poměr Gamma(m−x)/Gamma(m+1),
jehož odhad je právě poměrová limita dokázaná výše.
Řada v (12) proto konverguje absolutně pro x>-1.

Sečtením binomické řady pod integrálem, oprávněným právě absolutní
majorantou, dostaneme

```text
sum_{m>=2} a_m x^(falling m)
 = integral_0^infinity
      [x exp(−t)+(exp(−xt)−1)/(exp(t)−1)]dt/t.          (N2)
```

Tento integrál je ln Gamma(x+1). Přímo: logaritmus konečné Eulerovy
aproximace (13) se od pravé strany (N2) liší o
`integral_0^infinity exp(−mt)[(1−exp(−xt))/(exp(t)−1)−x]dt/t`.
Závorka je O(t) u nuly a má nejvýše exponenciální růst v nekonečnu;
pro dost velké m tedy integrál jde k nule rozdělením na (0,1)
a (1,infinity). Tím je shoda obou rozšíření dokázána na reálném
oboru x>-1, který zahrnuje všechny kladné neceločíselné argumenty.
Text nelze číst jako neomezené tvrzení o obyčejné řadě na všech
záporných reálných číslech. Původní Hermitův pramen a přesný historický
obor je nutné posoudit samostatně; nerozšiřujeme závěr pouhou analogií.

## Graf a číselný certifikát

Logaritmická derivace `psi(x)=Gamma'(x)/Gamma(x)` pro x>0 má
`psi'(x)=sum_{j>=0}1/(x+j)²>0`, odvozením (G1).
Z 0<gamma_E<1 plyne psi(1)<0<psi(2), takže má právě jeden kořen
v (1,2). Gamma je kladná; tento bod je její jediné minimum na
kladné poloose. Rekurence určuje střídání znamének mezi zápornými
celými póly, jejich strany a hodnoty Gamma(1)=Gamma(2)=1,
Gamma(3)=2,Gamma(4)=6. To kontroluje kvalitativní obsah obr. 7.
Nové umístění popisek z errat 1998 nemění funkci.

Jediný běh `check_gamma_constants.py` prošel. Racionální intervaly
certifikují znaménko psi na obou koncích intervalu obsahujícího
minimum; následuje interval pro ln Gamma a exponenciálu.
Výpočty posouvají argument o 64 rekurencí a používají rozvoj
s Bernoulliho čísly definovanými níže a s výslovným zbytkem. Pro kladný
reálný argument jsou absolutní zbytky rozvojů ln Gamma a psi
nejvýše absolutní hodnota prvního vynechaného členu;
viz [DLMF 5.11(ii)](https://dlmf.nist.gov/5.11#ii).
Všechny zaokrouhlovací operace v certifikátu směřují ven.
Výsledek `results/gamma-constants.json` obsahuje zejména

```text
1.46163214496836234126265954 < x_min
                           < 1.46163214496836234126265955,
0.885603194410888700278815900582588733184546743 < Gamma(x_min)
                           < 0.885603194410888700278815900582588733242547461.
```

Na levém konci je psi<0, na pravém psi>0. Její monotonie zaručuje
jediný kořen; věta o střední hodnotě omezuje změnu ln Gamma mezi
levým koncem a kořenem. Tím je potvrzeno všech 25 otištěných
desetinných míst obou souřadnic, včetně zaokrouhlení. Stejný běh
ověřil log10(1000!), sqrt(pi), exp(−8) a příklad pro 8!.
Používá už dříve certifikované intervaly konstant; dřívější kontroly
se neopakovaly. Knihovní vyhodnocení Gamma není součástí důkazu.

## Divergence Stirlingovy řady a historické prameny

Bernoulliho polynomy B_r(t) jsou určeny formální identitou
`s exp(ts)/(exp(s)−1)=sum_{r>=0} B_r(t)s^r/r!` a Bernoulliho
čísla jsou B_r=B_r(0). Odtud B_1(t)=t−1/2,
`B_r'=r B_(r−1)`, nulový integrál pro r>=1 a B_r(1)=B_r(0)
pro r>=2. Integrací po částech vyjde pro nenulové celé j
Fourierův koeficient B_r roven `−r!/(2pi i j)^r`.
Pro r=2k>=2 je Fourierova řada absolutně konvergentní a dosazení
t=0 dává

```text
|B_(2k)| = 2(2k)!/(2pi)^(2k) sum_{j>=1} j^(−2k).
```

Koeficient logaritmické Stirlingovy řady při z^(−2k+1) je
`B_(2k)/[2k(2k−1)]`; jejich absolutní hodnoty proto rostou alespoň
jako `2(2k−2)!/(2pi)^(2k)`. Pro každé pevné nenulové z tedy
členy nejdou k nule. I multiplikativní Stirlingova mocninná řada
v 1/z má nulový poloměr konvergence: kdyby měla kladný poloměr,
její hodnota 1 v nule by umožnila analytický logaritmus v okolí
nuly, a ten by dal konvergentní logaritmickou Stirlingovu řadu.
Asymptotický smysl těchto rozvojů a použité zbytky jsou v DLMF 5.11;
divergence tedy neodporuje odhadu (S2) ani konečným aproximacím.

Relevantní pasáže Davisova článku z roku 1959 byly přečteny ze
skenu: s. 850–853 popisují Eulerovu interpolaci a limitu,
s. 860–862 obsahují součinové formule a konvergentní Newtonovu
řadu připisovanou Hermitovi. Davis uvádí obor Re(z)>0; náš důkaz
výše zahrnuje reálné x>−1. Jde o kontrolu Knuthova konkrétního
odkazu na Davise, nikoli o čtení všech historických originálů.
Hermitovy dopisy Pincherlemu z roku 1900 byly publikovány v roce
1901 a přetištěny v Oeuvres IV, s. 529–543; primární pasáž zatím
není získána. Knoppova citace a ostatní historické atribuční údaje
zůstávají otevřené v evidenci zdrojů.

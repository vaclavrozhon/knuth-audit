# §1.2.4-39–40: replikativní funkce

Kontrola 1. listopadu 2026. Zadání s. 43–44 a odpovědi 478–479
byly přečteny z původních obrazů. Funkci f nazýváme replikativní,
jestliže pro každé kladné celé n a každý přípustný reálný x platí

```text
sum_{k=0}^{n−1} f(x+k/n) = f(nx).                       (1)
```

V základní třídě jsou hodnoty konečné; zvláštní příklad 39(f)
výslovně dovoluje −nekonečno. Operace s nekonečnými hodnotami
používáme jen tehdy, když jsou definovány. `floor`, `ceil` a
`frac(x)=x-floor(x)` jsou celé a zlomkové části z předchozí poznámky.
Indikátor `[P]` má hodnotu 1, když tvrzení P platí, jinak 0.

## Úloha 39: všechny příklady

(a) Pro f(x)=x−1/2 je levá strana
`nx+(n−1)/2−n/2=nx−1/2`.

(b),(c) Je-li nx celé, mezi x+k/n pro 0<=k<n je právě jedno
celé číslo: ceil(x). Je kladné právě když je celé číslo nx kladné.
Není-li nx celé, není celé žádné z těchto čísel. Tím jsou dokázány
oba indikátory, včetně x<=0 a bodů na hranici.

(d),(e) Využijeme iracionalitu pi: zápis r pi+s s r,s racionálními
je jednoznačný. Pokud nx=r' pi+m' s r' racionálním a m' celým,
pak x+k/n=(r'/n)pi+(m'+k)/n má celočíselný druhý koeficient
právě pro jeden k v 0,...,n−1. Tento koeficient je ceil(m'/n),
a je kladný právě když m'>0. Rovněž r'/n>0 právě když r'>0.
Pokud nemá nx žádný takový zápis, nemá jej žádný člen vlevo.
To dokazuje základní indikátor i všechny tři verze s kladností
r a/nebo m. Stejný důkaz funguje s libovolným pevným iracionálním
číslem místo pi; nepotřebuje žádnou numerickou aproximaci pi.

(f) Položme z=exp(2 pi i x), kde i²=−1, a omega=exp(2 pi i/n).
Faktorizace polynomu t^n−1 dává
`product_{k=0}^{n−1}(1−z omega^k)=1−z^n`.
Absolutní hodnoty tedy dávají

```text
product_{k=0}^{n−1}|2 sin(pi(x+k/n))| = |2 sin(pi n x)|.  (2)
```

Logaritmus dokazuje (1) mimo nuly. Pokud nx je celé, právě jeden
člen má nulový sinus, takže obě strany logaritmické identity
jsou −nekonečno; nevyskytuje se neurčité nekonečno minus nekonečno.
Platí to pro libovolný pevný logaritmický základ >1.
Pro základ mezi 0 a 1 by nuly dávaly +nekonečno, což není zde
zvolená konvence.

Silnější podepsaný součin v knižní odpovědi je rovněž správný.
Použitím `2 sin(theta)=(1−exp(−2i theta))exp(i theta−i pi/2)`
dostaneme fázový faktor exp(i pi(nx−1/2)) a faktor
1−exp(−2 pi i nx), jejichž součin je 2 sin(pi nx).
Dvě pomocné exponenciální identity v knize jsou platné i s komplexním
argumentem; v první se pro tento účel dosadí ix za x.

(g),(h) Konečný součet v (1) je lineární: součet funkcí a skalární
násobek splňují stejnou rovnici. Pro funkce s nekonečnými hodnotami
se musí zachovat obvyklá definovanost aritmetických operací.

(i) Pro g(x)=f(frac(x)) jsou obě strany požadované identity
periodické s periodou 1/n: posun x o 1/n jen cyklicky permutuje
argumenty vlevo a posune nx o 1 vpravo. Stačí proto 0<=x<1/n.
V tomto intervalu všechny argumenty x+k/n i nx leží v [0,1),
a rovnice pro g je totožná s rovnicí pro f. Toto je krátký
důkaz bez neodůvodněného posouvání samotné nereplikované f.

## Úloha 40: přesná klasifikace pro lokální Riemannův integrál

Knižní tvrzení je správné: každá konečná replikativní funkce,
která je Riemannovsky integrovatelná na každém omezeném intervalu,
má skoro všude tvar

```text
f(x)=a(x−1/2)+b max(floor(x),0)+c min(floor(x),0).        (3)
```

„Skoro všude“ znamená mimo množinu Lebesgueovy míry nula; (3)
nepředepisuje jednotlivé výjimečné hodnoty. Pro spojitou f se
tvrzení zjednoduší na f(x)=a(x−1/2) všude. Následující důkaz
rozepisuje kroky z odpovědi a vysvětluje, proč samotné použití
Fourierových koeficientů nevynechá další řešení.

Nejprve definujme h(x)=f(x+1)−f(x). Odečtení (1) pro argumenty
x+1/n a x dává h(nx)=h(x). Odtud h(qx)=h(x) pro každé kladné
racionální q. Funkce h je lokálně Riemannovsky integrovatelná,
má tedy bod spojitosti v každém otevřeném intervalu.
Zvolme jeden kladný bod spojitosti y. Pro libovolné x>0 existují
kladná racionální q_j s q_j x→y; proto h(x)=lim h(q_j x)=h(y).
Stejně je h konstantní na záporné poloose. Označme tyto konstanty
d_+ a d_−. Při spojitosti f je h spojitá i v 0, takže d_+=d_−.

Teď vezměme periodickou funkci g(x)=f(frac(x)), která je podle
39(i) replikativní a omezená na periodě. Její Fourierův koeficient
definujeme jako `c_j=integral_0^1 g(x) exp(−2 pi i j x) dx`.
Integrace (1) a změna proměnné dávají

```text
c_0=0,  c_(nj)=c_j/n   (j celé, n>=1).                 (4)
```

Například vlevo po násobení exp(−2 pi i nj x) dostaneme n c_(nj),
zatímco vpravo změnou y=nx a rozdělením n period dostaneme c_j.
Pro j=0 a n=2 vyjde c_0=0. Všechny kladné koeficienty jsou tedy
c_1/j a záporné c_(−1)/j pro j>0.

Pro odstranění možné kosinové složky použijeme Fejérův průměr:
jde o aritmetický průměr prvních N+1 částečných Fourierových součtů,
tedy konvoluci s nezáporným jádrem integrálu 1. V bodě 0 má hodnotu

```text
(c_1+c_(−1)) (sum_{j=1}^N 1/j − N/(N+1)).             (5)
```

Jeho absolutní hodnota je nejvýše sup|g|. Závorka v (5) roste
bez omezení, takže c_(−1)=−c_1. Periodická pila
s(x)=frac(x)−1/2 má c_0=0 a koeficient −1/(2 pi i j) pro j!=0,
jak plyne jednou integrací po částech. Funkce g a a s při
a=−2 pi i c_1 mají tedy všechny Fourierovy koeficienty shodné.
Fejérovy průměry konvergují v L1 k funkci, a proto g=a s skoro
všude. Není zde předpokládána bodová konvergence obyčejné řady.

Pro x=t+j, 0<t<1 a j celé, pak platí
f(x)=f(t)+j d_+ pro j>=0 a f(x)=f(t)+j d_− pro j<0.
Spojením s výsledkem na (0,1) dostáváme (3), kde
b=d_+−a a c=d_−−a. Spočetná unie posunutých nulových výjimečných
množin má opět míru nula. Obráceně všechny tři funkce v (3)
jsou replikativní: pro kladnou a zápornou část podlahy to plyne
z Hermitovy identity odděleně na x>=0 a x<0.

Pokud f je spojitá, shoda s a(x−1/2) na téměř celém (0,1)
se rozšíří na celý [0,1]. Odtud d_+=d_−=f(1)−f(0)=a;
posuny pak dávají globální tvrzení. Tím jsou doloženy oba
konkrétní klasifikační závěry v knižní odpovědi, včetně nulové funkce.

## Obecnější rovnice a příklady v zadání 40

Pišme obecně `sum f(x+k/n)=A_n f(nx)+B_n`.
Existuje-li derivace, derivováním dostaneme parametry n A_n,0.
Je-li B_n=0 a F primitivní funkce, derivace výrazu
`sum F(x+k/n)−(A_n/n)F(nx)` je nulová, tedy jde o konstantu
C_n nezávislou na x. Tím je přesně ověřeno tvrzení o integraci;
nové konstanty C_n nemusí být nula.

- Bernoulliho polynomy B_j(x) definujme koeficienty
  `t exp(xt)/(exp(t)−1)=sum_{j>=0} B_j(x)t^j/j!` blízko t=0.
  Geometrický součet v generující funkci dává
  `sum_{k=0}^{n−1} B_j(x+k/n)=n^(1−j) B_j(nx)`.
  Viz také [DLMF 24.4.18](https://dlmf.nist.gov/24.4.E18).
- Logaritmická derivace podepsaného součinu sinusů z 39(f),
  mimo póly, dává `sum cot(pi(x+k/n))=n cot(pi nx)`.
  Další derivace dává
  `sum csc²(pi(x+k/n))=n² csc²(pi nx)`.
  Originál opravdu uvádí **csc²**; chybějící druhá mocnina
  v Markdownu je již evidována jako V1-X0008.
- Pro Hurwitzovu funkci zeta(s,x)=sum_{j>=0}(j+x)^(−s), x>0
  a Re(s)>1, je řada absolutně konvergentní. Rozdělení indexů
  podle zbytku modulo n dává `sum zeta(s,x+k/n)=n^s zeta(s,nx)`.
  Pokračování v parametru s platí tam, kde jsou konečné hodnoty
  definovány; s=1 je pól. [DLMF 25.11.1 a 25.11.15](https://dlmf.nist.gov/25.11)
  potvrzuje obor řady i pokračovaný vztah.
- Psi je logaritmická derivace gama funkce, psi(x)=Gamma'(x)/Gamma(x).
  Logaritmická derivace Gaussova součinového vzorce dává
  `sum psi(x+k/n)=n psi(nx)−n ln(n)`, mimo póly.
  Parametry jsou A_n=n,B_n=−n ln(n).
  [DLMF 5.5.6 a 5.5.9](https://dlmf.nist.gov/5.5) potvrzuje znaménko.

Oblast definice je podstatná: příklady s cot, csc², psi a zeta
nejsou konečné spojité funkce na celé reálné ose, takže neodporují
výše dokázané klasifikaci. Zadání výslovně otevírá obecnější třídu;
netvrdí existenci bezpólového rozšíření těchto příkladů.

## Primární prameny a přesný rozsah

Yoderův původní článek *Continuous replicative functions*,
Aequationes Math. 13 (1975), 251–261, je uložen v
`sources/yoder-continuous-replicative-1975.pdf`. Knihovní zdroj:
[GDZ, svazek 13](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356261603_0013/PPN356261603_0013.pdf).
Uchován je jen článek, původní strany souboru 258–268; hash celého
staženého svazku i výřezu je v metadatech. Prohlédnuty úvod,
Fourierův důkaz Theorem 3 na s. 253–255, příslušné části
Corollary 3.4 na s. 256 a bibliografie s. 261. To ověřuje relevanci
citace; nejde o audit všech tvrzení Yoderova článku. Yoder normalizuje
levou stranu faktorem 1/n, takže běžná replikativita u něj má a_n=1/n.

Jeho [disertace z roku 1978](https://thesis.caltech.edu/17845/)
byla použita jako další primární navigace k tématu; článek nebyl
nahrazen pozdější disertací. Mordellovu citaci 33 (1958),371–375
potvrzuje [vydavatelský záznam](https://academic.oup.com/jlms/article-abstract/s1-33/3/371/798195),
ale samotný text dosud nebyl získán. Tento zdrojový zbytek zůstává otevřený.

Errata `all1-prepre`, s. 32, opravují chybějící i v exponenciále
na posledním řádku s. 478 (8. března 2002). Opravený vzorec je
právě (4) s opačnou znaménkovou konvencí Fourierova koeficientu.
Errata 5. dubna 2026 odstraňují chybnou značku řady (2) u
Mordellova svazku 33; náš první dotisk tuto pozdější chybu nemá.

# §4.5.3: konečné vstupy, symetrie a průměry

Audit 2026-11-03. Uzavírá úlohy 25–29 a matematický obsah
367–371, opravenou identitu(57) a podmíněné odvození(58)/(62).
Samotná Porterova věta(60), historické atribuce a složitost(63)
do tohoto bloku nepatří. Nový nález C0133 se týká dvou vad
v náhradě důkazu lemmatu M z roku 2011; lemma je správné.

Původní strany 367–373,376,652 a příslušné listy všech čtyř
vrstev errat byly přečteny. V all2-prepre jsou relevantní
opravy věty E z roku 2004, sedmi přibližných rovností z roku
2000, tabulky tau z roku 1998 a(57)/odpovědi29 z roku 2000.
All2-pre mění důkaz lemmatu M v roce 2011; nové vady v této
náhradě dokumentuje [C0133](C0133-lemma-m-quantifiers.md).
All2 a err2 neobsahují další opravu zde kontrolovaných tvrzení.

## 1. Lemma M a úloha25

Míra mu množiny zde znamená její délku. Pro jeden interval H
v [0,1] a rovnoměrnou síť P_n={0,1/n,...,(n-1)/n} platí

```
| |H intersect P_n| - n mu(H) | <= 1.                  (D1)
```

To je přímý počet celých čísel mezi n-násobky konců, pro
všechny čtyři volby otevřených či uzavřených krajů. Nechť I
a J jsou sjednocení po dvou disjunktních intervalů, jejichž
společný doplněk má míru nula. Vyberme z každé rodiny prvních
N intervalů tak, aby jejich celková délka byla alespoň
1-epsilon. Jejich sjednocení označme I_N a J_N. Pro
a_n=|I intersect P_n|/n dostáváme z(D1)

```
mu(I)-epsilon-N/n <= a_n <= mu(I)+epsilon+N/n.           (D2)
```

Při pevném epsilon je pevné také N. Nejprve necháme n růst,
pak epsilon klesat k nule. Tím je správná limita(45) dokázána.
Opravená inkluze používá zbytek K_N, nikoli původní nulovou
množinu K. Pomocné limity r_n/n a(r_n+t_n)/n samy obecně
nejsou mu(I); přesný protipříklad je v poznámce C0133.

Úloha25 ukazuje, že samotné spočetné sjednocení intervalů
nestačí. Očíslujme všechny racionální body v [0,1] jako q_k.
Pro pevné 0<epsilon<1 obalme každý q_k relativně otevřeným
intervalem H_k délky nejvýše epsilon/2^k. U krajních bodů
použijeme interval tvaru [0,b) nebo(a,1]. Jejich sjednocení
I obsahuje všechny racionální body, ale mu(I)<=epsilon.
Jeho komponenty jsou po dvou disjunktní intervaly; je jich
nejvýše spočetně mnoho, protože každá obsahuje jiný racionální
bod. Přesto |I intersect P_n|/n=1 pro všechna n. To přesně
vyvrací(45) při vynechání podmínky na doplněk. Argument
v odpovědi652 pomocí postupného odčítání konečného počtu
intervalů dává alternativní disjunktní rozklad a je správný.

## 2. Věta E, symetrie a úloha26

Pravidelný řetězový zlomek zapisujeme [0;a_1,...,a_t], kde
a_i jsou kladná celá čísla a poslední a_t>=2. Konečný zlomek
má hodnotu v (0,1). Gaussova transformace x->1/x-floor(1/x)
odstraňuje první podíl. Pro pevné k a kladné a jsou množiny
bodů, kde (k+1)-ní podíl existuje a je roven a, respektive je
jiný než a, sjednocení intervalů určených konečnými prefixy.
Kraje se přiřadí podle kanonické konečné reprezentace;
zbývající body s příliš krátkým rozvojem tvoří spočetnou
množinu míry nula. Lemma M se tedy použije na rovnoměrné
vstupy v/n, v=0,...,n-1. To je přesně opravený model věty E.

Je-li X_k zbytek po k Gaussových krocích a F_k jeho distribuce
pro původně rovnoměrný reálný vstup, dostáváme

```
lim_(n->infinity) Pr(A_(k+1)=a) = F_k(1/a)-F_k(1/(a+1)). (D3)
```

Případné rovnosti na krajích nemění spojité rozdělení.
Teprve dalším přechodem k->infinity dává věta W limitní
pravděpodobnost lg((a+1)^2/((a+1)^2-1)), kde lg je logaritmus
při základu2. Tato dvojí limita sama neurčuje rozdělení
podílu uprostřed libovolně dlouhého konečného rozvoje;
text tuto mez platnosti správně výslovně uvádí.

Continuant K_t(a_1,...,a_t) je jmenovatel konečného zlomku
v základním tvaru; jeho maticový důkaz a symetrie při obrácení
byly ověřeny v euclid-basic.md. Zlomky m/n s1<=m<=floor(n/2)
jsou právě kanonické rozvoje s a_1>=2, a_t>=2 a K_t dělícím n.
Obrácení seznamu podílů zachová všechny tři vlastnosti, což
dokazuje úlohu26 pro každé n, včetně redukovatelných zlomků.

Pro nesoudělné čitatele m a n je čitatelem obráceného zlomku
předchozí jmenovatel konvergentu. Determinantová identita
proto dává m*m_reverse = (-1)^(t-1) modulo n. To ověřuje
i dodatečnou poznámku odpovědi652. Pokud první podíl je1,
lze koncovou jedničku po obrácení normalizovat identitou(46).

Celá tabulka 28 zlomků se jmenovatelem29 byla přepočtena.
Má96 podílů, z toho39 jedniček,21 dvojek a8 trojek. Čtyři
limitní procenta na368 i tři empirická procenta na369 souhlasí
s předepsaným zaokrouhlením; známá změna rovností na přibližné
rovnosti je správná. Identity(46),(47) už byly obecně odvozeny
v základním bloku. Pro úlohu26 proběhlo65536 přesných obrácení
pro všechny n<=512, s vyhodnocením obráceného seznamu nezávisle
přes racionální zlomky.

## 3. Aritmetické identity a úlohy27/28

Značme T(u,v) počet dělení Eukleidova algoritmu; pro v=0
je T(u,0)=0, pro n>0 je T(0,n)=1. Definujeme

```
T_n = (1/n) sum_(m=0..n-1) T(m,n),
tau_n = (1/phi(n)) sum_(0<=m<n, gcd(m,n)=1) T(m,n).
```

Funkce phi(n) počítá nesoudělné zbytky modulo n, s phi(1)=1.
Společné vydělení vstupů jejich největším společným dělitelem
nezmění počet kroků. Rozdělení podle d=n/gcd(m,n) dává

```
n T_n = sum_(d|n) phi(d) tau_d.                         (D4)
```

Zahrnuje také m=0, které odpovídá d=1 a tau_1=1.

Möbiova funkce mu(n) je0, pokud n obsahuje čtverec prvočísla,
a jinak (-1)^r, kde r je počet různých prvočinitelů. Platí
mu(1)=1. Von Mangoldtova funkce Lambda(n) je ln p pro mocninu
prvočísla n=p^r, r>=1, a0 jinak. Z rozkladu na prvočísla
a z rozdělení n zbytků podle největšího společného dělitele
plynou první identity úlohy28:

```
sum_(d|n) mu(d) = [n=1],
sum_(d|n) Lambda(d) = ln n,
sum_(d|n) phi(d) = n.                                  (D5)
```

Hranatá závorka je1, když je výrok uvnitř pravdivý, jinak0.
Pro první identitu je součet roven součinu (1-1) přes různé
prvočinitele. Inverzní vztah: je-li f(n)=sum_(d|n)g(d), pak

```
sum_(d|n) mu(n/d)f(d)
 = sum_(c|n) g(c) sum_(e|n/c)mu(e) = g(n).               (D6)
```

Aplikace(D6) na druhou a třetí identitu(D5) dokazuje zbývající
dvě identity úlohy28, včetně n=1.

Pro úlohu27 potřebujeme přesnou váženou logaritmickou identitu

```
(1/n) sum_(d|n) phi(d) ln d
 = ln n - sum_(d|n) Lambda(d)/d.                        (D7)
```

Její odvození bez aproximace:

```
sum_(d|n)phi(d) ln(n/d)
 = sum_(d|n)phi(d) sum_(e|n/d)Lambda(e)
 = sum_(e|n)Lambda(e) sum_(d|n/e)phi(d)
 = n sum_(e|n)Lambda(e)/e.
```

Spolu se sum phi(d)=n to dává(D7). Je-li hypoteticky
tau_n=a ln n+C+e_n, a=12 ln2/pi^2, je z(D4),(D7) přesně

```
T_n = a(ln n-sum_(d|n)Lambda(d)/d)+C
      +(1/n)sum_(d|n)phi(d)e_d.                        (D8)
```

Pro omezené e_n je poslední člen omezený. Jestliže e_n->0,
jde i tento člen k nule: váha každé konečné množiny d je
O(1/n), zbývající hodnoty e_d jsou libovolně malé a všechny
váhy dohromady dávají1. To přesně vysvětluje podmíněný
přechod(54)->(55), bez tvrzení, že empirické1.47 je přesná
asymptotická konstanta. Samotné tvrzení o tau_n se zde
nepředpokládá dokázané.

Všechny čtyři typy identit úlohy28 a(D7) prošly pro n<=1024.
Logaritmické identity byly kontrolovány jako přesné racionální
koeficienty u ln p pro každé prvočíslo p, nikoli zaokrouhlenými
reálnými součty. Identita(D4) prošla pro všech512 jmenovatelů.

## 4. Průměr ve čtverci a úloha29

Pro 1<=m<n platí T(n,m)=T(m,n)-1, protože obrácené pořadí
přidává počáteční dělení s nulovým podílem. Na diagonále
T(n,n)=1. Přesný součet ve čtverci je tudíž

```
sum_(1<=m,n<=N)T(m,n)
 = sum_(n=1..N) [2 sum_(m=1..n-1)T(m,n)-(n-1)+1]
 = 2 sum_(n=1..N)n T_n - N(N+1)/2.                     (D9)
```

Ve druhé rovnosti používáme T(0,n)=1. Po vydělení N^2 dostáváme
právě opravené(57): 2/N^2 sum nT_n -1/2-1/(2N). Původní
prostý průměr T_n přes n odpovídá jinému rozdělení vstupů.
Přímé součty pro11 různých N do128, celkem30193 dvojic,
potvrdily(D9), včetně N=1.

Předpokládejme nyní(D8) s omezenou chybou. Elementární
integrální srovnání rostoucí funkce x ln x dává

```
sum_(n=1..N)n ln n
 = (N^2/2)ln N-N^2/4+O(N ln N).                         (D10)
```

Pro opravu s funkcí Lambda platí přesné přeskupení

```
sum_(n=1..N)n sum_(d|n)Lambda(d)/d
 = sum_(d=1..N)Lambda(d) sum_(k=1..floor(N/d))k.          (D11)
```

Pravá strana je O(N^2), protože 0<=Lambda(d)<=ln d a
sum_(d>=1)ln d/d^2 konverguje. Vložením(D10),(D11) do(D9)
dostaneme průměr a ln N+O(1), přesně požadované(58).
To uzavírá úlohu29 i opravenou odpověď z roku2000.

Lze doložit také přesnou limitní konstantu pod předpokladem
tau_n=a ln n+C+o(1), například pokud se později prokáže(60).
Pro každé pevné d má 2/N^2 sum_(k<=N/d)k limitu1/d^2;
pro všechna d,N je tento výraz nejvýše2/d^2. Dominovaná
konvergence v(D11) proto dává

```
(2/N^2) sum_(n<=N)n sum_(d|n)Lambda(d)/d
 -> A = sum_(d>=1)Lambda(d)/d^2 = -zeta'(2)/zeta(2).     (D12)
```

Funkce zeta(s)=sum_(n>=1)n^-s je zde používána jen pro s>1.
Poslední rovnost plyne i přímo z(D5): sečtením ln n/n^2
a přeskupením absolutně konvergentních řad dostaneme
-zeta'(2)=zeta(2) A. Není potřeba věta o rozložení prvočísel.

Průměr ve čtverci má za uvedeného předpokladu tvar

```
a ln N + D + o(1),
D = C-a/2-a A-1/2.                                    (D13)
```

Omezené chyby e_n->0 nepřispějí ke konstantě, protože po
vložení do(D9) jejich konečná počáteční část mizí a zbytek
je omezen libovolně malou konstantou. Dosadíme-li tištěný
vzorec(61) pro C a zeta(2)=pi^2/6, dostaneme

```
D = (6 ln2/pi^2)(3 ln2+4 gamma-12 zeta'(2)/pi^2-3)-1,   (D14)
```

kde gamma je Eulerova konstanta. To je přesný algebraický
vztah(62). Identifikace C jako konstanty v Porterově větě
zůstává samostatným úkolem; samotný číselný přepočet tohoto
vzorce takovou větu neprokazuje.

## 5. Tabulky, logaritmický součin a numerické konstanty

Přesné celočíselné počítání všech vstupů m=0,...,n-1
potvrdilo všech27 hodnot T_n na369 a všech27 hodnot tau_n
na370 po známé opravě98:55.6->5.6. Také tau_50=tau_100
a tau_60=tau_120. Pro n=100 je součet počtů kroků456,
tedy T_100=4.56 přesně. Heuristická hodnota4.59 na371 je
konzistentní s dosazením do(55).

Při kladných nesoudělných vstupech U=N,V=m<N označme
U_i,V_i dvojici před i-tým dělením a X_i=V_i/U_i. Potom
U_(i+1)=V_i a poslední kladný V_(t-1)=1. Proto

```
product_(i=0..t-1)X_i = 1/N,
sum_(i=0..t-1)ln X_i = -ln N.                          (D15)
```

To dokazuje(51). Přechod od tohoto přesného součinu k odhadu
průměrného t v textu zůstává výslovně heuristický. Integrál,
který v něm vystupuje, je však přesný:

```
(1/ln2) integral_0^1 ln x/(1+x) dx
 = -(1/ln2) sum_(k>=1)(-1)^(k-1)/k^2
 = -pi^2/(12 ln2).                                    (D16)
```

Záměna integrálu a řady je oprávněna součtem absolutních
integrálů sum 1/k^2. Rovnice(52) je integrál logaritmu vůči
hustotě F_n'; díky uniformnímu(53) a integrabilitě |ln x|
je jeho rozdíl od(D16) O(2^-n). Odhad(53) už byl dokázán
v euclid-gauss.md. To samo nepovoluje zaměnit náhodnou délku
konečného rozvoje za pevný počet nezávislých kroků.

Arb při100 pracovních desetinných místech dal mimo jiné

```
a = 0.8427659132721945169072631939639641...,
a ln10 = 1.9405402287840678514805120384200217...,
C = 1.4670780794339754728977984847072300...,
D = 0.0653514259230373213787826267631079... .
```

Všechny vytištěné zaokrouhlené číslice souhlasí. Derivace
zeta'(2) byla získána jako koeficient lineárního členu
intervalové mocninné řady zeta(2+x). JSON obsahuje intervalové
obaly; dvojí vzorec pro D byl ověřen také intervalově.
Věta(60), její zbytek, historické citace a rozptylový dodatek
na373 tím nejsou uzavřeny.

## 6. Reprodukce a průběh kontroly

Program verify_euclid_discrete.py používá přesné celé
a racionální hodnoty; python-flint0.9.0 je potřeba jen pro
číselné konstanty. Reprodukce:

```
python3 workstreams/vol2/verify_euclid_discrete.py --resume
```

Bez --resume program znovu provede všechny čtyři bloky.
Výsledky jsou v results/euclid-discrete.json.

První běh session9934/PID1201990 skončil exit1 až po úspěšné
kontrole obou tabulek a dvou rovností tau. V ručně přepsaném
zlomku18/29 chyběla jedna jednička; původní kniha má správně
pět jedniček před poslední trojkou. Chyba se netýkala knihy.
Hotová kontrola tabulek byla zachována jako metadata, její
jednotlivé přesné součty se před selháním neuložily. Program
je při čerstvém běhu znovu vypíše do JSON. Neopakovali jsme
ji pouze kvůli formátu výstupu.

Po opravě doslovného přepisu pokračoval session11174/PID1202774
s --resume: tabulky přeskočeny, tabulka29,65536 obrácení,
512 konvolucí,30193 dvojic a1024 aritmetických vstupů plus
všechny intervalové konstanty prošly; exit0. Matematické
závěry stojí na obecných důkazech výše, nikoli na rozsahu
těchto konečných kontrol.

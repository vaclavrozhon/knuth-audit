# Batcher16: přesné sumy, analytická konstanta, perioda a úplný průměr

7. listopadu2026. Zadání135/file146 a odpověď630/file641 zobrazeny,
detail vzorce `images/batcher-mean-formula-1.png`. P1012 dokazuje
váhu každé hrany; neopakujeme jej. Primární zdroj Sedgewick,
*Data Movement in Odd-Even Merging*, SICOMP7(1978),239–272,
je uložen v `sources/sedgewick-1978-batcher.pdf`; jeho266 zobrazená
v `images/batcher-sedgewick-mean-28.png`. Následující odvození
výslovně doplňuje vlastní zbytky a normalizaci.

Vnější analytické identity: NIST DLMF25.11.13 a25.11.18
pro ζ(0,a),ζ′(0,a), a>0;5.4.3 pro |Γ(it)|;5.11.9 pro
vertikální Stirlingův odhad. Byly přečteny v primárním zdroji:
https://dlmf.nist.gov/25.11 , https://dlmf.nist.gov/5.4 ,
https://dlmf.nist.gov/5.11 . Používáme je pouze pro a=1/4,1
a pevný vertikální pás, tedy uvnitř uvedených předpokladů.
Mellinovu inverzi níže zdůvodníme Fourierovou inverzí.

## P1020: pravděpodobnostní model a normalizace

Pro náhodnou permutaci2n různých klíčů dostane každá n-prvková
množina lichých pozic právě(n!)² stejně pravděpodobných vstupů.
Po seřazení obou podposloupností tedy každá z binom(2n,n)
mřížových cest nastává stejně často. Označ B_n střední počet
výměn posledního slučování, S_n=binom(2n,n)B_n jejich součet
přes všechny cesty. Nesměšujeme tento součet s průměrem nebo
s celým rekurzivním tříděním.

## P1021: všechny meze a faktory první dvojité sumy

Svislou hranou(i,j)→(i+1,j) prochází

    binom(i+j,i) binom(2n−i−j−1,n−i−1)

cest: prefix a suffix volíme nezávisle. Záporná výška i−j<0
se při otočení celé cesty a obrácení směru spáruje se svislou
hranou(n−i−1,n−j)→(n−i,n−j), jejíž výška je j−i−1≥0.
Oba počty cest jsou stejné, váhy jsou1+f(j−i−1) a f(j−i−1).
Jde o bijekci všech záporných a všech nezáporných hran, včetně
dvojice hladin−1 a0. Po přeznačení nezáporné hrany na(i,i−j)
tedy přesně

    S_n=Σ_(0≤j≤i<n)(2f(j)+1)
          binom(2i−j,i−j) binom(2n−2i+j−1,n−i−1).

To dokazuje celou první sumu odpovědi, nejen její hlavní člen.

## P1022: obecná f-identita, všechny konečné součty

Označ K_(n,j) vnitřní sumu obou binomických faktorů pro i=j,…,n−1.
Dokážeme K_(n,j)=Σ_(k=j+1)^n binom(2n,n−k). Polož
D=1−4z a C(z)=(1−√D)/(2z), tedy C=1+zC².

Pro A_j(z)=Σ_(r≥0)binom(2r+j,r)z^r platí
A_0=1/√D a A_1=(A_0−1)/(2z)=C/√D. Pascalova identita
dává A_j=A_(j−1)+zA_(j+1), takže indukcí A_j=C^j/√D.
Toto je vlastní důkaz potřebné generující funkce.

Substituce i=j+r a v=n−j−r−1 dává

    Σ_(n≥j+1)K_(n,j)z^n=z^(j+1)A_j A_(j+1)
                              =z^(j+1)C^(2j+1)/D.

Generující funkce pravé strany je

    Σ_(k≥j+1)z^k A_(2k)
      =(zC²)^(j+1)/(√D(1−zC²))
      =z^(j+1)C^(2j+1)/D,

protože1−zC²=2−C=C√D. Rovnost koeficientů dokazuje identitu.
Všechny manipulace jsou formální řady s konečným počtem
příspěvků ke každému koeficientu.

Nechť F(k)=Σ_(0≤j<k)f(j). Záměnou konečných sum vyjde
S_n=Σ_(k≥1)binom(2n,n−k)(2F(k)+k). Dále

    k binom(2n,n−k)
      =n[binom(2n−1,n−k)−binom(2n−1,n−k−1)].

Teleskopování dává sumu(n/2)binom(2n,n). Proto

    B_n=n/2+2/binom(2n,n) Σ_(k≥1)binom(2n,n−k)F(k).   (1)

To je úplná uváděná transformace pro obecné f, s konečnou
podporou binomických koeficientů.

## P1023: přesná transformace na diference f a znak liché části

Piš g(k)=f(k)−f(k−1), k≥1. P1013 ukázal |g(k)|=1.
Přesněji, při k=2^r u,u liché, se změní r-tý Grayův bit
z0 na1 při u≡1(mod4), z1 na0 při u≡3(mod4). Proto
g(k)=χ_4(u), kde χ_4(1)=1,χ_4(3)=−1.

Definuj H_j(k)=binom(2j,j−k), c_j=H_j(0)/4^j,

    b_j=Σ_(k≥1)H_j(k)g(k)/H_j(0),
    T_n=Σ_(k≥1)H_n(k)F(k).

Dvojitá Pascalova identita je
H_n(k)=H_(n−1)(k−1)+2H_(n−1)(k)+H_(n−1)(k+1).
Přesun indexů v T dává

    T_n−4T_(n−1)=Σ_(k≥1)H_(n−1)(k)g(k),

protože F(k+1)−2F(k)+F(k−1)=g(k), F(0)=F(1)=0.
Žádný hraniční člen tedy nezůstává. S T_1=0 se rekurence
rozvine na přesnou rovnost

    B_n=n/2+(1/(2c_n))Σ_(1≤j<n)c_j b_j.               (2)

## P1024: absolutní Gaussian chyba O(j^(−1/2))

Pro1≤k≤j je H_j(k)/H_j(0)=∏_(i=1)^k(j−i+1)/(j+i).
Rozvoj logaritmů pro k≤j/2 dává

    log(H_j(k)/H_j(0))=−k²/j+u_(j,k),
    |u_(j,k)|≤C(k²/j²+k⁴/j³),
    u_(j,k)≤−½ln(1−k²/j²)≤Ck²/j².

První člen je součet−(2i−1)/j. Všechny kladné sudé členy
teleskopují na Σ_(r≥1)k^(2r)/(2r j^(2r)); záporné liché
členy řádu≥3 jsou absolutně O(k⁴/j³). To zdůvodňuje obě
nerovnosti jednotně, ne pouze pro pevné k.

Odtud

    |H_j(k)/H_j(0)−exp(−k²/j)|
        ≤C exp(−k²/j)(k²/j²+k⁴/j³).

Součet obou Gaussian momentů je O(j^(−1/2)), protože
Σk²exp(−k²/j)=O(j^(3/2)) a Σk⁴exp(−k²/j)=O(j^(5/2));
například rozdělení do intervalů délky√j tyto meze přímo
dokazuje konvergentními Gaussian řadami. Pro k>j/2 monotónní
binomický poměr i Gaussian ocas mají exponenciální součet,
včetně k>j, kde je binomický člen0. Konečně mnoho malých j
se zahrne do konstanty. Proto

    b_j=Σ_(k≥1)g(k)exp(−k²/j)+O(j^(−1/2)).             (3)

Chyba je absolutní a byla sečtena před využitím znamének g.
Nevytýkáme relativní O před oscilující sumu, což by bez dalšího
argumentu nebylo oprávněné.

## P1025: celá Dirichletova řada a aplikovatelnost vnějších hodnot

Pro Re s>1 dovoluje absolutní konvergence rozklad k=2^r u:

    Q(s)=Σ_(k≥1)g(k)/k^s=β(s)/(1−2^(−s)),
    β(s)=Σ_(l≥0)(−1)^l/(2l+1)^s
        =2·4^(−s)ζ(s,1/4)−(1−2^(−s))ζ(s),
    Q(s)=2ζ(s,1/4)/(2^s(2^s−1))−ζ(s).                (4)

Poslední vztah plyne oddělením tříd1 a3 modulo4. Póly obou
Hurwitzových zeta funkcí v s=1 se v β ruší; Q tam nemá pól.
Použité hodnoty z DLMF mají splněný předpoklad a>0:

    ζ(0,1/4)=1/4, ζ(0)=−1/2,
    ζ′(0,1/4)=lnΓ(1/4)−½ln(2π), ζ′(0)=−½ln(2π).

Tyto klasické identity jsou výslovnou vnější závislostí,
nikoli vydávaným novým důkazem obecné Lerchovy formule.

## P1026: Mellinova inverze, přesun kontury a celá chyba

Pro c>0 je Γ(c+it) Fourierovou transformací hladké integrabilní
funkce e^(cu−e^u). Fourierova inverze po substituci x=e^u
dává e^(−x)=(1/(2πi))∫_(c−i∞)^(c+i∞)Γ(z)x^(−z)dz.
Pro c=1 můžeme zaměnit tento integrál se sumou v(3):
Σk^(−2)<∞ a vertikální Γ je absolutně integrabilní. Tedy

    S(x):=Σ_(k≥1)g(k)e^(−k²/x)
       =(1/(2πi))∫_(1−i∞)^(1+i∞)Γ(z)Q(2z)x^z dz.    (5)

Přesuneme konturu na Re z=−1/2. Eulerova–Maclaurinova formule
pro ζ(s,a), ukončená přes B4, má integrální zbytek s čtvrtou
derivací. Pro−1≤Re s≤2, |Im s|≥1 a konec sumy K≈|Im s|+1
proto dává jednotnou polynomiální mez v |Im s|; integrál
absolutně konverguje, protože Re s+4≥3. Γ má podle DLMF5.11.9
v tomto pevném pásu exponenciální pokles e^(−π|Im z|/2).

Horní/dolní hrany volíme v polovinách mezi výškami pólů
t_k=πk/ln2. Tam je4^(i Im z)=−1 a jmenovatel4^z−1 je
jednotně vzdálen nule po celé šířce kontury. Tyto hrany
tedy v limitě zmizí. Na levé hraně je jmenovatel také
vzdálen nule a celý integrál je O(x^(−1/2)). Pól z=1/2
se podle(4) ruší; zbývá dvojitý pól0 a jednoduché póly
z=it_k,k≠0. Žádný záporný celočíselný pól Γ jsme nepřekročili.

Tím jsou doloženy přesun, úplný seznam reziduí i absolutní
zbytek potřebný v(3), nikoli pouze formální reziduový výpočet.

## P1027: Laurentova konstanta a celý periodický člen

Piš A=lg(Γ(1/4)²/(2π)). Z(4) a P1025 je

    Q(2z)=1/(4z ln2)+A−1/4+O(z).

Například e^(−z ln4)/(e^(z ln4)−1)=1/(z ln4)−3/2+O(z);
vynásobení2ζ(2z,1/4) a odečtení ζ(2z) dává právě−1/4.
Γ(z)=1/z−γ+O(z) plyne z Γ(1+z)=1−γz+O(z²), stejné
hodnoty derivace použité již v P0924/P0978. S x^z=1+z ln x+O(z²)
je reziduum v0

    ¼lg x + A−1/4−γ/(4ln2).

Pro k≥1 definuj

    t_k=πk/ln2,
    a_k=(2/ln2)Γ(it_k)ζ(2it_k,1/4),
    ε(x)=Σ_(k≥1)Re(a_k x^(it_k)).

To jsou přesně spárovaná rezidua nenulových pólů. Díky
polynomiální mezi ζ a exponenciální Γ tato řada i její
derivace podle ln x konvergují absolutně. Proto ε je omezená,
|ε′(x)|≤C/x a ε(4x)=ε(x). Z(3)–(5) dostáváme

    b_j=¼lg j + A−1/4−γ/(4ln2)+ε(j)+O(j^(−1/2)).      (6)

Znaménko před γ je určeno členem−γ v Laurentově rozvoji Γ.

## P1028: každá transformace zpět na průměr B_n

Z rekurence c_j=binom(2j,j)/4^j je
2(j+1)c_(j+1)−2jc_j=c_j, takže přesně
Σ_(j=0)^(n−1)c_j=2nc_n. Zároveň Stirling dává
c_j=(πj)^(−1/2)+O(j^(−3/2)) a1/c_n=√(πn)+O(n^(−1/2)).

Konstantní člen C_0=A−1/4−γ/(4ln2) v(6) přispěje do(2)
C_0 n+O(√n), protože suma začíná j=1. Logaritmický člen
přispěje

    (√n/(8ln2)) Σ_(1≤j<n) j^(−1/2)ln j +O(√n)
      =¼n lg n−n/(2ln2)+O(√n log n).

Zde integrál od0 do n je2√n ln n−4√n. Rozdíl sumy a
integrálu je O(log n), například rozdělením v pevném bodě
monotónnosti x^(−1/2)ln x; singularita u0 je integrabilní.
Chyba O(j^(−1/2)) v(6) po váze c_j a vnějším√n přispěje
O(√n Σ_(j<n)1/j)=O(√n log n).

U ε jsou chyby Stirlinga O(√n). Funkce x^(−1/2)ε(x) má
pro x≥1 absolutně integrabilní derivaci O(x^(−3/2)), takže
sumu lze nahradit integrálem0…n s chybou O(1). Absolutní
konvergence Fourierovy řady dovoluje integraci po členech:

    ½√n ∫_0^n x^(−1/2)ε(x)dx = n δ(n),
    δ(n)=Σ_(k≥1)Re(a_k n^(it_k)/(1+2it_k)).             (7)

Tedy δ(4n)=δ(n). Připojením počátečního n/2 z(2) dostáváme

    B_n=¼n lg n + (A+1/4−(γ+2)/(4ln2)+δ(n))n
                       +O(√n log n).                 (8)

Každý konstantní příspěvek je uveden samostatně: n/2,
−n/4,−γn/(4ln2),−n/(2ln2). Originál630 má před(γ+2)
plus; toto znaménko je chybné, viz C0029. Vedoucí člen je
správný. Rovnice(8) souhlasí s primárním Sedgewickovým
Theorem3 na266, jehož sazba má mínus.

## P1029: rigorózní mez |δ|<.0005 bez dlouhého výpočtu

Nejprve čistě analytický ocas. Eulerova formule pro ζ(s,1/4)
s K=1, členem B2 a integrálním zbytkem dává pro s=iu,u≥8.8

    |ζ(iu,1/4)|≤3/2+(5/4)/√(1+u²)+u/15+u√(u²+1)/15
                 ≤3+(u²+u)/15.

Použili jsme sup|B2({x})|=1/6 a integrál(5/4)^(−1).
Pro u=2t,t≥4.4 je poslední mez≤t²/2. Identita DLMF5.4.3
dále dává

    |Γ(it)|=√(π/(t sinh πt)) <3t^(−1/2)e^(−πt/2).

Z .69<ln2<.70 a3.14<π<22/7 plyne4.48k<t_k<4.56k a
πt_k/2>7k. Proto každá amplituda v(7) je menší než

    |a_k|/√(1+4t_k²)<4.65√k·10^(−3k).

Pro k≥2 použijeme√k≤k; celý nekonečný ocas je pak menší
než4.65(r/(1−r)²−r)<.0000094, r=.001.

Pouze první amplituda vyžaduje přesnější cílené vyčíslení.
`results/batcher-mean-periodic-bound.py` používá intervalovou
aritmetiku45 číslic,64 konečných členů Hurwitzovy sumy a
Eulerovu formuli přes B4. Pro A=64+1/4,s=2it_1 má zbytek
explicitní mez

    |s(s+1)(s+2)(s+3)|/(2160 A³),

protože sup|B4({x})|=1/30 a integrál x^(−4) je A^(−3)/3.
Modul Γ je vyčíslen přes přesnou výše uvedenou identitu,
nikoli numerickou analytickou kontinuací. Výstup
`results/batcher-mean-periodic-bound.json` dokládá

    první amplituda <.000490085,
    ocas             <.000009314,
    celkem           <.000499399 <.0005.

Proběhl jediný úspěšný krátký běh s nice15; před ním byla
opravena nepodporovaná funkce sinh intervalového API na její
identitu pomocí exp. Nejde o enumeraci ani opakování úspěšné
kontroly. Hranice .0005 v knize je tedy samostatně potvrzena.

## P1030: asymptotický průměr celého třídění a správný podíl1/4

Pro N=2^t označ E_N střední počet výměn celého M. Podmíněně
na množinách klíčů jsou relativní permutace obou polovin
rovnoměrné; rovnoměrnost cest posledního slučování je P1020.
Linearita očekávání proto dává E_N=2E_(N/2)+B_(N/2),E_1=0.
Po rozvinutí, s C=A+1/4−(γ+2)/(4ln2), máme z(8)

    E_N/N =t(t−1)/16 +Ct/2 +½Σ_(r=0)^(t−1)δ(2^r)+O(1).

Chyba je O(1), protože Σ_(r≥0)(r+1)2^(−r/2)<∞; pro
malé r lze asymptotickou mez zvětšit pevnou konstantou.
Perioda δ(4x)=δ(x) tedy dává také přesnější tvar

    E_N=N[t²/16+t(C/2−1/16+(δ(1)+δ(2))/4)+O(1)].      (9)

Zvláště E_N∼N(lg N)²/16. P1004 má c(N)∼N(lg N)²/4,
tedy E_N/c(N)→1/4. Stejný podíl platí pro poslední slučování,
jehož počet porovnání je n lg n+O(n). Chybná lineární
konstanta(8) tento vedoucí podíl ani algoritmus nevyvrací.

## P1031: konkrétní rozpor chybného znaménka, nikoli jen rozdíl pramenů

Opravený a tištěný lineární koeficient se liší o
Δ=(γ+2)/(2ln2)>1. Oba periodické členy mají podle tvrzení
knihy a právě doloženého P1029 absolutní hodnotu<.0005,
takže jejich případný rozdíl může mít velikost nejvýše.001.
Po odečtení obou asymptotik a vydělení n by muselo platit
Δ+δ_book(n)−δ(n)=O(log n/√n)→0. Levá strana má ale
absolutní hodnotu>0.999 pro všechna n. To je spor i podél
n=2^r, tedy přesně v omezení zadání. Nelze jej absorbovat
do periodické funkce ani do uvedeného zbytku.

Originál, obecný důkaz a pět vrstev errat jsou spojeny
v `notes/V3-C0029-batcher-mean-sign.md`. Správná oprava je
jediné znaménko před(γ+2)/(4ln2); ostatní části16 jsou
samostatně doložené výše.

# §3.4.2-18: prohazování s celým polem

Kontrola 1. listopadu 2026. Nové zadání a odpověď jsou v all2-prepre,
souborové strany8 a33; obě byly vizuálně přečteny a porovnány se všemi
pozdějšími vrstvami errat. Všechny tři třídy grafů a jejich počty souhlasí.
Obecné tvrzení o nejméně pravděpodobném výsledku bylo ověřeno v původním
důkazu Robbins–Bolker; hranice18 v Goldstein–Moews včetně reprodukce
její konečné výpočetní části. Bez nového nálezu.

## Graf a konvence

Počáteční pole je (1,...,n). Krok j prohodí pozice j a a_j, kde každé
a_j je nezávisle rovnoměrné v {1,...,n}. Každá z n^n historií má tedy
stejnou pravděpodobnost. **Násobnost** výsledku je počet jeho historií.
Graf historie má orientovanou hranu j→a_j z každého vrcholu. Každá
souvislá komponenta má jediný orientovaný kruh; dovolujeme i smyčku.
Pozicová permutace pi posílá původní číslo karty na její novou pozici;
je tedy inverzí vypsaného výsledného pole. Funkce skládáme zprava doleva:

```text
pi = (n,a_n) ... (2,a_2) (1,a_1).
```

Komponenta s jedinou smyčkou je strom orientovaný ke kořeni a vytváří
jeden permutační cyklus. Komponenta s kruhem délky alespoň2 vytváří dva
permu­tační cykly. Důkaz: součin transpozic odpovídajících hranám stromu
je jeden cyklus, což plyne odstraněním listu a cyklickým přesunem faktorů
(konjugací). Odebrání jedné hrany kruhu dá strom; vrácení této transpozice
rozdělí jeho jediný cyklus na dva. To také řeší dvojici opačných hran,
které odpovídají dvěma výskytům stejné transpozice.

## (a) Posun doprava: přesná rekurzivní třída

Výsledné pole (n,1,...,n−1) znamená pi=(1,2,...,n). Jeho graf musí být
jediným zakořeněným stromem. Následující pravidlo přesně popisuje obrázek
v odpovědi; lze je používat i na libovolném intervalu [l,r].

Položme k=a_r. Jestliže k=r, všechny vrcholy intervalu míří do r.
Jestliže l<=k<r, všechny vrcholy l,...,k−1 míří do r, hrana r míří do k,
a na intervalu [k,r−1] se pravidlo opakuje. Jiné grafy přípustné nejsou.

Pro důkaz nejprve pozorujme: strom s kořenem v největším vrcholu r,
který vytváří posun doprava, musí být hvězda. Karta r má skončit v l;
na jediné stromové cestě do l by poslední hrana měla čas l. Časy hran
musí podél cesty přísně růst, proto tato cesta obsahuje jedinou hranu
l→r. Karta l se tak dostane do r a musí následně do l+1; stejný argument
vynutí l+1→r, a postupně všechny ostatní hrany.

Je-li a_r=k<r, odstraníme poslední transpozici. Z původního cyklu vzniknou
dva cykly na množinách {l,...,k−1,r} a {k,...,r−1}. Odebrání hrany r→k
rovněž rozdělí strom na dvě komponenty; první má kořen r a podle
předchozího odstavce je hvězdou. Druhá je stejnou úlohou na menším
intervalu. Obrácení těchto kroků dokazuje postačitelnost pravidla.

Je-li F_m počet takových stromů na m vrcholech, dostáváme
F_1=1 a F_m=1+sum_{j=1}^{m−1} F_j, tedy **F_m=2^(m−1)**. Pro pevný
kořen r je počet C(n−1,r−1), kde C je binomický koeficient. Ekvivalentně
lze prokládat řady1,...,r−1 a n,...,r+1, nakonec připojit r; rodičem
každého vrcholu je první pozdější vrchol z opačné řady, případně r.
To je význam „slévání“ dvou řad v tištěné odpovědi.

## (b) Identita

Každá grafová komponenta musí vytvářet pouze pevné body. Z úvodního
cyklového pravidla plyne, že může jít jen o jediný vrchol se smyčkou
nebo o dvojici protisměrných hran. To jsou přesně **involuce**: permutace
a splňující a(a(j))=j. Označíme-li jejich počet Q_n, rozhodnutí, zda je
vrchol1 samostatný nebo spárovaný s jedním z n−1 dalších, dává

```text
Q_0=Q_1=1,   Q_n=Q_(n−1)+(n−1)*Q_(n−2).
```

Také Q_n>=sqrt(n!). Pro n>=2 lze indukcí ukázat
`sqrt(n)<Q_n/Q_(n−1)<sqrt(n)+1`. Položíme-li x=sqrt(n−1), dolní
indukční mez je `1+x^2/(x+1)=x+1/(x+1)>sqrt(n)`; horní je
`1+x<1+sqrt(n)`. Počáteční n=2 je přímé. Součin dolních mezí dokazuje
požadované tvrzení (pro0,1 rovnost). Odmocnina v horní mezi nezahrnuje +1;
toto bylo ověřeno v sazbě primárního článku.

## (c) Posun doleva a binární vyhledávací stromy

**Binární vyhledávací strom** zde znamená zakořeněný strom, v němž má
vrchol nejvýše jedno levé a jedno pravé dítě; všechna čísla v levém
podstromu jsou menší a v pravém větší než kořen. Položíme a_j rovno
rodiči j a v kořeni a_j=j. Takový graf vytváří pole (2,...,n,1).

Užitečná silnější indukce: má-li strom na intervalu [l,r] vnějšího rodiče
p mimo interval a nahradíme jeho kořenovou smyčku hranou do p, součin
je klesající cyklus na [l,r]∪{p}. Pro kořen b jsou součiny levého a
pravého podstromu cykly `(b,b−1,...,l)` a `(r,...,b+1,b)`; mezi nimi
je transpozice(b,p). Jejich složení dává tvrzený cyklus. Při původní
kořenové smyčce vznikne `(r,...,l)`, což je pozicová permutace posunu
doleva. Prázdný podstrom přispívá identitou.

Počet těchto stromů C_n splňuje C_0=1,
`C_n=sum_{b=1}^n C_(b−1)*C_(n−b)`, tedy Catalanovo číslo
`C_n=binomial(2n,n)/(n+1)`. Žádné další grafy pro tento výsledek nejsou:
Robbins–Bolker, věty3–4 a8 (str.273–277), dávají celkový počet C_n.
Jejich argument byl přečten celý. Po vynechané první transpozici počty
W_n splňují W_1=W_2=1 a `W_n=sum_{j=1}^{n−1} W_j W_(n−j)`, proto
W_n=C_(n−1). Rozklad podle první transpozice pak dává pro celkový počet
V_n rekurenci `V_n=sum_{j=1}^n C_(j−1) V_(n−j)`, V_0=1. Její jediné
řešení je C_n. Spolu s předchozí konstrukcí tím dostáváme i nutnost
binární vyhledávací struktury.

## Nejmenší a největší násobnost

Minimálnost případu(a) není odvozena jen ze tří porovnávaných příkladů.
Robbins–Bolker, věta2 na272, dává indukci pro libovolnou permutaci:
vybere sestup i→j s j<i, odstraní buď i nebo j a obě menší reprezentace
rozšíří vloženou transpozicí(i,j). Nutné konjugace mění pouze druhé
souřadnice pozdějších, respektive dřívějších transpozic. V jedné rodině
a_j!=i, ve druhé a_j=i, takže rodiny jsou disjunktní. Indukce zdvojnásobí
2^(n−2). Pro identitu postačuje rekurence Q_n>=2^(n−1), od n>=3 ihned
z indukčního předpokladu; n=1,2 přímo. Důkaz a jeho konvence skládání
byly přečteny v originálu; primární článek skládá zleva doprava.

Pro maximum používáme strukturální důsledek15 Goldstein–Moews. Při
pevných délkách cyklů L_1,...,L_q dosáhnou maxima oddělené klesající
cykly na souvislých intervalech. Označme G_(m,p) maximální počet
reprezentací dvou cyklů délek m,p jedinou komponentou. Článek dává

```text
G_(m,p) = [C(2m,m)*C(2p,p)*(m+p+4mp)
           −(m+p)*C(2m+2p,m+p)] / [2(m+p)(m+p+1)].
```

Maximální násobnost pro dané délky je součet přes všechna rozdělení
cyklů na jednotlivce a dvojice; jednotlivec přispívá C_(L_i), dvojice
G_(L_i,L_j). **Je nutné zahrnout i dvě samostatné stromové komponenty:**
pro dva cykly je celkový počet C_m*C_p+G_(m,p), nikoli jen G_(m,p).

Přesná rekurence na multimnožině délek v našem programu prověřila všech
**18459 celočíselných rozkladů n pro1<=n<=28**. Pro4<=n<=17 vyhrávají
dva cykly co nejbližších délek; pro18<=n<=28 vyhrává identita. Výjimky
n=1,2,3 přesně souhlasí s větou16. Pro n>=29 jsme zkontrolovali obecný
argument článku: stromové a násobnosti komponent s kruhem délky alespoň 2 jsou nejvýše
4^(m−1), respektive4^(m−2), tudíž celková násobnost permutace s q cykly
je nejvýše Q_q*4^(n−q). Poměry Q_q/4^q mají od q=15 rostoucí chování
a hodnota pro29 převyšuje všechna dřívější maxima. Všechny konečné
počáteční nerovnosti a rekurzivní meze komponent s kruhem délky alespoň 2 do velikosti 21
byly přesně reprodukovány. Velký ocas plyne z Catalanovy řady
`sum C_j/4^j=2` a nerovnosti `(n−1)C_(n−1)<=2*4^(n−3)` pro n>=22;
ta platí přímo v22 a poměr levé strany k4^(n−3) dále klesá.

Tím je práh **n>=18** doložen. Reprodukce konečné části není vydávána
za nezávislý nový důkaz strukturálních lemmat původního článku.

## Nezávislé výpočty a prameny

[C++ soupis](../verify_exchange_shuffle.cpp) prošel všech17 650 828
historií pro1<=n<=8. Pro každou historii porovnal všechny tři grafové
predikáty se skutečně prohozeným polem, v obou směrech. Násobnosti(a),(b),(c)
pro n=8 jsou128,764,1430; globální maximum1931. Pro n=6 minimum32 a
maximum159 reprodukují také původní tabulkový údaj článku1981.

[Nezávislá validace](../verify_exchange_shuffle.py) skládá rozdělení
permutací po jednotlivých krocích, aniž by znovu procházela n^n historií.
Potvrdila počty všech permutací, extrémy, jejich násobnosti i všechny
tři zvláštní výsledky do n=8. Další blok počítá výše popsané rozklady
cyklů do28. Oba běhy66321/46508 skončily0.

Primární Robbins–Bolker, Aequationes Mathematicae22(1981),268–292,
[scan GDZ](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356261603_0022/LOG_0037.pdf),
byl vizuálně přečten na268–279. Jde o DOI10.1007/BF02190184; stejně
nazvané krátké sdělení na114–115 má jiný DOI a nebylo zaměněno za tento
článek. Původní PDF a manifest v sources zachovávají knihovní metadata.

[Goldstein–Moews](https://arxiv.org/pdf/math/0010066) je arXiv preprint,
nikoli časopisecká sazba2003. Přečteny §2–3, §4 do strany9 a §6
(strany14–18); strany4 a18 také vizuálně. Příslušné grafové definice,
rozklad na komponenty, strukturální meze a výpočetní redukce souhlasí
s použitím výše. Důkazy nesouvisejících limitních zákonů v§7 tento audit
neověřuje.

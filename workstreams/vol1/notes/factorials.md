# §1.2.5: permutace, faktoriály a diskrétní důkazy

Kontrola 1. listopadu 2026, třetí vydání, první dotisk 1997.
Zobrazeny s. 45–52 a odpovědi 480–483. Soupis má 25 úloh;
v prověřených vrstvách errat nejsou další přidané úlohy této sekce.
Analytická část je v [gamma-functions.md](gamma-functions.md),
úloha 21 v [composite-derivatives.md](composite-derivatives.md).

## Počítání a generování permutací

Permutace je uspořádání všech n různých objektů. Injekční posloupnost
délky k vybírá k různých objektů z n, včetně jejich pořadí. Pro
celá 0<=k<=n má postupně n,n−1,...,n−k+1 možností, tedy
`p_(n,k)=n(n−1)...(n−k+1)`. Pro k=0 je jedna prázdná posloupnost.
Pro k>n je počet 0, což rovněž dává součin obsahující nulový faktor.

Metoda 1 má jednoznačnou inverzi: odstraň největší prvek n a zapamatuj
si jeho pozici. Metoda 2: odstraň poslední prvek k a od všech zbývajících
hodnot větších než k odečti 1. Inverzní operace vrátí právě původní
permutaci a parametr, takže obě konstrukce jsou bijekce. Totéž platí
při libovolné pevné pozici pro k, jak říká text. Ukázky z permutace
231 na s. 46 souhlasí s oběma konstrukcemi.

Faktoriál `n!=product_{j=1}^n j` proto počítá permutace; 0!=1
a n!=n(n−1)! pro n>=1. Číselné hodnoty 0! až 5! a 10!=3628800
jsou správné. Při jedné milisekundě na případ je 10! případů
přesně 3628.8 sekund, tj. 1 hodina a 28.8 sekundy. Úvaha o praktičnosti
je v knize výslovně neurčitá, nikoli obecná mez současných počítačů.

## Úlohy 1–7 a číselné údaje

1. Každá karta je odlišná, proto 52! možností. Celý desetinný řetězec
odpovědi je porovnáván s přesným celočíselným součinem, nikoli jen
s jeho počátečními číslicemi.

2. `p_(n,k)=p_(n,k−1)(n−k+1)` pro 1<=k<=n. Při k=n je poslední
faktor 1: zařazení n−1 objektů jednoznačně určuje poslední objekt.
Zde n>=1; p_(0,−1) by nepatřilo do právě zavedené definice.

3. Vložení 5 do 3124 dává 53124,35124,31524,31254,31245.
Připojení přejmenovaného k dává 42351,41352,41253,31254,31245.

4. Pro kladné celé N je počet desetinných číslic `floor(log10 N)+1`.
Z uvedeného logaritmu tedy plyne 2568. Jeho zlomková část leží
mezi log10(4) a log10(5), proto první číslice je 4. Poslední je 0;
počet koncových nul je minimum násobností 2 a 5. Níže uvedený
vzorec dává násobnost 5 rovnou 200+40+8+1=249, násobnost 2 je vyšší.
Počáteční řetězec 4023872600770 souhlasí s přesným součinem.
Přesná kontrola logaritmu je samostatnou součástí číselného certifikátu.
Historické tvrzení o Uhlerově celé tabulce vyžaduje i získání tabulky;
výpočet samotného 1000! je nenahrazuje.

5. Násobení původního odhadu 39902 číslem 97/96 dává přibližně
40317.65, tedy po zaokrouhlení 40318. Výpočet z nezaokrouhlených
konstant dává stejný celočíselný odhad. Obecný základ přiblížení
je dokázán v analytické poznámce.

6. Rozklad 20! je `2^18 3^8 5^4 7^2 11 13 17 19`.
7. Polynom `T(x)=x(x+1)/2`, zvaný zde termial, splňuje
T(x)−T(x−1)=x pro všechna reálná i komplexní x; T(1/2)=3/8.

## Násobnosti prvočísel a úlohy 11–14

Pro prvočíslo p označme v_p(N) počet výskytů p v prvočíselném
rozkladu kladného celého N. Každé j v 1,...,n přispívá jednou za
každé p^r, které je dělí. Po výměně konečných součtů dostaneme

```text
v_p(n!) = sum_{r>=1} floor(n/p^r).                     (1)
```

Nuly po p^r>n dovolují zápis nekonečným součtem. Vnořené podlahy
umožňují postupné celočíselné dělení. Příklad n=1000,p=3 dává
333+111+37+12+4+1=498, včetně tvrzení o nedělitelnosti 3^499.

11–12. Je-li `n=sum_{j=0}^k a_j p^j`, 0<=a_j<p, pak

```text
sum_{r>=1} floor(n/p^r)
 = sum_{j>=1} a_j(1+p+...+p^(j−1))
 = (n−sum_j a_j)/(p−1).                               (2)
```

V binárním zápisu je součet číslic počet jedniček r; násobnost je
n−r. Vzorec platí také pro n=0 s prázdným součtem a 0!=1.

13. Pro každý nenulový zbytek a modulo p existuje jediné inverzní
a'. Existence plyne z Bézoutovy identity, jednoznačnost z krácení
zákonem 1.2.4B. Odkaz na D v prvním dotisku je známá chyba,
opravená 8. listopadu 2005. Inverze je involuce. Její pevné body
řeší a²=1, tedy jsou 1 a −1. Pro liché p jsou různé; všechny
ostatní prvky se párují do součinu 1, takže (p−1)!≡−1 (mod p).
Pro p=2 je jen jeden pevný bod, 1=−1, a výsledek platí přímo.
Tato drobná oddělená větev doplňuje zkrácený knižní důkaz.

14. Zapišme n=pq+a_0. Součin činitelů 1,...,n nedělitelných p
je modulo p roven `(−1)^q a_0!`, podle předchozího párování
v každém úplném bloku délky p. Po odstranění jednoho p z každého
násobku p zbývá q!. Označíme-li `U(n)=n!/p^v_p(n!)`, máme
`U(n)≡(−1)^q a_0! U(q)`. Opakováním přes číslice vznikne
`U(n)≡(−1)^mu product_j a_j!`, kde mu je (1).
Pro p=2 je (−1)^mu≡1; důkaz pokrývá i tento případ.

## Úloha 15: permanent

Permanent matice A velikosti n je součet `product_i A_(i,pi(i))`
přes všechny permutace pi, bez znamének determinantového rozvoje.
Šest členů pro matici 3×3 v zadání přesně odpovídá šesti permutacím.
V požadované matici je **A_(i,j)=i*j**; Markdown ji nesprávně změnil
na mocniny. Každý člen je `product_i i * product_i pi(i)=(n!)²`
a členů je n!, proto permanent je (n!)³. Konvence prázdné matice
dává rovněž 1, pokud se rozsah rozšíří na n=0.

## Rovnice (11), (12) a úloha 16

Položme `d_k=sum_{j=0}^k (−1)^j/j!`. Pro celé n>=0 platí

```text
sum_{k=0}^n d_k n!/(n−k)!
 = n! sum_{k=0}^n sum_{j=0}^k (−1)^j/[j!(n−k)!]
 = n!.
```

Poslední rovnost je součet koeficientů stupně 0 až n v součinu
exp(t)exp(−t)=1: po položení r=n−k je j+r<=n. Alternativně jde
o roztřídění permutací podle počtu pevných bodů a inkluzi a exkluzi
pro derangementy. Pro necelé komplexní z žádný faktor v padajícím
součinu nezmizí a absolutní poměr jeho sousedních členů je |z−k|,
který je nakonec >2. Součin tedy roste bez omezení. Protože
d_k→e^(−1)>0, členy řady nejdou k nule. Totéž platí pro záporné
celé z; jedinými konvergentními případy jsou nezáporná celá z.
Dodatek odpovědi 16 z 22. srpna 2025 výslovně doplňuje růst druhého
faktoru, který ve starší stručné odpovědi nebyl vyřčen.

Rovnice (12) má v originálu `product_{0<=j<=k}(n−j)`, tedy k+1
faktorů u a_(k+1). Obraz v měřítku 300 tuto mez jednoznačně potvrzuje.
OCR i Markdown ji změnily na j<k. Podezření V1-C0005 je proto
**dismissed**; v knize se index neopravuje. Koeficienty pro
`ln(n!)=sum_{m>=1} a_m n^(falling m)` jsou jednoznačně
`m! a_m=Delta^m ln(n!) při n=0`, kde Delta f(n)=f(n+1)−f(n).
Tudíž a_1=0, a_2=ln2/2, a_3=(ln3−2ln2)/6. Obecný význam a
konvergence této Newtonovy řady jsou dokázány v analytické poznámce.

## Úlohy 22,24,25

22. Přirozená hypotéza je `(n+x)!/(n! n^x)→1` pro pevné x.
Pro kladné celé x je podíl konečný součin (1+j/n); pro x=0 je 1,
pro x=−r je převrácený součin (1−j/n), 0<=j<r, pro n>=r.
Pokud navíc funkce splňuje x!=x(x−1)!, dostáváme nutně
`x!=lim n^x n!/[(x+1)...(x+n)]` mimo záporné celé x.
To je definice (13). Hypotéza a rekurence tak určují rozšíření
jednoznačně; existence a platnost hypotézy pro toto rozšíření jsou
ověřeny v analytické poznámce. Samotná rekurence by jednoznačnost
nedávala, protože připouští periodické násobitele.

24. Monotonie ln(x) dává pro n>=1
`integral_1^n ln x dx <= ln(n!) <= integral_1^n ln x dx+ln n`.
Integrál je n ln n−n+1. Exponenciací vzniknou přesně obě knižní
meze `n^n/e^(n−1) <= n! <= n^(n+1)/e^(n−1)`.
Při n=1 nastává rovnost. Knižní alternativní součiny teleskopují
na stejné podíly; aplikace 1+x<=exp(x) je platná. Podmínka k>1
u pomocného výrazu k/(k−1) byla doplněna známým erratem z 2020.

25. Padající a rostoucí mocninu definujeme konečnými součiny
`x^(falling k)=product_{j=0}^{k−1}(x−j)` a
`x^(rising k)=product_{j=0}^{k−1}(x+j)` pro celé k>=0.
Převrácení pořadí a vytažení znamének dávají (20).
Rozdělení součinu do dvou bloků dává

```text
x^(falling(m+n)) = x^(falling m) (x−m)^(falling n),
x^(rising(m+n))  = x^(rising m)  (x+m)^(rising n).       (3)
```

Původní odpověď má v druhé řádce chybné x−m; pro x=2,m=n=1
dává 6 versus 2. Oprava na x+m je v erratech z 21. ledna 2001.
Gama podíly (21) dokazují pokračované identity pro necelé parametry
tam, kde jsou definovány, resp. jako identity meromorfních funkcí.
Při celočíselném k se odstranitelná neurčitost inf/inf vyhodnotí
pokračováním konečného součinu, nikoli aritmetikou nekonečen.

## Prameny a omezení

Legendre, Essai sur la théorie des nombres, 2. vydání (1808),
s. 8–10, byl získán a zobrazen v originálu. Odstavec XVI začíná
na s. 8 a na s. 9 dává součet podlah; XVII na s. 10 obsahuje
přesně číslicový vzorec úlohy 12 a XVIII binární případ úlohy 11.
Tiráž datuje vydání 15. října 1808. Tato konkrétní atribuce i
odkaz doplněný erratem z 2005 jsou uzavřeny; nejde o audit
zbytku Legendreovy knihy.

Leibniz 1682, Stickelberger 1890 a Uhlerova tabulka zůstávají
pramenně otevřené. V hlavním textu zbývají Knopp, Hermitův
originál, Kramp, Hankel, Capelli/Toscano a Dutka, v úloze 18
Wallisův text ve Struikově Source Book. Davisův konkrétní odkaz
je ověřen v analytické poznámce. Stav získání je v
`sources/factorials-primary-source-access.json`; matematické
důkazy se s těmito pramennými mezerami nezaměňují.

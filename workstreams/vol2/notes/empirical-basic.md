# §3.3.2 A–F: základní empirické testy

**Rozsah:** text str. 61–66 do konce permutačního testu a úlohy
1–10, 21–22 s odpověďmi na str. 562–563 a 565. Matematické odvození,
algoritmy G/C/P a uvedené příklady dokončeny; nový podstatný nález
v tomto bloku nevznikl. Navazující run test, překrývající se tice
z úlohy 24 a ostatní části sekce mají samostatnou frontu.

Základní model: U_j jsou nezávislá rovnoměrná čísla v [0,1);
Y_j=floor(d U_j) jsou nezávislé rovnoměrné číslice 0,...,d-1.
Používáme celočíselné d>=1 a kladné počty pozorování; netriviální
chí-kvadrát test navíc vyžaduje více než jednu kategorii s kladnou
pravděpodobností. Mezery v tomto bloku jsou počty neúspěchů do zásahu
intervalu, nikoli kruhové vzdálenosti z úloh 26–30.

## A–B a úlohy 1–2: četnosti a disjunktní tice

Intervaly [r/d,(r+1)/d) mají délku 1/d. Mapa U -> floor(dU) tedy
dává pravděpodobnosti 1/d a zachovává nezávislost mezi různými j.
Pro disjunktní tice délky t dostáváme d^t stejně pravděpodobných
kategorií; jednotlivé tice jsou nezávislé. Chí-kvadrát rozdělení
s d^t-1 stupni volnosti je limitní, s pevným d,t a rostoucím počtem
tic n. Doporučení n>=5d^t je praktická volba, nikoli ostrá věta
o přesnosti aproximace; ta byla již rozlišena v §3.3.1.

Překrývající se dvojice tento model nesplní. Například pro d>=2 má
událost, že (Y_0,Y_1)=(0,0) a (Y_1,Y_2)=(0,0), pravděpodobnost d^-3,
zatímco součin marginálních pravděpodobností je d^-4. Původní
multinomická kalibrace tedy není oprávněna. Úloha 24 opravuje test
jinou statistikou; nebude zaměňována s touto jednoduchou námitkou.

Polootevřené intervaly a počet dvanácti testů jsou známé opravy
2022/2024, nikoli nové nálezy. Schéma G na str. 63 souhlasí s kroky
algoritmu, včetně návratu po zaznamenání každé mezery.

## C a úlohy 3–4: mezery do dalšího zásahu

Nechť p=beta-alpha>0 je pravděpodobnost zásahu. Označme L počet
neúspěchů před prvním úspěchem. Nezávislost vstupů dává

```
Pr(L>=r)=(1-p)^r,
Pr(L=r)=p(1-p)^r.
```

Sloučením hodnot r>=t dostaneme přesně (4). Délky po sobě jdoucích
mezer jsou nezávislé: pro předepsané délky je odpovídající počáteční
binární slovo jednoznačné a jeho pravděpodobnost je součin těchto
geometrických pravděpodobností. Totéž plyne ze začátku nové nezávislé
posloupnosti po každém zásahu.

Invariant G: před G3 je r počet dosavadních neúspěchů od posledního
zapsaného zásahu a j index posledního přečteného vstupu. Počáteční
j=-1 zajistí první čtení U_0. G5 připíše právě jednu kategorii
min(r,t); G6 zastaví po n zásazích. Při náhodném vstupu s p>0
algoritmus skončí skoro jistě, při libovolném vstupu končit nemusí.

Celkový počet přečtených hodnot T je součet n veličin L+1. Pro j>=n
musí být j-tý vstup úspěch a z předchozích j-1 přesně n-1 úspěchů:

```
Pr(T=j)=binom(j-1,n-1)*p^n*(1-p)^(j-n),
E z^T = (p*z/(1-(1-p)*z))^n,
E T=n/p,  Var(T)=n*(1-p)/p^2.
```

To potvrzuje odpověď 3 a směrodatnou odchylku sqrt(n(1-p))/p.
Při p=1 je T=n deterministicky; obvyklé označení maximální doby
čekání jako nekonečné platí jen pro 0<p<1. Případ p=1 stejně nemůže
splnit požadavek kladných očekávaných četností všech kategorií testu.
Tuto triviální degeneraci výslovně oddělujeme od platných vzorců.

## Úloha 5: pevná délka a kruhové spojení binárního slova

Zde je N délka vstupu a n_N náhodný počet zásahů. Pro 0<p<1 platí
n_N/N -> p skoro jistě. Lineární zpracování prvních N vstupů obsahuje
n_N dokončených geometrických mezer. Uzavření do kruhu změní jen
první z nich, ke které se připojí neúspěchy na konci vstupu. Vektor
četností se tedy změní nejvýše o jednu ztracenou a jednu přidanou
kategorii. Pravděpodobnost n_N=0 je (1-p)^N a jde k nule.

Zbývá zdůvodnit náhodný počet pozorování, což samotná nezávislost
mezer bez dalšího nedělá. Nechť pi_r jsou pravděpodobnosti (4), e_r
jednotkové vektory kategorií a W_i=e_(min(L_i,t))-pi. Jsou nezávislé,
centrované a omezené. Pro k=floor(Np) je

```
(sum_(i<=n_N) W_i - sum_(i<=k) W_i)/sqrt(N) -> 0
```

v pravděpodobnosti. Důkaz: mimo událost |n_N-k|<=epsilon*N je
pravděpodobnost malá podle zákona velkých čísel. Uvnitř této události
stačí omezit maximum částečných součtů na okně délky epsilon*N
kolem k. Kolmogorovova maximální nerovnost dává po dělení N odhad
konstantou krát epsilon/delta^2 pro překročení libovolného delta>0.
Nakonec necháme epsilon klesnout k nule. Nevyžaduje se nezávislost
indexu n_N na mezerách.

Proto funguje stejná vektorová centrální limitní věta jako při pevném
počtu pozorování, s kovariancí diag(pi)-pi*pi^T. Po vydělení odmocninami
pi_r jde o ortogonální projekci hodnosti t. Pearsonův součet má tedy
v limitě chí-kvadrát rozdělení s t stupni volnosti, jak žádá úloha.
Kruhová úprava o omezený vektor tuto limitu nemění.

Poznámka odpovědi o neplatné náhradě n_N za Np je také správná.
Vlastní konkrétní doklad: p=1/2,t=1. Pak Z_0 počítá cyklické vzory
11 a Z_1 vzory 10. Z překryvů dvou sousedních dvojic dostaneme pro N>=5

```
E Z = (N/4,N/4),
Cov(Z) = (N/16) * [[5,-1],[-1,1]].
```

Po nesprávném standardizování jmenovateli N/4 má limitní kovariance
vlastní čísla (3+sqrt(5))/4 a (3-sqrt(5))/4. Výsledná kvadratická
forma je součet těchto násobků dvou nezávislých chí-kvadrát veličin
s jedním stupněm volnosti. Není to chí-kvadrát rozdělení. Normální
limita zde plyne z centrální limitní věty pro omezené lokální funkce
nezávislých bitů, jejichž závislost dosahuje jen na sousední dvojici.
Celé momenty byly navíc přesně ověřeny enumerací pro N=5,...,12.

## D: pokerové rozklady

Stirlingovo číslo S(k,r) počítá rozklady k označených pozic do r
neprázdných skupin. Označme (d)_r=d(d-1)...(d-r+1). Každému rozkladu
lze přiřadit r různých číslic právě (d)_r způsoby, například při
kanonickém seřazení skupin podle první pozice. Proto

```
Pr(přesně r různých číslic v k-tici)=(d)_r*S(k,r)/d^k.
```

Rekurence S(k,r)=r*S(k-1,r)+S(k-1,r-1) současně poskytuje algoritmus
a ověřuje hraniční hodnoty S(0,0)=1, S(k,0)=0 pro k>0.
Pro sedm klasických vzorů pěti číslic jsou počty po řadě

```
(d)_5, 10(d)_4, 15(d)_3, 10(d)_3, 10(d)_2, 5(d)_2, d.
```

Jejich součet je d^5 a sloučení podle počtu různých číslic odpovídá
(5). Sloučení obecně ztrácí informaci: alternativy mohou měnit
poměr dvou párů a trojice, aniž změní počet různých hodnot.
Knižní „nearly as good“ je praktické hodnocení, nikoli tvrzení
o stejné síle proti všem alternativám.

## E a úlohy 7–10: sbírání kupónů

Označme T_w počet hodnot potřebný k získání w různých číslic,
1<=w<=d. Aby T_w=r, prvních r-1 hodnot musí obsahovat právě w-1
číslic a poslední musí být nová. Stejným počítáním jako výše:

```
Pr(T_w=r)=(d)_w*S(r-1,w-1)/d^r.
Pr(T_w>=t)=sum_(j=0)^(w-1) (d)_j*S(t-1,j)/d^(t-1).
```

Druhá rovnost je ekvivalentní vytištěnému výrazu v odpovědi 9;
pro w=d dává (6). V algoritmu C se mění d na w pouze v dolní mezi
COUNT a v podmínce dokončení C4. Pole OCCURS nadále zahrnuje všech d
číslic. Invarianty: r je počet přečtených hodnot v aktuálním úseku,
q počet různých číslic a OCCURS jejich přesný indikátor. Každé dokončení
začne další nezávislý úsek, takže pro n úseků opět platí multinomický test.
Úloha 7 dává délky `5,3,5,6,5,5,4`; spotřebuje všech 33 zadaných číslic.

Po získání j různých číslic čekáme na další s úspěšností
q_j=(d-j)/d. Tyto čekací doby jsou nezávislé geometrické veličiny
na {1,2,...}; paměť předchozích barev mění jen jejich počet, nikoli
úspěšnost při rovnoměrném losování. Označíme-li
H_d=sum_(i=1)^d 1/i a H_d^(2)=sum_(i=1)^d 1/i^2, máme

```
E z^T_w = product_(j=0)^(w-1) ((d-j)*z/(d-j*z)),
E T_w = d*(H_d-H_(d-w)),
Var(T_w) = d^2*(H_d^(2)-H_(d-w)^(2))-d*(H_d-H_(d-w)).
```

Pro n nezávislých úseků se střední hodnota i rozptyl násobí n.
Vzorce v odpovědích 8–10 souhlasí. Pro w=1 je T_w=1 jistě,
takže „max infinity“ v běžném popisu čekání předpokládá w>=2;
geometrický vzorec i nulový rozptyl mezní případ zachycují správně.

## F a úlohy 21–22: číslování permutací

Spojitý nezávislý výběr má bez rovností všech t! relativních pořadí
stejně pravděpodobných, podle symetrie jeho společné distribuce.
Následuje multinomická kalibrace s t!-1 stupni volnosti. Při konečné
strojové abecedě je třeba rovnosti výslovně řešit; ideální spojitý
model tvrzení je v textu uveden.

V algoritmu P je před P2 počátečních r prvků stále neuspořádaných
a zbytek obsahuje největší hodnoty již správně. Index maxima s
určí číslici s-1 v rozsahu 0,...,r-1. Operace f<-r*f+s-1 přidá
číslici a výměna přesune maximum na pozici r. Při následujícím r-1
platí požadovaná mez f<t!/(r-1)!. Postup skončí seřazeným polem.

Zpětné dělení f čísly 2,...,t vrací zbytky s-1 v opačném pořadí;
výměny s pozicí r jsou involuce. Z hodnoty f lze tedy rekonstruovat
každou původní permutaci. Je jich t! a výsledky leží v [0,t!), takže
jde o bijekci. Současně tím plyne jedinečnost faktoriálového zápisu
f=sum_(j=1)^(t-1) j!*c_j s 0<=c_j<=j.

Úloha 21: cifry při r=10,...,2 jsou 2,3,7,6,4,2,2,1,0, výsledek
886862. Úloha 22: inverze 1024 dává `(9,6,5,2,3,4,0,1,7,8)`.
Všechny permutace délek 1–8 byly ověřeny, celkem 46233 případů:
správné seřazení, bijekce a nezávislé obrácení výměn.

## Úloha 6: cifry e v jiných základech

Výzkumnou otázku zde řeší konkrétní reprodukovatelný experiment,
nikoli obecná věta o všech základech. `experiment_e_digits.py`
vypočítal prvních 10000 míst za radixovou čárkou pro základy 2 až 36.
Každý prefix je certifikován intervalem

```
sum_(j=0)^K 1/j! < e < sum_(j=0)^K 1/j! + 1/(K*K!), K=4797.
```

Horní mez plyne z geometrického odhadu zbytku: každý další faktor
je nejméně K+1. Po vynásobení b^10000 dávají oba racionální konce
stejnou celočíselnou podlahu. Nejde tedy o neověřenou přesnost
aritmetiky s plovoucí čárkou. Samostatná implementace Decimal.exp
při 10030 místech navíc potvrdila všech 10000 desetinných číslic.

V desítkové soustavě jsou četnosti prvních 2000 míst
`196,190,207,202,201,197,204,198,202,203`; Pearsonova statistika je
přesně 53/50=1.06. Pro 10000 míst vychází přesně 861/100=8.61.
Jde o místa za čárkou: zahrnutí úvodní celé číslice 2 by dalo jiné
hodnoty, 1.11 a 8.628. Volba v knize je tak jednoznačně rekonstruována.
Také pravděpodobnost překročení 1.15 pro devět stupňů volnosti je
.9990068148..., ve shodě s uvedenými zaokrouhlenými 99.9 procenta.

Pro srovnání je H_b(v) pravděpodobnost, že chí-kvadrát veličina
s b-1 stupni volnosti nepřekročí v. Je to asymptotická nulová
kalibrace, nikoli pravděpodobnost nějaké vlastnosti pevné konstanty e.

| Základ | Statistika pro 2000 míst | H_b | Statistika pro 10000 míst | H_b |
|---|---:|---:|---:|---:|
| 2 | 4.608 | .968177 | .1936 | .340063 |
| 3 | .037 | .018330 | 1.1498 | .437239 |
| 8 | 4.328 | .258682 | 2.9936 | .114406 |
| 10 | 1.06 | .000714 | 8.61 | .525975 |
| 16 | 14.528 | .514081 | 18.3584 | .755708 |
| 27 | 10.663 | .003454 | 21.8006 | .300444 |

Mezi těmito 35 základy je při délce 2000 desítkový prefix nejvíce
vyrovnaný podle spodního percentilu, následuje základ 27. Pro délku
10000 má nejnižší spodní percentil základ 19, přibližně .051529.
Podobná tendence tedy někde existuje, ale není společná všem základům
ani oběma délkám. Výběry z různých základů nejsou nezávislé; nehledáme
zde po zhlédnutí výsledků nový společný test s tvrzenou hladinou.
Přesné četnosti, všechny statistiky, hashe prefixů a rozsah certifikace
jsou v `results/e-digits.json`.

## Kontroly a zdrojový rozsah

`verify_empirical_basic.py` dokončil 40890 algoritmických případů G,
25384 slov pro poker/kupóny a 97728 případů algoritmu C. Druhý model
kupónů, Markovův řetězec počtu získaných typů, ověřil 1872 přesných
pravděpodobností a 78 dvojic momentů proti uzavřeným vzorcům.
Samostatně byly vyčerpány všechny pokerové vzory pro d=5.
Výsledky `results/empirical-basic.json` se ukládají po blocích;
žádný blok neselhal a úspěšné výpočty se neopakovaly.

Bibliografická kontrola: Pólya 1930 (ZAMM 10, 96–97), von Schelling
1954 (AMM 61, 306–311), Bofingerovi 1961 (AMS 32, 524–534).
Odkaz u úlohy 6 je Stonehamova práce *A Study of 60,000 Digits of
the Transcendental e*, AMM 72 (1965), 483–500, nikoli článek
Geiringerové; její jméno je v knize připsáno zadání/příkladu, takže
to není rozpor. Metadata a přesný rozsah v
`sources/empirical-basic-bibliography.json`. Plné historické články
nebyly získány; matematické výsledky výše jsou vlastní odvození.
[Stonehamův primární záznam](https://www.jstor.org/stable/2314118),
[von Schellingův primární záznam](https://doi.org/10.1080/00029890.1954.11988466).

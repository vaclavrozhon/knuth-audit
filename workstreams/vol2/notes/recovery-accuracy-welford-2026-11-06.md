# Obnova 232 (14)–(16) a celé úlohy 16

7. listopadu 2026. Originály 232,244,615 a relevantní errata
znovu porovnány. Milionové součty ani 12884 archivních kontrol se
**neopakují**. Každý přechod součtu je níže nově doložen analytickou
posloupností v jednotlivém exponentovém pásmu; výpočet není důkazem
obecné nezápornosti. Hranice celé úlohy zahrnuje i závorku v odpovědi.

## Přesná statistická algebra a inicializace

Pro reálná data x1,…,xn a n≥2 je výběrový rozptyl
`S_n/(n−1)`, kde `M_n=(∑x_i)/n` a `S_n=∑(x_i−M_n)²`.
Rozvoj čtverců dává `S_n=∑x_i²−nM_n²`; dosazení průměru
a společný jmenovatel dávají přesně (14):

`σ²=(n∑x_i²−(∑x_i)²)/(n(n−1))`.

Čitatel je v přesné aritmetice nezáporný; n=1 by dělilo nulou
a není zde definovaným výběrovým rozptylem. Při nahrazení operací
plovoucími předchozí Cauchyho argument ani tato algebra nezaručují
nezápornost vypočteného čitatele. Konkrétní záporný výsledek je níže.

Pro k≥2 položme a=M_(k−1), d=x_k−a. Z definice průměru plyne
`M_k=a+d/k`. U starých hodnot se změní centrování o d/k:

`∑_(i<k)((x_i−a)−d/k)² = S_(k−1)+(k−1)d²/k²`,

protože `∑_(i<k)(x_i−a)=0`. Nový člen je
`(x_k−M_k)²=d²(k−1)²/k²`. Součet obou přírůstků je
`(k−1)d²/k=d(x_k−M_k)`. Tím jsou odvozeny obě přesné rekurence,
jejich každý koeficient i vazba na (14).

Původní inicializace M1=x1,S1=0 a k=2,…,n je správná.
Známé erratum 2024 ji sjednocuje na M0=S0=0 a k=1,…,n:
první krok má M1=0+(x1−0)/1=x1 a S1=0+(x1−0)(x1−x1)=0.
Tyto první kroky jsou přesné i v plovoucím modelu, je-li x1 platný
vstup. Různé inicializace se proto neliší v dalším výpočtu.

Plovoucí zápis (15) počítá nejprve rozdíl, potom podíl k, potom
součet s M_(k−1). (16) používá uložené staré M_(k−1) **i nové M_k**.
Záměna obou za stejný nový průměr by nebyla tištěnou rekurencí.
Násobení a dělení mají obvyklou přednost před sčítáním.

## Celá 16(c): obecná nezápornost a všechny okraje

Nejprve pro libovolné t≥0 a K≥2 dokážeme
`R(R(t)/K)≤t`, pokud jsou operace definovány. Nula je triviální.
Pro d=R(t)>0:

* Je-li d≤t, pak d/K≤d a monotonie dává R(d/K)≤R(d)=d≤t.
* Je-li d>t, označme l kladného předchůdce d v **ideální**
  normalizované soustavě se všemi exponenty. Takový l existuje,
  i když by byl mimo konečný strojový rozsah. Nejbližší volba d
  vyžaduje t≥(l+d)/2. Ale d/K≤d/2<(l+d)/2, protože l>0.
  Proto R(d/K)≤l<t. Poslední přísnost plyne z
  t≥(l+d)/2>l. Je-li výsledek mimo konečný rozsah, není operace
  definována a není protipříkladem zákona s touto podmínkou.

Tento argument nevyžaduje určitý výběr půlek; uvnitř důkazu druhé
R porovnává s půlkou přísně. Nezaměňuje l za nulu u nejmenšího
kladného čísla konečného formátu.

Pro v≥u položme t=v−u. Krok z=R(R(t)/K) leží v [0,t].
Tedy u+z∈[u,v] a vnější R nemůže překročit reprezentovatelné konce,
protože R(u)=u,R(v)=v a R je neklesající. Proto
`u⊕((v⊖u)⊘K)` leží v [u,v]. Pro v<u lze argument zrcadlit.
Dokonce ani u nedourčených lichých půlek není nutné předpokládat
globální lichost R: operátor `R_−(t)=−R(−t)` je opět nejbližší
neklesající zaokrouhlení a splňuje stejný pomocný důkaz. Zrcadlený
přírůstek pak leží v [v−u,0]. Případ u=v dává nulový přírůstek.

V rekurenci (15) je K=k≥2. Pokud se velký celočíselný k musí
nejprve reprezentovat zaokrouhleně, stačí pro tuto **nezápornost**
K≥2; přesné statistické identity s k tím ale nevzniknou. V milionovém
příkladu jsou všechna k přesně reprezentovatelná.

Je-li M_k mezi M_(k−1) a x_k, mají oba přesné rozdíly
`x_k−M_(k−1)` a `x_k−M_k` stejné znaménko nebo jsou nulové.
Zaokrouhlení jejich znaménko neobrátí. Jejich plovoucí součin je
nezáporný. Ze S0=0 nebo S1=0 plyne indukcí, že také každý plovoucí
součet v (16) je nezáporný. To dokazuje 16(c), tvrzení na 232 i
tištěný odkaz na intervalový krok v odpovědi 615; nevyužívá
naivní střed `(u⊕v)⊘2`, který obecně nemusí ležet uvnitř intervalu.
Strojová −0 má numerickou hodnotu 0. Výjimky rozsahu zůstávají mimo
tvrzení a nezápornost sama nezaručuje malou chybu.

## Celá 16(a): proč stačí sedm úseků místo dalšího milionového běhu

Ve všech následujících tabulkách b=10,p=8 a R vybírá sudé celé K.
V pevném exponentovém pásmu jsou součty násobky mřížky h. Přidáváme
konstantu c; pokud `c/h=q+r`, 0≤r<1, pak vnitřní přírůstek je
qh pro r<1/2, (q+1)h pro r>1/2. V našich tabulkách žádné r
není půlka. Proto mezi přechody platí přesně
`S_k=S_(k0)+(k−k0)D`, kde D je uvedený zaokrouhlený přírůstek.
Na samotném přechodu se musí znovu zaokrouhlit **přesný**
`S_(k−1)+c` na nové pásmo; není dovoleno jen převzít staré D.

Pro c=1.1111111 jsou všechny vnitřní přírůstky:

| Začátek k0 | S_(k0) | h po přechodu | D až do dalšího přechodu |
| ---: | ---: | ---: | ---: |
| 1 | 1.1111111 | .0000001 | 1.1111111 |
| 10 | 11.111111 | .000001 | 1.1111110 |
| 91 | 101.11110 | .00001 | 1.1111100 |
| 901 | 1001.1102 | .0001 | 1.1111000 |
| 9001 | 10001.020 | .001 | 1.1110000 |
| 90009 | 100000.91 | .01 | 1.1100000 |
| 900819 | 1000000.0 | .1 | 1.1000000 |

Každý uvedený přechod má kontrolu posledního předchozího členu:

| k | S_(k−1) z příslušné lineární formule | Přesný S_(k−1)+c | Nový R |
| ---: | ---: | ---: | ---: |
| 10 | 9.9999999 | 11.1111110 | 11.111111 |
| 91 | 99.999991 | 101.1111021 | 101.11110 |
| 901 | 999.99909 | 1001.1102011 | 1001.1102 |
| 9001 | 9999.9091 | 10001.0202111 | 10001.020 |
| 90009 | 99999.797 | 100000.9081111 | 100000.91 |
| 900819 | 999998.90 | 1000000.0111111 | 1000000.0 |

V každém řádku je předchozí člen pod hranicí pásma a uvedený přesný
nový součet nad ní. Monotónně rostoucí lineární formule a její krok
nedovolují žádný vynechaný dřívější přechod. Následující R je v novém
pásmu a stanoví start dalšího řádku. První hodnotu 101.11110
opravuje známé erratum z roku 2007; původní 101.11111 není převzato.

Po posledním přechodu zbývá 1000000−900819=99181 přírůstků 1.1.
Proto `S_1000000=1000000+99181·1.1=1109099.1`, přesně odpověď.
To je analytický důkaz všech šesti vytištěných přechodů i výsledku;
uložené `results/accuracy-basic.json:welford` se s ním shoduje.

## Celá 16(b): součet čtverců a každá operace (14)

Přesně `1.1111111²=1.23456787654321`, tedy
`c=R(x_k²)=1.2345679`. Archivní druhý součet lze stejně uzavřít:

| Začátek k0 | S_(k0) čtverců | h | D |
| ---: | ---: | ---: | ---: |
| 1 | 1.2345679 | .0000001 | 1.2345679 |
| 9 | 11.111111 | .000001 | 1.2345680 |
| 81 | 100.00001 | .00001 | 1.2345700 |
| 810 | 1000.0015 | .0001 | 1.2346000 |
| 8100 | 10000.235 | .001 | 1.2350000 |
| 80975 | 100000.86 | .01 | 1.2300000 |
| 812682 | 1000000.5 | .1 | 1.2000000 |

| k | Předchozí součet | Přesný nový součet | Nový R |
| ---: | ---: | ---: | ---: |
| 9 | 9.8765432 | 11.1111111 | 11.111111 |
| 81 | 98.765439 | 100.0000069 | 100.00001 |
| 810 | 998.76697 | 1000.0015379 | 1000.0015 |
| 8100 | 9999.0009 | 10000.2354679 | 10000.235 |
| 80975 | 99999.625 | 100000.8595679 | 100000.86 |
| 812682 | 999999.24 | 1000000.4745679 | 1000000.5 |

Stejný argument o lineárních úsecích uzavírá všechny hranice.
Zbývá 187318 přírůstků 1.2, takže poslední součet je
`1000000.5+187318·1.2=1224782.1`.

Položme A=1109099.1, B=1224782.1, n=1000000. Vyhodnocení
(14) s příslušným zaokrouhlením v každé operaci je:

| Operace | Přesná vnitřní hodnota | Výstup R |
| --- | ---: | ---: |
| n⊗B | 1224782100000 | 1224782100000 |
| A⊗A | 1230100811622.81 | 1230100800000 |
| rozdíl předchozích | −5318700000 | −5318700000 |
| n⊗(n−1) | 999999000000 | 999999000000 |

U A² má mřížka krok 100000 a odříznutý zbytek 11622.81 je
menší než polovina tohoto kroku. Ostatní tři řádky už jsou
reprezentovatelné. Absolutní hodnota přesného konečného podílu,
v jednotkách 10^−10, je

`53187000000000/999999 = 53187053 + 187053/999999`.

Zbytek je přísně menší než 1/2, takže konečný výsledek je
`−.0053187053`. Odmocnina reálného záporného čísla neexistuje;
není to problém s přesností implementace odmocniny.

Welfordova varianta je pro tato konstantní data naopak přesná:
M1=c0=1.1111111,S1=0. Je-li M_(k−1)=c0, oba rozdíly od
konstantního x_k jsou 0; podíl, přírůstek i násobek zůstanou 0.
Indukcí M_k=c0,S_k=0 až do milionu a směrodatná odchylka je 0.

## Závorka odpovědi 16: přesný rozbor pomalu rostoucích dat

Tuto část stará poznámka pouze označovala jako varování. Zde ji
nepřebíráme za plně dokázanou. Položme `a=10^−7` a
`x_k=1+a·floor((k−1)/2)`, pro 1≤k≤10^6. Všechny vstupy,
celočíselné k i rozdíly `a·floor((k−1)/2)` jsou přesně
reprezentovatelné v b10,p8; potřebné exponenty jsou v běžném rozsahu.

Indukcí **M_k=1**. Je-li starý průměr 1, přesný rozdíl je ja,
kde j=floor((k−1)/2), a `ja/k<a/2`. Monotonie R zaručí, že
zaokrouhlený podíl je nejvýše a/2. Vnější součet s 1 tedy leží
nejvýše na půlce 1+a/2. Sudé K pro hodnotu 1 (10000000)
vrací i tuto půlku na 1. Průměr se proto nikdy nezvýší.

Pro sudé n=2m jsou pravý průměr a jeho chyba přesně
`M_true=1+a(m−1)/2` a `M_float−M_true=−a(m−1)/2`.
Tato absolutní chyba má lineární růst v n při pevné jednotce a.
Při milionu je chyba −.02499995. To rigorózně potvrzuje škodlivý
jev popisovaný závorkou pro průměr.

Oba rozdíly používané v (16) jsou nyní ja. Bez dalších zaokrouhlení
produktů a akumulace by vznikl součet

`T=a²·m(m−1)(2m−1)/3`,

protože každé j=0,…,m−1 se vyskytne dvakrát. Skutečný centrovaný
součet těchto dat je

`S_true=a²·m(m²−1)/6`.

První formule používá součet čtverců celých j; druhá odečte
`n·(a(m−1)/2)²` od T. Jejich poměr je přesně
`T/S_true=2(2m−1)/(m+1)=4−6/(m+1)` pro m>1.
Absolutní rozdíl T−S_true je `a²m(m−1)²/2`, tedy kubický
v m, ne lineární. Nelze proto bez uvedení měřítka interpretovat
slova „errors of order n“ jako absolutní chybu surového S_n.

Nejde pouze o analýzu hypoteticky přesné akumulace. Z nejbližší
osmimístné desítkové mřížky plyne relativní chyba jedné nenulové
operace nejvýše η=5·10^−8. Pro nezáporné sčítance a nejvýše
n+1 násobných chybových faktorů má skutečné S_float meze

`(1−η)^(n+1) T ≤ S_float ≤ (1+η)^(n+1) T`.

Dolní Bernoulliho mez je `1−(n+1)η`; horní je nejvýše
`1/(1−(n+1)η)`, neboť binomické koeficienty jsou nejvýše
odpovídající mocniny n+1 a lze sečíst geometrickou řadu.
Pro n=10^6 dávají tyto meze
`.9499999 T < S_float < 1.052632 T`. S uvedeným přesným
poměrem tedy zejména `3.79 S_true < S_float < 4.211 S_true`.
Skutečná rekurence (16) je tak pro tyto údaje podstatně nepřesná,
i když nezápornost platí. Nový milionový běh není potřeba.

Pokud by závorka slovem chyba označovala **výslednou směrodatnou
odchylku**, vzniká z T hodnota `a·sqrt(m(m−1)/3)`, kdežto pravá
odchylka je `a·sqrt(m(m²−1)/(6(2m−1)))`. Jejich rozdíl roste
jako `a·m/(2sqrt(3))`, tedy lineárně, stejně jako chyba průměru.
To je konzistentní výklad výstrahy. Závorka ovšem sama neurčuje
normu, jednotku chyby ani to, zda míní S_n, rozptyl či odchylku.
Její **doslovný rozsah ponecháváme partial**, zatímco jev, přesná
chyba průměru i velká chyba skutečného S_n jsou výše prokázány.

## Bibliografie, errata a rozsah dokončení

Vydavatelská stránka Welfordova článku potvrzuje název, svazek 4
(1962) a strany 419–420. [Metadata vydavatele](https://www.tandfonline.com/doi/abs/10.1080/00401706.1962.10490022).
Jeho PDF vrátilo 403 a nebylo přečteno. Van Reeken 1968,
149–150 z doplnění 2024 nebyl obsahově získán. Chan–Lewis 1979,
526–531 má dohledaný DOI, ale stránka i PDF ACM vrátily 403;
obsah nebyl čten a nedokládá zde přesný význam sporné závorky.
Úplné vlastní algebraické důkazy se o tyto nedostupné texty neopírají.

Přesně převzata kontrola všech čtyř vrstev errat a TeXu v
`accuracy-errata-excerpts.txt`: závorky (15),(16) z roku 2000,
hodnota 101.11110 z roku 2007 a sjednocená inicializace/citace 2024.
Nejsou to nové nálezy. Odkaz na lepší garanci kompenzovaného sčítání
v úloze 19 se posoudí s celou touto úlohou, nikoli předem.

Hlavní vzorce (14)–(16), všechny části 16(a–c), oba dlouhé součty
a všechny konkrétní tištěné výsledky jsou nyní matematicky uzavřeny.
Celý záznam 16 zůstává partial pouze pro přesný význam slov o řádu
chyby v dodatečné závorkové větě. Následují všechny mezikroky
(17)–(19) a definice/nerovnosti porovnání (21)–(39).

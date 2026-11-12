# Rozklad podle stupňů, stopa a statistiky: §4.6.2

Matematický blok: text 447–448 a úlohy 28–31,37, odpovědi 686–690.
Původní sazba zobrazena; všechny relevantní vrstvy errat prohledány.
Pět výpočetních checkpointů prošlo. C0209–C0212 níže jsou konkrétní
chyby hranice, vzorce pravděpodobnosti, přesnosti pomocného modelu
a jednoho indexu. Vlastní důkazy uzavírají matematiku uvedených úloh.
Rychlejší algoritmy z 449 a historické atribuce zůstávají samostatným
otevřeným blokem, nikoli automaticky prověřenými stránkami.

## 1. Notace a oddělení stupňů

F_p je těleso zbytků modulo prvočíslo p. Monický polynom má vedoucí
koeficient 1. Polynom je bez násobných faktorů, pokud se žádný
ireducibilní faktor neopakuje. Píšeme a_d pro počet monických
ireducibilních polynomů stupně d nad F_p. Z úlohy 4 již máme
a_d=(1/d)Σ_{c|d} μ(c)p^(d/c), kde μ je Möbiova funkce.

Algoritmus D po odstranění násobností pracuje se zbytkem v vstupu u.
Na začátku D2 má každý faktor v stupeň větší než d a
w≡x^(p^d) modulo v. Platí-li 2(d+1)>deg(v), zbývá nejvýše jeden
faktor: každý by měl stupeň alespoň d+1. Jinak zvýšíme d a umocníme w
na p. Ireducibilní polynom stupně e dělí x^(p^d)−x právě když e|d.
Protože stupně menší než d jsou už odstraněny, gcd v D3 obsahuje
právě všechny faktory stupně d. Po vydělení gcd a redukci w invariant
trvá. Tím je dokázána úplnost, ukončení i správnost předčasného konce.
Počáteční w=x stačí jako kongruence i pro vstup stupně 1.

Úprava D1–D3 z 6. ledna 2011 přidává názvy kroků, nikoli novou
matematiku. Násobnosti se zpracují samostatně v úlohách 33–36.

## 2. Náhodný Berlekampův rozklad a jeho cena

Čínská věta o zbytcích, dále CRT, ztotožňuje řešení v^p=v modulo
součin r různých ireducibilních faktorů s vektory v F_p^r.
Rovnoměrné nezávislé koeficienty v bázi tedy dávají rovnoměrný vektor
hodnot. Pro liché p označme θ=(p−1)/(2p). Faktor je v
gcd(u,v^((p−1)/2)−1) právě když jeho hodnota je nenulový čtverec,
což má pravděpodobnost θ. Jednotlivé souřadnice jsou nezávislé.

Pravděpodobnost netriviálního rozdělení je 1−θ^r−(1−θ)^r. Pro r≥2
je nejmenší při r=2; pak je (1−p^(−2))/2≥4/9. Rozvinutí sudých
členů binomické věty dává přesně vzorec na 447.

Každá dvojice faktorů zůstane po k nezávislých kolech nerozlišená
s pravděpodobností c^k, kde c=θ²+(1−θ)²≤5/9. Z unijní meze je
pravděpodobnost nedokončení nejvýše binom(r,2)c^k. Součet této meze,
omezené shora 1, dává očekávaně O(log r) kol. Tím je doplněno
knižní „as we may“ obecným důkazem.

Pro n=deg(u) stojí vytvoření v nejvýše O(rn) operací v F_p;
modulární mocnění a gcd přes aktuální faktory stupňů n_i stojí
O(Σn_i² log p) těchto operací. Protože Σn_i=n, dostáváme
O(n²(log p)³ log r) bitových operací při školské aritmetice.
Týká se to náhodné fáze po získání báze, ne ceny celé lineární algebry.

## 3. Cantor–Zassenhaus a úloha 29

Nechť g je součin r≥2 různých ireducibilních polynomů stejného
stupně d a q=p^d. Každý zbytek t modulo jeden faktor je prvkem
F_q. Nenulové prvky se dělí na čtverce a nečtverce, po (q−1)/2.
Proto t(t^((q−1)/2)+1)(t^((q−1)/2)−1) mizí na každé složce.
Tři možnosti 0,−1,1 jsou navzájem výlučné. Z toho plyne přesná
součinová identita (21) pro tři monické gcd, bez násobností.

Zvolme dva různé faktory q_1,q_2. Rovnoměrné t stupně <2d má
podle CRT nezávislé rovnoměrné zbytky t_1,t_2 stupňů <d. Právě
jeden je nenulový čtverec v (q²−1)/2 z q² případů. Gcd s −1 proto
oddělí aspoň tuto dvojici s pravděpodobností

```text
2 ((q−1)/(2q)) ((q+1)/(2q)) = 1/2 − 1/(2q²).
```

Je-li r=2, je to přesná pravděpodobnost; pro větší r dolní mez.
Normalizace nenulového t na monický může prohodit třídy +1 a −1,
ale celý tříčlenný rozklad (21) zachová. Nulové a konstantní volby
mohou být vynechány jako neúspěšné. Tím nelze bez dalšího zachovat
přesnou distribuci jediného gcd s −1; posuny d=1 mají vlastní
pravděpodobnost odvozenou v [sqrt-mod-prime.md](sqrt-mod-prime.md), §2.

**C0212:** první řádek 687 vyhodnocuje druhý zbytek t_2 modulo q_1,
má však být modulo q_2. Konkrétně nad F_3 vezměme
q_1=x²+1, q_2=x²+x+2, t=(x+2)q_1. Pak t_1=0,t_2=x,
x^4 mod q_1=1, ale x^4 mod q_2=−1. Vytištěná podmínka tedy
prohlašuje rozdělení, zatímco skutečné gcd(g,t^4−1)=1.
Oprava indexu obnoví celý důkaz.

**C0211:** následující heuristický odstavec předpokládá nezávislé
bity pravděpodobnosti přesně 1/2 a tvrdí, že se předpoklad stane
rigorózním při volbě deg(t)<rd. CRT skutečně dává nezávislost,
ale pravděpodobnost je stále θ=(q−1)/(2q), nikoli 1/2. Například
p=3,d=1,r=2 dává pravděpodobnost 1/3 na jeden faktor, 4/9 pro
rozdělení a průměrně 9/4 pokusů místo 2. Nejde o selhání algoritmu
ani o neplatnost velkého O. Stačí použít správné vychýlené bity.

Dokonce ani úplnou nezávislost mezi všemi faktory nepotřebujeme
pro odhad ceny. V každém kole se počítá na nerozdělených blocích.
Blok m≥2 faktorů přispívá m²≤4binom(m,2). Očekávaný součet počtů
nerozlišených dvojic přes všechna kola je

```text
binom(r,2) sum_{k>=0} (θ²+(1−θ)²)^k
  = binom(r,2)/(2θ(1−θ)) = 2 binom(r,2)/(1−q^(−2)).
```

To platí i pro deg(t)<2d, neboť potřebujeme jen nezávislost každé
dvojice a nezávislost po sobě jdoucích voleb t. Při školském
modulárním mocnění má blok m faktorů cenu O(m²d³(log p)³) bitů.
Celá fáze tedy stojí očekávaně O(r²d³(log p)³). Knižní závislost
O(r²(log p)³) odpovídá pevnému d; d zde není schováno v konstantě.
Původní rekurence s vyváženými bity má skutečně řešení
A_r=2binom(r,2); vyplývá ze stejného počítání dvojic s c=1/2.

Tabulka osmi kubických polynomů nad F_3 na 448 byla celá ověřena.
Tři posuny dávají všech osm různých podpisů. Obecná překážka
a_d>2^p je prostý princip přihrádek pro d>1: každý polynom má
jen p binárních výsledků posunových zkoušek. Pro d=1 nemůže být
a_d>2^p, takže tento argument nepotřebuje rozhodovat nulové hodnoty.

## 4. Stopa a úloha 30

Stopou prvku a∈F_(p^d) rozumíme T(a)=a+a^p+…+a^(p^(d−1)).
T(a)^p=T(a), proto T(a)∈F_p. Mapa T je lineární nad F_p.
Není nulová: polynom T(X) má stupeň p^(d−1)<p^d a vedoucí
koeficient 1, takže nemůže mizet na celém tělese. Nenulová lineární
mapa do jednorozměrného F_p je surjektivní a každý její vzor má
p^(d−1) prvků. To je potřebná, v tištěném řešení jen implicitní
rovnoměrnost stopy, včetně případů p|d.

Polynomická identita ∏_{s∈F_p}(T(X)−s)=T(X)^p−T(X)=X^(p^d)−X
pak dává analogii (21). Pro p=2 a náhodné t stupně <2d jsou stopy
na libovolné dvojici faktorů nezávislé rovnoměrné bity, takže se
odliší s pravděpodobností 1/2. Výpočet v←t, v←t+v^p opakovaný
d−1krát je přesně Hornerovo seskupení součtu Frobeniových mocnin.

Cohenovy volby t=x,x³,…,x^(2d−1) stačí deterministicky. Pro každé
k>0 se T(x^k) rovná T(x^j), kde j je lichá část k, protože stopa
je invariantní vůči umocnění na p=2. Konstantní člen přidává
stejnou hodnotu na všech faktorech, takže je nerozlišuje. Pokud
žádný z uvedených d monomů neodděluje nějakou dvojici, linearita
říká totéž pro každý t stupně <2d, ve sporu s CRT a surjektivitou
stopy. Proto každý reducibilní blok některá z těchto voleb rozštěpí.

## 5. Úloha 31: společný počet a výjimka d=1

Stupeň prvku α∈F_(p^d) je nejmenší e>0 s α^(p^e)=α; je to
stupeň jeho minimálního polynomu nad F_p. Prvky stupně d jsou
rozděleny do Frobeniových orbit po d prvcích, jedné na každý
monický ireducibilní polynom stupně d.

Pro d>1 posun α↦α+t i zlomková transformace
α↦(α+t_1)/(α+t_2) zachovávají množinu prvků stupně d bijektivně.
V druhém případě jmenovatel není nula a obraz není 1; inverze
je α=(t_1−βt_2)/(β−1). Obě transformace mají koeficienty v F_p,
takže tělesa generovaná α a jeho obrazem jsou stejná. Podmínka
rovnosti dvou charakterů je podmínkou čtvercovosti podílu.
Tím je dokázána rovnost obou počtů pro d>1.

Počet prvků plného stupně, které jsou čtverci, získáme Möbiovou
inverzí přes podtělesa. V podtělese F_(p^(d/c)) je každý nenulový
prvek čtvercem v celém tělese, pokud je c sudé; při lichém c je
čtvercem přesně polovina. Po vydělení délkou orbity vyjde

```text
n(p,d) = (1/(4d)) sum_{c|d} (3+(-1)^c) μ(c) (p^(d/c)−1).
```

Pro liché d>1 je to přesně a_d/2: všechny c jsou liché a Σμ(c)=0.
Knižní rozlišení mezi náhodným vstupem a náhodným posunem je správné;
tato věta sama nezaručuje úspěch posunů pro každý pevný součin.

**C0209:** zadání výslovně dovoluje d≥1. Pro d=1 však část(i) dává
(p−1)/2 polynomů a část(ii) jen (p−3)/2. Stačí p=3,t_1=0,t_2=1:
část(i) pro t=0 má jediný polynom x−1, zatímco část(ii) nemá žádný.
Obecně součet charakterů χ((a+t_1)(a+t_2)) je −1 a dvě hodnoty a
dávají nulu; shodná nenulová znaménka proto nastanou (p−3)/2krát.
Oprava d≥2 zároveň opraví větu „exactly half when d is odd“
v doprovodné odpovědi, jejíž výjimkou je právě d=1.

## 6. Úloha 37: přesná distribuce stupňů

Náhodným polynomem rozumíme rovnoměrný monický polynom stupně n nad
F_p; libovolný rovnoměrný nenulový vedoucí koeficient tento rozklad
stupňů nezmění. Označme k_j počet faktorů stupně j **s násobnostmi**,
tedy Σj k_j=n. Pro každý j vybíráme multiset k_j prvků z a_j možností.
Jednoznačnost rozkladu dává přesnou pravděpodobnost

```text
P_p(k_1,k_2,…) = p^(−n) product_{j>=1} binom(a_j+k_j−1,k_j).
```

**C0210:** tištěný výraz ∏(a_j/p^j)^k_j/k_j! je pouze asymptotický,
nikoli přesný. Pro p=2,n=2,k_1=2 jsou tři polynomy x²,x(x+1),(x+1)²
ze čtyř, tedy 3/4; tištěný vzorec dává 1/2. Ani výklad bez násobných
faktorů tento výraz neopraví: tehdy je v čitateli binom(a_j,k_j).

Pro pevné n a p→∞ máme a_j~p^j/j a pro pevné k_j
binom(a_j+k_j−1,k_j)~a_j^k_j/k_j!. Limita je proto
∏1/(j^k_j k_j!). Přesně n! krát tento součin je počet permutací
daného cyklového typu: uspořádáme všech n prvků, pak odstraníme
j rotací každého j-cyklu a k_j! permutací stejně dlouhých cyklů.
Asymptotický závěr zadání je správný.

Galoisovská poznámka na 689–690 používá další, hlubší externí věty:
Frobeniovu/Čebotarevovu hustotu a van der Waerdenův výsledek pro
téměř všechny celočíselné polynomy. Nezaměňujeme je za důsledek
právě provedeného konečného počítání. Definice Galoisovy grupy přes
součin lineárních forem je konzistentní: nezávislé proměnné y_i
rozlišují všechna pořadí kořenů; ireducibilní racionální součin
obsahující identické pořadí odpovídá přesně jeho orbitě pod
automorfismy rozkladového tělesa. Historické údaje a původní hlubší
důkazy zůstávají odděleně evidovány v otevřeném podbloku.

## 7. Úloha 28: přesné tabulky, limita a rychlost konvergence

V počítaném případu „lucky“ se každý stupeň vyskytuje nejvýše
jednou, včetně násobností. Jeho pravděpodobnost je
[z^n]G_p(z), kde G_p(z)=∏_{j≥1}(1+b_j z^j), b_j=a_j/p^j.
Pro pevné n a p→∞ dostaneme G(z)=∏(1+z^j/j). Obě tištěné tabulky
pro n=1,…,10 byly přesně ověřeny, také nezávislým úplným výčtem
malých polynomů. Tento výklad je přísnější než „po odstranění
násobností zůstane nejvýše jeden faktor každého stupně“.

Pro úplný důkaz asymptotiky označme γ=lim(H_m−log m), Eulerovu
konstantu. Pišme G(z)=h(z)/(1−z),

```text
h(z)=A(z) exp L(z),       A(z)=(1+z)exp(−z),
L(z)=sum_{j>=2} [log(1+z^j/j)−z^j/j].
```

Koeficienty L splňují
L_n=−(1+(-1)^n)/n²+O(n^(−3)). Člen s druhou mocninou v logaritmu
je −2/n² pro sudé n. Ostatní mají součet O(n^(−3)): v součtu
1/(m j^m) s mj=n,m≥3 rozdělíme m≤sqrt(n) a m>sqrt(n).
V první části dominuje m=3 a následující členy jsou geometricky
menší; ve druhé je j≥2 a tedy exponenciální pokles v m.

Z tohoto odhadu plyne pro E(z)=exp L(z), že E_n=O((n+1)^(−2)).
Podrobně: pro w_n=(n+1)^(−2) platí (w*w)_n≤Cw_n, protože
v každém součinu jeden index nepřesahuje n/2 a druhý člen je
nejvýše 4w_n. Proto norma sup_n |a_n|/w_n je až na pevnou
konstantu submultiplikativní; exponenciální řada konverguje i v ní.

Identita E'=L'E dává nE_n=Σ_{j=0}^{n−1}(n−j)L_(n−j)E_j.
Pro j≤n/2 dosadíme odhad L a nahradíme 1/(n−j) hodnotou 1/n;
chyba je O(log n/n²), protože Σ_{j≤n/2}j|E_j|=O(log n).
Pro j>n/2 použijeme |E_j|=O(n^(−2)) a
Σ_{k≤n/2}k|L_k|=O(log n). Po vydělení n tak dostaneme

```text
E_n=−(E(1)+(-1)^n E(−1))/n² + O(log n/n³).
```

Koeficienty A mají konečné absolutní momenty všech řádů. Vynásobení
A proto dává stejný vzorec s E(±1) nahrazenými h(±1).
Protože A(−1)=0, alternující člen zmizí. Součet absolutně
konvergujících koeficientů h je

```text
h(1)=lim_{m→∞} (m+1) exp(−H_m)=exp(−γ),
h_n=−exp(−γ)/n²+O(log n/n³),
[z^n]G(z)=exp(−γ)+exp(−γ)/n+O(log n/n²).
```

Poslední rovnost je součet koeficientů h do n a odhad zbývajícího
ocasu. Tím je de Bruijnova asymptotika uvedená v knize dokázána
vlastním argumentem, nejen numericky ilustrována.

Pro pevné p platí 0≤b_j≤1/j a |b_j−1/j|≤2p^(−j/2)/j.
Stejný rozklad s log(1+b_jz^j)−z^j/j má koeficienty O(n^(−2));
lineární rozdíl je exponenciálně malý a vyšší mocniny odhadneme
jako výše. Předchozí norma tedy dává

```text
[z^n]G_p(z)=c_p+O(1/n),
c_p=product_{j>=1} exp(−1/j)(1+a_j/p^j).
```

Pro numerickou kontrolu c_2 se použilo 4096 členů. Logaritmický
ocas je mezi −1/(2N)−2·2^(−(N+1)/2)/((N+1)(1−2^(−1/2))) a 0.
S 80ciferným numerickým vyhodnocením to dává
0.39673409647<c_2<0.39678252889, což potvrzuje tištěné ≈.397.
Odhad ocasu je analytický; zaokrouhlení numeriky není certifikováno
intervalovou knihovnou. Také exp(−γ)=0.56145948356… souhlasí.

## 8. Běhy, prameny a zbývající rozsah

`verify_equal_degree.py` prošel v session74107 čtyřmi bloky, exit0,
limit180s na blok. Nový doplněk constants proběhl zvlášť v session91694;
žádný z předchozích úspěšných bloků se při doplnění neopakoval.

| Blok | Rozsah | PID | Sekundy |
|---|---|---:|---:|
| distinct | 1610 vstupů D,3014 etap,24 položek kubické tabulky | 1335249 | 0.754034812 |
| split | 16908 polynomů,44 distribucí,16 dalších distribucí Berlekampových hodnot | 1335256 | 5.012064537 |
| trace | 1367 stop,56 Cohenových dvojic,324 binárních rozdělení | 1335260 | 0.523224342 |
| counts | 2382 polynomů,106 typů,46233 permutací,10 těles úlohy31 | 1335262 | 0.734071293 |
| constants | 4096 členů součinu a analytický odhad ocasu | 1335373 | 1.500372648 |

Časy jsou pouze kontroly správnosti, nikoli asymptotický benchmark.
Výsledky a logy jsou v `results/equal-degree*`; procesy jsou dokončeny.
Zdrojový manifest `sources/equal-degree.json` vymezuje přečtené originály
a zdroje pouze stažené pro další práci. Knopfmacher–Warlimont a
Cantor–Zassenhaus PDF odmítlo AMS; nejde o důkaz jejich nedostupnosti
jinde. Kaltofen–Shoup1998 a von zur Gathen–Shoup1992 jsou staženy
pro samostatný audit rychlejších algoritmů. Známá oprava 20. července
2000 na449 přidává citaci1992 a zlepšuje uvedenou praktickou mez.
V tomto bloku tyto algoritmy ještě neprohlašujeme za zkontrolované.

Lehmerův originál1972 byl vizuálně přečten na379–388 (šest dvojstran
PDF). Theorem2 na381–382 potvrzuje limitu a rozsah citace. Ostatní
aritmetické posloupnosti a jejich tabulky nebyly nezávisle auditovány;
článek neobsahuje zde citovanou de Bruijnovu zpřesněnou formuli.
Ta je výše dokázána samostatně; její osobní atribuce a Greene–Knuth
§4.1.6 zůstávají historicky otevřené. OCR obrázků nebylo spuštěno,
protože tesseract není instalován; jde o vizuální čtení, ne OCRdoklad.

# §4.6.1: dělení, obsah, gcd a úlohy 1–10

Kontrola 4. listopadu 2026. Tento blok pokrývá matematické jádro stran
420–427, zadání 1–10 na 435–436 a odpovědi 672–673. Uvedené stránky
byly přečteny v původní sazbě. Celý oddíl má 27 úloh a končí až nahoře
na 439; poslední odpověď je na 678. Subresultanty, zbývající úlohy
a historický kontext mají navazující samostatné bloky.

## Dělení nad tělesem a algoritmus D

Těleso F je komutativní okruh, v němž má každý nenulový prvek inverzi.
Pro nenulový dělitel v stupně n a dividend u platí jednoznačné rozdělení
`u=q*v+r`, kde `deg(r)<n`. Stupeň nuly chápeme jako `-infinity`.
Je-li stupeň u menší než n, vezmeme q=0,r=u. Jinak lze nejvyšší člen
u zrušit odečtením násobku `x^(deg(u)-n)*v`; jeho koeficient získáme
dělením vedoucím koeficientem v. Opakováním stupeň zbytku klesá.

Algoritmus D tento postup provádí na pevných pozicích od m−n do nuly.
Před krokem k stačí, aby platilo

```text
u_original = v * sum_(i>k) q_i*x^i + u_remaining,
deg(u_remaining) <= n+k.
```

Volba `q_k=u_(n+k)/v_n` zachová identitu a zruší pozici n+k. Kniha
tento koeficient v poli fyzicky nepřepisuje nulou, protože jej už
nepoužije. Menší koeficienty smí být aktualizovány sestupně, bez změny
uloženého q_k. Pro konstantní v je zbytek prázdné pole, tedy nula.
Jednoznačnost plyne ze stupně `(q1−q2)*v=r2−r1`: nenulová levá strana
by měla stupeň alespoň n, pravá menší než n.

Každý krok D2 má n násobení a n odčítání plus jednu operaci podílu.
Pro n>=1 je tedy uvedený počet úměrný `n*(m−n+1)`. Pro hraniční n=0
zůstává m+1 skalárních dělení; jednotný odhad je
`O((n+1)*(m−n+1))`. Monický dělitel, tedy v_n=1, dělení nevyžaduje.
Při dané inverzi v_n lze všechna dělení nahradit násobeními. Týž
důkaz funguje v libovolném komutativním okruhu, je-li v_n jednotka.

## Jednoznačná faktorizace, obsah a Gaussovo lemma

Jednotka je prvek mající násobnou inverzi. Obor integrity je nenulový
komutativní okruh bez dělitelů nuly. UFD je obor integrity, v němž
se každý nenulový nejednotkový prvek rozkládá jednoznačně na
ireducibilní faktory, až na pořadí a jednotkové násobky. Ireducibilní
znamená, že prvek není jednotka a v každém rozkladu má jednotkový
faktor. V UFD je takový prvek také prvočinitelem v silnějším smyslu:
dělí-li součin, dělí alespoň jeden faktor. To plyne porovnáním
jednoznačných rozkladů.

Polynom nad UFD S je primitivní, pokud žádný prvočinitel S nedělí
všechny jeho koeficienty. Pro daný prvočinitel p vyberme nejnižší
indexy j,k koeficientů u,v, které p nedělí. V koeficientu součinu
při x^(j+k) není člen u_j*v_k dělitelný p, kdežto všechny ostatní členy
jsou. Součin je tedy primitivní. To dokazuje Lemma G bez použití
jednoznačné faktorizace v S[x], která je teprve cílem úlohy 10.

Obsah c nenulového polynomu je gcd jeho koeficientů, určený až na
jednotku. Exponent každého prvočinitele v c je minimum jeho exponentů
v nenulových koeficientech. Potom `u=c*pp(u)`, kde pp je primitivní
část. Tento popis dává existenci i jednoznačnost Lemma H. V argumentu
o ukončení vyjímání prvočinitelů stačí sledovat jeden nenulový
koeficient; nulové koeficienty nemají konečný počet prvočinitelů.
Gaussovo lemma a jednoznačnost obsahu dávají násobnost cont a pp
až na vzájemně inverzní jednotky, přesně jako (4).

Nad Z normalizujeme pp kladným vedoucím koeficientem; obsah pak může
být záporný. Nad tělesem volíme obsah rovný vedoucímu koeficientu,
takže pp je monický. Příklady −26x²+39 a 21x+14 na 424 souhlasí:
obsahy −13,7; primitivní části 2x²−3,3x+2; součin má obsah −91.
Rozklad na 422 se ověří přímo:
`2*3*x*(3x−4y)*(5x+yz)=90x³−120x²y+18x²yz−24xy²z`.
Poslední faktor je primitivní a lineární v x nad Q(y,z), proto je
ireducibilní nad Z[y,z][x]; stejně pro 3x−4y. Faktory 2,3 jsou nad Z
ireducibilní konstanty, nad Q jednotky.

Známá oprava Lemma H z 17. srpna 2024 pouze nahrazuje u výrazem u(x).
Nejde o nový nález ani o změnu důkazu.

## Pseudodělení R a zobecněný Eukleidův algoritmus E

Pseudodělení se vyhne skalárnímu dělení. Položme a=v_n, m>=n. V kroku
k se pracovní polynom R nahradí `a*R − b*x^k*v`, kde b je jeho
koeficient na pozici n+k. Současně můžeme celý dosavadní podíl Q
nahradit `a*Q+b*x^k`. Po m−n+1 krocích dostaneme

```text
a^(m−n+1) * u = Q*v + R,   deg(R)<n.
```

Člen b*x^k přidaný v k-tém kroku se následně ještě k-krát násobí a,
proto lze přímo uložit `q_k=b*a^k`, jak činí kniha. Všechny kroky
jsou polynomiální identity, takže platí i v okruhu s děliteli nuly,
včetně případu, kdy a^(m−n+1)=0. Nevynecháváme kroky s b=0:
i ty násobí zbývající pole koeficientů číslem a.

Optimalizace závorky v R2 je správná. Koeficient u_t, t<m−n, nejprve
projde právě m−n−t kroky s k>t, ve kterých se pouze násobí a.
Tyto násobky lze provést předem a v těchto krocích již pozici t
neměnit. Další kroky s k<=t proběhnou obvyklým způsobem.
V oboru integrity je Q,R jednoznačné: stejný stupňový argument jako
pro D používá pouze nenulovost součinu vedoucích koeficientů.

Pro gcd (největšího společného dělitele ve smyslu dělitelnosti) platí
`gcd(u,v)=gcd(v,u−qv)` až na jednotky, protože dvojice mají stejné
společné dělitele. Algoritmus nad tělesem končí díky poklesu stupňů;
poslední nenulový zbytek normalizujeme na monický. Skalární obsah gcd
nad UFD se oddělí jako gcd obsahů u,v, jak uvádí (7).

Při primitivních vstupech v algoritmu E skalár a^(m−n+1) nevnáší
nové nekonstantní společné faktory. Lze to zdůvodnit v podílovém
tělese K (tělese zlomků prvků S), kde je a invertibilní; Gaussovo
lemma pak dovolí vrátit se k primitivním polynomům nad S. Po každém
pseudodělení vezmeme pp zbytku, a na konci připojíme gcd původních
obsahů. Výsledek dělí oba vstupy a každý jejich společný dělitel
dělí výsledek. Pro implementaci výslovně prohodíme vstupy, když
deg(u)<deg(v). Vytištěné E pořadí opakuje z předchozího odstavce;
alternativně prázdná smyčka R1 při nižším stupni vrátí r=u a první
průchod E3 provede prohození. Tento hraniční detail nepovažujeme za
doložený nesprávný výsledek algoritmu E.

Všechny čtyři celočíselné řádky tabulky (12), čtyři nenulové racionální
zbytky v (13), pseudopodíl (11) a čtyři dělení modulo 13 v (5)–(6)
byly ověřeny přesně. Nad Z i sedmi okruhy modulo 2,3,4,6,8,10,13
prošlo 1280 pseudodělení, včetně nulových vnitřních koeficientů,
konstantních dělitelů a nulových mocnin vedoucího koeficientu.
Ověřena byla vždy celá identita a mez stupně, i optimalizovaná verze.
Pro 160 celočíselných dvojic byl gcd nezávisle doložen dělitelností
a Bézoutovou identitou získanou přesným racionálním dělením.

## Úlohy 1–3

**1.** Výsledek je q=8x³−4x+8, r=28x²+4x+8. Platí `16u=qv+r`.

**2. Oprava posouzení 12.11.2026:** Vytištěná posloupnost i následující
gcd `x³+3x²+4x+6` modulo 7 jsou správné. V2-C0192 byl odmítnut:
předchozí audit chybně přečetl koeficient jako 2. Dělitelé obou vstupů
i samostatná Bézoutova identita potvrzují skutečně vytištěný výsledek.
Symetrie gcd polynomu a jeho obrácení platí: jejich společný dělitel
má nenulový konstantní člen, obrácení zachovává dělitelnost a prohodí
oba vstupy. Monické gcd je proto jednotkovým násobkem svého obrácení.

**3.** Bézoutova identita vyjadřuje gcd jako kombinaci vstupů. Udržujme
pro každý zbytek r_i koeficienty A_i,B_i s `r_i=A_i*u+B_i*v`.
Inicializace jsou (1,0) a (0,1); při dělení podílem q přejdeme z dvojice
řádků na druhý a rozdíl prvního s q-násobkem druhého. Identita se zachová.
Na konci současně normalizujeme r_i,A_i,B_i. V notaci zadání je
V=A_i a U=B_i.

Jsou-li m,n oba větší než stupeň d výsledného gcd a m>=n, označme d1
stupeň předposledního nenulového zbytku. Stupně koeficientů posledního
řádku jsou přesně `deg(U)=m−d1`, `deg(V)=n−d1`. Důkaz: po první
nenulové redukci mají dvě koeficientové posloupnosti přísně rostoucí
stupně; násobení dalším podílem stupně rozdílu dvou po sobě jdoucích
zbytků tak v rekurzi nemůže být vyrušeno předchozím členem. Teleskopický
součet těchto rozdílů dává uvedené vzorce. Zvláštní první řádek je
(0,1); následující má (1,−q1), stupně 0,m−n. To založí indukci
i při m=n. Proto oba stupně jsou menší než m−d,n−d.

Při d=n je druhý vstup dělitelem prvního a nastává výjimka U=1,V=0
pro monický v. Kniha má koeficienty prohozené (V2-C0189). Pro obecné v
má U hodnotu 1/leading(v), pokud má být gcd monický.
Přesně 12 810 případů v soupisu nad konečnými tělesy splnilo nenulové
stupňové podmínky a potvrdilo oba přesné stupňové vzorce.

Pro `u=x^m−1`, `v=x^n−1` mají všechny nenulové zbytky tvar
`x^d−1`. Dělení monickým polynomem zachovává celočíselné koeficienty;
totéž tedy platí pro všechny Bézoutovy koeficienty. Pro 21,13 vychází

```text
V = x^11+x^8+x^6+x^3+1,
U = -(x^19+x^16+x^14+x^11+x^8+x^6+x^3+x),
(x^21−1)V + U(x^13−1) = x−1.
```

Obě vytištěné explicitní odpovědi souhlasí.

## Úlohy 4–5: celé rozdělení stupňů a jeho průměry

Pracujeme v tělese F_p zbytků modulo prvočíslo p. Pro pevný monický
v stupně n a monický u stupně m>=n je mapování `u -> (q,r)` při
dělení bijekcí mezi monickými u a dvojicemi monického q stupně m−n
a libovolného r stupně <n. Zbytek je proto rovnoměrný mezi p^n
možnostmi a nezávislý na náhodném v. Podmíněně na jeho nenulovém
stupni je monická normalizace zbytku opět rovnoměrná. Tím se stejný
argument opakuje v každém kroku; nezávislost je podmíněná na stupních.

Každá přísně klesající posloupnost `n>n1>...>nt>=0` má pravděpodobnost
`(p−1)^t/p^n`, včetně prázdné posloupnosti s pravděpodobností p^(−n).
Ekvivalentně se každý stupeň j z množiny {0,...,n−1} objeví nezávisle
s pravděpodobností `q=1−1/p`. Označíme-li jeho výskyt indikátorem I_j,
pak t je součet I_j a součet stupňů je součet j*I_j. Okamžitě dostáváme

```text
E(t) = n(1−1/p),
E(n1+...+nt) = n(n−1)/2 * (1−1/p).
```

Třetí veličina je součet `(previous_degree−j)*j` přes vybrané stupně j.
Podmíněně na výběru j je vzdálenost k předchozímu vyššímu stupni
(nebo k n) v průměru `sum_(h=1)^(n−j) p^(1−h)`. Její násobení
pravděpodobností q dá 1−p^(j−n). Celý průměr je tudíž

```text
sum_(j=0)^(n−1) j*(1−p^(j−n))
 = n(n+1)/2 − (n+1)*p/(p−1)
   + (p/(p−1))^2 * (1−p^(−n−1)),
```

přesně jako v knize. Tento důkaz pokrývá i n=0, kdy všechny veličiny
jsou nula. Vytištěný alternativní kombinatorický vzorec pro součet
přes t-prvkové posloupnosti lze odvodit takto: doplňme n0=n a
n_(t+1)=−1; mezery `g_i=n_(i−1)−n_i−1` pro 1<=i<=t+1 jsou
nezáporné a mají součet n−t. Pak
`sum_(i=1)^t (n_(i−1)−n_i)*n_i`
`=sum_(i=1)^t (g_i+1)*(t−i+sum_(j>i)g_j)`.
Symetrie složení a vytvořující funkce `(1−z)^(−t−1)` dávají součet
`binom(n+2,t+2) − (n+1)binom(n+1,t+1) + binom(n+1,2)binom(n,t)`,
tedy vzorec S_t na straně 672. Pro t=0 je nula.

V dovětku je chybný index události t=n (V2-C0191), nikoli její
pravděpodobnost q^n. Pro úlohu 5 je gcd konstantní právě tehdy, když
se objeví stupeň 0: pravděpodobnost je 1−1/p při n>0. Při n=0
jsou oba monické vstupy rovny 1, a pravděpodobnost je 1.
Celé rozdělení stupňových posloupností, všechny tři průměry i úloha 5
byly přesně ověřeny pro všech 13 678 monických dvojic: p=2,m<=5 a
p=3,m<=4, vždy 0<=n<=m. Nejde jen o srovnání zaokrouhlených průměrů.

## Úloha 6: gcd od nejnižších koeficientů

Pro nenulový polynom f označme val(f) nejmenší index nenulového
koeficientu. Odebereme z obou vstupů mocniny x a jejich společnou
část na konci připojíme jako `x^min(val(u),val(v))`. Zbývající vstupy
mají nenulové konstantní členy. Jejich obrácení definujeme
`f*(x)=x^deg(f) f(1/x)`; v této třídě zachovává stupeň, součiny
a je involucí. Lze tedy spočítat gcd obrácených vstupů obyčejným
Eukleidovým algoritmem, výsledek obrátit a normalizovat.

Jednotlivé dělení od nízkých koeficientů má tento přesný tvar. Při
deg(u)=m>=n=deg(v)>0 a v(0)≠0 vybereme q stupně nejvýše m−n tak,
aby prvních m−n+1 koeficientů u−vq zmizelo. To lze postupně jednoznačně
udělat, protože každý krok dělí pouze v(0). Pak

```text
u=v*q+x^(m−n+1)*r,  deg(r)<n.
```

Získáme jej i obrácením identity `u*=v* Q+R`, kde deg(R)<n:
q je Q obrácené s doplněním na délku m−n+1, r je R obrácené
s doplněním na délku n. V dalším kroku odstraníme případné mocniny x;
protože v(0)≠0, nemění tím gcd. Stupně klesají, takže postup končí.
To dokazuje možnost binární analogie bez jakéhokoli požadavku na
uspořádání koeficientů.

Kniha v exponenciálním posunu uvádí m−n. V2-C0190 přesně rozlišuje
rozpor s touto obvyklou interpretací od existence jiné platné redukce.
Proto je tento detail veden jako kandidát; výše uvedená správná
konstrukce a její ukončení jsou dokázány obecně. Bylo navíc ověřeno
100 racionálních dělení s obrácením a nenulovými konstantními členy.
Citaci [Norton 1989](https://epubs.siam.org/doi/abs/10.1137/0218042?journalCode=smjcat) potvrzuje vydavatelský záznam.
[Ma–von zur Gathen 1990](https://cosec.bit.uni-bonn.de/fileadmin/user_upload/publications/pubs/magat90.pdf) byl získán z autorského archivu; vizuálně přečteny strany
429–431 (PDF 1–3). Potvrzují bibliografii, různé varianty posouvání
a přesný počet operací obyčejného dělení. Celé analýzy všech variant
zde nejsou reprodukovány; tato úvodní část nerozhoduje interpretaci C0190.

## Úlohy 7–10: jednotky a faktorizace nad podílovým tělesem

**7.** Ze součinu uv=1 a sčítání stupňů v oboru integrity plyne,
že u,v mají stupeň nula. Jednotkami S[x] jsou tedy přesně jednotky S.

Následující pomocný fakt vysvětluje přechod mezi S a jeho podílovým
tělesem K. Každý nenulový h v K[x] lze zapsat jako `(a/b)*H`, kde
a,b jsou nesoudělné nenulové prvky S a H je primitivní v S[x].
Nejprve odstraníme společný jmenovatel koeficientů, pak jejich obsah
a zkrátíme skalární zlomek. Pokud je F primitivní a F*h má koeficienty
v S, Gaussovo lemma říká, že F*H je primitivní. Z toho, že b dělí
všechny koeficienty a*F*H, plyne, že b je jednotka. Tedy h patří do S[x].
To je potřebný fakt o sestupu dělitelnosti, nikoli předpoklad UFD pro S[x].

**8.** Nekonstantní ireducibilní u v Z[x] je primitivní: jinak jeho
obsah a primitivní část jsou dvě nejednotky. Pokud by se rozložil
na dva nekonstantní polynomy nad Q, odstranění jmenovatelů, vyjmutí
obsahu a Gaussovo lemma by daly nekonstantní rozklad u nad Z, spor.
Takto opravené tvrzení je správné. Konstantní prvočísla jsou
protipříklady původního znění (V2-C0188), které výslovně používá
definici ireducibility zahrnující konstantní prvočinitele. Tatáž poznámka
zaznamenává znaménko primitivní části v odpovědi.

**9.** Pro primitivní nenulové u,v je nesoudělnost v S[x] ekvivalentní
nesoudělnosti v K[x]. Jeden směr je přímý; druhý plyne vyjmutím
skaláru a právě dokázaným sestupem dělitelnosti. Eukleidův algoritmus
nad K dá kombinaci u,v rovnou 1; společným násobkem jmenovatelů
obou koeficientových polynomů ji převedeme na kombinaci nad S rovnou
nenulové konstantě. Naopak společný nekonstantní dělitel by musel
dělit tuto konstantu, což odporuje stupňům. Společný konstantní
nejednotkový dělitel je vyloučen primitivitou. Případ jednotkového
vstupu se vyřídí přímo. Nulový vstup, pokud jej konvence primitivity
nad tělesem připouští, neporušuje ekvivalenci: druhý musí být jednotka,
aby mohla kombinace být nenulová konstanta.

Čtyřsložková konstrukce v odpovědi zachovává
`u1*u+u2*v=u3*u4` a `v1*u+v2*v=v3*v4`.
Jestliže `a*u4=q*v4+b*r`, pak koeficientová dvojice
`a*v3*(u1,u2)−q*u3*(v1,v2)` má při kombinaci se vstupy hodnotu
`b*u3*v3*r`, přesně jako v odpovědi. Nenulové skaláry lze zkracovat
společným obsahem. Zastavení při konstantním zbytku dává žádanou
kombinaci; je-li už počáteční druhý primitivní vstup konstanta,
potřebná kombinace je k dispozici bez dalšího zbytku.

**10.** Faktorizace v S[x] existuje: oddělíme obsah, jehož rozklad
existuje v S. Primitivní část rozložíme nad K postupným snižováním
stupňů. Každý faktor nahradíme jeho primitivní verzí s koeficienty v S
pomocí společných jmenovatelů. Gaussovo lemma zaručuje, že celkový
skalár mezi dvěma primitivními polynomy je jednotka S. Dostáváme
faktorizaci v S[x]. Její nekonstantní faktory jsou ireducibilní:
rozklad nad S by dal rozklad nad K, vyjma konstantní nejednotky,
kterou primitivita nepřipouští.

Nad K jsou ireducibilní polynomy prvočiniteli, protože Bézoutova
identita pro nesoudělné polynomy dokazuje Eukleidovo lemma. Rozklad
je tedy nad K jednoznačný. Dva primitivní polynomy nad S, které
se liší nenulovým skalárem K, se liší jednotkou S, jak ukazuje
porovnání exponentů prvočinitelů v koeficientech. Unikátnost
nekonstantních faktorů tak sestoupí do S[x]; obsah má jednoznačný
rozklad už v S. To dokončuje necirkulární důkaz úlohy 10.

## Stav výpočtu, errata a omezení

Čtyři bloky `verify_polynomial_division.py` prošly, celkem přibližně
1,106 s úspěšné práce. První běh PID 1321204 skončil s kódem 1 na
porovnání gcd s chybně přepsaným koeficientem (C0192); blok core
byl již uložen jako passed. Po opravě očekávané odpovědi
pokračoval PID 1321264 s `--resume`, kód 0, limit 180 s. Již úspěšný
core se neopakoval. Konečné kontroly nenahrazují obecné důkazy výše.

Všechny dostupné vrstvy errat byly prohledány; log a metadata vymezují
konkrétní rozsah. Potvrzené nálezy: C0188, C0189, C0191. C0192 byl
při kontrole 12.11.2026 odmítnut; kniha měla správný koeficient již
v prověřovaném prvním dotisku, nešlo o opravu jejího výsledku.
C0190 zůstává kandidátem z interpretačních důvodů uvedených v jeho
poznámce. Historie Gauss/Nuñez/Stevin, text od 428, subresultanty
a úlohy 11–27 jsou předmětem další práce. Není tvrzeno ověření
nejnovějšího fyzického dotisku ani odeslání hlášení.

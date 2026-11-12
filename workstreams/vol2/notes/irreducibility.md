# Ireducibilita a velikost faktorů: §4.6.2–38,39,41

Audit 4. listopadu 2026. Zadání460–461 a odpovědi690–691 byly
zobrazeny v původním třetím vydání / prvním tisku. Ireducibilní znamená
nerozložitelný na dva polynomy kladného stupně nad daným tělesem;
u primitivních celočíselných polynomů používáme Gaussovo lemma pro Q a Z.
Monický polynom má vedoucí koeficient1. Výška H(f) je maximum absolutních
hodnot koeficientů f. Úloha41 je výzkumná; zde kontrolujeme formulaci,
publikovaná tvrzení a konkrétní příklady, nikoli nevyřešenou obecnou otázku.

## 1. Perronovo kritérium:38

Píšeme u(x)=x^n+a*x^(n−1)+...+u_0, kde u_0!=0. Kořeny počítáme
s násobností. Používáme následující podobu Rouchého věty: je-li na
jednotkové kružnici |g|>|h|, mají g a g+h stejně kořenů uvnitř.
Pro polynomy to plyne i sledováním g+t*h,0<=t<=1: na kružnici nikdy
nevznikne nula, a počet uvnitř, daný argumentovým principem, je tedy
konstantní. To je použitý standardní vstup komplexní analýzy.

Při |a|>1+sum_{j=0}^{n−2}|u_j| použijeme dominantní člen a*x^(n−1).
Uvnitř je přesně n−1 kořenů a na kružnici žádný. Každý monický
celočíselný netriviální faktor má nenulový celočíselný konstantní člen;
součin velikostí jeho kořenů je alespoň1. Musí proto obsahovat jeden
kořen mimo kruh. Dva takové faktory však nemohou sdílet jediný vnější
kořen. Tím je první varianta dokázána.

Při a=0 a A=u_(n−2)>1+sum_{j=0}^{n−3}|u_j| použijeme A*x^(n−2).
Uvnitř je n−2 kořenů a vně dva. Kdyby se u rozložil na dva monické
celočíselné faktory, každý by obsahoval právě jeden vnější kořen.
Nereálné kořeny každého reálného faktoru tvoří sdružené dvojice;
oba vnější kořeny by tedy musely být reálné. Pro reálné z,|z|>=1,
položme r=1/z. Potom 0<|r|<=1 a

```
1 + A*r^2 + sum u_j*r^(n−j)
 >= 1 + A*r^2 − sum |u_j|*|r|^(n−j)
 >= 1 + r^2*(A − sum |u_j|) > 1.
```

Žádný takový z není kořenem. Stejný argument zahrnuje n=2 a prázdný
součet. Pro n=1 je ireducibilita triviální; druhá podmínka se nepoužívá.

**C0219, confirmed:** v tištěném dolním odhadu690 chybí absolutní
hodnoty u r^3,...,r^n. Pro u=x^3+4x+1 a r=−1/2 je absolutní hodnota
výrazu15/8, ale tištěná dolní mez17/8. Jde o chybnou algebraickou
nerovnost použitou v důkazu, nikoli protipříklad kritéria nebo tvrzení,
že toto r je převráceným kořenem. Přesná oprava je výše.

Bibliografický odkaz na Rouchého21,cahier37(1858),1–34 má kandidáta
C0221. Běžně citovaný původní článek je22,cahier39(1862),193–224,
ale zde nebyly získány plné oba originály. Kritérium na rozhodnutí této
bibliografické otázky nezávisí. Perron1907 a Brauer1948/1951 nebyly
v tomto bloku plně čteny; jejich obecnější věty nejsou nově auditovány.

## 2. Co osvědčuje stručný certifikát:39

Certifikát je konečný zápis, jehož správnost lze přesně ověřit.
Stručnost zde znamená počet bitů omezený polynomem ve stupni n
vstupu a největší bitové délce jeho koeficientů. Hledání certifikátu
nemusí mít polynomiální čas.

Nejprve nápověda: je-li v ireducibilní nad Q a netriviální h dělí
v(t(x)), zvolme kořen alpha polynomu h. Pak beta=t(alpha) je kořen v
a Q(beta) je podtělesem Q(alpha). Proto deg(h)>=deg(v); při redukovatelném
h stačí zvolit jeho ireducibilní faktor. Alternativně resultant
R_h(y)=Res_x(h(x),y−t(x)), determinant Sylvesterovy matice, má tvar

```
R_h(y) = a_h^deg(t) * product_alpha (y−t(alpha)),
```

kde a_h je vedoucí koeficient h. Má stupeň deg(h), nenulový vedoucí
koeficient a společný kořen s v, a proto v dělí R_h. Konstantní t lze
vyřídit přímo; v stupně>=2 nemá racionální kořen, takže v(t)!=0.
U lineárního v je požadovaná mez deg(h)>=1 automatická.

Je-li u monický stupně n a t celočíselný, je
v(y)=Res_x(u(x),y−t(x)) monický celočíselný stupně n a u dělí v(t(x)).
Je to také charakteristický polynom násobení prvkem t v algebraickém
prostoru Q[x]/(u). Jestliže v splní Perronovo kritérium, každý
netriviální faktor u má podle nápovědy stupeň alespoň n. To je
certifikát ireducibility u, který nepotřebuje předpokládat ireducibilitu
u při **ověřování**. Tu použijeme pouze při důkazu existence t.

## 3. Malé obrazy kořenů dávají Perronovy nerovnosti

Nechť n>=3, v monický celočíselný a všechny jeho kořeny beta_j
nenulové. Položme delta=1/(4n). Předpokládejme jednu z možností:
(a) všechny kořeny kromě jediného reálného B mají velikost<=delta;
(b) všechny kromě jedné sdružené dvojice beta,conj(beta) mají
velikost<=delta a |Re(beta)|<=delta. Toto je přesný význam
„smallness condition“ v odpovědi690.

Pro monický Q tvořený N malými kořeny pišme
Q(y)=y^N+q_1*y^(N−1)+...+q_N a S=sum_{j>=1}|q_j|.
Součinová koeficientová nerovnost dává
S<=(1+delta)^N−1<1/3, protože N<=n−1 a
(1+delta)^N<=1/(1−N*delta)<4/3.

V případě(a) máme N=n−1 a v=(y−B)Q. Nenulový celočíselný
konstantní člen v dává |B|>=delta^(−N)>2. Součet L absolutních
hodnot koeficientů v pod stupněm n−1 splňuje
L<=(S−|q_1|)+|B|S. Proto

```
|v_(n−1)| − 1 − L >= |B|*(1−S) − 1 − S > 0.
```

To je první Perronova podmínka.

V případě(b) je N=n−2>=1, s=2*Re(beta), R=|beta|^2 a
v=(y^2−s*y+R)Q. Jeho celočíselný koeficient v_(n−1)=q_1−s
má velikost<=N*delta+2*delta=1/4, takže je nulový a q_1=s.
Dále |s|<=1/6, R>=delta^(−N)>=12 a
A=v_(n−2)=R−s^2+q_2>=R−s^2−S (q_2=0 při N=1).
Pro součet L koeficientů pod stupněm n−2 platí
L<=(1+|s|+R)S. Tedy

```
A − 1 − L >= R*(1−S) − 1 − s^2 − (2+|s|)*S
           > 8 − 1 − 1/36 − 13/18 > 0.
```

To je druhá Perronova podmínka. Tato část nutně používá
celočíselnost v; pro libovolný reálný polynom by neplatila.

## 4. Existence malého t a počet bitů

Nechť nyní u je ireducibilní, monický, stupně n>=3. Označme jeho
r reálných kořenů a s sdružených dvojic alpha_j; n=r+2s. Zobrazení
celočíselného vektoru (a_0,...,a_(n−1)) na hodnoty
sum_i a_i*alpha_j^i poskytuje n reálných lineárních forem:
r reálných hodnot a s reálných plus s imaginárních částí.
Vynecháme jednu formu: při s=0 jednu reálnou hodnotu, jinak jednu
imaginární část. Ostatních n−1 forem označíme S_j.

Zvolme celé B>=max_j sum_{i=0}^{n−1}|alpha_j|^i pro sledované kořeny
(včetně sdruženého protějšku, je-li poslední kořen komplexní).
Pro celé 0<=a_i<b je |S_j(a)|<bB. Každé floor(8n*S_j(a)) má
nejvýše16nbB možných hodnot. Zvolíme-li celé b>(16nB)^(n−1), je
b^n>(16nbB)^(n−1). Dva různé vektory proto mají všech n−1
zaokrouhlených hodnot společných. Jejich rozdíl tvoří nenulový
polynom t stupně<n, s celočíselnými koeficienty velikosti<b.
Kontrolované reálné/imaginární části t(alpha_j) mají velikost<1/(8n).

Při samých reálných kořenech je tedy nejvýše jeden obraz velký.
Jinak může být velká jediná sdružená dvojice; její reálná část
zůstává malá. Ostatní velikosti jsou<sqrt(2)/(8n)<delta, takže platí
podmínky oddílu3. Nenulový celočíselný konstantní t by již porušil
malou kontrolovanou reálnou formu; t není konstantní. Žádný obraz
není nula: minimálním polynomem alpha_j nad Q je u, tedy
`t(alpha_j)=0 => u divides t`, ve sporu s 0<=deg(t)<n.

**C0220, candidate:** poslední věta odpovědi39 píše opačný směr,
„t(x) would divide u(x)“. Přirozená oprava je „u(x) would divide t(x)“.
Evidujeme redakční nejasnost směru, nikoli vyvrácení závěru: předpoklad
nulového obrazu je při všech hypotézách sám nemožný a důkaz lze
okamžitě doplnit argumentem minimálního polynomu. Proto ji zde
nepočítáme jako samostatný potvrzený matematický protipříklad.

Zbývá skutečná bitová mez, v knize ponechaná implicitně. Je-li H=H(u),
standardní kořenová mez |alpha|<=1+H dovoluje
B=ceil(n*(1+H)^(n−1)). Pak

```
log B = O(n*log(2+H)+log n),
log b = O(n^2*log(2+H)+n*log n).
```

Stačí tedy zapsat n koeficientů t, každý s polynomiálním počtem bitů.
Koeficienty v, získané determinantem velikosti nejvýše2n−1, mají
O(n*(log n+log H+log b)) bitů; vidíme to rozvojem determinantu na
součinové členy. Přesné výpočty resultantu, dělení a Perronových
nerovností lze také provést v polynomiálním bitovém čase.

Nemonický primitivní vstup s vedoucím koeficientem a převádíme na
U(y)=a^(n−1)u(y/a); U je monický celočíselný, má stejné rozklady nad Q
po invertibilní změně proměnné a koeficientové bity O(n*log(2+H)).
Případy stupně1 jsou triviální; ve stupni2 stačí nesquare diskriminant
(důkaz zápornosti nebo umístění mezi dvě po sobě jdoucí celé druhé
mocniny). Ověření primitivnosti je gcd koeficientů.

## 5. Výzkumná otázka41: co konkrétně bylo ověřeno

V otázce se ptáme na univerzální c, pro které každý nenulový
celočíselný polynom kladného stupně má alespoň jeden ireducibilní
faktor výšky<=c*H(f). Konstanty a obsah jsou běžně vyňaty; jinak
by slovní zadání zahrnovalo jednotky bez ireducibilních faktorů.
To není tvrzení o každém faktoru ani o libovolném rozdělení f=g*h.

Boydova vytištěná identita platí:

```
4*x^8+4*x^6+x^4+4*x^2+4
 = (2*x^4+4*x^3+5*x^2+4*x+2)
   (2*x^4−4*x^3+5*x^2−4*x+2).
```

Oba faktory jsou ireducibilní, např. redukce modulo3 splňuje přesný
Frobeniův test uvedený níže. Poměr výšek je5/4. Silnější pozdější
příklady převzaté z Abbott, *Bounds on Factors in Z[x]*, §7.5–7.7,
byly znovu přesně vynásobeny a jejich ireducibilita doložena:

| Stupeň součinu | H(faktoru)/H(součinu) | prvočíslo certifikátu |
|---|---|---|
|8 (Boyd)|5/4|3|
|20 (§7.5)|3|13|
|20 (§7.7)|3|13|
|20 (§7.6)|1921/873|2|
|40 (§7.6)|55/4|37|

Úplné koeficienty oboustranně ověřených příkladů jsou v
[results/irreducibility.json](../results/irreducibility.json).
Pro faktor g stupně d je partner x^d*g(−1/x); u palindromických g
se rovná g(−x), ale obecně se musí obrátit pořadí koeficientů.
Všechny uvedené stupně d jsou sudé. Substituce a převrácení zachovají
ireducibilitu a výšku; oba faktory tedy dosahují daného poměru.

Pro monický redukovaný g nad F_p stupeň d používá certifikát
`x^(p^d)=x mod g` a `gcd(x^(p^(d/q))−x,g)=1` pro každé prvočíslo
q dělící d. První identita říká, že g je squarefree a všechny stupně
ireducibilních faktorů dělí d; druhé testy vylučují každý vlastní
dělitel d. Z původního vedoucího koeficientu je p vyloučeno, takže
ireducibilita modulo p dává ireducibilitu nad Q. Tato nezávislá
cesta používá vlastní aritmetiku F_p, vedle rozkladu v SymPy.

Z příkladu40 plyne nutná podmínka c>=55/4. Abbottova obecná
neomezená rodina v §7.3 však připouští **redukovatelné** faktory,
takže neřeší otázku41. Závěr článku výslovně odděluje tuto rodinu
od domněnky neomezenosti poměru pro ireducibilní faktory. Kontrolován
byl text arXiv0904.3057v1,§7.2–7.8 a závěr; ne celý článek ani
úplnost jeho počítačových hledání. Omezená rešerše současných zdrojů
nenalezla řešení; netvrdíme, že prokazuje otevřenost k dnešnímu dni.
Boydovo autorství dalších nevytištěných příkladů jsme nezávisle
neověřovali; pozdější příklady potvrzují matematickou mez c>2.

## 6. Kontroly a rozsah uzavření

`verify_irreducibility.py` má tři dokončené bloky:
216 celočíselných Perronových příkladů a přesnou neplatnou nerovnost;
7 přijatých certifikátů porovnaných přes charakteristický polynom
matice i Sylvesterův resultant, přesné dělení u|v(t) a3 nemonické
resultanty;5 dvojic faktorů s5 nezávislými modulárními certifikáty.
Numerické kořeny a LLL pouze hledají t; žádná přibližná hodnota není
součástí rozhodnutí o přijetí certifikátu.

Časy úspěšných bloků:0.258600380s,0.547601698s,0.246201605s;
součet1.052403683s. Timeout240s/blok, všechny exit0. Dva předchozí
neúspěšné pokusy posledního bloku zachovány: chybný vlastní název
API `powmod` a poté chybná vlastní interpretace převráceného faktoru.
Nejsou to selhání knihy. Úspěšné bloky se neopakovaly.

Všech šest vrstev errat prohledáno podle jmen, témat, úloh i stran;
log a hashe viz [sources/irreducibility.json](../sources/irreducibility.json).
Rozšíření druhého vydání z2.8.1981 opakuje vadnou nerovnost i směr
poslední věty39. Odpovídající oprava nenalezena. Fyzický nejnovější
dotisk ani prvenství nálezu neověřeny, žádné hlášení neodesláno.
38/39 jsou matematicky uzavřeny.41 je uzavřena jako audit výzkumné
úlohy s výslovně omezeným rešeršním rozsahem; obecná konstanta není
ani dokázána, ani vyvrácena.

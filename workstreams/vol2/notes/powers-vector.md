# §4.6.3: společné mocnění, transpozice a Olivosova mez

Stav 2026-11-04: úlohy 36, 37, 39 a 40 uzavřeny. Níže jsou úplné
vlastní důkazy konstrukcí, asymptotiky pro pevný počet cílů a obecné
transpoziční identity. Nezávislé konečné kontroly prošly. V tomto bloku
nevznikl nový nález. Opravy formulací z let 2002 a 2022 jsou známá errata.
Úloha 38 a složitostní redukce 41 jsou samostatné následující bloky.

## 1. Model a značení

Sčítací řetězec začíná číslem 1 a každý jeho další člen je součtem dvou
již dostupných členů. Jeho délka je počet sčítání. Píšeme
lambda(n)=floor(lg(n)), kde lg je dvojkový logaritmus. Hodnota
l(n_1,...,n_m) je nejkratší délka řetězce obsahujícího všechny zadané
kladné cíle. Cíle se smějí opakovat; to je výslovné znění opravy 2022.
Hodnoty řetězce lze bez zvýšení ceny sjednotit a vzestupně seřadit.

Vektorový výpočet začíná m jednotkovými vektory e_1,...,e_m, kde e_i má
jedničku v souřadnici i a jinde nuly. Každý placený krok sečte dva již
známé vektory. Vektor (a_1,...,a_m) představuje monom x_1^a_1...x_m^a_m;
sčítání exponentů odpovídá násobení monomů. Pracujeme s formálními
proměnnými a pouze násobením, nikoli se zvláštními hodnotami x_i.
Nulový vektor představuje jednotku; přičtení nuly není placený krok.

Pro m krát p matici nezáporných celých čísel N označíme L(N) nejmenší
počet sčítání k získání jejích p sloupců z m jednotkových vektorů.
Při transpozici v §4 předpokládáme, že žádný řádek ani sloupec není
nulový. Výstupy se smějí opakovat a mohou být vstupními jednotkami.
Tato konvence je potřebná například pro N=(1,1).

## 2. Úloha 36: Strausova konstrukce

Nejprve předpočítáme všechny neprázdné součiny podmnožin m proměnných.
Jednoprvkové jsou vstupy; každý další součin získáme přidáním jedné
proměnné k již známé menší podmnožině. Cena je přesně 2^m-m-1.
Položme n=max(n_1,...,n_m), d=lambda(n). Dvojkové zápisy exponentů
čteme současně po sloupcích od nejvyššího bitu. První sloupec je již
v tabulce; každý z dalších d sloupců vyžaduje jedno umocnění aktuálního
monomu na druhou a nejvýše jedno násobení tabulkovým monomem. Tedy

```text
l([n_1,...,n_m]) <= 2*lambda(n) + 2^m-m-1.
```

Zobecnění používá základ B=2^k, k>=1. Tabulka nyní obsahuje všechny
vektory s každou souřadnicí v {0,...,B-1}. Kromě nulového vektoru a m
jednotek vyžaduje každý jeden krok: zmenšíme jednu kladnou souřadnici
o 1 a přičteme jednotku. Lexikografické pořadí zajišťuje dostupnost
předchůdce. Cena tabulky je B^m-m-1. Po nejvyšší cifře zbývá
q=floor(lambda(n)/k) cifer; každá stojí nejvýše k zdvojení a jedno
sčítání. Dostáváme explicitní konečnou mez

```text
l([n_1,...,n_m]) <= (k+1)*floor(lambda(n)/k) + 2^(km)-m-1.
```

Pro pevné m a epsilon>0 vybereme k tak, aby 1/k<epsilon. Konstantní
cenu tabulky potom pro dostatečně velké n pohltí rozdíl
(epsilon-1/k)*lambda(n). To dokazuje asymptotické nahrazení hlavního
členu 2*lambda(n) členem (1+epsilon)*lambda(n), uvedené v odpovědi.
Nejde o zachování původní ceny binární tabulky pro všechna malá n.

Původní Strausův text, AMM 71 (1964), byl přečten na stranách 806–808.
Strana 806 obsahuje Bellmanovu úlohu, vlastní řešení 807–808 odpovídá
citaci v knize. Strausova explicitní mez je právě výše uvedená tabulková
konstrukce (s jinými písmeny); následuje volba délky bloků rostoucí s n.
Číslo svazku 70 na jedné sekundární bibliografické stránce je nesprávné;
původní záhlaví i DOI metadata mají 71. To není chyba Knuthovy knihy.

## 3. Úloha 37: společná tabulka mocnin a dolní mez

### 3.1 Konečná horní mez

Položme n=max(n_1,...,n_m), d=lambda(n) a B=2^k. Jednou předpočítáme
1,2,4,...,2^d zdvojováním, celkem d kroků. Pro jeden cíl a s ciframi a=sum_t d_t*B^t rozložíme
každou nenulovou cifru jednoznačně jako d_t=2^e*q, q liché. Pro každé
liché q<B vytvoříme skupinový součet

```text
y_q = sum { 2^(kt+e) : d_t=2^e*q }.
```

Každý člen je v předpočítané tabulce, protože kt+e<=lambda(a)<=d.
Je-li v nenulových cifer a g neprázdných skupin, součty stojí v-g
kroků, tedy nejvýše floor(lambda(a)/k). Prázdné skupiny mají hodnotu 0.

Položme K=B/2. Klesajícím průchodem lichých q spočítáme
H_q=sum_{p>=q, p liché} y_p. Pak platí

```text
a = H_1 + 2*(H_3+H_5+...+H_(B-1)).
```

Koeficient y_q vpravo je 1+2*((q-1)/2)=q. Všechny H_q stojí nejvýše
K-1 sčítání; součet H_3,... stojí nejvýše K-2; poslední zdvojení a
sčítání přidají dva kroky. Pro K>=2 je cena nejvýše 2K-1=B-1.
Pro K=1 je a=H_1 a další kroky nejsou potřeba. Nuly i shodné hodnoty
lze vynechat. Celkem máme pro libovolné kladné cíle, včetně opakování,

```text
l(n_1,...,n_m)
 <= lambda(n) + sum_j [ floor(lambda(n_j)/k) + 2^k-1 ].       (V1)
```

To je přesná verze Bernsteinova zlepšení z errata 2002-01-01. Původní
odpověď násobila jednotlivé y_q koeficienty q zvlášť a potřebovala
O(k*2^k) kroků; i tento starší postup dává uvedenou asymptotiku.

### 3.2 Asymptotika a její kvantifikátory

Označení O(g) znamená absolutní hodnotu omezenou konstantním násobkem
g pro dostatečně velký argument; O_m dovoluje závislost konstanty na
pevném m. Položme u=lg(d) a pro velké d zvolme
k=floor(u-2*lg(u)). Potom

```text
k = u-2*lg(u)+O(1),
2^k = O(d/u^2),
d/k = d/u + O(d*lg(u)/u^2).
```

Dosazení do (V1) dává

```text
l(n_1,...,n_m) <= d + m*d/lambda(d)
                     + O_m(d*lambda(lambda(d))/lambda(d)^2). (V2)
```

Zaokrouhlení logaritmů mění jen uvedený zbytek. Ekvivalentní volba
k=floor(lg lg n-2*lg lg lg n) je v opravené odpovědi. V původní
odpovědi stačí koeficient 3 místo 2 kvůli ceně O(k*2^k).

Zápis knihy čteme pro pevné m a n rostoucí. Netvrdíme jednotnou
konstantu nezávislou na proměnném počtu cílů. Pro takové použití je
přímo k dispozici (V1). Yaoův původní článek výslovně používá pevný
počet cílů při porovnání hlavních asymptotických členů.

### 3.3 Zobecnění Erdősova počítání

Dokážeme také tvrzení o odpovídající dolní mezi. Pro pevné m>=1 a
0<epsilon<1 počítejme řetězce s největším členem a, lambda(a)=D,
a délkou r<=D+(1-epsilon)*m*D/lg(D). Označme s=r-D.
Použijeme již samostatně dokázané kódování z
[powers-counting.md, §2–3](powers-counting.md#3-kódování-řetězců-rovnice-2933):
minikroky jsou pomalu rostoucí nezdvojovací kroky definované pomocí
b=2^(epsilon/4); t je jejich počet, v počet ostatních nezdvojovacích
kroků a beta konstanta omezující jejich vzdálenost od posledního členu.
Platí t<=s/(1-epsilon/2), t+v<=3.271*s a počet řetězců s těmito
parametry je nejvýše

```text
binom(r,t+v)*binom(t+v,v)*beta^(2v)*binom(r^2,t).              (V3)
```

Pro t=0 je poslední faktor 1. To zachovává okrajový případ C0224.
Pro pevné m máme r<=2D při dostatečně velkém D. Počet voleb s,t,v
je polynomiální v D. Logaritmy všech faktorů v (V3), kromě posledního,
jsou O_m(D*lg lg D/lg D)=o(D), kde o(D)/D jde k nule. Z nerovnosti
(1-epsilon)/(1-epsilon/2)<=1-epsilon/2 plyne

```text
t <= T=(1-epsilon/2)*m*D/lg(D),
lg binom(r^2,t) <= T*lg(4*e*D^2/T)
                = (1-epsilon/2)*m*D + o(D).
```

Zde e je základ přirozeného logaritmu a monotonnost
x*lg(e*r^2/x) pro x<=r^2 dovoluje nahradit t jeho mezí T.
Takových řetězců je tedy nejvýše
2^((1-epsilon/2)*m*D+o(D)). Každý obsahuje nejvýše (r+1)^m
uspořádaných m-tic cílů, což je jen faktor 2^o(D).

Naproti tomu počet kladných m-tic s lambda(max)=D je
(2^(D+1)-1)^m-(2^D-1)^m, tedy konstantní násobek 2^(mD)
v asymptotickém smyslu. Podíl m-tic s tak krátkým řetězcem jde
exponenciálně k nule. Nejkratší řetězec lze ukončit v maximu cílů,
takže spočítání řetězců skutečně pokrývá všechny výjimky.
Tím jsou oba hlavní členy (V2) pro téměř všechny m-tice nezbytné.

Yao, SICOMP 5 (1976), 100–103, byl přečten celý v původním PDF,
včetně poznámky přidané po korekturách. Základní společné předpočítání,
pevný počet cílů, počítací dolní mez i původní volba k s koeficientem 3
souhlasí. Uvedený důkaz s koeficientem 2 je novější zlepšení.

## 4. Úloha 39: transpozice bez skrytých předpokladů

Orientovaný acyklický multigraf je konečný graf se směrovanými hranami,
bez směrovaného cyklu, ve kterém smíme mít několik hran mezi stejnými
vrcholy. Vstupní vrcholy mají vstupní stupeň nula, výstupní vrcholy
výstupní stupeň nula. Stupeň počítá hrany včetně násobnosti. Pro každý
sloupec výsledku přidáme odlišnou koncovou kopii výstupního vrcholu
s jednou vstupní hranou. Taková kopie nic nestojí. Díky tomu jsou
vstupy a výstupy oddělené i při jednotkových či opakovaných výstupech.

Výpočet s r užitečnými sčítáními má m vstupů, r binárních vrcholů
se dvěma vstupy a p koncových kopií. Má tedy V=m+r+p vrcholů a
E=2r+p hran. Indukce po výpočtu ukazuje, že počet cest od vstupu i
k výstupu j je právě N_ij. A zároveň

```text
r = E-V+m.                                                 (V4)
```

Nepoužité vrcholy odstraníme; nenulové řádky zaručují, že žádný vstup
není zcela zbytečný. Nenulové sloupce zaručují dosažitelnost výstupů.

Naopak v libovolném takovém grafu spočítáme každý nevstupní vrchol
sečtením hodnot jeho předchůdců. Má-li vstupní stupeň d, stojí to d-1
sčítání. Jednovstupní kopie stojí nula. Součet cen je E-(V-m).
Indukce dává tentýž počet cest, tedy správnou matici. Shodné vektory
můžeme znovu použít a cenu jen snížit. Proto L(N) je přesně minimum
E-V+m přes grafy s maticí počtů cest N.

Obrácení všech hran zachová E,V a obrátí každou cestu; počet cest je
pak N^T, kde horní T znamená transpozici matice. Vstupy a výstupy si
vymění role. Grafy obou úloh jsou v bijekci, a proto

```text
L(N) = L(N^T) + m-p.                                       (V5)
```

Pro jediný sloupec (n_1,...,n_m)^T je levá strana počet násobení
jednoho monomu; transponovaná úloha vytváří m mocnin jedné proměnné.
Tedy přesně

```text
l([n_1,...,n_m]) = l(n_1,...,n_m)+m-1.
```

Například pro všechny n_i=1 je vpravo 0+m-1, správný počet násobení
m nezávislých proměnných. Důkaz nepotřebuje striktní pořadí cílů.
Grafová konvence s kopiemi a možnými opakovanými vektory je zde
výslovná; problém interpretace numerických řetězců C0229 z předchozího
bloku tak nevzniká. Pro minima obě definice souhlasí odstraněním duplicit.

Olivos, Journal of Algorithms 2 (1981), 13–21, byl vizuálně přečten
celý. Jeho věta 1 je přesně tato identita. Původní důkaz místo obrácení
hran používá rozklad výpočtu podle uchovávaných mezivýsledků; počet
kroků se upraví o počet vstupů minus počet výstupů. Reference 5 na
straně 21 uvádí předběžnou zprávu na kolokviu ve Štrasburku
18.–20. října 1979. Rok 1979 v zadání tedy není rozpor s publikací 1981.

Citace Knuthovy poznámky Q58 má podle jeho vlastní bibliografie strany
2–4; chybných 2–3 už opravují errata 2022-08-14. Původní úplný text
Q58 jsme nezískali a jeho přečtení netvrdíme. Obecná identita (V5)
je výše dokázána samostatně.

## 5. Úloha 40 a obecná matice koeficientů

Nejprve vytvoříme x^m_1,...,x^m_t za l(m_1,...,m_t) násobení.
Potom s těmito hodnotami zacházíme jako s t vstupy a použijeme úlohu
39 pro exponenty n_1,...,n_t. Výsledkem je x^(sum_i m_i*n_i), za cenu
nejvýše

```text
l(m_1,...,m_t)+l(n_1,...,n_t)+t-1.
```

Stejné či algebraicky závislé dosazené vstupy nevadí: každý původní
formální krok zůstává platnou operací. Případná shoda hodnot cenu sníží.
To dokazuje tvrzení v zadání.

Pro silnější verzi vezměme dva řetězce a_0,...,a_r a b_0,...,b_s
a nezápornou celočíselnou matici (c_ij). Položme C=sum_ij c_ij>0.
Vytvoříme seznam C dvojic, v němž je (a_i,b_j) zopakována c_ij-krát.
Délka řetězce obsahujícího všechny první složky je nejvýše r, pro
všechny druhé složky nejvýše s. Předchozí nerovnost s t=C dává

```text
l(sum_ij c_ij*a_i*b_j) <= r+s+C-1.                          (V6)
```

Podmínka C>0 je přesně známé erratum 2022-02-22: nulová matice by
vyžadovala l(0), které v daném modelu není definováno. Není to nový nález.

## 6. Pippengerův dovětek: rozsah převzaté věty

V odpovědi 39 je navíc citován nejhorší počet operací pro matice
s omezenými položkami. Nechť M(m,p,n) je maximum L(N) přes všechny
m krát p matice s celočíselnými položkami mezi 0 a n. Položme
H=m*p*lg(n+1), v=min(m,p), w=max(m,p). Kniha uvádí

```text
M(m,p,n) = v*lg(n) + H/lg(H)
          + O(m+p+H*sqrt(lg lg H)/(lg H)^(3/2)).             (V7)
```

Jde o asymptotický zápis pro velké H, nikoli číselný vzorec při H=1.
Originál Pippengera, SICOMP 9 (1980), 230–250, byl přečten vizuálně
celý ve skenech. Hlavní věta na straně 230 dává

```text
v*lg(n) + (H/lg(H))*U(sqrt(lg lg H/lg H)) + O(w),
```

kde autor definuje U(t)=exp(O(t)). Protože t jde k nule, U(t)=1+O(t),
a to je přesně (V7), neboť w<=m+p<=2w. Omezení poměrů rozměrů
uvedená v abstraktu se týkají čistšího relativního zápisu s o(1),
nikoli této hlavní věty s O(w). V knize tedy neschází potřebná podmínka.

Dolní důkaz na 232–245 nejprve kóduje standardně seřazené výpočty.
V obtížném případě rozlišuje vektory, v nichž jedna souřadnice převáží
součet ostatních. Exponenciální růst této převahy odděluje nutná
zdvojení od kroků nesoucích informaci o matici. Dvě kódování dávají
hlavní členy v*lg(n) a H/lg(H) současně, se zbytkem ještě menším než
ve (V7). V horním důkazu 246–250 se cifry koeficientů rozloží na
obdélníkovou binární matici, jejíž rozměry se vyváží přibližně na
sqrt(H). Náklady na posuny a opětovné složení dodají člen v*lg(n).

Podstatný limit: horní důkaz na 246 přebírá z reference 6 dřívější
větu o nejmenším počtu hran grafu s předepsanými počty cest.
Tento externí výsledek zde znovu nedokazujeme. (V7) evidujeme jako
správně citovanou a z původní věty odvozenou mez, nikoli jako zcela
nezávislou reprodukci všech jejích externích předpokladů. Vlastní
úplné důkazy úloh 36/37/39/40 na (V7) nezávisejí.

## 7. Kontroly, errata a doklady

`verify_powers_vector.py` má čtyři oddělené bloky. Každý vygenerovaný
výpočet kontroluje operandové indexy a přesné celočíselné výsledky.

- `straus`: 1471 všech kladných vektorů ve vymezených malých krychlích
  a 42 dalších případů s 17, 65 a 257 bity a základy 2, 4, 8.
  Ověřena tabulková cena i konečná mez pro každou konstrukci.
- `yao`: 16384 dvojic (a,k), a=1,...,2048, k=1,...,8, a 48 výpočtů
  více cílů až do 1025 bitů. Záměrně zahrnuje opakované cíle.
  Samostatný validátor zkontroluje vzestupně seřazený skalární řetězec.
- `duality`: minima pro 136 matic a jejich transpozice spočítána
  prohledáváním množin dostupných vektorů po vrstvách. Tento výpočet
  nepoužívá grafovou dualitu. Omezit mezivýsledek na vektor nepřesahující
  po složkách alespoň jeden cíl je úplné, protože nemáme odčítání.
  Jde o 63 různých úloh po odstranění duplicit; součet 2638 návštěv
  započítává i opakovaně použitá uložená řešení. Navíc 13 skutečných
  výpočtů transponováno samostatnou grafovou konstrukcí.
- `composition`: všech 47 řetězců se zvolenými operandy délky nejvýše
  4, všech 2209 uspořádaných dvojic těchto řetězců, pro každou jednu
  deterministicky vylosovanou nenulovou matici koeficientů 0,1,2.
  Ověřen konkrétní výsledný řetězec i (V6); nejde o výčet všech matic.

Časy bloků jsou 0.222291810, 6.403495748, 0.018953347 a 1.079832418 s.
Celý obal trval 8.101999125 s, session 12714, všechny exit 0, limit
300 s na blok. PID 1575527, 1575529, 1575537 a 1575540. Žádný blok
neselhal ani nebyl opakován. Census X0065 je jiný, dosud běžící proces.

Původní sazba knihy byla vizuálně ověřena na 485, 697, 698 (začátek
odpovědi 36 na 696 byl přečten v předchozím bloku). Všech šest vrstev
errat je zahrnuto v manifestu; relevantní úplné stránkové výpisy jsou
v `sources/powers-basic-errata.txt`. Zohledněny zejména:

- 2002-01-01: Bernsteinova náhrada prvních pěti řádků odpovědi 37.
- 2002-01-31: mírnější popis Pippengerova rozšíření v odpovědi 39.
- 2022-08-14: libovolné, případně opakované cíle v úloze 37 a odpovědi
  39; oprava rozsahu Knuthovy citace na 2–4.
- 2022-02-22: nenulová matice v silnější verzi odpovědi 40.
- Ve druhém vydání 1981-06-15: doplnění citace Olivosova článku.

Primární soubory a přístupové neúspěchy jsou v
`sources/powers-vector-source-access.json`; integritu všech dokladů
zaznamenává `sources/powers-vector.json`. Yaoovo PDF pochází z autorova
univerzitního webu, skeny ostatních článků z Bernsteinova archivu.
Vydavatelský PDF přístup pro Olivose vracel 403 a JSTOR pro Strause
420; následně získané původní skeny pokrývají celé relevantní články.
Bibliografické stránky nejsou počítány jako přečtení originálu.
Fyzický výtisk, prvenství případného hlášení ani novější dotisk jsme
neověřovali. Žádné hlášení nebylo odesláno.

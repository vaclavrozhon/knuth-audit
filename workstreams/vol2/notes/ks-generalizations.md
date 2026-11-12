# §3.3.1-19,21,22: zobecnění KS testu

Kontrola 1. listopadu 2026, třetí vydání/první tisk (1997), zadání na
[str. 60](../images/vol2-p060.png), vážená statistika v odpovědi 6 na
[str. 559](../images/vol2-p559.png). Jde o výzkumné úlohy bez hotových
odpovědí. Níže jsou vlastní konstrukce, přesné příklady a konečné
experimenty. Uzavření auditu těchto úloh neznamená úplné vyřešení všech
možných zobecnění ani optimálnost navržených testů.

Základní pojmy: distribuční funkce F udává pravděpodobnost pozorování
nejvýše daný práh; empirická funkce F_n je příslušný podíl v n nezávislých
pozorováních. Nulová hypotéza říká, že pozorování mají právě distribuci F.
Hladina alpha je pravděpodobnost nesprávného zamítnutí této hypotézy.
Síla testu při jiné distribuci G je pravděpodobnost, že ji test odhalí.
Všude níže F známe předem; nezískáváme její parametry z testovaných dat.

Výpočty: [verify_ks_extensions.py](../verify_ks_extensions.py),
[úplné výsledky](../results/ks-extensions.json). Všechny části dokončeny
s kódem 0. Matematické důkazy nejsou nahrazeny simulací.

## 1. Úloha 19: několik souřadnic

Pro vektor X=(X_1,...,X_r) je
`F(x)=Pr(X_1<=x_1,...,X_r<=x_r)`. Oblast určenou všemi těmito
nerovnostmi nazýváme dolní ortant. F_n(x) je podíl pozorovaných vektorů
v tomto ortantu. Přirozené statistiky jsou

```
D+ = sup_x (F_n(x)-F(x)),
D- = sup_x (F(x)-F_n(x)),
D  = max(D+,D-).
```

### 1.1 Proč nelze převzít jednorozměrnou tabulku

Již pro n=1 platí `D+=1-F(X)`: uvnitř ortantu s vrcholem X je F_n=1
a nejmenší hodnota F právě F(X); mimo něj je rozdíl nekladný.

V jedné dimenzi je F(X) rovnoměrné pro každou spojitou F. Ve dvou
dimenzích to neplatí. Například pro nezávislá rovnoměrná U,V je
`F(U,V)=UV`, zatímco pro (U,U) se stejnými okrajovými distribucemi je
`F(U,U)=U`. V obou případech je společná distribuční funkce spojitá,
ale distribuce D+ jsou různé.

Rozdíl není způsoben jen koncentrací druhého příkladu na přímce. Pro
`-1<theta<1` definujme na jednotkovém čtverci

```
F_theta(u,v) = uv[1+theta(1-u)(1-v)],
f_theta(u,v) = 1+theta(1-2u)(1-2v).
```

Malé f značí hustotu, tedy smíšenou derivaci F. Je všude kladná,
integruje se na 1 a obě okrajová rozdělení jsou rovnoměrná. Přesto

```
E[D+] = integral integral (1-F_theta) f_theta du dv
      = 3/4-theta/18.
```

Integrál je elementární a byl navíc přesně ověřen symbolicky. Ani mezi
všude kladnými hustotami se stejnými okraji tedy neexistuje jediná
knižní KS tabulka. Empirická kovariance vysvětluje závislost na F:

```
Cov(F_n(x),F_n(y)) = [F(min(x,y))-F(x)F(y)]/n,
```

kde minimum bereme po souřadnicích. Je to kovariance dvou indikátorů
příslušných ortantů, dělená n.

### 1.2 Jedna platná a konzistentní konstrukce

Předpokládejme spojité okrajové distribuční funkce. V každé souřadnici
zvolme m kvantilových intervalů s pravděpodobností 1/m, včetně nekonečných
krajů. Jejich kartézský součin dává mřížku s nejvýše L=(m+1)^r vrcholy.
Označme `D_grid=max_z |F_n(z)-F(z)|` přes tyto vrcholy.

Pro libovolný x existují sousední vrcholy a<=x<=b. Monotonie F_n a F
a sjednocení r okrajových proužků dávají

```
F(b)-F(a) <= r/m,
D_grid <= D <= D_grid+r/m.                          (G1)
```

Pro pevný vrchol z je nF_n(z) binomická veličina. Její centrovaná
vytvářející funkce splňuje
`E exp(lambda*(I-EI)) <= exp(lambda^2/8)` pro indikátor I. Například
logaritmus levé strany má druhou derivaci rovnou rozptylu exponenciálně
nakloněného Bernoulliho rozdělení, nejvýše 1/4; hodnotu i první derivaci
v nule má nula. Dvojí integrace tuto nerovnost dokáže. Nezávislost,
Markovova nerovnost a volba lambda=4*epsilon potom dávají

```
Pr(|F_n(z)-F(z)| > epsilon) <= 2 exp(-2n*epsilon^2).
```

Sjednocení přes vrcholy a (G1) tedy dokazuje

```
Pr(D > r/m + sqrt(log(2L/alpha)/(2n))) <= alpha.     (G2)
```

To je explicitně kalibrovaný vícerozměrný test. Nevyžaduje nezávislost
souřadnic uvnitř jednoho vektoru, jen nezávislost n vektorů.
Pro m=n a pevné r klesá práh k nule. Pokud G není F, existuje pevný bod
s rozdílem delta>0; zákon velkých čísel v tomto bodě zaručí zamítnutí
s pravděpodobností jdoucí k jedné. Test je tedy konzistentní.

Naivní vyhodnocení mřížky může stát O(nLr) operací, takže tento důkaz
není tvrzením o praktické efektivitě ve velké dimenzi. Přímé použití
D_grid se prahem bez r/m je také platný test; s rostoucí mřížkou je
konzistentní stejným argumentem. Konstrukce je jedno konkrétní řešení
výzvy „develop tests“, nikoli prohlášení o nejlepším možném testu.

## 2. Úloha 21: distribuční funkce se skoky

### 2.1 Správná statistika a její přesná distribuce

Nechť podpora obsahuje uspořádané body a_1<...<a_k, s kladnými
pravděpodobnostmi p_j. Napišme `P_j=p_1+...+p_j` a `C_j=Y_1+...+Y_j`,
kde Y_j je počet pozorování a_j. Z definice suprema přímo plyne

```
D+ = max_(0<=j<=k) (C_j/n-P_j),
D- = max_(0<=j<=k) (P_j-C_j/n),
```

s C_0=P_0=0. Mezi body podpory jsou obě funkce konstantní. Rozdělení
vektoru počtů je multinomické:

```
Pr(Y=y) = n!/(y_1!...y_k!) * product_j p_j^y_j,
```

kde y_j jsou nezáporná celá čísla se součtem n. Konečný součet tohoto
vzorce přes všechny přípustné počty přesně kalibruje libovolný z testů.

Spojitý vzorec s levými limity F(X_j) nelze slepě přenést: pro rozdělení
s jediným atomem je skutečně F_n=F, tedy D+=D-=0, zatímco spojitý vzorec
pro D- by dosadil F(X_j)=1 a nesprávně dal D-=1. Kniha kontinuitu
výslovně požaduje; není to její přehlédnutá chyba.

Pro dva atomy s první pravděpodobností p a n=1 má D+ hodnoty 1-p a 0
s pravděpodobnostmi p a 1-p; D- má hodnoty 0 a p s týmiž pravděpodobnostmi.
Zde obecně neplatí ani rovnost rozdělení obou znamének. Oboustranná
statistika pro libovolné n je `D=|Y_1/n-p|`. Pearsonova statistika je
`V=nD^2/[p(1-p)]`, takže při přesné kalibraci mají oba oboustranné testy
stejné pořadí výsledků a stejnou sílu.

### 2.2 Co se stane při použití spojité tabulky

Jestliže při hodnotě a_j přidáme nezávislé rovnoměrné číslo V z [0,1],
transformace `U=P_(j-1)+p_j*V` je rovnoměrná v [0,1]. Empirické
odchylky původního diskrétního výběru odpovídají odchylkám tohoto
rovnoměrného výběru pouze v bodech P_j. Proto po této vazbě

```
D+_discrete <= D+_continuous,
D-_discrete <= D-_continuous.
```

Použití pouze horních kritických hodnot ze spojitého rozdělení tedy
vede ke konzervativnímu testu. Použití i dolního kritického ocasu,
jaké kniha připouští při zkoušení generátorů, takovou záruku nemá:
u jediného atomu je výsledek vždy nula. Pro rozdělení se skoky je třeba
počítat jeho skutečné nulové rozdělení nebo použít uvedenou randomizaci.

### 2.3 Přesná srovnání s chí-kvadrát

Testovaná nulová distribuce je p=(1/4,1/4,1/4,1/4). Porovnáváme
oboustranný D s Pearsonovým V. Aby nestejně velké skoky distribucí
nezkreslily srovnání, oba testy kalibrujeme na přesně alpha=0.05:
zamítáme vždy nad kritickou hodnotou a na kritické hodnotě s vypočtenou
pravděpodobností gamma. Gamma je podíl zbývajícího povoleného ocasu
ku hmotnosti tohoto atomu. V JSON jsou její přesné racionální hodnoty.

Alternativa „posun“ má pravděpodobnosti (0.35,0.35,0.15,0.15);
„střídání“ má (0.35,0.15,0.35,0.15). Pearsonova statistika nerozlišuje
permutaci kategorií, kumulativní odchylka KS ano.

| n | Alternativa | Síla KS | Síla Pearsonova testu |
|---:|---|---:|---:|
| 20 | posun | 0.384170 | 0.291300 |
| 20 | střídání | 0.136533 | 0.291300 |
| 60 | posun | 0.857562 | 0.765908 |
| 60 | střídání | 0.396450 | 0.765908 |

Všechna čísla jsou zaokrouhlení přesných racionálních součtů, nikoli
Monte Carlo odhady. Enumerováno 1771 konfigurací počtů při n=20 a
39711 při n=60, pro každou tři distribuce. Součty hmotností jsou přesně
jedna; za nulové hypotézy vychází E[V]=3 a skutečné hladiny obou testů
přesně 0.05. Nezávislý model prošel všech 726 uspořádaných slov pro
n=1,...,5 na třech symbolech ve dvou pravděpodobnostních modelech
 a porovnal celé histogramy statistik s multinomickou enumerací.
Tyto malé kontroly ověřují způsob sčítání, ne všechny velké případy
samostatnou enumerací slov.

Navíc je uloženo 18 konkrétních reprodukovatelných náhodných výběrů:
pro každé n a každou distribuci tři výběry, seed 20261101. JSON uvádí
počty, obě statistiky a přesné horní ocasové pravděpodobnosti. Výběry
jsou ilustrace; závěr o síle vychází z úplných součtů. Potvrzují smysl
příkladu v textu na str. 53: kumulativní a střídavé odchylky se chovají
jinak a žádný z obou testů není ve všech situacích lepší.

## 3. Úloha 22: odchylka dělená místní směrodatnou odchylkou

### 3.1 Definice a výpočet

Po transformaci spojitou F máme opět nezávislá rovnoměrná pozorování.
Definujme novou statistiku

```
W+ = sqrt(n) sup_(0<u<1) (F_n(u)-u)/sqrt(u(1-u)).
```

Jmenovatel standardizuje rozptyl v každém pevném bodě. V krajních bodech
0 a 1 je nula, proto supremum bereme přes otevřený interval. To je
přirozené upřesnění návrhu v odpovědi 6, nikoli použití původní KS tabulky.
Statistika W- má opačné znaménko v čitateli.

Pro pevné a z [0,1] je funkce `g_a(u)=(a-u)/sqrt(u(1-u))` klesající:

```
g_a'(u) = -[a+(1-2a)u]/[2(u(1-u))^(3/2)] < 0
```

pro 0<u<1. Proto W+ stačí počítat po skocích F_n, W- před nimi.
Pro seřazená u_j tak dostaneme maxima známých n výrazů. Zrcadlení
u_j na 1-u_(n+1-j) opět prohodí znaménka a zachová distribuci.

Pro s>0 položme lambda=s/sqrt(n) a a_j=j/n. Nerovnost W+<=s je
právě soustava u_j>=b_j, kde

```
b_j = [2a_j+lambda^2
       -lambda*sqrt(lambda^2+4a_j(1-a_j))]/[2(1+lambda^2)].    (G3)
```

Kořen leží v (0,a_j]; pochází z rovnice
`a_j-u=lambda*sqrt(u(1-u))`, takže při umocnění nebyla vybrána nesprávná
větev. Meze b_j jsou rostoucí: g_a roste v parametru a a klesá v u.
Distribuční funkce W+ je n!-násobek objemu uspořádaného simplexu
s těmito dolními mezemi. Tím je test přesně určen i pro konečné n.

Dvě implementace se nezávisle shodují na 24 případech n=1,2,3,5,10,20
 a s=1/4,1,2,5: přímá integrace polynomů versus nezáporná rekurence
podmíněných binomických počtů. Ve druhém modelu při hranici b_j nesmí
počet bodů vlevo překročit j-1. Přechod z hranice b_(j-1) používá
binomickou pravděpodobnost s parametrem
`(b_j-b_(j-1))/(1-b_(j-1))`. Počítáno při 90 desetinných místech,
shoda vyžadována do 10^-65. Tento rozsah není tvrzením o stabilitě
polynomické implementace pro libovolně velké n.

### 3.2 Krajní chování a kalibrace

Pro n=1 je `W+=sqrt((1-U)/U)`, tedy

```
Pr(W+<=s) = s^2/(1+s^2),   s>=0.
```

Na rozdíl od obyčejné KS statistiky je W+ neomezená a má nekonečný
druhý moment: integrál `integral_0^infinity 2s/(1+s^2) ds` diverguje.
Standardizace jednotlivých bodů tedy nedělá ze suprema standardní
normální ani obyčejnou KS veličinu.

Kontrolované 95% kvantily jsou

| n | Kvantil W+ |
|---:|---:|
| 1 | 4.358898943540674 = sqrt(19) |
| 5 | 4.611264189886427 |
| 20 | 4.692356684626446 |

Každý numerický kořen binomické rekurence byl ověřen druhým,
integrálním modelem. Již n=1 ukazuje zásadní rozdíl od tabulky 2.

### 3.3 „Lepší“ neznamená lepší pro každou alternativu

Pro n=20 jsme zvolili vlastní přesné 95% kvantily obou jednostranných
testů. Je-li skutečná distribuční funkce G spojitá, podmínku u_j>=b_j
převedeme na rovnoměrná pořadová pozorování s mezemi G(b_j). Oba výpočetní
modely tak nezávisle dávají následující síly:

| Skutečná distribuce G(u) | Obyčejné K+ | Vážené W+ |
|---|---:|---:|
| u, nulová hypotéza | 0.050000 | 0.050000 |
| u^0.8 | 0.196160 | 0.185719 |
| 0.95u+0.05 min(1000u,1) | 0.095744 | 0.659438 |

Poslední alternativa znamená pětiprocentní příměs rovnoměrných čísel
z [0,0.001]. Vážený test výrazně pomáhá u takové odchylky v ocasu,
ale u rozptýlené změny u^0.8 byl v tomto příkladu slabší. Výsledky jsou
vyhodnocení konečných integrálů, nikoli náhodný odhad síly.

### 3.4 Primární literatura a hranice rešerše

Přečteno §2, §5 a dodatek A.2 článku A. Moscovich, B. Nadler,
C. Spiegelman, *On the exact Berk-Jones statistics and their p-value
calculation*, Electronic Journal of Statistics 10 (2016), 2329–2354,
[autorská kopie](https://www.wisdom.weizmann.ac.il/~nadler/Publications/Exact_Berk_Jones_EJS_2016.pdf).
V §2 je stejná váha ve statistice Higher Criticism s parametrem alpha_0=1;
§5 používá objemy uspořádaných rovnoměrných pozorování. Náš důkaz (G3)
a binomická rekurence jsou uvedeny samostatně výše.

Dodatek A.2 pečlivě rozlišuje jmenovatele sqrt(F(1-F)) a
sqrt(F_n(1-F_n)). Nezaměňujeme tyto dvě statistiky ani nepřenášíme
asymptotickou větu z jednoho jmenovatele automaticky na druhý.
Odkazy na původní práce Eickera a Jaeschkeho (1979) byly bibliograficky
nalezeny, ale dostupné adresy Project Euclid vracely HTML místo PDF;
jejich úplné důkazy tedy nejsou zde vydávány za přečtené. Pro tuto
úlohu máme vlastní konečnou kalibraci a konkrétní srovnání síly.

Nebylo nalezeno nové erratum: kniha návrh výslovně předkládá jako
výzkumnou otázku. Všechny čtyři vrstvy errat byly kontrolovány společně
s ostatními úlohami §3.3.1.

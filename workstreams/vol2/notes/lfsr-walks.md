# §3.3.2-31–33,35: procházky z lineárních binárních rekurencí

Uzavřený matematický blok1.11.2026; původní strany79–80 a570–572
vizuálně přečteny. LFSR znamená posuvný registr s lineární
zpětnou vazbou: nový bit je součet vybraných starších bitů
modulo2, tedy jejich XOR. Maximální perioda délky2^k−1 zde
znamená, že rekurence stupně k projde právě všechny nenulové
k-bitové stavy; všechny počáteční fáze jsou stejně pravděpodobné.
Primitivitu55/24 jsme již ověřili v auditu §3.2.2 a neopakujeme ji.

## 1. Přesné rozdělení pro31

U rekurence Y_j=Y_(j−24) XOR Y_(j−55) je prvních79 bitů
rozděleno na24 disjunktních trojic
(Y_i,Y_(i+31),Y_(i+55)), i0..23, a7 zbývajících bitů24..30.
V každé trojici je poslední bit XOR prvních dvou; z jejích
čtyř stejně pravděpodobných vstupů jeden dává nula jedniček
a tři dávají dvě. Před vyloučením nulového stavu jsou bloky
nezávislé. Generující funkce počtu jedniček W je proto

```text
F(z)=((1+z)/2)^7 ((1+3z²)/4)^24.
```

Přesné podmínění na nenulový stav mění funkci na
(2^55 F(z)−1)/(2^55−1). Celkový počet stavů s W>=40 je
18509401282464000, což dává pravděpodobnost
0.5137390868954483523..., v souladu s knihou.

Po86 bitech máme17 původních trojic a7 komponent o třech
nezávislých vstupech A,B,C. Pět výstupních bitů jedné komponenty
je A,B,C,A XOR B,C XOR A XOR B. Její váhový polynom je
1+2z²+4z³+z^4, což dává vytištěný faktor dělený8.
Následující dva faktory se jmenovateli32 a128 vzniknou
spojováním komponent. Program vytváří lineární formy všech
výstupů v55 počátečních bitech, spojí překrývající se podpory
a vyčerpá všechny vstupy každé komponenty. Potvrzuje oba
vytištěné polynomy včetně všech koeficientů:

```text
1+2z²+5z³+5z^4+10z^5+8z^6+z^7,
1+2z²+7z³+7z^4+15z^5+25z^6+29z^7+28z^8+13z^9+z^10.
```

Rozklad na disjunktní trojice platí obecně pro prvních k+l
bitů s k>2l. Přímá rekurence nad7512 počátečními stavy ve20
malých modelech souhlasí s nezávislou binomickou konvolucí.

Výběr každého druhého bitu splňuje tutéž rekurenci: umocnění
charakteristické identity v tělese dvou prvků zdvojnásobí
indexy bez smíšených členů. Navíc gcd(2,2^k−1)=1, takže tento
výběr permutuje všechny fáze. Rozdělení každého konečného
okna je proto stejné, nikoli pouze přibližné.

Nejnižší bity aditivního generátoru se řídí stejnou XOR
rekurencí. U multiplikativního55/24 s lichými vstupy napišme
X=1+2b modulo4; součin dává b_new=b_old+b_lag modulo2.
To potvrzuje i tvrzení o druhých nejnižších bitech v zadání.

## 2. Úloha32: převaha jedniček versus záporný třetí moment

Původní tříbodový protipříklad je správný. Pro epsilon1/10
jsou hodnoty X rovny−51/50,2/25,4/5 s pravděpodobnostmi
2/5,1/10,1/2. Jejich průměr je0, Pr(X>0)=3/5 a pro nezávislé
kopie Pr(X+Y>0)=9/25. Obecně při0<epsilon<(sqrt(2)−1)/2
jsou všechny součty s prvním záporným bodem záporné,
zbývající kladné; dává to vytištěné(1/2+epsilon)²<1/2.

Zjednodušená odpověď z29.3.2005 je také správná. Hodnoty−b,a
s pravděpodobnostmi a/(a+b),b/(a+b), kde a<b<(1+sqrt(2))a,
mají nulový průměr a kladný výsledek častěji než záporný.
Součet je kladný pouze při dvou kladných hodnotách, s
pravděpodobností(b/(a+b))²<1/2. Konkrétní a2,b3 dává stejné
3/5 a9/25. Golfová interpretace vyžaduje nezávislé výsledky kol. Obě
původní strany Coverova článku277–278 byly vizuálně přečteny;
obsahují obdobné obrácení pravděpodobnosti při dvou kolech
a rozlišení střední hodnoty od šance na vítězství.
Také originál errata2005 na straně32 byl přečten.

## 3. Vlastní uniformní asymptotický důkaz33

Položme a=k−2l>=1, b=l>=0, L=a+3b=k+l. Nechť S=2W−L
je součet znamének, kladný právě při převaze jedniček. Před
vyloučením nulového stavu je S součtem a nezávislých znamének
±1 s pravděpodobnostmi1/2,1/2 a b nezávislých veličin
−3,+1 s pravděpodobnostmi1/4,3/4. Má střední hodnotu0,
rozptyl L a třetí kumulant, zde stejný jako třetí moment,−6b.

Charakteristická funkce phi(t)=E exp(itS), tedy Fourierův
obraz pravděpodobnostního rozdělení, je

```text
phi(t)=cos(t)^a (cos(t)^3+i sin(t)^3)^b.
```

Pro celočíselné S parity L dávají konečné trigonometrické
součty přesnou identitu

```text
Pr(S>0)+(1/2)Pr(S=0)
 = 1/2+(1/pi) integral_0^(pi/2) Im(phi(t)) K_L(t) dt,
K_L(t)=1/sin(t) pro liché L; K_L(t)=cot(t) pro sudé L.
```

Ověření identity pro jednotlivé nenulové celé s: integrál
sin(st)/sin(t) pro liché s a sin(st)cot(t) pro sudé s je
(pi/2)sign(s). Poté stačí vzít očekávání konečné distribuce.

Blízko t=0 platí rovnoměrně v a,b, a+3b=L,

```text
log phi(t)=−Lt²/2+i b t³+O(Lt^4)+i O(b t^5),
K_L(t)=1/t+O(t).
```

Na0<=t<=L^(-2/5) tedy imaginární část má tvar
exp(−Lt²/2)[b t³+O(b t^5+Lb t^7+b³t^9)]. Integrací po
vynásobení K_L dostáváme hlavní člen

```text
(b/pi) integral_0^infinity t² exp(−Lt²/2) dt
 = b/(sqrt(2pi)L^(3/2))
```

a chybu O(L^(-3/2)), protože b<=L/3. Střední část intervalu
je exponenciálně malá: |phi|=|cos t|^a
(1−3sin²t cos²t)^(b/2) a vzdálenost od obou konců je kladná.
Mezi L^(-2/5) a pevným malým okolím0 dává stejný argument
mez exp(−c L^(1/5)).

Druhý konec t=pi/2 nelze automaticky zahodit, když a zůstává
malé. Položme u=pi/2−t. Pokud b<L/6, máme a>L/2 a příspěvek
je exponenciálně malý. Jinak b je řádu L a pro a>=2 je
amplituda nejvýše C u² exp(−c b u²), jejíž integrál je
O(L^(-3/2)). Pro a=1 zbývají dvě parity: při lichém b je L
sudé a cot(t)=O(u) dodá druhý faktor u. Při sudém b je i^b
reálné, takže imaginární část začne až členem O(bu³);
celý integrál je O(b integral u^4 exp(−cbu²)du)=O(L^(-3/2)).
Tím je dokázáno rovnoměrně

```text
Pr(S>0)+(1/2)Pr(S=0)
 = 1/2+b/(sqrt(2pi)L^(3/2))+O(L^(-3/2)).
```

Pro sudé L je centrální pravděpodobnost
(2/pi)integral_0^(pi/2)Re(phi(t))dt. U0 je rozvoj
exp(−Lt²/2)[1+O(Lt^4+b²t^6)]. U druhého konce platí
předchozí meze; v jediném zbývajícím případě a1,b liché je
i^b ryze imaginární, takže reálná část opět začíná b u³.
Proto

```text
Pr(S=0)=sqrt(2/(pi L))+O(L^(-3/2))  pro sudé L.
```

Pro striktní převahu jedniček se odečte polovina tohoto
výrazu. Vyloučení nulového stavu mění pravděpodobnosti nejvýše
O(2^(−k)), což se vejde do uvedené chyby, neboť L<3k/2.
To potvrzuje oba hlavní závěry knihy. Chyby pomocných výrazů
a znaménko v argumentu posledního O jsou evidovány v C0031.
Osmnáct přesných binomických součtů do k1000 ověřuje číselnou
shodu; tyto příklady nejsou náhradou obecného důkazu.

## 4. Obecné momenty v35

Všechny výstupní bity jsou nenulové lineární funkce počátečního
stavu vektorového prostoru F_2^k. Následující součty vždy
běží přes N=2^k−1 nenulových stavů. Pro nenulovou lineární
funkci f platí sum(−1)^f=−1: nad všemi2^k stavy je součet0,
nulový stav přispívá1. Proto sum Z_i=1 a při různých pozicích
i,j v okně délky m<=N také sum Z_i Z_j=−1. Odtud

```text
E S_m=m/N,
E S_m²=m−m(m−1)/N,
Var(S_m)=m−m(m−1)/N−m²/N².
```

Pro nezávislá symetrická znaménka jsou příslušné hodnoty0,m,m.
Relativní rozdíl rozptylu je malý při m/N malém. Změna2024
jen slovně rozepisuje tento předpoklad. Ve vytištěném rozvoji
nezávislého druhého momentu na572(c) chybí faktor2 před
smíšeným součtem; všechny jeho členy jsou zde0, takže rovnost
v daném nulově středovaném modelu i závěr zůstávají správné.

Pro tři pozice je Z_h Z_i Z_j=−(−1)^(f_h+f_i+f_j).
Součet přes fáze je1, pokud je výsledná forma nenulová, a−N,
pokud je nulová. Při opakovaných indexech zůstává nenulová.
Je-li B počet neuspořádaných trojic různých indexů v okně
s nulovou formou, rozvinutí všech m³ uspořádaných součinů dává

```text
E S_m³=[m³−6B(N+1)]/N.
```

Trojice lze posunout tak, aby první index byl0. Trojice
(0,i,j) má v okně m−j posunů. V tělesové reprezentaci
Y_t=f(xi^t), kde xi je kořen primitivního charakteristického
polynomu, se nulovost rovná1+xi^i+xi^j=0. Těleso je zde
k-rozměrný prostor nad F_2. Zobrazení
x -> (f(x),f(xi x),...,f(xi^(k−1)x)) je prosté: nenulový
stav nemůže dát k nulových výstupů. Počáteční stav1,0,...,0
proto ztotožňuje prvek1 s tímto souřadnicovým vektorem.
Pro i!=j je1+xi^i=xi^j právě tehdy, když posledních k−1
souřadnic souhlasí; první se pak musejí lišit. To dokazuje
přesně vytištěnou definici B pomocí úseků Y_(i+1)..Y_(i+k−1).

Nezávislý přímý průchod všech51 primitivních rekurencí stupňů
2–8 kontroluje6977 délek oken a všechny tři momenty.
Pro55/24 souhlasí dvě reprezentace: projekce konkrétního stavu
a XOR lineárních forem. První dvě dvojice jsou(31,55),(62,110).
Pro m79 je B=24; třetí moment je
−5188146770730318353/36028797018963967≈−144. Stejná hodnota
vychází nezávisle z váhového polynomu v části1. Chybějící
jmenovatel v jednom řádku odpovědi je C0029; zadání je správné.

## 5. Obrázek a delší procházky

Úplný průchod periody2047 pro11/2 dává pro každou délku okna
přesný počet kladných výsledků i remíz. Při délce445 je
1306/2047=0.638007... kladných, což zaokrouhleně dává64%.
[Rekonstrukce obrázku](../results/lfsr-walk-curve.svg) používá
liché délky, aby nepletla tvar s oscilací způsobenou remízami;
tvar odpovídá původnímu obrázku570. Všech2047 délek je v JSON,
včetně úplné periody, kde je součet vždy1.

Vlastní experimenty používají200000 pevně reprodukovatelných
počátečních stavů odvozených ze SHAKE256. Nejde o historická
semena ani důkaz nezávislosti kryptografického proudu.

|Počet bitů|Podíl převahy jedniček,55/24|
|---|---:|
|79|0.514505|
|101|0.519080|
|1001|0.537250|
|10001|0.523700|
|1001, pouze55 bitů z každé dávky165|0.498910|

Binomická směrodatná chyba pod nulovým modelem je přibližně
0.001118. Výsledky podporují tvrzení o dlouhých procházkách
i zlepšení při vynechávání dávek, ale nedokazují platnost
pro všechna okna. Ještě dva experimenty s mod4 aditivní a
subtraktivní rekurencí sledují79 **sudých hodnot** a jejich
druhý nejnižší bit: podíly jsou0.514045 a0.514905. To podporuje
samostatnou poznámku o podposloupnosti vybrané podle parity;
nezaměňovat tento výběr s každým druhým časovým indexem.

Zdrojové řetězce, pořadí bajtů a hashe počátečních stavů jsou
v `results/*walk-experiment-seeds.json`; C++ program je
`experiment_empirical_tail.cpp`. Přesné kontroly a obrázek
vytváří `verify_lfsr_walks.py`, výsledky jsou uloženy průběžně.
Příslušné pasáže Vattulainen1994 byly přečteny; publikovaný
dvourozměrný test se od zdejší jednorozměrné varianty liší.
Matsumoto–Kurita1992/1994 potvrzují popsané selhání testů
váhy i při velkých stupních,1996 uvádí dlouhé úseky nízké
hustoty poblíž pevného vektoru. Příslušné pasáže autorských
preprintů byly přečteny; jejich úplné testy se neopakovaly.
Lindholm1968 byl ověřen jako bibliografická citace z metadat
vydavatele; obecný důkaz momentů výše je vlastní.
Přesný rozsah zdrojů je v `sources/empirical-tail-bibliography.json`.

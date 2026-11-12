# §3.4.1: konečné volby a základní transformace

Stav 2026-11-01. Vizuálně přečteny strany119–122,138–142,584–587.
Sekce má33 původních úloh, poslední je na str.142; původní konec141
v pracovním inventáři byl opraven. Tento blok uzavírá A/B a úlohy1–9,
13–15. Polární metoda a ostatní normální metody pokračují v dalším bloku.
Výpočet: `verify_distributions_basic.py`, výsledky
`results/distributions-basic.json`; konečné testy doplňují obecné důkazy.

## 1. Konečná přesnost, MIX a úlohy1–3

Nechť J je rovnoměrné celé číslo v {0,...,m−1}, U=J/m a k je kladné celé
číslo. Vynásobení J*k dává horní slovo floor(J*k/m), dolní slovo jeho
zbytek modulo m. Tím souhlasí význam registrů A/X po LDA/MUL na str.119–120;
celé k se vejde do slova. Pro 0<=r<k platí přesně

```
Pr(floor(kU)=r) = (ceil(m(r+1)/k)−ceil(mr/k))/m.
```

Rozdíl od1/k je rozdíl dvou čísel v [0,1), dělený m, tedy má absolutní
hodnotu menší než1/m a relativní chybu menší než k/m. Toto platí i k>m
v matematickém modelu; většina výsledků pak má nulovou pravděpodobnost.
Úloha1: pro alpha<beta transformace alpha+(beta−alpha)U posílá délky
intervalů na jejich délku dělenou beta−alpha.

Pro zbytek R=J mod k napišme m=qk+s, 0<=s<k. Hodnoty r<s mají q+1
vzorů, ostatní q. Podmínění na J<qk odstraní přebytek a dá přesně
rovnoměrné rozdělení, pokud q>=1. Oprava `>` na `>=` v odmítacím testu
je známá: all2-prepre,20.8.2001,str.584. Úprava zadání „dividing“ na
„computing its remainder“ je známá7.2.2000.

**C0052:** číselný příklad v odpovědi3 má nesprávný poměr. Položme
h=ceil(k/2), počet celých r s r<k/2. Potom

```
Pr(R<k/2) = (q*h+min(s,h))/m.                       (1)
```

Při m=3k a sudém k je to1/2, nikoli přibližně2/3. Pro skutečnou
binární velikost slova m=256 a k=86 je to129/256. Když m roste a
k/m->1/3, jde (1) k1/2. Tištěné „k≈m/3“ lze opravit na „k≈2m/3“;
při m=3k/2 a sudém k je (1) přesně2/3. Například m12,k8.

Varování o krátkých nízkých bitech LCG je správné v uvedeném příkladu:
pro sudé m se parita řídí afinním zobrazením dvou stavů a má periodu
nejvýše2. Obecné doporučení nesdílet dělitele s m se týká takových
nízkých složek; nevyvozujeme z něj univerzální horní mez celé posloupnosti
zbytků pro libovolné částečně společné dělitele. Rychlost DIV versus MUL
je dobový komentář, nikoli tvrzení o všech dnešních procesorech.

Přímé počítání všech J ověřilo20480 dvojic m<=128,k<=160 a1648640
jednotlivých pravděpodobností, včetně přijetí po správném odmítání.

## 2. Aliasy a úlohy7,8

Aliasová tabulka rozděluje jednotkový interval na k sloupců stejné
šířky. Ve sloupci i se s podílem P_i vybere vlastní výsledek x_(i+1),
s podílem1−P_i náhradní výsledek Y_i. Pro ideální spojité U jsou
K=floor(kU) a V=kU−K nezávislé: událost K=i,V<v má pravděpodobnost v/k.
U konečné m-bodové mřížky nezávislost obecně neplatí; úvod tuto
idealizaci výslovně stanovuje a konečnou chybu výše odděluje.

Pro konstrukci udržujeme n zbývajících vah q_i se součtem n/k.
Pokud n>1, existují různé nejmenší a největší indexy i,j s
q_i<=1/k<=q_j. Sloupec i dostane hmotnost q_i vlastní barvy a
1/k−q_i barvy j. Všechny váhy zůstanou nezáporné a po odebrání sloupce
je součet (n−1)/k. Indukce končí jedinou vahou1/k. Funguje pro libovolné
reálné pravděpodobnosti, včetně nul. Celočíselné kostky v zadání jsou
tentýž argument po změně měřítka. Barva s původní vahou<1/k nemůže
být dárcem, protože váhy pouze klesají.

Na posledním kroku nastavíme P=1; Y je nepoužité. Doslovný popis knihy
pak ještě zbytečně maže/vkládá tentýž poslední pár. Protože všechna
výstupní P/Y už jsou správná a smyčka ihned končí, neklasifikujeme to
jako chybný výsledek. Implementace tento zbytečný krok vynechává.

Přímý nezávislý součet hmotností jednotlivých větví ověřil31816
racionálních rozdělení, všechna složení součtů1–10 do1–7 složek.
Všech16 položek tabulky121 odpovídá36 stejně pravděpodobným dvojicím
kostek. Čtyři hvězdičky Y jsou nepoužité, protože P=1.

Úloha8: V<P_i právě když U<(i+P_i)/k při K=i. Nová mez tedy je
(i+P_i)/k. Ověřeno567028 racionálními sondami, včetně mezí0,1 a rovnosti.

Známé erratum4.10.1999 mění „absolute minimum“ na „absolute maximum“.
Obtížnost maximalizace lze doložit přímo balením: mějme3m čísel a_i
se součtem mB a B/4<a_i<B/2. Zvolme k=4m barev a hmotnosti měřené
v jednotkách jednoho sloupce: m velkých barev váhy2 a3m malých vah
1−a_i/B. Největší možný součet vlastních podílů je3m. Dosáhneme jej
právě tehdy, když lze deficity a_i/B rozdělit mezi m dárců s kapacitou1.
Každý musí dostat právě tři položky. To je přesně původní úloha rozdělit
a_i do trojic součtu B. Greedy konstrukce slibuje pokus o maximalizaci,
nikoli globální optimum; tomu text po známé opravě odpovídá.

Dynamické váhy: [primární článek Matias–Vitter–Ni](https://theory.stanford.edu/~matias/papers/MVN03.dynamic_rv_gen.pdf),
věta8 na str.16, výslovně uvádí konstantní očekávaný čas obou operací.
Autorský katalog spojuje tuto práci se SODA1993,361–370. Čten byl
indexovaný abstrakt, věta a obrys konstrukce tabulek; plný důkaz jsme
nezávisle nereprodukovali. Přímý PDF download selhal, metadata a rozsah
jsou v `sources/matias-vitter-ni-2003.json`. Starší dvouautorský report1992
s log-star mezemi není důvod zpochybňovat pozdější společný výsledek.

## 3. Inverze, maxima, směsi; úlohy4–6

Distribuční funkce F(x)=Pr(X<=x) je neklesající a má limity0,1.
Pro spojitou přísně rostoucí F a0<U<1 platí
Pr(F^(-1)(U)<=x)=Pr(U<=F(x))=F(x). Hodnoty na nulové krajní události
je nutné při strojové implementaci ošetřit podle konkrétní distribuce.

Nezávislost X1,X2 dává
Pr(max(X1,X2)<=x)=F1(x)F2(x). Komplement události min<=x je
{X1>x,X2>x}; proto minimum má CDF F1+F2−F1F2. Tento důkaz funguje
i s atomy. Pro t rovnoměrných veličin je maximum distribuováno x^t,
což je také CDF U^(1/t). Tedy příklad se sqrt(U) je správný.

Úloha5: vyberme stupeň1,2,3 s pravděpodobnostmi p,q,r a potom maximum
tolika nezávislých rovnoměrných veličin. CDF je px+qx²+rx³ na[0,1].
V každé větvi je podmíněně přeškálované U opět rovnoměrné, což dokazuje
i MacLarenovu úspornou variantu. Nulová váha příslušnou větev vynechá,
takže nezpůsobí dělení nulou. Zobecnění na mocninné řady předpokládá
nezáporné koeficienty se součtem1; nelze je použít na libovolné znaménkové
polynomy pouze proto, že náhodou tvoří CDF.

Úloha6: přijatý bod je rovnoměrný ve čtvrtkruhu U²+V²<1. Marginalizací
podle V dostaneme pro0<=x<=1

```
F(x)=(2/pi)(asin(x)+x*sqrt(1−x²)).
```

Pravděpodobnost přijetí je p=pi/4. Počet pokusů má zákon
Pr(N=n)=(1−p)^(n−1)p, n>=1; součet geometrické řady a jeho první dvě
derivace dávají E(N)=1/p a SD(N)=sqrt(1−p)/p.
Číselně1.27323954... a0.58982997..., takže oprava0.587→0.590
z30.9.2003 na str.122 je správná. Obrázek A–4 má odpovídající plochy;
pozdější grafická úprava4.12.2005 nemění matematiku.

Úloha9: pro polonormální hustotu f(x)=sqrt(2/pi)exp(−x²/2), x>=0,
je f''(x)=(x²−1)f(x). Proto je na(0,1) konkávní a na(1,infinity)
konvexní. Úprava terminologie25.2.1998 věcný závěr nemění.

## 4. Normální vektory, škálování a součet; úlohy13–15

Kovariance C_ij je E((Y_i−mu_i)(Y_j−mu_j)). Pro nezávislé standardní
normální X_j a Y=mu+A*X je tedy C=A*A^T, kde T značí transpozici.
Každá lineární kombinace Y je normální (případně konstantní); například
součin charakteristických funkcí exp(−t²/2) to ukazuje přímo.

Symetrická C je pozitivně semidefinitní, tedy z^T*C*z>=0 pro všechny
reálné vektory z, právě když takový rozklad existuje. Spektrální rozklad
dá odmocninu matice. Trojúhelníkovou variantu dostaneme eliminací:
je-li první diagonála kladná, odečteme vnější součin první části sloupce
a pokračujeme na pozitivně semidefinitním Schurově doplňku. Je-li nula,
celý příslušný řádek/sloupec je nulový (z nerovnosti pro2×2 podmatice),
nastavíme tento sloupec A na nulu a pokračujeme. Tím je ošetřena i
singulární kovariance; nejde o povinnost dělit nulovým pivotem.
Přesná racionální kontrola LDL^T rozkladů proti původní Gramově matici
je v bloku `covariance` výsledků. První běh testeru omylem dělil dva
Python int a vytvořil float; opravený běh obnovil pouze tento blok.

Úloha14: pro c>0 je CDF cX rovna F(x/c); pro c=0 indikátor[x>=0];
pro c<0 je1−F(x/c), protože zadání předpokládá spojitou F. Kdyby F
měla atomy, byl by nutný levý limit, ale to není dané zadání.

Úloha15: podmíněním na X2=t dostaneme CDF součtu
integral F1(x−t) dF2(t). S hustotami vyjde
integral f1(x−t)f2(t) dt. Nezápornost dovoluje přehodit integrály;
normalizace je1. Není nutné předpokládat konečné momenty.

## 5. Další zachycená chyba C0053; úloha24 pokračuje

Na str.140 je u logistického zobrazení T(v)=4v(1−v) vytištěna
hustota1/sqrt(2*pi*x*(1−x)). Její integrál přes[0,1] je sqrt(pi/2)>1:
substituce x=sin²(theta),0<=theta<=pi/2, mění
dx/sqrt(x*(1−x)) na2 dtheta. Proto toto nemůže být hustota.

Pro V=sin²(pi U), U rovnoměrné, je na[0,1] správná CDF
F(x)=(2/pi)asin(sqrt(x)), tedy hustota1/(pi*sqrt(x*(1−x))).
Předobrazy intervalu[0,x] v U tvoří dva stejně dlouhé krajní intervaly;
to dává přímo uvedenou CDF. Identita T(sin²(theta))=sin²(2theta)
se opravou nemění. Empirická a teoretická část konečné přesnosti
úlohy24 zatím není v tomto bloku uzavřena.

## 6. Zdrojová sazba a errata

C0052 doložena snímkem str.584 (souborová str.596), C0053 str.140
(souborová str.152), třetí vydání/první dotisk9/1997. Prohledány všechny
řady `all2-prepre`, `all2-pre`, `all2`, `err2`, dále aktuální err2 TeX:
strany119–142,584–590 i hesla alias, polar, remainder, m/3, logistic,
arcsin a příslušná čísla úloh. Jediná oprava odpovědi3 mění odmítací
nerovnost; změny str.140 se týkají úlohy25. Odpovídající opravu poměru
nebo normalizace jsme nenašli. Nejde o tvrzení prvenství; nejnovější
fyzický dotisk nebyl zkontrolován. Návrhy hlášení jsou neodeslané.

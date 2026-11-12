# §3.3.2-34 a strana75: chybějící dvojice znaků

Uzavřený matematický a experimentální blok1.11.2026. Původní
strany75,79,571 vizuálně přečteny. Máme n nezávislých znaků
rovnoměrné m-písmenné abecedy. X je počet z m² uspořádaných
dvojic, které se nevyskytnou na žádné z n−1 sousedních pozic.
Překrývání dvojic je součást modelu; nelze je nahradit
nezávislými míčky v urnách.

## 1. Šest generujících funkcí

S_n^(j) označuje počet slov délky n vyhýbajících se příslušné
množině zakázaných dvojic v řádku j. Generující funkce F_j(z)
ukládá tyto počty jako koeficienty z^n a zahrnuje prázdné slovo.
Všechna uvedená písmena a,b,c,d jsou navzájem různá.
Položme p(z)=1−(m−1)(z+z²).

|Případ|Zakázané dvojice|Správná F_j(z)|
|---|---|---|
|1|aa|(1+z)/p(z)|
|2|ab|1/(1−mz+z²)|
|3|aa,bb|(1+z)/(p(z)+z²)|
|4|aa,bc|(1+z)/(p(z)+z²+z³)|
|5|ab,bc|1/(1−mz+2z²−z³)|
|6|ab,cd|1/(1−mz+2z²)|

Přímé odvození všech šesti funkcí: označme L_i funkci slov
končících zvláštním písmenem i a d počet takových písmen.
Přidání posledního znaku říká

```text
L_j=z(F−sum_(i:ij zakázáno)L_i),
F=1+(m−d)zF+sum_j L_j.
```

Soustava má nejvýše čtyři neznámé L_i; její symbolická
eliminace dává tabulku. Původní řádek5 má navíc čitatel1+z,
viz C0030. Jeho koeficient délky1 by byl m+1 místo m.
Stejná eliminace potvrzuje i tři vytištěné ekvivalence:
{ab,ba} a {aa,ab} mají funkci případu3; {ab,ac} případu6.

Nezávislý model prochází všechna slova:21 dvojic(m,n),
m4..6,n0..6, celkem80979 slov. Porovnává šest přesných počtů,
součet X a součet X² s automatovým dynamickým výpočtem.
Všechny kontroly po opravě čitatele souhlasí.

## 2. Oba momenty

Pišme (m)_r=m(m−1)...(m−r+1) pro klesající součin.
První moment je součtem indikátorů jednotlivých chybějících
dvojic: m možností aa a (m)_2 možností ab. Proto

```text
E X = [m S1+(m)_2 S2]/m^n,
```

kde Sj znamená S_n^(j). Ve druhém momentu rozlišíme stejné
dvojice a dvě různé dvojice. Ty, které používají pouze dvě
různá písmena, mají celkovou násobnost6(m)_2 a funkci S3:
dvě smyčky, opačné hrany a smyčka spojená s incidentní hranou.
Při třech písmenech máme smyčku s disjunktní hranou, cestu
délky2 a dvě hrany se společným počátkem či koncem; každá
třída má násobnost2(m)_3. Čtyři písmena dávají(m)_4 S6.
Tedy přesně

```text
E X² = [m S1+(m)_2(S2+6S3)
        +2(m)_3(S4+S5+S6)+(m)_4 S6]/m^n.
```

To jsou vytištěné vzorce; podtržení exponentů v sazbě označuje
klesající součiny, nikoli obyčejné mocniny.

## 3. Asymptotické sloupce a přesná kalibrace

Položme epsilon=1/m a přejděme k normalizované funkci
G_j(s)=F_j(s/m)=A_j(s)/D_j(s). Její kladný pól s0 je blízko1;
implicitní věta o funkci platí, protože při epsilon0 je
D_j(s)=1−s a derivace v1 je−1. Příspěvek tohoto jednoduchého
pólu ke koeficientu s^n je

```text
c exp(n tau),
tau=−log(s0),  c=−A_j(s0)/(s0 D_j'(s0)).
```

Zbývající charakteristické kořeny v původní proměnné mají
modul menší než1 pro dostatečně velké m. U kvadratických
rovnic to plyne přímo z kořenového vzorce. Pro případ4 je
charakteristický polynom
r³−(m−1)r²−(m−2)r+1; změny znaménka na(−1,0),(0,1),(1,infinity)
dávají dva malé a jeden hlavní kořen. Pro případ5 na kružnici
|r|=1 člen−mr² převládá nad r³+2r−1 při m>4; Rouchého věta
(počet kořenů se při takto malé perturbaci nemění) dává dva
kořeny uvnitř jednotkového disku. To odůvodňuje vytištěný
absolutní zbytek O(1) pro počty slov, při pevném velkém m.

Program rozvíjí s0 po mocninách epsilon, pak nezávisle c,tau.
Všech šest řádků a všechny vytištěné členy souhlasí. Zejména
v případě5 vychází c=1+2epsilon²−2epsilon³+12epsilon^4+...
a tau=−2epsilon²+epsilon³−6epsilon^4+..., takže tabulka
asymptotik již používá správný čitatel1.

Pro n=2^21,m1024 se k zaokrouhlení nespolehneme na zkrácenou
asymptotiku. Automat má stavy dané posledním zvláštním
písmenem a jeden souhrnný stav pro ostatní písmena. Povolený
přechod do zvláštního stavu má pravděpodobnost1/m a do
souhrnného stavu(m−d)/m; zakázané přechody mají0. Výchozí
vektor po prvním znaku má tytéž váhy. Součet souřadnic po
n−1 přechodech je přesná pravděpodobnost vyhnutí se vzorům.

Každé číslo omezujeme intervalem celočíselných násobků2^(-160).
Všechny matice jsou nezáporné, takže dolní součin dolních mezí
a horní součin horních mezí obsahují skutečný součin.
Po každé skalární sumě součinů zaokrouhlujeme dolů či nahoru.
Binární umocnění matic je tudíž rigorózní indukcí přes všechny
operace. První moment a druhý moment mají kladné koeficienty;
pro rozptyl použijeme interval
[lower(E X²)−upper(E X)², upper(E X²)−lower(E X)²].

Výsledky jsou

```text
E X = 141909.32995500691890740108161117408...,
Var X = 84368.32646163049085579893634725520...,
sqrt(Var X) = 290.46226340375179768668162964087....
```

Racionální intervaly v `results/monkey-test.json` dokazují
zaokrouhlení na141909.33 a290.46. Pro směrodatnou odchylku
porovnáváme interval rozptylu přímo se čtverci mezí290.455
a290.465, takže plovoucí odmocnina není součást certifikátu.

## 4. Reprodukce všech šesti pokusů na75

Použili jsme přesně uvedené parametry
X_(j+1)=(62605 X_j+113218009) mod2^29 a X_1=1234567.
Každý pokus zahrnuje2^21 hodnot, tedy2^21−1 překrývajících se
dvojic deseti nejvyšších bitů. Další pokus začíná následující
hodnotou stejného proudu.

|Pokus|Chybějících dvojic|Odchylka v násobcích směrodatné odchylky|
|---|---:|---:|
|1|141395|−1.77073|
|2|140909|−3.44392|
|3|141449|−1.58482|
|4|141066|−2.90341|
|5|141398|−1.76040|
|6|141219|−2.37666|

Všechny hodnoty leží v uvedeném intervalu1.5 až3.5 odchylky
pod očekáváním. C++ model prochází rekurenci a zaznamenává
navštívené dvojice. Nezávislý Python/NumPy validátor sestaví
pomocí zdvojování všechny afinní mocniny
X_j=A_j X_1+B_j modulo2^29 a počítá histogram dvojic.
Ověřuje všech12582912 hodnot v šesti příslušných konstrukcích,
jejich počáteční a koncové stavy a počty chybějících dvojic.
Výstupní hodnoty C++ nejsou jednotlivě uloženy: nezávislost
znamená konstrukci celého proudu a shodu všech šesti výsledků,
nikoli souborové porovnání každé hodnoty obou proudů.

Perioda generátoru je2^29: přírůstek je lichý a násobitel je1
modulo4. Podíl délky vzorku k periodě je skutečně1/256.
Věta „probably because“ je vysvětlující hypotéza autora;
samotná velikost tohoto podílu nezaručuje dané vychýlení.
Poznámka o generátoru69069 modulo2^30 nemá všechny parametry
a historická data, proto ji zde neoznačujeme za rekonstruovanou.

Oficiální záznam článku Marsaglia–Zaman, *Monkey tests for
random number generators*, potvrzuje časopis26(9),1993,str.1–10,
DOI10.1016/0898-1221(93)90001-C. Celý článek nebyl dostupný
při přímém otevření; uvedené důkazy a reprodukce jsou vlastní.
Všechny čtyři vrstvy errat i aktuální TeX zkontrolovány1.11.2026.
Nový nález je pouze C0030 v pomocném čitateli; fyzický dotisk
a prvenství neověřeny, draft neodeslán.

# MPR103–104: všechny kompozice, zastavení a generující funkce

Úplný obnovený argument, 7. listopadu 2026. Zadání p21/file41,
odpovědi p385/file405; obojí přímo zobrazeno. Autorský Pre-Fascicle5A
11.9.2019 má zadání p21/file27 a odpovědi p42/file48, rovněž zobrazené.
P103 byl skutečně znovu otevřen: jeho94 přesných absorpčních řetězců
pro47 hodnot p a189 konečných pravděpodobností jsou zachovány, nikoli
znovu spuštěny nebo vydávány za obecný důkaz. Níže je úplný argument
pro všechny parametry a podčásti včetně konkrétní realizace103(f).

E131 je známá oprava X→X_n v103(e),2.1.2025. E132 jsou obě známé
opravy výstupních zákonů104,3.3.2026. Originální errata a TeX byly
zobrazeny; tyto opravy nejsou nové nálezy. Odlišný lokální F170 je
chybný index112 místo122 v první rekurenci103(b), podrobně níže.
Kontrola všech šesti vrstev a tří TeX zdrojů je v příslušném manifestu.

## 103(a): každý konečný zákon a mezikrok

Pišme f_0=(0,0,1), f_1=(1,2,2) jako tabulky funkcí na{0,1,2}.
Obě jsou neklesající. Pro pevné n má IID slovo(X_1,…,X_n) stejný
zákon jako jeho obrácení. Proto má celá náhodná funkce
Φ_n=f_X1∘…∘f_Xn stejný zákon jako f_Xn∘…∘f_X1. Jde o pevný čas,
nikoli o totožnost společných historií nebo zastavených procesů.

Druhá kompozice má přechodovou matici

```
P = (1/2) [1 1 0; 1 0 1; 0 1 1].
```

Každý řádek plyne přímo ze dvou hodnot f_0(k),f_1(k). Tudíž
p_0ij=[i=j] a
p_(n+1)ij=Σ_(k=0)^2 p_nik([f_0(k)=j]+[f_1(k)=j])/2,
což je právě tištěná rekurence. Jelikož0≤p_nij≤1, všechny řady
g_ij(z)=Σ_n≥0p_nij z^n absolutně konvergují pro|z|<1. Sečtením
rekurence, včetně počátečního členu, vzniknou všechny tři rovnice

```
g_i0=[i=0]+(z/2)(g_i0+g_i1),
g_i1=[i=1]+(z/2)(g_i0+g_i2),
g_i2=[i=2]+(z/2)(g_i1+g_i2).
```

Řádkové vektory u=(1,1,1),v=(1,−2,1),w=(1,0,−1) splňují
uP=u,vP=−v/2,wP=w/2. Přímé dosazení dává
e_i=u/3+β_i v+γ_i w, kde β_i=(1−3[i=1])/6 a
γ_i=([i=0]−[i=2])/2: pro i0 jsou koeficienty(1/3,1/6,1/2),
pro i1(1/3,−1/3,0), pro i2(1/3,1/6,−1/2).
Násobením P^n dostaneme pro každý i,j,n≥0 přesně

```
p_nij=1/3+β_i v_j(−1/2)^n+γ_i w_j(1/2)^n.
```

Součty tří geometrických řad dávají tištěné
A=(1/3)/(1−z),B=β_i/(1+z/2),C=γ_i/(1−z/2) a
(g_i0,g_i1,g_i2)=(A+B+C,A−2B,A+B−C).
Tři nenulové vlastní vektory jsou lineárně nezávislé, takže tento
rozklad také jednoznačně řeší celý systém; nejde jen o kontrolu
několika koeficientů. Odchylka od1/3 je uniformně O(2^−n).

Pro sudé n mají koeficienty β_i v_j+γ_i w_j hodnotu2/3 na
diagonále a−1/3 mimo ni. Protože2^n≡1(mod3), dostáváme nahoře
ceil(2^n/3) na diagonále a floor(2^n/3) jinde. Pro liché n má
−β_i v_j+γ_i w_j hodnotu−2/3 při i+j=2 a1/3 jinde;
2^n≡2(mod3), takže právě antidiagonála používá floor. Po dělení
2^n je to přesné tištěné pravidlo. Platí i n0: diagonála1 a ostatní0.

## 103(b,c): úplné přechody a absorpce

Trojice a znamená tabulku právě složené funkce. Aktualizace musí být
současná, jak stanovuje přiřazení celé trojice. V(b) je nová funkce
a∘f_x, v(c) f_x∘a. Indukcí z obou neklesajících funkcí zůstává
0≤a_0≤a_1≤a_2≤2. Proto a_0=a_2 právě tehdy, když jsou všechny
tři hodnoty stejné. V(c) lze aktualizovat pouze krajní hodnoty;
v(b) potřebujeme vnitřní hodnotu pro nepřímé indexování.

Všechny dosažitelné přechody před zastavením jsou:

|Stav|b, bit0|b, bit1|c, bit0|c, bit1|
|---|---|---|---|---|
|012|001|122|001|122|
|001|000|011|000|112|
|011|001|111|000|122|
|122|112|222|011|222|
|112|111|122|001|222|

Každá buňka vzniká přímo z tabulek f_0,f_1. Tabulka je uzavřená
na uvedených pěti přechodných stavech a třech konstantách; indukce
tedy dokazuje úplnost, ne pouze dosažitelnost některých stavů.
Po prvním kroku má každý přechodný stav právě jeden bit vedoucí
do konstanty. Za férových bitů proto podmíněná šance přežití
každého dalšího kroku je1/2. N je konečné skoro jistě a
P(N=n)=2^(−(n−1)) pro n≥2, u obou metod.

Pro pevné j definujme g_s(z)=E[z^N_s [výstup=j]], kde N_s je
počet ještě potřebných kroků ze stavu s. Pro konstantní s=ccc
je g_ccc=[j=c]. V(b) je celý systém

```
g012=(z/2)(g001+g122),
g001=(z/2)([j=0]+g011),  g011=(z/2)(g001+[j=1]),
g122=(z/2)(g112+[j=2]),  g112=(z/2)([j=1]+g122).
```

Z druhého páru se po substituci stává
(1−z²/4)g001=(z/2)[j=0]+(z²/4)[j=1]; obdobně
(1−z²/4)g122=(z²/4)[j=1]+(z/2)[j=2]. První rovnice pak dává

```
g012=([j≠1]+[j=1]z) z²/(4−z²).
```

To je tištěný výsledek. Při z1 všechny tři hodnoty jsou1/3.
Součet je G(z)=(2+z)z²/(4−z²)=z²/(2−z), což souhlasí s výše
odvozeným celým zákonem N. Derivace v1 jsou G′(1)=3,G″(1)=8;
tedy EN=3 a VarN=8+3−9=2. Derivace jsou legitimní, protože
geometrický ocas dává analytickou řadu v okolí1.

F170: tisk místo g122 používá v první rovnici g112. Pro j2
nemůže001 ani112 během jediného kroku skončit222, jak ukazují
obě příslušné buňky tabulky(b). Tištěná pravá strana má tedy
koeficient z² rovný0. Skutečný proces z012 při slovu11 přejde
012→122→222, a dává koeficient1/4. Přepis112→122 opravuje tento
lokální mezikrok; výsledná GF, zákon výstupu, EN a VarN jsou platné.

V(c) je první rovnice opět g012=(z/2)(g001+g122), ale ostatní jsou

```
g001=(z/2)([j=0]+g112),  g112=(z/2)(g001+[j=2]),
g122=(z/2)(g011+[j=2]),  g011=(z/2)([j=0]+g122).
```

První z nich odpovídá tištěné změně. Tabulka nemá vstup do111,
proto výstup1 nikdy nevzniká. Záměna0↔2 a bit0↔bit1 zachovává
férový zákon a mění výstup0 na2. S již prokázaným ukončením jsou
obě pravděpodobnosti1/2. Podmíněný hazard dává stejný celý zákon N
a oba momenty. Každý krok obou metod vyžaduje konstantně mnoho
operací a slov paměti; střední počet kroků je právě3.

## 103(d): proč se zákony liší

Nekomutativnost lze vidět už na0: (f_0∘f_1)(0)=0, ale
(f_1∘f_0)(0)=1. V(c), pokud f_0∘a=111, musí a=222, protože
jediný vzor hodnoty1 při f_0 je2; pokud f_1∘a=111, musí a=000.
Proto první koalescence nikdy nemůže být111. V(b) je konstantní
funkce stabilní při libovolném dalším skládání zprava; v(c)
skládání zleva může měnit její hodnotu, i když zůstane konstantní.
Slovo011 dává první koalescenci v čase3 v obou metodách, ale
v(b)111 a v(c)222. Rovnost zákonů pro každý pevný čas v(a)
nezachovává zastavovací události při obrácení slova. Všechny
tištěné vysvětlující věty tím mají konkrétní argument.

## 103(e): celý chybný restart, přesná řada a ukončení

Po zapracování E131 generuje sub(T) v každém volání čerstvých T
IID bitů. Musí provést všech T kroků, i po koalescenci: v(c) se
hodnota konstanty dále mění. Vnější cyklus volá T=2,4,8,…;
všechna T jsou tedy kladná sudá, nejméně2. Z tabulky(c) plyne,
že přežití T kroků je možné právě pro dvě střídavá slova. Pro
sudé T končí ve112 a011, každé s pravděpodobností2^−T.

Podle(a) je marginální zákon a_0 při sudém T ze startu0
((2^T+2)/3,(2^T−1)/3,(2^T−1)/3)/2^T. Od výsledků0 a1 odečteme
po jednom neabsorbovaném slovu; výsledku2 se toto netýká.
Proto přesný zákon návratu(−1,0,1,2) je

```
(2,(2^T−1)/3,(2^T−4)/3,(2^T−1)/3)/2^T.
```

Všechny složky jsou nezáporné pro sudé T≥2 a jejich součet je1.
Nezávislost čerstvých restartů dává pravděpodobnost dosažení
volání k rovnou ∏_(j=1)^(k−1)2^(1−2^j)=2^(k+1−2^k).
Násobení jeho pravděpodobností výstupu0 a sečtení dává přesně

```
P(výstup0)=(1/3)Σ_(k≥1) 2^(k+1)(2^(2^k)−1)/2^(2^(k+1))
          =1/4+5/32+85/4096+… .
```

Už první dva členy dávají13/32>1/3, takže tento postup selhává.
Po třech voláních je součet1749/4096 a zbývající pravděpodobnost
všech budoucích výstupů nejvýše1/2048. Tedy
1749/4096≤P(výstup0)≤1751/4096. Oba kraje leží mezi0.4265
a0.4275: pro horní stačí1751·400=700400<700416=171·4096;
pro dolní1749·2000=3498000>3493888=853·4096.
Tištěné zaokrouhlení0.427 je tím přesně doloženo bez nového běhu.
Staré přesnější0.4271647160251935 se pouze zachovává jako starý výsledek.

Pravděpodobnost neúspěchu prvních k volání je
2^(k−(2^(k+1)−2))→0, tudíž i chybný postup skončí skoro jistě.
Střední práce v jednotkách vnitřních iterací je
Σ_k≥1 2^(2k+1−2^k)<∞. Konkrétně první tři členy jsou2,2,1/2;
pro k≥4 platí2^k≥3k (indukcí), takže zbytek je nejvýše
Σ_k≥4 2^(1−k)=1/4. Práce má tedy průměr nejvýše19/4, ale
výstupní zákon je špatně. Subroutine vyžaduje dva stavy a čítače,
tedy O(1) slov v běžném modelu; nevydáváme to za konstantní bitovou
paměť neomezeného čítače.

## 103(f): konkrétní oprava, invariant, ukončení a cena

Nechť Y_1,Y_2,… jsou jednou zvolené IID férové bity. Zvolíme tuto
zcela konkrétní realizaci konzistence, bez předpokladu určitého PRNG:

```
T=1; cache=[]
opakuj:
    T=2*T
    doplň cache novými nezávislými bity až do indexu T
    lo=0; hi=2
    pro j=T,T−1,…,1:
        lo=f_cache[j](lo); hi=f_cache[j](hi)
    je-li lo=hi, vrať lo
```

Invariant je cache[j]=Y_j při všech pozdějších voláních. Vnitřní
cyklus používá pořadí Y_T,…,Y_1 a proto spočítá právě krajní
hodnoty Φ_T=f_Y1∘…∘f_YT. Je-li N první koalescence v(b),
pak pro T<N krajní hodnoty nejsou stejné; pro T≥N je Φ_T
konstantní se stejnou hodnotou jako Φ_N. Důvod je
Φ_T=Φ_N∘f_Y(N+1)∘…∘f_YT. Výstup je tedy cestově totožný
s(b), nikoli pouze stejně rozdělený.

První úspěšné T je nejmenší dyadická hodnota alespoň N, takže
T≤2N. Celkový počet vnitřních iterací je2+4+…+T=2T−2<4N;
počet jednotlivých vyhodnocení f je menší než8N. Počet nově
vygenerovaných bitů je T≤2N. Z EN=3 plyne střední počet iterací
<12, vyhodnocení <24 a bitů≤6; ukončení skoro jistě již plyne
z N<∞. Ukládání potřebuje O(T) bitů plus dva stavy a čítače.

Tištěný reset vhodného generátoru je alternativní způsob
reprodukce stejných očíslovaných bitů. Musí obnovit stejné stavy
na hranicích stejných časových bloků, nikoli při každém pokusu
začít libovolným novým proudem. Uvedený invariant je přesné
požadované rozhraní. Žádný konkrétní generátor kniha nezadává;
není zde tvrzena jeho náhodnost ani proveden test nespecifikované
knihovny. Původní článek výslovně uvádí jak ukládání, tak reset
na dyadických hranicích. Úloha je opraveným algoritmem výše
vyřešena úplně. Obecná aplikace a tvrzení o ceně jsou samostatně
doloženy v `sequential-mpr-ex103-cftp.md`.

## 104: všechny reálné pravděpodobnosti, obě orientace, všechny momenty

Nyní0≤p≤1,q=1−p,a=pq∈[0,1/4],D=1−az². V celé tabulce
násobíme větev0 vahou q a větev1 vahou p. Pro(b) eliminace dvojic
001↔011 a122↔112 dává

```
D g001=qz[j=0]+p²z²[j=1],
D g122=q²z²[j=1]+pz[j=2],
g012=z(qg001+pg122).
```

Proto vektor označených GF výstupů(0,1,2) je
(q²z²,az³,p²z²)/D. Při z1 dostaneme přesně opravený zákon
(q²,pq,p²)/(1−pq). Normalizace: q²+pq+p²=1−pq.

Pro(c) z dvojic001↔112 a122↔011 vzniká

```
D g001=qz[j=0]+p²z²[j=2],
D g122=q²z²[j=0]+pz[j=2],
g012=z(qg001+pg122).
```

Výsledný vektor je(q²z²(1+pz),0,p²z²(1+qz))/D; při z1
to je opravené(q²(1+p),0,p²(1+q))/(1−pq).
Čitatel součtu je q²+p²+pq(q+p)=1−pq. Oba zákony jsou
nezáporné a normalizované i v krajích p0,p1. Pro p0 je výstup0,
pro p1 výstup2 v obou metodách. Tím jsou E132 ověřena pro všechny
parametry, nikoli jen pro původních47 racionálních hodnot.

V obou orientacích se vektor sčítá na

```
G(z)=[1−a(2−z)]z²/(1−az²).
```

Pro r≥1 jsou koeficienty P(N=2r)=(1−2a)a^(r−1) a
P(N=2r+1)=a^r. Jsou nezáporné a součet je
((1−2a)+a)/(1−a)=1, takže N<∞ skoro jistě pro každý p.
Při a0 je G=z², tedy N=2 deterministicky. Pro a>0 řada
konverguje pro|z|<1/√a, což obsahuje okolí1; všechny následující
derivace proto skutečně počítají momenty.

Položme L=ln G v okolí1. Platí
L=2ln z+ln(1−2a+az)−ln(1−az²), tedy

```
L′(1)=2+3a/(1−a)=3/(1−a)−1,
L″(1)=−2+(2a+a²)/(1−a)².
```

První derivace pochází z2/z+a/(1−2a+az)+2az/(1−az²).
Druhá má členy−2/z²−a²/(1−2a+az)²
+2a(1+az²)/(1−az²)²; v1 se složí na uvedený výraz.
Proto EN=G′(1)=L′(1) a
VarN=G″(1)+G′(1)−G′(1)²=L″(1)+L′(1)
=a(5−2a)/(1−a)², přesně tisk. Při p1/2 jsou to3 a2;
při p0 nebo1 jsou2 a0. Jmenovatel1−a≥3/4 se nikdy nenuluje.

Úplný rozsah103(a–f),104 je tím doložen. Nové matematické běhy0,
opakované staré běhy0. Původní PS a všechny známé změny jsou
odlišeny od nového F170. Žádný výsledek nepředpokládá nezávislou
revizi koordinátora nebo fyzický tištěný exemplář.

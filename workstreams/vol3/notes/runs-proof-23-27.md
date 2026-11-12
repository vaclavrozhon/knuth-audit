# Runs: úlohy23–27, zadání47, odpovědi606–607

Sazba v `images/runs-file-058.png`, `multisets-file-617.png`,
`runs-file-618.png`. Pět vrstev errat v `sources/runs-errata-review.json`;
znaménko v odpovědi23 a upřesnění oriented forest jsou známé opravy2006.
Bez nového nálezu a bez nového výpočtového běhu.

## 23. Dlouhé běhy

První dvě hodnoty určují směr a první porušující hodnota začíná další
běh, proto všechny kromě případného posledního mají délku≥2.
V příkladu75|62|389|14 první dva bloky klesají, další dva rostou;
přes každou vyznačenou hranici by se směr porušil.

Při začátku u a m dalších monotónních hodnotách je hustota příštího
začátku x
`g_m(u,x)=[u^m+(1−u)^m−|u−x|^m]/m!`, m≥1.
První dva členy počítají oba směry, poslední odečte pokračování stejným
směrem až za x. Používáme opravené minus. Součet dává
`g(u,x)=e^u+e^(1−u)−1−e^|u−x|`.
Integrál v x je1, protože integrál posledního členu je
e^u+e^(1−u)−2. Proto jde o Markovovo jádro začátků běhů a
`f_(k+1)(x)=∫f_k(u)g(u,x)du`. Pro f_1=1 vychází
`f_2=2e−1−e^x−e^(1−x)`.

Ocas délky při začátku u je pro délku≥m+1 roven
`[u^m+(1−u)^m]/m!`, m≥1. Součet ocasů včetně prvního členu1
dává `w(u)=e^u+e^(1−u)−1`. Integrací tedy
`Llong_1=2e−3`, `Llong_2=3e²−8e+2`.
U druhého výpočtu stačí položit A=e^x+e^(1−x):
integrál A je2(e−1), integrál A² je e²−1+2e.
Tištěné aproximace2.43656 a2.42091 souhlasí s již uloženými
intervaly e a L_2=e²−2e v `results/runs-numeric-reference.json`;
platí Llong_2=3L_2−2e+2. Žádný starý výpočet se neopakoval.

Označme s=sin(1/2), c=cos(1/2), d=3s−c a
`f(x)=[2cos(x−1/2)−s−c]/d`, `μ=(s+c)/d`.
Je d>0, neboť tan(1/2)>1/2>1/3; čitatel f má minimum c−s>0.
Integrál f je1, protože integrál2cos(x−1/2) je4s.

Pro h(x)=∫e^|u−x| f(u)du platí
`h''−h=2f`, `h'(0)=−h(0)`, `h'(1)=h(1)`.
Funkce μ−f splňuje tutéž rovnici i obě okrajové podmínky, neboť
`f''+f=−μ`, `f'(0)=μ−f(0)`, `f'(1)=f(1)−μ`.
Homogenní řešení Ae^x+Be^(−x) s oběma podmínkami má A=B=0,
takže h=μ−f. Integrací h dostaneme současně
`∫h=∫w f−1=μ−1`, tedy ∫w f=μ. Proto Tf=μ−h=f:
tištěná hustota je skutečně stacionární a její střední délka je μ.

Konvergence není pouze předpokládána. Pro x∈[1/4,3/4] a každé u
je už `g_1(u,x)=1−|u−x|≥1/4`; všechny další členy jsou nezáporné.
Jádro tedy obsahuje složku hmotnosti1/8 rovnoměrnou na tomto intervalu.
Zbývající složka má hmotnost7/8, a tudíž T kontrahuje L1 vzdálenost
hustot nejvýše faktorem7/8. Dostáváme f_k→f v L1. Jádro je omezené,
takže po dalším kroku jde i o stejnoměrnou konvergenci hustot.
Omezenost w dává konvergenci středních délek k
`μ=(1+cot(1/2))/(3−cot(1/2))`.
Alternující Taylorovy řady dávají
0.4794255<s<0.4794256 a0.8775825<c<0.8775826.
Dosazení krajů do poměru dává2.42022<μ<2.42024, a potvrzuje2.4202.

## 24. Vychýlené bitové sekvence

Model z§5.1.1-18 je převzat, n>0, q=1−p. Pišme
A=p²+q², B=2pq, C=A−pq. Sousední indexy i,i+1 mají k společných
nejvyšších bitů, pak0→1 a m=n−k−1 přenosových bitů1→0. Takových
párů je2^k. Ve společném prefixu jsou výstupní bity shodné s
pravděpodobností A a uspořádání> nastane s pravděpodobností pq.
Pravděpodobnost poklesu je proto

`(1−A^k)/2+A^k[p²+Bq² Σ_{j=0}^{m−1}B^j]`.

První různé původní bity0,1 dávají pokles s pravděpodobností p²;
jsou-li shodné (pravděpodobnost B), následující páry1,0 mají pokles
q² a shodu B. To dokazuje i všechny krajní m0 případy.

Po součtu přes k a přičtení jednoho běhu přeuspořádáme prefixový člen:
`Σ_k 2^k(1−A^k)/2=Σ_k 2^kA^k B(2^(n−k−1)−1)`.
Vzniká přesně první tištěný konečný součet.
Protože B−1=−A a A−B=2A−1, jeho tři geometrické části jsou

`(p²/A)[(2A)^n−1]`,
`2^(n−1)(1−A^n)`,
`−[p q³/(AC)][(2A)^n−B^n]`.

Poslední používá2A−B=2C. Sečtení s1 a identita
`pC−q³=(p−q)A` dávají přesně druhý tištěný vzorec:

`(2A)^n[p(p−q)/C−1/2]+B^n p q³/(AC)+q²/A+2^(n−1)`.

A≥1/2 a C≥1/4, takže konečný výraz nemá nepovolený jmenovatel.
Případ2A−1=0 je ve výše uvedeném součtu zkrácen polynomicky,
nikoli dělením nulou. Pro p0 vyjde1, pro p1 vyjde2^n.
Pro p1/2 vyjde2^(n−1)+2^(−n−1), což souhlasí i přímo s nezávislými
rovnoměrnými hodnotami nad abecedou velikosti2^n a s možností rovnosti.

## 25–27. Tři závěrečné identity

25. V_j=(U_1+...+U_j) mod1 je po podmínění celou minulostí opět
    rovnoměrná nezávislá hodnota: posun modulo1 zachovává rovnoměrnou
    míru. Tudíž všechna relativní pořadí V_1,..,V_n mají šanci1/n!.
    Pišme V_0=0; při přičtení U_j nastane přenos přes1 právě když
    V_j<V_(j−1), s výjimkou nulové množiny rovností. První přenos je0.
    Součet přenosů je floor(ΣU_j), tedy počet sestupů V_1,..,V_n.
    Požadovaná pravděpodobnost je A(n,k)/n!.
26. Formální derivování geometrické řady dává
    `θ^m(1−z)^−1=Σ_j≥0 j^m z^j`.
    Pro m≥1 již dokázaný Eulerův vzorec dává
    `Σ_k A(m,k)z^(k+1)/(1−z)^(m+1)`.
    Při m0 se přímo ponechá1/(1−z); nulová mocnina operátoru
    nepotřebuje konvenci0^0. Tištěný příklad m5 přebírá ověřený
    Eulerův řádek1,26,66,26,1.
27. Pro neprázdný orientovaný rostoucí les se pořadí kořenů i sourozenců
    kanonicky volí podle klesajících čísel. Preorder pak jednoznačně
    určí permutaci. Obráceně první hodnota a_1 je kořenem; její potomci
    jsou maximální následující úsek hodnot>a_1 před prvním menším prvkem.
    Rekurze uvnitř tohoto úseku i za ním dává přesně tištěnou konstrukci.
    Všichni potomci jsou větší než rodič a kořeny postupně klesají,
    takže obě zobrazení jsou navzájem inverzní.

    Má-li vrchol potomky, následuje v preorder jeho větší dítě: vzestup.
    Po listu následuje menší sourozenec některého jeho předka, případně
    menší další kořen; jeho hodnota je menší než tento předek, a tedy
    i než původní list. Jde o sestup. Poslední vrchol je list.
    Listy tedy přesně odpovídají sestupům plus poslední pozici,
    což dává k+1 listů a počet A(n,k). Tento argument má n≥1;
    prázdný les/permutace mají samostatné nulové konvence.

Historické atribuce a citované články606–607 zůstávají přeskočeny.
Úlohy28–29 přidané teprve pozdějšími erraty nejsou úlohami prvního
dotisku a tento checkpoint je neprohlašuje za vyřešené.

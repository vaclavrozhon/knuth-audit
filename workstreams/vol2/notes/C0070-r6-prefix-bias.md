# V2-C0070: R6 může mít převahu v každém prefixu

Původní odpověď §3.5-31 na straně 597 (DjVu 609) říká, že obdobný
protipříklad pro R6 není znám. R6 vyžaduje správné četnosti po všech
efektivních adaptivních výběrech, přesně podle definice na straně163. Věcný obsah tohoto upozornění je třeba
aktualizovat: existuje reálná R6 posloupnost U_0,U_1,... taková, že
v každém neprázdném prefixu je přísně více než polovina členů menších
než 1/2. Níže je úplný přímý důkaz přesně pro definici R6 knihy,
nikoli jen odkaz na odlišně pojmenovanou moderní náhodnost.

Strany 163 a 597 byly vizuálně zkontrolovány. Prohledány všechny
čtyři vrstvy errat a aktuální TeX podle 31/597, Ville, R6, Shen a tématu;
nenalezena oprava tohoto komentáře. Známá oprava indexu v zadání 31
z 26.12.2002 ani náš C0062 o opačném směru převahy se jej netýkají.
Novější fyzický tisk ani prvenství nejsou ověřeny; nic se neodesílá.

## 1. Nezávislé souřadnice, jejichž rozdělení se blíží rovnoměrnému

Položme K=4096. Vytvořme nezávislé reálné veličiny U_j v[0,1).
Pro j<K nechť je U_j rovnoměrné v[0,1/2). Pro j>=K položme

```
delta_j = 1/(4(j+1)^(1/4)),
f_j(u) = 1+2 delta_j  pro 0<=u<1/2,
         1−2 delta_j  pro 1/2<=u<1.
```

f_j je hustota: je nezáporná a její integrál je jedna. Zejména
Pr(U_j<1/2)=1/2+delta_j. Pro jednotný zápis položme delta_j=1/2
při j<K. Platí delta_j->0 a pro každou b-adickou buňku
I_a=[a/b,(a+1)/b), 0<=a<b, máme

```
|Pr(U_j in I_a)−1/b| <= 2 delta_j/b -> 0.
```

Ukážeme, že s pravděpodobností jedna je U náhodné podle R6.
Fixujme základ b, algoritmus adaptivně čtoucí různé dosud neviděné
hodnoty Y_j=floor(bU_j), a pravidlo rozhodující před čtením, zda
novou hodnotu vybere. Jejich složení pokrývá algoritmy a R5 pravidla
z definice R6. Po libovolné konečné historii mají nepřečtené souřadnice
stále původní vzájemně nezávislá rozdělení; výběr jejich indexu může
záviset na viděné historii, hodnotu nové souřadnice však nezná.

Pro pevné a nechť Z_i je indikátor, že i-tá vybraná hodnota je a,
a pi_i její podmíněná pravděpodobnost před přečtením. Na každé větvi,
kde je výběr nekonečný, vybrané indexy opustí každou konečnou množinu.
Proto pi_i->1/b a jejich aritmetické průměry také směřují k1/b.
Stačí ověřit, že průměr rozdílů Z_i−pi_i jde k nule.

Pro veličinu Z s hodnotami 0 a 1 (Bernoulliho veličinu) s průměrem pi je

```
E exp(lambda(Z−pi)) <= exp(lambda²/8).
```

Krátké odvození: druhá derivace logaritmu levé strany je rozptyl
Bernoulliho veličiny po exponenciálním převážení, tedy nejvýše1/4;
hodnota a první derivace v nule jsou nulové. Dvojí integrace dává mez.
Aplikace podmíněně před každým čtením ukazuje, že

```
exp(lambda sum_(i<=m)(Z_i−pi_i)−m lambda²/8)
```

má nezvětšující se podmíněnou střední hodnotu. m je počet dosud
vybraných hodnot; při přeskočeném čtení se výraz nemění. Takový
nezáporný proces se nazývá supermartingal.

Zastavme jej při m-tém výběru nebo po T přečteních. Jeho střední
hodnota nepřesáhne1. S lambda=4 eta dostaneme pro každé eta>0

```
Pr(m-tý výběr nastane a sum_(i<=m)(Z_i−pi_i)>=eta m)
    <= exp(−2 eta² m).
```

Nejprve platí mez do T čtení; přechodem T->nekonečno platí i při
neomezeném adaptivním čtení či ukončení. Stejně se ošetří záporná
odchylka. Součet pravděpodobností přes m je konečný. Pravděpodobnost
nekonečně mnoha takových odchylek je tedy nulová: pravděpodobnost
jejich výskytu po kterémkoli M je nejvýše ocas konvergentní řady.
Po průniku přes kladné racionální eta dostaneme požadovaný nulový
limit. Výběr, je-li nekonečný, má tudíž četnost a rovnou1/b.

Základů b, hodnot a i efektivních dvojic algoritmů je spočetně mnoho.
Průnik všech těchto událostí pravděpodobnosti jedna má pravděpodobnost
jedna. To dokazuje R6 pro náš reálný součinový model. Důkaz nepotřebuje
žádnou jednotnou rychlost běhu výběrových algoritmů.

## 2. Kladná pravděpodobnost převahy v každém prefixu

Označme H_n počet j<n s U_j<1/2 a D_n=H_n−n/2. Pro n<=K je D_n=n/2
jistě kladné. Pro každé n>=1 má D_n střední hodnotu

```
mu_n=sum_(j<n) delta_j >= n/(4 n^(1/4)) = n^(3/4)/4.
```

Všechny indikátory v H_n jsou nezávislé, některé mohou být konstantní.
Stejný exponenciální odhad jako v části1 dává

```
Pr(D_n<=0) <= exp(−2 mu_n²/n) <= exp(−sqrt(n)/8).
```

Pro n>K tedy sjednocení všech nepříznivých událostí má pravděpodobnost
nejvýše

```
sum_(n>K) exp(−sqrt(n)/8)
 <= integral_K^infinity exp(−sqrt(t)/8) dt
  = 16(sqrt(K)+8) exp(−sqrt(K)/8)
  = 1152 exp(−8)
  < 1152 (3/8)^8 = 59049/131072 < 1/2.
```

Použili jsme pouze e>1+1+1/2+1/6=8/3. Tudíž s pravděpodobností větší
než1/2 jsou všechny D_n kladné zároveň. Průnik této události s R6
z části1 má stejnou kladnou pravděpodobnost a je neprázdný.
To je hledaný protipříklad pro přesnou reálnou formulaci úlohy31.
Nevyžaduje experiment ani předpoklad o otevřeném problému.

## 3. Co přesně dokládají primární zdroje

Shenův článek „On relations between different algorithmic definitions
of randomness“, Soviet Math. Dokl.38(2) (1989),316–319, původně rusky
1988, byl přečten celý vizuálně. Věta1 a lemma2 dokazují rozlišení
Kolmogorovovy–Lovelandovy stochastičnosti (správných četností po adaptivních
výběrech) od Martin-Löfovy náhodnosti (vyhýbání se všem efektivně
popsaným nulovým testům)
pomocí nezávislých bitů s pomalu mizející odchylkou jejich rozdělení.
Jeho konkrétní závěrečná volba odchylek je jiná; samotnému článku zde
nepřipisujeme výslovnou větu o každém jednostranném prefixu.

Kniha A. Shen, V. A. Uspensky, N. Vereshchagin, *Kolmogorov Complexity
and Algorithmic Randomness* (AMS,2017), věta203(b), str.307–308, tuto prefixovou
vlastnost uvádí přímo pro binární Kolmogorovovy–Lovelandovy výběry.
Podrobnosti čtení a výňatek eviduje `sources/randomness-history-sources.json`.
Náš důkaz výše poskytuje navíc přímé ověření pro reálné U a všechny
základy b, které jsou v Knuthově R6 požadovány.

Název „Kolmogorov–Loveland random“ bývá dnes používán pro silnější
podmínku neúspěchu všech výpočetních sázkových strategií. Tu nelze
zaměňovat se stochastičností (správnými četnostmi po výběrech), která
odpovídá R6 zde. Tento nález neřeší otázku rovnosti této silnější
sázkové náhodnosti s Martin-Löfovou náhodností.

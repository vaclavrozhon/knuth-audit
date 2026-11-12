# MPR98–99 — úplný důkaz proměnlivého driftu

D196–D197, 7. listopadu 2026. Původní p21/file41 a p384/file404
byly přímo zobrazeny, stejně jako PS p21/file27 a p41/file47.
P099 byl skutečně znovu otevřen, protože starý správný potenciálový
důkaz neuváděl každý tištěný indukční a integrační krok. Jeho
156 konečných řetězců,1248 přesných mezí a1092 rostoucích přechodů
se zachovávají jako stará evidence, bez jediného opakovaného běhu.

## Model, historie a měřený počet kroků

X začíná v nezáporném celém n a končí po prvním dosažení0.
Po ukončení nastavujeme X_m=0 pro všechny další m. Počet skutečně
provedených redukcí označme R, s dovolenou hodnotou∞ v úloze99,
dokud neprokážeme opak. Jde o počet provedení přiřazení; náklady
na vygenerování F nejsou v zadání specifikovány ani účtovány.

Při každém aktivním volání ve stavu j>0 je D=F(j) čerstvý tah
z příslušného rozdělení a jeho střední hodnota je alespoň g_j.
Přechodové zákony mohou být pro různá volání různé, jak odpověď98
výslovně připouští. Potřebný přesný důsledek je tedy

```
E(D | dosavadní historie, X=j) ≥ g_j.
```

Je to obvyklý podmíněný význam zadání o novém nezávislém losování
F(j), nikoli tvrzení, že hodnota F(X) je bez podmínění nezávislá
na minulém stavu X. Všechny následující argumenty jsou uniformní
v přípustném budoucím zákoně; lze proto měnit rozdělení mezi
voláními. Na nulových historiích nic nepodmiňujeme dělením nulou.

Definujme potenciál

```
V(0)=0,   V(j)=Σi=1..j 1/g_i  pro j≥1.
```

V je nezáporný, konečný v každém konečném stavu a rostoucí,
protože0<g1≤g2≤⋯. V98 stačí definice do n, v99 do všech
kladných celých stavů. Řada V(j) se nikde nesčítá přes
nekonečný koncový stav; každý jednotlivý tah D je konečné celé číslo.

## 98: invariant, ukončení a každý řádek stavové indukce

Z1≤D≤j plyne0≤j−D≤j−1. Stav zůstává nezáporný celý
a každým aktivním krokem striktně klesne, takže R≤n bodově.
V n=0 je R=0. Pro j>0 předpokládejme indukčně, že z každého
menšího stavu a každé přípustné historie je průměr zbylých kroků
nejvýše V tohoto stavu. Označme aktuální pravděpodobnosti D=k
jako p_k a aktuální průměr d=Σk=1..j kp_k≥g_j.

Tištěný symbol E_{j−k} znamená průměr z příslušné pokračující
větve. Při měnících se rozděleních se nemusí jednat o jedinou
časově homogenní funkci, ale uniformní indukční mez se na
každou takovou větev vztahuje. Pravidlo úplného očekávání
a následně všechny tištěné kroky jsou

```
E R = 1+Σk=1..j p_k E(R_remaining | D=k)
    ≤ 1+Σk=1..j p_k V(j−k)
    = 1+Σk=1..j p_k(V(j)−Σi=j−k+1..j 1/g_i)
    = V(j)+1−Σk=1..j p_k Σi=j−k+1..j 1/g_i
    ≤ V(j)+1−Σk=1..j p_k k/g_j
    = V(j)+1−d/g_j ≤ V(j).
```

Součet pravděpodobností je1. V každém vnitřním součtu je
přesně k členů a g_i≤g_j, takže každý1/g_i≥1/g_j.
Pro k=j je koncový stav0 a součet V(j), pro k=1 jde
o jediný člen1/g_j. Jmenovatele jsou kladné. Všechny součty
jsou konečné a integrabilita R plyne už z R≤n.

Indukce tedy pro začátek n dává právě ER≤Σi=1..n1/g_i.
Neformální poznámka zadání o „zlomku kroku na pokles o1“
je konkretizována tímto potenciálem a přesným d/g_j≥1.

## 99: všechny obrácené součty a integrabilita jednoho tahu

Nyní D může být libovolné celé k≤j, včetně0 a záporných hodnot.
Nový stav j−k je stále nezáporný, ale nemusí klesnout, proto
indukce podle stavu z98 není oprávněná. Horní mez D≤j zaručuje
E D^+≤j. Předpoklad E D≥g_j>0 vylučuje nekonečnou
zápornou část; tedy E D^-<∞ a E|D|<∞ na každé pevné
kladně pravděpodobné historii. Není zde rozdíl∞−∞.

Tištěné rozšíření pro a>b je přesně

```
Σ_a^b = −Σi=b+1..a−1 1/g_i,
```

neboli pro všechny potřebné a,b je Σ_a^b=V(b)−V(a−1).
Pro a=b+1 jde o prázdný součet0. Pro a=j+3,b=j je tedy
−Σ_{j+3}^j=1/g_{j+1}+1/g_{j+2}≤2/g_j, což ověřuje
i minus v tištěném příkladu, oba indexy a směr nerovnosti.

Pro každé celé k≤j platí jednotná identita a nerovnost

```
V(j)−V(j−k)=Σ_{j−k+1}^j ≥ k/g_j.                 (*)
```

Pro k>0 je to již dokázaný součet k členů. Pro k=0 jsou
obě strany0. Pro k=−l<0 je levá strana
−Σi=j+1..j+l 1/g_i; každý kladný sčítanec je≤1/g_j,
takže po změně znaménka dostaneme nejméně−l/g_j.
V98 i99 jsou tím pokryty všechny přípustné kroky.

Při k≥0 je0≤V(j−k)≤V(j); při k<0 je
V(j−k)≤V(j)+(−k)/g_j. Z konečnosti E D^- tedy plyne
podmíněná integrabilita V(j−D). Také rozdíl v(*) je
absolutně integrabilní: pro k≥0 je jeho velikost nejvýše V(j),
pro k<0 nejvýše(−k)/g_j. Podepsané součty v odpovědi tedy
lze skutečně přeskupit a dostaneme

```
E(V(j−D)|historie) ≤ V(j)−E(D|historie)/g_j
                  ≤ V(j)−1.                    (**)
```

Žádná očekávání přes nekonečné podpory nezůstávají neodůvodněná.

## 99: úplná časová indukce tištěné odpovědi

Pro limit m≥0 a start j definujme E_{m,j}=E min(m,R),
přičemž opět dovolíme všechny přípustné pokračující historie.
Vždy0≤E_{m,j}≤m. Počáteční případy jsou
E_{0,j}=0 pro všechna j a E_{m+1,0}=0 pro všechna m.
Pro j>0 se první krok provede jistě, takže bodově
min(m+1,R)=1+min(m,R_remaining). Proto

```
E_{m+1,j}=1+Σk=−∞..j p_k E_{m,j−k}.
```

Přesněji je každý průměr v pravé straně průměrem z příslušné
větve; stejná uniformní časová indukce to dovoluje. Součet
je konvergentní už díky omezení m a součtu p_k=1.
Indukční předpoklad E_{m,j−k}≤V(j−k), platný pro všechny
stavy, a(**) dávají

```
E_{m+1,j}≤1+Σk p_k V(j−k)≤V(j).
```

Vnitřní součet potenciálů je konečný podle předchozího odstavce.
Jeho přepis pomocí obrácených Σ a poslední dvě nerovnosti
jsou přesně týmiž algebraickými kroky jako v98, nyní oprávněnými
i pro záporné k. Indukce podle m tedy nepředpokládá, že j−k<j.

Pro R∈{0,1,…,∞} platí bodově
min(m,R)=Σr=1..m[R≥r]. Očekávání konečného součtu dává
E min(m,R)=Σr=1..m P(R≥r), jehož rostoucí limita je ER
podle nezáporného součtu všech indikátorů. Tím je zde potřebný
limitní krok doložen přímo; neodvoláváme se na dosud neauditovanou
úlohu100. Výsledek je ER≤V(n)<∞. Navíc
mP(R=∞)≤E min(m,R)≤V(n) pro každé m, tedy P(R=∞)=0.
Ukončení s pravděpodobností1 a požadovaná očekávaná cena jsou
skutečnými závěry, nikoli předpoklady indukce.

## 99: celý supermartingalový dovětek a globální integrabilita

Označme H_m celou historii po m pokusech a udržujme stav0
absorbující. X_m je H_m-měřitelná. Podle(**) a zmrazení0

```
E(V(X_{m+1})|H_m) ≤ V(X_m)−[R>m].
```

Nejdříve tuto rovnost čteme jako rozšířené podmíněné očekávání
nezáporného potenciálu. Z EV(X_0)=V(n)<∞ a nezáporného
Tonelliho součtu přes historie indukcí plyne EV(X_m)≤V(n)
a konečnost každého z těchto očekávání. Proto lze následně
používat i obvyklé integrabilní podmínění. Nepředpokládáme
neodůvodněně globální E|F(X_m)| z pouhé konečnosti v jednotlivých
stavech; pro důkaz stačí právě toto integrované sevření potenciálu.

Proces z tištěné poznámky je

```
Z_m=V(X_m)+min(m,R).
```

Je adaptovaný, nezáporný a integrabilní; min(m,R)≤m.
Rozdíl časových členů je přesně
min(m+1,R)−min(m,R)=[R>m]. Přičtením k předchozí
podmíněné nerovnosti proto E(Z_{m+1}|H_m)≤Z_m.
Věžová identita pak dává supermartingale i vůči jeho vlastní
historii. To dokazuje celý Jansonův matematický dovětek.
Po očekávání a vynechání nezáporného potenciálu opět
E min(m,R)≤V(n), takže souhlasí s časovou indukcí.

Původní poznámka P099 navíc uváděla ostrý příklad: kroky D=±1
s nezávislým kladným průměrem d>0 a konstantní g_j=d.
Právě dokázaná mez dává ER≤n/d a ukončení. Součet
Σr≥1[R≥r]D_r je absolutně integrovatelný, protože jeho
absolutní součet je R. Nezávislost nového D_r na události
R≥r dává očekávání dER; po ukončení je součet bodově n.
Tedy ER=n/d. I tento převzatý příklad má přesný argument.

## Bibliografické výjimky a závěr

[Autorská stránka Wigdersona](https://www.math.ias.edu/avi/node/765)
potvrzuje Karp–Upfal–Wigderson, titul The Complexity of Parallel
Search, JCSS36(2),1988,225–253. Konkrétní p252 se však
nepodařilo přímo prohlédnout: stažení veřejně odkazovaného PDF
vrátilo403; webový renderer poskytl odkaz bez viditelného obrazu.
Matematika98 je úplně dokázána výše, přesný obsah citované p252
zůstává výslovnou bibliografickou výjimkou.

Přesné znění cvičení1.6 v Motwani–Raghavan, Randomized Algorithms
(1995), nebylo při krátké kontrole získáno v primárním originále.
Stejně není nezávisle doložen historický původ osobní poznámky
připsané Svante Jansonovi. Obě atribuce se výslovně vynechávají;
jejich potřebná matematická tvrzení mají úplný vlastní důkaz.

Manifest `mpr-098-099-drift-errata.json` pokrývá6lokálních vrstev
a3TeX zdroje. Shody p21 patří následujícím102/103 a budou
posouzeny tam; ostatní shody jsou rovněž mimo98–99. Žádná
známá oprava tohoto bloku, nový nález nebo kandidát nevznikl.

P099 lze nyní znovu uzavřít s oběma uloženými přechody stavu
a se zachovanou původní evidencí. Celé98–99 jsou reviewed
s přesně vypsanými bibliografickými výjimkami. Žádný matematický
výpočet, census nebo restart neproběhl. File404 má nyní každý
obsahový blok92–99 doložen; file41 zůstává partial pro100–104.

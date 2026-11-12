# MPR100–102 — nekonečný čas, geometrické ocasy a kupóny

D198–D200, 7. listopadu 2026. Původní zadání p21/file41
a odpovědi p385/file405 přímo zobrazeny; porovnány s PS
p21/file27 a p41/file47. Původní errata all4b p3 a9,
all4f5 p10 a odpovídající TeX potvrzují tři níže uvedené
známé změny. Žádný matematický běh.

## 100(a,b): každý člen včetně hmotnosti v nekonečnu

Nechť T∈{1,2,…,∞}, p_t=P(T=t), Σt<∞p_t+p_∞=1.
Pro konečné celé m≥1 je přesně

```
E min(m,T)=Σt=1..m t p_t + mΣt=m+1..∞,t<∞ p_t + m p_∞.
```

Všechny členy jsou nezáporné a celý výraz je≤m. To je
právě tištěné rozepsání s koeficientem m i u p_{m+1},p_{m+2},…
a u p_∞. Vynechání druhého a třetího členu dává dolní mez
Σt=1..m t p_t; bodová min(m,T)≤T dává horní mez ET
v rozšířeném nezáporném smyslu. Použitá konvence je
∞·p=∞ pro p>0, ale0 pro p=0, přesně jako v odpovědi.

Pokud p_∞=0, rostoucí dolní součet konverguje k ET;
sevření tedy dokazuje(a), ať je ET konečné nebo nekonečné.
Pokud p_∞>0, je ET=∞ a z výše uvedeného skutečného
rozpisu plyne E min(m,T)≥m p_∞→∞. Samotný konečný
dolní součet by v tomto případě nestačil; tento případ
je nyní výslovně doložen pomocí členu uvedeného i v(b).

Alternativně bodová identita min(m,T)=Σr=1..m[T≥r],
včetně T=∞, dává monotónní limitu všech nezáporných
indikátorů rovnou T. Je to tentýž limitní argument, který
byl vD197 samostatně doložen pro ukončení driftového procesu.
Pro(b) z ET≥E min(m,T)≥m p_∞ pro každé m okamžitě
plyne, že konečné ET nutí p_∞=0. Nic se nedělí nekonečnem.
Prázdná truncation m=0, pokud ji připustíme, dává0 a nemění limitu.

E128 je pouze zveřejněné doplnění závěrečné závorky z19.6.2023:
`0).`→`0).)`. PDF i PS mají původní chybějící závorku;
all4b p9 a TeX4b.385 uvádějí opravu. Matematická konvence
je jasná už z vnitřního podmíněného výrazu. Není to nový nález.

## 101: přesná distribuce, střední hodnota a konvergence MGF

Uvažujeme konečné m≥1 a0<p_k≤1; tyto podmínky určují
uvedená geometrická rozdělení a v důkazu zajišťují existenci
minima p i kladnou konečnou μ. Pro p_k=0 by uvedené
hmotnosti měly součet0, takže by nešlo o zadané rozdělení.
Pro p_k=1 je X_k=1 deterministicky; nultá mocnina v prvním
geometrickém členu má standardní hodnotu1.

Pro q_k=1−p_k a n≥1 je P(X_k≥n)=q_k^(n−1).
Součet nezáporných ocasových indikátorů proto dává

```
E X_k=Σn≥1 q_k^(n−1)=1/(1−q_k)=1/p_k,
μ=EΣk X_k=Σk1/p_k.
```

Pro p=min_k p_k a0<t<p je e^(−t)>1−t>1−p_k,
protože t<p≤p_k.
Tedy q_k e^t<1 a geometrická MGF řada skutečně konverguje:

```
E e^(tX_k)=Σn≥1 p_k q_k^(n−1)e^(tn)
         =p_k/(e^(−t)−1+p_k)
         <p_k/(p_k−t).
```

Oba jmenovatele jsou kladné; e^(−t)−1>−t plyne ze
striktní konvexity exponenciály pro t>0. Nezávislost dává
E e^(tX)=Πk E e^(tX_k). To ověřuje každou rovnost a
ostrou nerovnost první tištěné věty včetně případů p_k=1.

## 101: každá logaritmická nerovnost známého doplnění

Zvolme0<θ<1 a t=θ/μ. Protože μ≥1/p, je1/μ≤p
a t<1/μ≤p, tedy předchozí MGF výpočet platí. Pro s>t
definujme h(s)=s ln(1−t/s). S u=t/s∈(0,1) má derivaci

```
h′(s)=ln(1−u)+u/(1−u).
```

Výraz na pravé straně má jako funkce u derivaci
u/(1−u)²≥0 a limitu0 při u↓0. Je tedy nezáporný,
takže h je rostoucí. Jelikož p_k≥p≥1/μ, dostaneme
přesně celý tištěný řetězec

```
p_k ln(1−t/p_k) ≥ p ln(1−t/p)
 ≥ (1/μ)ln(1−tμ) = (t/θ)ln(1−θ).
```

Všechny argumenty logaritmů leží v(0,1), takže žádná
substituce nepřekračuje doménu. E129 zaznamenává, že
právě tento řetězec byl oficiálně přidán9.6.2022 v odpovědi101
na historické p196. PS2019 jej ještě nemá, naše4B jej
již obsahuje. Původní all4f5 p10 i TeX4f5.196 byly
přímo posouzeny. Jde o známé doplnění, nikoli nový nález.

## 101: každý exponent, optimalizace a všechny kraje

Pro r>1 aplikujeme exponenciální Markov, ekvivalentní původní
sv1 1.2.10–(25), který byl přímo posouzen vD195. Všechny
tištěné kroky nyní mají následující odůvodnění:

```
P(X≥rμ) ≤ e^(−rtμ) E e^(tX)
 ≤ exp(−rθ−Σk ln(1−t/p_k))
 ≤ exp(−rθ−Σk (t/p_k)ln(1−θ)/θ)
 = exp(−rθ−ln(1−θ)).
```

Při přechodu z logaritmické dolní meze na exponent se
znaménko otočí kvůli minus před součtem. Poslední rovnost
používá Σk(t/p_k)/θ=tμ/θ=1. Nerovnosti nevyžadují,
aby rμ bylo celé; událost je X≥ceil(rμ).

Funkce−rθ−ln(1−θ) má derivaci−r+1/(1−θ), druhou
derivaci1/(1−θ)²>0 a pro r>1 jediné minimum v
θ=(r−1)/r∈(0,1). Dosazení dává−r+1+ln r, tedy
právě P(X≥rμ)≤r e^(1−r). Pro r=1 je pravá strana1
a tvrzení je triviální; nemusíme nepřípustně vkládat t=0
do dřívějšího ostrého odhadu. Tentýž případ plyne také
limitou θ↓0. Žádné tvrzení pro prázdný součet m=0
se do domény normalizovaného μ nepřidává.

Všechny deterministické parametry p_k=1 jsou zahrnuty:
pak X=μ=m, takže pro r>1 je ocas prázdný a pro r=1
má pravděpodobnost1. Obecně dolní kraj X≥m je rovněž
kompatibilní s mezí; není vyžadována kladná variance.

## 101: celý dovětek o ostrosti

Pro m=1 a0<p<1 je přesně

```
P(X≥r/p)=(1−p)^(ceil(r/p)−1).
```

Jde o součet geometrické řady od ceil(r/p) a správně
obsahuje minus1. Pro pevné r≥1 máme
p(ceil(r/p)−1)→r. Z integrálních nerovností
−p/(1−p)≤ln(1−p)≤−p plyne ln(1−p)/p→−1.
Logaritmus této pravděpodobnosti tedy konverguje k−r,
a pravděpodobnost k e^(−r), přesně jako v dovětku.

Výraz „nearly sharp“ je zde kvalitativní: odhad r e^(1−r)
má stejný exponenciální faktor e^(−r), liší se násobkem er.
Netvrdíme, že poměr obou mezí konverguje k1 nebo že je
prefaktor r optimální. Ve dvojitém smyslu nejprve p↓0
a pak r→∞ je logaritmická rychlost právě−r; nelze ji
uniformně nahradit rychlejší−c r pro c>1 s pouhým
polynomiálním prefaktorem. To přesně vymezuje doložený
matematický obsah poznámky.

Historická osobní atribuce řešení Svante Jansonovi nemá
v tomto bloku nezávisle získaný primární doklad; výslovně
ji bibliograficky vynecháváme. Každý krok řešení je doložen.

## 102: model čekání a úplná dominace

Pro každý parametr n uvažujeme konečné m=m(n)≥1 a
konečné s_k=s_k(n)≥1. T_k znamená počet pokusů na
získání k-tého kupónu poté, co již bylo získáno prvních k−1,
nikoli celkový počet pokusů od začátku. Celkový čas je T=Σk T_k.
Na každém dosud neúspěšném pokusu ve fázi k je úspěch
nezávisle generován s pravděpodobností alespoň1/s_k.

Pokud je tato pravděpodobnost stálá q_k, jsou T_k
nezávislé geometrické s průměry1/q_k≤s_k, což je
přímo model tištěné odpovědi. Stejný závěr stačí i při
případném měnění jednotlivých úspěšnostních pravděpodobností
nad jejich dolní mezí. Pro úplnost zkonstruujme dominaci:
pro každou fázi k vezmeme samostatnou nekonečnou řadu
nezávislých uniformních čísel U_kj∈[0,1]. Skutečný j-tý
pokus uspěje, když U_kj nepřekročí jeho příslušnou
podmíněnou pravděpodobnost q_kj≥1/s_k. Tím se
zachová zákon úspěchů podle jejich podmíněných pravděpodobností.

Nechť G_k je první index, kdy U_kj≤1/s_k. Pak G_k
jsou nezávislé geometrické s parametry1/s_k a bodově
T_k≤G_k: jestliže fáze neskončila dříve, musí skončit
nejpozději při tomto pokusu. Každá G_k je konečná
skoro jistě, protože P(G_k>j)=(1−1/s_k)^j→0.
Konečný počet fází tedy také skončí. To poskytuje
všechny potřebné dominance bez neodůvodněné nezávislosti
případných složitějších skutečných čekání.

## 102: celkový a.s. čas se správným prahem

Označme S=Σk s_k=EΣk G_k. Pro n≥e zvolme r=ln n≥1.
Z bodové T≤ΣG_k a úlohy101 plyne

```
P(T≥S ln n) ≤ P(ΣG_k≥S ln n)
             ≤ (ln n)e^(1−ln n)=e(ln n)/n →0.
```

Takže všechny kupóny jsou získány přísně před S ln n
a.s., přesně jako v zadání. Celočíselné čekání a reálný
práh jsou kompatibilní díky neostré události selhání.
Pokud se použije přímo geometrický model s μ=ET≤S,
událost T≥S r je podmnožinou T≥μr; to vysvětluje
i přesné tištěné dosazení μ≤s1+⋯+sm. Mez nezávisí
na počtu m nebo hodnotách s_k, a proto platí i při
jejich závislosti na n bez další podmínky pro první závěr.

## 102: každá fáze, libovolná rostoucí f a společné q.s.

Pro libovolnou rostoucí f(n)→∞ položme r=f(n)ln n.
Úloha101 s jediným G_k dává uniformně v k

```
P(T_k≥s_k r) ≤ r e^(1−r).
```

Pro r≥2 platí ln r≤r/2: v r=2 je ln2≤1 a derivace
1/r je na tomto intervalu≤1/2. Tedy
r e^(1−r)≤e exp(−r/2)=e n^(−f(n)/2).
Pro každý pevný K je f(n)/2≥K pro všechna dostatečně
velká n, takže každá fáze má superpolynomiálně malou chybu.
Tento argument platí i pro velmi rychle rostoucí f; nepředpokládá,
že samotný prefaktor f(n)ln n je polynomiální.

Zadaná volba f(n)=ln ln n je rostoucí a jde do∞.
Pro m(n)≤C n^1000 dá unijní mez

```
P(některá fáze překročí s_k ln n ln ln n)
 ≤ C e n^(1000−(ln ln n)/2).
```

Pro požadované pevné K stačí nakonec(ln ln n)/2≥K+1000.
Tím je společný výrok pro všechny k≤m q.s.; meze jsou
uniformní v k a nezávislost událostí selhání různých fází
se pro tento poslední krok nepotřebuje. Neostré horní
ocasy případně zahrnují rovnost, což horní mezi nevadí.

E130 je zveřejněné upřesnění4.4.2026: a.s./q.s. v102
odkazují na implicitní parametr n. V původním PDF2022
i PS tato věta chybí; originální all4b p3 a TeX4b.21
ji přímo potvrzují. Výše jsou všechny závislosti na n
vypsány, takže žádný nový kandidát z této známé věci nevzniká.

## Přesný rozsah

Celé100(a,b),101 s každým mezikrokem a dovětkem a102
se všemi kvantifikátory jsou doloženy. E128–E130 jsou
pouze známé opravy, bez karet nebo chybových lokací.
Šest vrstev errat a3TeX zdroje jsou zaznamenány v
`mpr-100-102-geometric-errata.json`; zbývající shody
patří103/104 nebo nesouvisejícím pozdějším oddílům.

Jedinou novou bibliografickou výjimkou je historická
Jansonova atribuce101. Žádný nový nález, kandidát,
numerický běh nebo restart. File41 zůstává partial
pro103–104; file405 pro103–105.

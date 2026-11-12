# D109 — celá MPR6 a úplný odkaz MPR20

6. listopadu 2026. MPR6: celé zadání13/file33 a odpověď
371–372/file391–392. MPR20: celé zadání14/file34 a odpověď
373/file393. Všechny tyto originály byly přímo zobrazeny;
také odpovídající místa autorova Pre-Fascicle5A na13–14
a28–29/file19–20,34–35. Níže je úplný argument obou úloh,
včetně konkrétního tištěného příkladu v odpovědi20.
Žádný numerický běh není potřeba.

## MPR6: první distribuce a její normalizace

Nechť n≥2. Každý binární vektor s právě dvěma jedničkami
má pravděpodobnost1/(n−1)², nulový vektor pravděpodobnost
(n−2)/(2n−2) a všechny ostatní vektory0. Všechny hmotnosti
jsou nezáporné. Součet je přesně

```
binom(n,2)/(n−1)²+(n−2)/(2n−2)
 = n/(2(n−1))+(n−2)/(2(n−1))=1.
```

Jde tedy o platné rozdělení pro každý uvedený n≥2.
Pro danou souřadnici j existuje n−1 dvoujedničkových
vektorů s X_j=1, proto

```
p₁=P(X_j=1)=1/(n−1),
p₀=P(X_j=0)=(n−2)/(n−1).
```

Pro různá i,j existuje právě jeden podporovaný vektor
mající obě tyto souřadnice1. Proto P(X_i=X_j=1)=p₁².
Zbývající tři konfigurace nevyžadují žádnou domněnku:

```
P(1,0)=p₁−p₁²=p₁p₀,
P(0,1)=p₁−p₁²=p₀p₁,
P(0,0)=1−2p₁+p₁²=p₀².
```

To jsou všechny čtyři atomy dvojice, takže každé dvě
souřadnice jsou nezávislé. Všechny vytištěné dílčí
pravděpodobnosti odpovědi6 jsou tím dokázány přímo.

Pro n≥3 má událost X_i=X_j=X_l=1 u tří různých indexů
pravděpodobnost0, kdežto součin jejích marginálních
pravděpodobností je p₁³>0. Stejný přímý svědek funguje
pro každý dostupný počet3≤k≤n: k určených jedniček
má pravděpodobnost0, ale součin p₁^k je kladný.
Není tedy k-násobná nezávislost pro žádný takový k.

Pro okraj n=2 je vektor deterministicky11, p₁=1,p₀=0,
a uvedené čtyři rovnosti stále platí. Žádná trojice
různých souřadnic zde neexistuje. Tvrzení o neexistenci
vyšší nezávislosti se vztahuje k dostupným řádům k≤n;
nepoužívá se k prohlášení dvousouřadnicové konstanty
za závislou na neexistující třetí souřadnici.

## Celá MPR20: momentové kritérium bez skrytých vzorů

Pro binární veličiny X₁,…,X_k označme p_j=E X_j=P(X_j=1).
Předpoklad úlohy20 říká pro každou podmnožinu J,
že E(∏_{j∈J}X_j)=∏_{j∈J}p_j. Pro J prázdnou jsou
oba součiny1. Všechny veličiny jsou omezené, takže
všechny potřebné střední hodnoty existují.

Fixujme libovolný binární vzor. Nechť I jsou jeho
jedničkové a Z nulové souřadnice, I∪Z={1,…,k},I∩Z=∅.
Indikátorem tohoto jediného vzoru je přesně

```
∏_{i∈I} X_i ∏_{j∈Z}(1−X_j).
```

Roznásobením konečného součinu a linearitou dostáváme

```
P(určený vzor)
 = Σ_{T⊆Z}(−1)^|T| E(∏_{i∈I∪T}X_i)
 = Σ_{T⊆Z}(−1)^|T| ∏_{i∈I∪T}p_i
 = ∏_{i∈I}p_i ∏_{j∈Z}(1−p_j).
```

Tím má každý z2^k společných atomů přesně součinovou
pravděpodobnost, což je definice nezávislosti. Důkaz
neobsahuje dělení žádným p_j nebo1−p_j, a zahrnuje
tedy i deterministické okraje0 a1. Pro libovolné jiné
podmnožiny hodnot dostaneme tutéž faktorizaci součtem
příslušných atomů. Naopak nezávislost samozřejmě
u jedničkových událostí dává uvedený momentový předpoklad;
nejde jen o postačující kritérium pro jediný vzor.

Konkrétní příklad vytištěný v odpovědi20 pro k≥4 je
rovněž ověřen v každém členu:

```
X₁(1−X₂)(1−X₃)X₄
 = X₁X₄−X₁X₂X₄−X₁X₃X₄+X₁X₂X₃X₄,
E(...) = p₁p₄−p₁p₂p₄−p₁p₃p₄+p₁p₂p₃p₄
       = p₁(1−p₂)(1−p₃)p₄.
```

Případ k<4 nepoužívá tento čtyřčlenný příklad, ale
obecný důkaz výše. Odkaz20 v odpovědi6 je tedy věcně
i stránkově správný. Celá úloha20 a odpověď jsou zde
uzavřeny, nikoli jen předpokládány jako cizí lemma.

## MPR6: přesná trojnásobná nezávislost

Druhé zadání vyžaduje závislost čtyř různých souřadnic,
takže jeho věcný rozsah je n≥4. Pro takové n položme

```
a₀=2 binom(n−2,3),
a₁=binom(n−2,2),
a₃=1,
a_j=0 pro ostatní j,
P(X=x)=a_{νx}/(n−2)³.
```

Všechny hmotnosti jsou nezáporné, jmenovatel je kladný
a rozdělení závisí jen na νx, jak zadání požaduje.
Jeho součet přes všechny vektory je

```
[a₀+n a₁+binom(n,3)]/(n−2)³.
```

Čitatel se rovná

```
(n−2)/6 · [2(n−3)(n−4)+3n(n−3)+n(n−1)]
 = (n−2)/6 · [6n²−24n+24]
 = (n−2)³.
```

Je tedy normalizovaný přesně na1. Označme p=1/(n−2).
Jedničkový marginál má čitatel

```
a₁+binom(n−1,2)
 = (n−2)(n−3)/2+(n−1)(n−2)/2
 = (n−2)²,
```

tedy P(X_i=1)=p. Pro dvě určené jedničky existuje
právě n−2 podporovaných vektorů váhy3, takže
P(X_i=X_j=1)=(n−2)/(n−2)³=p². Pro tři určené
jedničky existuje jediný takový vektor, a pravděpodobnost
je1/(n−2)³=p³.

To není konec kontroly: potřebujeme všechny konfigurace
trojice, nikoli jen111. Pro r určených jedniček a s
určených nul, kde r+s≤3, stejný konečný rozvoj jako
v MPR20 dává

```
P(r určených jedniček a s určených nul)
 = Σ_{T⊆Z}(−1)^|T| p^{r+|T|}
 = p^r(1−p)^s.
```

Všechny jedničkové momenty do řádu3 byly právě spočteny,
včetně prázdného momentu1. Dvojice i trojice tedy mají
úplná součinová rozdělení a jsou nezávislé.
Naopak čtyři určené jedničky mají pravděpodobnost0,
protože rozdělení nepodporuje váhu≥4, zatímco p⁴>0.
Požadovaná čtyřnásobná nezávislost proto selhává.

V nejmenším případu n=4 je a₀=0,a₁=a₃=1 a jmenovatel8:
jde přesně o rovnoměrné rozdělení osmi vektorů liché parity,
každá trojice je férová a1111 má nulovou pravděpodobnost.
To přímo pokrývá hraniční nulovou hmotnost a₀.
Pro n=3 by tentýž vzorec dal pouze konstantu111 a čtyři
různé souřadnice by opět neexistovaly; pro n=2 se uvedený
trojnásobný vzorec s nulovým jmenovatelem nepoužívá.
Žádný z těchto nedostupných řádů se neprezentuje jako
skutečná vyšší závislost.

## Errata a přesně uzavřené strany

Pro obě úlohy byly porovnány všechny šest místních
vrstev errat a tři dostupné původní TeXy. Žádná oprava
MPR6 ani MPR20 nebyla nalezena. Opravy sousedních
MPR5,18,21,24 nebo stejně číslovaných úloh jiných oddílů
nejsou připsány tomuto rozsahu. Samostatná bibliografická
výjimka zde není: matematický odkaz20 byl přečten celý
a jeho úplný důkaz je součástí tohoto záznamu.

D109 uzavírá celé MPR6 a MPR20 včetně odpovědí.
File391/tištěná371 nyní lze uzavřít celý společně
s D105–D108: obsahuje části odpovědí2–6 a všechny jsou
hotové. File33 má nadále otevřené7–13. File34 se tím
uzavírá pouze pro úlohu20, file392 pouze pro dokončení
odpovědi6 a file393 pouze pro odpověď20. Zobrazení
ostatních částí těchto stran není jejich ověřením.
Žádný nový nález, kandidát, početní běh nebo restart.

# Obnova §4.2.2: všechny relace (21)–(39) a celé úlohy 8–9

7. listopadu 2026. Původní 233–234, 243 a 614 znovu osobně přečteny
v obrazech. Všechny neostré hranice, oba předpoklady (33), původní
i opravené vstupy úlohy 8 a každý mezikrok odpovědi 9 jsou níže.
Žádný experiment nebyl opakován. C0083 je převzatý existující nález.

## Definice, uložený exponent a přesná trojice možností

Pišme `B_u=b^(e_u−q)>0`; pro každou dovolenou reprezentaci,
normalizovanou i nenormalizovanou, platí `u=f_u B_u`, `|f_u|<1`,
tedy `|u|<B_u`. Parametr `ε>0` je reálný a není sám zaokrouhlován.
Přesné hodnotové rozdíly v definicích nejsou plovoucí odečítání.

Každá definice samostatně:

| Vztah | Přesný obsah |
| --- | --- |
| (21) `u≺v(ε)` | `v−u>ε max(B_u,B_v)` |
| (22) `u~v(ε)` | `|v−u|≤ε max(B_u,B_v)` |
| (23) `u≻v(ε)` | `u−v>ε max(B_u,B_v)` |
| (24) `u≈v(ε)` | `|v−u|≤ε min(B_u,B_v)` |

Nechť `D=v−u` a `H=ε max(B_u,B_v)>0`. Reálná přímka je
disjunktní sjednocení `D>H`, `−H≤D≤H`, `D<−H`. Právě tyto
tři případy dávají ≺,~,≻, a proto platí tvrzení o právě jedné
z nich včetně obou přesných hraničních hodnot ±H. Nejde o
čtyři disjunktní možnosti: `min≤max` dává `≈⇒~`.

Silnější vztah je skutečně silnější. Například v b=10,p=2,q=0
vezměme `u=(0,.50)=.5`, `v=(1,.06)=.6`, ε=.01. Rozdíl .1
je roven `ε max(B_u,B_v)=.1`, ale převyšuje
`ε min(B_u,B_v)=.01`. Platí ~, neplatí ≈.

Relace jsou vlastnostmi reprezentací, ne pouze hodnot. Při
ε=.05 a `w=(0,.60)` má `u=(0,.50)` proti w rozdíl .1>.05,
takže u≺w. Tatáž hodnota zapsaná `u'=(1,.05)` má s w práh
pro ~ rovný .5 a splní `u'~w`. Změna exponentu bez změny
hodnoty tudíž může změnit odpověď. Nula rovněž nese zadaný
exponent; nenormalizovanou nulu z úlohy 8 nelze tiše přepsat.

## Všechny čtyři interpretace pomocí okolí

Originál má **uzavřené** `N(u)={x:|x−u|≤εB_u}`,
tedy interval `[u−εB_u,u+εB_u]`. Stejné ε je v obou okolích.
Zápis `N(u)<v` znamená, že každý jeho prvek je menší než v;
díky zahrnutí koncového bodu je to ekvivalentní `u+εB_u<v`.
Obdobně `u<N(v)` znamená `u<v−εB_v`.

1. Konjunkce těchto dvou podmínek je
   `v−u>εB_u` a `v−u>εB_v`, tedy přesně (21).
2. `u∈N(v)` znamená `|u−v|≤εB_v`; `v∈N(u)` znamená
   `|u−v|≤εB_u`. Jejich disjunkce je (22), protože alespoň
   jedna mez platí právě tehdy, když platí větší z obou mezí.
3. `u>N(v)` je `u>v+εB_v` a `N(u)>v` je `u−εB_u>v`.
   Jejich konjunkce je `u−v>ε max(B_u,B_v)`, tedy (23).
4. Konjunkce obou podmínek příslušnosti z bodu 2 je právě
   `|u−v|≤ε min(B_u,B_v)`, tedy (24).

Změna ε mění obě okolí; potlačení parametru v zápisu N je pouze
zkratka, jak výslovně říká následující závorka v knize.

## Každý důsledek (25)–(32)

| Vztah | Argument v celém vytištěném rozsahu |
| --- | --- |
| (25) | `u≺v` i `v≻u` požadují tutéž kladnou mezeru v−u nad stejným symetrickým maximem. |
| (26) | `min(B_u,B_v)≤max(B_u,B_v)` a ε>0 dovolí zvětšit mez. |
| (27) | `|u−u|=0≤ε B_u`, včetně nuly a nenormalizované reprezentace. |
| (28) | `v−u>ε max(B_u,B_v)>0`, tedy u<v. |
| (29) | Je-li `ε₁≥ε₂>0`, pak `ε₁ max≥ε₂ max`; ostrá mez nad větším prahem je i nad menším. Rovnost ε₁=ε₂ nevadí. |
| (30) | Je-li `0<ε₁≤ε₂`, pak mez s maximem lze zvětšit z ε₁ na ε₂; obě rovnosti zůstávají dovoleny. |
| (31) | Stejný argument s minimem dokazuje zachování ≈ při zvětšení ε. |

Pro (32) položme `ε*=min(ε₁,ε₂)>0`. Z první hypotézy
`v−u>ε₁ max(B_u,B_v)≥ε*B_u`; z druhé
`w−v>ε₂ max(B_v,B_w)≥ε*B_w`. Po sečtení je

`w−u>ε*(B_u+B_w)>ε*max(B_u,B_w)`.

Druhá ostrá nerovnost využívá kladnost obou B. To je přesně
u≺w(ε*), bez předpokladu normalizace nebo stejného exponentu.

## Celá úloha 9 a každý tištěný krok (33)

**Oba předpoklady jsou ≈**, nikoli ~. Úloha 9 žádá důkaz (33)
a nemožnost obecně zesílit jeho závěr na ≈. Každá nerovnost
v odpovědi na 614 je tato:

1. `|u−w|≤|u−v|+|v−w|` je trojúhelníková nerovnost.
2. Součet vpravo je nejvýše
   `ε₁ min(B_u,B_v)+ε₂ min(B_v,B_w)` použitím obou hypotéz.
3. Ten je nejvýše `ε₁ B_u+ε₂ B_w`, protože první minimum
   nepřevyšuje B_u a druhé B_w, oba násobitele jsou kladné.
4. Poslední součet je nejvýše
   `(ε₁+ε₂)max(B_u,B_w)`, odděleným zvětšením obou B
   na stejné maximum a následným vytknutím.
5. Podle definice (22) je závěr právě `u~w(ε₁+ε₂)`.

Všechna čtyři porovnání jsou neostrá, jak ukazuje původní sazba.
Není použita nepravdivá tranzitivita ~ při nezměněné toleranci.

Konkrétní úplný protipříklad k zesílení: b=10,p=2,q=0,
`u=(0,.50)`, `v=(1,.05)`, `w=(1,.06)`, ε₁=ε₂=.01.
Všechny zlomky mají dvě místa; nenormalizované v,w jsou výslovně
dovoleny. Hodnoty jsou .5,.5,.6 a B jsou 1,10,10.

První rozdíl 0 splňuje `0≤.01 min(1,10)=.01`.
Druhý rozdíl .1 splňuje `.1≤.01 min(10,10)=.1` na hranici.
Závěrečný rozdíl .1 nesplňuje `.1≤.02 min(1,10)=.02`,
ale splňuje `.1≤.02 max(1,10)=.2`. Hypotézy i slabší závěr
tedy platí a silnější závěr neplatí.

Vágní exponentový návrh v tištěné odpovědi lze takto rozšířit
na libovolnou mezeru K≥1: ponechme hodnoty .5,.5,.6 a exponenty
0,K,K; zvolme p≥K+1, aby všechny tři reprezentace existovaly,
a `ε₁=ε₂=10^(−K−1)`. První rozdíl je 0, druhý .1 se rovná
`ε₂ 10^K`; závěrečná esenciální mez je
`2·10^(−K−1)<.1`. Tím je doložen i mechanismus poslední věty
odpovědi pro e_u libovolně menší než e_v,e_w.

## (34)–(37), přesný nulový okraj a převzetí C0083

Označme `D=|u−v|`. Pro (34) obě hypotézy znamenají
`D≤ε min(|u|,|v|)`. Jelikož `|u|<B_u`, `|v|<B_v`,
je to nejvýše `ε min(B_u,B_v)` a vychází ≈. Zahrnuje to
nuly; pak obě hypotézy vynucují D=0.

Pro (35) disjunkce hypotéz znamená
`D≤ε max(|u|,|v|)`. Monotonie maxima dává
`D≤ε max(B_u,B_v)`, tedy ~. Opět je důkaz platný i při nule,
obou znaménkách a nenormalizovaných vstupech.

Pro **nenulovou normalizovanou** hodnotu je `B_u/b≤|u|`,
čili `B_u≤b|u|`. Proto ≈ dává samostatně
`D≤ε B_u≤bε|u|` a `D≤ε B_v≤bε|v|`.
To je (36) pro u,v≠0, dokonce pro každé ε>0 bez požadavku ε<1.

Doslovné zahrnutí normalizované nuly je již doložené **C0083**.
Celý existující důkaz v `C0083-essential-zero-boundary.md` byl
znovu přečten; odpovídá přesně nynějšímu rozsahu. Definice 215
v obraze výslovně normalizuje nulu s nejmenším exponentem.
V b=10,p=8,q=0, e v 0..99 mají

`u=(0,.00000000)=0`, `v=(0,.10000000)=.1`, `ε=.1<1`

oba B rovna 1. Hypotéza ≈ je `.1≤.1`, první závěr (36)
je nepravdivé `.1≤10·.1·0=0`. Neprovádí se žádná plovoucí
operace, tedy ani výjimka exponentu.

Oprava u,v≠0 je dokázána výše. Alternativní oprava `ε<1/b`
funguje i s nulou: kdyby právě jedna hodnota byla nulová,
normalizace druhé by dávala
`B_v/b≤|v|≤ε min(B_u,B_v)≤εB_v`, tedy ε≥1/b, spor.
Jsou-li obě nuly, oba závěry platí; ostrý práh 1/b je potřebný,
neboť protipříklad má právě tuto toleranci.

(37) tento problém nemá. Jsou-li oba argumenty nenulové,
`max(B_u,B_v)≤b max(|u|,|v|)` a ~ dává
`D≤bε max(|u|,|v|)`, ekvivalentní vytištěné disjunkci.
Je-li právě jeden argument nula, jeho normalizovaný exponent
je nejmenší; větší B proto patří nenulové hodnotě nebo je stejné.
Stejný argument funguje pro tuto hodnotu a disjunkce platí.
Při obou nulách je D=0. Ani (37) nepotřebuje ε<1.

Všechny čtyři vrstvy errat a aktuální TeX byly znovu prohledány.
Oprava z 15. května 2026 následuje **za (37)** a (36) nemění;
plán konvence pro čtvrté vydání z roku 1999 rovněž nemění
tento konkrétní rozpor ve třetím vydání. C0083 se neduplikuje.

## Opravená mez za (37) a celý krok (38)

Převezměme z předchozí obnovy `B=b^(e−1)≤|x|<b^e`,
`h=b^(e−p)`, `η=ε₀/2=b^(1−p)/2`, `ρ=R(x)−x`.
Pro x≠0 již máme `|ρ|≤h/2=ηB` a `B≤|x|`.
Navíc `|R(x)|≥B`: na kladné straně jakákoli hodnota pod B
je od x vzdálenější než B; na záporné platí stejný argument
pro −B a absolutní velikost. Je to důsledek nejbližšího R,
nikoli dodatečný předpoklad o volbě půlek.

Proto `|ρ|≤η|x|` a `|ρ|≤η|R(x)|`, tedy

`|x−R(x)|=|ρ|≤η min(|x|,|R(x)|)`.

Pro x=0 je také pravdivá, obě strany jsou 0. Neostrost je
skutečně potřebná: pro b=2,p=2 a x=5/4 je R(x)=1, protože
půlka mezi 1 a 3/2 vybírá sudé K=2 u hodnoty 1. Pak
`|ρ|=1/4=η min(5/4,1)`. Přesný kladný příklad vyvrací
původní ostré znaménko, které je **známě opraveno 15. května 2026**.
Obraz errata i aktuální TeX souhlasí; nejde o nový nález.

Z této meze a (34) plyne (38) s ε=η. Je přitom nutné vyjasnit
zápis: přesné x nemusí mít p cifer. V (38) a následném `u+v`
je tedy relace přirozeně rozšířena na přesnou reálnou hodnotu
opatřenou exponentem, nikoli na falešné tvrzení, že x již je
strojově reprezentovatelné. Pro x≠0 zvolíme jeho přirozené
pásmo, tedy `B_x=b^e>|x|`; pro x=0 lze použít nulový exponent
formátu. Definice (21)–(24) i důkaz (34) potřebují pouze
kladné B a `|x|<B_x`, nikoli konečnou délku jeho zlomku.
Takto je rozšíření přesné a (38) platí. Pomocný exponent přesného
x nemusí být uložitelný; skutečný výsledek R musí být definován.

Dosazení x=u+v dává `u⊕v≈u+v(η)` pomocí symetrie absolutního
rozdílu a minima. Totéž samostatně platí pro x=u−v, uv a u/v;
poslední vyžaduje v≠0. Nulový vnitřní výsledek dává dvě stejné
nuly, nikoli použití chybného (36). Všude jde o ideální R,
nikoli o potvrzení vadné implementace C0251.

## Obě relativní meze a celý závěr (39)

Nechť `L=(u⊗v)⊗w`, `T=u⊗(v⊗w)` a
`K=2ε₀/(1−ε₀/2)²`. Pro nenulové uvw je z (19)
`|L/T−1|<K`, tedy násobením kladným |T|
`|L−T|<K|T|`. Stejný důkaz čtyř faktorů s prohozeným
čitatelem a jmenovatelem dává `|T/L−1|<K`, tedy
`|L−T|<K|L|`. To samostatně zdůvodňuje větu o prohození
obou asociací; jedna jednostranná relativní mez by sama nestačila.

Je-li `ε≥K`, obě ostré meze implikují neostré
`|L−T|≤ε|L|` a `|L−T|≤ε|T|`. Podle (34) je
`L≈T(ε)`, přesně (39). Originál má **ε≥K**, ne pouze ε>K.
Pro uvw=0 a definované vnitřní operace jsou oba výsledky nula,
takže (39) platí přímo z (27); předchozí ostrý relativní výpočet
se na 0/0 nepoužívá. Ani zde není potřeba ε<1 nebo (36).

V desítkové ukázce p=8 máme ε₀=10^(−7), η=5·10^(−8).
Protože `(1−η)²>1−10^(−7)>20/21`, platí

`K=2·10^(−7)/(1−η)² < 2·10^(−7)·21/20=0.00000021`.

Uvedená desetinná hodnota ε tedy splní požadavek s rezervou;
jde o přesnou racionální nerovnost, ne o zaokrouhlený odhad.

## Celá úloha 8: původní i opravené hodnoty

Zde b=10,p=8,q=0, ε=10^(−4). V tabulce `T_min` a `T_max`
jsou přesně ε krát minimum/maximum B. V žádném řádku se
hodnota nepočítá plovoucími operacemi. Všech pět podčástí
a všechny čtyři požadované relace jsou určeny.

| Varianta | Hodnoty u,v | D=|u−v| | T_min | T_max | Platné relace |
| --- | --- | --- | --- | --- | --- |
| (a) | 3.1415927, 3.1416000 | .0000073 | .001 | .001 | ~ a ≈ |
| (b) | .99997000, 1.0000039 | .0000339 | .0001 | .001 | ~ a ≈ |
| (c), původní | 6.02252·10²³, 6.0225·10²³ | 2·10¹⁸ | 10²⁰ | 10²³ | ~ a ≈ |
| (c), 1999 | 6.02214·10²³, 6.0221·10²³ | 4·10¹⁸ | 10²⁰ | 10²³ | ~ a ≈ |
| (d), původní | 6.02252·10²³, 6·10²³ | 2.252·10²¹ | 10²⁰ | 10²⁷ | pouze ~ |
| (d), 1999 | 6.02214·10²³, 6·10²³ | 2.214·10²¹ | 10²⁰ | 10²⁷ | pouze ~ |
| (e), původní e_v=32 | 6.02252·10²³, 0 | 6.02252·10²³ | 10²⁰ | 10²⁸ | pouze ~ |
| (e), 1999 e_v=28 | 6.02214·10²³, 0 | 6.02214·10²³ | 10²⁰ | 10²⁴ | pouze ~ |

V (a) jsou B oba 10; v (b) jsou 1 a 10. V (c) jsou
10²⁴ a 10²⁷, v (d) 10²⁴ a 10³¹. V (e) jsou exponenty
přesně ty ze dvou verzí zadání. Oprava 28. ledna 1999
mění v (c–e) cifry u, v (c) cifry v a v (e) také exponent
nuly 32 na 28; všechny tyto změny jsou zahrnuty.

V každém řádku je D≤T_max, takže ~ platí a disjunktnost
trojice vylučuje **oba** vztahy ≺ a ≻. V prvních čtyřech
řádcích je také D≤T_min; v posledních čtyřech D>T_min.
Tím souhlasí každá položka odpovědi 614, pro původní i opravené
zadání. Změny fyzikálních konstant v jiných odstavcích se sem
bez konkrétní změny tohoto zadání nepřenášejí.

## Rozsah uzavření

Všechny matematické kroky (21)–(39), včetně nutného přirozeného
rozšíření (38), mají výše argument. Doslovný chybný nulový okraj
(36) je již existující C0083; chybné ostré znaménko za (37)
je známé erratum. Celé úlohy 8 a 9 jsou uzavřeny včetně všech
tištěných odpovědí a podčástí. Žádný nový nález, běh nebo
ověření nedostupné bibliografie se netvrdí. Další hlavní text
je věta A a lemma T na 235; následující úlohy se nepřebírají
jen podle starého obecného označení.

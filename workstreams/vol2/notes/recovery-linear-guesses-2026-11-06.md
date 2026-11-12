# Obnova algoritmu L, věty G a úlohy 42 — V2-X0156

6. listopadu 2026. Rozsah: hlavní text 173 a 174 až po větu G,
zadání 42 na 183, celé odpovědi 42(a,b) na 598 a 42(c) na 599.
Všechny tyto sazby vizuálně znovu přečteny. Převzatý důkaz je celý
§3 v `cryptographic.md`; zde jsou rozepsány jeho vazby na každý
tištěný mezikrok, cena a krajní případy. Žádný archivní program ani
konečný soupis se nespouští. Nový nález nevznikl.

## Korelace a celý čtyřbitový příklad

R a k jsou kladná celá čísla, všechny vektorové operace níže probíhají
nad F₂. Každý správný odhad přispívá do (40) hodnotou +1 a chybný −1,
tedy s=p−(1−p)=2p−1 a p=(1+s)/2. Průměr je uniformní přes všechny
masky z. Pro náhodný G se navíc průměruje přes jeho vnitřní mince.

Tištěný G(z)=[z₁≠z₂][z₃+z₄<2] se od lineární funkce ℓ(z)=z₁+z₂
liší právě na E={0111,1011}. Pro x=1100 jsou dvě chyby ze šestnácti,
takže p=14/16=7/8 a s=12/16=3/4. Pro libovolný vektor a platí

```
s_a = [a=1100] − (1/8) Σ_{z∈E} (−1)^((a+1100)·z).
```

První člen je ortogonalita znaků: pro nenulový a+1100 se členy
spárují převrácením souřadnice s nenulovým koeficientem. Tímto vzorcem
je doložena každá z následujících šestnácti hodnot 16s_a:

| a | 16s_a | a | 16s_a |
|---|---:|---|---:|
|0000|4|1000|0|
|0001|−4|1001|0|
|0010|−4|1010|0|
|0011|4|1011|0|
|0100|0|1100|12|
|0101|0|1101|4|
|0110|0|1110|4|
|0111|0|1111|−4|

Je tedy právě pět kladných korelací a ostatních jedenáct je ≤0.
Archivní přesná tabulka `results/cryptographic.json:walsh` souhlasí.
Záměna 0001→0011 je známé erratum z 30. listopadu 1997, nikoli nález.

## L1–L3: invariant, ukončení a přesná aritmetická cena

L1 volí všech kR bitů B nezávisle a férově. Pro každý i definujme
a_i(0)=0 a a_i(c)=(−1)^G(cB+e_i) pro c≠0. Potom (41) je přesně
Hadamardova transformace tohoto pole. Obsahuje 2^k−1 členů ±1,
tedy každé h_i(b) je liché a nikdy nulové. L3 proto jednoznačně
vybere znaménko v každé souřadnici; vydá přesně 2^k slov délky R.
Shodní kandidáti v seznamu nejsou zakázáni a nedokládá se jejich
odlišnost. Všechny smyčky jsou konečné.

Po j transformačních stupních obsahuje každý částečný výstup
správný znaménkový součet přes prvních j transformovaných bitů.
Přidání dalšího bitu rozloží tento součet na dvě poloviny a spojí je
součtem a rozdílem. To indukcí dokazuje výsledek po k stupních.
Každý stupeň má 2^(k−1) dvojic a každá dvě operace: přesně k2^k
sčítání/odčítání pro každý i, tedy k2^kR celkem. Název Walsh→Hadamard
je známá oprava z 23. června 2001; matematická transformace je tatáž.
Samostatný důkaz zde uzavírá potřebný obsah dopředného odkazu 4.6.4(38).

Hodnoty G se cachují podle (i,c), nikoli přepočítávají pro každé b:
je jich přesně R(2^k−1), méně než vytištěná horní mez R2^k.
Vektory cB lze vytvořit za O(R2^k) bitových operací postupným
Grayovým pořadím a xorováním jediného řádku B; e_i se mění a vrací
jediným přepnutím. Cena zápisu výsledků je O(R2^k), L1 stojí kR.
Celkem dostáváme deklarované O(k2^kR) aritmetických operací a cenu
R2^k volání G. Transformované hodnoty mají O(k) bitů; tento účet
je účet sčítání a odčítání, nikoli tvrzení, že libovolně dlouhé
celočíselné operace mají stejnou bitovou cenu. Plná bitová cena se
z tohoto počtu bez uvedení modelu nedovozuje.

## Každá rovnost redukce na nulový vektor

Nejprve nechť G′(z)=G(z)+z_j. Skalární součin s x se tím přesně
změní na součin s x+e_j, takže počet správných odpovědí se zachová.
Ve výrazu pro h′ dá (cB+e_i)·e_j člen c·B_j+δ_ij. Tudíž

```
h′_i(b) = (−1)^δ_ij h_i(b+B_j),
x′(b) = x(b+B_j)+e_j.
```

Zde B_j je sloupec B, tudíž má potřebnou délku k. Překlad b↦b+B_j
je permutace všech k-bitových slov i při B_j=0. Znaménková identita
pro x′ používá právě nenulovost h; bez ní by přepnutí znaménka
nemuselo komplementovat Iversonovu závorku. Opakováním přes jedničky
obecného hledaného x, nebo přímou algebraickou expanzí, dostáváme

```
G′(z)=G(z)+x·z,
h′_i(b)=(−1)^x_i h_i(b+Bx),
x′(b)=x(b+Bx)+x.
```

Proto úspěšný nulový kandidát b=0 u G′ odpovídá kandidátu b=Bx
u původního G. Důkaz netvrdí, že každý kandidát v seznamu je správný.

## Úloha 42(a): rozptyl a všechny tištěné nerovnosti

Pro n≥1, konečný společný průměr μ a rozptyl σ², a nulové vzájemné
kovariance, má X=ΣX_j střední hodnotu nμ. Každé E(X_j²)=σ²+μ²;
expanze čtverce a 2·binom(n,2) kovariančních členů dává

```
E[(X−nμ)²]
 = n E(X₁²)+2Σ_{i<j}E(X_i)E(X_j)−n²μ²
 = n E(X₁²)−nμ² = nσ².
```

Pro Y=(X−nμ)² a kladný práh a=tnσ² platí bodově
Y≥Y·[Y≥a]≥a·[Y≥a]. Střední hodnota a dělení a dávají
Pr(Y≥tnσ²)≤1/t pro t>0 a σ²>0. To kontroluje obě tištěné
nerovnosti po vynechání malých hodnot a nahrazení zbývajících
hodnot prahem. Tištěné sumy přes jednotlivé hodnoty jsou doslova
zápisem diskrétního případu; bodový argument dokazuje i obecná
rozdělení a nevyžaduje diskrétní předpoklad.

Při σ²=0 je X=nμ skoro jistě. Tištěná neostrá událost je pak jistá,
takže pro t=2 dostaneme nepravdivé 1≤1/2. To je převzatý **C0068**,
nikoli nový nález. Oprava vyžaduje σ²>0 nebo ostrou událost >.
V aplikaci algoritmu se deterministický případ vyřídí přímo níže.

## Úloha 42(b): uniformita a počet řešení podle tištěné odpovědi

Pro nenulové c má v každém sloupci B skalární součin c·B_j férový
bit, protože jeden vybraný bit s koeficientem 1 jej může přepnout.
Nezávislost sloupců dává uniformní cB. Dva **různé** nenulové
vektory c,c′ jsou nad F₂ lineárně nezávislé. Doslova podle odpovědi
zvolíme i s c_i=0,c′_i=1 (v případě potřeby je prohodíme) a j s
c_j=1. Pak j≠i. Fixujeme ostatních k−2 řádků B. Požadavek cB=d
určí jednoznačně řádek j a požadavek c′B=d′ následně řádek i.
Z 2^(kR) matic tak přesně 2^((k−2)R) dává zadanou dvojici.
Pravděpodobnost je 2^(−2R), rovná součinu obou uniformních okrajů.

Při k=1 neexistují dva různé nenulové vektory, takže tento případ
je prázdný, nikoli požadavek fixovat záporný počet řádků. Chybějící
c≠c′ v zadání je známé erratum z 26. ledna 2001 a zůstává mimo nálezy.
Důkaz dává párovou nezávislost; nezávislost všech cB současně netvrdí.

## Úloha 42(c), věta G a krajní případ s=1

Pro hledaný x=0 a pevné i jsou X_c=(−1)^G(cB+e_i), c≠0, párově
nezávislé s E X_c=s a rozptylem 1−s². Posun e_i zachovává uniformitu
i nezávislost. Pro n=2^k−1, μ=s>0 a X=ΣX_c plyne z X<0, že
(X−nμ)²>n²μ². Použití právě dokázané nerovnosti proto dává

```
Pr(X<0) ≤ (1−s²)/(ns²) ≤ 1/(ns²).
```

Pro s=1 je každý X_c=1 skoro jistě a chyba nulová, bez použití
chybného nulového rozptylu v zadání42(a). Žádné h_i(0) není nula,
takže neúspěch x(0)=0 znamená alespoň jednu zápornou souřadnici.
Součet R horních mezí chyb je ≤R/((2^k−1)s²); nezávislost souřadnic
i se nepředpokládá. Jestliže 2^k>ceil(2R/s²), pak
2^k−1≥ceil(2R/s²)≥2R/s², a pravděpodobnost úspěchu je ≥1/2.
Redukce výše převádí tento výsledek na libovolný x a zachovává cenu.
Přísné >1/2 v předběžném odstavci lze zajistit větším k; samotná
věta správně používá ≥1/2. Nevzniká zaokrouhlovací mezera.

## Náhodný prediktor a bibliografický rozsah

Pro použití v P se každému volání G pro pár (i,c) přidělí vlastní
nezávislé mince, výsledek se uloží a použije ve všech b. Pak mají
X_c potřebnou párovou nezávislost a průměr s zahrnuje i mince.
Při porovnání G a G′ lze odpovídající volání svázat stejnými mincemi;
algebraická znaménková identita tak platí pro každou realizaci.
Pouhé použití jediné společné náhodné pásky opakované od začátku
ve všech voláních by párovou nezávislost obecně nezajistilo a zde
se takový postup nepřebírá. Starší stručná poznámka o fixované pásce
je v tomto přesném smyslu zpřesněna.

Přečtený autorský přetisk Levin1993 z roku2012 obsahuje párové
výběry a transformační algoritmus; jeho matematická část byla celá
znovu přečtena. Originální časopisecká sazba není porovnána.
Goldreich–Levin1989 zůstává přečten pouze v rozsahu stran1–4;
jeho další kvantitativní algoritmy se nepovyšují na auditované.
Historické prvenství se touto matematickou kontrolou neprohlašuje.

Prověřeny vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální
TeX; uvedené tři známé opravy173/183 jsou v `all2-prepre`.
Žádný z těchto známých zásahů nevytváří novou kartu. Rozsah dalších
odstavců174–176 a úloh43–44 je předmětem následujícího checkpointu.

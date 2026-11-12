# MPR111: celá minwise rodina, tabulka, sketche a jejich odhad

7. listopadu 2026. Celé zadání p23/file43, odpověď i poznámky
p387/file407 a autorský PS11.9.2019 p23/file29, p43–44/files49–50
přímo zobrazeny. Šest místních vrstev errat a tři TeX zdroje
neobsahují použitelnou opravu111. F173 níže je lokální vada
mezivěty; žádný z hlavních výsledků se nemění. Fyzický výtisk
nebyl kontrolován. Kořenové přijetí se zde netvrdí.

## Rodina a úplnost malé kontroly

Permutaci čteme jako šest obrazů 1π,...,6π. Každý z deseti
tištěných seedů obsahuje právě1,...,6 a začíná1. Jejich levé
cyklické posuny jsou opět permutace. Jedna orbita má právě šest
prvků, protože poloha1 určuje posun. Dvě orbity se nemohou
protnout: rotací společného prvku do polohy1 vpředu bychom
dostali oba původní seedy, které jsou různé. Je tedy přesně60
různých permutací. Nejde o přičítání konstanty ke všem obrazům.

`verify_mpr111_minwise.py` konstrukci zapíše v pořadí posun0,...,5,
uvnitř deset seedů zleva doprava. Pro každé k1,...,6 používá
všechny rostoucí k-tice z1,...,6. Každá neprázdná podmnožina
má jediný takový zápis: dohromady2^6−1=63 množin. Pro každou
permutaci a podmnožinu najde jediný původní prvek a s nejmenším
obrazem aπ; jednoznačnost zajišťuje injektivita permutace.
Sečte60 indikátorů pro každého a. Zjištěné počty jsou vždy60/k,
tedy pro k1,...,6 postupně60,30,20,15,12,10. Je zkontrolováno
Σ_k k binom(6,k)=6·2^5=192 jednotlivých podmínek, nikoli
pouze požadovaný jeden příklad. Certifikát uchovává všech63
množin a jejich jednotlivé počty. To je úplná konečná kontrola
uvedené rodiny; netvrdí nic o nevypsaných rodinách.

Výpočet skončí po63·60=3780 určeních minima, každé na nejvýše
šesti hodnotách; žádné hledání rodin ani průchod6! permutacemi.
Jediný běh nice15 trval0.012043097987771034s. Úspěšný certifikát
se nepřepisuje a nebyl opakován. Staré censy zůstaly nedotčeny.

##(a): každá trojice i každý tučný znak

Pro každou z60 permutací se vypíší pozice1,3,4. Vznikne přesně
tištěná tabulka, včetně opakovaných trojic. Například první
seed dává134; jeho první levý posun234561 dává245 na11.pozici.
Vedle ruční transkripce je použita přímo XML extrakce původního
PDF p387. Tři řádky se získají z původních souřadnic, segmenty
se seřadí zleva a mezery se odstraní; každý řádek má60 číslic.
Font9/T26 byl na zobrazené originální stránce identifikován jako
tučná minima, font3/T6 jako obyčejné číslice. Segmenty přesahující
mezery mezi trojicemi se zachovávají po jednotlivých znacích.

Všech60 výpočtových trojic souhlasí s ruční transkripcí i s PDF.
V každé trojici je právě jeden tučný znak a je to její minimum.
Řádkové počty vítězných souřadnic1,3,4 jsou

```
řádek1: 12, 4, 4
řádek2:  3, 4,13
řádek3:  5,12, 3
součet: 20,20,20.
```

Tím je přímo ověřeno(a), nejen neformálně rovnoměrný vzhled
tabulky. Žádná její položka ani zvýraznění nevyžaduje opravu.

##(b,c): přesná ekvivalence událostí a okraje

Pro neprázdné A,B položme U=A∪B a nechť W je jediný prvek U
s nejmenším obrazem Wπ. Minwise vlastnost a rovnoměrný výběr
π dávají P(W=w)=1/|U| pro každé w∈U.

Je-li W∈A∩B, jeho obraz je minimální v obou množinách, takže
S_A=S_B=Wπ. Naopak ze S_A=S_B a injektivity π plyne, že
prvky, které v A a B dosáhly minima, jsou týž w∈A∩B.
Jejich obraz je nejmenší v obou množinách, tedy v celé U,
takže w=W. Událost shody je přesně {W∈A∩B}. Součet
|A∩B| disjunktních pravděpodobností1/|U| dává tištěný podíl.

Pro tři neprázdné množiny vezmeme U=A∪B∪C. Úplně stejná
obousměrná argumentace, nyní se třemi minimy, dává
{S_A=S_B=S_C}={W∈A∩B∩C}, a tedy podíl z(c). Platí i
pro libovolný konečný kladný počet neprázdných množin.
Disjunktní průnik dává0, všechny stejné množiny dávají1;
n1 je zahrnuto. Nezávislost sketchů různých množin se netvrdí:
všechny používají tutéž náhodnou π, což je pro výsledek zásadní.

Definice minima má přirozený obor neprázdných množin.
Slovo „arbitrary“ v zadání nevede k jinému konečnému výsledku
pro prázdné množiny, nýbrž vyžaduje obvyklé doplnění konvence.
Lze položit S_empty=∞. Je-li alespoň jedna množina prázdná
a alespoň jedna neprázdná, shoda všech sketchů má pravděpodobnost0
a podíl je0. Jsou-li všechny prázdné, shoda je1 a Jaccardův
podíl0/0 se definuje konvencí jako1. Alternativou je ponechat
vzorce pouze na oboru neprázdných vstupů. Tisk tuto konvenci
nerozepisuje; neklasifikuji běžné doplnění oboru jako samostatné
erratum ani kandidáta. Tento krok neslouží k obcházení žádného
protipříkladu s definovanými konečnými hodnotami.

## F173: původní prvky nejsou hodnoty sketchů

První mezivěta odpovědi(b) tvrdí, že S_A a S_B patří do A∪B.
To neplyne z definice S_A=min aπ a je nepravdivé i pro
neprázdné vstupy: n2, rovnoměrná minwise rodina{12,21},
A=B={1}, π=21. Pak S_A=S_B=2, ale A∪B={1}. Obě
permutace splňují minwise podmínku pro jednoprvkové množiny
a každá ze dvou hodnot vítězí jednou pro{1,2}; svědek proto
splňuje všechny předpoklady. Chybná mezivěta selže s pravděpodobností1/2.

Správně S_A,S_B∈π(A∪B); případně π^−1(S_A),π^−1(S_B)∈A∪B.
Zbytek důkazu se přesně vyjádří pomocí W výše. Ani vzorec(b),
ani(c), ani minwise rodina nejsou chybné. Stejná mezivěta je
v původním PDF a autorském PS. Všech šest vrstev a tři TeX
zdroje bez opravy; závažnost low, lokace jen p387/file407.

## Poznámky: odhad, náklady a nutná velikost přesné rodiny

Pro m nezávislých výběrů π_j jsou I_j=[S_j(A)=S_j(B)] nezávislé
Bernoulliho proměnné s parametrem J=|A∩B|/|A∪B|. Proto
C=ΣI_j má přesný zákon P(C=c)=binom(m,c)J^c(1−J)^(m−c),
EC=mJ a Var C=mJ(1−J). Normalizovaný odhad C/m je nestranný
a má varianci J(1−J)/m≤1/(4m). Pro m100 je směrodatná
odchylka nejvýše1/20. Z úplně doložené MPR89 pro pevné
intervaly I_j∈[0,1] plyne

```
P(|C/m−J|≥t) ≤ min(1, 2 exp(−2mt²)), t>0.
```

Tištěná nečíselná formulace o spolehlivosti tedy znamená odhad
s touto výběrovou chybou, nikoli přesnou rovnost nebo absolutní
záruku libovolně malé chyby. Počet shod dává odhad po známém
dělení100; nejde o chybu měřítka. Pro vyhodnotitelné permutace
stojí vytvoření m sketchů O(m|A|) vyhodnocení/porovnání a O(m)
uložených hodnot, porovnání dvojice připravených sketchů O(m).
Nevyžaduje opětovné čtení obou původních dokumentů.

Pro ε-přibližnou minwise rodinu, kde každé w∈U vítězí
s pravděpodobností v[(1−ε)/|U|,(1+ε)/|U|], součet přes průnik
dává kolizní pravděpodobnost v[(1−ε)J,(1+ε)J]. Tedy absolutní
bias nejvýše εJ; nezávislé opakování má navíc stejný typ
výběrové chyby kolem své skutečné střední hodnoty. Nepředpokládáme,
že libovolná běžná hashovací rodina tuto podmínku splňuje.

Tvrzení o nepraktičnosti přesně minwise rodiny pro obrovské n
má elementární dolní mez. Protože N/k je celé pro každé k≤n,
je L=lcm(1,...,n) dělitelem N. Pro0≤r≤n−1 číslo
n binom(n−1,r)=n!/[r!(n−1−r)!] dělí L: exponent prvočísla p
je součet

```
Σ_{j≥1}(floor(n/p^j)−floor(r/p^j)−floor((n−1−r)/p^j)).
```

Každá závorka je0 nebo1, neboť n=r+(n−1−r)+1, a pro p^j>n
je0. Exponent je tedy nejvýše floor(log_p n), přesně exponent
p v L. Vzorec pro exponent faktoriálu vzniká počítáním násobků
p,p²,...; není tu odkaz na neověřený asymptotický odhad.
Jelikož součet n čísel binom(n−1,r) je2^(n−1), některé
n binom(n−1,r) je alespoň2^(n−1). Odtud

```
N ≥ L ≥ 2^(n−1).
```

Rovnoměrný výběr z přesné rodiny tedy potřebuje stav rozlišující
nejméně2^(n−1) možností, tj. nejméně n−1 bitů. Pro n2^64
to odůvodňuje praktickou nemožnost obecného přesného výběru.
Nejde o důkaz nemožnosti spočítat jednotlivý dotaz nebo přibližný
sketch; konstrukce z další úlohy s tím není v rozporu.

## Bibliografie v přesně omezeném rozsahu

Primární autorská kopie článku Broder–Charikar–Frieze–Mitzenmacher
JCSS60(2000),630–659 potvrzuje metadata, na p633 přímo
n2^64, typickou velikost1000,100 sketchů i přibližnou variantu;
originál této strany byl zobrazen. Na p636 uvádí související
Mulmuleyho konstrukci; bibliografie obsahuje Broderovu aplikaci
na konferenci SEQUENCES1997. Kontrola nepřebírá celý článek.
Vlastní důkazy výše jsou nezávislé na jeho dalších větách.

Primární Springer metadata potvrzují Mulmuley, Algorithmica16
(1996),450–463 a téma geometrických algoritmů. Přesný obsah
a historickou nezávislost jeho původního důkazu výslovně
vynechávám: plný článek není rychle dostupný bez předplatného.
Také přesný Jaccardův historický text na p249 z1901 vynechávám:
primární ETH E-Periodica obsahuje odpovídající bibliografický
záznam, ale pokus o PDF vrátil HTML. Žádný neplatný PDF soubor
nebyl uložen. Poznámka o švýcarských lokalitách není vydávána
za přímou kontrolu původního textu. Jde o dvě explicitní
bibliografické výjimky, nikoli matematické mezery.

Výsledek: celá111 matematicky doložena, F173 low v mezivětě,
dvě historické bibliografické výjimky. Stránky43 a407 nadále
partial kvůli následujícím dosud neuzavřeným úlohám.

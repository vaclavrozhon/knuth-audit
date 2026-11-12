# Úlohy 80 a 82: skutečný neizometrický graf a optimální služba

Checkpoint X0104, P0973–P0982. Originály zadání p90–91/
file107–108 a odpovědi p549/file566 byly přečteny. Celá81
se přebírá z P0945. Žádné grafy ani posloupnosti nejsou
brute force enumerovány.

## 80(a): celý jedenáctivrcholový graf — P0973

Vytištěné binární štítky odpovídají číslům

    V={0,1,2,3,4,6,7,12,13,14,15}.

Graf definujeme jako indukovaný podgraf Q_4. Jeho všechny
hrany podle měněného bitu a,b,c,d (váhy 8,4,2,1) jsou:

| bit | hrany |
|---|---|
| a | 4–12, 6–14, 7–15 |
| b | 0–4, 2–6, 3–7 |
| c | 0–2, 1–3, 4–6, 12–14, 13–15 |
| d | 0–1, 2–3, 6–7, 12–13, 14–15 |

Seznam je úplný: pro každou váhu se párují všechny prvky
V, které se liší právě touto váhou a mají ostatní bity
shodné. Graf je souvislý, např. všechny vrcholy leží
na spojených následujících čtyřcyklech:

    0–1–3–2–0, 0–2–6–4–0, 2–3–7–6–2,
    4–6–14–12–4, 6–7–15–14–6, 12–13–15–14–12.

Tyto konkrétní cykly propojují protějšími hranami každou
celou řádku předchozí tabulky. Všechny jejich hrany
jsou v úplném seznamu; jiný cyklus není potřebný.

## 80(a): vyloučení všech jiných izometrických označení — P0974

V každém injektivním vložení grafu do libovolné hyperkrychle,
které posílá hrany na hrany, má každý čtyřcyklus střídavě
dvě různé souřadnice. Proto šest uvedených cyklů nutí
všechny hrany každé řádky a,b,c,d měnit tutéž souřadnici.
Ve vrcholu 6 se stýkají hrany 6–14,6–2,6–4,6–7 ze všech
čtyř řádek. Jejich souřadnice musí být různé, jinak by
dva sousedé dostali stejný štítek.

Žádná další souřadnice se nemůže změnit na žádné hraně,
a vzhledem k souvislosti je tedy na všech vrcholech
konstantní. Po volbě štítku 0 jsou všechny ostatní
štítky určeny změnami podél cesty. Všechna krychlová
vložení jsou tudíž právě původní, až na permutaci,
komplementování a přidání konstantních souřadnic.
To dokazuje vytištěné „cannot be labeled in any
essentially different way“, včetně možnosti vyšší dimenze.

Vrcholy 1=0001 a 13=1101 mají Hammingovu vzdálenost 2.
Jediné dvě možné prostřední hyperkrychlové pozice jsou
5=0101 a 9=1001; obě ve V chybějí. V grafu tedy není
cesta délky 2. Je bipartitní a oba konce mají stejnou
paritu, takže každá jejich cesta má sudou délku. Cesta

    1–3–7–15–13

má délku 4, tedy grafová vzdálenost je přesně 4.
V každém jiném krychlovém vložení však zůstane Hammingova
vzdálenost 2 podle právě dokázané jednoznačnosti.
**Graf není partial cube**, nikoli pouze „toto označení
není izometrické“. Celá80(a) i celý její tištěný argument
jsou tím doloženy.

## 80(b): celý izometrický cyklus C_(2m) — P0975

Pro m≥2 a 0≤k<m označme vrcholy cyklu 0,...,2m−1
v cyklickém pořadí a položme

    l(k)=1^k 0^(m−k),
    l(m+k)=0^k 1^(m−k).

Štítky jsou navzájem různé a sousední cyklické pozice
se liší právě v jednom bitu, včetně obou přechodů
mezi polovinami. Pro dvě pozice i,j v téže polovině
je Hammingova i cyklická vzdálenost |i−j|. Mezi i a
m+j je Hammingova vzdálenost

    i+(m−j), pokud i≤j;
    j+(m−i), pokud i≥j,

tedy m−|i−j|. To je právě
min(m+j−i,m−j+i), cyklická vzdálenost. Jsou tím
pokryty všechny dvojice, takže jde o izometrické vložení,
nejen o přiřazení sousedních štítků. C_(2m) je partial cube.

## 80(b): chybějící medián a přesná mez m>2 — P0976

Trojice 0,m−1,m+1 má bitový medián

    M(0^m,1^(m−1)0,01^(m−1))=01^(m−2)0.

Pro m>2 má vnitřní jedničku a nuly na obou krajích.
Není tedy žádným štítkem s jedním přechodem 1→0 nebo
0→1 z P0975. V izometrické podmnožině krychle musí
bod ležící ve všech třech intervalech mít v každém bitu
majoritní hodnotu: dvě shodné krajní hodnoty jej v
příslušném intervalu fixují. Takový bod zde neexistuje,
proto graf nemá pro tuto trojici medián.

Při m=2 je zobrazený vektor 00 přítomen a C_4 je
mediánový graf; vytištěné omezení m>2 je přesné.
Pro jednoduché cykly se m=1 nepoužívá.

## 82: booleovská optimální zbytková cena — P0977

Nechť v_1,...,v_t jsou požadavky v {0,1}. Pro k≤t
nechť J_k(a) je minimum ceny suffixu k,...,t, když
před jeho začátkem je stav a. Náklady jsou jednotkové:

    J_k(a)=min_(b∈{0,1})(|a−b|+|b−v_k|+J_(k+1)(b)),
    J_(t+1)(a)=0.

Konečné minimum existuje. Každá pevná posloupnost
stavů mění při změně počátečního a pouze první pohyb,
a ten nejvýše o 1. Porovnáním optimálních posloupností
v obou směrech tedy

    |J_k(0)−J_k(1)|≤1.

Dále vždy J_k(v_k)≤J_k(1−v_k). Položme c=v_k a
F=J_(k+1). Z Lipschitzovy nerovnosti dostáváme přesně

    J_k(c)=min(F(c),2+F(1−c))=F(c),
    J_k(1−c)=1+min(F(c),F(1−c))≥F(c).

To je argument, proč se při rozhodování stačí podívat
na příští požadavek; není předpokládáno, že suffix
má jednoznačnou optimální posloupnost.

## 82: všechny větve optimálního mediánového pravidla — P0978

Ve stavu a=u_(k−1), k<t, označme b=v_k,c=v_(k+1).

- Je-li a=b, volba u_k=b stojí nyní 0 a opačná volba 2.
  Budoucí rozdíl J_(k+1) je nejvýše 1, takže b je optimální.
- Je-li a≠b, oba možné stavy mají nynější cenu 1. Budoucí
  cena je nejmenší při u_k=c podle P0977 pro suffix k+1.

V obou případech lze zvolit právě

    u_k=M(u_(k−1),v_k,v_(k+1)).

Volba dosahuje minimum DP recidivy pro každé možné
pokračování, a indukce na zbývající délce dokazuje
optimalitu celé posloupnosti. Pro poslední krok

    min_b(|a−b|+|b−v_t|)=|a−v_t|,

a u_t=v_t je vždy jednou z optimálních voleb. Tím jsou
ověřeny i případy t=1; pro t=0 je jediný stav u_0=v_0
a cena nula. Žádný krok nevyžaduje jiné koncové omezení.

## 82: přesná výjimka v odpovědi a nejednoznačný příklad — P0979

Z mediánového pravidla je u_k≠v_k právě když
u_(k−1)=v_(k+1)≠v_k. V takovém případě musí navíc
v_(k−1)=u_(k−1): pro k=1 to plyne z u_0=v_0;
pro k>1 by opačná hodnota v_(k−1)=v_k způsobila
u_(k−1)=M(u_(k−2),v_(k−1),v_k)=v_k, spor.
Tak dostáváme přesně vytištěnou čtyřčlennou výjimku
u_(k−1)=v_(k−1)=v_(k+1)≠v_k, a také její opačný směr.
Poslední krok k=t má vždy u_t=v_t a žádný v_(t+1) nepotřebuje.

Pro v_0v_1v_2v_3=0110 pravidlo vrátí 0110, s pohybovou
cenou 2 a obslužnou 0. Druhá uvedená možnost 0000 má
pohybovou cenu 0 a dvě jednotkové chyby obsluhy. Obě
mají cenu 2, kterou optimalita první posloupnosti
certifikuje jako minimum. Je tedy doložena i poznámka,
že optimum nemusí být jediné.

## 82: přenos na libovolný mediánový graf — P0980

P0945 dává isometrické štítky; vzdálenosti se sčítají
po bitech. Každá přípustná grafová posloupnost má v
každé souřadnici cenu alespoň booleovského minima
P0977. Součet těchto minim je tedy dolní mez grafového
optima, i když ne všechny bitové kombinace jsou vrcholy.

Konstrukce u_k=m(u_(k−1),v_k,v_(k+1)), u_t=v_t zůstává
v grafu, protože medián je jeho vrchol. V každé souřadnici
současně realizuje právě optimální booleovské pravidlo.
Dosáhne tedy součtu všech dolních mezí a je grafově
optimální. To dokazuje celý požadovaný výsledek bez
neoprávněné nezávislé volby neexistujících vrcholů.

Je použito t−1 mediánů a poslední přiřazení; s hotovými
b-bitovými štítky jde o O(tb) bitové práce a O(b)
průběžného stavu mimo výstup. Kniha zde netvrdí cenu
vybudování štítků ani převodu výsledku na jiný grafový
identifikátor. Jednovrcholový graf má vždy cenu nula.

## Dodatky odpovědi 82: přesný externí vstup o lookahead — P0981

Zdroje byly získány přímo z autorčina webu Fan Chung:
`sources/chung-graham-saks1987.pdf` a `...1989.pdf`.
Nejde o samostatnou rekonstrukci celé teorie dynamické
lokace. Jako explicitní vnější výsledek přebíráme:

**Chung–Graham–Saks 1987, Theorem2, tištěná p371:**
pro netriviální graf je window index 2 právě když má
izometrické vložení do krychle uzavřené na bodový medián.
Původní sazba tohoto výroku i jeho navazující argument
byla přečtena v `images/cgs1987-theorem2.png`.

Přesnou definici použitého parametru ověřuje původní
p112 v článku1989 (`images/cgs1989-intro-02.png`):
pro souvislý graf se standardní neohodnocenou vzdáleností
minimalizuje právě Σ(d(s_(i−1),s_i)+d(s_i,r_i)), s daným
s_0; window k dovoluje při volbě s_i znát r_j pro j<i+k.
Proto k=2 znamená právě současný a jeden následující
požadavek, vedle známé minulosti a počátečního stavu.
Je to přesně problém82, při přeznačení r_i=v_i,s_i=u_i.

Nutná strana externí věty dává izometrickou majority-closed
podmnožinu krychle, tedy mediánový graf: majority každé
trojice je přítomna a díky izometrii leží ve všech třech
intervalech; jediná možná bitová hodnota v každé souřadnici
zaručuje jednoznačnost. Dostatečnou stranu jsme nezávisle
dokázali P0977–P0980. Singleton je triviální a mediánový.
Tím je aplikace externí charakterizace v dodatku správná
v obvyklé konečné souvislé doméně; externí nutnost sama
se zde neprohlašuje za nově dokázanou.

## Obecný konečný lookahead a historický rozsah — P0982

Článek1989 má na p114 přímo Theorem2.9
(`images/cgs1989-theorem29.png`): konečný window index
je charakterizován slabými retrakty součinů klik;
při konečném indexu je roven velikosti největší kliky.
Definice nákladů a okna jsou tytéž jako výše. To
ověřuje přesně tvrzení knihy, že autoři charakterizovali
i všechny případy, kdy stačí dané konečné množství
lookahead. Tuto další strukturální větu **přebíráme
jako externí vstup**, bez opakování jejího obecného důkazu.

Originály1989 p111–114 ověřují názvy, autory, rok,
časopis9(2),111–131, definici i obě uvedené věty.
Autorův bibliografický seznam ověřuje1987 *Dynamic Search
in Graphs*, Discrete Algorithms and Complexity,351–387;
primární PDF má shodný název a p371. Motivaci samouspořádávajícími
datovými strukturami ani všechny historické implementace
jsme zvlášť nereprodukovali; jde o bibliografickou výjimku.
Metadata s hash a přesným rozsahem četby jsou
`sources/dynamic-service-bibliography.json`.

## Errata a úplná stránka90

Pro80/82 prohledáno všech pět relevantních vrstev errat.
Známé F0 p90 (13.12.2009) upřesňuje „induced“ v80(a),
což náš dotisk už obsahuje a důkaz P0973 přesně splňuje.
Oprava F0 odpovědi83 patří další úloze. Žádný nový nález.

Celá p90 má nyní argumenty: pokračování75(b–f) P0917–P0922,
76 P0876,77 P0947–P0956,78 P0958,79 P0959–P0963,
80 P0973–P0976,81 P0945 a zadání82 P0977–P0982.
P91 je zatím vyřešen jen dokončující odstavec82;83 a dále
zůstávají otevřené. P549 je úplná po82, ale začínající83
ještě nikoli, takže celá odpovědní stránka zůstává partial.

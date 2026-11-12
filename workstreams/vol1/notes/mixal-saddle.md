# §1.3.2-10–12: sedlové body, pravděpodobnosti a časy

Kontrola 1. listopadu 2026. Matice má m řádků a n sloupců;
v zadání m=9,n=8. Sedlový bod je prvek, který je minimem ve svém
řádku a maximem ve svém sloupci; rovnosti jsou dovoleny. Originály
s.159 a513–515 zobrazeny. Přepisy programů jsou v `mixal_saddle.py`,
nezávislé vzorce v `saddle_expectations.py`. Časová jednotka u je
jednotka MIX; níže uvedené numerické výsledky zahrnují 1u za HLT.
Asymptotické vzorce v oddílech 4–5 HLT nezahrnují, což je výslovně
uvedeno. Nesměšovat to s čekáním na operátora.

## 1. Invarianty a známé opravy úlohy 10

Označme R(i)=min_j a[i,j] a C(j)=max_i a[i,j]. Vždy
R(i)<=a[i,j]<=C(j), tedy max_i R(i)<=min_j C(j). Je-li a[i0,j0]
sedlový bod, pak R(i0)=C(j0), což nutí obě krajní hodnoty k rovnosti.
Obráceně rovnost R(i0)=C(j0) vtlačí a[i0,j0] mezi dvě stejné hodnoty.
Tím je dokázána věta i to, že všechny sedlové body mají stejnou hodnotu.
Známé erratum 22.3.1999 opravuje R(j) na R(i) v tomto důkazu.

**První program.** Řádky prochází zdola, každý zprava. rI1 je posun
v matici, rI2 číslo sloupce, rX aktuální minimum a LIST[1..rI3]
obsahuje právě všechny dosud nalezené pozice tohoto minima. Menší
hodnota seznam zruší, stejná přidá pozici, větší jej nemění. Na konci
řádku rI1=(i-1)n. Kandidátní sloupce se zkoušejí opačným pořadím
seznamu, tedy zleva. Prvek větší než rX kandidáta vyřadí; jinak byl
nalezen sedlový bod. Po úspěšném průchodu sloupcem rI2=j-n a
`INC1 A10+n,2` vrátí přesně adresu 1000+ni+j. Při neúspěchu všech
řádků rI1=0. Seznam potřebuje nejvýše n slov. Všechny indexy zůstávají
v platném rozsahu; záporné nuly se při porovnání chovají jako nuly.

**Druhý program.** První fáze prochází sloupce zprava a každý zdola.
rX je průběžné maximum. Koncový index rI2=j-n uloží maximum do
CMAX+j. První sloupec (j=n) inicializuje rA; další v něm ponechávají
μ=min_j C(j). Ve druhé fázi rI3 je pravý okraj právě zkoušeného
řádku. Jakýkoli prvek <μ řádek vyloučí. U rovnosti a[i,j]=μ se navíc
ověří C(j)=μ a uloží adresa. Pokud celý řádek projde, libovolný sloupec
s C(j)=μ v něm nutně má hodnotu μ; proto je uložená adresa platná,
i když jiné kandidáty z dřívějších neúspěšných řádků rI1 obsahoval.

Erratum 10.3.2013 správně mění inicializaci druhé fáze na
`ENT3 m*n; ENT2 0,3`. Původní dvojice vynechá první řádek.
Konkrétní regresní matice má první řádek samé dvojky a v každém dalším
řádku jednu nulu, ostatní hodnoty jedničky. Sedlové body jsou v prvním
řádku; původní program vrátí nulu. Oprava 30.4.2013 v první fázi
pouze přidává vysvětlující komentář k již správné instrukci.

Erratum 18.5.1999 přesouvá `ENT1 0` až za `J3P 3B`. Je to úspora
času, nikoli oprava správnosti; po posledním neúspěchu se výsledek
vynuluje v obou verzích. Současné 540u→530u opravuje orientační
experiment s rovnoměrnými hodnotami 0..4. Jeho přesnou historickou
náhodnou posloupnost neznáme a průměr 530u netvrdíme jako identitu.

**Nápověda třetího programu.** Všechny sedlové řádky leží v průniku
množin {i:a[i,j]=C(j)} přes sloupce splňující C(j)=μ. Tato nutná
podmínka plyne z a[i,j]>=R(i)=μ a a[i,j]<=C(j)=μ. Po zachování
všech takových řádků stačí zkoušet jejich řádková minima. Pro různé
prvky má průnik právě jeden kandidátní řádek (sloupec s maximem μ
je jediný); při shodách se nesmí ponechat pouze jeden jeho zástupce.

## 2. Úloha 11: přesné pravděpodobnosti

V modelu různých prvků jsou všechny (mn)! pořadové permutace stejně
pravděpodobné. Sedlový bod je nejvýše jeden. U pevné pozice jde jen
o relativní pořadí m+n-1 prvků jejího řádku a sloupce: m-1 sloupcových
musí být menší, n-1 řádkových větší. Pravděpodobnost pevné pozice je
(m-1)!(n-1)!/(m+n-1)!, součet přes mn disjunktních možností dává

```
P = (m+n)/binom(m+n,m);       P(9,8)=1/1430.
```

V binárním modelu jsou všechny prvky nezávislé férové bity. Sedlová
nula existuje právě tehdy, když existuje nulový sloupec; sedlová jednička
právě tehdy, když existuje jedničkový řádek. Tyto dvě možnosti se
vylučují, protože jejich průsečík by musel být současně 0 i1. Proto

```
Pbin = 2-(1-2^(-m))^n-(1-2^(-n))^m,
Pbin(9,8) = 924744796234036231/18446744073709551616.
```

Suma n*2^(-m)+m*2^(-n) má nezápornou chybu nejvýše
binom(n,2)*2^(-2m)+binom(m,2)*2^(-2n), podle první dvojice Bonferroniho
nerovností (součet jednotlivých událostí nadhodnocuje jejich sjednocení;
odečtení všech dvojic je dolní mez). Tím je i význam aproximace přesný.
Erratum31.7.1997 odstraňuje pouze omylem opakovaný čitatel v textu.

## 3. Přesné instrukční náklady a C0023

Při skenování jednoho řádku prvním programem stojí inicializace a poslední
přechod 10u. Každý další prvek stojí 6u, pokud je větší než dosavadní
minimum, 13u při novém ostrém minimu a11u při rovnosti. U různých
prvků je tedy řádková část `6n+4+7K`, kde K je počet nových minim
po prvním prvku. Zkouška kandidátního sloupce, jejíž první větší prvek
je t-tý v pořadí shora uvedeného procházení (tj. zdola), stojí `5t+3`;
pokud projde celý sloupec, stojí `5m+4`. Po zamítnutí všech kandidátů
přibude 1u za přechod na další řádek. Počítání neobsahuje HLT.

První fáze druhého programu stojí přesně `5mn+9n+2Kc+2Kmin`,
kde Kc je součet nových sloupcových maxim po jejich prvních prvcích
a Kmin počet nových minim posloupnosti sloupcových maxim po prvním.
Ve druhé fázi stojí přijatý prvek >μ 7u, rovný μ 10u nebo11u podle
testu C(j); první zamítnutý prvek včetně přechodu na další řádek5u.
Příprava každého řádku stojí2u. Samostatně je třeba započíst inicializaci
rI3 a závěrečné nulování při celkovém neúspěchu.

Pro nulovou matici9×8 jsou součty:

| Část | Řešení1 | Řešení2 |
|---|---:|---:|
| Inicializace a řádková část / první fáze | 1+87 | 432 |
| Sloupcová zkouška / příprava a řádková zkouška | 3+45+1 | 3+88 |
| HLT | 1 | 1 |
| Celkem | **138** | **524** |

Pár137u,524u na s.514 není konzistentní ani při vynechání HLT:
pak jsou správné hodnoty137u,523u. Jejich rozdíl musí být386u,
nikoli387u, nezávisle na stejné volbě ceny HLT. Nález C0023.

## 4. Různé prvky: první program a C0024

H_k=1+1/2+...+1/k označuje harmonické číslo. Při rovnoměrném pořadí
je E K=H_n-1: každý z k dosud přečtených prvků má stejnou šanci být
nejmenší. Řádková část proto má střední cenu `6n+7H_n-3`.
Koeficient5 u H_n v doplněné odpovědi12 neodpovídá tištěnému programu.

Pro přesnou kontrolu zbytku očíslujme řádky i=0,...,m-1 v pořadí
provádění. Nahraďme permutaci nezávislými rovnoměrnými hodnotami z(0,1):
program závisí pouze na pořadí, a všechna pořadí mají stejnou pravděpodobnost.
Minimum U řádku má hustotu n(1-x)^(n-1). Položme
`a_t=E U^t=1/binom(n+t,t)` pro t>=0. Prozatím nechme program zpracovat
všechny řádky i po případném nalezení sedla. Počet porovnání D_i
v kandidátním sloupci daného řádku má střední hodnotu

```
E D_i = sum(t=0..m-1) a_(t-[i<t]),
D = sum_i E D_i
  = sum(t=0..m-1) ((m-t)*a_t + t*a_(t-1))
  = n*(m+1)/(n-1) - (m+n)^2/((n-1)*B),     n>1,
B = binom(m+n,m).
```

V součtu je člen s t=0 ve druhém sčítanci nulový. Indikátor[i<t]
vyjímá vlastní prvek řádku, jehož porovnání nikdy neukončí sloupcovou
zkoušku. Poslední identita plyne ze součtu geometrické řady v beta
integrálu pro a_t; není potřebná nezávislost různých D_i.

Celá dokončená řádková iterace, bez ohledu na úspěch, stojí
`W_i=6n+8+7K_i+5D_i`: neúspěšná větev má sloupcovou cenu5D_i+3
a přechod1, úspěšná má5m+4. Proto se střední čas tištěného programu
**bez HLT** rovná přesně

```
A - 5*(m+n)^2/((n-1)*B) - Delta,
A = 6mn+7mH_n+6m+6+5*(m+1)/(n-1).
```

Delta je očekávaná práce ušetřená tím, že se po prvním sedle další
řádky neprovádějí. Události sedla v různých řádcích jsou disjunktní
a každá má pravděpodobnost P/m, kde P=(m+n)/B. Jelikož pro každý
úplný řádek platí `6n+13 <= W_i <= 13n+5m+1`, dostáváme rigorózní meze

```
(6n+13)*(m-1)*P/2 <= Delta <= (13n+5m+1)*(m-1)*P/2.
```

Tím je doložen nejen chybný koeficient harmonického členu v odpovědi12,
ale i příliš malý uvedený zbytek: pro m=n=k má Delta řád k^3/B,
nikoli O(k^2/B). Obě korekce vůči A mají záporné znaménko a nemohou
se vyrušit. Bezpečný obecný zbytek je O(m*(m+n)^2/B). Ještě bez
řešení přesné podmíněné hodnoty Delta uvedené meze dokazují nesouhlas.

## 5. Různé prvky: druhý vzorec je správný

První fáze má střední čas
`5mn+7n+2nH_m+2H_n-2`. Minimum sloupcových maxim μ má hustotu
`nm*x^(m-1)*(1-x^m)^(n-1)` na(0,1). Podmíněně μ=x je pravděpodobnost,
že zvolený prvek jiného sloupce je aspoň x,
`s(x)=(1-x)/(1-x^m)`. Pro minmaxový sloupec je tato pravděpodobnost1/m.
Je-li q_j(x) pravděpodobnost, že prvních j prvků libovolného řádku
projde testem >=x, rozlišení polohy minmaxového sloupce dává

```
q_0=1,
q_j=(1-j/n)*s^j + j/(nm)*s^(j-1),       1<=j<=n.
```

Pro řádek obsahující μ je odpovídající hodnota
`r_j=(1-j/n)*s^j+(j/n)*s^(j-1)`. Počet skutečně přečtených prvků má
střední hodnotu Q=sum(j=0..n-1) E q_j, respektive R=sum(j=0..n-1) E r_j.
Horní mez n-1 je důležitá: průchod všech n prvků nezpůsobí(n+1)-ní čtení.
Položme pro celé k>=0,N>=1

```
I(k,N) = integral(0..1) m*(1-x)^k*x^(m-1)*(1-x^m)^(N-1) dx.
E q_j = (n-j)*I(j,n-j)+(j/m)*I(j-1,n-j+1),  j<n,
E r_j = (n-j)*I(j,n-j)+j*I(j-1,n-j+1),      j<n.
Eeq = sum(j=0..n-1) I(j,n-j).
```

Eeq je očekávaný počet skutečně navštívených pozic s hodnotou μ při
zkoušení všech řádků. Každý integrál je přesná konečná racionální suma
po roznásobení dvou celočíselných mocnin; tak jej počítá validátor.

V jednom řádku označme C počet čtení, E počet rovností s μ a S indikátor
úspěchu. Cena řádkové části druhé fáze je `7C+4E+2S`.
S přihlédnutím k inicializaci, závěrečnému nulování a zastavení na sedle
je střední čas bez HLT

```
E Phase1 + 2 + 7mQ + 4Eeq + P - Delta2,
7*(m-1)*P/2 <= Delta2 <= (7n+6)*(m-1)*P/2.
```

Zbytek tištěného asymptotického vzorce lze dokázat bez problematických
přesnějších rozvojů v preprintu. Pro Y=-m*log μ má Y rozdělení maxima
n nezávislých exponenciálních veličin s průměrem1. Tedy
E Y=H_n a E Y^2=H_n^2+sum(k=1..n)1/k^2; tato fakta plynou například
z nezávislých exponenciálních mezer uspořádaného vzorku (paměťová
vlastnost exponenciálního rozdělení dává sazby n,n-1,...,1).
Přímou změnou hustoty v q_1 dostaneme

```
m E q_1 = E[m*(1-exp(-Y_(n-1)/m))]+1/n
        = H_n + O(H_n^2/m).
```

Použita nerovnost y-y^2/(2m)<=m*(1-exp(-y/m))<=y.
Pro Y<=m/4 a m>=8 je s<=(Y+1)/m<=1/2. Geometrická řada dává
sum(j>=2)q_j=O(s^2+s/(nm)). Doplněk má pravděpodobnost nejvýše
n*exp(-m/4); i po vynásobení n členy řady je zanedbatelný oproti
libovolné mocnině1/m, jestliže log(n)/m→0. Proto
`Q=1+H_n/m+O(H_n^2/m^2)` a podobně `Eeq=O(1/n)`.
Korekce předčasného zastavení je menší než každý pevný záporný
polynomiální řád v m+n, když m,n oba rostou: binom(m+n,m) převyšuje
libovolnou pevnou mocninu m+n. Výsledek je právě

```
E T2/u = 5mn+2nH_m+7m+7n+9H_n
       + O(1/n)+O((log n)^2/m),          bez HLT.
```

## 6. Binární model: přesné průměry obou programů

Níže jsou všechny indexy řádků v pořadí provádění i=0,...,m-1.
Položme p=2^(-m), q=1-p, r=2^(-n), P0=1-q^n. P0 je pravděpodobnost
existence nulového sloupce. Pro druhý program stojí první fáze průměrně

```
5mn+10n-2np+2q*(1-q^(n-1)).
```

Ve sloupci je po prvním prvku nový ostrý rekord právě když první bit
je0 a někde dále je1; pravděpodobnost1/2-p. Nové minimum sloupcových
maxim nastane nejvýše jednou, s pravděpodobností q*(1-q^(n-1)).

Na události μ=0 projde hned první řádek; jeho vážená očekávaná cena
včetně inicializace rI3, bez HLT, je

```
E0=(3+7n)*P0 + 3n*(1/2-(1/2-p)*q^(n-1)) + np.
```

Zde další3u platí za každou nulu v řádku a další1u za každý nulový
sloupec. Na události μ=1 řádek i dosáhneme s pravděpodobností
`A_i=(1-r)^i-P0`; jeho prvních k bitů je současně jedničkových
s pravděpodobností `B_i,k=2^(-k)*((1-r)^i+q^(n-k)-1)`.
Jde o inkluzi a exkluzi událostí nulového sloupce, které samy zaručují
neúspěch všech dřívějších řádků. Úspěch i-tého řádku má pravděpodobnost
r*(1-r)^i, neúspěch `F_i=(1-r)^(i+1)-P0`. Proto

```
E1=q^n+2*sum_i A_i+11*sum_(i,k=1..n) B_i,k
   +5*sum_i F_i+(1-r)^m-P0.
E T2 = E Phase1 + E0+E1+1.             Poslední1 je HLT.
```

Pro první program podmiňme konkrétní řádkový bitový vzor x s z nulami,
který má pravděpodobnost r. Jeho řádkový čas c(x) určuje pravidlo
10 plus6/13/11u z oddílu3. Položme h=2^(-(m-1)), v=1-h.
Je-li z=0, předchozí řádky nesměly být jedničkové a žádný nulový
sloupec být nemůže. Příspěvek tohoto vzoru je
`r*sum_i (1-r)^i*(c(x)+5m+4)`.

Je-li z>0, první řádek může skončit při prvním nulovém kandidátním
sloupci. Pro kandidátní sloupec s vynucenou nulou v řádku i definujme
Fcol_i jako očekávanou cenu jeho neúspěšné zkoušky, vynásobenou
indikátorem neúspěchu:

```
Fcol_i = sum(t=1..m, t!=i+1) (5t+3)*2^(-t+[t>i+1]).
```

Cena úspěšné zkoušky je5m+4. Celý příspěvek prvního řádku daného vzoru
je `r*(c(x)+(sum(k=0..z-1)v^k)*(Fcol_0+h*(5m+4))+v^z)`.
Poslední člen je přechod na další řádek, když všechny zkoušky selžou.

Pro i>0 program řádek dosáhne právě tehdy, když neexistuje nulový
sloupec ani jedničkový dřívější řádek. Společná pravděpodobnost
s konkrétním vzorem je `w_i=r*((1-r)^i+v^z-1)`. Všechny jeho nulové
kandidáty teď musejí selhat. Inkluze a exkluze přes množiny dřívějších
jedničkových řádků dává pro součet sloupcových cen

```
r*z*(v^(z-1)*Fcol_i + G_i),
G_i = -r*sum(k=0..i-1) (1-r)^(i-1-k)*(13-5*2^(-k)).
```

Pro vysvětlení G_i: pokud nejčasnější vynucená jednička sloupce leží
v řádku k, první jednička přijde nejpozději tam. Její průměrné pořadí
je2-2^(-k), tedy průměrná cena13-5*2^(-k). Sečtení znamének a vah
všech podmnožin pozdějších vynucených řádků dává faktor
`-r*(1-r)^(i-1-k)`. Pro každý vzor a i>0 tedy přičteme
`w_i*(c(x)+1)+r*z*(v^(z-1)*Fcol_i+G_i)`.
Nakonec přidáme2u za počáteční ENT1 a konečné HLT. Jde o konečný
přesný výpočet přes2^n vzorů, nikoli simulaci2^(mn) matic.

## 7. Ověřené výsledky a zbývající rozsah úlohy 12

`check_mixal_saddle.py` prošel9381 kontrolami. Vyčerpává binární matice
rozměrů1×1,1×4,4×1,2×2,2×3,3×2,3×3 a permutace různých prvků
1×3,3×1,2×2,2×3,3×2. Srovnává MIX, nezávislé sdružené ceny,
přímou definici sedla, přesné pravděpodobnosti, integrály a očekávání.
Navíc jsou testovány9×8 matice s krajními hodnotami slov v radixech64
a100. Regrese2013 a úspora1999 mají konkrétní svědky.
První běh selhal pouze při exportu profilu na neexistujícím `asm.rows`;
po opravě na původní vstupní řádky prošel. Nešlo o chybu knihy.

| Rozdělení9×8 | Průměr řešení1 v u | Průměr řešení2 v u |
|---|---:|---:|
| Různé prvky | [670.9397852,671.1887363] | [553.8082883,553.9621345] |
| Férové bity | 1137.8157888503172 | 600.8753726825132 |

Intervaly prvního řádku jsou rigorózní racionální meze z oddílů4–5,
ne intervaly spolehlivosti. Druhý řádek má přesné racionální hodnoty
v JSON. Druhý tištěný program je tedy průměrně rychlejší v obou
zadaných modelech, při téže konvenci HLT.

Pro různé prvky je konkrétní třetí program `solution3_distinct`:
při každém novém sloupcovém maximu ukládá jeho posun v rI5; při
novém minimu sloupcových maxim ukládá pravý okraj řádku v rI6 a
adresu kandidáta v rI3. Pak otestuje jediný řádek proti μ, vrací
zapamatovanou adresu nebo0. Nutná podmínka z oddílu1 dokazuje správnost.
Oproti první fázi řešení2 přidává nH_m+3H_n časových jednotek.
Druhá fáze stojí6C+2+2S, kde C je počet čtení a S indikátor sedla.
Její přesný celkový průměr včetně HLT je

```
5mn+7n+3nH_m+5H_n+6R+2P.
```

R a P byly definovány v oddílech5 a2. Samostatný nový checker ověřuje
jen tuto variantu; staré úspěšné testy neopakuje. Při rozšiřování
instrukčních bloků bylo nutné opravit relativní skoky JGE/JLE; chybu
vlastního prvního přepisu zachytil malý test, nikoli nález v knize.
Tato konkrétní varianta vyhrává v modelu různých prvků: průměr
506.9704989108009u, přesný zlomek166417392735132713/328258533963360.
Nový checker prošel3118 kontrolami.

**Stav před doplněním oddílu8:** binární analýza dvou tištěných programů
je úplná, stejně tak obě publikované asymptotické odpovědi jsou prověřeny
(jedna vyvrácena). Zbývá vybrat a analyzovat konkrétní třetí variantu
s uchováním všech kandidátních řádků při shodách. Pouhé vynechání
řádků neudává cenu tvorby seznamu. `solution3_distinct` není řešením
pro binární vstup a takové tvrzení se z těchto testů nevyvozuje.

## 8. Uzavření úlohy 12: obecná třetí varianta i pro shody

Zbývající bod z předchozího checkpointu je nyní uzavřen. Protože kniha
nedává instrukce třetí varianty, její čas musí být spojen s konkrétním
provedením. `mixal_saddle_candidates.py` uchová v rI5 číslo j0 jednoho
sloupce s C(j0)=μ. Potenciální řádky z něj vybírá postupně: přeskočí
řádek s a[i,j0]<μ, ostatním ověří všechny prvky proti μ. Když řádek
projde, vrátí adresu a[i,j0]; jinak zkouší dalšího kandidáta. Uchovává
tedy nadmnožinu průniku z nápovědy, jehož další podmínky vyřizuje při
ověřování řádku. Nematerializuje předem celý seznam a neztrácí žádné
sedlo při rovnostech. Jde o vymezenou realizaci principu třetího řešení,
nikoli o tvrzení totožnosti s nějakým v knize neuvedeným strojovým kódem.

Správnost je obecná: každý sedlový řádek musí mít a[i,j0]=μ, jak plyne
z oddílu1. Kandidát, jehož všechny hodnoty jsou>=μ, má v j0 skutečně
sedlo. Všechny kandidáty program v konečném počtu kroků vyzkouší.
Na rozdíl od `solution3_distinct` tento program přijímá libovolné
uspořádané hodnoty v rozsahu slova, včetně shod a záporných čísel.

První fáze je řešení2 plus jediná instrukce při každém novém minimu
sloupcových maxim, včetně prvního. Druhá fáze má úvodní cenu2u,
přeskočený řádek stojí6u, kandidát zamítnutý při t-tém čtení stojí
6t+6u a úspěšný kandidát6n+6u. Po neúspěchu všech řádků přibude1u
za vynulování výsledku; nakonec vždy1u za HLT. Tyto ceny jsou přímo
odvozeny z uvedených instrukcí, a pak samostatně porovnány se strojem.

**Různé prvky.** Nová instrukce v první fázi se provede průměrněH_n-krát.
Kandidát je jediný a délka jeho řádkové zkoušky má střední hodnotu R
z oddílu5. Pokud neexistuje sedlo, projde výběr všech m řádků. Jestliže
sedlo existuje, jeho poloha je rovnoměrná mezi m řádky a ušetří se
průměrně(3m-2)u oproti vzorci pro plný průchod s neúspěchem kandidáta.
Dostáváme přesně, včetněHLT,

```
E T3 = 5mn+7n+2nH_m+3H_n+6m+6R+2-(3m-2)P.
```

Pro9×8 je to5788361188114057/10821709910880,
tedy534.8841574744595u. To je méně než dolní mez553.8082u pro řešení2.
Specializovaná varianta pro různé prvky z oddílu7 je ještě rychlejší;
tato obecná varianta však shody nijak neomezuje.

**Binární prvky.** Použijme p,q,r,P0,A_i,B_i,k z oddílu6 a označme
S_i=r*(1-r)^i pravděpodobnost, že i-tý řádek je první jedničkový.
Dodatečná instrukce první fáze stojí průměrně
`L=1+q*(1-q^(n-1))`. Na události μ=0 projde prvním kandidátem první
řádek, s cenou6n+8u včetně inicializace, bezHLT. Na události μ=1 jsou
všechna sloupcová maxima1, takže uložený j0 je pravý krajní sloupec.
Řádek i se dosáhne s pravděpodobností A_i a je kandidátem s
pravděpodobností B_i,1. Jeho vážená cena je
`6A_i+6B_i,1+6*sum(k=1..n)B_i,k-6S_i`. Celkem

```
E T3 = E Phase1(řešení2) + L + 1
     + (6n+8)*P0 + 2*q^n + (1-r)^m-P0
     + sum_i (6A_i+6B_i,1+6*sum(k=1..n)B_i,k-6S_i).
```

Samostatné1 jeHLT; `(1-r)^m-P0` platí za závěrečné vynulování právě
při neexistenci sedla. Pro9×8 vyjde přesně
2722238257925623591942129/4722366482869645213696,
tedy576.4563736847883u, méně než600.8753726825132u pro řešení2.

Nový `check_saddle_candidates.py` prošel6126 kontrolami: vyčerpání
binárních matic do3×3, permutací do2×3/3×2, navíc ternárních2×2
a2×3 a zvolené9×8 matice v radixech64/100. Přímá definice sedla,
nezávislý sdružený čas a obě přesná očekávání souhlasí s MIX.
Starší úspěšné checkery se neopakovaly. Celkové pořadí vymezených
obecných implementací na9×8 je v obou modelech T3<T2<T1.
Tím je srovnání úlohy12 hotové; globální optimalita všech možných
MIX programů ani přesný čas každé jiné realizace nápovědy se netvrdí.

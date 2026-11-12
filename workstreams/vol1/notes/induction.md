# §1.2.1: indukce, invarianty a zobecněné dělení

V1-X0025, kontrola 1. listopadu 2026. Ze skenu zobrazeny s. 10–21
a odpovědi 468–469. Soupis cvičení 1–15 potvrzen. Přepis opakovaně
zaměňuje nerovnosti a exponenty; následující závěry vycházejí z obrazů.
Historické citace a výzkumná úloha 14 mají níže výslovně omezený rozsah.

## 1. Hlavní princip a první příklady

Indukce od 1 vychází z P(1) a z implikace
P(1),...,P(n) => P(n+1). Kdyby některé P neplatilo, nejmenší
neplatný index by nebyl 1 a jeho předchůdci by jej vynutili. Algoritmus
I realizuje tutéž myšlenku pro jednotlivé n: před testem I2 jsou
vypsány důkazy P(1),...,P(k), k roste od 1 do n. Obrázek 2 souhlasí.
Výklad sám později upozorňuje, že tím nelze odvodit princip indukce
bez přijetí příslušné základní vlastnosti přirozených čísel.

Součet prvních n lichých čísel je n^2: přírůstek při n->n+1 je 2n+1.
Pro geometrický obrázek 3 stačí rozdělit čtvercovou mřížku n×n
podle maxima obou souřadnic; vrstva s maximem k má 2k−1 polí.
Číselné rozklady p(0),...,p(7) jsou 1,1,2,3,5,7,11,15. Zde p(n)
počítá neuspořádané součty kladných čísel, p(0)=1 prázdný součet.
Kontrola v programu přímo generuje neklesající seznamy s daným součtem.
Neshoda p(7)=15 s posloupností prvočísel je správným protipříkladem
ke zkoumanému empirickému odhadu, nikoli chybou knihy.

Fibonacciho čísla mají F_0=0, F_1=1 a F_(n+1)=F_n+F_(n−1).
Zlatý řez phi=(1+sqrt(5))/2 splňuje phi^2=phi+1. Horní mez
F_n<=phi^(n−1) i dolní mez F_n>=phi^(n−2) z úlohy 4 platí pro n>=1.
Stačí ověřit n=1,2 a sečíst příslušné meze pro n−1,n; identita
phi^2=phi+1 dá požadovaný další člen. Není dovoleno v kroku z n=1
bez důkazu použít P(0), i když horní mez pro 0 náhodou také platí.
Tento rozdíl dodatek 2023 výslovně vysvětluje.

## 2. Rozšířený Eukleidův algoritmus a úloha 6

Vstupy m,n jsou kladná celá čísla a během běhu se nemění. Pracovní
proměnné c,d jsou současná dvojice; a',b',a,b jsou její celočíselné
koeficienty. Před dělením E2 platí invariant, tedy vlastnost zachovávaná
každým návratem do téhož místa:

```text
a'm+b'n=c, am+bn=d, d>0, gcd(c,d)=gcd(m,n).
```

Inicializace jej splňuje. Dělení c=qd+r s 0<=r<d doplní tvrzení A3
v obrázku 4. Je-li r=0, d=gcd(c,d) a současně am+bn=d, což je A4.
Jinak E4 změní koeficienty na (a,b) a (a'−qa,b'−qb), neboť
(a'−qa)m+(b'−qb)n=c−qd=r. Dočasná proměnná t zachová staré hodnoty
při předepsaném sekvenčním přiřazení. Společné dělitele dvojice
(c,d) zachová přechod na (d,r), takže dostáváme A6 a další iteraci.
Kladné d při každém E4 klesá, čímž je doloženo i ukončení.

Všechny čtyři řádky tabulky na s. 14 souhlasí s přímým výpočtem.
Výsledek pro m=1769,n=551 je a=5,b=−16,d=29; skutečně
5·1769−16·551=29. Samotná lokální tvrzení bez klesání d by dokázala
jen částečnou správnost: pokud výpočet skončí, vrátí správný výsledek.

Původní formulace pravidla (7) pro větvení požadovala všechny výstupní
aserce, i na neprovedené větvi. Například při r=0 nelze dokázat A5,
která vyžaduje r>0. Oprava z 26. července 1997 správně omezuje
požadavek na relevantní šipky. Konkrétní důkaz v textu už používá
podmínky příslušných větví. Jde o známé erratum V1-X0026.

## 3. Úlohy 1–3, 5 a 7–11

1. Pro indukci od n=0 se základ změní na P(0) a předpoklad na
   P(0),...,P(n). Ostatní argument z oddílu 1 se nemění.
2. Původní vadný důkaz a^(n−1)=1 v kroku n=1 nepřípustně používá
   a^((n−1)−1)=a^(−1)=1. Předpoklad poskytuje jen exponenty od 0
   do n−1. Už a=2,n=2 vyvrací závěr. Verze z 19. dubna 2019 místo
   toho zavádí b=a^((n−2)/(n−1)); při n=1 však není b definováno.
   Odpovídající nová odpověď je správná. Vadný důkaz je záměrné zadání.
3. Součet 1/(k(k+1)) pro 1<=k<n je 1−1/n, protože člen je
   1/k−1/(k+1). Při n=1 je součet prázdný, tedy 0. Chybný důkaz
   přiřadí tomuto případu první nenulový člen 1/2. Pro n=6 jsou
   vytištěné hodnoty 5/6 a 4/3 skutečně odlišné. I zde jde o záměr.
5. Je-li celé N>1 prvočíslo, představuje součin jediného prvočísla.
   Jinak N=uv s 1<u,v<N a indukce rozloží oba činitele. Dokazuje se
   existence rozkladu, nikoli jeho jednoznačnost; odpověď je správná.
7. Označme S_n=n^2−(n−1)^2+...+(−1)^(n−1)1^2. Pak S_1=1
   a S_(n+1)=(n+1)^2−S_n, odkud S_n=n(n+1)/2.
8. N-tá skupina n lichých čísel začíná n^2−n+1 a končí n^2+n−1.
   Pro přechod k n+1 přičteme 2n ke každému starému členu a navíc
   nový poslední člen n^2+3n+1. Součet se změní z n^3 na
   n^3+2n^2+n^2+3n+1=(n+1)^3. Skupiny na sebe navazují bez mezery,
   takže součet prvních n krychlí je čtverec počtu použitých lichých
   čísel, tj. (1+...+n)^2. Oprava úvodu odpovědi z roku 2005 dává
   též n(n^2−n)+(1+3+...+(2n−1))=n^3; netrpí nejasným prázdným
   rozdílem součtů pro n=1 ve staré formulaci.
9. Správné znaménko je **>=**, nikoli OCR `>`. Pro 0<a<1 platí
   (1−a)^n>=1−na pro všechna celá n, jak upřesňují errata 2019.
   Z n>=0 postupujeme vzhůru: po vynásobení 1−a přibude k cílové
   pravé straně nezáporný člen na^2. Z n+1<=0 postupujeme dolů:
   (1−(n+1)a)/(1−a)=(1−na)−na^2/(1−a)>=1−na.
   Základ n=0 je rovnost. Tím jsou zahrnuty i záporné exponenty.
10. Základ 2^10=1024>1000 je správný. Pro n>=10 platí
    (1+1/n)^3<2, takže 2^(n+1)>2n^3>(n+1)^3. Starý první
    mezikrok s pevnou 1/10 a následující rovností s 1/n přepisovalo
    erratum z 6. ledna 1998. Obě meze jsou pravdivé; oprava dává
    souvislý řetěz s proměnným n.
11. Položme B_k=4k^2+1 a A_k=k/B_k. Přímým roznásobením
    (2k+1)^4+4=B_k B_(k+1) a
    (2k+1)^3=k B_(k+1)+(k+1)B_k. Sčítaný člen je tedy
    (−1)^k(A_k+A_(k+1)). Mezilehlé členy se zruší a A_0=0 dává
    přesně (−1)^n(n+1)/(4(n+1)^2+1). Je to zároveň indukční důkaz.

### Geometrie obrázku 5

Čtverec strany n(n+1) se rozdělí na vnitřní čtverec strany n(n−1)
a rám šířky n. Rám tvoří 4n čtverečků strany n; jeho plocha je
4n^3. Opakováním pro n−1,...,1 dostaneme plochu
4(1^3+...+n^3). Vnější strana je současně 2(1+...+n), což dává
požadovanou identitu. V obrázku n=5 je všech pět rámů přítomno,
ale původní popisek plochy vynechal 4·4·4^2=256. Vytištěný
součet je proto 644 místo 900. Oprava 30. července 1997 je
V1-X0027; změna atribuce Floyd->Warren Lushbaugh z roku 2004
zůstává zdrojovým údajem k ověření, nikoli novým matematickým nálezem.

## 4. Úloha 12: dva různé významy dělení v Z[sqrt(2)]

Z[sqrt(2)] značí čísla u+v sqrt(2) s celočíselnými u,v. Rovnost
dvou takových čísel znamená rovnost obou koeficientů, protože sqrt(2)
je iracionální. Znaménko se zjistí bez desetinné aproximace: při
souhlasných znaménkách u,v je zřejmé; při opačných porovnáme u^2
s 2v^2. Pro nenulové u,v nemůže nastat rovnost těchto čtverců.

První varianta zachovává celočíselný podíl q a podmínku 0<=r<d.
Opakované odečítání kladného d od c zjistí q v konečném počtu
kroků; jeho konečnost plyne z Archimedovy vlastnosti reálných čísel.
Každé jednotlivé dělení je tedy efektivní, i když celá metoda nemusí
skončit. Pro m=1,n=sqrt(2) by při ukončení poslední nenulový
zbytek d dával 1=kd a sqrt(2)=ld s kladnými celými k,l. Poměr
sqrt(2)=l/k je nemožný. Nejde o závěr odvozený z dlouhého běhu.

Číselný příklad z textu je společný násobek dvojice (3,5) číslem
4−2sqrt(2)>0. Podíly jsou 0,1,1,2, výsledek 4−2sqrt(2)
a koeficienty 2,−1. Všechny původní aserce platí s dělitelností
definovanou celočíselným násobkem. Pokračování dělení odpovídá
rozvoji poměru c/d na řetězový zlomek: c/d=q+r/d a další poměr
d/r je převrácenou hodnotou zlomkové části. Není nutno přebírat
hlubší výsledky o řetězových zlomcích.

Druhá varianta v poznámce odpovědi dovoluje podíl q v Z[sqrt(2)].
Normou N(u+v sqrt(2)) nazveme celé číslo u^2−2v^2. Je nenulové
pro nenulový argument a násobí se: N(xy)=N(x)N(y). Pro d!=0
jsou koeficienty x,y v c/d=x+y sqrt(2) racionální, protože
c/d=c conjugate(d)/N(d), kde conjugate(u+v sqrt(2))=u−v sqrt(2).
Zaokrouhleme x,y na nejbližší celá U,V a položme q=U+V sqrt(2).
Pak r=c−qd splňuje

```text
|N(r)| = |N(d)| · |(x−U)^2 − 2(y−V)^2|
       <= |N(d)|/2 < |N(d)|.
```

Poslední ostrá nerovnost platí, neboť N(d)!=0. Tedy absolutní
normy nenulových zbytků jsou klesající kladná celá čísla a metoda
skončí. Změny koeficientů stále zachovávají Bézoutovu rovnost
am+bn=d, nyní s a,b v tomto okruhu. Poslední d dělí oba vstupy
a každý jejich společný dělitel dělí d. To je význam gcd v okruhu;
nevyžaduje se největší reálná velikost mezi jeho asociovanými prvky.
Poznámka v odpovědi je matematicky správná, včetně zaokrouhlovacích vazeb.

## 5. Úloha 13: přesná mez hodin

T počítá provedené kroky E1–E4 a zvětšuje se na začátku každého z nich.
K A1 se přidá T=0, k A2 T=1 a k A3,A4,A5,A6 se přidají postupně

```text
T<=3(n−d)+2,  T<=3(n−d)+3,  T<=3(n−d)+3,  T<=3(n−d)+1.
```

K A4 se navíc přidá d>0. Přechody E1,E2,E3 zachovávají tyto meze
přímo. V E4 máme staré d>=r+1, a proto po zvýšení T a nastavení d=r
platí T<=3(n−d_old)+4<=3(n−r)+1. Každá aserce tak implikuje T<=3n.
Neomezený běh by vytvářel stále větší T, což je spor. Počet dělení L
dává přesně T=3L; mez 3n není asymptotický odhad, ale platí pro každý
vstup. Původní n=0 v zadání je známý překlep opravený 27. listopadu
1997 na n>0 (V1-X0028). OCR navíc vypouští rovnost ze znaménka <=.

## 6. Úloha 15: dobrá uspořádání

Dobré uspořádání je striktní úplné uspořádání, v němž každá neprázdná
podmnožina má nejmenší prvek. Striktní znamená x není menší než x;
úplnost umožňuje porovnat každé dva různé prvky.

- (a) Celá čísla s obvyklým < nemají nejmenší prvek: pod každým x
  leží x−1. (b) Pořadí 0,−1,1,−2,2,... je dobré: nejprve se
  minimalizuje absolutní hodnota a pak znaménko. Odpověď jej vystihuje.
- (c) Kladná reálná čísla nemají nejmenší prvek, protože x/2<x.
  Proto ani nezáporná reálná čísla nejsou dobře uspořádána pomocí <.
  Poznámka o „explicitním“ jiném uspořádání není přesně definovaný
  matematický požadavek. Je třeba odlišit existenci z axiomu výběru
  od definovatelnosti v konkrétním modelu; historická formulace této
  poznámky není tímto elementárním důkazem certifikována.
- (d) Pro pevnou délku n vybíráme postupně nejmenší dostupnou první,
  druhou atd. souřadnici neprázdné množiny n-tic. Konečný postup dá
  lexikografické minimum. Tranzitivita a trichotomie se přenesou
  porovnáním první rozdílné souřadnice. Platí i pro prázdné S,
  kdy není žádná neprázdná podmnožina n-tic k posouzení.
- (e) Pro proměnnou délku a dva prvky a<b je posloupnost
  (b),(a,b),(a,a,b),... striktně klesající. Výjimky |S|=0,1
  skutečně jsou dobře uspořádané. Pokud se nejprve porovnává délka
  a až při stejné délce lexikograficky, získáme dobré uspořádání:
  zvolíme nejmenší délku a použijeme (d). Překlep oddělovače
  souřadnic v odpovědi je známý z 16. prosince 1997.
- (f) Nekonečný sestup by tvořil neprázdnou množinu bez minima.
  Obráceně lze v množině bez minima opakovaně vybrat menší prvek.
  Tato druhá implikace používá závislé volby, které jsou v obvyklém
  rámci ZFC k dispozici; není zde vydávána za tvrzení bez axiomu výběru.
- (g) Množina protipříkladů by měla nejmenší prvek x. Všechny
  předchůdce už splňují P, takže indukční předpoklad vynutí P(x).
  Proto protipříklad neexistuje. Stejný argument s hodnotami klesající
  stavové funkce dokazuje uvedené kritérium ukončení algoritmu.

## 7. Otevřený rozsah, errata a reprodukce

Úloha 14 je výzkumné zadání s hodnocením 50, bez odpovědi na s. 468–469.
Požaduje program, který se pokouší doplňovat aserce; netvrdí existenci
úplného rozhodovacího algoritmu pro správnost libovolného programu.
Naše kontrola konkrétního Euclidova programu neřeší tuto výzkumnou úlohu.
Citované práce Floyda a Kinga z IFIP 1971 ještě potřebují kontrolu
primárního textu. Podobně zůstávají historické citace s. 17–18 a
atribuce obrázku 5. Úloha 15 má hotové matematické části (a)–(g),
ale její neformální poznámka o explicitním uspořádání reálných čísel
vyžaduje samostatné posouzení; celé cvičení proto zůstává `partial`.

Prohledány `all1-prepre`, `all1-pre`, `all1`, `err1` pro s. 10–21,
468–469 i indukci, Euclida, Floyda, Hoara a Maurolica. Zobrazeny
relevantní sazby errat: první řada s. 4–5,30–31, druhá s. 4,13
a současná s. 3. Změna tvrzení o prvním evropském užití indukce
z roku 2023 je známá a nepřebíráme staré tvrzení o prvenství.

`check_induction.py` prošel jednou: 16 384 vstupů 1<=m,n<=128,
všechny aserce a hodiny v každém kroku, nezávislý gcd přes výčet
dělitelů; dále 257 racionálních součtů, 100 indexů součtových identit,
11 590 racionálních případů Bernoulliho nerovnosti včetně záporných
n a 14 520 dvojic v Z[sqrt(2)] s koeficienty −5,...,5 a druhým
vstupem nenulovým. U posledních se kontroluje pokles normy, Bézoutova
rovnost i dělitelnost obou vstupů výsledkem. Vše používá přesná celá
a racionální čísla. Výsledky jsou v `results/induction.json`.

# Obnova celé 4.1–33: každá počítací rovnost a rozsah algoritmu

Zadání213/file225 a odpověď610–611/file622–623 znovu vizuálně
porovnány. `digit-recurrence.md` §§1–5 obsahuje dostatečný důkaz
věty pro konečné D; níže se samostatně dokládá každá tištěná
množinová rovnost, mez, inicializace a řádek příkladu. Doplněn
je i přesný význam určení koeficientů z konečného prefixu.
Žádný archivní výpočet se neopakoval. Existující C0081 zůstává
kandidátem rozsahu; doslovně neomezené D se nepovýšuje na checked.

## Hodnoty, prázdná a jednoprvková množina, posuny vzorů

K_n jsou různé hodnoty slov přesně n cifer. Rozdílná slova
mohou mít stejnou hodnotu; počítá se množina hodnot, ne |D|^n.
K_0={0}, neboť prázdný součet má hodnotu0. Oddělením poslední
cifry dostáváme přesně K_n=bK_(n−1)+D pro n≥1; obě inkluze
vznikají odstraněním, resp. připojením této cifry. Nevyžaduje
se vedoucí nenulová cifra; při0∈D smíme mít vedoucí nuly.

Pro D=∅ je K_n=∅ pro n≥1, k_0=1,k_n=0 a generující funkce1.
Pro D={d} je jen jedna hodnota dΣ_(j<n)b^j, takže k_n=1 pro
všechna n a funkce1/(1−z). Při b=1 je tato hodnota nd.
Tyto kraje jsou vyřešeny přímo, bez min/max prázdné množiny.

Nyní D konečné neprázdné a b≥2. Relace S~T znamená rovnost
S=T+x s celočíselným x; jde o ekvivalenci (posun0,inverzní
posun a skládání posunů). Pro neprázdný konečný S je posun
x určující konkrétní kopii x+S jedinečný: x=min(x+S)−minS.
Rodina takových podmnožin K_n je proto v bijekci s přípustnými
posuny a její počet je k_n(S). Posunutí S jen přeznačí x,
takže k_n(S+c)=k_n(S). Jednoprvkový vzor má jednu kopii pro
každý prvek K_n, tedy k_n(S)=k_n.

Pro n=0 má každý singleton právě jednu kopii{0}; vzor s více
než jedním prvkem žádnou. Prázdný vzor má také právě jednu
kopii, samotnou∅, nikoli nekonečně mnoho kopií za všechny
posuny. Proto je vytištěné k_0(S)=[|S|≤1] správně. Prázdný
vzor však musí být z následné počítací formule se zbytky
vypuštěn; konkrétní rozsah této výjimky je na konci poznámky.

## Množinová rovnost610 a určení všech indexů

Nechť S={s_1,…,s_r} je neprázdné, prvky různé, r≥1. Posun x
má jedinečný Eukleidův rozklad x=bq+j,0≤j<b; platí to i pro
záporné x. Pro x+s_i∈K_n volíme poslední cifru a_i∈D a číslo
t_i∈K_(n−1), aby x+s_i=bt_i+a_i. Redukce modulo b vynucuje
a_i≡s_i+j mod b a dělení dává t_i=q+(s_i+j−a_i)/b.
Obráceně každé takové přiřazení a_i a společný q dávají právě
kopii x+S v K_n. Tím jsou dokázány obě inkluze velké tištěné
sjednocovací rovnosti, nikoli jen shoda počtů.

Zaveďme T_α={(s_i+j−a_i)/b:1≤i≤r} pro přiřazení α=(a_i).
Některé členy mohou být shodné; T_α je skutečná množina,
nikoli multiset. Tištěné pojmenování t_i se určuje rozdíly
t_i−t_i'=(s_i−a_i)/b−(s_i'−a_i')/b.
Člen j se v rozdílu ruší. Právě tyto rovnosti znamenají, že
všechny t_i vznikly z téhož posunu q původního T_α; naopak
společný posun je zaručuje. Pro neprázdnou konečnou množinu
je posun q její kopie jedinečný, takže jsou hodnoty všech
pojmenovaných t_i určeny i při opakovaných prvcích T_α.

Pro pevné j a α nastává příslušná kopie právě pro
Q_α={q∈Z:q+T_α⊆K_(n−1)}. Každé Q_α je konečné: vybereme
jeden člen T_α a jeho obraz může ležet jen v konečném K_(n−1).
Počet přiřazení α je také konečný, nejvýše |D|^r. Když
některý požadovaný zbytek nemá cifru v D, příslušných α je0,
a daná větev přispívá prázdnou rodinou a počtem0.

Kopie odpovídající různým j jsou disjunktní: z hotové kopie
S+x je jedinečný x, tedy i x mod b. V jednom pevném j mohou
různá přiřazení vytvořit stejnou kopii; proto je nutná inkluze
a exkluze. Samotné sečtení všech přiřazení by bylo chybné.

## Každý průnik, koeficient a obě meze611

Pro různá přiřazení α_1,…,α_m při témže j platí přesně
∩_(l=1..m)Q_(α_l)={q:q+∪_(l=1..m)T_(α_l)⊆K_(n−1)}.
Sjednocení vpravo tedy obsahuje všechny vytištěné členy
(s_i+j−a_i^(l))/b,1≤i≤r,1≤l≤m. Je neprázdné a jeho počet
kopií je k_(n−1) tohoto sjednoceného vzoru. To je první věta
na611 i přesný obsah f(S,m,j) z610. Rozdílné rodiny α mohou
mít stejné Q; inkluze a exkluze funguje i v tomto případě,
protože jde o konečnou indexovanou rodinu množin.

Pro m≥1 má průnik znaménko(−1)^(m−1). Sečtení přes všechny
m-prvkové podrodiny a potom přes disjunktní j dává tištěnou
formuli pro k_n(S). Po seskupení totožných nebo posunutím
ekvivalentních vzorů T je koeficient c_T součtem celých±1,
tedy celé číslo nezávislé na n. Vzor se smí normalizovat až
po sjednocení všech T_(α_l); normalizovat je před sjednocením
by změnilo jejich vzájemné polohy a zpravidla průnik.

Každý člen výsledného T má tvar(s+j−a)/b se s∈S,a∈D,
0≤j≤b−1. Proto
minT≥(minS−maxD)/b,
maxT≤(maxS+b−1−minD)/b.
Obě nerovnosti jsou neostré, přesně jako originál, a platí
i pro záporné s,a. Při průniku je j společné, takže rozpětí
navíc splňuje span(T)≤(span(S)+maxD−minD)/b.

## Přesná tištěná konečná oblast a získání generující funkce

Přebíráme pouze definice l=−maxD/(b−1),u=−minD/(b−1)
z úlohy19; její předpoklad jedné cifry na zbytek zde není
potřeba. Pro S⊆[l,u+1] dávají právě dokázané meze
minT≥(l−maxD)/b=l,
maxT≤(u+1+b−1−minD)/b=u+1.
Všechny T tedy zůstávají v téže konečné množině celých bodů
J=Z∩[l,u+1]. D je neprázdné, takže l≤u a interval má délku
nejméně1; obsahuje alespoň jeden celý bod. Mezi neprázdnými
podmnožinami J proto je singleton, jehož posloupnost je k_n.
Počet všech takových vzorů je d=2^|J|−1, konečný; slučování
posunutých vzorů je jen volitelné zmenšení systému.

Vyjmenujeme vzory a jejich konečná přiřazení/průniky. Dostaneme
celočíselnou matici M a vektor v_n všech k_n(S), s v_n=Mv_(n−1).
Počáteční vektor má1 u singletonů,0 jinde. V generující řadě
V(z)=Σ_(n≥0)v_nz^n posun indexu přesně dává
V(z)=v_0+zMV(z). Po složkách je to vytištěná rovnice
k_S(z)=[|S|≤1]+zΣ_T c_T k_T(z), nyní pro neprázdné S.
Matice I−zM má konstantní člen I, tudíž formální inverzi;
pomocí adjungované matice jsou všechny složky racionální
s jmenovatelem det(I−zM), který má konstantní člen1.
Singletonová složka je požadovaná Σk_nz^n.

Přímo: charakteristický polynom χ_M(t) je monický stupně d
s celočíselnými koeficienty. Cayleyho–Hamiltonova identita
χ_M(M)=0 po aplikaci na každé v_n dává homogenní rekurenci
s konstantními koeficienty pro všechny složky. Její platnost
není odhadnutá pouze z prvních hodnot.

Tištěnou větu o určení c_T z „first few values“ lze nyní
zpřesnit konečným důkazem. Pro každý řádek nechť L_j je počet
povolených přiřazení a B=Σ_(j=0..b−1)(2^L_j−1). Je to horní
mez součtu absolutních hodnot příspěvků před seskupením,
takže každý skutečný c_T leží v[−B,B]. Vyjmenujme všechny
celočíselné řádky v tomto konečném boxu (případně jen povolené
sloupce) a vyberme kterýkoli splňující rovnice pro n=1,…,d,
kde v_0,…,v_d byly vypočteny přímo z konečných K_n. Nejméně
jeden takový řádek existuje, totiž skutečný kombinatorický řádek.
Pro rozdíl nalezeného a skutečného řádku a je a·v_t=0 pro
0≤t<d. Jelikož v_t=M^t v_0, stejná charakteristická rekurence
vynucuje a·v_t=0 i pro všechna t≥d. Nalezené koeficienty tedy
dávají správnou rovnici pro každý n, i když nejsou jednoznačné.
Tím je doloženo konkrétně prvních d+1 vektorů a konečný postup;
nepřisuzujeme mu dobrou praktickou složitost. Neomezené hádání
rekurence z libovolně krátkého prefixu by tento důkaz nenahradilo.

## Fibonacciho příklad: všechny čtyři řádky bez interpolace

Pro D={−1,0,3},b=3 je l=−3/2,u=1/2, takže J={−1,0,1}.
Jeho7 neprázdných podmnožin po posunech dávají právě čtyři
třídy: singleton{0}, sousední pár{0,1}, pár{−1,1} ekvivalentní
{0,2}, a trojici{−1,0,1} ekvivalentní{0,1,2}. V D jsou dvě
cifry zbytku0 (0,3), žádná zbytku1 a jediná zbytku2 (−1).
Označme příslušné posloupnosti a_n,b_n,c_n,d_n.

Pro S={0}:
* j=0: cifry0,3 dávají T={0},{−1}; sjednocení{−1,0}.
  Příspěvek je2a_(n−1)−b_(n−1).
* j=1: žádná cifra, příspěvek0.
* j=2: cifra−1 dává T={1}, příspěvek a_(n−1).
Tedy a_n=3a_(n−1)−b_(n−1).

Pro S={0,1}:
* j=0 vyžaduje chybějící zbytek1 u s=1; j=1 jej vyžaduje
  u s=0. Obě větve jsou prázdné.
* j=2: přiřazení(−1,0) dává T={1}, přiřazení(−1,3) dává
  T={0,1}; jejich sjednocení je{0,1}. Součet s odečtením
  průniku je a_(n−1)+b_(n−1)−b_(n−1)=a_(n−1).
Tedy b_n=a_(n−1), včetně vysvětlení přesného zrušení dvou členů.

Pro S={0,2}:
* j=0: přiřazení(0,−1) dává T={0,1}, přiřazení(3,−1)
  dává T={−1,1}; sjednocení je{−1,0,1}.
* j=1 vyžaduje chybějící zbytek1 u s=0, j=2 u s=2.
Tedy c_n=b_(n−1)+c_(n−1)−d_(n−1).

Pro S={0,1,2} při každém j jeden prvek vyžaduje zbytek1,
takže d_n=0 pro n≥1. Také d_0=0, protože K_0={0}.
Proto lze člen−d_(n−1) v předchozí rovnici vypustit pro každý
n≥1, jak kniha činí. Stejný důvod lze vyjádřit tím, že K_n
pro n≥1 nemá žádný prvek1 mod3 a nemůže obsahovat tři sousedy.

Tím jsou odvozeny všechny prvky matice
M=((3,−1,0,0),(1,0,0,0),(0,1,1,−1),(0,0,0,0)).
Z v_0=(1,0,0,0) dostaneme přesně
v_1=(3,1,0,0), v_2=(9−1,3,1,0)=(8,3,1,0),
v_3=(24−3,8,1+3,0)=(21,8,4,0).
Tyto čtyři vektory dokazují každou z16 tištěných počátečních
hodnot pro n≤3. Nejsou použity k neodůvodněnému hádání M.

Generující funkce splňují přesně čtyři tištěné rovnice
A=1+z(3A−B), B=zA, C=z(B+C), D=0.
Dosazení dává A=1/(1−3z+z²), B=z/(1−3z+z²),
C=z²/((1−z)(1−3z+z²)). Z Fibonacciho rekurence plyne
F_(r+4)=3F_(r+2)−F_r; a_0=F_2=1,a_1=F_4=3, takže
a_n=F_(2n+2) pro všechny n≥0.
Pro n≥1 platí c_n=Σ_(t=1..n−1)F_(2t). Protože
F_(2t)=F_(2t+1)−F_(2t−1), součet teleskopuje na
c_n=F_(2n−1)−1. Pro n=1 je prázdný součet0; pro n=0
je c_0=0 zvlášť. Poslední tištěná formule platí i tam,
pokud F_(−1)=1 podle zpětného prodloužení Fibonacciho rekurence.
Žádná nová chyba Fibonacciho hodnot z toho neplyne.

## Základ1: celý samostatný důkaz včetně efektivního prahu

Pro b=1 jsou K_n n-násobné součtové množiny. Prázdnou a
jednoprvkovou D jsme vyřešili. Jinak odečteme d_min a vydělíme
rozdíly kladným g=gcd{d−d_min:d∈D}. Na K_n jde o bijekci
x↦(x−nd_min)/g, která nemění počet. Výsledná E má min0,
maxh>0 a gcd(E)=1. Také E'=h−E má min0,maxh a gcd1,
protože h∈E a společný dělitel h a h−e dělí všechna e.

Součty E generují všechny zbytkové třídy modulo h: nezáporné
kombinace v konečné cyklické grupě tvoří podgrupu, jelikož
inverzi prvku řádu t nahradí(t−1) kopií téhož prvku. gcd(E)=1
pak dává celou grupu. Pro každý r∈{0,…,h−1} tedy existuje
nejmenší nezáporný součet w_r v této třídě. Zvolme jeho
zápis s ℓ_r členy E. Najdeme ho konečně v grafu h zbytků,
kde přičtení e∈E má nezápornou cenu e; z nejkratší cesty
lze odstranit cykly, takže stačí konečně mnoho jednoduchých
cest a ℓ_r≤h−1. Pro r=0 stačí prázdná cesta. Totéž dává
w'_s,ℓ'_s pro E'. Když h=1, jediná třída má obě hodnoty0.

Položme N=max_r(ℓ_r+ℓ'_(−r mod h)). Pro n≥N a s=−r mod h
zápis w_r doplníme ciframi h a0 na n míst. Dostaneme všechny
členy třídy r v posloupnosti
w_r,w_r+h,…,w_r+h(n−ℓ_r).
Zrcadlením analogické posloupnosti pro w'_s dostaneme
hℓ'_s−w'_s,…,nh−w'_s, opět krokh a stejný zbytek r.
První horní konec je nejméně druhý dolní, protože rozdíl je
h(n−ℓ_r−ℓ'_s)+w_r+w'_s≥0. Obě posloupnosti se tedy dotýkají
nebo překrývají. Každý součet E v této třídě je≥w_r podle
minimality, a jeho zrcadlený n-ciferný součet E' je≥w'_s,
takže je≤nh−w'_s. Obě posloupnosti proto společně vyčerpají
přesně celý interval mezi těmito krajními členy, bez mezer.

V semigrupě všech součtů E jsou v třídě r právě hodnoty
w_r+th,t≥0: všechny jsou možné doplněním h, menší nejsou
možné z minimality. Počet nezáporných mezer je tedy
G=Σ_r(w_r−r)/h; konečné nezáporné celé číslo. Analogicky G'.
Pro každou třídu má n-ciferný interval
(nh−w_r−w'_s)/h+1 členů. Součet přes r užívá
Σ_rw_r=hG+h(h−1)/2 a stejný vzorec pro w'_s, neboť
r↦−r modh je permutace. Vyjde přesně
k_n=nh+1−G−G' pro n≥N.

Konečný prefix se vypočte přímo opakovaným sčítáním konečných
množin. Celá generující funkce je
Σ_(n<N)k_nz^n+z^N((Nh+1−G−G')/(1−z)+hz/(1−z)²).
Při N=0 je prefix prázdný, vzorec stále platí. Zvláště pro
E={0,1},h=1,N=0 dostaneme k_n=n+1 a1/(1−z)².
Druhá diference je0 od N; charakteristický polynom
t^N(t−1)² tak dává homogenní rekurenci platnou od začátku
v obvyklém smyslu k_(j+N+2)−2k_(j+N+1)+k_(j+N)=0,j≥0.
Celá konečná věta je tedy uzavřena pro všechny kladné základy,
ačkoli tištěné meze obsahující b−1 samy větev b=1 nepokrývají.

## Přesný zachovaný kandidát C0081 a prázdný vzor

Doslovné „any set of integers“ zahrnuje D=Z; už K_1=Z je
nekonečná a k_1 není konečný celočíselný koeficient obyčejné
generující funkce. V kontextu konečné ciferné abecedy lze
konečnost přirozeně chápat implicitně, proto C0081 zůstává
redakčním kandidátem rozsahu. D=∅ zase nemá min/max a b=1
nemá definované l,u s dělitelem b−1; správné zvláštní větve
jsou nyní dokázány výše. Žádná z těchto výhrad nevyvrací
větu pro konečné D a kladné b.

Navíc na610 zavádí obecné konečné vzory S,T a připouští |S|≤1
v inicializaci; pro S=∅ je k_n(∅)=1 pro každý n. Množinové
sjednocení ještě platí, ale jeho převod na součet přes j
potřebuje S≠∅. Pro prázdný vzor existuje právě jedno prázdné
přiřazení α v každé třídě j, m=1 přispívá1 a všechny vyšší
m nic. Pravá strana počítací formule je tedy b, levá1.
Konkrétně b=2,D={0},S=∅,n=1 dává nesprávnou rovnost1=2.
Příčina je přesná: hotová prázdná kopie neurčuje jedinečný
posun x ani jeho zbytek j. Na611 následující systém už výslovně
užívá jen **nonempty integer subsets**, takže tato lokální
výjimka nezasahuje hlavní k_n, konečný systém ani příklad.
Do počítacího odstavce stačí výslovně přidat S≠∅.

Tento dodatečný okraj evidujeme pod stávajícím C0081 jako
zpřesnění rozsahu, nikoli pod novým ID. Originály213,610,611
a všechny čtyři vrstvy errat byly znovu porovnány/prohledány;
žádná související oprava33 nalezena. Novější fyzický dotisk
ani prvenství nejsou ověřeny. Kandidát není povýšen na confirmed.

## Bibliografie, archiv a uzavřený rozsah

Klarnerův článek *An algorithm to determine when certain sets
have 0-density*, Journal of Algorithms2(1981),31–43, má v
předchozí poznámce potvrzená vydavatelská metadata. Přímé
otevření `https://www.sciencedirect.com/science/article/abs/pii/0196677481900055`
nyní opět vrátilo403. Primární obsah se výslovně vynechává;
není použit k doplnění žádného chybějícího důkazu.

Pouze přečteno `results/digit-recurrence.json`: přesná matice,
generující funkce a příklady do n=10;224 matic,7368 hodnot
vzorů do hloubky5,maximální dimenze32;224 případů b=1,z toho
215 netriviálních,nejvyšší doložený práh60. Žádný běh obnoven
nebyl. Každá tištěná počítací rovnost je posouzena výše;
matematika pro konečné D včetně všech kladných b a příkladu
je uzavřená. Celé neomezené doslovné zadání a formulace pro
prázdný vzor zůstávají výslovnou otázkou rozsahu C0081.

# D187–D188 — celé MPR87–88, první zásahy a supremum

7. listopadu 2026. Zadání p20/file40, odpovědi
p383/file403 a PS p20/file26,p39–40/file45–46
přímo zobrazeny. Šest vrstev errat a tři TeX
zdroje v manifestu87–88; použitelné opravy nenalezeny.
D099 již doložil88(a) a D100 celé86. Tyto přesné
výsledky zůstávají zachovány bez opakování běhů.
Níže je úplná obecná enumerace, která zahrnuje
všechny další části, každý tištěný mezivýsledek
a dodatky. Dosažení suprema má samostatný úplný
důkaz v sequential-mpr-ex088-supremum.md.

## Základní zákon a obor t

Fig.P začíná stavem(1,1). Každé konečné slovo
s a červenými a b černými přidáními má pravděpodobnost

    a! b!/(a+b+1)!
      =1/((L+1) C(L,b)), L=a+b.

Je to přesně cestový součin dokázaný v D173;
proto jsou všechny cesty k pevnému uzlu stejně
pravděpodobné. Použití zde nepotřebuje nezávislost
jednotlivých barev (ta v urně neplatí).

Parametr t v t-árních ballotových číslech je celé
číslo≥2. To je obor odkazovaného kombinatorického
modelu, výslovný i v původním článku, Proposition5.2.
Vzorce pro tento parametr se neextrapolují na reálné t.

## Přesný počet prvních zásahů, včetně periodických slov

Potřebujeme následující elementární tvrzení.
Máme slova délky L s celočíselnými kroky≤1,
celkovým součtem d>0 a pevnými násobnostmi kroků.
Mezi L označenými cyklickými řezy libovolného
slova je právě d takových, že všechny neprázdné
částečné součty po řezu jsou kladné.

Důkaz: pro původní částečné součty A₀=0,…,A_L=d
položme m=min(A₀,…,A_{L−1}). Pro každé
h=m,m+1,…,m+d−1 existuje poslední index j<L
s A_j=h. Existence plyne z m≤0, konečné hodnoty d
a z toho, že kladné kroky nepřeskakují celé hladiny.

Řez za takovým j je kladný: každý pozdější A_i
je větší než h, jinak by cesta při pozdějším
výstupu k d musela znovu navštívit h. Po obtočení
je každá hladina A_i+d≥m+d>h. Obráceně,
kladný řez za j má všechny pozdější A_i>A_j,
takže globální minimum m leží nejpozději v j.
Obtočená část vyžaduje m+d>A_j, a tedy
m≤A_j≤m+d−1. Index j je posledním výskytem
této hladiny. Takové řezy jsou tudíž přesně
uvedené d řezy.

Při dvojím počítání označených dvojic(slovo,řez)
každé původní slovo dává d dobrých dvojic
a každé dobré výsledné slovo má právě L
inverzních dvojic. I u periodického slova
zůstávají označené polohy odlišné; žádný
předpoklad aperiodicity se nepoužívá.
Počet dobrých slov je proto d/L krát počet
všech slov daných násobností.

Nyní vezměme kroky+1 a−(t−1), s b zápornými
kroky a součtem d>0; délka je L=tb+d.
Počet všech slov je C(L,b). Obrácení pořadí
slova převádí podmínku „hladiny d poprvé
dosaženo právě v posledním kroku“ na podmínku
kladných neprázdných částečných součtů:
nový součet délky j je d−A_{L−j}.
Tedy počet prvních zásahů je přesně

    (d/L) C(L,b).                                  (1)

Poslední krok do d je+1; d nelze přeskočit
kladným krokem. To zajišťuje, že počítáme
všechny a pouze první zásahy.

## Přesná vazba na odkazy svazku4A

Původní sv4A p451/file468 obsahuje(23),
p452/file469 diagram(28), zadání36 je na
p476/file493 a příslušná obecná odpověď na
p790/file807. Všechny tyto zdrojové strany
byly přímo zobrazeny v potřebném rozsahu.

Pro t-ární ballotové číslo, p≥0,q≥(t−1)p,
přidáme k nezáporné cestě s p zápornými
a q kladnými kroky počáteční+1.
Dostaneme kladnou cestu délky p+q+1,
součtu q−(t−1)p+1. Předchozí řezový důkaz
tak dává celý použitý vzorec

    C^(t)_{p,q}
      =(q−(t−1)p+1)/(p+q+1) C(p+q+1,p)
      =(q−(t−1)p+1)/(q+1) C(p+q,p).

Pro t=2 je to přesně(23). Podmínka nezáporné
cesty je po obrácení orientace stejná jako
cesta v původním diagramu(28) z(p,q) do(0,0),
která neopustí povolenou oblast. Obě souřadnice
zaznamenávají počty zbývajících kroků.
Tím je doložen každý potřebný odkaz, nikoli
celý algoritmus generování stromů na těch
stránkách svazku4A.

## 88(a–c): každý uzel a každý faktor

Položme α=(t−1)/t a D=R−(t−1)B.
Na počátku D=2−t; červený tah přidá1,
černý odečte t−1. Událost S>α je přesně
událost, že v některém konečném čase D>0:
je-li supremum větší než α, musí existovat
člen nad α, a opačný směr je okamžitý.

První takový čas má D=1 a uzel
(R,B)=((t−1)k+1,k), k≥1. Má b=k−1
černých a a=(t−1)k červených tahů,
celkem L=tk−1. V součtech relativních
k počátku jde o první dosažení d=t−1.
Z(1) je počet příslušných slov

    (t−1)/(tk−1) C(tk−1,k−1).

Po vynásobení pravděpodobností jedné cesty:

    p_k=(t−1)/((tk−1)tk)
       =(t−1)(1/(tk−1)−1/(tk)).                   (2)

Všechny události prvního zásahu jsou disjunktní
a jejich sjednocení je právě S>α. Neztrácí se
žádná nekonečná cesta, která by α pouze limitně
dosahovala: taková cesta nepatří do ostré události.

Po odebrání posledního červeného tahu dostaneme
v jazyce sv4A p=k−1,q=(t−1)k−1, tedy
C^(t)_{k−1,(t−1)k−1}; předchozí obecný vzorec
dává tutéž hodnotu. Pro t=2 jde o Catalanovo
C_{k−1,k−1}. Tím je přesně spárována
knižní cesta v88(a) i použití t-árních čísel(b,c).

Definice AppendixA je
H_x=Σ_{j≥1}(1/j−1/(j+x)).
Všechny zde užité x jsou>−1; řada je absolutně
konvergentní, protože její člen je x/(j(j+x)).
Teleskopování dává H_{x+1}=H_x+1/(x+1).
Proto z(2)

    P(S>α)=−(1−1/t)H_{−1/t}
           =1−(1−1/t)H_{1−1/t}.                  (3)

To je každý faktor a celý součet tištěné(c).
Pro t=2 je p_k=1/(2k−1)−1/(2k);
součet je ln2, jak již doložil D099.
Níže uvedený integrální výpočet jej rovněž
identifikuje jako ∫₀¹1/(1+x) dx.

Pro t=3 dostáváme z nezáporné geometrické řady

    P(S>2/3)
      =2∫₀¹ (x−x²)/(1−x³) dx
      =2∫₀¹ x/(1+x+x²) dx
      =ln3−∫₀¹ dx/(x²+x+1)
      =ln3−π/(3√3)=ln3−π/√27.                    (4)

V posledním integrálu doplníme čtverec;
je to(2/√3)[arctan((2x+1)/√3)]₀¹,
s mezními úhly π/6 aπ/3. Výměna součtu
a integrálu je dovolena monotónní konvergencí
nezáporných členů, nikoli formální divergentní
rozdíl dvou harmonických řad.

## Slabá hranice a celá87

Pro celé t>2 uvažujme první dosažení D=0,
tedy R=(t−1)B. Počet tahů do uzlu
((t−1)k,k) je L=tk−2, počet černých k−1
a počáteční deficit d=t−2. Z(1) a
stejné cestové pravděpodobnosti vychází

    h_k=(t−2)/((tk−2)(tk−1)).                    (5)

Není možné dosáhnout D>0 bez předchozího
zásahu D=0, protože kladný krok je jen1.
Součet(5) je tedy pravděpodobnost, že
proces v konečném čase dosáhne nebo překročí α.
Pro t=2 je α=1/2 dosaženo již v čase0;
tento případ má pravděpodobnost1 a nevkládá
se do neurčitého prvního členu(5).

Úloha87 je t=4: „thrice as many red“ znamená
R=3B, ekvivalentně někdy Z_n≥3/4.
Pro konečný horizont m dává již úplně
dokázané(33)/MPR86

    P(max_{0≤n≤m}Z_n≥3/4)
      ≤ E Z_m/(3/4)=(1/2)/(3/4)=2/3.

Události s rostoucím m rostou, takže stejná
mez platí pro jejich sjednocení. E Z_m=1/2
je převzatý urnový martingale D098.
To doplňuje konečný i nekonečný rozsah
první věty tištěné odpovědi87.

Její přesný dovětek má podle(5) hodnotu

    Σ_{j≥0}2/((4j+2)(4j+3))
      =2∫₀¹ x/((1+x)(1+x²)) dx
      =∫₀¹ (−1/(1+x)+(x+1)/(1+x²)) dx
      =π/4−(1/2)ln2.                             (6)

Každý rozklad je přímá algebra; součet a
integrál lze opět prohodit nezáporností.
Z definice H a její rekurence je stejný
součet

    (1/2)(H_{−1/4}−H_{−1/2})
      =(1/2)H_{3/4}−(1/2)H_{1/2}+1/3,

takže i prostřední tištěný harmonický
výraz souhlasí, včetně konstanty1/3.

## Každý dodatek88 před hlubší větou

S≥Z₀=1/2 vždy. Z(a) tedy přímo plyne
P(S=1/2)=1−ln2, bez věty o dosažení suprema.

Pro t=3 dává součet(5)

    P(někdy Z_n≥2/3)
      =Σ_{j≥0}1/((3j+1)(3j+2))
      =∫₀¹ dx/(1+x+x²)=π/√27.                  (7)

Jde o případy, které procházejí některým
z uzlů(2,1),(4,2),(6,3),… . Odečtením
ostré události(4), která je podmnožinou
této návštěvní události, dostáváme

    P(S=2/3)≥2π/√27−ln3.                         (8)

Bez dalšího argumentu je zde skutečně
nejprve jen nerovnost. Posloupnost tahů
BRRBRR… má v každém čase R<2B, ale poměr
se blíží2/3. Po k blocích jsou počty
(2k+1,k+1); obě mezipozice také mají R<2B.
Supremum2/3 tedy nemusí být dosaženo jako
bodová vlastnost všech nekonečných cest.
Tato jednotlivá cesta má pravděpodobnost0,
ale samotná existence bodové výjimky
vysvětluje opatrnost tištěné poznámky.

Kniha při základních definicích používá
diskrétní prostory a nepřevádí bez další
teorie všechny nekonečné trajektorie
na již definovaný náhodný objekt S.
Konečné události max_{n≤m}Z_n>x jsou přesto
vždy definované a mají monotónní limity.
Náš další důkaz už výslovně pracuje na
standardním produktovém pravděpodobnostním
prostoru; tento krok není skryt za
bibliografickou citaci.

## Dosažení suprema a konečný atomový vzorec

Samostatná poznámka sequential-mpr-ex088-supremum.md
dokazuje, že supremum je dosaženo v konečném
čase s pravděpodobností1. Obsahuje každý krok:
přesnou směs Bernoulliho zákonů, konvergenci
z převzaté platné deterministické Hoeffdingovy
meze, elementární opuštění intervalu a
neomezené kladné výkyvy, konečné maximum.
Není převzata nedokázaná LIL ani hlubší
pravděpodobnostní výpočet.

Proto návštěvní událost(5) a událost S≥α
mají stejnou pravděpodobnost, a(8) je rovnost.
Všechny jednotlivé Z_n jsou racionální,
takže také P(S je racionální)=1. Je-li T
nejmenší čas dosažení maxima, T<∞ skoro
jistě, a tedy P(T≤m)→1; to je i přesný
význam tištěného „within n steps, a.s.“.

Pro t>2 lze(5) sečíst ještě obecně:

    P(S≥α)
      =(1−2/t)(H_{−1/t}−H_{−2/t})
      =(1−2/t)(H_{1−1/t}−H_{1−2/t})+1/(t−1).

Odečtením(3) je tudíž

    P(S=(t−1)/t)
      =(2−3/t)H_{1−1/t}
       −(1−2/t)H_{1−2/t}−(t−2)/(t−1).           (9)

Pro t=2 pravá strana samostatně dává
H_{1/2}/2=1−ln2, protože H₀=0.
Tím je pokryta i tato hranice finálního
tištěného vzorce, aniž bychom dosazovali
t=2 do(5).

## AppendixA a čtyři desetinné hodnoty

Původní p659/file679 byl přímo zobrazen.
Kontrolují se pouze definice H a hodnoty
H_{1/2},H_{2/3},H_{3/4}, které se zde používají;
ostatní tabulka se tím neprohlašuje za hotovou.

Integrální definice dává
H_{1/2}=∫₀¹2u/(1+u)du=2−2ln2.
Rovnice(3),(4) dává
H_{2/3}=3/2+π/(2√3)−(3/2)ln3.
Rovnice(6) a harmonický mezikrok dávají
H_{3/4}=4/3+π/2−3ln2. Všechny tři
tištěné hodnoty tedy souhlasí, včetně
jednotlivých koeficientů.

Jediný nový cílený běh ověřil pouze
zaokrouhlení čtyř již přesně odvozených
konstant:87→.439,88(a)→.693,88(b)→.494
a atom2/3→.111. Trval0.0011198559659533203s,
nice15; žádná enumerace ani simulace.
Skript verify_mpr087_088_rounding.py ukládá
přesné racionální intervaly, nikoli jen
plovoucí porovnání.

Používá střídavé zbytky arctan řad,
Machinovu identitu π=16atan(1/5)−4atan(1/239),
kladnou řadu ln((1+z)/(1−z)) a geometrickou
horní mez jejího zbytku. Machinova identita
se ověří přes tan(2atan(1/5))=5/12,
tan(4atan(1/5))=120/119 a
tan(4atan(1/5)−atan(1/239))=1, s úhlem
v(0,π/2). Pro ln2 je z=1/3, pro ln3
z=1/2. Obě meze√3 se dokazují přesným
umocněním racionálních čísel. Skript má
pevně omezené konečné součty a všechny
čtyři intervaly leží uvnitř příslušného
zaokrouhlovacího intervalu šířky.001.

## Bibliografie a uzavření

Autorský [Schulte-Geers–Stadje, arXiv1401.1805v4](https://arxiv.org/pdf/1401.1805)
byl stažen; původní strany3,4 a10 přímo
zobrazeny. Theorem3.1, Propositions3.2–3.3
a5.2 odpovídají zde posouzené reprezentaci,
dosažení maxima a finálnímu vzorci.
Publikační metadata52(2015),180–190
potvrzuje [původní vydavatelský index](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/6D05942A39A0DB2A92960D1A613223BD/S0021900200113208a.pdf/journal_of_applied_probability_volume_52_2015_index.pdf).
Není potřeba nová bibliografická výjimka.

Celé87 a88(a–c), všechny poznámky, odkazy,
všechny ostrosti a každý tištěný výraz
jsou uzavřeny. Žádný nový nález/kandidát.
Dřívější partial88 z D099 je zachován jako
historický omezený rozsah a doplněn D188.
Staré výpočty ani censy nebyly zopakovány.


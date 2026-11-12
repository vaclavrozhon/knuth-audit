# Úloha15: úplné rekurence, derivace, rozptyl a dodatky odpovědi

Zadání103/file114, odpovědi620–621/file631–632,
hlavní tvrzení88/file99. Původní sazba zobrazena;
pět vrstev v `sources/insertion-errata-review.json`.
Používá se oprava2002: v rekurenci ĝ_n je g_(n−1)(z),
nikoli nevyznačená konstanta. Žádný program ani nový nález.
Níže n označuje **polovinu** délky cesty, tedy permutaci2n prvků.

## P0740: rozklad kladné cesty při prvním návratu

g_n počítá cesty z(0,0) do(n,n), které neprojdou
pod diagonálu i=j; váha W je součet svislých vah|i−j|.
ĝ_n pro n>0 navíc zakazuje vnitřní návrat na diagonálu.
Taková primitivní cesta začíná R a končí D. Po odstranění
prvního a posledního kroku a překladu zbývá právě
libovolná cesta počítaná g_(n−1). Každý z n−1 vnitřních
kroků D má o1 větší výšku, poslední D má váhu1.
Obousměrná konstrukce tedy dává

    ĝ_n(z)=z^n g_(n−1)(z).

Každá neprázdná kladná cesta má jednoznačný první návrat
po2k krocích. Její první část je primitivní a zbytek
po překladu libovolný; váhy se sčítají. Proto

    g₀=1,  g_n=∑_(k=1)^n ĝ_k g_(n−k).

Rozklad a spojení jsou vzájemně inverzní, takže
rekurence nevynechává žádné cesty a žádné nezdvojuje.

## P0741: odraz primitivní cesty a jeho přesný mocninný posun

Primitivní neomezená cesta leží uvnitř buď přísně
nad, nebo přísně pod diagonálou. Transpozice i↔j
je mezi těmito dvěma třídami bijekce. U kladné cesty
má vodorovný krok končící v(i,j) váhu j−i podle P0729;
po transpozici z něj vznikne D se startem(j−1,i)
a vahou j−1−i, tedy o1 menší. Je právě n takových
kroků. Proto celková váha odrazu je W−n, nikoli W.

To dává

    ĥ_n=ĝ_n+z^(−n)ĝ_n=(z^n+1)g_(n−1),
    h₀=1,  h_n=∑_(k=1)^n ĥ_k h_(n−k).

Záporný exponent zde nezavádí záporné váhy: ĝ_n
je dělitelný z^n, jak již dokázal P0740. Úplný
neomezený rozklad je zase podle prvního návratu.

## P0742: obě dvouparametrické GF a jednoznačnost

Polož G(w,z)=∑g_n(z)w^n a H(w,z)=∑h_n(z)w^n.
Předchozí rekurence dávají přesně

    G=1+wz G(wz,z)G(w,z),
    H=1+w(zG(wz,z)+G(w,z))H.

Každý koeficient w^n je polynom v z a pravé strany
obsahují v novém členu faktor w. Při G(0,z)=H(0,z)=1
jsou tedy všechny koeficienty určeny indukcí podle n.
Všechna následující derivování je formální po koeficientech;
není třeba tvrdit analytickou konvergenci v okolí z=1.

## P0743: všechny počáteční polynomy v zadání

Pro n=1 dávají rekurence g₁=ĝ₁=z, h₁=ĥ₁=z+1.
Pro n=2 je ĝ₂=z²g₁=z³,
g₂=ĝ₁g₁+ĝ₂=z²+z³;
ĥ₂=ĝ₂+z^(−2)ĝ₂=z³+z,
h₂=ĥ₁h₁+ĥ₂=z³+z²+3z+1.
Spolu s g₀=h₀=1 je tím ověřena každá vytištěná
počáteční hodnota a její přesný význam2n kroků.

## P0744: G při z=1 a obě čisté w-derivace

Piš t=sqrt(1−4w), C=G(w,1). Z první GF plyne
C=1+wC² a podmínka C(0)=1 vybírá

    C=(1−t)/(2w)=2/(1+t),
    C_w=1/(wt)−(1−t)/(2w²),
    C_ww=2/(wt³)−2/(w²t)+(1−t)/w³.

Obě derivace vzniknou přímo z t_w=−2/t.
Ekvivalentně C_w=C²/t. Zdánlivé záporné mocniny w
se ruší: jde o derivace formální řady C, nikoli
skutečné póly v w=0. Pomocná identita
C+wC_w=1/t bude použita níže.

## P0745: první z-derivace a smíšená derivace

Označ U=G_z(w,1). Řetězové pravidlo dává
∂_z G(wz,z)|_(z=1)=wC_w+U. Derivace rovnice pro G je

    U=wC²+w²CC_w+2wCU.

Protože1−2wC=t, dostáváme

    tU=wC(C+wC_w)=wC/t,
    U=wC/t²=1/(2t²)−1/(2t),
    U_w=2/t⁴−1/t³.

To jsou přesně vytištěné G′ a jeho smíšená derivace;
spodní/vrchní apostrofy originálu se zde nahrazují
jednoznačnými indexy w,z.

## P0746: úplná druhá z-derivace G

Polož V=G_zz(w,1). Pro B(z)=G(wz,z) platí
B_z=wC_w+U a B_zz=w²C_ww+2wU_w+V při z=1.
Dvojnásobné derivování G=1+wzBG proto dává

    tV=2w²CC_w+4wCU+w³CC_ww
         +2w²CU_w+2w²C_wU+2wU².

Zvlášť jsou tedy zahrnuty oba smíšené členy a oba
výskyty V na pravé straně před jejich přesunem doleva.
Dosadíme-li w=(1−t²)/4, C=2/(1+t),
C_w=4/(t(1+t)²),
C_ww=8(1+3t)/(t³(1+t)³),
U=(1−t)/(2t²), U_w=(2−t)/t⁴,
pravá strana se zkrátí na

    (1−t)²(5t²+6t+5)/(8t⁴).

Po vydělení t a zpětném dosazení w je to přesně

    V=1/t³−(1−2w)/t⁴+10w²/t⁵.

Tím jsou doloženy všechny G-derivace v odpovědi,
nejen následný rozptylový výsledek.

## P0747: obě H-derivace včetně všech řetězových členů

Označ J(w,z)=w(zG(wz,z)+G(w,z)); pak H=(1−J)^(−1).
V bodě z=1 máme J₀=2wC=1−t, H₀=1/t a

    J₁=w(C+wC_w+2U)=w/t².

Proto H_z=J₁H₀²=w/t⁴, jak uvádí text.
Dále

    J₂=w(2wC_w+2U+w²C_ww+2wU_w+2V).

Identita2wC_w+w²C_ww=2w/t³ zjednoduší závorku
na2U+4w/t⁴+2V. Po vložení P0745–P0746 to je

    J₂=w(−1/t−1/t²+2/t³+20w²/t⁵).

Z H_zz=J₂H₀²+2J₁²H₀³ pak vychází

    H_zz=−w/t³−w/t⁴+2w/t⁵+(2w²+20w³)/t⁷.

Včetně členu2J₁²H₀³ je to celá rovnost odpovědi,
bez spoléhání na počítačovou symbolickou manipulaci.

## P0748: přesná extrakce druhého momentu

Protože pro exponent W platí W²=W(W−1)+W,
požadovaná GF součtu druhých mocnin je H_zz+H_z.
Předchozí vzorce a t²=1−4w dávají

    H_zz+H_z=w(1+2w+4w²)/t⁷.

Pro Eulerův operátor D=w∂_w máme

    D(t^(−1))=2w/t³,
    D²(t^(−1))=2w/t³+12w²/t⁵,
    D³(t^(−1))=2w/t³+36w²/t⁵+120w³/t⁷.

Proto

    (7D³+4D²+4D)(t^(−1))/30
       =w/t³+10w²/t⁵+28w³/t⁷
       =w(1+2w+4w²)/t⁷.

Koeficient t^(−1) je choose(2n,n), a D násobí
koeficient w^n číslem n. Dostáváme přesně

    h_n″(1)+h_n′(1)
      =(7n³+4n²+4n)choose(2n,n)/30.

Všechny koeficienty zadání jsou tedy odvozeny,
nikoli kontrolovány jen pro několik malých n.

## P0749: celý rozptyl pro sudé délky a jeho kladná konstanta

Máme h_n(1)=choose(2n,n) a z H_z=w/(1−4w)²
h_n′(1)=n4^(n−1), shodně s již dokázaným A_(2n).
Pro rovnoměrnou2-ordered permutaci2n prvků tedy

    Var W=(7n³+4n²+4n)/30
             −(n4^(n−1)/choose(2n,n))².

Pro n=0 se původní derivace vyhodnotí přímo na0,
bez používání zápisu n4^(n−1). Stirlingův odhad
z P0737 dává pro n→∞

    Var W=(7/30−π/16)n³+O(n²).

Konstanta je přísně kladná, takže skutečně
σ(W)~sqrt(7/30−π/16)n^(3/2). K jejímu znaménku
stačí i hrubý elementární odhad
π/4=∫₀¹dx/(1+x²)<∫₀¹(1−x²+x⁴)dx=13/15,
tedy π/16<13/60<7/30. Nejde o odčítání dvou
vedoucích členů s neověřeným nenulovým rozdílem.

## P0750: proč hlavní tvrzení platí také pro liché délky

Vezmi rovnoměrnou vyváženou cestu s n kroky D,n kroky R
a vlož nový D do rovnoměrně zvolené z2n+1 mezer.
Každá cesta s n+1 kroky D,n kroky R má přesně n+1
vzorů této operace: lze smazat kterýkoli její D,
včetně odlišených pozic ve stejné souvislé sérii.
Výsledná lichá cesta je tedy rovnoměrná.

Nový D má váhu nejvýše n. Každý pozdější původní D
má první souřadnici zvýšenou o1, takže jeho absolutní
váha se změní nejvýše o1. V tomto spojení obou
rozdělení proto |W_odd−W_even|≤2n. Pro směrodatné
odchylky z trojúhelníkové nerovnosti v L² plyne

    |σ(W_odd)−σ(W_even)|≤σ(W_odd−W_even)≤2n.

Rozdíl je nižšího řádu než n^(3/2), takže stejná
vedoucí konstanta platí i pro2n+1 prvků. Ve značení
hlavního textu s celkovou velikostí N je

    σ(W)~sqrt((7/30−π/16)/8) N^(3/2).

Poměr směrodatné odchylky k průměru tak konverguje
ke kladnému sqrt(56/(15π)−1); tím je přesně podložena
poznámka o značném rozptylu vzhledem k průměru.
Žádná neodvozená věta o limitním rozdělení se nepřidává.

## P0751: proč jsou principielně dostupné všechny momenty

Při r-tém z-derivování rovnice pro G se nejvyšší
neznámá G_(z^r)(w,1) objeví dvakrát s faktorem wC.
Ostatní řetězové členy obsahují nižší z-derivace
a jejich w-derivace, již známé indukcí. Koeficient
po přesunu vlevo je opět t s konstantním členem1,
tedy invertibilní formální řada. Tak se určí každá
další derivace G a potom H=(1−J)^(−1).
Obyčejné momenty lze získat přímo aplikací
(z∂_z)^r na H a dosazením z=1. Toto zdůvodňuje
„in principle“ v odpovědi; netvrdí se praktická
levnost velmi vysokého řádu.

## P0752: přesná stromová interpretace a kontrola konvence

Zde jde o **kořenové uspořádané stromy** s n+1 uzly,
tedy n hranami. Jejich konturový průchod dělá R při
přechodu z rodiče do dalšího dítěte a D při návratu.
Vždy j≥i; každý nerootový uzel se vrací právě jednou
a výška j−i před tímto D je přesně jeho hloubka.
Součet svislých vah je proto součtem hloubek všech
uzlů, s nulovým příspěvkem kořene: vnitřní délka cest.

Naopak z nezáporné cesty vytvoříme při R další dítě
aktuálního uzlu a sestoupíme, při D se vrátíme k rodiči.
Nezápornost brání návratu nad kořen a konečný návrat
uzavře všech n hran. To je bijekce zachovávající váhu,
takže skutečně g_n(z)=∑z^(internal path length).

Konvence n+1 uzlů u ordered trees je přímo na
sv.1,389/file404, zobrazené v
`images/insertion-tree-convention-vol1-file404.png`.
Odkazovaná úloha2.3.4.5–5 na405/file420 je také zobrazena
v `images/insertion-tree-reference-vol1-file420.png`:
pojednává o **binárních** stromech a příbuzné délkové
statistice. Nepřebíráme ji jako doslovný důkaz totožnosti
její GF s g_n; tu pro správnou třídu stromů dokazuje
výše uvedený vlastní konturový argument.

## P0753: celý podíl F a doména formálních parametrů

Polož

    F(x,q)=∑_(n≥0) x^n q^(n²)/∏_(k=1)^n(1−q^k).

Odečtení F(qx,q) ruší v n-tém členu právě faktor
1−q^n; přeznačení n=m+1 dává

    F(x,q)−F(qx,q)=xq F(q²x,q).

Pro x=−w,q=z tedy
F(−w,z)=F(−wz,z)−wzF(−wz²,z).
Řada F má konstantní člen1 v w, takže podíl
R(w,z)=F(−wz,z)/F(−w,z) existuje v Q(z)[[w]].
Po vydělení předchozí identity dostaneme

    R=1+wz R(wz,z)R(w,z).

Jednoznačnost P0742 proto dokazuje R=G.
Samotné jednotlivé koeficienty F mají při z=1 póly;
**nedosazuje se z=1 do čitatele a jmenovatele zvlášť**.
Podíl se nejprve chápe koeficientově v uvedeném tělese
a identita s G zaručí, že výsledné koeficienty jsou
polynomy v z a mají regularizované dosazení1.

## P0754: úplná partiční interpretace koeficientů F

Pro n kladných částí p₁,…,p_n s p_j≥p_(j+1)+2
odečti minimální liché schodiště

    u_j=p_j−(2(n−j)+1).

Pak u₁≥…≥u_n≥0 a ∑p_j=n²+∑u_j. Obrácené
přičtení schodiště zachovává obě požadované nerovnosti
i kladnost poslední části; obě mapy jsou inverzní.
Polož v_j=u_j−u_(j+1)≥0 s u_(n+1)=0. Platí
∑u_j=∑jv_j, a nezávislé v_j proto dávají
∏_(j=1)^n(1−q^j)^(−1). Přidání q^(n²) a označení
počtu částí x^n je přesně n-tý člen F. Pro n=0 je
jediná prázdná partition a prázdný součin1.

Tím jsou dokázány i oba dodatky odpovědi621, nejen
požadovaný rozptyl. Celá úloha15 je uzavřená včetně
všech rekurencí, meziderivací, předpokladů a hranic.
Další kurzor je TheoremH na88/file99; již hotové
2-ordered důkazy se znovu nepřepočítávají.

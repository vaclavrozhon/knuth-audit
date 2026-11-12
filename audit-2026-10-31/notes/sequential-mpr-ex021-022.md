# D123–D124 — celé MPR21–22

6. listopadu 2026. Celé zadání p14/file34 a odpovědi p373/file393
byly zobrazeny přímo, stejně jako Pre-Fascicle5A p14/file20 a
p30/file36. Vydaná odpověď21 už obsahuje známou opravu E121.
Následující důkazy se vztahují ke skutečnému znění svazku4B.
Žádný numerický běh ani nový nález.

## D123: nejmenší počty hodnot a tištěný příklad

Je-li některá náhodná proměnná konstantní skoro jistě, je s každou
druhou nezávislá: společná událost má buď nulovou pravděpodobnost,
nebo pravděpodobnost události pro druhou proměnnou. Závislý příklad
tedy potřebuje nejméně dvě hodnoty každé proměnné s kladnou hmotností.

Mají-li obě přesně dvě takové hodnoty, lze je psát

    X=x₀+(x₁−x₀)U,       Y=y₀+(y₁−y₀)V,

kde U,V jsou binární a x₀≠x₁, y₀≠y₁. Označme p=EU, q=EV,
r=E(UV)=P(U=V=1). Přímým rozvojem středních hodnot dostaneme

    covar(X,Y)=(x₁−x₀)(y₁−y₀)(r−pq).

Oba koeficienty jsou nenulové. Nulová kovariance tedy vynutí r=pq.
Zbytek společné tabulky je pak

    P(1,1)=pq,                 P(1,0)=p−pq=p(1−q),
    P(0,1)=q−pq=(1−p)q,        P(0,0)=1−p−q+pq=(1−p)(1−q).

To je úplná nezávislost, včetně případných degenerovaných p,q.
Jde právě o důsledek předchozí MPR20, ale s explicitním rozvojem
pro dvojici a s doložením, že argument platí pro libovolné dvě
reálné hodnoty, nejen pro hodnoty0 a1. Pro závislý nekorelovaný
příklad je tedy nejmenší možná dvojice počtů hodnot (2,3), až
na prohození X a Y.

V knize má (X,Y) právě pět stejně pravděpodobných hodnot

    (0,0), (0,2), (1,0), (1,1), (1,2).

Jejich pravděpodobnosti1/5 jsou nezáporné a dávají celkem1.
Marginály jsou

    P(X=0)=2/5,       P(X=1)=3/5,
    P(Y=0)=2/5,       P(Y=1)=1/5,       P(Y=2)=2/5.

Proto EX=3/5, EY=(0+2+0+1+2)/5=1 a
E(XY)=(0+0+0+1+2)/5=3/5. Kovariance je přesně0.
Současně P(X=0,Y=1)=0, zatímco
P(X=0)P(Y=1)=2/25>0. Tento chybějící společný atom je důvodem
poslední vytištěné nerovnosti a dokazuje závislost. Všechny
tištěné zlomky a všech pět bodů tím byly ověřeny.

Minimalita, kterou odpověď odůvodňuje svou první větou o nemožnosti
dvou binárních proměnných, se týká počtů hodnot jednotlivých
proměnných. Kniha výslovně netvrdí minimalitu pěti společných atomů.
Tato dvě měřítka není vhodné zaměňovat. Pro úplnost lze přesně vyřešit
i druhé přirozené měřítko: na třech stejně pravděpodobných bodech

    (X,Y)=(0,0), (0,2), (1,1)

platí EX=1/3, EY=1, E(XY)=1/3, ale P(X=1,Y=0)=0≠1/9.
Má tedy rovněž nejmenší počty hodnot(2,3) a jen tři společné atomy.
Na nejvýše dvou atomech je buď některá proměnná konstantní, nebo
obě nabývají pouze dvou hodnot; předchozí důkaz pak vylučuje
požadovanou závislost s nulovou kovariancí. Tři atomy jsou tedy
minimum pro toto alternativní měřítko. Vyřešená kontextová
odlišnost sama není kandidátem na tiskovou chybu.

## E121: zveřejněná oprava starší odpovědi21

Fascicle5 p185, řádky3–4 odpovědi21, má veřejnou opravu z11. července2022:
pravděpodobnost1/5, EXY=EX=3/5, EY=1 a součin marginál2/25.
Vše bylo přečteno ve zdrojovém TeXu `err4f5.textxt`, řádky735–739,
a přímo zobrazeno v `images/sequential/all4f5-09.png`.
Náš svazek4B p373 má toto správné znění již zapracované.
E121 je jen evidence známého errata; žádná karta ani barevná lokace.

Pre-Fascicle5A z11. září2019 má jinou předběžnou šestibodovou
parametrickou odpověď. Není zaměněna za znění vydaného svazku ani
za přesnou předchozí sazbu vydaného Fascicle5. K ověření aktuálního
pětibodového důkazu není její neplatný obecný výpočet potřeba a
nevytváří se z něj nový nález v4B. Pro transparentnost: jeho šest
vah je (a,b,3a+b+3d,d,1,1), součet D=4a+2b+4d+2; správné
EX=(d+2)/D, a nikoli obecně2/D, zatímco EXY=3/D a EY=3/2.
Nulová kovariance by vyžadovala d=0. Jde o starší nahrazenou verzi,
nikoli o chybu přítomnou v současné kontrolované odpovědi.

## D124: celá sjednocovací nerovnost a každý tištěný krok

Pro konečný počet n≥1 událostí označme I_j=[A_j] a
I=[A₁∪⋯∪A_n]. Bodově I=1 právě tehdy, když aspoň jeden I_j=1;
proto I=max(I₁,…,I_n). Jelikož všechny I_j jsou nezáporné,

    max(I₁,…,I_n)≤I₁+⋯+I_n.

Všechny proměnné jsou omezené, jejich očekávání existují.
Rovnost E[A]=P(A) je přímo součet0·P(Ā)+1·P(A), tedy
ověřená rovnice(8). Monotónnost očekávání a konečná linearita,
doložené v D093, proto dávají přesně řádek odpovědi:

    P(A₁∪⋯∪A_n)=EI
      =E max(I₁,…,I_n)
      ≤E(I₁+⋯+I_n)
      =EI₁+⋯+EI_n
      =P(A₁)+⋯+P(A_n).

Nikde není třeba nezávislost ani disjunktnost. Případy prázdných
či jistých událostí jsou zahrnuty bodovou nerovností; n=1 je
rovnost. Kdyby se připustilo n=0, přímo máme P(∅)=0 a prázdný
součet0, bez zavádění nedefinovaného maxima prázdné rodiny.

Rozdíl je nezáporná proměnná ∑I_j−I, která je nulová právě tehdy,
když nastane nejvýše jedna událost. Rovnost v pravděpodobnostní
mezi nastává právě při této vlastnosti skoro jistě, ekvivalentně
při P(A_i∩A_j)=0 pro všechny i≠j. Tento okraj také potvrzuje,
že překryvy nemění směr vytištěného znaménka.

## Rozsah a evidence

Obě celé úlohy21–22 mají úplný argument včetně odpovědí a okrajů.
Šest vrstev errat a tři TeX zdroje prohledány podle stran, čísel
a pojmů; jediná relevantní změna je známá E121. Všechny ostatní
shody patří sousední24 nebo jiným oddílům.
`results/sequential/mpr-021-022-errata.json` uchovává konkrétní kontext.
Žádné bibliografické výjimky pro tyto dvě úlohy. File34 a393
zůstávají partial kvůli dalším přesně vyjmenovaným obsahům.

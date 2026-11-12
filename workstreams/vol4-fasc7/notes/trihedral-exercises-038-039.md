# Úlohy38(a–f),39(a–b): determinanty, oktanty a úhly

Zadání p116/file131 a odpovědi p166–167/file181–182 byly přečteny
v originální sazbě. Zohledněny jsou známé opravy22.9.2026 (ε vůči
neincidentním stěnám),22.10.2026 (binární zápis oktantu) a13.9.2026
(celá odpověď39b). Bibliografická změna stran149–176 místo85–120
z8.3.2026 je zaznamenána, historické práce se podrobně neověřují.
Opravy nejsou našimi nálezy. Žádný numerický běh není pro tento blok
potřeba; následuje úplný obecný argument každého tištěného kroku.

## T38-a — nezávislost, znaménko a objem

Položme u_i=v_i−v_0. Dvě sousední hrany v jedné stěně nejsou kolineární:
jinak by v_0 nebyl jejím rohem, ale vnitřním bodem úsečky. Kdyby všechny
tři u_i ležely v jedné rovině, každá z incidentních stěn by ležela právě
v této rovině, protože obsahuje dvě nezávislé u_i. Tím by se sousední
stěny staly koplanárními a nebyly by odděleny hranou. Proto jsou tři
u_i lineárně nezávislé.

Odečtením prvního řádku determinantu od ostatních a rozvojem podle
posledního sloupce dostáváme

D(v_0,v_1,v_2,v_3)=−det(u_1,u_2,u_3)≠0.

Záměna v_2,v_3 obrátí znaménko. Přesně tři sudé permutace mají kladné
D a jsou navzájem cyklickými posuny; to dokazuje jedinečnost cyklického
pořadí v odpovědi, nikoli jedinečnost lineárního vyjmenování. Objem
tetraedru je |D|/6: lineární mapa s maticí[u_1,u_2,u_3] násobí objem
absolutním determinantem a simplex a,b,c≥0,a+b+c≤1 má objem
∫₀¹∫₀^(1−a)∫₀^(1−a−b) dc db da=1/6. Tím je doložen i pomocný
objemový fakt v bibliografické závorce bez závislosti na jejím původu.

## T38-bc — rovina a správná polorovina

F(v)=D(v_0,v_1,v_2,v) je nenulová afinní lineární funkce, nulová
právě na afinním obalu v_0,v_1,v_2. Má tedy za nulovou množinu p12.
Na každé ze dvou otevřených polorovin má stálé opačné znaménko.
Po volbě pořadí z části(a) je F(v_3)>0, takže požadovaná strana je
přesně F(v)>0. Body roviny mají F=0 a nejsou v žádné otevřené straně.

## T38-d — osm oktantů a obecně použitelný výpočet

Každý bod se jednoznačně píše v=v_0+α_1u_1+α_2u_2+α_3u_3.
Roviny p23,p31,p12 jsou postupně α_1=0,α_2=0,α_3=0. Lineární
izomorfismus z α-prostoru převádí osm otevřených standardních
ortantů na osm neprázdných otevřených oblastí. Například body
v_0±u_1±u_2±u_3 přímo svědčí jejich neprázdnosti. Body na rovinách
se do otevřených oktantů nečíslují.

Označme o_i=[α_i<0]. Protože v_i má α_i=1, je to právě test
opačné strany od v_i. Číslo je4o_1+2o_2+o_3, tedy (o_1o_2o_3)_2
a následně jediná oktalová číslice0..7. Původní index8 byl již opraven.
Koeficienty α lze spočítat Cramerovým pravidlem, případně testovat
znaménko součinu dvou determinantů. Ten druhý postup funguje i při
D<0; není třeba měnit explicitní souřadnice z částí(e),(f).

## T38-ef — oba konkrétní body

Při standardních jednotkových v_i jsou α=(x,y,z), takže kladný bod
(π,φ,γ) leží v oktantu0. Toto konkrétní pořadí má D=−1, ale geometrické
číslování z(d) je nezávislé na předchozí orientační volbě. Není správné
do(e) mechanicky vložit test F>0 z(c) bez jeho předpokladu D>0.

Pro v_1=(1,1,0), v_2=(0,1,1), v_3=(1,0,1) dostáváme

α_1=(x+y−z)/2, α_2=(y+z−x)/2, α_3=(x+z−y)/2.

Platí π>3,1<φ<2,0<γ<1. První nerovnost dává vepsaný pravidelný
šestiúhelník do jednotkové kružnice; druhou vzorec φ=(1+√5)/2.
Pro γ lze použít H_n−log n: rozdíly mezi součtem a integrálem ukazují
kladnou limitu; už první interval dává dolní mez1−log2>0 a
H_2−log2<1, neboť log2>1/2, dává ostrou horní mez. Tudíž
π>φ+γ, π+φ>γ a π+γ>φ. Znaménka α jsou +,−,+, binární zápis010
a výsledek2. Všechny tři koeficienty jsou nenulové. Toto pořadí má
D=−2 a platí stejné rozlišení jako v(e).

## T39-0 — proč opravené ε opravdu izoluje roh

Je jen konečně mnoho kompaktních stěn. Každá neincidentní stěna má
od v_0 kladnou vzdálenost; zvolené ε je menší než všechny. Uvnitř
koule tedy neexistuje jiná plocha hranice než tři incidentní roviny.
Konec některé incidentní hrany by přitom musel mít třetí, neincidentní
stěnu: stejné tři nezávislé roviny se nemohou protnout ještě v jiném
vrcholu. Žádný takový konec tedy v kouli není. Místní hranice sestává
ze tří paprsků +u_i a tří rovinných sektorů mezi nimi. Každý sektor je
buď menší nežπ, nebo reflexní, větší nežπ. Úhelπ je vyloučen
nezávislostí hran. Uvnitř každého otevřeného oktantu koule je členství
v tělese stálé, protože oblast je souvislá a nenarazí na hranici.

Původní vzdálenost pouze k ostatním vrcholům tuto izolaci nezajišťovala:
cizí plocha může procházet blízko, i když její vrcholy jsou daleko.
Použit je přesně opravený předpoklad, nikoli neprokázaná původní verze.

## T39-a — úplný rozklad a kritérium3,5,6

Dvě z místních stěn nemohou mít současně reflexní sektor. Jejich
roviny sdílejí jednu incidentní hranu, řekněme +u_1; oba reflexní
sektory by obsahovaly i záporný paprsek −u_1 ve svých relativních
vnitřcích. Dvě stěny by se tam nepřípustně protínaly vnitřkem. Jsou
tedy jen čtyři možnosti: žádný reflexní sektor nebo právě jeden
v p23,p31,p12.

Přes kteroukoli rovinu se členství v tělese změní právě tam, kde je
skutečná stěna. V rovině p23 je to buď kladný sektor α_2,α_3>0,
nebo jeho reflexní doplněk; analogicky pro další dvě roviny. Tyto
přechody určují obsazení všech osmi oktantů až na globální doplněk,
protože graf sousedství oktantů je souvislá krychle. Následující
tabulka má přesně požadované přechody na každé z jejích12 hran:

|Reflexní stěna|Jedna z možných obsazených množin|Druhá možnost|
|---|---|---|
|žádná|{0}|doplněk{0}|
|p23|{1,2,3}|doplněk{1,2,3}|
|p31|{1,4,5}|doplněk{1,4,5}|
|p12|{2,4,6}|doplněk{2,4,6}|

Například u{1,2,3} se přes p23 mění obsazení právě při
(o_2,o_3)≠(0,0), tedy v reflexním sektoru, a přes p31,p12 právě
v kladných sektorech. Ostatní řádky jsou permutace souřadnic nebo
globální doplněk. Tím jsou doloženy všechny případy, nikoli jen příklad.

V kolmém řezu blízko kladného paprsku u_1 jsou dvě stěny dva paprsky.
Pro první řádek tabulky je vnitřní malý sektor buď jediná čtvrtina,
nebo jeho tříčtvrtinový doplněk. V dalších řádcích se může obrátit
jeden z obou paprsků, protože právě jedna incidentní stěna je reflexní.
V každém řádku je hrana1 konkávní právě tehdy, když je obsazen oktant3:
v {1,2,3} ano a v jejím doplňku ne; u {1,4,5},{2,4,6} ne a v
jejich doplňcích ano; u{0} ne a v doplňku ano. Řez ukazuje totéž
přímo jako velký, respektive malý materiálový sektor. Záměnou
souřadnic dostáváme pro hrany2,3 oktanty5,6. To dokazuje celé39(a).

## T39-b — každý faktor a volba úhlu v opravené odpovědi

Opět u_i=v_i−v_0. Pro hranu1 definujme n12=u_1×u_2 a
n13=u_1×u_3. Oba normálové vektory jsou nenulové a neparalelní.
Kolmé průměty u_2,u_3 do roviny u_1^⊥ označme p_2,p_3.
Operace u_1×p je rotace v této rovině o90° a násobení |u_1|,
tedy zachovává úhel i poměr skalárního součinu k délkám.

Skutečný vnitřní směr incidentní stěny v řezu u kladné hrany je p_i,
má-li daná stěna u v_0 menší úhel, a −p_i, má-li reflexní úhel.
Proto je kosinus menšího úhlu β mezi skutečnými paprsky roven

cosβ = (−1)^(r12+r13) (n12·n13)/(|n12||n13|),  0<β<π.

Nejvýše jeden z r12,r13 je1 podle T39-a. Znaménko je tedy záporné
právě tehdy, když **jeden nebo druhý** z uvedených rovinných vnitřních
úhlů přesahuje180°, přesně jak říká erratum. Není nutno přidávat
neřešený případ dvou reflexních stěn: v3VP nemůže nastat.

Autorovo θ je **vnější** dihedrální úhel. Je θ=β při konkávní hraně
a θ=2π−β při konvexní. Obě volby mají stejný kosinus, takže
n12·n13=±|n12||n13|cosθ; znaménko je právě výše odvozené a volba
intervalu0<θ<π čiπ<θ<2π jej jednoznačně určuje. Materiálový vnitřní
úhel je2π−θ. Takto se také vyjasní zdánlivě obrácené intervaly v
tištěné odpovědi. Překlad do v_0=0, který erratum výslovně předpokládá,
je obsažen v definici u_i. Celá opravená formule, včetně znaménka,
obou délek a obou intervalů, je tedy uzavřena.

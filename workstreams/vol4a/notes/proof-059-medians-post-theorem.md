# Mediány, Theorem P a přesné náklady konstrukce

Checkpoint X0088, P0821–P0831. Celý text p63–64/file80–81
přečten z originálu sources/proof-median-pages063-064.pdf,
images/proof-median-1/2.png. Žádný matematický program.
Dřívější P0812 dokazuje obě booleovské formy(43), P0607–P0611
monotónnost a prime formy; tento přesný rozsah se neopakuje.
Značíme M(x,y,z)=⟨xyz⟩.

## Prostřední hodnota, reálná čísla a hranice — P0821

Pro x≤y≤z jsou tři párová minima x,y,x; jejich maximum je y.
Tři párová maxima jsou y,z,z; jejich minimum je rovněž y.
Obě formy(43) proto dávají(44). Jsou symetrické v argumentech,
takže výsledek je prostřední hodnota při libovolném pořadí,
včetně shodných hodnot. Platí na libovolné úplně uspořádané
množině; nevyžaduje sčítání, hustotu ani archimédovskou vlastnost.

V booleovském řetězci to dává M(000)=M(001)=0 a
M(011)=M(111)=1, a symetrie pokrývá všechna zbývající pořadí.
V rozšířených reálných číslech jsou přípustné i ±∞: pouze
operace min/max jsou použity, takže nevznikají neurčité součty.

## Obě konstantní specializace a monotónní funkce — P0822

Při prostředním argumentu0 dává(43) M(x,0,y)=xy;
při prostředním argumentu1 dává M(x,1,y)=x∨y. Nahrazením
každého AND/OR v monotónní formuli podle(45) vznikne formule
z mediánů a konstant0/1. P0608 už dokázala, že každá nekonstantní
monotónní funkce má takovou AND/OR formuli; obě konstantní
funkce vyjádří příslušný konstantní list. Obráceně medián
a konstanty zachovávají monotónnost při skládání.

Pro libovolný řetězec s dolním a horním prvkem ⊥,⊤ platí
M(x,⊥,y)=min(x,y), M(x,⊤,y)=max(x,y). V reálném rozšíření
jsou to přesně −∞,+∞. Přeznačení těchto konstant symboly∧,∨
a jejich posunutí dopředu v polském zápisu nemění funkci,
protože M je symetrický; nejde o nový algebraický předpoklad.

## Selfdualita, výměna operací a minimum arity — P0823

Definice(46) je ¬f(x)=f(¬x), kde se komplementují všechny
souřadnice. U formule F z proměnných a∧,∨ bez konstant
strukturní indukce z De Morganových zákonů dává

    F^d(x)=¬F(¬x),

kde F^d zamění∧ a∨ na všech uzlech. Proto F je selfduální
právě tehdy, když F^d představuje tutéž funkci. Pokud používáme
rozšířený jazyk s konstantami, dualizace musí také prohodit0 a1;
obě konstantní funkce samy nejsou selfduální. U nekonstantních
monotónních funkcí je k dispozici bezkonstantní formule podle
P0608, což je rozsah použitého odstavce.

M je monotónní podle(43) a selfduální, protože komplement
obrátí počet jedniček ze s na3−s, takže většina se obrátí.
U binární monotónní selfduální funkce musí být f(00)=0,
f(11)=1 a hodnoty f(01),f(10) se doplňují. Dvě možnosti
jsou přesně levá a pravá projekce. Pro unary aritu je jediná
monotónní selfduální funkce x; nulární taková funkce neexistuje.
M přitom závisí podstatně na každé ze tří souřadnic: při
zbylých hodnotách0,1 se rovná třetímu argumentu. Tím je
nejnižší netriviální arita3 skutečně doložena.

## Uzavřenost skládání a celý tištěný příklad — P0824

Projekce jsou monotónní a selfduální. Jsou-li g1,g2,g3 selfduální,

    M(g1(¬x),g2(¬x),g3(¬x))
      =M(¬g1(x),¬g2(x),¬g3(x))=¬M(g1(x),g2(x),g3(x)).

Monotónnost se také zachová po souřadnicích. Indukce přes strom
formule proto dokazuje tvrzení pro libovolný bezkonstantní
mediánový výraz, i když se některé proměnné mnohokrát opakují.

Vytištěný příklad je F=M(w,M(x,y,z),M(w,M(u,v,w),x)).
Označíme-li A=M(x,y,z), B=M(u,v,w), C=M(w,B,x), jeho
jednotlivé kroky jsou

    ¬F=M(¬w,¬A,¬C),
    ¬A=M(¬x,¬y,¬z),
    ¬C=M(¬w,¬B,¬x),
    ¬B=M(¬u,¬v,¬w).

Po dosazení je výsledkem přesně původní výraz s komplementem
každého výskytu všech u,v,w,x,y,z. To kontroluje i opakované w
 a negace ve všech třech vytištěných rovnostech.

## Opakovaný medián(47) — P0825

Definujme h_1(x1;y)=x1 a pro s≥2

    h_s(x1,…,xs;y)=M(x1,y,h_{s−1}(x2,…,xs;y)).

Chceme dokázat h_s=(U_s∧y)∨P_s, kde U_s=∨x_i a P_s=∧x_i.
Pro s=1 pravá strana absorpcí dává x1. Pro indukční krok
položme U'=∨_{i≥2}x_i, P'=∧_{i≥2}x_i a H=U'y∨P'. Potom

    M(x1,y,H)=x1y∨yH∨x1H
      =x1y∨U'y∨P'y∨x1U'y∨x1P'
      =(x1∨U')y∨x1P'.

Použito P'≤U' pro neprázdnou zbývající rodinu a absorpce
x1U'y≤x1y. To je přesně požadovaný tvar. Vytištěná vnoření
obsahují s−1 mediánů a s−1 výskytů prostředního y pro s≥2;
s=1 je přirozená nulová základna. Prázdný seznam se nepoužije.

## Průnik prime implikantů a singletonová větev — P0826

Monotónní selfduální f není konstantní, takže f(0)=0 a f(1)=1.
Její prime DNF podle P0601/P0609–P0611 má alespoň jeden
neprázdný kladný term; žádný term se nevyskytuje uvnitř jiného.

Kdyby dva termy měly disjunktní množiny proměnných A,B,
zvolme x s jedničkami právě na A. Pak první term dává f(x)=1,
ale komplement x má jedničky na všech B a dává f(¬x)=1,
spor se selfdualitou. To platí pro libovolné velikosti i další
nepoužité proměnné, nejen pro vytištěný příklad dvou a tří literálů.

Je-li některý prime term pouze proměnná x_i, každý další by
kvůli průniku musel obsahovat x_i. To odporuje prime antichainu;
žádný další term tedy není a f=x_i=M(x_i,x_i,x_i). Tím je
samostatná singletonová větev úplná. V netriviální větvi mají
všechny velikosti s_j≥2. Pro n=0 je Theorem P prázdné tvrzení,
protože nulární selfduální funkce neexistuje.

## Konstrukce(48): invariant všech dosud zahrnutých termů — P0827

Při g0=x1 a g_j=h_{s_j}(proměnné t_j;g_{j−1}) plyne z(47)

    g_j=(U_j∧g_{j−1})∨t_j.

Současný term t_j proto vždy implikuje g_j. Jestliže k<j,
indukce dává t_k≤g_{j−1}; společná proměnná t_k a t_j dává
t_k≤U_j. Tedy také t_k≤U_j∧g_{j−1}≤g_j. To dokazuje
invariant t1∨…∨t_j≤g_j a tím f≤g_m. Žádný obecný vztah
 g_{j−1}≤g_j se netvrdí a pro důkaz není potřebný.

Každé g_j je konečná bezkonstantní mediánová formule, protože
začíná projekcí a konstrukce používá jen konečně mnoho vnoření.
P0824 dává její monotónnost i selfdualitu. Volba x1 v g0 nemusí
patřit prvnímu ani všem prime termům; invariant se o to neopírá.

## Proč dominance selfduálních funkcí znamená rovnost — P0828

Pro n≥1 jsou vstupy v disjunktních dvojicích x,¬x. Každá
selfduální funkce má právě jednu jedničku v každé dvojici,
tedy přesně2^{n−1} jedniček. Pokud f≤g_m, jejich stejně velké
množiny jedniček musejí být totožné. Tím je Theorem P dokázána.

Stejný závěr lze číst bodově: f(x)=0,g_m(x)=1 by selfdualitou
dalo f(¬x)=1,g_m(¬x)=0, spor s dominancí. Zde není potřeba
další externí klasifikační věta ani předpoklad o pořadí termů.

## Lichá většina a všech deset prime termů pro pět bitů — P0829

Pro2k−1 bitů je většina1 právě při alespoň k jedničkách.
Je monotónní. Komplement přepne počet s na2k−1−s;
podmínka s≥k se tím změní na s≤k−1, takže je selfduální.
Theorem P se použije pro všechna k≥1, včetně jediné proměnné.

Pro pět proměnných každý kladný trojliterálový term implikuje
většinu. Žádný term se dvěma literály ji neimplikuje, protože
při ostatních nulách má funkce hodnotu0. Všechny větší termy
obsahují některý trojterm, takže nejsou prime. Úplná prime DNF
má proto právě C(5,3)=10 termů:

    vwx, vwy, vwz, vxy, vxz, vyz, wxy, wxz, wyz, xyz.

To je přesně celý vytištěný seznam a jeho úplnost má obecný
argument; neplyne jen z kontroly jednotlivých kladných bodů.

## Přesně2046 operací v rozbalené formuli — P0830

V tomto příkladu má každý t_j velikost3. V h_3=M(x1,y,M(x2,y,x3))
jsou dva mediány a dvě kopie y. Při měření počtu výskytů mediánů
ve **formuli jako stromu**, nikoli ve sdíleném výpočetním grafu,
proto platí T0=0, T_j=2T_{j−1}+2. Indukce dává

    T_j=2^{j+1}−2, tedy T_10=2048−2=2046.

Při uložení a dvojím použití už spočteného g_{j−1} by vznikl
jiný objekt, řetězec s20 mediánovými kroky. To nezpochybňuje
uvedenou délku rozbalené formule; book právě nazývá g10 formulí.
Nepředstíráme, že2046 je optimální, ani z tohoto příkladu
neodvozujeme polynomiální velikost obecné formule z Theorem P.

## Celá identita(49) a přenos na libovolný řetězec — P0831

Původní sazba začíná **v**, nikoli OCR písmenem y:

    median5(v,w,x,y,z)=M(v,M(x,y,z),M(w,x,M(w,y,z))).

Pravá strana má čtyři mediánové uzly. Pro booleovské y,z
stačí následující vyčerpávající rozklad:

* y=z=0: M(x,y,z)=0, M(w,y,z)=0, M(w,x,0)=wx.
  Celá pravá strana je vwx, právě podmínka tří jedniček mezi pěti.
* y=z=1: vnitřní dvě hodnoty jsou1, M(w,x,1)=w∨x.
  Výsledek je v∨w∨x, právě podmínka alespoň jedné další jedničky.
* y≠z: M(x,y,z)=x, M(w,y,z)=w a M(w,x,w)=w.
  Výsledek M(v,x,w) vyžaduje dvě jedničky mezi zbývajícími třemi,
  neboť y,z už obsahují právě jednu jedničku.

Všechny možné v,w,x jsou v těchto rovnostech ponechány volné.
Tím je identita dokázána bez výčtu32 případů. Porovnání4<2046
ji prokazuje jako kratší vyjádření; tvrzení o absolutním optimu
v tomto odstavci není a neověřuje se zde.

Platnost platí i pro libovolnou úplně uspořádanou množinu.
Pro každý prahový prvek a zobrazení H_a(x)=[x≥a] zachovává
min,max a tedy M. Také H_a prostřední z pěti hodnot je většina
pěti H_a-bitů. Dvě strany proto mají stejné všechny prahové
indikátory podle booleovského důkazu. Kdyby jejich hodnoty byly
r<s, práh a=s je odliší; tudíž jsou stejné. Tento argument
pokrývá shody i ±∞ bez předpokladu existence mezilehlého čísla.

## Stránková mapa, meze bibliografie a pokračování

**p63/file80** má nyní argument ke všemu matematickému:
majority/reálné pořadí P0821, specializace a úplnost s konstantami
P0822, selfdualita a binární klasifikace P0823, obecné skládání
a všechny kroky příkladu P0824, Theorem P P0825–P0828.
Úvodní „probably most important“ je autorovo hodnocení, nikoli
samostatná matematická mez. Historický vznik v Postově disertaci
1920 nebyl nezávisle doložen a zůstává bibliografickou výjimkou.

**p64/file81**: každá rovnost a krok důkazu P0825–P0828,
všechna tvrzení o liché většině a celý seznam P0829, přesný
náklad a neoptimalita dané formule P0830/P0831, celá kratší
identita i závěrečný přechod k uspořádaným množinám P0831.
Přesné strany Post1941,74–75 a Miiller/Winder1962,89–90 se
nově bibliograficky neověřovaly; matematika je zde odvozena.

Známá změna F0 na p63 upravuje jen formulaci „if we wanted to“;
vrstvy all4a-pre/all4a/err4a/all4f0/err4f0 neobsahují další
relevantní matematickou změnu tohoto p63–64 bloku. Žádný nový
nález ani změna dřívějších karet. Obě stránky mohou dostat
review_depth: argument, s uvedenými bibliografickými výjimkami.

Dále hlavní text p65/file82, median algebras/graphs. Sekvenční
úloha56 zůstává další; herní i jiné dřívější mezery se tím
neuzavírají. Čtenářský kurzor p218/file235 se nemění.

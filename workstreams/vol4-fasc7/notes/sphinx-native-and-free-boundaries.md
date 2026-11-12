# Nativní sfinga a všechny čtyři volné obvody

Rozsah: Fig.101(a), 104(a), poslední věta p13 a první tři odstavce
p14 (file24,26,28,29). Zde se ověřuje rovinná kresba a její CSP.
Dosud neuzavřená prostorová realizace sfingy ani opačný pohled103(a)
se tím nepovyšují. Původní stránky a dva velké výřezy tváře byly
zobrazeny. Známé errata p9–14 nepřidávají opravu těchto počtů;
oprava textu o projekci na p10 je již samostatně zaznamenána.

## SP-1 — úplná rovinná síť, bez předpokladu veřejného3D modelu

`check_sphinx_native_network.py` začíná přesným seznamem68 vrcholů
a102 hran původního drátového102(a), již uzavřeným v G-1. Souřadnice
veřejného3D modelu se nepoužívají. V původním104(a) se projdou
všechny path18–191:56 černých obrysů/bílých výplní a všechny barevné
značky. Každý bod obrysů je jednoznačně přiřazen původnímu vrcholu.
Tři nekolineární kotvy26,61,34 určují afinní mapu s kladným
determinantem. Největší kvadrát bodové odchylky je
`323605940998138159564929537721/8581691805966424191027200000000000`,
tedy méně než0.000038 bodu². Jde o obvyklé zaokrouhlení sazby,
nikoli ztotožnění odlišných čtyř vrcholů veřejného modelu.

Pro každý černý tah se zjistí všechny průsečíky s pozdějšími
bílými výplněmi. Mezi po sobě jdoucími průsečíky se příslušnost
do těchto polygonů nemění; winding test středního bodu proto
rozhodne celý otevřený interval. Zůstávají právě úseky, které
žádná pozdější výplň nezakryje. Tato konečná indukce podle pořadí
kreslení je přesný argument pro výsledný rovinný obraz. Není to
prostorový ray test. Každý přeživší úsek leží na právě jedné
původní hraně; všechny další průsečíky se rozštěpí a kolineární
vrcholy stupně2 odstraní. Každý zbylý vrchol má stupeň2 nebo3,
žádné nepovolené křížení či překrytí nezůstane.

Výsledkem je68 junctions a97 čar:10V,27W,21Y,10T. Každé místní
pořadí je určeno přesnými determinanty podle již uzavřených
definic. T má protilehlé bary a správnou stranu stonku; W má
prostřední paprsek mezi krajními; Y má všechny tři cyklické mezery
menší nežπ. Výsledné relace jsou přesnými řádky Tabulky1 převedenými
na globální orientaci jednotlivých proměnných.

Celý geometrický blok je uložen v `results/sphinx-native-geometry.json`.
Po jeho dokončení se při zkoumání značek znovu nepočítal.

## SP-2 — všechny značky a výslovně uvedené chybějící značky

Každá červená tříbodová značka je šipka; dvě její ramena určují
střední směr od středu pat k hrotu. Červená dvoubodová značka je
kolmý tick a bílá dvoubodová značka podélná mezera konkávní čáry.
Pozdější bílé výplně se aplikují i na oba segmenty každé značky.
Přežije115 značek; path39,43,44 jsou celé zakryty. Všechny viditelné
značky mají jednoznačné přiřazení podle vzdálenosti od čáry,
směru a překrytí s jejím viditelným intervalem. Opakované značky
téže čáry dávají stejný štítek.

Dvě důležité kreslicí situace nejsou přeskočeny:

- Path24 má zakrytý střed bílé mezery, ale viditelný konec.
  Path31 má zakrytý hrot šipky, ale viditelnou část ramene.
  Rozhoduje přeživší segment a překryv původní značky s čárou,
  nikoli podmínka, že její střed musí být viditelný.
- Path58 překračuje T spoj. Její viditelný hrot určuje jeden
  úsek; příslušná T relace určí stejný směr druhého baru.
  Jedna značka se nevydává za dva nezávislé důkazy.

Čtrnáct velmi krátkých úseků nemá vlastní přeživší značku.
Jejich přesný seznam je v `results/sphinx-native-network.json`;
devět z nich leží na obvodu. Po propagaci všech zobrazených
značek zůstávají neurčené pouze

`j45_j63 ∈ {−,>}` a `j49_j52 ∈ {+,−,<,>}`.

Oba jsou na obvodu. Standardní doplnění předepíše jejich šipky
po směru hodinových ručiček. Potom jsou všechny proměnné určeny
jednoznačně a každá ze68 úplných místních relací je splněna.
Všechny přímo zobrazené obvodové značky také míří po směru
obvodu. Přesný ověřený výrok je tedy: **zobrazené značky104(a)
mají jediné standardní doplnění**. Není tvrzeno, že každý krátký
úsek má v originálu vlastní viditelnou šipku, ani že tato čistě
rovinná zkouška dokazuje prostorovou správnost každého štítku.

Obvodový průchod má34 různých junctions. Jeho určení používá
již uzavřený stěnový průchod B-1; součet orientovaných ploch
odliší vnější průchod od všech vnitřních. Výsledek včetně všech
značek, původních indexů, chybějících značek a propagace je
uložen ve dvou souborech `sphinx-native-network.json` a
`sphinx-native-mark-analysis.json`.

## SP-3 — neoznačený originál101(a) je skutečně tentýž obrázek

`check_sphinx_repeated_view.py` páruje všech56 původních path28–83
ve file24 s právě doloženými56 obrysy/výplněmi104(a). Každý pár
má stejnou barvu, stejný počet a pořadí vrcholů; zachováno je
i celé pořadí překrývání. Jediná kladně orientovaná afinní mapa
souhlasí se všemi body, s maximální odchylkou² menší než0.000031
bodu². Afinní mapy zachovávají incidenci, pořadí průsečíků,
vnitřek polygonu a orientaci. Proto jsou odpovídající viditelné
sítě totožné. Nejde jen o podobnost dvou rasterových siluet.
Výsledek: `results/sphinx-repeated-view.json`.

## FB-1 — úplný konečný počet obvodových označení

Ve všech čtyřech obrázcích je obvod jednoduchý cyklus
`v_0,…,v_(r−1)`. Označme jeho hranu `v_i v_(i+1)` jako b_i,
všude ve stejné globální orientaci, a ostatní proměnné jako
vnitřní. Každý obvodový junction obsahuje právě b_(i−1),b_i
a případně jedinou vnitřní čáru c_i. Tabulka1 poskytne lokální
relaci R_i. Její projekce na dvě obvodové proměnné je matice
M_i velikosti4×4 s prvky0,1 v pořadí `+,−,<,>`.

Každé obvodové označení určuje právě jeden uzavřený průchod
stavy těchto matic, začínající hodnotou b_(r−1). Naopak každý
takový průchod dává právě jedno označení všech b_i. Proto je
počet přesně `trace(M_0 M_1 … M_(r−1))`. Indukce podle počtu
matic dokazuje i význam každého prvku mezisoučinu: je to počet
částečných cest mezi příslušnými krajními hodnotami. Nejde
o náhodný vzorek ani o předpoklad nezávislosti junctions.

`check_hc_free_boundaries.py` ukládá každou M_i, všechny prefixové
součiny a výslednou stopu. Dostáváme postupně720,3,6,4.
Rozdílné orientace globálních proměnných jsou převzaty přímo
z příslušných úplných relací, nikoli z neorientovaných obrázků.

## FB-2 — faktorizace je silnější než shoda výsledného součinu

Samotný počet řešení by volnost obvodu nedokázal. Pro každou
lokální dvojici(a,b) se proto samostatně ověří, zda může ležet
na uzavřené cestě: přesně tehdy, když `M_i[a,b]=1` a součin
všech ostatních matic má prvek(b,a)>0. To je úplná podmínka,
protože spojuje místní krok s cestou kolem zbytku cyklu.

Pro všechny takto globálně možné dvojice se projdou všechny
odpovídající plné řádky R_i. **Každá vnitřní čára incidentní
obvodu má ve všech těchto řádcích stejný štítek.** Pokud čára
spojuje dva obvodové junctions, oba požadavky souhlasí.
Celý vektor těchto pevných štítků je uložen jako
`fixed_interior_ports`; není odhadnut pouze z jedné realizace.

Z toho plynou obě inkluze pro přesný kartézský součin:

1. Každé úplné řešení dává přípustné obvodové označení a vnitřní
   řešení se stanovenými pevnými štítky.
2. Libovolné přípustné obvodové označení lze spojit s libovolným
   takovým vnitřním řešením. V obvodových junctions je správný
   plný řádek díky pevnému vektoru; zbývající junctions se
   dotýkají pouze vnitřních proměnných a zůstávají splněny.

Standardní obvodové šipky jsou také jednotlivě ověřeny jako
přípustné. Proto je množina vnitřních řešení přesně stejná
pro standardní obvod i pro všechny ostatní přípustné obvody.
To uzavírá celý tištěný argument o zaměnitelnosti, nejen čtyři
číselné součiny. Počet označení splňujících pouze obvodové
junctions je zde míněn na proměnných, kterých se tyto junctions
dotýkají; zcela vnitřní proměnné do tohoto mezipočtu nevstupují.

## FB-3 — každý zbylý vnitřní faktor

Szilassiho počet2 se přebírá z úplného tříuzlového certifikátu45
(`results/szilassi-standard-labelings.json`) a histoscape1
z ruční úplné klasifikace(22): ze čtyř tamních řešení je právě
jedno standardní. Nová faktorizace FB-2 přesně ospravedlňuje
převzetí těchto počtů jako vnitřních faktorů. Staré výpočty se
znovu nespouštěly.

Pro sfingu a clasp se řeší jen vnitřní relace s pevnými štítky
z FB-2. Propagace odstraňuje právě hodnoty bez podporujícího
řádku. Takové odstranění neztrácí řešení; každý průchod zmenší
konečnou doménu, takže skončí. Při rozdělení podle jedné
proměnné jsou větve disjunktní a pokryjí všechny zbývající
možnosti. Úplné větvení sfingy má pouze3 uzly a2 listy.

U claspu stačí jediný propagační uzel. Po omezení domén má
každá zbývající relace tolik různých řádků, kolik prvků má
kartézský součin jejích domén; řádky jsou jeho podmnožinou,
takže se mu rovnají. Zbývající proměnné jsou tedy skutečně
nezávislé. Jsou to

- `j09_j17`, `j12_j19`, `j23_j24`, každá s doménou{+,−,<,>};
- `j05_j25`, `j13_j14`, každá s doménou{+,>}.

První tři čáry jsou přímo ověřené stonky mezi dvěma T junctions;
obě T relace stanoví pouze své bary a dovolují každou hodnotu
stonku. Poslední dvě čáry spojují T stonek s V a mají právě
uvedené dvě možnosti. Ostatní vnitřní čáry jsou pevné. Proto
je počet přesně `4³·2²=256`, bez enumerace256 celých řešení.

Standardní počty jsou tudíž(2,2,256,1) a celkové počty
`(720·2,3·2,6·256,4·1)=(1440,6,1536,4)`.
Pevná chyba C0006 v jednom fyzickém štítku claspu nemění
jeho síť ani tyto abstraktní počty; fyzika a CSP se nezaměňují.

## SP-4 — přesně dvě změny u sfingy

Ze dvou vnitřních řešení je první přesně standardní doplnění
104(a). Druhé mění pouze

`j37_j39: −→>` a `j37_j40: −→<`.

Jsou to původní hrany38–41 a38–54 u spodku hlavy. Jejich
společný junction má souřadnice přibližně(167.065,109.467);
druhé konce jsou(157.946,107.318) a(187.923,105.955).
Obě concave značky tedy nahradí půlhrany ukazující odlišnými
globálními směry; viditelná plocha hlavy zůstává po jejich
pravé straně. To přesně ověřuje tištěné dvě změny a jejich
lokální význam: tyto styky již nemusí znamenat společnou
konkávní hranu hlavy s tělem, nýbrž zakrytí. Netvrdí se zde
nová kompletní prostorová realizace oddělené hlavy.

## Meze tohoto bloku

Všechny konečné certifikáty jsou v `results/hc-free-boundaries.json`.
Nový početní běh trval méně než0.01s s nice15; geometrie nebyla
opakována. Teze „exceptions seem rare in practice“ nemá určený
soubor dat ani statistický význam a zůstává partial. Definice
volného obvodu je uzavřena výše; úlohy49–56, nemožné obrázky24–27
a další obecná tvrzení p14 budou ověřeny samostatně. Žádná nová
karta chyby z těchto správných počtů nevzniká.

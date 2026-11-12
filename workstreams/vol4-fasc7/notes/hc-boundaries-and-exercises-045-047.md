# Obvodový průchod a úlohy45–47

Rozsah: poslední odstavec p13/file28, tvrzení o dvou standardních
označeních Szilassiho obrázku na p14/file29, zadání p117/file132
a odpovědi p168/file183. Původní sazba byla zobrazena. Geometrie
101/104(b–d), všechna její viditelná rozhraní a jejich značky se
přebírají z přesně vymezených již uzavřených poznámek, nikoli
z tvrzení o standardnosti nebo počtu řešení.

## B-1 — jednoznačnost boundary cycle a opakované hrany

Zde „cycle“ označuje orientovaný uzavřený obvodový průchod, ne nutně
jednoduchou kružnici. Odpověď52 na p170/file185 výslovně připouští
opakovanou čáru. Její počet označení se tímto odkazem neověřuje.

Pro pevný konečný souvislý rovinný obrázek zvolme malý pravidelný
okolní pás kolem všech hran a malé disky kolem vrcholů. Šířka může
být kladná a dostatečně malá, protože neincidentní konečné úsečky
a vrcholy mají kladnou vzdálenost. Toto okolí má právě jednu
vnější hraniční složku. Důkaz lze vést od vnořeného kostrového
stromu: přidáním listové větve se k disku přilepí tenký obdélník
a koncový disk, takže hranice zůstane jediná. Každá zbývající
hrana je jednoduchý oblouk v jedné stávající stěně; rozdělí tuto
stěnu na dvě. Je-li rozdělena vnější stěna, právě jedna nová část
je neomezená; jinak se vnější hranice vůbec nezmění. Tím současně
vzniká elementární důkaz Eulerova vztahu F=E−V+2.

Stažení vnějšího pásu na graf dává právě jeden obvodový průchod,
až na volbu počátku. Při směru s obrázkem vpravo je orientován
po směru hodinových ručiček. Most se projde jednou v každém směru;
některé vrcholy se mohou opakovat. To není protipříklad k větě
p13. Rozhodující je pevný obrázek, tedy rovinné vložení; samotná
abstraktní síť může mít různá vložení a různé vnější obvody.

Čistě kombinatorická konstrukce užívá oba směry každé hrany.
Po příchodu u→v pokračuj po první větvi následující za v→u
v cyklickém pořadí po směru hodinových ručiček. Tato permutace
orientovaných hran rozděluje všechny hrany na stěnové průchody.
Vnější z nich má v PDF souřadnicích kladnou orientovanou plochu;
ostatní mají zápornou. V našich neprázdných HC obrázcích existuje
kružnice, protože každý vrchol má stupeň≥2, takže vnější plocha
není nulová.

## B-2 — přesný obvod(20) a význam standardnosti

Dosazením všech původních bodů a všech26 uzavřených hran(20)
do předchozí permutace vyjde, po pojmenování podle N20-4,
právě `(a b e f q s r o m c)`. Tím je kontrolován celý tištěný
příklad v posledním odstavci p13.

Na skutečném vnějším okraji konečného neprůhledného tělesa je na
jedné straně viditelný povrch a na druhé pozadí. Jeho značka je
proto polohrana; definice šipky klade povrch napravo, takže
šipka sleduje právě orientaci vnějšího obvodu. Tento argument
je již uzavřen jako G-8. Standardní označení abstraktního obrázku
vyžaduje stejný směr na každém výskytu obvodové čáry. Má-li
obvod most, jsou opačné požadavky neslučitelné a obrázek nemá
standardní označení. Definice standardnosti existenci neslibuje.
Neomezená podlaha nebo stěna naopak mění někdejší obrys na
vnitřní konkávní hranu, jak přesně ukázal L22-4; to vysvětluje
výklad o nepřipojeném objektu uvnitř obvodu.

## B-3 — původní standardní označení104(b–d)

`check_hc_picture_networks.py` z již uzavřených viditelných intervalů
odvodí každou čáru, její oba junctions, jejich skutečné úhlové typy
a všechna uspořádání větví. Každé V/W/T má jediné vhodné pořadí,
u Y je začátek zvolen nejmenším názvem. Podle Tabulky1 se pak
ověří každá lokální relace, nikoli pouze obvod.

Pro každý z obrázků104(b–d) vychází jediný vnější stěnový průchod.
Každá jeho fyzická hrana má v originálu přeživší značku a všechny
jsou polohrany ve správném směru. Výsledky jsou úplně uloženy
v `results/hc-picture-networks.json`:

- histoscape:19 junctions,26 čar,10 obvodových úseků;
- clasp:27 junctions,37 čar,8 obvodových úseků;
- Szilassi:15 junctions,20 čar,8 obvodových úseků.

U clasp a Szilassi jsou některé velmi krátké vnitřní úseky bez
přeživší značky; pro úplnou lokální kontrolu se používá výslovně
uvedené doplnění z již ověřené fyzické geometrie. Žádný takový
úsek neleží na obvodu. Chybná fyzická značka F7-C0006 u clasp
byla převzata tak, jak je skutečně vytištěna: kupodivu stále
vyhovuje abstraktní lokální relaci svého V a volnému stonku T.
Proto její fyzická nesprávnost nevyvrací standardnost označení.

Tento blok uzavírá standardnost b,c,d. Obvod a každé označení
sfingy104(a) dosud nejsou uzavřeny; obecná věta se nesmí použít
k automatickému schválení její konkrétní sazby. Proto celá
poslední věta p13 a celá stránka zůstávají přesně vymezené partial.

## E45-1 — jiné standardní označení a přesně dvě možnosti

V `results/hc-picture-networks.json` má Szilassi dvě Y, označené
j04 a j06. j06 je vnitřní Y u otvoru. Jeho tři čáry vedou k j04,
j09 a j10. Původní prostřední vnitřní čára j04–j06 je−; zbývající
dvě jsou polohrany, jedna ven a druhá dovnitř. Změň právě tyto
dvě polohrany na−. U j06 vznikne povolený řádek `---`, u j04
se nic nezmění. j09 a j10 jsou T, pro které změněné čáry jsou
právě volné stonky. Všechny ostatní lokální relace zůstanou stejné.
Žádná změněná čára neleží na vnějším obvodu, proto je nové označení
standardní a různé od původního. To je úplné konstruktivní řešení45.

Po vnucení osmi obvodových polohran propagace všech15 relací
vynutí18 z20 čar. Zbývají pouze dvě právě uvedené čáry, s možnostmi
`(j06–j09,j06–j10)=(>,<)` nebo `(−,−)`. Relace j06 je spojuje;
obě volby vyhovují i oběma T. Žádná jiná volba není možná.
`check_szilassi_labelings.py` obsahuje celý tříuzlový certifikát
této propagace a obou listů v `results/szilassi-standard-labelings.json`.
Tím je uzavřeno také přesné tvrzení o dvou standardních označeních
na p14; nejde o předpoklad převzatý z odpovědi45.

## E45-2 — omezená nejasnost slova „lower“

Tištěná odpověď45 říká „lower Y“. Přímé původní rovinné souřadnice,
kde y roste dolů, jsou pro j04 přibližně(314.480469,114.472656)
a pro správné vnitřní j06 přibližně(306.705636,113.501953).
j04 je tedy na stránce o necelý bod níže, ale jeho změna na`---`
poruší dvě sousední W a změní dvě obvodové polohrany. Úplné oba
testy jsou v citovaném výsledku a originál ve výřezu
`images/file-026-szilassi-labels.png`.

Matematické řešení a počet jsou uzavřeny; vizuální referent slova
„lower“ zůstává interpretační partial bez nové karty. Tvrzení,
že dvě nové konkávní hrany už lokálně neohraničují pozadí otvoru,
plyne z jejich definice. Samostatná prostorová realizace změněného
objektu není tímto lokálním označením dokázána a není zde přidána.

## E46 — odraz, všechny typy a všechny vypsané množiny

Zrcadlení obrátí orientaci roviny, a tedy pořadí větví. Při
pevných názvech jsou T(l,m,r),V(l,r),W(l,m,r),Y(a,b,c) převedeny
na T(r,m,l),V(r,l),W(r,m,l),Y(c,b,a). Sousednost ani názvy čar
se nemění. Vypuklost/konkávnost se odrazem nemění. Šipka však
musí obrátit směr, aby viditelná plocha opět ležela napravo.
Proto hodnotová involuce R fixuje+ a− a vyměňuje<,>.

Je třeba ověřit i abstraktní sítě, kde fyzický argument nelze
použít. V lokální notaci O/I z L22-1 odraz obrací pořadí symbolů
a pak vyměňuje O,I. Na indexech řádků Tabulky1 působí přesně

```
T: 1→1, 2→2, 3↔4
V: 1↔3, 2→2, 4↔6, 5→5
W: každý ze tří řádků zůstává sám sebou
Y: 1↔3, 2→2, 4→4, 5→5.
```

Každá celá lokální relace se tedy přenese bijektivně. Na pevné
globální orientaci čáry se stejná operace projeví právě R, takže
každé řešení H dává jedno řešení H^R a druhý odraz vrací původní.
To platí pro libovolnou abstraktní síť, i prázdnou a nerealizovatelnou.

V uvedeném příkladu má odražené a=V(c,b) na(ac,ab) řádky
`<+,<>,+>,>-,><,-<`. Přehodíme-li souřadnice, dostaneme
`+<,><,>+,->,<>,<-`, přesně druhou tištěnou množinu.
Přerovnáním prvků je to `>+,><,+<,<-,<>,->`, přesně R obrazu
původní množiny pro(ab,ac). Každý ze tří vypsaných mezikroků
tedy souhlasí. Bibliografický odkaz na Gardnerovu knihu zde
není potřebný a nebyl samostatně prověřen.

## E47-0 — definice realizovatelnosti a zákaz vnějšího T

HC síť má různé vrcholy a různé sousedy na svých větvích; jde
o tentýž běžný jednoduchý grafový předpoklad jako v N20 a E42.
Realizace znamená vložit tento graf přímými neprotínajícími se
úsečkami, s předepsanými úhlovými typy a pořadím, a bez T, jehož
obě kolineární větve jsou vnějšími obvodovými čarami. Systém
lokálních labelů je definován i bez takového vložení.

U skutečné obecné projekce je T překrytím vzdálenějšího stonku
bližším obrysem. Na zakryté straně obrysu musí být stonek neviditelný,
tedy jeho viditelná část vstupuje na opačnou stranu. Kdyby obě
obrysové větve tvořily právě vnější hranici celého obrázku, stonek
na této opačné straně by sám vstoupil do vnější oblasti a hranice
by jej musela obejít. Obě kolineární větve by tedy v tomto
místě netvořily přímý vnější obvod. Opačné umístění stonku by
zase bylo zakryté. To odůvodňuje vysvětlení v závorce zadání.

## E47(a) — nejmenší příklad

Síť a=V(b,c),b=V(c,a),c=V(b,a) má tři vrcholy. V jakémkoli
nekolineárním trojúhelníku mají determinanty větví v pořadích
(b−a,c−a), (c−b,a−b), (a−c,b−c) stejné nenulové znaménko.
První dvě požadovaná V vynutí jeho kladnost, třetí však obrací
poslední dvojici a vyžaduje zápornost. Realizace tedy neexistuje.
Kolineární umístění neposkytne V. S méně než třemi vrcholy není
žádná neprázdná jednoduchá HC síť, protože každý junction
potřebuje alespoň dva různé sousedy. Příklad je tedy nejmenší.

## E47(b) — všechny cykly V včetně konstrukčního kroku

Realizovatelnost lze rozhodovat po komponentách: restrikce
realizace dává každou komponentu a naopak konečně mnoho realizací
lze zmenšit a umístit do disjunktních disků. Prázdná síť je
triviální. Každá neprázdná komponenta jen s V je konečný jednoduchý
2-regulární graf, tedy cyklus délky p≥3. Očíslujme jeho vrcholy
cyklicky. Pak j_k=V(j_(k+σ_k),j_(k−σ_k)), σ_k∈{+1,−1}.

V realizaci orientované po směru hodinových ručiček odpovídá
σ=+1 přísně konvexnímu rohu a σ=−1 reflexnímu. Každý jednoduchý
nekolidující polygon má alespoň tři přísně konvexní rohy: vyberme
jeho konvexní obal; nejméně tři jeho skutečné extrémní vrcholy
mají všechny ostatní vrcholy v sektoru<π. Po případném globálním
odrazu E46 jsou tedy alespoň tři σ kladné.

Nutná podmínka je i postačující, a je třeba doložit tištěné
„perturbing them slightly“. Tři zvolené kladné vrcholy položme
do vrcholů trojúhelníku v cyklickém pořadí. Na jedné jeho straně
u→v má být k−1 mezivrcholů. Položme je do bodů
`p_i=u+(i/k)(v−u)+ε h_i n`, i=0…k, kde n je normála vpravo
od strany a h_0=h_k=0. Předepsaná znaménka vnitřních rohů s_i
dosáhneme řešením
`h_(i+1)−2h_i+h_(i−1)=s_i`, například

```
h_i = iA + Σ_(r=1)^(i−1) (i−r)s_r,
A = −(1/k) Σ_(r=1)^(k−1) (k−r)s_r.
```

Determinant dvou po sobě jdoucích hran má znaménko právě s_i
pro ε>0. Rovnoměrně rostoucí projekce na směr u→v zaručuje,
že se tato lomená čára neprotne sama. Na všech třech stranách
zvolme společné dostatečně malé ε: vzdálené části různých stran
zůstanou disjunktní, u tří kotev zůstanou jejich původní přísně
konvexní rohy a pořadí větví. Tím se realizuje každá posloupnost
s alespoň třemi plussy. Je-li takových alespoň tři minusy,
zkonstruujeme odraženou síť a odrazíme ji zpět.

Pro p=3 musí být všechny σ stejné. Pro p=4 musí být alespoň
tři stejné, jak správně uvádí erratum; pouhé zakázání střídání
by nestačilo. Pro p>4 má každá binární posloupnost alespoň tři
stejná znaménka. To uzavírá všechny případy i celou tištěnou
trojúhelníkovou konstrukci, nikoli pouze její náčrt.

## E47(c) — celý důkaz neplanárnosti uvedené sítě

Síť a=b=c=W(d,e,f),d=e=f=W(a,b,c) má právě všech devět hran
mezi dvěma trojicemi, tedy K_(3,3). Má V=6,E=9, žádný most
a žádný lichý cyklus. Kdyby měla rovinné vložení, Eulerův vztah
z B-1 by dával F=5. Každá stěna by měla délku alespoň4, takže
2E≥4F, tj.18≥20, spor. Jakékoli další úhlové podmínky W mohou
realizaci pouze ztížit; už samotný graf tedy nevyhovuje.

## E47(d) — nejméně tři V/W a tištěný úhlový mezikrok

Krátký obecný důkaz pracuje s konvexním obalem celé neprázdné
komponenty. Body nemohou být všechny kolineární, protože každý
typ HC obsahuje nekolineární větve. Obal má nejméně tři extrémní
vrcholy s přísně konvexním úhlem. Všechny incidentní větve tam
leží v sektoru<π, což dovoluje pouze V nebo W, nikoli T či Y.
Jde o tři různé junctions; mosty ani opakované obvodové vrcholy
tento argument neovlivňují.

Také tištěný pomocný úhlový argument je správný. Pro jednoduchý
polygon s m rohy je součet úhlů(m−2)π. Úplný elementární důkaz
triangulace: z přísně konvexního rohu v s předchůdcem u a
následníkem w uvažujme trojúhelník uvw. Neobsahuje-li jiný
vrchol, uw je vnitřní diagonála. Obsahuje-li jiný vrchol,
vezměme r nejblíže v ve směru normály k uw. Otevřený vrcholový
trojúhelníkový výřez nad rovnoběžkou přes r neobsahuje vrcholy.
Hrana křížící vr nemůže křížit uv ani vw a nemůže dvakrát
křížit přímku základny, proto by měla konec v tomto prázdném
výřezu. Taková hrana neexistuje a vr je vnitřní diagonála.
Rozštěpením na dva menší polygony a indukcí dostaneme m−2
trojúhelníků; jejich úhly dávají uvedený součet. Případ vrcholů
na základně se zahrne volbou nejvyššího r v uzavřeném trojúhelníku;
úsečka vr nemůže obsahovat další vrchol blíže v.

U obecného vnějšího průchodu, kde se vrcholy či mosty opakují,
platí tentýž vztah při počítání jednotlivých výskytů. Lze to
odvodit na malém okolním pásu z B-1 nebo rozkladem v artikulacích
bloků a mostů, které se dotýkají vnější stěny. Blok vložený do
vnitřní stěny se do vnějšího průchodu nezapočte. Jednotlivé
blokové obvody jsou jednoduché cykly; most je obvod
délky2 se dvěma nulovými koncovými úhly. Při slepení dvou blokových
obvodů v artikulaci se počet výskytů sečte a součet nových dvou
vnitřních úhlů převýší původní dva o2π. Vztah(m−2)π se proto
zachová indukcí po stromu bloků. Bikonexní blok nemůže mít
opakovaný obvodový vrchol: dvě oddělené vnější úhlové mezery u
takového vrcholu by rozdělily sousedy na části bez cesty mimo něj,
jinak by uzavřená rovinná křivka oddělila obě mezery od vnější
stěny. Takový vrchol by byl artikulací.

V konečném HC obvodu mají všechny jednotlivé úhly hodnoty
striktně mezi0 a2π. Proto nanejvýš m−3 z nich může být>π;
m−2 takových by již překročilo celý součet. Úhel=π by vyžadoval
právě zakázané obě kolineární vnější větve T. Zbývají tedy
nejméně tři konvexní výskyty, a ty mohou být pouze V/W.
U jednoho junctionu může být nejvýše jeden: mezi jeho různými
paprsky může být nejvýše jedna vnější mezera>π. I tento delší
tištěný způsob tedy dává tři různé junctions, nikoli pouze tři
výskyty téhož vrcholu.

## E47(e) — obecná perturbace i tehdy, když sousedé jsou T

Pouhé posunutí jediného bodu může porušit kolinearitu u sousedního
T. Proto je třeba krátkou tištěnou radu doložit společnou
perturbací, která zachová všechny zbývající přesné rovnosti.

V původní realizaci má každý T vrchol i mezi svými dvěma
kolineárními sousedy a_i,c_i. Existuje tedy pevné λ_i∈(0,1),
pro něž `p_i=λ_i p_(a_i)+(1−λ_i)p_(c_i)`. Vybraný vrchol j
prohlásíme za volný kotevní bod; všechny vrcholy jiných typů
(V/W/Y) ponecháme také jako kotvy. U ostatních T
zachováme právě tyto původní kladné barycentrické rovnice.

Tyto rovnice mají jediné řešení závislé lineárně na kotvách.
Důkaz: neexistuje neprázdná množina T uzavřená vůči oběma svým
barovým sousedům. Generická lineární funkce by na takové konečné
množině měla jediný maximalizující bod, ale ten by byl kladným
průměrem dvou přísně menších hodnot. Spor. Ze všech T tedy vede
cesta po kladných váhách do kotev. Pro nezápornou matici P vah
mezi zbývajícími T existují N a η>0 tak, že každému řádku P^N
chybí alespoňη do součtu1. Proto P^(kN)→0 geometricky a
`(I−P)^(-1)=I+P+P²+…` existuje s nezápornými prvky.
To dokazuje jednoznačnost i spojitost bez předpokladu
neregulárnosti nějakého náhodně vybraného systému.

Posuňme pouze kotvu j o δ. Každý jiný vrchol i se posune
o h_iδ, kde h_i≥0 je jeho harmonická váha této kotvy; ostatní
kotvy mají h=0. Všechny kotevní váhy se sčítají na1, protože
konstantní funkce1 vyhovuje stejným rovnicím. Pro i≠j navíc
h_i<1: při h_i=1 by i závisel pouze na jediné kotvě j, a už
v původních souřadnicích by platilo p_i=p_j, což odporuje
různým vrcholům realizace.

Položme původně `p_a−p_j=−αu`, `p_c−p_j=βu`, α,β>0,
a `w=p_b−p_j` pro stonek. Zvolme δ=εw. Po posunu jsou
barové paprsky
`−αu−(1−h_a)εw` a `βu−(1−h_c)εw`, zatímco stonek je
kladným násobkem w pro dostatečně malé |ε|. Determinant
dvou barových paprsků je

`ε[α(1−h_c)+β(1−h_a)] det(u,w)`.

Koeficient v hranaté závorce je přísně kladný, tedy ohyb opravdu
nastane na libovolně zvolené straně. V kanonické poloze T s a
vlevo, c vpravo a b dole dá ε>0 právě Y(c,b,a) a ε<0 právě
W(c,b,a). Ostatní T zůstávají přesně mezi svými barovými sousedy;
ostatní úhlové typy a pořadí jsou přísné nerovnosti a zachovají
se při dostatečně malém posunu. Neincidentní úsečky mají kladné
odstupy, takže nevzniknou nové průniky. Cyklické pořadí větví
se nezmění, tedy ani vnější stěnový průchod; u zbývajících T
nevznikne zakázaná dvojice vnějších barů. To je úplný důkaz
obou opravených variant pro každou realizovatelnou síť.

## E47(e), dodatek errat — obrácená pořadí nejsou obecně možná

Je třeba doložit také dodatek „but not W(a,b,c) or Y(a,b,c)“
ve smyslu absence obecné záruky. Konkrétní původní realizace je

```
a=(-1,0), b=(0,1), c=(1,0), d=(0,-1), j=(0,0);
a=W(d,j,b), b=W(a,j,c), c=W(b,j,d), d=V(c,a), j=T(a,b,c).
```

Je to vnější kosočtverec a–d–c–b a tři neprotínající se čáry
z j do a,b,c. Všechny úhlové determinanty mají požadovaná
znaménka; j je vnitřní. Jeho náhrada W(a,b,c) nebo Y(a,b,c)
obrátí jedině cyklické pořadí u j, ostatní zůstanou pevná.
Permutace orientovaných hran má pak přesně dva stěnové průchody:

```
ab, bj, jc, cd, da, aj, jb, bc, cj, ja;
ad, dc, cb, ba.
```

Síť má5 vrcholů a7 hran, takže každé rovinné vložení musí
mít4 stěny podle B-1. Dvě stěny dávají Eulerovu hodnotu0,
nikoli2; požadované pořadí tudíž nemá žádné rovinné vložení,
ani při jiné poloze bodů. Všechny původní průniky a oba nové
stěnové průchody jsou přesně uloženy v
`results/realizability47-wrong-order.json`; kontrola pěti pevných
bodů proběhla nice15. Obě zakázané varianty mají stejné obrácené
cyklické pořadí, takže je týž příklad vyvrací současně.

## Errata a meze uzavření

Přímý TeX i obě veřejné textové vrstvy byly porovnány. Použity
jsou všechny relevantní známé opravy: p117,22.10.2026,
Y(a,b,c)→Y(c,b,a); p168,13.9.2026, alespoň tři shodná znaménka
pro p=4; p168,23.10.2026, dodatek o obou nesprávných pořadích.
Žádná z nich není nový nález. E46 a všechny části E47 jsou
doloženy včetně pomocných konstrukcí a obou dodatků. U45 je
samotné řešení i počet úplný, ale slovní „lower“ zůstává partial.
U48 se existence obecného rozhodovacího postupu a jeho přesná
složitost posuzují odděleně; tato poznámka je ještě neuzavírá.

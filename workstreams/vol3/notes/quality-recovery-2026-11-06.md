# Obnova důkladnosti svazku 3

Pravidla: AGENTS.md, QUALITY_RECOVERY.md a QUALITY_EXAMPLES.md z 6. listopadu.
Vlastněná cesta je pouze workstreams/vol3. Bez nového výpočtového běhu.
Čtenářský kurzor139/file150 není důkazový kurzor; ten zůstává u začátku
Tableaux47/file58. Dřívější explicitní mezery se tímto zápisem neruší.

## Nové odvození tří uzavřených položek

Nejprve byly znovu přečteny původní strany6/9 a odpovědi585/590–591
(file17/20 a596/601/602), včetně obrazů posledních tří stran. Níže uvedené
argumenty byly odvozeny před otevřením obou uložených chapter5-proof poznámek.
Nejde o statistický certifikát kvality ostatních tvrzení.

### §5-22: úplný invariant volného stromu, V3-P0052

Pro zakořeněný konečný strom definuj kód vrcholu jako závorky kolem
lexikograficky seřazených kódů jeho dětských podstromů. List má kód `()`.
Vyvážené závorky určují hranice jednotlivých dětských kódů jednoznačně.
Indukce podle počtu vrcholů proto dokazuje obě implikace: zakořeněný
izomorfismus zachová multiset kódů dětí; rovnost kódů naopak dovolí spárovat
děti se stejnými kódy a jejich induktivně získané izomorfismy spojit.
Pouhé shodné stupně takový závěr nedávají, úplný závorkový kód ano.

Pro nezakořeněný strom vezmi lexikografické minimum těchto kódů přes všechny
volby kořene. Izomorfismus permutuje možné kořeny, takže minimum zachová.
Rovnost minim vybere dvojici kořenů se shodným kódem a indukce dá
izomorfismus původních stromů. Jediný vrchol i dvouvrcholový strom jsou
zahrnuty; prázdnému stromu lze, pokud jej připustíme, přidělit zvláštní
prázdný kód. Pro orientované hrany stačí v dětském kódu zachovat i směr
hrany k rodiči. Kniha v této větě neslibuje čas konkrétní implementace.

Srovnání: původní notes/chapter5-proof-10-25.md používá místo minima přes
kořeny společné odstraňování listů. To je také platné: strom s alespoň3
vrcholy má neprázdnou souvislou množinu nelistů (cesta mezi dvěma nelisty
obsahuje jen nelisty); velikost se zmenšuje. Proces tedy skončí v1 nebo2
spojených vrcholech a je izomorfně invariantní. Jeho závorková indukce má
stejný rozsah jako nové odvození. Uzavření P0052 ponecháno, bez potřeby
přebírat neověřený časový výsledek citovaného článku.

### §5-24: rekonstrukce seznamu, V3-P0056–57

Předpoklady: vstup je právě cesta přes N různých jmen, nikoli obecný graf;
N=3000000. Pro krok t má F dvojice `(x_i,x_(i+t))`, i≤N−t, a G označený
suffix `(i,x_i)`, i>N−t. Kopie H má stejné dvojice jako F. Klíče prvních
složek H a druhých složek G jsou disjunktní a pokrývají všechna jména.
Každá druhá složka x′ z F proto musí mít právě jeden protějšek:

- v H dostaneme `(x_i,x_(i+2t))`, právě pro i≤N−2t;
- v G se známou pozicí y=i+t dostaneme `(y−t,x_i)=(i,x_i)`.

Řazení F podle druhé, H podle první a G podle druhé složky dovolí tyto
shody najít pouze dopřednými ukazateli. Přeskočený menší klíč už neodpoví
nynějšímu ani pozdějšímu klíči F. Vyčerpaný soubor má sentinel+∞.
Nové označené prvky jsou bez opakování a neleží ve starém G. Jejich
sloučení s G dá suffix délky min(2t,N), zatímco F′ obsahuje zbývající
dvojice s odstupem2t. To dokazuje celý invariant i ukončení při t≥N.

Počáteční zvláštní krok použije dvě seřazené kopie hran. Jejich spojení
podle prostředního jména vytváří odstup2; jediná druhá složka bez
protějšku v prvních složkách je x_N. Příslušná hrana určí x_(N−1),
takže první dvě pozice v G jsou známy. Konec není odhadován z pořadí jmen.
Čárky x′ v testech(ii)–(iv) jsou v původní sazbě skutečně přítomny.

Nová samostatná konzervativní mez: vytvářej v RAM běhy po16 záznamech
a slučuj trojcestně na šesti páskových jednotkách. Po prvním průchodu
je nejvýše187500 běhů, méně než3^12; libovolné třídění nejvýše N záznamů
tedy stojí nejvýše13 synchronních průchodů. Takto malý buffer dovoluje
i víceslovná jména: např.16 dvouklíčových záznamů a šest bufferů po
jednom záznamu při nejvýše64 slovech na klíč spotřebují2816 slov plus
malou řídicí režii. Uložené ostatní soubory během třídění nepotřebují
aktivní páskovou jednotku; při joinu jsou tři vstupy a dva výstupy.

Každému zdvojení přidělme tři třídění, jednu kopii, jeden join a jedno
sloučení, tedy nejvýše42 průchodů, i když první krok tolik nepotřebuje.
Zdvojení je22, protože2^21<N<2^22. Závěrečné třídění G přidá13:
`22·42+13=937<1000`. Průchod počítá synchronní přečtení/zapsání dat,
nikoli zvlášť každý běh každé jednotlivé pásky. Není to čas v sekundách
ani mez nezávislá na neomezené délce reprezentace jmen.

Srovnání: původní důkaz používá1000 dvouslovných záznamů, dvoucestné
slučování a přesnější účtování prvního kroku. Jeho
`28+21·42+13=923` je správné v jím výslovně uvedeném klíčovém modelu.
Původní invariant také přesně pokrývá všechny větve i EOF. P0056–57
zůstávají checked v tomto rozsahu; obecné O(log²N) nenahrazuje číselnou mez.

### §5-8 Solution1: minimum bez skoků, V3-P0021

Nechť radix bytu je β,64≤β≤100, W=β^5−1. Nemusí být sudý.
Použita přesná sémantika MIX z1.3.1: ADD/SUB s nulovým výsledkem
ponechávají znaménko rA; posuny nemění znaménka; DIV zaokrouhluje
k nule a zbytek má znaménko dělence (svazek1 s.125,131–132,135).

Prvních deset instrukcí získá a=2u+r, b=2v+s, |r|,|s|≤1, se znaménky
zbytků odpovídajícími vstupům. Rozdíl d=u−v má |d|≤2floor(W/2)≤W.
Potom R=r−s má velikost≤2. SRAX1 jeho velikost v rA změní na0, ale
znaménko ponechá; ADD d dá znaménko a−b. Pro d≠0 je shoda znamének
důsledkem monotonicity celočíselného podílu; pro d=0 rozhoduje R.
ENTX1;SLAX5 tedy vytvoří σ=±1 se správným znaménkem. Při a=b je
R=0, takže libovolné znaménko nuly neovlivní další výsledek.

MUL R;STX AB3 uloží σR. Další blok má hodnotu
`r+s−σ(r−s)`: je2s, pokud a>b, a2r, pokud a<b; při rovnosti jsou
r=s. Dělení2 tedy dá z odpovídající vybranému zbytku. Závěr je
`u+v+z−|u−v|`, což je podle znaménka d a v případě d=0 podle R
přesně menší vstup. Field(1:5) při posledním SUB opravdu vynechává znaménko.

Ani mezivýsledek nepřeteče. Součty zbytků a výsledek jejich bloku mají
velikost≤2. |z+u|≤floor(W/2)+1≤W. Pro |u+v+z| lze použít
|u|+|r|≤ceil(W/2), pokud z=r, a analogicky pro z=s; druhý podíl má
velikost≤floor(W/2). Součet je tedy≤W i pro lichý radix. Poslední
odečtení je již prokázaný platný vstup a nebo b. Násobení má velikost≤2;
před každým DIV je horní rA nulové, což vylučuje přetečení podílu.
Program neobsahuje skok ani závislost správnosti na testu overflow.

Srovnání: uložený důkaz v notes/chapter5-proof-01-09.md má tytéž nutné
předpoklady i samostatnou mez pro libovolný radix. Nový rozbor nezjistil
nepodložené uzavření. P0021 zůstává checked. Známý komentářový dodatek
2019 k SRAX/SLAX je zohledněn; nejde o nový nález.

## Porovnání úplnosti inventáře do47

Nově byl porovnán souvislý text1–47, odpovědi584–607 a relevantní změny
dosavadních errata reviews s položkami P0001–0375. Inventář není pouhý
výběr úloh: zachycuje25 úvodních,29 inverzních,24 multisetových a29
aktualizovaných úloh Runs, jejich části, tabulky a tvrzení odpovědí.
Začátek Tableaux v dolní části47 do dokončeného bloku nepatří.

Přesto dřívější formulace o všech tvrzeních byla příliš silná:

1. Pomocná Eulerova rekurence v historické poznámce odpovědi Inversions14
   (594/file605) neměla samostatný argument. Není to jen bibliografický
   údaj. Její odvození a odkaz na již dokázanou pentagonální identitu
   jsou doplněny jako samostatná položka P0377.
2. Kvalitativní tvrzení o pomoci třídění při vyhledávání na2/file13
   bylo jen dopředným odkazem na kapitolu6. P0376 nyní uvádí konkrétní
   binární vyhledávání a jeho invariant; není tím předem uzavřena
   celá kapitola6.
3. P0365 dokazuje listy=sestupy+1 pouze pro n≥1, a to i výslovně uvádí.
   Úloha Runs27 n≥1 výslovně neříká. Pro prázdný les je listů0,
   kdežto A(0,0)=1; bez vyloučení n=0 nelze tvrdit celý rozsah.
   Hranice se vrací na partial, spolu s příslušným uzavřením úlohy27.
   Platný důkaz pro neprázdné lesy se neruší. Zatím nejde o kartu chyby:
   je třeba rozlišit implicitní obor úlohy od tvrzení pro prázdný objekt.
4. P0280 používá Hadamardovu faktorizaci a P0295 spojitostní větu pro
   charakteristické funkce. Aplikace jsou věcně doloženy, ale dosavadní
   poznámky neměly přesný externí zdroj. Doplnění zdrojů a podmínek
   aplikace je uloženo v quality-recovery-addenda.md; nejsou vydávány za nově dokázané věty.

Další dřívější partial zůstávají: P0010/P0011(model na5),P0050(hash/radix),
P0055(C0001),P0063/P0064(diskrétní logaritmy),P0137(kombinatorická
involuce),P0199(C0017),P0372(C0018). Historické implementace, slovníky,
hudební pramen a neověřené bibliografické priority jsou stále výjimky.
Samotné přiřazení položek ani tento vzorek neuzavírá žádnou celou stránku
v UI. Přesná mapa a doplnění jsou v quality-recovery-addenda.md.
Checkpoint je konzistentně uložen pro uživatelem vyžádaný restart;
377 položek,367 checked a10 partial. UI hloubka žádné stránky nebyla povýšena.

## Přečtené vzory a konkrétní použití

- workstreams/vol1/notes/binomial-inequality.md: celé odvození obou
  nerovností, hraniční rovnost i oddělení chyby kroku od pravdivého
  výsledku. Zde stejný princip znamená samostatně sledovat znaménka
  nuly a libovolný radix MIX a neuzavřít n=0 jen důkazem pro n≥1.
- audit-2026-10-31/SAT_ALGORITHM_NOTES.md: počítání kroků Algorithm R,
  obecné meze i celá rodina F024 s C_m=5+2C_(m−1). Zde proto počítám
  konkrétní operace pointer doubling a třídicí průchody; existence
  jiného rychlého algoritmu by neověřila vytištěný postup.
- audit-2026-10-31/COGRAPH_NOTES.md: všechny F033–35, realizace událostmi,
  souvislý protipříklad a obecné opravené kritérium. Zde proto držím
  rozlišení úplného stromového invariantu od pouhých grafových filtrů,
  správnosti algoritmu od jeho reprezentace a hranice od chyby výsledku.

Žádný starý numerický verifier, census ani enumerace nebyly opakovány.


## Výslovné upřesnění obnoveného rozsahu po restartu

Uživatel chce znovu důkladně projít části dříve čtené nedbale: celý
čtenářský náskok47–139 se všemi úlohami, podčástmi, odpověďmi a dodatky;
současně všechna nedoložená tvrzení a mezikroky úvodu1–46, i pokud měly
staré checked. Převzetí je přípustné jen pro konkrétní již uložený důkaz
stejného rozsahu. Tři znovu odvozené vzorky ani inventář neuzavírají
celý úvod. Při zjištění nepodloženého uzavření se otevře související blok.

První následný blok je notes/opening-cost-models.md: P0010/P0011
nebyly uzavřeny nevyřčeným modelem. Samostatně byly doloženy bitová
délka, transformační lemma, správnost/cena košů a dopředný L² odhad
úlohy38; uniformní konstanta jiného algoritmu je oddělená mezera.
Konkrétně tak používám vzor rozlišování pravdivé věty, vadného argumentu
a nedoloženého předpokladu; žádné kvantifikátory se tiše nezaměňují.


Tableaux47–54 je nově doložené v notes/tableaux-proof-47-54.md, P0384–0406.
Z rozpracovaného draftu nebyl převzat závěr bez doplnění: zvlášť jsou
oba směry inverznosti I/D, všechny skenovací/přechodové invarianty,
přípustnost každého reverzního rohu a úplná indukce symetrie. Úloha2
má obecný invariant minimálních konců, nikoli jen kontrolu příkladu.
Předpoklady přímého přístupu i prázdný/singletonový vstup jsou výslovné.
To uplatňuje vzor obecného argumentu a hranic ze svazků1/4B.
Následující AlgorithmS ani zbývající náskok55–139 se tím neuzavírají.


U AlgorithmS se nová kontrola řídila skutečnou sazbou: S3 používá
sentinelovou relaci, takže rovnost dvou∞ vede doS5 a návratS4 přímo
doS3 je korektní. Úlohy10–12 nyní mají úplné argumenty v
notes/tableaux-proof-sorting-55-56.md. V průměru byly výslovně odděleny
dvě distribuce. VětyC/D ani involutivita nebyly uzavřeny z odkazů
nebo obrázku; obecné závislosti4–5 zůstávají skutečným dalším úkolem.


Notes/tableaux-proof-interchanges-04-05-cd.md uzavírá skutečné obecné
závislosti4–5, C/D a involutivitu. Zvlášť byl doplněn mezikrok, že
největší prvek neovlivní ostatní ani při svém pozdějším vytlačení;
samotné pozorování při jeho vložení by nestačilo. Obě řádková lemmata
obsahují krátké/prázdné řádky a∞, nikoli jen obecnou polohu. P0418–20
jsou změněny na checked až s těmito důkazy, ne z odkazu na známou větu.


Notes/tableaux-proof-counting-58-60.md doplňuje i podmínky rozšířené
domény(34), normalizaci prázdného tvaru a všechny nulové členy
rekurence. Konvence záporného faktoriálu byla vyhledána ve skutečném
zdroji svazku1 místo domnělého nálezu. Notes/tableaux-proof-repeated-labels.md
odděluje bibliografii od matematického tvrzení o opakovaných štítcích:
existence je nyní doložena konstrukcí a obousměrnou inverzí, nikoli
přeskočena jako pouhá citace. Důkaz hook formula je samostatný vůči
chybnému pravděpodobnostnímu argumentu, jehož závislost je výslovně ukázána.


Blok60–62 v notes/tableaux-proof-catalan-involutions-60-62.md má
obě strany všech použitých bijekcí, skutečnou opravenou orientaci
vzoru312 a odlišuje slabou/striktní ballot podmínku včetně prázdného
případu. Externí Hermitova normalizace je konkrétně ověřena vNISTDLMF,
aplikace na imaginární argument má polynomiální zdůvodnění.
Připravovaná asymptotika63–64 zatím není tímto blokem uzavřena.


Asymptotika63–64: každý přechod nyní má samostatný důvod v notes/tableaux-proof-asymptotics-63-64.md. Zvlášť se rozlišují diskrétní ocas, nenormalizovaný integrální ocas, libovolný Eulerův řád a vážený Taylorův zbytek. Podle vzoru binomické nerovnosti/COGRAPH je potvrzená chyba nového errata2006 oddělena od pravdivého původního odhadu a finální asymptotiky; ty mají vlastní důkaz. Žádný soubor koeficientů ani starý běh nebyl převzat jako náhrada obecného zbytku. Zbývající úlohy a náskok65–139 nejsou tímto uzavřeny.


Úlohy1–9 jsou doloženy v notes/tableaux-proof-01-09.md; dřívější hotové důkazy2/4/5/7 se jen přebírají. U6 byla nově doložena skutečná involuce vytlačeného zápisu, parita každé třídy a nulové dolní sloupce. U9 je oddělen počet tableau od počtu permutací. Tím se uplatňuje kontrola všech předpokladů a hranic ze vzorů1/4B; ani nový uzavřený blok neopravňuje zavřít zbývající66–139 nebo dřívější mezeru na607.


Notes/tableaux-proof-14-20.md odvozuje celé odpovědi včetně vedlejšího obecného Feitova determinantu a skutečné vzájemné nezávislosti stromových minim. Počet průniku událostí sám nebyl zaměněn za nezávislost. Požadavek14 na nový přímý důkaz zůstává partial i při už dokázané větě; tím se drží přesný rozsah místo formálního spárování všech čísel úloh.


Posunutá tableaux21: notes/tableaux-proof-21-shifted-hooks.md doplňuje obecný pólový argument namísto pouhé derivace v jednom bodě a přesný řádkový součin všech háčků. Nulový poslední díl, rovnost po odebrání a shodné pravé konce řádků jsou výslovně ošetřeny. Tím je uzavřen výsledek i potřebný argument, bez vydávání krátké tištěné nápovědy za úplný důkaz.


Notes/tableaux-proof-22-24.md ověřuje i všechny mezikroky determinantové indukce, přidaný význam trojúhelníku2020 a součet24 bez vypsané odpovědi. Krajní šířka0, nedostatek štítků, nulový koeficient a prázdná abeceda mají explicitní obory; formalita jmenovatele yz byla doložena v předchozím bloku. Žádná všeobecná stránková kontrola nevznikla z pouhého spárování úloh.


Notes/tableaux-proof-27-29.md drží přesné hranice: involuce27 používá skutečné duální pořadí; hluboká28 má primární theorem a zvlášť odvozené momentové důsledky;29 potřebuje prefaktor Stirlinga, který hrubá exponenciální mez nemá. Externí analytický důkaz není vydáván za vlastní ani za nezávisle zrevidovaný. Samotná distribuční konvergence nebyla zaměněna za konvergenci průměru.


Důkladný Tableaux30 checkpoint: notes/tableaux-proof-30-poset-evacuation.md a sources/tableaux-poset-evacuation-source.json, P0538–0545. Obecný invariant, terminace, přesný slovní model, úplné algebraické rušení i převod opačného numerického pořadí doloženy; náklady a krajní posety samostatně. Celkem545 položek:533 checked/12 partial. Bez nálezu a výpočtu.68 argumentově uzavřená,69/611 partial. Další kurzor69/file80 úloha31; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Zásada ze vzoru AlgorithmR použita konkrétně: slovní operace je odvozena z přesných posunů, ne jen pojmenována jako známá involuce; počet porovnání neztotožněn bez předpokladu s časem reprezentace posetu.


Důkladný Tableaux31–34 checkpoint: notes/tableaux-proof-31-34.md, P0546–0561. Symetrické věže mají přesnou bijekci i asymptotiku s oběma ocasy;33 celé determinantové/Schurovy doplňky včetně symetrie a dvou obousměrných korespondencí;34 přesný spodní okraj a obě opravené větve. Celkem561 položek:549 checked/12 partial. Bez nálezu a numeriky, známé opravy2005/2006/2022 odděleny.611 argumentově uzavřená,69/612 partial. Další kurzor69/file80 úloha35; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Vzor binomické nerovnosti použit na celý obor celých argumentů a nuly v33; vzor kografů na odlišení známé vady dílčího kroku34 od platného výsledku. Asymptotika31 má globální majorantu, nikoli jen lokální Taylorovu shodu.


Důkladný Tableaux35–37 checkpoint: notes/tableaux-proof-35-hillman-grassl.md a notes/tableaux-proof-36-37-plane-partitions.md, P0562–0575. Úplné oba invarianty a pořadí cest, oba směry inverze a cena; všechny koeficientové kroky36 včetně sevření při opakovaných hodnotách;37 formální stabilizace, nulové doplnění výslovné. Celkem575 položek:563 checked/12 partial. Bez nálezu a programu.69 a612 argumentově uzavřené,70/613 partial. Další kurzor70/file81 úloha38; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Vzor AlgorithmR použit na skutečné jednotlivé kroky a cenu G/H; vzor binomické nerovnosti na konstanty, pevné parametry a oba limity36. Původní stručná věta o obrácení algoritmu byla nahrazena dvěma samostatnými důkazy, nikoli pouze názvem známé bijekce.


Důkladný Tableaux38 checkpoint: notes/tableaux-proof-38-hook-walk.md, P0576–0581. Všechny cesty a indukční větve včetně nulových indexů, přesný podíl háčků, rekurence i uniformita doloženy. C0008 převzat; nový nález ani běh nevznikl. Celkem581 položek:569 checked/12 partial.70/613 partial kvůli39. Další kurzor70/file81 úloha39; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Vzor kografů použit konkrétně: chybný základ důkazu je oddělen od pravdivého pravděpodobnostního vzorce a závěru; všechny degenerované indukční větve jsou samostatně doloženy.


Průběžný konzistentní checkpoint39: nový C0020 confirmed/medium v notes/V3-C0020-inverse-tableau-row-boundary.md, pět vrstev sources/tableaux-inverse-boundary-errata-review.json. Platný čtyřbuněčný pár vyvrací kandidátní invariant a bez hranice aktuálního řádku zastaví inverziQ. P0582 eviduje pouze tento rozpor; celá opravená bijekce zatím není uzavřena. Celkem582 položek:570 checked/12 partial;16 confirmed nálezů (15 kniha,1 errata). Anglická karta a lokace614/file625 uložené. Bez výpočtového běhu. Kurzor zůstává70/file81 úloha39.
Zásada vzoru AlgorithmR: nový rozpor vzniká na skutečně přípustném vstupu a po přesných krocích; hranice z primárního zdroje je spárována transpozicí, nikoli přenesena bez kontextu. První rychlé čtení tento bod nedoložilo.


Dílčí důkladný checkpoint39: notes/tableaux-proof-39-forward-examples.md a sources/tableaux-nps-inverse-source.json. P0583–0593 checked, P0594 partial: dopředné invarianty/náklady, mezeQ, malé části, všech8/16 kroků,15 hran a5 kódů doloženy; celý obecný přenos kandidátů opravené inverze a první kód ještě nedokončen. Jednoznačnost(e) na něm závisí. Celkem594 položek:581 checked/13 partial. Bez programu a bez dalšího nálezu; C0020 dříve uložen. Žádná celá stránka nepovýšena. Přesný další kurzor39(f)/P0594 na70–71 a614; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Konkrétní použití vzoru AlgorithmR: korektní dopředné třídění a úspěšné příklady se nezaměňují za obecnou správnost inverze; geometrický invariant zůstává explicitně otevřený přes dostupný publikovaný důkaz.


Důkladné uzavření Tableaux39: notes/tableaux-proof-39-inverse-invariant.md. P0594 checked: vlastní obě lokální inverze, rovinné pořadí, dvě bariéry min-kroků, oba přenosy všech kandidátů, meze Q, první kód a bijekce bez hook formula; tím i jednoznačnost(e). C0006/C0020 se neruší. Celkem594 položek:582 checked/12 partial.70 a613 argumentově uzavřené,71/614 partial kvůli40 onward. Žádný program. Další kurzor71/file82 úloha40; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Uplatnění vzorů1/4B: lokální inverzi a obecnou stabilitu jsem oddělil; obecný důkaz nyní zahrnuje všechny přenosy kandidátů i mezní řádek, místo uzavření podle shody s primárním zdrojem.


Důkladný Tableaux40 checkpoint: notes/tableaux-proof-40-corner-growth.md a sources/tableaux-corner-growth-source.json, P0595–0600. Všech15 faktorů, ekvivalence hodin/neexploze, deterministické časové sevření, konstanta6 a uniformní všechny řádky doloženy. Hluboká Rostova věta je výslovná přesná externí závislost; žádné předstírání úplného analytického důkazu. Celkem600 položek:588 checked/12 partial.71 argumentově uzavřena,614 partial. Bez nálezu a programu. Další kurzor72/file83 úloha41; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Uplatnění vzorů: přesné oddělení externí věty a vlastního převodu, kontrola náhodného času místo neoprávněné substituce a uniformní zachycení krajních řádků.


Důkladný Tableaux41 checkpoint: notes/tableaux-proof-41-library-distance.md a sources/tableaux-fredman-source.json, P0601–0605. Oba směry dis=n−L a explicitní konstrukce, převzatý první řádek a vlastní ostrá horní mez porovnání. Matching lower bound přesně vymezen jako externí Fredmanova věta; celý důkaz po timeoutu netvrzen. Známé erratum2006 odděleno. Celkem605 položek:593 checked/12 partial. Bez nového nálezu a programu. Další kurzor72/file83 úlohy42–44 a přidaná45(a)–(f) z2020;72/614 partial, čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Uplatnění vzorů: obecný počet nezměněných prvků místo několika příkladů, zvlášť konstruktivní opačná nerovnost a přesný porovnávací model externí dolní meze. Inventář rozšířen o pozdější45 se všemi podčástmi.


Důkladný Tableaux42 checkpoint: notes/tableaux-proof-42-signed-reversals.md a sources/tableaux-reversal-sources.json. P0606–0612/P0614–0615 checked: všechny cykly, orientace, pět prvních možností, čtyři přesná dokončení a důkaz nemožnosti druhé větve. Primární zdroje modelu a aktuálního nákladu ověřeny, hluboké algoritmy externí. P0613 partial: povoleně vynechaný census179904, žádný BFS. Celkem615 položek:602 checked/13 partial. Bez nového nálezu;72/614/615 partial. Další kurzor72/file83 úloha43, potom44 a přidaná45; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Uplatnění vzorů: přesné podepsané operace, všechny cyklové případy a obecné kritérium orientace; konkrétní cesty nenahrazují důkaz dolní meze. Census oddělený od ověřené vzdálenosti.


Důkladný Tableaux43 checkpoint: notes/tableaux-proof-43-reversal-diameter.md, P0616–0621. Všechny kontrakce, polohové případy a dvojitý zisk, nekruhová indukce i obě extrémní rodiny doloženy. Celkem621 položek:608 checked/13 partial. Bez běhu a nálezu;72/615 partial. Další kurzor72/file83 úloha44, potom přidaná45(a)–(f); čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Uplatnění vzorů: každý speciální krok má konkrétní interval a hranice; silnější negativní indukce je od obecné meze oddělena a lichý extrém nezůstává na neurčitém „podobně“.


Důkladný Tableaux44 checkpoint: notes/tableaux-proof-44-average-reversals.md, P0622–0630. Všechny cyklové počty, tři nemožné příklady, přesný počet doplnění, znaménka9/5, algebra i ostrá průměrná mez pro n≥1 doloženy. Levopravá kompozice ověřena ve sv.1; historický nepodepsaný Gollanův výsledek je přesně vymezená externí věta. Celkem630 položek:617 checked/13 partial. Bez nálezu a běhu;72/615 partial. Další kurzor přidaná45(a)–(f),72/file83 a errata2020; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Uplatnění vzorů: před srovnáním permutací byla ověřena skutečná kompoziční konvence; počet formálních objektů je oddělen od realizovatelných a ostrá nerovnost má vlastní důvod i přesnou doménu.


Dodatek Tableaux45: P0631–0643 dokládají celý pozdější přídavek, nejen první tisk. Podle vzorů1/4B je rozlišen skutečně potřebný předpoklad(ii), oba směry bijekce, všechny hraniční štítky i přesná konvence nápovědy. Obecný důkaz nepoužívá několik numerických příkladů jako náhradu inverze. Bibliografické zdroje nejsou skrytou matematickou závislostí. Stav643/630checked/13partial; notes/tableaux-proof-45-permutation-tableaux.md.


Obnova počítacího bloku73–79: P0644–0659 nahrazují čtení přesnými invarianty každé fáze i celými tabulkami a náklady, ne pouhým spárováním odpovědí. Vzorové rozlišení tvrzení a předpokladů ponechává P0646 partial, zatímco abstraktní D je dokázán i pro u=v a vadná implementace má převzatý C0009. Celkem659/645checked/14partial; notes/internal-proof-counting-73-79.md.


Cyklický blok10–11: přesný invariant původních/změněných záznamů a p, obousměrné přesuny, ukončení a celý nákladový součet; u pravděpodobnosti explicitní uniformita a nevyužití falešné nezávislosti pevných bodů. Vzorové rozlišení externího srovnání od vlastního výsledku vede k P0668partial. Stav668/653checked/15partial; notes/internal-proof-10-11-cycles.md.


MacLaren12: podle standardu1/4B nestačí nerovnost LINK(j)≥j k vyloučení smyčky. P0670–74 proto vedou skutečně konečnou jednoduchou cestu a její přesnou transformaci, čímž dokazují správnost i přesný amortizovaný počet. Inverze je konstruktivní, nikoli jen shodaN!. Relativní heuristická rychlost zůstává odděleněpartial. Stav676/660checked/16partial; notes/internal-proof-12-list-rearrangement.md.


Důkladný distribuční13 checkpoint: notes/internal-proof-13-distribution-shuffle.md, P0677–0684. Pevné intervaly, celý cyklus s dírou, všechny větve skeneru, ukončení z nejmenší zbývající pozice, přesné lineární náklady, paměť a nestabilita doloženy. Současné opravy2019/2024 zohledněny bez nového nálezu. Celkem684 položek:668 checked/16partial. Bez programu; žádná celá stránka nepovýšena. Další kurzor§5.2.1 od80/file91; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný přímé-vkládání checkpoint: notes/insertion-proof-straight-80-82.md, P0685–0700. Celý S/MIX, tabulka, všechny momenty, úlohy1–5 a vkládací část33 mají obecné argumenty včetně přesné kubické ceny osmiřádkové varianty. P0697partial je výslovná domněnka minimálního počtu instrukcí, nikoli chyba. Celkem700 položek:683 checked/17partial. Bez nálezu a běhu; žádná nová celá stránka nepovýšena. Další kurzor82/file93, binární/dvousměrné vkládání a6–7; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný binární/dvousměrný checkpoint: notes/insertion-proof-binary-twoway-82-83.md, P0701–0711. Binární invariant, celý kruhový přechod s opačnou dírou a rotace, přesný poloviční vedoucí počet přesunů a všechny momenty vzdálenosti včetně dodatku2002 jsou doloženy. P0703partial je neověřený historický strojový údaj, nikoli matematický rozpor. Celkem711 položek:693 checked/18partial. Bez nálezu/běhu a nových celých zelených stran. Další kurzor83/file94, Shellsort; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný Shellsort-program checkpoint: notes/insertion-proof-shellsort-program-83-86.md, P0712–0724. Celý h-invariant, každá samomodifikace/MIX četnost, obě tabulky s novýmiA, úlohy8–10/43 a přesná3(C−T) úspora doloženy; C0010 převzat. P0718 čeká na průměrový blokH, P0723/P0724 jsou empirické/výzkumné partial. Celkem724 položek:703 checked/21partial. Bez nového nálezu/běhu. Další kurzor86/file97,2-ordering a lattice11–15; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný2-ordered-lattice checkpoint: notes/insertion-proof-two-ordered-86-88.md, P0725–0739. Rovnoměrnost, celý obrázek, obě váhy a plocha, všechny hraniční členy, úplné11–14, vlastní binomickáGF, obě parity průměru a ostré maximum doloženy. Celkem739 položek:718 checked/21partial. Strany86–87 mají úplnou argumentovou coverage. Bez nálezu/běhu. Další kurzor88/file99 přes celou úlohu15 na103, odpovědi620–621; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný distribution15 checkpoint: notes/insertion-proof-15-distribution.md, P0740–0754. Celé rozklady/rekurence, všechny G/H derivace, Eulerova koeficientová extrakce, rozptyl pro obě parity, všechny momenty i oba dodatky621 mají samostatné důkazy. Stromová konvence/odkaz ověřeny v originálu sv.1, dva obrazy v images/. Celkem754 položek:733 checked/21partial. Bez nového nálezu a programu. Další kurzor88/file99, TheoremH a corollary; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný H checkpoint: notes/insertion-proof-h-88-89.md, P0755–0766. H/corollary má celý podmíněný model,16 současné maximum všech průchodů,17 jedinečnost,19 všechny minima; graf12, uniformní režim a přesné optimum doloženy. P0718 uzavřen jen jako přibližné srovnání s přesnými hodnotami, nikoli globální práh13. Celkem766 položek:746 checked/20partial. Čtyři cílená racionální dosazení bez enumerace; bez nálezu.84/88/89 argumentově uzavřené. Další kurzor18 na103/file114 a621, potom main90/file101; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný18 checkpoint: notes/insertion-proof-18-optimization.md, P0767–0773. Celá kladná doména, globální minimum, všechny faktory/limita,18 čísel i platné dělitelné zaokrouhlení a bariéra90 doloženy. Celkem773 položek:753 checked/20partial. Jedno přímé dosazení, bez enumerace a nálezu.621 argumentově uzavřená;90/103 partial. Další kurzor90/file101 K/L a20, potom21; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný K/L checkpoint: notes/insertion-proof-k-l-20-21-25.md, P0774–0785. Úplné L/K/20/21/23 a matchingová25 mají vlastní argumenty, hlavní<2N injekci, výstup konkrétní nerovnoměrnost. P0785partial pro dvě další konstanty25 z42. Celkem785 položek:764 checked/21partial. Bez výpočtu/nálezu a nové celé zelené stránky; související ostrá26 zůstává čekat. Další kurzor104/file115 úloha26, potom22 aP/24; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný ostrá26 checkpoint: notes/insertion-proof-26-sharp-bound.md, P0786–0790. Všechna pořadí mají úplný šestistavový model,13 přechodů a potenciál; konstrukce, ostré N≡2, všech devět inversí, nejkratšíN8 a asymptotika všech N doloženy bez enumerace. Celkem790 položek:769 checked/21partial. Bez běhu/nálezu;90 argumentově uzavřená,104/623 nadálepartial. Další kurzor22 na103/file114 a622, potomP/24; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný22 checkpoint: notes/insertion-proof-22-semigroups.md, P0791–0797. Obě celé intervalové rodiny, všechny genus/rekurence a15 tabulkových minim doloženy bez enumerace. Jediná mezera P0797 je možný chybějící rozsah s≥2; V3-C0021candidate-low má explicitní s1 rozklad a pět vrstev, žádný nový confirmed. Celkem797 položek:775 checked/22partial. UI karta/lokace uložené;103/622partial. Další kurzorP na91/file102 a24; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Dílčí důkladný P/24 checkpoint: notes/insertion-proof-p-and-24-construction.md, P0798–0804. Celá horní P včetně režie a malých t, kvadratický kontrast, obecná konstrukce24, všech20 hodnot a počet nových pozic doloženy. P0804partial pouze pro obecné c(w_k)≥Q/2−2k; přesný vzorec jeho inversí je prokázán. Celkem804 položek:781 checked/23partial. Bez běhu/nálezu a nové celé zelené stránky. Další kurzor právě P0804 na622/file633; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladné uzavření24: notes/insertion-proof-24-local-bound.md, P0804checked a P0805–0810. Vlastní bitový test/monotónní inverze a tři disjunktní rodiny dokazují celý lokální odhad, konstantu i padding bez programu. P0810partial pouze pro nedostupný širší historický odkaz včetně(12). Celkem810 položek:787 checked/23partial. Bez nálezu a nové celé zelené stránky; samostatné P0785/P0797 zůstávají. Další kurzorPratt91/file102 a30/31; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Nálezový checkpoint811: nový C0022confirmed/low v notes/V3-C0022-pratt-eight-item-overhead.md a pět vrstev sources/pratt-eight-item-errata-review.json. Průměr276.24u je menší než minimum324u; všech22 instrukcí ukazuje vynechaných15T=75u. P0811checked, celkem811 položek:788 checked/23partial;17confirmed(16kniha,1errata),5candidate. Bez výpočtu či enumerace, přesnýAave netvrzen. Anglická karta a lokace624/file635 uloženy. Kurzor zůstává celý Pratt30/31, žádná nová celá stránka nepovýšena.


Důkladný Pratt checkpoint: notes/insertion-proof-pratt-30-31.md, P0812–0824. Celé30, každá adresa/invariant/četnost31, statistická involuce, celý příklad, maximumA10, přesný počet40/S9045 a generátor doloženy. P0821partial pro malé průměry/maxB, P0823partial pro empirii/model. Celkem824 položek:799 checked/25partial. Bez programu a dalšího nálezu; C0022 převzat. Žádná nová celá stránka nepovýšena. Další kurzor konec91/file102 a92, konstrukce(8); čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný Incerpi checkpoint: notes/insertion-proof-incerpi-41.md, P0825–0833. Celá báze, součinový/gcd invariant, uniformní Θ růst, přesná suma a konstanta větyI včetně režie i prvočíselný limit mají vlastní argument. PNT je doložená vnější závislost; opravy2000 známé, žádný nový nález. Celkem833 položek:808 checked/25partial. Jedno malé přesné gcd dosazení, bez enumerace;92/105/627partial. Další kurzor dolní92/file103 a tabulka5 na93; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny. Vzor1/4B použit: nezamlčené zakázané prvočinitele, konkrétní rozsah vnější věty, součin konstant místo neplatného opakování O a oddělený neuniformní limit.


Důkladný N8 checkpoint: notes/insertion-proof-eight-items-table5.md, P0834–0843 a P0821checked. Celá tabulka, obecný přesný rankový součet, všech15 trojic, globální časové optimum, ruční maxima17/19 a úplné Prattovy malé statistiky doloženy. P0839/C0023candidate-low jen pro nejasný rozsah minimize; nezávislá GF dokládá rozdíl1/21. Známá274.41 oddělena. Celkem843 položek:818 checked/25partial,17confirmed/6candidate. Krátké nice15 součty a256stavový potenciál; žádné generování permutací. Další kurzor93/file104 pod tabulkou5;92 nadálepartial, čtenářský139/file150 a nejstarší otevřené5/file16 beze změny. Vzor1/4B použit: nejhorší svědek doplněn horní mezí; pro prefixový stav prokázána jeho dostatečnost; nový protipříklad ověřen samostatnou GF, ale kontextová nejasnost stále brání confirmed.


Důkladný praktický checkpoint: notes/insertion-proof-practical-93-95.md, P0844–0854. Prvních8 momentových řádků, všechny39 časové substituce, všechny součty Table7, Pratt-like cutoff a celý aktuální nákladový/rekurenční text doloženy. Zdroj Sedgewick1986 potvrzuje rozsah opravy2025. P0846/P0852/P0854partial jen pro jmenované experimenty, fit a29. Celkem854 položek:826 checked/28partial. Bez nového nálezu; malá aritmetika bez náhodných vstupů. Další kurzor27 na104/file115 a623, potom42/P0785 před list insertion; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny. Vzor1/4B použit: explicitní rozdíl mezi podobnými posloupnostmi/větami a mezi přesnou aritmetikou dodaných čísel a neověřeným experimentem.


Důkladný27 checkpoint: notes/insertion-proof-27-lower-bounds.md a sources/insertion-lower-bound-sources.json, P0855–0863. Celé(a)/(b), všechny konstanty/předpoklady, prázdný interval a různé klíče doloženy; Poonen17 je výslovná vnější závislost. P0862partial pro uniformní c<1/2 bez logaritmického dělitele, nikoli nový nález. Celkem863 položek:834 checked/29partial. Bez matematického běhu a nové celé zelené strany. Další kurzor42 na105/file116 a627, potom list insertion; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný42(a) checkpoint: notes/insertion-proof-42-first-second.md, P0864–0870. Všechny momenty, párové/CRT rozklady, fázové okraje a oba režimy doloženy. C0024candidate-low pouze nevyjádřený rozsah pomocné8N/(gh), hlavní výsledek platí; pět vrstev v sources/phase-shift-bound-errata-review.json. Celkem870 položek:840 checked/30partial,17confirmed/7candidate. Bez běhu a nové celé zelené strany. Další kurzor42(b) na105/627 a P0785, pak list insertion.


Důkladný42(b) checkpoint: notes/insertion-proof-42-third-psi.md a sources/insertion-three-increments-sources.json, P0871–0883. Celá modulární/Fourier/coupling argumentace, oba chybové režimy a psi asymptotika včetně krajů doloženy. P0785 uzavřen přesnými1/4 a1/3, chyba O(1). Berry–Esseen je výslovná klasická závislost, ne skrytý předpoklad. Celkem883 položek:854 checked/29partial. Bez běhu/nálezu a nové celé zelené strany; C0024/P0862 ponechány. Další kurzor list insertion dolní95/file106 a32–40/44; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


DůkladnýL checkpoint: notes/insertion-proof-list-95-97-32-33.md, P0884–0894. Celé95–97/32/33 a seznamová36 mají invarianty, všechny instrukce/náklady, Nprime statistiku i konkrétní lineární přerovnání. Nový notes/V3-C0025-list-insertion-example-time.md confirmed-low:433u místo358u, pět vrstev v sources/list-insertion-time-errata-review.json. Celkem894 položek:865 checked/29partial,18confirmed/7candidate. Bez běhu;96–97 plně argumentově pokryté. Další kurzor98/file109, pak M a34–40/44; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný M checkpoint: notes/insertion-proof-trees-batching-98.md a notes/insertion-proof-m-program-99-100-34-36.md, P0895–0909. Celý obrázek, oba stromové nákladové modely, dávkování, všechny instrukce/frekvence M/spojování,34–36 a END optimalizace doloženy. P0896partial je pouze neurčený praktický exponent na98. Celkem909 položek:879 checked/30partial,18confirmed/7candidate. Bez matematického běhu a nového nálezu;99/100/625 plně argumentově pokryté. Další kurzor101/file112, všechny momenty a37–40, potom44; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Vzory1/4B použity při oddělení marginálů od nezávislosti, průměrného stromu od garantované varianty a při přesném rozlišení skoku na štítek5H od průchodu přes nový END zápis. Žádný empirický fit ani úplná kapitola6.2.2 nejsou uzavřeny pouhou ilustrací.


Důkladný M-analýza checkpoint: notes/insertion-proof-m-analysis-101-102-37-40.md, P0910–0926. Všechny průměry/extrémy, harmonické zbytky, celé37 GF/koeficienty/rozptyl,39 a40 včetně nekonečného ocasu i konstant doloženy. P0381 převzat, odlišnáP0383partial ponechána. Nový notes/V3-C0026-multiple-list-total-times.md confirmed-low:44.62N/41.89N místo44.99N/41.95N, pět vrstev v sources/multiple-list-total-time-errata-review.json. Celkem926 položek:896 checked/30partial,19confirmed/7candidate. Tři přímé racionální Taylorovy intervaly nice15, žádná enumerace;101 argumentově pokrytá. Další kurzor105/file116 celé44 a pokračování43 na628, pak§5.2.2; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Standard1/4B použit při společné optimalizaci7B−3A, rozlišení režimůM=1/fixní/proporcionální, kontrole absolutní chyby u singularityu0 i v nekonečném ocasu a vyčíslení přesně té instrukce, kterou prázdný seznam přeskočí. Část38 ani celá odpovědní stránka se nezavírá přes silnější dosud neprokázanouP0383.


Důkladný44 checkpoint: notes/insertion-proof-44-orders.md, P0927–0933. Celé definice/rankové ekvivalence, všechny44(a)–(c), silná reverzní implikace a explicitní chybějící join doloženy; slabá mřížka a sousední cesta převzaty. Závěr43 je správný s plným h1, ale praktické srovnáníP0928partial. Celkem933 položek:902 checked/31partial,19confirmed/7candidate. Bez běhu/nálezu a nové celé zelené strany. Insertion není paušálně uzavřena; všechny zbývající konkrétní mezery jsou vypsány v bloku proof-audit. Další kurzor§5.2.2,105/file116, celý bubble sort106–110 a úlohy; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Zásada vzorů1/4B: důkaz musí pokrýt přesný předpoklad;44(b) se proto doložilo prahovými počty pro silnou relaci, a ne pouhým převzetím pravdivé slabé implikace z odpovědi. U neexistence mřížky nestačí dvě neporovnatelné horní meze: výslovně vyloučen i možný join pod nimi.


Důkladný bubble-core checkpoint: notes/exchanging-proof-bubble-core-105-108.md, P0934–0945. Celé výměny/cykly, všechny B/MIX instrukce, obrázek14, větaI, hranice a oba důkazy6 i distribuceA doloženy. Konvence n−c počítá netriviální S výměny, nikoli samovýměny. Celkem945 položek:914 checked/31partial,19confirmed/7candidate. Bez matematického běhu/nálezu;106–108 argumentově uzavřené. Další kurzor109/file120, momenty a4/7/8, pak refinements110; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný bubble-moments checkpoint: notes/exchanging-proof-bubble-moments-109-4-7-8.md, P0946–0956. Celé4/7/8, oba momentyA, všechnyCDF souřadnice, konečné Cave, extrémy a vedoucí čas doloženy. UzavřenéP(n) ze svazku1 převzato přesně. P0955partial čeká pouze na jemné Cave128–130/44. Celkem956 položek:924 checked/32partial,19confirmed/7candidate. Bez běhu/nálezu a nové celé zelené strany. Další kurzor refinements109/file120 a110, pakW128–130/44; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný cocktail checkpoint: notes/exchanging-proof-cocktail-109-110-9.md, P0957–0968. Všechny skutečné průchody/šipky/hranice, oba směry Iversona, úplná prahová redukceu a konkrétní posun počátku doloženy. Nový notes/V3-C0027-cocktail-pass-count.md candidate-low pro poslední ověřovací průchod, pět vrstev v sources/cocktail-pass-count-errata-review.json; redukce i algoritmus platí. Výzkumné/modelové P0964/65/67 zůstávají partial. Celkem968 položek:932 checked/36partial,19confirmed/8candidate. Bez matematického běhu; žádná celá stránka nepovýšena. Další kurzorW128/file139 až130/43–44 proP0955, pak zpět k Batcher110–111; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný W checkpoint: notes/exchanging-proof-bubble-w-128-130-43-44.md, P0969–0983 a P0955checked. Všechny jednotlivé uniformní odhady, Eulerovy endpointy/zbytky, Gaussian řady, celé43 a čtyři příspěvky44 dokazují49/36 i jemné Cave. Nový notes/V3-C0028-regularized-sum-upper-limit.md confirmed-low: nekonečná pomocná suma má harmonický záporný ocas, oprava0<t<m; výsledné asymptotiky správné. Pět vrstev v sources/regularized-sum-upper-limit-errata-review.json, known opravy odděleny. Celkem983 položek:948 checked/35partial,20confirmed(19kniha,1errata)/8candidate. Bez matematického běhu;109/129 argumentově uzavřené. Další kurzor Batcher110/file121 až114 a10–16, bez přepočtu bubble; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.


Důkladný Batcher-core checkpoint: notes/exchanging-proof-batcher-core-111-113-10-13.md, P0984–0996. Všechny M kroky, bitové dvojice, libovolné délky a shodné klíče, celé10, obrázky17–18, tabulka1 i55/40/73 doloženy. Celkem996 položek:961 checked/35partial,20confirmed/8candidate. Bez matematického běhu/nálezu;111–112 argumentově uzavřené. Další kurzor celé12 a11/14–16 na134–135/629–630, potom Quicksort již na spodní113. Čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Zásada vzorů1/4B: geometrický obrázek nahrazen prahem pro každou hodnotu, výslovně doloženy obě hranice seznamů i shodné klíče; podobné paralelní modely nejsou zaměněny. Uzavřená část13 se nevydává za důkaz dalších algoritmů Q/R.


Důkladný Batcher-counts checkpoint: notes/exchanging-proof-batcher-mix-12.md a notes/exchanging-proof-batcher-counts-14-15.md, P0997–1011. Celé opravené instrukce/frekvence,939u, obecnéD/E, všechny části14–15 a obecná identita dodatku2021 doloženy. P1002partial je pouze nevymezené praktické srovnání. Celkem1011 položek:975 checked/36partial,20confirmed/8candidate. Bez matematického běhu/nálezu a další celé zelené stránky. Další kurzor celé11/16 na134–135 a629–630, potom Quicksort na spodní113; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Zásada vzorů1/4B: každý instrukční přechod a konečný index má invariant; pomocné počty mají přesně vyjádřený objekt. Rovnost aktuálního dodatku dokázána pro všechna N z obou rekurencí, nikoli ověřena jen na několika velikostech.


Důkladný Batcher-worst checkpoint: notes/exchanging-proof-batcher-worst-11.md, P1012–1019. Přesná hranová váha, globální cesta/penalizace, liché okraje, maximum61 a celý svědek i obecný asymptotický poměr mají vlastní důkazy. Celkem1019 položek:983 checked/36partial,20confirmed/8candidate. Bez enumerace/matematického běhu/nálezu;629 argumentově uzavřená. Další kurzor celé16 na135/630, potom Quicksort na spodní113; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Zásada vzorů1/4B: svědek61 je doplněn horní mezí pro všechny cesty a důkazem současné dosažitelnosti v rekurzivních podproblémech; lichá délka se neodvozuje neplatným pouhým odstraněním posledního prvku.


Důkladný Batcher-mean checkpoint: notes/exchanging-proof-batcher-mean-16.md, P1020–1031. Celá16 včetně každé konečné identity, uniformního Gaussian zbytku, Mellinovy kontury/konstant, periodického odhadu a průměru celého třídění doložena. Nový notes/V3-C0029-batcher-mean-sign.md confirmed-low: minus před(gamma+2)/(4ln2); původní1/4 platí. Pět vrstev v sources/batcher-mean-sign-errata-review.json, jediný malý intervalový běh nice15 s explicitním nekonečným ocasem. Celkem1031 položek:995 checked/36partial,21confirmed(20kniha,1errata)/8candidate. Další kurzor Quicksort spodní113/file124; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Zásada vzorů1/4B: znaménko nebylo přijato jen z rozporu pramenů; doložena správná normalizace a všechny konstanty i nemožnost absorbovat rozdíl do periodické chyby. Oscilující sumy mají absolutní chybu před součtem, mez nekonečné Fourierovy řady má výslovný analytický ocas.


Důkladný Quicksort-core checkpoint: notes/exchanging-proof-quicksort-core-113-117-17-21.md, P1032–1047. CeléQ1–Q9, každý příklad/17výměn,17–21 a Qčást13 mají vlastní argumenty; FIFO mez odvozena přes binomické vrstvy, C0011převzat. P1033partial pouze nevymezené praktické modely. Nový notes/V3-C0030-quicksort-equal-key-trace.md confirmed-low: vadná varianta čteK[-1] už ve druhé fázi, hlavní varování i původníQ správné. Celkem1047 položek:1010 checked/37partial,22confirmed(21kniha,1errata)/8candidate. Bez matematického běhu;116plně argumentově pokryta. Další kurzor celéMIX117–118/file128–129, pak119/22; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Standard1/4B použit při odlišení operační a pravděpodobnostní nezávislosti, zarážek s rovností, obou případů křížení a každé větveQ7. FIFO dolní mez má obecný důkaz včetně neúplného posledního patra; neznámý hardware model není nahrazen pozorováním na malém příkladu.


Důkladný Quicksort-MIX checkpoint: notes/exchanging-proof-quicksort-mix-117-118.md, P1048–1055. Každá instrukce/adresa, všechny větve a četnosti, prázdný pop i přesná cena(15)–(16) mají argumenty s explicitním rozsahem. P1055/C0031candidate-low: u velkého M může přetéct efektivní adresa M+j; doporučenéM9 bezpečné, nejasný zamýšlený rozsah neoznačen za chybu. Doklad definiceMIX ze svazku1p127 zobrazen. Celkem1055 položek:1017checked/38partial,22confirmed/9candidate. Bez matematického běhu a nové celé zelené stránky. Další kurzor119/file130 a22–24, čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Standard1/4B použit při kontrole mezivýsledku efektivní adresy, odlišení abstraktního algoritmu od strojového programu a oddělení přesného protipříkladu od nejasného rozsahu tvrzení. Žádná konvence o malémM nebyla potichu zaměněna za obecný důkaz.


Důkladný Quicksort-GF/means checkpoint: notes/exchanging-proof-quicksort-means-119-121-22-24.md, P1056–1067. Podmíněná produktová uniformita, všechnyGF/báze, každá rekurence/konstanta(18)–(25), celé22–24 a přesná guarded úsporaC−2A mají důkazy. P1067partial výslovně zbývá pro rozptyl a limitní dovětek; samotnéGF je neuzavírají. Celkem1067 položek:1028checked/39partial,22confirmed/9candidate. Bez nálezu/běhu/nové celé zelené strany. Další kurzor120/file131 momenty/limit, potom(26) na121; čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Standard1/4B použit při podmínění celým binárním vzorem (nikoli jen průměrným rankem), odlišení D od původních sestupů, obou krajních N uS a explicitním režimu každé aproximace. Nenormální limit není vydáván za důsledek pouhé formálníGF.


Důkladný Quicksort-limit/cost checkpoint: notes/exchanging-proof-quicksort-limit-cost-120-121.md, P1068–1075 a P1067checked. Výslovná vnější RöslerovaL2 věta přesně spárována; vlastní varianceA, přenosC=X+2A, integrály konstanty, nenormalitaMGF a každý pevnýcutoff doloženy. Celé(26), striktní konvexita/unikátníM9 a obě desetinné konstanty ověřeny bez hledání. Celkem1075 položek:1037checked/38partial,22confirmed/9candidate. Jeden malý aritmetický intervalnice15, bez nálezu;120/135/631plně argumentově pokryté. Další kurzor spodní121/file132, celé25–27 a náhodnýpivot(27); čtenářský139/file150 a nejstarší otevřené5/file16 beze změny.
Standard1/4B použit při přenosu mezi dvěma odlišnými nákladovými modely: deterministickéO(N) nestačí, proto je doložena přesná varianceA. Nenormalita není vyvozena z kresby či numerických momentů; optimumM9 má obecnou diskrétní konvexitu, nikoli konečný test.

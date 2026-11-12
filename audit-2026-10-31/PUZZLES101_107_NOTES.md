# DLX101–107: logické hádanky, hudební řady a hledání slov

Pracovní průchod 2. listopadu 2026. Zadání 134–136, odpovědi 438–440;
lokální PDF, první vydání/druhý dotisk 2022. Vizuálně zkontrolovány také
autorovy stránky PS143–144 z roku 2019. Výsledky a vstupy jsou v
`results/puzzles101_107/`; nové prameny v `sources/puzzles101_107/`.
Žádný nový emailový návrh.

## 101 — zebra

`check_zebra101.py` sestrojí všech 80 možností a oba převody. Celé množiny
řešení souhlasí mezi původním DLX2, doslovným interpretem Algorithm C
a nezávislým výčtem permutací poloh pěti kategorií. Jediné řešení:

| Dům zleva | Země | Povolání | Zvíře | Nápoj | Barva |
|---|---|---|---|---|---|
| 1 | Norsko | diplomat | liška | voda | žlutá |
| 2 | Ukrajina | ošetřovatel | kůň | čaj | modrá |
| 3 | Anglie | sochař | šneci | mléko | červená |
| 4 | Španělsko | houslista | pes | pomerančová šťáva | bílá |
| 5 | Japonsko | malíř | zebra | káva | zelená |

Přidání existence zebry a vody je přesně předpoklad implicitní v otázce.
V každé kategorii se pak všech pět hodnot vyskytuje alespoň v jednom
povinném vodítku. Pět různých hodnot nemůže obsadit méně než pět domů,
protože každá sekundární položka domu připouští jen jednu barvu. Proto
každá hodnota obsadí právě jeden dům: „all-different“ je skutečně redundantní.
Obráceně každé řešení logické hádanky vybírá právě jednu možnost každého
vodítka. Převod zachovává celou množinu řešení, nejen odpověď na dvě otázky.

Inverzní položky dovolují dřívější propagaci. Volba #5 nastaví inverzní
polohu Norska na0; ze všech osmi možností #11 pak zbude modrý dům na1.
Bez inverzí může #11 dočasně umístit další norský dům jinam. Samotné
inverze naopak nestačí: explicitní kompatibilní volba všech16 vodítek
v `zebra-checked.json` umisťuje všech pět národností do domu0.

`check_puzzle_details.py` vysvětluje benchmarkovou závislost na pořadí.
Numerické pořadí vodítek dává112 uzlů bez inverzí a34 s inverzemi;
lexikografické pořadí `c1,c10,...,c9` dává s inverzemi32. Všechny celé
modely jsou stejné. Kniha pořadí při rovnosti priorit neurčuje, takže
34versus32 není nový nález. Zaznamenané mems dovolují porovnat i cenu vstupu.

První parser terminálního výstupu nerozpoznal jednotné číslo „1 solution“.
Program přitom řádně skončil kódem0 se112 uzly. Původní výstup byl přijat
po opravě parseru bez opakování nativního hledání; chybná původní metadata
jsou zachována jako `zebra-direct-parser-before-fix.json`.

Historie zůstává oddělená. Vassbergův vlastní konferenční příspěvek2009
na ResearchGate výslovně popisuje reprodukci původní stránky95 z Life
International17.12.1962; text je přístupný, stažení reprodukce však vrátilo403.
Nemáme zatím ověřený úplný ročník35 ani datum přímo v originálním čísle.
Sekundární opakování tvrzení o prvenství není nezávislé ověření prvenství.

## 102 — stabilní označení orientovaného grafu

Obecný důkaz platí pro konečné jednoduché orientované grafy, včetně smyček
a vrcholů bez následníků. Paralelní hrany lze předem sloučit, protože počet
různých viděných značek na jejich násobnosti nezávisí. Každá zadaná značka
musí být respektována při tvorbě možností H aI. Značky mimo rozsah stupně
nedají žádnou možnost, tedy správně nesplnitelnou instanci.

I_v vybírá jedinou hodnotu λ(v), nastaví všechny indikátory i_vd a uvede
všem předchůdcům, že vidí tuto značku. H_v vynutí, že počet pravdivých
indikátorů h_vd je λ(v). Pro každou dvojici v,d vybere E_vd buď první
následník se značkou d, nebo možnost „žádný takový následník“. Podmínky
i_wj,d=0 pro všechny dřívější následníky zajišťují nejen ekvivalenci OR,
ale i jediné rozšíření každého skutečného označení do XCC modelu.
H aI sdílejí barvu položky v; I aE sdílejí indikátory i; H aE sdílejí h.
Tím jsou splněny právě rovnice
`λ(v)=|{λ(w): v→w}|`. Opačný směr získáme výběrem možností z těchto rovnic.
Pro stupeň0 je hodnota0, pro stupeň1 hodnota1, i při smyčce.

`check_arrows102.py`: všech6974 testovacích instancí,3469 modelů,
4452 nesplnitelných. Zahrnuje všechny grafy na1–3 označených vrcholech
včetně smyček, bez předepsané značky i se všemi jednotlivými předepsanými
značkami0..n; dalších200 deterministicky generovaných grafů na4/5 vrcholech.
Celé množiny se rovnají přímému výčtu všech přípustných označení. Ověřena
i jednoznačnost pomocných možností, nikoli pouze projekce řešení.

Původní autorův `pi-day-dlx.w` byl stažen, archivován, přeložen a spuštěn.
Reprodukuje přesně11351 možností na880+1216 položkách. Původní DLX2 dává
jediné řešení,19768 uzlů,134501157 vstupních a25252124 čistých hledacích mems.
To odpovídá tiskovým135Mμ a25Mμ. Všech100 rovnic, všech34 daných nebo
triviálně vynucených značek a celá shoda s dřívějším nezávislým řešením
Backtrack68 byly ověřeny. Dřívější originální stabilizační výpočet měl
6865501 mems, tedy uvedených7Mμ.

Nezjednodušená konstrukce po vynechání indikátorů i_vd s d>deg(v) má
1200+1831 položek:100 hodnot,1000 h a731 i. Počty možností jsou
H=53889,I=514,E=5468, celkem59871, tedy uvedených60tisíc.
Zadané značky již omezují přípustná d v H/I; jiné propagace se zde nepoužívají.
Obecný výraz pro E je1000+součet(deg(w)+1) přes všechny hrany v→w.

Vytištěné příklady H00,I00,E004 odpovídají ověřenému řešení:
λ(00)=3, viděná množina{4,7,9}, předchůdci01,03,05,70,80;
první jižní následník s hodnotou4 je50. Příslušné předchozí čtyři značky
nejsou4. Přesně123 dvojic šipek v téže řadě/sloupci ukazuje stejným směrem.
Obecná nerovnost je prostá inkluze obrazů množin:
N⁺(v)⊆N⁺(u) ⇒ množina viděných značek v je podmnožinou té pro u ⇒ λ(v)≤λ(u).
Dodatečná primární položka s dovolenými dvojicemi barev tento důsledek
vynutí. Matematická konstrukce, příklady i všechny uvedené počty jsou uzavřené.

## 103 — all-interval rows

Pracujeme s n≥2, jak je výslovně uvedeno v(b). Při formálním rozšíření
na n=1 má jednoprvková permutace prázdnou množinu intervalů; tvrzení(a)
o sudosti by mělo tuto triviální výjimku. Neoznačujeme to bez dalšího za
nový nález mimo zamýšlený rozsah hudební úlohy.

(a) Součet všech rozdílů je n(n−1)/2 modulo n. Lichá délka by dala
x_(n−1)=x_0, což pro permutaci n≥2 nejde. Pro n=2m koncový prvek je x_0+m.
(b) Položky j,p_t vynucují permutaci hodnot; d_k,q_t vynucují permutaci
intervalů a jejich pozic. Sdílené x_j připojí obě permutace správně.
Normalizace x_0=0 vybírá právě jednoho zástupce aditivní transpozice;
poslední prvek je nutně m. Znaky ≠ v podmínce vynechání možností byly
zkontrolovány vizuálně; OCR je někdy ztrácí.

`check_music103_104.py` porovnal pro všechna n=2..12 celé množiny původního
DLX2 s nezávislým C++ procházením permutací hodnot. Pro sudá n vycházejí
1,2,4,24,288,3856; pro lichá0. Každý uložený řádek má nezávisle ověřenou
permutaci hodnot i rozdílů. C++ větví přes nepoužité hodnoty, odmítá použitý
rozdíl a rezervuje nezbytný poslední prvek; nevynechá tedy žádné přípustné
řešení. Úplné seznamy do n14 jsou uložené binárně. Výčet skončil pro všechna
n=2..18; n14=89328, n16=2755968 a n18=103653120. Poslední běh skončil
2. listopadu v03:11:12 UTC, s14947359311 navštívenými uzly. Terminální
výstup, návratový kód0 a hashe programu i výsledků přijal samostatný
`check_puzzle_checkpoint.py`; znovu hledání nespouštěl. Nově nezávisle
zkontroloval i všech89328 uložených řad pro n14.

(c,d) Reverze změní rozdíly na opačné v opačném pořadí; násobení jednotkou c
je permutace hodnot i nenulových rozdílů. Q odřízne před jedinečným
intervalem m; vynechaný interval m nahradí obvodový rozdíl x_0−x_(n−1)=m.
RQ=QR dává přesně pořadí x_(k−1),...,x_0,x_(n−1),...,x_k. Operace R,Q
jsou involuce a komutují také s násobením c. Na třídách modulo aditivní
transpozici tvoří grupu řádu4φ(n); pro n2/4 může mít konkrétní řádek větší
stabilizátor.

### Nezávislý obecný důkaz klasifikace symetrií v(e)

Položme n=2m a x_0=0. Jednotka c je lichá. Pokud x≡cx^T pro netriviální
T∈{R,Q,QR}, vyvolává T na hodnotách afinní zobrazení t↦ct+a. Protože T²=1
a hodnoty proběhnou všechny zbytky, c²≡1 a(c+1)≡0 modulo n. Rovnice
(c−1)t=−a má buď0 řešení, nebo gcd(c−1,n) řešení; její řešení jsou právě
pevné hodnoty této afinní involuce. Násobení −c fixuje mezi zbytky přesně
gcd(c+1,n) prvků, násobení c přesně gcd(c−1,n).

R obrací indexy hodnot a nemá pevný index. Na n−1 intervalech má jediný
pevný index m, takže jediný pevný nenulový rozdíl při násobení −c je m.
Tedy gcd(c+1,n)=2. Z n|(c−1)(c+1) plyne m|(c−1), tedy c je1 nebo1+m.
Druhá možnost není jednotkou při lichém m; při sudém m má afinní mapa
t↦ct+m pevný bod t=1, což odporuje reverzi hodnot. Proto c=1.

Při symetrii Q musí být jedinečný vnitřní interval m na stejném místě
před a po Q, tedy k=n−k=m. Posun indexů o m nemá pevné body ani na
hodnotách, ani na zbývajících n−2 intervalech. Proto gcd(c−1,n)=2.
Z involuce plyne m|(c+1), tedy c=n−1 nebo m−1. Afinní posun je a=x_m,
nemá pevný bod, a proto a není sudé. Možnost c=m−1 by však z a(c+1)=0
vynucovala sudé a. Zbývá c=n−1.

Pro QR se index hodnoty i zobrazuje na k−1−i modulo n, index obvodového
intervalu j na k−j. Dvě výskyty intervalu m (vnitřní a obvodový) se vymění.
Je-li k liché, mají hodnoty dva pevné indexy a intervaly žádný. To dává
gcd(c−1,n)=gcd(c+1,n)=2; spolu s c²=1 z toho plyne n≤4. Pro n>4 tedy
k musí být sudé: hodnoty nemají pevný index, intervaly mají dva pevné
indexy, a gcd(c+1,n)=4. Při zápisu n=2^e s, s liché, nutně e≥2 a c≡1 mod s.
Jestliže e>2, pak v₂(c+1)=2 a v₂(c−1)=1; z c²=1 plyne e≤3.
Pro e=3 je gcd(c−1,n)=2s a z a(c+1)=0 plyne 2s|a, takže afinní mapa
má pevný bod — spor. Proto e=2, n≡4 mod8, c≡3 mod4 a c≡1 mod s.
Čínská věta o zbytcích dává c=1+n/2. To je přesně tvrzení knihy.

Symetrie cx bez R/Q vyžaduje c=1, neboť normalizace dává posun0 a řádek
obsahuje hodnotu1. Kdyby n>4 mělo dvě různé z uvedených tří symetrií,
jejich součin by v abelovské grupě dal třetí s koeficientem odporujícím
právě dokázané klasifikaci; rovnost by vyžadovala n=4. Stabilizátor má
tedy velikost1 nebo2 a orbity velikost4φ(n) nebo2φ(n).

Celé grupové působení a stabilizátory byly zkontrolovány pro každý řádek
do n12, včetně degenerací n2/4. Všechny vytištěné příklady n12 i n20
mají požadované rozdíly a symetrie. n12 má22 R-orbit,15 −Q-orbit a15
7QR-orbit; celkem267 orbit všech typů. Velké C++ počty fixovaných řádků
do n18 odpovídají uvedeným počtům orbit po dělení2φ(n). Pro n18 je
22464 R-pevných řad a16152 −Q-pevných řad, tedy1872 a1346 orbit.
Samostatná konečná kontrola afinních kongruencí do n1024 podpírá uvedený
obecný důkaz; nenahrazuje ho. Ověřila179728 přípustných afinních případů.

Notový zápis byl přečten z výřezu původního PDF: F4,E4,C5,A4,G5,D5,
Ab5,Db5,Eb5,Gb4,Bb4,B3. Jeho třídy výšek jsou přesně
8,7,3,0,10,5,11,4,6,9,1,2, tedy stejné jako vytištěná řada.

Otevřené zůstává ověření historických prvních výpočtů v původním Lehmerovi,
Gilbertovi a Morrisovi–Starrovi, hudební historie a přesné historické
benchmarky100Mμ/107Gμ/4.7Gμ/281Gμ. Hodnoty běhů vlastního C++ nejsou mems
Knuthovy implementace. Gilbertovu citaci189–198 potvrzuje autorův vlastní
seznam a Crossref; PDF původního článku se nepodařilo získat. DOI je
10.1137/1007035; dřívější odhad jiného DOI byl neúspěšný a není důkazem.
Nová citace AMM132(2025)94–96 je známé erratum; metadata potvrzují příslušný
oddíl89–99, plný text zůstal nepřístupný. Důkaz výše je nezávislý na něm.

## 104 — perfect rows

Pro prvočíslo p=n+1≥3 označme y_k=x_(k−1), k∈F_p^*.
Dokonalost po normalizaci x_0=0 znamená y_(kr)=y_k+c_r a c_r=y_r.
Proto r↦c_r je homomorfismus F_p^*→Z_n. Protože x je permutace,
jde o bijekci. Pro primitivní r je tedy c_r jednotkou modulo n;
existuje d s dc_r=1 a R=r^d splňuje R^(x_(k−1))=k modulo p.
To doplňuje implicitní zdůvodnění inverze c_r v knize.

Stejné dva sousední rozdíly by daly po umocnění R rovnost
(k+1)/k=(l+1)/l v F_p; po vynásobení kl získáme k=l. Všech n−1
rozdílů je proto různých a nenulových. Dále násobení indexu číslem
n=−1 modulo p prostě obrací pořadí, tedy x^(n)=x^R.

Obráceně diskrétní logaritmy v libovolné primitivní bázi R dávají dokonalou
řadu. Je jich právě φ(n) po normalizaci. Checker to ověřil pro všechna
prvočísla3..101; do n6 také přímo ve všech normalizovaných permutacích
a do n12 ve všech již úplně vyčíslených all-interval řadách. Vytištěný
příklad i dvanáct indexů pro r=5 jsou správně. Definiční přeformulování
ze15.9.2025 je známá úprava, nemění tento důkaz.
Matematická část je uzavřená, ale závěrečný odkaz na původní Lehmerův
a Gilbertův článek ještě není obsahově prověřený. Úloha104 proto zůstává
v úplném registru částečná, společně s touto přesně vymezenou mezerou.

## 105–107 — slova, obrázky a sudoku

Každá možnost představuje všechny buňky jedné přímočaré orientované
polohy slova; shodné barvy buněk jsou právě podmínkou slučitelnosti překryvu.
XCC proto přesně reprezentuje výběry poloh. Souřadnice se nevztahují na
torus a žádné slovo nepřechází okraj. Validator obrázků čte původní PDF
vektory:311 znaků a91 jednotlivých zakřivených obrysů v8 mřížkách.
Všechny obrysy mají stabilní příslušnost buněk pro tři výšky středu znaků;
všechny vytištěné polohy jsou členy úplných nativních množin řešení.
Typografické tečky jsou posunuté vůči základně písmen a sdružené PDF cesty
mohou obsahovat i rámeček další mřížky; checker tyto skutečnosti řeší
geometricky, nikoli opravováním dat podle očekávaného výsledku.

105: nativní DLX2 našel352 výběrů poloh bez podmínky počtu volných buněk.
Z nich40 má právě jednu volnou buňku; je to40 různých mřížek,5 tříd modulo
osm symetrií čtverce. Ostatních312 modelů pokrývá všech36 buněk, a nesplňuje
proto zadání. Z požadovaných40 modelů je24 souvislých a16 má dvě komponenty
grafu překryvů. To přesně odpovídá třem dobrým a dvěma nesouvislým obrázkům.
Pět vytištěných reprezentantů je navzájem neekvivalentních.

106: zdvojené hlavní položky a pomocná položka bránící opětovnému použití
téže polohy dávají256 modelů,32 označení dvou kopií pro každou z8 polohových
konfigurací. Nezávisle sestavený vstup původního DLX3 s násobností2 najde
přesně těchto8 konfigurací bez označení kopií. Výpočet měl23430242
hledacích a53977 vstupních mems, pod uvedenými24 miliony. Každá ze dvou
vytištěných mřížek má čtyři různé rotace a obě třídy jsou disjunktní.

107:729 sudoku možností má právě buňku,řádek/písmeno,sloupec/písmeno,
blok/písmeno a společnou barvu buňky. Vzorec pro blok v knize je ve
číslování od1 správný:3floor((i−1)/3)+ceil(j/3). K tomu všechny polohy
slov a původní autorův doplněk `dlx2-sharp.ch`.

Pro dvojici COMPUTER,CORPORATE je úplný výsledek UNSAT. Všech jedenáct
slov bez CORPORATE má16 modelů výběrů poloh,8 různých sudoku mřížek
a jedinou třídu modulo symetrie čtverce. Dva modely téže mřížky se liší
výhradně výběrem jednoho ze dvou výskytů slova ART. Nejde o různá sudoku.
Maximum11 je tedy doloženo horní mezí z neslučitelné dvojice a dolní mezí
konkrétního obrázku. Všech8 sudoku má nezávisle zkontrolováno27 jednotek.

Náš úplný běh107 měl6.369M vstupních+17.733M hledacích mems, ne uvedených
7.3M celkem. Pořadí možností, rozbití symetrie a hledání jediného zástupce
mohou cenu měnit; tento rozdíl není sám důkazem chyby. Přesný historický
benchmark a inspirace knihou Sudoku Masterpieces2010 zůstávají otevřené.
Také původní historické prameny k Ramosovi1966,Gibatovi1968 aOuelletovi1970
zatím nebyly přímo ověřeny; matematická kontrola105 není kontrola jejich historie.

`check_word_puzzles_sat.py` navíc spouští samostatné booleovské modely
s kardinalitními omezeními. Katalog poloh nezávisle rekonstruuje ze všech
uspořádaných dvojic koncových buněk. Blokování modelů ignoruje pomocné
proměnné i libovolná písmena v nevyužitých buňkách. Živé SAT běhy se
nepovažují za dokončené, dokud není uložen terminální záznam s vyčerpaným
hledáním a shodou celé množiny požadovaných modelů.

## Errata a hranice uzavření

`check_puzzle_errata.py` prohledal šest úplných aktuálních a historických
vrstev, včetně původních TeX souborů, a ověřil čtyři aktuální originály
proti Stanfordu. Tři současné úpravy: kurzíva v103(3.1.2023), formulace104
(15.9.2025), citace důkazu103(3.7.2025). Historické opravy103(e) z30.3.2022
jsou v4B již zapracované; starší PS naopak stále obsahuje koeficient5 místo7
a9 místo11 v ukázkách QR. Nejde o nové chyby nynějšího lokálního4B.
Rovněž označení(a) u104 bylo přidáno již16.12.2019.

Celý svazek není dokončen. Úplnost jednotlivých matematických převodů,
úplnost velkých výčtů, reprodukce benchmarků a historické citace se vedou
odděleně; definitivní stav příslušných úloh je v `full-review.json`.

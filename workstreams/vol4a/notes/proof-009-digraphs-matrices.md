# Grafy, matice a turnaje: str. 17–22, §7–54 až 62 a 68–69

6. listopadu 2026. Jednotlivé argumenty; bez matematického programu.
Sazba: images/file034.png až file039.png, zvlášť proof-file036.png;
zadání file057–058, odpověď proof-file539-540-1.png. OCR je navigace.
Odpovědi 63–67 mají již uzavřený rozsah v proof-008; neopakují se.

## Stromy, barvení a digrafy

Minimální souvislý podgraf spojující předepsané vrcholy nemá cyklus:
odstranění kterékoli hrany cyklu zachová souvislost a zmenší počet hran.
Je tedy stromem. Historickou pasáž o Heinenovi/Gaussovi nahrazuje známé
erratum all4a-pre, str. 17, 4. 3. 2013 (Gergonne 1811); primární článek
se zde znovu nedohledával.

Rozklad do nejvýše k nezávislých množin je ekvivalentní k-barvení
přiřazením čísla části. Podgraf zdědí barvení. C_n lze dvěma barvami
obarvit právě pro sudé n střídáním barev. Theorem B přebírá celý argument
z proof-007, úloha 48, včetně obecného pořadí objevování vrcholů.
K_m,n má mn hran, protože vybírá nezávisle oba konce; K_1,n je souvislý
a bez cyklu, tedy strom. Úplný multipartitní graf má všechny a pouze
mezitřídní hrany; obrázkové počty odpovídají této definici.

Čtyřbarevná věta a kvadratický algoritmus jsou explicitní externí vstupy.
Autorova stránka potvrzuje jejich přesné použití pro bezsmyčkové rovinné grafy:
https://thomas.math.gatech.edu/FC/fourcolor.html (otevřeno 6. 11. 2026).
Institucionální záznam potvrzuje autory, STOC 1996, str. 571–575 a
kvadratickou mez:
https://collaborate.princeton.edu/en/publications/efficiently-four-coloring-planar-graphs/
Důkaz reducibility ani programy čtyřbarevné věty se nereprodukovaly.
Původní články Appel–Haken–Koch a König ani datum Polya dopisu neověřeny;
nejde o mezeru v samostatně doloženém bipartitním argumentu.

Každý oblouk se započte právě jednou do součtu vstupních a jednou do
součtu výstupních stupňů; oba součty jsou m. Jednoduchý digraf má nejvýše
jeden oblouk na každý uspořádaný pár, včetně smyček; J_n má n² oblouků.
Orientované K, P, C mají v diagramu přesně příslušné tranzitivní,
následnické a cyklické orientace.

Obrázek 3: z původní sazby byly vypsány oblouky
1→0; 0→8,14,15,6,16,13; 8→14,3; 14→8; 15→6; 6→15;
16→3; 13→12; 4→5; 5→4; 10→11; 11→10.
Je jich 18 na 17 vrcholech. Ignorováním orientace dostáváme přesně
šest tištěných komponent; 2, 7, 9 jsou izolované.
Ukázkový sled 1→0→8→14→8→3 je platný. Historická shoda s románem
neověřena; známé opravy jmen Hector Willard / Cyrus Bethman z 23. 4. 2011
zohledněny bez nové karty.

Nejkratší orientovaný sled nemůže opakovat vrchol: uzavřený úsek lze
vyříznout. Zřetězením dvou cest a odstraněním opakování plyne trojúhelníková
nerovnost, také s nekonečnými vzdálenostmi. Náhrada neorientované hrany
dvojicí protilehlých oblouků dává bijekci orientovaných průchodů a zachová
vzdálenosti i stupeň jako vstupní/výstupní stupeň.
Smyčka dává dva oblouky a příspěvek 2 ke stupni. Multigraf (26) má
6 hran, stupně (3,3,6) a matici [[2,1,0],[1,0,2],[0,2,4]].
Všechny čtyři předchozí matice (27) přímo odpovídají definicím.

## Matice a reprezentace

(A²)_uv = Σ_w a_uw a_wv rozděluje sledy podle prostředního vrcholu;
indukce rozdělením u posledního oblouku dává totéž pro každé k≥0,
včetně A⁰=I a prázdného sledu. Pevné A²/A³ a čísla 12/18 přebírá
results/first-pass-sanity.json; žádné opakované násobení.
Přeznačení současně permutuje řádky a sloupce, tedy P^T A P.
Šest matic (30) odpovídá pořadím 123,132,213,231,312,321.
Různé diagonální hodnoty 2,0,4 vylučují netriviální stabilizátor,
takže jsou různé a vyčerpávají všech 3! možností.

Nechť N=n(n−1)/2 a U_n je počet neoznačených grafů. Každá třída má
nejvýše n! označení, takže U_n≥2^N/n!. Pro n>1 je nerovnost ostrá,
protože prázdný graf má pouze jedno označení a n!>1.
Pro libovolné prosté binární kódování je počet kódů délky nejvýše L
menší než 2^(L+1). Volba L=N−2n log₂ n dává podíl tak krátce
kódovatelných grafů nejvýše 2 n! n^(−2n)→0. Proto téměř všechny
potřebují Ω(n²) bitů, i při proměnné délce.

Pro náhodný označený graf má počet hran M binomické rozdělení
Bin(N,1/2). Z E exp(t(M−N/2))=cosh(t/2)^N≤exp(Nt²/8)
a Markovovy nerovnosti po minimalizaci plyne
P(|M−N/2|≥εN)≤2 exp(−2ε²N).
Nerovnost pro cosh plyne integrací tanh x≤x. Pro neoznačené grafy
je podíl výjimek nejvýše n!-krát větší, takže stále mizí například
pro ε²=2n log n/N. Výrok o přibližně N/2 hranách tedy platí v obou
běžných významech „téměř všechny“. Pro n=5·10⁹ je N/2≈6.25·10¹⁸;
průměrný stupeň 10⁴ dává n·10⁴/2=2.5·10¹³ hran.
Sociologické zobecnění o „real-life“ řídkosti je motivace, ne univerzální věta.

Primární gb_graph.w z již uloženého
audit-2026-10-31/sources/knuth-programs/sgb.tar.gz byl cíleně přečten:
Vertex má 2 ukazatele a 6 util, Arc má 2 ukazatele, long a 2 util,
Graph má ukazatel, 2 long, id[161], util_types[15], 2 Area a 6 util.
Při čtyřbajtových ukazatelích/long/util a odpovídajícím zarovnání jsou
velikosti 32,20,220 (Graph: 12+161+15+8+24). Nejde o tvrzení pro každý ABI.
Sekvenční vrcholy a propojené výstupní oblouky odpovídají primárnímu zdroji.

Průchod (31) navštíví každý uzel seznamu jednou, proto d je přesně
výstupní stupeň. Dvojice sousedních arc uzlů jsou vzájemní mates.
Ve (33), a mod 8=0 dává (a&4)−1=−1, takže maska vrátí 40 a adresa a+20;
a mod 8=4 dává masku 40&3=0 a adresu a−20.
Pro velikost 24 a první adresu dělitelnou 16 je analogicky maska
48&((a&8)−1), tedy 48 nebo 0, a posun ±24.
Pevné staré případy v first-pass-sanity se neopakovaly.
10¹²·3.6 ns=3600 s. Rovnice (34) je definice škálované pointer aritmetiky.
Známé zpřesnění „v's location“ místo „v“ z 29. 9. 2018 zohledněno.

## Úloha 54: certifikáty bez grafového censu

(a) Kódy se stejným prvním písmenem tvoří kliky. Všechny takové kliky
se připojí ke skupině A následujícími dvojicemi se stejným druhým písmenem
(v tomto pořadí lze přidávat nové skupiny):
AL–IL, IA–CA, ID–ND, NC–DC, AL–FL, IA–GA, IA–MA, MS–KS,
IA–LA, AR–OR, IA–PA, MI–RI, ID–SD, IN–TN, CT–UT, IA–VA, IA–WA.
Je tím pokryto všech 18 počátečních písmen ze seznamu 49 kódů.
Graf má jedinou komponentu. Je to hranový graf bipartitního grafu,
kde XY představuje hranu mezi oddělenými kopiemi počátečního X
a koncového Y; sdílení konce hrany je právě shoda na stejném místě.

(b) Uvažujme nejprve písmenový digraf, jehož oblouky jsou kódy.
Net­riviální silná komponenta písmen je
C={A,C,D,I,K,L,M,N,O,R,S,T,V}.
Z A do všech C vedou oblouky stromu
AR,RI,AL,ID,DC,CO,OK,KS,IN,NM,CT,NV;
zpět do A vedou RI,IA,LA,DC,CA,OR,KS,SC,NM,MA,TN,VA.
Všechny kódy s oběma písmeny v C proto tvoří jednu silnou komponentu
hranového digrafu: mezi XY a UV použij cestu Y→U uvnitř C.
Ze seznamu zbývají přesně zdroje FL,GA,PA,UT,WA,WI,WV, izolovaný WY
a sinky AZ,DE,KY,ME,NE,NH,NJ,NY,OH,TX.
Jejich nulové vstupní/výstupní stupně jsou přímým porovnáním se seznamem
počátečních/koncových písmen. Tím jsou prokázány všechny komponenty.

(c) Přidané kódy rozšíří písmenové jádro o H,P,W:
M→H→I, A→P→R a P→W→A. Proto se připojí právě původní
NH,OH,PA,WA,WI,WV; nové kódy uvnitř jádra jsou AA,AK,AP,AS,HI,MH,MP,PW,PR,VI.
Mimo něj přibudou GU→UT a zdroj FM, sink AE; WY se stane sinkem.
Všechny ostatní původní jednovrcholové komponenty zůstávají.
Známý bibliografický doplněk z 2012 a jeho oprava z 2022 byly zohledněny;
časopisecké stránky nebyly nezávisle otevřeny.

## Úlohy 55–62, 68–69

55: Z binom(N,2) všech párů odečteme disjunktní vnitrotřídní páry
Σ_i binom(n_i,2). Ekvivalentně e=Σ_{i<j} n_i n_j.

56: Paralelní neorientované hrany dávají opakované oblouky; smyčka dá
dva stejné smyčkové oblouky. Proto odvozený digraf je jednoduchý
právě tehdy, když multigraf nemá smyčky ani násobnost. J_n pro n>0
není odvozeným multigrafem, protože má lichou smyčkovou násobnost.

57: u→w←v je souvislý, ale nemá orientovanou cestu mezi u,v ani jedním
směrem. Silná souvislost je naopak přesně konečnost obou vzdáleností.

58: V konečné souvislé 2-regulární komponentě sledování hran bez
bezprostředního návratu uzavře cyklus. Žádný vrchol mimo cyklus se
nemůže připojit, aniž by vznikl stupeň≥3. Minimum délky je u grafu 3,
u multigrafu 1 (smyčka); délku 2 tvoří dvě paralelní hrany.

59(a): Indukcí najdi Hamiltonovu cestu po odstranění v_n. Vlož v_n
před první v_k s v_n→v_k; je-li k>1, minimalita dává v_(k−1)→v_n.
Není-li takové k, vlož na konec. Tím vznikne požadovaná cesta.

59(b): Díky symetrii přičtení konstanty modulo 5 stačí začátek 0.
Po 01 může následovat 2 nebo 3: 012 dává jen 01234, větev 013
uvízne přes 0134. Po 02 může následovat 3 nebo 4: vzniknou jen
02341 a 02413. Každý z pěti začátků má právě tři cesty, celkem 15.
„Cyclic shifts“ zde používáme jako cyklické přeznačení modulo 5,
nikoli jako rotaci pozic obecné neuzavřené cesty.
Szeleho obecná lichost počtu je explicitní externí vstup; katalog
https://real-j.mtak.hu/7300/ potvrzuje ročník 50 (1943) a příslušný článek.
Plný 216 MB sken nebyl stažen a přesné strany ani důkaz nebyly ověřeny.

59(c): Unikátní cesta v T vynutí unikátní cestu v T−v_n: každou cestu
menšího turnaje lze vložením rozšířit a po odstranění v_n ji obnovit.
Indukcí je menší turnaj tranzitivní. Zapiš b_i=1, když v_n→v_i,
jinak b_i=0; možnosti vložení odpovídají přechodům 0→1 v řadě
0,b_1,...,b_(n−1),1. Je jich 1 plus počet přechodů 1→0.
Jedinečnost tedy vynutí samé nuly následované samými jedničkami,
což rozšíří tranzitivní pořadí. Obrácená implikace je okamžitá.
Známé erratum z 28. 11. 2024 „up to isomorphism“ je aplikováno.

60: Pokud maximálně výstupní u nedosáhne v do dvou kroků, musí v→u
a v→x pro každý výstupní soused x vrcholu u. Tedy d⁺(v)≥d⁺(u)+1,
spor. Tvrzení i tištěný ekvivalentní argument s množinami platí.

61: Digraf se smyčkami 1→1,2→2 a obloukem 1→2 má pro k≥0 právě
k takových sledů: vyber krok jediného přechodu 1→2.
A=I+N, N²=0, takže A^k=I+kN pro všechna celá k, u záporných
s využitím (I+N)^−1=I−N. O sledech záporné délky se nic netvrdí.

62(a): Každý spanning permutation digraf má jedinou cílovou permutaci π;
pro ni lze vybrat konkrétní oblouky v ∏_i a_(i,π(i)) způsobech.
Součet je per A, i při násobných obloucích a smyčkách.
(b): Cyklus délky l má znaménko (−1)^(l−1), proto sign π=(−1)^(n−k).
Determinant tedy odčítá liché od sudých. Historický Hararyho odkaz neověřen.

68: Přeznačení tvoří akci S_n na maticích. Vlákno každé výsledné matice
je jedna množina P·Aut(G) velikosti s, takže různých matic je n!/s.

69: Vynuluj všechny IDEG. Při jediném průchodu každého výstupního seznamu
inkrementuj ODEG zdroje a IDEG cíle. Každý oblouk včetně smyček se
započte právě jednou na obě místa; čas O(m+n).

## Meze tohoto bloku

Konkrétní matematické argumenty výše jsou uzavřeny. Primární historické
citace, které nebyly rychle ověřeny, jsou explicitně přeskočené.
Datové počty a generátory z konce str. 23 navazují v proof-010;
žádný zde uvedený obecný důkaz není důkazem jejich historických dat.

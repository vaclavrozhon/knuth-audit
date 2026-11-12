# Důkladná kontrola: druhá sada úloh §5-10 až25

S. 6–10, odpovědi 586–591. Pokračování notes/chapter5-proof-01-09.md.
Jednotlivé výsledky jsou v proof-audit.json. Existující C0001/C0002
a pátá mocninová identita z intro-targeted-checks se přebírají bez
opakování. Jeden nový cílený běh ověřil čtvrtou mocninovou identitu,
nice15, bez hledání. Další níže uvedené důkazy jsou ruční.

## Úlohy 10–16: soubory a permutace

10. Po seřazení tvoří každá hodnota souvislý interval. Počet různých
    slov je proto počet změn mezi sousedy plus1, pokud soubor není
    prázdný. Zahazování opakované hodnoty už při slučování zachová
    přesně množinu různých slov.
11. Při průchodu vzestupným souborem informačních formulářů ukazatel
    na daňové formuláře nikdy nemusí zpět. K_i<K nemůže odpovídat
    nynějšímu ani budoucímu formuláři, proto jej lze přeskočit.
    Při K_i>K chybí daňový formulář; při rovnosti máme správnou osobu.
    Sentinel zajistí konec přeskočení i za poslední osobou. Účetní
    podmínka „information is reflected“ musí znamenat zohlednění
    všech příjmů, např. agregaci celé skupiny podle osoby a typu
    příjmu; samotné opakované porovnání každé částky s celkovým
    přiznáním by nestačilo a kniha takový zjednodušený test nepředepisuje.
12. Klíč (j,i) přesně určuje cílové pořadí transpozice; obecně totéž
    funguje s jednoznačně vypočteným cílovým indexem. Zvláštní páskový
    postup po k slučovacích průchodech obsahuje střídavě na dvou
    páskách bloky nejvýše2^k původních řádků, uvnitř bloků po sloupcích.
    Sloučení sousedních bloků prokládá odpovídající sloupce a zdvojnásobí
    velikost bloku. Neúplný poslední blok se prostě doplní jen existujícími
    řádky. Po ceil(lg n) sloučeních je blok jediný. Počítáme také první
    rozdělení řádků: ceil(lg1000)+1=11 průchodů, podle známého errata.
    Klíče se nemusí zapisovat, protože indexy bloků/sloupců určují pořadí
    synchronního čtení. Stačí čtyři pásky a konstantní řídicí paměť.
13. Nezávislé stejně rozdělené spojité náhodné klíče mají shody s
    pravděpodobností0. Všech N! relativních pořadí má stejnou pravděpodobnost
    díky symetrii indexů, a tedy pravděpodobnost1/N!. Totéž platí pro
    rovnoměrné klíče bez opakování z konečné abecedy dostatečné velikosti.
    Pouhé slovo „random“ zde musí zahrnovat tuto výměnnost, ne libovolně
    různá rozdělení pro různé záznamy.

    Alternativní nezávislé hodnoty b_i rovnoměrné v0,…,N−i tvoří N!
    stejně pravděpodobných inverzních tabulek. Bijection: při i=N,…,1
    vlož i do pořadí větších prvků tak, aby před ním bylo právě b_i
    větších prvků. Předepsané číslo je v přípustném intervalu; výsledná
    permutace jednoznačně vrací b_i. Tím je uniformita úplně doložena.

    Odkazovaný páskový převod §5.1.1-5 lze dokázat bez numerické tabulky:
    řetězec [m₁,n₁]… značí m₁ prázdných míst, n₁, m₂ prázdných míst,
    n₂,… a nekonečný prázdný ocas. Operace α∘β vyplní prázdná místa α
    symboly i mezerami β. Asociativita plyne z toho, že zbývající mezery
    jsou právě mezery β uvnitř mezer α. První symbol je z α pro m≤m′,
    přičemž m′ klesne o m; pro m>m′ je z β a m klesne o m′+1.
    To jsou přesně obě větve vytištěné rekurze. Každá větev vypíše
    jeden symbol, takže cena je lineární v součtu délek. Vyvážené
    slučování potřebuje ceil(lg N) průchodů a O(N log N) operací.
    Součin [b₁,1]∘…∘[b_N,N] postupně obsazuje (b_i+1)-ní volné místo;
    po N obsazeních jsou první N místa plná a mezery nulové. Tento
    obecný důkaz lze později převzít pro §5.1.1-5; jeho konkrétní
    devítiprvkový příklad zde znovu nepočítáme.
14. Tabulka, která znaku přiřadí jeho pořadí v cílové abecedě, je
    izomorfismem obou lineárních uspořádání. První odlišný znak proto
    rozhodne stejně jako na cílovém stroji. Pro předpočítané klíče lze
    použít stejně dlouhé kódy a koncový symbol nižší než všechny znaky,
    takže se zachová i pravidlo kratšího prefixu. Při porovnání za běhu
    se převede jen prefix po první rozdíl; test rovnosti znaků může
    převodu shodného prefixu předejít. Univerzální výkonové vítězství
    jedné varianty není tvrzeno.
15. Přímé pole počítadel má po zpracování prvních j osob invariant
    count[s]=počet z těchto osob narozených ve státě s. Jediné zvýšení
    správného počítadla invariant zachová. Malý počet států se do
    paměti vejde. Je-li kategorií příliš mnoho, třídění a počítání
    souvislých skupin je korektní náhrada.
16. Každý výskyt identifikátoru převedeme na (identifikátor, řádek,
    pozice). Slovník se seznamy výskytů nebo externí třídění těchto
    záznamů vytvoří pro každý identifikátor přesný index. Identifikace
    tokenů je práce vstupního lexeru; tvrzení neobchází syntaxi jazyka.
    Paměťová varianta závisí na počtu výskytů; externí varianta používá
    pouze paměť třídicího procesu.

## Úloha 17: pomocné knihovní klíče

Ručně přidělený klíč umožňuje převést libovolná daná katalogová pravidla
na běžné lexikografické porovnání. Přidání původních dat za terminátor
odliší různé karty se stejným pomocným klíčem. To není automatický důkaz
správnosti práce knihovníka ani historických pravidel ALA.

U tištěné tabulky na588 byla porovnána každá sousední dvojice; rozhoduje
již viditelný prefix. Potřebné pořadí znaků je mezera < písmena < číslice
(např. MIX) a číslice0<…<9. Dvouznakové mezery0,…,8 dávají uvedenou
prioritu typů hranic. Mezi jmennými větvemi BROWN rozhodují postupně
J versus JOHN, terminátor versus popis, MATHEMATICIAN versus OF,
písmena versus čtyřciferný rok, roky1715<1761<1810 a oddělovače2<3<8.
Pro DEN rozhoduje2<7<8; pro DIX2<8 a HUIT<NEUVIEME. Ve zbytku
rozhodují běžné první odlišné znaky, zejména I␣ před IA, LABOR␣ před
LABOUR, MACCARTHY před MACHINE před MACMAHON a SAINT␣ před SAINTE.
Ostatní sousední prefixy jsou přímo abecedně vzestupné.

Nulou doplněné čtyřciferné nezáporné roky mají lexikografické pořadí
shodné s číselným pro0–9999; prosté prodloužení na10000 by tuto
vlastnost porušilo. Proto technická poznámka o formátu roku odpovídá
zvolenému kódu. Akcenty, překlady číslovek, odhadované životní letopočty
a historická katalogová pravidla zůstávají bibliografickou výjimkou.
Zohledněny známé změny německého názvu a COOK BOOK; nejde o nálezy.

## Úlohy 18–20: vyhledávání shod

18. Každé řešení šestých mocnin se rozdělí na dvě trojice s hodnotami
    u⁶+v⁶+w⁶ a z⁶−x⁶−y⁶. Rovnost implikuje shodný zbytek modulo m;
    po seřazení lze spojit stejné zbytky a ověřit původní celá čísla.
    Modulární shoda není postačující, proto je poslední přesný test
    nezbytný a v odpovědi výslovně uvedený. Nerovnosti u≤v≤w a
    x≤y≤z neztrácejí žádné řešení: levé členy lze přerovnat a každá
    kladná levá proměnná musí být menší než z. Tříděné záznamy nesou
    trojice jako satelit, aby bylo možné závěrečný test provést.

    Pátá mocninová identita z textu je už uzavřena v
    results/intro-targeted-checks.json a nebyla spuštěna znovu.
    Výrok o nekonečně mnoha řešeních čtvrtých mocnin má nový přesný
    svědek95800⁴+217519⁴+414560⁴=422481⁴=31858749840007945920321.
    Libovolné kladné celočíselné násobení všech čtyř proměnných dává
    další řešení. Výsledek jediného krátkého výpočtu je v
    results/fourth-power-identity.json. Historická atribuce tohoto
    tvrzení Elkiesovi a silnější otázka primitivních řešení tím nejsou
    nezávisle ověřeny. Žádné šesté mocniny se nehledaly.
19. Komplement 30bitového x je (2³⁰−1)−x, takže úloha je součet c.
    Pro vzestupné různé hodnoty a krajní i<j: je-li x_i+x_j<c,
    x_i nemá partnera mezi zbývajícími j′≤j; při >c analogicky x_j
    nemá partnera. Při rovnosti je partner každého z nich jednoznačný,
    takže lze oba vyřadit. Varianta j−i klesá a žádný pár se neztratí.
    Dvě opačně seřazené kopie realizují krajní ukazatele sekvenčně.
    Případ i=j v zobecněné odpovědi připouští opakované použití stejné
    hodnoty; původní c je liché, takže v zadání nikdy nenastane.

    Původní pomocný klíč podle parity funguje pro liché c: oba členy
    komplementárního páru se zobrazí na lichý člen. Známá novější
    verze klíče je max(x,c−x) a funguje obecně; shoda klíčů dvou
    různých hodnot je ekvivalentní jejich součtu c.
    Pro max součtu≤c uchovávej nejlepší přípustný součet a při jeho
    přípustnosti zvyš i, jinak sniž j. Pro min{x_i+y_j>t} začni i=1,
    j=n: při >t zapiš kandidáta a sniž j, jinak zvyš i. Vyřazený
    řádek/sloupec nemůže skrývat lepší přípustnou hodnotu. Cena
    následného průchodu je O(N), resp. O(m+n).
20a. x_i XOR x_j má právě tolik jedniček, kolik je rozdílných bitů.
    y AND(y−1) smaže nejnižší jedničku; pro y=0 zůstane0. Po dvou
    smazáních je výsledek0 právě pro vzdálenost≤2. Počet dvojic
    binom(1000,2)=499500 už byl aritmeticky ověřen, neopakuje se.
20b. Koule poloměru1 kolem dvou binárních slov se protínají právě pro
    vzdálenost≤2: nutnost je trojúhelníková nerovnost, postačitelnost
    dává střed nebo přepnutí jednoho ze dvou odlišných bitů. Každá
    koule má31 slov, celkem31000 záznamů. Je nutné nést index původu
    a v případě požadavku na seznam bez opakování deduplikovat výstupní
    páry; jeden pár může mít více společných sousedů. Jde o doplnění
    obecně popsaného hledání shod, ne o tvrzení, že jediný společný
    soused je unikátní.
20c. Nejvýše dva různé bity nemohou zasáhnout všechny tři desetibitové
    bloky. Přiřazení páru prvnímu shodnému bloku zaručí úplnost i
    neopakování mezi třemi případy. Potom přímý XOR test odstraní
    falešné kandidáty. Pro nezávislá rovnoměrná slova má shoda bloku
    pravděpodobnost2^−10, takže očekávaný počet v každém případě je
    nejvýše499500/1024<500. Dodatečné vyloučení předchozích bloků
    pravděpodobnost pouze snižuje.

## Úlohy 21–23: kanonizace a kliky

21. Seřazené posloupnosti písmen jsou shodné právě tehdy, když jsou
    shodné všechny četnosti písmen. Proto je to úplný anagramový klíč.
    Uvedené skupiny mají společné multisety ACERT, CELRU, DORWY,
    AEPRS a AELST; poslední výčet má7+12+3=22 navzájem různých
    posloupností AELST. Lexikální existence těchto slov, priority,
    superlativy a nevypsané rozšíření na14 slov nebyly znovu ověřeny.

    Součet náhodných písmenových konstant je invariant permutace.
    Po shodě hashe je stále nutný přesný test/kontrola celé kolizní
    skupiny; samotný hash anagramy úplně necharakterizuje. Pro novější
    m=2^floor(2lg N) a dvě různé pětipísmenné četnostní tabulky je
    alespoň jeden rozdílový koeficient d nenulový a |d|≤5. Podmíněně
    na ostatních konstantách má rovnice d h=c modulo m nejvýše
    gcd(d,m)≤4 řešení, tedy pravděpodobnost kolize≤4/m. Jelikož
    m>N²/2, očekávaný počet falešně kolidujících dvojic je O(1).
    Skutečné anagramy se samozřejmě nadále musí zpracovat celé.
    Obecný polynomiální hash multiword klíče je stejný pro stejné
    klíče, ale ani on není důkazem rovnosti bez sekundárního testu.
    Slovo „faster“ závisí na ceně operací a implementaci třídění;
    odkaz na dvouprůchodový interní radix sort není zde nezávisle
    převeden do omezeného páskového modelu, tento výkonový rozsah
    zůstává partial. Matematická korektnost filtru je uzavřena.
22. Izomorfismus zachovává stupně vrcholů, proto i multiset dvojic
    (in-degree,out-degree). Zachovává také konce každého oblouku,
    tedy multiset čtveřic jejich stupňů. Komponenty se zobrazují na
    komponenty; seřazený seznam jejich invariantů je opět invariant.
    Nutná podmínka se správně netvrdí jako postačující.

    Úplný invariant volného stromu lze zkonstruovat bez citovaného
    článku: opakovaně odstraň všechny listy až do1 nebo2 vrcholů.
    Tato množina je zachována každým izomorfismem. Při jednom centru
    strom zakořeň v něm, při dvou nahraď jejich hranu novým kořenem
    s dvěma dětmi a označ tento případ. Kód vrcholu je pár závorek
    kolem lexikograficky seřazených kódů dětí. Indukce podle velikosti
    podstromu dokazuje ekvivalenci shody kódů a zakořeněného izomorfismu.
    Tím vzniká úplný invariant; lineární čas konkrétní citované
    implementace zde není tvrzen ani potřeba.
23. Při společném prefixu a₁,…,a_(k−2) dvě (k−1)-kliky zaručují
    všechny potřebné hrany kromě(b,c). Test této poslední hrany je
    tedy nutný a postačující. Každá k-klika má jediný prefix nejmenších
    k−2 vrcholů a poslední dva b<c, takže vznikne přesně jednou.
    Pro k=2 je základ vstupní seznam hran. Počet podklik n-kliky
    je binom(n,k), protože každá k-podmnožina je klika.
    Protipříklad k neformálnímu tvrzení o malém výstupu zůstává
    převzatý C0001, candidate. Jeho konstrukce ani výpočty se neopakovaly.

## Úloha 24: invariant a konkrétní počet průchodů

Pro krok t má F páry(x_i,x_(i+t)) pro i≤N−t, H je jeho kopie
seřazená podle první složky a G nese označený konec(i,x_i), i>N−t.
Klíče H a G dohromady rozdělují všech N jmen. Pro každý druhý klíč
x′ z F proto existuje právě jeden shodný záznam buď v H, nebo v G.
V H vznikne(x_i,x_(i+2t)); v G se známým pořadím y=i+t vznikne
(y−t,x_i)=(i,x_i). Tři monotónní ukazatele přeskočí jen menší klíče;
ukazatel F nemůže zůstat bez protějšku. Vyčerpaný soubor se chápe
jako sentinel+∞. Sloučení starého G s novými označenými prvky dává
suffix délky min(2t,N), tedy indukční invariant dalšího kroku.
Po zdvojení až k t≥N je F prázdný a G obsahuje pořadí všech osob.
Na s.591 jsou ve všech příslušných testech opravdu čárky x′;
nejde o chybu OCR považovanou za nález.

Konkrétní mez pro N=3000000 v běžném modelu dvouslovných záznamů:
vezmi RAM pro1000 záznamů (2000 slov plus malá režie). Vytvoření
počátečních setříděných běhů stojí jeden průchod; nejvýše3000 běhů
sloučíme dvoucestně v dalších12 průchodech. Každé třídění tedy≤13.
Čtyři pracovní pásky na třídění dovolují současně uchovat dva další
soubory: celkem šest jednotek, jak dovoluje zadání.

Úvodní příprava t=2 stojí jednu kopii, dvě třídění a jeden join:
1+2·13+1=28 průchodů. Každý další krok t=2,4,…,2²¹ stojí nejvýše
tři třídění (H,F,G′), jednu kopii, jeden třícestný join a jedno
sloučení označených souborů: 3·13+3=42. Je21 takových kroků,
protože2²¹<3000000<2²². Závěrečné třídění G stojí≤13. Celkem
28+21·42+13=923<1000. Průchod je synchronní přečtení/zapsání
zpracovávaných dat, stejně jako u předchozího páskového merge sortu.
Není to přesný optimalizovaný počet a žádný běh s miliony položek
nebyl proveden. Pro víceslovná jména se velikost běhů mění s jejich
reprezentací; číselná mez je doložena pro standardní klíčový model.

## Úloha 25: diskrétní logaritmus

Primitivní kořen má řád p−1, proto exponenty1,…,p−1 dávají přesně
všechny nenulové zbytky. Pro m=ceil(sqrt p) lze každý požadovaný
n≤p−1<m² zapsat n=mn₁+n₂, 0≤n₁,n₂<m. Dvě tabulky
a^(mn₁) a b a^(−n₂) proto mají shodu. Každá shoda naopak dává
správný exponent modulo p−1; zbytek0 se v požadovaném intervalu
reprezentuje p−1. Generování po sobě jdoucích mocnin je lineární
v m, s předvýpočtem a^m a a^−1. Porovnávací třídění stojí
O(m log m), následný merge O(m), tedy O(sqrt p log p) modulárních
jednotkových operací. Jde o uvedenou mez v p, nikoli instančně
optimální mez pro malé neznámé n.

Pro liché prvočíslo je a^((p−1)/2) jediný prvek řádu2, tedy−1.
Proto b^((p−1)/2)=(-1)^n a paritu určí binární umocnění v O(log p)
modulárních operacích. Doplňující chybný modul již uzavřel C0002,
který se přebírá bez nového testu.

Konstrukce po cifrách: známe-li n₀=n mod D a další prvočinitel q
s Dq|(p−1), polož c=b a^(−n₀). Pak
c^((p−1)/(Dq))=(a^((p−1)/q))^((n−n₀)/D).
Pravý základ má řád q, jeho q-členná tabulka určí následující cifru
modulo q. Nastav n₀←n₀+D·cifra, D←Dq. Po všech faktorech máme
n mod(p−1). Tabulky opakovaných prvočísel lze používat opakovaně;
při malém největším q je tedy počet potřebných operací malý oproti p.

Odstavec o Pollardově metodě používá externí algoritmus a teorii
náhodných zobrazení. Očekávaný O(sqrt p) čas s malou pamětí nebyl
z tohoto odstavce nezávisle dokázán; stejnou mezerou zůstává odkaz
na asymptoticky rychlejší metody §4.5.4-46. Jsou to matematické
partial záznamy, nikoli pouhá bibliografická výjimka ani nové nálezy.

Další aktivní důkladný kurzor: §5.1.1 Inversions, s.11 / file22.
Nejstarší otevřené modelové mezery zůstávají na5; další dílčí meze
u21 a25 i kandidát C0001 jsou výslovně vedeny v proof-audit.json.

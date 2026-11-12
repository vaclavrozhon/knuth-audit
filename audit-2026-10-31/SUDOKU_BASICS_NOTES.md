# Sudoku: DLX43–50 a hlavní strany74–77

Kontrola 1. listopadu2026. Zadání str.128, odpovědi424–426, hlavní text74–77.
Původní PDF má offset20; odpověď425 je tedy strana445 souboru. Autorův
Pre-Fascicle5C má odpovědi43–50 na128–130 a zadání na64. Jeho stránka129
je135. stranou konvertovaného souboru. Originály knihy ani PS nejsou upravené.

Vzorce, úplné množiny řešení a všechny kandidátní diagramy jsou prověřeny.
Nové F112 a F113 jsou drobné opravy odpovědí48–49. Úlohy45–50 mají dokončený
průchod;43–44 ponechávám částečné kvůli přesným stránkovým citacím, které
nebyly zpřístupněny. Hlavní text74–77 je také částečný: jeho matematické
příklady nejsou dokladem všech historických údajů a osobních benchmarků.

## Zdroje a kontrolní programy

`check_sudoku_basics.py` čte souřadnice všech číslic přímo z PDF přes
`pdftotext -bbox`. Pozice a slova jsou archivovány v `results/sudoku_basics/`;
nejde o přepis posunutých řádků prostého OCR. Původní stránky74–76 a425 byly
také zobrazeny. Všech243 hodnot v(28), všech81 polí každého zadání(29) a všech
405 buněk pěti kandidátních diagramů(31)–(33),48(a,b) je porovnáno.
Z těchto405 buněk404 souhlasí a jedna je F112.

Nezávislý řešič používá masky obsazení řádků, sloupců a boxů a volí buňku
s nejmenším počtem hodnot. `check_sudoku_native.py` konstruuje plný model
přesného pokrytí a spouští nezměněný, dříve ověřený Knuthův DLX1. Porovnává
celé množiny dokončených čtverců, nikoli pouze jejich počty. Vstupy, úplné
modely, profily a hashe binárky zůstávají uložené.

Další programy:

- `check_sudoku_matching.py`: všechny podmnožiny všech27 grafů jednotek a9
  grafů hodnot; nezávislý výčet všech perfektních párování permutacemi.
- `check_sudoku_diagram.py`: všech15 hran skutečného vektorového obrázku
  v PDF a všech14 hran staršího PS.
- `check_sudoku_pi.py`: racionální interval pro π a dva úplné řešiče
  publikované kruhové varianty s22 nápovědami a dvěma diagonálami.
- `check_sudoku_sources.py`: původní de Ruiterův puzzle a všech81 číslic
  novinového čtverce z1895, jehož fotografii zveřejnil Boyer.

Vlastní chyby při přípravě nebyly vydávány za chyby knihy: první přepis
izotopie omylem obrátil výstupní permutaci místo druhého argumentu; opravena
podle původního vzorce. Pomocná kontrola sousední pevné3 původně měla
sloupec6 místo5. Samotná dokazovaná pevná5 je stále správně v(5,4).
Zpočátku selhalo také čtení dočasného objektu pikepdf a předpoklad pouhých
translací u PS; výsledný parser zachovává vlastníka PDF a skládá celé matice.

##43: vzorce a izotopie

Píšeme `i=3i1+i0`, `j=3j1+j0`, výsledné číslice zmenšíme o1. Tři vytištěné
formule dávají všech243 hodnot přesně. V(a) je pro pevný řádek posun modulo9;
pro sloupec permutace číslic indexu. V každém boxu proměnné `i0,j0` vyčerpají
všech devět zbytků. V(b) je výstup dvojice `i0+j1, i1+j0` modulo3, což je
bijekce při změně každé řady, sloupce i boxu. V(c) je pro sloupec matice
koeficientů `[[1,1],[-1,1]]` nad F3 invertibilní; pro řádek a box je
bijektivita také přímá. Zkontrolováno všech27 jednotek každého čtverce.

Správné čtení izotopie je
`c'[i,j] = π(b'[π(i),π^(-1)(j)])`, kde `π(a,b)=(a,a+b)` modulo3.
Po substituci dostáváme dvojici
`(i0+i1+j1, i0-i1+j0)`, jak požaduje(c). Všech81 párů souhlasí.

[Boyerův původní web](http://www.multimagie.com/English/SudokuAncestors.htm)
poskytuje francouzské přílohy z2006 včetně fotografií novin. Zobrazeno původní
zadání v *La France*,6.7.1895, a řešení21.7.1895. Žádá součty v řádcích,
sloupcích a diagonálách; podmínku boxů nezmiňuje. Všech81 číslic starého
řešení po přeuspořádání řádků `[4,2,6,5,0,7,3,1,8]` dává přesně(28c).
To je přímá kontrola příbuznosti vzoru, nikoli tvrzení, že jde o obvyklou
symetrii libovolného sudoku zachovávající pásy.

Crossref vydavatelská metadata potvrzují *Mathematical Intelligencer*29(2),
59–63,2007, DOI[10.1007/BF02986207](https://doi.org/10.1007/BF02986207).
Přesnou citovanou stranu63 se nepodařilo otevřít; tento detail zůstává otevřený.

##44: číslice π a dva historické příklady

Machinova identita a střídavé řady pro arctan dávají přesný racionální interval
obsahující π. Oba konce mají stejnou celočíselnou část po násobení10^32:
`314159265358979323846264338327950`. Třiatřicátá číslice včetně úvodní3 je0,
která do standardního sudoku nepatří. Předchozích32 číslic přesně souhlasí
s postupným čtením nápověd(29a).

Starý odkaz PuzzlePicnic se změnil na aplikaci. Její veřejná data pro
[puzzle346](https://data.puzzlepicnic.com/puzzles/346.json) potvrzují autora
Johan a datum7.7.2007. Jeho32 nápověd má tentýž řetězec π a jediné řešení.
Rozmístění je jiné než v(29a); kniha netvrdí totožnost. Prvenství mezi všemi
historickými autory tím samostatně neprokazuji.

[Pythagoras, recenze z1.2.2017](https://www.pyth.eu/exotische-sudoku-s)
reprodukuje kruhovou úlohu Thoena a van de Weteringa. Všech22 nápověd jsem
opsal z obrázku po směru hodinových ručiček a porovnal s π. Přidání dvou
diagonálních podmínek dává přesně jedno řešení ve dvou nezávislých modelech.
Původní stranu144 knihy *Exotische Sudoku’s*(2016) nemáme, takže tuto
stránkovou citaci neoznačuji za přímo ověřenou. Samotný matematický příklad
a vazba na uvedené autory jsou doložené reprodukcí v časopisu.

##45–47: všechny vynucené tahy

Úloha45: všech49 tahů při prioritě nejmenšího `ij` souhlasí s celým vytištěným
seznamem. Výsledek je jediným úplným řešením(29a). Úloha46: všech17 singleton
seznamů přesného pokrytí odpovídá tisku, včetně dvou naked položek `p44,p84`.
Podle slovního rozlišení jsou zbývající15 hidden; odpověď záměrně uvádí
všechny položky délky1, což není nový nález.

Úloha47: po dosazení3 do(2,3) je seznam přesně
`r13,c03,b03,b24,b49,b69`; poslední tři jsou singletony už před tímto tahem.
Při pořadí `p,r,c,b` vznikne po16 vynucených dosazeních přesně celý diagram(33).
Žádná jeho buňka se neliší od přepočtu přímých zákazů.

## F112: chybná pevná hodnota v48(a)

V odpovědi48(a), str.425, na průsečíku řádku označeného5 a hodnoty označené5
je vytištěno **6**. Má být **4**. Tabulka uvádí sloupce, v nichž se hodnota
může nacházet. Už zadání(29b) má `s[5,4]=5`; sloupec4 se objeví stejně
v diagramech(32) a(33). Není k tomu potřeba žádné řešení, heuristika ani
interpretace malých kandidátních číslic. Hodnota5 se tedy nemůže nacházet
v jiném sloupci téhož řádku.

Obě tabulky mají celkem162 buněk. Všech ostatních161 souhlasí s přesným
převodem původního diagramu(33). Stejnou6 má autorův PS na str.129.
PDF i PS byly zobrazeny. Nízká závažnost: lokální číselný překlep v diagramu.

##49 a F113: párování a konzistence indexů

V jednom řádku jsou zbývající buňky vrcholyU a zbývající hodnoty vrcholyV.
Každé dokončení sudoku indukuje perfektní párování. Pro `S⊂U` s
`|N(S)|=|S|` musí párování spotřebovat celé `N(S)`, a proto žádná hrana
z `U\S` do `N(S)` nemůže být použita. To dokazuje eliminace naked skupiny.
Hidden případ je duální. Pokud `T⊂V`, `|N(T)|=|T|=q` a existuje perfektní
párování, pak `U\N(T)` má právě `r−q` vrcholů a sousedství přesně `V\T`.
Opačný směr je stejný. Při čtení „only q“ jako „nejvýše q“ lze sousedství
doplnit do q prvků a důkaz existence komplementární skupiny funguje i bez
předpokladu splnitelnosti; rozpor s Hallovou podmínkou pak rovnou znamená
neřešitelnost. Nezaměňuji tuto konvenci za novou chybu49(b).

Při doslovném odstranění položek v úvodu49 zůstanou mimo zvolený řádek
samostatné jednoznačkové komponenty `pij`. Vynechání těchto nezávislých
komponent je implicitní, když text mluví o dvouznačkových možnostech
zvoleného řádku. Matematický argument se týká právě této komponenty.

**F113 je jeden záznam dvou indexových překlepů v odpovědi49(a,b):**

1. Sloupcová konstrukce má používat hranu **u_i—v_k**, když možnost obsahuje
   `p_(i,j0)c_(j0,k)`. Vytištěné `u_j` má index, který v této možnosti není
   volnou souřadnicí. Například pro sloupec0 a kandidáta(2,0,2) je levý vrchol
   u2. Ztotožnění j se zvoleným sloupcem by všechny buňky zkolabovalo do u0.
2. V49(b) má být **r−q**, jak je definováno v zadání, místo vytištěného
   **n−q**. U zobrazeného grafu je r=5 a q=2, takže ne-sousedé jsou přesně
   tři: u3,u8,u1. Samotný argument je po sjednocení symbolu správný.

Navíc je vhodné ve vzorci pro box důsledně psát `3(x0 mod3)`, kde je nyní
`3(x mod3)`. V této zbylé komponentě lze x=x0 dovodit z položky bx0k;
proto tento redakční detail nepočítám jako další samostatnou chybu.
Opravené souřadnice `i=3⌊x0/3⌋+⌊j/3⌋`, `c=3(x0 mod3)+(j mod3)` jsou
ověřeny pro všech81 dvojic x0,j. PDF425 i PS129 mají stejné znění.

Úplný výčet27 jednotkových grafů dává přesně tři netriviální naked skupiny:

| Jednotka | Skupina | Zakázané možnosti (ijk) |
|---|---|---|
| řádek4 | u3,u8 | 411,417,421,427,471 |
| řádek4 | u1,u3,u8 | předchozí a424 |
| box4 | u0,u3,u6 | 341,346,347,351,356,357 |

Žádné další skupiny v řádcích, sloupcích nebo boxech nejsou; hidden skupiny
jsou přesně komplementy. Ve všech9 grafech řádky–sloupce při pevné hodnotě
je jediná další skupina pro9: řádky1,5 s možnostmi sloupců7,8; ta vyloučí
079,279. Všech1472 perfektních párování jednotek a749 párování hodnotových
grafů nezávisle potvrzuje bezpečnost vyřazení. Úplné sudoku řešení neobsahuje
žádnou odstraněnou možnost. „Pointing pair“ pro4 a8 v boxu4 přesně vyloučí
314,324,328,364,368,378.

E027 je známá oprava F5.126/49 z9.8.2021: přidat hranu u7—v1.
Přímý rozbor vektorových souřadnic všech hran potvrzuje15 správných hran
v našem PDF128 a14 ve starším PS64, kterému chybí právě tato hrana.
Nejde tedy o nový nález v našem vydání.

Citace Gould2005 potvrzena [katalogem vydavatele Collins](https://collins.co.uk/products/9780007207329);
Mephamův titul a rok přímo [jeho původním tutorialem](https://www.sudoku.org.uk/pdf/Solving_Sudoku.pdf)
čteným webovým nástrojem, i když stažení přes běžné HTTP selhalo.
[Lulu, první vydání Berthiera](https://www.lulu.com/shop/denis-berthier/pattern-based-constraint-satisfaction-and-logic-puzzles/paperback/product-19zegke5.html)
potvrzuje2012 a popsaný rozsah teorie. Novější vydání nejsou důvodem měnit
historickou citaci v knize. Jejich úplný obsah zde nebyl auditován.

##50: přesně36 možností

(29c) má přesně dvě dokončení v nezávislém souřadnicovém hledání i původním
DLX1. Liší se jen záměnou7 a8 na18 buňkách. Přidaná nápověda v jiných
buňkách buď zachová obě řešení, nebo je vyloučí obě. V každé z18 odlišných
buněk lze zvolit7 nebo8, a vždy zůstane jediné dokončení. To dává36 úloh,
spojených záměnou číslic do18 párů. Všech36 instancí bylo navíc samostatně
spuštěno v původním DLX1 a celé jediné řešení porovnáno s nezávislým modelem.

## Hlavní text74–77: ověřená část a zbytek

Bijekce s přesným pokrytím plyne ze čtyř značek každé trojice(i,j,k):
jedna hodnota v buňce a jeden výskyt hodnoty v řádku, sloupci, boxu.
Je729 možností a324 položek. Konzistentní nápovědy pokrývají po čtyřech
různých položkách; po32 nápovědách tedy zůstává196 položek a přímý výčet
dává146 možností. Ověřeny i první/poslední možnosti a příklady r02,c01
na str.75. Při změně r,c,b na sekundární zůstane každá řada devíti obsazených
buněk injekcí do devíti hodnot, tedy permutací; množina řešení se nezmění.

| Případ | Řešení | Uzly původního DLX1 | Inicializační memy | Hledací memy |
|---|---:|---:|---:|---:|
|29a|1|50|90267|18380|
|29b|1|89|215568|47042|
|29c|2|129|236239|63611|
|29b, jen p primární|1|41877|215570|13647672|

Všech89/129/41877 uzlů souhlasí s knihou. Všech šest vytištěných řádků
průběhu řešení29b souhlasí doslova, včetně větvení7→8 a následných vynucení.
Hledacích47K je v souladu s přibližnými50K; inicializační údaj kolem250K
není našimi215568 přesně reprodukován. Může zahrnovat jinou verzi kódu
nebo přípravu; tento rozdíl není sám důkaz chyby knihy.

[McGuire–Tugemann–Civario, arXiv1201.0749v2](https://arxiv.org/abs/1201.0749)
je archivovaný primární zdroj věty o nejméně17 nápovědách. Obsahuje
5 472 730 538 tříd a3,6sekundy na čtverec pro konečnou verzi programu.
V§8.4 uvádí dokončení výpočtů v prosinci2011; autorská stránka oznamuje
výsledek1.1.2012. Kniha říká „completed in2012“; rozdíl mezi koncem výpočtu
a dokončením/oznámením projektu ponechávám k redakčnímu dořešení, nikoli
jako nový potvrzený matematický nález. Údaj asi16000 přeživších podmnožin
nebyl v získaném textu nalezen. Celý miliardový certifikát zde nebyl znovu
počítán. Nezávislé formální potvrzení takového rozsahu netvrdím.

Rovněž nejsou uzavřeny: původní Dell1979/6, přesná historie Nikoli1984,
původní Hayesův citát a autorova neuvedená sada běžných sudoku, z níž
pochází70%,10% a maximum282. Strany74–77 proto zůstávají `partial`.

## Errata, omezení a pokračování

`results/sudoku_basics/errata-check.json` obsahuje nové vzdálené SHA256
kontroly všech čtyř relevantních oficiálních souborů a prohledaná místa
včetně historických posunů, názvů diagramů, singles, sousedství a odpovědí.
Obsah errat je proti archivu beze změny. Nalezené opravy stejných čísel
v jiných sekcích nejsou opravami48–49 zDLX; správné E027 je výslovně odlišeno.

F112/F113 jsou doložené v našich PDF+PS, nikoli v fyzickém výtisku.
Nenalezení veřejného errata nezaručuje prvenství ani odměnu. Žádný nový
emailový návrh nevznikl. Další souvislý blok začínáDLX51; hlavní otevřené
citace43–44 a historie74–77 zůstávají výslovně v registru.

# Dancing Links: základy, úlohy 1–13

Rozsah: hlavní text str. 65–69, zadání 124–125, odpovědi 416–418.
Zadání, odpovědi, tabulky a obrázky byly zobrazeny v původním PDF.
Jádro algoritmu X pracuje s neprázdnými možnostmi; u rozšíření o sekundární
položky musí každá možnost obsahovat primární položku, jak výslovně stanoví
str. 71. Duplicitní možnosti se rozlišují svými pořadovými čísly.

## Úlohy 1–2: proč jsou odkazy obnovitelné

Při odstranění uzlu k zůstávají jeho vlastní L(k),R(k) beze změny. Jsou to
sousedé k mezi dosud přítomnými prvky. Pozdější odstraňování se už žádného
pole odstraněného uzlu nedotkne. V opačném pořadí vložený binární vyhledávací
strom obsahuje právě tyto později odstraněné prvky; hranice hledací cesty
jsou jeho největší předek menší než k a nejmenší předek větší než k.
Pokud takový předek chybí, hranici zastupuje hlava 0. To dokazuje 1(a).

Ze dvojic hranic se strom obnoví jednoznačně: kořen má hranice (0,0),
kořeny levého a pravého intervalu mají příslušné dvě krajní hranice a
postup se rekurzivně opakuje. Každý tvar binárního stromu je dosažitelný
například odstraněním v postorderu. Třídy tedy odpovídají Catalanovým
stromům: C_0=1, C_n=sum C_i C_(n−1−i)=binom(2n,n)/(n+1).

Relace k≺L(k), k≺R(k), s vynecháním hlavy 0, vytvářejí právě uspořádání
„potomek před předkem“. Každý bezprostřední rodič je jednou z těchto hranic
a všechny hranice jsou předkové. Počet permutací ve třídě proto je počet
lineárních rozšíření tohoto uspořádání. Je jediný právě pro řetězový strom;
pro n≥1 dává n−1 nezávislých voleb levého/pravého dítěte 2^(n−1) takových
stromů. Prázdný strom se obsluhuje zvlášť a má jednu prázdnou permutaci.

Při obnovování ve stejném pořadí je indukční invariant
L(a_k)=a_k−1, R(a_k)=(a_k+1) mod(n+1) těsně před obnovou a_k.
Pokud soused a_k−1 nebyl odstraněn dříve, levý odkaz byl správný už při
odstranění a_k. Jinak dřívější obnova tohoto souseda nastavila L(a_k)
správně; jiná předchozí obnova ho podle indukce nepřepíše. Pravá strana
je symetrická. Každý obnovený uzel tak zapíše dvě správná sousední pole.
Nakonec je celý seznam původní, i když mezistavy nemusejí být platné.
L(1),R(n) zůstávají 0, ostatní pole se při úplné obnově přepíší právě jednou.
Pro částečné odstranění se důkaz použije na jednotlivé souvislé intervaly
odstraněných prvků s neodstraněnými hranicemi. Libovolné jiné pořadí fungovat
nemusí: po odstranění 1,2,3 a obnově 1,3,2 zůstane R(0)=3 místo 1.

[check_linked_foundations.py](check_linked_foundations.py) prošel všech
**46 233 permutací pro n=1..8**, ověřil každé pole vůči skutečně sestavenému
vyhledávacímu stromu a obě pořadí obnovy. Pro všech 2055 vzniklých stromů
nezávislý bitový DP spočítal lineární rozšíření. Dále prošlo **16 072**
částečných mazacích posloupností pro n=0..7. Stavové vektory obrázků
(3)–(4) odpovídají mazání 3,2,4,1 a zobrazeným šipkám.

Příklad LEO/PISCES a AQUARIUS/hlava byl ověřen rekonstrukcí uvedeného
pořadí vložení i přímo v [obr. 10 svazku 3](images/vol3-fig10-p427.png),
str. 427, DjVu pořadí 438. Cizí pracovní větev ani zdrojová kniha se neměnily.
Opravený důkaz X. Lou z historického errata 24.10.2020 už náš 4B obsahuje.

## Úlohy 3–5: lineární rovnice, grafy a dualita

V (5)/(6) je 16 jedniček a jediné řešení tvoří možnosti 1,4,5.
Odečtení první a čtvrté rovnice zadání 3 dává x6=0; postupně pak
x1=1,x3=0,x5=1,x2=0,x4=1. Sedmá kontrola souhlasí, tedy řešení je
jediné i bez omezení na bity. Samostatná racionální eliminace potvrzuje
hodnost 6. Trojúhelníkové tři rovnice v odpovědi dávají jediné řešení
(1/2,1/2,1/2), takže lineární řešitelnost sama nezaručuje exact cover.
Obecná hodnost nejvýše n ponechává při m>n alespoň m−n volných proměnných;
jejich binaritu prostá eliminace nevyřeší. Praktická poznámka v odpovědi
není tvrzením o nepoužitelnosti všech metod celočíselného programování.

Po volbě adg zbývají položky b,c,e,f a možnosti ce,bcf. Obě jsou nutné,
ale překrývají se v c, takže (7) nemá řešení. Po volbě adf zbývají
b,c,e,g a disjunktní možnosti ce,bg, tedy (8) řešení má.

V incidenční matici grafu musí být pro každou hranu uv přesně jeden
z u,v vybrán. Vybrané a nevybrané vrcholy proto tvoří bipartici a opačně.
V každé souvislé komponentě jsou dvě volby; zahrnuje to i izolovaný
vrchol, který lze nezávisle vybrat nebo vynechat. Celkem je 2^k řešení,
pokud je graf bipartitní, a žádné jinak. Vyčerpávající kontrola všech
**1100 jednoduchých grafů s nejvýše pěti vrcholy**, včetně izolátů a
prázdného grafu, souhlasí. Výkonový dovětek řeší zvlášť C017 níže.

Transpozice incidenční matice převádí volbu hyperhran na volbu vrcholů.
Podmínka součtu 1 v každém sloupci se po transpozici stane podmínkou
„každou původní hyperhranu trefit právě jednou“. Pro obyčejné pokrytí
s nerovností ≥1 vzniká analogicky hitting set. Ověřeno i všech **689**
0–1 matic rozměrů nejvýše 3×3, včetně prázdných rozměrů a hyperhran.

## Úlohy 6–13 a celý algoritmus X

Uložení tvoří N hlavičkových uzlů, L výskytů položek a M+1 spacerů,
celkem Z=N+L+M+1. Horizontální záznamy jsou samostatné: Tabulka 1 má
hlavu 0 a N záznamů, rozšířená inicializace v odpovědi 8 přidává pomocnou
hlavu sekundárního seznamu N+1. Adresní prostory záznamů a uzlů se neslévají.
Spacer 23 následuje za čtvrtou možností a jeho DLINK=25 je poslední uzel
páté možnosti. To vysvětluje obě hodnoty úlohy 7.

I1–I2 vytvářejí dvě oddělené kružnice: 0,1,...,N1 a N+1,N1+1,...,N.
Když sekundární položky chybějí, pomocná hlava N+1 ukazuje sama na sebe.
I3 vytvoří prázdné sloupce. Každý krok I4 připojí nový výskyt na konec
příslušného sloupce a zvýší LEN. I5 propojí krajní uzly možnosti přes
okolní spacery a uloží její záporné pořadové číslo. Duplicitní názvy,
neznámé položky a opakování položky v jedné možnosti jsou chybné vstupy,
které má I1/I4 podle odpovědi odmítnout.

Invariant algoritmu X: aktivní primární hlavičky jsou dosud nepokryté
položky a sloupce nepokrytých položek obsahují právě možnosti disjunktní
od dosavadních voleb. Cover(i) ponechá vlastní sloupec i jako neměnný
seznam větví a odstraní ostatní výskyty možností obsahujících i.
Po volbě možnosti O se pokrytím jejích zbývajících položek získá právě
reziduální problém. Každé úplné řešení obsahuje právě jednu možnost pro
zvolenou primární položku i, takže větve tvoří disjunktní a úplný rozklad
řešení. Prázdný primární seznam má jedinou prázdnou dostavbu; prázdný
zvolený sloupec nemá žádnou. Unhide/uncover a X6 vracejí operace v přesně
opačném pořadí, a proto obnoví všechny odkazy i délky. To dokazuje
správnost rekurzivní (9) i explicitních kroků X1–X8 na platných vstupech.

Průchod MRV porovnává jen ostré zlepšení, proto při shodě délky zachová
nejmenší aktivní číslo položky. V úloze 10 je LEN≤M; přirážka M pro
nepreferovanou položku délky>1 ji posune za všechny preferované položky,
zatímco nucené či prázdné sloupce zůstanou vpředu. To přesně realizuje
zadanou sharp preference bez změny množiny řešení.

Odpověď 12 prochází neměnné uzly možnosti od x cyklicky přes koncový
spacer, takže vytiskne přesnou rotaci začínající TOP(x). Lineární průchod
aktuálního sloupce vrátí jeho pořadí a LEN, nebo ohlásí nepřítomnost.
Pro x=21 dostaneme d,f,a a pozici 2 ze 3. Barevný dovětek je správný při
invariantu str.89–90: kladný COLOR je vlastní barva, záporný COLOR označuje
barvu uloženou v hlavičce; nula netiskne příponu. Tím není automaticky
ověřen celý algoritmus C. Odpověď 13 spolehlivě najde následující záporný
spacer, tedy pořadové číslo i začátek zvolené možnosti.

[spacer_algorithm_x.py](spacer_algorithm_x.py) implementuje skutečná
pořadí I1–I5 a X1–X8, odděleně od dřívějšího modelu s vodorovnými odkazy.
[check_spacer_algorithm_x.py](check_spacer_algorithm_x.py) porovnal obě
vytištěné tabulky: **111 definovaných položek v každé, celkem 222**, včetně
sedmi názvů, bez nedefinovaných pomlček. První X7 nastává pro i=e, l=2,
x0=12,x1=16, přesně podle odpovědi 11. Zobrazený diagram (10) má stejné
uzly, spacery a svislá pořadí jako počáteční tabulka.

Celkem **1878 případů × 3 politiky = 5634 úplných běhů** souhlasí s nezávislou
kontrolou všech podmnožin možností. Jde o1806 různých vstupních rozložení;
náhodná část záměrně připouští opakování malých případů.
Obsahují primární i sekundární položky,
duplicitní možnosti, různá pořadí položek v možnosti a prázdné sloupce.
Prošlo 22 675 přesných obnov celého stavu po cover/uncover, 34 314 kontrol
reziduálních sloupců a 123 964 popisů uzlů. Výsledky obou programů jsou
v [foundations.json](results/dancing_links/foundations.json) a
[spacer-verified.json](results/dancing_links/spacer-verified.json).

## C017 — neformální „quickly“ v odpovědi 4

Klasifikace grafů a počty řešení výše jsou správné. Samotný algoritmus X
však nemusí neexistenci řešení odhalit rychle. Vezměme k disjunktních hran
a další komponentu tvořenou trojúhelníkem. Položky jsou nejdříve samostatné
hrany, potom tři hrany trojúhelníka; možnosti jsou incidenční množiny vrcholů.
Graf má 2k+3 vrcholů a k+3 hran, není bipartitní a nemá žádné řešení.

Každá samostatná hrana má dva totožné jednopoložkové řádky, jeden pro
každý koncový vrchol. MRV s obvyklou remízou podle pořadí nejprve rozvětví
všech k komponent, až potom zjistí konflikt v trojúhelníku. Trojúhelník
má tři uzly stromu a každá další předřazená hrana mění N na 1+2N.
Celkově tedy **N_k=2^(k+2)−1**, s profilem 1,2,...,2^(k+1).
Oba nezávislé datové modely to potvrdily pro k=0..9:
[check_incidence_runtime.py](check_incidence_runtime.py),
[incidence-runtime.json](results/dancing_links/incidence-runtime.json).

Tato věta je stejně vytištěna v [PDF416](images/vol4b-p416.png) a
[PS120](images/fasc5c-foundations-p120.png). Relevantní errata neobsahují
opravu. Protože „quickly“ není formální polynomiální mez, vedeme C017 jako
**candidate**, nikoli jednoznačně potvrzené erratum. Možné upřesnění by
uvádělo předchozí rozklad na komponenty nebo výslovně lineární test
bipartitnosti. Samotná úloha 4 zůstává kvůli tomuto dovětku částečná.

## Publikované opravy a rozsah uzavření

E022 zahrnuje dvě již vydané drobné úpravy: na str.68 se 16.12.2022
zpřesnilo, že i je číslo pokrývané položky; na str.69 se 17.11.2024
doplnila deklarace globálních N,Z,i,j,l,p. Nejde o nové nálezy.
Historické opravy odpovědi 2 (24.10.2020) a výstupu odpovědi 12
(27.3.2020 a 30.7.2021) už naše kniha obsahuje. Audit je používá.
Podklady a kontrolní součty: [errata-check.json](results/dancing_links/errata-check.json).

Celé úlohy 1–3 a 5–13 jsou nyní `reviewed`. Úloha 4 zůstává `partial`
pro C017 a úloha 14 má samostatný rozbor. Hlavní str.66–69 a odpověď417
jsou uzavřené. Epigrafy na65/416 a další obsah zadání124–125 či odpovědi418
zůstávají výslovně otevřené; tyto celé stránky se za uzavřené nepočítají.

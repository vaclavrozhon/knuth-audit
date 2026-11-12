# Souvislý průchod §2.3.5 — 5. listopadu 2026

X0979. Přímo přečteny všechny části oddílu na 408–423 a 601–605,
včetně všech 12 úloh, obrázků, tabulek a všech kroků algoritmů.
Přezkoušeny tři obecné důkazové poznámky, celý garbage_collection.py
a garbage_collection_mix.py, výsledky starších testů a následné
pramenné kontroly. Staré rozsáhlé testy se neopakovaly.
Nové tři malé vstupy nice 15 odhalují opomenutí v odpovědi 7:
C0096. Hlavní text zůstává partial pouze kvůli citátu C0072;
úlohy 7/8/9/12 jsou uzavřeny s uvedenými bibliografickými výjimkami.

## C0096: neodstraněné přiřazení do neexistujícího pole

Zadání 7 na 422 dovoluje pouze MARK, ALINK a BLINK, výslovně
bez ATOM. Odpověď na 603 přikazuje smazat E2/E3 a přiřazení
ATOM(P)←1 v E4, přidat MARK(P)←1 v E5 a zaměnit dva testy
ATOM v E6 za testy MARK. Původní E6 na 419 má vedle testů také
přiřazení ATOM(Q)←0 v levé návratové větvi. Jeho odstranění
v seznamu úprav chybí. Rovnost v testu a přiřazovací šipka
jsou na obou původních obrazech dobře rozlišitelné.

Nejmenší svědek je strom A s levým listem B; obě pravé hrany
a levá hrana B jsou NULL. Všechna MARK jsou zpočátku 0.
E1 nastaví T=NULL,P=A; E4 převrátí levou hranu A a přejde do B.
B přes E4/E5 nastaví svůj MARK=1 a dospěje do E6.
Tam Q=A a MARK(A)=0, takže po nahrazení testu následuje
ponechané přiřazení ATOM(A)←0. Zadání takové pole nemá.
Jednouzlový strom ani samotná pravá hrana tuto větev nespustí.

check_floyd_literal_edits.py zachovává všechna výslovně zadaná
nahrazení a třídu se sloty jen pro tři dovolená pole. U levé
hrany nastane právě uvedený zakázaný zápis; kontrolní singleton
a pravá hrana doběhnou. Stávající mark_floyd, který již navíc
tento zápis vypouští, na všech třech vstupech obnoví oba odkazy
a nastaví všechny značky. Trasy i SHA256 jsou uložené v
results/sequential-floyd-literal-edits.json.

Oprava: doplnit odstranění ATOM(Q)←0 v E6. Žádná změna
zamýšlené metody není nutná. Je možné rozumně domyslet, že
všechny zápisy do odstraněného pole mají zmizet, ale vytištěný
seznam jednotlivých úprav tento krok neobsahuje. Jde o drobnou
neúplnost specifikace, nikoli o protipříklad správnosti Floydovy
opravené metody. Proto confirmed-low, s přesnou lokací pouze 603.
Strany 419 a 422 obsahují správný výchozí algoritmus a zadání.

Dřívější 15 017 testů a obecný důkaz se týkají zamýšlené varianty
s tímto dodatečným vypuštěním. Neověřily doslovnou úplnost
tištěného seznamu změn. X0458 i původní poznámky mají tento
rozsah nyní výslovně upřesněn; výsledky testů se nepřepisují.
Čtyři současné vrstvy errat nemají příslušnou opravu. Prohlédnuty
všechny záznamy dotčených stran i tematické výskyty Floyd/ATOM/E6.
Veřejné hledání nedalo použitelný doklad další opravy; není
důkazem prvenství. Fyzický výtisk ani pozdější dotisk neověřen.

## Reprezentace a hlavní algoritmy

Abstraktní List je konečný orientovaný graf s uspořádanými
výstupními hranami, rozlišeným kořenem a atomy/prázdnými Listy.
Cyklus a sdílení jsou přípustné. Opačná orientace proti dřívější
definici stromu je v odpovědi 1 správně uvedena. Hlavička zachová
identitu prázdného seznamu i po vyjmutí první položky.
Zkontrolovány všechny hrany příkladu L,N, 14 řádků tabulky 8
a rozdíl devíti položek proti pěti hlavičkám plus devíti položkám.
T=0/1/>1, REF a konec NULL/hlavička jsou ve všech formátech odlišeny.

Počítání referencí musí zahrnout vnější kořeny. Konečný nedosažitelný
acyklický zbytek má zdroj s počtem nula; indukcí se odstraní celý.
Cyklus se samými kladnými počty může zůstat. Odložené vracení
ve SLIP odpovídá přímo doloženému původnímu článku v X0802.

A používá známé K1←min(K1,BLINK(K)), nikoli původní chybné K.
Např. root=3, BLINK(3)=2, BLINK(2)=1, uzel1 atom a ALINK všude
NULL: při prvním průchodu se 2 označí pozdě, chybné přiřazení
nezmění K1=4 a 1 zůstane neoznačen. Oprava zajistí nový průchod
od 2. Invariant všech nevyřízených značek od K1 a konečný počet
nových značek dokazují A/A3'; mez O((n+1)M), obvykle O(nM).
B označuje před vložením, takže každý dosažitelný uzel má
nejvýše jedno nové vložení; seznam počátečních kořenů je další náklad.

C má efektivní kapacitu H−1; vypadlá položka je zachycena minimem K1.
Každý čekající označený uzel je ve frontě nebo na adrese ≥K1.
To dokazuje úplnost také pro H=1. Doporučení H=50 je praktická
heuristika, nikoli záruka pro každou vstupní strukturu.
D ukládá zásobník do REF hlaviček, nikoli do atomických dat.
Každý řetězec položek se projde jednou, typ cíle určuje zacházení.
Kořen musí ukazovat na hlavičku; vnitřní ukazatele jsou výslovně
zmíněný další problém. Obnova původního pracovního REF se neslibuje.

E: levý rámec uchovává staré T v ALINK a má ATOM=1; pravý
v BLINK s ATOM=0. Skutečné atomy nejsou rámci. Silná indukce
s již označenými bariérami dává přesné značky, P=P0 a obnovu
všech polí i při cyklech a sebeodkazech. Čas je lineární.
Všech 14 stavů P/T obrázku 39 souhlasí. Přenesení typů na hrany
vyžaduje uchovat řídicí bit; samotná atomická data se nečtou
jako adresy. Vyhrazení nízkého bitu předpokládá zarovnání.
Heuristická zrychlení a historické „fastest known“ nejsou
univerzální časové nerovnosti nad libovolným strojem.

Náklad c1*N+c2*M dělený počtem získaných buněk M−N dává
(c1*rho+c2)/(1−rho), rho=N/M. Dosazení 3/4 a 1/4 souhlasí;
rho=1 žádnou volnou buňku nedává. Slovní poměr k „garbage“
je známá chyba na 421. Kvalitativní závěry závisejí na modelu
nákladů; nepředstíráme nové měření historického počítače.

## Všech dvanáct úloh

1–3: grafová definice výše; obvyklé stromové nitě nestačí
jednoznačně vracet sdílený podlist; obecný důkaz E má výslovné
bariéry a nulové větve. Odkaz na 2.3.4.2-25 správně nabízí
incidenční reprezentaci; její vlastní hlavičková chyba je C0055.

4: všech 42 instrukcí MIX přezkoušeno. MARK je znaménko,
ATOM první byte, odkazy 2:3 a 4:5, X=−1. JANP testuje dříve
načtené slovo. Zvláštní +0 je správně pouze označeno, protože
oba odkazy jsou NULL; kniha tuto optimalizaci vylučuje z času.
Pro neatomický kořen t1+t2=n−1 dává součet instrukcí
23n+3+15t1+11t2+3a−5b = 34n+4t1+3a−5b−8.
Samotný atom má čas10u mimo deklarovanou doménu n>0.
Starých 12 728 běhů se neopakovalo.

5–6: S rozděluje nově označené uzly mezi přímý levý průchod,
čekající pravé cíle a při přeplnění vnitřní E. Vnější R zůstává,
vnitřní T se vrátí na NULL; bariéry neztrácejí čekající práci.
Funguje N=0, prostor je ≤N, čas lineární. Plný Schorr–Waite
včetně dříve chybějící503 dokládá hybrid. c2*M je sken celé paměti.

7: po vypuštění zbylého zápisu ATOM se MARK nastavuje až po
levé větvi. MARK=0/1 rozliší levý/pravý rámec. V acyklickém
grafu nelze znovu vstoupit do aktivního neoznačeného předka;
sdílení je bezpečné, obecné cykly nejsou zaručeny. Viz C0096.

8: F obrací LINK datového slova, návrat najde vlastní označenou
hlavičku; SIZE se nemění. G ukládá zásobník do SIZE a obnoví
velikost rozdílem adres. Kniha výslovně předpokládá, že SIZE
pojme ukazatel. V obou případech SIZE=0 funguje; datové MARK
zůstávají nulové, žádný cizí označený datový sentinel nevzniká.
Každé datové slovo se projde nejvýše konstantněkrát.

9: H používá výslovné sentinely 0 a M+1, páruje levé díry
s pravými živými buňkami a zaznamená jediný forwarding odkaz.
Po překřížení je K počet živých. Staré živé adresy ≤K zůstaly,
adresy >K mají cíl v prefixu; jeden překlad postačí.
Atomická data se nepřekládají. Vnější kořeny přeloží volající;
zadání žádá pole uzlů. Odkaz 2.5-33 již přímo ověřen.

10: Z vyžaduje explicitní hlavičky s REF=0, přímé řetězce
a dost disjunktní volné paměti. Staré REF uchovává kopii,
REF nové hlavičky další starou hlavičku ve frontě.
Nastavení před sledováním podlistu ukončuje i cykly.
Z6/Z7 ukončí frontu a vynulují pracovní REF na obou stranách;
zdroj i sdílení jsou obnoveny. Příklad kopíruje 14 strukturálních
buněk; atomické hodnoty lze sdílet. Varování před D v průběhu
neúplné kopie je správné. Plný Robson1977 dokládá druhou citaci.

11: konečná fronta dvojic podlistů testuje bisimulaci rozvinutí,
nikoli izomorfismus fyzických grafů. Nejvýše l1*l2 dvojic,
nesoulad má konečnou cestu; uzavřená relace po skončení dokazuje
shodu všech konečných cest. Příklad AB vyžaduje CF,EF a DG,
jak uvádí odpověď; nadbytečná závorka v B je známá chyba.

12: znovu přezkoušena vlastní úplná třífázová konstrukce.
Bariéra shade při každém zápisu cíle chrání i rozpracovaný šedý uzel.
Během sweepu se staré černé barvy nemažou, nové alokace jsou černé,
nově vrácené buňky zůstávají nepřístupné ve FREE. Samostatný reset
neprovádí uvolnění a končí s bílými barvami. Konstantní kořeny,
omezený počet změn/alokací za operaci a žádné skryté oživování
odpadlých ukazatelů jsou výslovné předpoklady.
Cyklus má ≤cM+r kroků, rezerva d*ceil((cM+r)/q)+d stačí při
q krocích sběrače za operaci. L≤M−2N a nejvýše N nových buněk
dávají zase ≥N volných; bez rezervy není slib nepřetržitého běhu.
To není doslovné prokládání původního E s měnícími se odkazy.
Tištěná odpověď detail dosažitelnosti výslovně vynechává;
vlastní doplnění neznamená novou knižní chybu.

## Prameny, errata a mapa stran

Staré mezery uzavřené dalšími přímými kontrolami:
Weizenbaum1963 včetně programové přílohy končí544, nikoli536;
Wiseman–Hiles338–346 a Hansen499–507 jsou celé doloženy;
Schorr–Waite501–506 včetně503; Robson431–433;
Steele1975 a jeho oprava1976; Wadler1976 a Griesův dopis1977.
Tuto práci dokumentují příslušné root-review poznámky;
její rozsah se zde nepovyšuje na novou úplnou četbu cizích článků.
Relevantní přečtené části Deutsch–Bobrow, Cohen, Dijkstra a
autorův HTML Baker zůstávají přesně omezené v původní evidenci.
Steeleova chybná historická implementace není novou chybou
Knutha, který ji nepřepisuje. Vlastní bariérový důkaz se jí netýká.

Podle uživatelského pokynu se samostatně přeskakuje:
- Přesný kalendář obou objevů roku1965; přijatý rozhovor dokládá
  Deutschovu nezávislost, ne všechny datované detaily.
- Osobní atribuce Floydovi(7), Deutschovi(8), Edwardsovi(9)
  a Minskému(12); Minskyho memo1963 řeší kopírování a není
  nezávislým dokladem konkrétní rady o real-time spolupráci.
- Plný Thorelli BIT12(1972),555–568; je doložen jen abstract.
  Umístění citace po F nepřipisuje Thorellimu přesně variantu G.
- Kolace časopiseckého Friedman–Wise1979 s přečteným plným TR;
  Bakerova původní časopisecká sazba proti dostupnému autorovu HTML.
Tyto výjimky nejsou důkaz historických tvrzení.

C0072 zůstává candidate-low: originál1894 má opačné pořadí
dvou slov než citát422. Autorizovaná varianta či redakční
adaptace není vyloučena; nepodepsaný článek sám nedokládá autora.
Pozitivní textový rozpor se neschovává za bibliografické přeskočení.
Celá stránka422 i hlavní text proto zůstávají partial.

Čerstvý výpis čtyř vrstev zachycuje 10 různých známých oprav
a sousední obsah společných stran. X0464 mapuje skutečné
původní obsahové vady jen na415(A2),421(poměr a dva rozsahy
citovaných článků),423(závorka). Gramatika411, typografie415,
velké L418 a sazba Solution603 netvoří další matematické vady.
408 konvexita patří historii stromů, 605 B3' následujícímu §2.4.
C0096 ani C0072 mezi opravami nalezeny nebyly.

Celé408–421,423 a601–604 mají teď stránkový záznam reviewed,
422 je partial kvůli C0072. Na605 je přečtena odpověď12;
zbytek §2.4 teprve následuje. Barvy nálezů mají přednost před
pokrytím:603 červená C0096,422 oranžová C0072. Pokračuje424.

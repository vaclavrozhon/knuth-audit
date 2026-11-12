# Souvislý průchod §3.2.2: další metody

6. listopadu 2026, V2-X0091–X0092. Přečteny původní strany 26–40
a odpovědi 551–559 proti důkazům, zdrojovým programům a všem řadám
errat. Inventář: 37 původních úloh a přidaná úloha 38. Strany 26 a 551
jsou tím dokončeny i za předchozí sekci. Na 559 zbývají odpovědi §3.3.1.
Na 36 zůstává odložená kontrola kryptografické redukce z §3.5F; stránka
proto ještě nemá úplné matematické pokrytí.

## Přijatá matematika a algoritmy

Kvadratické kritérium z úlohy 8 znovu porovnáno s originálem: nutnost
plyne z projekcí a neprostosti kvadratického polynomu nad lichým tělesem,
dostatečnost z prvního zvednutí modulo p² a následujícího p-násobného
růstu. Zvláštní podmínka modulo 9 i Coveyouova podmínka pro vyšší stupně
jsou podstatné. Substituce X=4Y+2, střední bity a Fibonacciho determinant
b²−ab−a² dávají tvrzené periody. Obecná polynomická věta úlohy 11
platí i při nejednotkovém nejvyšším koeficientu; používá f(0)=1.
Horní mez 2^(e+1) v úloze 12 se odvozuje z univerzální posloupnosti,
nikoli z neplatného tvrzení o zdvojování periody libovolného seedu.

Algoritmus A a dávková varianta mají správné pořadí aktualizací a MIX
časy 14+2/55 a 12+6/55. Algoritmy M/B, obě malé tabulky a binární
programy odpovídají zadání. Výstup B má úvod délky 46, i když celý
vnitřní stav má úvod 47. Příklady jsou kontrolou deterministických
posloupností; obecná slovní doporučení statistické kvality nejsou
přetvořena v důkazy nezávislosti. Synchronizační slovo úlohy 27 má
(k²+7k−2)/2 symbolů; pravděpodobnostní dovětek potřebuje náhodný model
vstupu a nedává bezpodmínečnou záruku pro každou periodickou posloupnost.

Pro velký příklad (13) přijat starý úplný průchod 2^35 stavů a jeho
dokončovací log. Nezávislý archivovaný důkaz pokrytí 4096 bloků dává
dostatečnou horní mez mezer 8 389 366 < 2^34; přesné maximum 1616
pochází z výčtu. Jedinečná menší četnost nulového intervalu a
gcd(2^35−1,2^29−1)=1 vynutí periodu mezer 2^35−1. Hlavní věta
úlohy 15 pak dává výstupní periodu 2^70−2^35. Výčet se neopakoval.

Kritérium primitivity na 30 je nutné i postačující bez dodatečného
předpokladu ireducibility: podgrupa generovaná x obsahuje všechny
nenulové konstanty a její podíl má řád r, takže vyčerpá všech p^k−1
nenulových prvků okruhu. Počet polynomů φ(p^k−1)/k souhlasí.
Všech 12 dvojic z tabulky 29 porovnáno s přepisem v programu; přijaty
archivované polynomické důkazy, Lucasovy certifikáty a osm
Lucasových–Lehmerových testů. Kontrolní kód byl přečten, výpočty
nebyly znovu spuštěny. Stejně přijato 63 vyvážených masek a 46 dvojic
koeficientů úlohy 19; první dva sloupce tabulky 408 byly znovu porovnány
s přepisem. Zbytek strany 408 tím není uzavřen.

U úplných posloupností znovu ověřen Eulerovský důkaz hladové konstrukce,
vložení nuly, obě seskupení pro prvočíselné mocniny a součin abeced.
Algoritmy X/Y odpovídají pravidlu po komplementaci číslic v článku
Amram et al. (2019). Znovu přečteny definice a důkaz věty 4 s lemmaty
6–9; jeho FKM rozklad je použitý citovaný výsledek. Případ k=1 je
přímý sestupný cyklus. Vlastní výjimka m=1 byla dříve v programu
doplněna navíc: nyní je samostatně evidována jako nízký **C0240**.
Povolený záporný pomocný práh Y při prázdné množině neznamená zápornou
výstupní cifru. O(log k) či O(1) průměr je v knize spekulace, nikoli
prokázaná mez. Starý první neúspěch testu byl vadný předpoklad testu
o jedinečnosti běhu nul; pokračování neopakovalo již dokončený blok.

Dvě výjimečné identity úlohy 30 přesně charakterizují selhání růstu
periody; potřeba vyloučit obě znaménka vyplývá z t(t+1)=0 nad F_(2^k).
Trojčleny stupně >2 obě výjimky vylučují. Důkazy úloh 23 a 31
navazují přes reciproký polynom a rozklad lichých zbytků na (−1)^Y3^Z.
V úlohách 32–33 se nejprve pracuje nad celými čísly; dělení 2 či 3
nevyžaduje jejich invertibilitu modulo m. Všech 20 koeficientů X₅₀₀
a šest koeficientů X₁₆₅ znovu porovnáno s originálem i uloženými
symbolickými výpočty. Víceslovný experiment úlohy 28 přijat v přesném
2D rozsahu; obecná překážka plyne z normály (−a,1).

Inverzní generátory 34–37: projektivní matice, počet
(p−1)φ(p+1)/2, dvouadická ohodnocení a důkaz meze d bodů v nadrovině
znovu odvozeny proti tištěným vzorcům. Implementační vynechání ∞
mění délku plného cyklu z p+1 na p; není to rozpor. Póly jsou záporné,
což je rozhodující pro rozlišení známého errata a C0014. Doplňující
„otherwise“ v odpovědi 36 je čteno v permutační třídě s lichým a;
obecný důkaz nutnosti ošetřuje také neprostou větev sudého a.

## Nálezy a přesné lokace

| ID | Závěr souvislé revize | Původní strana s chybou |
|---|---|---|
| C0007 | Mez mezer neplatí pro k=2; perioda 8 místo nejvýše 4, hlavní věta správná. | 554 |
| C0008 | Dodatek 2019 vynechal výjimku pro samé maximální cifry. | Žádná; 40/559 jen souvisejí. |
| C0009 | Návod může běžet navždy; závěr o discrepancy potřebuje růst period. | 37,39 |
| C0010 | Připsaný výsledek pro k=3 potřebuje primitivitu. | 39 |
| C0011 | Maska z dodatku 2013 má faktor x+1 a nenulový pevný stav. | Žádná; 555 jen souvisí. |
| C0012 | Dodatek 2001 nahradil správné sX+Y neúplným součtem X+Y. | Žádná; 556 jen souvisí. |
| C0013 | Nesprávný index v součinu: 4 versus 8 při a=1,c=2,n=1. | 558 |
| C0014 | Po opravě jmenovatelů zbývá změnit dosazení na x=−u_j. | 559 |
| C0240 | X2 nemá hledaný index pro povolené m=1; stačí vrátit 0. | 557 |

C0009/C0010 nejsou vyřešením zamýšlené otevřené Reiserovy domněnky.
Z původní zprávy znovu vizuálně ověřeny předpoklady na 1, věta 4.2
na 20, věta 4.4 a podmínka růstu na 25 a domněnka 4.1 na 26.
Dolní mez počtu nul má uvedený vlastní maticový důkaz; hlubší kubický
odhad je přijat s předpoklady jako citovaný výsledek. Současná obecná
otevřenost ani prvenství nálezů se netvrdí.

**X0092** mapuje známé opravy původní sazby: 29,33–35,39,552–555,
557–558. Doplnění věty o j/k na 28 není samo novou chybou algoritmu.
Zpřesnění odkazu na 31 ani změna pomlčky na 27 nejsou novou matematickou
vadou. Zatoulané „(2)“ před odpovědí 21 opravené v roce 2026 v našem
prvním tisku není. Oprava sup na 559 patří až §3.3.1, nikoli této sekci.

## Zdroje, výjimky a navazující práce

Payneova inicializace (primární zpráva 1973, str.7–8) začíná nenulovým
sloupcem a jeho obrazy invertibilní matice; každý bitový sloupec proto
skutečně má nenulovou fázi. Celá jeho tabulka ani FORTRAN znovu
ověřovány nejsou. Lüscherova věta 2.2, rovnice 2.9–2.12, opět potvrzuje
násobitel b^(−t) pro t kroků. Jeho přesné parametry jsou jiné než
knižní ilustrace 55 z 500; nejsou zaměňovány. Staré empirické testy
z textu a tabulky spektrální kvality nejsou v tomto bloku reprodukovány.

Rychlé hledání Coveyouova článku, Martina (1934) a Bays–Durhama
nepřineslo přímo použitelný primární plný text; ACM vrátil 403.
Sekundární vyhledané odkazy nejsou přijaty jako přečtené články.
Dále výslovně přeskočeny nedostupné/unpublikované historické prameny
Mauchly 1949, Mitchell–Moore 1958; úplný obsah Green–Smith–Klem,
Normand–Herrmann–Hajjar, Alanen–Knuth, Tausworthe, Stahnke, Rees,
Lempel, Greenwood, Gebhardt, Ward, Robinson, Wall/Jansson a články
o inverzních generátorech. Existující dílčí metadata nejsou důkazem
celého obsahu ani historického prvenství. Algebru jejich zde použitých
tvrzení pokrývají výše uvedené důkazy a konkrétní uložené výsledky.

Kryptografická redukce na 36 a srovnání potřebných modulů budou
porovnány s §3.5F a související úlohou §4.5.4-43 v jejich pořadí.
Zde ověřena pouze definice, kvadratické zbytky a podmíněný/distribuční
smysl tvrzení. Pevný seed 1 ani maska 0 nejsou vyvrácením takto
kvantifikovaného bezpečnostního tvrzení. Datum 1997 se nezaměňuje
za současné výkonnostní doporučení.

Další kurzor: §3.3 a §3.3.1, původní str.41, odpovědi559.

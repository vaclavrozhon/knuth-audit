# Slovní schody: úplný rozsah kontroly 7.2.2.1–91 až 93

Originály: zadání 4B str. 133–134, odpovědi 436–437; autorův Pre-Fascicle
5C z 11. 9. 2019, str. 140–141. Stránky byly vizuálně porovnány.
Používáme původní pořadí `sources/wordlists/words5-from-sgb`.
Číselný rank je jedničkový. Žádné nové návrhy emailů nevznikají.

## 91: geometrie a přesná definice výpočtu

Čtrnáct znaků kernelu a osm pětic jsou doslovně v `word_kernel91.py`.
Pravé schody mají fyzické řádky A_i; pro levé při konstrukci kernelu
každý řádek obrátíme. V obou případech je kernel u řádku t

```
A_(t-2)[4] A_(t-1)[3:5] A_t A_(t+1)[0:4] A_(t+2)[0:2].
```

Indexy uvnitř slov jsou zde od nuly. Tištěná devítice zdroje a cíle
souhlasí přesně s posunem t→t+1. První přispěné slovo je A_t, u levých
schodů obrácené zpět. Druhé je fyzické svislé slovo začínající v řádku t−2.
Obráceně devět rovností mezi sousedními kernely vynutí všechny tyto
překryvy. Uzavřená procházka s 2p různými přispěnými slovy tedy dává
právě platný slovní schod; není třeba sjednocovat libovolně vybraná x
z lokálních doplnění.

Pro reprodukci knižních čísel musí být **všech osm lokálních slov různých**.
Bez této podmínky je pravých kernelů 245 421, levých 233 538. Samotné
odlišení dvou prostředních slov také nestačí. Osm různých slov je nutnou
podmínkou každého platného schodu s p≥4. Pro obecný algoritmus je proto
bezpečné ošetřit p=1,2,3 zvlášť nebo ponechat opakování v lokálním modelu
a různost vyžadovat teprve u celé procházky. V obou zde hledaných maximech
je dosažená perioda alespoň 4, takže tato výhrada nemění horní mez.

Join nejprve promítá všechny osmice na c1,…,c14. Následný úplný test
disjunktních slovních masek přesně zachovává dvojice spojené x5 a x7,
dvě zbývající slova i obě prostřední slova. Ke každému přijatému kernelu
je uložen konkrétní svědek osmi různých slov; všechna jeho písmena byla
znovu porovnána s doslovnými osmi vzory. Soubor `build_kernel91_graphs.py`
umožňuje výpočet reprodukovat. Bez nové pochybnosti se neopakuje.

Nezávislý doslovný XCC model používá osm primárních pozic, 26 barevných
písmenových položek a neobarvené položky slov. **96 úplných porovnání**
malých slovníků, celkem **57 789 doplnění**, potvrzuje celé množiny
kernelů s opakováním i bez něj. Plný původní DLX2 navíc nezávisle
promítá všechna doplnění pro levé WORDS(500); jeho terminální výsledek
a porovnání celých množin přijímá `check_word_stairs_checkpoint.py`.
Dokončeno 2. 11. 2026 v 01:37:06 UTC: **5 372 478 doplnění**, přesně
**136 771** různých kernelů, celá množina shodná s nezávislým joinem.
Vstup, binárka, zdroj, stdout digest a celý diagnostický log mají uložené
kontrolní součty; běh skončil kódem 0, nikoli timeoutem.

## F127: chybný počet hran redukovaného levého grafu

| Míra | Pravé WORDS(1000) | Levé WORDS(500) |
|---|---:|---:|
| Všechny různé kernely / hrany | 180 524 | 136 771 |
| Všechny vrcholy | 96 677 | 74 568 |
| Vrcholy po odstranění nulového vstupního/výstupního stupně | 30 | 6 280 |
| Hrany po této redukci | 34 | **12 269** |
| Vrcholy největší silně souvislé komponenty | 10 | 6 150 |
| Hrany uvnitř této komponenty | 12 | 12 050 |

Na str. 436 je **13 677** místo **12 269**. Stejných 13 677 má autorův
PS na str. 140; ostatní uvedené počty souhlasí. Rozdíl je 1 408 hran.

Redukci ověřily tři postupy: fronta nulových stupňů, opakovaný průchod
všemi hranami a nezávislý NetworkX graf s výpočtem stupňů. Shodují se
celé množiny zbývajících hran, nikoli jen jejich počty. Silné komponenty
z iterativního Kosarajuova algoritmu jsou shodné s NetworkX.

Výsledek je největší indukovaný podgraf s kladnými oběma stupni:
žádný vrchol libovolného takového podgrafu nemůže být první odstraněný,
protože by stále měl svého předchůdce a následníka. Po skončení mají
všechny ponechané vrcholy požadované stupně. Redukce je tedy nezávislá
na pořadí odstraňování a 12 269 nelze vysvětlit jinou volbou podgrafu.

Doklady: `results/stair_kernels/*-distinct.json`, úplné množiny kernelů,
`left500-scan-core.json`, `left500-sat-verified.json`, původní stránky.
Šest úplných vrstev errat neobsahuje odpovídající opravu; čtyři aktuální
oficiální originály byly 2. 11. 2026 shodné s archivem.
Fyzický tištěný exemplář zůstává neověřený.

## 91: maxima 5 a 36 jsou správná

Odstranění vrcholu, jímž neprochází žádný jednoduchý cyklus s různými
přispěnými slovy, je bezpečné i pro hledání uzavřených procházek:
z libovolné takové procházky přes v lze vymazat vnitřní cykly a dostat
jednoduchý cyklus přes v se stejnou podmínkou různosti. Odstranění hran
mezi různými silnými komponentami je bezpečné z definice souvislosti.

Levý graf: 11 kol, **3 798** přímých vyřazení, **7 296 855** navštívených
stavů při testech cyklů, žádný nedokončený test. Nakonec 703 vrcholů
a 1 317 hran. Každé z 3 798 tvrzení o neexistenci cyklu nezávisle
ověřil **CaDiCaL 1.9.5** přes PySAT: jedna booleovská proměnná na hranu,
na aktivním vrcholu právě jedna příchozí i odchozí hrana, každé slovní
označení nejvýše jednou. Vynucení v je SAT právě tehdy, když takový
jednoduchý cyklus přes v existuje; další disjunktní cykly lze zahodit.
Použitá CNF má 51 927 proměnných a 136 893 klauzulí.

Úplný následný průchod dovoluje i opakované vnitřní vrcholy a pokračuje
i po prvním návratu do počátku. Nepřehlédne tedy spojení kompatibilních
cyklů. Různost slov omezuje délku na W/2. Po kanonizaci rotací získává
**181** procházek, všechny ve skutečnosti jednoduché; čtyři mají největší
periodu **36**. Výměna napříč/svisle je páruje do dvou tříd. Pravý graf
má dvě orientované pětice (jednu takovou třídu), žádnou delší procházku.
Všechna nalezená řešení byla znovu ověřena přímo v geometrii a slovníku.

Tištěná pravá devíticová trasa sedí znak po znaku:

```
SEDYEARST → DRSSTEASA → SAMSALEMA → MESMARKDR → SKSDRIEYE → SEDYEARST.
```

Levý tištěný svědek má 72 různých slov a nejvyšší rank 498.
GLORY=496, FLOWS=498. Pravý svědek má 10 různých slov a rank 908.
Historická oprava **E045**, 6. 6. 2021, mění ve vydaném Fascicle 5
„the shortest“ na „an optimum“ a FALLS na WALLS. Naše 4B má obě opravy;
PS z roku 2019 má „the longest“ a FALLS. **FALLS i WALLS jsou platné
optimální varianty** (v odpovídajícím svislém slově FOODS/WOODS).
Změna slova proto sama není důkazem neplatnosti starého svědka.

## C026: nejasný cíl hledání cesty

Odpověď 91 požaduje hledat „a simple path, from v“ a při neexistenci
vrchol odstranit; neuvede konec cesty. Doslovně má každý uvažovaný
vrchol s výstupním stupněm 1 už jednou hranou takovou cestu, protože
každá hrana přispívá dvěma různými slovy. Například

```
AHSEREHMA → SHTMAERDE  přispívá THERE, AHEAD.
```

Přesto tímto vrcholem žádný cyklus s různými slovy neprochází, jak
samostatně potvrzuje SAT. Přirozené upřesnění je „a simple cycle through v“
nebo cesta vracející se do v. Kontext cyklů dovoluje zamýšlený význam
uhodnout, proto jde o **kandidáta na upřesnění**, nikoli další potvrzenou
matematickou chybu. Obě maxima byla ověřena nezávisle na této formulaci.

## C027: krátké periody potřebují výslovnou výjimku

Výše popsané rozlišení osmi různých slov není jen technická drobnost:
platný levý schod **WRITE / WHOLE** v WORDS(136) má svislá slova
WHILE / WROTE, avšak **ani jeden z jeho dvou kernelů nemá doplnění
osmi různými slovy**. To pro každý pevný kernel potvrdil i neupravený
DLX2 úplným XCC výčtem. Doslovná podmínka členství osmi slov ve slovníku
jej zachová, ale tato interpretace zase nedává vytištěné počty grafu.

Znění by mělo výslovně rozlišit model použitý pro počty a ošetření p<4.
Jde o **kandidáta na doplnění rozsahu**, protože podmínka osmi různých
slov v odpovědi není výslovně napsaná a byla rekonstruována z čísel.
Neoznačujeme za chybná prokázaná maxima 5 a 36.
Doklad: `results/stair_kernels/left136-boundary.json` a oba nativní vstupy.

## F128: pravý směr v odpovědi 92 má špatné indexy řádků

Při pevných řádcích A_i jsou levá svislá slova
`B_i[j] = A_(i+j)[j]`, pravá `D_i[j] = A_(i+j)[n−1−j]`.
V tištěném XCC ale možnosti b_i i d_i používají **tutéž** diagonálu
`(i+j,j)`, druhé pouze v obráceném pořadí písmen. Model tedy vyžaduje,
aby každé levé svislé slovo mělo mezi vybranými slovy svůj reverz.
To neodpovídá dvěma obrázkům v zadání, kde je pořadí vodorovných řádků
stejné v levém i pravém schodu.

Pro knižní příklad p=3:

| Směr | Slova |
|---|---|
| Napříč | WAVES, LINED, LEPER |
| Vlevo dolů | WIPED, LEVER, LANES |
| Vpravo dolů | SEPAL, DEVIL, RENEW |
| Co místo pravého směru vynucuje tisk | DEPIW, REVEL, SENAL |

Všech devět skutečných slov je v WORDS(4378), nejhůře SEPAL=4378.
DEPIW ani SENAL nejsou v celém slovníku. Tištěný model tedy vyloučí
vlastní platný příklad i s celým slovníkem.

Oprava při zachování označení buněk i pořadí c_n,…,c_1: v d_i nahradit
`i+j` výrazem **`i−j` modulo p**. Konkrétně

```
d_i  i1:c_n  ((i−1) mod p)2:c_(n−1)  …
     ((i−n+1) mod p)n:c_1  c_1…c_n.
```

Je to fyzické pravé slovo s přejmenovaným počátkem. Odlišné přejmenování
indexů pouze d_i je neškodné; obrácení společných řádků pro celou redukci
by současně změnilo levý směr, a chybu tak neřeší.

Nejmenší přehledný pomocný příklad pro obecný předpis n=2,p=3 je
`AA / BC / CB`; po doplnění obou směrů obsahuje všech devět dvoupísmenných
slov nad A,B,C. Původní model pro fixované vodorovné řádky má 0 řešení,
opravený 1. Totéž platí pro výše uvedený pětiznakový knižní příklad.
Oba případy potvrdil doslovný interpret i **neupravený původní DLX2**.
Vstupy, celé malé výstupy a hashe jsou v `results/three_way_stairs/`.

PDF str. 437 i autorův PS str. 141 mají stejné plusové indexy.
Známá **E046** z 25. 5. 2021 pouze opravuje jména w′ na w@; ve 4B
je zapracovaná a indexovou chybu neopravuje. Žádná odpovídající oprava
nenalezena ve všech šesti vrstvách ani aktuálních originálech.

## 92–93: bijekce, symetrie a svědci

Po opravě 92 mají oba modely 3p primárních pozic, pn barevných buněk,
W položek pro různost a W pomocných markerů. Každá fyzická buňka má
stejné písmeno ve třech vybraných slovech. To dává bijekci s uspořádanými
platnými řádky; volba primární pozice určuje, které slovo se kam čte.
Seřazení možností podle ranku dovoluje pomocí w@ vybrat nejběžnější
vodorovné slovo jako první: kořenové markery jsou různé, podmínka opravy
F123 je splněná. Všech p rotací je různých, protože řádky jsou různé.

U 92 je p=1 nemožné: levé slovo se shoduje s vodorovným. U 93 jsou
svislé směry `A_(i+j)[j]` a `A_(i−j)[j]`; pro p≤2 se shodují, takže
3p různých slov není možné. Obrácení pořadí řádků tyto směry vymění.
Pro p≥3 má spolu s rotacemi orbitu přesně 2p: pevná reflexe by musela
ztotožnit dva různé řádky. Knižní poznámka o obtížnější implementaci
této druhé symetrie nepopírá její matematickou platnost.

**39 úplných malých instancí**, včetně vysazených platných vzorů a prázdných
případů, dává celé shodné množiny ve třech metodách: geometrické permutace,
doslovný opravený XCC a samostatné slovní CSP. Celkem 230 uspořádaných
modelů. Navíc se shodují celé rotací normalizované množiny CSP.

Všech 17 tištěných příkladů je platných. Jejich dosažené ranky:

| Perioda | 92: oba schody | 93: obě diagonály |
|---:|---:|---:|
| 2 | 3402 | nemožné |
| 3 | 4378 | 2000 |
| 4 | 4492 | 1499 |
| 5 | 5091 | 1410 |
| 6 | 4533 | 1506 |
| 7 | 4606 | 1574 |
| 8 | 5109 | 1626 |
| 9 | 4237 | 1506 |
| 10 | 5149 | 1438 |

Tabulka svědků sama **neprokazuje optimalitu**. Samostatná fronta
`run_three_way_queue.py` vyčerpává slovní CSP při prahu B−1; případné lepší
řešení uloží a pokračuje níž. Limit 48 hodin na případ vyvolá stav
`incomplete`, nikdy UNSAT. Přijaté dokončené dolní meze i zbývající případy
jsou v `results/three_way_stairs/checkpoint.json`. Živé výstupy se necommitují.

Obě ilustrace RAPID/RATED/LACES/ROBES a SLANT/FLUNK/BLINK ověřeny celé,
včetně šesti slantových slov v obrázku. Historický TINE/SALE/MALE/VINE
má diagonály TILE/SINE/MANE/VALE a TALE/VILE/MINE/SANE, celkem 12 různých
slov; jde o kontrolu geometrie příkladu, ne jeho datování.

## 93: historická mezera zůstává otevřená

[Oficiální Oulipo](https://www.oulipo.net/fr/contraintes/algorithme-de-mathews)
připisuje příbuzný sloupcový algoritmus Mathewsovi, ale s francouzským
příkladem a webovým údajem 1982. To nedokazuje, že knižní rok 1975 je chybný.
[Bibliografie archivu](https://archives-oulipo.fr/node/16005) potvrzuje
Mathews/Brotchie, *Oulipo Compendium*, Atlas, 1998, a odlišné vydání 2005.
Oba originální HTML soubory mají archivované URL, čas a SHA-256.

Přesný rok uvedení 1975 a obsah stran 180–181 vydání 1998 zatím nemáme
ověřené v původním prameni. Butlerův katalog dovolil přes webový nástroj
přečíst bibliografii Mathewsova článku *Oulipo*, Word Ways 9(2), 1976,
ale přímé stažení katalogu i článku vrátilo HTTP403. Žádný PDF originál
tohoto článku není vydáván za získaný nebo vizuálně ověřený.
Podrobnosti: `sources/word_stairs/history.json`.


## Přijaté přírůstky 2. listopadu 2026, blok DLX94–100

Původní fronta874050 dokončila diagonal-7 a diagonal-8: prahy1574 a1626,
193108 a369529 uzlů. Oba terminální výsledky prošly kontrolou zdrojových
hashů, úplné dolní meze B−1 a všech slov svědka; hledání se neopakovalo.
Spolu s dříve přijatými3–6 jde o šest prokázaných diagonálních optim,
650587 uzlů. Periody9/10 a devět two-way případů zůstávají ve frontě.
Původní historická mezera1975 / Compendium180–181 se tím nemění.

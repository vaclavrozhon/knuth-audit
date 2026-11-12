# Konvexní polyomina, Bitland a Dominosa — DLX68–71

Kontrola 1. 11. 2026, lokální 4B, první vydání / druhý dotisk2022.
Zadání str.130–131 (PDF150–151), odpovědi430–431 (PDF450–451).
Všechny čtyři původní stránky byly zobrazeny. Hlavní polyominový text79–82
zůstává samostatným příštím blokem; pouhé zobrazení jeho stran jej neuzavírá.

## F119: v odpovědi69 je 1467 místo1647

Na str.431, řádek s počty možností `N6,N5,N1,N0`, jsou prohozené prostřední
dvě číslice prvního počtu. Správně je **(1647,2362,163,2)**.
Týká se to přípustných umístění konvexního nonomina se šesti B, nikoli počtu
celých rozkladů. Konečný výsledek0 a60 řešení obou případů zůstává správný.

Stejných1467 je v autorově původním PS `fasc5c.ps.gz`, revize3 z11.9.2019,
na tištěné str.135 (strana141 převedeného PDF). Původní stránka byla zobrazena:
[autorův PS](images/fasc5c-bitland-p135.png), [naše4B](images/vol4b-p431.png).
Fyzický výtisk nemáme ověřený. Potvrzení zde znamená doložení v těchto zdrojích,
nikoli potvrzení priority hlášení nebo odměny.

Podkladová mřížka, čtená samostatně z obrázku a porovnaná se všemi243 glyfy
tří původních PDF diagramů:

```text
BBLBLLLLB
LLLBLLLBL
BBLBLBBLB
LLLLLLLLL
BBBLLBLLB
LBLBBBBBB
BBLBBBBBL
LBLLLLBLL
LLBLLBBLL
```

Úplný histogram přípustných umístění podle počtu B:

| B v dílku | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Počet | 2 | 163 | 1363 | 2785 | 2771 | 2362 | **1647** | 753 | 230 | 21 |

Součet12097 souhlasí s úlohou68. Výsledek vznikl třemi cestami:

1. Růst všech normalizovaných souvislých polyomin a test intervalů v řádcích
   a sloupcích; všechny povolené posuny325 tvarů do9×9.
2. Dříve ověřený úplný seznam AlgorithmuR, filtrovaný nezávislým obvodovým
   testem a podmínkou obálky4×4. Celé množiny umístění se shodují.
3. Samostatný program `check_bitland69_count.py` projde všech
   binom(16,9)=11440 podmnožin4×4, přímo zkontroluje souvislost a všechny
   mezilehlé buňky dvojic ve stejném řádku/sloupci. Normalizace dá325 tvarů,
   posuny přesně stejných12097 umístění. Tento program nepoužívá růst,
   obvodový filtr ani řešič přesného pokrytí.

Soubor [F119-six-B-placements.json](results/convex68/F119-six-B-placements.json)
obsahuje všech1647 různých svědků; buňka je `9*r+c`, indexováno od0.
[F119-count.json](results/convex68/F119-count.json) uchovává úplné počty a hashe.
Tím je možné výsledek ověřit i bez důvěry v solver nebo v tištěnou odpověď.

## Úloha68: úplné možnosti a symetrie

Konvexita zde znamená jediný interval v každém neprázdném řádku i sloupci.
Je-li v obálce w×h celkem R řádkových a C sloupcových intervalů, obvod je
2(R+C). Souvislost zajišťuje alespoň jeden interval v každém z h řádků
a w sloupců. Rovnost s2(w+h) tedy nastává právě při uvedené konvexitě.
Je to obecný důkaz závorky v zadání, nikoli jen konečný test.

Každý souvislý tvar lze zmenšit o list kostry jeho grafu sousedností a
zachovat souvislost. Indukcí proto postupné přidávání sousední buňky a
normalizace posunutím vytvoří všechny pevně orientované tvary.
Obě charakterizace konvexity se navíc shodly u každého takto vytvořeného
tvaru velikostí1–9. Z12 volných pentomin je právě11 konvexních; jediná
výjimka je U, ověřeno úplnou D4 normalizací.

| n | Normalizované konvexní tvary | Umístění v n×n | Rozklady |
|---|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 2 | 4 | 2 |
| 3 | 6 | 22 | 10 |
| 4 | 19 | 113 | 117 |
| 5 | 59 | 523 | 2908 |
| 6 | 176 | 2196 | 162616 |
| 7 | 502 | 8438 | 18187302 |
| 9, obálka≤4×4 | 325 | 12097 | 8113709 |
| totéž bez čtverce3×3 | 324 | 12048 | 5406376 |

V `options.json` pole `convex_shapes` označuje původní množinu tvarů před
dodatečným odebráním čtverce: proto obsahuje325 i u varianty bez čtverce.
Odebrána jsou všechna49 umístění3×3, nikoli jen devět standardních sudoku boxů.
Na rozdíl od62 jsou zde přímé dílky povolené. n1 je triviální jediný rozklad.

Nezávislá masková rekurence potvrdila všechny vypsané počty. Volí první
nepokrytou buňku a postupně každý přípustný dílek, který ji obsahuje;
každý úplný rozklad tak započítá právě jednou. Oddělené komponenty volného
prostoru se násobí, protože souvislý dílek nemůže překlenout dvě komponenty.
Komponenta s velikostí nedělitelnou n dává nulu. Memoizace výsledek nemění.

Původní neupravený DLX1 používá jiný model: primární položky buněk a
možnosti odpovídající celým dílkům, s MRV. **Všechny jeho úplné výčty nyní
dokončily se shodnými počty.** Poslední n9 bez čtverce skončil
2.11.2026 v00:41:42UTC:5 406 376 řešení,83 027 265 uzlů a celý profil
jsou ověřeny proti zaznamenaným vstupům, zdrojům, binárce a výstupům.
Nezávislá masková rekurence dala tentýž počet dříve. n7 má18 187 302
řešení a163 499 709 uzlů; n9 se čtvercem8 113 709 a111 286 419.
`check_convex68_final.py` pouze přijal hotový výsledek, žádnou enumeraci
neopakoval. `results/convex68/final-verified.json` spolu s úplnými
symetriemi a obecným důkazem uzavírá X068. Starší `counts-checkpoint.json`
zůstává datovaným průběžným stavem, nikoli aktuálním seznamem mezer.

Symetrie byly dokončeny celé, nezávisle na době plných DLX1 běhů:

| n / varianta | stabilizátor1 | stabilizátor2 | stabilizátor4 | stabilizátor8 |
|---|---:|---:|---:|---:|
| 2 | 0 | 0 | 1 | 0 |
| 3 | 1 | 0 | 1 | 0 |
| 4 | 10 | 7 | 4 | 1 |
| 5 | 355 | 15 | 4 | 0 |
| 6 | 20154 | 342 | 8 | 0 |
| 7 | 2272821 | 1181 | 5 | 0 |
| 9, obálka≤4×4 | 1014148 | 119 | 24 | 1 |
| 9 bez čtverce | 675797 | 0 | 0 | 0 |

Pro každý ze sedmi neidentických prvků D4 vytvoříme celou jím generovanou
podgrupu. Její orbity dílků, jejichž dílky se nepřekrývají, slouží jako
možnosti dalšího přesného pokrytí. Pevný rozklad je právě sjednocením těchto
orbit; odpovídající bijekce je obousměrná a úplná. Každý takový problém
vyřešil původníDLX1 a nezávislý bitový výčet; shodují se počty i celé profily.
Všechny získané modely byly geometricky validovány a kanonizovány D4.
Asymetrická část je (úplný počet−počet neidenticky symetrických modelů)/8.
Váha třídy se stabilizátorem velikosti s je8/s; všechny součty souhlasí.

Citace Bousquet-Mélou/Fédou, DiscreteMath137(1995),53–75, DOI
[10.1016/0012-365X(93)E0161-V](https://doi.org/10.1016/0012-365X(93)E0161-V),
má správné údaje; metadata dodaná vydavatelem přesCrossref jsou archivována,
abstrakt vydavatele potvrzuje generující funkci podle plochy/šířky/výšky.
Samotné odvození její obecné formule není tvrzením této úlohy.
[Klarnerův a Rivestův původní článek](https://people.csail.mit.edu/rivest/pubs/KR74.pdf)
je uložen celý; zobrazená str.31 přímo definuje tentýž pojem, uvádí autory
a bibliografii8(1974),31–40. Tím je prověřen věcný obsah historického odkazu
na odpověď303; nejde o nový audit všech vzorců úlohy303.

## Úloha69: obvody a všechna řešení

Všechny tři původní diagramy mají stejných36B a45L. Každý standardní3×3
obvod v prvním diagramu má4B/5L. Druhý i výsledný diagram mají počty
`0,1,5,5,5,5,5,5,5`, tedy sedm vyhraných obvodů. Každý obvod má9 buněk;
u odpovědi byla navíc ověřena konvexita a obálka nejvýše4×4.

Sedm výher spotřebuje nejméně35B, osm by vyžadovalo40B a není možné.
Zbývající jediný B buď přidáme k vítězi (jeden6B, šest5B, dvě0B), nebo
k jednomu poraženému (sedm5B, jeden1B, jeden0B). Tím jsou vyčerpány právě
oba případy z odpovědi; dílky se7B či více nemohou v sedmivýherním řešení být.

První případ má navíc krátký geometrický důkaz nemožnosti: obě jediné
přípustné možnosti s0B obsahují buňku(řádek1,sloupec5), indexováno od1.
Nemohou tedy současně tvořit dva disjunktní obvody. Ve skutečnosti sdílejí
osm buněk; výsledek0 není závislý jen na vyčerpání stromu řešičem.

Přímý kapacitní výčet a původní neupravený DLX3 souhlasí **celými množinami**:
první případ0, druhý60 řešení. Všech60 modelů má validovaný úplný rozklad
81 buněk, požadované násobnosti a přípustnou geometrii; vytištěný rozklad
je členem této množiny. ModelM používá81 položek buněk s násobností1 a
položky Nk s předepsanými násobnostmi. Výběr každého dílku splní právě jeho
devět buněk a jednu příslušnou položkuNk, proto je kódování bijektivní.

Naměřené původníDLX3 náklady: první případ2,962,264 iniciačních a40,607
hledacích memů; druhý1,787,184 a10,075,232. Druhý případ samotný je11.862M,
tedy po zaokrouhlení12M jako v knize. Přesné historické pořadí vstupu a
započítání přípravy však není doloženo; z rozdílných konvencí neděláme chybu.

Oficiální [seznam disertací JHU](https://engineering.jhu.edu/ams/academics/graduate-studies/doctoral-program/dissertations/)
uvádí přímo1968, RobertGarfinkel, OptimalPoliticalDistricting.
Tento údaj byl dostupný v indexovaném výsledku oficiální stránky; přímý
archivační download skončil403. Také stažení archivuPhilpott skončilo429,
autorský seznamBousquet odmítl spojení. Manifest zachovává tato selhání;
nevydává je za stažené nebo přečtené úplné dokumenty.
Historických1000 náhodných hlasovacích vzorků a výsledků696/8 nelze ztotožnit
s našimi novými vzorky bez původního seznamu/semen. Tento dosud neověřený
experiment a přesný historický benchmark udržují X069partial; nepopírají
úplně prokázanou matematiku konkrétního Bitlandu.

## Úloha70: původní obrázky a úplné množiny řešení

PDF používá bitmapové Type3 fonty. `check_dominosa70.py` načte původní
charprocs a vyčíslí bílé souvislé komponenty uvnitř každé dlaždice;
získané počty0–6 se shodují s ručně zobrazeným atlasem. Spojovací tahy
jednoznačně párují sousední buňky. Všechna párování jsou vzájemná,
bez výstupu z desky. Stejné pojmenované glyfy ve fontechT42/T35 mají
identické bitové programy. Původní vrstvy nebyly opravovány.

Zkontrolováno112 čísel obou matic,168 buněk s tečkami a84 kamenů ve třech
diagramových rozkladech. Každý rozklad obsahuje právě jednou všech28
neuspořádaných dvojic0≤x≤y≤6; každá hodnota má v matici8 výskytů.

Souřadnicový DFS vezme první neobsazenou buňku a zkusí její volného pravého
nebo dolního souseda, pokud dvojice hodnot nebyla použita. Horní/levý soused
musí být při tomto pořadí již obsazen. Tím je výčet úplný a bez duplicit.
PůvodníDLX1 má položky56 buněk a28 typů kamenů a všech97 sousedních umístění.
Oba postupy dávají celé stejné množiny: **(a)2 řešení, (b)1 řešení**.

Vytištěné řešení(a) má s původním diagramem společných24 kamenů;
zbývající čtyři se opravdu mění. U druhého zadání souhlasí všech28 kamenů.
Rozložení teček2,3,6 rozlišuje vodorovnou a svislou orientaci. Jeho přidání
k první matici zachová právě původní rozklad; tento vizuální údaj tedy
skutečně odstraňuje druhé řešení. Matice čísel jej neobsahuje.

Získán úplný veřejný sken [Adler/Jahn, třetí vydání1920](https://commons.wikimedia.org/wiki/File:Adler-Jahn1920_Dominosa.pdf).
Titulní list potvrzuje oba autory. Původní předmluva na str.5 je podepsána
FritzemJahnem v září1912; následující předmluva přímo označuje podzim1912
za první vydání. Adlerův vlastní historický text str.24–31 byl zobrazen;
str.30 potvrzuje patent1893 a pseudonymRichardOsa. Rozdílná paginace
třetího vydání sama neopravňuje měnit knižní odkaz23–64 na vydání1912.

Přesné číslo patentu71539, stránky prvního vydání, původní Lucas1883
str.52–63 a PhilpottJRM4(1971),229–243 zatím nebyly všechny uzavřeny
primárními stránkami. Dohledané Philpottovy archiválie a jeho jiný článek1967
nejsou náhradou požadované citace1971. Proto X070partial, přestože celá
matematika i obrázky byly ověřeny. Rešeršní podklady a jejich meze jsou
oddělené od potvrzeného početního nálezuF119.

## Úloha71: obecný převod na3DM

Tři disjunktní třídy vrcholů jsou28 typůDxy,28 černých a28 bílých buněk
šachovnicového obarvení7×8. Každé povolené sousední umístění spojuje právě
jeden vrchol z každé třídy. Perfektní3DM proto pokryje každou buňku a každý
typ kamene právě jednou a je právě rozklademDominosa. Obráceně každý rozklad
takové párování dává. Nejde jen o empirické porovnání dvou příkladů.

Horizontálně7×7=49 možností, vertikálně6×8=48. Všech97 možností obou matic
má správnou paritu. Šest vytištěných příkladů odpovědi bylo jednotlivě
porovnáno s původní maticí70(a); všechny souhlasí. X071 je dokončený průchod.

## Errata, vlastní opravy a reprodukce

Čerstvě porovnány SHA256 vzdálených originálů `all4b.ps.gz`, `all4f5.ps.gz`,
`err4b.textxt`, `err4f5.textxt`: všechny beze změny. Prohledány celé historické
i současné textové vrstvy, podle různých stránek i obsahu;39 kontextů
uchovává [errata-check.json](results/convex68/errata-check.json).
Odpovídající oprava1467→1647 nenalezena.

- E033:25.5.2021, odpověď70, `63];`→`63;`, v našem4B již zapracováno.
- E034:4.7.2020, odpověď72,1292687→1292697, rovněž zapracováno.
  Záznam této známé opravy ještě není úplnou kontrolou úlohy72.

První automatická aserce převzala1467 z knihy a selhala; následoval nezávislý
geometrický výčet, ne pouhé přepsání očekávané hodnoty. Vlastní pomocné chyby:
`pikepdf.Dictionary` nemá `.values()`; použití`.items()` opraveno. ParserDLX1
nejprve neuměl doplňující pole`cleansings` ve výstupuDLX3; zpracování bylo
opraveno před přijetím výsledků. První renderautorPS spletl tištěnou a
souborovou stranu; správně135+6=141, a teprve tato stránka je doklademF119.
Tyto chyby našich nástrojů nejsou nálezy v knize.

Reprodukční vstupy a výstupy jsou v `results/convex68/`. Zdrojový stav,
nezávislé kontroly, binárky a archivy mají SHA256. Již probíhající wrapper
se nespouští podruhé; po jeho dokončení se převezmou výstupy a aktualizuje
rozsahX068. Ostatní původní dlouhé úlohy běží samostatně.

```bash
python3 prepare_convex68.py
python3 run_convex68_counts.py
python3 check_convex68_symmetry.py
python3 check_bitland69.py
python3 check_bitland69_count.py
python3 check_dominosa70.py
python3 check_convex_dominosa_errata.py
```

Spouštět z adresáře tohoto auditu. Při nové reprodukci použít samostatný
checkout; nepřepisovat vstupy právě běžícího dlouhého výpočtu. Úspěšné
hotové kontroly není důvod opakovat bez změny nebo konkrétní pochybnosti.

## Převzetí dokončeného běhu při pokračování 2. listopadu

Původní DLX1 pro n=7 skončil: **18 187 302 řešení**, **163 499 709 uzlů**,
2 583 850 inicializačních a 2 901 169 011 107 vyhledávacích memů.
Profil je `1,200,8548,166158,2516757,24819194,117801549,18187302`.
Počet přesně souhlasí s dřívější nezávislou maskovou rekurencí; log a hashe
byly převzaty, výpočet se neopakuje. Aktualizovaný `counts-checkpoint.json`
uchovává tento dokončený výsledek. Tentýž původní wrapper už běží na n=9,
potom provede n=9 bez čtverce. X068 zůstává do jejich dokončení partial.


## 2. listopadu2026: dokončený původní DLX1 n9

Původní běh817294 dokončil 1.11.23:59:16 UTC všech **8113709 řešení**,
shodných s nezávislou maskovou rekurencí. Má **111286419 uzlů**,
5797027853800 memů hledání a profil uložený v
`results/convex68/n9-verified.json`. `check_convex68_n9.py` ověřil
zdrojové, binární, vstupní i výstupní hashe a celý profil bez opakování
výčtu. Původní wrapper808725 přešel na n9 bez čtverce (dítě853845).
X068 zůstává partial do dokončení poslední nezávislé kontroly.

## 2. listopadu2026: poslední výčet přijat, úloha68 uzavřena

Závěrečný původníDLX1 bez čtverce skončil v00:41:42UTC. Všech5 406 376
řešení souhlasí s nezávislou maskovou metodou; profil má83 027 265 uzlů.
Ověření `check_convex68_final.py` zkontrolovalo také vstupy, binárky,
zdroje a výstupní hashe. Všechny úlohy původního wrapperu jsou dokončené;
výše uvedené průběžné odstavce popisují dřívější stav. Společně s obecnými
důkazy, úplnými symetriemi a prověřenými citacemi je nyní X068 checked
a DLX:68 reviewed. Žádný plný výčet se kvůli převzetí neopakoval.

# Okraje a periodický dílek — 7.2.2.1, úlohy 127–128

Stav 2. listopadu 2026. Zadání je na tištěné straně 138, odpovědi na
447–448. Původní stránky byly zobrazeny; žádná nová chyba se v tomto
bloku zatím neprohlašuje za potvrzenou. Úloha 128 je prověřena včetně
obou obrázků. U 127 je úplná charakterizace přípustných okrajů hotová,
ale další početní a statistická tvrzení odpovědi zůstávají částečná.

## 127: právě všechny okraje se sudými četnostmi

Každá ze čtyř barev je na 18 hranách celé sady 24 dílků. Vnitřní hrana
spotřebuje dva výskyty téže barvy, takže počet výskytů na okraji musí
být sudý. Počet slov délky 12 se všemi čtyřmi četnostmi sudými je

    (2·4^12 + 8·2^12) / 16 = 2 099 200.

Jde o projekci na sudé exponenty v rozvoji (a+b+c+d)^12: sečteme hodnoty
pro všech 16 dosazení ±1 a dělíme 16. Stejný výsledek dává generátor
87 979 rozdělení pozic do nejvýše čtyř sudých tříd. Rozdělení s k třídami
přispívá 4!/(4−k)! pojmenovanými slovy.

Při postupném čtení hran kolem skutečného šestiúhelníku používáme pořadí

    -20 -30 /40 /41 \32 \23 -14 -04 /03 /02 \01 \10.

Geometrické rotace a zrcadlení byly odvozeny z transformací koncových
bodů hran a všech 24 buněk, nikoli z předpokládané permutace slova.
Na indexech i=0,…,11 mají tvar i↦i+j pro sudé j a i↦−i+j pro liché j.
Těchto 12 transformací s 24 přejmenováními barev dává 288 prvků.
Jejich akce má **7 889 orbit**. Úplný výčet je nezávisle ověřen
Burnsideovým součtem pevných slov a součtem velikostí orbit.

Pro každou z těchto 7 889 orbit je uložen **konkrétní platný vektor
všech 42 barev hran**. Samostatná geometrická kontrola potvrzuje každou
hraniční podmínku, shodu sousedních hran a použití všech 24 odlišných
dílků právě jednou. Zrcadlení zachová celou sadu dílků, i když zamění
chirální typy abc/acb; rotace a přejmenování ji rovněž zachovají.
Transformací svědků tedy dostáváme skládání pro všech 2 099 200 okrajů.
Spolu s paritou je to úplný důkaz odpovědi na vlastní otázku zadání.

Výpočet hledal jen prvního svědka každé třídy, nikoli všechny její
kompletace. Navštívil 5 093 057 uzlů, nejvýše 432 490 pro jednu třídu.
Počty svědků nelze vydávat za počty všech řešení.

## 127: co přesně znamená 4 054 a 576

Pokud na **abstraktním dvanáctiprvkovém cyklu** dovolíme i liché posuny,
dostaneme grupu o 24·24=576 prvcích a přesně **4 054 orbit**. Tento počet
z knihy je správný pro tuto abstraktní akci. Také tvrzení o jediné třídě
se stabilizátorem velikosti tři je správné: reprezentant je 001022021121.
Obě tvrzení kontroluje úplný generátor i nezávislý Burnsideův výpočet.

Posun o jedinou hranu však není izometrií triangulovaného šestiúhelníku.
Například sousední okrajové hrany na jedné přímé straně mohou patřit
dvěma různým trojúhelníkům, zatímco posunutá dvojice kolem rohu patří
jednomu trojúhelníku. Chybí důkaz, že abstraktní posun přesto zachovává
počet kompletací nějakou jinou bijekcí. Samotná absence geometrické
izometrie **není protipříkladem** takové případné bijekci.

Proto nebyla redukce na 4 054 použita v důkazu kompletovatelnosti.
Samostatná zaznamenaná fronta počítá přesné hodnoty pro
000000000011, 100000000001 a 000000000101. První dvě slova se liší
posunem o jednu hranu. V každém případě jsou a,b pevné barvy okraje
a c,d lze volně zaměnit; upravený C počítá polovinu označených řešení.
Tento faktor je volný, protože všechny dílky, tedy i ccc a ddd,
se používají. Práh volby primárních položek je Θ=c a CTH podle
největší barvy v názvu dílku, jako v dříve ověřeném 126.

Dvanáct omezených instancí invariantních vůči c↔d porovnalo **celé
množiny** původního a upraveného C, nejen konečné počty. Všechny
vypsané modely byly geometricky ověřeny. Těchto dvanáct nejmenších
testů má vždy pouze jednu barevnou orbitu, proto byly doplněny dvě
širší domény: 6 096 a 38 764 označených řešení. U nich se porovnávají
celé množiny původního C, upraveného C i nezávislého bitsetového řešiče;
přijetí všech tří je v `counts127-wide-checked.json`. Plné běhy mají vlastní
terminální metadata a limit 48 hodin na případ; průběžné výstupy
nejsou přijaté konečné počty. Zdrojové moduly zůstávají zmrazené.

Dosud neuzavíráme knižní počty 48 620 416 / 49 941 040, jejich pořadí
mezi všemi okraji, použití abstraktních symetrií na kompletace ani
globální statistický odhad více než čtyřnásobku bílého okraje a
pravděpodobné horní hranice 500 milionů. Kniha poslední tvrzení uvádí
jako Monte Carlo odhad, nikoli jako dokázanou deterministickou mez.
Počet 11 853 792 pro bílý okraj je již úplně přijat v bloku 126;
není znovu počítán.

## 128: úplný výčet a význam počtu 1 032

Sada tříbarevných dílků má podle Burnsidea (3^3+2·3)/3=11 typů:
tři monochromatické a osm dalších. Každá buňka tedy má 3+8·3=27
orientovaných možností. Oblast R tvoří buňky (x,y,z), x=0,1,2,
y=0,1, z=0,1, bez (2,1,1). Označení 2×3 v textu chápeme jako dvě
řady a tři sloupce; přesné souřadnice i obrázek jednoznačně souhlasí.

Má 21 geometrických hran. Identifikujeme tři uvedené páry

    -00 = -20, /01 = /30, -02 = -12.

Kódování má 22 primárních položek (buňky a dílky), 18 barevných
sekundárních položek a 11·27=297 možností. Každé řešení je bijektivně
skládáním R se všemi 11 dílky a těmito okrajovými rovnostmi.

Původní nezměněný DLX2 i nezávislý řešič s neměnnými konfliktními
bitovými množinami vypsaly všech **6 192 označených skládání**.
Celé množiny jsou totožné. Geometrický validátor kontroluje také
skutečné koncové body hran, nejen shodu názvů položek.

Po ztotožnění šesti globálních permutací tří barev je přesně **1 032
tříd**, každá velikosti šest. To je interpretace knižního počtu;
odpověď normalizaci barev výslovně neopakuje. Pro čtenáře je vhodné
ji uvést, ale tento běžný rozdíl v konvenci nepovyšujeme automaticky
na novou chybu. Hodnotu 1 032 neoznačujeme jako nekrácený počet.

První přijímací kontrola očekávala 1 032 nekrácených modelů a správně
se zastavila na 6 192. Hotový nativní běh se neopakoval: doplněna
explicitní normalizace a nezávislý druhý výčet, které objasnily faktor šest.

## 128: obecný důkaz pokrytí nekonečné roviny

Ve vrcholových souřadnicích z úlohy 124 použijme podmřížku L s bází
(3,−1),(2,3). Determinant je 11; L je přesně jádro homomorfismu

    φ(x,y) = x−8y mod 11.

K R přidejme kopii otočenou kolem bodu (3/2,0), tj. vrcholy zobrazme
(x,y)↦(3−x,−y). Na trojúhelnících je to
(x,y,z)↦(2−x,−1−y,1−z).

Celkem 22 buněk má všech 22 různých dvojic (φ(x,y),z). Jsou tedy
úplným systémem reprezentantů trojúhelníků modulo L. Jejich posuny
o L pokryjí **celou rovinu právě jednou**, bez překryvů a mezer.
Toto je konečný důkaz nekonečného tvrzení, nikoli extrapolace z obrázku.

Hrany v kvocientu jsou určeny typem −,/ nebo \ a hodnotou φ svého
počátečního vrcholu. Je jich 3·11=33, každá má dva incidentní trojúhelníky.
Porovnání barev původní a otočené kopie dává buď totožnou proměnnou,
nebo právě jeden ze tří vytištěných párů. Žádná další rovnost nevzniká.
Uvedené tři podmínky jsou tedy nutné a postačující pro barevnou shodu
všech hran této periodické konstrukce. Platí to pro každé ze skládání.

## 128: původní obrázky

Z vektorových cest původní PDF strany 448 bylo vyčteno všech **1 055
barevných výsečí**. Malý příklad má 33 výsečí, všech 11 odlišných dílků,
správné souřadnice, návaznosti a okrajové rovnosti; jeho přesný barevný
vektor je členem celé ověřené množiny 6 192 řešení.

Velký výřez má 1 022 nakreslených výsečí, uspořádaných do 359 buněk:
304 úplných a 55 s pouze dvěma viditelnými výsečemi. Všechny souhlasí
s periodickým pokračováním právě malého příkladu; při zvolené souřadnicové
normalizaci je fáze φ posunuta o šest. Samostatně souhlasí i všechny
viditelné sdílené hrany. Chybějící ořezané výseče nejsou vydávány za
viditelné údaje knihy. Největší zaokrouhlovací odchylka souřadnic je
uložena ve výsledku extraktoru.

## Errata a reprodukce

Prohledáno všech šest relevantních historických a současných textových
vrstev, včetně obou autorových TeXů. Čtyři aktuální autorovy soubory byly
znovu staženy a jejich SHA-256 jsou stejné jako archivované. Pro 127–128
nenalezena odpovídající oprava. Zásah z 21. října 2021 na straně 256
vydaného Fascicle 5 opravuje jinou část odpovědi 129, již zapracovanou
v lokálním 4B; nepřisuzujeme jej úloze 128.

- `border_orbits127.py`: oba úplné orbitové cenzy a Burnsideovy kontroly.
- `border_witness127.cpp`, `check_border_witness127.py`: svědci a validace.
- `borders127_128.py`: izolované modely, geometrie a důkaz kvocientem.
- `run_border_counts127.py`: omezené porovnávací případy a živá fronta.
- `check_supertiles128.py`: celé množiny dvou řešičů a normalizace barev.
- `extract_supertiles128.py`: všech 1 055 výsečí původních obrázků.
- `results/borders127_128/`: vstupy, celé modely, hashe a koncové protokoly.

K opětovnému přijetí výsledků slouží `check_borders_checkpoint.py`;
nespouští nové hledání. Úspěšné výčty se bez konkrétního důvodu neopakují.

## Doplnění 2. listopadu 2026: první úplný počet z fronty

Případ `side11`, okrajové slovo `000000000011`, dokončil **24 310 208**
tříd po výměně dvou nepoužitých okrajových barev. Tato výměna působí
volně, proto jde o **48 620 416 označených řešení**, přesně podle knihy.
Každý z 243 vypsaných modelů byl geometricky validován. Přijat je
koncový záznam s nulovým návratovým kódem, zdrojem, binárkou a všemi
vstupními a výstupními hashi; hledání se neopakuje.
[Samostatný doklad](results/borders127_128/side11-count-checked.json).

Fronta pokračuje `corner11` a `separated101`. První dokončený počet
sám neprokazuje, že abstraktní posun hranice o jednu hranu zachovává
počty kompletací, ani neověřuje všechny globální statistické odhady.
Úloha 127 zůstává částečná. Nové přijetí je součástí checkpointu 129;
starý checkpoint 127–128 je zachovaný historický stav.


## Přijetí dokončeného rohového případu 2. listopadu

Uložený terminál corner11 pro okraj `100000000001` má **26 277 908**
orbit záměny c/d, tedy **52 555 816** označených řešení. Kontrolní
součty a všech 262 vypsaných geometrických svědků znovu ověřil pouze
akceptační skript `accept_corner127.py`; žádné hledání se neopakovalo.
Výsledek je v `results/borders127_128/corner11-accepted.json`.
Fronta 978039 později v tomto bloku řádně dokončila také separated101: **24 970 520** orbit, tedy **49 941 040** označených řešení. Akceptační skript `accept_separated127.py` ověřil uložený terminál a všech 249 vzorků. Celá fronta je hotová a nesmí se restartovat. Dřívější mezery
v interpretaci abstraktních posunů, nezávislém úplném počtu a globálních
statistických odhadech zůstávají otevřené.

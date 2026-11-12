# Spojené a dosažitelné podmnožiny, 7.2.2–75–78

Kontrola 1. listopadu 2026: celé zadání a odpovědi na stranách 62–63,
413–414. `check_connected.py` obsahuje doslovný stavový přepis R1–R6;
nezávislý oracle vypisuje všechny podmnožiny a zkouší dosažitelnost.
Výsledky jsou v `results/connected/verified.json`.

## Úlohy 75–77

Všech 21 miniatur bylo přečteno přímo z poloh znaků původního PDF.
Jejich pořadí i všech pět čísel v každé miniatuře souhlasí s algoritmem
a s nezávislým BFS. Ze zdrojových vektorových cest bylo vyčteno také
všech 45 teček vyloučených vrcholů; přesně odpovídají nenulovému TAG
mimo právě zvolenou množinu. V orientované mřížce selžou právě obrázky 13 a 18.

Algoritmus prošel 26 705 úplnými případy neorientovaných grafů do pěti
vrcholů a 66 129 případy orientovaných grafů do čtyř vrcholů; každá
kořenová/velikostní volba je samostatný případ. Kontrolují se přesné
množiny a kanonická pořadí, nikoli pouze počty. Dále 2 000 náhodných
grafů s přeházenými seznamy sousedů a předem vyloučenými vrcholy.

Invariant: TAG je součet počátečních značek a dosud navštívených konců
hran v kanonickém BFS průchodu. Při prvním setkání s vrcholem může
algoritmus buď tento vrchol přidat, nebo jej ponechat označený jako
vyloučený. Následné výskyty téhož vrcholu nemohou vytvořit další volbu.
Každá dosažitelná množina určuje jednoznačně právě tuto posloupnost voleb.

Při návratu R6 byly úplně prohlédnuty seznamy v_k pro l ≥ k > i;
z rodičova seznamu byla prohlédnuta část za uloženou hranou a_l.
Odečtení právě těchto příspěvků obnoví předchozí stav, včetně značky
TIP(a_l), který je nyní vyloučenou volbou. To dokazuje správnost obnovy
i úplnost enumerace. U neorientovaného grafu má každý přidaný vrchol
aspoň vstupní hranu; u digrafu může být jeho seznam prázdný, proto je
návrat R4 na sebe v 77(d) nutný. To není chyba původního algoritmu.

Pro 77(b) volba rodiče s o jednotku menší vzdáleností od v dává strom:
vzdálenost po rodičích ostře klesá. Opačný směr je cesta ve stromu.
U neorientovaného grafu jsou dosažitelnost a souvislost ekvivalentní.

V 76 se množina přiřadí svému nejmenšímu vrcholu. Zkratka s přenášením
TAG byla ověřena i během všech velkých běhů: po skončení zůstane navíc
právě značka kořene, pokud odečteme jeho celý seznam sousedů.
Případ n=1 se obsluhuje zvlášť, jak odpověď výslovně požaduje.

Počty umístění n-omin do n×n jsou
1, 4, 22, 113, 571, 2816, 13616, 64678, 302574. Nezávislá metoda
postupně přidává okrajový čtverec, normalizuje posunutí a deduplikuje
celé tvary. Počet jejich umístění je (n−šířka+1)(n−výška+1).
Obě metody dávají všech devět stejných výsledků.

## Úloha 78 a F098

První věta odpovědi vypíše singleton vždy, když WT(v)<U. Chybí test
WT(v)≥L. Dva sousední vrcholy váhy 1, L=2, U=3: při kořeni v knižní
postup vypíše {v} i {v,u}, přestože platná je jen dvojice.

Oprava: po horním testu vypisovat singleton pouze při WT(v)≥L,
ale pokračovat v rozšiřování i při menší váze. Nezáporné váhy zaručují,
že horní ořez R5' nevyloučí žádné platné rozšíření. Kromě singletonu
je navržená úprava správná: nové w se rovná součtu aktuálního prefixu,
R6 odečte právě odebraný vrchol. Nulové váhy nezpůsobí cyklus, protože
se stále přidávají jen nové vrcholy konečného grafu.

Úplná kontrola 112 974 vážených případů zahrnuje všechny malé digrafy
i neorientované grafy do tří vrcholů, váhy 0/1/2, různé dolní a horní
meze, prázdné intervaly a dolní mez −1. Náhodné větší případy navíc
zkoušejí předem vyloučené vrcholy. Opravená verze vždy souhlasí s
úplným výčtem. Pro všechny souvislé množiny se použije kořenový rozklad
z 76; pro digrafy je ověřena verze s pevným kořenem a v-dosažitelností.

## Originály a errata

Zobrazeny původní strany PDF 62, 63, 414 a autorův PS `fasc5b`, str.52
(11. září 2019). Chybějící dolní test je v obou. Záměny ≠ za =
v prostém OCR se nepočítají jako chyby.

Známé opravy Fascicle 5 p.222 z 5. února a 12. května 2020 mění
p≥L na w≥L a doplňují v←v_i do R6. Naše 4B je už obsahuje;
neopravují počáteční singleton. Změna 77 z 1. června 2021 je sazba
značky orientované cesty. Prohlédnuté historické i aktuální vrstvy a
jejich hashe jsou v `results/connected/errata-check.json`.

F098 má návrh `knuth-report-f098-draft.txt`. Fyzický výtisk se nekontroloval;
žádný návrh nebyl odeslán.

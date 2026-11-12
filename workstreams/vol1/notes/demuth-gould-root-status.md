# V1-X0781–X0782: Demuth, Gould a převzetí asymptotických pramenů

Demuthův titul a říjnové datum 1956 jsou přímo doloženy původní
ukázkou disertace. Identita Gouldova časopiseckého příspěvku je
doložena metadaty. Citované obsahové pasáže obou zdrojů nadále
chybí; hlavní text §1.2.11.3 zůstává partial.

Root ověřil všech 54 souborů a 15 závislostí dílčího manifestu
`parallel/asymptotic-primary-followup/results/demuth-gould-source-limits-manifest.json`,
SHA-256 `48cad77c4fac22b171eeceb7bac66c907d51e61544db8a2e0f37aa20a5fd5e05`,
a přečetl úplnou poznámku a stavový záznam. Následně ověřil celý
zmrazený archiv, 294 souborů a 62 závislostí; jeho MANIFEST má SHA-256
`71aebf1adf394468351fc3ff7b9d9bd303ada6377e8d30fbc3f6410682e7a3b6`.
REPORT, UNIT_STATUS a souhrn SOURCE_STATUS byly porovnány s již
přijatými dílčími kontrolami. Přebírání celého archivu neznamená
novou četbu všech jeho uložených stran nebo opakování starých testů.

## Demuth: původní datum, omezená ukázka

Root přímo četl titul (PDF1), obsah na vii (PDF7) a poslední
dostupnou stranu 12 (PDF20) veřejné ukázky Electronic Data Sorting.
Titul uvádí Howard B. Demuth, Stanford University, Department of
Electrical Engineering, October1956. Katalogové 1957 tudíž není
nález v Knuthově bibliografii. Agentův širší rozsah je i–viii a12;
získané vlastní strany1–11 nebyly obsahově auditovány.

Ukázka obsahuje pouze i–viii a1–12, celkem20stran. Její původní PDF
má1 007 861B, SHA-256
`ee3e884b7c841cd5d9ad9e6129aa94d6a92794a9fc6af09780f63c2db4748756`.
Pochází z veřejného odkazu katalogu
https://www.proquest.com/docview/301940891. Dochovaný katalogový
výtah je výslovně odlišen od původního HTML; metadata popisují
derivaci i hash původní odpovědi. PDF je nezměněné.

Obsah umisťuje IV.A.1, analýzu modelu Circular-Nonreversible-Memory,
na60–68; další oddíl začíná69. To je správný kontext Knuthovy citace,
ale z konkrétních67–68 nebyla získána ani přečtena žádná strana.
Strana12 teprve otevírá shrnutí třídicích činností. Nemůže doložit
první asymptotický člen sqrt(pi*n/2) pro konkrétní funkci P(n)
definovanou v TAOCP §1.2.11.3. Zbývá ověřit původní veličinu,
normalizaci a vztah právě k tomuto P(n), nikoli jen existenci
nějakého odmocninového odhadu. Článek IEEE1985 je jiná publikace;
získaná metadata ho nenahrazují za původní disertaci.

## Gould: totožnost není obsah bibliografie

Root přímo přečetl uložená metadata Crossref: problém5541,
Robert Breusch a H.W.Gould, AMM75(9), listopad1968, počáteční1019,
DOI10.2307/2315564. Úlohy zadavatele a řešitele i úplný rozsah1019–1021
doplňuje pouze indexovaný autorův seznam, označený v archivu jako
vyhledávací navigace. Jeho chybný ročník72 není chyba TAOCP.
Přímý seznam se nepodařilo stáhnout a nepředstíráme jeho četbu.

Kniha na121 odkazuje konkrétně na Gouldovu bibliografii dalších
výzkumů funkce Q(n) definované v téže sekci. Z originálu1019–1021
bylo získáno a přečteno nula stran. Prázdný seznam referencí v Crossref
nevypovídá o skutečné bibliografii článku. JSTOR odpovědi, omezený
archivní sešit a neověřený Taylor–Francis identifikátor jsou
zdokumentované přístupové pokusy, nikoli obsahová evidence.

X0781 uzavírá pouze Demuthovo původní datum a bibliografickou
identifikaci Gouldova příspěvku. X0782 zachovává obě obsahové mezery.
Žádný nový nález ani závěr o globální nedostupnosti zdrojů nevzniká.

## Kniha, errata a celek archivu

Root přímo četl TAOCP120 a při navazující Ramanujanově kontrole121;
agent v tomto paketu četl obě strany. Všechny čtyři vrstvy errat
byly prohledány podle stran a jmen. Doplněná rejstříková jména2022
nevyplňují obsahové mezery. Známá oprava Ramanujanova koeficientu
je odděleně přijata v X0772. Fyzický výtisk TAOCP nebyl kontrolován.

Celkový archiv zachovává již přijaté kontroly Cauchyho, Tricomiho,
Carlitze, Barnese/Watsona, Ramanujana, Furcha a de Bruijna. Přesná
edice de Bruijn1961 nadále čeká na kolaci a Rousseau159–161 chybí.
Úloha20 zůstává partial. Starší důkazy a C0016–C0019 se nemění;
Temme, Odlyzko, Keller a Knuthovo vlastní svědectví jsou zachovány
jen v dosavadním přesném rozsahu. Žádné již úspěšné matematické
testy se neopakovaly.

# Stav po souvislém průchodu prvním svazkem

6. listopadu 2026, X0985. Původní dostupný svazek je prošlý od první
do poslední stránky. Závěr není „všechno dokázáno“: všech 665 stran
má explicitní záznam, ale 19 úloh, 24 z 51 hlavních textových oddílů
a 22 kandidátů mají níže vymezené otevřené části. Tyto stavy se
nepřepisují na checked jen proto, že skončil průchod knihou.

V UI je 310 zelených, 290 červených a 65 oranžových stran; šedých
zbývá 0. Červená zahrnuje také staré zveřejněné opravy, takže 290
není počet nových nálezů. Červená stránka může mít zároveň dosud
nevyřešenou část. Ve svazku je 913/932 původních sekčních úloh
uzavřených ve vymezeném rozsahu a všech šest dodaných čísel úloh.
Úvodní čtyři úlohy se počítají odděleně. Ledger má 70 potvrzených
nálezových záznamů, včetně veřejně známého C0001; nejsou to nové nálezy
tohoto posledního průchodu ani autorovo potvrzení jejich novosti.

## Devatenáct částečných úloh

| Sekce a úloha | Co přesně není uzavřeno |
|---|---|
| 1.2.5–4 | Uhlerova původní tabulka a tvrzení o Wrenchovi, době ruční práce a 2,5 minutách. Aritmetika 1000! je ověřená. |
| 1.2.5–13 | Historický rok Leibnizovy znalosti Wilsonovy věty, C0087. Samotná věta a důkaz jsou ověřené. |
| 1.2.6–53 | Přenos celočíselného oboru z (a) do (b), C0009; pro m = −1, n = 1 vzniká 0 versus 1, pro zamýšlené nezáporné m je důkaz hotový. |
| 1.3.1–16 | Obecná dolní mez prostoru při libovolné samomodifikaci; omezené třídy nestačí na globální minimum. |
| 1.3.1–17 | Globální časové optimum, nikoli správnost uvedených programů nebo přijaté tříslovné prostorové minimum. |
| 1.3.1–22 | Globální minimum sedmi slov bez časového omezení; čas 4u a prostor mezi 4u programy jsou doložené. |
| 1.3.1–23 | Globální prostorové minimum; opravený kontrakt znaménka nuly je doložen C0083. |
| 1.3.2–20 | Pořadí současného vnějšího požadavku a testu JOV na přechodu světel. Fáze, blikání i časy jsou pro definovaný model dokázané. |
| 2.2.2–18 | Zda se amortizovaná mez vztahuje i na inicializaci (11), C0035. Pro inicializaci (13) uvedený protipříklad neplatí. |
| 2.2.5–10 | Zadání vyžaduje skutečné pozorování vybraného výtahu. Simulátor není takovým měřením. |
| 2.3–11 | Význam počtu různých kardinálních úrovní, C0045. Samostatná chyba závěrečné poznámky je již C0056. |
| 2.3.1–19 | Zda je prozaická basic idea určena i pro konec průchodu u kořene, C0049; doplněný test HEAD je dokázaný. |
| 2.3.1–32 | Zda single node již předpokládá izolovaný list s nulovým LLINK, C0046; při tomto předpokladu postup funguje. |
| 2.3.4.4–17 | Katzova historická priorita proti datovanému Rubinovu–Sitgreavesové prameni, C0071. Matematika vzorce je doložená. |
| 2.5–18 | Původní proud požadavků pro přesnou reprodukci obrázků 42/43 chybí. Algoritmické porovnání samotné jej nenahrazuje. |
| 2.5–27 | Implicitní inicializace zvláštní hlavy sentinelového seznamu, C0074. Plusový TAG s nulovým odkazem nestačí. |
| 2.5–32 | Úplné vyhodnocení přesné racionální limity. Je dokázána existence, konečný regenerační vzorec a interval 11.03203 ≤ α < 12.99721822. |
| 2.5–39 | Historické tvrzení, že přesné N(m) nebylo známo pro žádné m > 2. Subaditivita, limita a číselné meze jsou ověřené. |
| 2.5–40 | Koeficient 1.1825 u ln m není doložen ani vyvrácen. Konkrétní chybně popsanou strategii vyvrací C0091; výzkumná otázka a výslovná harmonická domněnka se nepovažují za nové věty. |

U posledních výzkumných úloh audit nevyžaduje nově vyřešit otevřený
problém. Přesně neověřený číselný údaj nebo tvrzený koeficient se však
nesmí vydávat za dokázaný. Pro α by přímé vyhodnocení znamenalo
obrovský konečný strom či stavový prostor. Podle uživatelova výpočetního
omezení se nespouští další hrubá síla ani se neopakuje starý běh
52 milionů událostí. Zachováváme dostupný rigorózní výsledek a přesnou
mez, nikoli nové tvrzení o přesné číselné hodnotě.

## Závěrečná revize interpretačních kandidátů

Znovu přímo porovnány 73, 138, 141, 317, 327, 333, 562, 566, 570,
455–456, 615–616 a sentinelové 611–612. Přečteny konkrétní původní
důkazy a sémantické meze C0009, C0020, C0045, C0046, C0049 a C0074.
Žádný z nich se touto revizí automaticky nepotvrzuje:

- Úloha 53(b) neudává vlastní obor a odvozuje vzorec z části (a).
  Výpočet pro záporné m je správný; zamýšlené omezení prefixu zůstává
  otázkou formulace, nikoli numerického testování.
- Tabulka MIX společně uvádí NUM/CHAR/HLT, ale přímá definice času
  HLT je 1u plus čekání. Stejná tabulka také zkracuje floating varianty,
  jejichž časy text výslovně nespecifikuje. Pro algoritmické časování
  používáme přímou definici; kandidát se týká tabulkového vyjádření.
- U příkladu nekonečného stromu mají všechny uzly přesně kontinuum
  předků. Kardinální funkce level proto nabývá jedné hodnoty, zatímco
  hierarchie má nespočetný řetězec. To jsou rozdílné matematické výroky;
  nejistota je v použití slova levels, ne v tomto výpočtu.
- Inicializace vloženého Q s LLINK(Q) = P dává cyklus. Nevyvrací
  variantu, která vyžaduje Q již jako izolovaný list. Stejně tak
  prozaický postup následníka potřebuje zvláštní ošetření kořene,
  pokud má sám tvořit úplný algoritmus.
- Plusový TAG sentinelu s nulovým dopředným odkazem dává po LD4N
  zápornou nulu a J4NN pokračuje. Standardní hlava odkazující na sebe
  má nenulový odkaz a funguje. Bez rozhodnutí o kontraktu nejsou
  další desítky testovaných radixů novým důkazem chyby.

U semaforů znovu přijaty úplné součty času a uložené kontroly podle
`mixal-traffic.md`; neurčenou souběžnost nelze určit simulací.
U náhodné životnosti je původní „asi 14“ výslovně nejistý empirický
odhad. Lepší interval nezakládá chybu v tvrzení přesné hodnoty,
protože kniha takovou přesnost netvrdí.

## Ostatní fakta a další postup

24 částečných hlavních oddílů obsahuje zejména konkrétní historické
priority, soukromé atribuce, původní měření a některé uvedené kandidáty.
Strojový soupis `results/sequential-pass-summary-2026-11-06.json`
uchovává všechny aktuální odkazy na důkazy, částečné sekce i 22 kandidátů.
Původní frontmatter i, xv–xvii, xx stále chybí. Appendix A má otevřené
Wrenchovo historické tvrzení; index má deset původních a šest novějších
částečných cílů. Bibliografické výjimky z jednotlivých sekcí platí dál.

Krátká nová kontrola dostupnosti Krogdahla a přesného koeficientu 1.1825
nepřinesla čitelný původní důkaz. Vydavatelův
[záznam Krogdahla](https://www.sciencedirect.com/science/article/abs/pii/0020019073900252)
potvrzuje strany 96–99; přímé otevření textu vrátilo 403. Metadata ani
pozdější bibliografické seznamy nedokazují hledanou mez. Pokusy a přesné
dotazy jsou zaznamenány ve zdrojových metadatech; nevydáváme chybějící
článek za přečtený.

Souvislý průchod pokračuje svazkem 2 od jeho úvodu. První svazek zůstává
výslovně neuzavřený v uvedených bodech a vrací se do fronty následné
revize. Nepotřebujeme opakovat jeho již přijaté výpočty, abychom mohli
prověřovat nové stránky dalších svazků. Žádný proces nebyl spuštěn,
nový nález v X0985 nepřibyl a žádná korespondence nevznikla.

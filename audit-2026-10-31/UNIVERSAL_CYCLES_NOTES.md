# DLX94–100: univerzální cykly, torusy a obecné redukce

Kontrola 2. listopadu 2026. Lokální 4B, druhý dotisk 2022, zadání str. 134,
odpovědi 437–438. Vykreslené stránky porovnány s autorovým PS 5C,
str. 141–142. Nová potvrzená chyba z tohoto bloku nevznikla. C028 je
kandidát na doplnění normalizace; E047 je již zveřejněná oprava odpovědi 98.

## Přesný rozsah

| Úloha | Co je prokázané | Co zůstává |
|---|---|---|
| 94 | Úplných 65 536 binárních přiřazení; celá množina 64 řešení souhlasí s doslovným interpretem i původním DLX2. Jedna třída při rotaci, reflexi a komplementaci. | Původní Flye Sainte-Marie 1896, str. 155–161, nebyl získán; historická atribuce není uzavřena. |
| 95 | Obecná XCC bijekce a všechny tři úpravy primárních položek; oba tiskové cykly; přesné počty 137 216 a 41 280 determinantem i DLX2; čtyři rychlé benchmarky. | Běží jediný dlouhý benchmark s druhotnými a-položkami, uváděný přibližně 50 T mems. Přesné historické vstupní pořadí není doložené. |
| 96 | Všech 80 tříd binárních torů podle posunů; nezávislé úplné množiny DLX2 / přiřazování buněk; tiskový obrazec i křížové okno na zobecněném toru. | Nic v zadané konstrukci; netvrdíme počet bez podmínky komplementárních čtyř řádků. |
| 97 | Celý počet a všechny modely oběma metodami; symetrie, všech 81 oken, transpozice a její dvojice. | C028: popsané zafixování typu samo nevybere jediného zástupce zbývajících tří posunů. |
| 98 | Obecný důkaz NP-úplnosti po aplikaci E047; 2 097 úplných malých SAT kontrol. | Nic v opraveném důkazu. |
| 99 | Obecný důkaz identity množin vybraných možností, včetně neobarvených výskytů; 2 586 úplných kontrol. | Nic. Podezření na neobarvené výskyty vyvrací definice na str. 88. |
| 100 | Všech pět odpovědí, všech 31 možností; obecná redukce konečného CSP a normalizace domén; 1 000 úplných relačních kontrol. | Nekonečné relace nejsou konečné vstupy Algorithm C; neděláme o nich tvrzení. |

Hlavní výsledky: `results/universal_cycles/cycles-checked.json`,
`tori-checked.json`, `reductions-checked.json`, `benchmarks-checked.json`.
Samostatné poznámky k dřívějším úlohám 91–93 zůstávají ve
[WORD_STAIRS_NOTES.md](WORD_STAIRS_NOTES.md).

## 94: čtyři místa v binárním cyklu

Z primárních položek p_k vybereme právě jednu čtveřici pro každou pozici k.
Primární položky j zajistí všech šestnáct vzorů, barevná x_k jejich vzájemnou
shodu v každé buňce. Naopak každý požadovaný cyklus určuje právě těchto
šestnáct možností. To je bijekce, nikoli pouze nutná podmínka.

Zcela nezávislý přímý průchod všech 2^16 slov kontroluje okna na offsetech
(0,1,3,4). Dostane 64 slov, která se jako celá množina shodují s oběma XCC
výčty. Všechna jsou v orbitě vytištěného `0000011010111011` při rotaci,
obrácení a záměně bitů; samotná rotace dává čtyři třídy. V každém platném
slově je šestnáct různých oken, proto rotace působí volně.

Původní článek není nahrazen citací z nového Knuthova přepisu. Internet
Archive v uloženém dotazu nalezl jiné ročníky časopisu, nikoli svazek 3;
Gallica SRU vrátilo 403. Obojí je zaznamenáno v
`sources/universal_cycles/history-search.json`. Chybějící historický doklad
není důvod opakovat již dokončený matematický výčet.

## 95: nezávislý determinant a normalizace

Nechť W obsahuje povolená n-bitová slova a m=|W|. Platí m≥n+1: součet
obsahuje alespoň dvě sousední binomická čísla, jejichž součet je
C(n+1,p+1)≥n+1. Každá možnost tedy používá n různých buněk.

Primární a_j zajišťují jednu možnost pro každou pozici, b_k každé slovo
právě jednou. Barvy slepí překrývající se slova do cyklu; opačný směr je
jednoznačný. Pevné slovo k=0 se vyskytuje právě jednou, takže jeho umístění
do j=0 bezpečně odstraní faktor m. Zbývá 1+(m−1)^2 možností.

Je-li b sekundární, m vybraných možností má různá b a tím je pokryje všechna.
Stejný argument funguje pro sekundární a při primárních b. Dokonce lze a
vynechat: dvě možnosti ve stejné pozici by barevnou shodou určovaly totéž
slovo k, ale primární b_k jejich současný výběr zakáže. Tím je zachována
množina řešení ve všech čtyřech variantách. Výběr větví se ovšem mění.

Nezávislé počítání používá orientovaný graf. Každé slovo W je hranou z jeho
(n−1)-bitového prefixu do suffixu. Cyklus všech slov je Eulerův okruh;
zafixujeme jeho první hranu. Oba zde počítané grafy jsou vyvážené a silně
souvislé, což checker ověřuje přímo.

Při zápisu Eulerova průchodu určuje poslední odchozí hrana z každého vrcholu
mimo počáteční kořen strom orientovaný ke kořeni. Zbývající odchozí hrany
lze lokálně uspořádat; u kořene je první hrana již zafixovaná. Naopak průchod
v tomto lokálním pořadí nemůže uvíznout před spotřebováním všech hran:
nepoužité poslední hrany by podle stromu vedly zpět ke kořeni. Dostáváme
bijekci se stromy a lokálními pořadími. Počet je

`t_root · ∏_v (outdeg(v)−1)!`.

V našich binárních grafech jsou stupně nejvýše dva, takže součin je 1.
Počet t_root je kofaktor odchozího Laplaciánu. Smyčky se na diagonále
odečtou; jejich započtení by bylo chybné. Determinantová identita odpovídá
standardnímu vyrušení výběrů obsahujících orientovaný cyklus; zbývají právě
volby jedné hrany z každého nekořenového vrcholu směřující do kořene.

| Parametry | Hrany | Vrcholy | Přesný determinant / počet cyklů |
|---|---:|---:|---:|
| (7,0,3) | 64 | 42 | 137 216 |
| (7,3,4) | 70 | 50 | 41 280 |

Vlastní celočíselná Bareissova eliminace kontroluje každé přesné dělení;
nezávislá metoda `sympy domain-ge` dává stejné determinanty. Silnější
kontrolou modelování jsou všechny případy 1≤n≤4: přímý úplný průchod
binárních cyklů, determinant a čtyři XCC varianty mají vždy stejné počty,
XCC varianty navíc celé stejné množiny znormalizovaných slov. Vytištěné
cykly ze str. 134 mají správně 64 a 70 bitů a každé požadované okno právě
jednou; původní podezření na zkrácení bylo mylné.

Původní DLX2, úplné terminální běhy:

| Parametry a varianta | Řešení | Uzly | Vyhledávací mems po odečtu lmems |
|---|---:|---:|---:|
| (7,0,3), obě sady primární | 137 216 | 4 904 580 | 8 419 828 545 |
| (7,0,3), b sekundární | 137 216 | 5 042 105 | 8 054 682 875 |
| (7,3,4), obě sady primární | 41 280 | 1 675 813 | 3 190 670 977 |
| (7,3,4), b sekundární | 41 280 | 1 737 092 | 3 059 283 505 |

To podporuje uváděné přibližné náklady 8,5 / 3,2 G a tvrzení o větším stromu,
ale menších nákladech sekundárních b. Není to přesná shoda prvního čísla:
8,420 G nezaokrouhlíme vydávaně na 8,5 G. Původní pořadí vstupu ani přesná
historická implementace nejsou doložené; z rozdílu asi jednoho procenta
nevytváříme nález. Skutečné nástěnné časy při dalších paralelních výpočtech
nejsou důkazem kauzálního zrychlení.

Jediný nový dlouhý běh je `run_universal95_slow.py`, wrapper PID 882581,
varianta sekundárních a, s limitem 48 hodin. Má uložený vstup, příkaz,
kontrolní součty, PID i průběžný log. Timeout znamená incomplete. Moduly
`universal_cycles.py` a `run_universal_native.py` jsou po dobu běhu zmrazené.

## 96: torus 8×8 a zobecněné křížové okno

Při komplementárních spodních čtyřech řádcích stačí volit horních 32 bitů.
Každé 2×3 okno má v dolní polovině svůj komplement. Dvojice vzorů tedy
reprezentujeme 32 třídami, například vzory začínajícími nulou. XCC přiřadí
každou třídu právě jedné z 32 pozic v horních čtyřech řádcích a zahrne obě
možné základní barvy. Přechod přes spodní okraj proužku obrátí bity.

Jediné all-zero okno posuneme do (0,0), čímž dostaneme jednoznačného
zástupce každé translační třídy. DLX2 má 80 výsledků. Nezávislý C++ program
přiřazuje bity přímo buňkám a při dokončení okna odmítá opakovanou třídu.
Prošel 96 575 uzlů a dostal tutéž celou množinu 80 tabulek. Kontrola každé
rozvinuté tabulky ověřila všech 64 různých fyzických oken. Jejich všechny
posuny dávají 5 120 různých označených matic; tedy 80 je počet torů podle
posunů, nikoli počet matic s pevným počátkem. Tištěná tabulka je přímo mezi
těmito 80 zástupci.

Pro kříž je podklad Z² / ⟨(4,4),(4,−4)⟩, který má 32 pozic. Použité
reprezentanty mají 0≤x<8, 0≤y<4 a redukci
`(x,y) ↦ ((x−4 floor(y/4)) mod8, y mod4)`.
Checker ověřuje oba generátory, pět různých sousedů a všech 32 binárních
vzorů konkrétního svědka. Původní DLX2 byl záměrně zastaven po prvním
řešení (`t1`); žádný celkový počet křížových torů se netvrdí.

## 97: úplné množiny a kandidát C028

Podmínka `D[r+3,c+3]=D[r,c]+1 mod3` určuje celou matici z prvních tří
řádků. Čtyřbuněčné okno normalizujeme odečtením levého horního prvku;
zůstane typ (a,b,c), tedy 27 možností. Každý typ musí být právě jednou
mezi 27 pozicemi třířádkového proužku; zbývající dvě kopie téhož typu
vznikají posunem (3,3) a přidáním barvy. To přímo dokazuje XCC bijekci.
U přechodu z řádku 2 jsou správné indexy k−3,k−2 a barvy i+b−1,i+c−1.

**Pouhé spárování typu 00 s pozicí p00, jak text výslovně říká, dává
17 388 řešení, nikoli 5 796.** Rozdělení podle d00 je přesně
5 796 + 5 796 + 5 796. Každá ze tří barev je v doslovném seznamu možností.
Původní DLX2 dokončil 9 372 802 uzlů. Nezávislé přiřazování ternárních
buněk s d00=0 dokončilo 22 590 193 uzlů a všech 5 796 výsledků; po třech
globálních přičteních je celá množina přesně totožná s DLX2.

Číslo knihy má přesto přirozený správný význam. Globální přičtení 1 je
právě posun (3,3); dvojice `00 ↔ p00` tyto tři posuny ještě nerozlišila.
Přidáme-li **d00=0**, zbude přesně jeden zástupce každé translační třídy,
tedy skutečně 5 796. Bez normalizace počátku je 81·5 796 = 469 476
označených matic. Text neříká výslovně, zda dodatečné ztotožnění těchto tří
posunů pokládá za samozřejmé. Proto C028 není potvrzená chyba matematického
počtu; je to přesně doložená mezera mezi popsaným XCC vstupem a jeho
uváděným počtem výsledků. Doplnění d00=0 ji odstraní.

Všechny matice mají D≠Dᵀ. OCR ztrácí znak ≠, originál je správně.
Kromě úplného výčtu je zde krátký obecný důkaz: kdyby q-ární ourotorus
D velikosti q²×q² byl symetrický, každé symetrické okno (a,b;b,c) by při
transpozici zůstalo stejným vzorem. Jedinečnost oken by nutila jeho pozici
na diagonálu. Ale takových vzorů je q³, kdežto diagonálních pozic jen q²,
což pro q>1 nejde. Při ukotvení all-zero okna transpozice ukotvení zachová,
a tedy 5 796 zástupců tvoří 2 898 dvojic, jak kniha uvádí.

C028 je vidět v PDF 437 i v PS 141. Šest úplných vrstev errat neobsahuje
odpovídající doplnění. Tištěný fyzický exemplář nebyl kontrolován.

## 98: E047 a důkaz opravené konstrukce

Oficiální erratum **2. ledna 2025** nahrazuje položky l_ij v možnostech
identifikátory výskytů ij a výslovně uvádí 6m možností. Naše PDF 2022 i
PS 2019 obsahují původní zápis. Jde o známou opravu, nikoli nový nález.

Každá klauzule má tři primární výskyty spojené hranami trojúhelníku a pro
každý výskyt možnost spojující jej s barvou pravdivého literálu. Trojúhelník
sám nepokryje lichý počet tří výskytů; alespoň jeden pravdivostní výskyt
musí být vybrán. Shodné barvy proměnných vyberou konzistentní částečné
přiřazení splňující každou klauzuli, které lze libovolně doplnit.

Naopak ze splňujícího přiřazení zvolíme v každé klauzuli jeden pravdivý
literál a hranu mezi zbývajícími dvěma výskyty. Všechny barvy souhlasí.
Konstrukce je lineární, každá možnost má právě dvě různé položky; členství
v NP plyne z ověření vybrané podmnožiny. Jde o zachování existence řešení,
ne o zachování počtu SAT přiřazení.

Kontrola zahrnuje opakované literály, tautologie, nesplnitelné instance a
prázdnou konjunkci: 2 097 formulí, 39 761 XCC modelů, 82 UNSAT formulí.
U každé se úplná množina všech rozšíření barevných přiřazení rovná přímému
pravdivostnímu výčtu.

## 99: neobarvený výskyt není sdílená barva nula

Na str. 88 je výslovně definováno, že neobarvený výskyt má vlastní barvu,
která se neshoduje s žádnou jinou možností. Nula v paměťovém poli COLOR
na str. 89 je implementační značka, nikoli tato matematická barva.

Pro každý sekundární prvek a každou dvojici nekompatibilních možností
zavedeme privátní neobarvenou sekundární položku do obou možností. Výběr
obou je potom zakázán právě tehdy, když byl zakázán původními barvami.
Primární podmínky ani indexy možností se nemění. Je to ekvivalence pro
každou podmnožinu možností; konstrukce má nanejvýš kvadraticky mnoho
nových položek pro každý původní sekundární prvek.

Včetně směsí explicitních a neobarvených výskytů prošlo 2 586 rodin,
6 047 platných modelů; přímé podmnožiny před převodem, po převodu a
Algorithm C po převodu jsou jako celé množiny stejné. Počet možností
zůstává přesně stejný i při nulovém počtu řešení. Nové erratum zde není.

## 100: konečné CSP a domény

Přímý výčet všech 3^5 přiřazení dává právě 00112, 00122, 01112, 01122,
11111. Čtyři relace ≤ mají po šesti možnostech a součet tří vybraných
proměnných má sedm možností, celkem 31. Úplná XCC množina souhlasí.

Pro konečné explicitní relace má každá podmínka vlastní primární položku.
Její výběr určí jednu přípustnou n-tici na příslušných proměnných; barevná
shoda zajišťuje společné přiřazení. Pokud je každá proměnná obsažená
alespoň v jedné relaci, jsou oba směry bijekce jednoznačné.

Doménové podmínky je třeba zahrnout také pro proměnné, které nejsou v žádné
další relaci: lze je chápat jako unární C_j. Ekvivalentně lze po vyřešení
rozšířit chybějící proměnné přes jejich deklarované domény. Například pro
booleovské x1,x2 s jediným dalším požadavkem x1=0 samotná možnost určí
(0,nepřiřazeno); unární doména x2 dá oba výsledky (0,0),(0,1).
To je potřebná normalizace konečného vstupu, ne nová potvrzená chyba.
Doménově neomezené nekonečné CSP nejsou konečnými vstupy XCC.

U 1 000 různých malých relačních CSP porovnán celý kartézský výčet s XCC,
včetně prázdných relací. Ve 169 případech byly některé proměnné mimo ostatní
podmínky; 232 doplněných unárních domén zachovalo všechna přiřazení.

## Reprodukce a omezení výsledků

`check_universal_cycles.py`, `check_xcc_reductions.py`,
`check_ourotorus_results.py`, `check_generalized_cross.py` a
`check_universal_errata.py` mají konkrétní ukončené výstupy. Hotové výčty
neopakovat bez změny nebo nové pochybnosti. `check_universal_checkpoint.py`
jen přijímá hotové benchmarky a pozoruje původní pomalý proces.

První cell wrapper skončil před spuštěním hledání chybou Pythonu při
duplicitním klíči command v metadatech. Původní log, build a launch zůstaly
archivovány pod `failed-metadata-*`. Po opravě názvu compile_command byly
oba výčty dokončeny; nejde o timeout ani obnovení běžícího hledání.

Všechny čtyři aktuální autorovy erratové originály znovu porovnány přes
SHA-256 a jsou shodné s archivem. Podrobných jedenáct kontextů ze šesti
úplných textových vrstev je v `errata-check.json`. Žádné nové emailové
návrhy nevznikly a nic nebylo odesláno.

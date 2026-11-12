# Minimax a Monte Carlo — 7.2.2.1, úlohy 84–86

Kontrola 2. listopadu 2026. Zadání na straně 133, odpovědi na stranách
433–434, definice Algorithm C na straně 90. Autorův pre-fascikl 5c má
odpovídající strany 69 a 137–138; publikovaný Fascicle 5 strany 131 a
241–242. Původní vykreslené stránky PDF i autorova podkladu byly prohlédnuty.
Fyzický výtisk není ověřen. Celé tři úlohy jsou po tomto bloku zrevidovány;
na stejné straně začínající úloha 87 má vlastní navazující audit.

## 84: minimální největší číslo možnosti

Možnosti jsou v paměti za sebou ve vzestupném pořadí jejich čísel. Maximum
adres vybraných uzlů proto určuje stejnou možnost jako maximum jejích čísel.
Nejlepší dosud známou hodnotu označme B. Odstraněním možností s číslem větším
než B ztrácíme pouze řešení, která nemohou být minimaxová. Hodnota B klesá;
všechna řešení dosažená při poslední hodnotě B, včetně řešení, které ji
poprvé nastavilo, jsou právě požadovaná minimaxová řešení.

Smazání je odložené: při nalezení řešení jsou pokryté všechny primární
položky. Okamžitě se zkrátí seznamy zvolených větvicích položek. Seznamy
ostatních pokrytých nebo purifikovaných položek se zkrátí při jejich
obnovování. Každá možnost obsahuje alespoň jednu primární položku. Každá
odříznutá možnost proto byla při snížení hranice skrytá a při návratu se
už neobnoví. Je-li v obnovovaném uzlu uložen následník za hranicí, stačí
jej přesměrovat na hlavičku jeho položky. Seznamy jsou seřazené, takže
ostatní následníci a předchůdci zůstávají správní. Totéž platí v unpurify;
uzly s již sjednocenou barvou se řídí obvyklým pravidlem COLOR < 0.

`minimax_dlx.py` používá skutečné oddělovače možností, pole obou směrů,
TOP/LEN, barvy i jejich obnovování. Kontroluje vazby, seřazení, délky a
hranici všech aktivních primárních seznamů při každém vstupu do úrovně.
Hranici nelze takto použít po náhodném promíchání seznamů možností.

OCR na straně 434 ztratilo znaménko nerovnosti v podmínce `PP ≠ CUTOFF`.
V obou originálech je podmínka správná; nejde o chybu knihy.

## 85: jediné minimaxové řešení a návrat na k−1

Ponecháme si posledního nalezeného nejlepšího svědka a hledáme už pouze
přísně lepší. Oddělovač před maximální vybranou možností odřízne také tuto
možnost. Je-li zvolena na úrovni k, další možnosti v jejím seřazeném
větvicím seznamu jsou už všechny příliš velké. Dřívější možnosti byly
prohledány, nebo bezpečně odříznuty ještě slabší mezí. Lze tedy ukončit
celou úroveň k a pokračovat na úrovni k−1. Při k=0 končí hledání.

Návrat znamená řádně vrátit commity a pokrytí všech opouštěných úrovní;
nejde o pouhé přiřazení nového čísla úrovně. Vzájemné pořadí barevných
operací musí zůstat obrácené vůči cestě dolů. Tím vznikne přesně jeden
finální výsledek; průběžní zlepšující svědci se ukládají odděleně.
Pokud problém nemá řešení, výstup je prázdný. Triviální prázdný problém
řeší implementace zvlášť s obvyklou konvencí hodnoty 0 pro prázdné maximum;
nepočítá se to jako další nález.

Výčet v `check_minimax.py`: **5 587 matic, 22 348 běhů**, obě varianty
84/85 a obě volby položky (první/MRV). Referencí je přímý výčet všech
podmnožin možností s kontrolou primárních četností a slučitelnosti barev.
Součástí jsou všechny podmnožiny do velikosti 5 z dvanácti malých možností,
4 000 dalších reprodukovatelných matic s promíchaným pořadím položek,
duplicitní možnosti i prázdný problém. Bylo 781 nesplnitelných matic,
334 matic s několika optimy, 20 931 oprav následníka a 832 návratů přes
více úrovní. Úplné optimální množiny a výsledky pro jediného svědka souhlasí.

Dalších 100 matic ověřuje Knuthův původní DLX2 s jeho
[dlx2-cutoff.ch](https://www-cs-faculty.stanford.edu/~knuth/programs/dlx2-cutoff.ch).
Oficiální change file nelze přímo aplikovat na současný DLX2: starý
kontext `unpurify` neobsahuje novější diagnostický řádek. Lokální adaptace
mění **pouze očekávaný text v části @x**. Všechny autorovy náhrady @y jsou
bajtově zachovány a jejich shoda se při sestavení ověřuje. Neupravený
zdroj i původní neúspěšný build log zůstávají uložené. Tento technický
nesoulad sestavení nepřidáváme k matematickým nálezům knihy.

## F124: prázdný krok C6 nevrátí datové struktury

Odpověď 86 říká, že C6 nemá dělat nic, zatímco C7 a C8 zůstanou stejné.
Tím se ztratí jak zpětné uncommit operace, tak obnovení položky i dané
úrovně. Nejmenší přehledný příklad dokonce nepotřebuje barvy ani sekundární
položky:

```
p q
p
q
```

Na úrovni 0 se pokryje p, na úrovni 1 q a na úrovni 2 je jediné řešení.
Globální i má nyní hodnotu q. C8 vrátí úroveň na 1; prázdné C6 přejde do C7,
které odkryje q. Další návrat na úroveň 0 znovu odkryje q. Položka p zůstane
skrytá. Konkrétně RLINK(0) je 2 místo 1 a LLINK(q) je 0 místo 1.
Druhý pokus na tomto stavu počítá už jen dva uzly místo původních tří.

Samostatný příklad s jedinou možností `p q` ukazuje, že nestačí vrátit jen
hodnotu i: je potřeba také vrátit ostatní položky zvolené možnosti. Doslovný
postup ponechá LLINK(0)=0 místo q.

Oprava: v C6 zachovat celý zpětný průchod s uncommit a přiřazení
`i ← TOP(x_l)`. Vynechat pouze přechod na další možnost a návrat do C5;
místo toho pokračovat do C7. Tím se navštíví jedna náhodná cesta a všechny
její změny se vrátí v opačném pořadí. Volitelné cache barev v hlavičkách
nejsou součástí obnovovaného logického stavu, stejně jako u běžného C.

## F125: chybí faktor θ v odhadu cleansings

Při vstupu do úrovně je D převrácená pravděpodobnost, že jsme dosáhli
daného uzlu. Z jeho θ možností se jedna vybere s pravděpodobností 1/θ.
Cena C operací závislých na vybrané možnosti proto potřebuje váhu **DθC**.
Tištěné **DC** dává místo součtu cen potomků jejich průměr.

Konkrétní vstup:

```
p | x
p x:A
p x:B
```

Úplný strom má dva potomky. Každý jednou zavolá purify, tedy dohromady
2 cleansings. Každý náhodný pokus má D=1, θ=2 a C=1, takže tištěný odhad
je vždy 1. Jeho střední hodnota je přesně 1 místo 2, bez ohledu na počet
pokusů. Opravená váha dává vždy 2. Protipříklad platí i s opraveným C6.

Větší čtyřmožnostní příklad `p x:A / p x:B / q x:A / q x:B` zahrnuje i
přiřazování COLOR(q)←−1: úplný počet je 4, tištěný odhad vždy 2.
Neupravený původní DLX2 potvrzuje oba skutečné počty i počty aktualizací.

## F126: odhad vynechává aktualizaci prázdné položky

Při θ=0 odpověď 86 přeskočí C4 a jde přímo do C7. Obvyklý Algorithm C
však v C4 pokryje i prázdnou položku. Nastavení LLINK(r) je podle uvedené
definice jedna aktualizace, která má být započtena.

Pro jednu primární položku p bez možností má celý strom jediný uzel,
žádné řešení a **jednu aktualizaci**. Tištěný odhad vrací nulu aktualizací.
Také ne-prázdný vstup ukazuje tutéž chybu:

```
p q | x
p x
q x
```

Pokrytí p stojí 2 aktualizace. Commit x stojí další 2 a vyprázdní q.
Pokrytí prázdné q stojí ještě 1. Skutečnost je tedy 5, tištěný odhad 4.
Opět nejde o problém vzorkování; zde je jen jediná náhodná cesta.

Oprava: i při θ=0 provést C4, přičíst D·U′ (zde D) k odhadu aktualizací
a teprve pak přejít do C7. Neprovádět náhodnou volbu z prázdné množiny.
Případné řešení pomocí vynechání cover musí odpovídajícím způsobem změnit
i referenční Algorithm C a definici měřené práce; takové odlišné zadání
v odpovědi není. Neupravený původní DLX2 skutečně dává 1 a 5 aktualizací.

Samotné odkrytí dosud nepokryté prázdné položky v C7 je zde idempotentní;
neuvádíme jej jako další poškození struktury. Chyba F126 je chybějící cena.

## Opravená očekávání a nezávislé kontroly

Na neprázdném větvení je vytištěná aktualizační formule **D(U′+θU)**
správná. OCR nezachovalo čárku u U′; nejde o prohozené koeficienty.
Společná cena C4 patří do uzlu (váha D), cena C5 do náhodně vybrané hrany
(váha Dθ). Stejnou vahou Dθ je nutné násobit i cleansings. Při θ=0 zůstává
společná cena uzlu. Po sestupu se nastaví D←θD. Uzly v C2 mají váhu D;
úspěšný list přidá D řešení a neúspěšný list žádné. Při zpětném průchodu
se nic neodhaduje, proto není nutné D zpětně dělit.

Každý uzel s dosažitelností 1/D přispěje očekávanou cenou D·c/D=c;
každá hrana s dosažitelností 1/(Dθ) obdobně přispěje svou vlastní cenou.
Linearita střední hodnoty dává nezaujatost profilu, počtu řešení i obou
nákladových profilů. Jde přímo o princip věty 7.2.2E na straně 48,
již dříve prověřené v `ESTIMATION_NOTES.md`.

`check_dlx_monte_carlo.py` používá tři odlišné reprezentace:

- Doslovný C1–C8 nad obousměrnými seznamy, v původní i opravené verzi.
- Úplné běžné C s měřením změn délek, cover a purify, nezávisle na odhadech.
- Kopírované množiny zbývajících možností, primárních položek a barev;
  jejich náklady se počítají kombinatoricky, bez seznamů a bez undo operací.

Množiny řešení navíc souhlasí s přímým výčtem podmnožin. Na **1 795
maticích**, při dvou volbách větvení, bylo projito **10 633 možných náhodných
cest**. Jejich pravděpodobnosti jsou přesná racionální čísla. Opravené
střední hodnoty souhlasí s úplným stromem po jednotlivých hloubkách i
celkem. Každý opravený pokus vrací všechna pole do původního stavu;
další cesty se zkoušejí na téže znovu použité instanci. Nejde o přibližný
Monte Carlo experiment. Po doplnění svědka druhého pokaženého pokusu
byl kontrolní program znovu spuštěn.

Autorův starší [dance-random.ch](https://www-cs-faculty.stanford.edu/~knuth/programs/dance-random.ch)
navíc skutečně pokrývá i prázdnou položku a při závěrečném návratu vrací
ostatní položky zvolené možnosti. Je to podpůrná kontrola záměru; tento
starší program nepracuje s barvami, a proto nedokládá opravu F125.

## Errata, rozsah a reprodukce

`check_minimax_errata.py` prohledal šest úplných historických a současných
vrstev 4B/F5 podle stran, čísel úloh i pojmů. Čtyři originály byly čerstvě
staženy a mají stejné SHA256 jako archiv. Veřejná oprava odpovídající
F124–F126 nebyla nalezena. Změna jmen markerů v odpovědi 87 (25. 5. 2021)
se tohoto bloku netýká; stejně číslovaná úloha 84 v SAT je jiná úloha.
Vizuální originály obou našich vydání obsahují všechny tři uvedené chyby.
To nedokládá prvenství nálezu ani stav všech novějších tisků.

Výsledky, celý původní a koncový stav malých svědků, přesné pravděpodobnosti,
stopy, hashe zdrojů a nativní výstupy jsou v `results/minimax_mc/`.

```
python3 audit-2026-10-31/check_minimax.py
python3 audit-2026-10-31/check_dlx_monte_carlo.py
python3 audit-2026-10-31/check_minimax_native.py
python3 audit-2026-10-31/check_minimax_errata.py
```

Všechny tyto kontroly byly dokončeny. Není potřeba je znovu spouštět bez
změny zdrojů nebo konkrétní pochybnosti. Navazují úlohy 87–90 a odpovídající
slovní konstrukce; celý svazek zůstává zdaleka nedokončený. Žádný nový
emailový návrh ani zpráva Knuthovi nebyly vytvořeny.

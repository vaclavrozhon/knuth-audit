# §2.5–33/34: dosažitelnost, relokace a skutečný MIX

Uzel je blok délky `SIZE(P)>0` s hlavičkou na adrese P. Jeho prvních
T(P) datových slov obsahuje odkazy, kde `0<=T(P)<SIZE(P)`; další
data mohou mít libovolné bity. Odkaz je buď nulový, nebo adresa
hlavičky jiného uzlu. `USE` ukazuje na jeden skutečný uzel. Paměť
od 1 do AVAIL−1 je přesně rozložena na uzly bez mezer. Dosažitelný
uzel je ten, do něhož vede posloupnost odkazů z USE.

## Obecná správnost G1–G8

G1 vynuluje jen pomocné odkazy hlaviček. G2–G4 používají tyto odkazy
současně jako značku návštěvy a jako zásobník neprobraných uzlů.
Na dně je sentinel AVAIL, jehož odkaz je nulový. Každý skutečně
navštívený uzel má nenulový pomocný odkaz a je na zásobník vložen
právě jednou. Nulový odkaz na jiný uzel se ignoruje. Popnutý uzel
si značku ponechává; všechny jeho odkazy se prohlédnou. Indukcí
jsou všechny vložené uzly dosažitelné a každý dosažitelný uzel je
nakonec vložen, protože všechny odkazy jeho dosažitelného předchůdce
jsou prohlédnuty. Cyklus ani sdílení podgrafu nezpůsobí opakované vložení.
Sentinel se popne až po vyprázdnění skutečných uzlů.

G5–G7 procházejí původní adresy vzestupně. P je vždy začátek dosud
nezpracovaného uzlu nebo běhu mrtvých uzlů; Q je jedna plus celková
délka již navštívených živých uzlů. Živému uzlu se do pomocného
LINK uloží Q a Q se zvýší o jeho délku. Sousední mrtvé uzly se
sloučí do jednoho skokem přes součet jejich délek. Každý nový cílový
blok končí před cílem dalšího, zachovává původní pořadí a jeho
začátek nepřevyšuje původní začátek. Nenulově označený sentinel
délky nula zabrání tomu, aby byl sloučen s mrtvým koncem paměti.

G8 musí přeložit právě nenulové odkazy živých uzlů. Každý takový
cíl je opět živý a jeho pomocný LINK obsahuje nové umístění. Překlad
je tedy definován a zachovává všechny hrany. Překlad USE je stejný.
Nyní je možné uzly přesouvat: žádný skutečný odkaz už nezávisí na
starém rozložení paměti. Kód v knize tento test nuly v G8 vynechává,
ačkoli ho abstraktní algoritmus obsahuje; viz samostatný report.

## G9 a nutnost uchovat délku

Při cíli Q<=P lze kopírovat vzestupně: při zápisu slova Q+k není
zničeno žádné dosud nepřečtené zdrojové slovo P+j pro j>k. Kopírování
tedy zachová celý uzel, včetně znamének nul a všech datových polí.
Před přesunem je ovšem třeba uložit `S=SIZE(P)`. Po přesunu může
adresu P překrýt některé datové slovo; další P je proto `P+S`, nikoli
hodnota znovu přečtená z paměti. Doslovný G9 má tuto vadu; skutečný
MIX používá rI5 a má v tomto ohledu správný postup. Po posledním
přesunu jsou všechny živé uzly v souvislém intervalu 1..Q−1, všechny
jejich pomocné odkazy jsou nulové a data i skutečné odkazy zachovány.

Nezávislý validátor nejprve prohledá původní graf do množiny,
pak z původní nezměněné paměti vytváří výslednou kopii v jiné paměti.
Nepoužívá zásobník v hlavičkách, slučování mrtvých uzlů ani přesun
s překryvem. Doslovný i opravený G a skutečné MIX instrukce jsou
v `compaction.py`; nejmenší reprodukce v `reproduce_compaction_failures.py`.

## Čas MIX a úplná vstupní inicializace

Označme a počet živých uzlů, b počet jejich skutečných odkazových
polí (včetně nul), w součet jejich délek, c počet neprázdných běhů
mrtvých uzlů a d počet zbývajících mrtvých uzlů. Tedy celkový počet
uzlů je a+c+d. Sečtení frekvencí jednotlivých vytištěných instrukcí
s MIX časy dává následující kontrolu:

| Vytištěné řádky | Čas v jednotkách u |
|---|---|
| 05–21 | 11a+8b+8 |
| 22–25 | 5 |
| 26–32 | 10a+3c+6 |
| 33–38 | 10 |
| 39–47 | 9c+8d |
| 48–60 | 11a+9b+6c+9 |
| 61–71 | 12a+2w+6c+9 |
| Celkem | 44a+17b+2w+24c+8d+47 |

Tištěný koeficient 25c je o c větší. Vstup je přímo G2; žádný
volající JMP ani návrat v původním fragmentu není. Náš doplněný
HLT slouží jen jako adresa, před jejímž provedením se simulátor zastaví.

Oprava nuly vloží mezi řádky 50 a 51 `J6Z 1F`, kde 1H je na 53.
Je-li z počet nulových linků živých uzlů, nová instrukce se provede
b-krát a ušetří dvě dvoujednotkové instrukce z-krát. Opravený čas
je tedy `44a+18b+2w+24c+8d+47−4z`.

Volitelný skutečný MIX prefix G1 v našem programu vynuluje pomocné
hlavičky i při libovolných původních hodnotách. Používá vzestupné
SIZE skoky a pro n uzlů přidá přesně `8n+2` jednotek. Bez prefixu
platí výslovný předpoklad odpovědi 34, že G1 byl proveden předem
nebo pomocné LINK vynuloval alokátor. Vstupní data vlastních testů
pro úplný prefix obsahují také nenulové pomocné hlavičky.

MIX implementace platí pro všechny celočíselné základy bajtu 64–100.
Jeden MOVE přenáší nejvýše radix−1 slov; tato mez je v textu na 615
výslovně uvedena. T musí vejít do jednoho bajtu, adresy a délky do
dvou, všechny adresované buňky včetně sentinelů musí být 0..3999
a kód/data mimo pool se nesmí překrývat. Naše testová konfigurace
má kód 980–1068, proměnné 2000–2001 a pool pod 980. Obecný důkaz
nepředstírá, že tím byly ověřeny všechny možné paměťové rozvrhy.

Provedeno 59 708 všech slovních případů s 1–3 uzly, každým SIZE 1–3,
všemi T<SIZE, všemi nulovými/uzlovými cíli a každým USE. Opravený
G vždy souhlasí s nezávislým modelem. Skutečný MIX byl kontrolován
na všech případech s nejvýše 2 uzly a pravidelném vzorku tříuzlových,
celkem 2 564 případů se základem 64, dále na 1 110 deterministicky
náhodných případech napříč všemi 37 základy a 37 případech úplného
G1 prefixu. Doslovný MIX selhává právě na nulových dosažitelných
linkách v tomto rozsahu; všechny časové formule byly ověřeny.
Konečné kontroly doplňují uvedené obecné invarianty.

## Odkaz z §2.3.5–9

Originál 604 za algoritmem H odkazuje na úlohu 2.5–33. H komprimuje
označené pevně velké uzly a překládá jejich ALINK/BLINK pomocí
relokačních odkazů. Zadání 455 a G5–G9 na 613 řeší právě odpovídající
kompakci a relokaci pro proměnlivé délky, s explicitními skutečnými
linkovými poli a jediným kořenem USE. Jde o správný tematický odkaz,
nikoli záměnu úlohy. Zjištěné vlastní vady G9/MIX jeho význam nemění.

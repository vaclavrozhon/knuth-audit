# §5.2–13: úplný důkaz distribučního přeuspořádání

Zadání80/file91, odpověď618/file629. Zobrazena původní
sazba a obě relevantní změny: all3-pre.pdf/file11
z21.12.2019 a all3.pdf/file6 z3.9.2024. Pět vrstev
je spárováno v `sources/insertion-errata-review.json`.
V aktuálním D6′ má větev COUNT[K_r]=r nastavit
COUNT[K_r]←r−1. Původní první tisk také správně
odečítal1; přepis2019 toto vynechal a2024 jej opravil.
Nejde o nový nález. Níže se dokazuje aktuální znění.

## P0677: pevné cílové intervaly a skutečný význam COUNT

Po D4 původního algoritmu označme F_k počet klíčů k,
L_k=∑_(t<k)F_t a H_k=L_k+F_k. Správné cílové
pozice pro klíč k jsou disjunktní intervaly

    I_k={L_k+1,…,H_k}.

L,H jsou pouze důkazová označení původních počtů;
algoritmus je nemusí ukládat. Stav U je množina dosud
nepřidělených pozic. Na začátku D6′ platí:

    U = disjunktní sjednocení {L_k+1,…,COUNT[k]};
    COUNT[k]−L_k = počet dosud nepřidělených záznamů klíče k.

V každé pozici U leží právě jeden takový záznam.
Všechny ostatní pozice už mají konečný správný klíč
a do dalších cyklů nevstupují. Zpočátku U={1,…,N},
COUNT[k]=H_k a invariant je zjevný.

Navíc vedeme invariant skeneru r:

    Je-li j∈U a j>r, pak COUNT[K_j]<j.

Tento příkaz přesně vyjadřuje knižní „musí jít doleva“.
Na začátku r=N je prázdný. COUNT nikdy neroste.

## P0678: všechny tři větve D6′

Je-li r již přidělená pozice s klíčem k, musí
r>COUNT[k], protože přidělené pozice tvoří horní
část I_k. Proto větev COUNT[K_r]≥r zaručuje,
že r je skutečně nepřidělené, nikoli dříve hotové.

Při COUNT[K_r]<r pouze zmenšíme r. Pokud r∈U,
nově přeskočená pozice splňuje invariant skeneru;
pokud je hotová, nepatří do podmínky. Počty a U
se nemění. Při rovnosti COUNT[K_r]=r přidělíme
již správný záznam právě jeho nejpravější volné
pozici r. Snížení COUNT o1 odstraní z U přesně r
a odečte jeden nepřidělený záznam správného klíče.
Invarianty se zachovají a r se zmenší.

Zbývá COUNT[K_r]>r. Pozice r je nepřidělená;
záznam R_r uložíme do R a původní místo r
považujeme za dočasnou díru. Jeho dosud uložená
kopie se během cyklu nesmí číst a bude přepsána
teprve na konci. První rezervovaný cíl j>r je
určitě odlišný od díry, takže lze bezpečně zahájit D7′.

## P0679: cyklus s dírou, rezervace a přesné pořadí D7′

Pro nesený záznam klíče k rezervace vezme nejpravější
volné místo j=COUNT[k] a sníží COUNT[k] o1.
Je to vždy legální: nesený záznam patří mezi dosud
nepřidělené, takže zbývá aspoň jedno místo jeho klíče.
Tudíž L_k<COUNT[k]≤H_k před rezervací.

Pokud j≠r, obsazené místo j má jiný dosud nepřidělený
záznam S. Uložíme R na jeho správný konečný cíl j,
vezmeme S jako nový nesený záznam a opakujeme rezervaci.
Jestliže j=r, zaplníme díru a celý cyklus skončí.

Přesný invariant této logické verze: dosud volná místa
jsou konce intervalů uvedených v P0677; právě r
je prázdné, ostatní volné pozice mají po jednom
nepřiděleném záznamu a navíc je jeden takový záznam
nesen. Počet zbývajících záznamů každého klíče
souhlasí s počtem jeho zbývajících míst. Každá
rezervace ubere jedno místo a přidělí právě jeden
záznam, takže všechny rovnosti zůstanou.

Vlastní D7′ provádí následující rezervaci ještě
před zápisem dosavadního R: nejprve přečte S=R_j,
k=COUNT[K_j] a sníží COUNT[K_j], teprve pak píše
R_j←R,R←S,j←k. Je to totéž logické pořadí,
protože klíč S je přečten **před** přepsáním R_j
a změna COUNT je nezávislá na přesunu dat. Příští
rezervace nemůže dát právě spotřebované j: pro
stejný klíč už COUNT klesl a pro jiný jsou intervaly
disjunktní. Když nové j=r, algoritmus jej rovnou
zaplní a nečte starou duplicitní hodnotu v díře.

Rezervované cíle se nikdy neopakují. Je jich konečně
mnoho, takže cyklus skončí: pokud dříve nevybere r,
nakonec zůstane r jediným volným místem a odpovídající
nesený záznam je musí vybrat. Nemůže se vyčerpat
COUNT svého klíče nebo přistoupit mimo1,…,N.
Po zaplnění díry je obnoven celý invariant P0677.

## P0680: proč po dosažení r=0 nezůstane skrytý záznam

V cyklu se ostatní nepřidělené záznamy nepřemísťují:
navštívené pozice se přidělují natrvalo, r se také
nakonec přidělí, nenavštívené pozice si ponechají
své záznamy. Proto všechny dosavadní podmínky
COUNT[K_j]<j pro j>r zůstávají, neboť COUNT jen klesá.
Nová hodnota r−1 je tedy opět správným skenerem.

Po N sníženích je r=0. Kdyby U nebylo prázdné,
vezměme jeho nejmenší pozici j. Její nepřidělený
záznam klíče k vyžaduje aspoň jedno volné místo k;
tedy COUNT[k]∈U. Invariant skeneru ale tvrdí
COUNT[k]<j, v rozporu s minimalitou j.
Proto U=∅ a všechny záznamy jsou správně setříděné.
To je konkrétní obecný důkaz knižní věty, že
nezbude permutace, v níž by se všechny prvky měly
přemístit pouze doleva.

## P0681: ukončení celého algoritmu, čas a skutečná paměť

Vnější r klesne přesně N krát; D6′ se včetně
konečného testu provede N+1 krát. Každá rovnostní
větev přidělí jedno místo; každý zahájený cyklus
přidělí alespoň dvě. Počet všech rezervací je přesně
N a počet průchodů tělem D7′ je nejvýše N. Celá
nová fáze proto trvá Θ(N) při konstantní ceně
záznamu, včetně případů mnoha přeskočených pozic.
Celý distribuční sort s D1–D4 má Θ(N+v−u+1).

Textové přiřazování používá dva pomocné záznamové
hodnoty R,S a konstantní počet indexů; nedochází
k alokaci dalších N záznamů. S lze také odstranit:
po načtení jeho klíče a dalšího k vyměníme nesené R
s cílovým R_j slovo po slovu pomocí jednoho skaláru.
Stačí tedy jeden pomocný záznam plus O(1) slov,
stejně jako u předchozích přeuspořádání. „In place“
zde není tvrzení o doslova nulovém pracovním registru.
Pro délku záznamu ℓ je cena O(Nℓ+v−u+1).

## P0682: skutečná nestabilita, nikoli porucha třídění

Vstup tří označených záznamů je(2A,1B,1C).
Po D4 máme COUNT[1]=2,COUNT[2]=3.
Pro r=3 se přeskočí1C, protože2<3. Pro r=2
rovnost přidělí1B na místě2 a sníží COUNT[1] na1.
Pro r=1 se záznam2A rezervuje na3, odkud se vezme1C;
ten se rezervuje na1 a díra se uzavře. Výstup je

    (1C,1B,2A).

Klíče jsou setříděny, ale pořadí shodných1 se obrátilo.
To potvrzuje výslovné upozornění odpovědi, není to
nový nález. Zároveň ukazuje, proč invariant nesmí
vyžadovat původní pořadí stejných klíčů.

## P0683: nulové a krajní případy i aktuální oprava

Prázdný vstup má r=0 a okamžitý konec. Pro singleton
se provede jediná rovnostní větev. Při u=v, tedy
při jediném klíči, je vždy COUNT[K_r]=r; všechny
záznamy zůstanou na svých místech a D7′ se nespustí.
Totéž platí pro již setříděný vstup, blok po bloku
zprava. Prázdné klíčové intervaly F_k=0 nikdy
nedodají nesený záznam a nevynutí neplatnou rezervaci.

Snížení COUNT v rovnostní větvi je součástí významu
„přidělit cíl r“. Znění2024 tak přesně obnovuje
invariant, který by text2019 bez tohoto snížení
nesplňoval. To samo není zde vydáváno za nový
protipříklad výstupu staré varianty; veřejná oprava
je známá a aktuální varianta je úplně dokázaná.
Číselná chyba M=0 v jiném MIX programu odpovědi9
se s tímto správným abstraktním postupem nesměšuje.

## P0684: přesná souvislost s Foatovou konstrukcí

Přebíráme už dokázaný frontový model
`notes/multisets-proof-main.md` pro Theorem5.1.2B.
Každá dosud nepřidělená pozice i má předepsaný
finální klíč y (podle svého intervalu I_y) a současný
klíč x=K_i. Představuje hranu y→x. U každého klíče
je počet vstupních a výstupních hran stejný, protože
jde o stejný multiset záznamů a cílových míst.

Nesený klíč x vybere nejpravější zbývající místo
v bloku x a z něj se vezme nový klíč z; tedy se
pokračuje hranou x→z. Další volby z každého bloku
jdou zprava doleva a COUNT je ukazatel jeho fronty.
Po návratu do počáteční pozice se odebral uzavřený
vyvážený sled hran a zůstává vyvážený zbytek.
Stejný princip spotřebovávání front a cyklické
faktorizace je základem dříve dokázané Foatovy mapy.

Netvrdí se, že D′ má stejnou kanonickou volbu prvního
faktoru jako TheoremB: cyklus D′ je ukončen návratem
do konkrétního místa, nikoli nutně prvním návratem
do téhož klíče. Při opakovaných klíčích může týž
klíč během cyklu navštívit vícekrát. Tím je vymezena
skutečná strukturální souvislost poznámky bez
záměny obou různých bijekcí.

Žádný nový nález ani výpočet. Správnost celého
aktuálního algoritmu, jeho meze i nestabilita jsou
doloženy samostatně, bez závislosti na uvedené analogii.

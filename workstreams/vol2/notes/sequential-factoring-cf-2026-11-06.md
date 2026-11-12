# §4.5.4 — souvislé argumenty: řetězové zlomky a Dixonova metoda

6. listopadu 2026, V2-X0146. Původní sazba přečtena od posledního
odstavce 396 po 403 před nadpisem Secret factors; zadání 412–415
a odpovědi 659–660, 664–665. Párovány celé úlohy 11–14, 28–31,
36 a 37. Materiál ostatních úloh na těchto stranách se tím neuzavírá.
Přesná mapa je v results/sequential-factoring-cf-evidence.json.

Deset úloh: devět uzavřených v evidovaném rozsahu a jedna partial.
Úloha 37 má hotový obecný důkaz palindromu, ale nevyřešený výklad
doporučeného předčasného zastavení; C0175 zůstává candidate.
Nevznikl nový nález ani nový výpočet. Dřívější certifikáty a censy
se přebírají bez opakování.

## Převzaté argumenty a přesné hranice

`factoring-contfrac.md`, §1–7, pokrývá odděleně:
kongruenci (18), konstrukci (19)–(21), počet m+2 relací,
E1–E5 s opravenou inicializací z roku 2001, invariant, konečnost,
všechny řádky obou tabulek, F1–F5, úplnost pro jednotkové relace,
podmíněnou pravděpodobnost, filtr báze, lokální průměry i
heuristické (22)–(23). Parametrické zbytky a původní výsledky
jsou v results/factoring-contfrac.json. Nezkrácené konvergenty
přebírají obecný důkaz z euclid-quadratic.md, §12.

Výrok o řešení (18) skutečně nepotřebuje nesoudělnost x s N:
pokud gcd(x−y,N)=1, kongruence vynutí x+y=N; gcd nemůže být N
kvůli rozsahu. Úplnost F a přesná pravděpodobnost 2^(1−d)
naopak jednotkovost potřebují. C0159 má konkrétní šestirelační
protipříklad pro N=155; Dixonův text předpoklady výslovně splňuje.

C0158 se týká přesné rovnosti pro P redukované modulo N:
na 398 a 400 je třeba nezkrácený čitatel, v důkazu odpovědi 14
na 660 také. Kongruenční invariant E se nemění. Závažnost
snižujeme na low: jde o chybnou pomocnou identitu a značení,
nikoli o chybu výstupů algoritmu. C0159 je medium pro nepravdivou
úplnost a pravděpodobnost při dovolených nejednotkových relacích.

`factoring-basic.md`, oddíl Hladká čísla, dává úlohu 29:
vektory nezáporných exponentů se součtem nejvýše r mají počet
binom(m+r,r), dávají různá čísla nejvýše p_m^r a jejich počet
je nejméně m^r/r!. Platí i r=0. Pozdější známá oprava názvu
nerovnosti je zahrnuta, nejde o nález.

`factoring-dixon.md`, §1–5, samostatně dokazuje úlohy 30–31
a všechny kroky věty D. Ze stejného znaménkového vzoru se získá
čtverec modulo každé prvočíselné mocniny, Cauchyho nerovnost
a prosté přiřazení do s-prvkových podmnožin omezí násobnost
rozkladů vektoru. Podmíněná pravděpodobnost každé nové závislosti
je nejvýše 1/2; nezávislost odvozených relací není předpokladem.
Binomický ocas má samostatný Markovův důkaz. Volba celého sudého r,
prvočíselné meze směrem dolů, zaokrouhlení M a omezení počtu
pokusů při generování náhodných bitů jsou doloženy. Normalizovaná
eliminace má konečnou bitovou cenu; rostoucí exponenty se nepovažují
za čísla s jednotkovou cenou. Hlavní konstanta sqrt(8) a mez
selhání O(1/N) tedy mají obecný důkaz. Staré konečné kontroly
nejsou jeho náhradou a nebyly opakovány.

## Úlohy 36 a 37

`factoring-refinement.md`, §1–5, dokazuje všechny jednotlivé
matematické kroky, včetně opravy podlahy v odpovědi 36.
C0174 vyvrací tištěnou přesnost pro libovolnou uvedenou volbu m;
po doladění m je konečné optimum zachováno. Závažnost medium:
chyba ovlivňuje asymptotické odvození, nikoli platnost samotné
heuristiky či existence optimální volby.

Milion podílů pro D=10^18+314159 a čtyři četnosti se přebírají
z již dokončeného porovnání dvou celočíselných rekurzí. Znovu se
nepočítaly. Hustota min(1,1/t−1)/ln(2) je vlastním výpočtem
z explicitního invariantního rozdělení; ergodicita je uvedený
externí vstup. Přenos na každou pevnou kvadratickou iracionalitu
není dokázán a knižní poznámka jej používá jako heuristiku.

Involuce redukovaných kvadratických čísel dokazuje palindrom
i symetrii pomocných stavů. Z nich ale neplyne zachování
faktorizujících relací při libovolném předčasném ukončení.
Dva uložené příklady C0175 dokazují ztrátu relace, zároveň
kniha u tohoto volitelného kroku výslovně neslibuje úplnost.
Proto nezvyšujeme status candidate. Celková úloha 37 je nově
partial, ačkoli její hlavní matematické zadání je vyřešeno.
Tento rozdíl musí zůstat vidět také v pokrytí stran.

## Ostatní metody a historické údaje

Pollardův odstavec na 402 má obecný argument ve
`factoring-pminusplus.md`, §1, 3–4: řád báze dělí zvolený
hladký exponent; gcd může být celé N, proto je potřeba změna
báze či dělení dávky. Vlastní párování celých úloh 19–20
včetně odpovědi 661 patří do dalšího bloku.

`factoring-modern.md` dokládá všechny číselné rozklady F9–F13,
prvočíselnost 21 uvedených faktorů, počty číslic a složenost
obou zbývajících kofaktorů. Převzato 124 dříve ověřených
eliptických článků; žádné nové generování ani ověřovací běhy.
Formule ECM a NFS jsou pojmenované externí heuristické odhady
z citovaných primárních článků. Vlastní převod pro p řádu sqrt(N)
dává polovinu hlavního exponentu času E. Nejde o univerzální
ekvivalenci skutečných časů. Hasseova věta je externí vstup.

Zachované výjimky:
- 396–397: historické časy přibližně 30 s a 50 minut mají pouze
  doložené dobové srovnání v přepisu, nikoli nový benchmark.
- 399: Wunderlichův dostupný úvod potvrzuje 1324 faktorizací
  patnácti- až dvaačtyřiceticiferných čísel a exponent 0.152.
  Úplný knižní rozsah od 10^13 a všechny tabulky nebyly ověřeny.
- 400: doporučení m přibližně 150 pro N kolem 10^40 zůstává
  neověřeným dobovým empirickým údajem.
- 401: Williamsova bibliografie byla porovnána s primárním
  abstraktem; jeho numerické tabulky nejsou naším vlastním výsledkem.
- 402: přesné znění Guyova citátu nebylo získáno, výslovně přeskočeno.
- 403: přechod kolem 10^112 zůstává nedoloženým dobovým odhadem.
  Uvedené počty faktorů „at present“ se vztahují k dotisku 1997,
  nikoli k dnešnímu stavu.

Všechny tyto meze byly už zaznamenány v převzatých poznámkách
a nejsou povýšeny na nové nezávislé ověření. Čtyři vrstvy errat
byly spárovány při původních uzavřených blocích. Zde se ověřilo
jejich použití, bez opakované úplné rešerše. Fyzický nejnovější
dotisk a prvenství nálezů nadále nejsou ověřeny.

Další kurzor: nadpis Secret factors na tištěné 403 / file415,
pak 404. Zbývá párovat ostatní úlohy a odpovědi oddílu.

# Souvislý průchod §1.2.2: čísla, mocniny a logaritmy

5. listopadu 2026. Přímo přečteny původní strany 21–27 a odpovědi
469–471. Celé stránky 27 a 471 tento blok neuzavírá, protože na nich
pokračuje §1.2.3. Na 469 zůstává samostatná historická výhrada k 15(c)
z předchozího oddílu. Ostatní matematika této stránky je nyní pokryta.

## Převzatá a znovu porovnaná matematika

Přečteny celé `numbers-and-powers.md`, `logarithm-algorithms.md` a
kořenové recenze `logarithm-primary-root-review.md`,
`linsky-feynman-root-status.md`, `briggs-root-review.md`.

Kanonické desetinné rozvoje zahrnují zápornou celou část a zakazují
koncové devítky. Definice kořene, racionálních a reálných mocnin mají
obecné důkazy; u polootevřených intervalů nestačí jen pokles délky,
je třeba vyloučit horní kraj pomocí zákazu devítkového ocasu.
Převod základu se používá jen pro definované logaritmy. Hodnoty π, φ, e
a číselné příklady jsou pokryty dřívějšími přesnými intervaly a modely;
tyto výpočty se znovu nespouštějí.

Vzorce složeného úročení jsou posuzovány jako matematické příklady.
Limitní vztah (1+r/N)^N→exp(r) je správný pro pevné r. Zmínka o tom,
kolik bankéřů skutečně používá tuto konvenci, zůstává historicky
neověřená, nikoli potvrzená tímto limitním výpočtem.

Tabulka opakovaného umocňování na 24 souhlasí s uloženým modelem
zaokrouhlování. Invariant (19) v originálu obsahuje n; jeho vynechání
v pomocném Markdownu není chyba knihy. Záměrně vadné tvrzení úlohy 18
je předmětem zadání „prove or disprove“. Obor úlohy 21 je třeba číst
spolu s požadovanými reálnými výrazy ln ln x a ln ln b, tedy x,b>1;
pro obecnější definovanou levou stranu slouží varianta s absolutními
hodnotami z původní poznámky. Nepřidáváme nový nález jen kvůli tomuto
implicitnímu oboru.

Úlohy 25–27 mají důkazy ukončení, lineárního počtu kroků v počtu bitů
a chybových mezí v konkrétním, výslovně určeném modelu. Do chyby se
započítává také zahození spodních bitů pracovního x, nikoli jen tabulka.
U přesné rekurence jsou zahrnuty rovnosti s prahem normalizace.
Přijatý obecný důkaz není nahrazen konečným testem 8190 vstupů.

## Doplnění obecné exponenciální metody pro pevné b>1

Původní poznámka podrobně analyzovala konkrétní realizaci pro b=2.
Stejný argument lze dokončit pro každý **pevný** b>1, s předem
připravenou tabulkou a dostatečným celočíselným rozsahem. Není tím
potvrzen každý libovolný způsob zaokrouhlování tabulky.

Nechť h=2^(−p), p≥1, vstupní exponent a je násobek h mezi 0 a A=1−h.
Položme α_k=−ln(1−2^(−k))/ln b a tabulkovou hodnotu h B_k,
kde B_k=ceil(α_k/h). Opravená inicializace je zbytek R=A−a a y
zaokrouhlené na nejbližší násobek h k b^A. Při R≥h B_k odečteme
h B_k a provedeme y←y−h floor(y/(h 2^k)); jinak zvětšíme k.
Všechny tyto pracovní operace jsou posuny, součty, rozdíly a porovnání.

Protože −ln(1−t)≤2t pro 0<t≤1/2, stačí tabulku připravit do

    K=max(1, ceil(log_2(2/(h ln b)))).

Pak 0<α_K≤h, tedy B_K=1. Každý nenulový zbytek lze zmenšit a metoda
skončí v R=0. Pro k≥2 platí α_(k−1)<3α_k, protože při t=2^(−k)≤1/4
je (1−t)^3<1−2t. Proto B_(k−1)≤3B_k. Při prvním příchodu na k je
R/h<B_(k−1), a B_k se tudíž odečte nejvýše dvakrát. Na k=1 stačí
nejvýše ceil(log_2 b) odečtení. Celkově

    M ≤ ceil(log_2 b) + 2(K−1) = O_b(p).

Dolní index b výslovně říká, že konstanta závisí na základu. Nejde
o uniformní mez pro neomezeně velký či k jedné se blížící základ.

Zaokrouhlení tabulky dává δ_j=α_k−h B_k v (−h,0]. Posun y se zařízne
dolů, takže relativní oprava při odečtení je nezáporná. Invariant
y b^(−R) dává y≥1−h/2, a z příslušnosti k mřížce plyne y≥1.
Proto má každá tato relativní oprava velikost menší než 2h.
Počáteční relativní chyba má absolutní hodnotu nejvýše h/2. Stejné
teleskopování jako v původní poznámce tedy dává

    |ln(y_final/b^a)|
      ≤ −ln(1−h/2) + M [h ln b + ln(1+2h)] → 0.

Případ a=A končí ihned a tuto mez rovněž splňuje. Potřebný rozsah y
se nesmí nechat přetéct; chyba vstupní reprezentace b či a by byla
dalším samostatným příspěvkem. Důkaz výše nevyžaduje nový brute force.

## Dřívější potvrzený nález C0002

Původní stránka 22 stále definuje b jen jako kladné reálné číslo;
zadání 28 nepřidává b>1. Po použití obou známých oprav inicializace
zůstává pro b=1/2, a=ε=1/4 přesná posloupnost zbytku
1/2, 3/2, 5/2,…, stále s k=1. Je to důsledek tabulkové hodnoty −1,
nezávislý na zaokrouhlení y. Tím je potvrzena původní diagnóza C0002,
nikoli nalezena další chyba. Přidání b>1 opraví tento případ použití;
b=1 vyžaduje konstantní výstup a 0<b<1 samostatně upravený postup.
Výše uvedená realizace sama tuto druhou větev neimplementuje.

Všechny čtyři vrstvy errat pro 21–27 a 469–471 znovu prohledány.
Opravy E1 z 2002/2011 nepřidávají b>1. Stejný závěr platí po
aktuálním obnovení originálů 5. listopadu. Knuthovo přijetí ani
prvenství hlášení tím nejsou doloženy.

## Pramenné výjimky a uzavření

Briggsův primární doklad z X0735 a obsahové souvislosti Meggitt/Chen/
METAFONT z X0734 se přijímají v jejich dosavadním vymezení. Přeskočena
je nedostupná úplná Linského práce a přímé doložení Feynmanova předání
právě tohoto exponenciálního postupu. X0740 zůstává přesným záznamem
toho, co získáno nebylo; nyní neblokuje matematický audit úlohy 28.
Úloha se uzavírá s C0002 a s těmito bibliografickými výjimkami.

Fakticky částečné zůstávají starší atribuce Oresme/Wallis/Newton,
Napierovo rané datování a obecná historická věta o bankách na 22–24.
Vydavatelská změna atribuce značky lg je známá oprava, nikoli důkaz,
že byla nezávisle přečtena celá Truccoova původní práce. Přímá kolace
Cajoriho historické série se přeskakuje. Na 26 se také nezávisle
nedokládá osobní autorství podnětů Hamming/Feynman; matematická tvrzení
jsou ověřena samostatně.

Nově neopravená chyba v tomto bloku nevznikla. V1-X0934 je záznam
průchodu a obecného doplnění; X0935 eviduje známou záměnu u/v při
definici kořene a změnu atribuce lg. Původních uzavřených úloh je
845/932, zbývá 87 částečných. Na 27 pokračuje §1.2.3.

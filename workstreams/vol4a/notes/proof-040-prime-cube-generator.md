# §7.1.1–30: úplný invariant generátoru podkrychlí

6. listopadu 2026, X0069. Originál zadání p82/file99 a odpovědi
p538–539/file555–556. Buddy scan29 přebírán z proof-039. Žádný
program ani enumerace. Správnost výstupu je oddělena od časové meze,
u které je níže konkrétní výhradně algoritmická otázka C0004.

## P0654: reprezentace, všechny buddy příklady a maximalita

Pro n-bitové masky a,b s a&b=0 je c(a,b) množina všech x, které
mají mimo jedničky a pevné bity b. Každá neprázdná podkrychle má
právě jeden takový pár; její dimenze je počet jedniček a.
Pro a=00101,b=01000 je tedy c=01*0*. Volné jsou pozice2 a0,
pevné pozice4,3,1. Jejich překlopení dává postupně vytištěné buddies
11*0*,00*0*,01*1*, všechny a právě tři definované buddies.

Je-li definovaný j-buddy c' rovněž obsažen ve V, sjednocení c∪c'
je větší podkrychle ve V, s pozicí j nově volnou. Obráceně, je-li c
obsažena ve větší podkrychli d⊆V, má d alespoň jednu navíc volnou
pozici j. Příslušný buddy c' je částí d, tedy také ve V. Proto

    c je maximální v V ⇔ její tag je0.

Pojem maximality je inkluzní, ne maximum dimenze. Tag má nulu na
všech volných pozicích a jedničku právě u existujícího obsaženého buddy.

## P0655: inicializace tagů a jejich obecný přenos

V P1 každá bitová pozice j projde všechny j-buddy dvojice bodů
pomocí29. Každý bod má v dané pozici nejvýše jednoho buddy, takže
se bit 2^j přičte právě jednou nebo vůbec; sčítání nevytvoří přenos
do jiné pozice. Výsledné tagy jsou tedy přesné. Body s tagem0 jsou
právě maximální nulorozměrné krychle a lze je ihned vypsat.

Uvažujme nyní dva j-buddies c(a,b),c(a,b⊕2^j), b_j=0, oba ve V.
Jejich sjednocení je c(A,b), A=a+2^j. Pro libovolné ℓ≠j je
ℓ-buddy sjednocení obsažen ve V právě když jsou ve V ℓ-buddies
obou polovin. Jejich unie je totiž přesně tento nový buddy.
Proto nový tag vznikne bitovým průnikem obou tagů a odstraněním j:

    T_new=(T_left & T_right)−2^j.

Bit j je v obou starých tazích1, takže odčítání pouze vymaže tento
bit. Pozice už volné v a zůstávají0. To dokazuje celý předpis P3,
včetně rozhodnutí, zda nový cube vypsat nebo uložit.

## P0656: rozložení zásobníku a bezpečnost zápisů

Každý seznam má data S_s,…,S_(t−1) a ukazatel na začátek S_t=s.
Hodnota t je index řídicího slova, nikoli posledního datového prvku.
Prázdný seznam má S_t=t. Předchozí řídicí slovo je na s−1,
proto pop t←S_t−1 obnoví právě předchozí seznam.

P1 zkomprimuje kladně tagované body v původním pořadí. Při čtení
s platí t≤s, takže případné sdílené pole tagů nepřepíše nečtený
tag. Nakonec S_t=0 označí počátek základního seznamu; A=0.

V P3 se r=t,s=S_t uloží před zápisy. Starý seznam je přesně
S_s,…,S_(r−1). Nové datové položky začínají na r+1, takže nezasáhnou
starý seznam ani jeho ukazatel S_r. Konečné t←t+1,S_t←r+1 vytváří
správný nový řídicí záznam i při nulovém počtu uložených dat.
Buddy scan vypisuje dolní indexy v rostoucím pořadí, a proto je
nový seznam také přísně rostoucí. Jeho b má j-tý bit0, takže splňuje
A&b=0; žádná dodatečná úprava b nechybí. Tagy se čtou pouze na
datových pozicích, nikdy z řídicích slov.

## P0657: maskový průchod a oprávněnost vynechaných větví

Označme L_a úplný seznam všech krychlí c(a,b)⊆V s nenulovým tagem.
Při A=2^e1+…+2^er, e1>…>er, zásobník drží v tomto pořadí seznamy

    L_0, L_(2^e1), L_(2^e1+2^e2), …, L_A.

Všechny kromě případně posledního jsou neprázdné. P1 tento invariant
založí. Je-li poslední seznam neprázdný, P2 začne od bitu0 a binární
přenos odstraní dolní souvislý blok jedniček A. S každou odstraněnou
jedničkou se popne přesně její poslední seznam. První nulový bit j
se přidá. Zbývající vrchol zásobníku je L_a pro a=A_new−2^j,
a v A_new je j nejnižší jednička.

Je-li L_A prázdný a A≠0, P2 začne přenos až u nejnižší jedničky j.
Přeskakuje tím masky A+1,…,A+2^j−1. Každá taková maska přidává
alespoň jednu hvězdičku k A. Pokud by její krychle byla obsažena ve V,
rozdělení podle této přidané hvězdičky by dalo A-krychle s buddy ve V,
tedy s nenulovým tagem. To odporuje L_A=∅. Přeskočené masky tedy
nemohou obsahovat žádný potřebný výstup ani mezivýsledek.
Pokud je prázdný už L_0, byly všechny body vypsány jako maximální
a žádná kladná dimenze nemůže existovat; A=0 správně vede ke konci.

Po přenosu vyrábí P3 právě L_(a+2^j) z L_a. Každá krychle s touto
maskou má dvě jednoznačné a-poloviny, které mají j-buddy a tudíž
nenulový tag; obě jsou v L_a. Žádný potřebný pár tedy filtr tag0
neodstranil. P0655 dává přesný nový tag, vypsané nulové se odstraní
a všechny ostatní vytvoří celý L_(a+2^j). Tím se invariant zachová.

## P0658: úplnost, jedinečnost výstupu a ukončení

Masky A přísně rostou a jsou n-bitové. Zásobníkový přenos navštíví
každou nevynechanou masku jednou; přeskočené větve byly v P0657
dokázány prázdné. Každá krychle vzniká při své jediné masce A
jediným rozdělením podle nejnižší hvězdičky, s jediným dolním b.
Nulorozměrné maximální krychle už byly vypsány v P1.

Každý další výstup má podle P0655 tag0, tedy je maximální podle
P0654. Každá maximální krychle musí být vytvořena nebo už vypsána
v P1, nikdy není skryta v prázdné přeskočené větvi. To dokazuje
správnost, úplnost i žádné opakování výstupů. Konec nastane nejpozději
při přenosu za bit n−1. Prázdné V nevyprodukuje nic a skončí;
pro n=0 jsou pouze konstantní případy, které stejný invariant
nebo přímé ošetření prázdného/jednobodového vstupu řeší bez rekurze.

## P0659: paměťová mez a její přesný okraj

Krychle se stejnou hvězdičkovou maskou dimenze d jsou disjunktní
a každá obsahuje 2^d bodů V. Jeden seznam proto má nejvýše m/2^d
datových položek. V zásobníku je nejvýše jeden seznam každé dimenze
0,…,r. Pro m≥1 je součet jejich délek přísně menší než2m,
tedy nejvýše2m−1. Řídicích slov je r+1≤n+1, celkem nejvýše2m+n,
jak uvádí odpověď. Tentýž argument platí během tvorby nového seznamu.
T potřebuje stejný počet pozic po inicializaci, během ní pouze m.

Pro m=0 je jediná řídicí položka, takže mez2m+n stále platí při
obvyklé doméně n≥1. Pokud by se současně dovolilo m=n=0, je třeba
jedno řídicí místo nebo předem vrátit prázdný výstup; doslovná mez0
řídicí slovo nepočítá. Tento triviální implementační okraj pouze
zaznamenáváme, bez další karty. Není použit v časovém protipříkladu.

## P0660: časová mez a konkrétní přetrvávající otázka C0004

Známá oprava z 13.10.2013 mění původní mn+C na horní mez O(mn+nC),
kde C je celkový počet podkrychlí obsažených ve V. Sama neopravuje P2.
Pro n≥2 zvolme platný neprázdný vstup

    V={0,2^(n−1)}, m=2, C=3.

Existují právě dva body a jejich jediná hrana; vyšší podkrychle
nemůže mít jen dva body. P1 ponechá oba body s tagem2^(n−1).
Pro A=2^h, h<n−1, neexistuje h-buddy pár, takže P3 uloží prázdný
seznam. P2 jej popne a přejde na A=2^(h+1). Pro h=n−1 vznikne
jediná maximální hrana, její tag0 se vypíše a seznam opět zůstane
prázdný. Proto P2 postupně vstupuje do prázdného seznamu s
A=1,2,4,…,2^(n−1).

P2 výslovně nastaví j=0 a následně jej zvyšuje do nejnižší jedničky A.
Při A=2^h je takových zvýšení h. Celkem tedy vykoná

    0+1+…+(n−1)=n(n−1)/2

zvýšení j, kromě dalších lineárně mnoha přenosových zvýšení.
Doslovná smyčka má Ω(n²) operací už v tomto kroku, přestože
mn+nC=2n+3n=5n. Výstup je správný; vadná by byla výhradně uvedená
obecná časová mez pro tuto doslovnou realizaci P2.

Položka C0004 zůstává candidate kvůli přesně vymezenému výkladu:
pokud je celý příkaz „increase j … until“ míněn jako skrytá
konstantní operace hledání bitu, uvedený součet jednotlivých zvýšení
není jejím časem. Taková operace ani její implementace není v P2
uvedena. Matematická stopa doslovně napsaných zvýšení je přesná;
nepotřebuje experiment, nulární případ ani neobvyklou hodnotu vstupu.

## P0661: přímá oprava P2 a důkaz deklarované meze po opravě

Vyhledávání nejnižšího bitu ani není nutné. Po návratu z P3 je j
stále nejnižší jednička aktuálního A, jak dokázal P0657. Lze tedy
upravit začátek P2:

    Je-li vrchní seznam neprázdný, nastav j=0.
    Je-li prázdný a A=0, skonči.
    Je-li prázdný a A≠0, ponech j z předchozího P3.
    Pokračuj původní přenosovou smyčkou P2.

Po P1 je A=0, proto se nikdy nepoužije neplatné staré j z inicializace.
Po každém P3 platí požadovaný invariant j. Oprava proto volí přesně
stejnou hodnotu jako původní hledání, zachovává všechny masky,
zásobníkové kroky i výstupy a odstraní celý kvadratický součet.

P1 stojí O(mn) podle29. Každý neprázdný seznam L_a se použije pro
nejvýše n buddy scanů, přičemž součet délek všech takových seznamů
přes všechny masky je nejvýše C. Scany a vytváření dat tedy stojí
O(nC). Každý pokus o nový seznam vychází z neprázdného rodiče;
počet pokusů je nejvýše n krát počet neprázdných seznamů, tedy O(nC).
Po opravě se každý řídicí záznam vytvoří a popne nejvýše jednou,
a každé zvýšení j v přenosové smyčce právě popne jeden záznam.
Veškerá řídicí práce je tedy také O(nC). Pro n,m≥1 dostáváme
O(mn+nC) v deklarovaném modelu konstantních n-bitových operací.
Prázdný vstup lze vrátit rovnou; necháme-li původní P1 doběhnout,
jeho O(n) inicializační režie se účtuje zvlášť. Nulární konstanty
jsou rovněž přímý okraj, nikoli spor řešený tímto zlepšením.

## P0662: co v dodatku odpovědi30 ještě není prokázáno

Odpověď dále odkazuje na průměrný poměr počtu všech a maximálních
podkrychlí z34, pro rovnoměrné V dané velikosti m≤(1−ε)2^n.
Uvádí poměr **průměrných počtů**, nikoli průměr jejich náhodného
podílu. Celý asymptotický důkaz34 dosud nemáme, stejně jako všechny
odkazované velké výstupy32/116. Tyto tvrzení zůstávají partial;
správnost generátoru ani opravená režie z P0661 je nenahrazuje.
Neurčité „nearly proportional“ se také nesmí používat jako přesná
mez při ignorování délky jednoho n-bitového výstupního záznamu.

## Errata a pokračování

Původní sazba známé časové opravy je ve vlastním renderu
images/proof-errata-pre-p21.png. Prohlédnuty all4a-pre, all4a,
err4a, all4f0 a err4f0, včetně obdobných odpovědí kolem p158–159
Fascicle0; také doplňkově all4f1/err4f1. Žádná další změna P2 ani
časové věty nalezena nebyla. Historické Morreale citace se nezávisle
neověřovaly. Známé přidání faktoru n samo není naše karta.

P0617 už nemá mezeru ve správnosti a úplnosti generování, má přesné
argumenty P0654–P0659; partial nyní zůstává jen pro časovou otázku
C0004. Celá30 navíc zůstává partial pro P0662. P82 obsahuje začátek31
a p539 další odpovědi, proto nemají úplné argumentové pokrytí.

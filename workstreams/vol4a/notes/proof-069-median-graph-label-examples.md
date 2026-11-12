# Celá p67 a první odstavec p68: mediánové grafy a všechny štítky

Checkpoint X0098, P0923–P0931. Původní sazba p67/file84
a p68/file85 přečtena v `images/file084.png` a `file085.png`.
Přesně se přebírají důkazy celé 75 z proof-068, obou
distributivit P0871 a Lemma M P0872 z proof-063, metrické
kritérium P0879 a Theorem G na jeho doložené neprázdné
doméně z proof-064. Žádný program ani opakování těchto důkazů.

## Grafová relace splňuje všechny předpoklady 75 — P0923

Je-li konečný graf neprázdný a splňuje definici median graph,
je propojená každá dvojice u,v: jinak by průnik intervalů
pro trojici u,u,v byl prázdný, protože interval [u..v]
nemá žádnou nejkratší cestu. Vzdálenosti mezi jeho vrcholy
jsou tedy konečné. Intervalové kritérium P0879 dává

    [uxv] ⇔ d(u,v)=d(u,x)+d(x,v).

Axiom 75(i) platí: [uvu] vynucuje 0=2d(u,v), tedy u=v.
Pro axiom (ii) z [uxv] a [xyu] máme

    d(u,v)=d(u,x)+d(x,v)
          =d(u,y)+d(y,x)+d(x,v)
          ≥d(u,y)+d(y,v)≥d(u,v).

Obě nerovnosti jsou rovnosti; proto [vyu], přesně požadovaný
závěr. Axiom (iii) je právě definující jediný bod trojitého
průniku. Celá 75 tedy platí se všemi předpoklady a její
výsledek dává mediánovou algebru. Není pouze citován název úlohy.

Pro prázdný graf je podmínka trojic prázdná a vznikne prázdná
algebra; žádná souvislost prázdného grafu se zde nepoužívá.
Jednobodový graf dává jedinou operaci. Starší P0886 týkající
se slova souvislý v Theorem G tím není rozhodnuta.

## Původní hrany se opravdu obnoví — P0924

Pro různé u,v je interval na hraně délky 1 přesně {u,v}.
Obráceně pokud grafový interval obsahuje jen u,v, jejich
vzdálenost musí být 1; delší nejkratší cesta by poskytla
vnitřní vrchol. Algebraická a grafová intervalová relace
jsou totožné podle 75(c) a Lemma M. Konstrukce hran (61)
tedy vrátí přesně původní graf, nikoli jiný graf se stejným
názvem vrcholové množiny. Prázdný/singletonový případ je prázdný
seznam hran a rovněž souhlasí.

## Každý volný strom je mediánový — P0925

Ve stromu je mezi dvěma vrcholy jediná jednoduchá cesta,
a ta je nejkratší. Pro x,y,z se cesty x→y a x→z protínají
v jediné počáteční části x→w: dvě oddělené společné části
by vytvořily cyklus. Vezměme poslední společný bod w.
Zbývající větve w→y a w→z jsou disjunktní mimo w; jejich
spojení je proto právě cesta y→z. S první společnou částí
x→w se tato cesta protíná jen ve w. Všechny tři intervaly
tedy mají právě jediný společný bod w. Důkaz zahrnuje
opakované vrcholy a jednobodový strom, kdy část větví má délku 0.

## Hyperobdélníky a libovolné Cartesian součiny — P0926

V Cartesian součinu souvislých grafů každá hrana mění právě
jednu souřadnici. Každá cesta od u do v proto potřebuje
alespoň Σ_i d_i(u_i,v_i) kroků. Postupné projití nejkratších
cest jednotlivých souřadnic tuto mez dosáhne. Tedy

    d(u,v)=Σ_i d_i(u_i,v_i),
    [u..v]=Π_i [u_i..v_i].

Druhá rovnost plyne z první: součet nezáporných odchylek
v jednotlivých trojúhelníkových nerovnostech je nulový právě
když je nulová každá. Pro tři vrcholy je pak průnik tří
intervalů součinem průniků v jednotlivých faktorech. Jsou-li
faktory mediánové, je každý takový průnik singleton, a jejich
součin také. To je obecný důkaz všech uvedených součinů.

Hyperobdélník n_1×...×n_m je případ součinu cest na
0,...,n_i−1; intervaly jsou souřadnicové úseky a medián
souřadnicová prostřední hodnota. Jednotkový rozměr nic nemění.
Pokud je některý faktor prázdný, součin je prázdný a tvrzení
o trojicích vrcholů je prázdné. Součin bez faktorů lze
standardně chápat jako jeden vrchol; nevzniká žádný metrický
výpočet s neexistujícími vrcholy.

## Projekce, homomorfismus a bližší konec hrany — P0927

Pro p_uv(x)=m(x,u,v) je (62) doslova dlouhá distributivita
P0871. Podle P0872 má obraz právě interval [u..v] a na něm
je identita. Na hraně u—v je tedy obraz {u,v}, včetně obou
hodnot, protože p(u)=u a p(v)=v.

Navíc p(x) je jednoznačně bližší konec hrany. Je-li p(x)=u,
pak u leží na nejkratší cestě x→v (je v intervalu [x..v]
jako medián trojice x,u,v), a proto d(x,v)=d(x,u)+1.
Je-li p(x)=v, obdobně d(x,u)=d(x,v)+1. Není možná remíza.
To dokazuje metrické pravidlo tabulky bez skrytého předpokladu
bipartitnosti nebo budoucí věty o štítcích.

Na dvouprvkovém intervalu je medián většinou podle majority
a komutativity. Každé jeho označení 0/1 tak převádí projekci
na booleovský homomorfismus. Volba, který konec je 0,
nemění platnost tohoto argumentu.

## Celý obrázek a všech 56 projekcí v (63) — P0928

Z původní kresby jsou přesně hrany

    ac, bc, cd, de, ef, eg, dh.

Všech osm vrcholů je propojeno; graf se získá postupným
připojováním listů, takže nemá cyklus a je to strom se
sedmi hranami. Pro každý sloupec orientujme nulu směrem
k a. Komponenty po odstranění dané hrany, které a neobsahují,
jsou v pořadí sloupců přesně

    ac: {b,c,d,e,f,g,h}; bc: {b}; cd: {d,e,f,g,h};
    de: {e,f,g}; ef: {f}; eg: {g}; dh: {h}.

Příslušnost k této komponentě je hodnota bitu. Podle pravidla
bližšího konce dává úplná tabulka následující údaje, každý
porovnaný s původní sazbou:

| vrchol | ac | bc | cd | de | ef | eg | dh | štítek |
|---|---|---|---|---|---|---|---|---|
| a | a | c | c | d | e | e | d | 0000000 |
| b | c | b | c | d | e | e | d | 1100000 |
| c | c | c | c | d | e | e | d | 1000000 |
| d | c | c | d | d | e | e | d | 1010000 |
| e | c | c | d | e | e | e | d | 1011000 |
| f | c | c | d | e | f | e | d | 1011100 |
| g | c | c | d | e | e | g | d | 1011010 |
| h | c | c | d | d | e | e | h | 1010001 |

## Štítky určují mediány a strom nemá duplikované sloupce — P0929

Každé dva různé vrcholy stromu rozděluje libovolná hrana
jejich jediné cesty. Jejich štítky se tedy liší a označení
je injektivní, včetně jednobodového stromu s prázdným štítkem.
Z homomorfismů jednotlivých souřadnic plyne, že štítek
mediánu je bitový medián štítků. Injektivita umožní výsledek
jednoznačně převést zpět na vrchol.

V příkladu je po souřadnicích

    m(1100000,1011010,1010001)=1010000=l(d),

takže m(b,g,h)=d. Jsou doloženy všechny vstupy i výsledek.

Dvě různé hrany stromu nemohou dát stejný sloupec: konce
jedné hrany se liší v jejím vlastním sloupci, ale jsou na
stejné straně řezu druhou hranou. Jejich dvě hodnoty v druhém
sloupci jsou proto stejné. Sloupce se nemohou shodovat ani
po komplementaci; v zvolené orientaci mají navíc oba u a nulu.
Tím je doloženo i obecné tvrzení posledního odstavce p67.

## Přidání gh opravdu zachová median graph — P0930

Nejprve obecný argument pro spojení dvou mediánových grafů
v jediném společném vrcholu o, bez jiných přechodových hran.
Každý původní graf je konvexní: cesta, která ho opustí a vrátí
se, musí projít o dvakrát a nemůže být nejkratší. Pro x,y
z prvního grafu a z z druhého platí

    [x..z]=[x..o]∪[o..z],
    [y..z]=[y..o]∪[o..z].

Průnik s [x..y] je tedy přesně trojitý intervalový průnik
trojice x,y,o v prvním grafu, a má jediný bod. Jsou-li
všechny tři body na jedné straně, použijeme její medián.
Případy s bodem o jsou zahrnuty a oba směry spojení jsou
symetrické. Spojení v jednom bodě je tudíž mediánové.

Graf z (63) doplněný o gh má jádro čtyřcyklus d—e—g—h—d,
který je K₂□K₂, tedy mediánový podle P0926. K němu se
postupně připojí hrany dc,ca,cb,ef, každá v jediném bodě.
Předchozí argument tím dokazuje mediánovost celého doplněného
grafu; nevyvozuje se z pouhé podobnosti s původním stromem.

## Všech osm původních sloupců a šest různých souřadnic — P0931

Ponechme nulu vždy směrem k a a pořadí
ac,bc,cd,de,ef,eg,dh,gh. Mostové sloupce ac,bc,cd,ef se
nemění. Na čtyřcyklu mají de a gh jedničku přesně na
{e,f,g}; eg a dh přesně na {g,h}. To plyne ze souřadnic
K₂□K₂ a z toho, že připojené větve mají při porovnání
vzdáleností stejný přidaný úsek k jádru.

Všechny hodnoty jsou tedy:

| vrchol | osm sloupců ac,bc,cd,de,ef,eg,dh,gh | po vynechání dh,gh |
|---|---|---|
| a | 00000000 | 000000 |
| b | 11000000 | 110000 |
| c | 10000000 | 100000 |
| d | 10100000 | 101000 |
| e | 10110001 | 101100 |
| f | 10111001 | 101110 |
| g | 10110111 | 101101 |
| h | 10100110 | 101001 |

Proto jsou eg/dh totožné po přejmenování konců e↔d,g↔h,
gh je ekvivalentní de a šestibitové l(g),l(h) souhlasí
s prvními pěti řádky p68. Zbývající sloupce jsou vzájemně
různé: jejich jedničkové množiny jsou čtyři uvedené mostové
řezy a dva různé čtyřcyklové řezy. Žádná další duplicita se
neskrývá. Je osm původních sloupců, protože graf má osm hran;
„seven-bit“ je známé erratum, nikoli nový nález.

## Úplná obsahová mapa p67 a hranice checkpointu

| obsah celé p67 | přesný argument |
|---|---|
| definice intervalů a převod grafu na algebru | P0923/P0924 a celá75 |
| stromy, hyperobdélníky, Cartesian součiny | P0925/P0926 |
| homomorfismus62, projekce a dva možné konce | P0927, přesné převzetí P0871/P0872 |
| osm vrcholů, sedm hran, celý diagram63 | P0928 |
| všech56 projekcí a osm štítků | P0928 |
| bitové mediány, konkrétní bgh=d | P0929 |
| nemožnost duplicit ve stromu | P0929 |
| přidání gh, zachování median graph | P0930 |
| konec odstavce pokračující na68 | všechny sloupce P0931 |

Na p67 není žádná zbývající matematická ani bibliografická
mezera; může dostat `review_depth: argument`. Na p68 je
proveden jen první odstavec. Obecná zero-one reprezentace,
další identity a Theorem C jsou následující samostatný blok;
nepovyšují se na základě tohoto konkrétního příkladu.

Dne 2026-11-07 byly pro p67–68/projekce/labels prohledány
`all4a-pre`, `all4a`, `err4a`, `all4f0`, `all4f1`.
Oprava p68 line5 z 6. 10. 2018 mění seven-bit na eight-bit
a je plně zohledněna. Její sazba je v `proof-y-errata08.png`.
Oprava konce p68 z 18. 6. 2011 patří k pozdějšímu
Theorem C a v tomto bloku se nepovažuje za zkontrolovanou.

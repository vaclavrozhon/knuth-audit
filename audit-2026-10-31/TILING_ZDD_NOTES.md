# Pokrytí oblastí a velikosti ZDD — X262

Kontrola 31. 10. 2026. Zadání str. 155, odpověď str. 482–483.
Autorův draft `fasc5c.ps`, 11. září 2019, má odpověď na str. 186–187.
Historická tištěná Fascicle 5 má odpovídající stranu 291; v all4f5 ani
all4b nebyly níže uvedené opravy nalezeny.

## F058: chybějící horní mez souřadnic

V prvním vymezení nečárkovaných položek v 262(b) má být

    8 <= x+y < n+16,

nikoli pouze `x+y >= 8`. Ostatní meze zůstávají stejné. Doslovný tisk má
16n+92 nečárkovaných a 16n+64 čárkovaných položek. Každá možnost pokrývá
jednu od každého druhu, takže řešení nemůže existovat.

Ještě přímočařeji: všech 28 nadbytečných položek s x+y >= n+16 je
izolovaných. Jejich tři možné čárkované sousedy mají součet souřadnic
nejméně n+15, ale přípustné čárkované položky vyžadují součet < n+15.
Například položka (n+7,15) nemá žádnou možnost pokrytí.

Po doplnění horní meze mají oba druhy 16n+64 položek. Správná oblast dává
přesně vytištěné počty řešení a uzlů ZDD. Kontrola výčtem souřadnic pro
n=0..40 potvrzuje 28 izolovaných položek v každém chybném vstupu.
Znění bylo zkontrolováno v PDF str. 483 i PS str. 187.

## F059: konstanta v obdélníkové asymptotice

Na str. 483, třetí řádek, má být

    #tilings(R_(2m,n)) ~ a_(2m)^(-1/2) * mu_(2m)^(n+1),

jestliže se zachová vytištěná definice a_k. Pro m=1 má totiž a_2=5 a
mu_2=phi, zatímco počet pokrytí obdélníku 2×n je Fibonacciho číslo
F_(n+1) ~ phi^(n+1)/sqrt(5). Poměr skutečnosti k tištěnému odhadu tedy
konverguje k 1/(5 sqrt(5)), nikoli k jedné. Následující tvrzení s Θ je správné.

Obecně položme c_j=cos(j*pi/(2m+1)), b_j=sqrt(1+c_j^2), r_j=c_j+b_j.
Přesný součin pro počet pokrytí je

    product_j (r_j^(n+1) - (-1/r_j)^(n+1)) / (2 b_j).

Protože r_j>1, limitní koeficient je 1/product_j(2b_j). Součin čtverců
jmenovatelů je a_(2m), což dává uvedenou opravu. Tuto součinovou identitu
poskytuje také Chebyshevův polynom U_(2m) v bodě i.

Primární citovaný článek je [Stanley (1985), str. 82, rovnice (2) a lemma](https://math.mit.edu/~rstan/pubs/pubfiles/64.pdf).
**Pozor:** jeho vlastní rovnice (9) na str. 83 má v archivovaném PDF také
vytištěno a_k=2^delta d_k, bez potřebné mocniny −1/2. Nelze ji tedy uvádět
jako správnou kontrolní formuli. Správná konstanta plyne z rovnice (2),
lemmatu a také přímo z Fibonacciho příkladu. Článek je archivován v `sources/`.

Znění knihy potvrzuje PDF str. 483 a PS str. 187. Nezávislá rekurence
spočítala obdélníky výšek 2,4,6,8 a délek 10,40,80,160; všechny přesné
počty souhlasí se součinovým vzorcem při 300místné přesnosti. Normalizované
počty konvergují k opravené konstantě. Fyzický výtisk dosud neověřen.

## Jak se počítá ZDD

C++ programy používají přesnou rekurenci nad zbylými políčky, memoizovanou
podle první nepokryté položky a bitové hranice pokrytí. Počty jsou libovolně
velké celé hodnoty GMP. Každá úspěšná větev odlišného podproblému přidá
jeden instrukční uzel, přesně jako Z6. Dva terminály se přičtou u netriviálního
úspěšného ZDD; prázdná nebo nesplnitelná úloha má jeden terminál.

Nezávislá validace nejprve vypíše všechny exact covers a pak z této rodiny
postaví kanonický ZDD. Pro aztécké oblasti proběhlo 80 malých případů,
pro trojúhelníkové oblasti 15. Souhlasí počty řešení i uzlů; nejde jen o
druhé provedení stejné rekurence.

## Aztécké oblasti: úplný důkaz lineárního vzorce

S_16 má 68719476736=2^36 pokrytí. S_32 má přesně
152326556015596771390830202722034115329 pokrytí. Obě čísla byla nezávisle
ověřena determinantem podepsané bipartitní matice: vodorovná hrana má
váhu 1, svislá v sloupci c má váhu (−1)^c. U oblasti bez děr mají všechny
členy determinantu odpovídající perfektním párováním stejné znaménko.
Poměr znamének dvou párování se rozloží přes střídavé cykly; vnitřek
každého takového cyklu obsahuje sudý počet vrcholů. Absolutní determinant
tedy počítá pokrytí. Toto pravidlo prošlo také všemi 80 malými případy.

Velikost ZDD byla přímo přepočtena pro n=16,28,29,30,31,32,33,34,40.
Pro n≥30 je správný i obecný vzorec 154440n−2655855:

1. Na hranici plných sloupců může z levé strany přečnívat maska, která
   má stejný počet jedniček na sudých a lichých řádcích. Takových masek
   je binom(16,8)=12870.
2. Od levého zkoseného okraje počty dosažitelných masek postupně jsou
   1,2,5,14,42,132,429,1430,4862,8502,11050,12310,12750,12854,12869,12870.
   Po 15 sloupcích je dosažitelná celá tato množina. Je uzavřená pod
   přechodem plným sloupcem, což bylo vyčerpávajícím způsobem ověřeno
   na všech 265729 přechodech. Analogicky se chová pravý okraj.
3. Každý další plný prostřední sloupec má stejné přípustné masky z obou
   stran. Obsahuje 102960 odlišných úspěšných vnitřních podpisů a přidá
   přesně 154440 uzlů. Oba konce přispívají konstantně.
4. Základ n=30 má 1977345 uzlů včetně terminálů. Pro všechna n≥30 tedy
   dostáváme 1977345+(n−30)*154440, jak je uvedeno v knize.

Nejde pouze o extrapolaci z několika hodnot: konečná kontrola hranic a
jejich uzavřenosti dává indukční důkaz pro libovolně dlouhý prostředek.
Certifikát je v `results/aztec_linearity.json`.

## Šestiúhelníky po opravě F058

Pro n=1,5,6,7,8,9,10,16,20 souhlasí rekurence s přesným MacMahonovým
součinem pro box 8×8×n, včetně obou velkých čísel vytištěných v knize.
V malých případech byl součin navíc porovnán s přímým výčtem pokrytí.

Obecný vzorec velikosti ZDD, 257400n−1210061 pro n≥7, byl také dokázán
konečnou kontrolou přechodů. Levá osmisloupcová část dosáhne všech
12870 šestnáctibitových masek váhy 8; její počty po sloupcích jsou
1,9,45,165,495,1287,3003,6435,12870. Pravý konec je její zrcadlový protějšek
se záměnou typů trojúhelníků. Plný sloupec má 735471 přechodů mezi těmito
maskami a přidává 257400 uzlů ze 205920 úspěšných podpisů. Základ n=8 má
849139 uzlů; pro n≥8 tedy platí linearita. Zbývající n=7 má přímo ověřeno
591739 uzlů, rovněž podle vzorce.

Počty svislých kosočtverců v řádcích jsou pevné: řez mezi y−1 a y musí
vyrovnat rozdíl počtů trojúhelníků obou orientací na jedné straně řezu.
Jediné možnosti přes tento řez mají tvar (x,y)–(x,y−1)'. Rozdíly jsou
1,2,...,8,7,...,1, dohromady 64. Malý výčet tuto invariantní řadu také ověřuje.

## Rozsah a reprodukce

Algoritmus nepoužívá MRV, časy Knuthových implementací a přesné mems se
nereprodukují. Historická tvrzení o tehdejším stavu výzkumu arktických křivek
nejsou hodnocena jako nové chyby. Samotné limitní věty o náhodných pokrytích
nebyly znovu dokazovány.

Skripty: `aztec_zdd.cpp`, `hexagon_zdd.cpp`, `check_aztec_zdd.py`,
`check_hexagon_zdd.py`, `check_aztec_linearity.py`,
`check_hexagon_linearity.py`, `check_rectangle_asymptotic.py`.
C++ překlad: `g++ -std=c++17 -O3 ... -lgmpxx -lgmp`.
Výsledky jsou ve stejnojmenných JSON souborech pod `results/`.

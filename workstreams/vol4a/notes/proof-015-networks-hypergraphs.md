# Sítě a hypergrafy, str. 31–35, §7–112 až 123

6. listopadu 2026. Původní sazba file048–052, file061 a proof-file546.
Samostatné argumenty bez programu a bez opakování starých censů.

## Sítě: přesný limit datových tvrzení

Síť je graf s dodatečnými údaji; příklady nepřidávají další matematickou
podmínku. Bishopův přesun z rohu do protějšího rohu desky 8×8 má délku 7
v konvenci délky oblouku board, tedy počet jednotkových diagonálních kroků.
Kompletní síť 128 měst má C(128,2)=8128 hran. Konkrétní váhy miles
(3496 a data z roku 1949), econ (81/4902, tok 44, bilance a záporné dovozy),
games (120/1276, skóre 27–25 a datum), risc (3240/7878 a konkrétní obvod)
nejsou touto aritmetikou ověřeny. Jejich datové a historické části jsou
partial; z definice DAG plyne jen nepřítomnost orientovaných cyklů.
Archivní popis SGB ani budoucí odkazy nejsou vydávány za nezávislou
reprodukci všech generátorů. Známé opravy plane_lisa, level of gray,
obráceného významu oblouku a TAKE_RISC/risc(8) jsou zohledněny.

## Fanoův příklad a incidence

Vrcholy i jména hran jsou nenulové vektory F₂³, incidence e·v=0.
Jádro nenulového lineárního funkcionálu má čtyři prvky, z nichž tři
jsou nenulové. Každá hrana proto obsahuje tři vrcholy; symetrie skalárního
součinu dává každému vrcholu stupeň tři a zároveň izomorfismus s duálem.
Výčty sedmi trojic v (56) odpovídají přímému dosazení. V pořadí
001,010,011,100,101,110,111 jsou řádky (57):
0101010, 1001100, 0011001, 1110000, 0100101, 1000011, 0010110.
Souhlasí s původní maticí. Dva různé nenulové vektory jsou nezávislé,
takže jejich společný kolmý prostor obsahuje právě jeden nenulový vektor:
každá dvojice bodů je na jediné přímce a každé dvě přímky mají jediný bod.

Obrázek bipartitního grafu (57) má po obvodu střídavě
[010],001,[100],010,[001],100,[011],011,[111],110,[110],111,[101],101.
Všech 14 obvodových incidencí platí. Zbývajících sedm hran je
[010]–100, [100]–011, [001]–110, [011]–111, [111]–101,
[110]–001, [101]–010; tím je zkontrolováno všech 21 hran diagramu.
Trojúhelník hypergrafu určuje trojice nekolineárních bodů a naopak.
Kolineárních trojic je sedm, tedy C(7,3)−7=28 trojúhelníků.
Všech šest incidencí vytištěného cyklu (58) má skalární součin nula.

Obecně je K_n^(r) tvořen r-podmnožinami, tedy má C(n,r) hran.
Indukování odebírá právě sloupce, které nejsou obsaženy ve vybrané
množině řádků; uniformní komplement doplní chybějící r-podmnožiny.
Incidenční matice má řádky V a sloupce E; její bipartitní graf používá
disjunktní kopie obou tříd (známé erratum V∩E=∅ z roku 2024).
Duál matici transponuje, proto r-regulární graf dává r-uniformní duál.
Stejné sloupce znamenají opakované hrany; po jejich vyloučení je
charakteristická booleovská funkce (59) s hypergrafem v bijekci.

## Booleovský zápis (60), také úloha 119

Čtyři XOR faktory mají být rovny 1. Nad F₂ z nich plyne
x₃=1+x₁+x₂, x₆=1+x₂+x₄, x₇=x₁+x₂+x₄ a x₅=1+x₁+x₄.
Pro u=1+x₁, v=1+x₂, w=1+x₄ tedy platí
x_j=1+(w,v,u)·binary(j), 1≤j≤7.
Nulová trojice (w,v,u) dává všech sedm jedniček a je právě jedinou
trojicí zakázanou závěrečnou klauzulí ¬x₁∨¬x₂∨¬x₄.
Zbývajících sedm přiřazení jsou přesně charakteristické vektory přímek.
Po odebrání klauzule přibude jediná hrana V, jak tvrdí odpověď 119.
Starší změna (60) a zadání 119 z errat F0 je už v tomto dotisku obsažena.

## Pokrytí, nezávislost, barvení

U pokrývá právě tehdy, když žádná hrana neleží celá ve W=V\U;
to je přesně nezávislost W. Odebrání vrcholu z U odpovídá přidání do W,
proto se minimální a maximální množiny párují. Minimum cover má velikost
|V|−α(H). Sloupcové součty vybraných řádků jsou při pokrytí kladné,
při přesném pokrytí rovny 1. V jednoduchém grafu je součin dvou různých
incidenčních řádků počet jejich společných hran (0 nebo 1), takže
nezávislost je totéž co jejich párová ortogonalita.

Čísla USA 38/11 a 30/19 v (61)/(62), přesné označení všech teček,
maximalita/minimalita a globální optimum 19 zůstávají partial.
Archivní USA239_246 ověřuje jiná rozdělovací optima a stejný zdroj
sousedností, nikoli tento konkrétní nezávislostní certifikát.
Čas pod jednu sekundu je historický benchmark, nereprodukován.
NP-úplnost je externí vstup pro rozhodovací verzi; polynomialita
bipartitního pokrytí a matchingů je odkaz na pozdější algoritmy,
nikoli důkaz na této stránce. Známá oprava rozdělení odkazů §7.5.1/7.5.5
je aplikována. Pro duál grafu je vertex cover množinou původních hran,
které pokrývají původní vrcholy; izolované vrcholy znamenají neexistenci.
Maximum matching je nezávislá množina line grafu přímo podle definice.

Barevné třídy jsou nezávislé. Naopak z pokrytí nezávislými množinami
přiřaď každý vrchol jedné z množin, které ho obsahují; její podmnožina
zůstane nezávislá, takže minimum počtu množin je χ(H).
Klika v G je nezávislá v komplementu, proto ω(G)=α(bar G);
χ(bar G) je minimum počtu klik rozdělujících vrcholy G.
Tyto konečné číselné identity předpokládají existenci barvení/pokrytí:
singletonová nebo prázdná hyperhrana může barvení znemožnit.
Takové okrajové případy nepovyšujeme na nový nález ani nezamlčujeme
konvenci minima nad neprázdnou množinou možností.

## Jednotlivé úlohy

112: žádná reprodukce vyhledání nejrovnostrannějšího trojúhelníku.
Odpověď 748,746,748 má rozptyl délek 2, ale datová správnost,
neexistence přesně rovnostranného a jednoznačnost optima jsou partial.

113: podle definice n řádků (vrcholy) a m sloupců (hrany).

114: smyčka přispívá do svého sloupce 2, obyčejná hrana dvěma jedničkami.
Matice obrázku (26) je 210000 / 011100 / 001122, jak je vytištěno.
Má šest sloupců součtu 2; odpovídající bipartitní multigraf má 3+6
vrcholů a 12 incidencí s násobností. Známé graph→multigraph uplatněno.

115: pro jednoduchý graf má každý sloupec B právě dvě jedničky.
Diagonála BᵀB je 2, mimo diagonálu jsou dva sloupce v součinu 1
právě při společném koncovém vrcholu: BᵀB=2I+A(L(G)).
Analogicky (BBᵀ)_vv=deg(v) a mimodiagonála je A(G), tedy BBᵀ=D+A(G).
Smyčky a paralelní hrany by vyžadovaly jiné formule; zadání mluví o grafu.

116: hyperhrany K_(m,n)^(r) jsou r-podmnožiny, které potkávají obě části.
Jsou přesně komplementem disjunktního součtu K_m^(r) a K_n^(r).
Počet je C(m+n,r)−C(m,r)−C(n,r), včetně r=1, kdy je nulový.

117: izomorfismus přejmenovává vrcholy, takže nerozlišuje pořadí
n násobností singletonových hran; kladné násobnosti jsou partition m
na nejvýše n částí. Pro m=4,n=3 jsou 4,31,22,211, přesně čtyři výpisy.

118: incidenční graf hyperlesa je les s n+m vrcholy, p komponentami
a D=Σdeg(v) hranami. Každý neprázdný strom má |V|−1 hran indukcí
odebráním listu, tedy D=n+m−p (izolované uzly také vyhovují).

120: navržené zobecnění jako posloupnost, injektivní posloupnost nebo
množina zdrojů s jediným cílem dává definované struktury a obsahuje
obyčejné oblouky jako zvláštní případ. Historické „most authors“
a preference terminologie nejsou ověřeny.

121: každou barevnou třídu rozšiř na maximální nezávislou množinu F;
tak získáš pokrytí V množinami F. Naopak každé takové pokrytí obarví H.
V duálu I(H)ᵀ jsou vrcholy prvky F a hrana příslušná v∈V obsahuje
všechny F, které obsahují v. Vybraná F tedy pokrývají tento duál právě
tehdy, když pokrývají V. Předchozí komplementární identita dává
χ(H)=|F|−α(I(H)ᵀ), kdykoli existuje konečné barvení.

122(a): libovolných pět bodů má 15 incidencí se sedmi přímkami, a proto
některou přímku obsahuje celou. Komplement přímky je čtyřbodová afinní
nadrovina e·v=1 a je nezávislý: součet dvou jejích bodů má e·v=0.
Každá nekolineární trojice a,b,c tvoří bázi a její komplement obsahuje
přímku {a+b,a+c,b+c}. Jediné tříbodové covers jsou tedy sedm přímek;
jediné čtyřbodové nezávislé množiny jsou jejich komplementy. α=4.
Při dvou barvách by větší třída musela mít čtyři body, ale druhá by byla
přímka. Tři barvy stačí: {001,011,101,111}, {010,100}, {110}; tedy χ=3.
Známé other three colors→vertices opraveno.

122(b): v duálu Petersena je 15 vrcholů/hraničních objektů. Čtyři původní
hrany nepokryjí deset bodů, takže nezávislá množina má nejvýše 10 prvků.
Pět paprsků je perfect matching; jejich komplement 10 hran je nezávislý
v duálu. Paprsky červeně, ostatní zeleně dávají v každé duální hraně
jednu červenou a dvě zelené, proto α=10 a χ=2. Původní pětiúhelník
zůstává Bergeovým cyklem délky 5; u hypergrafů lichý cyklus nevylučuje
toto slabé barvení. Nejde o rozpor s větou pro obyčejné grafy.

123: graf K_n□K_n má v každém řádku a sloupci kliku n. Barvení n barvami
je proto přesně latinský čtverec; existenci dává barva i+j modulo n.
Maximum potřebných barev je tedy n a korespondence je oboustranná.

Bibliografie Berge 1957, primární definice directed hypergraphs a SGB
kniha nebyly v tomto bloku samostatně dohledávány. Přesná datová tvrzení
zůstávají partial, obecné výše uvedené argumenty na nich nezávisí.
Další důkazový kurzor: §7–124 na file061/p44, odpověď529/file546.

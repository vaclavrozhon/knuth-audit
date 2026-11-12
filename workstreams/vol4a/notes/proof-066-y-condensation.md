# Celá úloha 7.1.1–67: kondenzace Y a přesný 52kamenný obrazec

Checkpoint X0095, P0898–P0904. Originál zadání p88–89/file105–106
a odpovědí p546–547/file563–564 přečten v původní sazbě.
Podrobný výřez obrazce je `images/proof-y52-detail.png`.
Známé erratum z 8. 7. 2011 **prohazuje části (a)/(b)** a nahrazuje
první odpověď důkazem kondenzace. Originální vrstvy opravy jsou
v `images/proof-y-errata08.png` a `proof-y-errata22.png`.
Nejde o vlastní nález. Žádný matematický program ani enumerace.

## Síť, všechny souřadnice a malý diagram — P0898

Nechť n je nezáporné celé číslo. Vrcholy jsou trojice nezáporných
celých čísel se součtem n. Pro pevné z zbývá n−z+1 možností x,
proto je počet vrcholů

    Σ(z=0..n)(n−z+1) = (n+1)(n+2)/2.

Na straně x=0 je přesně n+1 dvojic (y,z); symetricky pro ostatní
strany. Při n>0 dvě nulové souřadnice vynucují třetí rovnu n,
tedy přesně tři rohy. Pro n=0 jediný bod leží na všech třech
stranách; tato zvláštnost je v zadání správně oddělena.

Rozdíl sousedních vrcholů je e_i−e_j, i≠j, což je právě změna
dvou souřadnic o ±1 se zachováním součtu. V řádkovém zápisu

    v(r,j)=(j,r−j,n−r),  0≤j≤r≤n,

jsou hrany v jednom řádku mezi j a j+1, mezi řádky r a r+1
pak j→j a j→j+1. Pro n=3 dávají řádky přesně vytištěná označení

    003;
    012,102;
    021,111,201;
    030,120,210,300.

Šest vodorovných a dvanáct mezířádkových hran z tohoto pravidla
jsou přesně všechny hrany malého diagramu. Žádná další dvojice
nesplňuje souřadnicovou definici.

## Subgridy a jejich složení — P0899

Pro a,b,c≥0 a a+b+c≤n je posun
(x,y,z)↦(x−a,y−b,z−c) bijekcí mezi t_abc a sítí řádu
n−a−b−c. Zachovává všechny hrany. Při rovnosti je jediným
vrcholem abc; t_001 skutečně vynechá právě spodní stranu z=0.
Pro a+b+c>n je množina prázdná a nepoužívá se jako vstup do
níže uvedených rekurencí, jejichž řád je vždy nezáporný.

Dva dovolené posuny se sčítají souřadnici po souřadnici:

    (t_abc)_def = t_(a+d)(b+e)(c+f) = (t_def)_abc.

To je celé tvrzení použité ve druhé odpovědi, včetně jeho domény.

## Kondenzace, černé Y dole implikuje černé Y nahoře — P0900

Pišme D(t)=t*, kde vrchol q řádu n−1 má barvu

    D(t)(q)=m(t(q+e_1),t(q+e_2),t(q+e_3)).

Předpokládejme n>0 a černé Y, tedy souvislou černou množinu C
dotýkající se všech stran. C má alespoň dva vrcholy, protože
žádný jediný vrchol při n>0 neleží na všech třech stranách.

Každou hranu a—b v C pošleme na q=min(a,b), minimum po
souřadnicích. Součet souřadnic q je n−1 a a,b jsou dva rohy
malého trojúhelníku q+e_1,q+e_2,q+e_3. Proto je q v t* černý.

Dvě po sobě jdoucí hrany a—b—c mají obrazy b−e_i a b−e_j.
Jsou buď stejné, nebo sousední. Zde je výslovně doplněn případ
shodných obrazů, který stručná opravená odpověď nevyčleňuje.
Hrany libovolného souvislého grafu s alespoň jednou hranou lze
spojovat takovými řetězci, takže množina jejich obrazů je souvislá.

Pokud v∈C leží na straně x=0, existuje v C incidentní hrana
v—w. Její obraz má x=min(v_x,w_x)=0. Totéž platí pro y,z.
Obrazy hran proto obsahují černé Y v t*. Důkaz pokrývá n=1:
všechny obrazy se tehdy mohou slít do jediného vrcholu.

## Kondenzace, černé Y nahoře implikuje černé Y dole — P0901

Pro černý vrchol q v t* nechť B(q) jsou všechny černé rohy
trojúhelníku {q+e_1,q+e_2,q+e_3} v t. Obsahuje alespoň dva
vrcholy a je souvislá, protože všechny tři rohy tvoří kliku.

Jsou-li q,r sousední, pišme r=q+e_i−e_j a nechť k je třetí
index. Jejich trojúhelníky mají společný roh

    a=q+e_i=r+e_j.

Je-li a černý, B(q) a B(r) se protínají. Je-li bílý, jsou
v obou trojúhelnících ostatní dva rohy černé. Zejména černé
q+e_k a r+e_k jsou sousední, protože se liší o e_i−e_j.
Proto sjednocení B(q) přes souvislé černé Y v t* je souvislé.

Má-li q například x=0, pouze jeden ze tří jeho rohů může
mít x>0. Alespoň jeden ze dvou černých rohů tedy leží na
původní straně x=0. Pro každou stranu se to opakuje, takže
sjednocení obsahuje černé Y v t. Platí i tehdy, když horní Y
je jediný vrchol řádu 0. Oba směry dávají Y(t)=Y(t*).

## Pyramida, selfdualita a monotónnost — P0902

Řád se každým D sníží o jednu. Po n krocích zbývá jediná
barva b; podle obou právě dokázaných směrů platí Y(t)=b.
Základ n=0 je skutečně hodnota jediné proměnné, neboť jediný
černý bod sám tvoří Y. Tím jsou doloženy ukončení i význam
vrcholového kamene, nikoli jen lokální pravidlo kondenzace.

Boolean median je monotónní a selfduální (přesně převzato
z proof-059-medians-post-theorem.md). D proto komutuje
s komplementací všech barev a zachovává souřadnicové pořadí.
Po n krocích to dává

    Y(¬t)=1−Y(t),   t≤s ⇒ Y(t)≤Y(s).

Monotónnost lze také přímo číst ze zachování černého svědka Y.
Existence černého Y je tedy ekvivalentní neexistenci bílého Y,
včetně všech krajních obarvení a n=0. Žádná topologická
neprůchodnost ani selfdualita nebyla v důkazu kondenzace použita.

Při přímém vrstveném provedení je počet mediánů přesně
Σ(k=1..n) k(k+1)/2 = n(n+1)(n+2)/6, bez rozbalování stejného
podvýrazu do stromu. Dvě sousední vrstvy mají nejvýše
(n+1)² hodnot; jde tedy o O(n³) kroků a O(n²) paměti.
Tyto náklady jsou doplněné odvození, ne vytištěný nárok knihy.

## Rekurence a původní geometrický argument — P0903

Posun t↦t_a komutuje s D, protože oba výrazy v bodě q
berou medián stejných hodnot t(a+q+e_i). Indukcí komutuje
i s opakovanou kondenzací v jejich společné doméně.

Před posledním krokem D^n zbývají tři hodnoty na e_1,e_2,e_3.
Hodnota na e_i je přesně vrcholová hodnota kondenzace t_(e_i),
tedy Y(t_(e_i)). Proto

    Y(t)=m(Y(t_100),Y(t_010),Y(t_001))  pro n>0.

To dokazuje původní část (a), po erratu část (b), z již
nezávisle dokázané kondenzace. Pro n=1 jsou všechny t_(e_i)
jednobodové, takže se vzorec redukuje na obyčejnou většinu.

Lze navíc přesně doplnit původní tvrzení, že dvě Y v t_100
a t_010 se protínají nebo jsou sousední. Nechť A,B jsou
taková Y a předpokládejme opak. Vyberme a=(1,y,z)∈A
a b=(x,1,z')∈B. Přidáním a'=(0,y+1,z) k A vznikne Y
v celé síti; přidáním b'=(x+1,0,z') k B také. Žádný přidaný
bod neleží ve druhé původní množině, jinak by A,B byly
sousední. Navíc a'≠b', protože a'_x=0 a b'_x≥1.
Vznikla by dvě disjunktní Y v celé síti. Obarvením prvního
černě a zbytku bíle by existovala Y obou barev, což odporuje
již dokázané selfdualitě. Proto původní lokální tvrzení platí.
Jejich spojené Y se dotýká x strany díky B, y strany díky A
a z strany díky oběma. Stejně platí kterékoli dvě posunuté sítě.

Původní indukční odpověď tím má doložen přesný geometrický
krok; opravené pořadí však poskytuje samostatný důkaz bez
kruhového předpokladu, že obě barvy nemohou mít Y.

## Všech 52 černých kamenů a minimalita — P0904

Velký obrazec na p88 má **řád 15**, nikoli 14; neprohlašuje
52 za maximum. Souřadnice r,j níže jsou ty z P0898. Původní
sazba dává následující úplné seznamy černých j v řádku r:

| r | černá j |
|---|---|
| 0 | žádné |
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 4 | 3 |
| 5 | 1,2,3 |
| 6 | 1 |
| 7 | 1,3,4,5,6 |
| 8 | 1,3,7 |
| 9 | 1,3,5,6,8 |
| 10 | 2,4,5,7,9 |
| 11 | 3,6,8,10 |
| 12 | 1,2,4,5,6,8,10 |
| 13 | 1,3,8,10 |
| 14 | 0,1,4,5,6,7,8,11,12,13 |
| 15 | 14 |

Počty po řádcích jsou
0,1,1,1,1,3,1,5,3,5,5,4,7,4,10,1, se součtem 52.
Všechny černé hrany tvoří tři cesty z jediného centra (10,5):

    (10,5)—(11,6)—(12,6)—(12,5)—(12,4)—(11,3)
    —(10,2)—(9,1)—(8,1)—(7,1)—(6,1)—(5,1)
    —(5,2)—(5,3)—(4,3)—(3,2)—(2,1)—(1,1);

    (10,5)—(10,4)—(9,3)—(8,3)—(7,3)—(7,4)
    —(7,5)—(7,6)—(8,7)—(9,8)—(10,9)—(11,10)
    —(12,10)—(13,10)—(14,11)—(14,12)—(14,13)—(15,14);

    (10,5)—(9,5)—(9,6)—(10,7)—(11,8)—(12,8)
    —(13,8)—(14,8)—(14,7)—(14,6)—(14,5)—(14,4)
    —(13,3)—(12,2)—(12,1)—(13,1)—(14,1)—(14,0).

Každá má 17 hran a mimo centrum jsou disjunktní. Pro kontrolu
absence tětiv stačí úplný seznam řádků: vodorovně jsou právě
sousední j, celkem 17 hran. Mezířádkově jsou přesně tyto dvojice
j→k mezi r a r+1:

| r | j→k |
|---|---|
| 0 | žádné |
| 1 | 1→1 |
| 2 | 1→2 |
| 3 | 2→3 |
| 4 | 3→3 |
| 5 | 1→1 |
| 6 | 1→1 |
| 7 | 1→1,3→3,6→7 |
| 8 | 1→1,3→3,7→8 |
| 9 | 1→2,3→4,5→5,6→7,8→9 |
| 10 | 2→3,5→6,7→8,9→10 |
| 11 | 3→4,6→6,8→8,10→10 |
| 12 | 1→1,2→3,8→8,10→10 |
| 13 | 1→1,3→4,8→8,10→11 |
| 14 | 13→14 |

Je to 34 hran, všechny na třech uvedených cestách. Dohromady
51 hran tedy tvoří přesně popsaný strom na 52 vrcholech.
Jediné černé body na stranách y=0,z=0,x=0 jsou po řadě
koncové body (1,1), (15,14), (14,0). Každé černé Y musí
obsahovat všechny tři. Jediný podstrom spojující tyto konce
je celý strom, takže každý ze 52 kamenů je nezbytný.
Po změně kteréhokoli na bílý černé Y zanikne; podle P0902
právě tehdy existuje bílé Y. Tím jsou doložena všechna
tvrzení o obrazci, nikoli globální optimum z úlohy 68.

## Errata, bibliografické meze a rozsah

Dne 2026-11-07 prohledány všech pět relevantních vrstev
`all4a-pre`, `all4a`, `err4a`, `all4f0`, `all4f1`, podle
stran 88/89/546/547, 67, Milnor/Schensted, kondenzace a Y.
Zohledněny jsou přeuspořádání p89 a náhrada odpovědi p546
z 8. 7. 2011. Oprava p547 line −5 z 2. 1. 2012 patří
odpovědi 75(b), nikoli 67. Historická F0 náhrada odpovědi 68
z 25. 8. 2008 je již v tomto dotisku; není naším nálezem.

Soukromé dopisy Schensted→Gardner (21. 1. 1979, 28 stran)
a Milnor→Gardner (26. 3. 1957) nebyly dostupným primárním
archivem nezávisle ověřeny. Historická data/rozsah dopisů a
název hry Triangle jsou bibliografická výjimka; důkaz je vlastní
a jejich obsah nepoužívá jako neověřený matematický vstup.

Celá úloha 67 i opravená odpověď mají nyní argument. P88
nepovyšujeme na úplnou argumentovou stránku kvůli starší
společné doménové mezeře P0863 v 65/66; p89 obsahuje další
úlohy. P546 obdobně zachovává P0863. Neproběhl žádný census
maximálních Y ani aplikace pyramidy jako program na obrazci.

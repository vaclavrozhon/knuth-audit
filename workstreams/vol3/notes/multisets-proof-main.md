# Multisety: jednotlivé argumenty hlavního textu

S.22–31. Základní algebra, věty A–C, všechny počítací vzorce a jejich
vytištěné příklady mají níže samostatné argumenty. Dopředně jsou
doloženy také úlohy12 a13, potřebné pro hlavní text. Bez běhu a bez
nového nálezu. Sazba vztahů20–30 a důkazů na25–27 prohlédnuta.
Historické citace a priority se přebírají jako výslovně neověřená
bibliografie; známé opravy v sources/multisets-errata-review.json.

## Počítání a aritmetické příklady

Označení jednotlivých kopií dá n! uspořádání. Každé neoznačené
slovo má přesně∏n_i! označení, protože každou skupinu stejných
písmen lze nezávisle očíslovat. To dokazuje multinomiální vzorec.
U3a,2b,c,4d je10!=3628800, součin faktoriálů288 a podíl12600.
Šest různých prvků má6!−2=718 pořadí mimo rostoucí a klesající.

Číslice4,8,5,5,5 dávají20 slov. Na každém místě se vyskytne4 čtyřikrát,
8 čtyřikrát a5 dvanáctkrát, takže součet číslic na místě je108.
Součet všech čísel je108·11111=1199988, stejný jako vytištěný
27·120·11111/(5·6). Novější historická oprava uvádí počet
15!/(4!3!3!2!)=756756000; násobení posledního čísla1728 dává15!.
Hudební pramen ani identifikace not v historickém tématu nebyly ověřeny.

## Interkalace jako součin front

Pro každé horní písmeno x označme Q_x(π) posloupnost dolních písmen
pod x zleva doprava. Interkalace splňuje
Q_x(α⊤β)=Q_x(α)Q_x(β), prosté zřetězení. Fronty určují slovo
jednoznačně, pokud horní řádek čteme ve zvoleném uspořádání.
Asociativita, obě krácení a prázdná identita tedy plynou přímo
z týchž vlastností zřetězení. Mají-li faktory disjunktní písmena,
pro každé x je alespoň jedna fronta prázdná; faktory proto komutují.

Pro cadab jsou fronty Q_a=ca,Q_b=d,Q_c=a,Q_d=b; pro bddad
Q_a=b,Q_b=d,Q_d=dad. Součin má fronty cab,dd,a,bdad, tedy
cabddabdad. Obrácený součin má bca,dd,a,dadb, tedy bcaddadadb;
to dokládá nekomutativitu a současně řeší úlohu2.

Cyklus je seznam hran x_1→x_2→…→x_n→x_1, se zachováním pořadí
odchodů z každého x. Cyklus(dbddacaabd) dává fronty cab,dd,a,bdad,
přesně vytištěný příklad. Obecná rotace může změnit fronty:
(aab) dává aba, ale(aba) dává baa. Rotace přes jediné y však
pořadí v žádné frontě nezmění. Pro disjunktní obyčejné cykly
interkalace a obvyklé skládání popisují tutéž funkci na jejich nosičích.

## Nejkratší levý faktor

Fronty lze chápat jako orientované hrany; v každém vrcholu je počet
vstupů stejný jako počet výstupů. Začněme v daném písmenu y a vždy
odeberme první dosud nepoužitou hranu aktuální fronty, až se poprvé
vrátíme do y. Mimo y nemůžeme uváznout: právě navštívený vrchol
má o jeden použitý vstup více než výstup, a vyčerpání všech výstupů
by překročilo celkový počet vstupů. Konečný počet hran vynutí návrat.

Uzavřená cesta používá prefix každé navštívené fronty, a proto je
levým faktorem π. Každý jiný levý faktor obsahující y musí obsahovat
jeho první hranu; bilance vstupů a výstupů jej postupně nutí obsahovat
celou cestu. Tím je faktor nejkratší a určený jednoznačně. Cyklus
s jediným y nemůže tuto cestu prodloužit: jeho jediný návrat do y
musí být až na konci. To dokazuje přesné tvrzení14, i n=0 pro smyčku(y).

Uπ=dbcbcacdaddbbbd jsou fronty Q_a=db,Q_b=cbcac,Q_c=dad,Q_d=dbbbd.
Start v a prochází a→d→d→b→c→d→b→b→c→a; start v b dává
b→c→d→d→b. Získají se oba vytištěné levé faktory(ddbcdbbca)
a(cddb), včetně mezikroku13.

## Kanonická faktorizace a věta B

Opakované odstraňování nejkratšího faktoru obsahujícího nejmenší
zbývající y dává cykly končící jediným minimálním y a neklesající
posloupnost těchto konců. Délka klesá, takže konstrukce skončí.
V každé faktorizaci splňující16 musí být první y celkovým minimem;
právě dokázaná jednoznačnost prvního cyklu, krácení a indukce
určí zbytek. Prázdná permutace odpovídá t=0. To je věta A.

V uvedeném příkladu zůstanou po prvním cyklu fronty b,ac,d,bd.
Další cykly jsou(ba),(cdb),(d), tedy přesně17. Po odstranění závorek
vznikne ddbcdbbcabacdbd. Obráceně jakékoli slovo rozřízneme po
prvním výskytu nejmenšího zbývajícího písmene, opakovaně. Získáme
právě podmínky16, takže vypuštění závorek je bijekce všech slov.

První dolní prvek původního slova je první hrana z nejmenšího
horního písmene, tedy první prvek výsledného slova: věta B(a).
Každá sestupná hrana y→x, y>x, leží uvnitř vypsaného cyklu;
závěrečná uzavírací hrana z minima sestupná není. Ani přechod
mezi cykly není sestupný, protože koncová minima neklesají.
Proto každý jednotlivý sestupný typ sloupce odpovídá právě jedné
sousední dvojici yx a naopak: B(b). V příkladu jsou tři d→b
v Q_d a tři db v novém slově, na pozicích2,5,13.

## Třípísmenné sousednosti, vzorec20

V horních blocích a,b,c délek A,B,C zvolme dolní a v počtech
A−k−m,m,k. Máme choose(A,A−k−m)choose(B,m)choose(C,k) voleb.
Zbylých míst pod a/b je B+k, a vybereme v nich B−l dolních b;
pod c vybereme l ze C−k míst. Zbytek tvoří c. Tím vzniká přesně
součin pěti binomických koeficientů20. Věta B převádí podmínky
sloupců na počty sousedností ca,cb,ba. Neproveditelné volby přispívají0.

## Prvočíselná faktorizace

Neprázdný cyklus bez opakování má pro každý svůj prvek nejkratší
levý faktor rovný celému cyklu, takže je nerozložitelný. Permutace
bez opakování, která není jediným cyklem, má vlastní disjunktní
cyklus jako faktor. Při opakovaném y obsahuje nejkratší faktor y
jen jednou, takže je vlastní. Jednotka ε se chápe jako prázdný
součin; tím je doložena klasifikace prvočinitelů i existence rozkladu
rekurzí podle délky.

Nechť ρα=σβ a prvočiniteleρ≠σ. Kdyby měly společné y, oba by
byly jediným nejkratším faktorem obsahujícím y, spor. Jsou disjunktní.
Frontyρ jsou prefixy front celé permutace a frontyσ v těchto písmenech
jsou prázdné, takžeρ je levým faktoremβ. Po odebráníρ vznikneθ;
krácení a komutativita disjunktních faktorů dávajíα=σθ,β=ρθ.
Indukce na délce a prohozeníρσ dokazují přesnou jednoznačnost věty C.

Příklad22 má činitelé P=(ab),Q=(a),R=(cd),S=(bc) a jediné
vynucené vztahy P<Q,P<S,R<S. Začíná-li P, jsou tři pořadí zbytku;
začíná-li R, musí následovat P a zbytek má dvě pořadí. Dostáváme
přesně pět uvedených řádků, všechny s frontami ba,ac,db,c a slovem baacdbc.

## Vzorce23–27

Bez smyček a s m hranami a→b bilance jednoznačně určí
a→c=A−m, c→b=B−m, c→a=C−B+m, b→c=C−A+m,
b→a=A+B−C−m. Výběr pořadí v každé ze tří front dává
N(A,B,C,m)=choose(A,m)choose(B,C−A+m)choose(C,B−m).

Možné jednoduché cykly jsou právě(ab),(ac),(bc),(abc),(acb).
Každé dva sdílejí písmeno, takže jejich pořadí je skutečně jediné.
Při k výskytech(abc) vynutí hrany násobnosti
m−k,C−B+m−k,C−A+m−k,k,A+B−C−2m+k
ve výše uvedeném pořadí cyklů. Součet je C+m−k. Multinomiální
počet uspořádání a součet přes přípustná k dává první řádek25.
Rozpis faktoriálů dává jeho druhý řádek přesně, včetně všech pěti
jmenovatelů. Po krácení choose(A,m) dostaneme26.

Substituce M=A+B−C−m,N=C−B+m,R=B,S=C,j=C−B+m−k dává
M+N=A, M−R+S=A−m, N+R−S=m, R+j=C+m−k.
Oba pravé binomické koeficienty se přepíší doplňkovými dolními
indexy. Vzorec27 je tedy přesně tatáž identita v přejmenovaných
parametrech na této kombinatorické oblasti; původní historický odkaz
se nepoužívá jako náhrada tohoto dvojího počítání.

## Čtyři písmena, cykly29 a dopředná úloha12

V tabulce28 jsou povoleny obě orientace hran čtyřúhelníku
a—b—c—d—a. Součty řádků/sloupců jsou A,B,C,D právě při
A+C=B+D. Jednoduché cykly jsou čtyři dvojice a dva oběhy délky4;
žádný trojúhelník není možný a více než4 různých vrcholů není.

Při s cyklech(abcd) dostáváme z hran a→b,b→c,c→d,d→a
počty α=A−r−s, β=B−q−s, γ=D−r−s, δ=A−q−s pro
(ab),(bc),(cd),(da). Z a→d dostanemeφ=q−A+r+s pro(dcba).
Zbylé hrany pak mají automaticky počty q,B−A+r,D−A+q.
Tím je dokázána celá tabulka29 a úloha12.

Jediné netriviální komutace jsou mezi(ab)/(cd) a(bc)/(da).
Pojmenujme cykly a,b,c,d,e,f v pořadí29. Orientujme prohození
ca→ac a db→bd. Lexikografické pořadí klesá, takže skončíme.
Levé strany se nepřekrývají; disjunktní prohození lze provést
v libovolném pořadí se stejným výsledkem. Indukce na zbývajících
krocích proto dává jediný normální tvar bez ca a db. To samostatně
dokazuje přesnou zvláštní instanci úlohy10 použitou v hlavním textu.

## Dopředná úloha13 a počet normálních tvarů

U šesti písmenných četností α,β,γ,δ,ε,φ převádí věta B zákaz
ca a db na zákaz dolních a pod c a dolních b pod d. Dejme
S=α+β+ε+φ. Nejprve umístíme α−t dolních a pod d,
choose(δ,α−t) způsoby; zbývajících t a do S míst mimo c,d,
choose(S,t) způsoby. Pro b zbývá mimo d právě S+γ−t míst,
tedy choose(S+γ−t,β). Zbývajícíγ+δ+ε+φ místa vyplníme
ostatními písmeny multinomiálním počtem. Součet přes t je přesně
vzorec úlohy13 i její odpověď.

Po dosazení cyklových četností29 platí S=B aγ+δ+ε+φ=D.
Dostáváme levý dvojnásobný součet na30, se všemi uvedenými
faktoriály. Přímý výběr čtyř front tabulky28 naproti tomu dává
choose(A,r)choose(B,q)choose(C,D−r)choose(D,A−q),
kde C=B+D−A, přesně pravou stranu téhož vztahu.

## Vzorec30 a jeho deklarované vyčíslení

Po vydělení choose(D,A−q) se součin faktoriálů jednoho s,t-členu
přepíše na
choose(B,t)choose(A−r−t,s)choose(B+D−r−s−t,D+q−r−t)
·choose(D−A+q,D−r−s)choose(A−q,r+t−q).
Rozpisy dávají stejné jmenovatele s!, (A−r−s−t)!, (D−r−s)!,
(q−A+r+s)!, (r+t−q)!, takže vzorec30 souhlasí.

V součtu přes s položme j=D−r−s a v27 vezměme
M=q−t,N=D−r,R=B−t,S=B+D−A=C. Tři faktory závislé na s
se sečtou na choose(B−t,q−t)choose(C,D−r). Pro t>q je původní
součet nulový: dolní a horní mez s si odporují. Zbytek vyčíslí
choose(B,t)choose(B−t,q−t)=choose(B,q)choose(q,t)
a Vandermondův součet
Σ_t choose(q,t)choose(A−q,r−q+t)=choose(A,r).
Výsledkem je přesně pravá strana30. Všechny matematické kroky
závěrečného odstavce jsou tím doloženy bez numerické enumerace.

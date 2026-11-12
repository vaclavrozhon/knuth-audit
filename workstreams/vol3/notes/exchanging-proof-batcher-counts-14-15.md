# Batcher14–15: všechny konečné počty a aktuální doplněk2021

7. listopadu2026. Originál135/file146 a630/file641 zobrazen.
Dopředné224/file235 a226/file237 jsou v
`sources/batcher-count-cross-reference.pdf` a zobrazených
`images/batcher-count-cross-reference-{1,2}.png`.
P0984–0989 a P0997–1001 dodávají algoritmus a program;
zde jsou nové obecné počty, bez matematického běhu.

Známý dodatek2021 k odpovědi15 identifikuje funkci s§5.3.4(10).
Je zahrnut v P1011, nikoli jen bibliograficky spárován. Pět vrstev
je pro hlavní blok v `sources/exchanging-errata-review.json`.
U224/226 byly navíc přečteny všechny příslušné záznamy těchto
pěti vrstev: změna obrázku48 na(7,4), opravy y_n/jména a
historických optimálních počtů nemění použité rekurence(4),(10).
Celé pozdější stránky tím nejsou zkontrolované.

## P1003: celé14(a), počet posledního slučování a základ

Definuj c(0)=c(1)=0. Pro N=2^t,t≥1 poslední p=1 cyklus
nejprve porovná2^(t−1) párů. Další mezery d=2^j−1,
j=t−1,…,1, mají2^(t−1)−2^(j−1) přípustných sudých
jedničkových začátků. Počet posledního slučování je tedy

    2^(t−1)+Σ_(j=1)^(t−1)(2^(t−1)−2^(j−1))
     =(t−1)2^(t−1)+1.

Předchozí sudé vzdálenosti pracují nezávisle na obou polovinách
pozic podle parity a po přeznačení jde o stejný algoritmus.
Proto c(2^t)=2c(2^(t−1))+(t−1)2^(t−1)+1. Pro t=1
je suma prázdná a c(2)=1, takže základ není vynechán.

## P1004: celé14(b) a skutečný podkvadratický sériový řád

Pro x_t=c(2^t)/2^t,x_0=0 je

    x_t=x_(t−1)+(t−1)/2+2^(−t)
       =t(t−1)/4+1−2^(−t),
    c(2^t)=2^(t−2)(t²−t+4)−1.

Součet geometrické řady i lineární řady je konečný a přesný.
Platí také při t=0. Monotónnost počtu s velikostí, doložená
níže P1005, dává pro2^e≤N<2^(e+1) meze příslušnými dvěma
mocninami, a tedy c(N)=Θ(N(log N)²).

V opraveném MIX programu je0≤B≤C=c(N),0≤E≤A=O(log²N)
a T=O(log N). Přesný čas P0999 proto také je
Θ(N(log N)²), a tedy o(N²). To je sériový řád této konkrétní
implementace; neuzavírá nevymezené praktické srovnání P1002.

## P1005: skutečně nové dvojice a obě rekurence15(a)

Při zvětšení souboru z N na N+1 zůstanou všechny původní
dvojice zachované. Pokud se změní t, přidaný první cyklus
p=N a přidané první dlouhé mezery dalších cyklů mají před
zvětšením pouze prázdné smyčky. Případně lze oba soubory
rovnou chápat jako omezení téže větší kapacity na prefix.
Nové porovnání proto vždy končí v nové nulté pozici N:
i+d=N. Tím je zdůvodněn pokyn odpovědi15, včetně překročení
mocniny2; c je monotónní.

Označ μ(N) počet porovnání posledního p=1 slučování,
μ(0)=μ(1)=0, a x(N)=μ(N+1)−μ(N). Je-li N liché, nová
pozice je pravým koncem právě jedné počáteční sousední dvojice.
Pozdější mezery končí na sudých nultých indexech, takže x(N)=1.
Je-li N≥2 sudé, počáteční dvojice nepřibude a pozdější nové
dvojice mají d=2^j−1,1≤j≤⌊lg N⌋. Všechny mají levý
index N−d lichý a nezáporný. Proto x(N)=⌊lg N⌋.
Dále x(0)=0.

Z rozkladu podle parity platí pro každé N

    c(N)=c(⌈N/2⌉)+c(⌊N/2⌋)+μ(N).

Případná nadbytečná kapacita kratší poloviční sítě přidává jen
prázdné smyčky, jak bylo právě doloženo. Pro a(N)=c(N+1)−c(N)
tedy a(0)=0 a

    a(2n)=a(n)+⌊lg(2n)⌋  (n≥1),
    a(2n+1)=a(n)+1       (n≥0).

Právě odvozené x také splňuje x(N)=a(N)−a(⌊N/2⌋).

## P1006: celý binární vzorec15(a)

Piš N=2^e_1+…+2^e_r>0,e=e_1>…>e_r≥0. Rozvinutím
rekurence vznikne a(N)=Σ_(k=0)^e x(⌊N/2^k⌋).
Je-li bit b_k=1, přispívá1; je-li b_k=0, přispívá e−k.
Proto

    a(N)=r+Σ_(k:b_k=0)(e−k)
        =binom(e+1,2)−r(e−1)+(e_1+…+e_r).

Vedoucí bit k=e je vždy1 a přispívá1. Vzorec tak zahrnuje
N=1 i každý okraj dolního nenulového bitu; není předpokládáno
liché N ani pevný počet bitů.

## P1007: celé15(b), z(n), oba parity a ukončení sumy

Polož b(n)=c(n+1)=Σ_(j=0)^n a(j), b(0)=0, a
y(n)=Σ_(j=1)^n x(j), y(0)=0. V součtu a(1)+…+a(2n)
přidá rekurzivní část a(⌊j/2⌋) jednou a(0), dvakrát
a(1),…,a(n−1) a jednou a(n). Proto

    b(2n)=2b(n)+y(2n)−a(n).

Pro2n+1 se poslední a(n) objeví podruhé, takže
b(2n+1)=2b(n)+y(2n+1). Definice
z(2n)=y(2n)−a(n), z(2n+1)=y(2n+1) proto dává

    b(N)=2b(⌊N/2⌋)+z(N)
        =Σ_(k≥0)2^k z(⌊N/2^k⌋).

Poslední zápis je konečný, protože z(0)=0 a b(0)=0. To je
přesně požadované c(N+1); nesmí se zaměnit s c(N).

## P1008: celé15(c), přesný součet logaritmů a N=1

Z x(2j−1)=1 a x(2j)=1+⌊lg j⌋ plyne pro m=⌊N/2⌋

    y(N)=N+Σ_(j=1)^m⌊lg j⌋.

Při m≥1,s=⌊lg m⌋ počítáme každý příspěvek výšky h:

    Σ_(j=1)^m⌊lg j⌋
     =Σ_(h=1)^s(m−2^h+1)=s(m+1)−2^(s+1)+2.

Pro N≥2 je s=e_1−1, tedy

    y(N)=N+(⌊N/2⌋+1)(e_1−1)−2^e_1+2.

Při N=1 je původní suma prázdná a pravá strana výslovně
dává1, takže stejný vzorec platí. N=0 má zvláštní definici
y(0)=0; nebere se logaritmus nuly. Externí cvičení1.2.4-42
není potřebným předpokladem tohoto odvození.

## P1009: obě pomocné konečné identity v odpovědi15(d)

Pro S_n=Σ_(k=0)^n2^k(n−k) je S_0=0 a
S_n−S_(n−1)=Σ_(k=0)^(n−1)2^k=2^n−1. To jednoznačně
dává S_n=2^(n+1)−n−2.

Pro T_n=Σ_(k=0)^n2^k binom(n−k,2) je T_0=0 a
Pascalova identita dává T_n−T_(n−1)=S_(n−1)=2^n−n−1.
Tedy T_n=2^(n+1)−binom(n+2,2)−1. Platí n≥0 včetně
obou prázdných krajních příspěvků, přesně jako v originálu.

## P1010: celý uzavřený vzorec15(d), bez neprovedeného rozvinutí

Znovu e=e_1, S_(j−1)=e_1+…+e_(j−1), S_0=0. Kniha uvádí

    c(N)=N(½binom(e,2)+2e−1)−2^e(e−1)−1
       +Σ_(j=1)^r 2^e_j
          (S_(j−1)−j(e−1)+½binom(e−e_j,2)).             (*)

Dokážeme všechny koeficienty pomocí disjunktních binárních
intervalů. Začneme c(2^e) z P1004. Při přidání dalšího
nenulového bitu h=e_j,j≥2, se rozšíří suma c(N)=Σ_(n<N)a(n)
o interval n=P+v,0≤v<2^h,P=Σ_(l<j)2^e_l. Horní bity
jsou pevné, dolních h bitů probíhá všechny možnosti a každý
má hodnotu1 právě2^(h−1)krát. Pro h=0 žádné dolní bity
neexistují, takže jejich příspěvek je0.

Z P1006 je přesný přírůstek

    2^h [binom(e+1,2)+S_(j−1)−(j−1)(e−1)
          +h(h−1)/4−h(e−1)/2].                        (**)

Poslední dva členy jsou polovinou součtu vah k−e+1,
k=0,…,h−1. Přímé seskupení koeficientů e²,e,h²,h,eh dává

    binom(e+1,2)−(j−1)(e−1)+h(h−1)/4−h(e−1)/2
     =½binom(e,2)+2e−1−j(e−1)+½binom(e−h,2).

To je přesně změna pravé strany(*) po přidání bitu h:
člen N se zvětší o2^h a přibude j-tý člen sumy; staré
členy se nemění. Pro základ r=1 se(*) zjednoduší na
2^e(e(e−1)/4+1)−1=c(2^e). Indukce přes všechny bity
proto dokazuje(*) pro každé N≥1, včetně e=0, a všechny
členy odpovědi. Fixní r omezuje pouze počet provedených
operací vzorce, nikoli jeho matematickou platnost.

## P1011: celý aktuální dodatek2021, identita s§5.3.4(10)

V originálu224 je C(m,n) definováno počtem komparátorů:

    C(m,n)=mn při mn≤1;
    C(m,n)=C(⌈m/2⌉,⌈n/2⌉)+C(⌊m/2⌋,⌊n/2⌋)
             +⌊(m+n−1)/2⌋ jinak.

Používáme pouze tuto přesnou číselnou rekurenci, ne zatím
nezkontrolovanou správnost všech pozdějších sítí. Symetrie
C(m,n)=C(n,m) plyne indukcí z téže rekurence.

Nejprve F(n)=C(n,n)−C(n,n−1). Základ F(1)=1.
Pro n=2k rozdíl rekurencí je F(k); pro n=2k+1≥3 je
F(k+1). Tedy F(n)=1 pro každé n≥1.

Dále A(n)=C(n+1,n)−C(n,n), A(1)=C(2,1)−C(1,1)=1.
Pro n=2k je

    C(2k+1,2k)=C(k+1,k)+C(k,k)+2k,
    C(2k,2k)=2C(k,k)+2k−1,

takže A(2k)=A(k)+1. Pro n=2k+1≥3 je

    C(2k+2,2k+1)=C(k+1,k+1)+C(k+1,k)+2k+1,
    C(2k+1,2k+1)=C(k+1,k+1)+C(k,k)+2k,

a tedy A(2k+1)=A(k)+1. Indukce dává A(n)=1+⌊lg n⌋.

Pro g(N)=C(⌈N/2⌉,⌊N/2⌋) máme g(0)=g(1)=0 a

    g(2n+1)−g(2n)=A(n)=⌊lg(2n)⌋  (n≥1),
    g(2n+2)−g(2n+1)=F(n+1)=1      (n≥0).

To jsou přesně přírůstky x(N) pro μ(N) z P1005. Proto
g(N)=μ(N) pro všechna N. Rekurence(10) na226 pak má
stejný základ i stejné rozdělení c(⌈N/2⌉)+c(⌊N/2⌋)+μ(N)
jako zdejší c. Silná indukce dokazuje úplnou identitu funkcí,
nikoli pouze souhlas na mocninách2 nebo malé tabulce.

## Rozsah

Každá část14–15 i obě pomocné identity a dodatek2021 jsou
uzavřeny obecnými argumenty. Ostatní tvrzení stránek224/226,
extrémy výměn11, průměr16 a Quicksort zůstávají mimo tento
blok. Nový nález nevznikl.

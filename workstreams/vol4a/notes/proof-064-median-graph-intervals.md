# Theorem G, celá úloha 73 a všechny tři části obrázku 7

Checkpoint X0093, P0877–P0886. Originál p66/file83 je v
`proof-file083.png`, zadání 73 p89/file106 v `file106.png`,
odpověď p547/file564 v `proof-median-answer-1.png`.
Přesně se přebírají axiomy, distributivita, Lemma M, intervalové
zákony a jednoznačnost mediánu z proof-063, P0864–P0876.
Žádný program, prohledávání grafů ani opakování těchto důkazů.

## Definice všech hran — P0877

Pro různá u,v je hrana definována tím, že m(z,u,v)∈{u,v}
pro každé z∈M. Obraz těchto hodnot je z definice [u..v],
a podle P0872 obsahuje oba konce. Podmínka je tedy ekvivalentní
rovnosti [u..v]={u,v}. Nutnost u≠v zůstává výslovná, takže
nevznikají smyčky. Symetrie u/v dává neorientovaný jednoduchý graf.

## Souvislost konečné neprázdné algebry — P0878

Předpokládejme, že mezi nějakými u,v není cesta, a ze všech
takových dvojic vyberme dvojici s nejmenším počtem bodů [u..v].
Konečnost M zaručuje konečná srovnávaná čísla. Dvojice je různá,
a interval nemůže obsahovat jen její konce: podle P0877 by
to byla hrana. Existuje tedy x∈[u..v]\{u,v}.

Kdyby v∈[u..x], měli bychom v=m(u,v,x)=m(x,u,v)=x, spor.
Obdobně u∉[x..v]. Oba intervaly [u..x] a [x..v] jsou podle
(59) podmnožinami [u..v], druhý po záměně konců. Oba jsou
tedy **vlastní** podmnožiny a mají méně bodů. Minimalita
zvolené dvojice zaručuje cestu u→x i x→v. Jejich spojení
obsahuje cestu u→v, spor. To dokazuje propojení všech dvojic.

Proto má konečný neprázdný graf konečný průměr, v souladu
s definicí souvislosti na p16. Jednoprvkový graf má průměr 0.
Význam slova souvislý pro zcela prázdnou algebru je oddělen
v P0886; není potřebný pro žádný následující důkaz o vrcholech.

## Úloha 73(a): metrické kritérium — P0879

V konečném souvislém neohodnoceném grafu platí

    x leží na některé nejkratší cestě u→v
      ⇔ d(u,v)=d(u,x)+d(x,v).                         (S)

Pokud platí rovnost, spojme nejkratší cestu u→x a x→v.
Vzniklý sled má délku d(u,v); opakovaný vrchol by umožnil
vynechat kladně dlouhou uzavřenou část a získat kratší sled,
a pak kratší cestu u→v. Proto je to již nejkratší cesta přes x.

Obráceně nechť taková cesta má úseky délky l a r. Pak

    d(u,v)=l+r ≥ d(u,x)+d(x,v) ≥ d(u,v).

Obě nerovnosti musí být rovnosti. Zahrnuty jsou x=u, x=v
i u=v; v posledním případě rovnost vynucuje x=u.

## Úloha 73(b): přenos hrany — P0880

Máme x∈[u..v], u∈[x..y], x≠u a hranu y—v.
Pro libovolné z položme p(s)=m(s,u,x). Předpoklady dávají
p(v)=x a p(y)=u. Krátká distributivita proto dává

    p(z)=m(z,x,u)=m(z,p(v),p(y))=p(m(z,v,y)).

Jelikož y—v, vnitřní medián m(z,v,y) je buď y, nebo v.
Výsledek tedy leží v {p(y),p(v)}={u,x} pro každé z.
Podle definice hran a x≠u je x—u hrana. Jde přesně o
vytištěnou argumentaci pro všechna z, nikoli jen pro z=u,v.

## Úloha 73(c): celý indukční krok a obě jeho větve — P0881

Dokazujeme x∈[u..v] ⇒ (S) indukcí podle D=d(u,v).
Pro x=u nebo x=v je výsledek bezprostřední. D=0/1 žádný
jiný x v intervalu nedovoluje podle singletonového zákona
a definice hran. Dále je x vnitřní a D≥2.

Záměnou u,v můžeme předpokládat

    d(x,u) ≥ d(x,v) > 0.

První nerovnost je v originálu **neostrá**. Vyberme nejkratší
cestu u→…→y—v, takže d(u,y)=D−1, a definujme w=m(x,u,y).
Absorpce dává w∈[u..y] i w∈[u..x]. Pro p(s)=m(s,u,x)
tedy máme p(v)=x, p(w)=w. Distributivita dává

    m(v,x,w)=m(v,p(v),p(w))=p(m(v,v,w))=p(v)=x.

Tudíž x∈[w..v]. Indukční předpoklad na dvojici u,y dává
d(u,y)=d(u,w)+d(w,y). Z toho a z hrany y—v plyne řetězec

    D=d(u,w)+d(w,y)+1
      ≥ d(u,w)+d(w,v) ≥ d(u,v)=D.

Všude musí nastat rovnost. Zejména w leží na nejkratší cestě
u→v a d(w,v)=d(w,y)+1.

* **w≠u.** Pak d(u,w)>0 a d(w,v)<D. Indukce pro x∈[w..v]
  dává d(w,v)=d(w,x)+d(x,v). Dosazením a trojúhelníkovou
  nerovností získáme

      D=d(u,w)+d(w,x)+d(x,v)
        ≥ d(u,x)+d(x,v) ≥ D.

  Proto platí (S).
* **w=u.** Rovnost u=m(x,u,y) je u∈[x..y]. Část (b) proto
  dává hranu x—u, takže d(x,u)=1. Z 1≥d(x,v)>0 plyne
  d(x,v)=1 a také hrana x—v. Cesta u—x—v má délku 2.
  Protože x je vnitřním bodem algebraického intervalu, u—v
  není hrana; tedy D≥2. Z existence dvouhranové cesty plyne
  D≤2. Máme D=2 a opět (S).

To doplňuje i poslední implicitní krok odpovědi, aniž by se
rovnost dvou vzdáleností mylně považovala za vyloučený případ.

## Úloha 73(d): opačný směr — P0882

Předpokládejme (S) a položme t=m(u,x,v). Absorpce umístí t
do všech tří intervalů [u..x], [u..v], [x..v]. Z již dokázané
části (c) a (a) dostáváme

    d(u,x)=d(u,t)+d(t,x),
    d(u,v)=d(u,t)+d(t,v),
    d(x,v)=d(x,t)+d(t,v).

Dosazení do (S) dává 2d(x,t)=0, a tedy x=t. Podle Lemma M
je proto x∈[u..v]. S P0878 je tím celý Theorem G dokázán
pro konečné neprázdné algebry, včetně všech částí 73(a)–(d).

## Přesné převzetí jednoznačnosti trojitého průniku — P0883

P0865 ukazuje, že m(x,y,z) je v intervalu každé dvojice.
P0867 dokazuje, že každý bod jejich společného průniku
se tomuto mediánu rovná. Oba směry jsou doloženy v
`notes/proof-063-median-axioms-distributivity.md`; nepoužívá
se jen slovní souhrn úlohy 74. To přesně pokrývá celý
odstavec mezi Theorem G a obrázkem 7.

## Souřadnicová algebra, všechny její intervaly a hrany — P0884

M={0,1,2,3}³ má operaci po jednotlivých souřadnicích. Na řetězci
zachovává každý práh h_a(t)=[t≥a] medián: alespoň dvě hodnoty
jsou ≥a právě tehdy, když je ≥a prostřední hodnota. To je přesný
prahový argument již doložený v P0831. Použitím na obě strany
(52), které pro bity platí podle P0864, dostaneme (52) na
řetězci; různé výsledky by oddělil práh roven většímu výsledku.
Majorita a permutace platí přímo z pořadí hodnot. Axiomy pak
platí souřadnicově i v M.

Medián m(s,a,b) svírá každou souřadnici s mezi příslušnými
souřadnicemi a,b. Naopak každý bod takto vymezeného kvádru
je pevným bodem tohoto mediánu. Proto pro libovolné a,b∈M

    [a..b] = PRODUCT_i {min(a_i,b_i),…,max(a_i,b_i)}.

Počet bodů je součin (|a_i−b_i|+1). Pro a≠b je roven 2
právě tehdy, když se jediná souřadnice liší o 1 a ostatní
jsou stejné. To dokazuje přesně popsané hrany obrázku, bez
předpokladu, že každá vizuálně blízká dvojice musí být spojena.
Graf má 64 bodů a ve třech osových rodinách po 3·4·4=48
hranách; všechny tři panely zobrazují stejnou tuto mřížku.

## Všechna zvýraznění obrázku 7 — P0885

Konce v popisku jsou x=(0,2,1), y=(3,3,3), z=(2,0,0).
Intervalový vzorec dává následující přesné tři množiny:

| panel | vyznačený interval | počet bodů |
|---|---|---:|
| (a), x–y | {0,1,2,3} × {2,3} × {1,2,3} | 24 |
| (b), x–z | {0,1,2} × {0,1,2} × {0,1} | 18 |
| (c), y–z | {2,3} × {0,1,2,3} × {0,1,2,3} | 32 |

Původní diagramy zkontrolovány po hladinách třetí souřadnice.
V každé hladině čteme řádky druhé souřadnice 3,2,1,0 a sloupce
první souřadnice 0,1,2,3; 1 znamená plný černý či šedý bod,
0 prázdný kruh. Šedá je způsob kresby zadních částí mřížky,
nikoli odlišná matematická množina.

    (a) k=0:       0000 0000 0000 0000
        k=1,2,3:   1111 1111 0000 0000

    (b) k=0,1:     0000 1110 1110 1110
        k=2,3:     0000 0000 0000 0000

    (c) k=0,1,2,3: 0011 0011 0011 0011

Čtvercově označené konce v každém panelu leží v jeho množině;
souřadnicové popisky krajních bodů souhlasí se třemi směry
mřížky. Jednotlivé rodiny hran spojují sousední hladiny nebo
sousední řádky/sloupce, jak vyžaduje P0884.

Průnik všech tří vyznačených kvádrů je po souřadnicích

    ({0,…,3}∩{0,1,2}∩{2,3})
      × ({2,3}∩{0,1,2}∩{0,…,3})
      × ({1,2,3}∩{0,1}∩{0,…,3}) = {(2,2,1)}.

To je i souřadnicový medián daných x,y,z a zvýrazněný společný
bod všech panelů. Je ověřena jeho **jednoznačnost**, nikoli
jen to, že do průniku patří jeden zvolený svědek.

## Pouze prázdná algebra a slovo souvislý — P0886, partial

Pro všechny neprázdné konečné M je Theorem G úplně doložen.
Jestliže by definice „any set M“ zahrnovala i M=∅, axiomům
vyhoví prázdná operace, ale definice souvislosti p16 odkazuje
na maximum prázdné množiny vzdáleností. Její konvence zde
není určena. Tento drobný doménový bod se ponechává partial,
bez chybové karty; žádný výsledek o existujících vrcholech
ani obrázku není zpochybněn.

## Mapa p66, errata a bibliografie

| obsah | argument |
|---|---|
| (61), ekvivalentní dvoubodový interval | P0877 |
| souvislost a minimalita intervalu v důkazu | P0878 |
| oba směry metrické charakterizace, odkaz na 73 | P0879–P0882 |
| trojitý průnik a přesný odkaz na 74 | P0883 |
| souřadnicová median algebra, intervaly a hrany | P0884 |
| všechny tři diagramy, popisek a jediný společný bod | P0885 |
| doslovná prázdná doména slova souvislý | P0886 partial |

Z tohoto důvodu zůstává p66 celé v UI partial, přestože jeho
matematika na neprázdných algebrách a celý obrázek jsou doloženy.
Změna čtecího kurzoru se tím netvrdí.

Dne 2026-11-07 prohledány všech pět relevantních vrstev
`all4a-pre`, `all4a`, `err4a`, `all4f0`, `all4f1` podle stran
66/547, čísla 73 a tématu Avann/median. Oprava all4a-pre
p547 line5 patří 67(b), nikoli 73; relevantní oprava zde není.
Primární [Avannův odkaz AMS](https://www.ams.org/journals/proc/1961-012-03/S0002-9939-1961-0125807-5/)
nebyl dostupný. Přesná historická bibliografie Proc. Amer.
Math. Soc.12 (1961),407–414 se proto nezávisle neuzavírá;
žádná věta z nedostupného článku není vstupem do důkazu.

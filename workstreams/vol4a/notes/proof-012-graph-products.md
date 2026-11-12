# Grafové součty a součiny: str. 27–28, §7–89 až 102

6. listopadu 2026. Samostatné argumenty, žádný matematický program.
Sazba file044–045, file059–060, proof-file543/544 a detail answer91.
Výpočty a podmínky níže jsou pro obyčejné bezsmyčkové grafy, pokud není
výslovně uvedená algebraická/multigrafová extenze.

## Text a úloha 89

Blokové matice (40)–(41) přímo rozdělují dvojice podle příslušnosti
do obou vrcholových částí: diagonální bloky A,B; mezibloky buď 0,
nebo J v příslušném směru. To současně ověřuje oba directed joins.

Asociativita (42)–(43), úloha 89: po zploštění do tří bloků mají obě
strany stejné diagonální A,B,C; všechny mimodiagonální bloky jsou
u součtu nulové, u joinu J, u → horní J/dolní 0, u ← obráceně.
Ve (44)–(45) komplementace převrátí každý takový blok a komplementuje
diagonální grafy, takže součet přejde v join a directed join obrátí směr.
Ve (46) mají obě strany diagonály 2A,2B a oba mimodiagonální bloky J.

(47): join prázdných částí vytváří právě kompletní multipartitní graf.
(48): join n jednovrcholových grafů dává K_n; directed join v daném
pořadí dává tranzitivní turnaj. Řád součtu je m+n, řád součinu mn.

Cartesian product má po jedné kopii H na každý u a přidává
odpovídající u–u′ hrany pro každý v; to je přesná bijekce s definicí.
Diagram (49) byl přečten, ale všechny jeho nakreslené hrany nebyly
jednotlivě označeny, takže jeho úplná obrazová certifikace je partial.
V (50) definice dává 12 vrcholů a 17/20/24 hran pro grid/cylinder/torus;
wrap spojuje příslušné konce cest. Hyperkrychle má 2^k binárních
k-tic a sousednost právě při Hammingově vzdálenosti 1.

Pět součinů je asociativních po přirozeném zploštění n-tic:
Cartesian mění právě jednu souřadnici po hraně a ostatní nechá stejné;
direct mění všechny po hraně; strong má v každé souřadnici rovnost
nebo hranu a alespoň jednu hranu; odd má lichý počet souřadnic s hranou.
První tři pravidla se skládají přímo, čtvrté je asociativita XOR.
To dokazuje všechny čtyři tištěné podmínky na a,b.
Lexicographic product se rozhoduje podle první různé souřadnice;
proto je také asociativní. Není komutativní:
K2∘bar(K2)=C4, kdežto bar(K2)∘K2 jsou dvě nezávislé hrany.
Historie součinů, kniha Imrich–Klavžar a atribuce Zykov/Nesetřil
nebyly nezávisle bibliograficky ověřeny.

## Úloha 90

Na čtyřech vrcholech jsou podle počtu hran 0,...,6 počty typů
1,1,2,3,2,1,1. Pro dvě hrany jsou 2K2 a P3⊕K1; pro tři hrany
jsou K3⊕K1, K1,3 a P4; ostatní získáme komplementem.
Tím je počet 11 doložen bez censu.
Deset kografů tvoří pět komplementárních dvojic:
K4; K1,1,2; K2,2; K1,3; K1⊕K1,2, vždy spolu s komplementem.
Každý úplný multipartitní graf je komplement sumy úplných grafů;
úplné grafy jsou komplementy sum K1. Všechny tyto zápisy tedy splňují
definici kografu. P4 není kograf podle správného indukovaného argumentu
v poznámce F0002; nepravdivou obecnou větu z téže poznámky neopakujeme.

V opraveném značení je W4=K1 join C4 kograf, protože C4 je kograf.
W5 má indukovaný C5 a v něm indukovaný P4, proto není kograf.
Známá errata odkazu (47)→(39) a označení kol jsou aplikována;
samotné chybějící „induced“ je samostatný F0002.

## Úlohy 91–94

91: Na čtyřech vrcholech (00,01,10,11) jsou výsledky:
(a) C4; (b) dvě nezávislé diagonální hrany; (c) K4; (d) C4;
(e) K4; (f) dvě nezávislé hrany; (g) K2,2.
Při různých prvních souřadnicích má K2△H hranu právě při nehraně
druhých souřadnic, včetně jejich rovnosti. Při stejných prvních
souřadnicích má hranu právě v H. Proto
K2△H=(K2□H)∪(K2⊗bar(H)).
První člen dodá oba H a matching, druhý právě zbývající cross nehrany.
Dále K2∘H=H join H. Odd/Cartesian a lexicographic/strong se shodují
právě tehdy, když H je úplný: jinak chybějící pár přidává v prvním
grafu skutečné další hrany. Pruhy v sazbě byly čteny v samostatném detailu.

92: Pro orientované K2 s 0→1 dává pořadí 00,01,10,11 tyto oblouky:
(a) 00→01,00→10,01→11,10→11;
(b) jen 00→11;
(c) oblouky (a) a 00→11;
(d) oblouky (a) a 01↔10;
(e) tranzitivní turnaj v uvedeném pořadí, všech šest oblouků.
To odpovídá pěti obrázkům a plyne přímo z příslušných pravidel.

93: Strong a lexicographic součin K_m,K_n jsou K_(mn):
každá různá dvojice souřadnic se buď liší v první souřadnici, nebo
při stejné první ve druhé. U ostatních součinů příslušné páry obecně chybějí.

94: Hammingovy hrany pětimístných slov odpovídají K26□...□K26.
Nemohou obecně být indukovaným podgrafem součinu cest: ten je
bipartitní (barva je parita součtu souřadnic), ale SGB obsahuje
trojúhelník tears,bears,pears. Členství ověřeno cíleným vyhledáním
v audit-2026-10-31/sources/sgb-words.txt, řádky 430,510,1406.

## Úlohy 95–97 a maticové identity

95: Označ d_u,d_v stupně. Cartesian má disjunktní třídy velikostí
d_u a d_v; direct d_u d_v; strong sjednocuje tyto tři disjunktní třídy.
Odd má d_u(n−d_v)+(m−d_u)d_v, podle toho, která právě jedna
souřadnice je sousední. Lexicographic má d_u n+d_v:
v sousedních prvních vrcholech je libovolná druhá souřadnice,
ve stejné první souřadnici soused v H.

96: Jednotlivé prvky Kroneckerových matic jsou právě indikátory
těchto možností:
Cartesian A⊗I+I⊗B;
strong A⊗I+I⊗B+A⊗B;
odd A⊗J+J⊗B−2A⊗B;
lexicographic A⊗J+I⊗B.
Odd vzorec je a+b−2ab pro a,b∈{0,1}. Pro násobnosti může být záporný,
například a=b=2 dává −4; nelze tak definovat obecný multigraf.
Ostatní součtové vzorce mají nezáporné celočíselné prvky a definují
zmíněné algebraické extenze, i když při smyčkách mohou vznikat násobnosti.

Historické maticové vzorce jsou doloženy nezávisle na atribucích.
Transpose zamění (u,v) a (u′,v′), proto (A⊗B)^T=A^T⊗B^T.
Násobení po indexech dává
Σ_(i,j) a_ui b_vj a′_iu′ b′_jv′=(AA′)_uu′(BB′)_vv′;
tedy součin tensorů je tensor součinů. Inverzní formule plyne
dosazením A′=A^−1,B′=B^−1.
Pro čtvercové matice
A⊗B=(A⊗I_n)(I_m⊗B).
Druhý člen je blokově diagonální, determinant (det B)^m.
První je permutačně podobný I_n⊗A, determinant (det A)^n.
Tím je dokázána i Zehfussova determinantová formule bez spektrálního vstupu.
Historické atribuce Hensel/Kronecker/Zehfuss/Hurwitz zůstávají přeskočené.

97: Součet G⊕G′ rozděluje první souřadnici do dvou částí bez hran.
Žádný Cartesian, direct, strong ani lexicographic součin s H je
nespojí, a uvnitř každé části zůstane odpovídající produkt.
To dokazuje všechny tištěné levé distributivní vztahy.
Cartesian/direct/strong jsou komutativní záměnou souřadnic,
proto mají i uvedené pravé distributivní vztahy.
Komplement lexicographic součinu je bar(G)∘bar(H), protože se
rozhoduje podle první různé souřadnice. K_m∘H je join m kopií H;
K_m∘bar(K_n) je proto úplný m-partitní graf s částmi velikosti n.
G∘K_n=G strong K_n, protože sousednost libovolných různých druhých
souřadnic je automatická.
Správná poslední identita je
bar(K_m⊗K_n)=K_m□K_n=L(K_m,n):
doplněk „obě souřadnice různé“ je „právě jedna shodná“.
Známá oprava polohy komplementace na str. 526 z 20. 5. 2011 je zohledněna.

## Úlohy 98–101

98: Žádná hrana nemění komponentu žádné souřadnice. Produkt dvou
souvislých komponent je Cartesian-souvislý postupným průchodem
první a druhé souřadnice; strong obsahuje tyto hrany také.
Je tedy právě kl komponent.

99: Cartesian cesta potřebuje alespoň d_G kroků v první a d_H
ve druhé souřadnici, disjunktně; zřetězené nejkratší cesty dosáhnou
součtu. Strong krok změní každou souřadnici nejvýše jednou, takže
dolní mez je maximum; současně postupuj po obou nejkratších cestách,
a po skončení kratší se v její souřadnici zastav. Dosáhneš maxima.
Nekonečné vzdálenosti souhlasí s rozkladem komponent.

100: Pro dva netriviální souvislé bipartitní grafy se při každém
direct kroku změní obě barvy, takže XOR barev je invariant.
Obě jeho hodnoty existují a produkt není souvislý.
Má-li naproti tomu G lichý cyklus, vezmi cestu z v do v′ v H
a stejně dlouhý libovolný sled v G z u do nějakého u″ (lze střídat hranu).
Mezi u″ a u′ existuje sudý sled: paritu jakékoli cesty lze obrátit
detourem k lichému cyklu, jeho obejitím a návratem. Tento sudý sled
spáruj v H se střídáním hrany z v′ k sousedovi a zpět. Tím dojdeš
do (u′,v′). Výjimka s K1: produkt nemá hrany, souvislý je právě
při druhém faktoru K1. Odpověď správně výslovně předpokládá oba řády≥2.

101: Rovnost maximálních stupňů v izomorfních Cartesian/direct
součinech dává d_G+d_H=d_G d_H, tedy (d_G−1)(d_H−1)=1.
Nezáporné celočíselné možnosti jsou oba 0 (oba K1), nebo oba 2.
Souvislé grafy s maximem 2 jsou cesty/cykly. Souvislost direct součinu
vyžaduje alespoň jeden lichý cyklus, řekněme G=C_m. Cartesian součin
jej obsahuje, tedy není bipartitní; direct součin by byl bipartitní,
kdyby H byl bipartitní. Proto také H=C_n s lichým n.

Po známé opravě „shortest cycle“→„shortest odd cycle“ je argument správný.
Odd girth Cartesian součinu je min(m,n): souřadnicové projekce lichého
cyklu mají alespoň jednu lichou délku, a faktorové cykly jsou vloženy.
V direct součinu je každá projekce lichým uzavřeným sledem stejné délky,
takže délka je nejméně max(m,n). Této meze dosáhneš oběhem delšího
cyklu a stejně dlouhým sledem v kratším (přidej sudý počet návratů);
delší souřadnice zaručí, že součinový cyklus neopakuje vrchol.
Izomorfismus proto vynutí m=n.
Pro liché n≥3 je (u,v)→(u+v,u−v) mod n bijekce a mění Cartesian
posuny na všechny čtyři diagonální direct posuny. Důkaz je úplný.

## Úloha 102: král a přesná planární hranice

P_m strong P_n dovoluje právě horizontální, vertikální a diagonální
jednotkové kroky. Pro min(m,n)=1 je to cesta. Pro min(m,n)=2 je
graf řetězec K4 na sousedních dvojicích sloupců; každý další K4 lze
vložit do prázdné stěny u společné hrany, takže graf je rovinný.

Pro 3×3 odstraň střed. Zbývá obvodový C8 a čtyři neprotínající se
tětivy tvořící čtyřúhelník ze středů stran. Jde o explicitní outerplanar
vložení; přidání středu do vnější stěny a spojení s osmi obvodovými
vrcholy ji rozdělí na osm trojúhelníků. Tím je dáno rovinné vložení.

Každá deska s rozměry alespoň 3×4 obsahuje následující K5 minor.
Řádky pojmenuj A,B,C, sloupce 1,2,3,4. Pět disjunktních souvislých
branch sets je
{B2}, {B3}, {A1,B1,C1,A2}, {A3,A4,B4}, {C2,C3,C4}.
První dva jsou sousední. Oba mají hranu do každé z dalších tří množin;
u B3 do třetí použij diagonálu B3–A2. Poslední tři jsou navzájem
spojeny hranami A2–A3, C1–C2 a B4–C4.
Kontrakcemi tedy vznikne K5, jehož neplanarita je již dokázána
v proof-007; kontrakce rovinnost zachová. Symetricky platí pro 4×3.
Přesně zbývají min(m,n)≤2 a m=n=3, jak uvádí kniha.

Další kurzor: str. 29 / file46, algoritmus H a úlohy 103–111.
Celá odpověď 526 nyní přečtena; 527 zatím cíleně 101–102 a navigačně
další text, nikoli dokončená argumentová kontrola 103–105.

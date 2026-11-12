# Barvení a kliky, §7–124 až 132

6. listopadu 2026. Zadání file061, odpovědi proof-file546–548;
detail Chvátalova grafu přímo renderovaný z file031 je proof-chvatal.png.
Bez matematického programu nebo výčtu. F0004 samostatně vyčleněn.

## 124: úplný krátký důkaz pro Chvátalův graf

Označ rohy A,B,C,D po směru hodin od levého horního. Dvojice vnitřních
vrcholů u těchto rohů jsou (p,w), (q,r), (s,t), (u,v): p,q nahoře;
r,s vpravo; t,u dole; v,w vlevo, vždy po směru hodin.
Z původního diagramu: vnější C₄, osm hran roh–jeho dvojice,
matching pq,rs,tu,vw a dvě K₂,₂ mezi dvojicemi A–C a B–D.
Tím je popsáno všech 24 hran a každý z 12 vrcholů má stupeň 4.

Nezávislá množina má nejvýše dva rohy. Bez rohů vezme nejvýše dvě
vnitřní místa z dvojic A/C a dvě z B/D, tedy nejvýše 4.
Se dvěma rohy, řekněme A,C, zbývá uvnitř K₂,₂ u B/D a opět nejvýše4.
S jediným rohem A jsou jeho dvě vnitřní místa zakázána; pro pět bodů
bychom museli vzít celou dvojici C a celou dvojici B nebo D.
To zakazuje hrana rs nebo tu. Rotace řeší ostatní rohy. α≤4,
a {A,C,q,r} je nezávislá čtveřice.

Ve tříbarvení má vnější C₄ dva protilehlé rohy stejné barvy;
rotací a přejmenováním dej A=C=1. Jejich vnitřní dvojice používají
jen 2,3 a jsou mezi sebou úplně propojené, proto p=w=2, s=t=3
nebo symetricky opačně. Rohy B,D mají každý barvu 2 nebo3.
Je-li B=2, pak r=1; je-li B=3, pak q=1. Je-li D=2, pak u=1;
je-li D=3, pak v=1. Úplné propojení {q,r} s {u,v} dává spor vždy.
Čtyři barvy stačí: {A,C,q,r}, {B,D}, {p,w,u}, {s,t,v}.
To současně doplňuje vynechané kroky tištěné odpovědi, nikoli jen její závěr.

## 125: konstrukce a výslovné externí meze

U Brinkmannova grafu s indexy modulo7 mají a_j sousedy
a_(j±2),b_j,b_(j+1); b_j sousedy a_j,a_(j−1),c_j,c_(j+2);
c_j sousedy c_(j±3),b_j,b_(j−2). Všechny jsou různé, tedy 21 vrcholů,
stupeň4 a42 hran. Barva b_j=4 a libovolné tříbarvení dvou sedmicyklů
na a a c dokazují χ≤4. Konkrétně po pořadích a₀,a₂,a₄,a₆,a₁,a₃,a₅
a c₀,c₃,c₆,c₂,c₅,c₁,c₄ použij barvy 1,2,1,2,1,2,3.

Trojúhelníky nejsou: sousedé b v části a mají rozdíl1 (nikoli2),
v části c rozdíl2 (nikoli3), mezi a a c nejsou hrany.
Čtyřcyklus s jedním b by měl třívrcholovou cestu v a nebo c;
její konce se liší ±4 respektive ±6, což není rozdíl společných
sousedů b (±1 respektive ±2). Se dvěma b je cyklus alternující;
dvě a nebo dvě c sdílejí nejvýše jedno b, a kombinace a,c by vyžadovala
současně rozdíl b rovný ±1 i ±2 modulo7. Bez b jsou pouze sedmicykly.
Cyklus a₀,a₂,a₄,a₆,b₀,a₀ délky5 existuje, tedy girth=5.

Nemožnost tříbarvení tohoto 21vrcholového grafu, jeho minimalita,
minimum Chvátalova grafu a mez35 pro girth>5 nejsou zde nezávisle dokázány.
Poslední historická otevřená otázka se neřeší násilným hledáním.
[Autorský seznam publikací](https://users.encs.concordia.ca/~chvatal/publ.html)
potvrzuje Chvátalův název, rok1970 a strany93–94; nejde o náhradu důkazu
minimality. Brinkmann/Meringer/Grünbaum bibliografie a aktuální stav
výzkumu mají explicitní výjimku; současná neznalost konstrukcí se netvrdí.

## 126: celé opravené barvení toru

Zadání má m,n≥3. Každá ploška 2×2 je K₄. Při čtyřbarvení vezmi
dva sousední řádky: dvojice barev v sousedních sloupcích jsou navzájem
doplňky ve čtyřprvkové paletě, takže se střídají a počet sloupců je sudý.
Stejný argument pro řádky nutí sudé m. Obráceně při obou sudých
rozměrech stačí dvojice parit souřadnic. Tím je χ=4 právě v tomto případě.

Pro m,n≥4 dá modulo5 konstrukce c(j,k)=a_j+2b_k správné barvení:
sousední rozdíly v a,b jsou ±1 a výsledný nenulový rozdíl na silné
hraně je ±1,±2 nebo ±3. Potřebný uzavřený sled délky l v C₅ existuje
pro sudé l střídáním a pro liché l≥5 jedním pětikrokovým oběhem
s vloženými dvoukrokovými návraty. Není-li obojí sudé, χ je tedy přesně5.

Pro m=3 (symetrií také n=3) je každý sloupec K₃ a dva sousední sloupce
tvoří K₆. Nezávislá množina obsahuje nejvýše jeden bod v každém sloupci
a sloupce musejí být nezávislé v C_n, tedy α=floor(n/2).
Pro n=3 je celý produkt K₉. Pro sudé n≥4 šest barev střídá palety
{0,1,2} a {3,4,5}; dolní mez K₆ je těsná.
Pro n=5 je dolní mez ceil(15/2)=8. Barvy ve sloupcích lze zvolit
{0,1,2}, {3,4,5}, {6,7,0}, {1,2,3}, {4,5,6}; sousední palety jsou
disjunktní včetně uzávěru, a proto osm stačí.

Pro liché n≥7 je nutných aspoň7 barev, protože 6 floor(n/2)<3n.
Sedm stačí: na sedmi po sobě jdoucích sloupcích cyklu použij trojice
S_j={3j,3j+1,3j+2} modulo7, j=0,...,6.
Sousední trojice včetně S₆,S₀ jsou disjunktní. Libovolnou lichou délku
n≥7 získáme vložením dvoukrokových návratů mezi dvěma sousedními S_j;
tím vznikne uzavřený sled trojic délky n a potřebné barvení.
Tištěná větev pro zbývající m=3,n≥6 je tedy chybná, F0004.
Protipříklad (3,6) má přímý K₆ a šestibarvení, žádný census.

Primární Vesztergombi1979 je dohledána v poznámce F0004; její omezení
lichých cyklů na délku>3 souhlasí s výše dokázanou opravou.
Známé bibliografické erratum roku nijak nemění tento matematický nález.

## 127: obě Nordhausovy–Gaddumovy meze

Indukce pro χ(G)+χ(bar G)≤n+1: po odebrání v platí součet≤n.
Spor může nastat jen při rovnosti n a nárůstu obou čísel o1.
Nárůst v G znamená, že žádné optimální barvení G−v nenechá v sousedství
v některou barvu nepoužitou; tudíž χ(G−v)≤d(v).
Stejně χ(bar G−v)≤n−1−d(v). Jejich součet by byl≤n−1, spor.
Pro G=K_a disjoint-union bar K_b, a,b>0, a+b=n, jsou čísla a a b+1;
n=1 je přímý základ. To poskytuje požadované příklady rovnosti.

Každé k-barvení G má třídu velikosti≥ceil(n/k), což je klika v bar G.
Proto χ(G)χ(bar G)≥k ceil(n/k)≥n. Rovnost dává G=K_n.
AM–GM pak dává součet≥2√n a součin≤(n+1)²/4.
Finckova úplná klasifikace grafů rovnosti je explicitní externí poznámka,
nikoli zde reprodukovaný výsledek; pro zadané důkazy není potřeba.

## 128 a 132: součinová barvení

128: oba faktory se v neprázdném Cartesian součinu vyskytují jako
indukované kopie, tedy dolní mez max(χG,χH). Pro k rovné této mezi
obarvi (u,v) součtem a(u)+b(v) modulo k. Na hraně se mění právě jedna
souřadnice, její nenulový rozdíl modulo k zůstane nenulový. Horní mez sedí.

132: dvě maximální kliky dávají v silném součinu kliku velikosti ωG·ωH.
Dvojice barev faktorů obarví součin nejvýše χG·χH barvami, protože
na každé hraně se mění aspoň jedna sousední souřadnice.
Při χG=ωG a χH=ωH jsou obě meze totožné.

## 129: co je uzavřeno a co zůstává

Řádky/sloupce dávají16 klik; diagonály délek4,…,7 po4 a délky8 dvě,
celkem18. Oba vystředěné pětičlenné vzory mají pro a=1,2,3
(8−2a)²=36,16,4 poloh. U kříže s jedním ramenem mimo desku je pro
jednu orientaci a(8−2a) poloh, tedy 24,32,24 pro všechny čtyři orientace.
Čtverce liché strany1,3,5,7 mají (8−a)²=49,25,9,1 poloh.
Každá vypsaná dvojice polí se napadá řádkem, sloupcem nebo diagonálou.
Součty dávají310 a rozdělení podle velikostí4,…,8 je168,116,4,4,18.
Zde však není dotažena úplná geometrická klasifikace všech maximálních
klik ani maximalita každého hraničního vzoru; celek zůstává partial.
Číselná shoda součtu není vydávána za důkaz úplnosti.

## 130 a 131: maximum počtu maximálních klik

V joinu G,H je maximální klika právě sjednocení maximální kliky G
a maximální kliky H: jakákoli nevyužitá možnost rozšíření v jednom
faktoru rozšíří celý join. Počty se proto násobí. Edgeless graf na n_i
vrcholech má n_i singletonových maximálních klik, takže pro kompletní
multipartitní graf je počet součin n_i.

Tištěný klonovací krok 131 je správný: pro nesousední u,v s m(u)≤m(v)
nahraď N(u) množinou N(v). Kliky obsahující u nově kopírují ty s v;
kliky s v se nezmění. Stará maximální klika bez obou zůstává maximální:
kdyby ji mohlo prodloužit nové u, mohlo ji už dříve prodloužit v.
Počet maximálních klik tudíž neklesne.

Pro úplnost zdůvodníme „appropriately repeating“ bez kruhu. Rozděl
vrcholy na třídy stejných otevřených sousedství (false twins); každá
třída je nezávislá. Pokud dvě nesousední třídy U,V mají různá sousedství,
porovnej počty maximálních klik na jeden jejich vrchol a klonuj menší
třídu do větší v tomto smyslu. Lze to provést po jednom vrcholu:
počty na zbývajících U a na V se během operace nemění, protože žádná
klika obsahující takový vrchol nemůže obsahovat jiný vrchol U∪V.
Žádná původní třída se nerozštěpí: nové sousedství je konstantní na
každé původní třídě. U,V se spojí, takže počet tříd přísně klesne.
Po konečně mnoha krocích jsou různé třídy všechny sousední a vznikne
kompletní multipartitní graf s alespoň původním počtem maximálních klik.

Maximum součinu kladných částí se součtem n>1 nemá část1:
připojením k jiné části se součin zvětší. Část a≥5 nahraď3 a a−3,
protože 3(a−3)>a; čtyřku lze nahradit dvěma dvojkami bez změny.
Tři dvojky je výhodnější nahradit dvěma trojkami (8<9).
Zůstanou tedy trojky a nejvýše dvě dvojky. To je současně dosažitelný
maximální počet: pro n≡0 je3^(n/3), pro n≡1 je4·3^((n−4)/3),
pro n≡2 je2·3^((n−2)/3), s přímým N(1)=1.
Požadované 3^floor(n/3)≤N(n)≤3^ceil(n/3) plyne okamžitě.
Známá oprava odkazu68(a)→68(b) zohledněna; odkaz není důkazovým vstupem.

Bibliografie Nordhaus–Gaddum, Finck a Moon–Moser nebyla samostatně
ověřována; uvedené obecné důkazy jsou zde rozepsány bez těchto vstupů.
Další důkazový kurzor §7–133 na file061/p44; čtecí kurzor hlavního
textu zůstává235/218. Odpovědi530–531 jsou celé přečteny,133–136 čekají.

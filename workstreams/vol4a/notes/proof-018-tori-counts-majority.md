# Zobecněné tory, počty podgrafů a majority, §7–137 až 145

6. listopadu 2026. Zadání file062–063; původní odpovědi
proof-pages549-551-1/2/3.png. Na poslední stránce kontrolována jen145.
Bez programu a bez enumerace grafů. Relevantní známá errata F0/4A
u137/138/140/142/145 uplatněna, nejsou nálezy.

## 137–138: integer row/column operace a označení toru

Nechť L je mřížka celočíselných kombinací řádků nesingulární A.
Řádková unimodulární operace mění jen bázi L. Sloupcová transformace V
mění souřadnice každého řádkového bodu x na xV; je bijektivní na Z^k.
To vysvětluje přesně obě elementární operace odpovědi137 i jejich inverze.

Doplnění existence diagonální redukce: vyber nenulový pivot a pomocí
Eukleidova dělení řádky/sloupci zmenšuj jeho absolutní hodnotu, pokud
některá položka v jeho řádku/sloupci není dělitelná. Poté zbytek tohoto
řádku/sloupce vynuluj. Pokud pivot nedělí některý prvek zbývajícího
bloku, přičti příslušný řádek k pivotovému; vznikne nedělitelný prvek
v pivotovém řádku a další dělení pivot přísně zmenší. Tento proces
musí skončit pivotem d₁ dělícím všechny zbývající prvky. Opakuj v bloku;
jeho prvky jsou násobky d₁, proto d₁|d₂ a induktivně d_i|d_(i+1).
Záměny lze kombinovat se změnou znaménka, takže pro det A>0
v úloze137 lze mít det U=det V=1 a kladnou diagonálu.

Gcd všech položek zůstává invariantní, takže v137 d₁=1 a diag(1,n),
n=det A. Pro V=(α β;γ δ) je původní label βx+δy modulo n.
Tato mapa je na Z/n surjektivní (druhý sloupec unimodulární V je
primitivní) a její jádro je právě L. Oba jednotkové kroky se zobrazí
na pevné přírůstky β,δ a jejich zápory, jak bylo požadováno.
Torus má n vrcholů, protože diagonální mřížka má přesně n zbytkových tříd.

U obecné k×k matice zachovávají unimodulární operace ideál generovaný
j×j minory: Cauchy–Binet vyjádří nové minory celočíselně ze starých
a inverzní operace dá opačné zahrnutí. Na diagonále s řetězem d_i|d_(i+1)
je gcd těchto minorů d₁…d_j; tento součin sám je jedním minorem
a dělí všechny ostatní. Tím jsou doloženy vytištěné invarianty SNF.
Body se označí souřadnicemi xV modulo d_i; triviální moduly1 odpadnou.
Počet je |det A|=Πd_i (při knižní kladné orientaci det A), a r souřadnic
modulo d_i>1 popisuje součin cyklických grup. Jde o souřadnice/labeling,
nikoli automaticky o obyčejnou toroidální sousednost; kroky jsou řádky V.
Pro det1 je jediný label. Předpoklad konečného toru znamená plnou hodnost.

Příklady137: pro (4,0),(0,3) je label3x+4y modulo12; obě periody
se nulují a gcd(3,4,12)=1. Tabulka nahoře má přesně tyto hodnoty.
Pro (5,2),(1,3) je determinant13 a label x+4y modulo13;
5+4·2=13 a1+4·3=13. Zobrazený dílek má právě13 různých labelů.
Každá volba jednoho reprezentanta z každé zbytkové třídy pokryje
mřížku unikátně svými posuny v L. Známé underlying graph→numbering scheme
je potřebné pro přesnost výroku o alternativním tvaru dílku.

## 138: konkrétní matice a opravené sousednosti

Vytištěné U má řádky(1,−2,0),(0,1,−1),(−1,−1,4), det U=1;
V má řádky(1,5,6),(0,1,1),(0,0,1), det V=1.
Pro A s diagonálou3 a ostatními prvky1 jsou řádky UA
(1,−5,−1),(0,2,−2),(0,0,10); násobení V dává diag(1,2,10).
Tedy přesně20 labelů (u,v)=((5x+y) mod2,(6x+y+z) mod10).
Kroky ±x dávají(1,±6), ±y dávají(1,±1), ±z dávají(0,±1),
modulo(2,10). Všech šest je různých: jde o jednoduchý6-regulární graf.
Původní ztracený přírůstek6 a následující multigrafový závěr opravilo
erratum27.10.2015; nejde o novou chybu.

Novou poznámku o dvacetibodovém dílku uvnitř3×3×3 lze doložit přímo.
Pro x,y,z∈{0,1,2} mají body s u=0 dosažitelné intervaly v:
0…2 z(x,y)=(0,0), 2…4 z(0,2), 7…9 z(1,1),
2…4 z(2,0), 4…6 z(2,2). Sjednocení je všech deset zbytků.
Pro u=1 jsou intervaly1…3 z(0,1), 6…8 z(1,0), 8,9,0 z(1,2),
3…5 z(2,1), opět všech deset. Vyber jeden bod pro každý label;
jeho mřížkové posuny dávají požadované tiling bez překryvů.
Zobecněné tory jsou Cayleyovy grafy konečných abelovských grup:
jednotkové kroky generují kvocient Z^k/L. Obráceně z generátorů konečné
abelovské grupy vznikne surjekce ze Z^k a mřížka relací plné hodnosti.
Historické síťové aplikace a primární Smithův článek zde nedohledány.

## 139: očekávané počty indukovaných podgrafů

Na každé pevné h-podmnožině vrcholů je všech2^C(h,2) grafů stejně
pravděpodobných. Z nich h!/|Aut H| odpovídá typu H podle orbit–stabilizer
(už samostatně doloženého v proof009). Linearita očekávání dává
C(n,h)·h!/|Aut H|·2^(−C(h,2)).
Pro K_h je počet označení1; pro P_h,h>1 je h!/2 (jediná netriviální
symetrie obrací cestu); pro C_h,h>2 je(h−1)!/2 (h otočení a dvě orientace).
Jsou to přesně všechny čtyři odpovědi, bez nezávislosti různých h-množin.

## 140: proportional grafy a wheel

Piš T,P,Q,I pro počty indukovaných trojic s3,2,1,0 hranami,
M=C(n,2), B=C(n,3). Z139 jsou očekávání B/8,3B/8,3B/8,B/8.
Platí3T+2P+Q=(n−2)e a3T+P=Σ C(d_i,2): první dvojím započtením hran
v trojicích, druhá centrovaných dvojic hran. Dále Σd_i=2e.
Je-li T=B/8, Σd_i=M a Σd_i²=nM/2, potom e=M/2 a
3T+P=(n−2)M/4=3B/4. Odtud P=3B/8, Q=3B/8 a I=B/8.
Naopak tyto čtyři počty pro n≥3 dají e=M/2 a uvedené dva stupňové součty.
Další vytištěná identita Σd_i(n−1−d_i)=2P+2Q počítá orientované
páry soused/nesoused se společným středem; rovněž souhlasí.
Výjimku n=2 výslovně přiznává sama odpověď; zde se nezakládá nová karta.

Po známém přeznačení W_n znamená n paprsků, n+1 vrcholů.
Pro n≥4 má W_n n trojúhelníků. P₃ s centrem v náboji je n(n−3)/2,
bez náboje n po sobě jdoucích trojic obvodu, dohromady C(n,2).
W₇ má8 vrcholů, T=7=B/8; stupně7,3,…,3 dávajíΣd=28 aΣd²=112.
Je proto proportional, jak požaduje opravené zadání a odpověď.
Citované asymptotické varianty rozptylu jsou explicitní externí vstup;
nejsou zde znovu dokázány ani používány v následující nemožnosti142.

## 141: aritmetická část uzavřena, census oddělen

Nutné e=M/2 vyžaduje n≡0,1 modulo4. Nutné B/8 celé znamená,
že n(n−1)(n−2) je dělitelné48. Pro n≡0 modulo4 se tím vyžaduje
8|n; pro n≡1 modulo4 je nutné16|(n−1). Proto n mod16∈{0,1,8}.

Pro n=8 lze všech osm stupňových posloupností (*) odvodit bez výčtu
grafů. Polož r_i=2d_i−7: lichá čísla z±1,±3,±5,±7 mají součet0
a součet čtverců56. Označíme-li a,b,c počty absolutních hodnot7,5,3,
odečtení osmi základních jedniček dává6a+3b+c=6.
Pro a=1 vzniká73333333 nebo komplement44444440.
Pro a=0,b=0,c=6 jsou tři+3,tři−3,jedno+1 a−1:55543222.
Pro b=1,c=3 lze komplementací dát znaménko5 kladné. Jsou-li k,l počty
kladných trojek/jedniček, 3k+l=4. Řešení(0,4),(1,1) dávají64444222
a65433322 a jejich komplementy55533331,55444321.
Pro b=2,c=0 musí být jedna+5,jedna−5,tři+1,tři−1:64443331.
Jiné případy neexistují. Tím je přesně doložen seznam osmi posloupností.

Pro self-complementary graf musí posloupnost být invariantní d↦7−d.
Z osmi zůstávají55543222 a64443331. První ale porušuje párování
d₃=d₄ a druhá d₁=d₂, které bylo dokázáno v107 pro n=8.
Žádný proportional graf řádu8 proto není self-complementary.
Počty grafů N, proportional podpočty N₁ a maximální symetrie čtyř
dalších obrázků zůstávají partial: jejich úplný grafový census se nespouští.

## 142: extraproportional graf neexistuje

Každá trojice leží v n−3 čtveřicích; součty přes jedenáct typů
čtyřvrcholových grafů tedy vynutí správné očekávání každého typu trojice.
Známý opravený hint má u jednotlivých typů přesně počet jejich trojúhelníků;
jde o tuto dvojitou incidenci, stejně pro ostatní typy trojic.
Zejména e=M/2 a počet dvojic hran se společným vrcholem je3B/4.
Počet dvojic disjunktních hran je3 C(n,4)/4: na každé čtveřici jsou
tři možné matchingy a pravděpodobnost obou jejich hran je1/4.
Všechny neuspořádané dvojice hran se dělí právě na tyto dva druhy.
Muselo by tedy platit C(M/2,2)=(3/4)(C(n,3)+C(n,4))=C(M,2)/4.
Levá strana je M²/8−M/4, pravá M²/8−M/8, rozdíl−M/8≠0 pro n≥4.
To je přímý obecný spor a ověřuje celou odpověď142 bez cenzu jedenácti typů.

## 143–145: redukce a algoritmus

143: hrany grafu řádků spojují dvojice lišící se právě v jednom sloupci
a nesou jeho index. Na cyklu se index každé hrany musí objevit znovu:
po návratu je hodnota každé souřadnice stejná, jediná změna by to porušila.
Odstranění hrany cyklu proto neodstraní žádný index úplně.
Po opakování zbude les s nejvýše m−1<n hranami a tedy méně než n indexy.
Sloupec bez indexu lze smazat; jinak by dvě původní řádky lišící se jen
v něm vytvořily právě chybějící hranu. Důkaz platí pro libovolné hodnoty,
nikoli jen bity.

144: spoj dvě řádky, právě když některý sloupec obsahuje v obou určené
různé bity. Stejný dokončený řádek nikdy nespojí sousední vrcholy.
Naopak v nezávislé barevné třídě jsou všechny určené bity v každém
sloupci kompatibilní; doplň je společně, neurčený sloupec třeba nulou.
Minimum různých řádků je proto přesně chromatické číslo konfliktního grafu.
Pro opačný převod má X nuly na diagonále, jedničky na hranách a* jinde.
Sousední i,j se liší ve sloupci i (i ve sloupci j), nesousední nekolidují:
mimo obě diagonály jsou pouze1/*, na diagonále nesouseda je*.
Tedy vytištěné X=A+*(J−I−A) realizuje přesně libovolný původní graf.

145: po každém prefixu jsou jeho nevyřazené položky c kopií kandidáta x;
ostatní lze rozdělit na dvojice nestejných hodnot. Při jiné nové hodnotě
odstraníme právě jednu takovou dvojici, při stejné zvýšíme c a při c=0
založíme kandidáta. Vyřazení nestejné dvojice nemůže zničit přísnou
majoritu: odebere nejvýše jeden její prvek a přesně dva celkové prvky.
Na konci proto musí být c>0 a x je zaručená majorita.
První vstup nevyžaduje srovnání hodnot; každý další nejvýše jedno,
takže nejvýše n−1<n. Test c=0 není srovnání prvků vstupního pole.

Obdobný argument ověřuje i zmíněné rozšíření nad n/k: udržuj nejvýše
k−1 kandidátů, při plném nesouhlasícím vstupu odeber k různých hodnot.
Každá hodnota četnější než n/k musí zůstat mezi kandidáty.
Celkové náklady hromadného snižování jsou O(n), protože odstraňují
disjunktně reprezentované výskyty. Vyhledávání/vkládání/mazání kandidátů
ve vyváženém stromu a následný průchod pro přesné četnosti stojí O(n log k).
Historická atribuce a hlubší analýza citovaná v pozdějším erratu nebyly
samostatně rekonstruovány; jednoduchý algoritmický argument je uzavřen.

§7 je tím po jednotlivých tvrzeních a úlohách zpracován s výslovnými
datovými/výzkumnými mezerami. Další důkazový kurzor file064/p47, §7.1.1.
Čtecí kurzor hlavního textu zůstává235/218.

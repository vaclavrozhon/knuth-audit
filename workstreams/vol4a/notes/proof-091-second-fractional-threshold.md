# Druhý necelý příklad104(c): přesné minimum69

7. listopadu 2026, p553/file570; checkpoint X0119,
P1127–P1131, uzavření P1116. Originál vytištěného devítiproměnného
příkladu byl zobrazen v X0115/X0117 a nepřepisuje se podle OCR.
Žádný program, LP běh ani census. Globální tvrzení „právě dva“
zůstává samostatná otevřená povinnost.

## 1. Přesný kandidát a vyloučení poloviny součtu

Vytištěné celočíselné váhy jsou

    v=(17,15,11,9,7,5,4,2,1),       Σv=71.

Odvodíme racionální optimum z vektoru

    a=(33,29,21,17,14,10,8,3,3),   Σa=138,
    w*=a/2,                       Σw*=69.

Žádná bitová podmnožina a nemá součet69. Sudé váhy14,10,8
dávají E∈{0,8,10,14,18,22,24,32}. Liché váhy jsou33,29,21,17,3,3,
se součtem106. Jejich požadovaný lichý součet by byl některý z

    {69,61,59,55,51,47,45,37}.

Jediná lichá váha je nejvýše33, pět vah nejméně106−33=73.
Všechny možné součty tří jsou

    {23,27,35,39,41,49,53,57,65,67,71,79,83},

jak plyne rozdělením podle největší vybrané váhy33/29/21/17.
Žádný neleží v požadované množině. Tím je nepřítomnost69
dokázána pro všechny vstupy. Funkce g=[a·x≥70] je self-duální,
protože komplementární sumy se doplňují do138 a hodnota69
nenastává. Vektor w* má na každém jejím pravdivém vstupu
normalizovanou podepsanou mezeru a·x−69≥1.

## 2. Všechny těsné podpory a shoda s vytištěnou funkcí

Pro a·x=70 je lichá část některá z{70,62,60,56,52,48,46,38}
a obsahuje sudý počet vah. Nula či šest lichých vah nevyhoví.
Dvojice mohou dát pouze62=33+29,46=29+17 nebo38=21+17.
Čtveřice jsou komplementy dvojic v celkové sumě106; vyhoví
pouze vyloučené dvojice o součtu36=33+3 (dvě volby),
46=29+17,50=33+17=29+21 nebo54=33+21. Doplnění příslušným E
dává přesně devět podpor v této tabulce:

|Řádek|Podpora B|λ|
|---|---|---:|
|A|127|15|
|B|2456|4|
|C|34567|14|
|D|2348|1|
|E|2349|1|
|F|13689|11|
|G|23589|8|
|H|14589|9|
|I|246789|6|

Položme δ=x_1+x_2+x_3+x_4+x_8−x_9. Platí2v·x=a·x+δ.
Je-li a·x≥70, pak δ≥1: pro x_9=0 by δ≤0 dalo sumu≤32;
pro x_9=1 by nejvýše jeden další kladný člen δ dal sumu
nejvýše3+33+32=68. Proto při a·x≥71 máme2v·x≥72.
Při a·x=70 jsou všechny možnosti uvedeny v tabulce; δ=2
na osmi řádcích a δ=4 na D=2348. Opět2v·x≥72.

Každý pravdivý vstup g je tedy pravdivý ve vytištěné většině
délky71, jejíž práh je36. Obě funkce jsou self-duální, takže
argument na komplementu dává i opačnou implikaci. Vektor w*
je proto přípustnou reprezentací právě vytištěné funkce,
nikoli jiné blízké funkce. Každá tabulková podpora je také
prime pro g: všechny její váhy jsou alespoň3 a odebrání
libovolné již nedosáhne70.

## 3. Duální certifikát reálného minima69

Nezáporné λ v tabulce mají součet69. Každý index1..9 má
váženou incidenci35; úplné ověření sloupců je:

    1: A+F+H       =15+11+9=35,
    2: A+B+D+E+G+I =15+4+1+1+8+6=35,
    3: C+D+E+F+G   =14+1+1+11+8=35,
    4: B+C+D+E+H+I =4+14+1+1+9+6=35,
    5: B+C+G+H     =4+14+8+9=35,
    6: B+C+F+I     =4+14+11+6=35,
    7: A+C+I       =15+14+6=35,
    8: D+F+G+H+I   =1+11+8+9+6=35,
    9: E+F+G+H+I   =1+11+8+9+6=35.

Vynásobení devíti nutných nerovností2Σ_Bw_j−Σ_allw_j≥1
těmito λ dává koeficient2·35−69=1 u každé proměnné.
Tedy Σw_j≥69, a w* tuto mez dosahuje. To je přesný duální
certifikát, nikoli numerický odhad LP minima.

## 4. Jediné optimum je necelé

Protože všechny λ jsou kladné, každé optimum69 musí mít všech
devět podmínek těsných, tj. všechny tabulkové podpory mají
novou váhu35. Z D−E plyne w_8=w_9=q. Zbývající proměnné
označme(a,b,c,d,e,p,r)=(w_1,…,w_7). Rozdíly C−B, G−D,
H−G a I−B dávají

    b=c+r,  d=e+q,  a=b+c−d,  e=r+2q.

Proto d=r+3q a a=2c−3q. Rozdíl F−A dá p=2r−2q.
Rovnosti B,D,A se potom redukují na

    c+5r+3q=35,
    2c+2r+4q=35,
    3c+2r−3q=35.

Poslední minus prostřední dává c=7q. První dvě pak
5r+10q=35 a2r+18q=35, tedy q=3/2, r=4 a c=21/2.
Zpětné dosazení určí všechny váhy jednoznačně jako w*=a/2
z §1. Některé jsou poloviční, takže žádné celočíselné optimum
s touž hodnotou69 neexistuje. Tím je samostatné tvrzení
o necelosti druhého příkladu skutečně prokázáno.

## 5. Přesný celočíselný závěr a meze rozsahu

Každá plochá většina má lichou délku. Reálná dolní mez69
není celočíselně dosažitelná, takže nejmenší možná délka je
nejméně71. Vytištěný vektor v ji dosahuje podle §2. I jeho
celočíselná optimalita je tedy doložena. Případné celočíselné
LP řešení se sudým součtem70 by podle proof-087 vedlo
odebráním jednoho hlasu k zakázanému součtu69.

P1116 je checked. P1115 („právě dva“ v úplné třídě) se tím
neuzavírá: ověření dvou konkrétních příkladů není úplný census.
Stejně zůstávají otevřené P1114 a P1117–P1120. Přebírá se
erratová rešerše tohoto přesného dodatku z X0117, bez nového
nálezu či opakované bibliografické/census práce.

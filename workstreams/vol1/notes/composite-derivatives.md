# §1.2.5-21: vyšší derivace složené funkce

Zadání s. 52 a odpověď s. 481–483 byly zobrazeny v originálu.
Nechť u=u(x), w=w(u) mají potřebných n derivací. Symbol D_x značí
derivaci podle x a D_u derivaci vnější funkce podle jejího argumentu.
Položme `u_r=D_x^r u`, `w_j=D_u^j w`. Po složení platí
`D_x(w_j)=w_(j+1)u_1` a `D_x(u_r)=u_(r+1)`.

## Indukce přes rozklady množiny

Rozklad množiny {1,...,n} je neuspořádaná množina neprázdných
disjunktních bloků, jejichž sjednocení je celá množina. Každému
rozkladu P přiřaďme výraz

```text
w_(number of blocks in P) product_{B in P} u_(size of B).  (1)
```

Při derivování (1) buď derivujeme w_j a přidáme nový jednoprvkový
blok {n+1}, nebo derivujeme jeden faktor u_r a vložíme n+1 do
příslušného bloku. Každý rozklad n+1 prvků vznikne právě jednou:
odstranění n+1 z jeho bloku jednoznačně určí předchůdce i operaci.
Od n=0, kde je prázdný rozklad a výraz w, tedy indukcí dostáváme
součet (1) přes všechny rozklady pro D_x^n w. Stromy výrazů a
rozkladů otištěné pro n=1,2,3 odpovídají této konstrukci.

Je-li k_r počet bloků velikosti r, platí `sum_r k_r=j` a
`sum_r r k_r=n`. Počet rozkladů s těmito počty je

```text
n! / product_{r=1}^n [k_r! (r!)^k_r].                   (2)
```

Důkaz: nejprve rozmístíme n označených prvků do označených krabiček
o předepsaných kapacitách a vydělíme r! za pořadí uvnitř každé.
Potom vydělíme k_r! za pořadí krabiček stejné kapacity. Tyto akce
jsou volné, protože prvky i bloky jsou neprázdné a různé.
Obrázek krabiček na s. 482 má právě tyto kapacity a skupiny.
Dosazením (2) do součtu (1) vzniká přesně vzorec v zadání.

## Rekurence koeficientů v odpovědi

Označme C_n(k_1,k_2,...) hodnotu (2), pokud sum r k_r=n,
a 0 pro nepřípustné či záporné indexy. Po jedné derivaci dostaneme

```text
C_(n+1)(k) = C_n(k−e_1)
             + sum_{r>=1}(k_r+1) C_n(k+e_r−e_(r+1)),   (3)
```

kde e_r má 1 na pozici r a jinde 0. V první větvi se počet bloků
zvýší o 1, v dalších zůstane stejný. Vytkneme-li z pravé strany
`n!/product k_r!(r!)^k_r`, z první větve zůstane k_1,
z r-té další větve (r+1)k_(r+1). Součet je n+1, což dokazuje
koeficient (2) pro n+1. Toto rovněž vysvětluje zdánlivou změnu
váženého součtu indexů v knižním textu: nový řádek má váhu n+1.

## Důkaz pomocí Taylorových koeficientů

V koeficientu z^n ve w(u(x+z)) lze všechny Taylorovy výrazy zkrátit
na konečné řady do stupně n. Vnější j-tý člen je
`w_j/j! * (sum_{r=1}^n u_r z^r/r!)^j`.
Multinomický rozvoj dává koeficient
`w_j product u_r^k_r/[product k_r!(r!)^k_r]` pro sum r k_r=n.
Porovnání s D_x^n w/n! je knižní třetí důkaz. Není nutná
konvergence nekonečné Taylorovy řady; při n-násobné spojité
diferencovatelnosti postačí konečný Taylorův vzorec se zbytkem o(z^n).

## Determinant na s. 483

Nejprve zaveďme **komutující formální proměnné** v_1,...,v_n.
Matice H_n má pro 1<=i<=j<=n prvek
`binom(n−i,j−i) v_(j−i+1)`, pod hlavní diagonálou hodnoty −1
a pod nimi nuly. Nechť D_n=det H_n a D_0=1.
Rozvoj prvním řádkem dává

```text
D_n=sum_{r=1}^n binom(n−1,r−1) v_r D_(n−r).            (4)
```

Minor příslušného prvku obsahuje r−1 faktorů −1; jejich znaménko
se ruší s kofaktorem. Zbývající pravý dolní blok je H_(n−r).
Stejnou rekurenci má součet `product_{B in P} v_(size B)` přes
rozklady P: zvolíme r−1 dalších prvků bloku obsahujícího 1 a potom
rozložíme ostatní prvky. Oba polynomy proto souhlasí pro všechna n.

Nyní dosaďme v_r=u_r D_u s významem: nejprve se násobí koeficienty
u_r a až pak se mocnina D_u aplikuje na w. Ekvivalentně považujme
x a argument vnější funkce za nezávislé proměnné a proveďme složení
až po derivování podle druhé proměnné. Pak proměnné v_r komutují
a (4) dává právě (1). To je standardní formální význam knižního
operátorového determinantu. Pokud by se u_r předčasně přepsaly
jako funkce u a D_u působilo i na ně, šlo by o jiný operátor;
tuto nestandardní interpretaci při kontrole nepoužíváme.

## Prameny

Matematický vzorec, všechny tři důkazy a determinant jsou doloženy
výše. Přečten byl také Arbelův přetisk francouzského textu
Faà di Bruna (arXiv:1612.05393, s. 4–5). Obsahuje tento vzorec
i determinant s výslovnou konvencí, že mocniny symbolu pro vnější
funkci se po rozvinutí čtou jako řády derivace. Přesun prvního
sloupce jeho matice na konec ruší uvedené znaménko (−1)^n
a dává tvar v knize. Jde o přetisk, nikoli zobrazení původní sazby
Quarterly Journal 1 (1857), s. 359–360; odkaz na originál
v Google Books nebyl přístupný.

Arbogast §52 a Wall 1938 zatím nejsou přečteny. Goodův odkaz
540–541 je dílčí rozsah článku The Multivariate Saddlepoint Method
and Chi-Squared for the Multinomial Distribution, Annals of
Mathematical Statistics 32 (1961), 535–548, DOI 10.1214/aoms/1177705059.
Metadata byla nalezena, plný text v tomto průchodu nebyl dostupný.
Historické citace proto zůstávají partial; vlastní důkazy výše
nejsou nahrazeny bibliografickými záznamy.

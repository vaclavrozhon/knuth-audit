# Runs: úlohy17–22, zadání46–47, odpovědi605–606

Sazba v `images/runs-file-057.png`, `runs-file-058.png`,
`multisets-file-616.png`, `multisets-file-617.png`. Errata převzata
ze `sources/runs-errata-review.json`. Bez nového nálezu a běhu.

17. Pro neprázdné binární slovo s k−1 poklesy10 počítejme pozice,
    kde se bit změní. Končí-li slovo0 a začíná0, je změn2k−2;
    začíná-li1, je jich2k−3. Součet
    `choose(n−1,2k−2)+choose(n−1,2k−3)=choose(n,2k−2)`.
    Při konci1 jsou obdobně počty změn2k−1 nebo2k−2, tedy
    `choose(n,2k−1)` možností. Pascalova identita dává celkových
    `choose(n+1,2k−1)`. Neplatné dolní indexy znamenají0.
18. (a) Převzatý V3-P0121 říká, že b_i>b_(i+1) právě tehdy,
    když i leží v původní permutaci napravo od i+1. Tedy jde o
    sestupy inverzní permutace a počet je A(n,k).
    (b) Po smazání b_1 zůstane libovolná tabulka velikosti n−1.
    Má-li k různých hodnot, přidání jedné z těchto k hodnot počet
    zachová. Má-li k−1 hodnot, právě n−k+1 hodnot z0..n−1 je nových.
    To dává tištěnou rekurenci f(n,k); základ f(1,1)=1 ji ztotožní
    s A(n,k−1) pro n≥1. Prázdná tabulka má samostatně0 různých hodnot.
19. (a) Rozmístění n věží je biword top=řádek,bottom=sloupec.
    Pod diagonálou je top>bottom. Převzatá Foatova bijekce dává A(n,k).
    (b) Každé částečné rozmístění k věží lze doplnit(n−k)! způsoby.
    Z úplného rozmístění s j dolními věžemi lze vybrat choose(j,k)
    takových částečných rozmístění. Po dělení(n−k)! a použití
    již dokázané úlohy2(a), q=n−k, vyjde S(n,n−k).

    Přímá bijekce: v každém bloku množinového rozkladu spoj po sobě
    rostoucí hodnoty x<y hranou x→y a polož věž do řádku y,sloupce x.
    Vstupní i výstupní stupeň je nejvýše1 a hrany přísně rostou,
    takže nevznikají cykly. Obráceně každé rozmístění pod diagonálou
    rozloží1..n na tyto cesty a izolované body. Při k věžích je bloků
    n−k. Obě zobrazení jsou inverzní.

    Obr.4 má na celé desce sloupce po řádcích2,6,1,5,8,4,7,3.
    Dolní věže jsou právě(3,1),(6,4),(8,3), což dává bloky
    {1,3,8},{2},{4,6},{5},{7}, stejně jako trojúhelníkový obrázek.
    Číslo15619=A(8,3) je převzato z ověřené tabulky1.
    Počet S(8,5)=1050 lze ověřit bez enumerace třemi možnými typy:
    jeden blok4: choose(8,4)=70; blok3 a blok2: choose(8,3)choose(5,2)=560;
    tři bloky2:8!/(2!³3!2!)=420. Součet je1050.
20. Nechť p_i je pozice hodnoty i. Další hodnota i+1 jde přečíst ve
    stejném průchodu právě když p_i<p_(i+1). Nový průchod proto začíná
    přesně v sestupu inverzní permutace. V příkladu491825367 jsou
    pozice `357|1689|4|2`, tedy průchody hodnot1–3,4–7,8,9, jak je tištěno.
21. Obrácení slova vymění vzestupy a sestupy, takže počet běhů je
    n+1−k. Inverzní pozice se změní na n+1−p_i, což komplementuje
    sestupy v inverzi, a počet průchodů je n+1−j.
22. Nutnost rs≥n: z s průchodů musí jeden obsahovat t>r hodnot,
    jestliže rs<n. Jejich pozice jsou rostoucí a hodnoty tvoří souvislý
    interval. Mezi každými dvěma sousedními vybranými pozicemi musí být
    alespoň jeden vzestup; jinak by první hodnota byla větší než poslední.
    Jde o disjunktní úseky, tedy alespoň t−1>r−1 vzestupů. To odporuje
    požadovaným n+1−r běhům, čili právě r−1 vzestupům.

    Dostatečnost v tištěném rozsahu: podmínky jsou r+s≤n+1, rs≥n,
    r,s≥1. Inverze následovaná obrácením zamění parametry r a s
    podle20–21, takže předpokládejme r≤s. Pro r1 nutně s=n a stačí
    klesající permutace. Jinak r≥2 a n≥2r−1.

    První konstrukce klade za sebe residue bloky α_r,...,α_1,
    uvnitř každého klesající hodnoty j modulo r. Uvnitř jsou poklesy;
    každý přechod mezi bloky je vzestup, neboť n≥2r−1. Proto má
    n+1−r běhů. Hodnoty v každé hladině {ar+1,...,ar+r} mají pozice
    v opačném pořadí, zatímco mezi hladinami pozice vzroste. Je tedy
    přesně n+1−q průchodů, q=ceil(n/r), včetně neúplné horní hladiny.
    Příklad n9,r4 je84|73|62|951, přesně tištěné slovo.

    Libovolné přeznačení hodnot uvnitř každé hladiny zachová srovnání
    mezi hladinami, tedy poklesy uvnitř residue bloků a vzestupy na
    jejich hranicích. Počet běhů se nemění. Přeznačme každou hladinu
    vzestupně podle pozice: uvnitř hladiny teď inverzní pozice rostou,
    mezi hladinami klesají, a proto zbude q průchodů.
    Z původního přeznačení do nového lze přejít sousedními záměnami
    hodnot téže hladiny. Jedna taková záměna prohodí dva sousední členy
    inverze a mění její počet sestupů nejvýše o1: změna prostřední hrany
    má opačné znaménko než změny obou vnějších hran. Cesta proto
    dosáhne každého celočíselného počtu průchodů mezi q a n+1−q.

    Jestliže s>n+1−q, položme h=n+1−r−s≥0. Z s>n+1−q a
    q≤ceil(n/2) plyne h<q−r≤(n−r)/2. Tištěná druhá konstrukce je
    spojení čtyř úseků
    `2h+1,2h−1,...,1 ; n+2−r,n+1−r,...,2h+2 ;
     2h,2h−2,...,2 ; n+3−r,...,n`.
    Prostřední vysoký úsek je neprázdný, třetí může být prázdný pro h0
    a poslední pro r2. Přechod z prvního do druhého je vzestup;
    poslední rostoucí úsek přidá dalších r−2, takže vzestupů je r−1.
    V inverzi je h poklesů typu2j→2j+1 a n−r−2h poklesů uvnitř
    vysokého klesajícího úseku; ostatní přechody jsou vzestupy.
    Počet průchodů je proto n+1−r−h=s. To pokrývá všechny zbývající
    případy včetně r2 a h0.

Historické atribuce a obsah citovaných prací nebyly ověřeny;
všechny zde uvedené počty a konstrukce jsou doloženy přímo.

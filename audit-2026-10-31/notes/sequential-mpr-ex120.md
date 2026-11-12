# MPR 120: profil náhodného BST a úplný martingalový argument

D218, 7. listopadu 2026. Zadání p24/file44, odpověď p389/file409
a autorův PS p24/46 (file30/52) zobrazeny. Odpověď obsahuje jen
bibliografický odkaz, proto je celý potřebný důkaz rozveden zde.
Žádný nový nález, kandidát, matematický běh ani restart.

## Stav, invariant a správná filtrace

Klíče U1,U2,… jsou nezávislé a rovnoměrné na[0,1]. Každá shoda
dvou má pravděpodobnost nula, a spočetné sjednocení všech shod
také; dále pracujeme na této události pravděpodobnosti jedna.
Úroveň kořene je0. Prázdný strom má jeden vnější uzel na úrovni0.
Vložení nahradí právě jeden vnější uzel vnitřním a vytvoří jeho
dva vnější syny. Indukcí má strom s n klíči n+1 vnějších uzlů,
každý v hloubce nejvýše n. Polynom

    B_n(z)=Σ_k T_nk z^k,     T_n(z)=B_n(z)/(n+1)

má tedy konečně mnoho členů, B_0=1 a T_0=1. Zápis stejného
písmene pro strom a normalizovaný polynom rozlišujeme argumentem z.

Nechť F_n je sigma-algebra relativního pořadí prvních n
očíslovaných klíčů. Je to filtrace: odstraněním labelu n+1
z pořadí prvních n+1 klíčů obnovíme pořadí prvních n. Z něho
lze rekonstruovat každý dřívější tvar stromu, takže B_n je
F_n-měřitelné. Pro každé pevné pořadí n starých labelů a každou
z n+1 možných pozic nového labelu existuje právě jedno pořadí
n+1 labelů. Všechna mají pravděpodobnost1/(n+1)!, neboť
společný spojitý zákon je symetrický v označeních. Podmíněně
na kterémkoli atomu F_n je proto nová pozice uniformní.

Mezi n setříděnými klíči je n+1 mezer včetně krajních. Každá
odpovídá právě jednomu vnějšímu uzlu: platí to pro prázdný strom
a vložení rozdělí jednu mezeru i její vnější uzel na dva.
To je přesná bijekce, nikoli předpoklad stejné délky mezer.
Je-li K hloubka vybraného uzlu, plyne

    E(z^K | F_n)=B_n(z)/(n+1)=T_n(z).

Totéž platí při podmínění celou historií tvarů stromu, pomocí
tower property. Neužíváme sigma-algebru přesných číselných
hodnot U1,…,Un: při takovém podmínění by pravděpodobnosti
mezer byly jejich délky. To není filtrace potřebná pro tvrzení.

## Každý normalizační krok

Vnější uzel v hloubce K přispíval z^K a jeho dva noví synové
přispívají2z^(K+1). Platí tedy přesná identita

    B_(n+1)=B_n+(2z−1)z^K,
    E(B_(n+1) | F_n)=[1+(2z−1)/(n+1)]B_n
                    =(n+2z)B_n/(n+1),
    E(T_(n+1) | F_n)=(n+2z)T_n/(n+2).

Definujme g_1=1 prázdným součinem. Z tištěného součinu plyne

    g_(n+1)(z)=(2z)(2z+1)…(2z+n−1)/(n+1)!,
    g_(n+2)(z)/g_(n+1)(z)=(n+2z)/(n+2).

Pro pevné reálné z, při němž všechny jmenovatele jsou nenulové,
tudíž

    E(Z_(n+1) | F_n)
      = (n+2z)T_n / [(n+2)g_(n+2)]
      = T_n/g_(n+1)=Z_n.

Na každém pevném kroku existuje jen n! pořadí, tedy konečně
mnoho konečných hodnot Z_n; integrabilita a adaptovanost jsou
tím doloženy. Navíc Z_0=1. Historie samotných Z je obsažena
ve F_n, a tower property proto dává i definici martingalu
použitou v knize. Komplexní z lze zpracovat po reálné a
imaginární složce; pro reálné tvrzení to není nutné.

## Parametr z a všechny okraje

Přímý podíl je definován pro
z∉{0,−1/2,−1,−3/2,…}; zejména pro všechna z>0.
To je přirozená doména tištěného podílu, nikoli nový kandidát.
Pozdější primární článek Chauvin–Klein–Marckert–Rouault tuto
množinu v rov.(7) také výslovně vylučuje.

Pro z=0 lze přirozeně doplnit odstranitelnou singularitu:
pro n≥1 jsou všechny vnější hloubky alespoň1, tedy B_n
je dělitelné z. Faktor z v g_(n+1) je jednoduchý, ostatní
faktory při n≥1 jsou po vyjmutí z nenulové. Každý podíl
má proto konečnou limitu při z→0. Na pevném kroku je
podmíněná střední hodnota konečný vážený součet, takže
limitou předchozí identity dostaneme martingal i v0,
s definicí Z_0=1. U ostatních záporných půlcelých bodů
netvrdíme obecnou odstranitelnost ani existenci podílu.

Pro z=1 je B_n=n+1, T_n=g_(n+1)=1 a Z_n=1.
Pro z=1/2 profilová identita dává B_n=1 pro každé n;
T_n=g_(n+1)=1/(n+1), takže opět Z_n=1.
Pro n=0 je K=0 a první vložení má cenu0; všechny
rovnosti včetně prázdných součinů zůstávají platné.

## Proč je g přesně PGF ceny vložení

Cena (počet porovnání s klíčem) při vložení do stromu s n
vnitřními uzly je právě hloubka zvoleného vnějšího uzlu K:
na každé úrovni před ním se navštíví jeden vnitřní uzel.
Podmíněný PGF této ceny je tedy T_n(z), a nepodmíněný
je E T_n(z). Normalizační rekurence dává indukcí

    E T_n(z)=Π_(j=0)^(n−1) (j+2z)/(j+2)=g_(n+1)(z).

Je to polynomická identita, takže platí i v bodech,
kde se martingalový podíl přímo nedefinuje. Tím je
ověřen přesný odkaz na cenu n-tého vložení, nikoli součet
cen prvních n vložení.

Původní svazek3, cvičení6.2.2–6 na p454–455 (DjVu file465–466)
a odpověď p709 (file720), byl zobrazen. Tamní P_nk počítá
permutace s cenou k při n-tém vložení a G_n=ΣP_nk z^k;
proto g_n=G_n/n!. Z našeho argumentu vyplývá také tištěný
potřebný vztah G_(n+1)=(2z+n−1)G_n a jeho koeficientová
verze P_(n+1),k=2P_n,(k−1)+(n−1)P_nk. Další části
odkazované úlohy o rozptylu a Stirlingových číslech nejsou
závislostí úlohy120 a zde se neuzavírají.

## Ukončení, náklady a zdroje

Jedno vložení sestupuje o úroveň na porovnání a po nejvýše n
porovnáních dosáhne vnějšího uzlu. Aktualizace profilového
pole mění jen T_nK a T_n,(K+1), tedy O(1) položek po zjištění K.
Strom i profil používají O(n) míst; N vložení má triviální
horní mez O(N²) porovnání. Vyhodnocení profilu a součinu
g na pevném kroku lze provést O(n) aritmetickými operacemi;
nejde o tvrzení o bitové složitosti nebo průměrném vyhledávání.
K důkazu nebyl třeba běh ani simulace.

Chauvin–Klein–Marckert–Rouault, primární autorský PDF
`embeddingejp.pdf`, byl přečten/zobrazen v potřebném rozsahu:
p1–2 konstrukce a filtrace, p3 doména z a p4 rov.(8).
Jejich C_n(z)=Π_(k=0)^(n−1)(k+2z)/(k+1)
je (n+1)g_(n+1), takže M_n=B_n/C_n je přesně naše Z_n.
Nepřebíráme další tvrzení o Yuleově procesu a konvergenci.

Původní Jabbour-Hattabův článek RSA19(2001),112–127 nebyl
rychle dostupný v plném znění. Vydavatelská Crossref metadata
ověřují autora, název, rok, svazek a stránky; přesný obsah
původního historického důkazu je jedinou bibliografickou
výjimkou. Není matematickou závislostí: vše potřebné je
dokázáno výše. Šest vrstev errat a tři TeX zdroje neobsahují
použitelnou opravu120. Celá120 je checked; file409 je
reviewed se čtyřmi přesnými bibliografickými výjimkami pro
117–120. File44 zůstává partial pro121–122.

# D186 — celá MPR85, poměr barev

7. listopadu 2026. Zadání p20/file40 a odpověď
p383/file403 přímo zobrazeny; autorův PS p20/file26
a p39/file45 také. Všechny šest vrstev errat
a tři TeX zdroje v samostatném manifestu85.
Žádný výpočet ani restart.

Na úrovni n původní Pólyovy urny platí
R_n+B_n=n+2 a1≤R_n,B_n≤n+1, protože počáteční
stav je(1,1) a každým tahem se přidá jedna koule.
Žádný níže použitý jmenovatel není0. V každém
pevném čase jsou všechny posuzované poměry omezené.

Červený podíl P_n=R_n/(R_n+B_n) je již plně
dokázaný martingale vůči celé urnové historii
v D098. Proto je i Q_n=1−P_n=B_n/(R_n+B_n)
martingale: podmíněné očekávání respektuje
odečtení od konstanty. Navíc Q_n≥1/(n+2)>0.

Funkce f(x)=1/x má druhou derivaci2/x³>0
pro každé x>0, a je tedy konvexní na celé
zde použité oblasti. Její transformace
f(Q_n)=(R_n+B_n)/B_n=R_n/B_n+1 je v čase n
nejvýše n+2, takže splňuje integrabilitní
podmínku přesně převzatého důkazu MPR84(a)
(D099, dokončení celé úlohy D185).

Konkrétně podmíněný Jensen vůči celé urnové
historii F_n dává

    E(f(Q_{n+1})|F_n)≥f(E(Q_{n+1}|F_n))
                         =f(Q_n).

Odečtením konstanty1 dostáváme stejnou
submartingalovou nerovnost pro T_n=R_n/B_n.
T_n je F_n-měřitelné. Podmínění obou stran
na jeho vlastní historii a věžová vlastnost
proto dokazují požadovaný submartingale
i v definici(32). Stejný závěr lze vyjádřit
přímo tím, že historie T a T+1 jsou ekvivalentní.
Žádné ztotožnění dvou různých podmínění F159
se zde nepřebírá.

Dovětek o přímém důkazu lze plně rozepsat.
V aktuálním stavu(r,b), s t=r+b, má příští
poměr dvě hodnoty: (r+1)/b s pravděpodobností r/t
a r/(b+1) s pravděpodobností b/t. Jeho rozdíl
oproti současnému r/b je v podmíněném průměru

    (r/t)(r+1)/b+(b/t)r/(b+1)−r/b
      =r((r+1)(b+1)+b²−(r+b)(b+1))/(t b(b+1))
      =r/(t b(b+1))>0.

Každý koeficient, společný jmenovatel i
zrušení členů jsou tím doloženy. Tento důkaz
vyžaduje přesně jen pozitivní celočíselné
stavy, které má Fig.P; nepřidává případy
prázdné nebo jednobarevné počáteční urny.
Vlastní historie se opět získá podmíněním.
V n=0 jde o stav(1,1), tedy platný první
krok s přírůstkem1/4.

Celé zadání, všechny tištěné transformace
i slíbená alternativní cesta jsou uzavřeny.
Jediné erratové shody patří SAT odpovědi85
ve Fascicle6 a nesouvisejí s touto úlohou.
Žádný nález, kandidát ani nová bibliografická
výjimka. Staré důkazy se přebírají v přesném
rozsahu, žádné staré testy se neopakují.


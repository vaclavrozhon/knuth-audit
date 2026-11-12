# Úloha40 — co je správné a co nestačí

P117/file132, odpověďp167/file182; originály zobrazeny. Aktuální
oprava13.9.2026 je zohledněna. Celková postačitelnost navržených
podmínek je samostatný candidate F7-C0005, podrobně v jeho poznámce.
Její vyvrácení neznamená, že jsou chybné následující pomocné kroky.

## P40-1 — bod, úsečka a projekce

Každá neprázdná fyzická hrana je A+t d, kde d≠0 a t je v uzavřeném
netriviálním intervalu. Kdyby její první dvě složky směru d byly
obě nulové, každý vnitřní bod by měl stejné(x,y) jako její koncový
vrchol a jiné z. První podmínka odpovědi proto skutečně implikuje
d_xy≠0. Za tohoto předpokladu se projekce každé hrany parametrizuje
injektivně a úsečka se nesmrští na bod.

Rovnost projekce vrcholu p s bodem hrany se rozhodne bez dělení
neurčitým výrazem: nejprve det(d_xy,p_xy−A_xy)=0 a pak se z kterékoli
nenulové složky d_xy vypočte jediné t. Zkontroluje se uzavřený
interval a případně rozdíl z. To je úplný kvantitativní test první
podmínky včetně konců; právě on byl použit u všech216 párů C0005.

## P40-2 — správná opravená kolinearita

Nechť dvě promítnuté podpůrné přímky mají směry(α,β),(α′,β′)≠0
a počátky(x_0,y_0),(x′_0,y′_0). Jsou totožné právě tehdy, když

αβ′−α′β=0 a (x′_0−x_0)β−(y′_0−y_0)α=0.

První rovnost říká, že směry jsou závislé, druhá, že posun počátků
leží v témže jednorozměrném směru. Je-li první podmínka nenulová,
přímky se pouze jednou protnou; je-li nulová jen první, jsou
rovnoběžné různé. Tím jsou dokázány obě strany přesného opraveného
testu. Původní zákaz pouze rovnosti αβ′=α′β byl příliš silný
a již opraven; zde se nepočítá jako nález.

Prostorově kolineární hrany se z tohoto zákazu záměrně vyjímají:
jejich společná podpůrná přímka se při netriviální projekci zachová
a různá neprotínající se podintervalová rozpětí se neslijí. Naopak
u prostorově nekolineárních hran se podmínka odpovědi požaduje pro
celé podpůrné přímky. Tuto silnější podobu C0005 také splňuje.

## P40-3 — stěna není kolmá na obrazovou rovinu

Rovina stěny má rovnici ax+by+cz=d, kde(a,b,c)≠0. Pokud c=0,
celá její projekce leží na přímce ax+by=d. Ve stěně ale existují
dvě sousední prostorově nekolineární hrany; jinak by neměla roh
ani nenulovou plošnou oblast. Jejich projekce jsou díky P40-1
netriviální a leží na téže přímce, což porušuje P40-2. Proto c≠0
a lze rovnici vydělit c, aby koeficient u z byl1. Toto dokazuje
celou závěrečnou závorku odpovědi pod jejími skutečnými předpoklady.

## P40-4 — neuzavřený celkový výsledek

Tyto tři správné pomocné argumenty neřeší shodu více promítnutých
průsečíků. C0005 má tři konvexní disjunktní tetraedry, splňuje všechny
výše uvedené testy, nemá vertikální stěny, ale vytváří čtyřvalentní
viditelnou křižovatku. Posuzování hlavního tvrzení zůstává candidate
a čeká na nezávislou revizi. Kompletní postačující oprava ještě není
prohlášena za dokázanou.

Byl cíleně přečten i jediný další indexový odkaz k obecné poloze:
odpověď61 na p172/file187. Tam autor u konkrétní sestavy krabic
výslovně požaduje vzájemnou různost všech průsečíků hran a jejich
odlišnost od rohů. To souhlasí s potřebou zabránit nové degeneraci,
ale je to podmínka tamního konkrétního obrázku; nedoplňuje chybějící
univerzální podmínku do samostatné odpovědi40. Počty a ostatní tvrzení
na p172 tím nebyly matematicky ověřeny.

# Kořenová revize opraveného lineárního deque algoritmu

Dne 2. listopadu 2026 byl převzat zmrazený blok
`parallel/deque-followup/`. Root přečetl celý obecný důkaz, celý
rozpoznávací program a celý nový validační program, jejich výsledky,
pramennou poznámku a kvalifikaci Dentonova důkazu. Přímo navíc zobrazil
Dentonovy originální strany 14–15 a 17–18. Původní knižní strany
243 a 539 jsou doloženy dřívějšími audity a přímým čtením podagenta;
root netvrdí jejich další vizuální průchod v tomto kroku.

Přijatý invariant uchovává přesnou množinu všech dosažitelných front
bez pasti. Past je menší prvek uvězněný mezi dvěma většími, který
nemůže být včas vypsán. Fronta bez pasti roste k maximu a pak klesá.
Vypsání dostupného nejmenšího prvku lze přesunout před pozdější vstupy:
na jeho budoucí výstupní straně nemohl mezitím přibýt blokující prvek.
Při jednoprvkové frontě lze zvolit právě tuto budoucí stranu.
Odebrání prvku navíc zachová nepřítomnost pasti.

Root přezkoumal všechny případy normalizace. U dvoustranného dolního
bloku je nutná kanonická forma: mezi oběma hlavami pak opravdu leží
větší svědek. Jinak by zamítnutí při příchodu většího prvku nebylo
odůvodněno. U jednostranného jednoprvkového centra dvě volby orientace
popisují stejnou skutečnou frontu; spojení bloků proto nic neztrácí.
U výstupu se dokazují obě inkluze množin smazáním a obnovením hlavy,
nikoli zachování počtu různých front. To pokrývá i sloučení dvou
realizací do jedné.

Příklad vstupu 231 z kvalifikace je správný: po výstupu 1 má zbývající
blok dvě realizace (2,3) a (3,2). Výstup 2 ponechá neprázdný blok,
ale jedinou realizaci (3). Dentonův mezikrok na začátku s. 18 tedy
není obecně platný. Lemma i opravený algoritmus zůstávají platné
na základě přímého množinového důkazu. Toto je kvalifikace externího
pramene, nikoli nový nález TAOCP.

Implementace skutečně spojuje spojové seznamy v konstantním čase
pomocí hlavy a posledního uzlu. Větve odpovídají obecné argumentaci;
prázdnost i ukončení jsou explicitní. Pro n přečtených prvků vznikne
nejvýše n bloků. Každá pokračující iterace normalizace blok odstraní
a každý úspěšný výstup odstraní prvek. Dostáváme lineární čas i paměť
ve slovním modelu pro permutaci 1..n. Ladicí výpisy a exponenciální
interpretace množin nejsou součástí tohoto tvrzení.

Nové výsledky obsahují 406 porovnání s přímým prohledáváním operací,
8534 porovnání celých množin, 150 dalších legálně vytvořených vstupů,
64 zakázaných vzorů a 12 dlouhých případů až do 100000 prvků.
Root tyto úspěšné testy neopakoval. Důkaz platí obecně a konečné testy
slouží k ověření jeho implementace.

Technická mezera X0220 je tím uzavřena jako samostatné X0664.
X0220 zůstává partial pro přesně vyjmenované původní prameny,
zejména Rosenstiehl–Tarjan 1984, s. 389–390. Správný titul tohoto
článku je v novém předání; chybný titul ve starých interních poznámkách
není chyba knihy, která titul vůbec neuvádí. Mealyho dodatečná s. 534
byla již samostatně převzata při X0657–X0660 a nepočítá se znovu.

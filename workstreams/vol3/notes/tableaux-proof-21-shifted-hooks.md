# Posunutá tableaux: úplná úloha21 a odpověď609

Zadání67/file78, odpověď609/file620. Původní obrázek i algebraická
odpověď byly zobrazeny v images/tableaux-file-078.png a -620.png.
Známá oprava1.1.2006 doplňuje závorky kolem součinu ve jmenovateli;
není naším nálezem. Níže jsou doloženy také dva zkrácené mezikroky
odpovědi: konstanta racionálního součtu a převod na zobecněné háčky.

## P0503: doména, rohy a rekurence

Tvar λ=(λ_1>…>λ_m>0) je striktní partition; řádek i obsahuje buňky
(i,j), i≤j≤E_i=λ_i+i−1. Konce E_i jsou slabě klesající a E_i≥m.
Rostoucí vyplnění štítky1,…,N, N=Σλ_i, může mít N jen v pravém
konci řádku bez buňky pod ním. Pro i<m je to ekvivalentní
λ_i−1>λ_(i+1); v posledním řádku je konec vždy přípustný. Smazání
poslední jedničkové řady zmenší počet řádků. Proto skutečný počet F
splňuje

    F(λ)=Σ_(přípustné i) F(λ−δ_i), F(prázdný tvar)=1.       (1)

Zde δ_i je jednotkový vektor v souřadnici i.
Každý menší tvar lze doplnit N právě do daného rohu. To dokazuje
oba směry rekurence, včetně případu λ_m=1.

## P0504: racionální identita platí pro všechna přípustná y

Nechť H(x)=Δ(x)/σ(x), kde
Δ=∏_(i<j)(x_i−x_j), σ=∏_(i<j)(x_i+x_j). Dokážeme

    Σ_i x_i H(x_1,…,x_i+y,…,x_m)=(Σ_i x_i)H(x).           (2)

Nejprve vezmeme obecná různá x_i, s nenulovými součty a s různými
párovými součty, aby všechny možné póly v y byly jednoduché.
Poté se identita rozšíří jako identita racionálních funkcí.

Možný pól y=−x_i−x_j vzniká jen ve sčítancích i,j. Pro i<j má
faktor páru v prvním členu reziduum−2x_j, ve druhém+2x_i.
Po násobení původními váhami x_i,x_j jsou rezidua−2x_i x_j a
+2x_i x_j. Zbývající faktory jsou v obou členech stejné: v prvním
se dvojice proměnných změní na(−x_j,x_j), ve druhém na(x_i,−x_i).
Pro každou jinou proměnnou se oba párové faktory zkrátí na+1,
leží-li její index mimo i,…,j, a na−1, leží-li striktně mezi i,j.
Společný faktor je tedy (−1)^(j−i−1) krát H na zbývajících indexech.
Rezidua se přesně vyruší.

Celá levá strana nemá žádný konečný pól. Každý její sčítanec je
navíc omezen pro y→∞, protože posunuté lineární čitatele a
jmenovatele mají stejný stupeň. Racionální funkce bez pólů je
polynom a omezený polynom je konstanta. Hodnota při y=0 je pravá
strana(2), čímž je identita dokázána.

Vypočtení derivace při y=0, uvedené v knize, je s tím konzistentní:
logaritmická derivace H přidá 2x_j/(x_i²−x_j²), takže vážené
členy páru mají součet

    2x_i x_j/(x_i²−x_j²)+2x_j x_i/(x_j²−x_i²)=0.

Pouhé vynulování derivace v jednom bodě by samo o sobě konstantnost
racionální funkce nezaručilo. Výše uvedené zrušení všech pólů je
zde potřebný doplněný argument; z této zkratky nezakládáme nález
nepravdivého výsledku.

## P0505: řešení rekurence a všechny hraniční členy

Definujme

    g(λ)=N! Δ(λ)/(∏_i λ_i! σ(λ)).

Pro kladný striktní tvar jsou všechny jmenovatele nenulové.
Po dělení rekurence pro g faktorem(N−1)!/∏λ_i! je zbývající
rovnost přesně(2) s x_i=λ_i a y=−1.

Nepřípustné odstranění z i<m znamená λ_i−1=λ_(i+1), a proto má
v příslušném členu Δ hodnotu0. Jeho σ je nenulové: pro dva různé
původní kladné díly je λ_i+λ_j−1≥2. Jestliže λ_m=1, dostane
poslední proměnná0. Všechny její faktory λ_j v Δ se přesně
zkrátí s λ_j v σ a0!=1, takže hodnota g je stejná jako po odstranění
nulového řádku. To je právě geometrická hranice rekurence(1).

Prázdný tvar má g=1. Indukce po N tedy dává F=g, včetně singletonu.
Dokázán je konkrétní vzorec počtu, nikoli pouze formální podobnost
s obyčejným hook vzorcem.

## P0506: přesná množina zobecněného háčku

Pro buňku(i,j) jsou v zobecněném háčku:
- její vlastní buňka a zbytek řádku i napravo;
- buňky sloupce j pod ní;
- celý řádek j+1, pokud j+1≤m.

Tyto tři množiny jsou disjunktní; poslední řádek začíná až ve
sloupci j+1. Je to U-tvar ve schodišťové části obrázku a obvyklý
L-tvar napravo od ní. Pišme E_i=λ_i+i−1 pro pravé konce řádků.

Pro i≤j<m existují pod buňkou právě řádky i+1,…,j: řádky dále
vpravo ještě ve sloupci j nezačaly a E_k≥m zaručuje existenci všech
předchozích. První dvě části háčku mají dohromady λ_i buněk,
třetí má λ_(j+1). Jeho délka je tedy λ_i+λ_(j+1).
Ve sloupci m je délka λ_i a napravo od něj zůstávají běžné háčky.
První m−i háčků v řádku i tak přidá součiny λ_i+λ_k, k>i.

## P0507: celý zbývající součin po řádcích

Pro j≥m označme c_j počet řádků končících nejdříve ve sloupci j.
Délka háčku v(i,j), m≤j≤E_i, je

    h_j=(E_i−j+1)+(c_j−i)=λ_i−j+c_j.

Začíná hodnotou h_m=λ_i. Když j přejde přes společný konec s<E_i
několika nižších řádků, c_j klesne o jejich počet r a h klesne
o r+1. Konkrétně pokud zde končí řádky
k=c_s−r+1,…,c_s, vynechané hodnoty jsou

    λ_i−s+c_s−r,…,λ_i−s+c_s−1
      = {λ_i−λ_k: E_k=s}.

Na konci j=E_i položíme pomocnou následující hodnotu0. Poslední
vynechané hodnoty1,…,c_(E_i)−i opět odpovídají přesně nižším řádkům
s E_k=E_i, protože λ_i−λ_k=k−i. Proto je množina háčků pro j≥m
právě {1,…,λ_i} bez různých hodnot λ_i−λ_k, k>i.

Vynásobením i s první schodišťovou částí řádku dostaneme

    ∏_(j=i)^E_i hook(i,j)
        =λ_i! ∏_(k>i)(λ_i+λ_k)/(λ_i−λ_k).

Součin všech řádků je ∏λ_i! σ(λ)/Δ(λ). Tím je z P0505 skutečně
odvozen tvar N! děleno součinem zobecněných háčků, jak žádá úloha21.

## P0508: všech17 háčků a zvýrazněný příklad

Pro λ=(7,5,4,1) vychází přímo z P0506–P0507

    řádek1: 12,11,8,7,5,4,1
    řádek2: 9,6,5,3,2
    řádek3: 5,4,2,1
    řádek4: 1.

To jsou všechny hodnoty obrázku a všech17 faktorů opraveného
jmenovatele. Háček(1,2) má šest buněk v prvním řádku, jednu ve
sloupci2 pod ním a čtyři buňky třetího řádku, celkem11; tím je
zkontrolováno i popsané zvýraznění, nikoli jen součin. Celková
velikost je7+5+4+1=17, takže uvedený čitatel17! má správný význam.
Závorky kolem jmenovatele se přebírají ze známé opravy.

Historická atribuce Thrallovi a obsah původního článku z1952 nebyly
samostatně ověřovány; všechna potřebná matematická tvrzení mají
výše vlastní důkazy. Úloha22 začínající na stejné straně se tím
neuzavírá; tato stránka dosud nemá celé argumentové pokrytí.

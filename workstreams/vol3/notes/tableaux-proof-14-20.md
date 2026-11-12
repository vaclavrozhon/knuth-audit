# Tableaux: úlohy14–20 a celé příslušné odpovědi

Zadání66–67/file77–78; odpovědi608–609/file619–620. Originály
images/tableaux-file-078.png, -619.png a -620.png byly zobrazeny.
Úlohy16 a17 jsou již doložené P0457 a P0435–P0436 a nepřepočítávají
se. Známá oprava z1.1.2006 vkládá závorky do součinu ve jmenovateli
úlohy20; oprava18.8.2002 mění elementární symetrické funkce a_j na e_j.
Obě jsou zohledněny, nikoli hlášeny jako nové chyby. Úloha14 níže
zůstává přesně vymezená partial. Žádný výpočtový běh nebyl spuštěn.

## P0489 — partial: požadavek úlohy14

Věta D(c) je již úplně dokázána v P0429–P0431 přes(a,b), Theorem B,
transpozici a lemma o odstranění největšího klíče. Úloha14 ale výslovně
žádá „a more direct proof“; odpověď v knize není uvedena. Dosavadní
důkaz tento zvláštní požadavek na jiný argument nesplňuje. Nepředkládám
odkaz na známé označení evacuation nebo growth diagram jako hotový
přímý důkaz. Otevřen je pouze tento dodatečný požadavek, nikoli
pravdivost či již doložený obecný důkaz D(c). Není to kandidát chyby.

## P0490–P0491: úloha15, bijekce, obor a příklad

Počty l,m,n jsou nezáporné celé. Do prvního řádku pišme pozice písmen a,
do druhého pozice b a do třetího pozice c. Řádky jsou striktně rostoucí
podle definice. Podmínka, že v každém prefixu #a≥#b≥#c, je ekvivalentní
tomu, že j-té a předchází j-tému b a j-té b předchází j-tému c,
kdykoli druhé z nich existuje. To je přesně striktní růst ve sloupcích.
Naopak z tableau dostaneme slovo jednoznačně určením řádku, který
obsahuje postupně1,…,l+m+n. Jde tedy o obousměrnou bijekci.

Jestliže l<m nebo m<n, selže již podmínka na celém slově a počet je0.
Pro l≥m≥n≥0 dosadíme do již dokázaného rozměrového vzorce posunuté
délky l+2,m+1,n. Tři Vandermondovy rozdíly dávají přesně

    (l+m+n)! (l−m+1)(l−n+2)(m−n+1) / ((l+2)!(m+1)!n!).

Rovnosti i nulové délky jsou povolené; nejde o přísné l>m>n.
Prázdný případ dává1. U vytištěného slova aabcabbcaca jsou pozice
a=(1,2,5,9,11), b=(3,6,7), c=(4,8,10), přesně tableau odpovědi608.
Každý sloupec roste a poslední počty jsou(5,3,3), takže je ověřen
také samotný příklad, nejen obecná formule.

## P0492: úloha18, polynomiální struktura

Pišme Δ(x)=∏_(i<j)(x_i−x_j) a

    G_m(x;y)=Σ_i x_i^m Δ(x_1,…,x_i+y,…,x_n), m≥0.

Při záměně dvou x se přejmenují sčítance a determinant změní znaménko.
G_m je tedy antisymetrický a dělitelný každým x_i−x_j, a tím jejich
součinem Δ. Podíl je symetrický v x a homogenní celkového stupně m
v x,y. Má proto tvar Σ_(k=0)^m b_k(x)y^k, kde b_k má stupeň m−k.
Současně je stupeň v y nejvýše n−1, protože tolik faktorů Δ se
změnilo při posunu jediné proměnné. Zejména b_k=0 pro k≥n i pro k>m.

Pro dočasně navzájem různá a nenulová x_i platí přesně

    Δ(x+y e_i)/Δ(x)=∏_(j≠i)(1+y/(x_i−x_j)).                (1)

Koeficient y^k tím dává uvedenou normalizovanou k-tou derivaci
na konci608. Po odvození se všechny identity rozšíří jako identity
polynomů i na shodná x_i; dělení nulou není předpokladem výsledku.

## P0493: seskupení k+1 členů a jeho obecný důkaz

V koeficientu y^k v(1) zvolíme pro každé i množinu k dalších indexů.
Po seskupení podle jejich sjednocení U, |U|=k+1, dostáváme

    b_k=Σ_(|U|=k+1) Σ_(i∈U) x_i^m / ∏_(j∈U,j≠i)(x_i−x_j).

Vnitřní součet je úplná homogenní symetrická funkce h_(m−k)(x_U),
s h_0=1 a h_d=0 pro d<0. Nejde pouze o odkaz na svazek1:
rozklad na jednoduché zlomky přímo dává

    Σ_(i∈U) 1/((1−x_i z)∏_(j∈U,j≠i)(x_i−x_j))
         = z^k / ∏_(i∈U)(1−x_i z).

Koeficient u pólu z=1/x_i je na obou stranách stejný; obě racionální
funkce mizí v nekonečnu. Nezávisle lze rovnost vynásobit jmenovateli
a dosadit k+1 různých hodnot1/x_i do polynomu stupně nejvýše k.
Z porovnání koeficientů z^m plyne požadovaný vztah. Nulové či shodné
hodnoty opět pokrývá polynomiální pokračování. V příkladu k=2 je U
trojice a,b,c, takže vznikají právě tři vytištěné zlomky na609.

## P0494: monomiální vzorec a oba příklady m=2,3

Každý monom stupně d=m−k s podporou j různých proměnných se objeví
v h_d(x_U) právě pro množiny U obsahující tuto podporu. Počet těchto
U je binom(n−j,k+1−j). Proto

    b_k=Σ_j binom(n−j,k+1−j)
              Σ_(p_1≥…≥p_j≥1, Σp_i=m−k) s(p_1,…,p_j).

To je přesně odpověď609. Zde s obsahuje každý různý monom právě
jednou, i při opakovaných exponentových částech; žádný další faktor
j! se nepřidává. Pro m=k je j=0 prázdná partition a s()=1, takže
b_m=binom(n,m+1). Pro ostatní nemožné indexy jsou součty prázdné.

Při m=2 tedy vyjde s(2)+(n−1)s(1)y+binom(n,3)y².
Při m=3 vyjde

    s(3)+((n−1)s(2)+s(1,1))y
        +binom(n−1,2)s(1)y²+binom(n,4)y³.

Oba vytištěné příklady jsou tak výslovně odvozené včetně koeficientu
s(1,1) a hranic n<3 či n<4. Pro m=0 dostáváme G_0=nΔ, také bez výjimky.

## P0495–P0496: oba generující tvary odpovědi18

Nechť e_r jsou elementární symetrické funkce a
D(z)=∏_(i=1)^n(1−x_i z)=Σ_r(−1)^r e_r z^r. Z P0493

    Σ_(m≥0)b_k z^m
       =z^k Σ_(|U|=k+1) 1/∏_(i∈U)(1−x_i z)
       =z^k Σ_r(−1)^r binom(n−r,k+1)e_r z^r / D(z).        (2)

Poslední rovnost má přímý kombinatorický důvod: po převedení na
společný jmenovatel zvolíme r indexů z doplňku U; každou r-tici
lze doplnit na U právě binom(n−r,k+1) způsoby. To ověřuje všechny
znaménkové a binomické koeficienty první racionální formule na609.

Vynásobíme(2) y^k a sečteme podle k. Identita

    Σ_(k≥0)binom(n−r,k+1)(yz)^k=((1+yz)^(n−r)−1)/(yz)

dává celý hledaný součet G_m jako koeficient z^m ve výrazu

    Δ(x)/(yz) ( ∏_i(1+z(y−x_i))/∏_i(1−z x_i) −1 ).

Čitatel rozdílu je dělitelný yz, takže je to dobře definovaná formální
řada i při y=0; po zkrácení tam dává Σ_i x_i^m. Žádné analytické
omezení na z ani kladnost x se nepředpokládá. Nové označení e_r
z errata2002 se používá místo původního a_r, význam se nemění.

## P0497: obecný determinant pro rozdíl dvou tvarů v poznámce19

Nechť λ=(λ_1≥…≥λ_m≥0), μ=(μ_1≥…≥μ_m≥0), μ_i≤λ_i,
N=Σ_i(λ_i−μ_i). Předpoklad, že μ je také tvar, je součástí
slov „two tableau shapes“; nejde o libovolné nesouvislé vyřezání.
Po přidávání buněk v pořadí štítků1,…,N dostáváme cestu od μ do λ,
jejíž každý prefix je opět partition. Je to bijekce: rostoucí řádky
a sloupce přesně vyžadují, aby levý a horní předchůdce už byly
v prefixu nebo v μ.

Posuňme souřadnice na a_i=μ_i+m−i a b_i=λ_i+m−i. Podmínka cesty
je nyní striktní pořadí všech souřadnic; každý krok přičte1 do
jediné souřadnice. Sečtěme se znaménkem všechny neomezené cesty
z permutovaných startů (a_(σ(1)),…,a_(σ(m))) do b. Pro danou σ
jich je N!/∏_i(b_i−a_(σ(i)))!, s konvencí1/r!=0 pro r<0.

Neplatné cesty párujeme podle první rovnosti dvou souřadnic.
Vyměníme jejich celé prefixy až do tohoto setkání. Po něm je cesta
beze změny; před ním je stále složena z kladných jednotkových kroků.
Vymění se dva starty, tedy znaménko. První setkání je stejné i po
výměně; před ním nebyly žádné rovnosti, takže tam nemůže vzniknout
jiná první kolize. Jde o involuci bez pevných bodů.

Cesta bez kolize musí začít ve správném striktním pořadí a, protože
neuspořádaný start nelze jednotkovými kroky převést do uspořádaného
konce b bez rovnosti souřadnic. Zůstanou tedy právě požadované cesty
z identity se znaménkem+. Výsledný počet je

    N! det_(i,j) (1/(λ_i−i−μ_j+j)!).                       (3)

Po transpozici matice je to přesně Feitova formule vytištěná na609.
Platí i N=0 a μ=λ. Její matematika je zde dokázána, nikoli pouze
převzata z bibliografického odkazu.

## P0498: úloha19, specializace odstranění dvou horních buněk

Nyní λ má celkem n≥2 buněk a λ_1≥2; μ=(2,0,…,0). Dvě chybějící
buňky se dají jednoznačně doplnit1,2; ostatní štítky se zvýší o2.
To dokazuje ekvivalenci obou znění úlohy, včetně pořadí ve sloupcích.

Položme L_i=λ_i+m−i. Po vyjmutí1/L_i! z řádků determinantu(3)
má jeho první sloupec klesající faktoriál L_i podtržené(m+1), další
sloupce mají stupně m−2,m−3,…,0. Pro obyčejné f(λ) by první sloupec
měl stupeň m−1. Označíme-li

    A=m(m+1)/2,
    B=(A²−m(m+1)(2m+1)/6)/2,

pak první polynom je L^(m+1)−A L^m+B L^(m−1)+nižší členy.
Nižší členy leží v rozpětí ostatních sloupců a determinant nemění.
Podíl alternantů pro první sloupec L^(m+1), L^m a L^(m−1) je
postupně h_2(L), h_1(L) a1. To plyne z kofaktorového rozvoje a
identity P0493 pro U={1,…,m}; je tím doložen i tento mezikrok.

Poměr upraveného determinantu k obyčejnému je tedy

    S=h_2(L)−A h_1(L)+B,
    počet=f(λ) S/(n(n−1)).                                (4)

Rozdíl faktoriálů(n−2)!/n! je podstatný: n zde znamená velikost
celého λ, nikoli počet buněk po odstranění.

## P0499: zjednodušení na řádky/sloupce a druhá identita odpovědi

Máme ΣL_i=n+m(m−1)/2 a h_2(L)=((ΣL_i)²+ΣL_i²)/2.
Po dosazení do(4) se koeficient lineárního n zruší, protože
m(m−1)/2−A+m=0. Konstantní část se také zruší; lze to ověřit
dosazením L=(m−1,…,0), kde klesající faktoriál prvního sloupce
je všude nula. Zůstává

    S=(n²+Σ_i λ_i²−2Σ_i iλ_i)/2.

Je-li λ'_j výška j-tého sloupce, dvojí sčítání buněk dává

    Σ_i iλ_i=Σ_j λ'_j(λ'_j+1)/2
             =(n+Σ_j (λ'_j)²)/2.

To je přesně doprovodná identita uvedená v odpovědi. Dosazením
do(4) dostáváme celý vytištěný symetrický výraz

    (1/2) f(λ) (1+(Σ_i λ_i²−Σ_j (λ'_j)²)/(n(n−1))).

Pro jediný řádek vrací f(λ), pro jediný sloupec a n≥2 vrací0,
jak musí být při požadavku1,2 v prvním řádku. Mimo n≥2 by zápis
s n(n−1) neměl význam; úloha ale vyžaduje odstranění dvou buněk.

## P0500: úloha20, obecný stromový součin

Jde o pevný konečný zakořeněný strom s rozlišenými vrcholy, nikoli
o počítání neoznačených stromů modulo automorfismy. Označme s_v velikost
podstromu vrcholu v. Pro jednovrcholový strom je tvrzení1=1!/1.
V libovolném rostoucím označení většího stromu musí kořen dostat1.
Mají-li jeho dětské podstromy velikosti n_1,…,n_r, lze jejich
množiny štítků vybrat multinomickým koeficientem
(n−1)!/∏ n_i!, a uvnitř nich použít indukční vzorec. Součin je

    ((n−1)!/∏ n_i!) ∏_(dětské T_i) (n_i!/∏_(v∈T_i)s_v)
      =(n−1)!/∏_(v≠kořen)s_v=n!/∏_v s_v.

Příslušné relativní pořadí libovolně zvolených štítků je jediné
přeznačení1,…,n_i, takže indukce nezávisí na jejich skutečných hodnotách.

## P0501: proč jsou zde minimové události opravdu nezávislé

Odpověď20 výslovně tvrdí nezávislost; samotný předchozí součin pro
průnik všech událostí by ji ještě nedokázal. Náhodné uniformní
označení lze generovat rekurzivně: zvolíme kořenový štítek rovnoměrně,
zbývající štítky uniformně rozdělíme na množiny dětských podstromů
a v každém nezávisle zvolíme uniformní označení. Každé celé označení
má pravděpodobnost

    (1/n) / ((n−1)!/∏ n_i!) × ∏(1/n_i!)=1/n!.

Hodnost kořene v jeho podstromu je tedy uniformní na1,…,n a nezávislá
na relativních pořadích potomků. Podmíněně na rozdělení štítků jsou
všechny vnitřní relativní hodnosti podle indukce nezávislé; jejich
rozdělení se navíc nemění s přidělenými množinami ani s hodností
kořene. Indukcí jsou proto všechny hodnosti r_v nezávislé a
r_v je uniformní na1,…,s_v. Událost „v je minimum svého podstromu“
je právě r_v=1, takže celá rodina těchto událostí je nezávislá.
Jejich pravděpodobnosti1/s_v skutečně lze násobit. Tím je oddělen
platný stromový argument od neplatné nezávislosti háčků obecného
tableau, již rozebrané v P0444.

## P0502: všechna čísla stromu a poznámka o inverzích

Z obrázku67 má kořen podstromy velikostí4,1,5. Levý4 má děti1 a2,
z nichž2 má jediný list. Pravý5 má děti3 a1, přičemž3 má dva listy.
Všech11 vytištěných velikostí je tedy správně a jejich součin je
11·4·5·2·3=1320. S opravou závorek je 11!/1320=30240=10·9·8·7·6.

Inverze stromového označení je dvojice předek–potomek s větším
štítkem u předka. Nulový počet takových dvojic je přesně požadovaný
růst po potomcích. Je-li strom cestou, pořadí vrcholů od kořene je
lineární a tyto dvojice jsou přesně obvyklé inverze permutace.
To ověřuje věcný obsah doprovodné poznámky, nikoli výsledky celé
citované práce Björnera–Wachse.

Historická spolupráce s Benderem, prvenství Feita a úplné bibliografické
údaje zde nebyly samostatně auditovány. Důkaz(3) ověřuje matematický
obsah Feitova odkazu; nepředstírá kontrolu jeho původního článku.
Další úloha21 a zbývající část odpovědí609 nejsou tímto uzavřeny.

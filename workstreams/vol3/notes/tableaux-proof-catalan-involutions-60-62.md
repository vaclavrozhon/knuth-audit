# Ballot cesty, stromy a involuce: konec60–62, úlohy7,16,25

Sazba71–73 a odpovědi607–608,611. Předchozí hook formula, bijekce
I/D a reverze se přebírají v jejich dokázaném rozsahu. Známá oprava
na61 mění poslední zakázaný vzor na a_i>a_k>a_j pro i<j<k;
používám toto aktualizované znění. Pět vrstev errat je ve
sources/tableaux-errata-review.json. Historické citace MacMahon,
Rotem, Rothe a tvrzení o „jednoduchosti“ vzorců se znovu neověřují.
Žádný početní běh ani nový nález.

## P0448–449: binární stromy, platné zásobníkové operace a vzor312

Zde jde o kořenové binární stromy s odlišeným levým a pravým
podstromem, z nichž každý může být prázdný. Kódujme je rekurzivně
D(T)=S D(L) X D(R), prázdný strom prázdným slovem. Má-li strom n
uzlů, slovo má n znaků S a n znaků X a v žádném prefixu nepřeváží X.
Naopak každé neprázdné takové slovo má jediný rozklad S u X v podle
prvního návratu rozdílu počtů k nule; u,v mají tutéž prefixovou
vlastnost. To rekurzivně vrací právě L,R. Jde tedy o bijekci, ne
jen shodnou rekurenci počtů.

Pro vstup1,…,n znamenají S vložení dalšího vstupu a X odebrání
vrcholu zásobníku. Stejná prefixová podmínka je přesně podmínkou,
že neodebíráme z prázdného zásobníku; na konci jsou všechny prvky
vydány. Výstupní permutace určuje postup jednoznačně: je-li další
požadovaný prvek nahoře, musí se odebrat; nebyl-li dosud načten,
musí se vložit všechny dosud nepřečtené hodnoty až po něj a pak
se odebere. Vložit ještě větší hodnotu před jeho vydáním nelze,
protože by mu překážela. Je-li už načten a není nahoře, výstup
vytvořit nelze. Získáváme bijekci platných slov a dosažitelných permutací.

Takové výstupy jsou právě permutace bez vzoru312, tedy bez
a_i>a_k>a_j pro i<j<k. Kdyby vzor existoval, při vydání a_i už byly
a_j<a_k vloženy a dosud nebyly vydány. a_k leží nad a_j, takže
jej nelze vydat až po a_j. Opačně, pokud uvedený vynucený postup
selže na požadované hodnotě v, leží nad ní nevydaná w>v. w musela
být vložena při přípravě dřívějšího výstupu u≥w; rovnost není
možná, protože w ještě zůstává v zásobníku. Výstup tedy obsahuje
u,v,w v tomto pořadí s u>w>v, zakázaný vzor. Bez vzoru postup
neselže. Tím je doložen i opravený poslední matematický výrok61.

## P0450–451: dvouřádkové tableaux a ballot počty

Pro slovo s n znaky S a m≤n znaky X dejme indexy S vzestupně do
prvního řádku a indexy X do druhého. Označme je s_j a x_j. Sloupcová
podmínka je s_j<x_j pro všechna1≤j≤m. Přesně to říká, že při
každém j-tém X už před ním bylo alespoň j znaků S, ekvivalentně
každý prefix má #S≥#X. Oba převody jsou jednoznačné, protože řádky
jsou vzestupné. Pro SSSXXSSXXSXX dostaneme horní řádek
1,2,3,6,7,10 a dolní4,5,8,9,11,12, přesně(37).

Pro(n,n) jsou háčky v prvním řádku n+1,n,…,2 a ve druhém n,…,1,
takže Theorem H dává(2n)!/((n+1)!n!), Catalanovo číslo. Předchozí
bijekce se stromy a zásobníkem identifikuje tentýž počet s oběma
třídami objektů, včetně prázdného případu.

Obecně z již dokázaného(34) při m=2 řádcích vychází pro tvar(n,m)
(zde písmeno m opět znamená délku druhého řádku)

    f(n,m)=(n+m)!(n−m+1)/((n+1)!m!).

To je slabá ballot podmínka výše. Chceme-li striktní náskok S
v každém neprázdném prefixu neprázdného slova, musí n>m a odstranění prvního S
vede na slabou podmínku pro(n−1,m). Počet je proto
(n+m−1)!(n−m)/(n!m!). Obě obvyklé konvence ballot problému jsou
tak rozlišeny; při n=m>0 striktní varianta na konci nemůže nastat.
Prázdné slovo splňuje obě prefixové podmínky vacuózně a počítá se jednou.

## P0452–454: rozdělení obdélníku, délky podposloupností a vzor321

V tableau A tvaru(n,n) buňky s hodnotami≤n tvoří ideál λ=(a,b),
a≥b, a+b=n: menší levý/horní soused takové buňky musí být také≤n.
Zbytek má v horním řádku n−a=b pravých buněk, v dolním n−b=a.
Otočení o180° z něj tedy udělá levě zarovnaný tvar(a,b), stejný
jako u vyříznutého P. Otočení obrátí směry nerovností a relabelování
x→2n+1−x je obrátí podruhé. Výsledek Q je tableau na1,…,n.

Naopak pro libovolnou dvojici P,Q stejného nejvýše dvouřádkového
tvaru(a,b), a+b=n, se Q otočí a relabeluje zpět do přesného
doplňku P v obdélníku. Uvnitř obou částí nerovnosti platí. Každá
sousední hrana překračující hranici jde z ideálu P do doplňku,
tedy z hodnoty≤n do hodnoty>n. Nemůže tak vzniknout opačná
nerovnost. Obě konstrukce jsou inverzní, včetně b=0 a n=0.

V příkladu(37) s n=6 je P=1236/45. Otočený doplněk má po změně
13−x řádky(1,2,4,5),(3,6), přesně Q v(38). Jsou tak ověřeny
všechny tři zobrazené mezistavy, nejen konečný tvar.

Úloha7: invariant minimálních konců P0403 už dokázal, že počet
sloupců P(w) je maximální délka rostoucí podposloupnosti w.
Rostoucí podposloupnost obráceného slova odpovídá po obrácení
pořadí přesně klesající podposloupnosti původního slova, se stejnou
délkou. P0427 dává P(w^R)=P(w)^T, takže počet řádků je maximální
délka klesající podposloupnosti. Tím jsou doloženy obě části úlohy7
i jejich použití na61.

Permutace bez klesající trojice, tj. vzoru321, proto odpovídají
přesně dvojicím tableaux s nejvýše dvěma řádky. Výše uvedená
obdélníková bijekce je spočítá jako f(n,n), tedy stejné Catalanovo
číslo jako binární stromy. Tvrzení o konkrétní další přímé bijekci
v Rotemově článku se přebírá pouze jako výslovně neověřená historie;
uvedená matematická rovnost počtů má vlastní důkaz.

## P0455–457: orientovaný graf, obecný poset a úloha16

V(39) je přesně15 vrcholů v řádcích6,4,4,1 a hrany spojují každé
dva sousedy vpravo nebo dole. Rostoucí označení podél těchto hran
je tedy přesně tableau, protože transitivita doplní zbytek každého
řádku/sloupce. Pro obecný konečný acyklický orientovaný graf dává
rostoucí označení1,…,n totéž co topologické pořadí vrcholů; opačný
převod každému vrcholu přidělí jeho pozici. Topologické pořadí
existuje: je vrchol bez předchůdce (jinak bychom sledováním
předchůdců v konečném grafu dostali cyklus), odstraníme jej a
indukčně pokračujeme.

Počet však nemusí dělit n!. Konkrétní čtyřvrcholový poset s hranami
a<c, b<c, b<d má5 lineárních rozšíření. Začíná-li a, zbývá nejprve
b a pak c,d v obou pořadích:2. Začíná-li b, zbylé a,c,d mají jen
podmínku a<c, tedy3 možnosti. Celkem5 nedělí24. Tím je doloženo
přesné omezení zmínky62: obecný vzorec n! děleno celočíselným
součinem háčků nemůže platit pro všechny posety. Netvrdíme, že
neexistuje žádná obecná formule nebo algoritmus.

Pro graf(39) a úlohu16 jsou háčky po řádcích
(9,7,6,5,2,1), (6,4,3,2), (5,3,2,1), (1).
Jejich součin má faktorizaci2^7·3^6·5^2·7. Naproti tomu15! má
2^11·3^6·5^3·7^2·11·13; rozdíly exponentů dávají
2^4·5·7·11·13=80080, přesně odpověď608. Výpočet je konečná
faktorizace podle již ověřených délek, nikoli enumerace pořadí.

## P0458–0459: involuce, všechna vytištěná čísla a počet podle cyklů

Rovnost t_n s počtem involucí je P0405. Rozdělení podle toho, zda
je n pevným bodem nebo má partnera j<n, a rekurenci
t_n=t_(n−1)+(n−1)t_(n−2), t_0=t_1=1, přebírám z P0414; není
potřeba znovu dokazovat cyklickou charakterizaci.

Postupné nové konečné dosazení dává všechny hodnoty ze62:

    t_2=1+1=2,        t_3=2+2=4,
    t_4=4+6=10,       t_5=10+16=26,
    t_6=26+50=76,     t_7=76+156=232,
    t_8=232+532=764,  t_9=764+1856=2620,
    t_10=2620+6876=9496.

Při přesně k transpozicích vybereme2k nepěvných prvků binom(n,2k)
způsoby. Jejich pořadí v k označených dvojicích má(2k)! možností,
ale každá dvojice se dá otočit2 způsoby, takže se dělí2^k.
Nakonec odstraníme označení dvojic dělením k!. Počet je tedy

    t_n(k)=n!/((n−2k)!2^k k!),   0≤k≤floor(n/2),

a součet přes k je(41). Prázdný případ má jediný člen1. Výběr
pevných bodů v textu má stejný binomický koeficient díky doplňku.

## P0460–0462: Hermitův zápis a celá odpověď25

Normalizace Hermitových polynomů H_n je ověřena v primárním zdroji
[NIST DLMF18.12.15](https://dlmf.nist.gov/18.12.E15):
exp(2xz−z²)=Σ_n H_n(x)z^n/n!. Rozvinutí obou exponenciál dává
vlastním porovnáním koeficientů polynomiální identitu

    H_n(x)=n! Σ_(k=0)^floor(n/2) (-1)^k(2x)^(n−2k)/(k!(n−2k)!).

Proto platí i pro komplexní x; nejde o neodůvodněnou aplikaci
integrálního vzorce pro reálné x. Po dosazení x=−i/sqrt(2) a
vynásobení i^n2^(−n/2) se každý koeficient změní na
n!/(2^k k!(n−2k)!), protože
i^n(−i)^(n−2k)(−1)^k=1. To je právě t_n(k), a tedy celý uvedený
Hermitův výraz. Byla zvolena H_n normalizace, ne jiná běžná varianta.

Pro samotnou úlohu25 stačí(41): po zavedení r=n−2k dostaneme

    Σ_n t_n z^n/n! = Σ_(r,k≥0) z^(r+2k)/(r!2^k k!)
                   = exp(z)exp(z²/2).

Každý formální koeficient používá jen konečný počet dvojic, takže
záměna součtů nepotřebuje dodatečnou analytickou podmínku.

Obecnější poznámka odpovědi611 se dokáže stejně: pro c_s cyklů
délky s je počet permutací n!/∏_s(s^(c_s)c_s!), kde Σs c_s=n.
Činitel s odstraňuje volbu počátku každého cyklu a c_s! odstraňuje
pořadí cyklů stejné délky. Pro libovolnou množinu kladných délek S
je proto EGF

    ∏_(s∈S) Σ_(c≥0) (z^s/s)^c/c! = exp(Σ_(s∈S) z^s/s).

Při S={1,…,k} jde přesně o tištěnou první generalizaci; S={1,2}
dává involuce. I pro nekonečné S má každý koeficient konečně mnoho
relevantních délek, proto jde o platnou formální identitu. S prázdné
dává pouze prázdnou permutaci. Tím je doložena celá matematika
odpovědi25, nikoli jen původní zvláštní případ.

Další neuzavřený souvislý blok začíná na63: poloha maxima součtu,
uniformní Stirlingův rozvoj, odříznutí ocasů a součtová asymptotika.

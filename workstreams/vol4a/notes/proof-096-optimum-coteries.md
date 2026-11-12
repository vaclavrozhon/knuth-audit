# Celá úloha 111: optimální dostupnost a všech sedm regulárních případů

7. listopadu 2026, X0123, P1166–P1179. Zadání p93/file110 a celé
odpovědi p554–555/file571–572 zobrazeny. Známé opravy jsou zapracovány.
Žádný matematický program, LP ani nový census.

Máme n≥1 jednotek se vzájemně nezávislými stavy. Pozitivní arita patří
k zadání používajícímu p_1 i x_1; nulární coterie nebyly nově zavedeny.
Přesně přebíráme P0585/P0586 z proof-033 (monotónnost dostupnosti a
pravděpodobnostní interpretace), párové optimum z proof-034, charakterizaci
coteries z proof-065, sedm tříd z proof-079, Chowovu větu z proof-084
a pokrytí/regularitu z proof-094/095. Tyto hotové důkazy se neopakují.

## (a) Optimální self-duální funkce pro libovolný kladný počet jednotek

Pro stav x označme jeho pravděpodobnost P(x). Self-duální funkce musí
z každé dvojice {x,¬x} vybrat právě jeden pravdivý stav. Stejný přesný
párový argument jako v proof-034 platí pro všech 2^(n−1) dvojic:
maximum dostupnosti je Σ_dvojice max(P(x),P(¬x)). Rovné pravděpodobnosti
dovolují obě volby; při striktní nerovnosti je volba v dané dvojici nutná.

V doméně 1>p_1≥…≥p_n≥1/2 položme r_i=p_i/(1−p_i) a
w_i=log r_i. Potom r_1≥…≥r_n≥1 a w_1≥…≥w_n≥0. Podmínka
P(x)≥P(¬x) je přesně

    ∏r_i^(x_i) ≥ sqrt(∏r_i),

čili H(x)=Σw_i x_i−(Σw_i)/2≥0. Vyberme

    g(x)=1, když H(x)>0 nebo když H(x)=0 a x_1=1.

Komplement změní H na −H a při rovnosti obrátí x_1. Funkce je tedy
self-duální a v každé dvojici vybírá pravděpodobnější stav; je optimální
mezi všemi self-duálními funkcemi. To přesně vysvětluje vytištěné ≥
s nahrazením za > pro x_1=0.

Zůstává regularita i při rovnostech, kterou pouhé napsání prahu neřeší.
Pro x≤y v majorizaci platí H(x)≤H(y) podle důkazu 110(b). Pokud
g(x)=1 díky H(x)>0, pak H(y)>0. Pokud H(x)=0 a x_1=1, je
y_1≥x_1=1 z první prefixové nerovnosti; při H(y)=0 proto rozhodne
stejná kladná tie volba. Ve všech případech g(y)=1. Funkce je regulární,
tedy monotónní, a podle již uzavřené charakterizace odpovídá coterie.
Takže maximum mezi všemi self-duálními funkcemi je v této doméně
skutečně dosaženo také v požadované třídě coteries.

Pro všechny p_i=1/2 je H identicky nula a vybrané g=x_1 je stále
regulární, self-duální a má dostupnost 1/2. Optimum nemusí být jediné.

## (b) Proč stačí minimální pravdivé body; přesné zacházení se shodami

Nechť f je regulární a self-duální. Pod každým x s f(x)=1 existuje
minimální pravdivý bod y≤x: vybereme minimum konečné neprázdné množiny
pravdivých bodů pod x. Jeho bezprostřední předchůdci jsou nepravdiví.
Pokud jsme u všech těchto y ověřili g(y)=1, regularita g dá g(x)=1
pro všechna pravdivá x. Tedy f≤g; self-dualita obou pak vynutí f=g:
případ f(x)=0,g(x)=1 by na komplementu porušil f≤g. Je to platný
dostačující certifikát optimálnosti přesně podle vytištěného důkazu.

Pevně zvolená tie konvence g=x_1 na H=0 však není tvrzením, že jiná
optimální f neexistuje. Úplný test, který přijme i další optimální volby
při shodě, je H(y)≥0 na všech minimálních pravdivých y. Pak pro každé
pravdivé x platí H(x)≥H(y)≥0, takže f vždy vybírá alespoň stejně
pravděpodobný stav. Je tedy optimální párově. Opačně H(y)<0 u některého
pravdivého bodu dává v této dvojici striktní ztrátu a f není optimální,
protože (a) globálního párového maxima dosahuje coterie. To dokazuje
i přesný rozhodovací smysl úlohy bez umělého požadavku jedinečnosti.

Je-li zadán seznam t minimálních bodů, test potřebuje t součtů délky n,
tedy O(nt) aritmetických operací po přípravě vah. To nepřipisuje stejnou
cenu generování seznamu ani přesnému vyhodnocování libovolných reálných
vstupů. Součinová forma dovoluje místo logaritmů přesná porovnání
racionálních součinů, jsou-li vstupní pravděpodobnosti racionální.

## Všech sedm regulárních self-duálních funkcí pro n=5, bez nového censu

Proof-079 již dokázal, že všech 81 monotónních self-duálních funkcí
na pěti označených proměnných tvoří přesně sedm permutačních tříd
a že všechny jsou prahové. Každá třída má regulární reprezentaci:
seřaďme její nezáporné váhy a použijme 110(b).

V regulární funkci je s_1≥…≥s_5. Párový argument 110(c) totiž
funguje přímo: vstup 01 se změnou na 10 posune nahoru v majorizaci.
V jedné permutační třídě jsou vektory Σ jen permutacemi téhož
multisetu a N je stejné. Seřazený vektor Σ je jediný; Chowova věta
proto připouští v každé třídě nejvýše jednu regulární funkci. Celkem
jich je přesně sedm. Tento závěr nepoužívá nové prohledávání 81 funkcí.

Následující tabulka dává každý vytištěný seznam minimálních bodů.
Prime podpory jsou po zvoleném přejmenování přesně dříve doložené
rodiny; v posledním sloupci je jejich redukce pod majorizací.

| Váhy a práh | Všechny prime podpory | Minimální body v majorizaci |
|---|---|---|
| (1,0,0,0,0), 1 | 1 | 10000 |
| (3,1,1,1,1), 4 | 12,13,14,15,2345 | 01111; 10001 |
| (2,1,1,1,0), 3 | 12,13,14,234 | 01110; 10010 |
| (3,2,2,1,1), 5 | 12,13,145,234,235 | 01101; 10011; 10100 |
| (1,1,1,0,0), 2 | 12,13,23 | 01100 |
| (2,2,1,1,1), 4 | 12,134,135,145,234,235,245 | 01011; 11000 |
| (1,1,1,1,1), 3 | všech deset trojic | 00111 |

Úplnost posledního sloupce: každý pravdivý vstup obsahuje nějakou prime
podporu a je proto nad ní také v majorizaci. V druhém řádku je 15 pod
všemi ostatními uvedenými dvojicemi a 2345 s ní nesrovnatelná. Ve třetím
je minimální dvojice 14 a s ní nesrovnatelná trojice 234. Ve čtvrtém
13≤12 a 235≤234, zatímco 13,145,235 jsou navzájem nesrovnatelné.
V pátém je 23 pod oběma ostatními dvojicemi. V šestém je 245 pod
všemi uvedenými trojicemi a nesrovnatelná s 12. V posledním je 345
pod každou trojicí. První řádek je jediná podpora. Všechny tyto relace
plynou také z pořadí pozic jedniček v proof-094.

Tím je ověřeno všech dvanáct vytištěných minimálních bodů, nikoli jen
číslo sedm. Nejvýše dvanáct testů g na těchto bodech stačí nalézt jednu
optimální z uvedených funkcí; optimální regulární g z (a) mezi nimi je.

## (c) Monotónnost optimální dostupnosti a smíšené pravděpodobnosti

Píšeme G(p)=max_f F_f(p), kde maximum běží přes konečnou neprázdnou
množinu monotónních self-duálních funkcí na n≥1 proměnných. Každý
polynom dostupnosti F_f je na [0,1]^n neklesající podle přesného
P0585 z proof-033. Maximum těchto funkcí je rovněž neklesající.

Předpokládejme po seřazení, že p_1≥…≥p_r≥1/2>p_(r+1)≥…≥p_n,
kde 1≤r<n. Nahradíme špatné pravděpodobnosti hodnotou 1/2 a dostaneme
p'. Monotónnost dává G(p)≤G(p'). Optimální funkce g pro p' z (a)
má u posledních n−r souřadnic nulové w_i. Ani tie pravidlo x_1 tyto
souřadnice nepoužívá, protože r≥1. Funkce na nich tedy nezávisí a

    F_g(p)=F_g(p')=G(p').

Současně F_g(p)≤G(p), takže všechny tři hodnoty jsou stejné. Ignorování
všech jednotek s p_i<1/2 tedy opravdu dosahuje optima. Nejde jen o
horní mez po změně pravděpodobností. Zde se používá správné g odvozené
ze zvýšeného vektoru p', jak už upřesňuje historické F0 erratum.

## Potřebná uniformní protínající se mez: úplný krátký kruhový důkaz

Nechť A je protínající se rodina m-prvkových podmnožin n-prvkové
množiny, 1≤m≤n/2. V pevně zvoleném orientovaném kruhovém pořadí
je mezi n cyklickými intervaly délky m nejvýše m členů A.

Pokud žádný není, je závěr hotov. Jinak po otočení jeden vybraný
interval končí v n a obsahuje n−m+1,…,n. Intervaly končící v
m,m+1,…,n−m jsou s ním disjunktní, a proto nemohou být vybrány.
Z ostatních, kromě konce n, vytvoříme m−1 párů konců

    i a n−m+i,       i=1,…,m−1.

Interval končící v i obsahuje n−m+i+1,…,n a 1,…,i; jeho partner
obsahuje n−2m+i+1,…,n−m+i. Jelikož n≥2m, jsou tyto dva intervaly
disjunktní. Z každého páru tedy patří A nejvýše jeden. Spolu s vybraným
intervalem končícím v n to dává nejvýše m.

Existuje (n−1)! orientovaných kruhových pořadí rozlišených prvků.
Pevná m-množina je intervalem právě v m!(n−m)! z nich: stáhneme ji
na jeden blok, uspořádáme n−m+1 bloků cyklicky a jejích m prvků uvnitř.
Proto dvojím počítáním

    |A| m!(n−m)! ≤ m(n−1)!,
    |A| ≤ C(n−1,m−1).

Tím je příslušná Erdősova–Koova–Radova mez pro všechny potřebné
parametry doložena přímo. Není zde neověřeným externím vstupem ani
pouhým odkazem na pozdější úlohu. Pro m=0 ji nepoužíváme.

## Všechny pravděpodobnosti pod polovinou: rozvinutí vynechaného závěru

Pro monotónní self-duální f nechť c_m počítá pravdivé vstupy s m
jedničkami. Jejich podpory jsou protínající se: disjunktní pravdivé
A,B by dávaly A⊆¬B, ale f(A)=1 a f(¬B)=0. Self-dualita navíc
dává c_m+c_(n−m)=C(n,m), včetně prostřední vrstvy. To je správná
příčina rovnosti po erratu z 22.1.2012; nesouvisí s úlohou 70.

Pro projekci x_1 jsou počty d_m=C(n−1,m−1), s d_0=0. Pro
m<n/2 máme c_m≤d_m z právě dokázané uniformní meze; při m=0
je c_0=d_0=0, protože monotónní self-duální f(0)=0. Pro n sudé
je c_(n/2)=C(n,n/2)/2=d_(n/2) už ze self-duality.

Nechť 0<p≤1/2 a q=1−p. Pro každé m<n/2 je
A=p^m q^(n−m)≥B=p^(n−m)q^m. Příspěvek páru vrstev do dostupnosti je

    c_m A+c_(n−m)B=C(n,m)B+c_m(A−B)
                    ≤C(n,m)B+d_m(A−B).

Pravá strana je právě příspěvek téhož páru pro projekci. Prostřední
vrstva je shodná. Sečtením všech vrstev proto dostáváme

    F_f(p,…,p) ≤ Σ_m C(n−1,m−1)p^m q^(n−m)=p.

Nyní pokud p_1≥…≥p_n a p_1<1/2, již dokázaná monotónnost dává

    G(p_1,…,p_n) ≤ G(p_1,…,p_1) ≤ p_1.

Projekce x_1 dosahuje p_1, tedy je optimální coterie přesně podle
odpovědi. Je to skutečné maximum mezi všemi coteries, nikoli jen
mezi prahovými či regulárními reprezentacemi.

## Hraniční pravděpodobnosti a rozsah

Kniha v pomocném rozboru (c) předpokládá 0<p_i<1. Samotný výsledek
lze uzavřít i pro endpoints: má-li nejlepší jednotka p_1=1, projekce
dosahuje absolutní meze 1. Je-li p_1<1 a aspoň jedna jednotka má
p_i≥1/2, ignorování ostatních používá pouze konečné odds dobrých jednotek,
i kdyby špatné měly p_i=0. Jsou-li všechny pod 1/2, vrstvový odhad
platí při p_1=0 spojitostí konečných polynomů; také přímo jsou všechny
jednotky nefunkční a každá monotónní self-duální funkce má f(0)=0.
Při n=1 je jedinou takovou funkcí x_1 a všechny větve dávají dostupnost
p_1. Rovnosti p_i=1/2 jsou již zahrnuty v dobré skupině a tie důkazu.

## Errata, bibliografie a celé stránky

Prohlédnuty all4a-pre, all4a, err4a, all4f0 a err4f0. Známé změny:
22.7.2011 „set“→„choose“ při volbě v ties; 22.1.2012 odkaz na 70
nahrazen self-dualitou; F0 14.2.2009 upřesňuje odvození ze zvýšených
pravděpodobností a 23.9.2008 opravuje F na F_k. Vše zohledněno,
žádný nový nález ani karta. Nulární doménové potíže starších jinak
formulovaných úloh 64–66 pod P0863 se tím neprohlašují za vyřešené.

[Primární SIAM záznam](https://epubs.siam.org/doi/abs/10.1137/S0895480100371110)
potvrzuje Makino–Kameda, název, ročník 14 (2001), p381–407.
[Amirův autorský seznam](https://www.cs.jhu.edu/~yairamir/archive.html)
potvrzuje Amir–Wool, Information Processing Letters 65 (1998), p223–228.
Historická priorita a širší algoritmické výsledky těchto článků nebyly
nově auditovány; žádný jejich neověřený výsledek není vstupem důkazu výše.

Úplný matematický obsah p93/file110 nyní má argument: Fig. 8 a části
109(b–h) v proof-094, celé 110 v proof-095 a celé 111 zde. Totéž platí
pro p554/file571: 108 v proof-093, 109 i trojúhelník v proof-094,
110 v proof-095 a začátek 111(a,b) zde, včetně pokračování jeho důkazu.
Bibliografické výjimky Goto/Winder/Lindström zůstávají zvlášť evidované.
P555/file572 zůstává partial, protože začíná dosud neuzavřená 112.

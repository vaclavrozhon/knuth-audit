# Tableaux: celé úlohy22–24, odpovědi a pozdější dodatky

Zadání67–68/file78–79, odpovědi610–611/file621–622. Sazba zobrazená
v images/tableaux-file-079.png, -621.png a -622.png. Známé změny:
2006 v odpovědi23 „row k from the bottom“ a součet od n=0;
2007 přejmenování A_n na E_n a sjednocení názvu Euler numbers;
2020 označení up-down permutations a výklad každého řádku trojúhelníku;
2024 přesnější úvod odpovědi22. Tyto změny jsou zohledněny, nejsou nálezy.
Bibliografické změny André/Seidel nepřebírají roli matematického důkazu.

## P0509: úloha22, skutečná doména a doplnění nul

Použijme λ pro tvar a N pro velikost abecedy1,…,N. Pokud počet
kladných řádků převyšuje N, první sloupec nelze vyplnit striktně
rostoucími štítky. Jinak lze doplnit nulové řádky do přesně N řádků.
V dalším píšeme m=N, λ_1≥…≥λ_m≥0. Počet označme F_m(λ).
Prázdný tvar má počet1. Prázdná abeceda dovoluje jen prázdný tvar.
Toto pořadí rozlišení domény je i smyslem opravy z22.9.2024.

## P0510: nezávislé vyhodnocení kandidátního determinantu

Položme L_j=λ_j+m−j a

    D_m(λ)=det_(r=m−1,…,0; j=1,…,m) binom(L_j,r).

Polynom binom(X,r) má stupeň r a vedoucí koeficient1/r!. Přičtením
násobků nižších řádků lze postupně zrušit všechny nižší mocniny;
vznikne Vandermondův determinant s řádky mocnin m−1,…,0. Tedy

    D_m(λ)=Δ(L_1,…,L_m)/∏_(r=0)^(m−1)r!.                 (1)

Pořadí řádků i klesajících L zachovává kladnou orientaci Δ.
Vzorec(1) je čistě algebraický, nezávislý na dosud dokazované
enumeraci. Zejména je D invariantní při stejném posunu všech λ_j.

## P0511: odstranění plných sloupců, v obou směrech

Je-li λ_m>0, prvních λ_m sloupců má výšku m. Jejich striktně rostoucí
štítky z1,…,m musí být právě1,…,m; řádek i je v nich vyplněn i.
Po odstranění těchto sloupců zbývá tvar λ−λ_m(1,…,1).
Naopak do každého jeho vyplnění lze tyto sloupce vrátit: každá
zbývající buňka v řádku i má hodnotu≥i díky i−1 buňkám nad ní,
takže i na začátku řádku neporuší slabý růst. Počty F jsou stejné.

Kandidát D je při tomto posunu stejný podle(1). Pro důkaz F=D
proto opravdu stačí případ λ_m=0; tento přechod nepředpokládá
rovnost F=D předem.

## P0512: rozklad podle všech výskytů největšího štítku

Odstraněním všech m z vyplnění λ s λ_m=0 zbude tvar κ na abecedě
1,…,m−1. V řádku j tvořila m koncovou souvislou část. Nad jakoukoli
buňkou nižšího řádku nesmí m zůstat, takže přesně platí

    λ_(j+1)≤κ_j≤λ_j, 1≤j<m.

Naopak každé takové κ a každé jeho vyplnění lze rozšířit připsáním m
na odstraněné konce. Interlacing zaručuje, že žádné m není nad jinou
buňkou a nad každým přidaným m je menší hodnota. Je tedy splněna
sloupková přísnost i řádková slabost. Rozsahy jednotlivých κ_j jsou
nezávislé a samy zaručují κ_j≥κ_(j+1). Dostáváme přesně rekurenci

    F_m(λ)=Σ_(λ_(j+1)≤κ_j≤λ_j) F_(m−1)(κ).                (2)

## P0513: všechny kroky determinantového součtu v odpovědi610

Indukční základ m=1 je F_1(λ_1)=1=D_1(λ_1). Po dosazení
indukčního determinantu do(2) lze díky multilinearitě sloupců
provést každý součet zvlášť. Pro r=0,…,m−2 jeho položka je

    Σ_(κ=λ_(j+1))^λ_j binom(κ+m−1−j,r)
       =binom(L_j,r+1)−binom(L_(j+1),r+1).

To je teleskopická Pascalova identita, včetně obou krajních mezí.
Z původní matice D_m nyní odečtěme sloupec j+1 od sloupce j pro
j=1,…,m−1 v tomto pořadí. Determinant zůstane stejný. Poslední
řádek se stane(0,…,0,1) a poslední sloupec je při L_m=0 rovněž
(0,…,0,1). Rozvoj podle této jedničky má znaménko+ a zbývající
matice je právě předchozí součet, s r+1=m−1,…,1.
Tím je F_m=D_m dokázáno;(1) dává i poslední vzorec odpovědi610.
Nezůstává nezdůvodněno její „which is the desired answer“.

## P0514: všechny tři příklady z horní části68

- Sloupec délky r vyžaduje výběr r různých štítků a jejich jediné
  vzestupné pořadí, tedy binom(N,r).
- Jediný řádek délky r odpovídá slabé kompozici r do N násobností,
  tedy binom(N+r−1,r), pro N≥1; prázdná abeceda byla vyřízena výše.
- Pro tvar(2,2), N≥2, se v poměru Vandermondů liší jen páry s prvním
  či druhým řádkem. Jejich součiny jsou
  N(N+1)/6 a N(N−1)/2, ostatní páry mají poměr1.
  Výsledek je N²(N²−1)/12=(1/3)binom(N+1,2)binom(N,2),
  přesně jak je vytištěno. Pro N<2 je počet0 na obou stranách.

Rovnosti mezi štítky v řádku jsou povolené, v sloupci nikoli;
tato odlišnost se v celé rekurenci nezaměňuje.

## P0515: úloha23 a up-down permutace v aktualizovaném znění

Čtěme cikcak buňky od levého dolního konce, střídavě doprava a nahoru.
Růst řádků dává a_1<a_2; následující pohyb nahoru dává a_2>a_3.
Dále se vztahy střídají. Dostáváme bijekci se slovy
a_1<a_2>a_3<a_4>… na různých štítcích1,…,n, tedy přesně up-down
permutacemi z dodatku2020. Každé slovo určuje všechny buňky a všechny
vodorovné/svislé relace; žádná další dvojice ve tvaru není skrytá.
V terminologii Runs jsou to běhy délky2, s případným posledním
singletonem, takže souhlasí i úvodní odkaz odpovědi23.

Počty dále značíme aktuálním E_n; E_0=E_1=1. Původní A_n zde
není Eulerovo číslo sestupů, ale starší označení téhož počtu.

## P0516: největší prvek a všechny části rekurence

Pro n≥2 musí n stát na sudé pozici2k, tedy na pravém konci k-tého
řádku odspodu, 1≤k≤floor(n/2). Ani první buňka, ani lichý koncový
vrchol nemůže být maximum, protože má většího souseda. Po odebrání n
zůstane vlevo up-down slovo délky2k−1 a vpravo stejného typu délky
n−2k. Obě sousední nerovnosti proti n jsou automatické. Výběr množiny
levých štítků a obě relativní permutace proto dávají bijekci a

    E_n=Σ_k binom(n−1,2k−1) E_(2k−1) E_(n−2k).             (3)

To vysvětluje opravu „from the bottom“ a pokrývá i prázdnou pravou
část při sudém n.

## P0517–P0518: celý přechod ke g, oddé části a řešení ODE

Nechť g(z)=Σ_(n≥0)E_n z^n/n! a h(z)=(g(z)−g(−z))/2.
Po posunu n→n+1 v(3) je pro n≥1 koeficient h(z)g(z) právě E_(n+1).
Proto

    h g = Σ_(n≥1) E_(n+1) z^n/n!
        = (Σ_(n≥0) E_(n+1) z^n/n!)−1 = g'−1.             (4)

V prostředním součtu s vypsaným−1 je tedy skutečně n≥0, jak opravuje
erratum2006; nesčítají se dvě odečtené konstanty.

Pišme g=h+k, kde k je sudá část. V(4) oddé a sudé části dávají
h'=1+h² a k'=hk, s h(0)=0, k(0)=1. Tyto počáteční podmínky určují
formální řady jednoznačně koeficient po koeficientu.
Řešení jsou h=tan z a k=sec z, protože splňují stejné derivace
a hodnoty v0. Rovněž

    sec z+tan z=(1+sin z)/cos z=tan(z/2+π/4)

v okolí0; tím je ověřen i poslední trigonometrický tvar odpovědi.
Tento argument nevyžaduje konvergenci obecné kombinatorické řady
před jejím určením.

## P0519: aktuální názvosloví a Bernoulliho formule

V aktuálním znění jsou všechny E_n nezáporná Eulerova up-down čísla;
liché E_(2r−1) jsou tangent numbers T_(2r−1). Přebíráme již
doložený převod tanh/tan a Bernoulliho řady P0289–P0290:
pro n=2r−1 dává přesně

    T_(2r−1)=(−1)^(r−1) 4^r(4^r−1)B_(2r)/(2r).

Změna konvence B_1 roku2021 se sudých B_(2r) nedotýká.
Původní tvrzení o absolutních hodnotách klasických sudých Eulerových
čísel odpovídá převodu sech(iz)=sec z; nezaměňuje se s nynějším
nezáporným E_n pro všechny indexy.

## P0520: skutečný význam trojúhelníku, včetně dodatku2020

Označme R_(n,j) počet up-down permutací délky n končících j.
Odstraníme poslední prvek a přeznačíme zbývající štítky pořadím.
Pro sudé n je poslední krok vzhůru, takže poslední hodnota prefixu
musí být<j. Pro liché n≥3 je krok dolů a po přeznačení má poslední
hodnota prefixu hodnost≥j. Tento postup je vratný, a tedy

    R_(n,j)=Σ_(i<j) R_(n−1,i),       n sudé;
    R_(n,j)=Σ_(i≥j) R_(n−1,i),       n liché.

Se základem R_(1,1)=1 jsou to přesně střídavé prefixové a suffixové
součty s nulou na příslušném konci. Každý řádek tak opravdu ukazuje
počty zakončení1,…,n, jak doplňuje erratum29.5.2020; součet řádku je E_n.

## P0521: každé vytištěné číslo trojúhelníku a počáteční posloupnosti

Výše uvedené součty dávají postupně tyto celé řádky:

    1
    0 1
    1 1 0
    0 1 2 2
    5 5 4 2 0
    0 5 10 14 16 16
    61 61 56 46 32 16 0
    0 61 122 178 224 256 272 272

To pokrývá všechna čísla tabulky611. Pro ověření posledního tištěného
E_9 stačí další suffixový řádek
1385,1385,1324,1202,1024,800,544,272,0, se součtem7936.
Součty předchozích řádků a E_0=1 jsou přesně
1,1,1,2,5,16,61,272,1385,7936. Jde o jeden ruční průchod touto
malou tabulkou, nikoli opakování starého programu či enumeraci permutací.

## P0522: úloha24, doména a převod q na partition

Nechť n≥1,m≥0 a t jsou celá čísla. Nejprve m≥n−1; označme

    M=m−n+1, L=nM, d=n(n−1)/2, r=t−d.

V součtu úlohy24 zmizí každá n-tice s opakovaným q kvůli Δ².
Zbytek je symetrický, takže jej lze omezit na q_1>…>q_n a vynásobit n!.
Položme λ_i=q_i−(n−i). Přísné q dávají slabě klesající λ_i≥0
a q_1≤m znamená λ_1≤M. Je to bijekce s partitions λ uvnitř
obdélníku R=(M^n), přičemž |λ|=r. Zde vzniká přesně posun t−d,
nikoli nezdůvodněná změna sumace.

## P0523: doplněk v obdélníku a Vandermondova identita nápovědy

Doplněk po otočení180° má tvar
μ=(M−λ_n,…,M−λ_1). Jeho posunuté délky jsou
m−q_n,m−q_(n−1),…,m−q_1. Záměna pořadí a změna znamének všech
párových rozdílů se vyruší, takže jejich Δ je přesně Δ(q).
To dokazuje také nápovědu s libovolnou konstantou komplementace.

Rozměrový vzorec pro oba tvary tedy dává

    f(λ)=r! Δ(q)/∏q_i!,
    f(μ)=(L−r)! Δ(q)/∏(m−q_i)!,

a odtud
    ∏binom(m,q_i) Δ(q)²=(m!)^n f(λ)f(μ)/(r!(L−r)!).        (5)

## P0524: úplná bijekce rozdělení obdélníkového tableau

Ve standardním tableau obdélníku R tvoří štítky1,…,r nějaký tvar λ.
Zbytek R\λ otočíme180° a každý štítek a nahradíme L+1−a;
tím dostaneme běžné tableau tvaru μ na1,…,L−r. Otočení i změna
štítků současně obrátí obě nerovnosti, takže jsou řádky a sloupce
opět rostoucí.

Obráceně libovolná dvojice tableaux λ,μ rekonstruuje jediné tableau R.
Přes rozhraní nemůže vzniknout obrácená nerovnost: λ je severozápadní
podtvar a všechny jeho štítky jsou menší než všechny štítky doplňku.
Proto pro každé0≤r≤L platí přesně

    Σ_(λ⊆R, |λ|=r) f(λ)f(μ)=f(R).                         (6)

Není to předpoklad rovnoměrnosti náhodného tvaru; jde o celou bijekci.

## P0525: vyhodnocení součtu a všechny faktory pravé strany

Z(5),(6) je levá strana úlohy

    n! binom(L,r) (m!)^n f(R)/L!.

Pro obdélník je
f(R)/L!=Δ(m,m−1,…,m−n+1)/∏_(j=0)^(n−1)(m−j)!.
Jeho Vandermonde je D=Δ(n−1,…,0)=∏_(j=0)^(n−1)j!.
Tedy

    (m!)^n f(R)/L!
       =D (m!)^n/∏(m−j)!
       =D² ∏_(j=0)^(n−1)binom(m,j).

Po dosazení L=nm−(n²−n) a r=t−(n²−n)/2 je to přesně celá
pravá strana zadání, včetně n!, druhé mocniny Δ a všech binomických
koeficientů. Odpověď24 v knize není vypsána; výše jsou dokázány
všechny tři kroky nápovědy.

## P0526: všechny hraniční a nulové případy úlohy24

Pro r<0 nebo r>L neexistuje příslušná partition a binom(L,r)=0,
takže obě strany mizí. Pro m=n−1 má obdélník šířku0; jediná možná
množina q je{0,…,n−1}, tedy t=d, a prázdná bijekce(6) má hodnotu1.
Pro n=1 jde přímo o binom(m,t)=binom(m,t).

Je-li m<n−1, nelze vybrat n různých čísel z0,…,m, takže levá strana
je0. Pravá obsahuje faktor binom(m,n−1)=0. Ostatní binomický
koeficient má případně záporný horní index; při běžné definici
binom(a,b)=[z^b](1+z)^a pro celé a a b≥0, s hodnotou0 pro b<0,
je konečný a součin také0. Hlavní kombinatorický důkaz tento
záporný rozměr nepoužívá. Pro n=0 se obě strany zvlášť rovnají1
při t=0 a0 jinak, s prázdnými součiny a determinanty.

Historická bibliografie Littlewood/André/Seidel a publikované tabulky
nebyly samostatně ověřovány; uvedená matematika, malé hodnoty a nový
výklad trojúhelníku mají vlastní argumenty. Úlohy25 a26 už jsou
doložené dříve;27 a další na stejné straně tímto blokem uzavřené nejsou.

# §5.2.1-42: první a druhý průchod

2026-11-07,105/file116 a627/file638 zobrazeny. P0864–0870.
Úplný druhý odhad platí s absolutní O-konstantou; chybějící mocnina N
v zadání je známá oprava2000. Pomocná neomezená8N/(gh) je candidate/low
C0024 kvůli možnému implicitnímu režimu N≥gh, nikoli chyba výsledku42(a).
Pro důkaz se nepoužila enumerace. K, převod přesunů na inverse a uzavřená
asymptotika náhodného2-uspořádaného seznamu z11–15 se přebírají.

## První průchod — P0864

Pro N=qh+r,0≤r<h má r tříd délku q+1, ostatní q. Každá neuspořádaná
dvojice klíčů uvnitř třídy je před prvním průchodem inversí s pravděpodobností1/2;
přesunů při vkládání je přesně počet inversí. Proto

    E B_h=[h q(q−1)+2rq]/4
         =N²/(4h)−N/4+r(h−r)/(4h)=N²/(4h)+O(N).

Pro h≤N je poslední člen≤h/16≤N/16. Pro h>N neproběhne přesun a
N²/(4h)≤N/4. Tedy chyba je O(N) uniformně; nevyžaduje dělitelnost.

## Dvě h-třídy a CRT — P0865–P0866

Po h-třídění vezměme dvě různé třídy b<c v1,…,h. Jejich fyzické
propletení A₀,B₀,A₁,B₁,… má délky lišící se nejvýše o1. Každé rozdělení
relativních hodností mezi třídy je stejně pravděpodobné: původní vstup je
rovnoměrná permutace a třídění odstranilo jen pořadí uvnitř tříd.
Proto jde přesně o náhodný2-uspořádaný seznam délky M, kde
M=2N/h+O(1). Převzatý, již odvozený výsledek14 dává

    E I_bc=sqrt(π/128) M^(3/2)+O(M)
          =(sqrt(π)/4)(N/h)^(3/2)+O(N/h+1).                 (1)

Změna argumentu M o konstantu mění M^(3/2) jen o O(sqrt(N/h+1)),
což je v uvedené chybě. Delší třída je první, jak vyžaduje propletení.

Položme L=gh. V každé třídě b modulo h existuje g kanonických fází
x∈{1,…,L}. Fáze x vybírá K_x,K_(x+L),…; různé fáze rozdělí celou
h-třídu. Pro dvě fáze x,y z různých h-tříd definujme G(x,y) jako počet
inversí v jejich fyzickém propletení. To je přesně knižní g(x,y): dva
součty přes j<k a diagonální r(x,y), jejíž pořadí určuje min(x,y).
Součty obsahují jen existující indexy. Obě vybrané třídy mají délky
lišící se nejvýše o1, nejdelší má ceil(N/L) prvků.

Každá inverse mezi úplnými h-třídami patří právě jedné dvojici fází,
takže **deterministicky**

    Σ_(x≡b mod h, y≡c mod h, 1≤x,y≤L) G(x,y)=I_bc.         (2)

Pro g-třídu a má díky gcd(h,g)=1 každá h-třída jedinou fázi
x≡b(mod h), x≡a(mod g),1≤x≤L. To je přesný CRT důvod, proč každá z
binom(h,2) dvojic přispěje do každé z g tříd jedním G(x,y).
Knižní příklad je dosazen správně: h=12,g=5,a=1,b=3,c=7 dává
x=51,y=31;51≡3(mod12),31≡7(mod12) a oba≡1(mod5).

## Fázový odhad bez ztracených konců — P0867

Pro dvě propletené rostoucí vybrané třídy A_i,B_j, jejichž fáze jsou x,y,
nechť s_i je počet B_j<A_i. Položme δ=[x>y]. Před pozicí A_i leží
přesně i+δ prvků druhé třídy. Počet inversí obsahujících A_i je tedy

    |i+δ−s_i|,

protože podle znaménka jsou buď některé větší B před A_i, nebo menší B
za ním. Součet přes A dává G. Stejná formule s prohozenými A,B dává G
z opačné strany. Platí i pro prázdnou třídu a pro jeden koncový prvek
navíc: fyzické propletení garantuje správný počet předchozích B.

Nyní změňme jen fázi B, zachovávajíce její h-třídu. Menší hodnoty v celé
rostoucí h-třídě tvoří prefix délky s. Počty prvků tohoto prefixu v jeho
g fázích jsou floor(s/g) nebo ceil(s/g), takže nové s_i se od starého
liší nejvýše o1. Také δ se mění nejvýše o1. Proto se G změní nejvýše
o2 za každý prvek pevné A, tedy o2ceil(N/L). Změníme-li poté fázi A,
použijeme symetrickou formuli s pevnou B a dostaneme stejnou mez.
Pro libovolné dvě kanonické dvojice fází tudíž

    |G(x,y)−G(x',y')| ≤4ceil(N/(gh)) ≤4(N/(gh)+1).          (3)

Tento argument vyřizuje i neúplné poslední bloky. Knižní posuny
x'=x+ph,y'=y+qh mezi kanonickými fázemi mají |p|,|q|<g. Bodové
nerovnosti v odpovědi jsou také správné pro existující indexy:
K_(j+ph−gh)≤K_j≤K_(j+ph+gh) a obdobně pro k, protože |p|≤g a
příslušná h-třída roste. Negativní nebo chybějící koncové indexy však
nelze bez dalšího sčítat jako původní prvky; právě ty zohledňuje(3).

Je-li N≥gh, ceil(N/(gh))≤2N/(gh) a(3) dokazuje přesně knižní

    |G(x,y)−G(x',y')|≤8N/(gh).                            (4)

Diagonálních členů r je nejvýše ceil(N/(gh))<N/(gh)+1. To souhlasí
se známou opravou2000; původní r<N/(gh) se nepřebírá.

## Druhý průchod, hlavní režim — P0868

Předpokládejme N≥gh. Z(2),(4) se každé G od průměru všech g² fází
liší o O(N/(gh)), a totéž platí pro očekávání. Podle(1) tedy

    E G(x,y)=(sqrt(π)/4)g^(−2)h^(−3/2)N^(3/2)
             +O(N/(gh)).                                 (5)

Chyba O((N/h+1)/g²) z(1) se do ní vejde, protože N≥gh.
Sčítání přes g výstupních tříd a binom(h,2) vstupních dvojic nyní dává

    E B_g=(sqrt(π)/8)(sqrt(h)−1/sqrt(h))N^(3/2)/g+O(hN).

Nejde o předpoklad nezávislosti jednotlivých dvojic; použita je pouze
linearita očekávání. Tím je zdůvodněn každý faktor h,g,2 i mocnina N.
Známé erratum na105 opravuje N/g na N^(3/2)/g.

## Zbytek domény — P0869

Pokud gh>N, samotný počet dvojic uvnitř g-tříd dává deterministicky
B_g≤N(ceil(N/g)−1)/2≤N²/(2g)<hN/2 pro g≤N; pro g>N je B_g=0.
Také hlavní člen je O(hN): pro h≤N použijeme g>N/h, čímž
sqrt(h)N^(3/2)/(g hN)<sqrt(h/N)≤1; pro h>N je tento poměr
sqrt(N/h)/g≤1. Oba členy lze tedy zahrnout do chyby O(hN).
To dokazuje tentýž odhad uniformně i v režimu, kde jednotlivá(4)
bez doplňku obecně neplatí.

Pro h=1 je vstup po prvním průchodu seřazen a hlavní koeficient je0.
Pro g=1 nejsou fázové rozdíly a argument redukuje na již prokázaný
součet dvojic h-tříd. Konečně N=0,1 má nulové náklady; asymptotická
formule se používá pro N≥1. Opačné pořadí2 a3 z odpovědi25 rovněž
splňuje gcd podmínku; obecný důkaz nepotřebuje h>g.

## Neomezený pomocný výrok — P0870 partial / C0024

Kniha před(4) neuvádí N≥gh. Pro h=18,g=17,N=36 a vstup
K₁=18,K₁₈=1,K_i=i jinde je první průchod již hotový: v každé18-třídě
jsou dvě hodnoty ve vzestupném pořadí. Pro x=1,y=18,p=q=1 je
G(1,18)=1, G(19,36)=0, kdežto8N/(gh)=16/17. Obě dvojice jsou
kanonické a vždy leží ve společné17-třídě; všechny indexy existují.
Jde tedy o přesný rozpor **neomezené** formulace(4).

Protože v asymptotickém důkazu lze N≥gh předpokládat a zbývající režim
vyřešit jako výše, zůstává nález candidate/low: chybí výslovný rozsah,
nikoli důkaz nesprávného konečného odhadu. Detail a pět vrstev errat jsou
v `notes/V3-C0024-phase-shift-bound-scope.md` a příslušném sources JSON.

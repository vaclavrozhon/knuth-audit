# §4.5.4: dodatek AKS z 28. dubna 2005

Stav 3. listopadu 2026: **C0153 potvrzuje záměnu `z` za `a`.**
Standardní věta AKS a elementární polynomiální čas jsou níže doloženy
vlastním úplným argumentem. Knižní silnější formulace bez dvou
předběžných podmínek zůstává **partial / C0155 candidate**; nebyl
nalezen její důkaz ani protipříklad. Časové výsledky dalších metod
jsou odlišeny jako externí věty ověřené v původních pramenech.

## 1. Značení a přesná věta, kterou dokazujeme

Nechť `n>=2` je celé číslo a `ell=lg n` je dvojkový logaritmus.
Řád `ord_r(n)` je nejmenší kladné `d` s `n^d=1 mod r`; předpokládá
`gcd(n,r)=1`. Kongruence modulo `(n,z^r-1)` znamená rovnost polynomů
po redukci koeficientů modulo `n` a exponentů modulo `r`.
Není to pouze rovnost hodnot pro nějaká celá `z`.

**Standardní kritérium.** Nechť `1<r<n`, `gcd(n,r)=1`
a `ord_r(n)>ell^2`. Předpokládejme navíc, že `n` není netriviální
mocnina, tedy není `u^v` pro celá `u>1,v>1`, a že nemá prvočinitele
`<=r`. Potom je `n` prvočíslo právě tehdy, když

```
(z+a)^n = z^n+a mod (n,z^r-1)
pro každé celé 0<=a<=floor(sqrt(r)*ell).                       (1)
```

Prvočísla vyhovují díky binomické a Fermatově větě. Pro opačnou
implikaci budeme porovnávat dvě meze pro počet prvků grupy `G`:
součinů několika lineárních polynomů vyhodnocených v kořenu jednotky.
Tuto grupu i její dvě meze definují následující dva oddíly.

## 2. Kořen jednotky a horní mez

Zvolme prvočinitele `p` čísla `n`. V konečném rozšíření tělesa `F_p`
existuje prvek `alpha` přesného řádu `r`: vezměme kořen nerozložitelného
činitele r-tého cyklotomického polynomu. Platí `p>r`, zejména `p` nedělí
`r`, takže takové kořeny jsou různé a mají opravdu řád `r`.

Nechť `A=floor(sqrt(r)*ell)`. Označme `H` množinu všech součinů
polynomů `z+a` s `0<=a<=A`, včetně prázdného součinu 1. Obrazy těchto
součinů při `z=alpha` tvoří konečnou multiplikativní grupu `G`.
Žádný generátor není nula: pokud `alpha+a=0`, pak (1) modulo `p`
dává `alpha^n+a=0`, tedy `alpha^n=alpha`, což by znamenalo
`n=1 mod r`, v rozporu s předpokládaným řádem.

Pracujme nejprve modulo `(p,z^r-1)`. Pro každý `f` z `H` platí
`f(z)^n=f(z^n)`. Totéž platí s exponentem `p`, protože v charakteristice
`p` je `p`-tá mocnina součtu součtem `p`-tých mocnin.
Platí to také pro exponent `n/p`: obě strany po umocnění na `p`
jsou podle (1) stejné. Toto umocnění je v daném okruhu prosté,
neboť na koeficientech je identita a indexy monomů permutuje násobením
`p mod r`. Z `gcd(p,r)=1` plyne, že je to permutace.

Vlastnost `f(z)^m=f(z^m)` je uzavřena na součiny exponentů.
Dosazení `z -> z^u` zachovává kongruenci, protože `z^r-1` dělí
`z^(ur)-1`. Proto platí pro všechny exponenty

```
m = (n/p)^i p^j,  i,j>=0.                                    (2)
```

Nechť `R` je podgrupa invertibilních zbytků modulo `r` generovaná
`n/p` a `p` a nechť `t=|R|`. Obsahuje i `n`, takže
`ell^2 < t <= phi(r) < r`, kde `phi(r)` je počet invertibilních zbytků.

Předpokládejme, že `n` není mocnina `p`. Čísla (2) pro
`0<=i,j<=floor(sqrt(t))` jsou pak navzájem různá: jiný prvočinitel
`n` určuje `i` a následně prvočinitel `p` určuje `j`.
Je jich více než `t`, takže dvě, `u!=v`, mají stejný zbytek modulo `r`.
Pro každý prvek `g=f(alpha)` grupy `G` tím dostáváme `g^u=g^v`.
Grupa je podgrupou multiplikativní grupy konečného tělesa, tedy je
cyklická; dosazením jejího generátoru plyne `|G|` dělí `|u-v|`.
Obě čísla jsou nejvýše `n^floor(sqrt(t))`, a tudíž

```
|G| <= |u-v| <= n^floor(sqrt(t))-1 <= n^sqrt(t)-1.              (3)
```

## 3. Dolní mez a rozpor

Dva různé polynomy `f,g` z `H` stupně menšího než `t` nemohou mít
stejný obraz v `G`. Kdyby `f(alpha)=g(alpha)`, pak pro všechny
exponenty (2) platí `f(alpha^m)=g(alpha^m)`. Tyto exponenty dávají
všechny zbytky z `R`, tedy `t` různých kořenů polynomu `f-g`.
Nenulový polynom stupně menšího než `t` nemá nad tělesem tolik kořenů.
Tento argument se týká právě součinů z `H`, pro něž byla vlastnost
exponentů dokázána, nikoli libovolných polynomů se stejnými obrazy.

Položme `B=floor(sqrt(t)*ell)`. Máme `B<t` a `B<=A<r<p`.
Polynomy `z,z+1,...,z+B` jsou proto různé monické lineární činitele
nad `F_p`. Součiny všech jejich vlastních podmnožin jsou díky
jednoznačnosti rozkladu různé polynomy, stupně nejvýše `B<t`.
Předchozí odstavec je pošle na různé prvky `G`. Tedy

```
|G| >= 2^(B+1)-1 > 2^(sqrt(t)*ell)-1 = n^sqrt(t)-1,            (4)
```

ve sporu s (3). Proto `n` musí být mocninou `p`. Předběžné vyloučení
netriviálních mocnin nyní dává `n=p` a dokončuje důkaz kritéria.

## 4. Elementární existence malého modulu

Pro časovou mez stačí vlastní poněkud slabší, ale uniformní odhad:
pro `L=ceil(lg n)` existuje vhodné `r<=4L^5`. Nejprve pomocné lemma:

```
D(M)=lcm(1,...,M) >= 2^(M-1),  M>=1.                         (5)
```

Důkaz: `D(M)=M*lcm{binom(M-1,j):0<=j<M}`. Pro prvočíslo `p`
položme `e=floor(log_p M)` a `a=v_p(M)`, kde `v_p` je exponent
prvočísla v rozkladu. Největší `p`-adická valuace v uvedeném řádku
binomických koeficientů je `e-a`. Při odčítání `j` od `M-1` v základu
`p` nemůže půjčka vzniknout pod pozicí `a`, protože tam jsou samé
číslice `p-1`, a nad pozicí `e-1` již další půjčka nevznikne.
Volba `j=p^e-p^a` dosáhne všech `e-a` půjček. Počet půjček je valuace
binomického koeficientu, jak plyne také odečtením Legendreových vzorců
pro valuace tří faktoriálů. Tím je dokázána lcm identita. Největší
koeficient je alespoň průměr `2^(M-1)/M`, což dává (5).

Pro `n>=3`, tedy `L>=2`, položme `M=4L^5` a `v=floor(lg M)`.
Předpokládejme, že žádné `r<=M` nesoudělné s `n` nemá řád větší
než `L^2`. Každá prvočíselná mocnina `q<=M`, nesoudělná s `n`,
pak dělí některé `n^j-1`, `1<=j<=L^2`. Každá zbývající prvočíselná
mocnina do `M` dělí `n^v`. Proto

```
D(M) | n^v * product_{j=1}^{L^2}(n^j-1).
```

Dvojkový logaritmus pravé strany je menší než

```
L*(v + L^2(L^2+1)/2)
<= (1/2)L^5 + (1/2)L^3 + 5L^2 + 2L
<= (11/8)L^5 < 4L^5-1 = M-1.
```

Zde `v<=2+5lg L<=2+5L`; prostřední nerovnost plyne vydělením
`L^5` a použitím `L>=2`. To odporuje (5). Pro `n=2` stačí `r=3`.
Argument výslovně ošetřuje i moduly sdílející prvočinitele s `n`.
Nevyužívá tvrzení, že po jediném dělení `s/gcd(s,n)` už musí být
výsledek nesoudělný s `n`.

## 5. Bitové časové meze

Zápis `soft-O` zde potlačuje pevné mocniny logaritmu argumentu.
Použijeme standardní rychlé násobení `k`-bitových celých čísel
v `soft-O(k)` bitových operacích.

Koeficienty součinu dvou polynomů stupně menšího než `r`, s koeficienty
menšími než `n`, jsou menší než `r n^2`. Zabalíme je tedy do číslic
základu `2^b`, kde `b=2L+ceil(lg r)+1`. Jedno celočíselné násobení
obnoví celý součin bez přenosu mezi těmito číslicemi. Redukce modulo
`z^r-1` skládá koeficienty se stejným indexem modulo `r` a redukce
modulo `n` je také rychlá. Jedno polynomiální násobení stojí
`soft-O(r(L+log r))`, pro `r=O(L^5)` tedy `soft-O(rL)`.

Binární umocňování vyžaduje `O(L)` takových násobení a testuje se
`O(sqrt(r)L)` parametrů. Celkem

```
soft-O(r^(3/2) L^3) = soft-O(L^(21/2)) = O(L^11).             (6)
```

Vyhledání `r` přímým testem prvních `L^2` mocnin pro každé `r`
stojí `soft-O(rL^2)`, menší člen. Vyloučení mocnin lze provést
binárním hledáním celých kořenů pro exponenty `2,...,L`, s hrubou
mezí `soft-O(L^3)`. Dělení malými čísly do `r` také nepřekročí (6).
Je-li `n<=r`, předběžné dělení již rozhodne; velká polynomiální
smyčka se nepouští.

Skutečné logaritmické hranice není třeba při implementaci počítat
do problematicky blízkého celého čísla. Lze je bezpečně nahradit
`L=ceil(lg n)`, požadovat řád větší než `L^2` a použít
`ceil(sqrt(r)L)` testů. Důkaz i asymptotika zůstávají stejné.

Knižní dolní exponent 6 odpovídá tomuto obecnému postupu s hustou
reprezentací polynomů a úplnou smyčkou: `r>ell^2` a počet
zpracovávaných bitů v jeho násobeních dává základní měřítko
`r^(3/2)ell^3`. Není to dolní mez pro všechny algoritmy prvočíselnosti,
ani tvrzení o čase při včasném odmítnutí konkrétního složeného vstupu.

## 6. Co zůstává z vynechaných předpokladů

**Podmínka `r<n` je pro samotné polynomiální kritérium zbytečná.**
Pokud `r>=n`, polynom `(z+1)^n-z^n-1` má stupeň menší než `r`,
takže redukce modulo `z^r-1` nemůže skrýt žádný jeho koeficient.
Pro složené `n` zvolme prvočinitele `p` s `p^e` přesně dělícím `n`.
Koeficient `binom(n,p)` má valuaci `e-1`: činitelé `n-1,...,n-p+1`
a `(p-1)!` jsou jednotky modulo `p`. Nedělí jej tedy `p^e`.
Test s `a=1` odmítne. Toto odstraňuje jednu původní pochybnost.

Je-li `p^2|n` a `p-1<=A`, pak dosazení `z=1`, `a=p-1` do (1)
dává `p^n=p mod n`, nemožné modulo `p^2`. Dosazení je zde legitimní,
protože `z^r-1` v jedničce mizí. Tím odpadnou i malé opakované faktory.

Nadále není vyřešeno vypuštění testu netriviálních mocnin a malých
prvočinitelů v celém obecném rozsahu. Důkaz oddílů 2–3 používá
`p>r` pro různost lineárních činitelů a vyloučení mocnin v závěru.
Pouhá absence protipříkladu ani toto místo v důkazu nejsou důkazem,
že Knuthova silnější formulace je chybná. **C0155 je kandidát.**

## 7. Přesný konečný experiment

[Validátor](../verify_primality_aks.py) záměrně vynechává oba předtesty
a přímo zkouší (1), po opravě `z/a`. Pro každý vstup bere nejmenší
`r` nesoudělné s `n` s řádem větším než `(lg n)^2`.
Zaokrouhlení `(lg n)^2` a `sqrt(r)lg n` certifikuje intervalová
aritmetika Arb; nejde o strojové desetinné odhady. FLINT počítá
polynomiální mocniny přesně, i při složeném modulu.

Všechny vstupy `2<=n<=2048` byly správně rozlišeny: 309 prvočísel
a 1738 složených čísel, dohromady 30 859 polynomiálních testů.
Pro `n<=127` je všech 1095 provedených kongruencí nezávisle ověřeno
přímým binomickým rozvojem s celočíselnými koeficienty. U složených
čísel stačí uložený první odmítající parametr; další nejsou potřeba.

Druhý checkpoint testuje 1215 čísel `p^2`, kde `47<=p<=10000`
je prvočíslo. Menší čtverce již patří do prvního bloku.
Všechny byly odmítnuty už při `a=1`. Dva případy byly navíc nezávisle
přepočteny vlastní cyklickou konvolucí a binárním umocňováním:

| n | r | řád n modulo r | konstantní koeficient levé strany při a=1 |
|---:|---:|---:|---:|
| 1093^2 = 1194649 | 821 | 410 | 478735 |
| 3511^2 = 12327121 | 1123 | 561 | 7422255 |

Pravá strana má v obou případech konstantní koeficient 1.
Přitom běžné dosazení `z=1` chybu neodhalí: `2^n=2 mod n`.
Třetí malý checkpoint ověřuje lcm identitu (5) do `M=257`.
Výsledky a přesné zbytky jsou v [JSON](../results/primality-aks.json)
a dvou CSV. Z nich nevyvozujeme žádnou nekonečnou klasifikaci.

Hlavní běh: PID 1273861, session 25030, limit 300 s, návrat 0,
124.782 s. Samostatný nový checkpoint `lcm_lemma` prošel za 0.367 s
s limitem 30 s; PID nebyl zachycen. Předchozí dva bloky se neopakovaly.

## 8. Prameny a další časová tvrzení

Originál [AKS 2004](https://pages.cs.wisc.edu/~cs812-1/AKS.pdf),
Annals 160, 781–793, byl vizuálně přečten celý. Sken nemá použitelnou
textovou vrstvu. Analytická Fouvryho věta pro lepší exponent 15/2
je externí výsledek; naše (6) ji nepotřebuje.
[Granville 2005](https://cr.yp.to/bib/2005/granville-easy.pdf),
Bull. AMS 42, 3–38: vizuálně 4, 15–20 a 24–29. Jeho výklad potvrzuje
standardní hypotézy, polynomiální kongruenci i uvedené algoritmické směry.
Zbytek článku, zejména analytické podklady, není označen jako plně auditovaný.

[Lenstra–Pomerance](https://math.dartmouth.edu/~carlp/aksfinal.pdf),
autorská verze 21. 12. 2018, publikována JEMS 21 (2019), 1229–1269:
str. 1–3 čteny, 1–2 a 9–11 vizuálně. Theorem 1 dává deterministickou
mez `L^6(2+log L)^c`, tedy `O(L^(6+epsilon))` pro každé pevné
`epsilon>0`. Algorithm 3.3 skutečně používá obecnější okruh vytvořený
pomocí Gaussových period. Úplná konstrukce a její analytické odhady
zůstávají výslovně externími výsledky; 49stránkový důkaz nepřepisujeme
jako vlastní nově ověřenou větu. Odkaz dodatku na tehdejší výsledek
podpírá už Granville 2005 a citace AKS na str. 793, nejde o anachronismus.

[Bernstein, verze 3. 12. 2004](https://cr.yp.to/primetests/quartic-20041203.pdf):
vizuálně str. 1–4 a 8. Přečten celý důkaz jednoduššího Theorem 2.1,
definice certifikátu a tvrzení o času; úplný optimalizovaný Theorem 3.2
a analytická konstrukce nejsou nově reprodukovány. Článek potvrzuje
čas `L^(4+o(1))` pro nalezení a ověření certifikátu prvočísla,
i vztah k Berrizbeitiovi, Chengovi, Mihailescuovi a Avanzimu.
Lenstra–Pomerance str. 2 uvádí výslovně očekávanou časovou mez.

Z očekávaného času `L^(4+o(1))` plyne Markovovou nerovností, že pro
každé pevné `epsilon>0` je pravděpodobnost překročení `L^(4+epsilon)`
nejvýše `L^(-epsilon+o(1))`, tedy jde k nule. To je přesný význam
vysoké pravděpodobnosti rychlého nalezení důkazu; hotový certifikát
je rigorózní. Nejde o bezchybnou pevnou časovou záruku pro každý los.
Původní články všech čtyř dalších autorů nebyly jednotlivě auditovány.

Všechny vrstvy errat zkontrolovány; přesné hashe a rozsah vizuálního
čtení jsou v [metadatech](../sources/primality-aks.json).
Původní odstavce prvního dotisku o APR a Adlemanovi–Huangovi zůstávají
samostatnou otevřenou historickou položkou, i když je dodatek nahrazuje.

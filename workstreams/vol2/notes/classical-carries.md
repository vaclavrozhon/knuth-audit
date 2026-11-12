# §4.3.1: komplementy, rozdělení přenosů a úlohy42/43

Dokončeno2.11.2026. Originály276–278,284,629–630 vizuálně přečteny.
Zde b>=2 znamená celočíselný základ a všechny náhodné vstupy jsou
navzájem nezávislé a rovnoměrné v uvedeném konečném rozsahu. K je počet
jednotkových přenosů při běžném sčítání zprava doleva, včetně případného
přenosu z nejvyšší číslice. Tento blok doplňuje dřívější kontrolu střední
hodnoty o celé rozdělení a rozptyl.

## Komplementová reprezentace na str.276

Pro D-bitový vzor je interpretace v dvojkovém doplňku buď jeho nezáporná
hodnota x, nebo x-2^D. Obě jsou kongruentní modulo2^D. Proto spodních D
bitů součtu nezávisí na signed/unsigned interpretaci. Podmínky přetečení
se liší: unsigned přetečení znamená překročení2^D-1, signed přetečení
opuštění intervalu[-2^(D-1),2^(D-1)-1]. Tyto dvě události nelze zaměnit.

Při použití w-bitových signed slov a b=2^(w-1) se nižší slova vejdou
do nezáporné poloviny, nejvyšší slovo nese znaménko. Tištěný příklad
s w8 má hodnotu

```
(-33)*128^2 +126*128 +107
 = -2^21 +95*2^14 +126*2^7 +107 = -524437.
```

Znaménkový bit se započítá jen jednou s vahou-2^21. Jestliže procesor
poskytuje plný unsigned součin a unsigned přenos, lze podle textu místo
b=2^(w-1) použít b=2^w. To je podmíněné tvrzení o dostupných instrukcích,
nikoli předpoklad, že takové instrukce má libovolný počítač.

Jedničkový doplněk má modul2^D-1 a dvě reprezentace nuly. Přenos za
nejvyšší bit má proto stejnou váhu jako nejnižší bit; přičte se zpět
a případně dále propaguje. Toto vysvětluje upozornění knihy. Pro násobení
a dělení je platná redukce na magnitudy a závěrečné znaménko. Při převodu
nejmenšího záporného dvojkového doplňku do téže signed reprezentace je
nutné umožnit další nejvyšší místo; jinak jeho kladná magnituda do stejné
šířky nepadne. Text neposkytuje rutinu s pevnou šířkou, jejíž chování by
na tomto extrému bylo předepsáno.

## Generující funkce a rozptyl přenosů

Nechť p_(n,k) je pravděpodobnost K=k a současně přenosu z nejvyšší
pozice, q_(n,k) stejná pravděpodobnost bez posledního přenosu. Pro n0
je p nulové a q_(0,0)=1. Pravděpodobnost přenosu z další číslice je
`alpha=(b+1)/(2b)` při vstupním přenosu1 a `beta=(b-1)/(2b)` při
vstupním přenosu0. Obě hodnoty vzniknou sečtením trojúhelníkové oblasti
mezi b^2 dvojicemi číslic. Tím se přímo odvodí rekurentní vztahy na277:

```
p_(n+1,k+1) = alpha*p_(n,k) + beta*q_(n,k),
q_(n+1,k)   = beta*p_(n,k) + alpha*q_(n,k).
```

Proměnná z zaznamenává počet přenosů, t počet číslic. Zaveďme formální
mocninné řady `P=sum p_(n,k)z^k t^n`, obdobně Q, a G=P+Q.
Tyto vztahy dávají P=zt(alpha P+beta Q), Q=1+t(beta P+alpha Q).
Vyřešením dvou lineárních rovnic dostaneme tištěný racionální výraz

```
G(z,t) = (b-zt)/d(z,t),
d(z,t) = b-(b+1)(1+z)t/2+zt^2.
```

Značení d zde nahrazuje tištěné p(z,t), aby se nepletlo s p_(n,k).
Dosazení z1 dává1/(1-t), tedy normalizaci všech pravděpodobností.
Koeficient G_n(z) u t^n je pravděpodobnostní polynom K. Derivace
G'_n(1) je E K, druhá derivace G''_n(1) je E[K(K-1)]. Všechny dvě
vytištěné derivace G podle z a oba rozklady na parciální zlomky na277
byly symbolicky zkontrolovány jako racionální identity pro obecné b.

Z koeficientů `(1-t)^(-j)` a `(b-t)^(-j)` dostáváme

```
mu_n = (n-(1-b^(-n))/(b-1))/2,
Var(K) = 1/4 * ( n+2n/(b-1) -(2b+1)/(b-1)^2
                  +(2b+2)b^(-n)/(b-1)^2 -b^(-2n)/(b-1)^2 ).
```

To jsou přesně vzorce na278. Platí i pro n0, kdy oba výrazy dávají0.
Pravděpodobnostní model je podstatný; tyto průměry ani rozptyly nejsou
obecnou zárukou pro závislé nebo nerovnoměrné vstupy.

Změna2026 přečíslovává rovnice původní(3)–(7) na(4)–(8), protože dříve
v sekci přibyla rovnice. Matematické vzorce přenosů tím nejsou změněny.

## Úloha42: konečná formule a Eulerova čísla

N=b^n označuje počet možných hodnot jednoho vstupu; sčítanců je m>=1.
Nyní sledujeme konečný přenos `floor((u_1+...+u_m)/N)`, jehož hodnoty jsou
k0,...,m-1. Eulerovo číslo E(m,k) je počet permutací m různých prvků,
které mají právě k vzestupů (sousedních dvojic v rostoucím pořadí).
Ukážeme, proč je limitní pravděpodobnost E(m,k)/m!.

Počítání nezáporných celočíselných řešení součtové nerovnosti a princip
inkluze a exkluze, který odečítá případy s některým u_i>=N, dávají přesný
počet pro interval `kN<=sum u_i<(k+1)N`:

```
N^m P_(n,k) = sum_{r=0}^k (-1)^r C(m+1,r)
                         C(N(k+1-r)+m-1,m).                 (A)
```

Konkrétně počet pro `sum u_i<=L` je
`sum_r (-1)^r C(m,r) C(L-rN+m,m)`, s nulovými členy pro záporné L-rN.
Odečtení hodnot pro L=(k+1)N-1 a L=kN-1 a Pascalova identita vytvoří
koeficient C(m+1,r) v(A).

Označme c(m,l) koeficient x^l v rostoucím součinu
`x(x+1)...(x+m-1)`. Jsou to nezáporná Stirlingova čísla prvního druhu;
pro výpočet platí `c(m,l)=(m-1)c(m-1,l)+c(m-1,l-1)`.
Rozvinutím binomického koeficientu v(A) dostaneme obecnou tištěnou formuli,
po doplnění znaménka z errata29.7.2024:

```
P_(n,k) = 1/m! sum_{j=0}^m c(m,m-j) N^(-j)
                   sum_{r=0}^k (-1)^r C(m+1,r)(k+1-r)^(m-j). (B)
```

Koeficient c(m,m)=1. Vnitřní součet pro j0 je E(m,k). Pro úplný důkaz
zaveďme `F_m(z)=sum_{l>=0}(l+1)^m z^l` a
`A_m(z)=(1-z)^(m+1)F_m(z)`. Koeficient A_m u z^k je přesně daný
střídavý součet. Platí A_0=1 a z formálního derivování
`F_m=(z*d/dz+1)F_(m-1)` plyne

```
A_m(z) = (1+(m-1)z) A_(m-1)(z) +z(1-z) A'_(m-1)(z).
```

Koeficienty tedy splňují
`E(m,k)=(k+1)E(m-1,k)+(m-k)E(m-1,k-1)`. Stejnou rekurenci dává
vložení největšího prvku m do permutace délky m-1: k+1 pozic zachová
k vzestupů, m-k pozic vytvoří k vzestupů z k-1. Počáteční hodnoty
souhlasí. Tím je identita i limitní koeficient odvozen bez předpokladu
platnosti tvrzení42.

Všechny ostatní členy v(B) jsou pro pevné m,k konečné konstanty krát
N^(-j), j>=1. Proto `P_(n,k)=E(m,k)/m!+O(b^(-n))`. Konstanta může záviset
na m,k. Chybějící faktor(-1)^r v prvním dotisku je známé erratum, nikoli
nový nález. Bibliografická atribuce Holtemu se ještě prověří v kontextovém
bloku; zde je úplný vlastní důkaz vzorce.

## Úloha43: přesné zaokrouhlení barevného součinu

Vstupy u,v jsou celá čísla0–255 a p=uv. Požadovaný w je nejbližší celé
číslo k p/255. Přesná půlka nemůže nastat, protože255 je liché.
Položme t=p+128. Pro každé nezáporné celé t platí

```
floor((t+floor(t/256))/256) = floor(257t/65536).
```

Důkaz: napišme t=256a+s, 0<=s<256. Rozdíl argumentů po vyjmutí celého
a je s/65536; zlomková část levého argumentu má krok1/256 a tento rozdíl
je menší než1/256, takže nemůže změnit podlahu.

Napišme p=255c+r, 0<=r<=254. Máme 0<=c<=255 a

```
257t = 65536c + (257r+32896-c).
```

Pro r<=127 je závorka mezi32641 a65535, takže výsledek je c.
Pro r>=128 je mezi65537 a98174, takže výsledek je c+1. Přesně toto je
zaokrouhlení p/255. Efektivní vzorec nepotřebuje počítat velké257t:
`t+floor(t/256)<=65407<65536`, tedy mezisoučet se vejde do16 bitů.

Záměna jmen x,y za u,v v původní odpovědi630 je známá oprava8.11.2005.
Žádný další problém v tomto vzorci nalezen nebyl.

## Reprodukce a vymezení

[verify_classical_carries.py](../verify_classical_carries.py),
[classical-carries.json](../results/classical-carries.json): pět obecných
symbolických identit, šest úplných společných rozdělení přenosů z21947
dvojic (nový rozsah zahrnuje koncový přenos a druhý moment),25 rozdělení
sloupcového součtu z43142 úplných m-tic, Eulerova čísla nezávisle podle
vzestupů všech permutací m1–8,5000 bitových párů pro komplementy a všech
65536 barevných dvojic. Všechny tři checkpointy dokončeny s kódem0.

Čtyři vrstvy errat prohledány pro276–278,284,629–630 i vzorce přenosů.
Vizuální doklady obsahují all2 str.10 (znaménko42) a all2-prepre str.38
(jména43). Historické citace Holte/Blinn a další kontext nejsou v tomto
matematickém bloku vydávány za přečtené primární prameny.

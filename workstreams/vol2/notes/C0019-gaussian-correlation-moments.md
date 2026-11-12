# V2-C0019: normalizace a momenty normální sériové korelace

**Confirmed**, 1.11.2026. §3.3.2-20, poznámka v odpovědi na str.565,
třetí vydání, první dotisk1997. Zdrojový obraz
`images/vol2-p565.png` byl přečten vcelku i zvětšený v oblasti vzorců.
Chyba je v Knuthově sazbě; původní Dixonův článek nebyl získán a
nepřipisujeme mu chybu.

## Nejkratší rozpory

N a D jsou čitatel a jmenovatel sériové korelace (23), tedy
N=n sum_j U_j U_(j+1)−(sum_j U_j)² a
D=n sum_j U_j²−(sum_j U_j)², s cyklickými indexy. Kniha uvádí pro
M(w,z)=E exp((wN+zD)/n) aproximaci

```text
sqrt(1−2z−2w) [1−2z+sqrt((1−2z)²−4w²)]^(−n/2) + O(w^n).
```

Při w=z=0 je levá strana1, pravá2^(−n/2). Zbytek O(w^n) nemůže
opravit nenulový konstantní člen. Například pro n=4 vychází1/4 místo1.

Hned následující vzorce pro momenty mají další rozpor. Při k=1
dávají E(N/D)=−1/(2n−1) a E(N/D)²=1/(2n+1). Pro n=3 jsou to
−1/5 a1/7. Přitom podle správné odpovědi18(b) na předchozí stránce
platí N/D=−1/2 pro každou nekonstantní trojici. Pro nezávislé normální
vstupy je trojice nekonstantní s pravděpodobností1, a správné momenty
jsou tedy −1/2 a1/4. Podmínka n>2k je splněna.

Závěrečný vzorec pro rozptyl, 1/(n+1)−1/(n−1)², je naopak správný
pro n>2. Hlavní obecný výsledek úlohy20 je rovněž správný; tento nález
se týká dvou zobrazovaných vzorců v doplňující normální poznámce.

## Odvození správné normalizace

Vezměme nezávislé standardní normální vstupy. Matice P cyklicky posouvá
souřadnice, J je matice samých jedniček. Platí

```text
N/n = U^T [(P+P^T)/2−J/n] U,
D/n = U^T [I−J/n] U.
```

Obě matice nulují konstantní směr. Na jeho kolmém doplňku má první
vlastní hodnoty lambda_j=cos(2 pi j/n), j=1,...,n−1; druhá je identita.
Ortogonální změna souřadnic zachovává nezávislé standardní normální
vstupy. Z jednorozměrného Gaussova integrálu proto dostáváme přesně

```text
M(w,z) = product_(j=1)^(n−1) (1−2z−2w lambda_j)^(−1/2).
```

Položme a=1−2z, h=(a+sqrt(a²−4w²))/2 a r=w/h. Pro w,z v dostatečně
malém okolí nuly je h>0 a |r|<1. Každý faktor před odmocněním je
h(1−r exp(2 pi i j/n))(1−r exp(−2 pi i j/n)). Součin přes všechny
n kořeny jednotky je h^n(1−r^n)². Odebráním j=0 vznikne

```text
M(w,z) = sqrt(a−2w) h^(−n/2) / (1−r^n).
```

Proto hlavní člen tištěné aproximace potřebuje faktor2^(n/2),
ekvivalentně dělení druhé závorky dvěma před umocněním.

## Obecný přesný způsob výpočtu momentů

Směr centrovaného normálního vektoru je rovnoměrný na jednotkové
sféře rozměru n−2. Označme (a)_r=a(a+1)...(a+r−1) rostoucí faktoriál
a [x^r] koeficient mocniny x^r. Pak pro každé nezáporné celé r platí

```text
E (N/D)^r = r! / ((n−1)/2)_r
            * [x^r] product_(j=1)^(n−1)(1−x lambda_j)^(−1/2).
```

Důkaz: poloměr a směr normálního vektoru jsou nezávislé, moment
čtverce poloměru řádu r je 2^r ((n−1)/2)_r. Vydělíme jím moment
kvadratické formy, získaný z Gaussovy generující funkce. Zvláště pro
n>2 vychází E(N/D)=−1/(n−1), E(N/D)²=1/(n+1), a uvedený správný rozptyl.

Nezávislé ověření v `verify_serial_correlation.py` porovnalo18
racionálních determinantů s Chebyshevovou determinantovou identitou.
123 momentů bylo spočteno pomocí stop přesných matic; stopy nezávisle
ověřuje počet uzavřených procházek na cyklu. Případy n=3 a4 mají
ještě přímou kontrolu: pro n=3 je korelace konstantní −1/2; pro n=4
je záporným čtvercem jedné souřadnice rovnoměrného směru na sféře S²,
tedy její r-tý moment je (−1)^r/(2r+1).

## Errata a limity

Dne1.11.2026 prohledány všechny vrstvy `all2-prepre`, `all2-pre`,
`all2`, `err2` a aktuální původní TeX: str.564–565, odpověď20,
Dixon, normální momenty. Na565 je pouze oprava odpovědi24 z5.2.2005;
oprava tohoto odstavce nenalezena. Náhled vydavatele končí před touto
stranou. Nejnovější fyzický tisk a prvenství nejsou ověřeny.

[Obsah původního čísla časopisu](https://www.jstor.org/stable/i312738)
a Crossref potvrzují Dixonův titul *Further Contributions to the
Problem of Serial Correlation*, Annals of Mathematical Statistics15
(1944),119–144, DOI10.1214/aoms/1177731279. Metadata:
`sources/dixon-1944-metadata.json`; přímé čtení článku se netvrdí.
Report `reports/C0019-gaussian-correlation-moments-draft.txt` nebyl odeslán.

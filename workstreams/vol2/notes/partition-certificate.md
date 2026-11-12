# Certifikát počtu omezených particí a narozeninové tabulky

Vlastní odvození1.11.2026 pro §3.3.2-28 až30. Zde p_n(M) je
počet rozkladů nezáporného celého M na nejvýše n kladných částí.
Jeho generující funkce je F_n(z)=prod_(j=1)^n(1−z^j)^(-1).
Certifikát používá všechny póly této racionální funkce; pól je
bod, v němž funkce diverguje jako záporná mocnina vzdálenosti.
Výsledek nevyžaduje nekontrolované zanedbání vedlejších oblouků
v tištěné metodě sedlového bodu.

## 1. Příspěvek pólu1

Položme N=n(n+1)/2 a a=M+N/2. Substituce z=exp(−t) v reziduu
dává pro příspěvek pólu z=1 polynom

```text
P_n(M) = (1/n!) [t^(n−1)] exp(a t) H_n(t),
H_n(t) = prod_(j=1)^n (jt/2)/sinh(jt/2).
```

Zápis[t^k] označuje koeficient příslušné mocniny. Reziduum je
koeficient mocniny−1 v Laurentově rozvoji; při substituci je
dz/z=−dt, což vyrovná minus v součtu ostatních reziduí.

Definujme h_k=[t^(2k)]H_n(t). V lichých stupních jsou koeficienty
nulové. Pro Bernoulliho čísla B_(2j), definovaná koeficienty
x/(1−exp(−x)), platí

```text
log H_n(t) = sum_(j>=1) ell_j t^(2j),
ell_j = −B_(2j) (sum_(r=1)^n r^(2j)) / [2j(2j)!],
h_0=1,   h_k=(1/k) sum_(j=1)^k j ell_j h_(k−j).
```

Volba znaménka B_1 zde nehraje roli: používáme pouze sudé indexy.
Po vynásobení n!(n−1)! je proto přesný polynom

```text
n!(n−1)! P_n(M)
 = sum_(k=0)^floor((n−1)/2) h_k (n−1)_(2k) a^(n−1−2k),
```

kde(x)_j=x(x−1)...(x−j+1) je klesající součin. Program počítá
h_k racionálně a vyhodnocuje polynom celočíselným Hornerovým
schématem v A², A=2M+N; společný jmenovatel je pevný pro každé n.

## 2. Certifikovaný zbytek po prvních L sudých členech

Eulerův součin pro sinus ukazuje, že H_n(iu)=sum|h_k|u^(2k)
má nezáporné koeficienty. Uvažujme celý interval M_lo<=M<=M_hi
a definujme a_lo=M_lo+N/2, a_hi=M_hi+N/2, r=8n/a_lo.
Program přesně ověří

```text
nr/2 <= 1,
E = (sum_(j=1)^n j²) r² / [24(1−n²r²/24)] <= 1/2.
```

Z Taylorovy meze sin(x)>=x−x³/6 a z
−log(1−v)<=v/(1−v) pro0<=v<1 plyne

```text
H_n(ir) <= exp(E) < 2.
```

Klesající součin(n−1)_(2k) je nejvýše n^(2k). Proto absolutní
zbytek v **normalizovaném polynomu** n!(n−1)!P_n(M) po k<L
nepřesahuje

```text
a_hi^(n−1) sum_(k>=L)|h_k|(n/a_lo)^(2k)
 <= 2 a_hi^(n−1) / 64^L.
```

Použito L=24; pro malá n se bere celý konečný polynom a tento
zbytek je přesně0. Horní mez se zaokrouhluje na celé číslo
nahoru, takže žádná plovoucí aritmetika neoslabuje certifikát.

## 3. Všechny ostatní kořeny jednotky

Nechť zeta je primitivní d-tý kořen jednotky,2<=d<=n, a p=floor(n/d)
je řád jeho pólu. Předpokládejme M>=4n². Kolem zeta vezměme
kružnici poloměru rho=p/M. Obsahuje jediný pól F_n: vzdálenost od jiného kořene řádu
d_prime<=n je alespoň4/(d d_prime)>=4/(dn), zatímco
rho<=1/(4nd). Pro násobky
d dává odhad binomického rozvoje

```text
|1−z^j| >= j rho/2.
```

Pro ostatní j platí |1−zeta^j|>=4/d a
|z^j−zeta^j|<=2n rho. Relativní změna je nejvýše
n p d/(2M)<=n²/(2M)<=1/8; postačí tedy slabší mez
|1−z^j|>=|1−zeta^j|/2.

V každém úplném bloku d indexů je součin nenulových hodnot
|1−zeta^j| roven d. V neúplném bloku je dolní mez3^(−d).
Pro její důkaz stačí uspořádat všechny možné vzdálenosti:
|1−exp(2pi i k/d)|>=4 min(k,d−k)/d. Součet záporných částí
jejich logaritmů má velikost nejvýše

```text
2 sum_(k<=d/4) log(d/(4k))
 <= 2 integral_0^(d/4) log(d/(4x)) dx = d/2.
```

Každý podvýběr faktorů má tudíž součin alespoň exp(−d/2)>3^(−d).
Pro všechny faktory dohromady z toho plyne

```text
|F_n(z)| <= 2^n 3^d / (rho^p d^(2p) p!).
```

Rovněž |z|^(−M−1)<3^(2p+1), protože
−(M+1)log(1−rho)<=2p+1. Integrál po malé kružnici proto
omezuje absolutní reziduum F_n(z)z^(−M−1) číslem

```text
B_d(n,M) = 2^n 3^(d+2p+1) (M/p)^(p−1) / [d^(2p) p!].
```

Primitivních kořenů řádu d je nejvýše d. Reziduum v nekonečnu
je0, takže přesný koeficient splňuje

```text
|p_n(M)−P_n(M)| <= sum_(d=2)^n d B_d(n,M).
```

Každá B_d je neklesající v M. Pro celý požadovaný interval tedy
stačí dosadit M_hi, zaokrouhlit každou mez nahoru a sečíst.
Program pak tuto mez násobí n!(n−1)!, aby ji mohl sečíst
se zbytkem z části2. Důkaz zahrnuje všechny kořeny jednotky,
nikoli pouze nejbližší sedlový bod.

## 4. Nezávislé kontroly a výsledné pravděpodobnosti

Pro n=2..20 porovnává program úplný P_n s nezávislým rozvojem
racionální funkce v proměnné1−z. Koeficient(1−z)^(-j) přispívá
binom(M+j−1,j−1); tento postup nepoužívá Bernoulliho čísla ani
exponenciální substituci. Všech76 hodnot souhlasí přesně.
Současně se porovnávají s celočíselným dynamickým výpočtem p_n(M);
rozdíly leží v uvedených mezích ostatních reziduí.

R je počet opakování mezi seřazenými narozeninovými mezerami,
s je počet mezer délky0. Používáme přesné generující funkce
z28/29, ověřené odděleně úplnými slovy a váženými particemi
v `verify_birthday_spacings.py`. Každý čitatel je konečný
polynom A(z). Koeficient A(z)F_n(z) je lineární kombinace
p_n(M−j), takže chybu omezí součet absolutních koeficientů A
krát společná mez. V příspěvcích s>0 je navíc přesný počet
rozdělení označených pozorování do neprázdných skupin,
Stirlingovo číslo{n\n−s}. Všechny příspěvky se **sčítají**.

Pro n=512,m=2^25 jsme certifikovali:

|Kategorie|Pravděpodobnost, informativně|Horní mez absolutní chyby|
|---|---:|---:|
|R=0|0.368801577097920890285859|2.445·10^(-43)|
|R=1|0.369035243450689819080441|1.250·10^(-40)|
|R=2|0.183471182131179017765623|2.388·10^(-38)|

Čtvrtá kategorie je komplement součtu. Racionální intervaly
a porovnání všech čtyř zaokrouhlení jsou v `results/birthday-table.json`.
Stejný certifikát ověřuje dlouhý prefix q_512(2^25) na str.570,
kde q_n(m)=p_n(m−N) počítá rozklady na n různých kladných částí.

## 5. Obecná asymptotika v úloze30

Nechť m=n³/alpha, kde alpha>0 je pevné a m celé. V části1
pro p_n(m) použijeme a=m+N/2. Pro první tři sudé koeficienty platí

```text
h_0=1,
h_1=−S2/24,
h_2=S2²/1152+S4/2880,
S2=sum_(j=1)^n j²,  S4=sum_(j=1)^n j^4.
```

Zbytek k>=3 je O(n^(-3)) po normalizaci m^(n−1): v argumentu
části2 nahraďme faktor8 faktorem sqrt(n). Pak
H_n(i sqrt(n)n/a)=exp(O(1)) a příspěvek k>=3 je O(n^(-3)).
Příspěvek S4 v h_2 je také O(n^(-3)). Meze části3 jsou
o(n^(-B)) vůči hlavnímu členu pro každé pevné B. Například
p<=n/2, pd>n/2 a p!>=(p/e)^p dávají po normalizaci
nejvýše exp(O(n)) n^(p−n), rovnoměrně ve2<=d<=n.

Stačí tedy rozvinout první tři členy. Program symbolicky ověřil

```text
n!(n−1)! p_n(m) / m^(n−1)
 = exp(alpha/4) [1−13alpha²/(288n)
   +(169alpha^4+2016alpha³−1728alpha²−41472alpha)/(165888n²)
   +O(n^(-3))].
```

Pro q_n(m) je střed a=m−N/2; tentýž výpočet změní alpha na
−alpha v koeficientech závorky i exponenciále. To potvrzuje
oba hlavní vzorce na79/569 nezávisle na chybných pomocných
identitách tištěného sedlového důkazu. Podrobný audit těchto
identit a pravděpodobnostního závěru úlohy30 je v
[birthday-spacings.md](birthday-spacings.md).

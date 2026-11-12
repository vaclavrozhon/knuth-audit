# §4.7–29: determinant dvojité mocninné řady

Stav 2026-11-04: celá nová úloha 29 z errat 2024-04-01 je
zkontrolována. **V2-C0231 confirmed:** dva exponenty v části (a)
mají být n(n−1)/2, nikoli n(n+1)/2. Část (b) a její výsledek 1
jsou správné. Jde o chybu v doplněné úloze, která v prvním dotisku
z roku 1997 ještě nebyla. Novější tištěný exemplář není ověřen.

## 1. Definice a nejmenší protipříklad

Dvojitá formální mocninná řada A(w,z) přiřazuje koeficient a(i,j)
každé mocnině w^i z^j. Znak [w^i] znamená koeficient u w^i.
Matice A_n obsahuje a(i,j) pro **0<=i,j<n**. Pro řady p,q,r,s
jedné proměnné definujeme

```text
T(w,z) = p(w) q(z) A(w r(w), z s(z)).
```

Matice T_n se sestaví stejným způsobem z koeficientů T. Substituce
je formálně přípustná: w r(w) i z s(z) mají nulový konstantní člen,
a proto každý výsledný koeficient závisí jen na konečném počtu
koeficientů vstupu.

Stačí n=1, A(w,z)=1, p=q=1, r=s=2. Pak T(w,z)=1 a obě matice
jsou [1]. Jejich determinanty jsou 1, ale vytištěná pravá strana
je 2^1*2^1=4. Chyba nezávisí na konvergenci, singularitě ani
nulových konstantách.

Také u každé velikosti n>=1 lze vzít A(w,z)=1/(1-wz), p=q=s=1,
r=2. Potom A_n je jednotková matice a T_n je diagonální s prvky
1,2,...,2^(n-1). Její determinant je 2^(n(n-1)/2), zatímco
vytištěný exponent je o n větší.

## 2. Obecný důkaz opravy

Pracujme nad libovolným komutativním okruhem s jednotkou, tedy
oborem, v němž lze sčítat a násobit a násobení nezávisí na pořadí.
Nejsou potřebné inverze nenulových prvků. Definujme dvě matice
s indexy 0,...,n-1:

```text
P(m,i) = [w^m] p(w) (w r(w))^i,
Q(k,j) = [z^k] q(z) (z s(z))^j.
```

Pro i>m je P(m,i)=0, protože každý člen obsahuje alespoň w^i;
stejně Q(k,j)=0 pro j>k. Obě matice jsou tedy dolní trojúhelníkové
(všechny prvky nad diagonálou jsou nula). Jejich diagonály jsou

```text
P(i,i) = p(0) r(0)^i,       Q(j,j) = q(0) s(0)^j.
```

Roznásobením konečného součtu koeficientů dostaneme
T_n = P A_n Q^t, kde Q^t označuje transponovanou matici, tedy matici
s vyměněnými řádky a sloupci. Vyšší indexy původní nekonečné řady
nemohou přispět ke koeficientům v tomto výřezu.

Determinant součinu je součinem determinantů a determinant
triangulární matice je součinem jejích diagonálních prvků. Proto

```text
det T_n = p(0)^n q(0)^n
          r(0)^[0+1+...+(n-1)] s(0)^[0+1+...+(n-1)] det A_n
        = p(0)^n q(0)^n r(0)^[n(n-1)/2] s(0)^[n(n-1)/2] det A_n.
```

Tento důkaz zahrnuje také nulové konstantní členy. Mocnina s nulovým
exponentem je prázdný součin, tedy 1; to je potřebné například pro
n=1 a r(0)=0. Stejná formule platí i pro prázdnou matici n=0,
jejíž determinant je 1.

Odpověď v erratech správně vysvětluje případ všech konstantních
členů rovných 1 pomocí přičítání předchozích řádků či sloupců.
Její konkrétní rozvoj pátého řádku je správný:

```text
t(5,j) = a(5,j) + 4 r1 a(4,j) + (3 r2+3 r1^2) a(3,j)
         + (2 r3+2 r1 r2) a(2,j) + r4 a(1,j).
```

Zde r_k=[w^k]r(w), r_0=1 a p=q=s=1. Chyba je právě v údajném
počátečním konstantním případě. Redukce na konstanty 1 navíc sama
neřeší nulové konstanty; výše uvedená maticová faktorizace je řeší
bez výjimek a bez dělení.

## 3. Část (b): determinant je vždy 1

Nyní pracujeme nad racionálními čísly, aby byly definovány
koeficienty exponenciály a logaritmu. Máme

```text
A(w,z) = exp(w+z)/(exp(w)+exp(z)-exp(w+z)).
```

Jmenovatel má konstantní člen 1, takže formální dělení je definováno.
Položme

```text
p(w)=1/(1+w),       q(z)=1/(1+z),
r(w)=log(1+w)/w,    s(z)=log(1+z)/z.
```

Podíly w a z zde pouze posouvají koeficienty: log(1+w) má nulový
konstantní člen, a r(w)=1-w/2+w^2/3-... je obyčejná mocninná řada.
Všechny čtyři konstantní členy jsou 1. Po substituci je

```text
A(log(1+w),log(1+z))
 = (1+w)(1+z) / ((1+w)+(1+z)-(1+w)(1+z))
 = (1+w)(1+z)/(1-wz).
```

Tedy T(w,z)=1/(1-wz)=sum_{k>=0} w^k z^k. Jeho koeficientová
matice T_n je jednotková a det T_n=1. Opravená formule části (a)
proto dává **det A_n=1 pro každé n>=0**. Nesprávný exponent části
(a) v tomto speciálním příkladu nic nemění, protože umocňuje 1.

## 4. Nezávislé konečné kontroly

`verify_series_determinant.py` provedl jediný úspěšný běh:

- 1024 přesných případů transformační formule: velikosti 1–4,
  všechny čtveřice konstant z {-2,0,1,2}, nenulové vyšší koeficienty;
  700 případů má alespoň jednu nulovou konstantu. Výsledné koeficienty
  jsou přímo rozvinuty a determinanty spočteny permutační formulí.
- Pro část (b) byly koeficienty spočteny nezávisle z identity
  `(exp(-w)+exp(-z)-1) A(w,z)=1`. To dává rekurenci
  `a(m,n)=-sum_{i=1}^m (-1)^i a(m-i,n)/i!`
  `        -sum_{j=1}^n (-1)^j a(m,n-j)/j!`, s a(0,0)=1.
  Determinanty prvních dvanácti matic jsou přesně 1. Tato kontrola
  nepoužívá substituci logaritmu ani transformační formuli.

Matematické kontroly 0.674550259 s, obalový běh 0.746982629 s,
PID 1585434, limit 120 s, exit 0. Žádný úspěšný test nebyl opakován.
Výsledky doplňují obecný důkaz; nejsou vydávány za důkaz všech n.

## 5. Sazba, errata a prameny

Vizuálně ověřeny all2.pdf, strany souboru 9 (úloha) a 12 (odpověď),
a err2.pdf, strana souboru 8 (stejná úloha). Oba výskyty mají plus
v obou exponentech. V originálním TeXu je přesně
`r(0)^{n(n+1)/2}s(0)^{n(n+1)/2}`. Čerstvě stažený soubor
[err2.textxt](https://www-cs-faculty.stanford.edu/~knuth/err2.textxt)
ze 4. listopadu 2026 je bajtově totožný s archivovanou kopií.

Prohledány všechny šestery vrstvy: all2-prepre, all2-pre, all2,
err2, err2-2e a originální err2.textxt. Nová úloha a odpověď jsou
z 2024-04-01; starší vrstvy ji neobsahují. Navazující oprava těchto
exponentů nebyla nalezena. Výpis je v
`sources/series-determinant-errata.txt`, kontrolní součty v manifestu.

Citovaný [Gessel–Xin, EJC 13 (2006), R53](https://doi.org/10.37236/1079)
byl získán od vydavatele. Relevantní pravidla v §4 na straně 14
jsou přečtena textově i vizuálně. Mají správný faktor c^binom(n,2)
a stejné indexy 0,...,n-1. Bibliografie potvrzuje Gesselovo řešení
části B úlohy 6151 v AMM 86 (1979), 64–65. Původní AMM řešení
zde nebylo získáno; vlastní úplný důkaz na něm nezávisí. Zbytek
48stránkového článku Gessel–Xin není tímto blokem auditován.

Nález se týká přesně nové úlohy §4.7–29(a), zamýšlené pro stranu
537; odpověď je přidána na stranu 725. Hlášení zůstává neodesláno.
Potvrzení neznamená doložené prvenství ani ověření nového dotisku.

# Restartovací strategie: SAT 306–308

Kontrola 31. 10. 2026. Definice a zadání jsou v 7.2.2.2–306–308;
odpovědi na str. 608–610. Tři nové nálezy jsou na str. 609. U všech
je stejné znění také v autorově Pre-Fascicle 6A, 23. 9. 2015, str. 245.
Obě stránky byly vykresleny a vizuálně porovnány. V úplných seznamech
`all4b` a `all4f6` ani v krátkých erratech odpovídající oprava není.
Fyzický výtisk dosud neověřen, žádná zpráva nebyla odeslána.

## Základní model a správný výpočet

Jednotlivé běhy jsou nezávislé. T je počet kroků do úspěchu, případně ∞.
Značme `q_N=Pr(T≤N)`, `E_N=Σ_(t≤N) t p_t` a

```
c_N = E min(T,N) = E_N + N(1−q_N)
    = Σ_(j=0)^(N−1) (1−q_j).
ell(N) = c_N/q_N, je-li q_N>0.
```

Pro posloupnost cutoffů N_j je pravděpodobnost dosažení j-tého běhu
`P_j=Π_(i<j)(1−q_(N_i))`. Monotónní konvergence nezáporných nákladů dává

```
E X = Σ_(j≥1) P_j c_(N_j).
```

Rovnost platí i s nekonečnou hodnotou. Pro periodickou posloupnost je
výsledek součet vážených nákladů jednoho cyklu dělený pravděpodobností,
že cyklus uspěje. To bylo porovnáno s nezávislým výpočtem: stavem
Markovova řetězce je číslo běhu v periodě a počet jeho již vykonaných
neúspěšných kroků; přechody používají podmíněnou pravděpodobnost dalšího
selhání. Racionální Gaussova eliminace řeší očekávanou dobu absorpce.

## F027: v odpovědi 307(a) chybí váha u E_N

Vytištěný postup aktualizuje α na pravděpodobnost přežití aktuálního běhu,
ale následně přičte celé E_(N_j). Tento příspěvek je nutné násobit
pravděpodobností **dosažení** aktuálního běhu, tedy starou hodnotou α.
Správné pořadí je například:

```
j ← j+1
s ← s + α (E_(N_j) + (1−q_(N_j))N_j)
α ← α (1−q_(N_j))
```

Přesný protipříklad: `p_1=p_∞=1/2`, všechny `N_j=1`.
X má geometrické rozdělení se střední hodnotou 2. Po j iteracích:

| j | vytištěné s | správný částečný součet |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 7/4 | 3/2 |
| 3 | 19/8 | 7/4 |
| 4 | 47/16 | 15/8 |

Vytištěný součet překročí celou střední hodnotu už při j=3 a potom
roste bez omezení. Volba ε=1/16 vrátí 47/16 místo aproximace hodnoty 2.
Obecně má vytištěný součet hodnotu `j/2+1−2^(−j)`; správný je
`2(1−2^(−j))`. Není to otázka malé chyby z useknutí nekonečné řady.

Samotná podmínka α≤ε navíc bez kontroly zbývajících očekávaných nákladů
nedává absolutní chybu ≤ε pro libovolnou posloupnost cutoffů. To zde
nepočítáme jako další nález; pro naše periodické testy se ocas sčítá přesně.

## F028: v odpovědi 307(b) má být T_(j−1)

Součin definující P_j obsahuje prvních j−1 selhání. Proto

`P_j = Pr(X>T_(j−1))`, nikoli vytištěné `Pr(X>T_j)`.

V předchozím protipříkladu je P_1 prázdný součin, tedy 1, zatímco
Pr(X>T_1)=1/2. Následující rozklad střední hodnoty používá součin správně:
`P_j q_(N_j)=Pr(T_(j−1)<X≤T_j)=P_j−P_(j+1)`.
Chyba je pouze v identifikaci pomocné pravděpodobnosti.

## F029: chybný předpoklad v důkazu 306(h)

Odpověď začíná podmínkou N*=∞ a konečnou ell(n), ale pak tvrdí, že lze
najít n' s `q_(n') ell(n')>ell(n)`. To obecně neplatí.
Samotná odpověď 306(j) dává protipříklad:

```
p_t = [t>1]/2^(t−1),
q_N = 1−2^(1−N),
c_N = q_N ell(N) = 3−2^(2−N), N≥2,
ell(N) = (3−2^(2−N))/(1−2^(1−N)) > 3.
```

ell(N) klesá k 3, žádný konečný cutoff minima nedosáhne, tedy N*=∞.
Přitom ell(2)=4 a všechna c_N<3, takže požadované n' neexistuje.

Pravděpodobná místní oprava je začít **E_∞=∞** místo N*=∞.
Tím dostaneme důkaz kontrapozicí první části. Celý platný argument:

1. Protože p_∞<1, existuje n s q_n>0 a ell(n)<∞.
2. Je-li E_∞=∞, monotónní konvergence dává c_N→∞, tedy i ell(N)→∞.
   Minimum je pak dosaženo v konečné množině cutoffů a N*<∞.
3. N*=∞ proto implikuje E_∞<∞, zejména p_∞=0. Pak q_N→1 a
   ell(N)=c_N/q_N→E_∞. Jestliže infimum není dosaženo, každá
   minimalizující posloupnost cutoffů musí unikat do nekonečna;
   tudíž ell=E_∞.

Zadání 306(h) je správné, opravit je potřeba důkaz.

## Ostatní části 306

- (a) Vyřešení obnovovací rovnice dává c_N/q_N.
- (b) Pro bodovou hmotnost p_m=m/n je ell(m+k)=n+k(n−m)/m.
- (c) Pro rovnoměrné 1..n je ell(N)=n−(N−1)/2 do N=n a poté
  (n+1)/2.
- (d) Rovnost všech ell(N) dává rekurenci
  `1−q_(N+1)=(1−p_1)(1−q_N)`, tedy geometrické rozdělení.
- (e) Stejná rekurence od n dává geometrický ocas s parametrem
  1/ell(n). Počáteční q_n musí být kladné, aby byla ell(n) definována;
  tento doménový předpoklad nepovažujeme za samostatný nález.
- (f) Při q_(n+1)=1 je rozdíl
  `(n−Σ_(j=1)^n q_j)(1−1/q_n)≤0`. Má-li být nezáporný, q_n=1.
- (g) Oblast je `1/2<x<1`, `0≤y<(2x−1)(1−x)/x`. Přímé porovnání
  tří nákladů souhlasí na 1210 racionálních rozděleních.
- (i) Pro těžký ocas je ell(n+k)=(k+1)(n+H_k)/k. Znaménko rozdílu
  sousedních hodnot určuje k+1−H_(k+1)−n, což roste v k. První k,
  kde je výraz nezáporný, je nejmenší optimum; n=10 dává N*=23.
  Pro n→∞ plyne k=n+ln n+O(1). Prošlo všech 101 případů n=0..100.
- (j) Uvedený geometrický příklad je správný; viz F029.

Pro (k) je L=min_N N/q_N dosaženo, protože N/q_N≥N. Z c_N≤N plyne
ell≤L. Pro N≤L použijeme q_j≤j/L a dostaneme
`ell(N)≥L−(N−1)/2≥(L+1)/2`. Pro N>L, J=⌊L⌋, platí

```
ell(N) ≥ c_N ≥ (J+1)(1−J/(2L)) ≥ (L+1)/2.
```

Poslední rozdíl je `(L−J)(J+1−L)/(2L)≥0`. Přechod k infimu dává
L≤2ell−1. Celkem 1020 rozdělení se čtyřmi konečnými hmotnostmi a
možnou hmotností v ∞ potvrzuje meze; zkontrolováno 5796 konečných cutoffů.

## 307(b–d): směsi a nutnost logaritmické ztráty

Pokud q_(N_j)>0 pro všechna j a n je nejmenší index s p_n>0, potom
N_j≥n a P_j≤(1−p_n)^(j−1)→0. Váhy P_j q_(N_j) se proto sečtou na 1.
E X je jejich směsí hodnot ell(N_j), tedy E X≥ell. Pro cutoffs s nulovou
pravděpodobností úspěchu buď algoritmus s kladnou pravděpodobností nikdy
neuspěje (E X=∞), nebo nulové váhy pouze přidávají nezáporné náklady.
Případ N*=∞ znamená jako limitní nejlepší postup vůbec nerestartovat.

Pro (d) lze cutoffs omezit na n. Nechť r je první index, kdy všechna
rozdělení p^(m) mají pravděpodobnost úspěchu alespoň 1/2. Jestliže takový
index neexistuje, alespoň jedno rozdělení má kladnou pravděpodobnost
nekonečné doby běhu. Jinak označme t_m počet prvních r cutoffů ≥m.
Bernoulliho nerovnost dává t_m≥n/(2m), proto
`Σ_(j≤r) N_j=Σ_(m≤n) t_m≥n H_n/2`. Pro alespoň jedno m přežívá prvních
r−1 běhů více než polovina pravděpodobnosti. Jeho E X je proto větší než
`(Σ_(j<r) N_j)/2≥n H_n/4−n/2`, jak požaduje zadání.

## 308: Lubyho posloupnost a univerzální mez

Generátor (131) vypíše pro každé u postupně
`1,2,...,2^ν₂(u)`. Počet již vypsaných členů před u je
`2(u−1)−popcount(u−1)`. Z toho indukcí dostaneme pozici k-tého výskytu
2^a, při číslování k od nuly:

```
r = 2^(a+1)(k+1)−1−popcount(k).
h_a(z) = z^(2^(a+1)−1) Π_(j≥0) (1+z^(2^(a+1+j)−1)).
```

Pro Σ(a,b,k), s=a+b a U=2^s k, je součet dokončených běhů generátoru
plus poslední částečný běh

```
Σ(a,b,k) = Σ_(c≥0) 2^c floor((U−1)/2^c) + 2^(a+1)−1.
Σ(a,b,1) = (s−1)2^s + 2^(a+1).
Σ(a,b,k+1)−Σ(a,b,k) = 2^s (s−1+2^(ν₂(k)+1))
                       ≤ 2^s (s+2k−1).
```

To ověřuje uzavřené vzorce i meze v (a–e). Test porovnal generátor
s pozicemi pro prvních 300 000 členů, 1568 hodnot Σ a 1519 rozdílů.

Pro (f) ignorujme veškeré úspěchy kromě běhů s cutoffem 2^a a započtěme
celý blok do jeho 2^b-tého výskytu. Takové zhoršení může jen zvýšit dobu
běhu. Blok selže s pravděpodobností `Q=(1−q_(2^a))^(2^b)` a očekávání
součtu nákladů bloků dává přesně požadovanou horní mez. Protože
2^a≥t a 2^b≥1/q_t, platí Q<exp(−1).

Součtem geometrických řad v (g) dostaneme, se s=a+b,

```
E X < 2^s (A s+B+2^(1−b)),
A = e/(e−1), B = e(3−e)/(e−1)^2.
```

Je-li b≥1, pak 2^s<8ell, s<lg ell+3 a 2^(1−b)≤1.
Konstanty splňují 8A<13 a 8(3A+B+1)<49. Pro b=0 máme dokonce
2^s<4ell, s<lg ell+2; obdobně 4A<13 a 4(2A+B+2)<49.
Jelikož ell≥1, obě větve dokazují vytištěnou mez
`E X < 13ell lg ell+49ell`.

## Rozsah a reprodukce

`python3 check_restarts.py` vytváří `results/restarts.json`. Vedle výše
uvedených výčtů porovnává 120 periodických strategií s nezávislým
Markovovým řešením na celkem 954 stavech. V první verzi tohoto pomocného
řešiče byly dvě jedničky Python int, takže dělení zaneslo float do jinak
racionální eliminace; opraveno na Fraction. Šlo o chybu našeho testu,
ne knihy. Všechny publikované výsledky používají přesnou aritmetiku.

Doklady znění: `images/vol4b-p609.png`, `images/fasc6a-p245.png`.
Navazující empirická srovnání strategií v úlohách 310–312 zatím tato
kontrola nepokrývá.

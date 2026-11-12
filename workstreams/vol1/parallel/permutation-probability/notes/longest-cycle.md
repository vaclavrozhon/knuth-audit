# §1.3.3-23: nejdelší cyklus a zbytek asymptotického rozvoje

Stav matematického tvrzení úlohy a vytištěného rozvoje: `checked`.
Původní s.184 a525 byly zobrazeny. Vlastní důkaz níže platí pro všechny
n v limitním tvrzení, nespoléhá na extrapolaci konečného výpočtu.
Bibliografické podrobnosti a omezení zdrojového auditu jsou odděleně
v `source-audit.md`.

## Definice a plán důkazu

L_n je délka nejdelšího cyklu rovnoměrné permutace n prvků, L_0=0;
l_n=E L_n. Exponenciální integrál pro x>0 označíme
E_1(x)=integral_x^∞ exp(−u)/u du. Nejde o alternativní funkci Ei(x)
s jinou konvencí znaménka. Konstantu knihy označíme λ.

Nejprve z vkládání a odstraňování jediného prvku odvodíme, že l_n leží
mezi dvěma přímkami vzdálenými konstantu. Potom použijeme Poissonův
model cv.22: průměr přes geometricky rozdělené velikosti lze snadno
vyjádřit součtem integrálů. Jeho odhad se zbytkem určí i konstantní
člen λ/2. Poslední krok převádí limitu těchto vážených průměrů zpět
na samotnou posloupnost; potřebnou implikaci dokážeme.

## 1. Dvě monotónní posloupnosti

Z uniformní permutace n−1 prvků vytvoříme uniformní permutaci n prvků
výběrem jedné z n stejně pravděpodobných možností: nový singleton
nebo vložení nového prvku za libovolný starý prvek v jeho cyklu.
Při vložení do některého nejdelšího cyklu vzroste maximum o1. Součet
délek těchto cyklů je nejméně L_(n−1), takže

```
l_n − l_(n−1) ≥ l_(n−1)/n.
```

Naopak při odstranění konkrétního prvku z uniformní permutace n prvků
může maximum klesnout jen o1, a jen pokud odstraněný prvek ležel
v jediném nejdelším cyklu. Pravděpodobnost je nejvýše L_n/n. Proto

```
l_n − l_(n−1) ≤ l_n/n.
```

Tedy l_n/(n+1) neklesá a l_n/n neroste (druhá věta pro n≥2).
Obě jsou omezené a jejich rozdíl jde k0, takže mají stejnou limitu λ.
Pro všechna n≥1 platí

```
λ n ≤ l_n ≤ λ(n+1).
```

Definujme d_n=l_n−λn. Pak 0≤d_n≤λ a z předchozích nerovností
vyplývá |d_n−d_(n−1)|≤λ/(n−1) pro n≥2.

## 2. Přesný průměr při geometricky rozdělené velikosti

V nezávislém Poissonově modelu cv.22 má počet j-cyklů parametr w^j/j.
Proto pro m≥0

```
R_m(w) = sum_{j>m} w^j/j,
P_w(L≤m) = exp(−R_m(w)),
E_w L = sum_{m≥0} [1−exp(−R_m(w))]
      = (1−w) sum_{n≥0} l_n w^n.
```

Všechny součty jsou nezáporné, L≤N a E_w N=w/(1−w)<∞, takže zde
není problém z cv.22(c). Člen m=0 je **w**, nikoli1 nebo0;
jeho správné započtení je důležité pro konstantní člen.

Položme w=exp(−t), t>0, a F(x)=1−exp(−E_1(x)) pro x>0, F(0)=1.
Pro m≥1 použijeme Eulerův–Maclaurinův vzorec na
f_t(y)=exp(−ty)/y. Protože integrál |f_t''| od m do∞ je
|f_t'(m)|=exp(−tm)(1+tm)/m², dostáváme **uniformně**

```
R_m(exp(−t))
  = E_1(mt) − exp(−mt)/(2m)
    + O(exp(−mt)(1+mt)/m²).                         (A)
```

Z monotónnosti f_t také přímo plyne
|R_m(exp(−t))−E_1(mt)|≤exp(−mt)/m≤1. Taylorův vzorec pro exponenciálu
s uniformně omezeným druhým derivátem na tomto intervalu proto dává

```
1−exp(−R_m(exp(−t)))
  = F(mt) + (t/2)F'(mt)
    + O(exp(−E_1(mt)) exp(−mt)(1+mt)/m²).           (B)
```

Zde F'(x)=−exp(−x−E_1(x))/x. Lokální rozvoj
E_1(x)=−γ−log x+x−x²/4+… ukazuje, že F je hladká v0,
F'(0)=−exp(γ), a exp(−E_1(x))≤C min(x,1). Její první dva deriváty
jsou integrovatelné na [0,∞); u∞ to plyne z exponenciálního poklesu.

Součet zbytků v(B) pro m≤1/t je O(t sum_{m≤1/t}1/m), pro m>1/t
je O(t), tedy dohromady O(t log(1/t))=o(1). Tento odhad je důvod,
proč zde lze sčítat lokální aproximace; samotné bodové O(1/m²)
by potřebný limitní závěr ještě nezdůvodnilo.

Označme A=integral_0^∞ F(x) dx. Další použití Eulerova–Maclaurinova
vzorce a Riemannových součtů dává

```
sum_{m≥1} F(mt) = A/t − 1/2 + O(t),
t sum_{m≥1} F'(mt) = integral_0^∞ F'(x) dx + O(t)
                   = −1 + O(t).
```

Po přičtení členu m=0 dostáváme

```
E_exp(−t) L = exp(−t) + A/t − 1/2 − 1/2
             + O(t log(1/t))
           = A/t + O(t log(1/t)).                  (C)
```

Z již dokázaných mezí λn≤l_n≤λ(n+1) plyne
λ/(exp(t)−1)≤E_exp(−t)L≤λ/(exp(t)−1)+λ, a tedy A=λ.
Integrace po částech (xF(x) mizí na obou koncích) dá tvar z knihy:

```
λ = integral_0^∞ [1−exp(−E_1(x))] dx
  = integral_0^∞ exp(−x−E_1(x)) dx.
```

Odečtením λ E_w N=λ/(exp(t)−1)=λ/t−λ/2+O(t) od(C) nyní získáme

```
(1−w) sum_{n≥0} d_n w^n → λ/2,  w→1−.             (D)
```

## 3. Proč (D) implikuje d_n→λ/2

Dokážeme pomocnou větu: je-li d_n omezená reálná posloupnost,
|d_n−d_(n−1)|≤C/n pro dostatečně velká n a
(1−w)sum d_n w^n→c, pak d_n→c.

Pro každé velké celé N definujme schodovou funkci h_N(x)=d_floor(Nx)
na [0,∞). Pro každé celé k≥1 platí přesně

```
integral_0^∞ exp(−kx) h_N(x) dx
  = [(1−exp(−k/N))/k] sum_{j≥0} d_j exp(−kj/N)
  → c/k.
```

Lineární kombinace funkcí exp(−kx), k≥1, aproximují indikátor
libovolného intervalu [a,b] s0<a<b v normě integrálu absolutní hodnoty.
Pro úplnost: po substituci y=exp(−x) se problém redukuje na aproximaci
integrovatelné funkce 1_[exp(−b),exp(−a)](y)/y polynomy v L¹[0,1].
Ta plyne aproximací po částech spojité funkce spojitými funkcemi
a poté Weierstrassovou větou. Omezenost h_N zaručuje uniformní
kontrolu chyby. Proto

```
integral_a^b h_N(x) dx → c(b−a).
```

Pro x∈[1,1+δ] je však
|h_N(x)−d_N|≤C log(1+δ)+o(1), sečtením odhadu na sousední rozdíly.
Průměr na tomto intervalu konverguje k c, takže
limsup_N |d_N−c|≤C log(1+δ). Necháme δ→0 a pomocná věta je dokázána.

Aplikace na(D) dává přesně požadované tvrzení

```
l_n = λn + λ/2 + o(1).
```

## 4. Další členy v odpovědi: co přesně je kontrolováno

Primární podklad: Xavier Gourdon, disertace1996,
`../sources/gourdon-thesis-1996.pdf`, kap.VII, zejména s.199,
200–214 a220–226. Přečten byl plán důkazu, uniformní přechod mezi
rozvoji v m a n, použití Eulerova–Maclaurinova vzorce, věty o
periodických koeficientech a konečné výpočty. Formule byly vizuálně
porovnány na s.199,222,225,226. Nejde o audit celé disertace ani všech
jejích dřívějších kapitol.

Gourdonův důkaz nejprve zajišťuje existenci úplného rozvoje s periodickými
koeficienty. To je zásadní: samotný radiální rozvoj generující funkce
u z=1 by zde nestačil, protože další kořeny jednotky také přispívají.
Věta6 na s.222 explicitně zajišťuje zbytek O(n^(−ell−1)) po příslušném
koeficientovém převodu. S ell=3 stačí zbytek O(n^−4).

Označme Ψ(z)=sum l_n z^n a ω=exp(2πi/3). Z části rozvojů na
s.225–226, které mohou přispívat až do n^−3, jsou logaritmické části:

```
u z=1:
  −exp(γ)[1/24 +(1−z)/48 +21(1−z)²/2560] log(1/(1−z));
u z=−1, z=−t:
  [(1−t)/8 +(1−t)²/8] log(1/(1−t));
u z=ω, z=ωt:
  [ω(1−t)²/12] log(1/(1−t));
u z=conj(ω): komplexně sdružená předchozí část.
```

Pólová část je λ/(1−z)²−λ/[2(1−z)], jejíž koeficient je λn+λ/2.
Použijeme přesnou identitu pro n>r≥0

```
[z^n](1−z)^r log(1/(1−z))
  = (−1)^r r!/[n(n−1)…(n−r)].
```

Pro reálný kořen1 je koeficient u n^−3
exp(γ)(1/48−42/2560)=17 exp(γ)/3840.
Pro kořen−1 je to (−1)^n(−1/8+1/4)=(−1)^n/8.
Komplexní dvojice dává [ω^(1−n)+ω^(n−1)]/6. Dostáváme

```
l_n = λn + λ/2 − exp(γ)/(24n)
    + [exp(γ)/48 − (−1)^n/8]/n²
    + [17exp(γ)/3840 +(−1)^n/8
       +ω^(1−n)/6 +ω^(n−1)/6]/n³
    + O(n^−4).
```

To je přesně rozvoj vytištěný v odpovědi23. Mocniny ω představují
reálný periodický součet; nelze je nahradit jediným konstantním
koeficientem ani je vyhodit do o(n^−3). Na skenu odpovědi23 není
uříznutý konec řady ani jiný tvrzený zbytek; kniha píše, že řada
takto začíná. V tomto směru není nové erratum.

Shepp–Lloyd1966 skutečně uvádějí druhý člen na s.355, ale podrobnosti
důkazu tam výslovně vynechávají. Samostatný důkaz v částech1–3 výše
tuto mezeru při naší kontrole vyplňuje. Jejich integrál pro λ je (14)
na s.347 a výsledek pro nejkratší cyklus je v §5; jeho kontrola je
zaznamenána ve zdrojovém auditu.

# Ramanujanova nerovnost: §1.2.11.3-13

Nechť n≥1 je celé a Q(n)=Q_1(n), R(n)=R_1(n), s funkcemi definovanými
v `asymptotic-findings.md`. Položme D(n)=R(n)−Q(n). Ověřovaný výsledek je

```text
2/3 + 8/[135(n+8/45)] ≤ D(n) ≤ 2/3 + 8/[135(n+2/21)].       (R1)
```

To je ekvivalentní formulaci úlohy s parametrem θ(n) mezi 2/21 a 8/45.
Dolní mez pro D(n) je větší než horní mez pro D(n+1), protože
`n+8/45 < n+1+2/21`; tedy plyne i tvrzená ryzí monotonicita.

## Primární důkaz a rozsah kontroly

Flajolet, Grabner, Kirschenhofer a Prodinger, *J. Comput. Appl. Math.*
58 (1995), 103–116, [kopie autorů](https://algo.inria.fr/flajolet/Publications/FlGrKiPr95.pdf).
Lokální PDF, text a metadata mají prefix
`sources/flajolet-grabner-kirschenhofer-prodinger1995-q`.
Přečteno celé matematické odvození v §§2–4 a závěr, včetně předpokladů
a konečné kontroly; sazba rozhodujících stran 109–115 je v `images/`.
Článek dokazuje tentýž výsledek v Theorem 7. Níže jeho metodu samostatně
rekonstruujeme, s mírně volnějšími konstantami a mezí n≥128 místo 116.
Článek není přijat jen na základě abstraktu ani grafu.

Při výpočtu se ukázaly dvě tiskové nesrovnalosti ve zdrojovém článku:
koeficient n^(−4) je **+17984/12629925**. Na s. 109 je vytištěno
+1794/12629925 a v polynomu D_10 na s. 113 −17984/12629925.
Přesné odvození níže i certifikát používají správnou kladnou hodnotu.
Nejde o nové samostatné nálezy v TAOCP. Důkaz nerovnosti tím není vyvrácen;
níže je dokončen s opraveným polynomem. Rovněž kontrolujeme spojitou větev
argumentu logaritmu přímo, bez spoléhání na větu článku o kvadrantech.

## Vytvořující funkce a přesný konečný polynom

Zápis [z^n] označuje koeficient z^n. Nechť y=y(z) je analytické řešení
`y=z exp(y)`, y(0)=0. Lagrangeova inverze dává pro j≥1
`[z^n]y^j = (j/n) n^(n−j)/(n−j)!` pro n≥j, jinak 0.
Rozvinutím −ln(1−y) nebo přímou Lagrangeovou inverzí dostaneme

`∑_{n≥1} Q(n)n^(n−1)z^n/n! = −ln(1−y)`.

Protože Q+R=n!exp(n)/n^n, má D vytvořující funkci
`ln((1−y)²/(1−ez))`. Pro kladné koeficientové indexy lze odečíst konstantu
ln 2. Definujme analytickou funkci

`Φ(w)=ln(w²/[2(1−(1+w)exp(−w))])=∑_{k≥1} c_k w^k`, Φ(0)=0.

Její koeficienty se získají jako záporný logaritmus řady
`h(w)=2∫_0^1 t exp(−wt)dt=∑_{j≥0}2(−1)^j w^j/[j!(j+2)]`.
Přesné Lagrangeovy koeficienty jsou polynomy v 1/n:

```text
B_k(n) = n! n^(1−n) [z^n](y−1)^k
       = sum_{j=1}^k (−1)^(k−j) binom(k,j) j
           product_{r=1}^{j−1}(1−r/n).
```

Položme `D_10(n)=∑_{k=1}^{10} c_k B_k(n)`. Výsledkem je

```text
2/3 + 8/(135n) − 16/(2835n²) − 32/(8505n³)
 + 17984/(12629925n⁴) + 13159709/(9699782400n⁵)
 − 977069/(1039262400n⁶) − 36669961/(28291032000n⁷)
 + 117191/(56582064n⁸) − 479/(561330n⁹).                 (R2)
```

Certifikát vytváří c_k a B_k odděleně z těchto definic a kontroluje (R2).

## Analytický odhad zbytku

Pro úplnost potřebujeme kontrolovat logaritmus a nikoli jen formálně
manipulovat řadami. Ve čtverci |Re w|,|Im w|≤π nemá
`g(w)=1−(1+w)exp(−w)` jinou nulu než dvojnásobnou nulu v 0.
Důkaz: kdyby exp(a+ib)=1+a+ib a 0<|b|<π, imaginární část dává
`a=ln(b/sin b)>0`, ale reálná část dává `a=b cot b−1<0`.
Poslední nerovnost plyne z derivace sin b−b cos b pro b>0; záporné b
se získá sdružením. Pro |b|=π je imaginární rovnost nemožná. Pro b=0
platí exp(a)>1+a mimo a=0. Singularita f(w)=w²/(2g(w)) v 0 je tedy
odstranitelná a f je nenulová, takže má jednoznačný analytický logaritmus
Φ s Φ(0)=0 v tomto čtverci i v okolí jeho hranice.

Na hranici čtverce platí

```text
L = π²/[2(1+(2π+1)exp π)] ≤ |f(w)|
  ≤ π²/[1−(π+1)exp(−π)] = U.                           (R3)
```

Dolní mez je trojúhelníková nerovnost. Pro horní mez stačí
|g(w)|≥1−(π+1)exp(−π): na pravé straně použijeme
`(π+1)cos b+b sin b≤π+1` pro 0≤b≤π; na levé straně
`|g|≥exp(π)(π−1)−1`; na horní straně je buď Re g≥1 (a≥−1),
nebo Im g=πexp(−a)≥πe (a<−1). Dolní polovina je sdružená.

V horní polovině hranice sledujeme spojitý argument g od pravého
reálného bodu k levému. Na pravé a horní straně je Im g>0.
Na levé straně má imaginární část znaménko
`(1−π)sin b−b cos b`; pro 0<b<π má právě jednu nulu, protože
b cot b přísně klesá od 1 do −∞. V tomto průsečíku je Re g<0:
součin (1+w)exp(−w) je kladný reálný a jeho velikost je alespoň
(π−1)exp π>1. Argument g tedy na celé horní hranici leží mezi 0 a 2π,
s koncovými hodnotami 0 a 2π. Také 2 arg w je mezi 0 a 2π.
Proto |Im Φ|=|2 arg w−arg g|≤2π, a totéž platí dole sdružením.
Z (R3) a Cauchyova koeficientového integrálu po hranici délky 8π plyne

`|c_k| ≤ (4/π) sqrt(max(|ln L|,|ln U|)²+4π²) π^(−k) < 11 π^(−k)`.

Při Cauchyově integraci vytvořující funkce změňme proměnnou na y:
`dz/z^(n+1)=(1−y)exp(ny)dy/y^(n+1)`.
Obrys tvoří svislá úsečka y=1+iτ, −1≤τ≤1, a delší kruhový oblouk
|y|=sqrt(2), Re y≤1. Je uvnitř oblasti analyticity Φ(y−1) a obepíná y=0.
Označme `T(w)=Φ(w)−∑_{k=1}^{10}c_k w^k`.
Na |w|≤1 platí silnější odhad
`|T(w)|≤μ|w|^11`, kde `μ=11/[π^10(π−1)]`.
Tento konkrétní odhad je nutný pro následující mocninu τ; nepoužíváme
jen slabší |w|^10, který naznačuje definice μ_K v článku.

Na svislé úsečce tedy absolutní hodnota normalizovaného zbytku nepřevýší

```text
(11/10) n sqrt(2πn)/(2π) · μ
  · integral_{−1}^1 |τ|^12/(1+τ²)^((n+1)/2) dτ
 ≤ G n^(−5),
G = (11/10) 2^13 Γ(13/2) μ/sqrt(2π) < 57.               (R4)
```

Použili jsme `n!<(11/10)(n/e)^n sqrt(2πn)` a
`ln(1+τ²)≥τ²/2` pro |τ|≤1; rozšířený Gaussův integrál je
`2^13 Γ(13/2)n^(−13/2)`. Stirlingova nerovnost plyne z dříve dokázaného
zbytku ≤1/(12n) a exp(1/12)<11/10.

Na oblouku je |w|≤1+sqrt(2), délka je 3πsqrt(2)/2 a Re y≤1.
S `ρ=(1+sqrt(2))/π<1` odhad geometrické řady dává

```text
normalizovaný zbytek ≤ H n^(3/2) 2^(−n/2),
H = (33/40) sqrt(2π)(1+sqrt(2)) · 11ρ^11/(1−ρ) < 14.    (R5)
```

Pro celé n≥128 je pravá strana <10^(−7)n^(−3): v n=128 se to ověří
po umocnění přesnou celočíselnou nerovností, a výraz n^9/2^n poté
klesá, protože `(129/128)^9<2`.
Tím máme obecně

`|D(n)−D_10(n)| ≤ Δ(n)=10^(−7)n^(−3)+57n^(−5)`, n≥128.

## Konečné a nekonečné části certifikátu

Program `check_ramanujan.py` kontroluje konstanty v (R3)–(R5) pomocí
racionálních intervalů pro π, exp a ln z dříve ověřených elementárních
konstant. Zlomky `D_10−Δ−dolní_mez` a `horní_mez−D_10−Δ` uvede na
společný jmenovatel. Oba jmenovatele mají nezáporné koeficienty a jsou
kladné pro n>0. Po dosazení n=t+128 mají oba čitatele **všechny
koeficienty kladné**, což dokazuje jejich kladnost pro každé reálné t≥0.
Nejde o vzorkování velkých n.

Pro 1≤n≤127 se Q(n) počítá přesnými zlomky z konečné definice a
`D(n)=n!exp(n)/n^n−2Q(n)` pomocí vnějších racionálních intervalů pro exp(n).
Každý interval leží ostře uvnitř mezí (R1). Všechny intervaly, kladné
rezervy, oba polynomy a jejich posunuté koeficienty ukládá
`results/ramanujan-bound.json`. Tím je spolu s analytickým odhadem
uzavřen důkaz pro všechna kladná celá n. Hraniční n=0 není třeba pro
definice Q a R v této kapitole; v rozšířené formulaci článku se ověří přímo.

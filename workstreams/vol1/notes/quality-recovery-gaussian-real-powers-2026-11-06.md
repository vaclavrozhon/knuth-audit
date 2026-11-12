# §1.2.11.3–14(d): každý reálný exponent t≥0

Původní zadání na123 výslovně dovoluje pevné **reálné** t≥0.
Pro celá t jsou všechny derivace x^t exp(−x²/(2n)) v nule
regulární a celý důkaz již obsahuje `asymptotic-sums.md`.
Následující argument rozepisuje tamější doplnění pro necelá t:
žádné neexistující derivace v nule ani neurčené rušení ořezů.

Pišme a=1/(2n)>0 a f_a(x)=x^t exp(−ax²). Pro libovolné celé
M≥1 zvolme celé R tak, že 2R>t+2M+1. Bernoulliho polynom
P_(2R) je již přesně definován v recovery1.2.11.2. Položme

```text
L_R(f) = −∫_0^1 f(x)dx + f(1)/2
         −Σ_(r=1)^R B_(2r) f^(2r−1)(1)/(2r)!
         −∫_1^∞ P_(2R)({x}) f^(2R)(x)dx/(2R)!.
```

Tato lineární funkcionála má smysl pro f_a i pro každé
x^(t+2j), 0≤j<M: u nuly se integruje jen samotná nezáporná
mocnina, derivace se vyhodnocují v1 a poslední integrál
konverguje díky t+2j−2R<−1. Eulerův vzorec od1 doN,
pak N→∞, dává přesnou rovnost

`Σ_(k≥1) f_a(k) = ∫_0^∞ f_a(x)dx + L_R(f_a)`.

Všechny derivace f_a v nekonečnu mizí a poslední integrál
je absolutně konvergentní; zde není potřeba žádná derivace
f_a v nule. Pro samotnou mocninu x^q, q≥0, stejný konečný
Eulerův vzorec a limitní odečtení hlavních mocnin dávají

```text
L_R(x^q) = lim_(N→∞) [Σ_(k=1)^N k^q − N^(q+1)/(q+1)
                     −N^q/2
                     −Σ_(r=1)^R B_(2r) q_falling(2r−1)
                                      N^(q−2r+1)/(2r)!]
         = ζ(−q),                  2R>q+1.
```

Poslední označení je právě Eulerovo analytické pokračování
zeta, již odvozené v recovery1.2.11.2; lze je také chápat
pouze jako definici této konkrétní konstanty. Ocas integrálu
je O(N^(q−2R+1)), takže limita existuje a nezávisí na dalším
zvýšení R. Pro q0 vyjde −1+1/2=−1/2, v souladu s ζ(0).

Zbývá doložit **kvantitativní** Taylorův zbytek uvnitř L_R.
Označme

`E_a(x)=x^t(exp(−ax²)−Σ_(j=0)^(M−1)(−ax²)^j/j!)`.

Na[0,1] je |E_a(x)|≤C a^M x^(t+2M); hodnoty všech potřebných
derivací v1 jsou O(a^M). Pro 1≤x≤a^(−1/2) můžeme derivovat
absolutně konvergentní řadu a dostaneme

```text
|E_a^(2R)(x)|
 ≤ x^(t−2R) Σ_(j≥M) (ax²)^j |(t+2j)_falling(2R)|/j!
 ≤ C a^M x^(t+2M−2R).
```

Poslední konstanta je konečná, protože součet polynomu vj
děleného j! konverguje a ax²≤1. Volba2R>t+2M+1 zajišťuje,
že integrál této majoranty od1 do a^(−1/2) je O(a^M).

Na ocasu x≥a^(−1/2) oddělíme Gaussovu funkci a konečný polynom.
Substituce y=√a x dává

```text
∫_(a^−1/2)^∞ |(x^t exp(−ax²))^(2R)| dx
 = a^(R−(t+1)/2) ∫_1^∞ |(y^t exp(−y²))^(2R)| dy
 = O(a^(R−(t+1)/2)).
```

Integral v y je konečný: na[1,∞) má každá derivace pouze
konečně mnoho mocninných faktorů krát exp(−y²). Každý odečtený
monom má tentýž řád integrálu,

`a^j ∫_(a^−1/2)^∞ x^(t+2j−2R)dx = O(a^(R−(t+1)/2))`.

Exponent R−(t+1)/2 je větší než M. Proto celý ocas je O(a^M).
Omezenost periodického P_(2R) nyní dává L_R(E_a)=O(a^M).
Linearita tedy opravňuje skutečný konečný rozvoj

`L_R(f_a)=Σ_(j=0)^(M−1)(−a)^j ζ(−t−2j)/j!+O(a^M)`.

Gaussův integrál je přesně
`∫_0^∞ x^t exp(−ax²)dx=Γ((t+1)/2)/(2a^((t+1)/2))`.
Přidáním k0, s0^0=1, konečně získáme pro každé pevné t≥0
a každý celý M≥1

```text
Σ_(k≥0) k^t exp(−k²/(2n))
 = (2n)^((t+1)/2) Γ((t+1)/2)/2 + [t=0]
   + Σ_(j=0)^(M−1) (−1)^j ζ(−t−2j)/(j!(2n)^j)
   + O(n^−M).
```

Konstanta závisí na t,M, nikoli na n. Pro t0 je celkový
konstantní člen1+ζ(0)=1/2. Pro ostatní nezáporná celá t
je výsledek shodný s hladkým Eulerovým postupem; pro necelá t
jsou všechny singularity v nule obejity integrací od1.
To dokazuje celý rozsah14(d), nikoli pouze celé exponenty
skutečně použité v14(c). Není potřeba nový numerický běh.

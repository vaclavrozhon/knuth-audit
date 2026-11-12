# MPR89 — vážené nezávislé Bernoulliho proměnné

D189, 7. listopadu 2026. Celé zadání p20/file40 a odpověď
p383/file403, včetně dovětku, byly posouzeny v původní sazbě.
Odpovídají autorovu PS p20/file26 a p40/file46. Původní svazek1
byl přímo zobrazen na p107/file122 a p502/file517; z tohoto odkazu
se přebírá jen tvrzení a důkaz22(a), které dovětek89 potřebuje.
Tím se neuzavírají celé cizí stránky ani další části22.

## Rozdělení, historie a všechny intervaly

B(p1,…,pn) je součinové Bernoulliho rozdělení: pravděpodobnost
vektoru x∈{0,1}^n je součin faktorů pi pro xi=1 a1−pi pro xi=0.
To je tatáž definice jako v61(d), již úplně posouzená vD163.
Pro pi=0 nebo1 používáme tyto dva přímo uvedené faktory, nikoli
nevymezené0^0. Součet pravděpodobností je Π(pi+1−pi)=1.
Sečtením přes libovolné neuvedené souřadnice vznikne faktor1;
všechny souřadnice jsou tedy vzájemně nezávislé a EXi=pi.

Každé ci je pevné konečné nezáporné číslo. Pro i=1,…,n položme

```
Yi=ci(Xi−pi),   ai=−cipi,   bi=ci(1−pi),   Y0=0.
```

Pro Xi=0 je Yi=ai, pro Xi=1 je Yi=bi. Nerovnost ai≤bi plyne
z ci≥0; rozdíl bi−ai je přesně ci. Každá proměnná je omezená
a integrabilní. Pro úplnou minulost Fi−1=σ(X1,…,Xi−1) platí

```
E(Yi|Fi−1)=ci(E(Xi|Fi−1)−pi)=0.
```

Historie Y0,…,Yi−1 je obsažena ve Fi−1, i když některá ci=0
a transformace ztratí informaci. Věžová identita proto dává
E(Yi|Y0,…,Yi−1)=0. Posloupnost je férová přesně v potřebném
smyslu; nevyžaduje se invertibilita transformace. Při pi=0,1
je Yi=0 skoro jistě. Při ci=0 je Yi=ai=bi=0 pro oba stavy.

## Ocasová mez a její doména

D100 v `sequential-mpr-009-010.md` již dokazuje každý krok
exponenciálního odhadu pro pevné šířky. Zde jsou všechny ai,bi
deterministické, tedy jeho podmínky přesně platí; F160 týkající
se náhodných šířek tento případ nezasahuje. S=ΣYi a V=Σci² dávají
pro λ>0

```
P(S≥x) ≤ exp(−λx+Vλ²/8).
```

Pro x>0,V>0 doplnění čtverce

```
−λx+Vλ²/8 = V(λ−4x/V)²/8 −2x²/V
```

ukazuje přípustné minimum λ=4x/V a přesně tištěnou pravou stranu.
Událost S≥x je právě ΣciXi≥Σcipi+x, takže součet ani práh
neobsahují žádný další faktor. Pro x=0 a V>0 stačí triviální
P(S≥0)≤1 (rovněž limita λ↓0). Záporné x nejsou doménou tohoto
kladného ocasového odhadu, stejně jako u zdrojového(37)/D100.

Pro V=0 jsou všechna ci=0 a S=0. Přesný výsledek je pak0
pro x>0 a1 pro x=0. To je standardní oddělení degenerované
normalizace; nepoužíváme0/0 v exponentu. Zahrnuje i případ
prázdného součtu n=0, pokud se připustí. Pro práh nad největší
možnou hodnotou součtu je událost prázdná a odhad zůstává platný.

## Celý dovětek a přesný odkaz1.2.10–22(a)

Při všech ci=1 má T=ΣXi generující funkci
G(z)=Π(1−pi+piz) a μ=ET=Σpi. To plyne rozvinutím součinu
přes všechny konečné atomy, tedy i při nulových/jistých pi.
Pro r>0 platí

```
1−pi+pir = 1+(r−1)pi ≤ exp((r−1)pi),
G(r) ≤ exp(μ(r−1)).
```

Použitá nerovnost1+u≤e^u je globální: e^u−1−u má derivaci
e^u−1 zápornou pro u<0 a kladnou pro u>0, tedy minimum0
v nule. Levé faktory jsou zde navíc kladné, neboť r>0.

Pro r>1 je {T≥μr}={r^T≥r^(μr)} a Markov dává

```
P(T≥μr) ≤ G(r)/r^(μr)
          ≤ exp(−μ(r ln r−r+1)) = (r^(−r)e^(r−1))^μ.
```

Pro0<r<1 je exponenciála klesající; stejná událost pro Markova
je nyní {T≤μr}. Vzniká přesně druhá potřebná větev22(a).
Pro r=1 jsou obě pravé strany1. Pro μ=0 jsou všechna pi=0,
T=0 skoro jistě; obě neostré události při prahu μr=0 mají
pravděpodobnost1 a pravá strana také1. Žádné děleníμ zde nebylo.
Tím jsou ověřeny i všechny mezikroky skutečně použité odpovědi22(a).

Pro μ>0,x>0 vezmeme r=1+x/μ. Odkaz tedy dává alternativní mez

```
P(T≥μ+x) ≤ exp(−(μ+x)ln(1+x/μ)+x),
```

zatímco89 dává exp(−2x²/n). První závisí naμ a má jiný tvar,
přesně jak říká dovětek; kniha netvrdí jednotné pořadí jejich
síly. Pro μ=0 a x>0 je skutečná pravděpodobnost0. Původní
strany107 a502 potvrzují číslo odkazu a oba neostré směry.
Další části22(b,c), poissonovský dovětek a bibliografická historie
Chernoffa nejsou tvrzením úlohy89 a nepřebíráme jejich audit.

## Kontrola vrstev a závěr

Manifest `mpr-089-weighted-errata.json` zaznamenává všech šest
lokálních vrstev errat a tři TeX zdroje s kontrolními součty.
Žádná použitelná oprava ani shoda pro zadaný rozsah nenalezena.
Jde o kontrolu existujících snapshotů, nikoli nový živý download.

Celá89 je doložena včetně dovětku. Bez nového nálezu, kandidáta,
bibliografické výjimky nebo matematického běhu. Staré důkazy
se používají v přesně uvedeném rozsahu a žádný test se neopakuje.

# §4.3.3D: převrácená hodnota a dělení

Kontrola 2.11.2026. Původní strany311–313 byly vizuálně přečteny,
stejně jako relevantní historická errata. Algoritmus R a převod
dělení na násobení jsou správné. C0104 je pouze drobná přísná
nerovnost při nulové chybě. Bibliografický odstavec o elementárních
funkcích zůstává součástí navazujícího kontextu.

## Inicializace a jeden krok R

Vstup v je normalizován do intervalu [1/2,1). Cílem je aproximace
1/v s absolutní chybou nejvýše2^(−n). Označme v'=floor(8v), tedy
celé číslo tvořené prvními třemi bity v; v' patří do{4,5,6,7}.
Inicializace je `z_0=floor(32/v')/4`, takže 1<=z_0<=2.
Chybu δ_0=1/v−z_0 rozdělíme na

```
eta_1 = (v'−8v)/(v v'),     eta_2 = (32/v'−floor(32/v'))/4.
```

Máme −1/2<eta_1<=0 a0<=eta_2<1/4, tudíž |δ_0|<1/2.
Z_0 leží na mřížce s krokem1/4, jak požaduje R2 pro k=0.

V iteraci k je V_k počátečních `2^(k+1)+3` bitů v. Nezaměňujme
2^(k+1) s2k+1: přesnost se v každém kroku přibližně zdvojnásobí.
Položme `h_k=2^(−2^(k+1)−1)` a

```
raw = 2 z_k−V_k z_k^2,
z_(k+1) = ceil(raw/h_k) h_k = raw+r_k,  0<=r_k<h_k.
```

Přímá algebra dává přesnou identitu

```
delta_(k+1) = v delta_k^2−z_k^2(v−V_k)−r_k.
```

Za indukčního předpokladu 0<z_k<=2 a |δ_k|<2^(−2^k) je první
nezáporný člen menší než2^(−2^(k+1)). Druhý nezáporný člen má mez

```
z_k^2(v−V_k)+r_k
 < 4*2^(−2^(k+1)−3)+2^(−2^(k+1)−1)
 = 2^(−2^(k+1)).
```

Rozdíl obou členů má absolutní hodnotu menší než stejná mez.
Tím je dokázán chybový invariant, včetně nulové chyby. Právě ta
vyžaduje opravu jedné přísné nerovnosti v tištěném důkazu; viz
[C0104](C0104-reciprocal-zero-error.md).

## Jednoduchý důkaz rozsahu

Místo tří případů na str.313 lze použít jedinou identitu

```
2z−V z^2 = 1/V−V(z−1/V)^2 <= 1/V <= 2,  pro V>=1/2.
```

Číslo2 je bodem mřížky s krokem h_k, takže zaokrouhlení nahoru
nemůže výsledek zvětšit nad2. Kladnost nového z plyne z již
dokázané chyby a1/v>=1. To uzavírá současnou indukci pro rozsah,
přesnost i počet zlomkových bitů. Argument platí také v první
iteraci a nevyžaduje pomocnou definici V_(−1).

Po ukončení je2^k>=n, a tedy chyba je menší než2^(−n).
Algoritmus provede nejméně jednu iteraci, i pokud n=1; to nevadí
správnosti ani časové mezi.

## Podíl a zbytek

Nechť U,V jsou nezáporná celá čísla menší než2^n, V>0. Pišme
d=bit_length(V) a v=V/2^d. Po spočtení aproximace z k1/v s chybou
nejvýše2^(−n) má `U z/2^d` od U/V vzdálenost menší než2^(−d),
tedy nejvýše1/2. Za předběžný celočíselný podíl vezmeme jeho dolní
celou část q. Přesný výpočet R=U−qV rozhodne poslední opravu:
je-li R<0, odečteme1 od q a přičteme V k R; je-li R>=V, provedeme
opačnou opravu. Jedna taková změna stačí, potom0<=R<V.

V kontrolním programu se používají ještě dva pomocné bity přesnosti;
obecný argument výše ukazuje, že pro tento účel stačí i knižní n.
Konečný zbytek a podíl se porovnávají s nezávislým `divmod(U,V)`.

## Časová mez

Každá iterace má dvě násobení a lineární práci; délky operandů
rostou geometricky. Po zahrnutí konstantního počtu bitů pro celou
část je uvedená mez `2T(4n)+2T(2n)+2T(n)+...+O(n)` oprávněná.
Je-li T(x)=x f(x) a f neklesá, je součet T přes tuto posloupnost
délkových mezí nejvýše T(8n), resp. přísně menší při konečném součtu.

Pro závěr O(T(n)) je vhodné výslovně ošetřit konstantní zvětšení
argumentu. Jeho platnost neplyne pro libovolně zvolenou funkci f
jen z monotónnosti. Násobení 8n-bitových operandů však lze rozdělit
na64 násobení n-bitových bloků a lineární sčítání. Multiplikátor
proto můžeme použít v této variantě a cenu větších operandů omezit
konstantním násobkem T(n). Menší úrovně geometrické řady dávají
totéž přímo z monotónnosti f. Takto dostáváme tvrzenou redukci
dělení na násobení s konstantním časovým faktorem, bez nepodloženého
předpokladu o libovolné funkci T.

Známé erratum na str.313 ze15.5.1998 doplňuje pouze koncovou tečku.
Všechny čtyři vrstvy byly prohledány i podle rovnic54–56 a popisu
Newtonovy metody. Obecné důkazy doplňuje `verify_fast_reciprocal.py`,
který používá přesné racionální hodnoty a kontroluje také každé
useknutí V_k, zaokrouhlení r_k a chybovou identitu.

Běh38256 skončil exit0; oba checkpointy prošly.16563 aproximací
převrácené hodnoty s74565 přesně kontrolovanými iteracemi; všechny
normalizované dyadické vstupy do14bitové přesnosti a další racionální
vstupy s cílovou přesností do4096 bitů.86870 úplných malých dělení
a210 velkých do16384 bitů prošlo proti divmod.191 předběžných podílů
potřebovalo zvýšit o1; zbývající byly správné bez opravy.

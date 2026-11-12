# V3-C0024 — rozsah pomocné fázové nerovnosti

**candidate / low**,2026-11-07. Kniha627/file638, odpověď5.2.1-42(a),
věty s g(x,y)≤g(x+ph,y+qh)+8N/(gh) a opačnou nerovností.
Původní sazba zobrazena: `images/insertion-file-638.png`.

Platný příklad: N=36,h=18,g=17 a permutace

    18,2,3,...,17,1,19,20,...,36.

Je18-uspořádaná, takže je možným výstupem prvního průchodu. V první
třídě jsou18<19, v poslední1<36, v ostatních i<i+18.
Volme x=1,y=18 a p=q=1. Obě hodnoty x,y jsou v jedné17-třídě;
také posunuté19,36 jsou v jedné17-třídě. Podmínky |p|,|q|≤g platí.
Protože gh=306>N, každá vybraná fáze má právě jeden existující prvek:

    g(1,18)=[K₁>K₁₈]=1,
    g(19,36)=[K₁₉>K₃₆]=0,
    8N/(gh)=288/306=16/17<1.

Neomezená pomocná nerovnost tedy neplatí. Není to srovnání s libovolným
nesouvisejícím grafem/modelovým vstupem: splněn je přímo Shellsortový
kontext, coprimalita, pořadí h>g a existence všech indexů.

**Proč zatím candidate:** okolní důkaz je asymptotický. Pro N≥gh platí
nerovnost správně. V `insertion-proof-42-first-second.md` je obecný důkaz
|g(x,y)−g(x',y')|≤4ceil(N/(gh)), z něj8N/(gh) při N≥gh, a samostatný
O(hN) argument pro gh>N. Celý požadovaný výsledek42(a) zůstává správný.
Možná oprava: před pomocným odhadem omezit N≥gh a uvést triviální druhý
režim, nebo zachovat obecnou mez O(N/(gh)+1).

Známá oprava2000 mění předchozí r(x,y)<N/(gh) na r(x,y)<N/(gh)+1.
Ta není naším nálezem; explicitní pozdější8N/(gh) nemění. Všech pět
vrstev prověřeno v `sources/phase-shift-bound-errata-review.json`.
Žádný výpočet ani enumerace; protipříklad má dva ruční indikátory.

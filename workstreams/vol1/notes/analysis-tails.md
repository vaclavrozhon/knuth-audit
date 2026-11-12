# §1.2.10: pravděpodobnosti velkých odchylek

Podklad: skutečně zobrazené s. 98, 104, 106–107, 502 a všechny vrstvy
errat. Kontrolujeme Čebyševovu nerovnost, (24)–(25), zobecnění pomocí
nezáporné funkce a celé úlohy 21–23. Novou chybu dodatku 2023 evidujeme
samostatně jako C0015 v `analysis-findings.md`.

## Obecné nerovnosti

Pro náhodnou veličinu X s konečnou střední hodnotou μ a rozptylem σ²
je při σ>0 a r>0
`Pr(|X−μ|>rσ)<1/r²`. Je-li pravděpodobnost vlevo kladná, plyne ostrá
nerovnost z `E((X−μ)²)>r²σ² Pr(|X−μ|>rσ)`. Je-li nulová, závěr je přímý.
Pro σ=0 je X=μ skoro jistě a událost je prázdná. Knižní výklad pro r≥1
je tudíž správný. Pro neostrou událost ≥ bychom obecně měli pouze ≤.

Pro nezápornou celočíselnou veličinu X s PGF G je při 0<x≤1
`Pr(X≤r)≤x^(−r)G(x)`, a při x≥1
`Pr(X≥r)≤x^(−r)G(x)`; r může být reálné. Důkaz spočívá v porovnání
indikátoru sledované události s x^(X−r) a v nezápornosti příspěvků
mimo událost. Pro x>1 a G(x)=∞ je odhad pouze triviální.
Horní indexy podlahy/stropu v knižním důkazu souhlasí s neostrými událostmi;
OCR znaky ≤ a ≥ opakovaně ztrácí.

Obecně potřebujeme f(t)≥s>0 na t≥r **a f(t)≥0 na celé podpoře X**.
Pak `[X≥r]≤f(X)/s`, takže `Pr(X≥r)≤E f(X)/s`.
Chybějící globální nezápornost prvního dotisku je známá oprava
z 30. října 2007; není to nový nález. Záměna f(t)=x^t a s=x^r
dává horní odhad (25).

## Úloha 21: binomické rozdělení

Nechť n≥1 je celé, 0<p<1, q=1−p a X je počet úspěchů v n nezávislých
pokusech s pravděpodobností p. Pro 0<ε<q minimalizujeme
`x^(−n(p+ε))(q+px)^n` v x≥1. Logaritmická derivace se vynuluje pro
`x=(p+ε)q/[p(q−ε)]`. Dostáváme

`Pr(X≥n(p+ε)) ≤ exp(−nD_p(ε))`,
`D_p(ε)=(p+ε)ln((p+ε)/p)+(q−ε)ln((q−ε)/q)`.

Pro hrubší knižní odhad stačí dvě nerovnosti:
`(p/(p+ε))^(p+ε) ≤ exp(−ε)` z ln u≤u−1 a
`(q−ε)ln(q/(q−ε))=ε−∑_{k≥2}ε^k/[k(k−1)q^(k−1)] ≤ ε−ε²/(2q)`.
Jejich spojením dostaneme `Pr(X≥n(p+ε))≤exp(−nε²/(2q))`.
Chybějící první člen ε v původní odpovědi opravují errata 1999.
Pro ε=q přejdeme k limitě; pro ε>q je událost prázdná; ε=0 dává odhad 1.
Záměnou úspěchu a neúspěchu vyjde
`Pr(X≤n(p−ε))≤exp(−nε²/(2p))`, se stejným ošetřením hranic.
Případy p=0,1 se posuzují jako deterministická rozdělení, nikoli dělením nulou.

Je-li p≥1/2, platí `D_p''(ε)=1/[(p+ε)(q−ε)]≥1/(pq)`,
a proto `D_p(ε)≥ε²/(2pq)`. Pro libovolné p platí D_p''≥4,
tedy D_p≥2ε². To dokazuje oba silnější odhady zmíněné v prvním dotisku.
Nový řadový člen přidaný 2023 je vadný; nález C0015 obsahuje dva
nezávislé přesné protipříklady i platné omezení oboru opraveného vzorce.

## Úloha 22: součet různých Bernoulliho veličin

Nechť X má PGF `G(z)=∏_{k=1}^n(q_k+p_k z)`, kde 0≤p_k≤1,
q_k=1−p_k, a μ=∑p_k. Výslovný obor p_k doplnila errata 2023.
Zvolíme x=r>0 v příslušném odhadu (24) nebo (25). Platí
`G(r)=∏(1+(r−1)p_k)≤exp((r−1)μ)`, tedy

`Pr(X≤μr)≤(r^(−r)exp(r−1))^μ` pro 0<r≤1,
`Pr(X≥μr)≤(r^(−r)exp(r−1))^μ` pro r≥1.

Položme δ=r−1. Záporný logaritmus základu je
`h(δ)=(1+δ)ln(1+δ)−δ`. Hlavní odhady dokazujeme bez spoléhání na
alternující řadu blízko její hranice:

- Na −1<δ≤0 je h''(δ)=1/(1+δ)≥1 a h(0)=h'(0)=0, tedy h≥δ²/2.
- Na 0≤δ≤1 je h≥δ²/3. Derivace rozdílu je ln(1+δ)−2δ/3;
  tato konkávní funkce je nezáporná na [0,1], protože na krajích je
  0 a ln2−2/3>0. Poslední ostrá nerovnost plyne například z
  ln2=2(1/3+(1/3)^3/3+…) >2/3.
- Pro každé δ≥0 platí h≥δ²/(2+δ). Nejprve
  ln(1+δ)≥2δ/(2+δ), protože derivace rozdílu je
  δ²/[(1+δ)(2+δ)²]≥0. Derivace h−δ²/(2+δ) je potom alespoň
  δ²/(2+δ)²≥0 a rozdíl v nule je nulový.

První dvě nerovnosti opravují znaménka exponentů podle errat 1999;
třetí je správný dodatek z 22. května 2023. V odhadu pravděpodobnosti
se každý exponent násobí μ. V bodě δ=−1 lze použít limitu r→0+;
pro μ=0 je X=0 jistě a odhady v zadání se čtou přímo jako 1≤1.

Pro část (c) pišme základ na jednotku μr jako
`c(r)=r^(−1)exp(1−1/r)`. Jeho logaritmická derivace je
`−1/r+1/r²<0` pro r>1, a c(r)→0. Proto c(r)<1/2 pro dostatečně
velká r a `Pr(X≥μr)≤2^(−μr)`.
Číselné meze c(2)<0.825 a c(4.32)<1/2 potvrzuje samostatná kontrola
racionálními intervaly logaritmu/exponenciály v `results/analysis-pgf.json`.
Errata 2023 opravují omylem vytištěnou rovnost na ostrou nerovnost.

Pro Poissonovo rozdělení s parametrem μ je G(r)=exp(μ(r−1)) přesně,
takže volba x=r dává stejný konečný odhad, jak správně poznamenává kniha.

## Úloha 23: záporné binomické rozdělení

Zde p>0 není pravděpodobnost; jde o parametr a q=p+1. Nynější zadání
povoluje každé reálné n>0. PGF `G(z)=(q−pz)^(−n)` má koeficienty
`n(n+1)…(n+k−1)p^k/(k! q^(n+k))`, které jsou nezáporné a mají součet 1.
Poloměr konvergence q/p>1 dovoluje níže uvedené optimalizační body.
Střední hodnota je np a rozptyl npq.

Pro 0≤ε<p a dolní ocas zvolíme
`x=(p−ε)q/[p(q−ε)]≤1`. Logaritmus odhadu dělený n je
`f_−(ε)=(p−ε)ln(p/(p−ε))+(q−ε)ln((q−ε)/q)`.
Platí f_−(0)=f_−'(0)=0 a
`f_−''(ε)=−1/[(p−ε)(q−ε)]≤−1/(pq)`.
Proto `Pr(X≤n(p−ε))≤exp(−nε²/(2pq))`.
V ε=p použijeme limitu; pro ε>p je událost prázdná.

Pro horní ocas při ε≥0 zvolíme
`x=(p+ε)q/[p(q+ε)]`, které leží v [1,q/p).
Logaritmus odhadu dělený n je
`f_+(ε)=(q+ε)ln(1+ε/q)−(p+ε)ln(1+ε/p)`.
Jeho derivace je
`ln(1−ε/[q(p+ε)])≤−ε/[q(p+ε)]`.
Na intervalu 0≤ε≤p je tato hodnota nejvýše −ε/(2pq), takže

`Pr(X≥n(p+ε))≤exp(−nε²/(4pq))` pro 0≤ε≤p.

To je právě vylepšený dodatek z roku 2024. Starší verze s 6pq byla
slabší, ale po opravě oboru v roce 1998 platná. Pro ε>p ponecháváme
obecný odhad exp(n f_+(ε)); kvadratický odhad se tam z uvedeného důkazu
odvozovat nesmí. Znaménka, optimalizační body i obory tak souhlasí
s opravenou odpovědí.

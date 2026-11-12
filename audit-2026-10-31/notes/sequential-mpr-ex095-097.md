# MPR95–97 — každý asymptotický kvantifikátor a každý ocas

D193–D195, 7. listopadu 2026. Celá zadání p20/file40 a odpovědi
p384/file404 přímo zobrazeny, stejně jako autorův PS p20/file26,
p40/file46 a p41/file47. Celý potřebný odkaz sv1 1.2.10–21
na p106/file121 a odpověď p502/file517 byl porovnán s původní
sazbou; pro97 také oba vzorce(24),(25) a jejich argumenty
na p104/file119. Cizí celé stránky se tím neuzavírají.

Používáme přesné knižní významy: a.s. znamená pravděpodobnost
konvergující k1 a q.s. znamená pravděpodobnost komplementu
O(n^(−K)) pro každé pevné K. Nezaměňujeme je za silnější
výrok o všech dostatečně velkých n na jedné nekonečné trajektorii.
Definice a uniformní unijní argument již úplně doložil D103.

## 95: celý zákon počtu červených a všechny malé časy

Při n přidáních je R_n=1+Σi=1..n Xi. D173 dává každému slovu
s a jedničkami a n−a nulami pravděpodobnost a!(n−a)!/(n+1)!.
Takových slov je binom(n,a); jejich součin je1/(n+1). Proto
R_n je rovnoměrné na{1,…,n+1}. To zahrnuje n=0 a jediný stav1.

Přesně tedy

```
P(R_n>100)=max(n−99,0)/(n+1),
P(R_n≤100)=min(100,n+1)/(n+1).
```

Tištěný výraz(n−99)/(n+1) se používá pro n≥99, tedy v relevantní
asymptotické oblasti; před dosažením100 přidání je událost prázdná.
Pro n≥99 je pravděpodobnost neúspěchu100/(n+1), která jde k0,
ale není O(n^(−2)): součin s n² roste do nekonečna. Tvrzení je
tedy a.s., ale nikoli q.s. Tištěný jednodušší svědek R_n=1 má
pravděpodobnost1/(n+1)≥1/(2n) pro n≥1 a sám ne-q.s. dokazuje.

Slovo „accumulates“ zde odkazuje na růst času v uvedené definici.
V jednom nekonečném modelu urna skutečně někdy překročí100
červených s pravděpodobností1: R_n neklesá a pravděpodobnost,
že dosud nepřekročila100, jde k0. To neříká nic jiného
o rychlosti této konvergence a nečiní konečný výrok q.s.

## 96: všechny horní meze a přesný rozsah prvního odkazu

Pro X~Bin(n,1/2) je pro x≥0 správná deterministická verze D100

```
P(|X−n/2|≥x) ≤ 2exp(−2x²/n),   n≥1.
```

Oba ocasy vyplývají z férových nezávislých přírůstků Xi−1/2
šířky1, druhý také z výměny hlav a znaků. Při x=0 je mez2
jen triviální. Původní sv1 úloha21 dává slabší exp(−ε²n)
pro jednotlivý ocas při p=q=1/2; její tištěné předpoklady a
obě znaménka jsou správné. Naše odvození přímo dokazuje všechny
potřebné instance ε=x/n, takže není převzata nedoložená věta.
Neauditujeme zde části obecného vychýleného případu, které96
nepotřebuje. Po konečném počtu malých n jsou všechny následující
logaritmy i odmocniny v požadovaném oboru.

Pro čtyři tištěné prahy dostaneme:

| část | práh | horní mez pravděpodobnosti neúspěchu |
|---|---|---|
| i | √n ln n | 2exp(−2(ln n)²) |
| ii | √(n ln n) | 2n^(−2) |
| iii | √(n ln ln n) | 2(ln n)^(−2) |
| iv | √n | 2exp(−2), samo nerozhoduje |

První tři meze jdou k0, tedy(i),(ii),(iii) jsou a.s.
Pro každý pevný K platí2(ln n)²≥K ln n, jakmile ln n≥K/2;
mez(i) je tedy O(n^(−K)) pro každé K, čili(i) je q.s.
Ostatní klasifikace vyžadují dolní meze; neodvozujeme je
z toho, že uvedená horní mez není dostatečně malá.

## 96: úplná potřebná binomická lokální asymptotika

Položme h=floor(n/2), η=n−2h∈{0,1} a b_n(j)=P(X=h+j).
Integrální důkaz v `F164-gambling-tail-constant.md` dal
pro q_h=binom(2h,h)/4^h přesné sevření

```
2/(π(2h+1)) ≤ q_h² ≤ 1/(πh),   h≥1.
```

Jeho integrační rekurence a oba směry jsou již doloženy;
zde je přebíráme bez nového výpočtu. Pro sudé n je b_n(0)=q_h.
Pro liché n je b_n(0)=(2h+1)/(2h+2)·q_h, což plyne přímo
z poměru dvou faktoriálů a mocnin2. Existují tedy absolutní
c,C>0, pro něž c n^(−1/2)≤b_n(0)≤C n^(−1/2) pro všechna
dostatečně velká n, obou parit.

Pro celé j≥0 v podpoře binomický poměr přesně dává

```
b_n(j)/b_n(0) = Πi=1..j (h+η−i+1)/(h+i)
             = Πi=1..j (1−d_i),
d_i=(2i−1−η)/(h+i).
```

Pro0≤j≤h/4 platí0≤d_i≤2i/h≤1/2. Z integrální identity
ln(1−d)=−∫0^d dt/(1−t) plyne ln(1−d)≥−2d v tomto
intervalu. Proto, včetně prázdného součinu j=0,

```
exp(−2j(j+1)/h) ≤ b_n(j)/b_n(0) ≤ 1.
```

Pro n≥5 je h≥2n/5, takže spodní mez lze oslabit na
exp(−5j(j+1)/n). Symetrie P(X=k)=P(X=n−k) pokrývá
i levou stranu středu. Pro každý pevný A>0 tedy všechny
přípustné celočíselné k s |k−n/2|≤A√n mají pravděpodobnost
Θ(n^(−1/2)), s konstantami závislými jen na A. To rigorózně
dokazuje potřebné tištěné tvrzení u k=√n, včetně jeho obvyklého
zaokrouhlení na binomickou mřížku. Nenutíme n/2±√n být celé
pro každé n a neodvozujeme žádný závěr z neexistujícího atomu.

Uvnitř |X−n/2|<√n je Θ(√n) atomů, každý má takovou
spodní mez. Jejich součet je oddělený od0 a nejvýše1,
tedy P(|X−n/2|<√n)=Θ(1). Samotná tato Θ(1) by ještě
nevyvracela konvergenci k1. Proto explicitně bereme také
anulus 2√n≤X−n/2≤3√n: pro velké n je v podpoře,
obsahuje Θ(√n) atomů a podle stejného uniformního odhadu
má pravděpodobnost alespoň pevnou kladnou konstantu.
Je podmnožinou neúspěchu(iv), takže(iv) není a.s. a tím
ani q.s. Tím je krátká tištěná argumentace úplně doplněna.

## 96: proč(ii) a(iii) nejsou q.s.

Zvolme j_n=ceil(√(n ln n)+1/2). Pro obě parity platí
h+j_n−n/2=j_n−η/2≥√(n ln n). Tento jediný atom tedy
porušuje ostrý interval(ii). Pro dostatečně velké n je
j_n≤h/4 a j_n(j_n+1)/n≤2 ln n. Důvodem je
√(n ln n)/n→0 a relativní chyba zaokrouhlení jde k0.
Přesné poměrové sevření výše proto dává

```
P(neplatí(ii)) ≥ b_n(j_n)
              ≥ c n^(−1/2) exp(−10 ln n)
              = c n^(−21/2).
```

Tato dolní mez není O(n^(−11)), protože n^11 krát pravděpodobnost
roste alespoň jako c√n. Proto(ii) není q.s. Pro velké n je
√(n ln ln n)≤√(n ln n); neúspěch(ii) je podmnožinou
neúspěchu(iii). Stejná dolní mez tedy vyvrací q.s. také u(iii).
Všechny části jsou tím skutečně klasifikovány, včetně posledního
tištěného „similar calculation“:
(i) q.s. i a.s.; (ii),(iii) pouze a.s.; (iv) ani jedno.

## F169: chybějící centrování v tištěné pravděpodobnosti96

PDF i PS však v prostředním kroku píší P(|X|<√n)=Θ(1).
X zůstává počtem hlav, nebyla provedena změna označení.
Pro n≥16 je √n≤n/4; protože X≥0,

```
P(|X|<√n) ≤ P(X≤n/4) ≤ exp(−n/8) → 0.
```

Poslední mez je již doložený jednostranný odhad s x=n/4.
To přímo odporuje tvrzené kladné asymptotické dolní meziΘ(1).
Lokální oprava je |X−n/2| místo |X|. Opravené tvrzení
i chybějící rozvedení anulu jsou dokázány výše. Nejde o chybu
zadání nebo hlavní klasifikace. F169 je low a mapuje pouze
p384/file404, nikoli platné zadání p20. Samostatná anglická
poznámka obsahuje přesný rozpor a rozsah opravy.

## 97: model, PGF a obě původní ocasové reference

V běžném hašovacím modelu jsou N=floor(n^(1+δ)) adres
nezávislé a rovnoměrné na n přihrádkách, δ>0 pevné. Pro pevnou
přihrádku H=Σi=1..N Ii, kde Ii mají Bernoulliho parametr1/n.
Konečné součinové rozvinutí tedy dává přesně

```
G(z)=E z^H=((n−1+z)/n)^N.
```

Vzorce sv1(24),(25) jsou přímo potvrzeny na p104. Pro a>1
implikuje H≥r nerovnost a^H≥a^r; pro0<a<1 ji implikuje
H≤r. Markov proto dává v obou případech a^(−r)G(a).
Prahy r nemusí být celé; události používají ceil(r), respektive
floor(r), přesně jako původní součtový důkaz. Každý jeho člen
má příslušný faktor a^(H−r)≥1 a přidání dalších nezáporných
členů pouze zvětšuje součet. V bodě a=1 jde o triviální mez1.
To dokládá obě reference i jejich zaokrouhlovací mezikroky.

Pro dolní ocas položme r=n^δ/2, takže N=floor(2nr).
Pro a=1/2 dostaneme

```
P(H≤r) ≤ 2^r(1−1/(2n))^floor(2nr)
        ≤ 2^r(1−1/(2n))^(2nr−1)
        ≤ 2^(r+1)e^(−r).
```

První směr po odstranění podlahy používá0<1−1/(2n)<1
a floor(2nr)≥2nr−1. Poslední krok rozloží mocninu na
(1−1/(2n))^(−1)≤2 a (1−1/(2n))^(2nr)≤e^(−r).
Nerovnost1−u≤e^(−u) již byla doložena vD189 jako1+u≤e^u.
Tak je ověřen i tištěný faktor2, ne pouze řád exponentu.

Pro horní ocas zvolme r=2n^δ, takže N=floor(nr/2).
S a=2 je celý řetězec

```
P(H≥r) ≤ 2^(−r)(1+1/n)^floor(nr/2)
        ≤ 2^(−r)(1+1/n)^(nr/2)
        ≤ 2^(−r)e^(r/2).
```

Tentokrát je základ>1 a floor(nr/2)≤nr/2. Poslední
nerovnost opět plyne z1+u≤e^u. Oba řetězce platí i n=1;
asymptotické tvrzení nezávisí na konečně mnoha malých n.

Z1/2<ln2<1, což plyne integrací1/t na[1,2], jsou konstanty
c1=(1−ln2)/2 a c2=2ln2−1 obě kladné. Pro každou
přihrádku je tedy pravděpodobnost selhání požadovaného
intervalu nejvýše

```
2exp(−c1 n^δ)+exp(−c2 n^δ).
```

Použité neostré ocasy případně zahrnují i hraniční dobré stavy,
což horní mezi nevadí. Máme dokonce silnější ostré vymezení
kromě zanedbatelných chyb. Meze jsou stejné pro všechny
přihrádky. Unijní mez proto přidá jen faktor n; nezávislost
různých H není potřebná a ve skutečnosti obecně neplatí.

Pro libovolné pevné K zvolme celé j tak velké, že δj>K+1.
Exponenciální řada e^(c n^δ)≥(c n^δ)^j/j! dává
n e^(−c n^δ)≤j!c^(−j)n^(1−δj)=O(n^(−K)).
Tím je výrok o všech n přihrádkách q.s. dokázán se všemi
kvantifikátory. Slovo „exponentially“ zde znamená exponenciálu
v počtu n^δ, nikoli nezbytně v n; každý pevný δ>0 stačí.

## Primární citace97 a přesné uzavření

[Autorský článek Knuth–Motwani–Pittel](https://arxiv.org/abs/math/9201303)
byl uložen jako `sources/knuth-motwani-pittel-1990.pdf`.
Jeho původní p8–9 byly přímo zobrazeny: Lemma1 obsahuje stejný
PGF, oba podlahové odhady a přechod od jedné adresátky ke všem.
Článek pracuje ve své aplikaci s0<δ<1/2; žádný z těchto
ocasových kroků horní omezeníδ nepoužívá, jak úplný důkaz výše
ukazuje. Nepřebíráme audit celého algoritmu manželství ani
ostatní lemmata. [Obsah vydavatele](https://onlinelibrary.wiley.com/toc/10982418/1990/1/1)
potvrzuje autory, rok1990, svazek1 a rozsah1–14.

Všech šest vrstev errat a tři TeX zdroje jsou v manifestu
`mpr-095-097-tails-errata.json`. Shody pro historickou p196
se týkají úlohy101, jiné92 se týká pozdějšího přesného pokrytí;
žádná není opravou96 nebo tvrzení95–97.

Celé95–97 mají důkaz každé části, původního mezikroku i odkazu
v uvedeném rozsahu. Jediný nový nález je F169 low. Žádná nová
bibliografická výjimka, numerický běh, census nebo restart.
File40 je v celém rozsahu83–97 posouzen; file404 zůstává
partial pro98–99. Starší partial důkazy jinde se nemění.

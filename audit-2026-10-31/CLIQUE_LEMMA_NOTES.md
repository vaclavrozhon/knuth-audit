# Další kontroly lokálního lemmatu: SAT 348, 352, 354–356

Kontrola 31. 10. 2026. Níže oddělujeme chyby v zápisu, neplatný
mezikrok důkazu a chybějící okrajovou podmínku. Samotná clique věta
po doplnění pokrytí všech vrcholů platí; její opravený důkaz je níže.

## F038: koeficient derivované řady v 348

Odpověď 348, str. 617 (autorův Pre-Fascicle 6A str. 253), má uvnitř
sumy přes m koeficient a_n. Správně je a_m:

`f^(n)(w)=Σ_(m≥n) m^(underline n) a_m w^(m−n)`.

Pro f(z)=1/(1−2z), n=0 a r=1/4 je levá strana 2, zatímco tiskovaný
výraz s a_0=1 dává 4/3. Není to otázka odhadu zbytku ani konvergence:
obě řady jsou v tomto bodě absolutně konvergentní.

Pringsheimova věta a postup důkazu jsou správné po této opravě.
Je-li ρe^(iφ) singulární bod na kružnici konvergence, Taylorova řada
kolem re^(iφ) má poloměr právě ρ−r. Kdyby ρ samo nebylo singulární,
řada kolem r by měla poloměr větší než ρ−r: všechny body uzavřeného
kruhu se středem r a poloměrem ρ−r kromě ρ leží uvnitř původního
kruhu konvergence a v ρ by existovalo analytické pokračování.
Kompaktnost dá kladnou rezervu. Nezáporné koeficienty a správný vzorec
derivace přitom dávají `|f^(n)(re^(iφ))|≤f^(n)(r)`, tedy řada kolem
re^(iφ) nemůže mít menší poloměr než řada kolem r. To je spor.

## C007: slabý, ale pravdivý podíl v odpovědi 352

Na str. 618 je z 344(e) vyvozeno `M_(G\i)/M_G≥1−θ_i`.
Tato nerovnost je pravdivá, ale sama neprokazuje požadovanou mez
`E_i≤θ_i/(1−θ_i)`: levá strana je totiž 1+E_i a je vždy alespoň 1.
Užitečný důsledek 344(e) má obrácený podíl,
`M_G/M_(G\i)≥1−θ_i`. Potom `1+E_i≤1/(1−θ_i)` dává výsledek.

Zatím jde o **kandidáta na opravu důkazu**, ne potvrzené nepravdivé
tvrzení. Čtenář může správnou nerovnost přímo převzít z odkazované
344(e). PDF i autorův PS mají stejnou podobu. Tuto položku nepočítáme
mezi doložené chyby a nemícháme ji s obráceným znaménkem v 355.

## F039: obrácená závěrečná nerovnost v 355

Odpověď 355 na str. 618 (PS str. 254) končí `E_j>1/δ`.
Z předchozího řádku plyne naopak `E_j<1/δ`; obecně má platit
neostrá mez ze zadání. Pro jedinou hranu a p₁=p₂=1/4 je
`M*(z)=1−z/2`, δ=1 a E₁=E₂=1/2. Tiskovaná závěrečná nerovnost
tedy tvrdí 1/2>1.

Bez dodatečných předpokladů nelze ani předchozí nerovnost dělat
ostrou: pro stejnou hranu a p=(1/2,0) je δ=1 a po zvýšení p₁
na p₁(1+δ)=1 vyjde M=0. Vrchol přitom není izolovaný v G.

Úplný opravený důkaz je krátký. Bod p*=(1+δ)p leží na hranici
uzávěru R. Zvýšení pouze p_j na (1+δ)p_j dává bod q≤p*, takže
M(q)≥0. Multiafinita v p_j pak dává

`0≤M(q)=M(p)−δ p_j M_(G\N[j])(p)`.

Po vydělení M(p)>0 dostaneme δ E_j≤1. Důkaz pokrývá izolované
vrcholy i nulové souřadnice. Pro p=0 lze slack chápat jako nekonečný
a všechny E_j=0. Část354 plyne přímo derivací M*(1)/M*(z) v z=1;
součet jejích příspěvků je Σ_j E_j.

## F040: index minima v zadání 356(b)

Na str. 349 (PS str. 165) je minimum indexováno `i—j in G`.
Index j zde označuje **kliku U_j**, nikoli sousední vrchol grafu.
Správně tedy minimum běží přes `j: i∈U_j`.

U grafu s jedinou hranou 1—2 a jedinou klikou U₁={1,2} by tisk
pro i=1 požadoval θ₁₂ a Σ₂, které vůbec nejsou definované.
Odpověď356(b) používá příslušnost i∈U_j správně. Známé erratum
ze 17.8.2017 opravuje v tomto řádku pouze odkaz na Theorems M a S;
index minima neopravuje.

## F041: překrývající se kliky porušují mezikrok důkazu356(a)

Na str. 618 (PS str. 254) se používá rozklad

`X_k=(S∩U_(j_k))\X_(k−1), Y_k=Y∪X₁∪…∪X_(k−1)`.

Následující použití indukčního předpokladu vyžaduje
`Y_k∩U_(j_k)=∅`, což tento rozklad nezaručuje. Nejde pouze
o opomenutí všech dřívějších X v odčítání: rozdělovat podle prvního
výskytu v klikách by stále nestačilo.

Přesný protipříklad k použité podmíněné mezi:

- Vrcholy {i,a,b}, G=K₃; A_i je prázdná událost, A_a a A_b jsou
  disjunktní a mají obě pravděpodobnost 2/5.
- U₀={i}, U₁={i,a}, U₂={i,a,b}.
- Všechny θ_(i,j)=0; θ_(a,1)=2/3 a θ_(a,2)=θ_(b,2)=2/5.
- Součty na klikách jsou 0,2/3,4/5. Podmínky zadání jsou splněny:
  pro a dávají obě meze 2/5 a pro b jediná mez 2/5.
- Při j₀=0 a S={a,b} je X₁={a}, X₂={b}, Y₂={a}.
  Důkaz tvrdí `Pr(A_b | ¬A_a)≤θ_(b,2)=2/5`, ale skutečnost
  je `(2/5)/(3/5)=2/3`.

Oprava přiřadí vrchol **poslední** klice, ve které se vyskytuje:

`X_k=(S∩U_(j_k)) \ ⋃_(h>k) U_(j_h)`.

Pak je Y_k od U_(j_k) disjunktní, jednotlivá X_k tvoří rozklad X
a pro neprázdné X_k máme |Y_k|<|S|. Stejný princip je třeba použít
i v závěrečném součinu přes všechny kliky; obyčejné prefixové sjednocení
W_k se s příští klikou může překrývat. Oba projevy vedeme jako jedinou
chybu v zacházení s překryvem, nikoli jako dva nálezy.

## F042: pokrytí hran neomezuje nepokryté izolované vrcholy

Zadání356 požaduje pokrytí všech **hran**, nikoli vrcholů.
Vezměme prázdný graf na {1,2}, jedinou kliku U₁={1}, θ₁₁=0,
a p=(0,1). Všechny předpoklady jsou splněny, ale
`M_G=(1−p₁)(1−p₂)=0`, takže p∉R(G).

Stačí požadovat také `⋃U_j=V(G)`, případně zvlášť p_i<1 pro
nepokryté izolované vrcholy. Pokrytí vrcholů je jednodušší a dělá
i minimum356(b) neprázdné. V356(c) je u izolovaných vrcholů přirozené
stanovit p_i=θ_i, místo nedefinovaného maxima přes prázdnou množinu.
Jde o okrajovou chybějící podmínku, ne o selhání metody pro grafy
bez izolovaných vrcholů.

## Úplný opravený důkaz356

Předpokládejme, že kliky pokrývají všechny vrcholy i hrany. Pro
události s (133) souběžně indukujeme kladnost pravděpodobnosti
vyhnutí a podmíněnou mez ze zadání.

Kladnost pro S plyne po vybrání kliky U_j s S∩U_j≠∅. Při
Y=S\U_j je |Y|<|S| a indukční mez pro jednotlivé l∈S∩U_j dává
`Pr(vyhneme se S)≥Pr(vyhneme se Y)(1−Σ_j)>0`.

Pro podmíněnou mez zafixujme i∈U_j a S∩U_j=∅. Rozdělme S na
sousedy X obsažené v klikách s i a zbytek Y. Podmínka (133) dává

`Pr(A_i | vyhneme se S)≤p_i/Pr(vyhneme se X | vyhneme se Y)`.

Rozklad podle posledního výskytu, uvedený u F041, dovoluje použít
indukci v každém bloku. Sjednocovací mez a řetězové pravidlo dávají
do jmenovatele nejméně `Π_(k≠j,i∈U_k)(1+θ_(i,k)−Σ_k)`.
Předpoklad zadání tedy dává požadované θ_(i,j). Prázdné bloky
mají pravděpodobnost 1 a odhad platí také pro ně.

Posledními výskyty rozdělme i celou množinu vrcholů do bloků
`D_k=U_k\⋃_(h>k)U_h`. Předchozí bloky jsou disjunktní od U_k,
takže stejný argument dává celkové vyhnutí nejméně
`Π_k(1−Σ_k)>0`. Důkaz platí pro všechny soustavy událostí splňující
(133); Shearerova obrácená konstrukce pak vynucuje p∈R(G).

Pro356(b) podmiňme na vyhnutí všem událostem mimo U_j. Každá
podmíněná pravděpodobnost uvnitř kliky je nejvýše θ_(l,j).
Další podmínění na vyhnutí ostatním členům kliky dává
`q_i≤θ_(i,j)/(1+θ_(i,j)−Σ_j)`. Pro krajní rozdělení platí
`E_i=q_i/(1−q_i)`, takže `E_i≤θ_(i,j)/(1−Σ_j)` pro každou
kliku obsahující i, jak tvrdí opravené minimum.

Část(c) je specializace na kliky tvořené jednotlivými hranami.
Protože θ_i,θ_j<1/2, mají součet <1. Nejmenší přípustná mez přes
hrany i—j je součin ze zadání dělený největším (1−θ_j).
Izolované vrcholy řešíme singletonovými klikami s p_i=θ_i.

## Doklady a stav

Všechny označené tištěné výrazy byly porovnány s vykresleným PDF
a původním PS. Odpovídající opravy v `all4b` a `all4f6` nenalezeny;
známá oprava odkazu u356(b) je výslovně oddělena. Fyzická kniha
dosud nebyla zkontrolována. `check_clique_lemma.py` ověřuje přesně
podmíněné meze, výsledný součin, příslušnost R a opravené rozklady
včetně překrývajících se klik; rozsahy jsou v `results/clique_lemma.json`.

Bibliografická kontrola potvrzuje citovanou práci
[Kolipaka–Szegedy–Xu, 2012](https://link.springer.com/chapter/10.1007/978-3-642-32512-0_51).
Veřejná stránka vydavatele poskytla jen abstrakt, ne celý text.
Na jeho neviděném důkazu žádný z našich závěrů nezakládáme.

## Další položky k prověření

- Hlavní text u(150) v OCR říká, že Case1 běží rychleji než Case2,
  ačkoli odpověď349 dává průměry7 a≈1.56. Nejprve ověřit skutečný
  tisk a přesný běh AlgorithmM; dosud nezařazeno mezi nálezy.
- Odpověď357 má v krajním případě (p,q)=(1,0) údaj y=1.
  Ověřit původní definici pole v(155), osu ve Fig.94 i obraz stránky.
  Dosud nezařazeno mezi nálezy.

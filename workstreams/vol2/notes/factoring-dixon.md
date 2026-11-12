# §4.5.4: Dixonův algoritmus, věta D a úlohy 30–31

Matematická část na str. 401–402 a úlohy 30–31 na 414–415/664
jsou ověřeny. Původní stránky byly přečteny vizuálně. Níže je
obecný důkaz včetně zaokrouhlení parametrů, podmíněných
pravděpodobností a omezeného času. Nevznikl nový nález.

## 1. Počet použitelných čtverců: úloha 30

Nechť N>1 je liché číslo, `p_1<...<p_m` jsou prvočísla
nedělící N a r=2s je nezáporné sudé celé číslo takové, že
`p_m^r<=N`. Prvočíselný rozklad N zapisujme jako
`N=product_i q_i^a_i`, kde q_i jsou různá prvočísla;
d označuje jejich počet. Číslo hladké vzhledem k bázi
`p_1,...,p_m` má všechny prvočinitele v této bázi.
Dokážeme, že alespoň `m^r/r!` hodnot `0<X<N` má hladký
nejmenší nezáporný zbytek `X² mod N`.

Uvažujme množinu E všech vektorů `e=(e_1,...,e_m)`
nezáporných celých čísel se součtem nejvýše s. Jejich počet
je `|E|=binom(m+s,s)`. Každému přiřadíme celé číslo
`h(e)=product_j p_j^e_j` a d znamének: v i-té souřadnici
rozlišujeme, zda h(e) je čtvercem modulo q_i. Jde o
Legendreovy symboly, jejichž násobnost byla dokázána v
[primality-jacobi.md](primality-jacobi.md), §1. Žádné
znaménko není nula. Nechť n_a je počet vektorů s daným
znaménkovým vzorem a.

Pokud e a f mají stejný vzor, `h(e+f)` je čtvercem modulo
každé q_i. Každý nenulový kořen se jednoznačně zvedá
z q_i^j na q_i^(j+1): při nahrazení y číslem y+t*q_i^j
se nový zbytek mění o `2yt*q_i^j`, a 2y je invertibilní
modulo q_i. Proto máme právě dva kořeny modulo q_i^a_i.
Čínská věta o zbytcích pak dává právě `2^d` kořenů modulo N.

Pro pevný součet g=e+f existuje nejvýše `binom(2s,s)`
uspořádaných dvojic e,f z E. Tento stručný krok odpovědi
lze doplnit takto. Vytvořme 2s označených předmětů:
g_j předmětů barvy j a zbývajících `2s-sum g_j` pomocné
barvy. Dvojici e,f přiřadíme podmnožinu s předmětů,
která obsahuje prvních e_j předmětů každé barvy j a prvních
`s-sum e_j` předmětů pomocné barvy. Dostatek pomocných
předmětů plyne z `sum f_j<=s`. Toto přiřazení je prosté.

Celkem máme `sum_a n_a²` dvojic se stejným vzorem. Každé
výsledné g určuje jiné celé číslo h(g), podle jednoznačnosti
prvočíselného rozkladu. Platí `h(g)<=p_m^(2s)<=N` a
`gcd(h(g),N)=1`; tedy ve skutečnosti h(g)<N. Různé tyto
hodnoty mají disjunktní množiny kořenů X. Počet vhodných X je
alespoň

```
2^d * sum_a n_a² / binom(2s,s)
  >= |E|² / binom(2s,s)
  >= (m^s/s!)² / ((2s)!/(s!²))
   = m^r/r!.                                                   (1)
```

První nerovnost je Cauchyho–Schwarzova nerovnost pro 2^d
tříd, včetně prázdných. Druhá používá
`binom(m+s,s)>=m^s/s!`. Důkaz funguje i pro r=0, kdy
h=1 a N má alespoň dva kořeny jednotky. N=1 není obvyklý
faktorizační vstup; samotné slovní „odd number“ v zadání
čteme v tomto kontextu s N>1. Bez této konvence by r=0,N=1
byl degenerovanou výjimkou, nikoli problémem věty D.

Při rovnoměrné volbě X z 1,...,N−1 je tudíž pravděpodobnost
výstupu nejméně `m^r/(r!*(N-1))`, a tím i knižní slabší
`P>=m^r/(r!*N)`. Není nutné, aby p_j byly první prvočísla;
to je využito až při optimalizaci času.

## 2. Sběr relací a pravděpodobnost úspěchu

Nyní předpokládejme d>=2. První m prvočísel byla vyzkoušena
jako dělitele N; žádné N nedělí, a proto je N liché.
Pro každý nový nezávislý rovnoměrný X vypočteme `V=X² mod N`.
Je-li V=0, pak `1<gcd(X,N)<N`: první ostrá nerovnost plyne
z N|X², druhá z 0<X<N. Jinak vyzkoušíme prvočísla báze.
Zbytek po jejich odstranění je 1 právě pro použitelnou relaci.

Počet relací z pevně daných M nezávislých voleb má binomické
rozdělení s parametry M,P. Jeho střední hodnota je μ=MP
a variance MP(1−P)<μ. Při dřívějším nalezení faktoru už
není třeba pokračovat; pro analýzu lze další volby předem
doplnit. Pokud nastane V=0, algoritmus je úspěšný nezávisle
na počtu hladkých relací.

Každá relace má m parit exponentů. Nejvýše m příchozích
řádků může zvětšit jejich lineární obal nad tělesem se
dvěma prvky. Z prvních m+k výstupů proto alespoň k vyvolá
test kongruence čtverců. Podmiňme se historií a novou hodnotou V.
Čerstvé X je rovnoměrné mezi přesně 2^d kořeny V; násobení
pevnou jednotkou z předchozích řádků tuto rovnoměrnost
zachovává. Pouze dvě možnosti dávají triviální kongruenci.
Podmíněná pravděpodobnost selhání je tedy `2^(1-d)<=1/2`.
Násobením podmíněných mezí, bez předpokladu nezávislosti
odvozených relací, dostáváme mez `2^-k`.

Zde jsou potřebné nesoudělnosti splněny výslovně. Problém
[C0159](C0159-factor-base-coprimality.md) v obecněji napsané
úloze 13 se na Dixonovo použití nepřenáší.

## 3. Binomická odchylka: úloha 31

Nechť Y je počet relací a μ=MP>=4m. Pro nezápornou náhodnou
veličinu `2^-Y` použijme Markovovu nerovnost:

```
Pr(Y<=2m) <= 4^m * E(2^-Y)
           = 4^m * (1-P/2)^M
          <= exp(2m*ln2 - MP/2)
          <= exp((2*ln2-2)*m)
          <= exp(-m/2).                                        (2)
```

Použili jsme `1-u<=exp(-u)` a `ln2<3/4`. Poslední vztah
plyne například z liché řady
`ln2=2*sum_(j>=0) (1/3)^(2j+1)/(2j+1)` a její geometrické
majoranty `2*(1/3)/(1-1/9)=3/4`, s ostrou nerovností pro j>0.
Platí tedy i požadovaná mez pro méně než 2m výstupů.

Odpověď 664 dosazuje MP=4m. Pro skutečné MP>=4m lze buď
použít (2), nebo každou Bernoulliho zkoušku nezávisle
proředit na pravděpodobnost 4m/M. Tím se počet úspěchů
jen zmenší. V odpovědi tedy není třeba požadovat, aby
skutečná neznámá pravděpodobnost P dávala rovnost.

## 4. Volba parametrů a asymptotika na 401–402

Píšeme `L=ln N`, `l=ln L`, `H=sqrt(L*l/2)`. Všechny další
odhady platí pro dostatečně velké N; konečně mnoho menších
vstupů lze vyřídit zkoušením dělitelů.
Zvolme nejbližší kladné sudé celé číslo

```
r=sqrt(2L/l)+theta, |theta|<=1.
```

Spočteme celočíselnou odmocninu `B=floor(N^(1/r))` a vezmeme
všechna prvočísla nejvýše B. Poslední označme p_m a položme
h=ln p_m. Bertrandův postulát zaručuje `h=L/r+O(1)`.
Je proto současně splněno `p_m^r<=N` i tištěná podmínka
`r=L/h+O(1/l)`. Není dovoleno zaokrouhlit p_m směrem nahoru
a bez ověření použít (1).
Pro dostatečně velké N je navíc `0<=L/h-r<2`, takže platí
i předchozí knižní definice `r=2*floor(L/(2h))`.

Rozvoj reciproké hodnoty r dává

```
h = H - theta*l/2 + O(1).
```

Klasický odhad počtu prvočísel
`pi(x)=x/ln x*(1+O(1/ln x))` dává přesně tištěný vztah
`ln m=h-ln h+O(1/h)`. Pro výslednou časovou mez by stačila
i Čebyševova slabší oboustranná mez `pi(x)=Theta(x/ln x)`;
není potřebný nový předpoklad o rozložení prvočísel. Dále

```
ln h = (l+ln l-ln2)/2 + o(1),
ln m = H - (theta+1)*l/2 + O(ln l).                            (3)
```

Pomocí Stirlingova odhadu `ln(r!)=r ln r-r+O(ln r)` dostáváme

```
ln(m^r/(r!*N)) = r ln m - ln(r!) - L
                = -sqrt(2L*l) + O(r ln l).                    (4)
```

Lze přímo zkontrolovat rušení zaokrouhlovacího členu:
`r*h=L+O(r)` a `ln(h*r)=ln L+O(r/L)`, takže levá strana
(4) je `-r*l+O(r+ln r)`. Člen `-theta*l` se vejde do
uvedené chyby, neboť l=o(r). Tím nevzniká nezapočtená
chyba velikosti H při přechodu k sudému r.

Položme `P_0=m^r/(r!*N)` a `M=ceil(4m/P_0)`.
Pak MP>=4m. Zkoušíme nejvýše M hodnot X a eliminaci
ukončíme nejpozději po 2m relacích. Čas zkoušení malých
dělitelů je `O(M*m*poly(L))`; eliminace potřebuje
`O(m^3*poly(L))`, podrobně v §5. Generování báze sítem
do B stojí `exp(H+O(l))*poly(L)` a není dominantní.
Z (3) a (4) vyplývá

```
ln(M*m*poly(L)) = sqrt(8L*l) + O(sqrt(L/l)*ln l),
ln(m^3*poly(L)) = (3/sqrt2)*sqrt(L*l) + O(l).
```

Proto eliminace nemění hlavní konstantu sqrt8. Jelikož
`ln l/l -> 0`, pro každé pevné c>sqrt8 je čas
`O(exp(c*sqrt(L*l))) = O(N^(c*sqrt(ln ln N/ln N)))`.

Podle §2–3 je pravděpodobnost selhání nejvýše
`exp(-m/2)+2^-m`. Z (3) plyne m/L→∞, a tedy tato
pravděpodobnost je dokonce o(1/N). Věta D je dokázána.

## 5. Velikost čísel v eliminaci a náhodné bity

Aby čas platil i s náklady na bity, nemusíme ukládat rostoucí
celočíselné exponenty. Každou relaci `(X,e)` normalizujeme na

```
z = X / product_j p_j^floor(e_j/2) mod N,
b_j=e_j mod2,     z²=product_j p_j^b_j mod N.                  (5)
```

Dělení znamená násobení modulární inverzí, která existuje.
Při spojení dvou normalizovaných řádků vynásobíme jejich z,
v každé souřadnici se dvěma jedničkami vydělíme jednou p_j
a nahradíme b jejich součtem modulo 2. Invariant (5) zůstane
zachován. Po vynulování b máme `z²=1 mod N`; kromě z=±1
vrací `gcd(z-1,N)` vlastní faktor. Tento postup uchovává
stejný poměr x/y jako eliminace F.

Nejvýše 2m vstupních řádků projde nejvýše m uloženými
řádky, každý průchod stojí O(m) modulárních operací.
Všechny z i předpočtené inverze mají O(L) bitů. S klasickou
aritmetikou tedy postačí O(m³ poly(L)) bitových operací.
Jde o provedení věty D; netvrdíme, že libovolná doslovná
implementace celočíselných exponentů F má jednotkovou
cenu za neomezeně velká čísla.

Pevnou horní mez času lze zachovat i při generování X
z nezávislých rovnoměrných bitů. Z b=ceil(log2(N−1)) bitů
vytvoříme u; přijmeme jej, je-li u<N−1, a položíme X=u+1.
Přijetí má pravděpodobnost alespoň 1/2 a podmíněná hodnota
X je přesně rovnoměrná. Každému ze M vzorků povolíme
`K=ceil(log2(M*N))+2` pokusů. Pravděpodobnost, že některý
vzorek nedokončíme, je nejvýše `M*2^-K<=1/(4N)`.
Je-li celý sběr dokončen, hodnoty zůstávají nezávislé
a rovnoměrné. Dodatečný čas O(M*L²) i pravděpodobnost
selhání odpovídají tvrzení věty. Žádná úspěšná větev
nevrací chybný faktor; neúspěch je explicitní ukončení
bez faktoru.

## 6. Prameny, errata a rozsah výpočtů

Původní [Dixonův článek](https://pages.cs.wisc.edu/~cs812-1/dixon.pdf),
Math. Comp. 36(153), 255–260 (1981), byl celý přečten včetně
všech šesti skenů. Jeho věta na 257 má hlavní konstantu
3sqrt2 pro průměrný čas. Knuthova sqrt8 a silná mez
selhání proto skutečně představují zesílení. Originál
uvádí přijetí rukopisu 5. září 1979. Rok objevu 1978
podporuje dobový odkaz na Carletonský report v
[Schnorrově konferenční verzi](https://link.springer.com/chapter/10.1007/3-540-10843-2_1),
reference 5; samotný report z roku 1978 nebyl získán.

[Schnorrův článek](https://www.sciencedirect.com/science/article/pii/0196677482900128),
J. Algorithms 3(2), 101–127 (1982), má správnou knižní
bibliografii a abstrakt potvrzuje další rigorózní zlepšení.
Přečteny byly metadata a abstrakty vydavatelů pro časopiseckou
i konferenční verzi; plný důkaz Schnorrova silnějšího výsledku
zde nepřebíráme jako vlastní ověření. Pro důkaz (1)–(5)
není potřebný.

Všechny čtyři vrstvy errat (`all2-prepre`, `all2-pre`,
`all2`, `err2`) byly prohledány podle stran i tématu.
Opravy na 402 se týkají pozdějšího odstavce o eliptických
křivkách; na 664 jsou opravy jiných odpovědí. Žádná
relevantní oprava Dixonova bloku ani 30–31 nebyla nalezena.

Program `verify_factoring_dixon.py` používá tři nezávislé
konečné kontroly: přímý průchod X versus dvojice exponentů
v (1), úplná vlákna čtvercových kořenů při normalizované
eliminaci a přesné racionální binomické ocasy versus
Markovův odhad. První část zahrnuje všechny liché N od 3
do 1023 a osm bází, i báze neobsahující první prvočísla.
Obecné důkazy výše nejsou odvozeny z experimentální shody.
Prošlo 6928 kombinatorických případů s 1362530 přímými
zbytky a 87556 dvojicemi exponentů; dále 3715 podmíněných
vláken s 15452 kořeny a 480 přesných binomických ocasů.
Číselné rozsahy, počty a doby jsou v `results/factoring-dixon.json`;
provenience a otisky souborů v `sources/factoring-dixon.json`.

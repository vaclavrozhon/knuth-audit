# D130 — celá MPR28(a–c), s převzatou F016

6. listopadu 2026. Celé zadání p15/file35 a odpověď p374–375/file394–395
přímo zobrazeny, také Pre-Fascicle5A p15/file21 a p31–32/file37–38.
Platné jádro starého P028 a přesný protipříklad F016 jsou převzaty.
Níže jsou doplněny všechny tištěné mezikroky, konce a konečnost
transformací. Staré úspěšné výpočty se neopakovaly.

## Společný model a každý dvoubitový koeficient

X je součet nezávislých bitů s parametry p_j∈[0,1], ∑p_j=np.
Funkce g má konečné reálné hodnoty na0,…,n, takže Eg(X) existuje.
Označení P_N(k) a nulové rozšíření mimo0≤k≤N přebíráme z D127.
Pro dvojici parametrů u=p_{n−1},v=p_n položme

    A=(1−u)(1−v),       B=u(1−v)+(1−u)v,       C=uv.

Jsou to pravděpodobnosti0,1,2 jedniček v posledních dvou bitech;
A+B+C=1, tedy také B=1−A−C. Součet Z ostatních bitů je na této
dvojici nezávislý. Proto pro každý k

    P_n(k)=A P_{n−2}(k)+B P_{n−2}(k−1)+C P_{n−2}(k−2),
    Eg(X)=∑_{k=0}^{n−2}P_{n−2}(k)h_k,
    h_k=A g(k)+B g(k+1)+C g(k+2).

První rovnost rozkládá všechny tři vzájemně disjunktní hodnoty
dvojice; druhá je konečné sečtení stejného rozkladu podle Z.
Obě zachovávají nulové či jisté bity. Při n<2 se žádná dvojice
nevybírá a závěry(a),(b) jsou bezprostřední; část(c) je v tomto
rozsahu zahrnuta přímými koncovými větvemi níže.

Pro u′=u+ε,v′=v−ε zůstává součet parametrů stejný a

    δ=u′v′−uv=ε(v−u)−ε².

Proto C′=C+δ, A′=1−u′−v′+u′v′=A+δ a B′=B−2δ. To dává

    h′_k−h_k=δ(g(k)−2g(k+1)+g(k+2)).

Pro fixované ostatní bity lze rovněž psát

    Eg(X)=αA+βB+γC,
    α=Eg(Z), β=Eg(Z+1), γ=Eg(Z+2),
    E′g(X)−Eg(X)=δK,       K=α−2β+γ.

Tím jsou konkrétně určeny i tři koeficienty použité v odpovědi(b).

## (a) Konvexita, invariant a skutečné konečné ukončení

Pokud všechny p_j=p, je tvrzení rovnost s binomickou distribucí.
Jinak existence průměru p zaručuje alespoň jeden parametr u<p
a jiný v>p; přeznačením je dáme do posledních dvou pozic.
Zvolme ε=min(v−p,p−u)>0. Nové parametry zůstanou mezi u a v,
tedy v[0,1], a alespoň jeden se stane přesně p. Přímý výpočet dává

    δ=ε(v−u)−ε²=(v−p)(p−u)>0:

ε je menší z obou vzdáleností a v−u je jejich součet, takže
ε(v−u−ε) je jejich součin. Tím je ověřena i specifická tištěná
hodnota δ, nikoli jen její znaménko.

Konvexita na[0,n], použitá v bodě k+1=(k+(k+2))/2, dává
g(k)−2g(k+1)+g(k+2)≥0. Jde přesně o rovnici(19), jejíž obecný
důkaz je již v D095. Proto všechny h_k, a tím i Eg(X), neklesnou.

V každém kroku zůstává ∑p_j=np. Parametry, které už jsou p,
se nevybírají; počet parametrů různých od p klesne alespoň o1.
Pokud ještě není hotovo, zachovaný průměr poskytne další dvojici
po opačných stranách p. Po nejvýše n−1 krocích jsou všechny p.
Jediný poslední nerovný parametr by totiž odporoval součtu np.
Nejde o nekonečný vyrovnávací limit. Při p=0 nebo1 je už původní
vektor konstantní, protože všechna p_j leží v[0,1].

Výsledná distribuce je binomická, takže

    Eg(X)≤∑_{k=0}^n g(k)binom(n,k)p^k(1−p)^{n−k}.

Pro n=0 je součet bitů0 a obě strany g(0); pro n=1 je p₁=p
a rovnost. Všechny konce jsou tedy zahrnuty bez umělých dvojic.

## (b) Existence maxima a úplná extremální redukce

Funkce parametrů Eg(X) je konečný polynom, a tedy spojitá na
neprázdném kompaktním průřezu

    K_p={ (p₁,…,p_n)∈[0,1]^n : ∑p_j=np }.

Proto maximum existuje. U vybraného maximalizátoru nechť r parametrů
je0, s je1 a h=n−r−s je vnitřních. Pro h=0 či1 je požadovaný
tvar{0,a,1} již dosažen. Při h≥2 má průměr vnitřních hodnot
a=(np−s)/h∈(0,1). Nejsou-li všechny a, existují dvě s 0<u<a<v<1.

Když K>0, posun k průměru a jako v(a) má δ>0 a zvýší Eg(X),
což odporuje maximu. Když K<0, položme η=min(u,1−v)>0 a
ε=−η. Nové u−η,v+η leží v[0,1] a alespoň jeden dosáhne hranice.
Jejich změna součinu je

    δ=−η(v−u)−η²<0,

takže také δK>0, znovu spor. Nutně K=0. Pro takovou dvojici
je celý přípustný posun při zachovaném součtu bez změny Eg(X).

Nyní provedeme posun k a. Oba nové parametry leží stále ostře
v(0,1); r,s,h i průměr a jsou zachovány. Počet vnitřních
parametrů různých od a klesne alespoň o1, a ty už rovné a
znovu nevybíráme. Každý další vektor je stále globální maximalizátor,
takže argument K=0 lze znovu použít pro nově vybranou dvojici,
i když se její koeficienty α,β,γ změnily. Nejvýše h−1 kroků
vede ke h stejným hodnotám a. To je celý tištěný závěr(b).

Předpoklad „g není konvexní“ se v této redukci nepotřebuje;
platí pro jakoukoli konečnou reálnou funkci g na daném rozsahu.
Nejde o tvrzení, že každý maximalizátor už původně má tento tvar,
ale že alespoň jeden takový vždy existuje, jak požaduje zadání.

## Převzatá F016 a zachované konečné důkazy

Právě ve větvi K<0 tisk píše δ=−min(u,1−v), ale jde o ε.
Přebírá se již potvrzená F016, včetně přesného svědka
u=1/4,v=3/4: ε=−1/4, skutečné δ=−3/16. Původní A=C=3/16;
dosazení tiskového δ=−1/4 by dalo záporné A′=C′=−1/16.
Po záměně symbolu je argument výše platný a hlavní věta zůstává.
Tento svědek nebyl znovu počítán programem ani založen pod novým ID.

`GENERAL_PROBABILITY_NOTES.md` a `results/poisson_binomial.json`
zachovávají1286 vektorů,7294 konvexních,3818 ocasových a6430
extremálních porovnání, spolu s5950 Samuelsovými nerovnostmi
a28 symbolickými identitami. Převzaty jsou jen v tomto přesném
konečném rozsahu. Poslední dvě skupiny nejsou uzavřením celého
důkazu29, který zůstává následujícím úkolem. Žádný starý běh se
nespustil znovu, F016 zůstává stejnou již evidovanou chybou.

## (c) Příprava maximalizátoru a význam znaménka K

Uvažujme g(k)=[0≤k≤m] a podmínku np≥m+1. Smysluplný rozsah
je celé0≤m<n, neboť np≤n. Při p=1 musí být všechna p_j=1,
a obě pravděpodobnosti P(X≤m) i B_{m,n}(1) jsou0. Případ
p=0 není za m≥0 přípustný. Zbývá0<p<1; tehdy m≤n−2.

Binomický vektor(p,…,p) má pravděpodobnost P(X=0)=(1−p)^n>0,
takže globální maximum dolního ocasu je kladné. Z(b) můžeme
vybrat maximalizátor s r nulami,s jedničkami,h=n−r−s hodnotami
a∈(0,1). Musí mít s≤m, protože při s>m je ocas0. Musí mít
h>0: jinak by X=s=np≥m+1 jistě a ocas by byl opět0.
Ve skutečnosti ha=np−s≥m+1−s≥1 a a<1, tedy h≥2.

Pokud r=s=0, už jsme dostali požadovaný binomický vektor a lze
skončit. V dalších krocích vždy vybereme **nestejnou** dvojici
parametrů, kterou lze přiblížit při δ>0. Pro takovou vybranou
dvojici nemůže být K>0, neboť by se globální maximum zvýšilo.
Tento rozsah je podstatný: u stejné dvojice může K>0 být, ale
její přiblížení žádný kladný δ neposkytuje. Tištěný argument
o nemožnosti kladného K je používán jen v prvním, relevantním smyslu.

Pro zvolenou dvojici zbývá součet Z s distribucí P_{n−2} a

    K=P(Z≤m)−2P(Z≤m−1)+P(Z≤m−2)
     =P(Z=m)−P(Z=m−1).

Tím je úplně odvozen tištěný rozdíl dvou zobecněných koeficientů.

## (c) Vyloučení nul, každý binomický exponent a první poměr

Předpokládejme r>0 a vyberme dvojici(0,a). Z pak má s jistých
jedniček a h−1 stejných vnitřních bitů. Pokud s=m, je
P(Z=m)>0, ale P(Z=m−1)=0, takže K>0. To odporuje maximalitě,
protože dvojici(0,a) lze přiblížit. Tato větev je řešena před
poměrem, který by měl ve jmenovateli m−s.

Při s<m položme j=m−s≥1. Z ha=np−s≥j+1 a a<1 plyne
h≥j+2. Proto obě pravděpodobnosti níže jsou kladné a všechny
indexy leží ve vnitřním přípustném rozsahu:

    P(Z=m)=binom(h−1,j)a^j(1−a)^{h−1−j}
          =binom(n−r−s−1,m−s)a^{m−s}(1−a)^{n−r−1−m},
    P(Z=m−1)=binom(h−1,j−1)a^{j−1}(1−a)^{h−j}
          =binom(n−r−s−1,m−1−s)a^{m−1−s}(1−a)^{n−r−m}.

Jejich poměr je přesně

    R₀=(n−r−m)a/((m−s)(1−a)),
    R₀−1=(np−m)/((m−s)(1−a))>0.

Druhý vztah používá ha=np−s a np−m≥1. Tedy K>0 i v této
větvi, znovu spor. Proto r=0. Každý exponent, oba binomické
indexy i ostrá nerovnost odpovědi jsou tím prověřeny bez dělení0.

## (c) Vytištěné vyloučení s=m v neterminálním případě

Pro r>0 již bylo s=m vyloučeno přímo. Pokud r=0,s=m=0,
jde o dříve vyřešený terminální vektor všech parametrů a=p;
žádná další redukce se po něm nepožaduje. Zbývá r=0,s=m>0.

Vyberme(a,1). Ostatní bity tvoří m−1 jedniček a h−1 vnitřních
bitů. Poměr P(Z=m)/P(Z=m−1) je(h−1)a/(1−a). Je větší než1,
pokud ha=np−m>1; to dává okamžitý spor. Na hranici np=m+1
je ha=1, a=1/h a K=0. Toto není důvod mlčky napsat ostré znaménko.

Proveďme proto nejprve posun(a,1) na(b,b), kde b=(1+a)/2.
Zachovává maximum, protože K=0. Zůstalo h−1 starých hodnot a,
dvě hodnoty b a m−1 jistých jedniček. Jelikož h≥2, lze vybrat
další nestejnou dvojici(a,b). Mimo ni jsou m−1 jedniček,
h−2 bitů s parametrem a a jeden bit s parametrem b. Označme
jejich náhodnou část W. Všechny její nulové pravděpodobnosti
jsou kladné a

    P(W=1)/P(W=0)
       =(h−2)a/(1−a)+b/(1−b)
       =(h−2)/(h−1)+(h+1)/(h−1)
       =(2h−1)/(h−1)>1.

Pro tuto druhou dvojici je tedy K>0 a její přiblížení zvýší ocas
nad původní globální maximum. Spor. Tím je v neterminálním případě
úplně doloženo i vytištěné „cannot have s=m“, včetně hraniční
rovnosti np=m+1, kterou starý stručný záznam nerozepisoval.

## (c) Vyloučení jedniček, druhý poměr a konečný proces při rovnosti

Máme r=0. Pokud s=0, je hotovo. Jinak zvolme dvojici(a,1).
Z obsahuje s−1 jistých jedniček a N=h−1=n−s−1 bitů s parametrem a.
Položme j=m−s+1≥1. Platí ha=np−s≥j a a<1, tedy N≥j.
Obě relevantní pravděpodobnosti jsou proto kladné, včetně případu
j=N. Jejich binomický poměr je

    R₁=P(Z=m)/P(Z=m−1)
       =(n−1−m)a/((m−s+1)(1−a)),
    R₁−1=(np−m−1)/((m−s+1)(1−a))≥0.

To ověřuje přesně druhou tištěnou formuli. Rovnost nastává právě
když np=m+1, protože její jmenovatel je kladný.

Pokud np>m+1, je K>0 a přiblížení(a,1) odporuje maximu.
Tedy v této větvi s=0. Pokud np=m+1, je K=0. Nahraďme
(a,1) dvojicí((1+a)/2,(1+a)/2). Ocas se nezmění, nevznikne
žádná nula a počet jistých jedniček s klesne právě o1.

Vnitřní hodnoty nyní nemusí být všechny stejné. Použijeme(b)
na právě dosažený globální maximalizátor: jeho vnitřní vyrovnání
nezmění hodnotu ani počty nul/jedniček a po konečně mnoha krocích
dá nový tvar{a′,1}. Celkový součet np se pořád nemění. Celý
cyklus lze opakovat; s je nezáporné celé číslo, které v každém
cyklu klesne o1. Nejvýše po původních s cyklech je s=0 a všechny
parametry jsou p. Každý cyklus má nejvýše n vyrovnávacích kroků,
takže jde i o konečnou konstrukci s nejvýše n² takovými kroky.

Globální maximum je tedy dosaženo u binomického vektoru, a pro
jakoukoli původní volbu platí P(X≤m)≤B_{m,n}(p). To uzavírá
celou část(c), včetně nulových parametrů, přípustných konců m,p,
obou poměrů, rovnosti np=m+1 a důvodu ukončení.

## Prameny, errata a rozsah převzetí

Šest textových vrstev errat a tři TeX zdroje byly znovu cíleně
porovnány s přesným místem28(b) a celou úlohou. F016 nemá
v těchto uložených vrstvách odpovídající veřejnou opravu; žádný
další rozpor se nepotvrdil. Doklad je
`results/sequential/mpr-028-smoothing-errata.json`.
Potvrzení fyzického výtisku ani prvenství se netvrdí.

Hoeffdingova atribuce a bibliografie27(1956),713–721 souhlasí
s [obsahem původního časopiseckého čísla](https://www.jstor.org/stable/i312787).
[Primární archiv autorského reportu](https://repository.lib.ncsu.edu/bitstream/1840.4/2268/1/ISMS_1955_128.pdf)
uvádí právě tento problém nezávislých pokusů a tříhodnotové extrémy.
Náš důkaz je celý výše; není založen na převzetí nepročtené věty.

Pitmanův odkaz souhlasí s
[metadaty vydavatele](https://www.sciencedirect.com/science/article/pii/S0097316597927473)
i [autorským univerzitním záznamem](https://statistics.berkeley.edu/tech-reports/453):
Journal of Combinatorial Theory A77(1997),279–303. Abstrakt skutečně
pojednává o stejných distribucích koeficientů. Celý přehled jeho
dalších výsledků se tím nepovažuje za matematicky auditovaný.

Odkaz4A7.2.1.5–63 byl přímo ověřen v originále p439/file456
a v odpovědi p777/file794. Jde opravdu o další vlastnosti téhož
součinu∏(1+p_j(z−1)). Tady je ověřena správnost odkazu a objektu;
všech pět cizích podúloh ani obě celé stránky4A se tím neuzavírají.
Žádná z těchto dodatečných vět nebyla použita jako předpoklad důkazu28.
Přesný zdrojový rozsah je v `sources/mpr028-bibliography.json`.

Celá MPR28 je reviewed s již existující F016. P028 zůstává partial
jen pro dosud nerozepsaný celý Samuelsův argument29. File394 má
nyní každou zdejší odpověď24–28 matematicky posouzenou, včetně F016;
file395 pouze pokračování28. File35 má zatím hotové27–28.
Žádný nový nález a žádný numerický běh.

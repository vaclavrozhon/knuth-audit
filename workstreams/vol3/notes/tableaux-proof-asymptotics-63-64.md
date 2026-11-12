# Tableaux: asymptotika involucí, s. 63–64

Samostatné odvození (43)–(53), všech přechodů a úlohy 26 s odpovědí
na 611. Původní sazba: images/tableaux-file-074.png, -075.png a -622.png.
Přebírám pouze již doložený součet a rekurenci P0458–P0459. Proměnná n
jde po kladných celých číslech do nekonečna; tvrzení o asymptotice se
netýkají n=0. Exponent ε je pevný, např. knižní 1/1000. Níže stačí
0<ε<1/20. Konstanty v O mohou záviset na ε a na pevném řádu rozvoje,
nikoli na n ani na poloze bodu v centrálním intervalu.

Zohledněna známá errata k (46), 17. 5. 1999, a k (49), 9. 8. 1999.
Nejsou našimi nálezy. Oprava ocasu z 1. 1. 2006 má samostatný nový
rozpor V3-C0019; pravdivost (52) a (53) tím není vyvrácena.

## P0463: poměr, maximum a skutečná mřížka

Pro 0≤k≤floor(n/2) je t_n(k)=n!/((n−2k)! 2^k k!). Přímým zkrácením
faktoriálů dostáváme (43), pokud k+1 ještě leží v oboru. S r=n−2k je
podmínka t_n(k+1)≥t_n(k) ekvivalentní

    r(r−1)≥n−r+2, tedy r²≥n+2.

Poměr proto překročí jedničku nejvýše jednou: součet je unimodální,
s možnou rovností sousedních členů. Bod obratu je
(n−sqrt(n+2))/2=(n−sqrt(n))/2+O(n^(−1/2)); celočíselné maximum leží
do vzdálenosti O(1) od c_n=(n−sqrt(n))/2. Za floor(n/2) jsou počty
nulové z kombinatorické definice. Rovnice (44) je přesná substituce
x=k−c_n; x obecně není celé, ale leží na mřížce Z−c_n.

Označme A=n^(1/4+ε). Centrální součet má body α,α+1,…,β−1, kde

    α=ceil(c_n−A)−c_n=−A+O(1),
    β=floor(c_n+A)+1−c_n=A+O(1).

Toto jsou skutečné meze použité dále, nikoli předpoklad celočíselného A.

## P0464: uniformní Stirlingův rozvoj (46)

Položme q=sqrt(n), m=n−2k=q−2x, u=n^(−1/4) a z=ux. V centrálním
intervalu |z|≤n^ε máme m~sqrt(n), k~n/2, oba kladné. Stirlingův
vzorec ve tvaru

    log(v!)=(v+1/2)log v−v+(1/2)log(2π)+1/(12v)+O(v^(−3))

je pro tři faktoriály uniformní, protože jejich argumenty mají právě
uvedené dolní meze; jde o použití §1.2.11.2-(18) pro kladné argumenty.
Po dosazení k=(n−m)/2 a rozložení log m a log(n−m) se přesně dostane

    log t_n(k)=(n/2−1/4)log n−n/2+m/2−(1/2)log π
       −(m+1/2)log(1−2x/q)
       −(n−m+1)/2 log(1−m/n)
       +1/(12n)−1/(12m)−1/(6(n−m))+O(m^(−3)+n^(−3)).

To dovoluje zkontrolovat konstanty i uniformní zbytek bez CAS.
Pro w=2x/q a v=m/n jsou dvě logaritmické části

    −(m+1/2)log(1−w)
      =q(w−w²/2−w³/6−w⁴/12)+w/2+w²/4
         +O(q|w|⁵+|w|³),

    −(n−m+1)/2 log(1−v)
      =m/2−m²/(4n)−m³/(12n²)+m/(2n)
         +O(m⁴/n³+m²/n²).

Zbytky jsou uniformní z geometrického odhadu Taylorovy řady, protože
|w|≤2n^(ε−1/4) a v=O(n^(−1/2)) jsou nakonec nejvýše 1/2.
Člen m spolu s qw dává q; −m²/(4n)=−1/4+x/q−x²/q²
zruší člen x²/q² v prvním rozvoji. Konstantní člen řádu 1/q je
−1/12+1/2−1/12=1/3. Výsledkem je

    C_n=(n/2)log n−n/2+sqrt(n)−(1/4)log n−1/4−(1/2)log π,
    log t_n(k)=C_n−2z²
       +u(2z−4z³/3)+u²(1/3−4z⁴/3)
       +O(u³(1+|z|⁵)).                                      (A)

Například nevypsané části −m³/(12n²) jsou O(u³|z|+u⁴z²+u⁵|z|³),
a 1/m=u²/(1−2zu); i ty splňují uvedenou mez. O(m^(−3)) je O(u⁶).
Po návratu k x má zbytek O(n^(5ε−3/4)), což je (46) po známé opravě
prvního členu na (n/2)log n. Chybějící n v prvním dotisku není nový nález.

## P0465: diskrétní ocas (47)

Unimodalita z P0463 znamená, že na každé straně centrálního intervalu
stačí omezit první vyřazený člen. Jeho x je ±A+O(1), a (A) na něm dává

    t_n(k)≤exp(C_n−2n^(2ε)+O(n^(3ε−1/4))).

Posun o O(1) změní kvadratický člen o O(n^(ε−1/4)), což je menší
než vypsaný zbytek. Při ε<1/20 je i člen n^(4ε−1/2) menší.
Členů celého součtu je nejvýše n pro n≥2. Součet vyřazených členů
je tedy nejvýše n krát tato mez, a vůči exp(C_n) je menší než
libovolná záporná mocnina n. Člen nejbližší x=0 je exp(C_n+o(1)),
takže tvrzení o zanedbatelnosti už není jen nezdůvodněná lokalizace
maxima. Toto je odhad diskrétních sčítanců (47), nikoli integrální
ocas v C0019.

## P0466: vyjmutí faktoru a opravené (49)

Vyjmeme F_n=exp(C_n+u²/3), přesně (48). Pro

    A(z)=2z−4z³/3, B(z)=−4z⁴/3

zbývá e^(−2z²) exp(uA(z)+u²B(z)+r_n(z)), kde
|r_n(z)|≤C u³(1+|z|⁵). Na celém zvoleném intervalu jsou všechny
tři členy exponentu stejnoměrně malé. Taylorův vzorec proto dává

    exp(uA+u²B+r)=1+uA+u²(B+A²/2)
                    +O(u³(1+|z|⁹))
       =1+u(2z−4z³/3)
          +u²(2z²−4z⁴+8z⁶/9)+O(u³(1+|z|⁹)).              (B)

Konkrétní odhad zbytku je C(|uA|³+|u³AB|+|u⁴B²|+|r|), který má
právě uvedenou polynomiální mez. Faktorový zápis (49) vznikne zvlášť
rozvinutím exp(−4x³/(3n)), exp(2x/sqrt(n)) a exp(−4x⁴/(3n sqrt(n))).
Druhý člen prvního exponenciálu je (8/9)x⁶/n²; to je známá oprava
z roku 1999. Nahrazení |z|≤n^ε dává vytištěný hrubší
O(n^(9ε−3/4)); pro konečnou přesnost ale níže ponecháme polynom v z.

## P0467: Eulerův vzorec na posunutém intervalu (50)

Platí β−α∈Z. Funkci proto přeložíme o α; Bernoulliho periodické
funkce mají celočíselné uzly přesně na této mřížce. Na každém jednotkovém
intervalu přímá integrace po částech s B_1(v)=v−1/2 dává

    sum f(α+j)=∫_α^β f−(f(β)−f(α))/2
                  +∫_α^β B_1({x−α}) f'(x) dx.

Další integrace po částech s B_j'=jB_(j−1) dávají (50). Pro j≥2
jsou krajní hodnoty B_j(0)=B_j(1); liché B_j s j>1 jsou nulové,
takže netriviální krajní členy mají znaménka právě jako v knize.
Hladkost f potřebná pro libovolný pevný počet integrací zde platí.

Zbytek řádu r je, až na znaménko, integrál periodického B_r/r!
krát f^(r). Jeho koeficienty Fourierovy řady pro r≥2 jsou
−1/(2π i h)^r, h≠0: nejprve je získáme integrací B_1(v) proti
exp(−2πihv), potom opakovanou integrací po částech. Řada je absolutně
konvergentní; její supremum je nejvýše 2ζ(r)/(2π)^r<4/(2π)^r.
Pro r=1 stačí přímo |B_1|≤1/2≤4/(2π). Tedy

    |R_r|≤4/(2π)^r ∫_α^β |f^(r)(x)| dx.

To ověřuje i konstantu pod (50), včetně r=1. Pozdější změna konvence
B_1 v erratech neovlivní výslovně napsané −[f]/2 ani sudé B_j.

## P0468: škálování derivací (51)

Pro pevné celé t≥0 položme g(y)=y^t exp(−2y²). Platí
f(x)=n^(t/4)g(n^(−1/4)x); řetězové pravidlo dává přesně (51).
Každá derivace g je polynom krát exp(−2y²), neboť
(P exp(−2y²))'=(P'−4yP)exp(−2y²). Je proto absolutně integrovatelná.
Substituce x=n^(1/4)y v mezním integrálu zbytku dává

    R_r=O(n^((t+1−r)/4)).

Konstanta závisí na pevných t,r, nikoli na n nebo posunu mřížky.

## P0469: nahrazení konců nekonečny, původní a opravené znění

Pro každý pevný t,r jsou krajní hodnoty f^(r)(α), f^(r)(β)
polynomem v n a A krát exp(−2n^(2ε)+o(1)). Integrální ocas má stejnou
mez s nějakým pevným mocninným faktorem: po substituci y=n^(−1/4)x
integrujeme polynom krát Gaussovu funkci; integrace po částech snižuje
stupeň, až na základní případ ∫_b^∞ exp(−2y²)dy≤exp(−2b²)/(4b).
Proto všechny tyto části jsou O(exp(−n^(2ε))) a tím i
O(exp(−2n^ε)). Původní slabší odhad prvního dotisku je platný.

Nová pravá strana opravy2006, O(exp(−2n^(2ε))), však pevný mocninný
faktor neabsorbuje. V3-C0019 obsahuje přesný důkaz, už pro integrální
člen t=0, asymptotiku obou ocasů i celočíselnou rodinu n=m^1000.
Je to lokální chyba v erratech; žádná z následujících vět ji nepotřebuje.

## P0470: síla závěru (52)

Nechť K≥0 je libovolně předepsaná přesnost; písmeno K oddělujeme od
řádu Eulerovy formule. Vybereme celé r≥t+1+4K. Z P0468 plyne
R_r=O(n^(−K)). Všechny krajní hodnoty a integrální ocasy podle P0469
jsou menší než každá mocnina n^(−1). Tím

    sum_(x=α,α+1,…,β−1) x^t exp(−2x²/sqrt(n))
       =∫_R x^t exp(−2x²/sqrt(n)) dx+O(n^(−K)).             (C)

Platí to i pro liché t a nesymetrickou mřížku: zbytková nesymetrie
nemusí být přesně nula, ale má libovolný záporný mocninný řád.
To je (52), včetně kvantifikátoru „pro všechna m≥0“.

## P0471–P0472: úloha26 a celá odpověď611

Pro n>0 a celé t≥0 substituce v=2x²/sqrt(n) přímo dává

    ∫_0^∞ x^t exp(−2x²/sqrt(n)) dx
        =n^((t+1)/4) Γ((t+1)/2)/2^((t+3)/2).

Dolní konec je integrovatelný i při t=0, horní díky exponenciále.
Na celé přímce je výsledek nula při lichém t. Při t=2j používáme
Γ(j+1/2)=(2j)! sqrt(π)/(4^j j!), které plyne z integrace po částech
a základního Gaussova integrálu. Ten lze ověřit umocněním integrálu
a polárními souřadnicemi: (∫_R exp(−y²)dy)²=2π∫_0^∞ r exp(−r²)dr=π.
Dostáváme přesně vytištěný výsledek

    ∫_R x^t exp(−2x²/sqrt(n)) dx
      =n^((t+1)/4) sqrt(π) t! / (2^((3t+1)/2) (t/2)!).

Zvlášť t=0 dává sqrt(π/2)n^(1/4), nikoli normalizovaný integrál1.

## P0473: sečtení (49) a odstranění ztráty9ε

V normalizované Gaussově míře úměrné exp(−2z²)dz jsou momenty
μ_2=1/4, μ_4=3/16, μ_6=15/64. Liché momenty jsou nulové. Tedy
koeficient u² v (B) má střední hodnotu

    2μ_2−4μ_4+(8/9)μ_6=1/2−3/4+5/24=−1/24.

Vzorec (C) platí pro každý z konečně mnoha monomů; násobení pevnými
mocninami u jeho libovolnou přesnost nezruší. Zbytek (B) se nesčítá
hrubým maximem n^(9ε). Použijeme |z|⁹≤1+z^10 a (C) pro t=0,10:

    sum e^(−2z²)(1+|z|⁹)=O(u^(−1)).

Součet zbytků je tedy O(u²), nikoli jen O(u² n^(9ε)). Výsledkem je

    sum normalized_summand
       =sqrt(π/2)(u^(−1)−u/24+O(u²))
       =sqrt(π/2)(n^(1/4)−n^(−1/4)/24+O(n^(−1/2))).

To přesně zdůvodňuje přechod před (53) se zbytkem bez9ε. Není třeba
spoléhat na neprovedený výpočet vyšších koeficientů.

## P0474: konstanta7/24 a závěr (53)

Po vynásobení F_n a přidání již zanedbatelného diskrétního ocasu je
konstantní hlavní faktor

    exp(C_n) sqrt(π/2) n^(1/4)
       =(1/sqrt(2)) n^(n/2) exp(−n/2+sqrt(n)−1/4).

Zbývající součin exp(u²/3)(1−u²/24+O(u³)) je
1+(1/3−1/24)u²+O(u³)=1+(7/24)n^(−1/2)+O(n^(−3/4)).
Rovnice (53) je proto dokázána v přesně vytištěné síle. Vada C0019
je vadou pomocného odhadu v pozdější opravě, nikoli vyvrácením (53).

## P0475: možnost libovolného pevného řádu

Stirlingův vzorec má pro kladné argumenty zbytek omezený první
vynechanou zápornou mocninou. Pro libovolnou konečnou přesnost lze
tedy vzít více jeho členů a více Taylorových členů obou logaritmů
v P0464. Protože |zu|≤n^(ε−1/4)→0, Taylorovy zbytky mají tvar
O(u^L(1+|z|^D)) pro vhodná konečná L,D; L lze zvětšovat bez omezení.
Při rozvoji exponenciály zůstává vyjmutá část exponentu stejnoměrně
malá (její největší oprava má velikost O(n^(3ε−1/4))). Stejný
Gaussův vážený odhad jako v P0473 integruje každý zbytkový polynom.
Eulerův řád se zvolí až podle požadované přesnosti; ocasy jsou stále
zanedbatelné vůči každé mocnině.

Tím vzniká pro každé pevné L konečný rozvoj s relativním zbytkem
O(u^L); pro O(n^(−K)) stačí L≥4K. Navíc transformace (u,z)↦(−u,−z)
nemění vstupní výrazy m=u^(−2)(1−2zu), n=u^(−4). Koeficient u^j
je proto polynom v z parity j. Liché integrály zmizí a výsledný
rozvoj má jen mocniny u²=n^(−1/2). To dokládá „in principle“ pro
libovolný pevný řád, nikoli konkrétní seznam dalších85 řádů.

## P0476: dodatek2024 a přesná hranice bibliografické kontroly

Primární [článek Ekhada, Kauerse a Zeilbergera](https://arxiv.org/html/2410.16334v1)
byl přečten v relevantních částech. Jeho metadata potvrzují autory,
rok2024 a čtyři stránky; text skutečně odkazuje na výstup do
O(n^(−85)) a používá rekurenci involucí. To ověřuje bibliografické
tvrzení přidané do errat16.11.2024. Všech169 dalších koeficientů,
jejich program ani numerické ukázky článku zde nebyly reprodukovány;
nejsou dokladem našeho vlastního odvození. Přesná hranice je uložena
v sources/tableaux-asymptotics-2024-source.json.

Historické prvenství Moser–Wyman a Laplace i podrobnosti jejich
původních publikací výslovně přeskočeny. Vytištěný odkaz na další
aplikace v §5.2.2 není důkazem této zatím neuzavřené sekce.
Úloha1 začínající na64 a další úlohy nejsou tímto blokem uzavřeny.
Žádný numerický výpočet ani starý verifier nebyl spuštěn.

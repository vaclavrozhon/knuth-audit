# D132 — celá MPR30(a–c) a oba výzkumné dovětky

6. listopadu2026. Celé původní zadání p15/file35 a odpověď
p375/file395 přímo zobrazeny, také autorův Pre-Fascicle5A
p15/file21 a p32/file38. Nezávislé nezáporné celočíselné
X₁,…,X_n mají EX_i=1; p=Pr(∑X_i≤n). Níže n≥1.
Prázdný součet n=0 má p=1 a nepotřebuje optimalizační argument.

## (a) Přesná hmotnost a striktní konstanta

Při podpoře{0,n+1} vynutí průměr1 hmotnost1/(n+1) v n+1
a n/(n+1) v0. Součet je≤n právě tehdy, když všechny členy
jsou0. Nezávislost proto dává

    p=(n/(n+1))^n.

Protože log(1+x)<x pro x>0 (integrace1/(1+t)<1),

    log p=−n log(1+1/n)>−1,       p>1/e.

Tištěné zaokrouhlení1/e≈0.368 je správné. Například řada
e=∑1/k! dává po k=6 hodnotu1957/720 a zbytek mezi0
a(1/7!)/(1−1/8)=1/4410; oba reciproké konce se zaokrouhlí
na0.368. Jde o přesný odhad řady, ne nový numerický běh.

## (b) Všechny koeficienty a přípustné nekonečné podpory

Fixujme prvních n−1 marginál, S=∑_{i<n}X_i,
A_m=Pr(S≤n−m), m≥0, a x_m=Pr(X_n=m).
Všechny A_m∈[0,1]; pro m>n je A_m=0.
Z ∑m x_m=1 a ∑x_m=1 dostáváme přesně

    x₀=∑_{m≥1}(m−1)x_m=x₂+2x₃+3x₄+⋯.

Řada konverguje, protože0≤(m−1)x_m≤m x_m a střední
hodnota je konečná. Podmínění podle X_n a nezávislost dávají

    p=∑_{m≥0} A_m x_m
      =∑_{m≥1}(A_m+(m−1)A₀)x_m.                (1)

Jsou to nezáporné řady; výměna a dosazení nepoužívají
podmíněnou konvergenci. Jde o každý koeficient tištěné formule.
Položme y_m=m x_m. Pak y_m≥0, ∑y_m=1, a(1) se stává

    p=∑_{m≥1} c_m y_m,
    c_m=(A_m+(m−1)A₀)/m.                       (2)

Naopak každé takové y určuje přípustné rozdělení:
x_m=y_m/m pro m≥1, x₀=∑(1−1/m)y_m≥0,
celková hmotnost1 a průměr1. Nechybí další nerovnostní
podmínka při eliminaci x₀.

## (b) Proč se minimum skutečně dosahuje a m≤n+1

Máme A₀>0: jelikož ES=n−1 a S je nezáporné celé číslo,

    n−1=ES≥(n+1)Pr(S>n),
    A₀≥2/(n+1)>0.

Pro m≥n+1 je c_m=A₀(1−1/m), což je striktně rostoucí
funkce celého m. Všechny m>n+1 jsou tedy horší než n+1.
Minimum c_m existuje v konečné množině1,…,n+1. Průměr(2)
je nejméně toto minimum, dosažené volbou y_m=1 v jednom
minimalizujícím indexu. Odpovídající X_n je{0,m}, s kladnou
hmotností1/m v m. Pro m=1 je degenerovaně konstantní1;
tištěné rozmezí1≤m≤n+1 tuto možnost v tomto kroku připouští.

Z libovolné původní sady provedeme postupně tuto náhradu
pro n souřadnic. Každý krok zachová nezávislost a průměry,
nezvýší p a ponechá dříve upravené podpory dvoubodové.
Po nejvýše n náhradách máme některou z konečných(n+1)^n
sad s m_i∈{1,…,n+1}. Jejich minimum je proto i globální
minimum nad všemi původními, včetně nekonečných podpor:
každá původní hodnota je≥některé konečné, a konečné jsou
samy přípustné. Žádný tento prostor se neenumeroval.

Navíc u každého globálního minimalizátoru je každá souřadnice
už minimem(2) pro své pevné ostatní souřadnice. Kladné y_m
u c_m>min c by vytvořilo striktně větší vážený průměr.
Proto má každá marginála podporu v{0,…,n+1}; to je skutečná
nutnost, nikoli jen tvrzení, že tak lze zvolit jeden příklad.

## (b) Silnější slovo „any“ není odvozeno z pouhé linearity

Samotný lineární argument ještě nevylučuje směs dvou různých
minimalizujících indexů. Například při n=2 a pevném X₁
rovnoměrném na{0,1,2} je A₀=1,A₁=2/3,A₂=1/3,A₃=0,
takže c₁=c₂=c₃=2/3. Pro tuto pevnou první marginálu je
minimalizující i tříbodová druhá marginála rovnoměrná na{0,1,2}.
Není to protipříklad knize: celkově p=2/3 není globální
minimum, neboť dvě{0,3} dávají4/9.

Úplné doplnění nutnosti je v
[sequential-mpr-ex030-feige.md](sequential-mpr-ex030-feige.md), §1–6.
Z podmíněných momentů je tam dokázána ostrá mez
p≥(n/(n+1))^n pro každou konečnou dvoubodovou sadu.
Rovnost nutí podmíněný průměr součtu při S≤n být0,
a tím všechna m_i=n+1. Přesná směsná reprezentace marginál
pak dokazuje, že i každý původní globální minimalizátor
má právě tyto marginály. Tím je celé tvrzení(b), včetně
jeho silnějšího kvantifikátoru, doloženo. Není evidováno jako
chyba ani jako neuzavřený kandidát.

## (c) Přesný přechod přes Samuelsovu mez

Společné nezáporné celočíselné dvoubodové rozdělení průměru1
musí mít tvar{0,t}, t≥2; pokud by jeho nižší hodnota byla≥1,
byl by průměr větší než1. Degenerovaná konstanta1 dává p=1.
Hmotnost v t je1/t a p=B_{⌊n/t⌋,n}(1/t).

Je-li t>n+1, nastává S≤n právě při všech nulách a
p=(1−1/t)^n>(n/(n+1))^n>1/e. Zbývá2≤t≤n+1,
kdy0≤m=⌊n/t⌋<n. Pro obecné0<p₀<1 s np₀≤m+1
označme q=1−p₀,d=n−m. Celá MPR29 v D131 dává

    B_{m,n}(p₀)≥((m+1)q/(mq+1))^d=x^{−d},
    x=(mq+1)/((m+1)q)>0.

Aritmeticko-geometrická nerovnost pro d kopií x a m kopií1
(celkem n členů) dává x^d≤((dx+m)/n)^n. Proto

    B_{m,n}(p₀)≥(n/(dx+m))^n
                =(1−1/(f+1))^n,
    f=(m+1)qn/(d p₀).

Každý faktor lze ověřit přímo:

    dx+m=(m(n+1)q+d)/((m+1)q),
    f/(f+1)=n(m+1)q/(n(m+1)q+d p₀),
    n(m+1)q+d p₀=m(n+1)q+d.

Jmenovatele jsou kladné. Pro m=0 je AM–GM rovnost a
všechny vzorce stále platí; m=n a p₀=0/1 se zde nepoužívají.

Napišme n=mt+r s0≤r<t. Celočíselnost r,t dává r≤t−1,
a tudíž přesně tištěnou silnější podmínku

    1/t≤(m+1)/(n+1),

protože n+1≤t(m+1). Tím je splněn i slabší předpoklad
n/t≤m+1 Samuelsovy meze. Při p₀=1/t je

    f=n(m+1)(t−1)/(n−m)≥n,

neboť (m+1)(t−1)−(n−m)=t−r−1≥0.
Funkce f↦f/(f+1) je pro f≥0 rostoucí, takže

    p=B_{m,n}(1/t)≥(n/(n+1))^n>1/e.

To uzavírá všechny větve(c), včetně t=n+1,m=0,
t=1 a t>n+1; nejsou skryty v tvrzení o minimalizátoru(b).

## Výzkumné dovětky a zdroje

Eltonův původní sedmistránkový článek
[arXiv:0908.3528](https://arxiv.org/abs/0908.3528) byl načten
a jeho p2–3 přímo zobrazeny. Uvádí redukci na dvoubodové
zákony a zprávu o kontrole n≤20. Původní historický běh
se nereprodukoval; shoda s autorovým sdělením je bibliografická,
zatímco platnost pro všechna n nyní dokládá úplný důkaz v dodatku.
Ostatní části jeho článku nejsou automaticky převzatým důkazem.

Dovětek „jsou tyto distribuce optimální pro všechna n?“ má
nyní kladnou odpověď i s jedinečností, viz dodatek§6.
Poslední Feigeho tvrzení pro obecné reálné proměnné EX_i≤1
a práh n+1/(e−1) je úplně dokázáno v dodatku§7–8.
Současná nová matematika neopravuje historické znění knihy
jako erratum; poskytuje chybějící důkaz pro tento audit.

Původní Feigeho conjecture1 byla přečtena v autorově verzi
[newmarkov.pdf](https://www.wisdom.weizmann.ac.il/~feige/Others/newmarkov.pdf),p2;
údaje SIAM Journal on Computing35(4)(2006),964–984 potvrzuje
[vydavatel](https://epubs.siam.org/doi/10.1137/S0097539704447304).
Zbylý 26stránkový text není prohlašován za celý prověřený.
Červencová práce2607.23980 byla přečtena v rozsahu formulace
a závěrečné implikace, ale její vnější předpoklady se nepřebírají;
pro tento audit je nahrazuje úplný říjnový argument.
Starší tvrzení o důkazu2508.07316 bylo zkontrolováno v aktuálnív2:
autor sám uvádí chybuv1; nepoužívá se jako důkaz.

Rychle nedostupný původní Winklerův sloupek CACM52(8),
August2009,104–105, včetně přesné paginace a pojmenování,
je výslovně bibliograficky vynechán. Také atribuce řešení(c)
E. Schulte-Geersovi není nezávisle doložena. Matematický důkaz
všech částí na těchto atribucích nezávisí.

Všech6errat+3TeX bylo zkontrolováno podle současné/historické
stránky, čísla30 a jmen; žádná oprava tohoto bloku nenalezena.
Položka4Bp421/answer30 je DLX a indexový záznam Elton není
opravou MPR30. Manifest a přesné kontexty jsou u claim-map.

D132/MPR30 jsou checked/reviewed ve vymezeném rozsahu.
File395 nyní celý matematicky reviewed s uvedenými bibliografickými
výjimkami. File35 zůstává partial pro31–40. Žádný nový nález,
žádný numerický běh, žádný starý výpočet či census nerestartován.

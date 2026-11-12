# Tableaux40: náhodný růst, normalizace a všechny řádky

Zadání71/file82 a odpověď614/file625 z původní sazby.
Pozdější dodatek6.4.2014 v all3-pre odkazuje na Romikovu kapitolu4;
jde o známé doplnění zdroje, ne o nález. Přesná externí závislost
je v sources/tableaux-corner-growth-source.json.

## P0595: přesný model a každý faktor příkladu

Do Youngova diagramu lze přidat buňku na konci prvního řádku,
na konci každého dalšího řádku, který je kratší než předchozí,
nebo jako nový poslední řádek. Proto je počet možností d(λ)
roven počtu různých kladných délek řádků plus1. U prázdného
diagramu je d=1. Přidání největšího dosavadního štítku právě
do takové buňky zachová standardní tableau; jiná buňka by
porušila tvar nebo řádkové/sloupcové pořadí.

Pro tableau(1) z počátku sekce (P0384, znovu se nedokazuje)
mají tvary před vložením štítku tyto přesné počty rohů:

| Štítek | Dosavadní tvar | d |
|---|---|---:|
|1|prázdný|1|
|2|(1)|2|
|3|(2)|2|
|4|(2,1)|3|
|5|(2,1,1)|3|
|6|(3,1,1)|3|
|7|(3,2,1)|4|
|8|(3,3,1)|3|
|9|(3,3,2)|3|
|10|(4,3,2)|4|
|11|(5,3,2)|4|
|12|(5,3,2,1)|5|
|13|(5,3,3,1)|4|
|14|(5,4,3,1)|5|
|15|(5,4,4,1)|4|

Konečný tvar je(6,4,4,1), tedy15 buněk. Součin podmíněných
pravděpodobností 1/d je přesně všech15 vytištěných faktorů.
Není třeba předpokládat nezávislost jednotlivých d: používá se
řetězové pravidlo podél konkrétního rostoucího tableau.
Rovnoměrná volba rohu v každém kroku neznamená rovnoměrnou
volbu ze všech konečných tableaux.

## P0596: ekvivalence s exponenciálními hodinami

Každá nově dostupná buňka dostane nezávislé hodiny Exp(1),
spuštěné až po zaplnění jejích potřebných předchůdců.
Shody časů mají pravděpodobnost0, takže přibývá vždy jedna buňka.
Při d dostupných rozích mají jejich zbylé časy nezávislé
rozdělení Exp(1). Pro určeného vítěze j a čas t je společná
hustota e^(−dt). Po integraci je jeho pravděpodobnost1/d;
součet hustot je d e^(−dt), takže čekání je Exp(d) a vítěz
je na jeho délce nezávislý.

Po odečtení vítězného času mají ostatní hodiny opět nezávislá
Exp(1): společná podmíněná hustota zbytků se rozloží na součin
e^(−x_l), bez t a j. Nové hodiny jsou nezávislé podle konstrukce.
Indukce podle celé dosavadní historie tedy dává přesně
diskrétní proces z P0595 jako posloupnost skoků. Počáteční
prázdný tvar má jediné hodiny; první štítek je deterministicky
v levé horní buňce, jeho čas je Exp(1).

Proces neudělá nekonečně mnoho skoků do konečného času.
Časy buněk prvního řádku jsou částečné součty nezávislých
Exp(1), totéž na prvním sloupci. Na každé ose téměř jistě
nastane nekonečně mnoho čekání≥1: pravděpodobnost, že po
daném indexu nenastane žádné, je lim_K(1−e^(−1))^K=0;
sjednocení přes počáteční indexy je stále nulové.
Oba osové součty divergují. Do daného konečného času tedy
vznikne jen konečný první řádek a sloupec, a celý Youngův
diagram leží v jejich konečném obdélníku.

## P0597: přesná externí věta a konstanta6

Používá se [Rostova věta ve formulaci Romika](https://danromik.com/resources/books/the-surprising-mathematics-of-longest-increasing-subsequences.pdf), Theorem4.5,
tištěná222/PDF232, v autorově rukopisu20.8.2014:
pro právě definovaný proces Λ(t), D={(x,y)≥0:√x+√y≤1}
a každé pevné 0<ε<1 platí

    Pr((1−ε)tD ⊆ set(Λ(t)) ⊆ (1+ε)tD) → 1.

set(λ) je sjednocení jednotkových buněk; osy představují
sloupcový a řádkový index. Francouzské kreslení zdroje pouze
obrací vizuální svislou osu, nemění tyto kladné souřadnice.
Zdrojový proces má nezávislé jednotkové exponenciální hodiny
aktivované v dostupných rozích, přesně jako P0596.

Plný analytický důkaz limitního tvaru v Romik§4.3–4.6 zde
není znovu odvozen. Toto je výslovná externí věta s ověřeným
modelem, kvantifikátory, škálou a typem konvergence; následující
převod do všech knižních tvrzení je vlastní argument.
Přímá diskrétní formulace Theorem4.1 na213 má tentýž výsledek;
nemusíme ale nahrazovat čas náhodnou dobou bez odůvodnění.

Plocha D je

    ∫_0^1 (1−√x)^2 dx = 1−4/3+1/2 = 1/6.

Proto z obou inkluzí plyne |Λ(t)|/t²→1/6 v pravděpodobnosti.
Na jednotkovou plochu se D zvětší faktorem√6, takže v měřítku
√n bude rovnice hranice √x+√y=6^(1/4). Faktor6 tedy není
důsledkem záměny tohoto modelu s rovnoměrnými permutacemi.

## P0598: přechod do diskrétního času bez náhodné substituce

Položme S=√(6n), T_n=čas n-tého přidání a λ(n)=Λ(T_n).
Pro cílové 0<ε<1 vezměme δ=ε/4, η=ε/8 a deterministické
časy t_−=(1−δ)S, t_+=(1+δ)S. Oba rostou do nekonečna.
Použijme externí větu s chybou η v těchto dvou časech;
průnik obou událostí má pravděpodobnost jdoucí k1.

Na tomto průniku platí podle plochy

    |Λ(t_−)| ≤ ((1+η)(1−δ))² n < n,
    |Λ(t_+)| ≥ ((1−η)(1+δ))² n > n,

protože η=δ/2 a 0<δ<1. Tedy t_−<T_n<t_+ a monotonie dává

    (1−η)(1−δ) S D ⊆ set(λ(n))
                             ⊆ (1+η)(1+δ) S D.

Oba součiny leží mezi1−ε a1+ε: ztráta vlevo je
δ+η−δη≤3ε/8 a přírůstek vpravo je
δ+η+δη≤3ε/8+ε²/32<ε. Dostáváme tak

    Pr((1−ε) S D ⊆ set(λ(n)) ⊆ (1+ε) S D) → 1.       (*)

Žádný krok nevkládá náhodné T_n do věty platné jen pro
deterministický čas. Výsledek odpovídá přesně Theorem4.1.

## P0599: počet řádků i oba osové konce

Je-li λ(n)=(λ_1,…,λ_m), maximální y v set(λ(n)) je m,
maximální x je λ_1. Z(*) přímo plyne

    (1−ε)S ≤ m,λ_1 ≤ (1+ε)S.

Proto m/√(6n)→1 v pravděpodobnosti, stejně jako λ_1/√(6n).
Obě osy jsou součástí inkluzí; nejde jen o výrok uvnitř
kompaktního intervalu vzdáleného od krajních řádků.

## P0600: uniformní výklad odmocninové rovnice

Na události(*) položme A=(1−ε)S, B=(1+ε)S.
Pro každý 0≤k<m je šířka řádku ve výšce y=k+θ,
0<θ<1, rovna λ_(k+1). Horní inkluze a limita θ↓0 dávají

    √k+√λ_(k+1) ≤ √B.

Je-li k+1≤A, dolní inkluze ve výšce těsně pod k+1 dává

    √λ_(k+1) ≥ √A−√(k+1),
    √k+√λ_(k+1) ≥ √A−1,

protože √(k+1)−√k≤1. Je-li k+1>A, pak už
√k≥√A−1 (pro A≥1 plyne z k>A−1; pro A<1 je pravá strana
záporná). Stejná dolní mez tedy platí pro všechny řádky,
včetně posledního:

    √((1−ε)S)−1 ≤ √k+√λ_(k+1) ≤ √((1+ε)S).

Spolu s P0599 a poté ε→0 z toho plyne přesný uniformní výrok

    max_(0≤k<m) |(√k+√λ_(k+1))/√m −1| → 0
                                                    v pravděpodobnosti.

Tím je doložen přirozený relativní asymptotický význam knižního
„≈“, se všemi indexy a diskrétní chybou≤1 v dolním odhadu.
Není zde tvrzena absolutní odchylka o(1), kterou zadání přesně
neformuluje. Pro n=0 rovnice s m ve jmenovateli nemá význam;
úloha je asymptotická pro n→∞, žádný nulový případ se nepoužil.

Autorova errata Romika z15.1.2021 byla přečtena: v kapitole4
mění údaj na251, nikoli uvedené věty. Původní celý Rostův článek
1981 se znovu nezískával; dostupná primární monografie dává přesný
zdroj výsledku. Žádná simulace ani enumerace nebyly spuštěny.


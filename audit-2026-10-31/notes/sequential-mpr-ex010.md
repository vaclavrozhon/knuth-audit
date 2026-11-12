# D113 — celá MPR10: náhodný polynom nad konečným tělesem

6. listopadu 2026. Přímo přečteno celé zadání 13/file33
a celá odpověď 372/file392; také autorův Pre-Fascicle 5A,
13/file19 a 29/file35. Níže je důkaz každého tištěného
kroku, všech tří rozměrových případů a dovětku o tělesech.
Žádný numerický výpočet není potřeba.

## Přesný prostor a jednotlivé marginály

Pro kladná celá m,n a prvočíslo p jsou všechny vektory
(Y₁,…,Y_m) v F_p^m stejně pravděpodobné, každý s p^(−m).
Definujme monický polynom

    f(t)=t^m+Y₁t^(m−1)+⋯+Y_m.

Pak X_j=f(j mod p). Při fixovaných Y₁,…,Y_(m−1)
je X_j součtem pevného prvku a rovnoměrného Y_m.
Posun je bijekce tělesa, takže každý X_j je rovnoměrný:
P(X_j=a)=1/p pro každé a. To platí i pro m=1 a j=p,
kde f(0)=Y_m. Kladné m je běžný rozsah uvedené rodiny
Y₁,…,Y_m; prázdná rodina zde není tištěná konstrukce.

## n>p: opakovaný bod znemožní párovou nezávislost

V tělese se p+1 rovná 1, tudíž X_(p+1)=X₁ bodově.
Pro každý a proto

    P(X₁=a, X_(p+1)=a)=1/p ≠ 1/p².

Protože p≥2, jde o striktní nerovnost. Celá rodina
není párově nezávislá, a tedy ani k-násobně nezávislá
pro žádný dostupný řád 2≤k≤n: nezávislost větší skupiny
by se sečtením ostatních hodnot přenesla na tuto dvojici.
Jednoprvkové rodiny jsou samozřejmě nezávislé. Knižní
„there's no independence“ je v tomto odstavci obvyklá
zkratka pro netriviální párovou či vyšší nezávislost,
nikoli samostatné tvrzení o neplatnosti tautologického
řádu 1. Některé jednotlivé podrodiny s různými body
mohou být nezávislé; definice k-wise vyžaduje všechny.

## Různé body a přesný počet vláken

Nyní n≤p, takže body 1,…,n jsou v F_p různé, včetně
možného posledního bodu p=0. Vyberme libovolných r
z nich, a₁,…,a_r, kde 1≤r≤min(m,n), a libovolné
předepsané hodnoty b₁,…,b_r.

Z koeficientů f ponechme volné m−r koeficienty mocnin
t^r,…,t^(m−1). Jejich každá volba určí polynom h(t)
s těmito členy a pevným monickým členem t^m. Zbývá
najít jediný polynom g stupně nejvýše r−1 splňující
g(a_i)=b_i−h(a_i). Existence je výslovná:

    L_i(t)=∏_(j≠i) (t−a_j)/(a_i−a_j),
    g(t)=Σ_i (b_i−h(a_i))L_i(t).

Všechny jmenovatele jsou nenulové prvky tělesa, tedy
invertibilní, a L_i(a_j)=[i=j]. Pro r=1 je součin
prázdný a L₁=1. Rozdíl dvou řešení by měl r různých
kořenů a stupeň nejvýše r−1, což je možné pouze pro
nulový polynom. Použitá kořenová věta má krátký důkaz:
je-li a kořen nenulového P, dělení polynomu monickým
t−a dává P=(t−a)Q; každý jiný kořen je kořenem Q,
neboť těleso nemá dělitele nuly. Indukce podle stupně
dává nejvýše deg P různých kořenů, včetně stupně 0.

Každá z p^(m−r) voleb vyšších koeficientů má právě
jedno doplnění nízkých koeficientů. Každé předepsané
r-tici hodnot tak odpovídá přesně p^(m−r) z celkových
p^m stejně pravděpodobných vektorů:

    P(X_(a₁)=b₁,…,X_(a_r)=b_r)=p^(−r).

Index X_(a_i) zde označuje původní vybraný index,
jehož reziduum je a_i; při a_i=0 je to index p.
Pravá strana je součin všech r marginálů. Tím je
prokázána každá skupina a každá konfigurace, nejen
nulové hodnoty nebo jedna vybraná matice.

## Vandermondův mezikrok a skutečný odkaz

Matice s i-tým sloupcem (1,a_i,…,a_i^(r−1)) má
determinant ∏_(i<j)(a_j−a_i). Je tedy invertibilní
i tehdy, když jeden a_i=0. Předchozí interpolace
to dokázala přímo; současně tím ověřuje knižní krok
o lineární nezávislosti libovolných m sloupců při r=m.

Přímo zobrazen také skutečný odkaz ve svazku 1:
§1.2.3, zadání 37 na p38/file53 a odpověď 37 na
p473/file488. Tam Vandermondova matice začíná mocninou
1, nikoli 0; její determinant je
(∏a_i)∏_(i<j)(a_j−a_i). Důkaz v
`workstreams/vol1/notes/matrices.md`, §2, a přesná
eliminace v `workstreams/vol1/notes/quality-recovery-section-1.2.3-2026-11-06.md`
byly přečteny v tomto rozsahu. Z každého sloupce lze
formálně vytknout a_i. V polynomiálním okruhu se pak
společný polynom ∏a_i zkrátí, což dává potřebnou
identitu s exponenty 0,…,r−1. Teprve poté se dosadí
prvky F_p. Nepoužíváme číselné dělení nulovým a_i;
polynomiální identita s celočíselnými koeficienty
platí po redukci modulo libovolné prvočíslo. Odkaz je
věcně správný, posunuté exponenty nejsou chyba.
Jiné části obou stránek svazku 1 se tím neuzavírají.

## m<n≤p: přesně m-násobná nezávislost

Předchozí argument dává všechny řády do m. Vyberme
libovolných m+1 různých bodů z 1,…,n. Jev, že všech
m+1 odpovídajících X je 0, má pravděpodobnost 0:
monický f je nenulový a má stupeň právě m, tudíž
nemůže mít m+1 různých kořenů. Při nezávislosti by
tento jev měl součinovou pravděpodobnost p^(−m−1)>0.
Proto (m+1)-násobná nezávislost selhává. Selhává
i každý vyšší dostupný řád, protože ten by implikoval
(m+1)-násobnou nezávislost sečtením marginálů.

## m≥n a n≤p: úplná nezávislost

Ve vláknovém argumentu lze vzít r=n. Každá celá
n-tice hodnot má pravděpodobnost p^(−n), takže všech
n proměnných je společně nezávislých. Nevadí m=n ani
m>p: používají se jen nízké mocniny 0,…,n−1, nikoli
neplatná kořenová argumentace pro stupeň m≥p. Pro n=1
jde o správnou jednoprvkovou hranici.

## Dovětek: libovolné konečné těleso

Nahradíme F_p konečným tělesem F_q, koeficienty
nezávisle rovnoměrnými prvky F_q a indexy vyhodnocení
různými prvky a₁,…,a_n tělesa. V předchozím důkazu
se pouze p nahradí q; používá se přesně existence
inverzí nenulových rozdílů, počet q^m koeficientových
vektorů a kořenová věta nad tělesem. Proto při n≤q
platí stejné rozlišení m<n a m≥n. Opakovaný bod
naopak znovu dává totožnou, nedegenerovanou dvojici,
která není nezávislá.

Při q=p^s nejde o doslovné použití celočíselných
zbytků 1,…,q modulo p: ty by navštívily pouze prvočíselné
podtěleso a opakovaly body. „Any finite field in this
construction“ přirozeně znamená vyhodnocovat ve
zvolených prvcích daného tělesa. Toto je potřebný
přesný výklad konstrukce, nikoli nový spor v textu.
Tvrzení není rozšířeno na obecné konečné okruhy,
kde nenulové rozdíly nemusí být invertibilní.

## Rozsah a errata

Celá MPR10 včetně všech vět odpovědi je checked,
bez nálezu a bez bibliografické výjimky. Převzatá
šestivrstvá kontrola stejných stránek z D109 byla
znovu posouzena pro tuto úlohu, včetně tří TeX
zdrojů: žádná oprava zadání 10 nebo odpovědi 10.
Opravy jiných odpovědí na p372/p184 se nepřenášejí
na tuto úlohu. Přesné soubory, hashe a rozsah jsou
v `results/sequential/mpr-010-polynomial-errata.json`.
Samotné dokončení úlohy neuzavírá celou p13 ani p372.

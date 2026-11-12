# Věta H, dělitelné přírůstky a přesné náklady — 7. listopadu 2026

Rozsah: celý zbývající matematický text88–89/file99–100, úlohy16,
17,19 na103 a odpovědi621–622; uzavření dosud otevřeného průměrového
srovnání P0718 v odpovědi9. Úloha18 zůstává následující samostatný blok.
Sazba je v `images/insertion-file-{099,100,114,630,632,633}.png`.
Pět vrstev errat je převzato ze `sources/insertion-errata-review.json`:
známé opravy2005 mění n na N v17,2010 přidává +j do konstrukce16,
2011 pojmenovává Corollary H; oprava0.15 na0.16 již byla zohledněna.
Žádná z těchto oprav není nový nález. Huntovu bakalářskou práci1967
ani historické prvenství znovu nedohledáváme; obecný důkaz je níže.

Přebíráme konkrétní hotové argumenty P0725–0739 pro dvě uspořádané
třídy, P0740–0754 pro rozdělení a P0712–0722 pro celý programD.
Zásada vzorů1/4B: skutečný pravděpodobnostní prostor, dosažitelnost
současných maxim a doména asymptotiky jsou samostatné části důkazu;
pouhé dosazení výsledné formule by nestačilo.

## P0755: rovnoměrný pár tříd

Nechť n≥0, h≥1 jsou celá čísla, q=⌊n/h⌋, r=n mod h.
Třída i obsahuje pozice i,i+h,… a má délku

    L_i=q+[i≤r],  1≤i≤h.

Uspořádání každé třídy na náhodné permutaci má přesně ∏L_i!
vzorů pro každý konečný h-ordered výsledek. Všechny takové výsledky
jsou tedy stejně pravděpodobné. Pro zvolené i<j podmiňme množinu
hodnot v jejich sjednocení a všechno mimo ně. Každá volba L_i
z těchto L_i+L_j hodnot pro třídu i má stejný počet vzorů; uvnitř
obou tříd již pořadí určuje třídění. Po přeznačení hodnot pořadím
dostáváme rovnoměrnou 2-ordered permutaci. Delší z nestejných tříd
je vždy dřívější: právě prvních r tříd má q+1 prvků. Její přebytečný
prvek proto stojí na konci prokládání, jak vyžaduje použitý model.

Každá inverse má právě jednu dvojici různých tříd; uvnitř třídy
žádná není. Sčítáme očekávání, nikoli nezávislé náhodné veličiny.
Nezávislost různých dvojic se nepředpokládá a obecně neplatí.

## P0756: všechny členy vzorce H a hranice

Z již dokázané střední hodnoty dvoutřídových inversí vyjádříme
společný faktor

    F_q=2^(2q−1)(q!)²/(2q+1)!.

Střední hodnoty pro délky2q,2q+1,2q+2 jsou postupně

    F_q q(2q+1)/2,   F_q q(q+1),   F_q(q+1)².

První výraz pro q=0 znamená nulu; prázdná permutace má0 inversí.
Počty dvojic krátkých, smíšených a dlouhých tříd jsou
binom(h−r,2), r(h−r), binom(r,2). Smíšenou hodnotu použijme jako
základ pro všech binom(h,2) párů. Krátký pár odečítá F_q q/2,
dlouhý přičítá F_q(q+1), takže přesně

    f(n,h)=F_q {binom(h,2)q(q+1)+binom(r,2)(q+1)
               −binom(h−r,2)q/2}.

To je(4), včetně všech faktorů. Pro h>n máme q=0,r=n,F_0=1/2,
tedy f=binom(n,2)/2. Pro h=n máme q=1,r=0,F_1=1/3 a opět
f=binom(n,2)/2. Pro h=1 je jediná uspořádaná třída a formule0;
n=0,1 dávají0 i při prázdných třídách. Platnost pro h≥n tedy
není formální extrapolace asymptotiky.

## P0757: důsledek H a skutečná podmíněná distribuce

Nechť h_0=1 a h_(s+1) je násobek h_s. Pro programD předpokládáme
N≥2 a skutečné přírůstky<N; abstraktní prázdné průchody lze vynechat.
Před průchodem h_s jsou třídy modulo h_(s+1) uspořádané.
Všechny dřívější přírůstky jsou násobky h_(s+1), takže nikdy
nepřesunuly hodnotu z této třídy. Poslední h_(s+1)-sort proto
zanechal právě seřazené původní množiny hodnot těchto tříd.

Podmiňme množinu hodnot jedné třídy modulo h_s. V původní náhodné
permutaci byly všechny její rozklady do k=h_(s+1)/h_s podtříd
s předepsanými velikostmi stejně pravděpodobné. Předchozí průchody
tyto množiny zachovaly a nyní je jen každá uspořádaná. Relativní
permutace této h_s-třídy je tedy rovnoměrná k-ordered permutace.
Její insertion sort provede právě tolik přesunů, kolik měla inversí.

Pro q_s=⌊N/h_s⌋, r_s=N mod h_s tak linearita dává přesně

    E B=∑_(0≤s<t) {r_s f(q_s+1,h_(s+1)/h_s)
                    +(h_s−r_s)f(q_s,h_(s+1)/h_s)}.          (6)

Virtuální h_t=N h_(t−1) dává v prvním průchodu k=N; každá
počáteční podposloupnost délky≤N je N-ordered bez omezení.
Tak se do stejné formule správně zahrne i původní náhodný vstup.
Mezi průchody ani mezi jejich cenami se nezávislost netvrdí.

## P0758: úloha16, maximum a opravená konstrukce

Hotový ostrý dvoutřídový výsledek dává pro krátký i smíšený pár
maximum q(q+1)/2; pro dlouhý pár (q+1)(q+2)/2. Součet horních
mezí je

    fhat(n,h)=binom(h,2)binom(q+1,2)+binom(r,2)(q+1).

Současné dosažení není automatické ze součtu mezí. Dejte dřívější
třídě vždy celý blok větších hodnot než kterékoli pozdější třídě,
uvnitř třídy vzestupně. Přesně pro existující pozice to znamená

    a_(i+jh)=1+q(h−i)+(r−i)[i≤r]+j,
    1≤i≤h, 0≤j<L_i.

První hodnota je1+∑_(k>i)L_k. Bloky jsou proto disjunktní,
společně obsahují1,…,n a v každé třídě rostou. Pro každý pár
dřívější/větší třídy a pozdější/menší třídy je inversí právě tolik,
kolik je poloh první třídy před polohami druhé; to jsou přesně
výše uvedená dvoutřídová maxima. Platí i q=0: neprázdné třídy
jsou jednoprvkové a dostáváme celou sestupnou permutaci.
Pro h=1 je maximum0. Člen+j, chybějící v prvním tisku, je známá
oprava2010, nikoli náš nález.

## P0759: všechny průchody mohou maxima dosáhnout současně

Pro dělitelné přírůstky je součet(6) s fhat místo f horní mezí
celkového B. Je dosažitelná následující zpětnou konstrukcí.
Začni konečným seřazeným výstupem. Máme-li předepsaný výstup
průchodu h_s, v každé jeho třídě uspořádej stejné hodnoty do
maximální k-ordered permutace z P0758, k=h_(s+1)/h_s. Vzniklý
stav je globálně h_(s+1)-ordered, průchod h_s ho vrátí přesně
na předepsaný výstup a každá třída při tom realizuje svou horní mez.
Tento stav nyní předepiš jako výstup předchozího průchodu.
Pokračuj pro s=0,1,…,t−1. Poslední virtuální k=N neomezuje
počáteční podposloupnosti, takže vznikne platná vstupní permutace.
Žádná dříve zvolená pozdější cena se novým zpětným krokem nemění.
To dokazuje tvrzení odpovědi16 o maximu celého algoritmu.

## P0760: úloha17, jedinečnost i bitový popis

Pro N=2^t a h_s=2^s musí rovnost s právě dokázanou horní mezí
nastat v každé třídě každého průchodu: všechny rozdíly proti
jednotlivým maximům jsou nezáporné. P0738 dokázal, že sudá
2-ordered permutace dosáhne maxima jedině ve tvaru

    m+1,1,m+2,2,…,2m,m.

Před posledním průchodem musí tedy liché pozice obsahovat větší
polovinu a sudé menší polovinu. Dřívější průchody působí na obě
parity odděleně; po přeznačení každé poloviny jde o stejný problém
pro t−1. Indukce od P_0=(1) proto dává právě jednu permutaci,

    P_t(2j−1)=2^(t−1)+P_(t−1)(j),
    P_t(2j)=P_(t−1)(j).

Je rovna a_j=1+rev_t(2^t−j): při lichém j má 2^t−j poslední
bit1, který se po obrácení stane nejvyšším; při sudém j je tento
bit0. Zbývajících t−1 bitů v obou případech odpovídá uvedené
rekurenci. Například t=2 dává4,2,3,1. Je pokryt i t=0 jako
jednoprvkový matematický okraj; MIX s ním není spouštěn.

## P0761: úloha19, všechny nové minima

Pro n≥1 může být novým prefixovým minimem v h-ordered permutaci
jen první prvek neprázdné třídy. Pozdější prvek stejné třídy má
před sebou její menší minimum. První prvek třídy j je novým
minimem právě tehdy, když nejmenší hodnota sjednocení prvních j
tříd patří do třídy j. Rovnoměrné rozdělení hodnot dává pravděpodobnost

    L_j/(jq+min(j,r)).

Pro j≤r je1/j, pro j>r je q/(jq+r). První prvek celé permutace
se do A nepočítá, takže

    g(n,h)=H_r−1+∑_(r<j≤h) q/(qj+r).

Při r=0 je H_0−1+H_h=H_h−1; při q=0 je r=n>0 a zbývající
členy jsou0, tedy g=H_n−1. Pro h=1 vyjde0. Prázdný n=0 se do
vzorce s0/0 nedosazuje: samostatná konvence je g(0,h)=0.
Stejný podmíněný argument P0757 dovoluje v(6) nahradit f funkcí g
a dostat přesný E A. V platném MIX modelu jsou použité třídy neprázdné.

## P0762 a doplnění P0718: přesná dvouprůchodová cena

Pro přírůstky h,1 a N=qh+r je

    E B={h q(q−1)+2rq}/4+f(N,h)
       ={N²/h−N+r(h−r)/h}/4+f(N,h),
    E A=r(H_(q+1)−1)+(h−r)(H_q−1)+g(N,h).

První člen B je součet polovičních binomických čísel náhodných
tříd prvního průchodu; druhý je H. První členy A jsou přesně
jejich prefixová minima, druhý je P0761. Z již doloženého počtu
instrukcí, T=2 a S=h+1 dostáváme

    E time_D=9 E B+10(2N−h−1)−3 E A+27,
    E time_S=9N²/4+31N/4−3H_N−6.

Čtyři cílená racionální dosazení h=4 jsou uložena v
`results/two-pass-crossover-exact.json`; žádné permutace ani programy
se neenumerovaly a výpočet se neopakuje. Rozdíly D−S jsou:

| N | přesný rozdíl v u |
|---|---:|
|10|947/168 >0|
|11|−41449/9240 <0|
|13|−122627/3432 <0|
|16|−23452733/240240 <0|

Odpověď9 říká „about N=13“, nikoli přesný univerzální práh13.
Při N=11 je zlepšení jen asi1.3%; její přibližné tvrzení i dovětek
o podobných časech při malých N jsou tak doloženy konkrétněji.
**Netvrdíme nejmenší N po optimalizaci všech h**, ani že programD
vyhrává pro každý vstup. Dříve doložený konkrétní16prvkový příklad
má stále D=567u proti S=514u; průměry jsou jiné veličiny.
P0718 lze tímto uzavřít jako kontrolu přibližného srovnání s přesným
vymezením. Nevzniká kandidát ani potvrzená chyba.

## P0763: přesná doména asymptotické aproximace

Ze Stirlingova vzorce pro střední binomický koeficient

    F_q=4^q/{2(2q+1)binom(2q,q)}
       =√π/(4√q)(1+O(1/q)).

Závorka v H je binom(h,2)q²+O(h²q), s absolutní konstantou
uniformně pro h≥2, protože0≤r<h. Její relativní chyba je O(1/q).
Jelikož q=(n/h)(1+O(h/n)), pro h≥2 a n/h→∞ vychází

    f(n,h)=(√π/8)n^(3/2)(h−1)/√h ·(1+O(h/n)).

Pokud navíc h→∞, je to

    f(n,h)=(√π/8)n^(3/2)√h ·(1+O(1/h+h/n)).

To přesně vymezuje „first approximation“ na89. Pro pevné malé h
nelze vynechat faktor(h−1)/h; pro h≥n správný výsledek dává P0756,
nikoli tato asymptotika. Optimální režim níže má oba požadované
parametry rostoucí, takže omezení skutečně splňuje.

## P0764: celý tvar obrázku12

Pro pevné q a r=n−qh je závorka H po roznásobení

    {q(q+1)²h²+q(q+1)(1−2n)h+(q+2)n²−(3q+2)n}/4.

Obrázek spojuje hodnoty celočíselných h. Jeho příslušné polynomiální
oblouky jsou konvexní a rostoucí: derivace závorky je
q(q+1){2(q+1)h+1−2n}/4>0 na n/(q+1)≤h≤n/q.
Na hranici r=0 se oba sousední popisy shodují, protože jen jinak
označují tytéž stejně dlouhé třídy. Pro h≥n je přesná křivka vodorovná.

Při n=64 má f(64,1)=0, f(64,16)=3072/7, f(64,32)=1984/3,
f(64,48)=2248/3 a f(64,64)=f(64,80)=1008. Na32<h≤64 je
konkrétně f=(h²−63.5h+2992)/3. Tyto výšky, rostoucí konvexní
oblouky a zlomy při změně⌊64/h⌋ souhlasí s původním obrázkem;
horní plošina je nad1000, nikoli rovna1000. Hladká křivka je
64√π√h, takže při64 má asi907.5 a při80 asi1014.6. Také její
průsečíky a konečná poloha odpovídají sazbě. Není zde tvrzena
statistická definice h-ordered pro neceločíselné h; interpolace
slouží jen popisu nakresleného grafu.

## P0765: minimum hlavního dvouprůchodového členu

První průchod má E B=N²/(4h)−N/4+r(h−r)/(4h). V režimu
1≪h≪N dává P0763 pro osmkrát vedoucí člen celkem

    L(h)=2N²/h+√π N^(3/2)√h.

Jeho derivace má znaménko výrazu
−2N²+(√π/2)N^(3/2)h^(3/2); tento výraz přísně roste od
záporné ke kladné hodnotě. Jediné globální minimum je tedy

    h³=16N/π,  h=(16/π)^(1/3)N^(1/3)≈1.72N^(1/3).

Oba kladné členy pak mají řád N^(5/3). Zaokrouhlení h na celé
číslo nezmění vedoucí člen. Zbytek přesné MIX ceny je O(N), neboť
0≤A≤2N a T=2; celkový průměr proto má stejný řád.

## P0766: proč optimum aproximace platí i pro přesnou cenu

Volba z P0765 dává přesnou cenu O(N^(5/3)). Naopak první průchod
má E B≥N²/(4h)−N/4. Pro2≤h≤N, q≥1 máme F_q≥c/√q pro
nějakou absolutní c>0 (Stirling s konečným doplněním malých q),
a závorka H je nejméně binom(h,2)q². Protože q≥N/(2h),

    f(N,h)≥c' N^(3/2)√h.

Tyto dvě dolní meze nutí každé přesné optimum do
c₁N^(1/3)≤h≤c₂N^(1/3). Případ h=1 má kvadratický čas a není
asymptoticky optimální. V uvedeném intervalu je aproximace P0763
uniformní; po dělení N^(5/3) se přesná cílová funkce blíží
kladnému násobku2/x+√π√x, x=h/N^(1/3). Ta má právě jedno
minimum, takže i přesně optimální celočíselné h splňuje
h/N^(1/3)→(16/π)^(1/3). Jde o dvouprůchodový programD;
otevřený problém nejlepší obecné posloupnosti přírůstků P0724
se tím nijak neuzavírá.

Strany88–89 mají po spojení s předchozími konkrétními důkazy
úplné argumentové pokrytí. Úlohy16,17,19 jsou uzavřené včetně
odpovědí;621 má ještě nedokončenou18 a622 další úlohy. Další
kurzor je úloha18 na103/file114, potom souvislý text90/file101.

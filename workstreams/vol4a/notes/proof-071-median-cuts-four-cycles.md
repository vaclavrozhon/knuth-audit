# Mediánové řezy, čtyřcykly a izometrické štítky

Checkpoint X0100, P0943–P0950. Originály: p69/file86,
p71/file88, zadání 77 a 81 na p90/file107, odpovědi
p548–549/file565–566. Záznam uzavírá celý čtyřcyklový
odstavec p69, metrické tvrzení p71, všechny části 77(a–c)
a celou 81. H/I, 77(d–e), náklady a tabulka průběhu se
zde neuzavírají.

Předpokládáme konečný neprázdný mediánový graf a jeho
medián m. P0923–P0927 a P0932 již dokazují algebraickou
strukturu, intervaly, homomorfnost hranových projekcí
a oddělení vrcholů. Tyto důkazy se přebírají přesně;
žádná vlastnost algoritmu H se nepoužívá. Pro samotné
81 je případ prázdného grafu triviálně bipartitní,
nezávisle na tom, zda jej definice řadí mezi mediánové.

## Souřadnice a konvexní poloprostory — P0943

Pro každou hranu e vezměme její projekci p_e(x)=m(x,u,v).
Má dvě hodnoty u,v a je homomorfismem na dvouprvkovou
mediánovou algebru. Kódováním konce bližšího pevnému
kořeni a číslem 0 dostáváme bit h_e(x), vždy h_e(a)=0.
Obě množiny h_e^−1(0), h_e^−1(1) jsou konvexní:
medián dvou jejich bodů s libovolným třetím bodem má
stejný bit. P0939 převádí tuto podmínku přesně na
všechny vrcholy všech nejkratších cest.

Dvě souřadnice nazveme ekvivalentní, určují-li stejný
neorientovaný řez. Normalizace u a pak zaručuje jejich
rovnost jako bitových funkcí. Po ponechání jedné kopie
každého různého řezu dostáváme redukovaný štítek l(x).
Injektivita z P0932 se odstraněním duplikátů neztrácí.

## Každá hrana mění právě jednu redukovanou souřadnici — P0944

Nechť u–v je hrana a h libovolná hranová souřadnice,
pro niž h(u)≠h(v). Pro libovolné x homomorfnost dává

    h(m(x,u,v))=m(h(x),h(u),h(v))=h(x).

Bod m(x,u,v) je u nebo v. Proto h(x) jednoznačně říká,
ke kterému konci tato projekce míří. Řez h je tedy
přesně řez vlastní projekce na u–v, případně s opačnou
orientací. Všechny souřadnice měnící se na u–v jsou
navzájem ekvivalentní a vlastní souřadnice se skutečně
mění. Po redukci tedy hrana mění právě jeden bit.

## Hammingova vzdálenost, indukovanost a celá 81 — P0945

Na nejkratší cestě se žádná souřadnice nemůže změnit
dvakrát: mezi dvěma přechody by existoval podúsek
nejkratší cesty s oběma konci v jednom poloprostoru
a s vnitřním bodem v druhém. To odporuje konvexitě
poloprostoru. Podúsek nejkratší cesty je opět nejkratší,
jinak by bylo možno zkrátit původní cestu.

Každý krok mění právě jeden bit a každý bit nejvýše
jednou. Délka cesty je proto přesně počet rozdílných
bitů jejích konců:

    d(u,v)=Hamming(l(u),l(v)).

Včetně u=v a jednovrcholového grafu s prázdným štítkem.
Zejména d(a,v) je počet jedniček l(v). Toto je celý
metrický odstavec p71, nezávisle na správnosti H.
Současně u–v právě když se štítky liší v jednom bitu,
takže graf je **indukovaný** podgraf hyperkrychle
(a dokonce její izometrický podgraf, partial cube).
Parita počtu jedniček dává jeho dvoubarevnost. To
dokazuje celé zadání i odpověď 81; tvrzení uvedené
před 80 je rovněž doloženo, ale příklady 80(a,b) nikoli.

## Dopředná čtyřcyklová ekvivalence a všechny tištěné kroky — P0946

Ve čtyřcyklu u–x–v–y–u se po oběhu musí každý bit
změnit suděkrát. Dva po sobě jdoucí kroky nemohou
měnit týž bit, jinak by se opakoval vrchol. Čtyři
kroky proto mění souřadnice i,j,i,j s i≠j. Protější
hrany jsou ekvivalentní a diagonály mají vzdálenost 2.

Tím jsou doloženy i předpoklady vytištěného algebraického
argumentu. Z m(z,u,x)=u plyne přesně

    y=m(u,v,y)=m(m(z,u,x),v,y)
     =m(m(z,v,y),m(u,v,y),m(x,v,y))
     =m(m(z,v,y),y,v).

První a poslední rovnosti používají y∈I(u,v),
v∈I(x,y); prostřední je dlouhá distributivita P0871.
Protože q=m(z,v,y) je v nebo y, poslední výraz je q,
a tedy q=y. Při m(z,u,x)=x analogický symetrický
výpočet dává m(z,v,y)=v. Totéž po cyklickém přeznačení
platí pro druhou dvojici protějších hran.

## 77(a): právě jeden soused na druhé straně — P0947

Pro pevnou hranu r–s označme její souřadnici h, s h(r)=0,
h(s)=1. P0927 dokazuje, že L={h=0} jsou přesně vrcholy
bližší r než s a R={h=1} přesně vrcholy bližší s.
Definované ranky tedy souhlasí s těmito poloprostory:
na R je rank vzdálenost do L, na L je 1 minus vzdálenost
do R. Každá strana je neprázdná. Rank 1 znamená souseda
v L a rank 0 souseda v R.

Je-li v∈R sousedem dvou různých u,u'∈L, pak
m(u,u',v) má bit 0, ale musí ležet v
I(u,v)∩I(u',v)={v}, což má bit 1. Spor. Existence
souseda ranku 0 plyne z ranku v=1, jednoznačnost
z právě uvedeného argumentu. Po záměně L,R platí
totéž i opačně. Hrany řezu proto dávají bijekci
mate mezi vrstvami B_0={rank 0}, B_1={rank 1}.
Každý pár mate se liší jen v souřadnici h (P0944).

## 77(b): konvexita pravé strany — P0948

Je to přesně konvexita h^−1(1) z P0943. Stejný důkaz
platí pro L a nezávisí na kterékoli pozdější klasifikaci
ranků v algoritmu. Při porovnání s odpovědí je tedy
odkaz na Corollary C oprávněný, ale není nutný jako
nový externí vstup.

## 77(c): konvexita obou hraničních vrstev — P0949

Nechť v,v'∈B_1 mají mates u,u'∈B_0 a w je libovolný
bod libovolné nejkratší cesty mezi v,v'. Definujme
z=m(u,w,u'). Souřadnice h(z)=0. V každé jiné souřadnici
se u shoduje s v a u' s v'. Proto tam

    z_j=m(v_j,w_j,v'_j)=w_j,

protože w∈I(v,v'). Platí h(w)=1 podle 77(b). Štítky
z,w se tedy liší právě v h, a P0945 dává hranu z–w.
Každý takový w má rank 1. To dokazuje plnou konvexitu
B_1, nejen existenci jedné cesty uvnitř vrstvy.
Symetrie dává konvexitu B_0.

Pro sousedy w,w' v B_1 se jejich mates liší v přesně
téže jiné souřadnici, takže jsou opět sousedy. Bijekce
mate je izomorfismus indukovaných grafů B_1 a B_0.

V tištěné odpovědi je w=v_1, z=u_1=m(u_0,v_1,u_k).
Je-li délka cesty k>0, souřadnicový argument výše dává
hranu u_1–v_1; u_0,u_1 se liší právě v souřadnici,
v níž se liší v_0,v_1, takže mají také hranu a nejsou
si rovny. Navíc d(u_0,v_1)=2. Tím jsou doloženy oba
vytištěné dílčí závěry, včetně vyloučení u_1=u_0.
Pro k=0 tvrzení platí přímo a žádné v_1 se nezavádí.

## Obrácená čtyřcyklová ekvivalence a jedinečnost — P0950

Každá hrana ekvivalentní r–s překračuje právě řez h,
tedy má tvar u–v s v∈B_1 a u=mate(v). B_1 je
konvexní, neprázdná a obsahuje s, proto je souvislá.
Vezměme cestu s=v_0,...,v_k=v uvnitř B_1. Její mates
tvoří cestu r=u_0,...,u_k=u uvnitř B_0. Každá čtveřice

    u_i–v_i–v_(i+1)–u_(i+1)–u_i

je čtyřcyklus: všechny hrany jsme dokázali a čtyři
vrcholy jsou různé díky rozdělení L/R a bijektivitě mate.
Postupně tedy propojí r–s s u–v řetězem protějších hran
čtyřcyklů. Pro k=0 jde o stejnou hranu. Spolu s P0946
je dokázáno přesné „právě když“ na p69.

Počet různých souřadnic je tedy přesně počet tříd
hran generovaných čtyřcykly. Kořen s nulovým štítkem
jednoznačně volí orientaci každého řezu. Redukované
štítky jsou tudíž určeny **až na pořadí sloupců**,
jak text výslovně uvádí na p71. Neprohlašujeme jedinečnost
číslování tříd bez jeho další volby.

## Bibliografie, errata a přesný zbývající rozsah

Primární DML-CZ potvrzuje Nebeský, *Median graphs*, CMUC
12(2), 1971, 317–325; vydavatelská stránka potvrzuje Mulder,
*The structure of median graphs*, Discrete Math. 24(2),
1978, 197–204. Metadata jsou v `sources/median-cuts-bibliography.json`.
Úplné historické články nebyly znovu matematicky přezkoušeny;
zde není jejich neověřená věta použita jako předpoklad.

Prohlédnuty odpovídající položky všech pěti vrstev
`all4a-pre`, `all4a`, `err4a`, `all4f0`, `all4f1`.
F0 p168/81 „an induced subgraph“ už je v našem prvním
4A dotisku. Známé opravy I4 (11. 7. 2011) a 77(d)
(10. 7. 2011) patří následujícímu algoritmickému bloku;
nejsou nové nálezy a zde se 77(d) neuzavírá.

Celé p69/p71/p90/p548/p549 zůstávají partial, protože
jejich ostatní algoritmy, úlohy nebo tabulkové průběhy
ještě nemají argument. Žádný výpočet, nový nález ani
opakovaný census nebyl potřeba.

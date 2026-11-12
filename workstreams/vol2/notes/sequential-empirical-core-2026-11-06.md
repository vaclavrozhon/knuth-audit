# Souvislá revize §3.3.2 A–I a K, 6. listopadu 2026

Třetí vydání, první dotisk 1997. Přezkoumán text na původních stranách
61–70, kolizní část71 a korelační část72–73; úlohy1–24 a jejich odpovědi
562–566. Úloha25 má ověřené číselné údaje, ale obecné vysvětlení zůstává
otevřené. Birthday test J, část L/M a úlohy26–35 navazují samostatně.
Nejde tedy o uzavření celé sekce.

Originály byly přečteny obrazově včetně indexů a znamének. Názvy obrazů
`vol2-pNNN.png` označují **tištěnou** stránku; v DjVu je pořadí o12 větší.
Přijaté programy, výsledky, logy a zdrojové záznamy mají kontrolní součty
v `results/sequential-empirical-core-review.json`. Žádný dřívější výpočet
nebyl restartován. Důkazy byly znovu čteny proti sazbě a kódu, ne pouze
převzaty podle starého statusu.

## Základní testy A–F a úlohy1–10,21–22

Rovnoměrné U v [0,1) dávají Y=floor(dU) s pravděpodobnostmi1/d.
Disjunktní t-tice tvoří d^t stejně pravděpodobných kategorií; při pevném
d,t má Pearsonova statistika asymptoticky d^t−1 stupňů volnosti.
Podmínka n>=5d^t je praktické doporučení pro očekávané četnosti, nikoli
univerzální rigorózní mez aproximační chyby. Překrývající se dvojice
nejsou nezávislé: dva sousední výskyty00 mají pravděpodobnost d^−3,
ne d^−4. Odpovědi1/2 jsou v tomto rozsahu správné.

Algoritmus G počítá neúspěchy před následujícím úspěchem. Při
p=beta−alpha mají mezery rozdělení p(1−p)^r, poslední sloučená
kategorie hmotnost(1−p)^t. Zpracování n mezer spotřebuje T vstupů,
Pr(T=j)=binom(j−1,n−1)p^n(1−p)^(j−n), E T=n/p a
Var T=n(1−p)/p². Kontrola zahrnuje vývojový diagram i počáteční j=−1.
Při p=1 je T=n deterministické; knižní max=infinity předpokládá
nedegenerovaný praktický test.

U cyklických mezer úlohy5 je počet n zásahů náhodný. Přechod od pevného
počtu mezer k náhodnému indexu vyžaduje argument, který krátká odpověď
nerozepisuje. Poznámka `empirical-basic.md` jej doplňuje: n/N→p,
maximální nerovnost pro centrované nezávislé příspěvky odstraní okno
o relativní délce epsilon a cyklické spojení změní omezený počet kategorií.
Rozdíl po dělení sqrt(N) mizí v pravděpodobnosti. Nezávislost indexu
a příspěvků se nepředpokládá. Nahrazení n hodnotou Np není stejné:
pro p=1/2,t=1 je kovariance dvojice četností N/16 krát [[5,−1],[−1,1]],
což dává vážený součet chí-kvadrát1 s vahami(3±sqrt(5))/4.

Pokerové četnosti vycházejí z rozkladů k pozic do r neprázdných skupin:
(d)_r {k\r}/d^k. Sedm klasických pětic má počty
(d)_5,10(d)_4,15(d)_3,10(d)_3,10(d)_2,5(d)_2,d; součet je d^5.
Sloučení tříd je ztrátou informace, takže slovní hodnocení jeho síly
není tvrzením shodné statistické síly pro všechny alternativy.

Pro sběr w různých kupónů je Pr(T_w=r)=(d)_w {r−1\w−1}/d^r.
Čekání na další nový symbol má geometrický parametr(d−j)/d,
j=0,...,w−1. Součin příslušných generujících funkcí dává
E T_w=d(H_d−H_(d−w)) a
Var T_w=d²(H_d^(2)−H_(d−w)^(2))−d(H_d−H_(d−w)).
Pro n úplných sad se střední hodnota i rozptyl násobí n.
Odpověď9 mění dolní index COUNT v C1, nikoli velikost pole OCCURS;
C4 ukončí po w typech. Odpověď7 dává délky5,3,5,6,5,5,4.
Pro w=1 opět platí deterministická výjimka z neomezeného maxima.

Algoritmus P je výběrové řazení doplněné faktoriálovým kódem:
f←rf+s−1 a záměna maxima s posledním dosud nezpracovaným prvkem.
Inverze pomocí div/mod pro r=2,...,t obnovuje všechny záměny a dokazuje
bijekci pořadí s čísly0,...,t!−1. Úloha21 má886862, úloha22 permutaci
(9,6,5,2,3,4,0,1,7,8). Předpoklad různých hodnot je v knize výslovný.

`verify_empirical_basic.py` byl přečten celý. Archivované výsledky:
40890 kontrol G,25384 slov/97728 kupónových případů,1872 srovnání
s Markovovým modelem,78 přesných dvojic momentů,46233 permutací.
Jde o doplněk obecných důkazů, nikoli jejich náhradu.

Úloha6: celý `experiment_e_digits.py` používá racionální interval
sum_(j=0)^K1/j! <= e <= sum_(j=0)^K1/j!+1/(K K!). Pro K=4797
oba kraje dávají stejnou celou část b^10000 e ve všech35 základech2–36.
Zdejší součty a log souhlasí s JSON. Desetinné četnosti prvních2000
zlomkových číslic jsou196,190,207,202,201,197,204,198,202,203;
V=1.06 a pro10000 číslic V=8.61. Nezávislá Decimal.exp kontrola
pokrývá10000 desetinných číslic. Hodnota Pr(chi9²>=1.15)=.9990068...
podporuje knižních99.9%. Experiment v dalších základech netvrdí
normalitu čísla e ani náhodnost jeho deterministických číslic.

## Běhy G, úlohy11–14 a otevřený rozsah25

Přezkoumány obecné pravděpodobnosti indikátorů(14), inkluze-exkluze(16),
střední hodnoty(17), kovariance(18)/(19) a rozdílový přechod(20).
Pro shodnou počáteční pozici se součin indikátorů redukuje na maximum
délek; pro p+q>n nemohou existovat dva odlišné příslušné začátky.
Na str.67 je skutečně Z19 a Z29; podezření na opakovaný index po
zobrazení v původní velikosti odpadá. Příklad běhů souhlasí.

Byl přečten celý `verify_run_tests.py`: nezávislý model je dynamické
počítání pořadí podle posledního ranku, nikoli dosazení do téže formule.
Sedí781 jednotlivých/24137 párových pravděpodobností,385 dvojic momentů,
225 inkluzně-exkluzních počtů a stará enumerace46233 permutací.
Všech72 zlomků C1/C2 i36 zaokrouhlených prvků inverze odpovídá sazbě.
Chyba původního parsování dvou desetinných koeficientů je v logu již
opravena přesnými racionálními hodnotami; není to chyba knihy.

Blokový důkaz normální limity pro konečně závislé omezené příspěvky
a podmíněné permutace oddělených buněk dokládají pozitivní definitnost
limity pro každé pevné t. Proto stupňů volnosti je t, při t=6 opravdu6.
Pevné zaokrouhlení inverze dává mírně váženou limitu, což odpovídá
výslovnému upozornění knihy na aproximaci. Doporučení n>=4000 není
nově dokázaná přesná mez chyby. Algoritmus R správně používá koncový
strážný prvek U_n=U_(n−1), který se sám nezapočítá.

V úloze14 vynechání prvku způsobivšího sestup oddělí vstupy dalších
úplných běhů zastavovací dobou. Délky jsou pak nezávislé, s pravděpodobností
1/r!−1/(r+1)! a poslední hmotností1/t!. Konec pevně dlouhého vstupu
by přidal cenzorovaný neúplný běh, který nemá toto rozdělení.

Úloha25: přesně racionálně ověřené rozsahy pro t=6 a20 odpovídají
odpovědi566; obecný důvod entrywise poměrů blízkých −t nebyl dokázán.
Přibližná deterministická vazba mezi počty běhů vysvětluje velkou inverzi,
ale sama nedokazuje uvedenou shodu. Stav úlohy a příslušného podbloku
je proto nyní **partial**. Je to zpřesnění našeho pokrytí, ne nový nález.

## Maximum H a překrývající se serial test, úlohy15–16,23–24

Maximální hodnota t nezávislých U má F(x)=x^t a její t-tá mocnina
je rovnoměrná. Přepis maxim sousedních oken musí jít zleva doprava.
Při překryvu je Cov([Z_j<=x],[Z_(j+k)<=x])=x^(t+k)−x^(2t)>0 pro
0<k<t. Pro dvě stejně pravděpodobné kategorie při t=2 dostává běžná
Pearsonova statistika násobek2sqrt(2)−1 místo1; popis zvýšených hodnot sedí.

V úloze23 je Q konvolucí distribucí P a P'. Jensenova nerovnost dává
kontrakci kvadratické odchylky od uniformního rozdělení. Není třeba
nesoudělnost period, ale je třeba průměrování přes náhodný posun,
jak stojí v zadání. Nejde o záruku pro každý pevný posun.

Úloha24 po známé opravě obsahuje čtverce četností. Odečtení součtů lze
přepsat na součet [N(gamma b)−p_b N(gamma)]²/[nP(gamma)p_b].
Příspěvky centrované podle historie mají nulové kovariance na různých
pozicích. Limitní kovariance po normalizaci sestává z projekcí
I−vv^T pro každý kontext, tedy celková hodnost d^(t−1)(d−1).
To dává požadované chí-kvadrát rozdělení. Cyklické uzavření mění jen
O(t) příspěvků; d,t jsou pevné a všechny p_b kladné.

Byl přečten celý `verify_serial_overlap.py`, opravený teleskopický
důkaz i log staré opravy Python int/float na racionální jednotku.
Archiv pokrývá63972 přepisů maxim,15376 míchacích případů,
16 kovariančních modelů,5057 cyklických slov a116190 položek
teleskopické identity. Knuthův číselný příklad01101/10101 sedí.
Pozdější změna odkazu v odpovědi15 reflektuje odstranění rovnice(23)
v §3.3.1; náš první dotisk ji stále obsahuje, nejde o jeho věcnou chybu.

## Kolizní test I a korelace K

Rozdělení počtu obsazených uren J je (m)_j {n\j}/m^n,
C=n−J a E C=n−m+m(1−1/m)^n. S2 je správná rekurence přes J;
S3 převádí Pr(J<=j) na Pr(C<=n−j−1). Přečten celý
`verify_collision_test.py` a výsledky. Nezávislá rekurence přes C
s160bitovým dolním zaokrouhlováním certifikuje sedm pravděpodobností
na str.70, chybu nejvýše1.73e−42 a průměr127.328238... .
Staré enumerace458961 slov ani širší experimenty se neopakovaly.

C0021 potvrzen v numerickém rozsahu: binary64 n=2,m=10 i10018 dává
součet1+2^−52 a zápornou CDF. Doslovná vnitřní smyčka může překročit
poslední práh; globální interpretace zastavení to může ošetřit,
ale záporný výstup vzniká dříve. Závažnost v UI změněna z critical
na medium. V přesné aritmetice tento protipříklad není. Paměťové
O(log n) nemá bez režimu přesnosti a m/n užitečný jednotný obsah;
konečná pozorování šířky nejsou důkazem jeho asymptotické nepravdivosti.

Korelační algebra(23)–(25), Binetova identita a degenerace n=2/3 sedí.
Výměnnost a omezené podíly čtverců rozdílů dávají E rho=−1/(n−1)
i bez surových momentů. Centrované symetrické součty dávají přesný
rozptyl z úlohy20. Přímá koncentrace průměrů U a U² dokládá uniformní
opravu24/(5n²);95% je asymptotická interpretace, ne přesná záruka
pro každou délku a libovolné rozdělení. Fourierova identita cyklické
autokorelace dává O(n log n), podrobný FFT audit patří do§4.6.4.

C0019 potvrzen: w=z=0 dává v tisku2^(−n/2), nikoli1; pro n=3,k=1
tištěné momenty−1/5 a1/7 odporují konstantní korelaci−1/2.
Správná spektrální generující funkce, sférické momenty i konečný vzorec
rozptylu byly přezkoumány. Dopad je v doplňkových formulích, proto
UI nynímedium. Nejde o obvinění Dixonova nedostupného článku.

C0020 potvrzen: m=ceil(1/delta) posune skutečný průměr četnosti.
Pro pevnéalpha=1 a n_k těsně nad řešením x/logx=k³ je dolní práh
jen o(n_k p_k(1−p_k))^(1/2) pod průměrem, takže selhání jedné buňky
směřuje k1/2. Tři racionální certifikáty zaokrouhlení a opravený obecný
argument koncentrace byly přijaty. Hlavní věta o rozptylu platí;
UI závažnostmedium. Celý `verify_serial_correlation.py`,10 identit,
255 permutačních modelů,18 determinantů,123 momentů a FFT srovnání
byly přezkoumány v uloženém rozsahu, bez opakování běhů.

## Errata a bibliografické výjimky

Všechny čtyři vrstvy porovnány6.11.2026; čerstvý manifest potvrzuje
shodu s archivem. Úplný výřez61–80/562–572 je uložen v
`sources/sequential-2026-11-06/empirical-tests-errata.json`.
Pro tento blok jsou podstatné61 (počet testů/intervaly),69 (inverze),
78/565/566 (úloha24). Slovní vylepšení68 a změna odkazu564 nejsou
nové matematické chyby. C0019–C0021 odpovídající opravu nemají.
Fyzický nejnovější tisk a prvenství nadále neověřeny.

Přečteny uložené metadata Pólya1930, vonSchelling1954, Bofingerovi1961,
Stoneham1965, Wolfowitz1944, Dixon1944 a Schmid1965. Plná historická
těla ani přesná atribuce Geiringerové nebyly nyní získány; netvrdí se
jejich přímá kontrola. Wolfowitz163–165 může odkazovat na část článku
163–172, samotný rozdíl není chyba. Marsaglia1984str.5–6 nedostupné,
HKU report2006 dříve jen částečně indexovaný. Tyto bibliografické mezery
jsou výslovné a nepřekrývají vlastní matematické důkazy.

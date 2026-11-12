# Osm prvků: celá tabulka5, obě maxima a přesné Prattovy statistiky

7. listopadu 2026. Sazba92–93/file103–104 a624/file635 zobrazená.
Přebíráme úplné H/g/corollary, přesný čas ProgramuD, všechny
algoritmické důkazy30/31 a statistickou involuci P0818. Níže je
nový argument ke každému dosud chybějícímu číslu a optimu.
Malé přesné součty běžely s nice15; žádné permutace ani náhodné
vstupy se negenerují. Poznámka obsahuje také obecný důkaz identity,
která dovoluje sloučit všechny permutace se stejným rankovým prefixem.

Známá oprava15.3.2023 mění v tabulce5 hodnotu274.42 na274.41.
Je zahrnutá, nikoli nový nález. Jediná nová výkladová mezera
je věta o minimu přesunů pro3,2,1: P0839/C0023 níže.

## P0834: uzavřené vzorce pro prvních osm řádků tabulky

První h-sort má třídy délek Lᵢ, proto

    E A_first=∑ᵢ(H_(Lᵢ)−1),   E B_first=½∑ᵢ binom(Lᵢ,2).

Pro následující1-sort platí přesně dříve prokázané g(8,h)
a f(8,h). U4,2,1 přibudou po prvním průchodu
2g(4,2)+g(8,2) a2f(4,2)+f(8,2). Celá tabulka je:

| Přírůstky | E A | E B | S | T | čas D |
|---|---:|---:|---:|---:|---:|
|1|481/280|14|1|1|204.846428…|
|2,1|8/3|338/35|3|2|235.914285…|
|3,1|35/12|91/10|4|2|220.15|
|4,1|37/12|10|5|2|217.75|
|5,1|437/168|10|6|2|209.196428…|
|6,1|1793/840|32/3|7|2|206.596428…|
|7,1|481/280|12|8|2|209.846428…|
|4,2,1|7/2|874/105|7|3|274.414285…|

Každý S je součet a T počet uvedených přírůstků. Poslední
sloupec je přímé dosazení do9E B+10NT+13T−10S−3E A+1,
N=8. Přesné zlomky v `results/insertion-eight-moment-sums.json`.
Pro4,2,1 jsou E B=2+8/3+128/35 a E A=2+1+1/2.
Všechna tištěná zaokrouhlení souhlasí po známé opravě2023.
Původní274.42 se dalo získat předčasným zaokrouhlením B na8.324;
opravená274.41 používá přesný průměr.

## P0835: obecná identita pro rankové prefixy

Tento důkaz platí pro libovolné pevné N a posloupnost přírůstků,
nikoli jen pro konkrétní osmiprvkový výpočet. Klíče jsou různé,
všech N! vstupních pořadí stejně pravděpodobných.

Pro S⊆{1,…,N} definuj Φ_h(S): v každé h-třídě obsadí prvních
|S∩třída| pozic. Je to množina pozic klíčů pod pevným prahem
po h-sortu, protože úplné uspořádání třídy přemístí všechny
menší klíče na začátek. Proto každý h-sort **komutuje s prahem**.
Φ_h zachovává velikost a je monotónní vůči inkluzi. Totéž platí
pro složení F předchozích průchodů.

Označ S množinu původních pozic k nejmenších klíčů a i původní
pozici dalšího klíče. Pak S→S∪{i} má pravděpodobnost

    k!(N−k−1)!/N! = 1/((N−k)binom(N,k)).                     (R)

Před právě analyzovaným průchodem h jsou menší klíče na F(S).
Poloha dalšího klíče je **jediný** prvek

    p=F(S∪{i})\F(S).

Jednoznačnost plyne z inkluze a rozdílu velikostí1, nikoli
z domněnky o nezávislosti výstupních pořadí.

Tento klíč přispívá k počtu inversí h-třídy právě

    b_h(S,i)=#{q∈F(S):q>p, q≡p (mod h)}.

Počítáme každou inversi při příchodu jejího většího klíče:
menší klíč je napravo v téže třídě. Součet je tedy přesně B_h.
Klíč přispívá k A_h právě tehdy, když není první ve své třídě
a žádný menší klíč neleží před ním:

    a_h(S,i)=[p>h][F(S)∩{p−h,p−2h,…} je prázdná].

To je ekvivalent levopravého minima, které při vložení dosáhne
levého konce; pozdější přesuny v této třídě definici nemění.
Lineárností očekávání dostáváme pro X=A_h nebo B_h

    E X =∑ₖ₌₀ᴺ⁻¹ ( ∑_|S|=k ∑_i∉S x_h(S,i) )
                       /((N−k)binom(N,k)).                  (M)

Pro N=8 jde o256 množin a1024 hran. Algoritmus vyhodnocuje
tuto konečnou identitu, žádný seznam8! vstupů. Není potřeba
nezávislost mezi průchody; F zachycuje jejich skutečné složení.

## P0836: poslední dva řádky tabulky5

Jmenovatele v(M), pro k=0,…,7, jsou

    8,56,168,280,280,168,56,8.

Celé celočíselné součty a_h,b_h pro každý rank a každý průchod
jsou uloženy vedle krátkého reprodukovatelného skriptu. Výsledek
po jednotlivých průchodech:

|Přírůstky|průchod|E A_h|E B_h|
|---|---:|---:|---:|
|5,3,1|5|3/2|3/2|
||3|31/30|11/6|
||1|43/56|29/6|
|3,2,1|3|13/6|7/2|
||2|109/140|12/5|
||1|3/8|27/14|

Proto5,3,1 má E A=2773/840, E B=49/6 a čas253.596428…u;
3,2,1 má E A=2789/840, E B=274/35 a čas280.496428…u.
Všechna A/B/S/T i obě tištěná zaokrouhlení času tím souhlasí.
P0843 navíc odvozuje B pro3,2,1 samostatnou malou GF.

## P0837: skutečný konečný prostor tří průchodů

Legální různé přírůstky pro osm prvků mají tvar h>g>1,
2≤g<h≤7. Jde přesně o15 dvojic, žádné další trojice nechybí.
Tři již doložené řádky byly převzaty; jen12 nových přesných
dosazení(M) je v `results/insertion-eight-three-pass-optima.json`.
Průměry přesunů a časů jsou:

|h,g|E B|čas D|
|---|---:|---:|
|3,2|274/35|280.496428…|
|4,2|874/105|274.414285…|
|4,3|278/35|260.671428…|
|5,2|817/105|260.603571…|
|5,3|49/6|253.596428…|
|5,4|589/70|245.796428…|
|6,2|874/105|256.914285…|
|6,3|253/30|247.15|
|6,4|128/15|237.496428…|
|6,5|269/30|232.696428…|
|7,2|601/70|249.496428…|
|7,3|42/5|237.1|
|7,4|133/15|230.867857…|
|7,5|139/15|225.896428…|
|7,6|31/3|226.846428…|

Každý je jedno přesné vyhodnocení prokázaného součtu; neprovádí
se empirická optimalizace. Minimum E B je817/105 pro5,2,1;
minimum času225.896428… pro7,5,1. Tvrzení, že3,2,1 není
časově nejlepší trojice, je tedy správné i v globálním smyslu.

## P0838: jedno- a dvouprůchodové optimum, i všechny vyšší T

Ze všech šesti možných dvouprůchodových řádků v P0834 je
časově nejlepší6,1, jak kniha tvrdí. Hodnota S=7 skutečně
kompenzuje větší E B: nezaměňujeme optimum přesunů s optimem
přesného času. Všechny15 tříprůchodové časy v P0837 jsou větší
než jednopřírůstkových204.846428…u.

Pro T≥4 není třeba zkoušet další posloupnosti. Každý vložený
levopravý minimální klíč vyžaduje alespoň jeden přesun, tedy A≤B.
Vkládací přesun o k pozic v h-třídě lze rozepsat na k sousedních
záměn v této třídě. Algoritmus tak třídí přesně B transpozicemi.
Jedna transpozice může zvýšit počet cyklů permutace nejvýše o1,
zatímco identita má N cyklů; proto B≥N−C pro každý vstup.
Známý a již doložený průměr C je H_N (viz cyklový blok10–11).

Pro N=8 tedy E(9B−3A)≥6(8−H₈)=4437/140. Zbývající
režie v přesném vzorci je93T−10S+1. Při T=4 je S nejvýše
7+6+5+1=19, takže režie≥183. Každý další legální přírůstek
zvýší tuto dolní mez alespoň o93−10·4=53. Pro všechna T≥4:

    E time_D≥183+4437/140=214.692857…u>204.846428…u.

Tím je jednopřírůstkové optimum pro **všechny** legální
posloupnosti doloženo bez průchodu jejich dalšími kombinacemi.
Opakovaný přírůstek nemůže pomoci: již uspořádaný průchod má
B=A=0 a kladnou režii. Přírůstky≥N se nepoužívají.

ProgramS je podle svého dříve doloženého vzorce ještě o13u
rychlejší: E time_S=191.846428…u, tedy tištěných191.85u.
Toto tvrzení se týká daných MIX programů a rovnoměrných
permutací, nikoli všech možných osmičlenných třídicích programů.

## P0839: nejasný rozsah slova „minimize“ — partial/C0023

Věta92 tvrdí, že tři přírůstky3,2,1 minimalizují průměrný počet
přesunů. V celé třídě legálních tříprůchodových posloupností je
to vyvráceno přesným rozdílem

    E B_(3,2,1)−E B_(5,2,1)=822/105−817/105=1/21>0.

Jde však o odstavec uvádějící tabulku5, která5,2,1 neobsahuje.
Mezi **vytištěnými** třemi trojicemi je3,2,1 opravdu nejlepší.
Proto je V3-C0023 candidate/low: matematický rozdíl je doložen,
nevyřešený je implicitní rozsah tvrzení. Jasná lokální formulace
je „among the sequences in Table5“; při globálním mínění je
třeba uvést5,2,1. Žádný confirmed z této nejasnosti nevzniká.

## P0840: přesně17 přesunů pro3,2,1 a důkaz maxima

Vytištěný vstup8,3,5,7,2,4,6,1 má průběh

    h=3: 6,1,4,7,2,5,8,3     B₃=3+3+1=7,
    h=2: 2,1,4,3,6,5,8,7     B₂=3+3=6,
    h=1: 1,2,3,4,5,6,7,8     B₁=4.

Obecně má první průchod třídy3,3,2, tedy nejvýše7 inversí.
Každá ze dvou následujících čtyřčlenných2-tříd má první klíč
menší než poslední, protože jejich vzdálenost6 je násobek3.
Mezi čtyřmi prvky s x₁<x₄ existují alespoň tři neinverse:
(1,4), a pro každé j=2,3 alespoň jedna z(1,j),(j,4).
Každá třída má proto nejvýše6−3=3 inverse, celkem nejvýše6.
Nakonec je soubor2- a3-ordered, tedy má jen disjunktní sousední
inverse (P0780–0781), nejvýše4. Horní mez7+6+4=17 je dosažena.

## P0841: přesně19 přesunů pro5,3,1 a důkaz maxima

Vytištěný vstup8,5,2,6,3,7,4,1 má průběh

    h=5: 7,4,1,6,3,8,5,2     B₅=3,
    h=3: 5,2,1,6,3,8,7,4     B₃=3+3+0=6,
    h=1: 1,2,3,4,5,6,7,8     B₁=4+1+2+2+1=10.

První průchod má jen tři dvojice, tedy B₅≤3. Kdyby následný
3-sort dosáhl maxima7 pro třídy3,3,2, všechny tři třídy by
musely být sestupné. Z5-ordering a těchto tří sestupností by
pro vstupní klíče x před3-sortem vznikl cyklus

    x₁<x₆<x₃<x₈<x₅<x₂<x₇<x₄<x₁,

což je nemožné. Proto B₃≤6.

Zbývá obecná horní mez10 pro každý3- a5-ordered soubor délky8.
Vzdálenosti3,5,6 dávají10 jistých neinversí. Potenciální inverse
jsou pouze při vzdálenostech1,2,4,7, celkem18. Následujících
osm dvojic **různých potenciálních inversí** je disjunktních;
v každé mohou nastat nejvýše jedny inverse:

|Dvojice párů|zakazující uspořádaný pár|
|---|---|
|(1,2),(2,4)|(1,4)|
|(2,3),(3,5)|(2,5)|
|(3,4),(4,8)|(3,8)|
|(4,5),(5,7)|(4,7)|
|(1,5),(5,6)|(1,6)|
|(4,6),(6,7)|(4,7)|
|(3,7),(7,8)|(3,8)|
|(2,6),(6,8)|(2,8)|

Obě inverse by tranzitivitou porušily uvedený uspořádaný pár.
Proto mezi18 možnostmi chybí alespoň8 a B₁≤10. Zbylé dva
nepárované páry(1,3),(1,8) nic dalšího nevyžadují. Celkem
B≤3+6+10=19, dosaženo uvedeným vstupem. Pomocný výběr osmi
hran byl malý matching na17 vrcholech; tabulka je celý výsledný
ručně kontrolovatelný certifikát, bez závislosti na tom výpočtu.

## P0842: Prattovy přesné průměry a celé maximum B=14

Pro6,4,3,2,1 dává(M) po průchodech

    E A: 1,4/3,23/30,5/12,3/8,
    E B: 1,4/3,73/60,137/105,267/140.

Součty jsou E A=467/120=3.891666… a E B=142/21=6.761904…,
tedy odpověď31 správně tiskne3.892 a6.762. U A jde nejprve
o levopravá minima ProgramuD; již uzavřená involuce P0818
přenáší celý společný zákon(A,B) na koncové inverse Programu31.
Nepřisuzujeme oběma A stejnou hodnotu na témže vstupu.

Maximum B má nezávisle na průměrech následující konečný
potenciálový certifikát. Pro hranu S→S+i polož
w(S,i)=∑ₕb_h(S,i), se skutečnými příslušnými F. Každá permutace
určuje cestu od∅ k plné množině a celkový součet hran je přesně
její B, jak dokazuje P0835. V JSON je256 celočíselných hodnot
Q(S), indexovaných bitovou maskou (bit0 je původní pozice1),
získaných zpětnou rekurencí

    Q(full)=0,
    Q(S)=max_i∉S (w(S,i)+Q(S+i)).

Ta je konečná a acyklická podle |S|. Obsahuje všechny pokračující
možnosti právě jednou na množinu; princip indukce od plné
množiny dokazuje, že Q je přesné maximum zbývajících přesunů.
Zejména každá hrana splňuje w(S,i)≤Q(S)−Q(S+i). Hodnoty mají
Q(∅)=14 a Q(full)=0, takže teleskopicky B≤14 pro každý vstup.
Již ručně ověřený vstup7,3,8,4,5,1,6,2 dosahuje14 (P0819).

Toto je dynamický program na256 stavech s doloženou dostatečností
stavu, nikoli neověřený výstup třídění všech permutací. Přesný
certifikát, definice vah i krátký zdroj jsou uloženy; opakovaný
výpočet již prokázaného maxima A=10 nebyl potřeba. Tím se celé
P0821 mění na checked.

Pro C0022 se nyní doplňuje přesný správný čas:

    324+7·467/120=42149/120=351.241666…u.

Původní důkaz chyby276.24u pomocí dolní meze324u se nemění;
nepotřeboval tyto průměry. Výsledek neuzavírá empirické údaje
pro N=1000 v P0823.

## P0843: samostatná malá GF pro srovnání5,2,1 a3,2,1

Pro dvě2-uspořádané třídy čteme klíče podle rostoucí hodnoty.
Je-li dosud o lichých a e sudých klíčů, d=o−e, pak příchod
dalšího lichého klíče přidá max(−d,0) inversí; dalšího sudého
max(d−1,0). Pořadí uvnitř každé parity je již rostoucí, proto
jde o všechny a pouze inverse finálního1-sortu.

Po5-sortu mají tři původní dvojice vzory lichý–sudý,
sudý–lichý, lichý–sudý; zbývá jeden lichý a jeden sudý singleton.
GF původních rankových prefixů je A²BCD, kde

    A=1+2tz+t², B=1+2tz⁻¹+t², C=1+tz, D=1+tz⁻¹.

Exponent t je velikost prefixu, exponent z jeho rozdíl d.
Koeficient2 pro jedno vybrané místo dvojice odpovídá dvěma
původním možnostem. Označené přechody k dalšímu lichému/sudému
klíči mají GF

    U₅=4ABCD+2tz⁻¹A²CD+A²BD,
    V₅=4tzABCD+2A²CD+A²BC.

Například dvojice typu A dovoluje při prázdném prefixu dva
liché přechody, při jednom vybraném místě dva sudé; proto její
příspěvky jsou2 a2tz. Dvě A vysvětlují faktor4. Analogicky
B a oba singletony dávají všechny zbývající členy.

Po3-sortu jsou třídy lichý–sudý–lichý, sudý–lichý–sudý
a lichý–sudý. Nyní polož

    A=1+3tz+3t²+t³z, B=1+3tz⁻¹+3t²+t³z⁻¹,
    C=1+2tz+t², Q=3+3t².

Koeficienty jsou binomické počty výběrů původních míst v třídě.
Označený přechod ze stavu s r vybranými místy má násobnost
binom(L,r)(L−r); odtud

    U₃=QBC+6tz⁻¹AC+2AB,
    V₃=6tzBC+QAC+2tzAB.

Pro obě varianty je čitatel ranku k přesně

    ∑_d [tᵏzᵈ]U ·max(−d,0)+[tᵏzᵈ]V ·max(d−1,0).

Přímé vynásobení těchto malých Laurentových polynomů dává

    5,2,1: 0,17,60,109,108,63,24,3,
    3,2,1: 0,21,36,65,80,39,12,3.

Po vydělení osmi jmenovateli(R) a sečtení vyjde183/70,
respektive27/14. Toto samostatné dosazení nepoužívá třídicí
rutinu ani smyčku přes podmnožiny; uložené v
`results/insertion-eight-final-pass-gf.json`.

Zbývající průchody lze zkontrolovat ručně. Pro5,2,1 má první
průchod průměr3/2. Jeho lichá třída před2-sortem je
(minA,minC,V,maxB), sudá(minB,U,maxA,maxC), kde A,B,C jsou
nezávislé dvojice a U,V nezávislé singletony. V každé třídě
mají šest párových inversí pravděpodobnosti, v příslušném pořadí,

    lichá: 1/2,1/3,1/6,1/3,1/6,1/3;
    sudá:  1/3,1/6,1/6,1/3,1/3,1/2.

Každý součet je11/6, tedy druhý průchod11/3. Například minimum
dvojice přesahuje maximum jiné dvojice právě pro jedno ze
šesti sloučení dvou dvojic. Ostatní zlomky jsou stejné malé
počty pozic minim/maxim mezi třemi nebo čtyřmi různými klíči.

Pro3,2,1 označ pořadové statistiky dvou trojic A,B a dvojice C.
Lichá třída je(A₁,C₁,B₂,A₃), sudá(B₁,A₂,C₂,B₃). Šest
pravděpodobností je

    lichá: 2/5,1/5,0,3/10,1/10,1/5;
    sudá:  1/5,1/10,0,3/10,1/5,2/5.

Každá dává6/5. Zlomky1/5 a3/10 odpovídají prvním dvěma
pozicím téhož typu při sloučení trojic, případně dvěma pozicím
před druhou pořadovou statistikou;1/10 je jediné sloučení,
v němž celá trojice předchází dvojici. První průchod má7/2.
Proto máme samostatně

    E B_(5,2,1)=3/2+11/3+183/70=817/105,
    E B_(3,2,1)=7/2+12/5+27/14=822/105.

Matematická nerovnost v C0023 tak nestojí jen na univerzálním
výpočetním součtu(M). Výklad věty zůstává výslovně candidate.

## Předání

P0834–0838/P0840–0843 checked; P0839 partial. P0821 uzavřen.
C0023 candidate/low má vlastní poznámku a pětivrstvou evidenci;
C0022 dostal přesný průměr bez změny původního potvrzení.
Strana92 zůstává partial právě kvůli rozsahu C0023. Na93 je
tabulka5 hotová; následují souvisle tabulka6, celé související
nákladové závěry a současná oprava Sedgewickova tvrzení z2025.

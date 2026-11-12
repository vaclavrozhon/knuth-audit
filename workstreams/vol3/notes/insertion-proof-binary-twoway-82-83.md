# Binární a obousměrné vkládání, kruhové pole a vzdálenosti

Zdroj82–83/file93–94, úlohy6–7 na102/file113,
odpovědi619/file630. Originály zobrazeny. Dodatek
rozptylu z23.11.2002 je zobrazen samostatně v
`images/insertion-displacement-errata-file030.png`;
pět vrstev je v `sources/insertion-errata-review.json`.
Nevznikl nový nález ani výpočetní běh.

## P0701: skutečný binární postup a počet porovnání

V seřazeném prefixu délky j−1 hledáme poslední pozici
s klíčem≤K, tedy mezeru r∈{0,…,j−1}. Udržujeme
virtuální meze l=0,u=j; skutečné klíče do l jsou≤K,
od u jsou>K. Krajní virtuální záznamy se nečtou.
Při u−l>1 vezmeme m=floor((l+u)/2). Je-li K_m≤K,
nastavíme l=m; jinak u=m. Počet přípustných mezer
se sníží nejvýše na ceil((u−l)/2); po nejvýše
ceil(lg j) porovnáních máme u=l+1 a správnou mezeru l.
Obě větve zachovávají invariant a přísně zmenšují
kladný rozdíl, tedy algoritmus končí. Rovnost jde
doprava, takže při pevném vstupním pořadí je stabilní.

Pro j=64 se prvně porovnává s32, potom16 nebo48
a tak dále. Je přesně64 mezer a půlení je šestkrát
rovnoměrné, proto opravdu stačí šest porovnání.
Žádný sedmý test krajní meze není skrytým porovnáním klíčů.

Celkový nejhorší počet je∑_(j=2)^N ceil(lg j),
mezi lg(N!) a lg(N!)+N. Integrální sevření součtu
logaritmů dává lg(N!)=N lg N−O(N), tedy N lg N+O(N).
Při rovnoměrných mezerách je průměrná hloubka každého
binárního rozhodovacího stromu alespoň lg j
(Kraftova nerovnost a konvexita), takže totéž
vedoucí chování platí v průměru. Tím je doložen
dopředný odkaz bez předstírání kontroly celé§6.2.1.

## P0702: proč počet porovnání neodstraní kvadratické přesuny

V původním ProgramS má vkládání j přesně b_j přesunů
a b_j+1−[b_j=j−1] porovnání. Z rovnoměrnosti b_j
v P0688 vychází E porovnání=(j−1)/2+1−1/j,
takže součet je N(N−1)/4+N−H_N≈N²/4.

Binární hledání určí tutéž mezeru r. Při pevném levém
okraji prefixu je třeba přesunout j−1−r záznamů doprava;
jejich očekávaný počet je(j−1)/2 a součet N(N−1)/4.
Za předpokladu konstantní ceny přesunu jednoho záznamu
zůstává průměrný čas Θ(N²), i když hledání stojí
O(N log N). Hromadný přesun na stroji s konečnou
propustností mění konstantu, nikoli asymptotický počet
přenesených slov. Netvrdí se dolní mez pro model,
který by neomezeně dlouhý přesun definoval jako jednu
konstantně drahou operaci, ani pro neomezený paralelismus.

## P0703: přesná neuzavřená historická část

Údaj o doporučené hranici přibližně128 osmdesátiznakových
záznamů na IBM705 vyžaduje konkrétní Naglerův strojový
model a srovnávací metodu. Rychlá rešerše nalezla
bibliografický záznam článku „An estimation of the
relative efficiency of two internal sorting methods“,
CACM3(1960),618–620, ale nikoli dostupný primární text,
z něhož by se tato hodnota dala znovu odvodit.
Číselná hranice ani konkrétní popis instrukce tumble
se proto zde nevydávají za nezávisle ověřené.

Jde o partial historický/modelový údaj, nikoli o
vyvrácení kvadratického argumentu P0702. Prvenství
Mauchly1946 a datování dvousměrné metody do počátku
50.let jsou výslovné bibliografické výjimky. Zpětné
citování stejného textu TAOCP by mezeru neuzavřelo.

## P0704: obousměrný invariant a všechny řádky Table2

Seřazený segment délky m má pro nový záznam mezeru r,
0≤r≤m. Lze posunout prvních r záznamů o místo doleva,
nebo posledních m−r o místo doprava. Posuny se provádějí
od volné krajní pozice směrem k mezeře: každý krok
zaplní stávající díru a vytvoří další, takže se žádný
záznam nepřepíše dříve, než se zachrání. Nakonec se
vloží nesený R. Relativní pořadí starých záznamů se
nemění; volba mezery za rovnými klíči zachovává stabilitu.
Rozšířený segment je opět seřazený. Menší počet starých
přesunů je min(r,m−r), s libovolnou volbou při rovnosti.

V Table2 je počáteční503. Další kroky jsou

    87:  (m,r)=(1,0), doleva0;
    512: (2,2), doprava0;
    61:  (3,0), doleva0;
    908: (4,4), doprava0;
    170: (5,2), doleva2 (61,87);
    897: (6,5), doprava1 (908);
    275: (7,3), doleva3 (61,87,170).

Všechny vytištěné mezery i segmenty tedy souhlasí.
Přesuny mají uvedené směry včetně170 a275, u nichž
není nový prvek na vnějším kraji. Nulový přesun
neznamená nulový zápis nového záznamu.

## P0705: přesný význam úspory přibližně poloviny

Pro různé náhodné klíče je r rovnoměrné0,…,m.
Součet min(r,m−r) je s² pro m=2s a s(s+1) pro m=2s+1.
Očekávaný počet starých přesunů při vkládání j=m+1 je

    floor((j−1)²/4)/j
      = j/4−1/2+[j liché]/(4j).

Po součtu j=2,…,N dostaneme

    N²/8−3N/8 + H_N/4 − H_floor(N/2)/8.

Vedoucí člen je tedy poloviční proti N(N−1)/4
u jednosměrného vkládání. V modelu stejné ceny přesunu
záznamu a binárního hledání s O(N log N) režie
konverguje poměr časů k1/2. Tato věta není měřením
času konkrétní krátké implementace. Následující
kruhová implementace přidá jen O(N) přesunů a tedy
zachová tentýž vedoucí člen.

## P0706: úloha6, úplný kruhový invariant včetně změny strany

Máme N kruhově sousedících buněk, jeden pomocný záznam R
a konstantní indexy. Na začátku kroku tvoří již vložené
záznamy jeden souvislý seřazený oblouk S; zbylé nepřečtené
záznamy tvoří jeho doplňkový oblouk U. Počáteční S
obsahuje jeden libovolně zvolený záznam. Nový záznam
vezmeme z krajní buňky U do R, čímž vznikne jediná
díra h vedle S. Na dalších iteracích bereme levý konec U
po předchozím rozšíření S doprava a pravý konec U po
rozšíření doleva, jak uvádí odpověď. První volba je libovolná.

Binárním hledáním přes kruhové indexy určíme mezeru r
a zvolíme kratší přesouvanou stranu S. Označme b buňku
těsně před levým, respektive za pravým okrajem S,
podle právě zvolené strany. **Nesmíme předpokládat,
že h už je na této straně.** Pokud b≠h, leží v b
ještě nezpracovaný záznam. Přeneseme jej z b do h;
tím vytvoříme potřebnou díru v b. Pomocný R stále
obsahuje právě vkládaný záznam. Tento jeden přenos
neznámého záznamu jen přesune konec oblouku U na druhý
konec a zachová jeho souvislost; nerozhoduje se podle
klíče přenášeného záznamu.

Teď se použije přesně posun s dírou P0704, na kratší
straně. Po vložení R je S o jednu buňku delší a U
je zase jediný doplňkový oblouk. Všechny záznamy jsou
zachovány právě jednou. Je-li v kroku poslední záznam,
S má N−1 míst a oba jeho vnější sousedé na kružnici
jsou tatáž jediná díra; b≠h se tedy vůbec nevyskytne.
Tím je ošetřen případ, kdy už nezbývá žádný záznam,
který by se dal použít k přenosu díry.

Jde o konkrétní dokončení stručného návodu odpovědi,
nikoli o tichý předpoklad volného místa na obou koncích.
Při N=0 nebo1 nejsou žádné vkládací kroky.

## P0707: úloha6, paměť, závěrečná rotace a distribuce

Posun záznamu z b do h lze kopírovat po slovech;
nepotřebuje druhý pomocný celý záznam. Stejně probíhají
ostatní posuny. Kapacita je N buněk plus jediný R,
tedy požadovaných N+1 záznamů a O(1) indexových slov.
Každé vložení spotřebuje min(r,m−r) starých posunů,
jeden zápis nového záznamu a nejvýše jeden přenos
nezpracovaného záznamu; hledání vyžaduje O(log(m+1))
porovnání s konstantním přepočtem kruhového indexu.

Na konci je pole kruhově setříděné; fyzický začátek
může být uprostřed logického pořadí. Je-li fyzické
pole rozdělené na B,A a správné pořadí je A,B,
obrátíme B, potom A a potom celé pole. Výsledek je
reverse(reverse(B),reverse(A))=A,B. Každé obrácení
se dělá párovými výměnami pomocí uvolněného R,
tedy s touž pamětí a O(N) přesuny. To dodává vlastní
důkaz rotace bez nezajištěného dopředného odkazu.

Adaptivní výběr z konců U stále dává rovnoměrnou
permutaci čtených **různých** klíčů: podmíněně na
dosud čtených hodnotách jsou zbývající hodnoty
rovnoměrně rozmístěny v U. Zvolený konec závisí jen
na minulosti; přenos z b do h je vůči nečteným hodnotám
slepou permutací pozic. Další čtený klíč je proto
rovnoměrný mezi zbývajícími. Indukce opravňuje použít
P0705 i pro tuto implementaci. Původní stabilita při
stejných klíčích se u takto změněného pořadí čtení
netvrdí; zadání6 ji nevyžaduje.

## P0708: úloha7, přesná střední vzdálenost

Pro n≥1 je každý a_j rovnoměrný1,…,n. Proto

    E|a_j−j| = (choose(j,2)+choose(n−j+1,2))/n.

Sečtení podle j a identita ∑_(j=1)^n choose(j,2)
=choose(n+1,3), dokázaná volbou největšího prvku trojice,
dávají E D=2 choose(n+1,3)/n=(n²−1)/3.
Na jeden záznam je to n/3−1/(3n), jak vyžaduje text83.
Je to čistá vzdálenost, nikoli tvrzení, že žádný záznam
nesmí v konkrétním algoritmu cestovat tam a zpět.

V zadání se používá aktuální známá oprava z12.5.1999:
druhý člen je |a₂−2|, ne |a₂−1|. Starý překlep
není nález. Při n=1 je vzdálenost0; prázdná permutace,
pokud se připustí zvlášť, má také0 a nepoužije dělení n.

## P0709: obecný rozptyl permutačního součtu

Pro n>1 a libovolnou reálnou matici c_ij polož
r_i=∑_j c_ij, s_j=∑_i c_ij, T=∑c_ij a

    d_ij=c_ij−r_i/n−s_j/n+T/n².

Všechny řádkové a sloupcové součty d jsou0.
Pro rovnoměrnou permutaci π platí
∑c_(i,π(i))−E∑c_(i,π(i))=∑d_(i,π(i)).
Jednotlivý člen má pravděpodobnost1/n, dvě různé
řádky/sloupce pravděpodobnost1/(n(n−1)). Pro každé i,j
je ∑_(k≠i,l≠j)d_kl=d_ij, protože ostatní celkové,
řádkové a sloupcové součty jsou nulové. Rozvinutí
druhého momentu tedy dává

    Var ∑c_(i,π(i)) = (1/(n−1))∑d_ij²
      = (1/(n−1))(∑c_ij²−(∑r_i²+∑s_j²)/n+T²/n²).

Odvození používá skutečnou závislost permutačních
pozic; nezaměňuje je s nezávislými uniformními klíči.

## P0710: všechny součty a rozptyl přidaný v2002

Pro c_ij=|i−j| je matice symetrická, r_i=s_i a

    T=n(n²−1)/3,
    Q=∑c_ij²=2n∑i²−2(∑i)²=n²(n²−1)/6,
    r_i=i²−(n+1)i+n(n+1)/2.

Napiš t_i=i−(n+1)/2; pak r_i=t_i²+(n²−1)/4.
Rozvinutím mocnin a konečných součtů1,i,i²,i³,i⁴ je

    ∑t_i²=n(n²−1)/12,
    ∑t_i⁴=n(n²−1)(3n²−7)/240.

Tedy

    ∑r_i²=∑t_i⁴+(n²−1)∑t_i²/2+n(n²−1)²/16
           =n(n²−1)(7n²−8)/60.

Po dosazení do P0709 se v závorce vytkne(n²−1):

    Var D=(n²−1)/(n−1) ·
       (n²/6−(7n²−8)/30+(n²−1)/9)
      =(n+1)(2n²+7)/45.

Pro n=1 je rozptyl0 přímo, takže platí přesně
erratový vzorec [n>1](2n²+7)(n+1)/45. Indikátor
je nutný; nebyl zahozen při dělení n−1. V n=2 mají
obě permutace vzdálenosti0 a2, rozptyl1 odpovídá
vzorce3·15/45. Nepotřebovali jsme enumeraci dalších n.

## P0711: přesný dosah dolní meze pro krátké přesuny

Pokud se záznam i dostane z původního místa i na místo a_i
posloupností jednotkových kroků, musí jich podle trojúhelníkové
nerovnosti urazit alespoň |a_i−i|. Celková skutečná
dráha je proto≥D. Jestliže jedna sekvenční konstantně
drahá operace posune nejvýše pevný počet záznamů o1
(například sousední výměna dva), počet operací je
alespoň D/c pro pevné c. P0708 dává očekávání Ω(n²).

Tím je pro uvedený model doložena věta před Shellsortem
na83. Nezaměňuje se s tvrzením o libovolném RAM sortu,
skokových přesunech, proměnlivě dlouhé blokové instrukci
za jednotkovou cenu nebo neomezené paralelní šířce.
U přímého vkládání je vlastní kvadratický počet starých
posunů doložen zvlášť P0702; pomocný nesený záznam
může při závěrečném zápisu sám přeskočit více pozic.

Historický údaj P0703 zůstává partial. Oba algoritmické
postupy, celá úloha6 i původní a přidaná část úlohy7
jsou argumentově uzavřeny. Další kurzor je Shellsort
na83/file94, nikoli pozdější již pouze přečtené stránky.

# §4.6.3: grafové znázornění a dualita, úlohy 33–35

Audit 4. listopadu 2026. Tištěné strany 467, 480–481, 484 a 696,
3. vydání, první dotisk. Původní sazba těchto míst zobrazena; fyzický
novější dotisk ani prvenství nálezů neověřeny. Nic nebylo odesláno.

**Závěr:** princip duality, příklady (52)/(54) a výsledné počty 33/35
jsou správné. Odpověď 34 má nadbytečný koncový exponent v seznamu
popisků duálního redukovaného grafu: C0228 confirmed. Obecná grafová
formulace potřebuje rozlišit výpočet se zvolenými operacemi od přísně
rostoucí číselné posloupnosti; C0229 zůstává interpretační candidate.
Úlohy 39–40 a jejich bibliografie patří do dalšího bloku.

## 1. Přesný model, redukce a počet cest

**Výpočet** zde znamená posloupnost hodnot začínající 1, spolu se zvolenou
dvojicí dřívějších indexů pro každou operaci sčítání. Indexy označují
výskyty hodnot, které obecně mohou být stejné. **Rostoucí řetězec** má
navíc všechny hodnoty různé a vzestupně seřazené, jak požaduje strana 467.
Toto rozlišení je podstatné v §3 níže.

Graf má pro každý výskyt hodnoty jeden vrchol. Z operandů do výsledku
vedou dvě orientované hrany; při zdvojení jsou rovnoběžné. **Vstupní**
či **výstupní stupeň** počítá hrany včetně jejich násobnosti. Zdroj má
vstupní stupeň nula a stok výstupní stupeň nula. Graf je acyklický:
každá hrana jde od dřívější operace k pozdější.

Nejprve ponecháme pouze předky požadovaného posledního výsledku.
Odstraněné operace jsou vzhledem ke zvolené reprezentaci nepoužité.
Potom vrchol s výstupním stupněm jedna vynecháme a jeho vstupní hrany
přepojíme do jeho jediného následníka. Tím se pouze odstraní jedno
uzávorkování součtu. Počet vrcholů V i počet hran E klesne o jedna.
Výstupní stupně ostatních vrcholů se nemění, takže pořadí těchto
potlačení neovlivní výsledný graf. Všechny vrcholy kromě zdroje mají
vstupní stupeň alespoň dva a kromě stoku výstupní stupeň alespoň dva.

V původním užitečném výpočtu délky r je E=2r a V=r+1. Proto

```
r = E - V + 1.                                      (G1)
```

Pro n=1 používáme jediný vrchol bez hran; vzorec opět dává nulu.

Hodnota vrcholu v je přesně počet orientovaných cest ze zdroje do v.
Prázdná cesta do samotného zdroje se počítá jednou. Indukce podle
pořadí operací je stejná jako součet hodnot operandů; rovnoběžné hrany
rozlišují různé cesty. Potlačení vrcholu zachová cesty i jejich počty.

Naopak pro libovolný takový acyklický multigraf lze vrcholy seřadit
**topologicky**, tedy tak, aby každá hrana směřovala dopředu. Vrchol
vstupního stupně d pak spočítáme d−1 sčítáními jeho d vstupů. Součet
cen je E−(V−1), což je (G1). Dostáváme výpočet, zatím bez záruky
různých hodnot; přesný limit tohoto tvrzení je v §3.

**Obrácení hran** mění zdroj ve stok. Obrácení cest je bijekce mezi
cestami obou grafů, takže výsledná hodnota n i cena (G1) zůstávají.
Dvojí obrácení vrátí původní graf. To dokazuje dualitu na úrovni
výpočtů bez omezení na různost mezivýsledků.

Tvrzení o optimální délce l(n) zůstává správné i pro rostoucí řetězce:
z libovolného grafu vyrobíme výpočet ceny (G1), odstraníme opakované
hodnoty a seřadíme zbývající hodnoty. Dostaneme rostoucí řetězec délky
**nejvýše** (G1). Na druhé straně optimální řetězec sám poskytuje graf
ceny l(n). Obě minima jsou proto stejná. U optimálního grafu nemůže
odstranění opakování skutečně ušetřit krok, jinak by nebyl optimální.

## 2. Hvězdové výpočty a příklady (52)/(54)

**Hvězdový výpočet** v tomto odstavci znamená, že zvolená operace
každého kroku používá bezprostředně předchozí výsledek. Jeho plný graf
obsahuje cestu procházející všemi vrcholy v pořadí. Redukce zachovává
vzájemnou dosažitelnost zbývajících vrcholů, takže je jejich topologické
pořadí jediné.

Obráceně, má-li acyklický graf jediné topologické pořadí v0,...,vs,
vede hrana z v(i−1) do vi. Jinak by šlo tyto sousední vrcholy prohodit;
delší cesta mezi nimi by vyžadovala další vrchol mezi nimi. Součet
vstupů vi tedy můžeme začít hodnotou v(i−1) a postupně přidávat
ostatní vstupy. Vzniká rostoucí hvězdový výpočet. Jeho mezivýsledky
jsou mezi dvěma sousedními popisky, a proto se neopakují. Takto
interpretované kritérium na konci strany 480 je dokázáno.

V grafu (52) jsou popisky 1,3,6,12,39,79 a nenulové násobnosti hran:

```
1 -> 3: 3       1 -> 79: 1
3 -> 6: 2       3 -> 39: 1
6 -> 12: 2
12 -> 39: 3
39 -> 79: 2.
```

Je E=14, V=6, tedy r=9. Po obrácení hran mají tytéž vrcholy,
v opačném pořadí, popisky 1,2,6,12,26,79. To souhlasí s (54).
Číselný příklad 1,2,4,6,12,24,26,52,78,79 skutečně tento graf redukcí
vytvoří. Oba původní příklady délky devět rovněž dávají (52).

## 3. C0229 candidate: které objekty jsou vlastně ekvivalentní?

Strana 467 výslovně zavádí jen rostoucí řetězce a při více rozkladech
maximalizuje větší index. Strana 480 naproti tomu vybírá určitou dvojici
operandů a pracuje s grafem, který na této dvojici závisí.

Konkrétní rostoucí posloupnost a její platně zvolené operace jsou:

```
1, 2, 3, 4, 6, 8, 14;
2=1+1, 3=2+1, 4=2+2, 6=3+3, 8=4+4, 14=6+8.
```

Všechny operace jsou v této reprezentaci užitečné. Redukovaný graf má
vrcholy 1,2,3,4,14 a hrany

```
1 -> 2: 2; 1 -> 3: 1; 2 -> 3: 1; 2 -> 4: 2;
3 -> 14: 2; 4 -> 14: 2.
```

Po obrácení mají tyto vrcholy v opačném pořadí hodnoty 1,2,2,6,14.
Vrcholů s hodnotou 2 jsou dva. Žádný přísně rostoucí řetězec nemůže
mít právě tento redukovaný graf: jeho vrcholy jsou podmnožinou různých
hodnot řetězce a jejich popisky jsou určeny počty cest.

Obrácený graf ovšem představuje platný obecný výpočet se šesti
operacemi, např. 1,2,2,4,6,12,14 s vhodným rozlišením obou dvojek.
Po ztotožnění dvojek lze zkrátit na 1,2,4,6,12,14. Dualita a minimum
podle §1 tím nejsou vyvráceny; problémem je automatické přenesení
konvence o přísném růstu na **všechny** grafy a zachování přesné délky.

Stejná původní číselná posloupnost je také hvězdová v numerickém smyslu:
4=3+1, 6=4+2, 8=6+2, 14=8+6. Výše zvolený graf však má neporovnatelné
vrcholy 3 a 4. Kritérium §2 proto musí mluvit o reprezentaci zvolenými
operacemi, ne pouze o posloupnosti čísel s existencí nějakých hvězdových
rozkladů.

**Hodnocení:** konkrétní nesoulady jsou přesné; závažnost je interpretační.
Autor mohl v grafovém odstavci záměrně přejít zpět k obecné definici
(1)/(2), nebo hvězdovost vztahovat ke zvolené reprezentaci. Proto pouze
candidate, nikoli tvrzení o nepravdivosti matematického principu duality.
Navržené zpřesnění: výslovně povolit v tomto odstavci výpočty s opakovanými
hodnotami a ekvivalenci definovat pro výpočty se zvolenými operacemi.

## 4. Úloha 33: osm řetězců

Před výpočtem 39 jsou povinné hodnoty 1,2,3,6,12. Součet
39=12+12+12+3 lze bez dalšího sdílení uzávorkovat čtyřmi způsoby.
Dvojice nových mezivýsledků před 39 jsou přesně

```
(15,27), (15,24), (24,27), (24,36).
```

Úplnost plyne také rozdělením kořene binárního stromu na jednu a tři
nebo dvě a dvě položky. Nezáleží na pořadí tří identických dvanáctek.
Po 39 lze součet 39+39+1 realizovat mezivýsledkem 78 nebo 40. Volby
jsou nezávislé, protože obě poslední hodnoty převyšují 39. Výsledek
je 4·2=8 různých rostoucích řetězců. Jejich úplný seznam je v JSON.

## 5. Úloha 34 a C0228: skutečné popisky duálního grafu

Pro n>=2 označme m=floor(log2 n), b_k k-tý binární bit n a
q_k=floor(n/2^k), k=m,...,0. Platí q_m=1 a

```
q_(k-1) = 2*q_k + b_(k-1).
```

Levo-pravá binární metoda má po redukci právě vrcholy q_m,...,q_0.
Mezi každými sousedními vrcholy vedou dvě hrany; je-li nový bit 1,
vede navíc hrana ze zdroje 1. Dočasný vrchol 2*q_k před přičtením
jedničky má výstupní stupeň jedna a odstraní se. Každý ponechaný
vnitřní vrchol má alespoň dvě výstupní hrany.

Pro k<m existuje od q_k do n přesně 2^k cest: kromě zdroje nevedou
z těchto vrcholů jiné hrany než dvojice k následujícímu vrcholu.
Zdroj má n cest. Proto má obrácený redukovaný graf popisky

```
1, 2, 4, ..., 2^(m-1), n.                           (G2)
```

Pravo-levá metoda nejprve vytváří mocniny dvou a sčítá vybrané mocniny.
Všechny dočasné součty mají jediné použití a redukcí zmizí. Rovněž
nejvyšší mocnina 2^m má při n>2^m jediné použití. Zůstane řetěz
zdvojování 1,...,2^(m−1), dvě hrany z 2^(m−1) do n a pro každý další
jedničkový bit jedna hrana z příslušné mocniny do n. Je to přesně
obrácený předchozí graf. Pro n=2^m je poslední mocnina sama stokem;
(G2) stále platí. Pro n=1 je graf jediný vrchol.

**C0228:** na straně 696 odpověď končí seznam popisků duálního grafu
členem 2^e0 před n. Pro n=3 je e0=1 a oba řetězce jsou 1,2,3.
Vrchol 2 se odstraní, takže v obou redukovaných grafech zůstanou pouze
1 a 3, spojené třemi hranami. Uvedená 2 není popiskem redukovaného
grafu. Nejmenší protipříklad je 3; pro 1/2 jsou grafy triviální.
Oprava pro n>=2 je 2^(e0−1); případ n=1 se uvede zvlášť. Samotná
odpověď „true“ i seznam původních popisků floor(n/2^k) jsou správné.

Poznámka o 2^e-ární metodě má stejný strukturální důkaz. Rozepíšeme
nenulovou číslici d_i jako 2^h_i*q_i, kde q_i je liché. Levý výpočet
předpočítá liché mocniny a přidává q_i v pozicích ei+h_i. Obrácením
hrany jeho hlavního postupu vzniknou mocniny 2^(ei+h_i), seskupené
do košů F_q=sum_{q_i=q} 2^(ei+h_i). Obrácením předvýpočtu lichých
čísel 1,3,5,... vzniknou postupné součty H_q=sum_{p>=q, p odd}F_p.
Výsledek je H_1+2*(H_3+H_5+...), protože F_q má koeficient q.
To je přesně košová konstrukce odpovědi 9; zbytečné jednotkové
násobení a nepoužité uzly se vynechají na obou stranách. Tento argument
je o grafu operací; případné číselné duplicity podléhají výhradě §3.

## 6. Úloha 35: obecné počty, nikoli jen experiment

Pišme n=sum_i 2^e_i, e0>...>et>=0, a nejprve předpokládejme
podmínku zadání e0>e1+1. Při t=0 je pouze řetězec zdvojování.

V levém redukovaném grafu z §5 má každý nový jedničkový bit součet
a+a+1, kde a>1. Jsou dvě uzávorkování: mezivýsledek 2a nebo a+1.
Obě hodnoty leží přísně mezi sousedními povinnými popisky a a 2a+1;
volby se tedy nekříží a nemohou vést ke stejné posloupnosti. Nulový
bit dává jediné zdvojení. Je t nezávislých dvojic voleb, tedy 2^t
řetězců. Když e0=e1+1, první součet je 1+1+1 a obě volby splývají;
zbývá 2^(t−1), jak uvádí odpověď.

Pro pravý graf jsou povinné mocniny 1,...,Q, kde Q=2^(e0−1),
a poslední součet má listy

```
Q, Q, 2^e1, ..., 2^et.                              (G3)
```

Díky e0>e1+1 jsou posledních t listů různé a menší než Q. Jejich
celkový součet je menší než Q. Číselná hodnota podmultimnožiny
jednoznačně určuje, které malé listy a kolik kopií Q obsahuje:
malé listy přečteme z bitů pod Q a počet kopií Q ze zbytku.

Žádný vnitřní součet stromu není povinnou mocninou <=Q. Dva vnitřní
vrcholy mají různé součty: při vnoření jeden obsahuje více kladných
listů; při disjunktnosti by shodné podmultimnožiny vyžadovaly dvě
kopie některého malého listu, anebo pouze jednotlivé listy Q.
Seřazení všech součtů a povinných mocnin proto dává platný rostoucí
řetězec. Naopak ze součtů obnovíme podmultimnožiny a jejich vztah
obsahování, tedy strom; dvě různé konstrukce nesplynou v jednu
číselnou posloupnost. Počet stromů je tudíž opravdu počet řetězců.

Označme f_j počet neuspořádaných plných binárních stromů s j+1 různě
pojmenovanými listy. Nový pojmenovaný list lze připojit na každé
z 2j−1 míst stromu s j listy, včetně místa nad kořenem. Tím je
f_j=(2j−1)f_(j−1), f_0=1, tedy f_j=(2j−1)!!.

Dočasně rozlišíme obě Q v (G3). Je f_(t+1) stromů. Záměna těchto
dvou jmen má pevné právě stromy, v nichž jsou oba listy sourozenci:
jinak by záměna musela přemístit i jiný, jedinečně pojmenovaný list.
Po sloučení sourozenců v jediný list je pevných stromů f_t.
Ostatní tvoří dvojice. Počet nerozlišených stromů je proto

```
(f_(t+1)+f_t)/2,
```

přesně jako v odpovědi. Podmínka o vedoucí mezeře je pro tento
argument podstatná: při e0=e1+1 jsou nejvyšší listy tři stejné.

## 7. Nezávislé kontroly a zdrojová omezení

`verify_powers_graphs.py` má oddělené bloky. Výpočty jsou celé přesné.
Blok `graphs` prochází všechny rostoucí řetězce se všemi zvolenými
páry operandů do délky sedm; nikoli jen hvězdové či optimální řetězce.
Počty cest kontroluje nezávislou maticovou řadou I+A+...+A^(V−1),
kde A je matice násobností hran. Obrácené grafy znovu rozepíše na
operace a redukuje. Hvězdové rekonstrukce jsou testovány explicitně.

`binary` porovnává grafy obou skutečných binárních konstrukcí pro
1<=n<=16384. `counting` enumeruje stromy všemi rozklady multimnožiny
listů, nezávisle na vzorci s dvojitým faktoriálem. Výsledné číselné
posloupnosti a jejich grafy znovu ověřuje; také hledá odpovídající
rozklady všech osmi řetězců v úloze 33 nezávisle na stromovém výčtu.
Přesné počty, časy a ukázky jsou v `results/powers-graphs.json`.

Prohledáno všech šest vrstev: all2-prepre, all2-pre, all2, err2,
err2-2e a původní err2.textxt. Kontrola zahrnuje stránky 467/480–481/
484/696, odpovídající starší stránkování a výrazy pro grafy, dualitu,
redukci a růst. Oprava C0228 ani zpřesnění C0229 nenalezeny. Sousední
oprava 2003 na str.481 mění pouze „(k+1)-st“ v úloze 5; opravy 2005
k duálu v úloze 42 se těchto tvrzení netýkají.

Primární doplňující zdroj: D. J. Bernstein, *Pippenger's exponentiation
algorithm*, verze datovaná 2002-01-18, sazba 2022-03-27, §5, str.10–13
(čten úplný text této části). Obsahuje vlastní maticové vysvětlení
transpozice a výslovně vztah obou 2^e-árních metod. Historické výroky
o jiných autorech nepřebíráme jako nezávisle ověřené prvenství.
Knuthův autorský seznam a stránka sborníku dokládají práci Q58;
její původní úplný text jsme tímto nezískali ani neprohlašujeme za čtený.

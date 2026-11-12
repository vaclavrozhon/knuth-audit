# Upřesnění dřívějších census mezí, 7. listopadu 2026

X0122. Primární [Muroga–Tsuboi–Baugh 1970](https://people.eecs.berkeley.edu/~alanmi/publications/other/01671639_002.pdf)
je nyní dostupný; originály p820–822 zobrazeny. Žádný census nebyl opakován.

* P1114: 175 428 patří kanonickým pozitivním self-duálním typům s nejvýše
  devíti podstatnými proměnnými; přesně devět má 172 958 typů.
* P1115: dva zlomkové případy znamenají necelá extrémní optima původního LP,
  nikoli libovolné necelé body optimální stěny. Oba konkrétní případy máme
  nezávisle dokázané v proof-089/091; úplnost počtu nikoli.
* P1117/P1118/P1120: pramen uvádí maxima první váhy 42, součtu 209 a
  poslední váhy 11. Globální meze zůstávají nereprodukované.
* P1119: výraz „unique“ u příkladu na p820 přímo kvalifikuje jeho optimum;
  jedinečnost funkce mezi všemi maximalizátory tím nepřebíráme.

Těchto šest povinností zůstává partial; dřívější bibliografická nedostupnost
je vyřešena. Přiřazení zdrojových údajů není nezávislý důkaz úplného censu.

## Přesný vlastní důsledek již uzavřené jednoznačnosti

Pro funkci z proof-091 je jediný normalizovaný optimální vektor

    (33,29,21,17,14,10,8,3,3)/2.

Libovolný automorfismus proměnných této funkce musí zachovat celý její
přípustný LP a cíl Σw, a tedy i jeho jediné optimum. Vektor má právě
jednu dvojici shodných souřadnic. Automorfismů je proto nejvýše dva;
záměna posledních souřadnic váhy opravdu zachová a je automorfismem.
Je jich přesně dva. Orbit-stabilizer tedy dává 9!/2=181 440 různých
označených funkcí už z přejmenování této jediné funkce. Všechny zůstávají
monotónní, self-duální a prahové a mají necelé jediné optimum.

Proto údaj 175 428 ani „dva“ nelze číst jako počty všech funkcí na
označených proměnných. Pro tento závěr se nic neenumerovalo: přebírá se
přesný důkaz jednoznačnosti v proof-091 a elementární grupové počítání.
Nezaměňovat s přepočítáním samotného zdrojového počtu typů.

## Zbývající otázka konvence, nikoli nový confirmed nález

Původní p78/file95 výslovně odlišuje všechny funkce od identifikace
přejmenováním v Table 4 a od dalších komplementací v Table 5 na p79/file96.
Rovněž odpověď 104 na p553/file570 byla zobrazena: její algoritmus K
předpokládá seřazené nezáporné váhy, ale statistická závorka typy výslovně
nepojmenovává. Zůstává tedy otázka, zda je v této závorce kanonizace
zamýšlena jako implicitní pracovní konvence. P1114 zachovává tento přesný
výkladový limit. Nevytváří se confirmed karta z pouhého vynechaného slova;
matematický rozdíl obou významů je výše doložen.

# První průchod: file 191–230 / tištěné 174–213

6. listopadu 2026. Celý rozsah přečten v OCR i původní sazbě. Dokončen text
§7.1.3 a všechna jeho zadání1–218; na202 začíná §7.1.4, přečten přes213.
Žádný nový nález ani kandidát. Žádný matematický program, census či simulace.
Zadání jsou přečtena, nikoli vyřešena; odpovědi čekají na souvislý průchod.

## Konkrétní obsah a omezení

- Str.174–175: Levialdiho automaton, Cheshire cat, hierarchie černých/bílých
  komponent a průběžné zpracování řádků. Argument M+N−1 používá posun
  nejnižší diagonály; zachování komponent a přesné časy obrázků se bez
  simulace přebírají jako tvrzení, jejich důkazy jsou v úlohách176/177.
- Str.176–180: digitizace křivek, horizontální hranice a prefixový XOR,
  kuželosečky, Algorithm T a squines. Diference170 vyplývají přímo z168.
  Q(20,0)=−75, Q(21,0)=85, Q(20,2)=−43, Q(20,3)=21 souhlasí. Přečteny
  všechny čtyři směry T, aktualizace Q/R/S a jejich předpoklady, včetně(v).
  Zrcadlové aktualizace a intervalová maska172 dávají správné znaménko a
  krajní bity. Úplný důkaz T/Bezierových konstrukcí v odpovědích182–187
  zatím nečten; obrázky a celá elipsa neregenerovány.
- Str.180–183: branchless příklady, merge loop, MOR/MXOR, perfect shuffle
  a CRC. Maska(q|−q)>>63 rozliší nulu; záporné indexy merge loop používají
  znaménkový test jejich AND. Časování, cache a výkon na skutečném hardwaru
  neměřeny. CRC181 odděluje horní a dolní byte, historická oprava exponentů
  v βm už je zapracovaná. Matice A/B a úplný64bitový CRC nebyly implementovány.
- Str.184–202: celá zadání1–218, včetně nimbers, broadword lower bounds,
  permutačních sítí, bytewise arithmetic, NCA, pentagridu, bitmap, parity
  patterns, kódování a MMIX. Původní negace, exponenty, diagramy a tabulky
  přečteny. Např. knight mask#42 vede na a3/c3/d2/e2/f3/h3, tedy#a51800.
  Neprováděla se syntéza minimálních řetězců, vyčíslení velkých period,
  Ulamův census, simulace Life/thinning ani implementace jednotlivých řešení.
  Aktuální status otevřených problémů a standardizační podrobnosti Unicode/
  UTF-8/UTF-16 nebyly porovnány s externími prameny. To není jejich certifikace.
- Str.202–205: ordered/reduced BDD, beads a jednoznačnost. Pro délku2^n
  je neprimitivnost právě opakovaným čtvercem. U medianu je šest beads,
  uvedená náhodná truth table má1+2+2+2+2=9 uzlů včetně sinků. Obrázky
  odpovídají rozkladům tabulek a negacím.
- Str.206–209: základní operace, sekvenční instrukce, Algorithm C, uniformní
  volba a Algorithm B. Faktory2^(v_child−v_parent−1) v C počítají přeskočené
  proměnné, ve váženém B je nahradí součet kladných vah z W. Příklad C dává8;
  u C6 je13+5=18 nezávislých množin a uvedeno5 jader. Oprava rozsahu
  podmínky h≠0 v B3 z2012 byla zohledněna. Všech48 pořadí instrukcí ani
  C100 počet1,630,580,875,002 a velikost855 BDD nepřepočítány.
- Str.210–213: vážené příklady, connectedness/reliability, abstraktní
  distributivní operace a friendly functions. Ve vypsaném kernelu100 jsou
  mezery2/3, takže splňuje independence/maximality;38−2·5=28. Optimalita
  a příklady grafu států155/492, počty266137/211954906 a velikosti428/780
  se nereprodukovaly. Součet koeficientů(19) je431; poslední koeficienty
  v(21) souhlasí s112 hranami a binom(112,2)−4=6212 (čtyři rohové řezy).
  Velké koeficienty a BDD43790 nebyly znovu počítány. Rozvoj22–25 zachovává
  pořadí nekomutativních operací; symetrický strom má n(n+1)/2 branchů
  a nejvýše dva sinky. Důkaz kondenzace proměnných je odkazován doúlohy40.

## Errata a pokračování

Relevantní `all4a-pre`, `all4a`, `err4a`, `all4f1`, `err4f1` prohledány.
F1 offset132 pokračuje i proBDD. Změny F1p47 Algorithm T a p51 CRC již
zapracovány; totéž zadání35/58/72/73/190/218 a bead count na213.
Pozdější známé opravy: parenthesis trace23 na186 (2024), anglické svazky25,
boardword127, definice D/L173, komponenta176, hint184, směr rotace189,
přiřazení196, nová varianta203, doplněná219, formulace208 a B3 na209.
Modulární zápis v191(c) na200 je opraven v2025. Vše pouze v evidenci;
žádné vlastní karty ani červené stránky.

Bibliografie, citace, historické priority, externí standardy a současné
stavy výzkumu výslovně neověřeny. Reviewed znamená celé přečtení v prvním
průchodu, nikoli úplné řešení všech cvičení či certifikaci číselných údajů.

Doklady: `sources/file191-230-ocr.txt`, `sources/file191-230.pdf`,
`images/file191.png` až `images/file230.png`. Offset file=printed+17.
Další kurzor **file231 / tištěná214**, pokračování friendly BDD functions.

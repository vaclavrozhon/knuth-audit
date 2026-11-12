# §3.4.2: prokládání karet a historický kontext

Kontrola 1. listopadu 2026. Text 142–148 a odpovědi 590–592 byly přečteny
v původní sazbě, včetně relevantních oprav všech čtyř vrstev errat.
Matematika S/R/P a úloh je v navazujících poznámkách. Zde doplňujeme
odhad promíchání a přesně vymezujeme historické doklady. Bez nového nálezu.
Úloha 16 zůstává samostatně partial kvůli konstantě lineárního sondování.

## Co znamená vzdálenost 10 procent

V citovaném Gilbertově–Shannonově–Reedsově modelu (GSR) rozdělíme balíček
N karet řezem velikosti Binomial(N,1/2), tj. velikost r má pravděpodobnost
binomial(N,r)/2^N. Pak opakovaně upustíme další kartu z levé nebo pravé
hromádky s pravděpodobností úměrnou počtu zbývajících karet v ní.
To není tvrzení o libovolném lidském proložení.

Pro dvě pravděpodobnostní rozdělení P,Q na permutacích definujeme jejich
**totální variační vzdálenost** jako polovinu součtu |P(pi)−Q(pi)| přes
všechny permutace pi. Rovná se největšímu rozdílu pravděpodobností téže
události. Q dále označuje rovnoměrné rozdělení, Q(pi)=1/N!.

Inverzní GSR proložení je totéž jako přidělit každé kartě nezávislý
rovnoměrný bit a stabilně je seřadit podle bitu; při rovnosti zachováme
původní pořadí. Binomický řez je počet nul, a podmíněně na něm jsou
všechna proložení stejně pravděpodobná. K takových inverzních proložení
odpovídá stabilnímu seřazení podle nezávislých rovnoměrných štítků
z 0,...,a−1, kde a=2^K. Inverze permutací zachovává vzdálenost od Q,
takže stačí analyzovat tuto jednodušší konstrukci.

Má-li výsledná permutace pi přesně d **sestupů**, tj. indexů i, kde
pi_i>pi_(i+1), její štítky musejí podél pi neklesat a na sestupech
striktně růst. Odečtení počtu předcházejících povinných růstů dává

```text
P(pi) = binomial(a+N−d−1,N) / a^N,
```

s hodnotou nula pro a<=d. Eulerovo číslo A(N,d) zde označuje počet
permutací N prvků s d sestupy. Vložením největšího prvku do menší
permutace dostaneme rekurenci

```text
A(1,0)=1,
A(N,d)=(d+1)A(N−1,d)+(N−d)A(N−1,d−1),
```

kde ostatní neexistující indexy mají hodnotu nula. Přesná vzdálenost je
proto polovina součtu A(N,d)*|P_d−1/N!| pro d=0,...,N−1.

[Program](../verify_riffle_distance.py) tuto formuli nejprve nezávisle
ověřil explicitním seřazením všech 6669 štítkových historií v 15 modelech
N=2,...,6, a=2,3,4. Počty sestupů zároveň porovnal s úplným soupisem
permutací. Pro N=52 pak počítal všechny hodnoty přesnými zlomky:

| Počet proložení K | Totální variační vzdálenost |
|---|---|
| 6 | 0.6135495965656284 |
| 7 | 0.3340609994681515 |
| 8 | 0.1671586419269574 |
| 9 | 0.0854201934090618 |
| 14 | 0.0026890129772813 |

Desetiprocentní práh je tedy v tomto modelu 9. Tištěné tvrzení, že
**alespoň 7 je nutných a 14 postačuje**, je správné; netvrdí, že 7 stačí.
Vzdálenost při dalším nezávislém proložení nemůže růst: násobení stejným
Markovovým jádrem kontrahuje součet absolutních rozdílů pravděpodobností.

Navíc existuje jednoduchá mez použitá už v citovaném článku. Podmíněně
na navzájem různých štítcích je pořadí přesně rovnoměrné. Rozdělení je
proto směsí Q a zbylého rozdělení při kolizi štítků, což dává

```text
TV <= 1 − product_{i=0}^{N−1}(1−i/a),  pokud a>=N.
```

Pro N=52,K=14 je tato horní mez 0.0778224924370754<0.1. Všechny
normalizace a nerovnosti pro K=1,...,14 byly ověřeny přesně; log obsahuje
pouze zaokrouhlené prezentace. Výpočet skončil s návratovým kódem 0.

Primární [Aldous–Diaconis, AMM 93 (1986), 333–348](https://www.stat.berkeley.edu/~aldous/Papers/shuffling.pdf)
byl v příslušných pasážích přečten ze scanu: definice vzdálenosti na 335,
lemma o silném rovnoměrném čase na 336, příklady na 338–340, model a
Reedsův odhad na 343–345 a související diskuse na 346. Uložené obrazy
343–345 potvrzují obě tištěné meze; vlastní přesná formule výše poskytuje
nezávislou kontrolu. Nejde o kritérium dosažitelnosti v úloze 14, které
řeší libovolné řezy a proložení bez tohoto pravděpodobnostního modelu.

## Další text a citace

Přibližná velikost rezervoáru n(1+log(N/n)) při N/n=1000 dává poměr
0.0079077553 k původnímu souboru, tj. přibližně 1/126.46. Údaj „about
1/125“ je rozumné hrubé zaokrouhlení, nikoli nová chyba. Přesný harmonický
vzorec a jeho rozptyl jsou dokázány v notes/sampling.md.

Různý seed při každém spuštění zabrání opakování téhož deterministického
běhu, ale sám o sobě není důkazem nezávislosti. Poznámka o datu na 143
nenahrazuje matematický předpoklad nezávislých rovnoměrných U v důkazech
algoritmů. Souběžné vzorkování kategorií používá pro každou vlastní stav
počítadel; pro nezávislost vzorků také nezávislé vstupní náhodné veličiny.

Historické doklady mají následující rozsah:

- Fan–Muller–Rezucha, JASA 57 (1962), 387–402: název, autory, ročník,
  číslo 298 a stránky potvrzuje [obsah vydavatele](https://www.tandfonline.com/toc/uasa20/57/298?nav=tocList).
  Přímý článek v tomto běhu vracel HTTP 403; původní důkazy nebyly čteny.
- T. G. Jones, CACM 5 (1962), 343: původní text nebyl dostupný.
  Bibliografii podporuje primární [Vitterův článek, reference 6](https://www.ittc.ku.edu/~jsv/Papers/Vit85.Reservoir.pdf),
  jehož indexovaný závěr byl přečten; nezávislost historického objevu
  není tímto auditem dokázána. Atribuce algoritmu R Watermanovi je
  osobní historický údaj knihy, nikoli rekonstruovaný primární dokument.
- Fisher–Yates, Statistical Tables (1938), Example 12: existenci vydání
  dokládá [Fisherova bibliografie v Adelaide](https://digital.library.adelaide.edu.au/bitstreams/dede5f0e-5d72-4390-996e-72da90748c33/download).
  [Wellcome katalog](https://wellcomecollection.org/works/zht9s9dd) je pro
  pozdější vydání. Samotný Example 12 prvního vydání nebyl přečten;
  tuto citaci nelze označit za ověřenou stránku ani za úplný důkaz priority.
- Durstenfeldův Algorithm 235 byl přečten celý v primárním přetisku
  Collected Algorithms from ACM, svazek 2, list 235-P 1-0 (souborová
  strana 22). Přesný klesající cyklus a výměna odpovídají P. Na stejném
  listu je Pikeova poznámka s citací CACM 7 (July 1964), 420. Samostatný
  list, text, obraz a metadata původního souboru jsou uloženy; nejde o
  tvrzení, že byla zkontrolována původní sazba časopisecké strany 420.
- Stanford GraphBase (1994), 104: inside-out konstrukce je matematicky
  dokázána v notes/sampling-extensions.md; tuto stránku jiného titulu
  jsme nečetli. [Autorova stránka knihy](https://cs.stanford.edu/~knuth/sgb.html)
  potvrzuje titul, ne tento konkrétní pinpoint.
- Vitterovy práce 1984/1985/1987 jsou doloženy jeho
  [vlastním katalogem](https://www.ittc.ku.edu/~jsv/Papers/catalog/5SAMPLING_HISTOGRAMS.html).
  Úloha 8 má vlastní úplný důkaz, včetně O(1) squeeze; nespoléhá na
  nepřečtené důkazy celých článků. Nové úlohy 18 a 19 mají samostatné
  podrobné primární doklady v notes/exchange-shuffle.md a priority-sampling.md.

Anekdoty o hráčích bridge a vzniku osobních nápadů nejsou novými
matematickými tvrzeními. Absence původního historického dokladu není
považována za protipříklad. Kapacita konečného seedu a hodnoty 13! proti
2^32 byly již ověřeny v notes/sampling-extensions.md.

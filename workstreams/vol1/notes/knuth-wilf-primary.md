# Knuth–Wilf: původní zobecnění Kummerova výsledku

2. listopadu 2026, X0693. Z původní sazby byly přímo přečteny
všechny strany 212–219 článku *The power of a prime that divides
a generalized binomial coefficient*, Crelle 396 (1989).
[Kopie SUB Göttingen](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0396/LOG_0011.pdf)
má devět stran PDF: knihovní obálku a osm stran článku.
SHA-256 je `15317d48fbaba1350c7adee03771c4abe85f70bf3851c3a63952c4f2b9c5b71c`.
Moderní knihovní manifest poskytl funkční odkaz; předchozí HTTP403
autorského přetisku a nefunkční staré katalogové cesty zůstávají
poctivě zachovány v protokolu.

Přímo porovnána byla úloha 1.2.6-11 na 70 a odpověď na 484.
Její poslední věta odkazuje právě na analogické výsledky pro
q-nomiální a Fibonomial koeficienty. Bibliografie souhlasí.
Článek tyto výsledky skutečně obsahuje: Theorem 1 na 216 pro
Gaussovy koeficienty s celým q>1 a Theorem 2 na 217 pro
Fibonacciho součiny. Výjimka prvočísla 2 je ošetřena zvlášť.

Jádro obecného argumentu je Proposition 1–3 na 213–215.
Pro kladnou celočíselnou posloupnost C_j je její zobecněný
koeficient podílem součinů, analogickým faktoriálnímu podílu.
Počet členů dělitelných p^k určuje příspěvek k násobnosti p.
Jestliže dělitelnost nastává právě na násobcích indexu r(p^k),
je tento počet floor(n/r(p^k)). Rozdíly tří takových podlah
pak počítají přenosy. Pro r(p^k)=p^k dostáváme původní
Kummerovu formuli, jejíž samostatný důkaz už je v
[binomial-congruences.md](binomial-congruences.md).

Tím je uzavřen přesný odkaz na zobecnění, nikoli všechny
historické citace celé §1.2.6. Dodatečný obsah článku o
determinantech na 218 a závěrečné poznámky na 219 byly
přečteny pro kontext; jejich úplný nezávislý audit není
součástí tohoto uzavření. Čtyři vrstvy errat neobsahují
změnu této citace ani příslušné věty odpovědi 11;
`sources/knuth-wilf-followup/errata-review.json` uchovává
vyhledání včetně sousedních změn odpovědi 10.

Nové matematické testy nebyly potřeba ani spuštěny.

## Původní Kummerova pasáž, X0694

[Kummerův článek](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0044/LOG_0014.pdf),
*Über die Ergänzungssätze zu den allgemeinen Reciprocitätsgesetzen*,
byl získán jako původní sazba Crelle 44, 93–146. Přímo přečtený
titul celého svazku uvádí Berlín 1852; nadpis na 93 identifikuje
Kummera a stejný název. PDF článku má knihovní obálku a 54 stran;
SHA-256 `492541904fa57a363e60c5a08c9d5dae5dff61adba8d13f521a61586920d3da4`.

Rozhodující četba je od samostatného Lehrsatz na dolní části 115
po závěr `N=epsilon+epsilon_1+...+epsilon_(k−1)` na 116.
Na 115 je násobnost prvočísla q ve faktoriálu vyjádřena pomocí
součtu číslic; na 116 jsou explicitní rovnice sloupcového sčítání,
jednotlivé přenosy 0 nebo 1 a závěr o jejich součtu. Jde přesně
o atribuci zadání 1.2.6-11, nikoli jen o příbuznou kongruenci.
Strany 114 a 117–118 byly prohlédnuty pro ohraničení této vložené
pasáže; navazující teorii zákonů reciprocity zde necertifikujeme.

V prostředních dvou zjednodušených čitatelích na 116 není zapsán
poslední přenos jako dodatečná vedoucí číslice součtu, ačkoli
v předcházejícím faktoriálním vzorci uveden je. Pro samotný důkaz
lze zápisy doplnit úvodními nulami tak, aby poslední přenos byl
nulový. Náš dřívější důkaz (K1) výslovně zahrnuje konečný vedoucí
sloupec a tuto nejasnost nemá. Není to chyba textu TAOCP a tento
detail externí sazby se nevydává za nový nález ve svazku.

Matematika úlohy 11, přesná Kummerova atribuce i citace zobecnění
Knuth–Wilf jsou nyní doloženy. Úloha 11 se proto může změnit na
checked; souhrnná X0084 a jiné binomické pramenné úlohy zůstávají
partial podle svých konkrétních nepřečtených citací.

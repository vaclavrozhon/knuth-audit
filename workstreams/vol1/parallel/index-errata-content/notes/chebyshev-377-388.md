# Kandidát: Čebyševovy cíle ze svazku 4B

Lokální označení `chebyshev-377-388-wrong-volume`. Bez globálního ID,
stav candidate. Předmětem je nové heslo ve veřejných erratech svazku 1,
nikoli správné původní heslo `index-0293`.

Přímo čtené indexové obrazy `all1` PDF 16 a `err1` PDF 14 mají
Čebyševovo jméno, nové cyrilské varianty a cíle **377, 388**. Krátký
`err1` je zde skutečný duplikát dlouhého seznamu. Čísla dokládá i
zdrojový TeX `errata/originals/err1.textxt`; nejde o OCR omyl.

Přímo znovu přečtené původní strany svazku 1:

- 377 (`parallel/oriented-trees/images/vol1-file392-p377.png`) obsahuje
  úlohy o automorfismech, překořenění a kostrách orientovaných stromů,
  Eulerových tazích a karetním patience. Čebyševova osoba či výsledek
  zde nemá věcný cíl.
- 388 (`parallel/tree-enumeration/images/p388.png`) pokračuje
  centroidovou enumerací volných stromů, připisuje formuli Jordanovi
  a začíná enumeraci uspořádaných a binárních stromů. Čebyševův cíl
  zde rovněž není.

Hledání podle obou stran i Chebyshev/Tschebyscheff ve všech čtyřech
vrstvách je uloženo v `results/chebyshev-errata-search.json`.
Přímo obrazově přečtené změny k 377 na prepre PDF 26 pouze opravují
P table a oriented walks; změna k 388 na all1 PDF 10 pouze doplňuje
podmínku maxima velikosti větve. Žádná z těchto změn nevkládá
Čebyševův text. Naproti tomu all1-pre PDF 19 má správné cíle
**inequalities, 98, 104, 472**. Původní index měl 98 a 104; nový
explicitní konec odpovědi 31 na 472, přímo viděný v pre PDF 14,
jmenuje Chebyshev's monotonic inequality.

Stejný nový řádek včetně cyrilice a dvojice **377, 388** byl přímo
přečten v `errata/pdf/all4b.pdf`, PDF 24 (obraz `images/all4b-24.png`).
V dostupném svazku 4B, první vydání, druhý tisk 2022, odpovídají oba
cíle konkrétním Čebyševovým zmínkám:

- 377, odpověď MPR-48: pravděpodobnostní nerovnost a explicitní
  Čebyševova citace z roku 1874; PDF 397, `images/vol4b-p377.png`.
- 388, poznámka odpovědi MPR-113: funkce psi(n)=ln lcm(1,...,n),
  její atribuce Čebyševovi a odhad Theta(n); PDF 408,
  `images/vol4b-p388.png`.

Přečteny byly uvedené cílové odstavce a okolí, nikoli matematické
závěry celého svazku 4B či citované Čebyševovy originály. Shoda
podporuje záměnu svazku při aktualizaci jmenných variant; konkrétní
redakční postup je inference.

Navržená lokální náprava ve svazku 1: odstranit nesouvisející 377,388
a zachovat správné cíle nerovností 98,104,472 z předchozí vrstvy,
při zachování nových pravopisných variant jména. Bez úplné novější
sazby indexu netvrdíme, že chyba již pronikla do dalšího tisku knihy,
ani že nová hlavní jmenná položka nutně vymazala staré podheslo
inequalities.

# Předání §2.3.4.3 — Infinity Lemma

Stav: **technický audit vlastní látky dokončen; bibliografický audit
částečný s přesně vypsanými mezemi**. Adresář je po vytvoření manifestu
zmrazen. Globální evidenci, modely ani commity tento pracovník neměnil.

## Inventář potvrzený originály

Hlavní text začíná dole na s. 382 a končí před cvičeními na s. 384.
Úlohy 1–5 začínají na s. 384, úloha 5 pokračuje na s. 385, úloha 6
je na s. 385 a úlohy 7–8 na s. 386. Odpovědi začínají dole na s. 586,
pokračují na s. 587 a odpověď 8 končí v horní části s. 588 před
nadpisem §2.3.4.4. Je právě **8 původních úloh**, žádné nově přidané
číslo. Pozdější doplňky mění odpovědi 4 a 5.

Všechny obrazy `images/p382.png` až `p386.png` a `p586.png` až
`p588.png` byly prohlédnuty. Přesné samostatné statusy hlavního textu
a osmi úloh obsahuje UNIT_STATUS.json.

## Technika a reprodukce

PROOFS.md obsahuje obecný důkaz K, algoritmickou kontrapozici,
strom prefixů, obě konečné sady dlaždic a přechod kvadrant -> rovina;
poté samostatně všechny úlohy 1–8. Nezávisle dokazuje také
kvaziperiodický doplněk odpovědi 4 z roku 2005.

Programový požadavek úlohy 4 plní skutečný úplný generátor
`tiles.py:decide_under_periodicity_assumption`. Úloha nežádá MIX;
v tomto oddílu není žádný požadovaný MIX program. Algoritmus je
správný a totální pouze za výslovným hypotetickým předpokladem zadání.

Pro úlohu 5 máme úplný přepis 92 typů a přesné konečné lokální lemma:
104 výplní 3 x 3 s vynucenými rohy, 12 výplní bez potřebného souseda,
92 makrotypů a všech 16 928 ekvivalencí společných hran. Následuje
obecná konstrukce libovolně velkých čtverců a důkaz, že každá perioda
musí být dělitelná libovolnou mocninou dvou. Tím nejde o pouhý
experiment na konečných polích. Uzavřená substituční podmnožina
86 typů dokazuje doplněk z roku 2019; šest vynechatelných typů je
výslovně určeno. Opravený obrázek 7 x 7 je validní. Doplňkové kontroly
zahrnují 31 x 31 pro všech 92 semen, 255 x 255 pro jedno semeno
a úplný výpis pro W(2,3)=9.

Reprodukce z kořene worktree:

```text
python3 -B workstreams/vol1/parallel/infinity-lemma/check_tiles.py
```

Výsledky jsou v `results/tiles-check.json`, úplné tabulky v
`results/blocks3.json`, `substitution-blocks.json` a `tiles92.json`.
Poslední běh po doplnění exportu úplné tabulky prošel. Konečné
kontroly nenahrazují obecné důkazy v PROOFS.md.

## Errata a kandidát

Prohledány všechny čtyři vrstvy a prohlédnuty jejich původní obrazy.
ERRATA.md rozlišuje **7 různých datovaných známých změn** od
duplicit mezi současnými soubory. Aktuálnost čtyř oficiálních souborů
ověřena ve stejné relaci 1. 11. 2026; otisky jsou uvedeny.

Jediný nový kandidát:
`reports/jeandel-rao-page-range.md` — doplněk z 31. 1. 2023
cituje 1:1–1:39, publikovaný článek má 1:1–1:37. Znění, originály,
primární PDF a prověření všech vrstev jsou samostatné. Report je
připraven k root revizi; pracovník mu nepřiděluje globální ID.
TRIAGE.md vysvětluje odmítnutá podezření a pouhé OCR vady.

## Přesné meze předání

SOURCES.md obsahuje každý primární zdroj, přečtené pasáže a dostupnost.
Primárně potvrzeny mimo jiné König 1927 a 1932, Watsonův chybný krok,
Wang 1965, Robinson 1971, van der Waerden 1927 a 1954, Kruskal 1960
a 1972 a Jeandel–Rao 2021. Německé vzpomínání potvrzuje Schreierovu
atribuci; přesná sazba anglického přetisku 1971 nebyla získána.

Zůstávají tyto **pramenné mezery**, nikoli nezodpovězené vlastní úlohy:

- datum konkrétního sešitu Watsonova článku (1874 proti předsádce 1875);
- úplný Bergerův původní důkaz a přesné srovnání jeho konstrukce;
- celé relevantní kapitoly Grünbaum–Shephard a Gardner a původní
  Penroseova historická konstrukce, dnes nahrazená doplňkem 2023;
- celý Durandův článek (výrok doplňku je však nezávisle dokázán);
- přesná sazba anglického van der Waerdenova přetisku z roku 1971;
- celý článek Dershowitz 1979 (bibliografie potvrzena autorem).

Klasifikace Jeandel–Rao a všechny výsledky Kruskalova přehledu nebyly
nezávisle znovu provedeny; ověřen je citovaný primární výsledek.
Toto předání neoznačuje celý svazek ani všechny bibliografické
odkazy za bezchybné a uzavřené.

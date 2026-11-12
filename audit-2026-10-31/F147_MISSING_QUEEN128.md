# F147 — v obrázku 128 dam chybí poslední dáma

Potvrzeno 3. listopadu 2026 v našich dvou zdrojích. Závažnost: střední.
4B, odpověď 7.2.2.1–236, tištěná strana 477 (PDF 497), pravý dolní obrázek.
Autorův draft Fascicle 5C z roku 2019, strana 181 (PDF 187), má tutéž chybu.

Obrázek má **127 dam**. Poslední řádek je prázdný; nepoužitý sloupec je 65.
Souřadnice zde číslujeme od 1, řádky shora dolů a sloupce zleva doprava.
Oprava je doplnit dámu na **(128, 65)**.

## Krátké ověření

1. V [zvětšeném dolním okraji knihy](images/queen230-236-original-128-bottom.png)
   je vidět prázdný poslední řádek. Totéž ukazuje
   [dolní okraj autorova draftu](images/queen230-236-draft-128-bottom.png).
2. Souřadnice všech 127 vytištěných dam získané z vektorových pozic znaků
   souhlasí mezi oběma zdroji. Zaujímají různé řádky, sloupce a diagonály.
   Ze sloupců 1 až 128 chybí právě 65.
3. Přidání (128, 65) doplní permutaci a nevytvoří útok po žádné diagonále.
   Samostatný [verify_f147.py](verify_f147.py) používá přímo tento seznam;
   nevyhledává řešení ani nepouští optimalizaci.

Výsledek je uložen v [f147-witness.json](results/queen230_236/f147-witness.json).
Nula na konci seznamu `PRINTED` je naše označení prázdného řádku, nikoli znak
vytištěný v knize. Úplné stránky:
[kniha 477](images/queen230-236-original-497.png),
[draft 181](images/queen230-236-draft-187.png).

## Nezávislý zdroj opravy

Fischetti a Salvagnin, *Finding First and Most-Beautiful Queens by Integer
Programming*, arXiv:1907.08246v1, příloha, strana 13, uvádějí všech 128
sloupců. Seznam končí hodnotou 65 a ostatních 127 hodnot se přesně shoduje
s našimi dvěma obrázky. Nejde pouze o jinou symetrickou variantu.
[Původní článek](https://arxiv.org/abs/1907.08246),
[archivovaný obraz tabulky](images/queen230-236-primary-paper13.png).

Kontrola všech obrázků a zdrojové hashe jsou v
[figures-checked.json](results/queen230_236/figures-checked.json).
Po opravě lze také nezávisle překlápět dvanáct uvedených čtverců; všech
4096 takto vzniklých rozmístění je neútočných a zachovává multiset vzdáleností.
To kontroluje uvedenou konstrukci, nikoli globální optimalitu.

## Errata a meze závěru

Šest archivovaných vrstev 4B/Fascicle 5 (úplné seznamy, krátké seznamy a TeX)
bylo prohledáno podle obou stránkování, úlohy i obsahu. Odpovídající oprava
nenalezena; [záznam hledání](results/queen230_236/errata-search.json) uchovává
hashe a návaznost na poslední kontroly aktuálnosti.

Potvrzení platí pro naše PDF a původní autorův PostScript převedený na PDF.
Fyzický výtisk ani celou nejnovější digitální verzi nemáme ověřené. Absence
v prohledaných erratech nedokládá prvenství. Žádné hlášení nebylo odesláno.

# F156 — čtyři číslice neodpovídají prostřednímu kosočtvercovému obrázku

Stav: confirmed, nízká závažnost, knižní text. Sekce 7.2.2.1,
odpověď 262(b), str. 483 (PDF 503), draft str. 187 (PDF 193).
Odkazovaný prostřední obrázek je v zadání na str. 155 (PDF 175),
draft str. 91 (PDF 97). Všechny čtyři celé stránky byly prohlédnuty.
Fyzický výtisk neověřen.

V prvním sloupci tabulky mají být na řádcích 4,5,6,7 (od jedné)
číslice 3,5,5,6 místo 2,4,4,5. Ostatních 60 znaků souhlasí.
Správná tabulka odpovídající skutečně vytištěnému prostřednímu obrázku:

    00012457
    1134569c
    12368abc
    35789bbc
    5578accc
    559aaccc
    669aaccc
    bbbbcccc

Obě tabulky jsou platné reverzní rovinné rozklady. Chyba je pouze
v tvrzené korespondenci s konkrétní ilustrací; počty pokrytí se nemění.

Přesný způsob odečtení: trojúhelníkovou mřížku vyjádříme v bázi
e₁ = (a,0), e₂ = (a/2,b), kde b = √3 a/2. Svislý kosočtverec
spojený s položkou A_ij, 0 ≤ i,j < 8, má levou koncovou souřadnici
své vnitřní vodorovné hrany

    (q,r) = (−4 + j + A_ij, 8 + i − j).

Na daném řádku r řadíme přípustné dvojice (i,j) podle i; rostoucí
q pak určí A_ij = q+4−j. Jde o jednoznačnou projekci sloupců
krychliček, nikoli volbu pořadí přizpůsobenou tabulce.

Nejkratší geometrický svědek: pro řádek 4, sloupec 1 tabulky je
i=3, j=0, r=11. Skutečný svislý kosočtverec má q=−1, tedy A=3.
Vytištěná 2 by potřebovala kosočtverec s q=−2, který na tomto řádku
není. Další tři rozdíly mají (r,q) = (12,1),(13,1),(14,2).

Z obou PDF byly nezávisle přečteny všechny vektorové hrany, všech
256 kosočtverců prostředního obrázku i všech jeho 512 trojúhelníků.
Žádná buňka nechybí ani není pokryta dvakrát. Všech 64 svislých
kosočtverců má počty v řádcích 1,2,…,8,7,…,1. Obě verze obrazu
i vytištěné tabulky se přesně shodují.

Důkazy: `check_zdd261_262_figures.py`,
`results/zdd261_264/reverse-plane-partition.json`, `original-figures.json`,
`draft-figures.json`, `figures-checked.json`. První vývojová projekce
zaměnila i−j za i+j; byla opravena před přijetím kontroly. Nález stojí
na výše uvedené přesné projekci a jednotlivých geometrických svědcích.

Šest vrstev errat včetně historického Fascicle 5 bez odpovídající
opravy: `errata-search.json`, `errata-supplement.json`.

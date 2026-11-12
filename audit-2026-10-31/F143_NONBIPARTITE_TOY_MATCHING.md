# F143: příklad (90) není bipartitní párování

3. listopadu 2026; confirmed, nízká závažnost. Hlavní text §7.2.2.1,
str.104, třetí řádek odstavce *Maintaining a decent focus*. Totéž v
autorském Fascicle 5c, str.40. Fyzický výtisk ani prvenství neověřeny.

Text označuje příklad (90) jako „2DM problem“. Na předchozí straně103
definuje 2DM jako bipartitní párování. Možnosti (90) ale zahrnují

    ‘1 4’, ‘1 5’, ‘4 5’.

Tyto tři hrany tvoří trojúhelník, takže žádné rozdělení položek na dvě
disjunktní množiny nemůže mít v každé možnosti jednu položku z každé
množiny. Je-li1 vlevo, musejí být4 i5 vpravo, což porušuje hranu45.

Přirozená oprava je **X2C problem**, případně obecný matching problem.
Všech13 možností má právě dvě položky. Nesplnitelnost, vytištěný
19uzlový strom a následná formule pro nezávislé kopie jsou správné.

Obě stránky byly zobrazeny:
[kniha104](images/focus202-207-original-124.png),
[draft40](images/focus202-207-draft-46.png).
Nová přesná kontrola čte všech13 možností, ověřuje tři hrany a porovnává
celý strom se zdrojovými uzly a hranami; nejde jen o chybu OCR.
Šest vrstev errat neobsahuje odpovídající opravu:
[záznam kontroly](results/focus202_207/errata-check.json).

[Úplné poznámky a navazující důkazy](FOCUS202_207_SOURCE_NOTES.md).

# C033 — výslovné doplnění symetrie hlav a ocasů

**Kandidát, nízká závažnost; nikoli potvrzená chyba v počtech.**
TAOCP 4B, odpověď 7.2.2.1–138(a), strana 452 / PDF 472.
Zadání a první příklad jsou na straně 140 / PDF 160.

Kniha uvádí 2118 možností, 42 680 sestav a 1056 podstatně různých
řešení. Popisuje posuny, vodorovné/svislé odrazy a přejmenování barev.
Čísla **přesně souhlasí**, pokud dovolíme také globální záměnu všech
hlav s ocasy. Tato dodatečná normalizace není v (a) výslovná.

| Co identifikujeme | Rohová natočení ABcd | Sestav | Tříd |
|---|---:|---:|---:|
| Čtyři barvy, posuny a odrazy; polaritu zachováváme | 4 | 85 360 | 1361 |
| Navíc globálně hlavy ↔ ocasy | 2 | 42 680 | 1056 |

Rychlá ruční kontrola: dolní levý obrázek na straně 452 má podle knihy
24 symetrií. Odraz shora dolů všechny hlavy a ocasy otočí; pro návrat
k originálu je nutné je globálně zaměnit. Se záměnou má skutečně 24
automorfismů, bez ní 12.

Jde o samostatnou operaci. Obrázek ze zadání a jeho globální záměna
hlav/ocasů jsou oba platné. Žádná z 96 prostorových operací s kteroukoli
z 24 permutací čtyř barev je neztotožní; všech 2304 případů je ověřeno.

Celé množiny původního DLX2 a nezávislého geometrického výčtu souhlasí.
Ověřeno je knižní rozdělení automorfismů i všechny původní obrázky.
Samostatný běh s 2118 možnostmi má 42 680 řešení a přibližně knižních
13 G hrubých memů.

Stejné znění má autorův draft z roku 2019. Šest vrstev aktuálně ověřených
errat obsahuje jen starou opravu `96/6=16`, v našem vydání zapracovanou.
Následující odpověď 139(a) globální výměnu hlav a ocasů výslovně připouští.

Otevřené zůstává, zda autor „přejmenováním barev“ myslí všechny párové
štítky Algorithm C. Pak jde pouze o zpřesnění výkladu. Správná knižní
čísla nemáme nahrazovat jinými bez současného upřesnění ekvivalence.

[Podrobnosti](HEADS138_NOTES.md) ·
[Malý certifikát](results/heads138/group-checked.json) ·
[Úplné výsledky](results/heads138/accepted.json).

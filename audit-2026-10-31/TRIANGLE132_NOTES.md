# DLX 132: trojúhelník ze 4 624 různých dílků

Původní zadání na str. 139 a odpověď na str. 450 byly zobrazeny.
Úloha se ptá na sestavení rovnostranného trojúhelníku o straně 68
ze všech cyklických typů trojúhelníků s 24 barvami, při shodě sousedních
hran a jednobarevném obvodu. **Existence je nyní úplně doložena**;
celá odpověď zůstává `partial` kvůli vedlejší diofantické klasifikaci
a dosud nedoloženým podrobnostem historických citací.

## Certifikát existence

[Stránka citovaná v knize](https://www.polyforms.eu/coloredpolygons/triindex.html#trios24)
stále obsahuje původní obrázek řešení. [Nadřazený index](https://www.polyforms.eu/coloredpolygons/index.html)
uvádí autora Petera F. Essera. Archivovaný GIF byl zobrazen a je uložený
nezměněný v `sources/triangles132/trios24.gif`; URL, datum stažení a SHA-256
jsou v souboru `retrieval.json`.

`extract_triangle132.py` z něj získal všech 4 624 dílků. Geometrická
mříž má vrcholy `(13+12r+24c, 18+20r)` v pixelech; ve vzorku 3×3 pixelů
u středu každé výseče má určená barva vždy striktní většinu, nejméně
5 z 9. Uloženy jsou všechny vzorky, nikoli jen vybrané úspěšné části.
Jde o dekódování již publikovaného svědka, ne nové hledání řešení.

Samostatný `check_triangle132.py` nepotřebuje obrázek ani pixelovou
geometrii. Na abstraktní celočíselné trojúhelníkové mříži ověřuje:

- právě jednu barvovou trojici v každé z 4 624 buněk;
- každý z 4 624 cyklických typů právě jednou, včetně obou chiralit;
- všech **6 834 vnitřních hran** se stejnými barvami na obou stranách;
- všech **204 obvodových hran** v jedné barvě;
- každou ze 24 barev v právě 578 výskytech stran dílků.

Certifikát je `results/triangles132/witness.json`, konečný výsledek
`witness-checked.json`. Hlavní otázka úlohy má tedy ověřenou odpověď ano.

## Počet typů a diofantická poznámka

Pro d barev je d jednobarevných typů, d(d−1) typů se dvěma shodnými
hranami a dva cyklické typy pro každou trojici odlišných barev. Celkem

`d + d(d−1) + d(d−1)(d−2)/3 = (d³+2d)/3`.

Totéž plyne z Burnsideova lemmatu pro tři rotace s počty pevných
obarvení d³, d, d. Pro d=24 vychází 4 624=68². Rovnice pro čtvercový
počet dílků je `3m²=d³+2d`. Substituce `X=3d, Y=9m` ji převádí na
eliptickou křivku `Y²=X³+18X`. Zpětně je nutné vyžadovat X>0,
dělitelnost X třemi a Y devíti. Přímé dosazení d=1,2,24 platí;
**tím není dokázáno, že žádné další kladné řešení neexistuje**.

Připravený `sources/triangles132/diophantine132.sage` byl odeslán
veřejné výpočetní službě SageCell, která vrátila HTTP 520 bez výsledku
a bez identifikátoru úlohy. Požadavek a chyba jsou zaznamenané; výpočet
nepovažujeme za provedený a automaticky ho neopakujeme. Stránka veřejné
Magma kalkulačky vrátila HTTP 401 ještě před jakýmkoliv výpočtem.
Pro příští pokračování je vhodný lokální Sage s důkazovým režimem
a úplnou Mordellovou–Weilovou bází, případně jiný úplný diofantický
postup. Při úpravě připraveného skriptu je třeba použít dokumentované
`rank(proof=True)` a `rank_bound()` místo neověřeného `rank_bounds()`
v původním pokusu; jeho přesné bajty zachováváme kvůli hashi požadavku.

[Dokumentace Sage](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html#sage.schemes.elliptic_curves.ell_rational_field.EllipticCurve_rational_field.integral_points)
výslovně váže úplnost `integral_points` na úplnou bázi skupiny. Konečný
scan do libovolné hranice zde není náhradou důkazu.

## Historie a errata

[Dobová zpráva Mathpuzzle z 11. dubna 2002](https://www.mathpuzzle.com/6may2002.htm)
zmiňuje Esserův řešič MacMahonových trojúhelníků. Sama však nedokládá
přesné datum konkrétního 4 624dílkového řešení ani jeho prvenství.
Dosud nemáme originál JRM 9 (1977), str. 209, původní Philpottovo
zadání z roku 1971 ani konkrétní pasáž Smartovy knihy z roku 1998.
Stránka Esserova řešení obsahuje starší neúplnou formulaci diofantického
problému; nepřebíráme ji jako vyvrácení novějšího tvrzení v TAOCP.

Šest vrstev errat bylo prohledáno podle stran včetně posunů do
Fascicle 5, jmen, čísla úlohy a počtu dílků. Tři zásahy se týkají
známé opravy odpovědi 133 na str. 450, čtvrtý typografie odpovědi
MPR 132(a) na str. 393, tedy jiné sekce. Oprava DLX132 nalezena nebyla.
Hashe jsou navázané na kontrolu oficiálních zdrojů 2. listopadu 2026
v 08:06 UTC; viz `errata-check.json` a `source-status.json`.

Nový nález z této kontroly nevznikl. Zbývá doložit nekonečnou
klasifikaci a uvedené historické podrobnosti, nikoli znovu hledat
nebo dekódovat již ověřené řešení skládanky.

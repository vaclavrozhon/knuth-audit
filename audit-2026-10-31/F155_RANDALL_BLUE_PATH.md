# F155 — modrá cesta v Randallově obrázku vynechává diagonálu

Stav: confirmed, nízká závažnost, knižní text. Sekce 7.2.2.1,
odpověď 262(a), str. 483 (PDF 503), draft str. 187 (PDF 193).
Obě celé stránky i zvětšené výřezy byly prohlédnuty; výtisk neověřen.

Každé vodorovné domino má podle legendy obsahovat dvě zkřížené
diagonály, modrou a červenou. Jedno domino má modrou cestu chybně
vedenou podél horní hrany a pak svisle uvnitř pravého políčka.

Pro ruční kontrolu otevři
[výřez knihy](images/zdd261-264-randall-blue-detail.png) a
[výřez draftu](images/zdd261-264-randall-blue-draft-detail.png).
Jde o vodorovné domino u pravé horní části obrázku s modrými cestami.
Souřadnice buněk jsou (12,1), (13,1), počítané od nuly od levého horního
rohu ohraničujícího obdélníku 16 × 24.

V jednotkách buňky vede modrá lomená čára přes body

    (12.5,1) → (13.5,1) → (13.5,4).

Prostřední bod má být (13.5,2). Pak první úsek prochází středem
domina (13,1.5) a kříží správnou červenou diagonálu. Oprava jednoho
ohybu současně zachovává napojení zbytku cesty.

Oba zdroje byly přečteny jako vektory. Mají stejné pokrytí 136 dominy
a 12 modrých + 12 červených cest. Všech zbývajících 135 lokálních
motivů vyhovuje legendě. Samotné dominové pokrytí je správné.
Ze 62 vodorovných domin má správnou modrou diagonálu 61.
Po normalizaci souřadnic a odstranění kolineárních mezibodů se všech
24 barevných cest mezi zdroji přesně shoduje, včetně tohoto ohybu.

Důkazy: `check_zdd261_262_figures.py`, `check_zdd261_265_claims.py`,
`results/zdd261_264/original-figures.json`, `draft-figures.json`,
`randall-repair.json`, `figures-checked.json`, `claims-checked.json`.
Rozdílný offset vloženého Randallova obrázku v draftu je započten.

V šesti vrstvách errat nebyla nalezena odpovídající oprava, viz
`errata-search.json` a `errata-supplement.json` v témže adresáři výsledků.
Tvrzení o autorství Randallovy nepublikované konstrukce tímto nálezem
ani výpočtem nedokazujeme.

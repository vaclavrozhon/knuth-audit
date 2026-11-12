# V3-C0003 — chybějící faktor generující funkce

Confirmed v rychlém prvním průchodu 6. 11. 2026. Odpověď §5.1.2-14,
tištěná 599 / souborová 610, poslední odstavec odpovědi. Sazba zobrazena:
images/multisets-file-610.png. Tvrdí, že generující funkce inverzí při
daných počtech sloupců n_ij je ∏ᵢ nᵢ!_z / ∏ᵢⱼ nᵢⱼ!_z.

Nejmenší protipříklad: multiset {a,b}, a<b, n₁₂=n₂₁=1 a n₁₁=n₂₂=0.
Jediné přípustné dvouřádkové uspořádání má nahoře ab a dole ba. Má
jednu inverzi, takže generující funkce je z. Vytištěný podíl je 1.
Předchozí text ani odkazovaná úloha 16 nezavádí posun počtu inverzí.

Obecná oprava: násobit podíl faktorem z^K, kde

    K = ∑_{i<k, j>l} n_ij n_kl.

Horní řádek dělí permutaci do bloků délek nᵢ. Počet inverzí mezi dvěma
různými bloky je pevně určen maticí n_ij a rovná se K. Uvnitř bloku i
je generující funkce nᵢ!_z / ∏ⱼ nᵢⱼ!_z podle úlohy 16. Násobení dává
uvedenou opravu. Žádná enumerace ani další program nebyly potřeba.

Rozsah chyby je jen chybějící mocninný faktor. K je invariantní vůči
transpozici matice, takže zamýšlená rovnost rozdělení pro n_ij a n_ji
a motivace hledat involuci zůstávají pravdivé.

Prohlédnuty all3-prepre, all3-pre, all3, err3 i historická err3-1e;
výřezy a rozsah hledání: sources/multisets-errata-review.json. Záznam
all3-prepre pro odpověď 14 z 1. 11. 2002 mění závorky na složené
závorky, netýká se tohoto vzorce. Odpovídající oprava nenalezena.
Prvenství nálezu ani fyzický výtisk nejsou ověřeny.

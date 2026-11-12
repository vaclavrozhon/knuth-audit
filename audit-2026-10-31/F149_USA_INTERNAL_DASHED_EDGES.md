# F149 — čárkované hrany uvnitř vyznačených komponent

Potvrzeno v našich dvou zdrojích 3. listopadu 2026. Nízká závažnost:
nesprávný styl čtyř hran, nikoli nesprávné rozdělení států.
4B, hlavní obrázek (116) na straně 116 a odpověď 7.2.2.1–246 na straně 479.
Draft 5C má stejné kresby na stranách 52 a 183.

| Obrázek | Modře čárkovaná hrana | Souvislá černá cesta mezi stejnými konci |
|---|---|---|
| (116), pravý | AL–MS | AL–TN–MS |
| 246, horní levý, exterior | SD–WY | SD–NE–WY |
| 246, dolní levý, interior | SD–WY | SD–NE–WY |
| 246, dolní pravý, interior | IN–KY | IN–IL–KY |

Konce každé vypsané hrany tedy patří do stejné komponenty. Pro zobrazení
indukovaných podgrafů mají být tyto hrany plné a černé. Náprava nemění
žádnou skupinu států ani její populační součet.

Zvlášť snadná kontrola je horní levý obrázek odpovědi 246:
zobrazuje **46 čárkovaných hran**, ale mezi různými skupinami je pouze
**45 hran**, tedy uvedená exterior cena **90**. Hrana SD–WY je zbytečně
zobrazena jako odstraněná; po jejím obnovení kresba souhlasí s cenou.
Všechny čtyři vytištěné ceny 90, 74, 176 a 230 správně popisují samotné
partitiony, když se vnitřní hrany započítají podle původního grafu.

[Zvětšené čtyři obrázky odpovědi](images/usa239-246-answer246-detail.png),
[hlavní obrázek a text](images/usa239-246-main116-text-and-graph.png),
[draft hlavní strany](images/usa239-246-draft-58.png),
[draft odpovědi](images/usa239-246-draft-189.png).
Barvy a konce každé uvedené hrany jsou přímo ověřeny z původních
vektorových tahů obou verzí; [krátký verifier](verify_f148_f149.py)
a [osm zdrojových svědků](results/usa239_246/f148-f149-witness.json).

Nejde o tvrzení, že všechny optimální rozklady byly znovu nalezeny.
Samotné populace a ceny zobrazených rozkladů jsou ověřené; globální
optimalita populačních příkladů je výslovně nereplikovaná.

Odpovídající oprava nebyla nalezena v šesti vrstvách errat;
[záznam hledání](results/usa239_246/errata-search.json).
Fyzický výtisk a prvenství nejsou ověřené.

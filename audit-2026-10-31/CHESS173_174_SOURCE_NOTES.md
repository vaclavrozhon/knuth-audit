# Úlohy 173–174 — úplné obrázky a následné opravy

Kontrola 3. 11. 2026. Původní `CHESS_SUDOKU_NOTES.md` a jeho jedenáct
výsledků zůstávají beze změny. Nová kontrola navazuje na jejich přijaté
SAT a DLX3 výsledky; žádný z těchto jedenácti výčtů se neopakoval.

Čteno zadání na str. 146, odpověď na str. 466 a pokračování 174 na
prvním řádku str. 467; také příslušné řešení v dodatku E, str. 671.
Autorský draft má PDF strany 88, 176, 177 a 259 (tištěné 82, 170,
171 a 253). Použita přímo zobrazená PDF, vektorové čáry a glyfy,
nikoli OCR. Celkem dekódováno **141 výskytů desek / 2 374 figur**
včetně opakování mezi verzemi. To není počet různých hlavolamů.

## Přesný rozsah

- Obě úplné ukázky mají 27 figur, po třech v každém řádku, sloupci
  a boxu, a všechny vytištěné sousedské počty souhlasí. Odečítací
  MCC konstrukce 173(a) je bijekce: pevné figury odečteme z kvót,
  záporná kvóta znamená spor, nulová vyřadí všechny zbývající buňky
  své množiny. Každá ostatní buňka spotřebuje právě příslušné kladné
  kvóty; opačný převod vrátí přesně původní podmínky. Nemohou
  vzniknout položky s nulovou kvótou v některé ponechané možnosti.
- Celá původní galerie má 16 zadání. Opravená galerie z roku 2023
  rovněž 16; společná jsou čtyři. Obě jsou nyní celé ověřené,
  stejně jako čtyři zadání 173(b) a čtyři obrázky 174.
- **27 nových platných zadání** bylo vyřešeno dvěma metodami.
  U každého obě daly jediné stejné řešení a to se přesně shoduje
  s odpovídajícím obrázkem v dodatku. Spolu s 11 přijatými případy
  tedy máme 38 různých platných zadání. Dvacátý osmý nový případ
  je stará chybná ukázka z draftu; oba řešiče prokázaly nesplnitelnost.
- Nové běhy zdědily nice 15, každý měl limit 15 sekund. Všech 56
  skončilo úplně; nejpomalejší trval 0,872 sekundy včetně spuštění
  procesu. Timeout nenastal. SAT přímo kóduje 81 buněk; DLX3 používá
  zbytkové kvóty. Každý vrácený model navíc validuje jednoduchá geometrie.
- Všech 20 původních řešení 173 v dodatku je v bijekci s původními
  4 + 16 zadáními; všech 20 opravených s opravenou sadou. Další
  čtyři řešení 174 jsou přesně staré přijaté modely. Všech 24
  původních řešení se shoduje s autorským draftem.
- 174 má dvě zadání, každé řešitelné jednoznačně oběma typy figur.
  První používá právě jednou každé číslo 0 až 8; druhé deset čtyřek.
  Pokračování na str. 467 potvrzuje právě tento druhý případ.

## Známé opravy

**E085, 12. 10. 2023:** nová Fig. A–3 a příslušných 20 řešení
v dodatku E. Nejde o nový nález. Úspornější zadání nejsou v našem
PDF ani draftu; nově stažená errata je poskytují. Počty nápověd
v pořadí obrázků:

| Řada | Původní | Opravená |
|---|---|---|
| Jezdci, konstanty 1–5 a kombinace 6,8,6 | 7,8,8,8,6,3 | 6,7,7,5,4,3 |
| Střelci, konstanty 1–5 | 7,9,10,5,6 | 4,5,7,5,4 |
| Střelci, konstanty 6–10 | 7,4,8,6,2 | 4,4,3,3,2 |

Erratum připisuje většinu nových zadání F. Stappersovi a uvádí
minimalitu při méně než pěti nápovědách. Tato globální dolní mez
**nebyla nezávisle reprodukována**. Krátké kontroly dokazují platnost
a jednoznačnost uvedených příkladů, nikoli nemožnost všech menších
zadání. Výslovně vynecháváme úplné hledání menších konstantních sad
pro jezdcovou 5 (čtyři nápovědy) a střelcové 1,5,6,7 (čtyři),
8,9 (tři). Jiná široká interpretace závorky o minimalitě zahrnující
i Beluhovovy příklady také není prohlášena za ověřenou. Tvůrčí
173(c) u vyšších počtů zůstává výzvou k hledání lepších příkladů;
původní odpověď sama netvrdí jejich optimalitu. Toto vynechání je
zapsáno samostatně podle uživatelova pokynu o dlouhém brute force.

**E086, 4. 12. 2019:** oprava ukázky (ii) ve Fascicle 5, str. 144.
Draft obsahuje devět nápověd a nemá řešení. Knižní PDF už má správnou
osmici, totožnou s opravným obrázkem. V souřadnicích od jedničky se
čtyřka přesunula z (2,5) na (2,7) a dvojka na (9,2) byla odstraněna.
Následující text správně uvádí osm zadaných a devatenáct doplněných
jezdců. Zbylých sedm obrázků zadání se mezi zdroji shoduje.

## Bibliografie a stav

**F141** je drobná chyba chronologie pod galerií: Nacin obě varianty
publikoval na svém blogu už v květnu a červnu 2018, jezdcová verze
je doložena i v CMJ ze září 2018. Viz `F141_NACIN_CHRONOLOGY.md`.
Nejde o chybu počtů ani o tvrzení našeho prvenství.

Úplné MAA Focus 38(6), str. 36 nebylo získáno; jeho citaci a název
ověřuje autorovo CV, nikoli přímé přečtení této strany. Kvůli této
konkrétní zdrojové mezeře ponecháváme **celou 173 jako partial**;
matematické výsledky jsou zachovány. **174 je reviewed** v rozsahu
celého zadání, odpovědi a všech čtyř dodatečných řešení. Zmínku o
Beluhovově použití SAT vedeme jako autorovo připsání způsobu objevu,
nikoli jako náš přístup k jeho soukromému výpočtu. Celý svazek
ani celá strana dodatku tím dokončeny nejsou.

## Reprodukce a meze extrakce

`extract_chess173_174.py` dekóduje tabulky, nápovědy a figury.
`check_chess173_174.py prepare` páruje všechny dodatkové diagramy,
`run` řeší jen nové případy. Úspěšné běhy neopakovat. Jejich JSON,
vstupy MCC, výstupy obou řešičů a hashe jsou v `results/chess173_174/`.

Při vývoji extraktoru příliš těsná mez 0,01 bodu vynechala poslední
řádek některých zmenšených obrázků v původním dodatku. Diagnostika
zjistila drift glyfů nejvýše přibližně 0,02 buňky; tolerance je nyní
0,06 buňky, přičemž každý původní obraz souhlasí s PS draftem a
všechna řešení splňují přesné kvóty 3/3/3. Před opravou nebyl žádný
takto neúplný diagram přijat jako důkaz. Staré kontrolní programy
nebyly změněny.

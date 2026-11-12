# Dokončení nezávislé fronty DLX 142

3. listopadu 2026 v **05:13:55 UTC** skončil celý nezávislý barevný
výčet, všech deset případů s návratovým kódem 0. Tento záznam doplňuje
časově předchozí [OCTAGONS142_NOTES.md](OCTAGONS142_NOTES.md); jeho
původní důkazy a kontrolní součty zůstávají beze změny.

| Případ | Všechna řešení po přejmenování barev | Shoda nahoře/dole | Shoda vlevo/vpravo | Obě |
|---|---:|---:|---:|---:|
| (i) | 264 093 722 | 387 840 | 21 024 | 192 |
| (ii) | 3 317 206 | 0 | **111 960** | 0 |
| (iii) | 239 198 | 0 | 0 | 0 |

Všechny tři hlavní počty souhlasí s knihou. Vedlejší počty se přesně
shodují s oddělenými výčty s vynucenými okrajovými podmínkami.
**F136** se tak potvrdil také jako podpočet neomezeného případu (ii),
bez přidání periodických identifikací do vstupu.

U hlavních (i)/(ii) bylo uloženo a přímo ověřeno **26 410 / 332 vzorků**,
u (iii) všech **239 198 řešení**. U (i) s horní/dolní shodou všech
**387 840 řešení**; (ii) s touto shodou má nulový úplný výčet. Každý
uložený model prošel kontrolou hran, všech 24 typů a jedinečnosti po
přejmenování barev. Byly ověřeny terminály, vstupy, zdroje, binárka,
kontrolní součty výstupů i pořadová čísla vzorků. Již přijaté dvojí
výčty se znovu neprocházely: jejich platné kontrolní záznamy byly převzaty.

Doklad: [independent-accepted.json](results/octagons142/independent-accepted.json)
a [samostatný přijímací program](accept_octagons142_independent.py).
Nově bylo validováno dalších **653 780 uložených modelů**. To není počet
všech řešení hlavních (i)/(ii): jejich velké výčty mají pouze vzorkový archiv.

Nativní fronta **1157664** dál běží. Celá úloha zůstává **partial**,
protože zbývá druhé nezávislé potvrzení hlavních a ostatních okrajových
počtů a přesné historické náklady 2607/10223/77 Gmems. Proces nezávislé
fronty **1157665** již neexistuje a byl přesunut mezi přijaté dokončené
úlohy. Žádný výčet se nespouštěl znovu.

První integrační kontrola správně zachytila, že tento proces mezitím
skončil; původní neúspěšný log je archivován. Předchozí údaj o dvou
živých frontách popisoval stav před dokončením, nikoli chybu výsledků.

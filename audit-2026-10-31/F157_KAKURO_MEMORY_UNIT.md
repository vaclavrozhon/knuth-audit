# F157 — paměť Algorithm C v tabulce kakuro má chybnou jednotku

Stav: confirmed, nízká závažnost, knižní text. Sekce 7.2.2.1,
odpověď 263(g), str. 484 (PDF 504), draft str. 188 (PDF 194).
V obou vykreslených zdrojích skutečně stojí 509 MB a 537 MB.
Fyzický výtisk neověřen.

Jednotka má být KB. Přesné zaokrouhlené hodnoty 509 KB a 537 KB jsme
nezávisle nereprodukovali. Vytištěné stovky MB však vyvrací horní mez
menší než 1 MB, aniž bychom hledali jediné řešení velkého kakuro 431.

Model z odpovědi 430(d) má v jedné buněčné možnosti pět výskytů
položek. Absorpční možnost má nejvýše devět číslic a jednu barvenou
položku bloku, tedy nejvýše deset výskytů. DLX2 používá 16bytový
uzel, 16bytovou položku a jeden spacer na možnost. Přidáme všechny
hlavičky, rezervu pro sentinel a zásobník délky nejvýše počtu
primárních položek P. Pro O možností a S sekundárních položek stačí
konzervativní horní mez použitých dat

    16 · (11O + 2(P+S+2)) + 4P + 128 bajtů.

| Varianta | P | S | O | Horní mez |
|---|---:|---:|---:|---:|
| unmodified | 1165 | 66 | 4889 | 904708 B |
| modified | 1187 | 66 | 5143 | 950204 B |

Počet řešení ani počet uzlů prohledávání paměť tohoto backtrackingu
nenásobí. Vzorec se týká používaných struktur vykazovaných v tabulce,
nikoli virtuálně rezervovaných maximálních C polí programu.
Proti vytištěným 509/537 MB jde o rozdíl přes dva řády i při této
úmyslně velkorysé horní mezi. Třetí, předzpracovaný řádek s 66 KB
neobsahuje tento jednotkový překlep.

Primární implementační doklad: `sources/knuth-programs/dlx2.w`, výpočet
`bytes` a definice struktur `node`/`item`. Důkazní aritmetika je
`results/zdd261_264/kakuro-memory-bound.json`, přijatá programem
`check_zdd261_265_claims.py`. Počty 18/1 řešení, náklady C/Z a velikosti
ZDD v této tabulce se tímto důkazem neověřují; jsou evidované odděleně.

Šest vrstev errat bylo prohledáno podle stránky, úlohy i čísel a
jednotek: `results/zdd261_264/errata-search.json`, `errata-supplement.json`.
Odpovídající oprava nenalezena. Není to záruka prvenství.

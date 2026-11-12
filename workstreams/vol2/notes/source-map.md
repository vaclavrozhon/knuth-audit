# V2-X0001: zdroje a stránkování

Kontrola 1. listopadu 2026 ve větvi `audit/vol2`.

Náš soubor `books/taocp-vol2-ed3-print1-1997.djvu` má 774 stran souboru.
Tiráž na straně souboru 3 byla zobrazena a udává třetí vydání, první tisk,
září 1997; viz [obrázek](../images/vol2-frontmatter.png).
SHA-256 souboru byl přepočítán a shoduje se s inventářem:
`97f20229e4e06ef20e67ad30c7564dde1943611259a7fe72f2551c900b910cd1`.
Jde o kontrolu skenu, nikoli fyzického exempláře.

Pro arabsky číslovanou část používáme **strana souboru = tištěná strana + 12**.
Přímo přes `djvutxt --page=...` byly ověřeny tyto kotvy:

| Tištěná strana | Strana souboru | Obsah |
|---|---|---|
| 1 | 13 | Začátek kapitoly 3 |
| 2 | 14 | §3.1 |
| 141–144 | 153–156 | Přechod §3.4.1/§3.4.2 |
| 270–273 | 282–285 | §4.3.1 |
| 589–591 | 601–603 | Odpovědi §3.4.1/§3.4.2 |
| 732 | 744 | Příloha B |
| 762 | 774 | Konec rejstříku |

Mapa byla ověřena v těchto kotvách, nikoli vizuálně na každé ze 774 stran.
Pozor: `text/vol2.txt` vynechává ilustrovanou stranu souboru 12 (číslice 1–9; viz revize 6.11.2026). Pořadí bloků
oddělených znakem form feed v tomto souboru proto není pořadí stran DjVu.
Počáteční chybné pojmenování obrázků podle pořadí OCR bloků bylo opraveno;
uložené obrázky nyní odpovídají tabulce výše a jejich tištěným záhlavím.

## Vrstvy errat

| Zdroj | Výchozí stav / období | Způsob použití |
|---|---|---|
| `all2-prepre.ps.gz` | Od prvního tisku 1997 do přechodu na tisk 26 (2011) | Nutný pro náš sken |
| `all2-pre.ps.gz` | Tisk 26 (2011) až tisk 45 (2022) | Navazuje na nejstarší vrstvu |
| `all2.ps.gz` | Od tisku 45 (2022), dlouhé znění | Aktuální změny včetně drobností |
| `err2.ps.gz` | Stejné současné období, krátké znění | Kontrola shody relevantních oprav |
| `err2.textxt` | Současný TeX zdroj | Jednoznačné čtení indexů a vzorců |

Všech pět originálů bylo znovu staženo z
[oficiálního webu](https://www-cs-faculty.stanford.edu/~knuth/taocp.html).
Bajtově se shodují s archivem z 31. října 2026; původ a přesné časy jsou v
[manifestu](../sources/manifest-2026-11-01.json). Aktuální seznam udává
poslední aktualizaci 9. června 2026; HTTP Last-Modified současných souborů
je 10. června 2026 UTC. Druhé vydání není zdrojem oprav třetího vydání.

Pro tento blok byly prohledány všechny tři dlouhé vrstvy, krátká errata
a aktuální TeX podle lokalit `142–147`, `270–273`, `590–592`, názvů algoritmů,
věty B a symbolů. Významné zásahy:

- 23. 1. 1998, str. 272: normalizace `floor((b-1)/v_{n-1})` se nahrazuje
  `floor(b/(v_{n-1}+1))`; reprodukce je ve [zprávě o dělení](division.md).
- 3. 2. 2005, D3 na str. 272: test `h=b` se mění na `h>=b`.
- 14. 5. 2026, str. 271–272: odhad již není omezen hodnotou `b-1`, věta B
  má mez chyby 3 a D3 zvlášť ošetřuje `h=b+2` při lichém základu.
  V této nové větě jsme potvrdili [chybu indexu](C0001-theorem-b-index.md).
- U samotných algoritmů S/R a vzorců odpovědí §3.4.2-5, 6, 7, 9, 11
  nebyla nalezena relevantní oprava. Odpověď 8 opravy má: 29. 6. 1999
  změna aktualizace `N` na `N-X-1`; 17. 9. 2011 závorky ve vzorci.
  Odpověď 8 proto nepovažujeme za nový nález ani za kompletně prověřenou.

Absence nalezené položky není zárukou, že chyba nebyla někomu známa nebo
že již není nahlášena neveřejně.

## Náhled digitálního vydání z července 2026

Pro cílenou kontrolu §3.2.2 byl 1.11.2026 stažen distribuční
[náhled Pageplace](https://api.pageplace.de/preview/DT0400.9780133488791_A23586210/preview-9780133488791_A23586210.pdf),
79 stran PDF, [metadata a SHA-256](../sources/publisher-preview-9780133488791.json).
Vizuálně přečtená [tiráž na straně souboru 6](../images/publisher-preview-copyright.png)
uvádí „Eighth digital release, July 2026“. Jde o doložený digitální
náhled, nikoli fyzický výtisk; původní DjVu zůstává hlavním zdrojem
úplného průchodu. Data v metadatech PDF nepoužíváme jako datum vydání.

Strana souboru = tištěná strana +16 pro ověřené kotvy 37,39,40
(tedy 53,55,56). Vizuální kontrola potvrdila přetrvávání C0009 na
[str.37](../images/publisher-preview-p037.png) i
[39](../images/publisher-preview-p039.png), C0010 na str.39 a C0008
v přidané úloze 38 na [str.40](../images/publisher-preview-p040.png).
Ostatní strany tohoto PDF tím nejsou prohlášeny za zkontrolované.

## Reprodukce obrázků

Například pro tištěnou stranu 272:

```sh
ddjvu -format=ppm -page=284 -scale=140 books/taocp-vol2-ed3-print1-1997.djvu page.ppm
```

PPM byl pomocí Pillow beze změn obsahu převeden do PNG. Pro dlouhá errata:

```sh
pdftoppm -f 6 -singlefile -scale-to 1800 -png errata/pdf/all2.pdf page
```

Lokální PDF jsou odvozené ze shodných originálů, které byly nově staženy.
Poppler při vykreslování errat vypisuje varování o obrysech písem Type 3;
rozhodující indexy jsou čitelné a shodují se s nezkompilovaným TeX zdrojem.

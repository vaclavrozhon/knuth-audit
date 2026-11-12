# Kakuro: úplný výčet malých diagramů

Rozsah: úloha 7.2.2.1–432, str. 181 a 543–544; kódování odpovědi 430(d).

## F062: neřešitelný zápis údajně nejtěžšího puzzle

Na str. 544 je uvedeno `6 19 6 / 8 11 10`. Řádkové součty dávají 31,
ale sloupcové jen 29. Každá buňka patří právě do jednoho řádku i sloupce,
takže tento puzzle nemá žádné řešení. Stejný zápis je v autorově
PostScriptu `fasc5c`, str. 248 (vydaný Fascicle 5 str. 352).

Oprava je **11 → 13**, tedy `6 19 6 / 8 13 10`. Jediné řešení je

```
5 1 .
3 7 9
. 5 1
```

Úplný nezávislý výčet všech 1 432 872 přípustných vyplnění potvrzuje
jednoznačnost. Navíc doslovné kódování 430(d), spuštěné nezměněným
Knuthovým DLX2, dává právě **79 uzlů**, jak kniha uvádí. Původní
chybný zápis má 0 řešení a 36 uzlů. Jiná jednopoložková oprava
`6 19 4 / 8 11 10` je také jednoznačná, ale má magic block a 30 uzlů;
nesouhlasí tedy s popsanými vlastnostmi. V `all4b` ani historickém
`all4f5` není odpovídající oprava.

## Počty a symetrie bez rozporu

`kakuro_enum.cpp` vyplňuje buňky přímo, s bitovými maskami zakázaných
číslic v řádcích a sloupcích. Seskupuje podle pěti součtů; šestý je
určen jejich celkovou sumou. Oddělený výčet restricted growth strings
slouží k nezávislé kontrole polynomu podle velikosti abecedy.

| Diagram | Všech vyplnění | Různých posloupností součtů | Jednoznačných | Tříd |
|---|---:|---:|---:|---:|
| (a), sedm buněk | 1432872 | 356215 | 78690 | 9932 |
| (b), celý 3×3 | 43038576 | 1077469 | 6840 | 49 |

Koeficienty RGS přesně souhlasí: (5,28,33,11,1) pro 3,...,7 symbolů
a (2,42,186,234,105,18,1) pro 3,...,9. Vyhodnocení v padajících
faktoriálech při abecedě velikosti 9 dává nezávisle obě celkové sumy.
Pythonový výčet permutací jednotlivých řádků potvrzuje celé seznamy
jednoznačných puzzle pro abecedy velikosti 3 a 4, u obou diagramů.

Pro (a) grupa transpozice, půlotáčky a doplňku číslic d→10−d dává
orbity velikosti 2:1, 4:190, 8:9741. Čísla knihy i jediný speciální
příklad `6 15 14 / 14 15 6` souhlasí. Pro (b) přibývají libovolné
permutace řádků a sloupců; jsou tři orbity velikosti 72 a 46 velikosti
144. Všechny tři uvedené symetrické příklady souhlasí. U všech 49 tříd
je skutečně vynucený průsečík 7 proti 20, nebo jeho duál 23 proti 10.

## C012: dosud nevyjasněný význam a počet forced moves

Statistiky 4011 a 570 ani popis dvou nejsnazších puzzle zatím nelze
reprodukovat pomocí dvou přesně definovaných lokálních testů:

- Průnik sjednocení všech dovolených číslic řádkového a sloupcového
  bloku je jednoprvkový: bez takové buňky je 3360 asymetrických tříd,
  z nich 576 nemá magic block. Pět tříd má čtyři takové buňky.
- Jednoprvkové primární položky přímo v XCC kódování 430(d): bez
  vynucené možnosti je 2750 asymetrických tříd, z nich 470 nemá
  magic block. Tady se mohou vynutit i absorpční možnosti.

Kniha pojem forced move v tomto odstavci blíže neurčuje. Proto tyto
rozdíly **nepočítáme jako potvrzené chyby**. Jsou oddělené od F062,
jehož nemožnost plyne jen ze součtu všech buněk. Skript uchovává oba
výklady, nikoli jedinou domnělou definici autora.

## Původní program a reprodukovatelnost

Zdroj [DLX2](https://www-cs-faculty.stanford.edu/~knuth/programs/dlx2.w)
a potřebný `gb_flip.w` z [oficiálního GraphBase archivu](https://cs.stanford.edu/pub/sgb/sgb.tar.gz)
jsou archivované v `sources/knuth-programs` s SHA-256 a časem stažení.
Překlad: `ctangle`, pak `gcc -O3 -std=gnu90`; zdroje nebyly upravovány.
Číslování kombinací odpovídá rostoucím bitmapám z odpovědi 430(b).

`check_kakuro_xcc.py` ukládá přesné vstupy a oba výstupní proudy.
Vedle opravy F062 reprodukuje i **488 uzlů** uvedeného 4×4 příkladu
`11 15 23 29 / 12 15 23 28`, s jedním řešením. Údaj o celkovém počtu
pěti tříd 4×4 zatím nezávisle neověřujeme.

Starý C program nemá explicitní návratovou hodnotu main, proto má při
překladu pro toto prostředí nenulové návratové kódy i po normálním
vypsání úplných výsledků. Nepoužíváme je jako indikátor správnosti;
kontrolujeme závěrečné počty a neporušené výstupy.

## Úplná kontrola vyhledávacích stromů

Původní DLX2 byl následně spuštěn nad **všemi 9932 + 49 reprezentanty**.
Každý měl právě jedno řešení, v souladu s nezávislým úplným výčtem.
Mezi všemi 1068 asymetrickými třídami typu (a) bez magic blocku má
jediné maximum 79 uzlů právě opravený příklad `6 19 6 / 8 13 10`.
To ověřuje tvrzení o nejtěžším příkladu i na širší množině, aniž by bylo
nutné rozhodnout význam nevyjasněné podmnožiny 570.

Napříč všemi třídami (a) je maximum 89 uzlů u `3 14 15 / 6 14 12`,
které má magic block a neleží v podmnožině diskutované knihou; není to
rozpor s knihou. Pro (b) je maximum 87. Archiv:
`dlx-sweep.models.jsonl`, `dlx-sweep-summary.json`. Celý dodatečný běh
trval přibližně 21 sekund. C012 zůstává pouze otázkou lokálních statistik.

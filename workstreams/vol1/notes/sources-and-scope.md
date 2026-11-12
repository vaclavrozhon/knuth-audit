# Podklady a rozsah první kontroly svazku 1

Datum: 1. listopadu 2026. Položka V1-X0001.
Pracoviště `.-worktrees/vol1`, větev `audit/vol1`.

## Identita knihy

Inventář a vizuálně přečtená [tiráž](../images/vol1-file003-copyright.png)
souhlasí: *Fundamental Algorithms*, třetí vydání, první dotisk z května 1997,
ISBN 0-201-89683-4. Soubor je `books/taocp-vol1-ed3-print1-1997.djvu`.
Jeho SHA-256 byl znovu vypočten a souhlasí s inventářem:

```text
e2c5ee120bad91e33f617614b846849c4801115b2e7aa820f56fc5ffb9bbebb9
```

Tištěný exemplář nebyl ověřen. Výsledky se vztahují k místnímu skenu a
uvedeným erratům; nejsou potvrzením nejnovějšího dotisku, prvenství ani odměny.

## Stránkování

Pro použité arabsky číslované strany platí `strana souboru = tištěná strana + 15`:

| Tištěná strana | Strana DjVu | Použití |
|---|---|---|
| bez čísla | 3 | tiráž |
| 43–44 | 58–59 | zadání §1.2.4-37–38, kontrola přepisu §1.2.4-40 |
| 176–178 | 191–193 | algoritmy I a J |
| 242–243 | 257–258 | zadání §2.2.1-3–5 |
| 478 | 493 | odpovědi §1.2.4-37–38 |
| 523 | 538 | odpovědi §1.3.3-13–14 |
| 536–538 | 551–553 | odpovědi §2.2.1-3–5 |

Čísla byla porovnána s hlavičkami zdrojových stran, nikoli odhadnuta
z názvů Markdown souborů. Toto je mapa použitých stran, ne audit
integrity všech 665 stran. Extrakce textu má navíc závěrečný prázdný
oddíl po posledním oddělovači; není to další stránka knihy.

## Vrstvy errat a nová kontrola aktuálnosti

Oficiální [rozcestník TAOCP](https://www-cs-faculty.stanford.edu/~knuth/taocp.html)
byl otevřen 1. listopadu 2026. Přímo z autorova serveru byly znovu staženy
následující soubory do vlastního `sources/`; jejich obsahové hashe ve všech
případech souhlasí se společným archivem z 31. října 2026.

| Soubor | Úloha při kontrole |
|---|---|
| `all1-prepre.ps.gz` | historické opravy od vydání v roce 1997 |
| `all1-pre.ps.gz` | další vrstva, podle úvodu 2011 až vydání dotisku 2022 |
| `all1.ps.gz` | úplná řada změn po roce 2021, včetně drobných úprav |
| `err1.ps.gz` | kratší aktuální výběr; není další časovou vrstvou |
| `err1.textxt` | aktuální TeX pro kontrolu znamének a indexů v erratech |

URL, časy získání a SHA-256 jsou v
[manifestu nového stažení](../sources/errata-refresh-2026-11-01.json).
Protože jsou originály totožné, bylo možné použít existující odvozená PDF
a texty v `errata/pdf/` a `errata/text/`. Důležité matematické položky byly
navíc přečteny z vykreslených PDF errat; textová extrakce z nich ztrácí
například minus ve výrazu „line -4“ i v matematických formulích.

## Reprodukce

Z kořene worktree:

```sh
python3 workstreams/vol1/check_first_blocks.py
python3 scripts/volume_ledger.py vol1 --check
```

První příkaz znovu provede konečné matematické kontroly a přepíše
`workstreams/vol1/results/first-blocks.json`. Druhý ověří strukturu ledgeru
a existenci jeho dokladů. Úspěšný matematický běh není nutné opakovat,
pokud se nezmění kontrolované formule, implementace nebo rozsah.

Obrazy DjVu vznikly `ddjvu -format=tiff -page=K -scale=150` a převodem
jedné výsledné stránky do PNG pomocí Pillow. K je zde pořadí strany souboru
z tabulky, nikoli tištěné číslo. Obrazy PDF errat byly vykresleny programem
`pdftoppm` z lokálních odvozených PDF. Originály se neměnily.

## Co se počítá jako výsledek

Tři matematické bloky mají obecné důkazy a konečné kontroly; samostatný
čtvrtý záznam `checked` je tato kontrola podkladů. Šest záznamů
`known_erratum` jsou již zveřejněné opravy nebo doplnění podmínky.
Jeden záznam `dismissed` zachycuje vadný přepis místo chyby v knize.
Nové potvrzené nálezy: **0**. Otevření kandidáti: **0**.

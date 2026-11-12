# Prameny a rozsah jejich ověření

## Kniha a křížové odkazy

Primární zdroj: *The Art of Computer Programming*, Volume 1, third edition,
first printing (1997), lokální DjVu `books/taocp-vol1-ed3-print1-1997.djvu`.
Všechny obrazy hlavního textu 280–298 a odpovědí 553–556 byly prohlédnuty.
Přepis OCR sloužil k vyhledávání, rozhodující jsou obrazy v `images/`.
Kniha na s. 283 sama neprohlašuje pravidla za jistou úplnou fyzickou
specifikaci výtahu; zůstává historickým svědectvím autora o jeho pokusech.

Křížový odkaz z odpovědi 12 na prioritní fronty: Volume 3, second edition,
first printing (1998), §5.2.3, tištěná s. 149. Obraz je
`images/volume3-page149.png`; potvrzuje explicitní vazbu na tento výtah
a O(log n) vkládání/odstraňování v haldě. Pro libovolné rušení události
je v našem důkazu navíc popsána mapa uzel→pozice. Celá §5.2.3 zde
auditována nebyla. Dřívější vlastní profilovací práce je ve zmrazené
`parallel/interpretive/` a v této složce se nepřepisuje.

## Citovaný článek

Donald E. Knuth, *An Empirical Study of FORTRAN Programs*, Software—Practice
and Experience 1(2) (1971), 105–133, DOI 10.1002/spe.4380010203.

* [Primární článek, kopie na Tufts](https://www.cs.tufts.edu/~nr/cs257/archive/don-knuth/empirical-fortran.pdf)
  je uložen v `sources/knuth-empirical-fortran-1971.pdf`. Prohlédnuty byly
  originální s. 105–107, uložené jako `images/fortran-01.png` až `03.png`.
  Textová extrakce PDF je prázdná: soubor obsahuje obrazy; její prázdnota
  nebyla zaměněna za chybějící obsah. Úvod definuje profil a vysvětluje
  dynamická měření. Popis sběru začíná koši, ale zahrnuje i další postupy.
* [Primární bibliografický záznam Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1002/spe.4380010203)
  potvrzuje svazek, číslo, stránky a vydání April/June 1971. Záznam byl
  dostupný ve vyhledávacím výstupu; přímé otevření DOI stránky vrátilo
  HTTP 403. Samotný článek je dostupný výše a nese původní tiráž.

Tento rozsah potvrzuje relevanci a bibliografii citace na s. 296; není
novou reanalýzou všech statistických výsledků článku. Autorův konkrétní
vstup 26 uživatelů pro profil výtahu článek nenahrazuje. Dva fragmenty
tabulky 1 nedeterminují jeho celý vstup; historické frekvence zůstávají
bez nezávislé reprodukce.

## Všechny čtyři vrstvy errat

Živé soubory na autorově webu byly znovu staženy 2026-11-01 v
19:39:46–19:39:50 UTC a jejich SHA-256 se ve všech případech shoduje
s uloženými `errata/originals/`. Aktuální `all1` a `err1` uvádějí poslední
změnu 2026-05-31. Přesné URL, časy, hashe a HTTP Last-Modified jsou
v `sources/live-errata.json`.

* [all1-prepre](https://www-cs-faculty.stanford.edu/~knuth/all1-prepre.ps.gz):
  původní PDF s. 20, 21, 41; obrazy prohlédnuty.
* [all1-pre](https://www-cs-faculty.stanford.edu/~knuth/all1-pre.ps.gz):
  PDF s. 12; obraz prohlédnut.
* [all1](https://www-cs-faculty.stanford.edu/~knuth/all1.ps.gz):
  PDF s. 9, 15; obrazy prohlédnuty.
* [err1](https://www-cs-faculty.stanford.edu/~knuth/err1.ps.gz):
  tytéž současné věcné změny ověřeny v textu, PDF s. 8 a 13 uloženo;
  duplicitní změny se nepočítají podruhé.

Přesný soupis 22 různých záznamů vztahujících se k této sekci je
v `ERRATA.md`. Opravy na s. 556 odpověď 5 už patří §2.2.6 a nejsou
připočteny. Žádná známá změna není vydávána za nový nález.

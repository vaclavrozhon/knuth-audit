# Skutečný čtecí rozsah a závislosti

Tento blok byl prověřen 2. listopadu 2026. Primární errata jsou
lokální soubory získané z autorova webu; jejich přesná URL, datum
stažení a hash zachovává `errata/manifest.json`. Kniha svazku 1
je třetí vydání, první tisk 1997. Novější vydavatelský náhled
a knihy dalších svazků se výslovně odlišují.

## Přímá obrazová četba indexových řádků

Celé indexové části těchto osmi původních obrazů byly přímo
zobrazeny a přečteny, včetně vstupních poznámek o neuvedených
delecích:

| Soubor PDF | Strany PDF | Sémantické řádky |
|---|---|---:|
| errata/pdf/all1-prepre.pdf | 48, 49, 50 | 69 + 96 + 67 |
| errata/pdf/all1-pre.pdf | 19, 20 | 64 + 45 |
| errata/pdf/all1.pdf | 16 | 47 |
| errata/pdf/err1.pdf | 14, 15 | 17 + 30 |

Obrazy jsou převzaty beze změn z `parallel/errata-additions/images/`.
Záhlaví jako Representation (inside computer) pouze vymezuje dvě
podhesla; samo bez změněného obsahu není novým sémantickým řádkem.
Úplná cizojazyčná podoba osobních jmen zůstává v obrazu. Normalizovaný
štítek záznamu není diplomatický přepis všech použitých písem.

Čtyři agregáty `all1-prepre:609`, `all1-pre:187`, `all1:190`
a `err1:163` byly převzaty z dokončeného inventáře errata-additions.
Převzetí tohoto inventáře není tvrzením o druhém úplném obrazovém
čtení všech jeho 101 stran.

## Přímé obrazy cílových a rozhodujících pasáží

U svazku 1 byly v tomto bloku přímo zobrazeny:

- Tiráž, fyzický obraz 3, odvozená římská iv: celý obraz, zejména
  označení ochranné známky TeX a webové adresy.
- 105: poznámka k úloze 1.2.10-13 s P. Lévym a continuity theorem.
- 363: celý obraz, grafy, walk/path/cycle a volné stromy; dále
  přímo terminologický doplněk na all1-prepre PDF 24.
- 377 a 388: celé obrazy, cíle obou nových Čebyševových odkazů.
  Dále doplňky k 377 na all1-prepre PDF 26 a k 388 na all1 PDF 10;
  jejich čtení bylo omezeno na příslušné opravné odstavce.
- 592: celý obraz, začátek odpovědi 31 a věta pokračující
  Hipparchovým jménem na 593. Kontext pokračování byl čten textově.
- All1-pre PDF 14: konkrétní dovětek k odpovědi 31 na 472,
  pojmenování Chebyshev's monotonic inequality a bibliografie.

Obrazy mají konkrétní cesty v jednotlivých záznamech, poznámkách
obou kandidátů a `INPUTS.json`. Původní indexové protějšky jsou
převzaty z dříve dokončeného obsahového auditu; zde netvrdíme
druhý přímý obrazový průchod původním indexem 628–650.

Ve svazku 2 byly přímo zobrazeny tištěné 362 a 363. Rozhodující
četba je odstavec o Lévyho zpřesnění Gaussova–Kuzminova odhadu
a jeho kontext na 363, DjVu filepage 375. Předchozí 362 zůstává
uložena se správným názvem. Na all2-pre PDF 19 bylo přímo přečteno
záhlaví a totožný Lévyho indexový řádek. Nejde o nový důkaz
Lévyho výsledku ani o četbu jeho článku.

Ve svazku 4B byly přímo přečteny příslušné odstavce s okolím:
MPR odpověď 48 na 377, PDF 397, a poznámka odpovědi 113 na 388,
PDF 408. Dostupná kniha je první vydání, druhý tisk 2022.
Na all4b PDF 24 bylo přímo čteno záhlaví a Čebyševův indexový
řádek. Nejde o audit celých stran dalších svazků ani citovaných
Čebyševových originálů.

## Textová navigace, primární web a novější sazba

Konkrétní pasáže `text/vol1.txt` a jednotlivé textové opravy
uvedené v `text_amendment_ids` byly čteny pro věcnou shodu cílů.
Převzaté starší záznamy mají explicitní `review_path`. Nevzniká
zde nové ověření všech větných důkazů, programů, autorství a
historických tvrzení, na které tyto stránky odkazují.

Všechny čtyři vrstvy byly prohledány jak podle stran, tak podle
jmen u obou kandidátů. Výsledky jsou v jejich dvou souborech
`results/*-errata-search.json`. U Čebyševa byl navíc čten přesný
řádek zdrojového `errata/originals/err1.textxt`. Nesouvisející
errata nalezená hledáním se nepovažují za nově obsahově ověřená.

Novější Pageplace PDF: přímé celé obrazy PDF 13 (xi), 22 (xx)
a 31 (9); textová četba segmentů PDF 1–4, 18 a 19. Přesné
provenienční meze a původní URL jsou v `notes/later-preview.md`.
Původní i, xv–xvii a xx tím nebyly získány. Pozdější plné strany
53–54, 582 a 629–650 v tomto náhledu nejsou.

OEIS: primární homepage a Welcome, čtené části názvu, účelu,
Referencing the OEIS a URLs. Ověřují institucionální definici
a adresu, nikoli právní registraci značek. Datum, URL a uložený
webový výstup jsou v `notes/oeis.md` a `sources/oeis-web-read.txt`.
Jiné životopisy se v tomto bloku nově neprohlašují za primárně
prověřené.

`INPUTS.json` je seznam konkrétních souborových závislostí,
nikoli seznam publikací přečtených v celém rozsahu. Závislost
na hlavním původním auditu, jeho čtyřech zmrazených dávkách
a inventáři errat je výslovná. Případné pozdější změny těchto
sdílených souborů se zjistí podle zachycených hashů; nelze
je tiše zaměnit za vstupy tohoto předání.

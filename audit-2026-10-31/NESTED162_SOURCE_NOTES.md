# DLX162: původní obrázky, opravy a Ahrensův pramen

Kontrola 3. listopadu 2026. Zadání str. 145, odpověď str. 462;
autorský draft str. 81 a 166. Ve všech čtyřech obrázcích každé verze
bylo přímo dekódováno všech 83 dam a 13 obarvených čtverců.
Rozmístění i barvy v PDF a draftu souhlasí. Všechny tři vytištěné
odpovědi jsou přímo v dříve přijatých archivech řešení.

## Matematické výsledky zůstávají přijaté

| Část | Požadavek | Nejmenší n | Úplný počet fyzických poloh |
|---|---|---:|---:|
| a | dvě Q4 | 15 | 224 |
| b | tři Q4 | 17 | 32 |
| c | čtyři Q4 | 17 | 32 |
| d | pět Q4 | 22 | 256 |
| e | dvě Q5 | 16 | 144 |
| f | tři Q5 | 19 | 64 |
| g | čtyři Q5 | 20 | 288 |
| h | dvě Q6 | 22 | 896 |
| i | tři Q6 | 25 | 3392 |

Žádný z těchto výčtů se neopakoval. Starých 51 případů vyčerpává
všechny rozměry od kt do minima. Negativní případy jsou dokončené
oběma metodami. U pozitivních d a i má původní DLX3 jen prvního svědka;
celkové počty pocházejí z úplného nezávislého geometrického výčtu.
Neoznačujeme je za dva úplné pozitivní výčty. Dřívější oprava parseru
je zachovaná a nové zdrojové obrázky souhlasí s jeho finálními výsledky.

Proč stačí začít u n=kt: dva bloky stejného druhu Qk v nezávislém
rozmístění nesmějí mít překryv řádkových ani sloupcových intervalů.
Překryv bez společné dámy by znamenal dvě dámy v jednom řádku nebo
sloupci. Překryv se společnou dámou vylučuje dříve přijatá úplná konečná
kontrola všech 2, 10 a 4 vzorů Q4, Q5 a Q6 a všech jejich překryvných
posunů. Při totožném čtverci se různé vzory také nemohou sloučit;
totožný vzor na totožném místě je pouze jeden blok. Proto n musí být
alespoň kt a zbývající mezery do minima pokrývají staré negativní běhy.

MCC přidá k obvyklé možnosti jedné dámy možnost celého bloku: sjednocení
jeho řádkových, sloupcových a diagonálních položek spolu s novou primární
položkou # násobnosti t. Přesné pokrytí řádků a sloupců a sekundární
diagonály vynutí nezávislost. Každá platná poloha s alespoň t bloky
se získá výběrem t těchto bloků a jednotlivých zbývajících dam. Stejná
poloha může vzniknout více výběry bloků; počty výběrů a poloh se rozlišují.

Dodatečné tvrzení v (a) je doloženo svědkem z již hotového archivu Q15:
obsahuje disjunktní Q4 i Q5. U (b,c) je přímo ověřena citovaná Ahrensova
větrníková Q17: čtyři bloky Q4 a dáma uprostřed, invariantní při otočení
o 90 stupňů. Souřadnice a odkazy na řádky starých archivů jsou
v souborech `source-checked.json` a `claims-checked.json`.

## Tři známé opravy, nikoli nové nálezy

- **E080, 4. 11. 2023:** Zadání upřesňuje „eight of the possible“ na
  „eight of the ten possible“. Všech deset Q5 je ve starém katalogu;
  právě osm obsahuje Q4. Naše PDF ani draft doplnění nemají.
- **E081, 13. 10. 2023:** Druhá dáma bloku leží na (j+1,k+3), proto
  má diagonály a_(j+k+4), b_(j-k-2). Vytištěné a_(j+k+3), b_(j-k-3)
  jsou špatně v obou zdrojích. Ostatní tři dvojice diagonál souhlasí.
- **E082, 13. 10. 2023:** Autor doplňuje sharp preference, snižuje
  náklady 1,2 Tμ na 150 Mμ, 35 Gμ na méně než 200 Mμ a 6 Tμ na
  180 Mμ. Současně má být obarvená také Q5 v největším obrázku.
  Přímá kontrola ji našla na řádcích 0–4 a sloupcích 6–10; v našem
  PDF i draftu skutečně není obarvená. Všechny tři Q6 obarvené jsou.

Historické náklady, původní i opravené, znovu nereprodukuji. Totéž
platí pro údaj 2 Mμ v (g). Je to výslovná výjimka podle pokynu uživatele,
nikoli mezera v důkazu minim. Dřívější matematické běhy už používaly
správné diagonály a původní sharp change file.

**F069 zůstává beze změny.** Počty tříd v (e,h) jsou 19 a 116 místo
4 a 28. I při širším sloučení shodných množin položek vychází 5 a 30.
Pět uložených neekvivalentních příkladů pro (e) nadále poskytuje malý
protipříklad. U (g) je vytištěných 18 platné pro sloučené MCC možnosti,
které se rozvinou do 288 fyzických poloh. Neoznačujeme to za další chybu.
V šesti vrstvách errat není oprava F069; nejde o tvrzení o prvenství.

## Citovaný Ahrens a doplnění odpovědi161

Odpověď161 má ještě poslední bibliografický odstavec na začátku strany462.
Předchozí kontrola159–161 ho přehlédla. Tento následný záznam doplňuje
jeho kontrolu; přijatá matematika a programy zůstaly beze změny.

Získán [veřejný sken Ahrensovy knihy](https://archive.org/download/mathematischeun01ahregoog/mathematischeun01ahregoog.pdf).
**Je to třetí, anastaticky tištěné vydání z roku1921**, jak dokládá
titulní stránka; pole `date:1910` v metadatech Internet Archive je
zavádějící. [Knihovní katalog SLUB](https://katalog.slub-dresden.de/id/0-1112711597)
dokládá původní druhé vydání prvního svazku z roku1910. Autorova předmluva
z roku1921 vysvětluje reprodukci předchozího vydání s menšími opravami.
Přesný exemplář1910 jsme nezískali a netvrdíme totožnost obou vydání.

V dostupném autorském vydání je citovaná kapitola X skutečně přehledem
dominujících dam: začíná na str.285, následující strana rozebírá
historické zdroje a variantu s neútočícími dámami. Byly zobrazeny obsah,
úvod kapitoly a následující strana. Subjektivní označení „excellent“ není
samostatné matematické tvrzení. Obsahový odkaz161 je tím doložený,
s výslovným omezením dostupného vydání.

Citace162(b,c) na str.258 také odpovídá: obrázek24 ukazuje Q17 s dámou
v centru a čtyřmi Q4. Jeho 17 souřadnic bylo ručně odečteno ze skenu,
ověřeno geometricky a nalezeno v našem starším úplném archivu.
Jde o doložení obsahu odkazu pomocí autorova pozdějšího vydání,
nikoli o nově prokázané datování prvního výskytu tohoto obrázku.

## Rozsah uzavření

Celá162 je **reviewed** s dřívějším F069, známými E080–E082 a výslovně
nereplikovanými náklady. Odpověď161 je doplněna o skutečné pokračování
a popsanou pramennou oporu; její dřívější uzavření tím získává chybějící
rozsah. Strany145 a462 jsou nadále částečné kvůli ostatním úlohám.
Naše PDF i draft jsou ověřené, fyzický výtisk TAOCP stále ne.

Další blok:163–170. Odpovědi budou vždy čteny až k následujícímu číslu,
včetně případného pokračování přes stránku.

- [Původní obrázky a archivní svědci](results/nested162/source-checked.json)
- [Krátké kontroly tvrzení a Ahrensův obrázek](results/nested162/claims-checked.json)
- [Známé opravy a prohledaná errata](results/nested162/errata-check.json)
- [Přesná metadata a omezení pramene](sources/nested162/source-observations.json)
- [Starší úplné výsledky](NESTED_QUEENS_NOTES.md)

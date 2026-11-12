# DLX 136: dvanáct pětiúhelníků na dvanáctistěnu

Kontrola 2. listopadu 2026. Zadání je na tištěné straně 139 (PDF 159),
celá odpověď na straně 451 (PDF 471). Používáme druhý dotisk lokálního 4B.

Matematická část souhlasí: **60 řešení při pevné poloze prvního dílku**,
**tři třídy** po ztotožnění geometrických symetrií a přejmenování barev,
se stabilizátory řádu **4, 6 a 12**. Dva úplné výčty mají shodné celé
množiny řešení. Ověřeno je všech **240 číslic** v původních obrázcích.
Nová chyba nevznikla. Celá úloha zůstává `partial` kvůli přesnému roku
objevu, historickému způsobu řešení a konvenci uvedených nákladů.

## Přesný model a úplnost

Souřadnice počítáme v tělese Q(φ), kde φ² = φ + 1, bez desetinného
zaokrouhlování. Vrcholy dvacetistěnu reprezentují stěny duálního
dvanáctistěnu. Každý má pět sousedů ve vzdálenosti 2; vzniká 30 hran
a 20 trojúhelníkových stěn. Kontrola přesně páruje všech 30 středů hran
s oběma vytištěnými souřadnicovými vzorci: šest názvů délky 2 a 24 délky 4.

Pětiúhelník má 5! = 120 pořadí pěti různých barev. Dvanáct typů získáme
podílem rotacemi a zrcadlením, které zde působí volně a mají řád 10.
Každá ze dvanácti stěn tedy má všech 120 možností, jak říká kniha.
Ukázková možnost pro stěnu `201` má přesně uvedených pět hran i barev
a opravdu patří typu `01243`.

XCC má 24 primárních položek (stěny a typy dílků) a 30 sekundárních
barevných položek (hrany). Každá hrana patří dvěma stěnám; barevná
kompatibilita vynutí stejnou barvu na obou stranách. Kotva ponechá
typ `01234` pouze na stěně `000` v orientaci `01234`; ostatní možnosti
ponecháme k odstranění běžným řešičem. Vstup má 1 321 možností.

Původní Knuthův `dlx2.w` vyčerpá tento vstup a najde 60 řešení.
Každé má všech dvanáct typů právě jednou, každá barva je na šesti
hranách a kotva je splněna. Terminální stav, celý výstup, přesný vstup,
zdroj a hash binárky jsou v [native/](results/dodeca136/native/).

Nezávislý výčet používá abstraktní graf dvou pětičlenných kruhů s póly,
domény 120 permutací a vlastní MRV rekurzi. Při hledání nepoužívá
souřadnice ani DLX. Teprve po úplném výčtu ověří izomorfismus s knižní
geometrií. Výsledných 60 modelů se jako celá množina shoduje s DLX.
Přejmenováním pěti barev vznikne všech 7 200 označených řešení: každé
obecné řešení má jedinou normalizaci barev podle stěny `000`, takže
žádné řešení mimo tuto konstrukci nechybí.

## Symetrie, matice a známé úpravy E067

Každá vytištěná matice je přesně ortogonální a permutuje dvanáct
vrcholů se zachováním hran. Pět generátorů lokálního 4B vytváří grupu
řádu 120. Je to celá grupa: obraz zvoleného vrcholu má 12 možností,
obraz sousedního vrcholu pět a volba strany sousedního trojúhelníku dvě.
Po určení obrazů tohoto trojúhelníku je sousední trojúhelník přes jeho
hranu určen jednoznačně. Souvislost dvaceti trojúhelníků určí celý graf.
Více než 12 · 5 · 2 automorfismů tedy není.

Geometrická transformace následuje přejmenováním barev, které obnoví
kotvu. Jde o působení na třídách podle globálního přejmenování barev;
geometrické změny s přejmenováním komutují. Úplný výpočet orbit dává:

| Velikost orbity mezi 60 modely | Počet automorfismů |
|---:|---:|
| 30 | 4 |
| 20 | 6 |
| 10 | 12 |

Oficiální vrstvy obsahují dvě **úpravy**, nikoli nový matematický omyl:

- **27. 10. 2020, Fascicle 5, str. 259:** nahrazení matice Q. Staré Q má
  řád 2, nové řád 5; s ostatními generátory obě dávají stejnou grupu 120.
  Tato změna už je v našem 4B zapracována.
- **6. 4. 2025, 4B, str. 451:** vynechání nadbytečných D₁ a D₂. Generátory
  D₀, P, Q samy dávají tutéž grupu; zbývající dvě reflexe jsou také
  konjugáty D₀ pomocí P. Lokální kniha ještě uvádí pět matic.

Obě položky jsou v autorově TeXu označené `amendpage`. Evidence E067
a její anglická karta je výslovně odlišují od chyby. Prohledány všechny
šest relevantních aktuálních a historických vrstev, devět kontextů
ručně rozlišeno; tři z nich patří nesouvisejícím úlohám 281/284.
Čerstvost vzdálených souborů přebíráme z dnešní kontroly v 08:06 UTC,
shodu všech lokálních hashů ověřuje nový program.

## Původní obrázky

Z vektorových cest a souřadnic glyfů v původním PDF bylo přečteno všech
60 číslic zadání a 180 číslic odpovědi. Dvanáct obrázků zadání tvoří
přesně dvanáct typů. Šest sítí odpovědi má po šesti pětiúhelnících.
Párování plochých společných hran používá skutečnou vzdálenost konců:
největší odchylka jejich zaokrouhlených souřadnic je přibližně
0,001415 bodu. Zaokrouhlování do pevných mřížkových buněk by zde
chybně rozdělilo některé shodné body; tento problém extrakce je opraven.

Každá dvojice sítí má právě jedno správné vzájemné otočení mezi pěti
možnostmi. Všech 30 hran souhlasí a všech 12 typů je použito jednou.
V pořadí obrázků vycházejí automorfismy 4, 6 a 12, přesně podle textu.
[Čitelný výřez](images/dodeca136-answer.png) a
[úplná evidence glyfů a skládání](results/dodeca136/figures-checked.json).

## Historický originál

Z veřejného [archivu Eureky 22](https://archive.org/details/eureka-22)
jsme získali celý původní sken i OCR; obě stažení souhlasí s kontrolními
součty archivu. Titulní strana potvrzuje **říjen 1959**. Článek
**M. R. Boothroyd a J. H. Conway, Problems Drive, 1959**, začíná na
straně 15; náš problém je číslo 6 na straně 16 a odpověď na straně 22.
Citovaný rozsah článku 15–17 a odpovědí 22–23 tedy sedí.

Všech dvanáct typů a všechny tři řetězce původních řešení byly ručně
přepsány podle zobrazených stránek, nikoli slepě podle OCR. Každý
řetězec má při pevné orientaci pásu právě jedno doplnění v našem
úplném výčtu. Původní pořadí řešení má stabilizátory **12, 4, 6**;
jde o tytéž tři třídy jako v TAOCP.
[Program](check_dodeca136_history.py),
[výsledky](results/dodeca136/history-checked.json),
[zadání 1959](images/eureka22-p16.png),
[odpověď 1959](images/eureka22-p22.png).

Jméno „Quintominal Dodecahedra“ je doložené také v knize, jejímž
spoluautorem je Conway: **Winning Ways, díl 4, druhé vydání**, strany
903 a 921. Obě stránky byly zobrazené; obsahují stejné zadání a tabulku
typů a tři řešení. Tato kopie PDF je obrazová, `pdftotext` nevydává text.
Zobrazená předmluva je podepsaná Berlekampem, Conwayem a Guyem a má
datum 7. února 2004. To potvrzuje užívání názvu, nikoli datum jeho vzniku.

Přesný **rok 1958** a tvrzení, že Conway úplný rozbor provedl ručně,
nejsou dosud těmito prameny nezávisle doložené. Publikace v roce 1959
není důkaz, že údaj 1958 je chybný. Neoznačujeme jej jako nový nález.

## Devět megamemů a zbývající rozsah

Původní program uvádí `505496 + 9138505 - 1848260` memů:
inicializaci, skutečné přístupy při hledání a možné ušetření při
vynechání aktualizací délek sekundárních sloupců. Hrubá hodnota
**9,138505 milionu** se zaokrouhlí na knižních 9; po odpočtu je
**7,290245 milionu**. Vytištěné operace na stranách 69 a 90 délky
aktualizují; dodatečné odčítání je v `dlx2.w` výslovně vysvětlené.

Máme tedy konkrétní vstup a úspěšnou reprodukci přibližné hrubé ceny.
Nemáme původní Knuthovo pořadí možností ani výslovný doklad, kterou
konvenci zde použil. Tuto shodu nepřenášíme automaticky na jiné úlohy,
u nichž předchozí měření souhlasila naopak s čistými náklady.

Pro uzavření celé úlohy zbývá nezávisle doložit přesnou chronologii
1958, původ ručního úplného rozboru a historickou nákladovou konvenci.
Souřadnice, všechny příklady a obrázky, úplné počty, grupy i citace
Eureky jsou již ověřené a není důvod tyto výčty znovu spouštět.

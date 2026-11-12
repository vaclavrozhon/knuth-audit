# Cestová domina — X151–153, průběžný záznam

Aktualizace 3. listopadu 2026: [nový průchod 151–152](PATHS151_152_NOTES.md) uzavírá původním obrázkem mezeru všech48 dílků. Starých6420 a certifikáty převzaty bez nového hledání. Níže je zachován starší časový záznam.

Kontrola 31. 10. 2026. Zadání str. 143–144, odpovědi 459–460.
Zatím žádná nová chyba. Výčet 6 420 faktorizovaných uspořádání je dokončen
a má nezávisle ověřené důkazy úplnosti. Sada všech 48 dílků zůstává otevřená.

## Katalog

Šest míst připojení je číslováno po obvodu, otočení o 180° přičítá 3 modulo 6.
Při 0,1,2,3 vnitřních podcestách jsou počty párování 1,15,45,15. Pevných
párování při půlotáčce je 1,3,9,7. Burnside tedy dává 1,9,27,11 dílků,
celkem 48. Výčet nekřížících se párování dává 1,9,18,4, celkem 32.

Pro start/stop z 153(b) se volí tři připojení, jedno z nich je terminál.
Žádná lichá trojice není pevná při půlotáčce: 20*3/2=30 různých vzorů.
Počty ze zadání i této odpovědi souhlasí.

## 151(a,b): vlastní ověřené smyčky

Nejprve se hledá pouze pokrytí buněk a shoda přítomnosti cesty na hranách.
Jednocestné vzory mají multiplicitu 1, dvoucestné multiplicitu 3.
SAT model je nezávisle ověřen dosazením: každá buňka právě jednou, přesné
multiplicity, shodné hodnoty hran a nulové výstupy na vnějším obvodu.

Pak se přiřadí všech 36 skutečných dílků. Druhý SAT problém má volbu
právě jednoho dílku na pozici a každého dílku právě jednou. Nesouvislé
cykly se vylučují řezy, dokud nevznikne jediný cyklus. Konečný výsledek
kontroluje přímý grafový výpočet: každý vrchol má stupeň dva a graf je souvislý.

- 18 vodorovných a 18 svislých: hotový svědek, 4 SAT kola, 9 řezů.
  Obrázek `results/path_dominoes/balanced36.svg` je odvozen z ověřených dat.
- 32 vodorovných a 4 svislá: hotový svědek, 3 SAT kola, 9 řezů.
  Každý z osmi řádků má lichou délku 9 a musí obsahovat lichý počet buněk
  svislých domin. Jsou proto potřeba nejméně čtyři svislá domina. Svědek
  dokazuje, že 32 je skutečné maximum.

Při tomto maximu musí být přesně jedna svisle pokrytá buňka v každém řádku.
Svislá domina tedy párují řádky (0,1),(2,3),(4,5),(6,7); jejich sloupce jsou
sudé, aby oba zbylé úseky řádku šly vyplnit vodorovně. Geometrických pokrytí
je proto 5^4=625. Přesný počet vyplnění vzory je nyní ověřen: 6420.

Kódování bylo srovnáno s nezávislým výčtem geometrických pokrytí a všech
podmnožin spojovacích hran na deskách 2×2,2×3,2×4: 21 různých inventářů,
56 řešení a dalších 96 dotazů s omezeným počtem vodorovných domin.

## 152: nemožnost všech 32 nekřížících se dílků

Šachovnicové obarvení dává jednoduchý obecný důkaz, dokonce pro libovolný
tvar složený z políček. Na každé straně domina leží tři připojovací body.
U 23 dílků z nekřížícího se katalogu je počet aktivních bodů na černém a
bílém políčku stejný. Zbývajících 9 dílků má rozdíl +2 nebo −2 podle polohy.
Každé spojení mezi dvěma dominy přitom spojuje černé políčko s bílým,
takže celkový rozdíl musí být nulový. Devět čísel ±2 však nulový součet
mít nemůže. Nemožnost platí i při povolení více smyček.

Tento důkaz a výčet příslušných rozdílů jsou nezávislé na SAT solveru.
Běh `planar32` byl po nalezení důkazu zastaven; neoznačujeme ho za UNSAT
výsledek solveru a žádný DRAT certifikát z něj netvrdíme.

## Otevřená práce a technické poznámky

`max36` je dokončen s přesným počtem 6420 a nezávisle ověřenými důkazy
úplnosti. `all48` ani omezené hledání s prázdným dílkem v rohu zatím
svědka nenašly; skončily časovým limitem, nikoli důkazem nemožnosti.
Obrázky 153(a,c) byly následně přepsány a úplně ověřeny; viz závěr tohoto záznamu.

První verze kódování počtu vodorovných domin používala každou variantu
vzoru zvlášť a měla 101497 proměnných. Tento nedokončený běh byl zastaven
a nahrazen ekvivalentním počítáním geometrických pozic s 18873 proměnnými.
Již nalezený svědek balanced36 z původního kódování zůstal zachován.
To je optimalizace našeho programu, nikoli chyba knihy.


## Dokončený výčet 6420

První globální SAT běh našel 5705 různých řešení za 1800 sekund. Jejich
uzávěr na obě osová zrcadlení obsahuje přesně 6420 řešení. Každé bylo
nezávisle zkontrolováno a uložené ID množiny nemají duplicity.

Úplnost byla dokázána jiným rozdělením problému. Všech 625 geometrií
určují čtyři sudé sloupce svislých dílků. Dvě osová zrcadlení dávají
169 orbit; jejich reprezentanti mají po řadě konkrétní CNF jen pro
příslušné geometrické pozice. Po vyloučení známých modelů je všech 169
formulí UNSAT. Každý DRAT důkaz nezávisle ověřil drat-trim; CNF a důkazy
jsou archivované gzipem spolu s SHA-256 původního obsahu. Součet
počtů modelů násobených velikostmi orbit je 6420.

`check_path_geometries.py` obsahuje úplný převod a kontrolu symetrií;
`results/path_dominoes/geometries/summary.json` odkazuje na jednotlivé
certifikáty. Původní globální pokračování bylo po dokončení tohoto
rozděleného důkazu zastaveno. Samo žádný UNSAT certifikát nevydalo;
nezaměňujeme je s úspěšnou nezávislou kontrolou všech geometrií.

Původní časový limit zůstává jako `max36-initial-timeout.json`, nový
souhrn jako `max36.json`, záznam zastavení jako `max36-global-resume.json`.
Soubory `all48.json` a `all48-corner.json` evidují neúspěšná časově omezená
hledání 48 dílků (1800 a 1200 sekund). Nejsou důvodem k nálezu v knize.


## Dokončené obrázky 153(a,c)

Na str. 460 patří pravý obrázek části (a), levý části (c). Přepis
`check_path153.py` zachovává jednotlivá vnitřní spojení a terminální
bod; nepoužívá pouze masky připojení. Inventář pravého obrázku se přesně
shoduje s osmi dílky zadání na str. 144. Oba obrázky mají osm různých
domin a čtyři prázdná políčka a tvoří jedinou cestu mezi terminály.

Úplný SAT výčet našel pro každý inventář přesně dvě polohy, související
otočením o 180°. Stejné počty dal původní autorův DLX2 nad samostatně
vypsaným XCC vstupem. Každá nalezená poloha prošla přímou kontrolou
pokrytí buněk, inventáře, souhlasných hran, stupňů a souvislosti grafu.
Žádná další sestava s vedlejšími smyčkami nevzniká. Jednoznačnost obou
puzzle je tedy potvrzena. Výsledky jsou v `results/path_dominoes/153a.json`
a `153c.json`, včetně přepisu obrázků a všech modelů.

Pro otevřenou sadu 48 dílků byl připraven také vstup pro původní DLX3:
4 096 možností, 116 primárních a 172 sekundárních položek. Běh s osivem 1
začal kolem 00:35 UTC; jeho výsledek je třeba zaznamenat zvlášť.

Běh původního DLX3 s osivem 1 skončil po 1 800 sekundách časovým
limitem (exit 124). Nenašel žádný model; poslední průběžný záznam
je 1 200 000 004 639 mems. Nejde o důkaz nemožnosti. Vstup, log
a metadata jsou uložené jako `all48.mcc` a `all48-dlx3-seed1.*`.

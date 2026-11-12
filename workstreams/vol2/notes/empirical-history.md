# §3.3.2 M: historie a rozsah empirických závěrů

Audit 1.11.2026, tištěné strany74–75, DjVu86–87. Matematické
části A–L a všech35 odpovědí mají samostatné poznámky. Tato kontrola
uzavírá historické odstavce v níže vymezeném rozsahu; nedostupné
původní materiály nepovažujeme za přečtené ani za vyvrácené.

## Kendall a Babington-Smith

Původní články [1938](https://academic.oup.com/jrsssa/article/101/1/147/7096459)
a [1939](https://academic.oup.com/jrsssb/article/6/1/51/7026479)
jsou dostupné v indexovaném PDF vydavatele. Přečteny pasáže o čtyřech
testech:1938 §24 a str.158–159,1939 §11–19. Číslice0–9,
frekvenční, sériový, pokerový a mezerový test souhlasí s Knuthem.

V1938 str.158 se dvojice překrývají a poslední číslice je spojena
s první. Autoři vyhodnocují statistiku pomocí chí-kvadrát rozdělení
s90 stupni volnosti; stejný postup opakují1939 str.55. Výhrada
v knize je oprávněná: [vlastní výpočet kovariance](serial-overlap.md)
už dokázal, že závislé četnosti obecně nedávají obyčejný Pearsonův
test. V případě dvojic nad10 symboly má limitní zákon podobu
`chi²_81 + 2 chi²_9`, s nezávislými sčítanci, nikoli `chi²_90`.
Symbol `chi²_r` znamená součet čtverců r nezávislých standardních
normálních veličin. Jde o asymptotický zákon, nikoli tvrzení
o přesném rozdělení vzorku5000 číslic.

Zmíněnou variantu sbírání kupónů se v těchto přečtených pasážích
nepodařilo lokalizovat. Její atribuce zůstává zdrojově nedoložená;
absence v prohledaném textu není důkaz chybné atribuce. Greenwoodův
článek1955 má potvrzené vydavatelské údaje, DOI
[10.1090/S0025-5718-1955-0068168-8](https://doi.org/10.1090/S0025-5718-1955-0068168-8),
svazek9,str.1–5. PDF AMS a náhled JSTOR byly nedostupné.
Samotný kupónový test má nezávislý důkaz v `empirical-basic.md`.

## Bienaymé a běhy

Přečten dobový přetisk Bienaymého práce v
[Bulletin des sciences mathématiques et astronomiques9(1875),219–225](https://www.numdam.org/item/BSMA_1875__9__199_0.pdf),
PDFstr.22–28. Jde o přetisk v souhrnu jednání akademie, nikoli přímo
citovaný svazek Comptes Rendus. Definuje střídající se vzestupné
a sestupné běhy a srovnává počty extrémů s teoretickými hodnotami
u astronomických a losovacích dat. To podporuje Knuthovu historickou
atribuci. Sám autor odkazuje na své dřívější oznámení z3.6.1874;
kniha netvrdí, že1875 byl první rok zveřejnění výsledku.
Původní astronomická data a všechny číselné příklady zde znovu
nepřepočítáváme.

Nezávislost na konkrétním spojitém rozdělení vyžaduje zachovat
předpoklad nezávislých stejně rozdělených pozorování. Jejich pořadí
pak tvoří rovnoměrnou permutaci, neboť pravděpodobnost shody je nula
a permutování indexů nemění společný zákon. Každé z n! pořadí má
proto pravděpodobnost1/n!. Tím se přenesou všechny testy založené
jen na pořadí, včetně běhů. Samotná absence shod bez uvedeného
předpokladu nestačí; např. nezávislá pozorování v navzájem oddělených
rostoucích intervalech jsou vždy seřazena. Knuthovu větu čteme
v kontextu testované hypotézy náhodné posloupnosti, která tento
předpoklad obsahuje, nikoli jako tvrzení o libovolných zákonech.

## Kermack a McKendrick: rok1937 je správný

Vydavatelský katalog uvádí rok1938 u obou článků, DOI
[10.1017/S0370164600013778](https://doi.org/10.1017/S0370164600013778)
a [10.1017/S0370164600013821](https://doi.org/10.1017/S0370164600013821).
To samo není důvod k nálezu. Původní
[titulní list a obsah](../sources/prse-volume57-front-matter.pdf)
byly zobrazeny: svazek57 je označen1936–1937, vytištěn1938;
články17 a22 vyšly samostatně10.6.1937 a5.10.1937.
Rozsahy228–240 a332–376 souhlasí.

Přečteny také vydavatelské úvodní výňatky obou článků. Podporují
téma testování náhodnosti a definici střídajících se běhů.
Plná PDF se při stažení přesměrovala na stránku bez přístupu.
Konkrétní citát o srážkách1785–1930 a výrok o použití pouze
průměru a směrodatné odchylky tedy zůstávají neověřeny v originálu.
Rozdíl katalogových roků je vysvětlen, nikoli nový kandidát.

## Další citace a doporučení

- Levene–Wolfowitz1944,15,58–69 a Barton–Mallows1965,36,236–260:
  vydavatelská metadata přes Crossref potvrzena; plné texty
  Project Euclid blokovala přístupová stránka. Historické prvenství
  opravy a celou diskusi omylů nepotvrzujeme jen z názvů článků.
  Nutnost kovariancí a správné vzorce zde mají vlastní důkazy
  v `run-tests.md` a `serial-overlap.md`.
- Christiansen1975 je výslovně nepublikovaný podklad. Nemáme jeho
  rukopis ani nezávislé potvrzení původu nápadu. Knuthovo
  svědectví takto ponecháváme; výpočet kolizí je samostatně ověřen.
- Označení prvního testu vyvinutého po příchodu počítačů čteme
  v návaznosti na probírané testy; nekvalifikujeme je jako
  univerzální prvenství mezi všemi statistickými testy.
- Relativní síla testů a praktická doporučení nejsou univerzální
  matematická tvrzení. Odkazy na3.3.3-23/24,3.5-26 a3.6-14
  budou znovu propojeny při kontrole příslušných sekcí.
- Příklady se středními čtverci a maximovým testem nemají uvedené
  parametry k rekonstrukci původních pokusů. Nehlásíme jejich
  reprodukci. Vyčerpávající záruku náhodnosti by konečný soubor
  testů neposkytoval.
- Vattulainen et al.1995: přečtené původní strany214–219 skutečně
  popisují selhání mezerového testu RCARRY, s lagy24/10 a maximem30.
  Podrobnosti a hranice reprodukce jsou v `lfsr-walks.md`.
  Marsagliův monkey příklad je celý uzavřen v `monkey-test.md`.

Všechny čtyři vrstvy errat a aktuální TeX prohledány podle stran,
jmen a názvů testů. Na74 se známá errata22.8.2002 a3.10.2008
týkají bibliografické formy a závorky. Neopravují rok1937.
Nový nález v historických odstavcích nepotvrzen. Uvedené mezery
v dostupnosti zdrojů zůstávají výslovnou mezí uzavřeného auditu.

# DLX 150 — Endless Chain, průchod 3. listopadu 2026

Nový **F139**: vytištěné zadání má nulový počet řešení, zatímco čtyři
obrázky v řešení i počet 43 patří sadě s jiným poměrem malých dílků.
Krátký obecný důkaz a opravu má [F139_ENDLESS_CHAIN_INVENTORY.md](F139_ENDLESS_CHAIN_INVENTORY.md).
Matematická část je dokončená; celá úloha zůstává **partial** kvůli
původu citované reklamy, přesnému datování circa 1887 a prvenství hlavolamu.

## Extrakce a důkaz

`extract_chain150.py` čte 18 obdélníkových obrysů a průsečíky inkoustových
čar s hranami dílků z původních vektorových stop. Respektuje ořezové masky
a používá vnitřní sondy, aby nepočítal samotný rámeček. Běžný konec má
čtyři tahy širokého článku, zvláštní konce posledních dvou dílků pouze dva.
Samostatně zapsaný seznam v `verify_f139.py` přesně souhlasí s extrakcí.
Původní PDF i draft mají totožné dílky. Obrázky byly také prohlédnuty.

Plochy dílků dávají 64, středové cesty procházejí 34 poli. Existuje 14
různých typů, čtyři ve dvou kopiích. Tyto dílčí počty knihy jsou správně.
Konce typu H/V mají lichou paritu právě u dílků 3, 14, 17. Ve všech čtyřech
otočeních se zachová; výsledný lichý součet vylučuje jakékoli uzavřené
sestavení. Neproběhl výčet původní sady.

Po nahrazení jednoho S-domina kopií L-domina zůstávají 14 typů a čtyři
páry. Změní se násobnosti dvou typů, nikoli rozměry nebo celková délka cesty.
Tuto opravu potvrzují všechny čtyři vytištěné sestavy. Každá má právě dvě L
a jedno S, úplné pokrytí, správné spoje a jedinou smyčku délky 34.

## Model a redukce symetrie

Před spojením dvou posledních dílků odpovídá popis Algorithm M 14 primárním
položkám typů a 64 polím. Násobnosti typů jsou 1 nebo 2; barvené sekundární
položky kódují přítomnost/absenci cesty na hranách sousedních polí.
Nejprve se musí opravit samotný inventář podle F139.

Zvláštní konce se nacházejí pouze na posledních dvou dílcích, musí se tedy
spojit. Jejich vzájemné posunutí a natočení je určeno. Vznikne jeden dílek
plochy 11, obsažený v obdélníku 6 × 2 s jedním chybějícím rohovým polem.
Všechny jeho vnější spoje jsou běžné; zvláštní spoj je uvnitř. Zůstává
13 typových primárních položek a 64 polí, celkem 77, a 112 sekundárních hran.

Po fixaci orientace složeného dílku je z každé rotační třídy právě jeden
zástupce. Jeho tvar nemá netriviální rotační symetrii. Kandidátní pozice
`x=0..2, y=1..6` dávají bezpečné omezení na 18 pozic; tři poslední se vyřadí
kvůli koncům mířícím mimo desku. Zbývá 15 skutečně přípustných umístění.
Knižních „one of 18 positions“ nemusí označovat minimální počet, takže tento
rozdíl není další nález. Nepředstíráme znalost původní autorovy konvence.

Každá možnost modelu určuje typ, obsazená pole a všechny vnější hrany
s barvou cesta/bez cesty. Přesné pokrytí odpovídá položení všech dílků se
shodnými rozhraními. Samotné barevné pokrytí obecně nevynucuje jediný cyklus;
proto byly komponenty každého nalezeného výsledku samostatně zkontrolovány.

## Jeden úplný, omezený výčet opravené sady

1355 možností, původní nezměněný DLX3 / Algorithm M. Malý vstup tvořený
jedním vytištěným svědkem potvrdil správné násobnosti. Úplný běh měl limit
60 s, prioritu nice 15 a skončil za **22,807 s**. Všech **43 modelů** bylo
přímo ověřeno podle geometrie a každý má jediný 34polový cyklus.
Nevznikla druhá dlouhá fronta. Náklad je 5 042 928 862 čistých mems;
historických 7 Gμ nepovažujeme za přesně reprodukované a pořadí neladíme.

Při odstranění hranic dílků, ale zachování rámu a identifikaci globálních
rotací, zbývá **8 cest**. Jejich násobnosti jsou 1, 1, 2, 3, 5, 7, 9, 15.
Vytištěné (i), (ii), (iii), (iv) se vyskytují **1, 15, 9, 3** krát.
Příklad (iv) skutečně nepoužívá celý pravý sloupec. Příklad (iii) má téměř
prázdný levý dolní kvadrant; přesný graf je uložený.

První klasifikátor odstranil také translace a dostal 7 tvarů a násobnost
4 u (iv). To slučuje dvě různé polohy stejné cesty v rámu. Samostatná
kontrola zachovávající rám reprodukovala všechna knižní čísla bez nového
hledání; nejde o další numerickou chybu. Původní diagnostika je zachována.

## Historie, errata a zbývající rozsah

Úplný místní dobový Hoffmannův sken byl prohlédnut na str. 99, 100 a 131
(PDF 62, 63, 78). Potvrzuje oddíl III, úlohu XVIII, 18 dílků a přímo
obrázek řešení (i), Fig. 305. Popis na str. 100 požaduje jediný uzavřený
řetěz. Vazba na Hoffmannovu úlohu je tím ověřena.

Autorská [nabídka reprodukce od Tona Delsinga](https://puzzleparadise.net/listing/endless-chain-c-the-reason-manufacturing-co-ltd-1880-1895/134050)
uvádí Reason Manufacturing a širší období 1880–1895. Její fotografie víka
má čitelný název výrobce. Jde však o moderní reprodukci, ne datovaný doklad
z roku 1887. Přesná původní reklama, její citované znění a prvenství jsou
otevřené; žádný dotaz autorům ani email nebyl odeslán.

Šest vrstev errat podle stránek, úlohy a motivu neobsahuje opravu F139.
Shody pro sousední 151 a 152 zůstávají oddělené. Známé opravy těchto úloh
budou přijaty při jejich vlastním průchodu.

Programy a hotové terminály se neopakují. Výslovně vynecháno je další
ladění historického nákladu 7 Gμ. Následuje DLX151; celý svazek není hotový.

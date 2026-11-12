# Primární zdroje a přesné meze

Stav k 2026-11-01. Místní `sources/SHA256.json` uvádí hashe stažených
souborů; `sources/retrievals.json` zachycuje první dávku stažení včetně
neúspěchů. Odkaz na primární zdroj není automaticky tvrzení, že byl
získán jeho plný text.

## Kniha a opravy

Autoritativní podklad je `books/taocp-vol1-ed3-print1-1997.djvu`, vydání
3, dotisk 1, květen 1997, SHA-256
`e2c5ee120bad91e33f617614b846849c4801115b2e7aa820f56fc5ffb9bbebb9`.
Tištěná strana p je souborová p+15. Všechny obrazy hlavního textu
334–348 a odpovědí 571–575 byly zobrazeny; vlastní rozsah přesně odděluje
začátky a konce sousedních sekcí. Fyzický tištěný exemplář nebyl ověřen.

Opravy pocházejí ze čtyř autorových řad
[all1-prepre](https://www-cs-faculty.stanford.edu/~knuth/all1-prepre.ps.gz),
[all1-pre](https://www-cs-faculty.stanford.edu/~knuth/all1-pre.ps.gz),
[all1](https://www-cs-faculty.stanford.edu/~knuth/all1.ps.gz) a
[err1](https://www-cs-faculty.stanford.edu/~knuth/err1.ps.gz).
Jejich živé hashe byly již v téže relaci ověřeny 2026-11-01 v
19:39 UTC, viz read-only doklad
`../doubly-linked/sources/live-errata.json`: všechny souhlasily se
sdíleným snapshotem, nejnovější all1/err1 mají Last-Modified 2026-05-31.
Stejné úspěšně ověřené soubory nebyly znovu stahovány. Výsledky
vlastního hledání k nynější sekci a hashe textů jsou v
`results/errata-*.json`; deset zásahů popisuje ERRATA.md. U rovnice (21)
byl navíc přímo prohlédnut původní obraz historické opravy. Root při
revizi tří nových nálezů nezávisle prohlédl původní vrstvy errat.

## Polský prefixový zápis: checked

Primární text Jana Łukasiewicze, „Uwagi o aksyomacie Nicod'a i o
dedukcyi uogólniającej“, v pamětní knize Polského filozofického spolku
ve Lvově (1931), pp. 366–382, byl získán z
[Śląské digitální knihovny](https://www.sbc.org.pl/dlibra/publication/edition/18864),
[celý původní svazek PDF](https://sbc.org.pl/Content/18864/PDF/18864.pdf).
Na p. 367 autor přímo vysvětluje prefixové umístění binárního operátoru
D a bez závorek zapisuje Nicodův axiom. Poznámka 3 popisuje nápad
z roku 1924 a první tisk v roce 1929. Originální obraz p. 367 je
`images/lukasiewicz-1931-p367.png` (PDF strana 374), přepis a celý
svazek v sources/. Tím je podložena atribuce na p. 338 knihy; tvrzení
o prvenství před všemi jinými možnými notacemi není předmětem závěru.

## Diferenciace „již roku 1952“: partial

Získán primární retrospektivní projev Grace Murray Hopperové na HOPL
1978, vydaný v *History of Programming Languages* (1981), Keynote
Address, pp. 7–19, z
[vydavatelského náhledu](https://api.pageplace.de/preview/DT0400.9781483266169_A23870219/preview-9781483266169_A23870219.pdf).
Přečteny pp. 12–14, obraz p. 13 je uložen. Autorka popisuje vlastní
funkční diferenciátor a následnou práci Harryho Kahrimaniana zakončenou
diplomovou prací v květnu 1953. Předchozí výslovný údaj květen 1952
se vztahuje k překladači A-0. Chronologie podporuje rané použití, ale
sama přesně nedokládá rok 1952 pro diferenciátor. Nepřevádím tuto
nepřímou návaznost v potvrzený konkrétní letopočet.

Přesný zbývající podklad: H. G. Kahrimanian, „Analytical Differentiation
by a Digital Computer“, *Symposium on Automatic Programming for Digital
Computers*, 13–14 May 1954, pp. 6–14, nebo jeho Temple thesis (1953)
s explicitním datováním vývoje/provozu. [Primární svazek v Google Books](https://books.google.com/books?id=6AkgAAAAIAAJ)
je identifikován, plný relevantní obsah se nezískal. DTIC AD0048481
vrací 403, příslušný odhad archivního identifikátoru nemá metadata,
vyhledání „1952“ uvnitř Google svazku dalo nulu; ani jedno není
důkazem nepřítomnosti roku v originálu. John F. Nolan,
[MIT thesis 1953](https://dspace.mit.edu/entities/publication/8eacf4c2-a442-466e-bdf5-04ca7b8d5981),
je bibliograficky ověřen přímo v institucionálním repozitáři, ale
stažení vrací 429 a nemůže samo dokázat rok 1952. Žádný nový historický
rozpor zde nebyl potvrzen.

## Sammetová v odpovědi 17: metadata checked, full text partial

Jean E. Sammet, „Survey of formula manipulation“, *Communications of
the ACM* 9(8) (August 1966), pp. 555–569,
[DOI 10.1145/365758.365762](https://doi.org/10.1145/365758.365762).
Primární metadata uložená vydavatelem v
[Crossref](https://api.crossref.org/works/10.1145/365758.365762)
potvrzují autora, titul, rok, svazek i rozsah a obsahují seznam citací
starších systémů, včetně Kahrimaniana a Nolana. Lokální JSON je
uložen celý. Vydavatelský PDF endpoint vrací 403; plný článek jsem
nečetl. Odkaz jako bibliografický rozcestník tedy doložen je, podrobná
kontrola obsahu všech jeho citovaných prací se netvrdí. Vlastní
programové řešení úlohy 17 je hotové nezávisle na získání článku.

## Nová odpověď 19: Skolem checked, Whitman content partial

Thoralf Skolem, *Logisch-kombinatorische Untersuchungen über die
Erfüllbarkeit oder Beweisbarkeit mathematischer Sätze nebst einem
Theoreme über dichte Mengen*, Videnskapsselskapets Skrifter I,
Matematisk-naturvidenskabelig Klasse, 1920, no. 4, pp. 1–36.
[Původní sken](https://richardzach.org/wp-content/uploads/2023/11/Skolem-1920-Logisch-kombinatorische-Untersuchungen-uber-die-Erfullbarkeit-oder.pdf)
je archivní reprodukce převzatá z BHL/Internet Archive. Získán celý;
prohlédnuta titulní strana a originály pp. 16 a 21, přečten §2
pp. 16–21. Definuje svazové operace pomocí dvojic a trojic a dokazuje
konečnou rozhodnutelnost odvození. To přesně vysvětluje relevanci
nového odkazu; nejde o pouhou shodu bibliografického názvu.

Philip M. Whitman, „Free Lattices“, *Annals of Mathematics* (2) 42(1)
(1941), pp. 325–330, [DOI 10.2307/1969001](https://doi.org/10.2307/1969001),
a „Free Lattices II“, 43(1) (1942), pp. 104–115,
[DOI 10.2307/1968883](https://doi.org/10.2307/1968883).
Autor, titul, roky a celé stránkové rozsahy jsou ověřeny přímo v
primárních obsazích čísel [1941](https://www.jstor.org/stable/i307206)
a [1942](https://www.jstor.org/stable/i307209). Crossref pro první
článek uvádí jen počáteční stránku 325, proto nebyl použit k rozhodnutí
o koncové straně. PDF endpointy JSTOR vracejí HTML, nikoli články.
Obsah a konkrétní lemma z Whitmanových originálů proto zůstávají
neověřené. Technická správnost odpovědi 19 má samostatný úplný důkaz
podle pravidel zadání a nezávislou kontrolu konečným svazovým uzávěrem.

## Dynastický příklad

Matematicky je princip „přednost potomků před mladšími sourozenci“
přesně preorder; to bylo dokázáno. Aktualizace z roku 2024 je zanesena.
Jako konkrétní primární doklad změny zvyklostí slouží
[Succession to the Crown Act 2013, section 1](https://www.legislation.gov.uk/ukpga/2013/20/section/1/enacted).
Není to audit všech evropských dynastií ani jednotlivých šlechtických
titulů a knižní ilustraci nepoužíváme jako obecné právní pravidlo.

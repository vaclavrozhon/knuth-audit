# §2.3.4.3: primární prameny a meze

Rozlišuji kontrolu výroku a citace v primárním prameni od nezávislého
opakování všech důkazů citovaného článku. Vlastní obecné důkazy všech
osmi úloh a hlavních konstrukcí jsou v PROOFS.md. Cizí klasifikace
všech malých sad dlaždic nebyla opakována.

Základem je třetí vydání, první tisk 1997, soubor
`books/taocp-vol1-ed3-print1-1997.djvu`, SHA-256
`e2c5ee120bad91e33f617614b846849c4801115b2e7aa820f56fc5ffb9bbebb9`.
Prohlédnuty všechny původní strany 382–386 a 586–588. Mapování je
tištěná strana p -> DjVu strana p+15. Hranice oddílu a odpovědí jsou
v HANDOFF.md. OCR ani Markdown nejsou autoritou pro vzorce a obrázky.

Úplné URL, čas získání, velikost a SHA-256 stažených podkladů obsahuje
`sources/downloads.json`; soubor zachovává také neúspěšné pokusy.
Následující odkazy míří na primární díla nebo jejich veřejné kopie.

| citace v knize | primární důkaz kontroly | přesný status |
|---|---|---|
| D. König, 1927 | [originál v institucionálním archivu](https://acta.bibl.u-szeged.hu/13338/1/math_003_121-130.pdf), s. 121–130; lokálně konig-1927.pdf | Přečteny s. 121–125, zejména obecný lokálně konečný graf na s. 122 a příklad lidských potomků na s. 125. Obsah a atribuce doloženy; neprováděn vyčerpávající průzkum světové priority. |
| H. W. Watson, J. Anthropological Inst. 4 (1874), 138–144 | [scan původního článku s Galtonovým úvodem](https://math.uchicago.edu/~shmuel/Modeling/Galton%20Watson.pdf), watson-galton-1874.pdf | Původní text a chybný krok na s. 143 přímo ověřeny; vlastní přesná nerovnost je v PROOFS. JSTOR předsádka má rok 1875, kdežto kniha 1874. Datum jednotlivého sešitu neověřeno, proto nejde o nový nález. |
| H. Wang, Scientific American 213(5), listopad 1965, 98–106 | [scan článku](https://www.math.ias.edu/~goresky/other/Mathematical%20Folklore%202025/Lecture%204%20%28February%2020%29/core/Wang-GamesLogicComputers-1965.pdf), wang-1965.pdf | Přečten argument kvadrant -> rovina na s. 104 a konec článku na s. 106. Digitální balík obsahuje i reklamu s. 107; údaj 98–107 v jeho metadatech není protiargument proti správné citaci knihy. |
| Grünbaum–Shephard, Tilings and Patterns (1987), kap. 11; též kap. 10–11 v historické odpovědi 5 | Citace z původního obrazu knihy | Plné příslušné kapitoly nezískány. Bibliografie a související historická tvrzení nejsou označena za přímo ověřená. |
| R. Berger, Memoirs AMS 66 (1966) | [primární vydavatelský záznam](https://doi.org/10.1090/memo/0066); přímý přístup k úplnému článku selhal | Název a vydání dohledány; původní 72stránkový důkaz nerozhodnutelnosti a přesná příbuznost s Knuthovou konstrukcí neprohlédnuty. Jeandel–Rao původní výsledek výslovně uvádějí. To není náhrada plného primárního auditu. |
| R. M. Robinson, Inventiones Math. 12 (1971), 177–209 | [originál článku](https://lipn.univ-paris13.fr/~fernique/qc/robinson.pdf), robinson-1971.pdf | Přečteny relevantní pasáže: šest geometrických tvarů na s. 180, oznámení 35 typů na s. 181, argument neperiodičnosti. Článek sám podrobně konstruuje 56 typů; redukci na 35 oznamuje. Knuthův odkaz odpovídá oznámenému výsledku; 35typová konstrukce nebyla nezávisle rekonstruována. |
| Penrose 1974; Gardner, Penrose Tiles to Trapdoor Ciphers (1989), kap. 1–2 | Historický odstavec původní odpovědi 5, nahrazený roku 2023 | Původní Penroseův článek ani příslušné kapitoly Gardnerovy knihy nezískány. Tvrzení o dvou polygonech a odvozených 16 typech zůstává historickou pramennou mezí. |
| B. Durand, TCS 221 (1999), 61–75, doplněk 2005 | [primární vydavatelský záznam a abstrakt](https://doi.org/10.1016/S0304-3975(99)00027-4) | Abstrakt potvrzuje existenci kvaziperiodického dláždění pro každou dlažditelnou konečnou sadu. Úplný článek nezískán (přístup 403). Výrok doplňku máme nezávisle dokázán v PROOFS. |
| E. Jeandel, M. Rao, Advances in Combinatorics 2021:1, doplněk 2023 | [vydavatel](https://www.advancesincombinatorics.com/article/18614-an-aperiodic-set-of-11-wang-tiles), [publikovaná sazba od autorů](https://arxiv.org/pdf/1506.06492), jeandel-rao-2021.pdf | Přečteny definice, hlavní výsledek, popis výpočetní klasifikace a první i poslední strana. 11 typů, 4 barvy a optimalita odpovídají citovanému výsledku. Jejich klasifikace nebyla znovu spuštěna. Přesný rozsah je 1:1–1:37; kandidát chybné koncové strany je oddělen v reports/. |
| B. L. van der Waerden, Nieuw Archief voor Wiskunde (2)15 (1927), 212–216 | [původní svazek v Delpher](https://resolver.kb.nl/resolve?urn=MMKWG01:022157001:00228), všech pět stran v images/van-waerden-1927-p*.jpg | Celý článek přímo přečten, včetně konečného znění a indukčního důkazu. Vydání je jako 1927 potvrzeno také vlastní autorovou citací v roce 1954, s. 53; metadata vázaného ročníku 1928 tedy nejsou novým nálezem. |
| Schreierova atribuce; van der Waerdenův účet v Studies in Pure Mathematics (1971), 251–260 | [primární německé vzpomínání z roku 1954](https://gdz.sub.uni-goettingen.de/id/PPN378850199_0009?tify=%7B%22pages%22:%5B53%5D%7D), Elemente der Mathematik 9, 49–56, obrazy všech osmi stran | Celý text přečten. S. 49–50 potvrzují diskusi 1926, Schreierovu konečnou otázku a diagonální argument. Jde o třetí sdělení série, jak uvádí původní poznámka na s. 49; katalogový název s II není autoritou. Přesná sazba a paginace anglického přetisku 1971 nebyla získána. |
| J. B. Kruskal, Trans. AMS 95 (1960), 210–225 | [scan článku](https://www.cs.tau.ac.il/~nachumd/term/Kruskal.pdf), kruskal-1960.pdf | Přečteny definice a hlavní věta na s. 211–214, včetně silnějšího označeného a homeomorfního výsledku. Kniha řeší vlastní variantu a tu jsme nezávisle dokázali. |
| D. König, Matematikai és Fizikai Lapok 39 (1932), 27–29 | [původní svazek](https://real-j.mtak.hu/7288/1/MTA_MatematikaiEsPhysikaiLapok_39.pdf), konig-1932-volume.pdf, PDF strany 37–39 | Všechny tři strany přečteny; tvrzení o konečnosti antichainů n-tic je přítomno, s německým resumé na s. 29. Nulový vektor je triviální rozšíření. Vlastní silnější sekvenční důkaz v PROOFS. |
| J. B. Kruskal, J. Combinatorial Theory A13 (1972), 297–305 | [originál článku](https://www.cs.tau.ac.il/~nachumd/term/WQO.pdf), kruskal-1972.pdf | Bibliografie a obsah přehledu vývoje dobře kvaziuspořádaných množin ověřeny v úvodu a příslušných pasážích. Nejde o nezávislý audit všech odkazovaných výsledků přehledu. |
| N. Dershowitz, Information Processing Letters 9 (1979), 212–215 | [autorův seznam publikací](https://www.cs.tau.ac.il/~nachumd/Termination.html), dershowitz-author.html | Autor potvrzuje A Note on Simplification Orderings, číslo 9(5), listopad 1979, 212–215. Úplný článek nezískán, aplikace na ukončování tedy bibliograficky partial. |

Všechny čtyři vrstvy errat a jejich současná dostupná verze jsou
doloženy v ERRATA.md. Jediný nový kandidát je bibliografická koncová
strana Jeandel–Rao. Omezený přístup k pramenům nevytváří sám o sobě
další kandidáty a není zaměněn za potvrzení bezchybnosti.

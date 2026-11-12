# Primární prameny a přesný rozsah čtení

Stav k 1. 11. 2026. Níže „ověřeno“ znamená ověření konkrétního tvrzení knihy,
nikoli úplný audit všech výsledků citovaného článku. Stahovací metadata, URL,
velikosti a SHA-256 jsou v `../sources/downloads.json`. Obrazy jsou v
`../images/`. Matematické důkazy auditu jsou vlastní a jsou odděleny
v `general-proofs.md`.

## Kirchhoff: s. 368

Získány [Gesammelte Abhandlungen (1882)](https://archive.org/download/gesammelteabhan00unkngoog/gesammelteabhan00unkngoog.pdf),
lokálně `kirchhoff-collected-1882.pdf` a archivní `-ocr.txt`. Přečteny obrazové
strany souborného vydání 1–2 a 15–17 článku z roku 1845; strana 18 byla
prohlédnuta jako hranice následujícího dodatku. První strana uvádí původní
Poggendorffovy Annalen 64 (1845). Strany 15–17 obsahují oba zákony a odvození:
součet proudů ve vrcholu je nula a součet úbytků v uzavřeném obvodu se rovná
součtu elektromotorických sil. Knižní výklad na s. 368 tomu odpovídá.

Pro tvrzení o Kirchhoffově vlastním použití stromové metody byly přečteny
obrazové s. 22–24, tj. úvod a celý první oddíl práce z roku 1847; OCR také
začátek s. 25. Jsou zde přímo popsány nezávislé fundamentální cykly získané
odebráním nejmenšího počtu hran a postupným jednotlivým vracením těchto hran.
Neauditoval jsem zbytek determinantového vzorce ani fyzikální analýzu desky
v první části práce z roku 1845.

Obrazové soubory `kirchhoff-collected-1882-file19/20/33/34/35/36/40/41/42.png`
odpovídají uvedeným stranám; v tomto úseku je číslo PDF strany tištěná strana
plus 18. Historická tvrzení knihy jsou ověřena **primárním autorským
přetiskem**. Původní časopisecký sken 1845 nebyl dostupný: Princeton vrátil
401, Gallica 403. To není nevyřešená matematická závislost.

## Ball a Larus: s. 369

[Optimally Profiling and Tracing Programs](https://faculty.cc.gatech.edu/~harrold/6340/cs6340_fall2010/Readings/p1319-ball.pdf),
ACM TOPLAS 16 (1994), 1319–1360, DOI 10.1145/183432.183527; lokálně
`ball-larus-1994.pdf/.txt`. Přečten titul, abstrakt, vybrané úvodní odstavce
a s. 1328–1329 oddílu 3.2. Prohlédnuty obrazy PDF stran 1, 10, 11. Text
výslovně odvozuje rozmístění čítačů pomocí kostry a obnovu toků od listů.
Tím je ověřen úzký odkaz knihy na další aplikace. Zbylé části 42stránkového
článku o trasování a jeho další výsledky auditovány nebyly.

## Knuth a Stevenson: odpověď 8, s. 579

[Optimal measurement points for program frequency counts](https://link.springer.com/article/10.1007/BF01951942),
BIT 13 (1973), 313–322. Uložena vydavatelská stránka
`knuth-stevenson-1973-publisher.html`; ověřeny bibliografické údaje a abstrakt.
PDF adresa vrací stránku s předplatným, nikoli článek.

Autorův přetisk je kapitola 5 v Selected Papers on Analysis of Algorithms
(2000), s. 43–53. Ve [veřejném textovém náhledu](https://www.scribd.com/document/365771795/Selected-papers-on-Analysis-of-Algorithms-Donald-E-knuth)
bylo přečteno vlastní tělo na s. 43–49 včetně redukce, její surjektivity,
minimality a ekvivalence s Nahapetianovou konstrukcí; též bibliografie na
s. 53. Programová příloha SIMULA na s. 49–52 nebyla auditována, protože
textový převod vynechává části zápisu. Relevantní veřejně zobrazený text
uchovává `knuth-stevenson-reprint-web-capture.json`; surové HTML se stejným
základem názvu celý tento text neobsahuje.

Knižní matematické tvrzení bylo navíc obecně dokázáno nezávisle. Zbývá
**zdrojová mezera**: původní článek 1973 ani obrazy sazby přetisku nebyly
získány. Stav pramene proto zůstává `partial`, nikoli „přečten původní článek“.

## Nahapetian: doplnění odpovědi 8 erratem 2001

[Node flows in graphs with conservative flow](https://link.springer.com/article/10.1007/BF00288650),
Acta Informatica 3 (1973), 37–41. Uložena vydavatelská stránka
`nahapetian-1973-publisher.html`; přečten abstrakt a ověřen titul, autor,
ročník, strany a datum. Znění abstraktu podporuje uvedený vztah mezi
vrcholovými toky a redukcí počtu měření. Autorský přetisk Knutha–Stevensona
výslovně obsahuje porovnání obou konstrukcí, ale není náhradou za přečtení
Nahapetianova textu.

Pokus o PDF skončil na předplatitelské stránce. Hledání přesného názvu,
autora a související stanfordské práce nepřineslo veřejný plný text.
**Konkrétně chybí pět stran původního článku**; stav `partial`. Žádná část
vlastního důkazu úlohy 8 na nepřečtené větě z tohoto zdroje nezávisí.

## Jarník a Prim: úloha 11 a erratum 2023

[Jarník, O jistém problému minimálním](https://dml.cz/bitstream/handle/10338.dmlcz/500726/Jarnik_01-0000-31_1.pdf),
Acta Societatis Scientiarum Naturalium Moravicae 6 (1930), 57–61;
`jarnik-1930.pdf/.txt`. Přečten celý český text 57–61 i německé resumé 62–63.
Prohlédnuty obrazy s. 57, 60, 61 (PDF 2, 5, 6). Jarník předpokládá kladné
navzájem různé ceny a dokazuje řezový princip i růst jediné komponenty.
Bibliografické strany 57–61 v erratu označují český text; katalogových 57–63
zahrnuje resumé, takže to není rozpor. Datum dopisu 12. února 1929 není
rokem vydání článku.

[Prim, Shortest Connection Networks and Some Generalizations](https://www.worldradiohistory.com/Archive-Bell-System-Technical-Journal/50s/Bell-1957-6.o.pdf),
Bell System Technical Journal 36 (1957), 1389–1401. Z celého čísla
`prim-1957-issue.pdf` byly vyňaty PDF strany 71–83 do `prim-1957.pdf`.
Přečten celý článek v textovém převodu; prohlédnuty obrazy s. 1389, 1392,
1393, 1400, 1401 (souborové 1, 4, 5, 12, 13). Ověřeny řezový výměnný
argument a vlastní růstový algoritmus. Implementace na s. 1400 odstraňuje
sloupec vybraného vrcholu a aktualizuje jen zbývající sloupce: chybu
odpovědi 12 v TAOCP neobsahuje. Další síťová zobecnění tohoto článku nejsou
samostatným předmětem zdejšího auditu.

Obě nové citace v erratu 2023 jsou ověřeny; žádné tvrzení o světovém prvenství
tohoto auditu či nálezu z nich nevyvozuji.

## Dijkstra a Stanford GraphBase: odpověď 12, s. 580

[Dijkstra, Some theorems on spanning subtrees of a graph](https://ir.cwi.nl/pub/9255/9255D.pdf),
Indagationes Mathematicae 22 (1960), 196–199; `dijkstra-1960.pdf/.txt`.
Přečten celý text a zobrazeny všechny čtyři strany. Bibliografie i význam
odkazu „see also“ odpovídají: článek rozvíjí výměnu hran a vlastnosti
minimálních koster. Netvrdí, že obsahuje doslovnou tabulkovou implementaci
z odpovědi 12.

[MILES_SPAN](https://mirror.gutenberg-asso.fr/tex.loria.fr/sgb/miles_span.pdf),
autorský zdrojový text Stanford GraphBase formátovaný 12. ledna 1994,
`miles-span-1994.pdf/.txt`. Přečteny oddíly 1, 8, 19–22 a začátek 23;
obrazy souborových s. 10–11 prohlédnuty. Algoritmus označuje vybrané vrcholy
KNOWN a při aktualizaci je výslovně vynechává. Potvrzuje správnou variantu,
nikoli chybnou reinicializaci z odpovědi 12. Všechny implementace prioritních
front v této kapitole auditovány nebyly.

[Vydavatelský náhled knihy](https://api.pageplace.de/preview/DT0400.9780135238257_A36005426/preview-9780135238257_A36005426.pdf)
`sgb-preview-2009.pdf`, obrazy souborových s. 3 a 7, potvrzuje počátek
MILES_SPAN na s. 460 a další kapitoly na s. 498, tedy citované rozpětí
460–497. Rok 1993 v TAOCP souhlasí s CIP a copyrightem programů; autorova
webová stránka označuje knihu rokem 1994 a copyright dodatečného knižního
materiálu je 1994. Bez původní tiráže první distribuce z toho nevyvozuji chybu.
Jde o bibliografickou nejednoznačnost, nikoli další kandidát.

## Vnitřní odkazy

Odkaz úlohy 6 na Algorithm 2.3.3E je použit pouze přes jeho kontrakt spojování
komponent; vlastní algoritmus má přidělen kořen. Algorithm 2.3.5A a §7.4.1.2
se zde znovu neauditují. Eulerovská existence, na niž odkazuje Theorem K
v úloze 2.3.4.2-24, je zde dokázána obecně; přesná kontrola tamějšího zadání
a odpovědi bude součástí následujícího bloku Oriented Trees.

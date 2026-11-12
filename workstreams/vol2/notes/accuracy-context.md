# §4.2.2: vymezený audit historického kontextu

Text229 a241–242 i příslušné vrstvy errat byly vizuálně přečteny.
Tato poznámka zaznamenává skutečný rozsah historické kontroly;
není tvrzením, že byly přečteny všechny citované knihy a články.
Matematické výsledky sekce mají samostatné důkazy v ostatních poznámkách.

## Epigrafy

Jeffersonova věta je v dopise Jaredovi Sparksovi ze4.2.1824,
*The Writings of Thomas Jefferson*, vydání1859, svazek7, str.332–333.
[Úplný přepis primárního textu](https://www.gutenberg.org/files/56035/56035-h/56035-h.htm)
obsahuje datum i shodné znění. Souvislostí je jeho číselný odhad nákladů
kolonizačního návrhu; matematická kapitola přebírá pouze obecnou větu.
Lokální soubor `jefferson-sparks-1824-excerpt.txt` uchovává okolí citátu,
metadata stažení jsou samostatně. Rukopis dopisu nebyl ověřován.

Johnsonovo znění potvrzuje *Johnsonian Miscellanies*, ed.G.B.Hill,
svazekII(1897), str.2: převzatý text ze sbírky Hawkinsových vzpomínek.
Str.1 v ediční poznámce uvádí Hawkinsovo vydání1787–1789. Obě stránky
byly vizuálně přečteny. **Rok1750 uvedený v TAOCP tento pramen
nedokládá.** Neznám datum vyslovení; pozdější vydání výroku samo
nevyvrací dřívější datum. Proto nejde o potvrzenou chybu.
[Digitalizace](https://archive.org/details/johnsonianmiscel02hilluoft).

## Zaokrouhlování v19. a počátkem20.století

Tanneryho *Leçons d'Arithmétique théorique et pratique*, Colin1894:
titulní list a str.231–233 byly přímo přečteny. Pravidlo první
vynechané cifry>=5 je na str.232 skutečně uvedeno. Odvození používá
porovnání absolutních chyb a přesnou mez poloviny jednotky;
**připisované zdůvodnění kompenzací podle pěti z deseti cifer jsem
v této pasáži nenalezl.** Ani cílené hledání v OCR celé knihy je
nevyhledalo. To nedokazuje nepřítomnost v jiném místě nebo prameni;
autorovu připisovanou motivaci tedy neoznačuji za ověřenou.
[Digitalizace](https://archive.org/details/leonsdarithmtiq00tanngoog).

C0090 je naproti tomu přímý historický protipříklad: půlky k sudému
jsou výslovně popsány v Newcombových tabulkách copyright1882,
str.14–15, i ve Woodwardově datovaném vydání1906, str.42.
Všechny citované stránky a titulní/copyrightové listy byly zobrazeny.
Viz `C0090-round-even-history.md`. Neprokazujeme jejich absolutní
prvenství. Scarboroughův původní text1930/1950 nebyl přímo dostupný;
existence staršího pravidla nijak nevyvrací, že jej také doporučoval.

## Matematické publikace a bibliografie

`accuracy-bibliography.json` uchovává23 cílených bibliografických
dotazů. Jen položky uvedené v `accepted_candidate_indices` byly
přijaty jako odpovídající metadata. Prázdný seznam neznamená,
že publikace neexistuje: část požadavků skončilaHTTP429, jiné
vrátily nesouvisející názvy. Po zjištění limitu další dotazy na
Crossref nebyly posílány. Srovnání metadat samo neověřuje obsah.

Přijaté bibliografické záznamy souhlasí v následujícím rozsahu:

| Citace v TAOCP | Ověřený údaj a omezení |
|---|---|
| Bauer–Samelson1953 | ZAMP4,312–316; potvrzeno i stránkou vydavatele. Prvenství analýzy neprokázáno. |
| Carr1959 | CACM2(5),10–15, *Error analysis in floating point arithmetic*. |
| Møller1965 | BIT5,37–50 a251–255; oba uvedené články. |
| Linnainmaa1974 | BIT14,167–202, článek o přesnosti plovoucích součtů. |
| Ashenhurst1962 | *The Maniac III arithmetic system*, počáteční str.195; konec202 metadata neuvádějí. |
| Gray–Harrison1959 | Článek s indexem významnosti, str.244–248. Název obsahuje „Normalized“; samotný název nevylučuje diskusi nenormalizované aritmetiky. |
| Gibb1961 | CACM4,319–320, Algorithm61, procedures for range arithmetic. |
| Moore1979 | Název *Methods and Applications of Interval Analysis* a vydání1979. |
| Kulisch–Miranker1981 | Metadata kapitol ve správné knize; nikoli přečtení celé knihy. |

Další primární autorské/vydavatelské stránky jsou v
`accuracy-history-web.json`: Dekker1971 (18,224–242), Brent1973
(C-22,601–607), Pascal-SC1987 a Highamovo první vydání1996.
Pascal-SC má všechny čtyři autory uvedené knihou a vydavatel
potvrzuje1987. V katalogu KIT se interně liší rok záznamu1989
 a údaj vydání Orlando1987; to není doklad chyby TAOCP.

Van Wijngaardenův původní článek BIT6(1966),66–81 je dostupný
[v institucionálním archivu CWI](https://ir.cwi.nl/pub/9206/9206D.pdf).
Přečtena §3, str.73–75: zavádí toleranci chyby a z ní vztahy
pro odlišnost, shodu a uspořádání. To podporuje Knuthovo mírné
srovnání podobných myšlenek, nikoli identitu definic obou textů.

Původní Reiser–Knuth1975 a Diamond1978 nebyly získány v plném
znění; metadata souhlasí, ale důkazy jsme provedli nezávisle
v `accuracy-drift.md` a `accuracy-diamond.md`. U Kahanových
nepublikovaných poznámek neověřujeme historickou prioritu.
Kahanova přílohaDiv754 byla naopak přímo přečtena a její rozsah
je uveden v poznámkách k iteracím.

Zbývající bibliografické odkazy (Fischer1958, Wilkinsonovy knihy,
Kahanův IFIP přehled, Ashenhurst–Metropolis1959/1963, Wadey1960,
Chartres1966, Moore1966, Kulisch1976/1977 a Hansen1968) byly
zahrnuty do kontroly textu a errat; jejich úplný obsah ani
všechny bibliografické údaje nejsou zde nezávisle potvrzeny.
Výroky o „první“ a „následující“ publikaci či osobním použití
roku1953 zůstávají historickými tvrzeními zdroje. Nová potvrzená
chyba z tohoto bloku je pouze C0090.

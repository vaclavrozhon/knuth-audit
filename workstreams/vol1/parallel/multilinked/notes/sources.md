# §2.4: přesně přečtené prameny a zbývající mezery

Četba dokončena v relaci auditu zahájené 1.11.2026. Nejde o fyzické
ověření prvního výtisku ani o úplný průzkum dějin všech kompilátorů.
Příslušné hashe a původ downloadů jsou v `../sources/downloads*.json`
a souhrnném `../sources/file-manifest.json`.

## Přímé knižní doklady

Originální obrazy 424–434 a 605–607 byly přečteny celé v rozsahu §2.4:
text, tabulky, oba diagramy B/C, zadání všech 15 úloh a všechny vytištěné
odpovědi. Odpověď 15 se v knize nenachází. Přesah 605 před nadpisem
SECTION 2.4 a přesah 607 od SECTION 2.5 není započten.
Pro křížový odkaz byl přímo přečten obraz 350, zejména (5) a definice
SCOPE nad ním. Čtyři vrstvy errat a jejich obrazy jsou vyjmenovány
v `errata.md`. Tyto technické křížové odkazy jsou uzavřeny.

## PL/I 1965: checked v uvedeném rozsahu

IBM, *Operating System/360 PL/I: Language Specifications*, C28-6571-1,
revize červenec 1965. Titul a tiráž přímo ověřeny z obrazů souborových
stran 1–2. Původní PDF:
<https://bitsavers.trailing-edge.com/pdf/ibm/360/pli/C28-6571-1_PL_I_Language_Specifications_Jul65.pdf>.
Lokálně `pli-1965.pdf`, OCR a obrazy `pli-1965-file*.png`.

Přečteny originály 25–27,39,63–64 (čísla tištěné strany a souboru jsou
zde stejná). Na 26 je výslovný příklad 1A,3B,2C se sourozenci B,C;
63–64 definují hranice struktury podle úrovní. Na 27 je kvalifikace
od vnějšího jména dovnitř s tečkami a možností vynechat mezilehlé skupiny.
Na 39 jsou pravidla opakovaných deklarací, přednost úplné kvalifikace a
příklad 1A,2A,3A. To přímo podpírá tvrzení úloh 3 a 6.

Neauditujeme celý PL/I manuál. Rozsahy bloků, pole a atributy zobrazené
na stejných stránkách nejsou zobecňovány na knižní model jednoho lesa.

## COBOL 1964: checked v uvedeném rozsahu

IBM, *Operating System/360 COBOL Language*, C28-6516-2, hlavní revize
prosinec 1964. Titul a datum/copyright přímo viděny na souborových
stranách 1 a 3. Původní PDF:
<https://bitsavers.trailing-edge.com/pdf/ibm/360/os/cobol/C28-6516-2_IBM_OS360_COBOL_Language_Dec64.pdf>.
Lokálně `cobol-1964.pdf`, OCR a obrazy `cobol-1964-file*.png`.

Přímo přečteny obrazy 14,32–33,85–86. Strana 14 popisuje OF/IN a
jednoznačnost kvalifikace, 32–33 skupiny a elementární položky,
85–86 párování MOVE CORRESPONDING podle jmen a všech mezilehlých
kvalifikátorů. Současně strana 86 vyžaduje skupinové kořenové operandy a omezuje
OCCURS/REDEFINES. Knižní definice na 430 a úloha 8 připouštějí elementární
kořen; úloha sama odkazuje výslovně na definici v textu. Nezaměňujeme
strukturální model s úplnou syntaxí tohoto IBM dialektu a z tohoto
rozdílu nevyvozujeme novou chybu algoritmu C.

Manuál má i další omezení kvalifikátorů. Kniha není označena za úplnou
specifikaci IBM 1964 ani dnešního COBOL; její jasně vyslovený matematický
kontrakt je ověřen samostatně. Přímý originál oficiálního COBOL-1961 se
zde nepodařilo získat: Google Books/Play poskytly katalog a veřejný
download nebyl dostupný. Archive.org hledání title:COBOL/year:1961 vrátilo
jen jiný IBM obecný manuál. Tento chybějící standard není vydáván za
přečtený. Novější 44 MB FIPS PDF nalezený při rešerši se ani nečetl.

## Conway 1963: checked v uvedeném rozsahu

Melvin E. Conway, *Design of a Separable Transition-Diagram Compiler*,
CACM 6(7),396–408, DOI 10.1145/366663.366704. Autorova kopie:
<https://melconway.com/Home/pdf/compiler.pdf>.
Lokálně `conway-1963.pdf/.txt`; přímo přečteny původní strany 402–404
(soubor 7–9), oddíl Data Structure Analysis včetně obrázků 11–13 a poznámky 3.

Na 403 je NAME/UP/NEXT, symbolová vstupní tabulka a přechod mezi úrovněmi
pomocí zásobníku. Na 404 jsou úplné diagramy konstrukce a kvalifikace;
poznámka pod obr.12 výslovně odkazuje na pravidlo COBOL VI-19 pro
nekonzistentní pokles čísel úrovní. NEXT spojuje stejnojmenné výskyty
dopředu, zatímco knižní PREV dozadu. Na 402 dodatek do korektury uvádí,
že autor se dozvěděl o Lawsonově podobné publikaci z 1962. Jde o dobový
doklad samostatného vývoje alespoň těchto dvou prací, nikoli o důkaz
šesti nezávislých objevitelů. Ostatní části 396–401 a 405–408 nebyly
systematicky auditovány.

## Lawson 1962: technický text čten, facsimile partial

Harold W. Lawson Jr., *The Use of Chain List Matrices for the Analysis
of COBOL Data Structures*, ACM National Conference Digest 1962,74–75,
DOI 10.1145/800198.806116. Veřejný autorův upload:
<https://www.researchgate.net/publication/255679649_Artificial_languages_The_use_of_chain_list_matrices_for_the_analysis_of_COBOL_data_structures>.

Přečten celý veřejně zobrazený OCR text obou stran, včetně definic sloupců,
popisu jednopřechodové konstrukce a analýzy velikostí, a OCR obrázků.
Stránka označuje vložení samotným autorem 6.12.2016; text obsahuje dataci
konferenčního sezení 6.9.1962 i patičku 74. J2 je index jména, J4 rodič,
J5 propojuje sourozence a J6 stejné názvy. To podporuje věcnou Lawsonovu
citaci; přidaný rozsah 74–75 souhlasí s položkou DOI a celým textem.

**Omezení:** původní obrazy tabulek/diagramů nebyly přímo přečteny.
ACM PDF i autorův správný RG PDF odkaz vracejí 403; webové tlačítko navíc
generuje chybnou cestu s `/publication/profile/` a vrací 404. Uložené
`lawson-1962.html` a `lawson-rg.html` jsou tyto chybové odpovědi,
nikoli článek. Technickou reprodukci každé buňky a celého původního
flowchartu proto označujeme partial. Z dostupného textu rovněž neplyne
globální prvenství oproti všem tehdejším publikacím.

## Lawsonova pozdější vzpomínka: partial

Autorova prezentace *Experiences and Reflections of a Computer and
Systems Engineering Pioneer*, soubor 42 stran:
<https://swedsoft.se/wp-content/uploads/sites/7/2016/03/Exp-ReflSeminar-copy.pdf>.
Vyhledávač/webový text zpřístupnil snímek 10: označuje práci z 1962
za první autorovu odbornou publikaci a první publikaci algoritmů pro
multilinked structures. Byla přečtena právě tato pasáž, nikoli všech
42 snímků. Přímé stažení a screenshot vracejí 404; lokální soubor
`lawson-author-slides.html` je chybová stránka. Tento retrospektivní
autorův výrok není náhradou za chybějící původní obraz ani úplný průzkum
priority.

## Konkrétní historické mezery

1. **Šest nezávislých objevitelů na 433:** dvě dobové práce výše podporují
   techniku a dílčí nezávislost. Jména a doklady dalších nejméně čtyř
   autorů nejsou v knize specifikována a nebyla nalezena. Stav partial.
2. **D. M. Dahm 1965 na 433 a v úloze 12:** techniku PREV/SCOPE jsme úplně
   dokázali, ale nebyla získána Dahmova publikace, datovaný rukopis ani
   korespondence dokazující tento rok a autorství. Hledání přesných jmen
   David/David Michael/D. M. Dahm s COBOL, scope a 1965 nepřineslo tento
   primární dokument. Obecné životopisné položky nejsou jeho náhradou.
3. **David S. Wise u odpovědi 4 a úlohy 15:** vlastní řešení jsou úplná,
   avšak nezávislý osobní příspěvek/korespondence uvedeného autora nebyly
   nalezeny. Knižní poděkování je přímou evidencí toho, koho Knuth
   uvádí, nikoli nezávislým ověřením historie. Stav atribuce partial.

Tyto mezery neoslabují technické důkazy. V UNIT_STATUS zůstávají kvůli
atribucím celkově partial úlohy 4,12,15 a historický odstavec hlavního
textu. Žádný nevyřešený algoritmický krok se pod tímto označením neskrývá.

# Prameny a meze čtení pro §1.4.1–1.4.2

Kontrola 1. 11. 2026. Jde o audit konkrétních tvrzení TAOCP, nikoli
o audit všech citovaných prací. Metadata stažených souborů, URL a
SHA-256 jsou v `../sources/external-metadata.json` a
`../sources/manuals-metadata.json`. Stažení souboru neznamená přečtení
celého díla. Omezení přístupu jsou uvedena níže, nikoli zaměněna za
negativní důkaz.

## Odkazy hlavního textu §1.4.1

- Wirth, *Program Development by Stepwise Refinement*, CACM 14 (1971),
  221–227. Přečten titul a úvod na 221–222 a závěry na 226–227 v kopii
  původního článku (`wirth1971.pdf`). Bibliografické údaje jsou přímo
  v patičkách původních stran. Rozklad úlohy do postupně zpřesňovaných
  podúloh a možnost návratu k dřívějším návrhovým rozhodnutím odpovídají
  charakteristice na s. 191. Výpočet osmi dam uprostřed článku se zde
  nereviduje.
  [Kopie článku](https://webarchive.di.uminho.pt/wiki.di.uminho.pt/twiki/pub/Education/ClubeProgramacao/Literatura/p221-wirth.pdf).
- Dijkstra, *Notes on Structured Programming*, EWD249. Přečten titul,
  obsah a začátek části *A first example of step-wise program
  composition* od úvodu přes description 1 a následující diskusi
  reprezentace tabulky. Primární archiv autora uvádí rok 1969 a druhé
  vydání zprávy 1970. Zpráva podporuje obsahový odkaz na postupné
  zpřesňování. Veřejný náhled knihy potvrzuje Notes jako část I, ale
  celé znění jejího přetisku v knize Academic Press 1972 nebylo
  porovnáno řádek po řádku se zprávou. Technický závěr je založen na
  autorské zprávě, nikoli na katalogu.
  [Archiv EWD249](https://www.cs.utexas.edu/~EWD/transcriptions/EWD02xx/EWD249/EWD249.html).
- Knuth, *Literate Programming*. Přečtena autorova stránka: rok 1992,
  popis metodiky, obsah a kapitola 11 věnovaná chybovému deníku.
  V online přepisu knihy byla přečtena tiráž a předmluva ix–xii;
  předmluva charakterizuje kapitolu 11 jako úplný seznam více než
  tisíce změn za více než čtrnáct let. V cíleném výsledku vyhledávání
  z téhož přepisu je přímo čitelné záhlaví kapitoly 11 s rozmezím
  1978–1991 a její úvod uvádějící rozšíření deníku do září 1991.
  To podporuje obsah a časový rozsah odkazu na s. 193. Celý deník ani
  jednotlivé jeho chyby se zde nerevidují. Pozdější přímé stažení
  stejné URL vrátilo jen 25 bajtů „website under maintenance“ a nové
  otevření nástrojem skončilo timeoutem. Místní soubor
  `literate-programming-transcript.html` je tedy záznam neúspěšného
  stažení, **nikoli kopie knihy**. Bibliografická poznámka v
  autorově rozhovoru z roku 1996, dostupná pouze jako vyhledaný
  výňatek, jmenuje CSLI i Cambridge University Press; vlastní PDF
  rozhovoru vracelo HTTP 403. Rozdíl mezi vydavatelem a distributorem
  proto není označen za nový nález, ale celé PDF rozhovoru není
  vydáváno za přečtené.
  [Autorova stránka](https://cs.stanford.edu/~knuth/lp.html),
  [přepis knihy](https://dokumen.pub/literate-programming-1.html),
  [rozhovor](https://www.tug.org/TUGboat/tb17-4/tb53knuc.pdf).
- Turingova citace o nedostatcích návrhu byla porovnána s původním
  strojopisem *Proposed Electronic Calculator*, tištěná s. 18,
  odstavec (6), souborová strana PDF 19. Soubor `turing-ace.pdf` byl
  stažen přímo od NPL; originál byl zobrazen jako
  `../images/turing-ace-pdf19.png`. Přečteny odstavce (4)–(6) včetně
  kontextu citace. Výrok odpovídá originálu; vysvětlení `[bugs]` v
  TAOCP je redakční vložka. Datace nedatovaného strojopisu nebyla
  archivně nově určena: Turingův archiv jej řadí pod rok 1945, zatímco
  historická stránka NPL popisuje návrh jako 1946. Rozlišení vzniku
  návrhu a institucionálního předložení zde není novým nálezem.
  Předchozí pokus stáhnout náhled z Wikimedia skončil HTTP 403;
  podkladem vizuálního porovnání je úspěšně získaný originál od NPL.
  [NPL originál](https://www.npl.co.uk/getattachment/ea5c6585-0929-4713-962c-2306f8dcf1f2/turing-proposal-Alan-LR.pdf?lang=en-US),
  [archivní soupis](https://www.alanturing.net/turing_archive/archive/index/aceindex.html).

## Vnitřní a dobové odkazy v obou oddílech

Program 1.3.2M na s. 145 byl zobrazen a jeho skutečný kód použit při
reprodukci rozporu v odpovědi 1.4.1-3. Odkazy na §1.4.3.1,
§1.4.3.2-7, §1.4.4 a §2.2.5 určují další místa ve svazku; v této
dávce se nepředstírá opakovaný audit celých odkazovaných oddílů.
Odkazy na kapitoly 8 a 10 jsou součást autorského plánu z roku 1997,
nikoli tvrzení o dnešním stavu vydávání. Budoucí náhrada MIX strojem
MMIX na s. 187 je také dobový autorský plán; kontrolovaným technickým
bodem je rozdíl mezi uložením návratu v datech/registrech a přepisem
instrukce. Tyto odkazy samy o sobě nevytvářejí nově zkontrolované
jednotky mimo přidělené §1.4.1–1.4.2.

## Primární manuály k odpovědi §1.4.2-4

Manuály jsou původní dokumentace výrobce uchovaná na Bitsavers.
Přečteny byly konkrétní definice použitých instrukcí. Navigační
náhledy okolních stran se nepovažují za audit celého manuálu.
Obecný důkaz vazeb je v `coroutines.md`, část cvičení 4.

- IBM 650, *Basic Operation Codes*, 24-5002-0: původní s. 10,
  definice STD, a s. 16, definice LDD a NOP. Souborové strany mají
  stejné číslo. STD ukládá celé slovo distributoru včetně znaménka;
  LDD načte slovo z datové adresy a instrukční adresa určuje další
  instrukci. Obrázky `ibm650-basic-pdf10.png` a `-pdf16.png`.
  [Manuál IBM 650](https://bitsavers.trailing-edge.com/pdf/ibm/650/24-5002-0_BasicOpcodes.pdf).
- IBM 650, *SOAP II*, 24-4000-0 (1957): obsah, úvod a původní s. 5
  (PDF 8), zejména pravidlo prázdné datové nebo instrukční adresy.
  Prázdné pole znamená adresu následující zdrojové instrukce,
  doplněnou assemblerem; tento význam prázdného pole je pro knižní
  zápis LDD zásadní. Obraz `ibm650-soap2-pdf8.png`.
  [Manuál SOAP II](https://bitsavers.trailing-edge.com/pdf/ibm/650/24-4000-0_SOAPII.pdf).
- IBM 709, *Reference Manual*, v dostupném složeném PDF: přečteny
  konvence instrukcí na s. 24 (PDF 2), TRA na 42 (PDF 20), TSX
  na 45 (PDF 23), AXT na 51 (PDF 29) a SXA na 52 (PDF 30).
  Definice TSX výslovně uvádí dvojkový doplněk instrukčního čítače
  a vztah mezi odečtením doplňku a přičtením původní adresy.
  Obrázky `ibm709-pdf2.png`, `-pdf20.png`, `-pdf23.png`,
  `-pdf29.png` a `-pdf30.png`.
  [Manuál IBM 709](https://bitsavers.trailing-edge.com/pdf/ibm/709/709_RefMan_Fortran.pdf).
- CDC 1604, Publication 031a, rev. 12/1960: původní s. 1-12
  (PDF 18), definice ALS, a 1-31 (PDF 37), definice SLJ včetně
  bezpodmínečného normálního skoku s j=0 a return-jump s j=4.
  Obě původní strany byly zobrazeny. ALS 0 je posun o nula bitů.
  [Popis a obsluha CDC 1604](https://bitsavers.trailing-edge.com/pdf/cdc/1604/031a_1604_Computer_Vol_1_Description_and_Operation_196012.pdf).
- CDC 1604, Publication 032a, rev. 11/1960: přečteno a zobrazeno
  s. 2-80 až 2-82 (PDF 128–130), normální a návratový skok,
  čtyři kroky return-jump a tabulka 2-11. Jde o přímý primární
  podklad pro přepsání horní instrukce, spuštění dolní instrukce
  a pokračování volajícího na dalším celém slově. Obrázky
  `cdc1604-principles-pdf128.png` až `-pdf130.png`.
  [Principy činnosti CDC 1604](https://bitsavers.trailing-edge.com/pdf/cdc/1604/032a_1604_Computer_Vol_2_Principles_of_Operation_196011.pdf).
- CDC 1604A, Publication 245a (5/1963): pomocné textové ověření
  definice return-jump na s. 2-29 a SLJ na 2-31. Pro závěr o
  původním CDC 1604 není nutné přenášet sémantiku z modelu 1604A:
  přímý zdroj 032a byl dodatečně získán a ověřen výše.
  [Manuál CDC 1604A](https://bitsavers.trailing-edge.com/pdf/cdc/1604/245a_1604A_Reference_Manual_196305.pdf).

Žádný z historických strojů nebyl emulován a nebyla testována latence
jeho fyzického úložiště. Pro kontrolované vazby stačí výslovná sémantika
uvedených instrukcí a obecný důkaz zachování pokračování. Technické
závěry o MIX jsou doloženy zvlášť původním programem, invarianty a
společným již validovaným modelem.

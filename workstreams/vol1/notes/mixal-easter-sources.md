# Prameny k velikonočním úlohám §1.3.2-14–15

Kontrola1.listopadu2026; originál s.518 byl znovu zobrazen. Technické
výsledky a obecné důkazy jsou v `mixal-easter.md`. Následující záznam
rozlišuje přečtený obsah od pouhého ověření bibliografie.

## Doložená historická oprava V1-C0025

Tvrzení o jediné netriviální středověké aplikaci aritmetiky je příliš
široké. Fibonacci, *Liber abaci*, kap.12, řeší složené úročení
100·(5/4)^18 pomocí opakovaného čtvercování. Konkrétní pasáž je
v Siglerově překladu na s.439, s odkazem na Boncompagniho s.313.
To je přímý protipříklad, který nevyžaduje odhad rozšířenosti obchodní
matematiky. Knihu lze opravit změnou výlučnosti na významnou aplikaci.

[Springer](https://link.springer.com/book/10.1007/978-1-4613-0079-3)
potvrzuje překlad, autora a rok2002. Lokální soubor je25stránkový
výbor s novodobými učitelskými poznámkami, nikoli celý překlad;
pro důkaz se používá samotný přeložený historický text. Zobrazeny
file6 (dedikace/prolog, tištěná s.15) a file22 (s.438–439).
Textově dále přečteny vybrané obchodní příklady s.127–130,159,
a příklad soustav na s.405. Nespoléháme na správnost každé číslice
OCR ani na chybný mezivýsledek5^9 v překladu; pro protipříklad
stačí explicitně vyložený postup umocňování při složeném úročení.

Všechny čtyři vrstvy errat neobsahují nalezenou opravu této věty;
seznam sousedních errat je v technické poznámce. C0025 je potvrzená
historická formulace, nikoli chyba velikonočního algoritmu.

## Prvenství Victoriova algoritmu: V1-C0026 zatím candidate

Přímý starověký pramen Eusebios, *Historia ecclesiastica* VI.22.1,
uvádí Hippolytův šestnáctiletý velikonoční kánon a chronologickou
tabulku. [Překlad McGifferta](https://www.newadvent.org/fathers/250106.htm)
byl přečten ve vymezeném odstavci. To je podstatná námitka proti
formulaci „first systematic algorithm“ pro Victoriův kánon457.
Zde však zatím není zrekonstruována úplná starší procedura ani
přesně rozlišena případná užší definice „systematic“. Proto nejde
o potvrzený druhý nález a neprohlašujeme Hippolyta za prvního autora.

Daniel McCarthy a Dáibhí Ó Cróinín, *The 'Lost' Irish84-Year Easter
Table Rediscovered*, Peritia6–7(1987–88),227–242, byl získán z
[MGH knihovny](https://www.mgh-bibliothek.de/dokumente/a/a149668.pdf).
Čteny s.227,230,233–234,237: rekonstrukce84letého cyklu, pravidla
z epakt a odvození počátečního roku438. Samotný první rok tabulky
není automaticky datem jejího sepsání. Tento článek tedy používáme
jako konkrétní cestu k dalšímu ověření, ne jako samostatný důkaz
prvenství. Úplný algoritmus i všechny opravy rukopisu neauditovány.
Novější McCarthyho2022 článek přes TARA vrátil403; text nečten.

## Ostatní citace a meze ověření

- Knuth, *The calculation of Easter?*, CACM5(1962),209–210,
  DOI10.1145/366920.366980; Williams, *Certification of the calculation
  of Easter…*, CACM5(1962),556, DOI10.1145/368996.369018.
  Bibliografie potvrzena v registraci vydavatele přes Crossref.
  Plný původní text ACM není získán (403). Naše důkazy první chyby
  a algoritmu na těchto nečtených textech nezávisí; algoritmus pro
  roky<=1582 z prvního článku ještě není ověřen.
- Veřejný archiv Computer History Museum obsahuje I.D.Hillův
  algoritmus a certifikace s odkazem na oba články1962. Přečten
  výřez původních file68–69; není to hledaný text Williamsův.
  Lokálně uložen jen tento výřez, hash plného staženého archivu
  ponechán v metadatech. Nelze jej zaměnit za důkaz Knuthovy citace.
- O'Beirne, *Puzzles and Paradoxes*, OUP1965: katalogový záznam
  potvrzuje bibliografii; obsah reprintu má kap.10 „Ten Divisions
  Lead to Easter“, s.168–184. Kapitola sama zatím nebyla přečtena.
  [Původní vydání](https://books.google.com/books/about/Puzzles_and_paradoxes.html?id=07w-AAAAIAAJ),
  [obsah reprintu](https://books.google.com/books?id=P-gvDwAAQBAJ).
  Připsání výsledků O'Beirneovi/Robertu Hillovi není nezávisle
  doloženo dobovým osobním pramenem. Matematika výsledků je dokázána.
- Reingoldova [autorská stránka](https://www.reingold.co/calendars.shtml)
  potvrzuje *Calendrical Calculations: The Millennium Edition*,2001,
  a algoritmický rozsah knihy. Starší článek1990 byl skutečně čten
  v rozsahu zaznamenaném v jeho metadatech a použit pro nezávislý
  algoritmus; neoznačujeme jej za druhé vydání knihy.
- Neri–Schneider: [vydavatel Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1002/spe.3172)
  potvrzuje SPE53(4),937–970, první online vydání3.prosince2022
  a svazkový rok2023. Přečten abstrakt a úvod preprintu2021, dále
  jeho s.20 o kalendářních převodech. Reference opravdu pojednává
  o optimalizaci těchto výpočtů; není to příslib globálně nejrychlejšího
  programu EASTER. Úplné důkazy článku ani všechny benchmarky se zde
  znovu neauditovaly. Crossref při doplňkovém pokusu vrátil429;
  bibliografie je doložena přímo vydavatelem.

Všechny otevřené meze zůstávají v X0173; úloha14 je proto partial.
Technický obsah úlohy15 je checked, s výše uvedenou explicitní mezí
historické atribuce. Žádný dopis nebyl odeslán.

# V4A-F0001 — stažení libovolné hrany triangulace

**Confirmed: chybný mezikrok důkazu, nikoli chybný vzorec e=3n−6.**
6. listopadu2026; TAOCP4A,1.vydání/1.dotisk2011. Zadání §7–46(b) na39/file56,
odpověď na521/file538. Původní sazba odpovědi je
[obraz](../images/proof-file538.png); zadání [file56](../images/file056.png).

Odpověď pro n>3 přikazuje stáhnout libovolnou hranu a tvrdí, že tím zmizí
jeden vrchol a právě tři hrany. Následuje popis odstranění hrany uv a jedné
hrany z každé z dvojic incidentních trojúhelníků. To obecně nezanechá
jednoduchý maximální rovinný graf s o3 méně hranami.

## Přímý protipříklad

Vezmi vrcholy a,b,c,d,e a hrany

    ab,bc,ca,ad,bd,cd,ae,be,ce.

Jde o trojboký dvojjehlan: trojúhelník abc, d uvnitř a e vně, oba vrcholy
spojeny se všemi a,b,c. Má rovinné vložení se šesti stěnami
abd,bcd,cad,abe,bce,cae. Diagram je maximální: jedinou chybějící hranu de
nelze přidat bez protnutí uzavřené křivky abc. Splňuje tedy zadání a má
n5,e9. Hrana ab má **tři společné sousedy c,d,e**, nikoli pouze dva.

Po stažení a,b do z má odpovídající jednoduchý graf právě hrany

    zc,zd,ze,cd,ce.

Má4 vrcholy a5 hran; z původních9 tedy zmizely **4 hrany**. Vzniklé dvojice
ac/bc,ad/bd,ae/be všechny splývají a navíc zmizí ab. Není ani maximální,
protože de lze nyní doplnit. Pokud knižní instrukci čteme doslova jako
odstranění pouze uv a dvou hran incidentních stěn, zůstane místo toho
šestihranový multigraf s paralelními hranami zc; pro indukci o jednoduchých
maximálních rovinných grafech je také nepřípustný.

To je konečný explicitní protipříklad bez výpočtu či hledání. Příčina je
separující trojúhelník abc: hrana může mít vedle dvou incidentních stěn
dalšího společného souseda. Pro n>3 nestačí příkaz „libovolná hrana“.

Samotný požadovaný vzorec je správný. Korektní krátký důkaz použije Eulerův
vztah n−e+f=2 a trojúhelníkové stěny3f=2e. Alternativně by indukce musela
oprávněně zvolit kontrahovatelnou hranu a doložit zachování třídy grafů.
Tato poznámka neprohlašuje existenci takové vhodné hrany za automatický
důsledek vytištěného kroku.

## Errata a rozsah

Prohledány relevantní uložené vrstvy:
`errata/text/all4a-pre.txt`, `all4a.txt`, `err4a.txt`, `all4f0.txt`, `err4f0.txt`.
Hledány strany, answer46, shrink/contract/triang a související znění.
Starší fasciklová odpověď má offset−380:4A521 odpovídáF0 141, což potvrzuje
stejná okolní úloha43 (F0 oprava girth4→3) a odpověď7 (515↔135).
U141 není oprava46. Na521 jsou známé opravy sousedních odpovědí47
(historická citace2020/2022) a49 (doplněk2015), nikoli kontrakčního kroku46.
Relevantní oprava tohoto mezikroku nebyla nalezena. Původní soubory errat
ani knihy nebyly měněny; fyzický výtisk nebyl ověřen.

Závažnost medium: důkaz používá nepravdivé obecné tvrzení a indukční krok
může opustit předpoklady. Nedokládá to chybu samotného standardního vzorce.

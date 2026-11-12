# V1-X0788 a C0026: starší velikonoční tabulkové postupy

Po přímé kontrole nových pramenů mění root C0026 z candidate
na confirmed pro příliš široké historické prvenství na518.
Závěr zahrnuje tabulkový kánon mezi systematické konečné postupy,
stejně jako u Victoriova vlastního kánonu. Nejde o chybu MIXového
programu, nové určení prvního autora ani tvrzení o pozdějším
fyzickém dotisku.

## Co nyní přibylo

Dříve jsme měli především Eusebiovu zprávu o šestnáctiletém
kánonu. Nyní jsou přímo dostupné tabulky, návod jejich použití
a Victoriovo vlastní srovnání starších postupů. To uzavírá
hlavní důvod původní opatrné klasifikace; neurčený odstín slova
*systematic* zachováváme v přesném popisu nálezu.

Paschální kánon zde znamená tabulku a pravidla pro velikonoční
datum podle určitého církevního měsíčního modelu. Měsíční model
nemusí být astronomicky přesný. Citovaná věta knihy neomezuje
prvenství na konkrétní 532letý západní cyklus nebo na novověké
gregoriánské pravidlo.

Root přímo zobrazil původní518, titul PG10 z1857, sloupce571–572
a875–884 (PDF294,446–450). Přečetl latinský překlad Eusebiova
VI.22, odpovídající Jeronýmovo paschální svědectví, nápis i
uspořádání obou tabulek; řecké číselné příklady porovnal s latinským
převodem. Neprohlašuje novou filologickou kolaci řeckých rukopisů.

Tabulka velikonočních nedělí na879–880 má sedm šestnáctiletých
sloupců. Je odlišná od vedlejší tabulky čtrnáctého dne Měsíce.
Její návod odkazuje na první rok císaře Alexandra a na čtení
dalších let podle tabulky. Ručně ověřené přechody prvního sloupce
a začátku druhého souhlasí s agentovým přepisem: XI Kal. Maii,
VIII Idus Apr., IV Non. Apr., XVII Kal. Maii. Při inkluzivním
římském počítání jde o21.dubna,6.dubna,2.dubna a15.dubna.
Poškozený znak v šestém sloupci je v edici výslovně přiznán;
netvrdíme úplnou novou rekonstrukci všech112 údajů.

Tabulku označme T[c,r], kde c je sloupec1,...,7 a r řádek1,...,16.
Její cyklické čtení lze v dnešním zápisu provést zbytkem t po
dělení počtu let od epochy číslem112 a výběrem
`T[1+floor(t/16),1+(t mod 16)]`. Každý vstup vyžaduje konečné
dělení a vyhledání; úplná pevná tabulka dává výstup. Tento zápis
je naše vysvětlení postupu, nikoli údajně dochovaný antický program.
Datace se neopírá pouze o počáteční rok tabulky: existence staršího
kánonu je doložena i předvictoriovským Eusebiovým svědectvím.

## Victoriova vlastní kontrola

Root přímo přečetl Mommsen1892, MGH Auctores antiquissimi9,
hlavní text §§3–4 na678–679 a §§10–12 na683–684; zobrazil také
titul edice a oddílový titul667 s datací457. Agent četl celý
hlavní list677–684; root toto širší čtení nepředstírá jako vlastní.

Victorius sám rozlišuje předchozí84-,95- a112leté cykly a jejich
návrat k počátku. Na679 uvádí u112letého cyklu šestnáctiletou
měsíční opravu. Na683–684 popisuje vlastní532letou tabulku a její
opakování. U některých alternativních dat výslovně ponechává
volbu církevní autoritě. Nelze tedy bez dalšího vyřadit starší
tabulkové výpočty jen proto, že nebyly astronomicky přesné nebo
jednotně závazné: kniha takové kritérium neuvádí a nepoužívá je
ani při označení Victoriova řešení.

Přepis nápisu a starověká svědectví jsou hlavní evidencí. Pozdější
Bucheriova rekonstrukce ani moderní Schmidtův výklad nejsou
vydávány za antický originál. Identita autora tradičně nazývaného
Hippolytos a identita restaurované sochy zůstávají oddělené otázky;
potřebujeme existenci dřívějšího postupu, nikoli jejich rozhodnutí.

## Errata a zbývající mezery

Root přímo porovnal všechny čtyři rozhodné erratové obrazy:
all1-prepre37, all1-pre16, all1/14 a err1/12. Texty celých vrstev
jsou prohledány podle stránek, jmen a tématu. Známá oprava
Aquitania na Aquitaine z2014 řeší jméno země, nikoli prvenství.
Ani další kalendářní dodatky toto prvenství neopravují.

Minimální návrh vypouští absolutní first a označuje Victoriův
kánon za významný raný příklad. Přesnější samostatné prvenství
konkrétního typu532letého cyklu zde netvrdíme. Anglický ASCII
návrh je v `reports/V1-C0026.txt`; nic nebylo odesláno.

Nový pramenný blok je checked jen v popsaném rozsahu. X0173
zůstává partial pro celé moderní Knuth/Williams1962,
O’Beirne1965 a osobní atribuce. Root přímo zobrazil nově nalezený
výřez Knuthova úvodu v pozdějším výkladu naPDF9: skutečně obsahuje
jen titulek, autora a úvod, nikoli oba programy. Z něj nelze
potvrdit větev pro roky do1582. I.D.Hillův program není dokladem
atribuce Robertu Hillovi. Technické důkazy a úspěšné testy X0172
se nezměnily a nebyly znovu prováděny.

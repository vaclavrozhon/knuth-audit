# Anacrostic, 7.2.2–73–74

Kontrola 1. listopadu 2026, zadání str.62 a odpovědi str.413.
Matematický výčet nad zveřejněnými autorovými slovníky souhlasí:
720 řešení, faktor 3×240, právě 43 počátečních dvojic xy, v řešení jen ar.
Neuzavřená část 73: nezávislé ověření přesných frekvencí BNC 2007,
historický pramen k vynálezu 1933 a původní článek Golomb–Baumert 1965.

## Data a dva řešiče

Všech 145 očíslovaných polí bylo vyčteno z poloh znaků v původním PDF,
nikoli z řádkového OCR. Každé číslo 1,...,145 se vyskytuje právě jednou.
29 dodaných klíčových slov je v prvních 1000 slovech GraphBase;
jejich iniciály dávají `solomonwgolombleonarddbaumert`. Dosazení reprodukuje
celý citát v odpovědi, po ignorování velikosti písmen a interpunkce.

Domény citátových slov vznikly jako prefixy veřejných Knuthových
`wordsN-from-OSPD4`, které jsou řazeny podle frekvence. Délky prefixů
jsou knižní čísla 85, 562, 1863, 3199, 4650, 5631, 5417, 4724, 3657, 2448.
Tato konstrukce nezávisle ověřuje následující kombinační tvrzení; sama
neověřuje, zda tyto délky přesně odpovídají prahu 32 výskytů v BNC.

První řešič používá bitové množiny domén a konzistenci dvojic tabulek
přes všechny jejich společné pozice. Úplný backtracking má 4132 uzlů.
Druhý řešič kóduje každé slovo a písmeno do SAT (CaDiCaL), vypisuje
modely do závěrečného UNSAT a porovnává přesné množiny. První SAT běh
používá pouze počáteční redukci konzistencí: 86 795 proměnných,
362 457 klauzulí, celkový čas obou metod 689 s. Obě metody daly stejné
množiny a všech 720 modelů prošlo doslovnou kontrolou 145 rovností.

Nad rámec této kontroly byl spuštěn SAT nad všemi 92 269 původními
slovními alternativami, bez sdílené počáteční redukce. Jeho samostatný
stav je `results/anacrostic/full-sat-run.json`; dokud není `pass`,
nepočítá se za dokončené další ověření. První běh má úplné výsledné
soubory se stavem pass, ale pozdější vyzvednutí terminálové relace
vrátilo 143; příčinu této obálkové anomálie netvrdíme známou. Uložené
modely byly znovu samostatně validovány.

## Faktorizace

V 27. klíčovém slově cxyab tvoří písmena c,a,b pouze citátové slovo abc;
jen x,y se vážou na zbytek hádanky. Proto lze vnější problém řešit
pouze přes dvojice xy a nakonec doplnit kompatibilní trojici c,a,b.
Ze slovníků vychází 43 dvojic (první ab, ag, poslední ve). Ve všech
řešeních je xy=ar. Tři možnosti jsou earth/the, harsh/shh, large/gel.
Po odstranění těchto dvou slov vznikne přesně 240 různých vnějších
řešení; každé má všechny tři doplňky. To přímo ověřuje součin 3×240,
nikoli jen rozdělení celkového počtu do stejně velkých skupin.

Analogické samovazby mají 137/139, 118/119, 46/48 a 32/35:
oba znaky patří témuž klíčovému slovu. Redukce domény podle příslušného
dvoupísmenného slova je tedy oprávněná, ale odpojí méně vnitřních znaků.
Všechna řešení se od pravého citátu liší pouze ve slovech délky nejvýše 5;
strojový citát vytištěný v odpovědi je mezi nimi.

## BNC a prameny

Stažený Kilgarriffův seznam není požadovaná verze korpusu. Jeho součty
přes slovní druhy dávají the=6187927, of=2941790, al=1357; kniha má
5405633, 3021525, 3515. Toto není evidováno jako chyba knihy.
[Oficiální stránka BNC](https://www.natcorp.ox.ac.uk/using/index.xml?ID=freq)
výslovně upozorňuje, že odkazované frekvenční seznamy patří staršímu
BNC World. Oficiální přístup k XML 2007 přes OTA zde skončil odmítnutím
Anubis; přístupová ochrana se neobcházela.

Původní [Spiegelthalův článek, EJCC 18 (1960), 39–56](https://bitsavers.computerhistory.org/pdf/afips/1960-12_%2318.pdf)
je uložen z veřejného mirroru Bitsavers. Str.39 potvrzuje IBM 704.
Str.42 výslovně popisuje procházení stromu s návraty jako nepoužitou
alternativu; jeho vlastní program vybírá a maže hypotézy heuristicky.
Knižní charakteristika „bez backtrackingu“ tedy souhlasí. Podstatný
text na stranách 39–46 přečten, str.42 zobrazená i jako původní sken.

Původní Golombův a Baumertův článek JACM 12(4), 516–524, DOI
10.1145/321296.321300 zatím není dostupný v plném primárním zdroji.
Dosazení citátu je ověřeno, jeho přesná shoda s prvním vydáním článku
zůstává otevřená. Podobně nerozhodujeme letopočet vynálezu jen podle
data první publikované hádanky 1934.

Známé erratum Fascicle 5 p.221 z 12. prosince 2019 opravuje roots na
roofs. Náš druhý dotisk 4B má už správné roofs; nový nález to není.

## Dodatečný nezávislý SAT dokončen

Dne 1. listopadu 2026 v 11:49 UTC doběhl SAT nad všemi původními doménami, bez sdíleného počátečního CSP prořezání. Po 5279 sekundách dal přesně stejných 720 řešení; všechna jsou doslovně validovaná. Model měl 191875 proměnných a 901001 klauzulí. Úplná množina řešení souhlasí, nejen počet; SHA-256 je `06c2836e32b22bd27441dda8494a77c718db882d0f7be1f0aff44778c0278800`. [Metadata](results/anacrostic/full-sat-run.json) a [program](check_anacrostic_full_sat.py). Historické a korpusové mezery uvedené výše tím nejsou uzavřeny.

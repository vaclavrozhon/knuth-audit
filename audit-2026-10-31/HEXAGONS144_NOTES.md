# DLX 144 — smíšené vrcholové a hranové skládání

Kontrola 3. listopadu 2026: zadání 4B str. 142 (PDF 162), odpověď str. 455
(PDF 475), autorův draft 2019 str. 78/159 (PDF 84/165).
**Průchod je uzavřen v rozsahu upraveném uživatelem:** není nutné reprodukovat
každý údaj dlouhým brute force. Níže jsou oddělené ověřené části a vynechané
výpočty. Žádná nová chyba v této úloze nebyla doložena.

## Dílky, model a původní obrázky

Při čtyřech barvách je počet rotačních typů tříbarevných trojúhelníků
`(4³ + 2·4)/3 = 24` podle lemmatu o počtu orbit. Z toho jsou čtyři
jednobarevné typy, dvanáct dvoubarevných a osm se třemi barvami.
Zrcadlové typy se neztotožňují. Každé pojmenované řešení používá všechny
čtyři barvy, takže volné globální přejmenování barev má přesně 24 prvků.

Deska má 24 jednotkových trojúhelníků, 19 vrcholů, 42 hran, z toho 30
vnitřních. Na každé straně trojúhelníku sledujeme dvě poloviny, rozlišené
koncovým bodem. Dílku typu E patří na obou polovinách stejná barva hrany;
u V patří polovinám barvy obou koncových vrcholů. Toto je přesný model
kontaktu vytištěných šestiúhelníků. Model XCC má 48 primárních položek,
84 sekundárních půlhran a 1536 možností. Nezávislá kontrakce shodných
barevných sektorů dává 35 proměnných pro (i), 28 pro (ii).

Z původních vektorů PDF bylo přečteno všech **144 barevných sektorů,
48 dílků a 48 žlutých značek**. Dílky byly geometricky přiřazeny k desce;
orientace barevných sektorů i značek souhlasí. Každý obrázek používá
všech 24 typů právě jednou. V (i) je V právě pět spodních dílků,
v (ii) ještě pět vlevo nahoře. Oba obrázky se přesně shodují s autorovým
draftem. Černá v převedeném PostScriptu má hodnotu 0.199951 místo 0.2;
jde o numerické zaokrouhlení barvy, nikoli obsahovou odchylku.

Samostatná geometrická kontrola porovnala skutečné shodné úsečky
vnějších obvodů dílků: pro každý obrázek 288 polovičních úseček,
60 shodných dvojic na 30 kontaktech. Všechny barvy souhlasí a kontakty
jsou právě ty, které používá trojúhelníkový model. Nejde tedy jen
o shodu obrázku s předem předpokládaným číslováním buněk.

Při přípravě extraktoru byly opraveny dvě kontrolou zachycené drobnosti:
horní levý pruh je otočení spodního o 240°, nikoli o 120°, a draft má
zmíněné zaokrouhlení černé. Původní diagnostické logy zůstávají archivované.
Tyto změny předcházely všem výčtům; starší důkazní programy se neměnily.

## Krátký úplný výčet (ii)

Nezávislý program pracuje přímo s barvami kontrahovaných sektorů a
s nepoužitými rotačními typy, bez matice nebo odkazů DLX. Větví nejvíce
omezenou buňku. Jedna možnost přiřadí její dosud neznámé barvy a vyřadí
použitý typ. Každé úplné přípustné přiřazení určuje právě jednu větev.
Pořadí voleb buněk je invariantní vůči přejmenování barev; zavádění
barev v pořadí prvního použití proto ponechá právě jednoho zástupce
každé barevné orbity. Opakované proměnné v jedné buňce jsou respektovány.

Na 16 všech kombinacích E/V pro čtyři malé buňky byly porovnány **celé
množiny** s doslovným výčtem nejvýše 4096 přiřazení a s původním DLX2.
Dvě jednobuněčné kontroly navíc pokrývají všechny čtyři barvy.
Tyto testy prověřují model i redukci; nejsou náhradou úplného běhu (ii).

Úplný běh (ii) skončil s **204 barevnými třídami a 23 674 uzly**, za
0.025 s měřeného času. Všech 204 výsledků bylo přímo ověřeno podle hran
a celé inventury dílků. Vytištěný příklad je mezi nimi. Jediná netriviální
symetrie předepsaného vzoru je zrcadlení; všech 204 výsledků se rozpadá
na **102 dvojic**, bez pevné barevné třídy. Tedy knižních `2·102` souhlasí.

Původní DLX2 bez redukce přejmenování barev dostal limit **60 s** a skončil
návratovým kódem **124**. Je to **nedokončený výčet**. Všech 2948 celých
vypsaných modelů je platných a pokrývá všech 204 tříd úplného prvního
výčtu. To nedokazuje, že druhý program dokončil svůj strom nebo našel
všech 4896 pojmenovaných modelů. Limit se neprodlužoval a hledání se
neopakovala. I kompilace, krátké výčty a následné validátory běžely s nice 15.

## Přechody režimů a otázka v závorce

Na styku E/V musí platit `e=a=b`: jedna hranová barva se rovná oběma
vrcholovým barvám. „Solid color“ se zde týká kontaktu, nemusí znamenat
jednobarevný celý dílek. Když má V buňka alespoň dva E sousedy, dvě
různé rovnosti již vynutí všechny její tři barvy stejné. Jelikož máme
jen čtyři jednobarevné dílky, pět takových různých buněk je překážka.

Konkrétní nemožný režim: všechny trojúhelníky mířící vzhůru jsou V,
všechny mířící dolů E. Každá z dvanácti V buněk má alespoň dva E sousedy;
potřebovali bychom dvanáct jednobarevných dílků. To je krátký důkaz
nemožnosti bez prohledávání.

Pro 24 pevných míst jsou dvě nezávislé volby režimu, tedy přesně `2²⁴`
specifikací. Úplnou klasifikaci realizovatelných specifikací neděláme.
Knižní „very few“ není číselně vymezené a nezávisle jsme nepřepočítali
jejich podíl. Závěrečnou otázku evidujeme jako autorovu výzkumnou otázku,
nikoli jako tvrzení, že její řešení není nikde na světě známé. Omezené
webové hledání našlo autorův draft na dvou zrcadlech, nikoli nezávislou
úplnou klasifikaci; to není důkaz její neexistence.

## Výslovně nereplikováno

- (i): `2·37586004 = 75 172 008` barevných tříd. Oba původní texty se shodují,
  vytištěné řešení je platné. Celý počet ani rozpad všech řešení (i) do
  zrcadlových dvojic nebyl přepočítán.
- Historických **643 teramemů** pro (i): neprováděl se benchmark.
- Podíl realizovatelných režimů mezi `2²⁴` možnostmi: neproběhl globální výčet.
- Druhý úplný výčet (ii): skončil limitem, jeho dílčí výstup má výše popsaný rozsah.

Tato vynechání vycházejí z výslovného pokynu uživatele 3. listopadu.
Jsou vedená také v registru `full-review.json`; žádný vynechaný údaj
není označen za nezávisle ověřený. Starší úlohy s jinými mezerami se
kvůli této změně pravidel automaticky neuzavírají.

Šest vrstev errat bylo prohledáno podle úlohy, obou vydání, stran,
hodnot a pojmů. Použité oficiální soubory byly naposledy stažené
3. listopadu v 05:37 UTC při úloze 143; nyní se ověřily jejich stejné
hashe. Odpovídající oprava 144 nenalezena. Fyzický výtisk a celou
nejnovější digitální verzi nadále neověřujeme.

Doklady: [přijetí výsledků](results/hexagons144/accepted.json),
[původní obrázky](results/hexagons144/figures-checked.json),
[malé porovnání celých množin](results/hexagons144/bounded/small-checked.json),
[errata](results/hexagons144/errata-check.json),
[zdroje](results/hexagons144/sources-checked.json).

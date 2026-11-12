# Slovní obdélníky a čtverce: 7.2.2, úlohy 23–33

Průchod 1. listopadu 2026; všechny níže spuštěné obdélníkové běhy již skončily.
Memové meze symetrických čtverců nyní podporuje samostatně měřená adaptace;
některé historické citace se ještě prověřují. Zdrojem slov je
autorův [wordlists.tgz](https://www-cs-faculty.stanford.edu/~knuth/wordlists.tgz),
stažený se SHA-256 a HTTP metadaty do sources/. Poslední změna archivu
je 10. dubna 2017; jednotlivé OSPD4 seznamy mají datum 22. května 2016.
SGB seznam je totožný s naší dříve archivovanou kopií sgb-words.txt.

Počty všech slovníků odpovídají poznámce na str.36. Pořadí OSPD4 ale nelze
bez dalšího ztotožnit se všemi číselnými příklady v knize: viz C014 níže.

## F083: prohozené délky slov v odpovědi 33

Strana402 přiřazuje trie se6347 uzly šestipísmenným slovům a komprimovanou
strukturu se63060 položkami pětipísmenným slovům. Tyto délky jsou obráceně.
Pro výpočet6×5 tvoří šestipísmenná slova sloupce a používají komprimovanou
strukturu; pětipísmenná slova tvoří řádky a používají běžné trie.

| Slovník | Běžné trie | Komprimované položky | Běžné po obrácení | Komprimované po obrácení |
|---|---:|---:|---:|---:|
| SGB, délka5 | 6347 | 18450 | 5188 | 16132 |
| OSPD4, délka6 | 23667 | 63060 | 20169 | 56064 |

Běžné trie má jeden uzel pro každý vlastní prefix včetně prázdného.
Komprimované trie má jednu položku pro každou hranu a jeden koncový nulový
prvek pro každý vnitřní uzel. Je-li P počet vlastních prefixů a W počet slov,
potřebuje (P−1+W)+P=2P+W−1 položek. Oba počty byly vypočteny také přímým
součtem stupňů vytvořeného stromu. Čtyři vytištěná čísla jsou správná, mají
jen chybné popisky délek slov. Znění bylo zobrazeno v PDF str402 a autorově
PS str40. Příslušná oprava není v prohledaných err4b/err4f5 ani all4b/all4f5.

## F084: po SLUMS a TOTAL zbývá 62 slov, ne 221

Strana37, první odstavec, má správné množiny přípustných písmen, ale chybný
počet slov, která jimi projdou. Z autorova slovníku WORDS(5757) je jich
**62**. Ověřeno třemi způsoby: test každého písmena, průnik pěti samostatně
vytvořených množin slov a ověření, zda každý z pěti vzniklých třípísmenných
prefixů patří některému šestipísmennému slovu. Samostatný regulární výraz
v nástroji rg dává také62:

    rg -c '^[aeioruy][^ehjkyz][emot][^abo][aeiouy]$' sources/sgb-words.txt

Úplný seznam je v basic-verified.json. Pro srovnání, ani použití všech8887
pětipísmenných slov OSPD4 nedá221: dává106. Pořadí slov nemá na tento
výsledek vliv. Mezisoučty997,4722,1370,5057,1646 z odpovědi25 naopak
přesně souhlasí; jde o počty pro jednotlivá písmenová omezení, nikoli jejich
průnik. Tvrzení o221 tedy neplyne ani z těchto mezisoučtů.

Znění potvrzeno v původním PDF str37, autorově PS str9 a v náhledu čtvrtého
digitálního vydání z dubna2026, str37. Celé err4b/err4f5 a all4b/all4f5 byly
prohledány podle místa i obsahu; oprava221 nenalezena. Oprava „though→through“
na stejné straně z15.2.2023 a stylistické změny na str35 Fascicle5 se týkají
jiných vět. Fyzické výtisky zatím nebyly ověřeny.

## C014: pořadí slov a číselné příklady

Kniha uvádí ranky CORNEA,CORNED,CORNEL,CORNER,CORNET jako
3879,3878,9602,171,5013. Autorův dostupný archiv dává
3889,3535,9382,218,4981. Čísla uzlů ST a CORNE jsou v knize260 a580,
v trie vytvořeném v pořadí současného archivu274 a722. Přípustná písmena,
celkové velikosti trie i všechny ověřené globální minimax hodnoty souhlasí.

Toto je zatím **rozdíl vstupního pořadí**, nikoli potvrzená chyba knihy.
Čísla interních uzlů jsou libovolné značky; četnostní pořadí vyžaduje dohledat
přesný použitý korpus či dřívější seznam. Otevřena zůstává také kontrola
četností slov v poznámce pod čarou na str36. Při kontrole matematických
množin a úplných počtů není rozdíl v pořadí překážkou.

## Algoritmy 24,25,28

Při volbě celého sloupce se pro každý řádek udržuje uzel trie pro dosavadní
prefix. Jediná chybějící hrana správně odmítne větev. Na poslední úrovni jsou
všechny prefixy celými slovy, takže každý přijatý obdélník je platný; naopak
žádný prefix platného obdélníku není odmítnut.

Sublists v úloze25 pouze vyberou kratší seznam kandidátů podle jednoho
řádku. Seznamy pro různé znaky jsou disjunktní, takže nevznikají duplicity;
všechny ostatní řádky se stále kontrolují. Signatura navštíveného neterminálního
uzlu je nenulová, protože jde o prefix nějakého slova a l≤n. Cyklus hledající
nejnižší nastavený bit tedy nemůže zabloudit na nulové signatuře. Při návratu
se i správně obnoví ze zvoleného slova a jeho pozice.

Při metodě28 je úroveň l jednoznačně polem (1+(l−1) mod m,1+floor((l−1)/m)).
Řádkové i sloupcové trie dovolí právě takové znaky, které prodlužují oba
platné prefixy. Nulová koncová položka komprimovaného uzlu ukončí výčet.
Úplnost a jedinečnost vyplývá z jednoznačných znaků každého pole.

Všechna tři schémata byla na100 náhodných malých slovnících porovnána
s úplným kartézským výčtem. Souhlasí celé množiny řešení i profily na
hranici dokončeného sloupce. Tím se kontroluje i optimalizace25, která
nesmí změnit strom na těchto hranicích. Ve Fascicle5 je známá oprava
odpovědi24 x₃→x_l (20.4.2020); hlavní PDF ji již obsahuje.

## Čtverce a svědci

Všechny ukázky obdélníků v úlohách23,26,29 a čtverců30,31 byly ověřeny
po řádcích i sloupcích proti příslušným slovníkům. Při vlastním přepisu
jedné ukázky jsem nejprve napsal ALONE místo vytištěného ALONG; obraz str401
to rozlišil. Nešlo o chybu knihy.

Samostatný C++ výčet po řádcích s kontrolou budoucích sloupců potvrdil všech
541968 symetrických SGB čtverců. Druhý Python výčet používá pouze požadovaný
prefix dalšího řádku a dostává totéž. Prvních500 slov dovoluje6 řešení,
prvních372 právě3 a menší slovník žádné. Diagonální podmínku splňuje27
čtverců; přesný minimax rank včetně diagonálních slov je3025. Palindromů
je18; vedlejší diagonála symetrického čtverce je nutně palindrom, protože
její protější pole se zamění transpozicí.

Pro OSPD4 souhlasí celá řada pro velikosti2–8:
717,120386,2784632,6571160,1117161,13077,6. Velikosti9–12 nemají řešení.
Souhlasí i všech sedm globálních minimax hodnot2,25,86,438,1607,5696,23623.
Program ukládá svědky a zvlášť byly ověřeny jejich řádky, sloupce a ranky.
Historické citace jsou rozebrány v [WORD_HISTORY_NOTES.md](WORD_HISTORY_NOTES.md):
De Morganův citát a příklad již potvrzeny, Dudeneyho Strand ověřen
s opravou rokuF103. Další prameny zůstávají otevřené. Meze120 Mμ / méně
než6 Gμ nyní podporuje měření popsané níže; přesný původní historický
čítač nemáme a nevydáváme vlastní adaptaci za jeho reprodukci.

Původní Knuthův program pro vyplňování po buňkách vypsal všech
1787056 obecných SGB čtverců5×5. Každý výstup byl nezávisle validován a
byla ověřena jeho jedinečnost. Z nich je541968 symetrických, ostatní se
párují transpozicí, takže počet nesymetrických dvojic je622544, jak je uvedeno
v odpovědi30. Výsledky ostatních rozměrů jsou shrnuty níže.

Reprodukce: check_word_rectangles.py, word_squares.cpp, run_word_programs.py.
Výsledky v results/word_rectangles/. Běh původních programů má průběžné
logy, PID, časové limity a u každého dokončeného případu samostatný certifikát.
Timeout se nepočítá jako nulový počet řešení. Na počty a memy, které ještě
nemají dokončený běh, se tyto výsledky nevztahují.

## Doplnění historické citace31

Babbageův původní text z1864, kapitolaXVIII, poslední odstavec na tištěné
str241, skutečně pokládá otázku, zda se mohou stát anglickými slovy obě
diagonály slovního čtverce. Ověřeno v plném přepisu
[Project Gutenberg](https://www.gutenberg.org/cache/epub/57532/pg57532-images.html),
archivovaném v sources/word-history/babbage-1864.html s kontrolním součtem.
Úloha31 má tím uzavřený i historický odkaz.

## Dokončené obdélníky 5×6, 5×9 a 5×10

Úplný běh po buňkách vydal625415 různých obdélníků5×6; každý byl ověřen
proti oběma slovníkům. Podposloupnost profilu po každých pěti polích přesně
souhlasí s(13):1,5757,2458830,360728099,579940198,29621728,625415.
Opakované slovo má přesně1618 modelů, což uzavírá počet z odpovědi29.
Memový počet398374118698 odpovídá uváděným přibližně400Gμ v odpovědi28.

Pro5×9 dokončený výčet vydal právě dva obdélníky z odpovědi26; pro5×10
nevydal žádný a skončil normálně. Jde tedy o úplné výsledky, nikoli timeout.
Běhy6×5 a postup po sloupcích dál ověřují transponovaný profil, průměrné
počty kandidátů, zbývající memové údaje a obrácené slovníky.

Dokončen i přímý běh6×5:625415 modelů,1618 opakovaných, celý transponovaný profil(1,15727,8072679,630967290,90962081,625415) a379438059140 memů. Sloupcové průměry a obrácené slovníky ještě běží.

Dokončen i obrácený běh6×5:625415 modelů,1618 opakovaných,824373357085 memů. Společně s přímým379438059140 potvrzuje přibližná měření380/825Gμ z33. OpravaF083a ostatní tvrzeníúlohy33 mají uzavřenou kontrolu. Dále běží pouze sloupcové varianty5×6a6×5.

Dokončeno1.11.2026,10:29UTC: sloupcové5×6 má625415 řešení a1 152 188 882 726memů. Každý model byl doslovně validován; SHA256-XOR a SHA256-sum celé množiny souhlasí s buněčným během. Profil a průměrné počty kandidátů jsou v `column-5x6.json`.

Dokončeno1.11.2026,14:45UTC: sloupcové6×5 má625415 řešení,
1618 s opakováním a **1 828 460 227 444 memů**. Všechny modely byly
validovány a byly odmítnuty duplicity; oba agregační hashe souhlasí
s buněčným výčtem. Profil i všechny průměrné velikosti domén souhlasí
s odpovědí27. Memový údaj v této odpovědi však nesouhlasí — viz F102.

## F102: desetkrát nadsazené memy v odpovědi27

Na [str.401](images/vol4b-p401.png) stojí „Total time ≈ 18.3 teramems.“
Správně má být přibližně **1.83 teramems**. Stejné znění bylo zobrazeno
v [autorově PS, str.39](images/fasc5b-p39.png), datovaném 11.9.2019.
Nejde tedy pouze o OCR nebo lokální PDF. Fyzický výtisk zatím ověřen nebyl.

Úloha27 výslovně požaduje algoritmus úlohy25. Přesně ten implementuje
[BACK-MXN-WORDS-NEW](sources/knuth-programs/back-mxn-words-new.w), jehož
veřejný zdroj má datum poslední změny 12.9.2015. Byl přeložen beze změn.
Počet memů není měření sekund na současném procesoru: počítají jej přímo
autorova makra o, oo a ooo v algoritmu. Stejný program pro5×6 dává
1.152188882726Tμ, což souhlasí s1.15Tμ na str37. Rozdíl pro6×5 proto
není změna jednotek ani automaticky rychlejší hardware.

### Samostatná horní mez z profilu a průměrných domén

Chybných18.3Tμ lze vyloučit i bez důvěry v konečný memový čítač dlouhého
běhu. Z knižního profilu plyne počet neterminálních uzlů
N=730017778 a počet úspěšných hran E=730643192. Jestliže w_l je vytištěná
průměrná doména zaokrouhlená na jedno desetinné místo a p_l počet uzlů,
počet všech zkoušených slov má horní mez

    T ≤ Σ_l ceil(p_l (w_l + 0.05)) = 324432071451.

Kód úlohy25 potřebuje na neterminální uzel nejvýše28m+26 memů:
dva přístupy k ukazateli/signatuře a nejvýše26 velikostí podseznamů pro
každou pozici, dále nejvýše26 hlav podseznamů. Na zkoušené slovo stačí
nejvýše3m+2 memů: načtení slova, dva přístupy a případný zápis pro každé
písmeno, potom přechod na další slovo. Každá úspěšná hrana ještě stojí
sedm přístupů při uložení a obnovení stavu. Pro m=6 tedy

    mems ≤ 758038 + 6 + 194N + 20T + 7E
         = 6635380138340 < 6.636 teramems.

Prvních758038 memů je konstrukce slovníkových struktur; následujících
šest inicializuje řádkové ukazatele. I tato záměrně hrubá mez je hluboko
pod18.3Tμ. Počítá stejnou konvenci jako kniha a původní program: diagnostický
výpis, statistiky a samotné předání hotového řešení se do memů nepočítají.
Uvedené průměry navíc samostatně souhlasí s dokončeným výčtem.

[check_word_costs.py](check_word_costs.py) kontroluje výsledky obou metod,
profil, průměry, dokončení procesů a hashe; výše uvedenou mez počítá
přesnými zlomky. Výsledek je v
[costs-verified.json](results/word_rectangles/costs-verified.json).
Mez vyvrací18.3, zatímco přesný opravený údaj1.83 plyne z dokončeného
původního programu. Počet řešení ani algoritmus se touto opravou nemění.

Relevantní errata byla prohledána 1.11.2026 podle strany, odpovědi i slov
„teramems“ a čísel18.3/1.83: `err4b.textxt`, `err4f5.textxt`, `all4b.txt`
a `all4f5.txt`. Oprava nenalezena. Záznam „answer27“ na str229 Fascicle5
opravuje jiné zadání v Dancing Links; netýká se zdejšího backtrackingu.
Také opravy1.2Tμ→150Mμ a6Tμ→180Mμ v err4b se vztahují k jiné odpovědi.

## Symetrické čtverce: přímá kontrola memových mezí

[symmetric_word_costs.cpp](symmetric_word_costs.cpp) je nová explicitní
adaptace odpovědi30. Používá jedinou komprimovanou trie pro oba směry
a vyplňuje horní trojúhelník po řádcích. **Není to nalezený původní
Knuthův program.** Smyslem je ověřit dosažitelnost uváděné náročnosti
přesně popsanou implementací stejného schématu.

Při volbě buňky `(i,j)`, kde `i≤j`, obsahuje `a[i][j]` uzel pro prvních
j znaků řádku i; obdobně `a[j][i]` uzel pro první i znaky řádku j.
Průnik dvou seřazených seznamů odchozích znaků dává přesně přípustná
písmena. Na diagonále stačí jediný seznam. Po volbě se uloží obě nové
prefixové pozice a pozice v seznamech pro návrat. Starší pole a se
nepřepisují, takže návrat vyžaduje obnovit jen pozice v seznamech.
Každý platný symetrický čtverec má v tomto stromu právě jednu cestu;
žádný jeho prefix není odmítnut. Terminální odkazy jsou ranky slov,
nikoli adresy dalších trie uzlů.

Každý přístup do komprimované trie, tabulky prefixů a zásobníku má
samostatný čítač. `(znak,odkaz)` se vejde do jednoho 64bitového slova,
jak výslovně používá kniha. Dva 32bitové návratové indexy lze rovněž
spojit do jednoho slova; všechny naše trie se do32 bitů bezpečně vejdou.
Pro kontrolu závislosti na této optimalizaci je uvedena i konzervativnější
varianta se dvěma oddělenými návratovými slovy: přidává přesně dva memy
na každou úspěšnou hranu stromu, jeden při uložení a jeden při obnovení.
Rekurzivní volání zde nejsou; souřadnice úrovně se mění aritmeticky.
Statistiky, výpis a samostatná validace modelů nejsou součástí měřeného
algoritmu, stejně jako v původních autorových programech.

K vyhledávání přičítáme horní mez konstrukce `(4n+10)W+128P+4E`, kde W
je počet slov, P počet vlastních prefixů a E=P−1+W počet trie hran.
První člen pokrývá vstup a procházení slov; druhý nulování, tři průchody
26větvovými uzly a pomocná pole; poslední ukládání a přemapování hran.
Jde o konzervativní mez jednoduché konstrukce v modelu paměťových slov,
nikoli měření systémového alokátoru nebo souborového I/O.

| Slovník | Řešení | Memy hledání | Včetně horní meze přípravy | Totéž se dvěma návratovými slovy |
|---|---:|---:|---:|---:|
| SGB5 | 541968 | 96241911 | 97275449 | 114026797 |
| OSPD2 | 717 | 4122 | 9640 | 11324 |
| OSPD3 | 120386 | 875022 | 934122 | 1249856 |
| OSPD4 | 2784632 | 51371119 | 51781179 | 64481259 |
| OSPD5 | 6571160 | 562469887 | 563937865 | 668722425 |
| OSPD6 | 1117161 | 2086623218 | 2090344884 | 2422486508 |
| OSPD7 | 13077 | 4433084201 | 4440552229 | 5107234479 |
| OSPD8 | 6 | 4516695249 | 4528337153 | 5175311899 |
| OSPD9 | 0 | 2219512021 | 2233469577 | 2536757997 |
| OSPD10 | 0 | 492064163 | 505008403 | 570115405 |
| OSPD11 | 0 | 150840189 | 162007259 | 181968975 |
| OSPD12 | 0 | 59360931 | 68486375 | 76296649 |

I konzervativnější varianta je pod120 miliony pro SGB5 a pod6 miliardami
pro všechny délky OSPD. Výkonový závěr knihy je tedy dosažitelný bez
závislosti na zabalení zásobníku. Netvrdíme shodu posledních číslic
s původním nezveřejněným měřením. Nevzniká nový nález.

[check_symmetric_word_costs.py](check_symmetric_word_costs.py) porovnal
celé množiny řešení na123 malých slovnících s úplnými kartézskými součiny.
Na všech12 velkých vstupech souhlasí počty s dřívějším nezávislým výčtem
po celých řádcích. Každý nový model byl zkontrolován proti původním slovům
a transpozici; také účetnictví prefixů a zásobníku souhlasí s profilem
vyhledávacího stromu. Všechny procesy skončily úspěšně.
Souhrn: [symmetric-costs-verified.json](results/word_rectangles/symmetric-costs-verified.json).
Příkazy, PID, časové limity a kontrolní součty:
[symmetric-costs-run.json](results/word_rectangles/symmetric-costs-run.json).

Úloha30 má tím ověřené počty, algoritmus, dosažitelnost výkonové meze
a historický příklad. U32 zůstávají otevřené pouze popsané historické
zdroje; přesné původní měření je u obou výslovně odlišeno od naší kontroly.

## F104: krajní délka prefixu v popisu trie

Na [str.36](images/vol4b-p36.png) stojí, že trie má jeden26položkový
uzel pro každý prefix délky `0≤l≤n`. Pro popsané uložené uzly má být
**`0≤l<n`**. Stejná neostrá horní nerovnost byla přímo zobrazena v
[autorově PS na str.8](images/fasc5b-p8.png). Jde o drobnou chybu
v rozsahu indexu, nikoli o chybný počet23667 nebo chybné prohledávání.

Terminální hrany z prefixů délky n−1 podle následujícího odstavce
obsahují ranky slov, nikoli odkazy na další26položkové uzly. To je také
konvence původních programů a odpovědi24. Prefix celé délky n se proto
samostatným26položkovým uzlem nereprezentuje. Kdybychom doslova
alokovali i tyto uzly, přidali bychom po jednom pro každé slovo.

Nejmenší příklad je slovník `{a}`: stačí kořen s terminálním rankem1
v položce a; uzavřený rozsah délky0 až1 by požadoval dva uzly.
Pro skutečný šestipísmenný slovník jsou počty různých prefixů po délkách

    1, 26, 279, 2501, 8297, 12563, 15727.

Součet prvních šesti hodnot je správných23667. Součet i s poslední
úrovní dává39394. Výsledek nezávisle potvrdily množiny textových prefixů
a úplný strom znaků; nezávisí na pořadí slov ani na dosud otevřených
konkrétních rancíchC014. Podrobnosti jsou v
[check_word_prefix_range.py](check_word_prefix_range.py) a
[prefix-range-verified.json](results/word_rectangles/prefix-range-verified.json).

Dne1.11.2026 prohledána `err4b.textxt`, `err4f5.textxt`, `all4b.txt`
a `all4f5.txt` podle prefixů, trie, čísel a odpovídajících stran36/34.
Oprava tohoto rozsahu nenalezena. Změna „though→through“ na následující
straně je jiná oprava. Fyzický výtisk zatím nebyl ověřen.

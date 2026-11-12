# Sudoku: minimální zadání, trojice a sedm sad dam — DLX55–58

Kontrola 1. listopadu 2026. Otázky: 4B str.129; odpovědi: str.427–428;
diagram k58: Appendix E, str.671. Zobrazeno původní PDF i autorův PS,
zejména PS str.131–132. V PDF je pořadí stránky tištěné číslo +20;
v tomto autorově PS jsou odpovědi posunuté o296 stran.

Výsledek: **F114 a F115**, dvě různé chyby v odpovědi57. E030 a E031 jsou
již zveřejněné a v našem 4B zapracované opravy. Matematická kontrola55–58
je rozsáhlá; přesně vymezené historické a benchmarkové mezery níže zachovávám.
Žádné nové emailové návrhy ani odesílání.

## 55: přesná minima18 a20

Oba vytištěné diagramy na str.427 byly vytaženy podle souřadnic jednotlivých
číslic: první obsahuje18, druhý20 nápověd. Původní DLX1 i nezávislý
souřadnicový řešič potvrzují jediné řešení, přesně(28a), respektive(28b).
Pro odstranění každé jednotlivé nápovědy je uložené jiné úplné platné sudoku.

Dolní mez18 má krátký obecný důkaz. V každém ze tří vodorovných pásů vezmeme
postupně číslice{1,4,7}, {2,5,8}, {3,6,9}. V obou tabulkách tvoří jejich
pozice tři řádky a tři sloupce, po jednom sloupci v každém svislém pásu.
Na těchto devíti pozicích lze vložit kteroukoli z12 latinských tabulek3×3
nad příslušnou trojicí. Každá záměna zachová všechny řádky, sloupce i boxy
celého sudoku. Při fixaci libovolné jediné buňky zůstávají čtyři možnosti,
tedy původní a tři jiné. Každá z devíti disjunktních oblastí proto potřebuje
alespoň dvě nápovědy: celkem nejméně18. Program kontroluje celý rozklad,
všech12 záměn každé oblasti i všech devět jednobuněčných fixací.

Pro(28b) jsme navíc získali **všech2043 minimálních nevyhnutelných množin
o nejvýše18 buňkách**:

| Velikost | Počet |
|---|---:|
| 6 | 162 |
| 16 | 567 |
| 18 | 1314 |

Každá má uložené celé alternativní sudoku, které se od(28b) liší přesně
na uvedených pozicích. Žádná dvojice uložených množin neobsahuje jedna druhou:
ověřeno všech2 085 903 dvojic.

Úplnost není odvozena z timeoutu. SAT instance vyjadřující alternativní sudoku
s nejvýše18 změnami a bez kterékoliv uložené množiny je UNSAT. Glucose4
vytvořil DRAT důkaz, samostatný `drat-trim` jej ověřil. Úplnost spolu
s antichainem a platnými alternativami dokazuje i minimalitu každé množiny:
menší alternativa by musela obsahovat jinou uloženou množinu, což je spor.

Druhá CNF vybírá nejvýše19 nápověd, požaduje zásah každé z2043 množin
a alespoň dvě nápovědy v každé z devíti výše dokázaných oblastí. Také ona je
UNSAT s nezávisle ověřeným DRAT důkazem. Každé jednoznačné zadání musí tyto
podmínky splňovat, proto **(28b) potřebuje nejméně20 nápověd**. Vytištěný
20prvkový příklad tuto mez dosahuje. Samostatné vyloučení18 už není nutné:
druhý důkaz vylučuje všechny velikosti≤19.

Pozor na význam čísla2043: jde o minimální nevyhnutelné množiny, nikoli
o všechny jejich nadmnožiny do velikosti18.

Přenos do(28c) byl proveden explicitně pomocí permutace z odpovědi43:
`p(3a+b)=3a+(a+b mod3)`, inverzní sloupcové permutace a přejmenování číslic.
Ověřena celá výsledná tabulka i převedených20 nápověd, opět oběma řešiči.
Obecně jde o bijekci zachovávající počet nápověd i jednoznačnost.

Doklady: `results/sudoku_variants/clue-bounds.json`, `supplement.json`,
`unavoidable55/run.json`, `trades.json`, `certificate-replay.json`, obě CNF,
komprimované DRAT důkazy a protokoly nezávislého ověření.
Důkazy mají po kompresi přibližně75.2MB a15.6MB. Kontrolní programy
`check_sudoku_unavoidable55.py` a `check_sudoku_unavoidable_certificate.py`
oddělují hledání od opakované kontroly certifikátu.

**Zbývá:** historický údaj177Mμ a nezávislý původní doklad atribuce
G.McGuireovi. Tyto mezery nemění právě dokázaná minima18/20.

## 56: čtyřicet nezbytných nápověd

Celých40 vytištěných nápověd přesně souhlasí s prvním řádkem souboru
`40puz2.txt`, přímo odkazovaného na
[stránce Mladena Dobricheva](https://sites.google.com/site/dobrichev/sudoku-puzzle-collections).
Soubor obsahuje dva příklady. Kopie a metadata jsou v `sources/sudoku/`.

Původní DLX1 dává jediné řešení. Nezávislý souřadnicový řešič jednoznačnost
potvrzuje a ke každému ze40 odstranění uloží jiné platné řešení. Tím je
irredundance ověřena pro každou nápovědu zvlášť.

Řešení nemá netriviální automorfismus. Kontrola zahrnuje přejmenování číslic,
permutace pásů a řádků/sloupců uvnitř nich i transpozici. Není nutné přímo
zkoušet9! přejmenování: první zdrojový řádek a zvolená sloupcová permutace
vynutí celé přejmenování; výsledné řádky pak vynutí řádkovou permutaci.
Všech2·1296·9 případů dává právě identitu. To je úplná redukce, nikoli vzorek.

Autorova stránka výslovně odlišuje41prvkové **víceřešitelné** pseudopuzzles
od jednoznačných sudoku. Nejde o protipříklad k otevřené otázce56.
Při aktuální rešerši nebylo nalezeno ověřené jednoznačné minimální sudoku
s41 nápovědami; **nedokazujeme, že40 je globální maximum**.

**Zbývá:** původní oznámení z roku2014. Odkaz
`https://forum.enjoysudoku.com/high-clue-tamagotchis-t30020-135.html`
byl nalezen, ale veřejné načtení skončilo timeoutem. Autorova vlastní sbírka
potvrzuje přesný příklad, nikoli sama o sobě datum jeho prvního objevu.

## 57: všechny trojice a dvě nezávislé chyby

Všechny úvodní příklady souhlasí. Tabulka(28a) má9 vodorovných a3 svislé
trojice, (28b) má3 a3; řešení(29a) má26 a23. Trojice{3,6,8} se v posledním
případě vyskytuje jednou vodorovně a dvakrát svisle.

Jeden box má **2592=2·(3!)⁴** možností. Nezávisle porovnány všechny9!
permutace číslic s konstrukcí12 latinských vzorů tří skupin krát(3!)³
rozmístění jednotlivých číslic. Množiny jsou totožné.

Každá možnost přesného pokrytí obsahuje box, devět dvojic řádek–hodnota /
sloupec–hodnota, tři vodorovné a tři svislé trojice: celkem25 položek.
Úplné množiny řešení původního DLX1 souhlasí s nezávislou reprezentací
pomocí bitových množin, včetně celého profilu stromu.

### F114 — po uvedené normalizaci je432 řešení, nikoli864

PDF str.427 i PS str.131 fixují první box na

```
1 4 7
8 2 5
6 9 3
```

a první řádek na `1472AB3CD`, kde `{A,C}={5,6}` a `{B,D}={8,9}`.
Za těchto podmínek oba úplné výčty vracejí **432**, nikoli vytištěných864.

Číslo864 se přesně reprodukuje při slabší normalizaci: v každém boxu horního
pásu mají první tři buňky postupně číslici ze skupin{1,2,3}, {4,5,6}, {7,8,9},
ale dvojka a trojka mohou být v kterémkoli ze dvou pravých pásů. Takový
generátor má právě `1+2·432+6·2592=16417` možností. Přesně polovina jeho
řešení má dvojku ve sloupci3; druhou polovinu dává záměna pravých dvou
svislých pásů. Každé takové párování je explicitně ověřeno.

Při doslovném předfiltrování všech prvních řádků podle vytištěné podmínky
vzniká `1+2·64+6·2592=15681` možností. Samotný počet ponechaných možností
závisí i na tom, které neslučitelné možnosti necháme později odstranit DLX;
rozhodující chyba je **počet řešení po výslovně uvedené normalizaci**.

Možnosti opravy: ponechat silnou normalizaci a uvést432 řešení, nebo oslabit
normalizaci tak, aby dovolovala i záměnu dvojky a trojky mezi pravými pásy.
Není dotčeno, že jde po všech povolených přejmenováních o jedinou třídu.

V naší slabší konstrukci má původní DLX1 přesně54 007 751 hledacích memů,
což souhlasí s uvedenými54M. Inicializace55 845 424 neodpovídá historickým58M;
pořadí/generátor původního vstupu nemáme. Samostatný nález z tohoto údaje
neděláme.

### F115 — k izomorfismu nestačí permutace řádků a sloupců

Další věta tvrdí, že všech864 řešení je izomorfních pouze pomocí permutací
řádků a sloupců zachovávajících sudoku. Ve skutečnosti takových tříd je
**šest, každá po144**; při silné normalizaci šest po72. Po přidání
**přejmenování číslic** se skutečně sjednotí. Pro každou třídu i všech864
tabulek je uložená a přímo zkontrolovaná explicitní transformace.

Krátký protipříklad vůči vytištěné tabulce je následující další platné řešení.
Splňuje i silnou normalizaci, takže chyba nezávisí naF114:

```
147259368
825736914
693481572
268347159
571692483
934815726
359168247
482573691
716924835
```

Přechod od prvního ke čtvrtému řádku tohoto příkladu je permutace číslic
`(1 2 3)(4 6 5)(7 8 9)`: číslice1 jde na2,2 na3 atd. Žádná z72 uspořádaných
dvojic různých řádků vytištěné tabulky tento přechod nemá. Přitom permutace
sloupců každý přechod zachovává a permutace řádků pouze přeuspořádá seznam
72 přechodů. Tabulky proto nelze takto ztotožnit ani při dovolení libovolných
řádkových/sloupcových permutací, bez podmínky zachování boxů.

Jiný chybějící přechod v certifikátu vylučuje i transponovanou vytištěnou
tabulku. Nezávislá druhá kontrola zkouší všech devět možných obrazů prvního
řádku; každý vynutí sloupcovou permutaci a následně narazí na chybějící
řádek. S transpozicí jde o18 přímo zkontrolovatelných případů.

Tento protipříklad ověřuje samostatný program
`check_sudoku_trio_certificates.py`, který nepoužívá žádný řešič. Minimální
oprava tvrzení přidává možnost přejmenovat číslice. PDF i PS mají stejné
chybné znění; fyzický výtisk není ověřen.

Vytištěná vnitřní symetrie boxů je správná: zobrazená permutace
`ABC/DEF/GHI → IBD/HAF/GCE` platí pro všechny čtyři sousední dvojice
směrem dolů a doprava. Tuto část s chybou izomorfismu neslučujeme.

Doklady: `trios57/validation.json`, `small-certificates.json`, oba úplné
DLX vstupy a výstupy. Počet možností, počet řešení a klasifikace byly
kontrolovány odděleně; F114 aF115 mají různé příčiny i opravy.

## 58: čtyři řešení se sedmi sadami dam

Nezávislý výčet nejprve generuje všech144 řešení devíti dam, která mají také
právě jednu dámu v každém boxu sudoku. Poté úplně vypíše24 množin sedmi
navzájem disjunktních rozmístění. Zbylých18 buněk se obarvuje číslicemi8/9:
každý řádek, sloupec i box v nich vytváří dvojici, tedy hranu grafu. Úplná
bipartitní obarvení dávají osm tabulek po přejmenování číslic, z nichž čtyři
splňují knižní podmínku pozic `p<q`, `p+q<9`.

Původní neupravený DLX2 s přesně729 běžnými možnostmi a20 dodatečnými
barevnými možnostmi vrací **stejné čtyři úplné tabulky**. Všechny jsou přímo
ověřeny jako sudoku i sedm řešení devíti dam. Po otočení o180° a normalizaci
číslic je každá sama sebou; normalizovaná transpozice je sdružuje do dvou
dvojic, jak uvádí opravená odpověď.

V Appendix E bylo zkontrolováno všech71 vytištěných číslic. Z10 prázdných
buněk se vyskytují jen číslice8/9; všech1024 doplnění bylo přímo vyzkoušeno.
Platná jsou právě dvě, jejich transpozice dávají zbývající dvě řešení.

**Zbývá:** historických3Gμ. Doslovný barevný model s pořadím primárních položek
`p,r,c,b,*` v našem původním DLX2 potřeboval220 616 937 621 čistých hledacích
memů. Původní volby pořadí/heuristik neznáme; počty řešení jsou úplně ověřeny,
ale tento benchmark nepovažujeme za reprodukovaný ani za samostatný nález.

## Errata, citace a rozsah

`check_sudoku_variants_errata.py` znovu porovnal čtyři aktuální oficiální
soubory s archivem: všechny se shodují. Prohledány celé historické i aktuální
seznamy4B/F5 a oba zdrojové TeXy, nejen čísla úloh. Kontrola zahrnuje i
posunuté stránky a charakteristická čísla/slova. ProF114/F115 odpovídající
oprava nenalezena; tím není dokázáno prvenství ani nárok na odměnu.

- **E030:** F5.127, otázka57, 10.9.2021: doplnění „at most“ k27 trojicím.
  Naše4B opravu obsahuje, autorův starší PS nikoli.
- **E031:** F5.236, odpověď58, 5.2.2021: doplnění barevných položek
  `*j:k` a oprava dvou řešení na čtyři, s redukcí transpozicí na dvě.
  Naše4B obsahuje celou opravu. Není to nový nález.

[Veřejná vydavatelská ukázka Thoenovy knihy](https://www.bruna.nl/images/active/InkijkPDF/cb/9789402188349.pdf)
potvrzuje rok2019 a názvy/umístění §2.7 a§3.4 v obsahu. **Neobsahuje text
těchto dvou oddílů**; nepředstíráme jeho přečtení ani nezávislé ověření
celé atribuce Thoen–van de Wetering. Kopie ukázky a metadata jsou archivované.

Zbývající historické/benchmarkové mezery ponechávají celé úlohy55–58
v registru `partial`, i když hlavní matematické výsledky, všechny dotčené
diagramy a dvě opravená tvrzení mají úplné důkazy. Pokrytí sousedních úloh
na stejných stránkách se tím automaticky nezvyšuje.

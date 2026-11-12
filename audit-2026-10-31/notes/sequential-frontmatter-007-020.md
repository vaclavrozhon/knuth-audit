# Předmluva, úvodní úlohy a obsah — file 7–20

Kontrola 6. listopadu 2026. Všech čtrnáct původních stran bylo skutečně
zobrazeno (`images/sequential/file-007.png` až `file-020.png`), stejně
jako odpovědi úvodních úloh na tištěné str. 370 (`file-390.png`). Níže
jsou odděleny uzavřené argumenty, omezené vnitřní odkazy a otevřené body.
Pouhé načtení odkazované stránky neuzavírá její matematický obsah.

## D088: předmluva v–ix (file 7–11), zatím partial

| Položka | Posouzený rozsah a důkaz | Co se nepřebírá jako ověřené |
|---|---|---|
| v: členění 4A/4B, kapitola 7 a oddíly 7.1, 7.2, 7.2.1, 7.2.2 | Lokální obsah obou svazků a nadpisy 4B souhlasí. Obecné nadpisy kapitoly patří do 4A; tři nulové odkazy v místním obsahu řeší E112 níže. | Přesný rozsah citátu z předmluvy 4A a historický vznik publikačního plánu nejsou samostatně zdrojově uzavřeny. |
| v: XC jako výběr pokrývajících možností a rozšíření XCC | Pro množinu primárních položek P je podmínka pro vybranou rodinu S: každé p v P leží právě v jedné možnosti S. XCC přidá sekundární položky, jejichž explicitně obarvené výskyty smějí být současně vybrány právě s jedinou barvou. Při absenci barev se vrací obyčejný model XC s nanejvýš jedním sekundárním výskytem. Tento popis souhlasí s převzatým invariantem Algorithm C v `COLORED_BASICS_NOTES.md`, oddíl „AlgorithmC: invariant a kontroly81–82“. | Nejde o nové uzavření všech aplikací ani všech jejich úloh. Tvrzení o nejvhodnější metodě a významu mnoha speciálních případů jsou autorské hodnocení, nikoli přesná optimalizační věta. |
| vi: XCC, MCC a minimální cena | XCC barva přidává lokální konflikt mezi dvěma možnostmi; nemění požadavek přesného primárního pokrytí. MCC přidává horní/dolní násobnosti. U ceny se minimalizuje součet cen vybraných možností; jde o další cíl nad stejnou množinou přípustných řešení. Definiční návaznost odpovídá zdrojům DLX2, DLX3 a DLX5 v `sources/knuth-programs/`. | „Almost as easily“ je kvalitativní srovnání bez univerzální nákladové meze; žádná taková mez nebyla odvozena. Historické doby a velké průmyslové SAT instance se nereprodukovaly. |
| vi: definice SAT | Pro booleovskou funkci f na n proměnných se hledá vektor a v {0,1}^n s f(a)=1. To je přesně otázka existence splňujícího ohodnocení. Konečný problém s N možnými konfiguracemi lze kódovat k=ceil(log2 N) bity a funkcí přijímající právě kódy řešení; zakázání každého odmítnutého bitového slova je jedna klauzule délky k. Toto dokazuje obecnou vyjádřitelnost, nikoli malé kódování nebo rychlé řešení. | Není z toho tvrzen polynomiální převod libovolného problému. Výrok o milionech proměnných a historickém průmyslovém průlomu je neověřený empirický/historický rozsah. |
| vii: sedm SAT solverů | Jména A, B, W, S, D, L, C tvoří sedm základních algoritmů; L′ je uvedená varianta L. Primární autorův uložený katalog `sources/usa239_246/programs.html`, položky SAT0 až SAT13, dává tuto korespondenci. | Katalog není důkaz správnosti programů ani srovnání se špičkou roku 2010. |
| vii: deset aplikací a sto benchmarků | V textu je vyhledáno devět hlavních aplikačních nadpisů od jednoduchého příkladu po tomografii; bounded model checking obsahuje více oddělených aplikací Life. Přesné seskupení, které dává autorových deset, zatím není uzavřeno. Předmluva skutečně odkazuje na kolekci SATexamples a tabulku 6. | Číslo deset zatím není ani potvrzené, ani vyvrácené; nejde o nový nález. Úplný soupis sta identifikátorů ani všechny generátory ještě nejsou tímto blokem přijaty. |
| vii: odkazy na str. 264 a úlohy 302,303,299,306 | Přesná čtyři čísla jsou na str.264; text u306 výslovně diskutuje optimální mez restartu a následuje reluctant doubling. Kontrola je pouze odkazu, ne opakovaný důkaz úloh. | Staré otevřené části těchto úloh se nemění. Ilustrace na300–301 se nepovažují za ověřené pouze na základě zmínky v předmluvě. |
| viii: programy a datové soubory | Uložený primární katalog potvrzuje DLX1→X, DLX2→C, DLX3→M, DLX5→C$, DLX6→Z, DLX-PRE→P a SAT0→A, SAT0W→B, SAT8→W, SAT9→S, SAT10→D, SAT11→L, SAT11K→L′, SAT13→C. Existují původní archivované wordlists.tgz, SATexamples.tgz a sgb.tar.gz s metadaty. | Není ověřena současná dostupnost všech adres, úplnost tisíce autorových programů ani bezešvá ekvivalence kódů s každým tištěným detailem. Pozdější známé programové odchylky zůstávají v ledgeru. |
| ix: MPR, návaznost Fig.67→68 a strany | MPR je skutečně samostatný úvod; §7.2.2 začíná na sudé str.30 a má Fig.68. Lokální 4A má Fig.67 na str.503. | Přesný konec §7.2.1 na pravé stránce 4A nebyl v tomto bloku vizuálně kontrolován. Úplnost notací/dalších křížových odkazů není tímto uzavřena. |
| ix: odměny, poděkování, značky časopisů | Částky a budoucí publikační postup jsou autorovo prohlášení z června2022, nikoli náš příslib odměny či nynější nabídky. Kódy časopisů jsou výslovně vysvětlené konvence; odkaz na budoucí úlohu se znakem00 je definován. | Aktuální odměny, osobní příspěvky jmenovaných lidí a historie názvů IEEE nejsou nezávisle ověřeny. |

Přesné historické citace Carroll1896, Gardner2013 a Knuth2008, osobní
výpovědi a dostupnost vnějších webů jsou výslovně vynechanou bibliografií.
Rozsahové výroky „more than a third“ a „second half“ nejsou zatím
nezávisle rozpočítány podle zvolené konvence pro odpovědi/dodatky;
neoznačuji je za přesně ověřené číselné údaje. Kvůli nezavřenému soupisu
aplikací/benchmarků a vnitřní návaznosti zůstává D088 i file7–11 partial.

## D089: notace, str. x (file 12), checked

1. Šestnáctkový příklad: #123 = 1·16²+2·16+3 = 291; jde o definici
   prefixu, nikoli o desetinné číslo123.
2. Monus: max(0,x−y) je0 pro x≤y a x−y pro x≥y; v x=y se větve
   shodují. Platí pro reálné argumenty, pro nezáporná celá čísla zůstává
   výsledek nezáporný celý. Z uvedené definice se neodvozuje obyčejné
   algebraické odčítání.
3. Medián tří hodnot je prostřední prvek po seřazení s násobnostmi;
   existuje i při rovnosti dvou či tří hodnot a je jednoznačný. Symbol
   není obecným součinem x·y·z ani zaokrouhlením.
4. Čtyři intervalové značky kódují nezahrnutí/zahrnutí levého a pravého
   konce. Při x=y je uzavřený interval singleton, ostatní jsou prázdné.
   Při x>y jsou podle obvyklé uspořádané definice prázdné.
5. Zápisy X∪x a X\x jsou výslovně zkratky X∪{x}, X\{x}; každý mění
   právě členství prvku x, nikoli všech členů případné množiny x.
6. Pro n≥0 je počet jedniček νn konečný a ν0=0. Pro n>0 existují
   největší a nejmenší index bitu, takže λn=floor(log2 n) a ρn je
   exponent největší mocniny2 dělící n. V n=0 se λ,ρ netvrdí.
   Z10=8+2 plyne ν10=2, λ10=3, ρ10=1 přesně jako v tisku.
7. Kartézský součin C_m□C_n má vrcholy (i,j) modulo(m,n) a hrany,
   které změní právě jednu souřadnici o±1. Je to obdélníková mřížka
   s oběma dvojicemi protějších hran ztotožněnými, tedy uvedený torus.
   Používá se obvyklý obor jednoduchých cyklů m,n≥3; netvrdíme novou
   konvenci pro C1/C2 ani homeomorfismus konečného grafu s plochou.

Úvodní hodnocení vhodnosti notace je autorská preference. Tvrzení, že
Appendix B je úplný rejstřík, nebylo ověřeno; jde o otevřenou kontrolu
rejstříku, nikoli o výsledek sedmi argumentů výše. D089 proto uzavírá
matematické definiční příklady, **ne celou stranu x**; stránka zůstává
partial do kontroly úplnosti příslušných odkazů.

## D090: poznámky k úlohám, xi–xiv (file 13–16), partial

Hodnocení00,10,20,30,40,50 a značkyM,HM,šipka jsou autorovy definice
a přibližná pedagogická vodítka; nepředepisují přesnou funkci času.
Výslovný dovětek naxii odmítá absolutní interpretaci. Proto „logarithmic“
nedává číselný zákon, který by se měl extrapolovat. Příklad24 versus25
souhlasí s mod5: zbytky4 versus0 oddělují více rutinní práce od tvořivosti.
Souhrnná tabulka naxiii odpovídá textu xi–xii. Doporučení k řešení,
používání dřívějších odpovědí a didaktické názory nejsou nové věty.
Bellmanova anekdota je v originále výslovně označena jako rumor; přesná
bibliografie Bellmana, Pólyi–Szegőho a citáty Aristofana, Diggese a Defoea
se nyní vynechávají. Žádný z těchto citátů není důkazem matematické úlohy.

Tři úvodní úlohy nejsou zahrnuty v původním registru1202 hlavních úloh;
vedou se navíc jako `Front:1` až `Front:3`:

- **Front:1, [00], checked:** M znamená matematické zaměření;15 leží
  mezi jednoduchou10 a průměrnou20. Odpověď „moderately easy“ pro
  matematicky zaměřeného čtenáře přesně odpovídá oběma definicím.
- **Front:2, [10], checked:** při řešení se musí definice použít na nový
  vstup a rozlišit, které předpoklady jsou potřebné; odpověď dovoluje
  porovnat vlastní postup a odhalit chybu. To je přímá odpověď na
  otevřenou pedagogickou otázku, nikoli experimentální psychologická
  univerzální věta. Tištěná odpověď uvádí jiný možný přínos: autorovu
  odměnu za první platné nahlášení chyby; to odpovídá prohlášení naix,
  podmínky prvenství a správnosti nelze vypustit.
- **Front:3, [HM45], partial:** zadání je Poincarého věta pro uzavřenou
  jednoduše souvislou trojrozměrnou varietu. V odpovědi není důkaz,
  ale literatura. Přesné Perelmanovy záznamy arXiv0211159/0303109/0307245
  mají uvedené roky2002/2003 a délky39/22/7 stran. První věta posledního
  článku má další předpoklad o prvočíselném rozkladu a odkazuje na
  předchozí chirurgickou konstrukci; prostá citace není celý důkaz.
  Morgan–Tian, `arXiv:math/0607607v2`, Corollary0.2(a), str.6, dává
  přesný hladký výsledek; kapitola18, str.399, vysvětluje závislost
  na15.9 a18.1. Tyto vstupní věty zde nebyly auditovány. Navíc přechod
  z obecné topologické k hladké kategorii vyžaduje samostatný výsledek
  o3-varietách. Známý platný výsledek se proto **nevydává za náš uzavřený
  důkaz této úlohy**. Jde o důkazní mezeru auditu, nikoli nový otevřený
  výzkumný problém a nikoli kandidát na chybu knihy.

Pramenný rozsah Front:3: `results/sequential/front-exercise3-sources.json`;
primární [Perelmanův závěrečný článek](https://arxiv.org/abs/math/0307245)
a [rozvinutý důkaz Morgan–Tian](https://arxiv.org/abs/math/0607607).
Bibliografická výjimka neuzavírá chybějící matematický argument.

File13,14,16 mají posouzený celý nematematický obsah s uvedenými výjimkami.
File15 zůstává partial kvůli Front:3. Odpovědní file390 se neuzavírá:
obsahuje také MPR1 a začátekMPR2, které tento blok dosud nekontroluje.

## D091: obsah xv–xvii a fotografie xviii (file 17–20)

Všech81 položek obsahu bylo zobrazeno v sazbě a samostatně přiřazeno.
70 z nich má doslovně odpovídající normalizovaný nadpis na cílové stránce.
U osmi se liší zkratka nadpisu; také jejich cílové originály byly zobrazeny:

| Cíl | Nadpis skutečně na stránce | Posouzení |
|---|---|---|
|188|A simple example|Začátek příkladů aplikací; obsah používá širší název.|
|238|Resolution|Zkrácený název rezoluce klauzulí.|
|244|SAT solving via resolution|Úvod rozsáhlejší části o učení klauzulí.|
|274|Message passing|V obsahu doplněno algorithms.|
|308|Tuning up the parameters|Začíná dole na308; běžící záhlaví je na309.|
|656|Table1, 40 decimal places|Obsah je popis tabulky konstant.|
|657|Table2, 40 hexadecimal places|Obsah je popis tabulky konstant.|
|658|Table3, Harmonic/Bernoulli/Fibonacci|Všechny tři rodiny jsou v titulku.|

Podrobná mapa81 položek: `results/sequential/toc-checks.json`.
Ověření cíle **neověřuje žádnou hodnotu tabulky ani důkaz na cílové straně**.
Citáty Strosse2001 a Kode Vicious2012 se bibliograficky vynechávají.
Fotografie naxviii má dvě kostky bez popisku, číselného výsledku nebo
tvrzení o pravděpodobnosti. Sama nedokazuje vyváženost ani nevyváženost.

### E112: tři nulové odkazy už opravené vydavatelem

V místním PDF naxv ukazují Chapter7,7.2 a7.2.1 na0. Ve veřejné
vydavatelské ukázce čtvrté digitální verze z dubna2026 je na stejné
tištěné straně správně [4A.1], [4A.281], [4A.281]. Byly zobrazeny oba
originály (`file-017.png`, `preview-toc-16.png`); zdroj a původní SHA256
má `sources/vol4b-publisher-preview.json`. Nejde o neopravenou novou
chybu ani naši kartu. Všechny ostatní položky obsahu byly kontrolovány
nezávisle na této opravě. Konečná mapa do4A se opírá také o obsah
lokálního4A. Fyzický dotisk4B s touto vadou či opravou neověřen.

Tři záznamy jsou považovány za jednu již opravenou navigační vadu.
Oprava je také výslovně zveřejněna v err4b i all4b: str.xv, náhrada
řádků11–13, **26.11.2022**. Ověřeny původní TeX a obraz str.3 úplných
errat (`images/sequential/all4b-03.png`). Hledání v šesti vrstvách,
jejich SHA256 a přesné shody ukládá `results/sequential/frontmatter-errata.json`.
První automatický souhrn chybně označil nalezené shody za absenci opravy;
před přijetím byl opraven podle skutečných výstupů a sazby. Nejde o chybu knihy.

### E113: další známé redakční změny úvodu

Na téže původní stránce errat jsou čtyři další položky: dělení jména
Marijn naix (6.1.2023), nahrazení příkladu10 příkladem18 nax (24.11.2023),
odstranění běžícího záhlaví naxiv (9.4.2023) a dvě změny Diggesova citátu
(27.4.2024). Z18=16+2 plyne ν18=2, λ18=4, ρ18=1; i původní příklad10
je matematicky správný. Úvodní výklad v D089 tedy nevyužívá chybnou
číselnou hodnotu. Tyto známé úpravy se neprezentují jako naše nálezy.

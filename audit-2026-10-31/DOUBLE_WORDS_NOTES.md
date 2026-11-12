# Dvojité slovní čtverce a schody — DLX87–90

**Aktualizace 2. 11. 2026:** plný DLX2 výčet SGB5 již skončil
a všech 323 264 uložených modelů je ověřeno. [Dokončení a přesný rozsah](SGB5_COMPLETION_NOTES.md)
nahrazuje níže uvedený původní stav „běží“ pro tuto jedinou úlohu.
Historický náklad 15 T zůstává otevřený; ostatní běhy mají samostatný stav.

Kontrola 2. 11. 2026. Lokální 4B, první vydání, druhý dotisk 2022.
Zadání na str. 133 (PDF153), odpovědi434–436 (PDF454–456).
Odpovídající původní autorův pre-fascikl5c má otázky69 a odpovědi138–140;
publikovaný Fascicle5 používá131 a242–244. Původní stránky4B a PS byly
zobrazeny; samotný OCR text není dokladem tvaru vzorce ani nového nálezu.

V tomto bloku zatím není nová potvrzená chyba. E043/E044 jsou už vydané
opravy, které naše4B obsahuje. Neuzavřené dlouhé výčty, historické náklady
a bibliografické mezery jsou vypsané níže a v `results/double_words/checkpoint.json`.

## 87: přesné pokrytí a dvojice transpozic

Každá primární položka vybere právě jedno slovo do příslušného řádku či
sloupce. Každá buňka patří právě k těmto dvěma vybraným možnostem; shodná
barva zajistí shodné písmeno. Sekundární položka jména slova vyloučí jeho
druhé použití. Tím vzniká obousměrná bijekce mezi řešeními XCC a čtverci
s2n různými slovy. Počet možností je2nW, primárních položek2n,
sekundárních bez symetrie n²+W.

Transpozice nemá pevný bod: pevný čtverec by měl totožné řádkové a
sloupcové slovo. Každá třída proto má přesně dva prvky. Dodatečná jména
`w@` pouze v možnostech prvního řádku a prvního sloupce, při prvním větvení
na první řádek, ponechají právě orientaci s běžnějším prvním řádkem.
Všechny první volby mají různá jména `w@`. Proto zde nenastává opětovné
obnovení sdíleného markeru z F123: žádná pozdější kořenová možnost
neobsahuje marker, který byl trvale zakázán dřívější kořenovou volbou.
Barevné buňky do této úvahy o nezabarvených markerech nevstupují.

Dříve dokončený úplný původní buňkový výčet5757 slov už neopakujeme:

- všech čtverců1 787 056;
- s opakovaným slovem1 140 528;
- dvojitých orientovaných646 528, tedy **323 264 transpozičních tříd**;
- přesný náklad45 800 972 376 memů se zaokrouhlí na knižních46G.

Úplný původní DLX2 s variantou83 běží samostatně kvůli druhému modelu a
údaji15T. Dokud neskončí, netvrdíme, že jsme změřili právě tento náklad.

## 88: minimum1720 a další pořadí1800

Pokud jsou všechny možnosti téhož slova seskupené a skupiny řazené podle
četnosti slov, nejvyšší číslo vybrané možnosti monotonicky určuje nejhorší
použité slovo. Minimax může dále rozlišit pozice stejného nejhoršího slova,
ale jeho výsledek vždy minimalizuje nejvyšší slovní pořadí. Nemusí přitom
vypsat všechny čtverce vázané pouze tímto slovním pořadím.

Původní DLX2 s oficiálními úpravami minimax/83 vrací nejlepší třídu
`BLAST/EARTH/ANGER/SCOPE/TENSE`. Sloupce jsou
`BEAST/LANCE/ARGON/STEPS/THREE`; nejhorší ARGON má přesně pořadí1720.

Nezávislý úplný buňkový výčet prvních1800 slov vytvořil2482 všech čtverců
a z nich přesně8 dvojitých:2 s maximálním pořadím1720 a6 s maximálním
pořadím1800. To dokazuje jak nemožnost na1719 slovech, tak následující
hranici1800 a její tři transpoziční třídy. Všechny uložené dvojité modely
byly znovu přímo geometricky zkontrolovány. Slovo PEERS má pořadí1800.

Samotný seznam minimaxových zlepšení by další nejlepší hranici nedokazoval:
mohl přeskočit jiné suboptimální výsledky. Zde ji dokazuje úplný omezený
výčet, nikoli pořadí několika nalezených svědků.

Nativní měření dává62 475 804 097 hledacích memů po odečtu údržby délek
sekundárních položek, plus350 349 033 inicializačních. To přesně
nereprodukuje knižních64G. Původní pořadí položek/možností a historická
implementace nejsou doloženy; tato odchylka zatím není nález chyby.

## 89: slovník OSPD4

Všech šest vytištěných čtverců má platná a vzájemně různá řádková i
sloupcová slova. Přesná maxima v dostupném autorově slovníku:

| Velikost | Nejhorší pořadí | Nejhorší slovo / rozsah kontroly |
|---|---:|---|
| 2 | 16 | celý nativní minimax dokončen |
| 3 | 64 | celý nativní minimax dokončen |
| 4 | 401 | celý nativní minimax dokončen |
| 5 | 1310 | celý nativní minimax dokončen |
| 6 | 5772 | CLOACA; úplný buňkový výčet přijat2.11., minimum prokázáno |
| 7 | 22038 | HOMAGER; platnost svědka ověřena, úplný buňkový výčet běží |

Pro2–5 je ve frontě také nezávislý úplný buňkový výčet do těchto hranic.
Pro6 je celý výčet dokončený a přijatý; pro7 nadále běží celý slovník
a očekávaných14 513 ještě není přijatým výsledkem. Údaj sedmi dvojitých7×7
je nutné posuzovat po transpozici. Nevyvozujeme chybu faktoru2 jen z toho,
že případný orientovaný výčet vydá14 modelů.

Aktuální efektivní hledací náklady minimax2–5 jsou39 736;2 863 106;
233 247 989;25 270 437 672 memů. Inicializace je vedená zvlášť v surových
logech a JSON. Čísla neztotožňujeme automaticky s historickými benchmarky
200K/15M/450M/25G. Existující C014 navíc eviduje jiné pořadí některých slov
v dostupném archivu; není důvod pokládat každou nákladovou odchylku za
chybu knihy. OSPD4 zde znamená přesně archivovaný seznam, nikoli novější
vydání slovníku s jinou množinou slov.

### Přijetí úplného6×6,2.11.2026

Wrapper862563 skončil korektně s terminálem0 po7.28h. Původní buňkový
program vypsal2 038 753 čtverců; každý byl při běhu validován vůči
přesnému slovníku, bez duplicit. Dvojitých je389 514, tedy194 757
transpozičních tříd. Celý tento uložený podseznam nezávislý přijímací
program znovu prošel: všech12 slov každého čtverce je odlišných,
transpozice sedí, každá orbita má dva prvky a celý histogram pořadí
souhlasí. Ověřeny hashe zdrojů, binárky, vstupu, výsledku i obou logů.

Nejlepší maximum5772 má jedinou transpoziční třídu, reprezentovanou
řádky CHESTS/LUSTRE/OBTAIN/ARENAS/CIRCLE/ASSESS; nejhorší slovo je
CLOACA. Následující hodnota5906 má dvě třídy. Jde o úplný výčet,
proto obě hodnoty mají důkaz globálního pořadí. Původní program
spotřeboval4 597 044 464 264 memů, což se zaokrouhlí na knižních4.6T.

`accept_ospd6_terminal.py` a `results/double_words/ospd6-terminal-checked.json`
přijímají již dokončené hledání; nic se znovu nepočítalo. Celý surový
stdout opakovaných slovních čtverců nebyl archivován, má ale hash a
při běhu proběhla jeho úplná validace. Všechny dvojité čtverce jsou
archivovány a znovu validovány. Sedmipísmenný výčet, další historické
náklady a konvenceC014 zůstávají nezávislými mezerami;89 je stálepartial.

## 90: geometrie a faktor2p

Indexujeme fyzické řádky A_i modulo p a pozice písmen od0 do n−1.
Svislá slova v obrázku jsou

```text
levé schody:  D_i[j] = A_(i+j)[j]
pravé schody: D_i[j] = A_(i+j)[n−1−j].
```

Tištěné kódování pravých schodů čísluje řádky opačně, než se postupuje
fyzicky dolů obrázkem. Jeho řádky E_i převádíme na A_i=E_(-i);
vybrané svislé slovo se přeznačí indexem−i−n+1. Po této změně souřadnic
se obě formulace přesně shodují. První pomocný program používal chybnou
konvenci; oprava našeho programu není nález v knize. Doslovně správné
kódování bylo porovnáno s úplným geometrickým výčtem na malých případech.

Pro levé schody definujme T(A)_i=D_(-i) a R_s(A)_i=A_(i+s). Potom
T² je identita a TR_sT=R_(-s). Pro pravé schody položme T(A)=D:
T²=R_(n−1) a T komutuje s R_s. V obou případech vzniká právě2p
transformací: p posunů původních řádků a p posunů řádků vzniklých ze
svislých slov. Vzájemná různost všech2p slov vylučuje shodu dvou takových
transformací. V každé třídě tedy existuje právě jeden reprezentant,
jehož první řádek je nejběžnější ze všech2p slov.

To dokazuje faktor2p i správnost použití83: přidáme marker `w@` do všech
pozic, začneme položkou prvního řádku a kořenové možnosti opět mají
různé markery. Pro levé p=1 dostaneme D=A, takže požadovaná různá dvojice
neexistuje. Pro pravé p=1 jsou slova navzájem obrácená: SPOTS/STOPS je
platný vytištěný příklad.

| p | Levé: nejvyšší pořadí | Pravé: nejvyšší pořadí |
|---|---:|---:|
| 1 | nemožné | 657 |
| 2 | 136 | 1633 |
| 3 | 447 | 1561 |
| 4 | 435 | 1036 |
| 5 | 370 | 908 |
| 6 | 454 | 1105 |
| 7 | 425 | 1254 |
| 8 | 504 | 1105 |
| 9 | 454 | 1203 |
| 10 | 474 | 1264 |

Všech19 svědků a obě zadávací ilustrace bylo geometricky prověřeno,
včetně každého slova, jeho pořadí a celé třídy symetrií. To potvrzuje
vytištěné výjimky NOTED504 pro levé p8 a prahy nad1300 pouze pro pravé
p2/p3. Optimalitu dokazuje oddělená úloha s prvními B−1 slovy pro každou
vytištěnou horní mez B, nikoli jen nalezení svědka na B.

`word_domain_csp.py` používá2p proměnných s bitovými množinami slov,
rovnosti písmen na každém fyzickém křížení a vzájemnou různost slov.
Nepoužívá přesné pokrytí, seznamy DLX, cutoff ani persistentní83 markery.
Propagace pouze odstraňuje prokazatelně nemožné hodnoty; úplné větvení
podle velikosti domény prochází všechny zbývající možnosti. Pravidlo
nejmenšího prvního slova zachovává řešitelnost díky právě dokázané symetrii.
Prázdný úplně vyčerpaný strom proto dává důkaz dolní meze; timeout by byl
uložen zvlášť a nikdy by se nepočítal jako UNSAT.

520 úplných malých porovnání CSP s prostými permutacemi řádků prošlo.
Samostatných520 porovnání doslovného XCC modelu s permutacemi také prošlo.
Zahrnují obě geometrie, čtverce, náhodné pořadí slov, opakovaná křížení
p<n, nemožné případy a varianty se symetrií i bez ní. Vypršení časového
limitu CSP bylo zvlášť ověřeno jako výjimka.

Nezávislý CSP dokončil **všech19 dolních mezí** bez timeoutu: každý problém
s prvními B−1 slovy je UNSAT. Celkem prošel122 123 uzlů. Spolu s platnými
vytištěnými svědky to potvrzuje všechna minima v tabulce. Nativní minimaxy
postupně dávají stejné hranice; jejich další průběh už není podmínkou
tohoto nezávislého důkazu. Matematika90 je dokončená, historická závorka
zůstává otevřená.

## Zapracovaná errata a historie

**E043:**25.5.2021, Fascicle5 str.242, odpověď87: přejmenování dalších
markerů z čárkovaného w na `w@`. Naše4B má upravené názvy.

**E044:**18.4.2021, Fascicle5 str.243, odpověď90: v levém příkladu p8
GIVES→GIVEN a BONES→TONES; v p9 WHILE→WHOLE. Původní PS139 má staré
chybné příklady, naše4B435 má všechny tři opravy. Staré p8 opakuje BONES
napříč i dolů; staré p9 vytváří neplatné STIRE a opakuje WHILE.
Nejde o nové nálezy.

Šest lokálních vrstev errat bylo prohledáno podle starých i nových stran,
čísel úloh, pojmů i konkrétních slov. Čtyři současné oficiální originály
mají stejné SHA256 jako archiv. Výsledky i48 kontextů obsahuje
`results/double_words/errata-check.json`.

Historickou závorku nelze uzavřít jen opakováním Knuthova textu na jiných
webech. [Současná vydavatelská ukázka Flower Power](https://www.pennydellpuzzles.com/wp-content/uploads/2019/04/FLW-sample-page.pdf)
má copyright2008 a18 dvojic pětipísmenných hesel. Její text byl dostupný
přes webový čteč; přímé stažení do archivu vrátilo403. Úplný lokální PDF
ani vizuální kontrolu této ukázky netvrdíme.

[Autorizovaný obsah GAMES z října2017](https://www.zinio.com/publications/games-world-of-puzzles/3766/issues/389793/articles)
výslovně popisuje Petal Pushers se40 sedmipísmennými slovy, tedy p20.
To podporuje existenci názvu a varianty, ale nevyvrací historické p16,
o němž píše kniha. Katalog Google Books navíc spojuje Petal Pushers
s Shortzovou knihou z1991. Přesný únorový výtisk1976, italský předchůdce
a počáteční GAMES stránky zatím chybí. Ani vysvětlení rozdílu četností
levých a pravých konstrukcí není samo o sobě kvantifikovaný statistický
výrok; geometrie rozdílné pozice písmen potvrzuje, obecnou převahu pro
všechny možné slovníky však netvrdí.

## Reprodukce a rozpracované běhy

Skripty `check_double_words_small.py` a `check_word_domain_csp.py`
ověřují nezávislé malé modely. Hotové kontroly zbytečně neopakovat.
`check_double_words_checkpoint.py` přijímá pouze dokončené výsledky,
ověřuje hashe a přehrává uložené dvojité modely bez nové enumerace.

`build_double_word_programs.py` uchovává autorovy nezměněné zdroje.
U kombinovaného cutoff changefile byl zastaralý vyhledávací kontext `@x`
sladěn se současným `dlx2.w`; všechny náhrady `@y` jsou doslova shodné.
Originály, upravený kontext, příkazy kompilace a hashe binárek jsou uložené.

Tři plné výčty a nativní fronta mají48h limit na případ; nezávislá CSP
fronta15min na případ. Příkazy, PID, vstupy, průběžné čítače a logy jsou
uložené. Živý proces se nesmí spustit podruhé. Podrobný rozpis viz
`RUN_STATE.json`, statické konfigurace a poslední skutečný procesní snapshot.

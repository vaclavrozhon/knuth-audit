# Úplný průchod 218–224 a zdrojové části Algorithm P

Kontrola 3. listopadu 2026. Přečtena obě znění hlavního textu 108–111,
zadání 151–152 a odpovědí 474–475; draft má odpovídající strany
44–47,87–88,178–179. Přímé obrazy a záznam rozdílů jsou v
`sources/preprocess218_224/source-observations.json`. Nové soubory
v `images/preprocess218-224-*`; části sdílených stran již zobrazené
v předchozích blocích se znovu nevytvářely.

Nový nález **F145**: doslovná mazací smyčka 221 při návratu na první
uzel pokračuje a může nesprávně spadnout do P9. Samostatný třířádkový
důkaz je v [poznámce F145](F145_PREPROCESS_DELETE_LOOP.md). Staré C013
(inicializace hlaviček) a F074 (počet kol 224) se potvrzují beze změny ID.

## Přesný rozsah dosavadních a nových testů

Starých 1 500 vstupů z `results/exact_preprocessing/random.json`,
nativní výpis n=6 a obě náhradní rodiny 224 pro n=2,…,30 jsou pouze
přečteny a opatřeny hashi. Žádný z těchto běhů se neopakoval.

Starý model používal seznam adres místo přepsaných TOP, úplný návrat
z testu blokování a předem sestavený seznam uzlů při mazání. Právě
poslední rozdíl skryl chybu F145. Staré označení „nízkoúrovňové smyčky
220–223“ v X218 bylo příliš široké; předchozí obsah je v ledgeru zachován
a závěr je nyní výslovně omezen na testovaný model.

Nový `check_preprocess218_224_sources.py` přebírá dříve ověřené uložení
uzlů, ale používá skutečný zásobník v TOP, doslovné procházení při
zkracování a výstupu, a opravu F145. Šest nových malých vstupů zahrnuje
dva současně naskládané řádky, sousední počáteční spacery, vnitřní spacery,
duplicitní řádky, oprávněné zhroucení a několik barevných commitů.
Každý má kontrolu všech množin řádků. Úplné odvinutí i předčasný návrat
od konkrétního místa v trojité smyčce mají stejný výsledek; kontroluje
se přesná obnova UP/DOWN/LEN. Celkem 12 drobných běhů, asi 0,023 s,
nice 15. Žádný nový solver, žádný dlouhý brute force.

První běh nového checkeru selhal na **našem** nepodloženém předpokladu,
že po smazání d v (6) nejsou další redukce. Ve skutečnosti e vynucuje c
a řádek bcf blokuje e. Kontrola byla opravena na tvrzení, která kniha
skutečně uvádí: zkrácení adg→ag, adf→af a zachování řešení {1,4,5}.
To není chyba knihy ani důvod zpochybnit F145. Zmrazení checkeru nastalo
až po této opravě a úspěšném celém běhu.

## Obecné důkazy a nízkoúrovňové invarianty

Blokující možnost nemůže patřit do řešení: některá primární položka
mimo tuto možnost by již neměla kompatibilní volbu. Jestliže primární
p vynucuje neobarvené i, každé řešení obsahuje přesně jednu možnost
pro p a v ní také i. Můžeme odstranit i a všechny jeho možnosti bez p.
Opačná rekonstrukce podle původních čísel řádků je jednoznačná. Zůstává
v každém ponechaném řádku primární p a zachovává se identita duplicit.
Každá změna ruší položku nebo možnost, takže počet měnících kol je
nejvýše jejich původní součet. Jednotlivé průchody jsou polynomiální.

**218.** Dvě barvy na vynucené sekundární položce nelze prostě zapomenout.
Pro řádky `p i:1`, `p i:2`, `q i:1` je jediné řešení {1,3}; po smazání
i přibude {2,3}. Pokud p vždy vyžaduje stejnou barvu, lze nejdřív
odstranit nekompatibilní možnosti a pak barevnou položku vypustit.
Tuto silnější redukci Algorithm P neprovádí; nejde o chybu 218.

**219.** Předpokládejme výběr o obsahující i, ale žádné p,q. Možnosti
pro p a q nesmějí použít neobarvené i, proto obě musejí obsahovat
neobarvené j. To je spor, protože p,q se nevyskytují v témže řádku.
Platí i pokud je i v o barevné. Symetricky pro j. Samotné vypuštění
i,j však může přidat řešení: `p i`, `p j`, `q i`, `q j` má dvě řešení,
po vypuštění čtyři při zachování identity řádků.

**220.** Po cover''(i) je zkoušená neobarvená možnost skryta ve všech
ostatních seznamech. Commit proto neodstraňuje její uzly znovu.
Značky COLOR hlaviček vylučují položky patřící do této možnosti z testu
blokování. Je třeba doplnit inicializaci C013. Značky potom není nutné
mazat po každém testu: adresa x se nepřiděluje jiné možnosti; jestliže
při pozdějším zkrácení některá položka z tohoto řádku zmizela, zmizela
z celé aktivní úlohy. Stará značka x tedy nemůže omylem označovat
živou položku mimo tento řádek. Uzly ani adresy se nerecyklují.

Při návratu se obrací pořadí položek, pořadí možností v každém seznamu
i pořadí uzlů v možnosti. Návrat při prvním zablokování začne přesně
před dosud neprovedeným odpojením a postupně odvine dokončený prefix
vnořených smyček. Odkaz na odpověď 122 tento obvyklý postup motivuje;
obecná otázka C031 ohledně jiné úpravy Algorithm C se tím neuzavírá.

**221.** TOP(x) lze dočasně použít jako zásobníkový odkaz: všechny
dotčené možnosti mají neobarvené i a po cover'' chybějí v ostatních
sloupcích. Další commity je tudíž nemohou navštívit a unhide(p) nečte
TOP samotného p. Před trvalým smazáním se TOP obnoví. Je nutná oprava
opakování prvního uzlu F145; detekce prázdného primárního sloupce pak
správně ukončuje nesplnitelnou úlohu.

**222.** Před změnou uzlu p se uloží jeho následující svislý soused p'.
Ponechaný řádek obsahuje S a nulový spacer skáče dopředu na p+1,
dozadu na p−1. Ostatní řádky se smažou z každého sloupce kromě i,
jehož hlavička se vyprázdní nakonec. Podmínka q≠p v této odpovědi
není podmínka q≥x z 221; F145 ji nepostihuje. Vložený spacer má barvu
0, protože vynucené i bylo ve všech ponechaných možnostech neobarvené.

**223.** DLINK(q)=q−1 rozpoznává vložené nulové spacery. Skutečný
svislý uzel nemůže mít souseda na bezprostředně předchozí adrese
(v možnosti se položky neopakují); původní spacer směřuje na konec
následující možnosti, tedy dopředu. Test proto najde právě první
přeživší uzel. Dopředný tisk ignoruje TOP=0 a končí na záporném TOP,
který uchovává původní číslo řádku. P9 vypíše jednu primární položku
bez možností, čímž reprezentuje nesplnitelnost. Zákaz vyprázdnění
ponechaného řádku plyne z invarianty S výše. Výstup je bezpečný na
začátku P3 po úplném vrácení dočasných změn.

**224.** Přijatý n=6 svědek a obecný popis náhradních rodin zůstávají
v `EXACT_PREPROCESSING_NOTES.md`. Čtyři pracovní průchody a pět návštěv
P2 neodpovídají šesti, při žádné z obou konvencí. Není nutné dokazovat
min(n,4) pro všechna n; dřívější experiment to tvrdí jen do n=30.

V barevné náhradní cestě má každá primární položka hodnoty 1,2, ale
P0 pouze 1. Různé hodnoty sousedů se vylučují. Sestupné pořadí
primárních položek dovolí odstranit právě jednu další hodnotu 2 za
kolo; barevné sekundární položky se nevynucují. Pro z vrcholů je tedy
z−1 měnících a jeden závěrečný průchod. V neobarveném převodu
vynucená sekundární položka odstraní ještě další hodnotu na sousedním
vrcholu; sestupné pořadí hran zabrání delšímu šíření v témže kole.
Při z=2n−2 tak je n pracovních průchodů, 4n−5 možností. Pro doslovných
n návštěv P2 včetně závěrečné je z=2n−4 (n≥3). To dává obecný důkaz
lineární náhradní rodiny, bez opakování jejích přijatých testů.

## Hlavní text a známé opravy

Příklady (6) a všech tří vyjmenovaných eliminací z (17) byly přímo
ověřeny krátkými množinovými testy. Tvrzení o absenci redukcí pro
Langforda n>5 a dámy n>3 má následující obecné důkazy:

- Dáma zablokuje v každém jiném řádku/sloupci nejvýše tři buňky.
  Při n≥4 tedy zbývá možnost. Možnosti pro jeden řádek či sloupec
  nemají společnou další položku, takže nic nevynucují.
- Langfordovo číslo h má 2n−h−1≥n−1≥5 možností; dvě obsazené
  pozice vyřadí nejvýše čtyři z nich. Každá pozice t má při n≥6
  nejméně n možných partnerů ve vzdálenostech 2,…,n+1; dvě obsazené
  pozice a již vybrané číslo odstraní nejvýše čtyři partnery. Ani
  číslo, ani neobsazená pozice tedy nejsou blokovány. Jedna pozice
  patří nejvýše dvěma možnostem daného čísla a dané číslo nejvýše
  dvěma možnostem dané pozice; žádný jejich celý seznam nemá další
  společnou položku. Vynucování rovněž chybí.

E011 zahrnuje čtyři konkrétní zásahy: argument p v (103),(105), mez
i>N v P3 a přeskočení barevného prvního uzlu v P5. **V našem PDF ani
draftu nejsou tyto opravy zapracované; v dosavadním checkeru ano.**
Anglická karta je zpřesněna, aby to bylo zřejmé. Autorův známý limit
barevného prvního uzlu zůstává výslovný; pro úplnost redukcí stačí
v každé možnosti dát všechny barevné sekundární položky nakonec.

E099 je publikované vypuštění věty o dalších zjednodušeních, Fascicle5
str107, 7.3.2020. Kniha ji již nemá, draft ji má. Samotné vypuštění
věty netvrdí, že další redukce neexistují. E100 je oprava počtu sudoku
na str111 z 14.12.2022: 30 286 432→30 258 432. Kniha i draft mají
staré číslo. Opravený počet byl již přijat dvěma dokončenými nezávislými
výpočty v X114/E058; žádný se zde neopakuje. E100 je jiná oprava než
pozdější náhrada odpovědi 114 z 2.1.2023.

Šest historických a aktuálních vrstev errat znovu prohledáno, shodné
hashes s předchozím blokem. Přímo zobrazeny all4b str5 a all4f5 str6.
Žádná nalezená oprava F145, C013 ani F074. Fyzický výtisk neověřen.

## Co ještě zůstává v hlavním textu

Úlohy 218–224 jsou celé zrevidované. Hlavní108 je uzavřena; na109
zbývají konkrétní negativní příklady (38) a Soma před(46). Na110–111
zbývají číselné redukce velkých příkladů a historické náklady, navazující
na225, a minimum-cost text od poloviny111. Tyto stránky proto zůstávají
partial. V tomto bloku se žádná další drahá reprodukce automaticky
neoznačuje za vynechanou ani za hotovou; přesný rozsah bude posouzen
u příslušných příkladů. Následuje225 a krátké kontroly těchto redukcí.

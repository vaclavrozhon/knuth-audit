# Recovery §1.4.3.2: celý tracer a všech sedm úloh

X1017 pokrývá všechny výroky212–214, každý řádek krátkého
traceru, všechna cvičení1–7 a celé odpovědi530–531. Původní
obrazy212–214/530–531 přímo zobrazeny;212/530 už v X1016.
Přečteny celý příslušný OCR text, všechny části programs.py,
celé NOTES.md a SELFTRACE.md, selftrace_program.py a všechny
check_trace/check_mutual/check_selftrace/check_self_checkpoint/
check_self_memory zdroje. Přijímané výsledky mají přesné
otisky v results/quality-recovery-trace-errata-2026-11-07.json.

Staré dlouhé běhy se neopakovaly. Při revizi vlastního LOG
se našla ztráta znaménka celého nulového slova. Samostatná
nová verze ji opravuje; důkaz a jediný malý nový kontrolní
balík jsou v§7 níže. Toto je oprava naší evidence/implementace,
nikoli nález v knize. C0039 zůstává výkladový candidate.

## 1. Přesný kontrakt krátkého traceru

MIX základ64≤b≤100, B=b^5, definované paměťové adresy0–3999,
platný počáteční/koncový PC a instrukce. Volání vstoupí do
ENTER s J=start a X=stop. Pole0:2 obou hodnot musí obsahovat
platnou adresu, nikoli libovolně velké číslo. Počáteční A,
indexy, CI a overflow jsou sledované hodnoty. Soukromý kód,
samomodifikované návraty a data traceru musejí být vyhrazené;
jejich zákaz čtení je právě nevyřčená část řešená C0039.

Na CYCLE je v host A další sledované PC=p, v AREG původní
sledované A a v adresním poli instrukce JREG sledované J.
X/I1–I6 a oba skutečné příznaky mají hodnoty sledovaného
programu. Jiná skutečná hodnota J je pouze pracovní vazba;
všechny guest operace, které J pozorují nebo mění, se níže
zpracují zvlášť. PREG po007 uchovává p. Invariant se týká
stavů mezi sledovanými instrukcemi, ne každé pomocné instrukce.

02/03 nastaví stop do TEST a LEAVEX. 04 uloží celé A včetně
znaménka nuly,05 uloží počáteční J do JREG,06 načte start.
007 uloží p a008–009 testují p−stop. Rozdíl platných adres
je velikosti pod4000, tedy výrazně pod B; nevyvolá overflow.
Při rovnosti se A obnoví a LEAVEX předá řízení na stop bez
provedení tamní sledované instrukce. Jinak010–011 načtou
instrukci do INST. SRA2 a STA INST1(0:3) uloží její původní
sign/adresu/index: pět bytů(a1,a2,I,F,C) se posune na
(0,0,a1,a2,I), z nichž STORE do0:3 vybere právě(a1,a2,I).
INST1 nadále má F/C pro ENTA. Zvlášť tedy zůstane zachován
efektivní cíl případného skoku.

014–030 klasifikují všechny kódy. Pro C<38 dá INCA6
hodnotu C−32: při C=32 se obslouží STJ, jinak DECA2
pozná C=34 (JBUS). Pro C≥38 dá DECA9 hodnotu C−47;
C≤47 jsou skoky38–47, větší kódy běžné operace. Jediná
přesměrovaná množina je tedy{34,38,…,47}; není zaměněna
za celý interval34–47 obsahující IOC/IN/OUT.

U běžné operace031 obnoví A,034 vykoná přesnou kopii
instrukce a035 uloží nové A. MIX adresa běžné instrukce
je zakódovaná absolutně s indexem, ne relativně k místu
provedení. Žádná běžná instrukce v této množině nečte J
ani nepřepisuje řídicí PC. Proto přesun na INST mění jen
hostitelské místo fetch, nikoli funkční efekt. 036–038
pak přejdou na p+1. HLT fyzicky zastaví uvnitř034; při
pokračování dokončí035 a následující krok, jak má guest HLT.
Strukturální argument platí i pro definovanou volitelnou
aritmetickou operaci nativního hardware se stejnými vlastnostmi;
uložené emulátorové testy jsou výslovně pouze celočíselné.

STJ019–023 zkopíruje původní0:4 do STA, která má stejnou
adresu, index i F. ENTA v JREG vytvoří kladný dvoubytový
guest J v A, ostatní byty nula. STA proto provede právě
STJ i pro částečná pole a samotné znaménko. 023 přeskočí
035, aby toto pracovní A nepřepsalo uložené guest A.
I1–I6, X, CI i overflow se při této obsluze nemění.

U skoků029–030 nahradí0:3 adresou JUMP a nulovým indexem,
zatímco F/C zůstanou původní. Podmínku vyhodnotí skutečný
hardware s guest registry a příznaky. Neprovedený skok
propadne do035/INCP a zachová guest J. Provedený skok jde
na JUMP; jump instrukce A nemění, proto není třeba znovu
STA AREG, jak říká poznámka4. 040–042 porovnají přesně
dvojici(F,C) s(1,39), tedy JSJ. Pro JSJ ponechají JREG,
jinak043–045 uloží p+1. 046 ENTA s původními adresními
byty a indexem vypočte skutečný cíl; indexové registry se
při skoku nezměnily. 047 vrátí řízení do CYCLE s tímto p.
JOV/JNOV zároveň zachovají skutečný účinek vypnutí overflow.

Pomocné aritmetické hodnoty jsou jen kódy/pole a adresní
rozdíly, nanejvýš řádu b². Nepřetečou celé slovo, žádná
pomocná CMP instrukce tu není, a žádná pomocná instrukce
netestuje a nemaže overflow. CI/overflow jsou proto přesné
po každém skutečně provedeném guest kroku. Původní A se
obnovuje, ostatní registry se mimo skutečný guest kód vůbec
nemění. J se při základním LEAVEX neobnoví; poznámka5
to výslovně uvádí a úloha1 jej řeší.

Krátký tracer má47 slov, ale kniha neprokazuje jeho globální
prostorové minimum. Doporučení preferovat prostor a tvrzení,
že čas obvykle spotřebuje výstup, jsou praktická vodítka.
Výstupní kód v základní verzi výslovně chybí; úloha2 jej
doplňuje. Každá pomocná cesta mezi dvěma definovanými guest
kroky je konečná. Celý program může běžet neomezeně, pokud
sledovaný program nikdy nedosáhne stop/HLT.

## 2. Všechna tři omezení a C0039

Zápis do soukromého stavu může zničit PREG/JREG/návratové
instrukce; nutnost oddělení dokládá i úloha4. Výstupní zařízení
traceru se nesmí používat pro cizí sledované I/O: přidávají
se záznamy a mění se busy stav. I u jiného zařízení může
zpomalení změnit počet úspěšných JBUS nebo čas dokončení
přenosu. Bod(c) není tvrzení rovnosti fyzických časů s běžným
neinstrumentovaným během. Funkční CPU důkaz výše podmiňuje
shodu pozorovaných zařízení; základní tracer je sleduje
v reálném pomalejším čase, není to časový simulátor M.

Doslovný bod(a) zakazuje pouze zápisy. Přímý protipříklad
je přesně starý C0039: tracer na3500, jeho AREG=3546 má
původně+0, guest A=1, X=101, J=100, na100 je LDA AREG.
Přímo tato instrukce načte0. Při vstupu do traceru04 uloží
do AREG číslo1, takže guest načte1 a na101 skončí s A=1.
Nejde o změnu J ani přístup k výstupnímu zařízení. Výrok
o „only three restrictions“ bez implicitní rezervace paměti
tedy není dostačující. Běžná alokační konvence může rezervaci
zahrnovat; proto žádná nová confirmed, C0039 stále candidate
a main_text_status celé1.4.3.2 stále partial.

## 3. Celá úloha1: obnova J

Předpoklad zadání je J=j≠0; jako návratová adresa MIX
platí1≤j≤4000. Proto j−1 je existující adresa. Odpověď
nejprve uloží X a I1 do dvou soukromých buněk, potom I1=j
a A=mem[j−1]. Do X načte instrukci konstanty1H, což je
JMP na následující instrukci obnovy. Tuto instrukci vloží
do j−1 a JMP −1,1 na ni skočí. Tam vykonané JMP nastaví
skutečné J právě na(j−1)+1=j a vrátí řízení za konstantu.
První STA −1,1 obnoví původní slovo držené v A. LD1/LDX
obnoví oba dočasné registry, LDA AREG původní A a závěrečné
JSJ se vrátí na stop bez dalšího přepsání J.

V běžné platné vazbě je j−1 původní volací/skoková instrukce
sledovaného programu. Dočasná buňka nesmí překrývat právě
vykonávané obnovovací instrukce či neobnovené soukromé scratch;
to je součást rezervace programu a traceru. j=4000 funguje
pomocí3999 a vejde se do I1 při každém b. j=0 tuto metodu
neumožňuje a je výslovně vyloučen. CI/overflow se nemění:
jsou tu jen přenosy registrů a nepodmíněné skoky. Znaménka
uložených X/I1/A jsou zachována celými slovy. Je to konečná
sekvence s plnou obnovou paměti, ne neurčitá výzva uložit J.

## 4. Celá úloha2 a její známá oprava

Buffer obsahuje100 slov BUF−99,…,BUF. PTR má před dalším
záznamem−100+10k, kde0≤k≤9. JBUS*(0) před první změnou
bufferu vyčká dokončení předchozího OUT. Deset zápisů je
na BUF+1+PTR,…,BUF+10+PTR, tedy právě další desetice.
Po každém úplném záznamu INC1 10 buď nechá PTR záporné,
nebo při desátém dá0, vyvolá OUT BUF−99(0) a vrátí PTR
na−100. ST1 uloží toto pokračování. Následující zápis
opět chrání JBUS; přenos nikdy nečte přepisovaný buffer.

Po007 je A=p: první částečná STA zapíše0:2 prvního slova.
Po011 je A celá instrukce: uloží se do druhého. Po013 se
načte AREG a I1REG pro slova3/4; ST2…ST6 a STX dají
slova5…10. JREG(0:2) zapíše guest J do4:5 prvního slova.
Všechna registrová slova zachovávají sign, včetně−0; J a
PC mají horní nezapsané byty v prvním slově nahrazené
příslušnými ostatními poli. První slovo je tedy přesně

    +(p div b, p mod b, CI+1+8[overflow off], j div b, j mod b).

Konstanta B4=1(1:1) má hodnotu b^4. První část CON dává
b^4−8 do nízkých čtyř bytů, druhá b^4−1(1:1) dá nejvyšší
byt b−1. BIG tedy je B−8. ENTA8;JNOV buď ponechá8
a vypnutý overflow, nebo při původně zapnutém příznaku
nejprve příznak vymaže a ADD(B−8) jej znovu zapne s A=0.
JL/INCA1/JE/INCA1 přidají podle původního CI0,1,2; žádná
z těchto instrukcí CI nemění a přírůstky nepřetékají.
Výsledný byte3 je přesný a oba příznaky zůstanou původní.

I1 je pro výpis pracovní index, a proto musí být obnoven
**před řádky014–035**, jak opravuje erratum3.9.2008.
Původní obnovení až po031 je obchází STJ větev019–023:
indexované STJ by použilo záporný index bufferu místo guest
I1. Například guest I1=3 a STJ997,1(0:2) má zapisovat
na1000; původní odpověď tam nezapíše. Přijatý starý běh
reprodukuje chybu a úspěch opravy. Po běžné034/035 se nové
I1 uloží do I1REG; STJ tuto větev obchází, ale I1 nemění,
takže I1REG už je správné. Na konci se obnoví i po048.

Při p=stop se před testem může zapsat pouze PC do příští
nepoužité desetice; PTR se nezvýší a žádná instrukce ani
registrový záznam pro stop se nevydává. Úplných deset záznamů
se vždy fyzicky vypíše. Zbytek po skončení je výslovně
vyhrazen doplňkové flush/rewind rutině v odpovědi531.
Ta zná k=(PTR+100)/10 platných záznamů, vyčká starého I/O
a vypíše poslední blok s oznámeným počtem platných záznamů;
při k=0 nový prázdný blok není nutný. Neuvedená volba
paddingu/koncového záznamu není zaměněna za další platné
instrukce. Samotné per-step řešení a všech deset polí je
úplné, není zde předstírán hotový tištěný závěrečný ovladač.

## 5. Celá úloha3 a přesné chování úloh4–5

**3.** V modelu této kapitoly je páska rychlejší výstupní
zařízení a přenese přímo100 MIX slov. Přímý tisk potřebuje
navíc převod každého registru/znamení na znaky a více
formátovacího kódu. Uložený binární záznam lze později
selektivně vytisknout a neopakovat sledovaný běh. To jsou
všechny tři důvody odpovědi; nejsou generalizací na každý
hardware ani důkazem konkrétní číselné rychlosti moderní pásky.

**4.** Po ENTX LEAVEX;JMP *+1 má J=ENTER a X=LEAVEX.
Vnější vstup uloží svůj A a začne sledovat ENTER. Prvních
pět sledovaných instrukcí postupně znovu provádí vstupní
uložení do stejné oblasti. Při prvním sledování CYCLE007
se jeho STA PREG(0:2) vykoná s A=ENTER, které bylo načteno
sledovaným006 z jeho JREG. Tím přepíše PREG, jenž vnější
tracer potřeboval jako adresu právě sledovaného CYCLE.
Vnější INCP čte místo této adresy ENTER a zvýší naENTER+1.
Proto skutečná první posloupnost při ORIG3500 je

    3500,3501,3502,3503,3504,3505,3501,3502,3503,…

Nikoli nekonečně vnořené věrné kopie. Důvod a přesný první
návrat odpovídají celé tištěné odpovědi. Sledovaný kód
skutečně zapisuje do vnějšího stavu a porušuje omezení(a).

**5.** Oddělení dvou statických kopií neoddělí paměť
vnějšího kontextu od paměti, kterou vnitřní kopie následně
„sleduje“. Jakmile B zkopíruje instrukci A zapisující A.TEST,
A.PREG nebo A.AREG a tato instrukce se vykoná, změní
aktivní stav vnější A. Není invariantem, že jsou zachovány
dva nezávislé stroje. Úloha nefixuje jedinou počáteční
konfiguraci J/X a pomocných vstupů, takže nelze přisoudit
jednu periodu všem myslitelným nastavením.

Přesné dokončené řešení má A na1000 a B na2000, plus
1998:ENTX A.LEAVEX;1999:JMP999;999:JMP B.ENTER.
Počáteční A má J=1998 a X=B.LEAVEX. A tedy sleduje
nastavení B a dva skoky, které při vstupu B dají jeho
virtuálnímu J hodnotu A.ENTER=1000. B začne sledovat A.
První křížový zápis je v kroku486: instrukce na B.INST
(2030) jako STX zapisuje do A.TEST(1006). Další zásahy
mění A.LEAVEX/AREG/JREG/PREG. Pro tuto přesnou konfiguraci
je kompletní stav v krocích2539 a2621 shodný, tedy perioda82.

Přijatý check_mutual zahrnuje PC, všech osm celých registrů,
J, oba příznaky a všechny měněné buňky1000–1046/2000–2046;
assert nad množinou writes potvrzuje, že nic jiného měněno
nebylo. Čas není pozorovatelný, protože tento běh nemá I/O.
Determinismus ze shodného celého stavu dokazuje opakování
navždy, ne pouze náhodnou shodu PC. Výsledek je stejný pro
všech37 radixů. Není to klasifikace všech inicializací a
taková klasifikace se zde netvrdí jako část řešení.

## 6. Úloha6: celé oddělení logické paměti

Konkrétní řešení je sestavitelné jako skutečný MIX program.
Aktuální úplný zdroj je parallel/interpretive/
recovery_selftrace_program.py; čitelné ORIG/CON/END obrazy
pro b=64/100 a mapy symbolů jsou v results/recovery-selftrace-
load{64,100}-2026-11-07.{mixal,json} ve stejném adresáři.
Zpětné sestavení dává přesně stejnou paměť a start3000.
Python pouze sestavuje/načítá obraz a pozoruje test; žádná
instrukce běžícího MIX programu není nahrazena Pythonem.

Fyzické0–1999 jsou dvojice(key,value),2000–2999 neměnná
kopie počátečního programu a3000–3537 vykonávaný kód,
data a scratch; zbytek do3999 je+0. Kopie v2000… obsahuje
původní adresy3000…, nejde o relokovaný vykonávaný program.
Počáteční logická paměť V[m] je+0 pro m<2000, fyzická
kopie[m] pro2000≤m<3000 a kopie[m−1000] pro3000≤m<4000.
Je to přesně tentýž obraz, ze kterého běží vnější program.
V tomto důkazu „ROM“ znamená neměnnou oblast, ne nové zařízení.

Na rozhraních VREAD/VWRITE je USED sudé,0≤USED≤CAPACITY,
kde kapacita je kladná sudá≤2000. Každý klíč je jedinečná
číselná logická adresa a jeho hodnota je poslední úplně
zapsané slovo; nepřítomný klíč znamená počáteční obraz.
Invariant není vyžadován v mezikroku mezi zvýšením USED
a následujícím uložením hodnoty téže nerozpracovaně volané
VWRITE. Žádný další lookup do téhož fyzického slovníku
se v tomto mezikroku nevolá.

VREAD002–026 zachová návrat a I1, ověří0≤I5<4000 a
projde klíče v sudých pozicích0,2,…,USED−2. Při zásahu
LDA1,1 vrátí celé slovo včetně sign. Při vyčerpání hledání
rozliší tři intervaly počátečního obrazu; převod horního
intervalu odečte1000 a čte vždy jen fyzické2000–2999.
Záporná nula adresy je číselně0 a CMP ji ztotožní se
stejným klíčem+0. I1 se obnoví z pole0:2 se svým sign,
X a I2–I6 se nikdy nezmění. Doba je O(USED), smyčka
zvyšuje I1 o2 a vždy skončí.

VWRITE027–047 analogicky hledá, zachovává X jako celé
zapisované slovo a I1 jako pracovní index. Při existujícím
klíči mění pouze value, i je-li USED již plné. Při novém
klíči nejprve testuje I1=USED proti CAPACITY. Je-li místo,
zapíše key, zvýší USED o2 a zapíše value. Proto žádné
duplicity nevzniknou. Poslední vložení při USED1998 použije
1998/1999 a dá2000; další nový klíč jde na MEMFULL před
zápisem do2000. I5 je pod4000, I1≤2000 a žádný adresní
registr nepřeteče při b≥64. Hodnoty−0 se nikdy nepřevádějí
na číselnou rovnost, ukládají se celé v X. ROM zůstane
nezměněná. Návraty a obnova I1 jsou soukromé jedné úrovně.

Všechny guest přístupy z M jsou nahrazeny: fetch010 přes
VREAD; MEMORY130/133 přes VREAD a SAVEWORD; druhé čtení
STORE218 přes VREAD; STORE221 přes VWRITE; každý zdroj
MOVE přes MEMORY a cíl přes VWRITE. Právě druhé čtení
STORE musí zachovat X s mezivýsledkem, což VREAD dokazuje.
MOVE při cílovém zápisu uloží/obnoví původní I5 zdroje,
I1 přes VWRITE zůstává cílové. Hranice se rozšíří z3500
na4000. Soukromé register cells a dekódovací stav používají
fyzické adresy **této** úrovně, žádný guest přístup je
nevydává za přímou sdílenou paměť.

Proto se důkaz všech skupin M z X1016 přenese doslovně
na abstraktní paměť V. Guest instrukce, která mění vlastní
kód, zapisuje do slovníku vnějšího interpretu; při příštím
fetch se změna správně vrátí. Další logický interpret má
svůj vlastní USED, dictionary, registry, PC a návratové
buňky jako hodnoty ve V. Nemůže přepsat skutečné aktivní
buňky vnější úrovně. Indukce podle dokončených CPU kroků
a podle konečného počtu úrovní dává oddělené stroje.

Toto řešení nepotřebuje přesný fyzický čas: vlastní CLOCK
je konečné MIX slovo. Při jeho případném přetečení se ve
vnějším dispatchi skutečný pomocný overflow vyčistí; je-li
tatáž INCA sledovanou instrukcí, její overflow se jako u
každé jiné guest aritmetiky přesně zapíše do guest OVTOG.
Program sám jej při vlastním JNOV opět obslouží. Žádná
adresa ani řízení slovníku nezávisí na hodnotě CLOCK.
Není tvrzen neomezený správný čítač uplynulého času.

## 7. Celý výpis, vlastní oprava sign a konečné vyčerpání

LOG dostává uloženou celou INST a I6=PC před zvýšením.
Zapíše24slovný řádek: deset desítkových číslic úrovně0,
deset PC, deset velikosti instrukce a samostatný sign.
CHAR má dost míst, protože b^5−1≤9999999999. Zbytek
LOGBUF zůstává blank. Po OUT čeká JBUS na fyzickou
tiskárnu, než buffer znovu použije. Po návratu fetch znovu
načte INST, aby LOGem použitá A/X nezničila sign potřebný
pro rozbalení instrukce. LOG nemění dekódovací indexy.

Původní vlastní selftrace_program.py používal LDX INST;
JXNN a tvrdil v SELFTRACE.md zachování celého−0. To bylo
příliš silné: JXNN testuje číselnou nezápornost, takže pro
−0 vybral+. Nová odvozená verze místo tohoto místa provádí

    LDX INST
    ENTA 1
    SRAX 5
    LDA PLUS
    JXNN *+2
    LDA MINUS
    STA LOGBUF+6

SRAX5 vytvoří v X číslo+1 nebo−1 s původním sign INST,
nezávisle na jejích bytech. Teprve potom JXNN rozliší sign.
Změna přidává dvě slova, celkový konec3537 je stále bezpečný.
Původní soubor/obrazy/manifesty nebyly přepsány a tvrzení
o starých bězích nejsou přesunuta na nový binární obraz.

Guest OUT na18 ověří celý24slovný buffer0≤M≤3976, pak
VREADem přečte všech24 hodnot do vlastního OUTBUF. VREAD
zachovává pracovní I1, takže po k průchodech jsou přesně
první k slova zkopírována a I5=M+k. Varianta24−k dává
konec; poslední inkrement může dát4000 bez dalšího čtení.
NUM přečte prvních deset desítkových číslic jako úroveň d,
INCA1 a CHAR ji nahradí d+1. Ostatní slova zůstanou stejná.
Pak skutečné OUT/JBUS dokončí přenos a vrátí řízení.

Přeposílání je zde definováno pro vlastní formát záznamu,
nikoli pro libovolný cizí text. JBUS na18 je po dokončeném
synchronním přeposlání false, JRED true; jiné I/O se odmítá.
Vlastní program používá jen tento tisk a jeho čekání, takže
to je uzavřená sada pro samotrasování. Nejde o slib rovnosti
počtu fyzických busy testů s neinstrumentovaným strojem:
logický výstup je dokončen před dalším guest krokem, v souladu
s již výslovným časovým omezením normálního traceru. Všechny
ostatní CPU efekty a pořadí/obsah záznamů jsou přesné.

Úroveň0 tiskne každý krok prvního sledovaného obrazu;
jeho vlastní LOG se při interpretaci přepošle jako úroveň1,
atd. Stejný počáteční obraz na každé úrovni zaručuje, že
první konečný prefix znovu dospěje ke sledování BEGIN.
Každý lookup, jednotlivý CPU krok a tisk skončí za předpokladu
dokončujícího se zařízení. Každý konečný prefix libovolné
konečné hloubky je tedy dosažitelný, pokud mezitím nedojde
k MEMFULL. Vyšší interpretace mezi guest kroky provádí
rozbalení, lookupy a další tisk, proto vnitřní sledované
programy postupují pomaleji, jak úloha požaduje.

Potřebná paměť je neomezená v hloubce: má-li vnitřní úroveň
n obsazených dictionary slov, vnější musela zaznamenat
zápisy do všech těchto n nízkých adres a alespoň jedné
horní pracovní buňky vnitřního programu. Každá z těchto
n+1 různých adres stojí dvě slova. Potřeba U(d) tedy
splňuje U(0)=0 a U(d+1)≥2(U(d)+1), odkud indukcí
U(d)≥2^(d+1)−2. Žádná konečná kapacita nemůže dovolit
všechny hloubky; jiná nekonečná čekací smyčka zde není,
proto nakonec MEMFULL nastane. Jde o obecný argument,
nikoli potřebu doběhnout obrovský experiment2000slov.
Počet dosažitelných úrovní je už touto mezí malý, takže
tag d+1 nepřeteče MIX slovo ani deset číslic. Reprezentované
hlubší MEMFULL nemůže předběhnout nedostatek vnějšího místa:
jeho plná oblast by vyžadovala ještě více míst vnějšího.

Malý nový nice15 kontrolní balík je check_recovery_selftrace.py:
původní chyba−0 reprodukována, nový LOG má222 případů
(37 radixů ×2signy ×velikosti0,1,B−1), celkem4995 skutečných
MIX kroků. Dva nové100krokové prefixy celého relokovaného
obrazu na b=64/100 mají202 porovnání úplného stavu a
55634 skutečných MIX kroků, včetně záznamů úrovní0/1.
Oba nové načítací obrazy navíc mají přesnou shodu po
zpětném sestavení. Obecná správnost a růst paměti výše
nejsou odvozeny z těchto konečných testů.

Starý zdroj má nadále vlastní archivní výsledky:3737
porovnání stavů ve37 radicích; dva celé běhy po4465344
krocích do128slovné meze; přesná hranice1998→2000 a
následující MEMFULL ve37 radicích; třetí úroveň z doloženého
mezistavu po12310 přímých krocích a11549 krocích vnějšího
interpretu. Poslední záznam před neúspěšnou alokací není
označen za dokončený guest krok. Celý dlouhý běh do2000
nikdy nebyl tvrzen ani nyní spuštěn. Tyto výsledky podporují
nezměněné mechanismy, ne přesná nová čísla kroků po opravě LOG.

## 8. Celá úloha7: skokový trace a rekonstrukce četností

Konstruktivní varianta drží logické p a J jako základní
tracer. Skenuje od p první potenciální skok x; před spuštěním
úseku uloží původní slova x a x+1. Instrukci na x ponechá
její podmínku/F/C, ale přesměruje ji na větev TAKEN bez
indexu; na x+1 dá přechod do FALL. Původní adresu/index
skoku uchová zvlášť. Po obnovení registrů/příznaků spustí
přímý úsek. K žádnému dřívějšímu skoku podle skenu nedojde.

V TAKEN zachytí stav po podmínce, spočte původní M podle
indexů, obnoví obě přepsaná slova, nastaví guest J=x+1
kromě JSJ a zapíše právě pár(x,M). Další p=M. Ve FALL
také obnoví obě slova, ponechá předchozí guest J a pokračuje
p=x+1 bez záznamu. Fyzické J změněné pomocnými návraty
se nepovažuje za guest J. Přesměrovaná větev odliší taken
od fallthrough i tehdy, když původní M=x+1. U JOV/JNOV
se zachová jejich skutečný post-condition overflow. A a
indexy skokem nezměněné stačí po obsluze obnovit; flagy
lze uchovat postupem úlohy2 a obnovit explicitním porovnáním
a zapnutím/vypnutím overflow před obnovou A.

STJ je přirozená další hranice skenu: vykoná se virtuálně
se správným guest J a pokračuje dál bez páru. Tak se
nenutí fyzicky obnovovat počáteční guest J=0, které není
běžným skokem nastavitelné. HLT/stop a konec platného
paměťového rozsahu jsou také hranice; nepatchuje se neexistující
x+1=4000. Neplatný pád mimo paměť nemá slíbený běh.

Přímý burst vyžaduje, aby jeho instrukce nevytvořily nový
dřívější skok a nepřepsaly instrumentované místo. Přesně
tuto možnost samomodifikace tištěná odpověď výslovně omezuje.
Pro průhlednost také nesmějí používat právě přepsaná kódová
slova jako významová data; takové čtení musí být virtualizováno
nebo z burstu vyňato, obdobně jako C0039. Toto je přesná
podmínka uvedené konstrukce, nikoli neprokázaný slib pro
každý MIX program. Úloha žádá diskusi efektivní metody;
neprohlašuje úplnou optimalitu obecného self-modifying traceru.

Je-li znám start s, poslední skutečně provedená adresa e
a páry(x1,y1),…,(xr,yr), vykonané intervaly jsou

    [s,x1], [y1,x2], …, [y_(r−1),xr], [yr,e].

Každý interval zahrnuje poslední skokovou instrukci; poslední
interval může být prázdný a musí se tak označit koncovou
informací. Pokud r=0, je pouze[s,e]. Počet vykonání adresy
a je součet indikátorů příslušnosti ke všem těmto intervalům.
Tím je rekonstruován celý tok i četnosti. Samotné páry bez
start/end informace nemohou určit prefix/suffix; tento
předpoklad je ve výsledku výslovný. Méně výstupu plyne
z vypisování jen dvojice adres na provedený skok místo
celého desetislovného stavu na každou instrukci, ne z tvrzení,
že každý program má dlouhé úseky bez skoků.

## 9. Úplná mapa, známé opravy a stav

§1 pokrývá každý řádek212–213 a poznámky1–5; §2 celé
omezení6(a–c) a přesný status C0039; §3 celou úlohu1;
§4 všech deset slov, blokování a opravu úlohy2; §5 celé
úlohy3–5; §6–7 celé skutečné řešení6 včetně rekurze,
mezí a ukončení při nedostatku paměti; §8 celou úlohu7
včetně poslední věty zadání i závorky v odpovědi.

Všechny čtyři vrstvy errat pro212–214/530–531 porovnány;
all1-prepre17/39 přímo zobrazeny. Komentář213 JXL→JXNP
je známá oprava jména,531 přesun LD1 je známá funkční
oprava. Dodatek na212 patří předchozímu simulátoru a je
řešen X1016. C0039 není dotčen žádnou z těchto vrstev.

Všechny části sedmi úloh mají přesné řešení s vyznačenými
předpoklady; staré checked nebylo převzato jako náhrada
důkazu. Vlastní chyba sign byla opravena v nové samostatné
implementaci a stará příliš silná věta o LOG se nepřebírá.
Nový knižní nález0, nová otevřená matematická mezera0,
jedna vlastní oprava a jeden malý cílený kontrolní balík.
Main_text_status partial kvůli starému C0039 je zachován.
Pokračuje celý úvod1.4.4 a všechny jeho pododdíly.

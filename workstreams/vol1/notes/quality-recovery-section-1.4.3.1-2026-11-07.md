# Recovery §1.4.3 a §1.4.3.1: každý výrok a všech devět úloh

X1016 zahrnuje celý úvod200–202, každý výrok a řádek simulátoru
202–212, všech osm původních úloh a celé odpovědi530 i dodatek9
z1.1.2025. Všechny tyto originály byly přímo zobrazeny. Celé
přečteny oba odpovídající OCR soubory, interpretive/NOTES.md,
programs.py, io_program.py, check_simulator.py, check_go_spec.py,
check_extensions.py, check_io.py, výsledky simulator/go-spec/io,
pramenné coverage/downloads a obě předchozí kořenové/sequential
revize. Trasovač začínající na212 není uzavřen tímto blokem.

Přijímáme konkrétní dřívější důkazy po kontrole jejich rozsahu.
Uložené testy jsou podpůrná konečná evidence; žádný se nespustil
znovu. Níže je úplný argument včetně kontraktů a hran. Současné
otisky vůči přijatým manifestům a všechny čtyři vrstvy errat jsou
v results/quality-recovery-simulator-errata-2026-11-07.json.

## 1. Celý obecný úvod200–202

Definice interpretu a strojově podobného jazyka jsou záměrně
neformální: program čte zakódovanou instrukci a provede její
předepsanou operaci. Označení simulator/emulator na202 zužuje
tento pojem na jazyk jiného stroje; není matematickou klasifikací
všech možných programů. Následující konstrukce dokládají uvedené
možnosti, nikoli univerzální optimální prostor nebo výkon.

Pro deset tříd levého a deset tříd pravého operandu je přesně
10·10=100 uspořádaných kombinací. Tabulka indexovaná dvojicí
vybere příslušný program. Nahradíme-li každé volání jednou
instrukcí ad hoc jazyka a správný obslužný podprogram zvolíme
podle jejího kódu, indukce po vydaných instrukcích dává stejnou
posloupnost operací. Bytová reprezentace může být kratší než
plná volání; kniha říká „ideally“ o jednom slově na program.
Nevyplývá z ní, že libovolných sto činností lze zakódovat po
jednom slově nebo že jejich výběr nemá režii.

Totéž dokazuje obousměrný převod mezi posloupností obslužných
volání a interpretovaným kódem na202. Pro větvení se navíc
zachovají cíle a stav řízení. V mezivýsledku víceprůchodového
programu jsou kódy a argumenty smlouvou následujícího průchodu;
první průchod je produkuje a další je vykonává. Není to důkaz,
že instrukční reprezentace je pro každou úlohu nejúspornější.

Přenositelnost znamená, že při shodně implementované virtuální
aritmetice, paměti a I/O se nemění program v tomto jazyce.
Indukce podle jeho kroků převede shodu obou interpretu na shodu
výsledků. Hostitelský interpret včetně vazeb na zařízení se musí
přizpůsobit; tvrzení neodstraňuje nutnost přesné sémantiky.
Diagnostika se vloží do společného bodu mezi kroky a má tam
přístup ke stavu i dalšímu kódu. Má-li obsluha instrukce cenu t
a rozbalení s výběrem d, relativní režie d/(t+d) je malá při
t≫d. To odůvodňuje kvalifikované „often“ o zanedbatelné režii;
simulace jednoduché MIX instrukce níže právě takový případ není.
Mikroprogramy a specializované obvody mohou obsluhy realizovat;
jejich historická rozšířenost/hodnota nejsou nový matematický
výrok a nejsou zde měřeny.

Pramenné a historické věty mají tyto přesné výsledky:

* Obecná historie prvních interpretů201 a tvrzení o jejich
  rozšíření zůstávají v X0225 partial. X0283 obsahuje konkrétní
  primární historické doklady; z doloženého příkladu neplyne
  prvenství ani univerzální výrok o tehdejším programování.
* Odkazy na kapitoly8/10 jsou plány série v daném vydání;
  nejsou předstíraným auditem nepřítomného vydaného pokračování.
* Plné Knuth1963 a Evans1964 výslovně bibliograficky přeskočeny.
  Uložená metadata a neúspěšné403 nejsou kontrola jejich obsahu.
* Randell–Russell1964: znovu přímo obrazy34–35 a navazující
  text36. Objektový jazyk Whetstone skutečně interpretuje
  Control Routine; tento konkrétní obsahový odkaz je doložen.
  Není tvrzena kontrola celé knihy ani jejího celého překladače.
* Autorův tex.web: celý potřebný modul545 popisuje čtyřbytové
  ligature/kerning instrukce a jejich řízení. Část31, modul583,
  výslovně uvádí Fuchs1979 a DVI jako proud operačních kódů
  s argumenty. Tím jsou doloženy obě uvedené role interpretu.
  Jde o uložený následnický autorský zdroj, ne přesnou sazbu1986.
* Oficiální dvips.texi, titul, autorství a oddíl Invoking Dvips,
  výslovně potvrzuje Rokického a převod DVI→PostScript. Nejde
  o ověření historického binárního souboru z doby vydání knihy.
* Původní Adobe text: znovu titul, copyright/first printing
  December1990 a §3.1 na24. Je to druhé vydání s elektronickými
  revizemi1992–1994, nikoli dříve omylem získané třetí1999.
  Překlad vstupu na objekty a provádění operátorů potvrzuje
  popsanou interpretaci. Konkrétní cesta těchto knižních desek
  přes vydavatele a tiskárnu zůstává autorovým svědectvím.

Úvod je tedy celý posouzen, ale jeho přesné historické/pramenné
limity zůstávají otevřené. Nemá vlastní cvičení.

## 2. Kontrakt simulátoru, stavy a čas

Základ bytu je libovolné celé64≤b≤100, B=b^5. Slovo je
znaménko± a pět bytů0,…,b−1. Program/data hosta simulovaného
stroje jsou0,…,3499; samotný interpret a pomocné buňky jsou
od3500 výše. Platná instrukce používá jen předepsané indexy,
pole, adresy a operace. Výsledky mimo definovanou sémantiku
MIX nejsou rozšířeny vlastním hardwarovým pravidlem. Zejména
nepřisuzujeme jediné A/X po přetečení dělení.

Na vstupu řádku010 reprezentují buňky AREG,…,XREG nezáporné
velikosti registrů, SIGNA,…,SIGNX celá čísla+1/−1. Pro I1–I6
je velikost menší než b², pro A/X menší než B. Reprezentace
rozlišuje obě nuly. JREG je nezáporná dvoubytová návratová
adresa; SIGNJ=SIGNZ=+1, ZERO=0. COMPI∈{−1,0,1} reprezentuje
CI a OVTOG∈{0,1} overflow. Hostitelské I6 je další guest PC.
Soukromé buňky nejsou přístupná data simulovaného programu.

Řádky007–009 přičtou adresní pole instrukce TIME do CLOCK.
Na010 tedy CLOCK zahrnuje všechny dokončené guest instrukce.
Při návratu těsně před CYCLE má ještě poslední základní cenu
v TIME: úplný čas je CLOCK+TIME. MOVE přičítá2u za slovo
průběžně. Tento rozdíl je nutný i pro interpretaci starých testů.
Předpokládáme reprezentovatelnost CLOCK, všech READY/DUE a
jejich součtů; jedno konečné slovo není neomezený časovač.

BEGIN v čerstvém obrazu inicializuje TIME, guest OVTOG/COMPI
a PC=0. Ostatní nulové registry a CLOCK pocházejí z CON0;
opakované volání BEGIN samo celý datový obraz neresetuje.
Skutečné hostitelské příznaky se smějí měnit pomocnou prací.
035 JNOV je vždy vypne před obsluhou, případná větev036
doplní přechod. Guest indikátory jsou oddělené buňky, takže
tato pomocná změna nic guestovi nepřidává ani neubírá.

Každá níže dokázaná obsluha buď skončí po konečně mnoha
hostitelských krocích se správným dalším stavem, nebo vstoupí
do uvedené diagnostiky/HLT. Indukce přes počet guest kroků
proto dává správnost libovolně dlouhého definovaného prefixu.
Není tvrzeno ukončení libovolného simulovaného programu.

Názory na nákladnost simulátorů a oba osobní příběhy202–203
nejsou univerzální časové věty. Pětinásobné zrychlení konkrétního
neuvedeného programu nebylo nezávisle měřeno. Řetězec A→B→C
je proveditelný složením sémantických simulací; jeho náklad není
kvantifikován samotnými písmeny A,B,C. Pedagogický účel,
možnost připravovat software před hardwarem a rozdíl oproti
simulaci diskrétních systémů jsou popsané účely, ne nové testy.

## 3. Všechny řádky řízení a pomocné rutiny

010–015 načtou instrukci, uchovají ji v INST, zvýší PC a
složí podepsanou adresu: LDX(1:2) získá její velikost, zatímco
SLAX5 zachová znaménko A z původního fetch. Znaménko−0 se
tak neztratí. 016–019 připustí I=0 nebo1,…,6; u nenulového I
je po DEC2 pracovní index I−6. 020/021 proto vyberou právě
SIGNI a IREGI. SLAX5 a ADD M připojí znaménko a provedou
signed součet. 024 CMPA ZERO(1:3) ověří nulové horní tři
byty, tedy |M|<b², pro obě znaménka včetně nuly. Potom
se výsledek uloží v M a pracovním I5.

027–036 načtou F a C. Přehled204 uvádí operační kód jako
obsah I4; ten je doslova v I4 po029. Pro vstup do obsluh
je nutno používat přesnou hodnotu **I4=C−63 po030**.
Tabulka OPTABLE je ukotvena poslední položkou, takže její
index C−63 vybere právě C-tou z64 položek. Přepis ani důkaz
nepoužívá přehled jako tvrzení I4=C po celém dispatchi.
J4P odmítne C≥64. Byte4 tabulky dá cenu,0:2 adresu obsluhy.
Byte3 je1 právě u LOAD/LOADN/ADDROP nad I1–I6; jinde0.
Každá z64 položek sestavená v programs.py odpovídá tištěnému
vzorci a skutečnému kódu, nikoli pořadí jmen ve slovníku.

MEMORY126–134 uloží návrat, testuje M<0 a M≥3500, a teprve
potom čte. −0 není záporná číselná adresa. LDX načte celé
slovo, ENTA1;SRAX5 vytvoří v X číslo±1 se znaménkem slova,
a LDA(1:5) vrátí jeho kladnou velikost. Pracovní I1/I2 se
nemění. Návratové pole je soukromé a každé volání je dokončeno
před dalším voláním téže rutiny.

FCHECK135–146 dělí nezáporné F osmi s horní polovinou A=0.
Vrátí L=⌊F/8⌋, R=F mod8; proto L,R≥0 a nedojde k dělicímu
přetečení. Kontroly R≤5 a L≤R jsou nutné a dostatečné pro
platné pole. L uloží také do I1; hodnoty L/R se vejdou do
registrů. Všechny neplatné F skončí ve FERROR.

GETV149–158 nejprve provede FCHECK a MEMORY. Při L=0
ponechá znaménko a všech pět bytů; při L>0 nastaví X=+1 a
SLA(L−1);SRA(L−1) vynuluje právě prvních L−1 bytů A.
SRA(5−R) zarovná zbývající výběr vpravo. Jeho velikost je

    v = floor(a/b^(5−R)) mod b^(R−max(1,L)+1)

pro neprázdnou bytovou část; při L=R=0 je v=0 se správným
původním znaménkem. I2=−R. GETAV147–148 vstupuje přímo do
stejné extrakce pro již načtenou dvojici velikost/znaménko;
L/R zůstávají z předcházejícího GETV v COMPARE. Výběr pole
0:0, plného0:5 i všech jedno-bytových polí je tím zahrnut.

## 4. Každá skupina tištěných operací

**NOP a aritmetika.** C=0 se přímo vrátí do CYCLE s cenou1,
ostatní guest stav nemění. ADD/SUB160–165 načtou V a vyberou
I1=0, tedy A. SUB navíc obrátí znaménko V v DEC279–280.
V INC281–288 označme velikosti a,v a jejich znaménka s,t.
Při s=t se uloží (a+v) mod B se znaménkem s a hostitelské
přetečení zachytí OVCHECK. Při s≠t se počítá v−a: je-li
kladné, uloží se v−a a znaménko t; jinak a−v a znaménko s.
Při a=v se větev JANP vybere také, takže nula má staré
znaménko registru. STA(1:5) bere velikost, nikoli host sign.
To přesně reprodukuje signed-magnitude pravidlo včetně−0.

MUL167–175 nastaví obě guest znaménka na st a násobí dvě
nezáporné velikosti. Výsledek je menší než B², proto se vejde
do A:X a STOREAX uloží horní/dolní velikost. DIV177–190
ponechá znaménko zbytku s, podílu dá st a dělí aB+x kladnou
velikostí v. Pro v>0 a a<v je podíl menší než B a zbytek
v rozsahu0,…,v−1; magnitudy jsou přesné. Pro v=0 nebo a≥v
je DIV overflow podle MIX a A/X nejsou definované: žádná
jediná následná hodnota se netvrdí. 191–194 na skutečný
overflow reagují zápisem1 do OVTOG, jinak starý OVTOG
ponechají. Sticky guest příznak se tedy nevypne po pozdější
operaci bez přetečení. Skutečný příznak JNOV vyčistí.

**LOAD a adresní operace.** LOAD201–205 používá index
55+I4=C−8; LOADN196–200 používá47+I4=C−16 a neguje
znaménko. Oba uloží celou vybranou velikost a znaménko.
SIZECHK289–293 kontroluje horní tři byty právě u I1–I6;
příliš velký indexový výsledek není potichu vydáván za legální.
U A/X následuje OVCHECK. V ADDROP265–278 je I1=15+I4=C−48
a F−3 vybere INC, DEC, ENT nebo ENN. |M| je již pod b².
Je-li M≠0, znaménko získá z něj; je-li číselně0,269 vezme
**původní INST**, a270/271 oddělí jeho znaménko. ENT proto
pro ENTA−0 i ENTA−5,1 při I1=+5 dá−0; ENN znaménko
obrátí. U INC/DEC nulový operand stejně nemění znaménko
původního registru, jak plyne z předchozího rozboru INC.

**STORE207–222.** Zdrojový index je39+I4=C−24, tedy0,…,9
pro A,I1,…,I6,X,J,ZERO. Nechť d1…d5 jsou původní byty
paměti a k=max(1,L). Při L=0 se I1 změní na1 a X dostane
sign zdroje; při L>0 zůstane v X sign původní paměti.
SRAX(5−R) odloží pravý suffix d_(R+1)…d5 do horní části
X. Po načtení velikosti zdroje SLAX(5−R) spojí její nízké
byty s tímto suffixem. SRAX(6−k) odřízne nepotřebné horní
byty zdroje. LDA původního slova;SRA(6−k);SRAX(k−1)
vrátí právě prefix d1…d_(k−1). Konečné X obsahuje

    d1…d_(k−1), nízkých R−k+1 bytů zdroje, d_(R+1)…d5.

STX připojí již zvolené znaménko. Při L=R=0 je k=1:
první SRAX5 a následující SLAX5 přesunou celé původní slovo
tam a zpět, vložená bytová část má délku0, mění se jen sign.
Při R=5 je suffix prázdný; při k=1 je prefix prázdný.
STJ automaticky doplní horní byty nulami a STZ používá+0.
Žádná větev nezasahuje mimo M; paměť byla ověřena MEMORY.

**JUMP224–256.** F∈0,…,9 vybere v tomto pořadí JMP,
JSJ,JOV,JNOV,JL,JE,JG,JGE,JNE,JLE. V posledních šesti
případech A=COMPI a spojené JAN/JAZ/JAP větve odpovídají
přesně daným šesti množinám z{−1,0,1}. JOV bere OVTOG,
JNOV bere OVTOG−1; JXNZ zvolí právě požadovanou podmínku.
Obě varianty vždy před skokem nebo pádem OVTOG vynulují.
Větev JMP uloží již zvýšené guest PC do JREG. JSJ tuto
instrukci obejde. MEMORY254 ověří cíl pouze pro skutečně
provedený skok a255 jej přenese do I6. Neprovedený skok
nemění JREG ani původní I6. Změny host J jsou jen vazby
interpretu, nemají přímý význam pro guest JREG.

REGJUMP258–263 vezme velikost registru C−40. Je-li0,
ponechá A=0 bez ohledu na sign; jinak vezme jeho±1 sign.
F−5 adresuje posledních šest větví JTABLE a F>5 je chyba.
Záporná nula proto splní JAZ/JANP/JANN podle číselné nuly,
nikoli test negativity. COMPARE295–309 načte pole V,
SRAX5 připojí sign a uloží je do V. Index XREG+I4 vybírá
registr C−56; GETAV extrahuje **stejné** pole tohoto registru.
Druhé SRAX5 a CMPX porovnají signed číselné hodnoty. Následující
STZ/ENTA/ENNA uloží0,+1,−1 právě podle výsledku; obě nuly
se porovnávají stejně. Guest OVTOG se porovnáním nemění.

Tím je odvozen každý uvedený kód0–4,8–33,39–63. Všechny
tyto cesty mají omezený počet hostitelských kroků. Nepodporované
floating-point operace,5–7 a I/O, načítání, chybová politika
a diagnostický výpis jsou na211 výslovně vynechány. Nejde
o skryté mezery vydávané za nálezy. HLT zarážky v přepisu
jsou pouze místa zastavení testu, ne knižní error routine.

## 5. Úlohy1–4 včetně konkrétní úpravy a hran

**1.** Obě a pouze obě volání FCHECK jsou150 a207, vždy
před MEMORY. Správná konkrétní reorganizace je:

    FCHECK STJ MEMRET
           ... původní136–144 ...
           JG FERROR
           LD2N R
           JMP GETMEM
    MEMORY STJ MEMRET
    GETMEM ... původní127–133 ...
    MEMRET JMP *

GETV a STORE volají jen tento FCHECK; následující samostatné
JMP MEMORY se zruší. Zruší se také LD2N R na156 a212.
MEMORY nikdy I2 nemění a COMPARE mezi GETV a GETAV také
ne, takže I2=−R zůstává správné na obou vstupech extrakce.
Samostatný MEMORY je zachován pro JSJ/MOVE bez kontroly F.
Nové JG a JMP GETMEM stojí totéž jako starý návrat JLE a
následující JMP MEMORY; zmizí druhé STJ, tedy se ušetří2u
na každém kombinovaném volání. Přesun LD2N pouze mění místo
provedení. Jde o konkrétní zlepšení, nikoli globální optimum.

**2.** Odpověď SHIFT530 testuje M<0 a F>5. F−5 vybere
jednu z šesti správných dvojic(4:5), které ST1 vloží do
instrukce s adresou1. Načtené guest velikosti v A/X se při
M=0 vůbec neuloží a guest stav zůstane beze změny. Jinak
po j průchodech loopu jsou A/X výsledkem j jednotkových
posunů daného druhu a I5=M−j. Invariant platí přímo po
SLA/SRA/SLAX/SRAX/SLC/SRC; DEC5 zachová variantu klesající
o1. Po přesně M iteracích se uloží výsledek. Pro posuny
je řetězení jednotek posun oM se saturací nulami, pro rotace
rotace modulo10. Oddělené SIGN buňky se nemění. To zahrnuje
M=0,5,10 i maximální b²−1 a oba signy nul. Guest cena je2u
z tabulky, hostitelská smyčka není tvrzena jako konstantně
rychlá ani optimální pro velké M.

**3.** MOVE530 má po j přenosech I5=m+j, velikost I1=n+j,
F_remaining=F−j a již provedl přesně j sekvenčních operací
mem[n+k]←mem[m+k] ve skutečném pořadí k=0,…,j−1. Nejde
o snapshot: překrytí směrem do zdroje správně znovu čte
již změněná slova. MEMORY ověří zdroj, SRAX5 spojí jeho
velikost a sign. LD1 I1REG;LDA SIGN1 ověří cíl: záporné
nenulové I1 je chyba,−0 je přípustné a STZ SIGN1(0:0)
změní buňku−1 na+1 před prvním inkrementem. Horní mez
n+j<3500 je ověřena před STX. Poté CLOCK+=2, I1REG a I5
se zvýší o1 a F_remaining klesne. Při posledním slově
se smějí ukazatele stát3500; na začátku další iterace F=0
vrací bez přístupu. Pro F=0 není žádný přenos, kontrola
adres ani změna znaménka I1. Varianta F−j zaručuje konec
nebo konečnou diagnostiku. Celý guest čas je1+2F u.

**4.** Mezi003 a004 vložené IN0(16);JBUS*(16) načtou
celých16 slov karty a čekají na dokončení před fetch.
004–006 nastaví guest overflow/CI/PC; čerstvý obraz má
JREG=0. Skutečné host JBUS sice mění host J, ale ne JREG,
takže guest má správný GO vstup. Fyzické čtení na jiném
počítači vyžaduje převod do MIX znaků, jak odpověď upozorňuje.
Nezavádí se neslíbený reset všech registrů při opětovném BEGIN.

## 6. Úloha5: celý přesný rozklad časů

Počítáme od CYCLE do dalšího CYCLE v původním jádru, bez
BEGIN a bez později přidaného TICK. Standardní kontrola
má při035 vypnutý host overflow; to po každé korektní
předchozí obsluze a reprezentovatelném CLOCK plyne z jejího
OVCHECK a omezených pomocných výpočtů. Kdyby byl před úplně
prvním cyklem host overflow libovolně zapnut,036 přidá1u
jednorázové normalizace; následující standardní cykly tím
nejsou ovlivněny. Guest OVTOG může být přitom0 i1.

007–017 při I=0 stojí19u a027–035 dalších15u, celkem34u.
Indexovaná větev018–026 přidá1+1+2+2+2+2+2+1+2=15u.
U GETV je rozklad

    STJ2 + JMP1 + FCHECK28 + JMP1 + MEMORY14
    + J1Z1 + LD2N2 + SRA2 + JMP1 =52u.

L>0 přidá ENTX1+SLA2+SRA2=5u. LOAD mimo GETV:
JMP1+ENT1+STA2+STX2+JMP1+LD1(2)+J1Z1+JNOV1=11u.
Indexový SIZECHK namísto posledního JNOV vykoná CMPA2 a
JE1, tedy přidá2u. Celkem LDA/LDX97u, LDi99u, plus
15u při I≠0 a5u při L≠0. Nativní všechny stojí2u.

ENTA/ENTX s M≠0 mají po dispatchi řádky265–268,270–274,
277,203–205,289–290,191; jejich ceny jsou

    1+1+1+1+1+2+2+1+1+1+2+2+1+2+1+1 =21u.

M=0 přidá LDX INST=2u, indexový SIZECHK opět2u. S34u
tedy ENTA/ENTX55u, ENTi57u, plus15u indexování a2u nulové
efektivní adresy. Nativní cena je1u. Přibližných50:1 je
konzistentní s97/2=48.5 a55/1=55, není přesný univerzální
poměr všech programů. Uvedené8422/178=4211/89≈47.31460674
se zaokrouhlí na47:1. Neuvedený historický testovací program
nelze rekonstruovat; jeho skutečný běh není tímto ověřen.

## 7. Úlohy6–7: celé skutečné MIX řešení a události

Originál211 výslovně omezuje jednotky na16 a18. Kompletní
io_program.py splňuje toto zadání se základním programem,
SHIFT/MOVE/SPEC; poslední uložená adresa3965 je pod4000
a žádná soukromá buňka neleží v0,…,3499. Pro I/O navíc
předpokládáme konečné dokončení fyzických zařízení a platné
buffery bez konfliktu s běžícím programem či jinou akcí.

Každá jednotka má READY, DUE a COMMAND. READY je konec
aktuální akce, DUE její ještě neprovedený přenos nebo−1,
COMMAND plná už vyhodnocená instrukce s I=0. Po každém
CYCLE/TICK buď není přenos čekající, nebo DUE>CLOCK;
jednotka je busy právě CLOCK<READY. Hodnoty−1 jsou mimo
nezáporný časový obor, takže bezpečně nahrazují∞ v odpovědi.

UNIT015–022 převede F=16 na pracovní I1=0 a F=18 na1,
vše ostatní odmítne. IN připustí jen16, OUT jen18, IOC
jen18 a M=0 (posun stránky). BUFCHK vyžaduje0≤M≤3484
pro16 slov karty a0≤M≤3476 pro24 slov řádku; poslední
slovo se tedy vždy vejde do3499. −0 má číselný význam0.
JBUS/JRED připustí obě jednotky a při provedeném neself
skoku používají již dokázaný JMP/JSJ s ověřením cíle.

ISSUE039–051 nejprve WAITem dokončí předchozí akci téže
jednotky. Uloží INST, nahradí0:2 skutečným M a vynuluje
index3; pozdější TICK proto index nepřičte znovu. Pro C=35,
36,37 je28+I4=C−35, což přesně vybírá doby10000,10000,
7500 a zpoždění5000,5000,3750. Ve variantě6 jsou zpoždění
všechna0. Nové DUE=CLOCK+delay, READY=CLOCK+duration;
TICK provede případný okamžitý přenos. TIME=1 přičte příští
CYCLE. Doba zařízení se měří od vydání, nikoli od skončení
hostitelské interpretace.

WAIT052–058 uloží vlastní návrat, a pokud READY>CLOCK,
nastaví CLOCK=READY a zavolá TICK. Tím se vyřídí nejen
akce právě vybrané jednotky, ale i všechny jiné již splatné
akce. Pokud není třeba čekat, žádné nové události kvůli
WAIT nevznikají. Před dalším ISSUE už stará akce téže
jednotky nemůže mít neprovedený přenos.

TICK074–093 uloží pracovní I1 do samomodifikované obnovy
a projde právě indexy0,1. Negativní DUE přeskočí, kladné
ověří vůči CLOCK. Je-li DUE≤CLOCK, uloží COMMAND do
GOIO a **před vykonáním** nastaví DUE=−1. Přenos tak
proběhne právě jednou. Pole4 uložené instrukce nastaví
skutečné JBUS WAITIO, které vyčká fyzického dokončení.
Tento host čas se do guest CLOCK nepřičítá. READY zůstává
beze změny, takže logická jednotka může nadále být busy.
Po obou položkách RESTORE obnoví I1 včetně znaménka
uloženého pole0:2. Další dekódovací I3–I6 se nemění;
host A/X/I1/J/CI jsou pomocné, guest COMPI/OVTOG oddělené.
TICK není reentrantní a fyzické čekání nespouští další TICK.

Pevné pořadí16,18 je správné pro platné současné akce
s nekolidujícími buffery. Při skoku CLOCK přes více událostí
jejich vzájemné paměťové účinky komutují; operace jedné
jednotky jsou WAITem serializované. Neurčené předčasné
přepisování/čtení busy bufferů nemá slíbený jediný hardwarový
výsledek. Poloviční přenos odhalí častou předčasnou práci
s bufferem, ale není detektor veškerého porušení jeho vlastnictví.

JBUS059–068 při CLOCK≥READY pokračuje bez skoku. Jinak
porovná M s I6−1, tedy právě prováděným guest PC=p.
Při různých adresách vykoná normální JMP. Při M=p může
přeskočit všechny opakované testy až na READY: po celém
čekání je stav stejný, každá provedená větev měla JREG=p+1
a žádný guest registr/CI/overflow neměnila. WAIT provede
splatné I/O a ST6 nastaví právě p+1. Poslední test v čase
READY již neskočí, ale stojí1u; ten zůstává v TIME. Jestli
jednotka nebyla busy již na vstupu, JREG se vůbec nemění.
JRED069–073 vybírá přesně doplněk busy a při skoku používá
tentýž JMP se správným guest J. Neoptimalizované opakování
JBUS* by provedlo až tisíce plných dispatchů, což vysvětluje
praktickou poznámku zadání, nikoli tvrzení o zastavení stroje.

V režimu7 je TICK vložen po započtení TIME a před fetch.
Přenos se provede na první takové hranici při dosaženém
polovičním čase; pokud ji instrukce přeskočí, provede se
na jejím konci. To odpovídá požadovanému „approximately“.
Není tvrzena instrukční simulace fyzického přenosu uvnitř
každého guest u. Vynucený WAIT události také vyřídí. HLT
projde WAIT pro obě jednotky a teprve pak započte1u a
zastaví; žádný čekající přenos nezůstane ztracen. Všechno
čekání je konečné za uvedeného předpokladu dokončení zařízení.

Indukce po ISSUE, TICK, WAIT, obou větvích skoků a běžných
krocích zachovává celý stavový invariant. To dokazuje obě
úlohy pro všechny platné konečné prefixy, nejen testované
časové hranice. Odpověď530 k7 doporučuje při mnoha zařízeních
seřazený seznam událostí; to je možnost datové organizace,
nikoli úloha vyžadující zde další zařízení nebo globální minimum.

## 8. Úloha8 a přidaná9

**8.** Vyvrácení je konkrétní: NOP na3499 padne na3500,
takže další010 čte BEGIN=STZ TIME(0:2). Protože TIME je
soukromá adresa≥3500, STORE vstoupí do MEMERROR. Před
zastavením se na010 objeví přesně mezní PC3500, ne větší.
Indukčně běžný krok z p<3500 dá p+1≤3500 a provedený
skok je ověřen MEMORY254 do0,…,3499. PC3500 v původním
obrazu vždy spustí právě uvedenou chybu. Proto odpověď
0≤I6≤BEGIN platí až do předání diagnostice; žádné tvrzení
o libovolném pokračování nevytištěné error routine se nepřidává.

**9.** Nové zadání na212 z1.1.2025 je samostatně přijaté
cvičení, není chybou původního počtu1–8. Naše SPEC nejprve
odečte2 od F; F>2 je chyba, F=2 HLT. U zbývajících0/1
načte velikosti A/X a dalším INC3 rozliší NUM a CHAR.
NUM nechá skutečný hardware převést desítkové číslice
bytů podle MIX a CHAR provede opačné rozdělení. Při
NUM overflow je skutečný příznak zachycen přes STOREAX/
OVCHECK. Soukromé SIGNA/SIGNX se těchto operací neúčastní,
proto zůstávají správně stejné i pro obě záporné nuly.
NUM nemění velikost X, CHAR obě nové velikosti uloží.
F=0 a1 používají opravenou tabulkovou cenu10u.

HLT místo tohoto tabulkového10 přičte přímo1 do CLOCK,
vynuluje adresní pole TIME a zastaví. Při následném pokračování
přejde na CYCLE; cena HLT se tedy nepřičte podruhé. Guest
PC byl zvýšen běžným fetch, guest J/CI/overflow se nemění.
I/O varianta předtím dokončí obě zařízení, jak dokázáno výše.
Všechny větve jsou konečné mimo explicitně zastavený stav.

## 9. Errata, původní testy a konečná mapa

Všechny čtyři současné textové vrstvy porovnány podle stránek
200–212/530 a podle témat/rI4/SPEC/FCHECK; původní obrazy
all1-prepre17, all1/err1 strana8 znovu přečteny. Známé:
202 logo/kurzíva,204 závorky,205 SPEC(1)→SPEC(10),208
zpřesnění komentáře I1,211 uvozovka a odkaz ve3.–5. tisku.
Náš první tisk už má správné1.3.1–26. Dodatek9 zahrnut.
V této části není nová confirmed ani candidate; X0224
zůstává known_erratum, nepřičítá se jako nový nález.

Převzatá konečná evidence má přesně tento rozsah:

* simulator.json:21899 úspěšných diferenciálních případů,
  odděleně1328 diagnostik, šest přesných časů a fetch3499/3500;
  všech37 radixů a úplná pole na krajních radicích, nikoli
  vyčerpání všech možných vstupních stavů.
* go-spec.json:74 vstupů GO,444 SPEC případů a37 diagnostik;
  znaménka, overflow, fyzické zpoždění0/17. To jsou staré běhy.
* io.json:1184 případů ve37 radicích, obou režimech a obou
  hostitelských prodlevách;12 hran polovičního času a8 chyb.
  Oracle je samostatný časový model nad stejným nativním
  emulátorem, nikoli nezávislý formální důkaz emulátoru.
* check_extensions.py podporuje stejný obecný událostní
  argument; jeho jiné výstupy o traceru se tímto neuzavírají.

Souhrnná mapa je úplná: úvod§1 pokrývá každý výrok200–202;
§2–4 každý výrok a řádek202–211; §5 všechna1–4; §6 celou5
včetně komentáře o měření; §7 celé6/7 a odpověď; §8 celé8/9.
Všechny matematické/algoritmické části1.4.3.1 jsou doložené.
X0225 zachovává výslovné historické a pramenné mezery;
autorovy anekdoty a neurčený benchmark nejsou vydány za
ověřená měření. Žádný nový matematický běh, žádná nová
matematická mezera. Pokračování je celá1.4.3.2, včetně
všech sedmi úloh a kompletního samotrasovače.

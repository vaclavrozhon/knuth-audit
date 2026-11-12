# Recovery §1.4 a §1.4.1: každé tvrzení a všech sedm úloh

X1014 přijímá dostatečné předchozí důkazy pouze v jejich přesném
rozsahu a níže doplňuje úplnou mapu, domény a krajní případy.
Přímo přečteny všechny originály186–193 a odpovědi527–528,
celé `parallel/subroutines/notes/subroutines.md`, `notes/sources.md`,
checker `parallel/subroutines/check_subroutines.py`, jeho celý
uložený výsledek a `notes/sequential-subroutines-2026-11-05.md`.
Původní Program1.3.2M a použitá sémantika MIX již mají úplné
rozbory X1002/X1003; neopakují se jejich úspěšné běhy.

§1.4 je na186 pouze nadpis bez samostatné prosy či úloh.
Veškerý další text patří1.4.1. Z193 je přímo potvrzeno sedm
úloh; dodatečné37/38 na527 patří1.3.3, nikoli této sekci.

## 1. Společný kontrakt a celé maximum

Báze b je libovolná povolená64≤b≤100. Kód, jeho vlastní
pomocné buňky, datové tabulky a volající pokračování mají platné
adresy a potřebné navzájem oddělené oblasti. U MOVE se mohou
překrývat zdrojová a cílová data; tento překryv není vyloučen.
Vyhrazený prostor rutiny není součástí přepisovaných dat.
Volající pokračování musí existovat, nejen samotný JMP.
Tyto fyzické předpoklady se nevydávají za nekonečnou paměť MIX.

Při vstupu do těla s rI3=n≥1 se nejprve bez porovnávání nastaví
rI2=n a rA=X[n]. Poté se rI3 sníží na n−1. Před CMPA pro
k>0 obsahuje rA maximum již zpracovaného suffixu k+1,…,n;
rI2 je jeho největší index a rA je celé slovo z tohoto indexu.
CMPA/JGE přeskočí změnu právě pro rA≥X[k]. Jinak ENT2 a LDA
zvolí k a celé X[k]. Tím se invariant rozšíří o k. DEC3
snižuje k o1, J3P pokračuje právě pro k>0. Po n poklesech
je I3=0 a invariant dává požadované maximum i nejpravější
výskyt. Při n=1 se CMPA neprovede; při shodných číselných
maximech se zachová celé pravější slovo včetně znaménka nuly.

Všechny procházené indexy leží0…n a vstupní n se vejde do
dvou bajtů. Data X+1…X+n jsou platná; klesající index tedy
nepřetéká. Nezmění se X,I1,I4,I5,I6 ani overflow. Porovnání
mění CI a skoky mohou změnit J; externí paměť se nezapisuje.
STJ na začátku ukládá návrat do vlastního adresního pole EXIT;
není v rozporu s výslovnou konvencí188 o **externí** paměti.

JMP volajícího na adrese c nastaví J=c+1. STJ EXIT uloží
c+1 dříve, než další skok J změní. EXIT JMP pak nastaví
PC=c+1 a J=EXIT+1. Stejný argument vysvětluje MAX100(1),
kontrakt(4) i abstrakci rutiny jako nové strojové operace.
Původní(4) má n≥1, nikoli OCR n>1. Parametr je proměnná
specifikace; argument je hodnota předaná konkrétním voláním.
ENT1 n/JMP a LD1 =n=/JMP oba nastaví potřebné n; druhý
způsob navíc potřebuje literalovou buňku podle konvence MIXAL.

## 2. Prostor, čas a přesný lokální smysl zachování I3

V modelu187 má m kopií po k instrukcích mk slov. Tělo
podprogramu s uložením a návratem má k+2, volání m, takže

    mk−(k+m+2)=(m−1)(k−1)−3.

Pro m=1 nebo k=1 je výsledek−3; pro k=2 je m−4,
tedy kladný právě při m>4. JMP,STJ,JMP stojí1+2+1=4u;
t dynamických volání přidá4t u. Pro c slov každého volání
a L dalších slov vazby je úspora

    mk−(k+mc+L)=(m−1)(k−c)−(c+L).

To je přesně(3) s konstantou nezávislou na m. Literalové
buňky, další argumenty a zachování registrů je nutné zahrnout
do c/L podle konkrétního sdílení. Kniha tyto idealizace sama
uvádí a nepřislibuje stejnou cenu při libovolné specializaci.

Vložené ST3 3F(0:2) uloží velikost i znaménko původního I3
do adresního pole budoucího ENT3; jeho indexové pole zůstane0.
Proto ENT3 obnoví i −0, nejen číselnou hodnotu. Před tímto
obnovením skončilo hledání s I3=0, takže jeho argument se
nemění. Přibudou dvě slova a2+1=3u na volání.

Pro tvrzení „shortest and fastest“ je přesná posouzená třída
**vložení zachování do právě vytištěného nezměněného MAX100,
při zachování všech ostatních částí jeho kontraktu**. Zde
musí být libovolné staré I3 zachyceno před ENT3 100 a vráceno
po posledním DEC3: jedno vložené vykonání nemůže udělat obojí.
A a I2 přepisuje tělo, zatímco I1,I4–I6,X nesmějí být
zničeny. Pouhé kopírování do takového registru by vyžadovalo
další zachování jeho nezávislé původní hodnoty. V této třídě
je tedy nutný zápis do paměti za nejméně2u a obnovení za
nejméně1u; uvedená dvojice obou mezí dosahuje. Nejde o
nedoloženou globální optimalitu všech možných přepracování
algoritmu maxima, ani o nejlepší čas celého problému.

## 3. Každá varianta vstupu a výstupu,186–190

(5) MAX100 nejprve nastaví I3=100 a pokračuje společným
MAXN. ENT3 nemění J, takže společné STJ uloží správný
návrat. Přímý vstup MAXN naopak použije libovolné zadané
n=I3≥1. Obě větve pak mají přesně invariant z§1.

(6) MAX50 nastaví50 a JSJ MAXN zachová návrat. Obyčejný
JMP na tomto místě by uložil adresu uvnitř obalu namísto
volajícího; nejde o zaměnitelné instrukce. Alternativa úlohy2
uloží J vlastním STJ EXIT ještě před ENT3 50 a JMP 2F,
takže již nepotřebuje zachovat J pomocným skokem.

(7)–(8): volání na c má argument n na c+1. STJ *+1
přepíše adresu následujícího ENT1 a ten nastaví I1=c+1.
LD3 0,1 přečte n. Tělo I1 nepoužívá ani nemění, proto
JMP 1,1 vrací na c+2 a přeskočí argument. Změna I1 je
zde skutečná; na tuto odlišnou rutinu se nepřenáší kontrakt(4).
Číslo n musí být kladné a vejít se do I3; obecné pětibajtové
CON n bez této meze není slibem proveditelnosti.

Dolní obal MAX100 na189 má své vlastní návratové pole1H.
Uloží do něj původní c+1, zavolá MAXN s argumentem100,
MAXN vrátí na1H a jeho JMP vrátí původnímu volajícímu.
Vnitřní změny J a I1 tento uložený návrat nepoškodí.

Dobová technická poznámka o System/360 je nyní doložena
přímo manuálem IBM, Form A22-6821-0,9 a64. Obecné
registry lze používat pro indexování; BAL/BALR do zvoleného
registru ukládá informaci zahrnující následnou instrukční
adresu a pak přejde na cíl. Cíl se určí před uložením,
R2=0 u BALR potlačí skok. To podporuje popsaný způsob
vazby, ne statistický průzkum všech tehdejších programů.
[Primární manuál IBM](https://www.bitsavers.org/pdf/ibm/360/princOps/A22-6821-0_360PrincOps.pdf).
Obě potřebné původní strany byly přímo zobrazeny; celý
manuál není označen za přečtený.

(9): po maximu je I3=0. JANP skočí při max≤0, včetně
obou nul. Jinak STX TEMP uloží X a CMPA s JGE skočí
při max≥X. Zbylá větev tedy existuje právě pro0<max<X
a nastaví I3=1. EXIT JMP *,3 vrací na c+1 nebo c+2
přesně podle zadaných dvou výstupů. Platí i pro X≤0,
n=1, shodná maxima a obě hraniční rovnosti. Externí TEMP
se mění právě při kladném maximu; žádný úplný kontrakt
této varianty nesmí tento zápis zatajit. I3 je příznak
druhého výstupu, ostatní nespecifikované registry i overflow
jsou zachovány. Pro max>0 je konečný CI porovnáním s X;
pro max≤0 zůstává CI z hledání. J je opět EXIT+1.

(10): při A→B→C→A druhé STJ EXITA přepíše původní
pokračování hlavního programu pokračováním uvnitř C.
První návrat A pak již nemá původní adresu k dispozici.
Stejný problém nastává u znovu použitých živých temporárních
hodnot. Známá oprava EXIT C→EXITC opravuje jen symbol
v sazbě; argument přepisování návratu se tím nemění.
Zásobník adres a lokálního stavu by obnovoval poslední
aktivaci první a řeší právě toto vnořené použití; omezení
se vztahuje k vytištěné jediné sdílené návratové buňce.

## 4. Celý návrhový postup a dočasné buňky,191–193

Kroky0 a1 navrhují strukturu a zpřesňují smluvené operace;
slib splnění každé smlouvy dovoluje uvažovat o volajícím
odděleně. Krok2 postupuje od hotových potomků k rodičům.
To je platná kompoziční metoda, pokud kód potomka skutečně
splňuje smlouvu a rodič jeho předpoklady. Samotné pořadí
psaní tuto správnost nedokazuje; text je návrhové doporučení.

Pro acyklické nerekurzivní závislosti lze definovat H(v)
zdola: buňky rutiny v začínají nad maximem H jejích přímých
potomků; H(v) je nejvyšší použité číslo po přidání jejích
vlastních buněk. Každý přímý i nepřímý potomek má menší
čísla než vlastní interval v. Na právě aktivním řetězci
volání jsou tedy intervaly po dvojicích disjunktní. Dva
neporovnatelní sourozenci mohou interval sdílet, protože
nejsou současně aktivní. To dokazuje doporučení TEMPj,
včetně rutiny s více různými potomky. Není to metoda pro
rekurzi, souběžné aktivace nebo nevrácenou korutinu.

Krok3 může změnit rozdělení práce, sloučit opakované
operace nebo odstranit nevolanou rutinu. Doporučení návratů
ke kroku1 výslovně doprovází varování před neomezeným
přepisováním. Tvrzení o úspoře ladění a zkušenostech
autorů nejsou věty o ukončení optimalizace ani dolní meze.
Krok4, sledování prvních dvou provedení instrukce, vhodná
testovací data, diagnostický kód a evidence vlastních chyb
jsou techniky odhalování vad; dvě provedení nepokrývají
všechny stavy a text z nich neodvozuje úplnou verifikaci.

Převzata přesná předchozí pramenná recenze Wirth221–222,
226–227 a DijkstraEWD249; druhý zdroj znovu přečten od
počátku příkladu přes description0/1 a volbu reprezentace
tabulky. Celý výpočet prvočísel není závislostí metodického
odkazu. Přesná sazba knižního přetisku1972 je výslovně
přeskočena. Přijata autorova bibliografická stránka Knuthova
Literate Programming a dříve zaznamenaný přesný rozsah
předmluvy/kapitoly11; lokální25bajtová odpověď údržby webu
se nepovažuje za knihu. Celý chybový deník1978–1991 nebyl
znovu kontrolován. Osobní vzpomínky1964/1980s, tvrzení
„most installations“ a anekdoty o ztracených programech
nejsou nezávisle provedený statistický/historický průzkum.

Turingův původní strojopis18, odstavce4–6, byl přímo
zobrazen; citace i redakční doplnění[bugs] souhlasí.
Datace vzniku/předložení1945/1946 se bez další archivní
evidence nezaměňuje za nález. Odkazy na budoucí kapitolu8
a MMIX jsou plán autora ve vydání1997, nikoli současný
slib vydání. Odkaz1.4.3.1 míří na pozdější příklady;
nezastupuje zde jejich vlastní budoucí důkazovou kontrolu.

## 5. Všechny části úloh1–5

1. Pro MAXN je n=I3≥1, pro MAX100 je n=100 bez omezení
   původního I3. Oba vstupy vracejí maximum a jeho pravý
   index v A/I2 a I3=0. X,I1,I4–I6 a overflow jsou
   nezměněny, externí paměť se nemění. To je celé(4),
   s n určeným právě zvoleným vstupem; řešení527 souhlasí.
2. Celá náhrada MAX50 STJ EXIT; ENT3 50; JMP 2F
   je doložena v§3. Nevstupuje znovu na STJ MAXN,
   které by uložený návrat přepsalo.
3. Pro q=I1≥1 platí maximum z§1 a J=EXIT+1. Pro q=1
   se neporovnává, CI se nemění. Pro q>1 je poslední
   CMPA porovnání dosavadního maxima X[2…q] s X[1].
   CI je greater, pokud výsledné maximum>X[1]; equal,
   pokud maximum=X[1] a jeho pravý výskyt má index>1;
   less, pokud je jediné maximum právě X[1]. Následná
   LDA/ENT2/DEC3/JMP již CI nemění. To dokazuje všechny
   vytištěné větve pro kladné q.

   **C0030 zůstává potvrzeno.** Pro q≤0 není normalizace
   na1: ENT3 a ENT2 nastaví q, LDA čte X[q], DEC3 dá
   q−1 a J3P neskočí. Při platném X+q a reprezentovatelném
   q−1 je tedy(A,I2,I3)=(X[q],q,q−1), CI původní,
   J=EXIT+1 a I1 původní. Pro q=−0 má první ENT3/ENT2
   s indexováním číselnou nulu, I1 si svůj signbit ponechá;
   výrok je číselný a výsledek I3 je−1. Na mezním záporném
   indexu může DEC3 přetéct; to není dodatečně definovaný
   fallback. Svědek q=+0,X[0]=5,X[1]=7 dává(5,0,−1)
   místo vytištěných(7,1,0), ve všech b plně definovaně.
4. Pro n,r>0 klesají indexy n,n−r,…,a, kde
   a=1+(n−1)mod r. Je jich ceil(n/r); poslední pokles
   dá a−r≤0, předchozí indexy jsou kladné, tedy algoritmus
   končí právě po požadovaných prvcích. Suffixový invariant
   z§1 platí nad touto posloupností včetně výběru pravého
   maxima. I3=a−r=(n−1)mod r+1−r=−((-n)mod r),
   protože obě strany jsou jediným zástupcem n modulo r
   v intervalu[1−r,0]. Pro r>n se čte jen X[n]; pro
   r=1 končí I3=0. Indexy ani poslední rozdíl nepřetečou:
   n,r≤b²−1, proto 1−r≥−(b²−2).

   **C0031 zůstává malé potvrzené opomenutí kontraktu.**
   SMAX1 nejprve ENT1 1, ačkoli jeho vstupní podmínka
   původní I1 neomezuje. Již n=1,I1=2 skončí s I1=1,
   neuvedeným ve výstupu528. Konvence188 výslovně říká,
   že neuvedené registry zůstávají. Obecný SMAX I1=r
   zachovává; oprava je pouze uvést I1=1 pro SMAX1.
   Není vadný výpočet maxima ani reziduální formule.
5. ENTA *+2 na c dá A=c+2, JMP na c+1 vstoupí do
   MAX100 a STA EXIT(0:2) tento návrat uloží. A je pak
   stejně nahrazeno prvním datovým slovem. EXIT vrací na
   c+2 bez čtení J, takže vazba funguje i na hypotetickém
   stroji bez J. „Entry conditions: None“ je při provedení
   **celé uvedené volací sekvence**, ne při svévolném
   skoku s náhodným A. Vstupní data jsou100 prvků a
   výstupní účinky odpovídají(4) s n=100. Jiný obyčejný
   registr lze obdobně uložit do pole(0:2); případné
   zachování jeho původní hodnoty se řídí kontraktem.

## 6. Celá úloha6: každá instrukce MOVE a obě překrytí

Použit celý kód528, shodný s MOVE_ROWS v přečteném checkeru.
Označme c adresu volajícího JMP, s původní efektivní
adresu A+I, d původní číselnou hodnotu I1 a f bajt F,
0≤f<b. Volající NOP leží na c+1 a pokračování na c+2.

STJ 3F uloží c+1 do návratu; STA 4F uloží **celé** A;
ST2 5F(0:2) uloží velikost i znaménko I2 do obnovení.
LD2 3F(0:2) z něj udělá ukazatel na NOP. LDA 0,2(0:3)
načte jeho znaménko/adresu/index do dolních tří bajtů A;
STA *+2(0:3) je uloží do budoucí ENTA, včetně indexu.
LD2 5F(0:2) obnoví původní I2 **před** touto ENTA.
Proto ENTA vyhodnotí přesně původní s i pro I=2; I1
se zatím nezměnil, takže i pro I=1. I=0 ignoruje registry,
I=3…6 čte stále původní hodnoty. Nejde o pouhé pokrytí
vzorky pro některé indexy.

Další LD2 načte adresu NOP, LD2N 0,2(4:4) dá−f.
Pro f=0 J2Z přeskočí všechny datové operace i změnu I1.
Obnoví se A a I2 a vrátí na NOP. To je identita nativního
MOVE(0), včetně případného −0 v I1. Pro tuto větev nemusí
s/d označovat přistupovanou datovou buňku; žádná se nečte.
ENTA umí celý součet dvoubajtové adresy a indexu v A,
i pokud by tento součet nebyl platnou adresou paměti.

Pro f>0 DECA 0,2 zvýší A na s+f a STA2F(0:2)
uloží konec zdroje. DEC1 0,2 zvýší I1 na d+f,
ST1 6F(0:2) uloží konec cíle. Při přípustném nativním
přenosu jsou s,d≥0 a s+f,d+f≤4000<64², takže ani
obě uložená adresní pole, ani I1 nepřetečou. Aritmetika
A také zůstává hluboko v pěti bajtech a nezmění overflow.

Před iterací k,0≤k<f, je I2=k−f. LDA*,2 tedy načte
**aktuální** mem[s+k], STA*,2 ji ihned uloží do mem[d+k].
INC2 zvýší I2 o1; J2N opakuje právě, dokud k+1<f.
Indukcí je po každé iteraci paměť stejná jako po témže
počtu kroků nativního vzestupného MOVE. Platí pro d<s,
d=s,d>s i částečný překryv; při d>s se může číst právě
dříve zkopírovaná hodnota, což je správné. Po f iteracích
I2=0, smyčka skončí. Nejde o současnou kopii zmrazeného
zdrojového pole.

LDA4F obnoví A včetně znaménka, ENT2* obnoví I2 včetně
−0, JMP3F vrátí na NOP. Ostatní registry kromě I1/J
nebyly změněny; neproběhne porovnání ani vypnutí overflow.
NOP nezapisuje data a poté přejde na c+2. Pro I=1 má
teď efektivní adresu s+f, která může být4000; NOP na ní
**nepřistupuje do paměti**, takže nejde o neplatné čtení.
Ostatní indexy jsou obnovené a mají původní s.

Celý podprogram má23 slov včetně poslední buňky CON.
Příprava až po J2Z stojí20u, obnovení/návrat4u; pro
f>0 nastavení obou konců6u a jedna iterace6u. Včetně
vnějšího JMP a vykonaného NOP je tedy čas

    26u,             f=0;
    (32+6f)u,        f>0.

Nativní MOVE stojí(1+2f)u; pro všechny f je emulace
skutečně delší. Dodatečný prostor i samomodifikace uvnitř
rutiny jsou dovoleny známou opravou21.8.2001. Není
tvrzena optimální emulace ani přípustnost přenosu přes
její vlastní živý kód/scratch; nutný prostor je vyhrazený.

## 7. Všech pět důvodů odpovědi7

1. Neměnné stránky kódu lze sdílet mezi více adresními
   prostory; jejich odložení nevyžaduje uchovat soukromé
   změny. To vysvětluje možnost hospodárnější správy paměti.
2. Neměnný kód nepotřebuje mechanismus zneplatnění instrukční
   cache po zápisu do instrukcí. Odpadá konkrétní povinnost
   koherence; nejde o změřený univerzální poměr rychlostí.
3. Změní-li se dosud nevykonaná přednačtená instrukce,
   musí se opravit/odstranit její stará podoba, jinak se
   provede neplatná instrukce. Vyprázdnění příslušné pipeline
   je popisované řešení; kontrola závislosti je dodatečná práce.
4. Dva nekoordinované procesy ve stejné měněné kopii MAX
   mohou uložit návraty c1,c2 před prvním výstupem. První
   pak chybně vrátí na c2. To dokládá omezení právě pro
   společnou mutable rutinu bez synchronizace; doslovná
   univerzální nemožnost libovolného samomodifikujícího
   souběžného programu se nepřebírá. Oddělené kopie nebo
   koordinace mění předpoklady praktického tvrzení.
5. Tracer, který předem rozpozná a upraví skoky v neměnném
   kódu, může minout skok později vytvořený přepsáním NOP
   nebo obnovit zastaralou instrukci. Tím je doloženo „can
   defeat“, nikoli nemožnost traceru sledujícího i zápisy.
   Odkaz1.4.3.2–7 bude posouzen ve svém úplném rozsahu.

## 8. Úplnost, errata a zachované hranice

| Celý původní rozsah | Přesný argument |
|---|---|
|§1.4 nadpis186; pojmy, knihovny, maximum186–187|§1,§4; zkušenostní/historické limity výslovné|
|Všechny formule a zachování registru187–188|§2, včetně lokální dolní meze a třídy úprav|
|Kontrakt(4), každý vstup/argument/výstup188–190|§1,§3|
|Celý příklad rekurze190 a každý krok0–4 na191–193|§3–4|
|Celé1,2,3,4,5 a odpovědi527–528|§5; C0030/C0031 zachovány|
|Celá6, všechny indexy, nuly, překryvy, náklady|§6|
|Celá7, všech pět vytištěných důvodů|§7 s přesnými praktickými předpoklady|

Všechny čtyři nynější vrstvy errat byly znovu prohledány;
původní sazba all1-prepre16 přímo zobrazena. Známé změny:
186 stylistické occupying less space;190 symbol EXITC;
193 povolený čas **a prostor** pro MOVE. Změny527 patří
předchozí permutační sekci, žádná zde neopravuje C0030/31.
Nejde o dva nové nálezy ani prohlášení jejich prvenství.

Uložených29520 kontrol,4592 MOVE případů,960 dvouvýstupových
maxim,240 stride a720 kladných CI případů byly přijaty jako
historická doplňková evidence. Checker i celý JSON přečteny;
žádný starý běh se neopakoval. Současné závěry jsou obecné
důkazy nad uvedeným kontraktem, nikoli jejich testovací odhad.
Otisky, rozsah zdrojů a errat jsou v
`results/quality-recovery-subroutines-errata-2026-11-07.json`.

Celé1.4 a1.4.1 jsou **reviewed_with_explicit_limits**.
Žádná matematická část zde nezůstala bez argumentu;
nové matematické běhy/nálezy/mezery0. Zachované zdrojové
a interpretační hranice se neruší. Nejstarší otevřená
matematická mezera svazku zůstává§1.2.1/p16.

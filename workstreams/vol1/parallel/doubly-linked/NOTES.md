# Audit §2.2.5: obousměrné seznamy a simulace výtahu

Stav: technická kontrola hlavního textu a úloh 1–9, 11–12 je dokončena
v níže vymezeném modelu. Úloha 10 je **partial**: chybí vybraný fyzický
výtah a skutečné záznamy jeho jízd. Historické počty instrukcí na s. 296
nelze reprodukovat bez autorova nepublikovaného vstupu `VALUES`.
Žádný nový kandidát errata nezůstal otevřený.

## 1. Inventář a význam stavů

Originál je `books/taocp-vol1-ed3-print1-1997.djvu`; fyzická stránka souboru
má číslo o 15 větší než tištěná stránka. Prohlédnuté obrazy jsou
`images/page-280.png` až `page-298.png` a `page-553.png` až `page-556.png`.
Začátek s. 280 ještě patří předchozí sekci; začátek s. 556 obsahuje konec
odpovědi 12 a pak začíná §2.2.6.

| Jednotka | Zadání/text | Odpověď | Technický stav |
|---|---|---|---|
| Reprezentace (1)–(5), obr. 11 | 280–281 | — | obecný důkaz |
| Model U/E/D, tabulka 1 | 282–287 | — | obecný rozbor + skutečný MIX |
| Agenda, obr. 12, formát (6) | 287–290 | — | invarianty a pole MIX |
| Podprogramy a úplná simulace | 290–296 | 554–555 doplňují E8/D | obecný důkaz + instrukce |
| 1, levý konec deque | 297 | 553 | úplné |
| 2, omezení jednosměrného řetězu | 297 | 554 | úplné, přesný model |
| 3, tři nezávislá tlačítka | 297 | 554 | osm rozlišitelných stavů |
| 4, význam E9 | 297 | 554 | dosažitelný vstup a obě varianty MIX |
| 5, uživatel 10 přichází na patro 2 | 297 | 554 | přesný průběh |
| 6, směrová světla | 297 | 554 | obecný důkaz a událostní model |
| 7, úmyslná chyba `JANZ CYCLE` | 297 | 554 | narušení invariantu i viditelný následek |
| 8, MIX E8 | 297 | 554–555 | tištěný i vlastní skutečný MIX |
| 9, MIX DECISION | 298 | 555 | tištěný i vlastní skutečný MIX |
| 10, experiment se skutečným výtahem | 298 | není | partial; protokol a simulátor připraveny |
| 11, řídké současné změny | 298 | 555 | obecný důkaz a implementace |
| 12, volba datových struktur | 298 | 555–556 | obecný rozbor a haldový důkaz |

Slovo „úplné“ v tabulce označuje rozsah matematického/programového úkolu,
nikoli nové fyzické měření Caltechského zařízení. Kniha sama na s. 283
výslovně omezuje model na hypotézu vysvětlující autorova pozorování.

## 2. Reprezentace a obecné operace

`L(x)` a `R(x)` zde označují levý a pravý odkaz uzlu `x`; `h` je hlavička.
Reprezentační invariant znamená, že pravé odkazy tvoří jediný konečný
kruh přes `h` a všechny datové uzly a že `R(L(x)) = L(R(x)) = x` pro každý
uzel tohoto kruhu. Samotné dvě rovnosti by bez podmínky jediného kruhu
připouštěly více oddělených cyklů; kniha je uvádí jako vlastnost již
definovaného seznamu, nikoli jako úplnou samostatnou definici.

Při odstranění datového uzlu `x` označme jeho původní sousedy `a=L(x)`
a `b=R(x)`. Přiřazení `R(a)=b`, `L(b)=a` nahradí cestu `a,x,b` jedinou
hranou `a,b`. Všechny ostatní sousednosti jsou beze změny. To funguje
i pro jediný datový uzel: `a=b=h` a obě pole hlavičky pak ukazují na `h`.
Teprve poté lze `x` vrátit do `AVAIL`. Hlavička se neodstraňuje.

Při vložení nového, od seznamu disjunktního uzlu `p` za `x` je `b=R(x)`.
Operace `L(p)=x; R(p)=b; L(b)=p; R(x)=p` nahradí hranu `x,b` cestou
`x,p,b` a zachová invariant. Pořadí uchová původní `R(x)` až do jeho
posledního použití. Případ `x=b=h` je prázdný seznam. Počet pěti
změněných odkazů v textu započítává ještě odebrání uzlu z `AVAIL`;
srovnávané tři změny u jednosměrného seznamu používají stejnou konvenci.

Obrázky 11 a 12 odpovídají uvedeným sousednostem a dvěma nezávislým
sadám odkazů. Uzel cestujícího může být zároveň v jedné frontě a v
agendě; sdílí obsah, nikoli linková pole.

### Úloha 1

Bez hlavičky mají `LEFT` a `RIGHT` hodnotu null právě pro prázdný
seznam; jinak `L(LEFT)=R(RIGHT)=null`. Vložení `p` vlevo:

```text
p = allocate(); INFO(p) = value
L(p) = null; R(p) = LEFT
if LEFT == null: RIGHT = p
else: L(LEFT) = p
LEFT = p
```

Odstranění vlevo nejprve hlásí underflow, pokud `LEFT=null`. Jinak
uloží `p=LEFT`, výsledek `INFO(p)`, nastaví `LEFT=R(p)`, a pokud je
nové `LEFT=null`, také `RIGHT=null`; jinak nastaví `L(LEFT)=null`.
Nakonec uvolní `p`. Rozbor prázdného, jednoprvkového a delšího seznamu
dokazuje invariant; pravé operace získáme záměnou stran. Tištěná
odpověď odpovídá tomuto rozboru.

### Úloha 2

Tvrzení platí pro reprezentaci, v níž každý uzel uchovává právě
ukazatel na následující uzel a máme jen konstantně mnoho krajních
ukazatelů. Opakovaná odstranění od konce vyžadují postupně jeho
předchůdce. Takový předchůdce není dosažitelný krokem po odkazu od
odstraňovaného konce; nejhorší případ vyžaduje průchod zbývajícím
řetězem. Konstantně mnoho uložených předchůdců pomůže jen konstantně
mnoha po sobě jdoucím odstraněním. Opačná orientace pouze vymění konce.

Nejde o dolní mez pro všechny struktury s jedním strojovým polem na
uzel: XOR kódování z §2.2.4-18 uchovává informaci o dvou sousedech,
nikoli jeden následnický ukazatel. Také deque ze dvou zásobníků má
jinou reprezentaci a amortizovanou analýzu. Odpověď v knize tento
XOR rozdíl výslovně uznává.

## 3. Přesný model času a invariant agendy

`TIME=t` je simulovaný čas v desetinách sekundy, nikoli počet cyklů
MIX. `FLOOR=f` je patro 0–4. Znaménko `STATE` vyjadřuje směr; jeho
číselná velikost není podstatná. Hodnoty `D1`, `D2`, `D3` jsou booleovské
ve smyslu nula/nenula. Jejich přesnou definici dávají přechody E3–E9;
úvodní fyzické popisy nejsou tvrzení „právě tehdy“, např. E3 nastaví
D1 už během otevírání dveří.

Agenda `WAIT` je kruhový obousměrný seznam budoucích událostí seřazený
neklesajícím `NEXTTIME`. Čas hlavičky je 0. V každé hranici mezi
aktivitami platí:

1. všechny naplánované časy jsou aspoň `TIME`;
2. každá aktivita má v agendě nejvýše jeden uzel;
3. každý čekající uživatel patří do právě jedné `QUEUE[f]` a má v agendě
   U4, případně právě vybranou okamžitou U5;
4. každý cestující ve voze patří do `ELEVATOR`, případně navíc čeká
   na právě vybranou okamžitou U6;
5. aktivní a volné uživatelské uzly jsou disjunktní a dohromady tvoří
   dosud přidělený fond;
6. `ELEV3` má nenulové první slovo právě tehdy, když je naplánována E9.

Při vykonávání jedné aktivity může být aktuální uzel dočasně vyňatý
z agendy. Invariant 3 se proto netvrdí u každé jednotlivé instrukce.
E4 nejprve přesune uživatelskou akci do agendy, potom naplánuje sebe;
uživatel mění frontu až při U5/U6. Kontrola toto přechodné členství
respektuje.

`SORTIN` prochází od pravého konce a zastaví na posledním čase
nepřevyšujícím nový čas. Každý krok zkrátí zbývající konečný úsek;
nejpozději hlavička s časem 0 splní podmínku. Vloží se za nalezený
uzel, takže se zachová pořadí a nové běžné události stojí **za** starými
událostmi téhož času. `IMMED` nastaví nový čas na `TIME` a vloží uzel
hned za hlavičku, tedy **před** ostatní právě současné události.
To jsou součásti modelu: libovolná změna rozlišování shodných časů
nemusí dát stejnou tabulku.

`CYCLE` odstraní levý uzel, nastaví čas na jeho `NEXTTIME`, a přes
instrukci JMP uloženou ve třetím slově pokračuje v příslušné aktivitě.
Naplánovaný `USER1` zaručuje neprázdnost agendy. V našem konečném
vstupu se další `USER1` při zadaném horizontu zastaví skutečnou
instrukcí HLT v `VALUES`; po prázdné agendě se nevykonává neplatný krok.

Pro lokálně konečný vstup (v každém omezeném časovém intervalu jen
konečně mnoho příchodů) nemůže vzniknout nekonečný řetěz okamžitých
aktivit: E3 přejde na kladné čekání 20, E4 po jednom výběru na čekání
25, U5/U6 vrací řízení do agendy a samy další okamžitou uživatelskou
akci nevytvářejí. Ostatní časované přechody mají kladné čekání.
Nekonečně mnoho příchodů s nulovým `INTERTIME` by tento vstupní
předpoklad porušilo. Simulace obecně běží dál, není to algoritmus,
který by měl bez zadaného konce vždy skončit.

## 4. Refinement: pravidla U/E/D versus skutečné instrukce

`book_program.py` obsahuje tištěné řádky 002–296, včetně vynechaných
symetrických řádků 190–195, a odpovědi E8 a DECISION. Vlastní
tabulkový `VALUES` je skutečný podprogram MIX: načte čtyři slova
`IN, OUT, GIVEUPTIME, INTERTIME`, zachová I4–I6, posune ukazatel
vstupu a vrátí se přes uložené rJ. Žádný krok U/E/D nenahrazuje
hostitelský Python. Auditní pozorovatel jen čte stav a počítá
instrukce; jeho výpis není prohlašován za chybějící autorův PRINT.

Formát uživatelského uzlu o čtyřech slovech je:

```text
word0: IN(1:1), LLINK1(2:3), RLINK1(4:5)
word1: NEXTTIME
word2: JMP NEXTINST, tedy adresa v poli(0:2), I=F=0, C=39
word3: OUT(1:1), LLINK2(2:3), RLINK2(4:5)
```

Hlavička `WAIT` potřebuje jen první dvě slova; hlavičky front a vozu
jen poslední slovo. Jejich formální základ je o tři menší než adresa
tohoto slova a používá se výhradně s offsetem 3. Čtyři trvalé uzly
USER1/ELEV1/ELEV2/ELEV3 potřebují první tři slova. Toto překrytí
fiktivních adres není překryvem skutečně používaných polí.

`CALL[f]` má UP v bajtu 1, CAR v bajtu 3 a DOWN v bajtu 5. Čtyři
nulová slova před i za tabulkou dovolují neomezeně vypadající čtyři
součty pro patra mimo 0–4: ve skutečnosti jsou všechny adresy platné
a jejich hodnoty nula. Součet nejvýše čtyř slov je nejvýše
`4*(b^4+b^2+1) < b^5` pro každý povolený základ bajtu `64 <= b <= 100`.
Test kladnosti proto přesně testuje existenci požadavku, bez přetečení.

| Řádky | Obecné zdůvodnění shody |
|---|---|
| 051–063 | INSERT vloží před I1, DELETE odstraní I6; důkaz sousedností z §2 výše, na poli s offsetem 3. |
| 064–087 | IMMED/SORTIN/HOLD a DELETEW používají nezávislá pole s offsetem 0; důkaz pořadí z §3. |
| 088–096 | CYCLE1 uloží pokračování bez čekání; HOLDC uloží pokračování a naplánuje HOLD; CYCLE dispatchuje nejbližší událost. |
| 098–114 | USER1 se nejprve znovu naplánuje, pak se vezme volný uživatel nebo čtyřslovný uzel z fondu; IN/OUT a celý JMP se inicializují. |
| 115–143 | Porovnání IN s I4 rozliší cizí patro; rovnost NEXTINST s E6 rozliší zavírání a DELETEW odstraní právě naplánovanou E6; D3 rozliší čekání s otevřenými dveřmi. Ostatní případy nastaví příslušný hall-call a podle D2/E1 zavolají D. |
| 144–159 | U3 vloží na konec fronty. U4 buď uživatele odstraní, nebo naplánuje další kladné čekání. U6 má společný kód odstranění a návratu do AVAIL; uvolněný uzel už není v agendě. |
| 160–172 | U5 přesune uživatele do vozu, nastaví CAR[OUT]; jen při neutrálním stavu určí znaménko OUT−FLOOR a přesune E5 na čas +25. E5 v tomto případě existuje, protože D1 drží dveře otevřené. |
| 174–200 | E1 je uložený marker, nikoli běžně vykonávaná instrukce. E2 testuje všechny požadavky před vozem, případně jen CAR za vozem, obrátí znaménko nebo vynuluje stav a vynuluje volání současného patra. |
| 201–213 | E3 případnou starou E9 odstraní podle markeru ELEV3, vloží E9(+300), E5(+76), nastaví D1/D2 a E4(+20). Při znovuotevření z E6 už E5 v agendě není. |
| 214–235 | E4 prochází vůz od nejpozději nastoupivšího, vybírá OUT=FLOOR; teprve potom levý konec fronty. Prázdná fronta se pozná tím, že její hlavička ukazuje sama na sebe; u neprázdného kruhu žádný datový uzel nemá vlastního následníka. Vybranou U4 zruší a U5/U6 vloží IMMED. Bez uživatele nastaví D1=0,D3!=0. |
| 236–244 | E5 při D1!=0 čeká dalších 40; jinak vynuluje D3 a naplánuje E6(+20). |
| 245–259 | E6 maže právě CAR a hall-call odpovídající znaménku stavu (oba při neutralitě). D se volá jen pro neutrální stav. Zbývající neutralita vede do E1, jinak se zruší aktivní E9 a po 15 následuje pohyb. |
| 260–292 | E7/E8 upraví patro, čekají 51/61, a testují přesně CAR, souhlasný hall-call, nebo domácí/opačný hall-call bez požadavků dále. Zastavení čeká dalších 14/23 před E2. |
| 293–296 | E9 vynuluje vlastní marker a D2 a volá D. Ostatní seznamy zůstávají platné. |

Každý uvedený lokální krok zachová invarianty z §3 a realizuje přesně
příslušný přechod U/E/D. Indukce podle počtu dispatchovaných událostí
proto dává shodu libovolného konečného průběhu při platných vstupních
a strojových mezích, ne pouze pro otestované příklady.

Při opakování U4 používá program aktuální globální `GIVEUPTIME`, který
mohl mezitím změnit nový U1. Pro první rozhodnutí je doba každého
uživatele správná. Další doba už pouze udržuje členství v agendě,
zatímco výtah obsluhuje jeho patro; musí být kladná, jak odpověď 7
výslovně předpokládá. Nevykládáme ji jako uložený neměnný atribut uzlu.

### Přesné časy podprogramů

Časy níže počítají od vstupu do podprogramu do návratu, bez volajícího
`JMP`. `k` je počet prohlédnutých předchůdců v SORTIN včetně posledního,
na němž porovnání skončí.

| Podprogram | Čas v jednotkách u |
|---|---:|
| INSERT | 13 |
| DELETE, DELETEW | 11 |
| IMMED | 19 |
| SORTIN | 16 + 5k |
| HOLD | 18 + 5k |

Například DELETEW má STJ(2), dvě načtení(4), dvě uložení(4), návrat(1).
Rozvinutí čtyř vlastních instrukcí do CYCLE ušetří volající JMP(1),
STJ(2), návrat(1), tedy přesně 4u, jak kniha uvádí. Každý další
průchod SORTIN stojí LD1(2)+CMPA(2)+JL(1)=5u. Testy ověřují i případy
prázdné agendy, shodných časů a vložení na oba konce.

Historické hodnoty 1432 průchodů smyčkou SORTIN, 437 volání SORTIN,
407 CYCLE, 32 DECISION a 142 průchodů smyčkou E4 patří nepublikovanému
vstupu 26 uživatelů do času 10000. Nejsou tvrzeny jako naše reprodukce.
V `elevator-evidence.json` je vlastní úplný profil všech tištěných
řádků pro přesně uvedený vstup. Oprava rozsahu E4 na 217–219 je známá.

## 5. Úlohy 3–7: obecné důvody a konkrétní průběhy

### 3. Osm odlišitelných kombinací

Na vnitřním patře `j` označme tři dosud nevyřízené požadavky `u,c,d`
(nahoru, z kabiny, dolů). Nestačí jen ukázat, že dva typy tlačítek někdy
působí odlišně: pro dolní mez tří bitů lze rozlišit všech osm kombinací.
Experimentátor může tlačítka stisknout nezávisle před příští obsluhou
patra, přičemž pomocným požadavkem podrží vůz na cestě jinam.

* Bit `c` rozliší E2 na vhodném jiném patře `k`, když vůz právě jel
  směrem od `j` a za `k` už žádná volání nemá. Pokud `c=1`, E2 ihned
  obrátí směr k `j`; pokud `c=0`, přejde do neutrality, bez ohledu na
  `u,d`. Pro `j=1` lze zvolit `k=2` a příjezd vzhůru; pro `j=2,3`
  lze zvolit `k=j-1` a příjezd dolů. Směr se dá přečíst ze šipek uvnitř
  kabiny (s. 282), nebo rozlišit nástupem uživatele mířícího dál od `j`.
  Pomocný CAR[k] zajistí zastavení na k a je zde vyřízen.
* Chceme-li rozlišit `u` při jinak libovolných `c,d`, necháme vůz
  obsloužit `j` cestou **dolů**, s pomocným požadavkem na patro 0.
  E2 zůstane v sestupném stavu a E6 vymaže `c,d`, ale zachová `u`.
  Následná cesta vzhůru s pomocným požadavkem na patro 4 zastaví na
  `j` právě když `u=1`. Existující vyšší požadavek zabrání speciálnímu
  zastavení na domácím patře 2 bez UP/CAR.
* Symetricky obsluha `j` cestou vzhůru s cílem 4 vymaže `u,c`, ponechá
  `d`, a následující cesta dolů s cílem 0 zastaví na `j` právě pro `d=1`.

Pro každé dvě různé trojice zvolíme z těchto pokusů ten, který čte
jejich rozdílný bit. Pomocní cestující během měření nenastavují další
požadavek na j. Jde tedy o osm budoucím chováním rozlišitelných stavů;
deterministický model pro ně potřebuje alespoň `ceil(log2 8)=3` bitů
informace. To nevyžaduje tři konkrétní fyzická relé ani konkrétní
paměťové uspořádání. Příklady v tištěné odpovědi odpovídají jednotlivým
rozlišením, zvláště rozdílu CAR versus hall-calls při E2.

### 4. Dosažitelná změna pořadí zastávek kvůli E9

Použijeme uživatele `(čas, IN, OUT, trpělivost)`:

```text
(i,0,2,10000) pro i=0,...,11
(600,2,4,10000)
(700,0,1,10000)
```

Jde o vstup z běžného počátečního stavu, nikoli o nedosažitelnou ručně
vloženou konfiguraci. Dvanáct prvních lidí vystupuje na patře 2:
E3 začne v čase 656, jednotlivé výstupy jsou 676,701,...,951,
první nový nástup až 976. Po celou dobu výstupů je STATE neutrální.
E9 v čase 956 vybere čekající volání na patře 0 a nastaví směr dolů.
Uživatel mířící na 4 při nástupu v 976 už směr nepřepíše. Následující
zastávka je 0 v čase 1192.

Bez E9 zůstane stav v 976 neutrální, nový uživatel určí směr nahoru
a další zastávka je 4 v čase 1152. `no_e9=True` odstraní skutečně
plánování i rušení E9 z MIX, nikoli jen jeden příkaz DECISION; model
nezávisle ignoruje celou aktivitu. Oba programy se shodují se svými
modely pro všech 37 základů. Obecný důvod je čas `20+25*n` do prvního
nástupu po n výstupech: pro `n=12` je 320>300. Odpověď knihy je správná.

### 5. Změněný příchod uživatele 10

V první části tabulky změníme pouze IN desátého uživatele z 0 na 2,
OUT=4 i čas 1048 zůstanou. V E2 v 1063 není žádné volání pod patrem 1;
všechny dosavadní CAR jsou právě pro patro 1. E2 je smaže a nastaví
neutralitu. Po výstupech čtyř dosavadních cestujících nastoupí uživatel
7 v 1183 a jeho OUT=2 určí směr nahoru. Uživatel 8 s OUT=0 nastoupí
až potom, proto už určený směr nezmění. To dokazuje výsledek odpovědi;
zkratku „nobody on board“ chápeme pro okamžik volby při prvním nástupu,
nikoli jako tvrzení, že kabina byla fyzicky prázdná už při E2 v 1063.
Nejde o nový kandidát errata.

### 6. Světelné ukazatele směru

Označme `eligible = ((OUT<IN and STATE!=UP) or
(OUT>IN and STATE!=DOWN))`. V U2 a U4 nahradíme test `FLOOR=IN`
testem `FLOOR=IN and eligible`; jde přesně o opravu z 2. května 2024.
V E4 se z fronty vybírá **první způsobilý** uživatel, nikoli nutně
její první člen. Pokud není žádný, provede se větev bez uživatele.
Je-li STATE neutrální, je způsobilý každý, protože OUT!=IN.

Výstupy mají nadále přednost. Indukcí každý nastupující jede buď ve
směru stávajícího stavu, nebo sám určí nový stav při neutralitě.
Přeskočení nezpůsobilých uchovává relativní pořadí ostatních; jejich
U4 zůstává naplánovaná. Směrem neslučitelný příchod při zavírání
nesmí znovu otevřít dveře a při U4 nesmí být chráněn před odchodem
jen tím, že vozidlo stojí na stejném patře. Tím jsou ošetřeny všechny
tři upravené větve. V simulaci tabulky nastoupí uživatel 8 v 1183;
uživatelé 7 a 9 počkají na pozdější správný směr. Úloha žádá změny
algoritmu, nikoli nový MIX; tyto změny jsou implementovány v modelu.

### 7. Úmyslná chyba z knihy

Po vyjmutí U4 agendou už její uzel v WAIT není. Pokud uživatel zůstává
ve frontě, správný návrat U4A jej znovu naplánuje. Chybný skok CYCLE
jej nechá pouze ve frontě. Pozdější E4 se přesto pokusí o DELETEW;
jeho staré odkazy už nemusí označovat současné sousedy.

Konkrétní vstup: čtyři uživatelé `(i,2,4,100)`, `i=0,1,2,3`,
a pátý `(20,0,1,100)`. U4 čtvrtého v čase 103 nastane během obsluhy
patra 2; chybná verze jej nenaplánuje znovu. V čase 115 jej E4 vybírá
a jeho staré odkazy obejdou pátého uživatele, jehož U4 má být v 120.
Správná verze nechá pátého v 120 odejít. Chybná verze jeho U4 nikdy
nevykoná a nakonec jej nechá nastoupit až v 774. Tato viditelná odchylka
i první selhání invariantu v 103 jsou uložené v evidence JSON.
Trpělivost 100 splňuje výslovný předpoklad odpovědi. Jde o reprodukci
záměrně chybného programu, **nikoli nový nález**.

## 6. Úlohy 8 a 9: vlastní skutečný MIX a obecný důkaz

`solutions.py` definuje vlastní E8 s explicitním cyklem přes nižší
patra a vlastní DECISION s přímým hledáním `j=0,...,4`. Export
`results/own-solutions-complete.mixal` je jejich sestavitelná integrace
do celého výtahu s vlastním VALUES; doslovná odpověď je samostatně
v `results/book-complete.mixal`. Oba exporty mají END a skutečné HLT.

### 8. E8

Vstupní E8 nejprve sníží patro a po 61 jednotkách testuje dosažené
patro f. `CAR[f] or DOWN[f]` znamená zastavit. Jinak je zastavení
možné pouze při `f=2 or UP[f]`; potom explicitní cyklus kontroluje
`f-1,...,0`. Invariant cyklu říká, že už prohlédnutá vyšší část tohoto
rozsahu má nulová volání. Nenulová hodnota ihned vrací E8, dosažení
indexu -1 dokazuje nulovost celého rozsahu a naplánuje E2 za 23.
Konečnost plyne z každého snížení indexu. Tištěné čtyři součty dávají
stejný predikát díky nulovému okraji CALL. Znaménko STATE se nemění.

Řádek 292, `JMP E2A`, je už vytištěn v hlavním textu; známá oprava
zadání mění 277–292 na 277–291. V běžícím programu je samozřejmě 292
zahrnut právě jednou.

### 9. DECISION

Na začátku se uloží návratová adresa. Nenulový STATE znamená okamžitý
návrat. Marker E1 se testuje podle `ELEV1+2(0:2)`, nikoli podle
přítomnosti hlavního uzlu v agendě. Při E1 platí FLOOR=2. Nenulové
CALL[2] má prioritu a naplánuje E3 za 20 bez změny stavu.

Jinak cyklus testuje patra vzestupně a vynechává FLOOR. Jeho invariant
je nulovost všech dosud prohlédnutých přípustných pater. První nenulové
patro je tedy požadované minimum j. Při neúspěchu se j=2 dosadí právě
při návratu do E6B, tedy pro volání z E6; jinak se nic nemění.
`STATE=j-FLOOR` má požadované znaménko, včetně nuly při domácím patře
a absenci dalších volání. Byl-li výtah v E1 a j!=2, uloží pokračování
E6 a vloží hlavní událost za 20. I6 se uloží a obnoví, FLOOR se nemění.
Vlastní podprogram užívá dvě vlastní pomocná slova a vlastní místo
návratu; žádné z nich nekoliduje s vnořeným HOLD. Není reentrantní,
což odpovídá sekvenčnímu dispatchování modelu.

Tištěná verze hledá tutéž hodnotu pomocí I1=j−4. Zvláštní dvojice
`J5NZ *+2; JANZ 1B` přeskočí současné patro, když je nalezená hodnota
nenulová; při nouzovém j=2 a nulovém A naopak dovolí nulový stav.
`JXNZ` používá dříve uložený rozdíl markeru od E1. Obecný rozbor tedy
pokrývá i tuto méně přímočarou implementaci.

Vyčerpávající doplněk testuje pro základ 64 všech 8192 kombinací
třinácti skutečných tlačítek: nejnižší patro nemá DOWN, nejvyšší UP.
DECISION se testuje pro všechna patra a obě relevantní návratové
situace, navíc pro dormanci na patře 2. E8 se testuje pro každé možné
dosažené patro 0–3. U libovolných syntetických kombinací se testuje
jen lokální volba E8; program není nucen pokračovat mimo budovu z
globálně nedosažitelného stavu. Ostatní základy testují jednotlivé
bity, jejich doplňky, všechny nuly/jedničky a nenulové stavy obou
znamének. Důkaz výše se na výčet nespoléhá.

## 7. Úloha 11: řídké současné přiřazení

`V[k]` je stará hodnota, `NEWV[k]` připravovaná hodnota. `LINK[k]=0`
znamená, že k v tomto kroku ještě nebylo změněno. `HEAD=-1` označuje
prázdný seznam změn; skutečné indexy jsou 1 až n, takže -1 ani 0
nemohou kolidovat s platným indexem.

Při prvním zápisu k se uloží `LINK[k]=HEAD`, `HEAD=k`, `NEWV[k]=value`.
Při druhém zápisu do stejného k se ohlásí chyba. Invariant seznamu:
obsahuje právě jednou každý dosud zapsaný index; právě tyto indexy mají
nenulový LINK. Vložení zachová invariant, protože nový index ještě
nepatří do seznamu a původní HEAD je buď platný index, nebo -1, nikdy 0.

Všechny pravé strany čtou V, které se během přípravy nemění. Na konci
se uloží starý HEAD, HEAD nastaví na -1 a seznam projde. V každém uzlu
se provede `V[k]=NEWV[k]`, před smazáním LINK se uloží následník, LINK
se vynuluje a pokračuje se následníkem. Seznam je konečný a bez cyklů,
proto se přesně s změnami provede s kroků, kde s je počet změněných
proměnných. Každý nezměněný V zůstává původní, každý změněný má svou
připravenou hodnotu, všechny LINK jsou opět 0 a další krok může začít.

Po jednorázové inicializaci O(n) je práce O(s) na krok, plus vlastní
výpočty pravých stran; paměť je O(n), jak zadání dovoluje. Rozptýlené
proměnné mají trojici polí V/NEWV/LINK v příslušných uzlech a HEAD je
ukazatel, nikoli nutně číselný index. Detekce druhého zápisu je o něco
přísnější než pouhá detekce dvou různých hodnot, ale splňuje zadání i
tištěnou odpověď. Chceme-li dovolit opakování stejné hodnoty, při
nenulovém LINK porovnáme NEWV a při rovnosti nic neměníme.

`check_sparse_updates.py` implementuje právě tištěnou přísnější
variantu a testuje 77632 posloupností včetně výměny dvou hodnot,
cyklických přesunů, konfliktů a opětovného použití nulovaných LINK.

## 8. Úloha 12 a zdrojové meze

WAIT potřebuje pravostranné hledání místa pro vložení, levostranný
výběr nejbližší události a také odstranění konkrétního uzlu při rušení
aktivity. QUEUE potřebuje kromě FIFO odstranění libovolného čekajícího
uživatele při U4. Obousměrné odkazy dávají pro poslední dvě operace
konstantní čas z adresy uzlu. Jednosměrný řetěz by při takovém rušení
musel dohledat předchůdce, obvykle lineárně. Sekvenční pole potřebuje
přesouvání nebo další nepřímé indexy a volná místa.

ELEVATOR se pro výstup stejně prochází; během hledání lze uchovávat
předchůdce a pak odstranit nalezený uzel. Pořadí opačné k nástupu
lze udržovat vkládáním na začátek jednosměrného řetězu. Proto právě
ELEVATOR lze převést bez zásadní změny asymptotické práce.

Poznámka o prioritní frontě je správná s vhodnou strukturou. Binární
halda má výšku floor(log2 n), protože na hloubce h potřebuje nejméně
2^h pozic. Vložení probublává nejvýše po jedné cestě vzhůru. Odstranění
minima nahradí kořen posledním prvkem a probublá dolů. Pro odstranění
libovolného známého uzlu je navíc potřeba mapa uzel→pozice; po náhradě
posledním prvkem stačí jedna cesta nahoru nebo dolů. Každá výměna
aktualizuje mapu v O(1), takže všechny tyto operace mají O(log n)
nejhorší čas. Samotná halda bez mapy by slib pro libovolné rušení
nesplňovala. Stabilní shody časů lze doplnit pořadovým klíčem a
okamžité aktivity lze zpracovávat zvláštní frontou před časovanými.

Přímá externí citace na s. 296 je Knuth, *An Empirical Study of FORTRAN
Programs*, Software—Practice and Experience 1 (1971), 105–133, DOI
10.1002/spe.4380010203. Primární článek je uložen ve `sources/`; originální
obrazy jeho s. 105–107 byly prohlédnuty. Bibliografii potvrzuje i primární záznam vydavatele.
Viz `SOURCES.md` pro adresy, relevanci a přesný rozsah čtení.

Křížový odkaz na profilování §1.4.3.2-7 je pokryt dřívějším zmrazeným
blokem `parallel/interpretive/`; tato práce jeho model ani evidenci
nemění. Odkaz na §5.2.3 je podpůrný pro obecný haldový argument výše,
ne prohlášení, že byl nově auditován celý svazek 3.

## 9. Strojové meze a co konečné testy neříkají

Předpoklady: `0<=IN,OUT<=4`, `IN!=OUT`, kladné GIVEUPTIME,
nezáporné INTERTIME, lokálně konečné příchody; všechny plánované časy
se vejdou do kladného MIX slova. Obsah CALL má pouze nuly/jedničky
v uvedených polích a kladné znaménko. Každý používaný uzel i celé jeho
pole leží v paměti, fond je disjunktní od programu a vstupu, každý
rušený uzel je právě jednou členem správného seznamu.

MIX má 4000 slov; poslední čtyřslovný uživatelský uzel může začínat
na 3996. Pole adres i indexové registry se vejdou do dvou bajtů,
protože `4000 < 64^2`; pro vyšší základ je rezerva větší. `TIME+delay`
musí být nejvýše `b^5-1`; přetečení by zničilo časové pořadí a program
je nekontroluje. Text výslovně neřeší overflow paměťového fondu,
protože očekává malé počty uživatelů. Není tedy tvrzen bezpečný běh
pro libovolně početný nebo neomezeně dlouhý vstup.

Naše běžící sestava má program od 100, fond od 900 a vstup od 3000.
První nový uzel je POOL+4; čtyři úvodní slova fondu zůstávají nevyužita,
což je neškodná konvence nejvyšší přidělené adresy. Při této konkrétní
relokaci je poslední bezpečná báze před vstupem 2996, tedy nejvýše 524
současně přidělených fondových uzlů. Vstupní loader dovoluje nejvýše
249 uživatelů po čtyřech slovech; naše největší náhodné běhy mají 49.
Obecný důkaz není omezen těmito testovacími rozměry, ale platnými
strojovými adresami a místem pro všechna data.

Známá trojice oprav z 8. července 1998 používá `POOLMAX NOP POOL`
a pole `(0:2)` v řádcích 103/105. Důvod je také syntaktický: POOL je
definováno až štítkem END po literálech, zatímco dopředný odkaz není
v MIXAL přípustný ve W-hodnotě CON (§1.3.2, pravidlo 13). NOP jej
dovolí jako A-část instrukce. Předem definované `POOL EQU 900` v naší
relokaci syntaktický problém odstraňuje; proto samotný strojový test
původního CON s již známou adresou není reprodukcí této chyby assembleru.

Konečné testy samy nedokazují absenci všech chyb ani reálné vlastnosti
současného výtahu. Dokládají shodu přepisu, přesné specifické scénáře
a okrajové implementační podmínky; obecný důkaz stojí v §§2–8 výše.

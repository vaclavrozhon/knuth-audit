# Návrh programů71–73 a začátek korutin74

7. listopadu 2026. Každý odstavec file71–74/p63–66 je zde
mapován spolu s úplným `exercises-1.4.1-001-016-recovery.md`.
Převzetí bibliografie má přesně rozsah nového svazku1:
`workstreams/vol1/notes/quality-recovery-section-1.4.1-2026-11-07.md`,
oddíl4, a `workstreams/vol1/parallel/subroutines/notes/sources.md`.
Tyto pramenné rozbory byly přečteny. Jejich důkazy o jiných
MIX programech ani historické testy se sem nepřenášejí.

## File71: každý krok0–3

Úvod a krok0 doporučují návrh obecného postupu. „One successful
way“ je nabídka metody, nikoli tvrzení o univerzálním ukončení,
optimálním rozkladu nebo pevné rychlosti vývoje. Krok1 rozkládá
specifikovaný úkol na podúkoly a dočasně předpokládá jejich
kontrakty. Logický obsah je kompozice: jestliže každé volání
splní precondition dítěte a jeho postcondition stačí následnému
kroku rodiče, platí odvozený postcondition rodiče. Dokud jsou
děti pouze skici, je tento závěr podmíněný; text to výslovně
připouští a dovoluje změnu dřívějšího návrhu.

Odkaz na Dijkstru je obsahově doložen primárním EWD249,
částí od začátku prvního příkladu přes description1 a volbu
reprezentace tabulky. Přesný přetisk v Academic Press1972
nebyl s autorskou zprávou typograficky porovnán; tento údaj
zůstává bibliografickou výjimkou. Wirthův původní článek
CACM14(1971),221–227 je doložen přečteným titulem, úvodem221–222
a závěry226–227. Ty pokrývají právě stepwise refinement;
řešení osmi dam není podmínkou tohoto metodického odkazu
a není tímto převzetím znovu auditováno.

Krok2 obrací pořadí implementace: nejprve kontrakty nejnižších
rutin a poté rodiče. Pro acyklický graf závislostí tak lze
kompozici ověřovat zdola; pro rekurzi je navíc potřeba indukční
kontrakt a klesající míra, jak bylo konkrétně doloženo na Fib.
Kniha zde neslibuje, že každý rekurzivní graf dovoluje přísné
pořadí bez dopředné deklarace — říká „as far as possible“.
PL/MMIX je příklad zamýšleného jazyka, ne tvrzení o nynější
dostupnosti produktu. Požadavek popsat vstup, výstup a calling
sequence odpovídá již ověřenému konkrétnímu kontraktu(10).

Global používaný současně pro dvě neslučitelné živé hodnoty
nemůže obě hodnoty uchovat: dvě různé požadované64bitové hodnoty
nelze současně uložit do téhož registru. Kontrola jejich
životnosti či oddělené přidělení proto chrání invarianty
obou rutin. Netvrdí se zde žádná algoritmická mez optimální
alokace registrů. Začátek kroku3 žádá posoudit každé skutečné
volání; „very nearly a working program“ je praktický cíl,
nikoli důkaz absence chyb po předchozích krocích.

## File72: celý krok3 a celý krok4

Přesun stejné přípravy či dokončení dovnitř rutiny zachová
chování, jestliže nové rozhraní zahrne jeho původní vstupy,
výstupy a vedlejší účinky. Sloučení dvou rutin potřebuje
stejnou kompoziční podmínku. Jednou volanou rutinu lze vložit
na místo volání se zachováním lokálních jmen a návratu;
nevolaný kód lze odstranit, pokud opravdu není dosažitelný
ani nepřímo přes adresy. Jsou to možnosti k posouzení,
ne bezpodmínečné transformace libovolného kódu.

Návrat ke kroku0/1 je doporučení využít získané znalosti.
Následující varování před nekonečným přepisováním výslovně
brání interpretaci jako ukončující optimalizační algoritmus.
Pravděpodobná úspora ladění, zlepšování každého komplexního
programu, diminishing returns a anekdota o nejlepších programech
vzniklých po ztrátě práce nejsou zde podložený empirický
průzkum. Tyto konkrétní zkušenostní věty jsou výjimky,
nikoli nově potvrzená matematická tvrzení či nové nálezy.

Krok4 mění hledisko na skutečné pořadí vykonávání. Sledování
prvních dvou návštěv každé instrukce může odhalit rozpor
sledovaného stavu s invariantem, ale nepokrývá všechny vstupy
a stavy. Text tuto pomůcku nevydává za úplnou verifikaci.
Vhodná testovací data, zobrazování interního stavu a evidence
vlastních chyb mají konkrétní diagnostický účel; tvrzení,
že mnoho nejlepších programátorů věnuje téměř polovinu kódu
ladění a získá překvapivou produktivitu, zůstává výslovně
neověřené zkušenostní zobecnění. Není třeba dokazovat novou
univerzální metodologickou větu, kterou text neformuluje.

Autobiografické datování textu do1964, rozsah tehdejších
projektů a pozdější osobní vývoj v1980s nebyly archivně
nezávisle ověřeny. Tato výjimka pokračuje do73.

## File73: literate programming, Turing a úlohy1–12

Autorova primární stránka Literate Programming potvrzuje
rok1992 a obsah včetně kapitoly11. Převzatá pramenná recenze
výslovně rozlišuje přečtenou předmluvu ix–xii a doložené
záhlaví/úvod kapitoly11 s rozsahem1978–1991 od nepřečteného
celého chybového deníku. Lokální25bajtová odpověď údržby
serveru není vydávána za knihu. Tvrzení, že text shrnuje
autorovy názory a kapitola obsahuje deník, je tímto doložené;
úplnost každé jednotlivé opravy TeXu tím prokázána není.
Přesné rozlišení Cambridge/CSLI jako vydavatele/distributora
a autorova autobiografická datace zůstávají výslovné limity.

Turingův původní strojopis Proposed Electronic Calculator,
tištěná18/PDF19, odstavce4–6, byl v převzatém důkazu přímo
zobrazen. Citace souhlasí a [bugs] je redakční vysvětlení.
Datace nedatovaného strojopisu1945 proti předložení1946
nebyla nově archivně rozhodnuta; rozdíl není nový nález.
Obsah citace je návrhové doporučení, nikoli tvrzení, že
každý program musí obsahovat chybu.

Všechna zadání1–12 jsou jednotlivě pokryta novým rozborem
úloh, oddíly1–12. E10 zůstává partial pro přesný význam
inicializace při permutaci. E11 má argument včetně POP po
SAVE, s explicitním běžným OS guard/abort předpokladem.
Známé erratumPUT rJ a dříve zaznamenané C0005 jsou oddělené.
Samotná73 tedy není úplně argumentově uzavřena.

## File74: úlohy13–16 a celý úvod korutin

Všechna čtyři zadání a všechny jejich části jsou pokryty
novým rozboremúloh13–16, včetně obou iterativních variant,
malých n, přesných časů, celého no-fp zdroje a obou rozšíření
nelokálního návratu. Známý požadavek n≥0 je aplikován.

Následující odstavce zavádějí coroutine jako komponentu,
která po aktivaci pokračuje v uloženém bodě pozastavení.
Symetrie znamená, že tutéž operaci lze popsat jako volání
druhého člena nebo návrat jemu; nepotřebuje pevnou hierarchii
caller/callee. Podprogram je zvláštní případ, v němž jeho
opakovaný vstup směřuje do stejného počátku, zatímco návrat
do hlavního programu mění místo podle posledního volání.
Příklad střídání dvou šachových programů splňuje tuto
strukturu, když jejich protokol po tahu předá řízení druhému;
není zde tvrzeno ukončení každé šachové partie.

Poslední věta74 pokračuje na75: globální a,b jsou dva odlišné
uchovávané continuation registry. A na adrese p provede
GO a,b,0: použije **staré** b jako cíl a uloží p+4 do a.
B na adrese q provede GO b,a,0 a analogicky se vrátí na
p+4, přičemž do b uloží q+4. Indukcí po každém předání
obsahuje neaktivní coroutine přesné místo následující po
svém posledním GO. Před prvním předáním musí být nastavena
adresa počátku dosud nezahájeného člena; vlastní init programu
se ověřuje v následujícím bloku. Cena každého GO je3υ.
To je celý technický závazek konce74, bez předstírání kontroly
celého následujícího překladače znaků.

## Úloha1.4.2′–1 a přesah odpovědi123–124

„Calls the other only once“ se v odpovědi vztahuje na jediné
**místo** předání, jak potvrzuje následující „distinct places“.
Má-li jeden člen jen jedno takové místo, je jeho continuation
po každém předání stejná adresa. Lze jej označit za subroutine
vstup a druhý za main, bez dynamického výběru mezi více
resume body; mohou zůstat jeho uchovávaná data. Dvě a více
míst na každé straně tuto zvláštní jednoduchost odstraní,
ale jsou pouze nutnou indikací vhodnosti příkladu, nikoli
dostačující nemožností použití jiného řídicího mechanismu.

Konečný počet resume bodů lze zakódovat do stavové proměnné
a při jednom pevném vstupu rozvětvit podle ní. To dokazuje
dodatek odpovědi na124: switch či rozlišující data mohou
malý příklad zjednodušit. S rostoucím počtem bodů roste
rozsah takového dispečinku; coroutine uloží přímo adresu.
„More useful“ je vysvětlení návrhového motivu, ne měřená
univerzální závislost užitku na počtu míst. Text odpovídá
otázce, proč je **pedagogicky přesvědčivý krátký příklad**
obtížný, nikoli tvrzení o nevyjádřitelnosti coroutine
obyčejným programem. Tím je zahrnut celý konec123 i pokračování
téže odpovědi124; ostatní obsah124 se zde neuzavírá.

## Přesná mapa a zachované výjimky

71: celý návrh0–3 a věcný význam obou primárních metodických
odkazů; přesný přetisk Dijkstra1972 zůstává přeskočen.
72: všechny návrhové a ladicí kroky; výše vyjmenované empirické
a autobiografické věty zůstávají výjimkami.
73: celý literate/Turing odstavec a všechny úlohy1–12;
E10 interpretační partial plus uvedené bibliografické limity.
74: celý obsah má konkrétní argument; další stránky korutin
se tím automaticky neuzavírají.
121: předchozí traffic část přebírá `exercises-1.3.2-034-recovery.md`
a C0020; zbytek jsou celé odpovědi1–3 nového rozboru. Stále
partial pro přesné timer/OS/sensor závazky E34.
122: všechny odpovědi4–13 mají nový rozbor; C0021/C0022,
E10 interpretace a UNIX přirovnání brání blanket closure.
123: celý konec13, odpovědi14–16 a začátek coroutine1 jsou
pokryté. Zkušenostní „similar behavior … other subroutines“
nemá vymezenou populaci či nezávislé empirické ověření;
tento jediný výslovný faktografický limit se nezazelení.

Vzory byly použity pro rozlišení podmíněné kompozice od
univerzálního slibu, přesný rozsah převzatého primárního
zdroje a skutečnou mapu všech tvrzení včetně přesahů stran.

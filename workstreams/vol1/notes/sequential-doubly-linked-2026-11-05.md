# Souvislý průchod §2.2.5 — 5. listopadu 2026

Přímo přečteny celé originály 280–298 a 553–556, všechny obecné
důkazy v `parallel/doubly-linked/NOTES.md`, pramenné meze, protokol
fyzické úlohy 10 a přijaté výsledky. V tomto průchodu tedy byly
zobrazeny všechny původní stránky hlavním agentem, nad rámec
užšího kořenového převzetí z 1. listopadu. Úspěšných 497 běhů
(včetně 37 záměrně vadných) ani ostatní výčty se neopakovaly.

## Odkazy, agenda a důkaz programu

Reprezentační invariant zahrnuje jeden konečný kruh přes hlavu;
samotné R(L(x))=L(R(x))=x by dovolovalo více disjunktních kruhů.
Smazání nahrazuje a,x,b hranou a,b, vložení provádí opačnou změnu.
Obě operace zvládnou i jediný datový uzel či prázdný seznam s hlavou.
Pět měněných odkazů při vložení započítává AVAIL stejně jako
srovnávané tři odkazy u jednosměrné varianty. Fig. 11 a 12 souhlasí.

WAIT a fronta/vozidlo používají dvě nezávislá pole uzlu. SORTIN
vkládá za dřívější události stejného času, IMMED před ně. Čas
hlavy je 0 a kladné či nulové plánované časy zaručují ukončení
pravostranného hledání. CYCLE odstraní nejbližší událost před
jejím provedením; členství je proto invariantem hranic aktivit,
nikoli každé jednotlivé instrukce. USER1 udržuje neprázdnou agendu.
Konečný auditní vstup končí explicitním HLT, běžný model sám
nevyžaduje konec. Lokálně konečný vstup a kladná trpělivost brání
nekonečné řadě okamžitých událostí v jednom čase.

Všechny tištěné řádky byly porovnány s obecným rozborem U/E/D:
pole NEXTINST skutečně obsahuje JMP, hlavy front používají pouze
slovo s offsetem 3 a jejich fiktivní báze nepřekrývají živá pole.
CALL obsahuje UP/CAR/DOWN v bajtech 1/3/5, čtyři nulová slova
na obou stranách zajišťují platné součty. Mez
4(b^4+b²+1)<b^5 platí pro všechny b=64,…,100, tedy žádné přetečení
nepokazí test existence volání. Adresy a plánované časy musí ležet
v rozsahu stroje; text výslovně předpokládá dostatek fondu.

Marker ELEV3 rozlišuje naplánovanou E9, E1 je uložené pokračování,
nikoli běžně vykonávaný příkaz. Při znovuotevření se ruší právě
existující E6; U5 při neutralitě přesouvá existující E5. E4 nejprve
vybere vystupující, pak nejstaršího čekajícího. Není-li uživatel,
právě samotná hlava má odkaz na sebe. U4A obnovuje členství WAIT,
ačkoli nová kladná GIVEUPTIME může pocházet od pozdějšího U1;
tato další doba pouze udržuje odklad při obsluze patra.

Přesné časy: INSERT 13u, DELETE/DELETEW 11u, IMMED 19u,
SORTIN 16+5k a HOLD 18+5k. Rozvinutí DELETEW v CYCLE uspoří
JMP+STJ+návrat, tedy 4u. Historický počet volání není potřeba
k tomuto obecnému výpočtu.

## Úlohy a tabulka

1–2: všechny krajní případy deque souhlasí. Dolní mez jednosměrného
řetězu předpokládá jediný následnický ukazatel, nikoli XOR kódování
dvou sousedů; kniha sama tuto výjimku uvádí.

3: potřebu tří bitů dokládá všech osm budoucím chováním
rozlišitelných kombinací UP/CAR/DOWN. Testy postupně mažou dva
typy požadavků a čtou třetí, pomocné volání udržuje požadovaný směr.
Nejde pouze o párovou odlišnost tří druhů tlačítek ani o tvrzení
o konkrétním počtu fyzických relé.

4: dosažitelný vstup se 12 výstupy posune první nástup na
20+25·12=320 po otevření, tedy za E9(+300). Ta může určit jiný
směr ještě před nástupem. Uložený úplný příklad má další zastávku
0 v čase 1192, bez E9 patro 4 v čase 1152.

5: při příchodu uživatele 10 na patro 2 se v 1063 vymažou právě
vyřízené kabinové požadavky a nezůstane volání na 0. Po výstupech
určí uživatel 7 směr nahoru. Formulace „nobody on board“ v odpovědi
se čte v kontextu nového nástupu, nikoli jako popření probíhajících
výstupů mezi 1083 a 1158.

6: způsobilost je (OUT<IN a STATE≠UP) nebo (OUT>IN a STATE≠DOWN).
Protože OUT≠IN, je ekvivalentní původní dvojici podmíněných vět.
Erratum 2024 činí spojení s FLOOR=IN jednoznačné; neprokazuje
chybně vypočtenou pravdivostní hodnotu původních podmínek.
E4 vybere prvního způsobilého, ostatní nechá se svou U4 ve frontě.
Neutralita připouští všechny směry. Toto přeformulování samo
nebarví 554 červeně; zdejší fyzické anekdoty zůstávají neověřené.

7: záměrně vadné JANZ CYCLE ponechá cestujícího ve frontě bez WAIT;
pozdější DELETEW už používá neplatné sousedy. Uložený vstup ukazuje
první porušení v čase 103 a ztracený odchod pátého uživatele v 120.
Jde o úmyslnou chybu zadání, nikoli nový nález v jeho řešení.

8–9: E8 má konečné klesající hledání nižších pater, DECISION
vzestupně hledá nejmenší jiné patro. Při E1 má domácí volání
prioritu. Fallback j=2 nastává jen při návratu do E6B. Tištěné
I1=j−4 i vlastní přímá implementace zachovávají stejný invariant.
Registry a vnořené HOLD používají odlišná návratová místa.

11: pravé strany čtou staré V, zápisy ukládají NEWV; nenulový LINK
označuje jediné členství v seznamu změn. HEAD=−1 nekoliduje
s platným indexem. Dokončení stojí O(s) a nulováním LINK připraví
další krok. Přísnější detekce každého druhého zápisu splňuje úlohu;
rovné opakované hodnoty lze volitelně tolerovat.

12: ELEVATOR může při hledání uchovávat předchůdce, WAIT a QUEUE
potřebují i rušení známého uzlu bez takového průchodu. Halda
s mapou uzel→pozice poskytuje O(log n) i pro obecné odstranění;
bez této mapy by samotná obyčejná halda nestačila. Přesný odkaz
do svazku 3 na 149 byl znovu zobrazen.

Tabulka 286 má přijaté ověření všech 78 řádků dvou fragmentů.
Druhý je podmíněný stavem 4257, nevymýšlí chybějící vstup mezi
fragmenty. Původní konečný čas je správně 4840, nikoli OCR 4820.
D2 při druhé 0180 a D3 při 4820 jsou známé opravy.

## Otevřené skutečnosti, prameny a errata

Úloha 10 zůstává partial: připravený simulátor a protokol nenahrazují
měření skutečného výtahu. Fyzické vlastnosti historického zařízení
na 282–285, poznámky na 297/554 a autorův počet návštěv na 298
nejsou naším nezávislým pozorováním. Strany 284–285 jsou technicky
kontrolovány jako explicitně hypotetická pravidla modelu; jejich
shoda se skutečným zařízením se nepřisuzuje této kontrole.

Na 291 není doloženo statistické „rarely exceeds 10“. Na 296
chybí úplný VALUES pro 26 uživatelů do času 10000, takže počty
1432/437/407/32/142 zůstávají nereprodukované. Nejde o drahý
brute force, který jsme jen vynechali, ale o chybějící vstup.
Hlavní sekce proto zůstává partial, přestože technické důkazy
a 11 matematických/programových úloh jsou uzavřeny.

Přímo přečteny primární strany 105–107 Knuthova článku 1971:
podporují definici profilu, bibliografii i počáteční sběr programů
z košů. Další programy pocházely z jiných cest; netvrdíme, že
všechny statistiky článku jsou nezávisle auditovány.

Nový výpis všech čtyř erratových vrstev obsahuje i kosmetické
změny. Do mapy vad patří tabulka 286, spojená oprava POOLMAX
na 292/296, chybné číslo smyčky na 296 a rozsah zadání 8 na 297.
CON POOL má nepřípustný dopředný odkaz ve W-hodnotě; NOP jej
dovolí v A-části a pak vyžaduje pole (0:2) na obou přístupech.
Program s předem zadaným POOL EQU tedy původní syntaktickou
chybu nereprodukuje. Typografie a ekvivalentní přepis podmínky
se nepočítají jako další matematická selhání.

Nový nález: 0. Stránky 282/283/291/296/297/298/554 mají přesně
uvedené historické či experimentální meze. Na sdílené 556 je zatím
uzavřen jen konec odpovědi 12; další odpovědi patří §2.2.6.
Pokračuje adresování polí na 299, úvod 298 už přečten.

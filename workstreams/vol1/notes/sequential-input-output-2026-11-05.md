# Souvislý průchod §1.4.4 — 5. listopadu 2026

Přímo přečteny originály 215–228 a 532–534, všech osm tematických
poznámek v `parallel/input-output/notes/` a předchozí kořenová revize.
Přijaty uložené výsledky se zde uvedenými mezemi; úspěšné výpočty
nebyly opakovány. Současná čtyři errata porovnána podle stran i tématu;
viz `sources/sequential-2026-11-05/input-output-errata-extract.json`.
Přímo zobrazeny také all1-prepre 17/18/39 a all1 14.

## Základní a vícenásobné bufferování

WAITIN nejprve zahájí IN a teprve pak čeká pomocí JBUS. Dva přesuny
MOVE po 50 slovech stojí 202u. Dvojité bufferování s kopírováním tedy
má periodu přibližně max(C,T)+202u místo C+T; text svůj odhad výslovně
označuje za přibližný. Výměna ukazatelů odstraňuje kopírování.

WORDIN má data B..B+99, zarážku B+100 a následný ukazatel B+101.
Zarážka musí být skutečně záporná, např. −1; záporná nula v testu
JXN nevyhoví. IN při přechodu na druhý buffer implicitně počká na
předchozí I/O téhož zařízení. Po změně ukazatele se načte první slovo
a přeskočí INC6. Nevzniká přístup do právě přepisovaného bufferu.
Předčítání vyžaduje dostupný následující blok nebo koncový marker;
není to obecná rutina s automatickou detekcí EOF.

WORDOUT správně doplní nulami jen neúplný poslední buffer. Prázdný
výstup ani přesný násobek 100 slov nevytvoří navíc prázdný blok.
HLT není bariéra I/O; přijaté testy výslovně dokončují čekající výstup.
Známá oprava CON na 532 odstraňuje zakázané dopředné symboly:
ENDBUF1 CON *+101 a BUFMAX až za definicemi bufferů. Korutinový WORDIN
má správnou inicializaci a běžnou cestu 8u; vlastní varianta ji
zkracuje na 7u bez volacího JMP. Při výměně bufferu se úspora neztratí.

Maximální zrychlení 2 pro jediné I/O, resp. n+1 pro n zařízení,
plyne v uvedeném idealizovaném modelu ze součtu dob proti jejich
maximu. Rozběh, ukončení a disková latence mají v textu vlastní
výhrady. Nejde o univerzální příslib skutečnému hardwaru.

V kruhovém bufferu n zahrnuje také probíhající I/O. Od NEXTR následují
červené, nejvýše jeden žlutý a zelené buffery. ASSIGN vyžaduje n<N
a žádný dosud neuvolněný žlutý buffer. RELEASE zvýší n; CONTROL
sníží n a posune NEXTR až po dokončení I/O. Ukazatel uložený před
bufferem leží mimo přenášená data. Inicializace n=N pro vstup a n=0
pro výstup vysvětluje shodný program. CONTROL mění I5, I6 a J,
ale původní verze zachovává CI, overflow i A.

**Oprava starší auditní poznámky:** Naše skutečně prohlédnutá strana
223 už má ve Fig. 25 šipku B6→B2. Také náhradní obrázek v erratech
z 8. 8. 1997 má B6→B2. Tvrzení v původním `notes/circle.md` a
`progress.json`, že naše figura vrací do B1, není doložené. Záměna
B1/B2 se nesmí přebírat jako vada naší kopie. Ve Fig. 23/24 i 25
byly přečteny také barvy, počty, popisky a přechody. Strana 223 se
kvůli samotné existenci náhradního obrázku nebarví červeně.

## Všech devatenáct úloh

U 1–8 souhlasí vysvětlení blokování, základní programy a odhady výše.
U 9–11 činí celkový výpočet 61000 a výstup 75000 časových jednotek.
První výstup může začít nejdříve v čase 1000; dolní mez dokončení
je tedy 76000. Úplné rozvrhy dávají pro N=1,2,3,4 postupně
110000, 89000, 81500, 76000. Čtyři buffery dosahují dolní meze.
Původní rozvrh na 227 souhlasí krok za krokem; při N=3 je CPU
nečinné 20500 a zařízení 6500 jednotek. Nejde jen o porovnání součtů.

**C0033 zůstává potvrzenou obsahovou chybou odpovědi 12 na 533.**
Přidané CMPA sice obnoví A, ale změní CI. Před JRED lze legálně
provést ENTA 0; CMPA =1=, potom JRED CONTROL(16); JL SUCCESS.
Na druhé ze dvou karet je tečka v 80. sloupci; JBUS před příkladem
zaručí její dočtení. Původní CONTROL ponechá „less“, nová verze vrátí
„equal“ a změní větev volajícího programu. Není použit neurčený
počáteční CI ani souběžný přístup do aktivního bufferu. Uložených
54 skutečných MIX běhů porovnává původní, tištěnou a opravenou
variantu pro báze 64/100, tři latence a tři indikátory. Oprava musí
obnovit CI po volbě větve konce vstupu, případně výslovně změnit
kontrakt všech volání CONTROL. Čtyři dnešní vrstvy errat tuto vadu
neopravují. Přesná chybová lokace je jen 533; 223 a 227 jsou kontext.

Úloha 13 dokončí všechen výstup včetně aktivního I/O, protože n
klesne na nulu až po obsluze dokončení. U 14 platí invariant
y≤N−n, před dalším ASSIGN musí být nerovnost ostrá. Více žlutých
bufferů vyžaduje FIFO pořadí RELEASE a uložení CURRENT před dalším
ASSIGN. Známé erratum z 28. 3. 2026 správně doplňuje n=0 pro N=1
a opravuje horní mez N na N−n; nejde o nový nález.

U 15 je podstatná známá vložená JBUS před posledním OUT. Počty jsou
1+33·3=100 čtení a 99+1=100 výstupů. Ideální dolní mez pipeline
je Ti+To+99 max(Ti,To). Vlastní rozbalená varianta má při nulové
další latenci 202u proti 269u; absolutní instrukční optimum netvrdí.

U 16 chybí tištěná odpověď, ale přijaté řešení dává čtyři barvy
G,Y,R,P a tři korutiny. Součet počtů je N, y≤1; P obsahuje volné
i právě načítané buffery, R čekající i právě zapisované. Přechody
P→G a R→P nastávají až po I/O, výpočet dává G→Y→R. Blok k používá
k mod N až po uvolnění blokem k−N. Při konečném I/O a spravedlivém
plánování nevzniká uváznutí. 1392 dříve probraných stavů je doplněk
k obecnému invariantu, nikoli jeho náhrada.

U 17 je vlastní pooling řešením otevřeného návrhového zadání,
nikoli přepsanou tištěnou odpovědí. Rezerva volných bufferů splňuje
|F|≥počet aktivních proudů s nulovou alokací; M≥D. Program drží
nejvýše jeden buffer ke zpracování pro každý proud a uvolní jej
před dalším požadavkem téhož proudu. S limitem
min(M−D+1,max(2,floor(M/D))) a předčítáním rostoucím až při čekání
rezerva brání vzájemnému zablokování. EOF a spravedlivé vyřizování
jsou součástí modelu. Testovací slučování 4885 slov porovnalo všechny
kladné statické trojice alokací. Pooling někdy vyhraje, jindy
prohraje; obecnou optimálnost z výsledků nevyvozujeme.

U 18 model skutečně provádí MIX kód a hardwarové přerušení, nemá
skryté algoritmické callbacky. Ukládá všechny registry, CI, overflow,
PC a znaménka nul do záporné řídicí paměti. ACTIVE se ruší až po
zpracování přerušení, ne už při fyzickém dokončení. RELEASE a obsluha
pracují s uloženým I6/I5, takže se změna počtu neztratí. Přerušení
mezi CMPI6 a JE může přidat jedno otočení čekací smyčky, ale nemění
správnost. Události během řídicího programu se odloží podle zadání.
Přijatých 648 běhů obsahuje 5208 přerušení, z toho 1108 odložených.
Neurčená vstupní doba hardwaru je modelována nulou; časy z modelu
proto nejsou tvrzením o skutečném zařízení.

U 19 je obecný důkaz pro n≥2, 0<T≤L≤P, C>0. Čtení k začíná v
t_k=(k−1)L+a_k P s neklesajícími celými a_k. Dolní mez konce je
T+C+(n−1)max(L,C). Pro C≤L stačí a je nutné N=ceil((T+C)/L).
Pro C>L určují nejpozdější přípustná čtení
t*_k=(k−1)L+P floor((k−1)(C−L)/P). Dostupnost N bufferů je přesně
t*_k≥T+(k−N)C pro k>N, tedy NC≥C+T+((k−1)(C−L) mod P).
Maximum těchto zbytkových mezí dává tištěné c_N a nejmenší vhodné N.
Obě tištěné horní meze plynou z b_k<C+T+P a
b_k≤L+T+n(C−L). Devět číselných příkladů dává
N=1,2,3,35,51,41,11,3,2. Staré racionální testy porovnávají
nezávislou rekurenci nejčasnějšího rozvrhu, ne dvě kopie téhož vzorce.

## Prameny, errata a rozsah uzavření

Citaci Itai–Raz ověřuje kopie od autora na 1338–1342; známé 1339→1338
je skutečná chyba lokace. Doklad není úplným auditem celého jejich
článku. Odkaz na svazek 3 byl zkontrolován na jeho stranách 317–318,
bez tvrzení, že tím byl prověřen celý svazek.

Na 215 se výslovně přeskakuje přesné historické vydání Websterova
slovníku a posloupnost slovníků, v nichž input/output byly pouze
substantivy. Novější primární slovníkový pramen podporuje samotný
význam buffer, nikoli všechny údaje o starém vydání. Formulace
„formerly“ není přesný letopočet vyvrácený datem prvního slovesa.
Komentář o singular/plural information je neformální významové
vyjádření. Budoucí MMIX je čten jako autorův plán v době vydání.
Tyto úzce vymezené bibliografické výjimky podle pokynu uživatele
nebrání uzavření hlavní matematické a faktické kontroly.

X0245 se mapuje na skutečné vady na 216, 225, 532, 533 a 534.
Přidání (a)/(b), názvy A′/R′/B′ a náhradní Fig. 25 nejsou samy
o sobě doloženým obsahovým selháním naší kopie. Oprava Fig. 27 na
221 platí jen pro dotisky 32–40. Seznam 12 publikovaných položek
zůstává archivován, ale není počtem 12 vad v našem skenu.

Celá §1.4.4 a všech 19 úloh jsou nyní zkontrolované v uvedeném
rozsahu. Nový neznámý nález: 0; C0033 potvrzen znovu přímou revizí.
Strany 215–228, 532–533 mají celé pokrytí. Strana 534 je zatím
částečná, protože dole již obsahuje odpovědi §2.1, úlohy 1–3.
Další průchod začíná historií na 229.

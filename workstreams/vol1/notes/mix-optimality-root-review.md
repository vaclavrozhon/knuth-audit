# Převzetí doplňků ke globální optimalitě MIX

2. listopadu 2026. Root přímo přečetl původní strany 142 a 508,
celou stabilní poznámku `parallel/mix-optimality/notes/zeroing.md`
a nový instrukční checker. Zadání 17 požaduje nulování adres
0 až N včetně, 0<=N<=2999, program začíná na 3000. Počet hodnot
bajtu b je libovolný v 64..100. Ostatní registry nemají předepsaný
počáteční stav. Konec je předání řízení na následující adresu;
samostatné HLT se v tomto zadání nepožaduje.

## X0678: rychlejší platná horní mez pro 17(b)

Nová konstrukce má 999 instrukcí na 3000..3998 a končí na 3999.
Po DEC2 994 vybere nezáporná větev celý blok 994 příkazů STZ,
záporná větev pomocí ENN1 a indexovaného JMP jeho koncový úsek.
Při N=994q+r, 0<=r<994, celé průchody zapisují vzájemně
disjunktní intervaly [N-994k+1,N-994(k-1)] pro k=1..q.
Poslední průchod má rI2=r-994 a rI1=994-r; skáče na adresu
3003+(994-r), tedy na STZ s operandem 994-r. Zapíše přesně
0..r a záporný J2NN na konci již nevrací řízení zpět.

Každý úplný průchod stojí 2*994+3 jednotek času u; poslední
stojí 2(r+1)+5. Celkem je to T(N)=2N+3 floor(N/994)+7.
Původní dlouhý program s 993 příkazy STZ má doložený čas
2N+3 floor(N/993)+8. Zlepšení je proto nejméně 1u pro každý
povolený N. Nejde jen o lepší nejhorší případ. Počáteční obě
nuly rI2 se prvním odečtením změní na -994; všechny efektivní
adresy jsou platné a kód nepoužívá neznámý počáteční registr.

777 uložených instrukčních kontrol pokrývá všech 37 radixů,
vybrané hranice obou délek průchodu a obě znaménka nuly.
Checker nastavuje jinak nenulovou paměť a registry a kontroluje
také neměnnost paměti mimo 0..N. Root úspěšný běh neopakoval.
Univerzálnost plyne z uvedeného rozkladu, nikoli z testovaných N.

Jde o ověřené zlepšení horní meze. Zadání sice žádá nejrychlejší
program, ale odpověď dlouhou variantu popisuje pouze jako o něco
rychlejší než předchozí. Nezaložili jsme automaticky nový nález
o výslovném nároku její globální optimality. Nová varianta sama
takový nárok také nemá. Úloha 17 a X0153 zůstávají partial.

Zejména pro prostorové dolní meze 16(a)/17(a) nelze jen spočítat
druhy původních instrukcí: samomodifikace může jejich druh změnit.
Ani obecná inicializace indexu nemusí vyžadovat samostatný krok
vedle jiné aritmetiky. Tyto mezery jsou výslovně zachovány.

## X0680: úplná časová dolní mez pro 24(b)

Root přečetl celý nový důkaz `notes/shift-time-optimum.md`, oba
symbolické programy, nezávislý číselný program v C++ a tři uložené
výstupy v `parallel/mix-optimality/`. Sedm souborů odpovídá
zmrazenému manifestu. Úspěšné výpočty se neopakovaly. Přímo byly
porovnány originály svazku 1 na 143, 509 a 139 a svazku 2 na 224;
poslední potvrzuje i účinek a časy plovoucích instrukcí FLOT/FIX.

Zadání přesouvá devět nezávislých bajtů mezi registry A a X,
bez předepsaného HLT. Knižní SRC 4; SRA 1; SLC 5 stojí 6u.
Nový výsledek vylučuje všechny přenositelné programy zaručující
nejvýše 5u; netvrdí nutnost 6u na každém jednotlivém vstupu.
Pro dolní mez stačí povolený radix 64. Předepsané konstanty
jsou libovolné a ostatní počáteční stav lze zafixovat nezávisle
na vstupních bajtech.

Sdruženým posunem se rozumí SLAX, SRAX, SLC nebo SRC. V čase 5u
mohou nastat nejvýše dva. Změna registru adresovou instrukcí
za 1u mění jeho velikost nejvýše o 4095 nebo nastaví hodnotu
nejvýše 4095. Větší symbolický model ponechá dolní dva bajty
libovolné a horní tři změní o -1, 0, +1 modulo 64^3, nebo vynuluje.
Přechod přes znaménko a přetečení jsou zahrnuty; model v žádném
kroku neodstraňuje možný skutečný běh.

Pro vstup W = (0,5,10,15,20; 25,30,35,40,45) vyčerpávají certifikáty
dva posuny s jednou adresovou operací, jeden posun s až třemi
adresovými operacemi a jeden posun s libovolnou náhradou celého A
a další adresovou operací. Poslední případ je silnější než všechny
zbývající přípustné aritmetiky a načtení A, včetně FLOT/FIX.
Kontroly mají 104544, 7986 a 4155 větví, žádná nedává cíl.
Nezávislé číselné vyčerpání má 214097400 případů. Úplnost zde
plyne z redukce instrukcí a zvětšení množin, nikoli z počtu testů.

Samostatně je nutné vyloučit načtení X, které vymaže jeho starý
obsah. Vedle jednoho posunu a LDX se již nevejde STORE. Rodina
všech kladných devíti bajtů má 63^9 různých požadovaných výsledků;
po načtení zbude nejvýše 4*64^5 rozlišitelných stavů nesoucích
informaci o vstupu. Bez sdruženého posunu musí na rodině s pevným
A a prvním bajtem X proběhnout LDX i velká změna A. Znovu není
čas na uložení starého X a jeho čtyři proměnné bajty se ztratí.

Propojení těchto rodin s bodem W je podstatné: W patří do obou
rodin. Pokud jeho běh spadne do některého případu s LDX, jediný
možný skok má stejný výsledek na celé příslušné rodině. Bez další
adresové operace jsou registry před a po posunu buď kladné,
nebo shodně nulové; načtené slovo i ostatní příznaky jsou pevné.
Pokud se místo skoku použije adresová operace, řízení je pevné
rovnou. Program tedy nemůže pro ostatní členy této rodiny uniknout
do jiného počtu posunů. Nejde o chybnou záměnu bodového svědka
s univerzálně stejnou posloupností instrukcí pro všechny vstupy.

Samomodifikace a indexování nejsou vyloučeny předpokladem.
V bodových případech se vyčerpávají všechny skutečně vykonané
instrukce a vzdálenosti posunů. V informačních případech se
zápis vstupu do paměti nevejde do časového rozpočtu. Předem
připravené tabulky proto informační ztrátu nenahradí.

Dolní mez je přijata. S prostorovým důkazem X0670 je celá úloha
24 nyní `checked`. X0153 zůstává částečný pro ostatní vyjmenované
úlohy; nevzniká nový nález chyby v knize.

## X0684: časové minimum úlohy22

Root přečetl celý `parallel/mix-optimality/notes/power-time-optimum.md`
a přímo porovnal zadání143 a odpověď509. Výsledkem je přesně4u
bez závěrečného HLT, tedy5u s jeho jednotkovým časem. Výsledek
znamená celé číslo X^13: oba znaménkové zápisy nuly jsou rovné.
Tabulka vrací+0 i pro−0, což splňuje toto číselné zadání.

Pro dolní mez stačí radix64, vstup+3 a nulové počáteční registry.
Nezměněné vstupní slovo má operační bajt3, tedy MUL za10u;
jeho vykonání nenahradí běžné čtení v rozpočtu3u. Přepsání
posledního bajtu před pozorováním vstupu vymaže rozdíl mezi+2
a+3. MOVE, OUT a následný vstup/přenos nedodají v tomto rozpočtu
velký vstupně závislý výsledek do A. Běžné čtení stojí2u;
zbývající jedna adresová instrukce nedostane |A| nad4098,
zatímco 3^13=1594323. Důkaz se tedy neomezuje na běžné zápisy
programu ani na zákaz samomodifikace. Spolehlivost periferií není
potřeba: přenositelný program musí fungovat i bez nepředpokládaného
vstupního zařízení, viz výslovná konvence na136.

Sedmislovné prostorové minimum úlohy22 zůstává otevřené. Důkaz
o délce řetězce násobení se nepřenáší na všechny MIX programy.
Celá úloha22 proto zůstává partial. Nový výpočet nebyl potřeba.

## X0685: tři slova pro úlohu17(a)

Root přečetl obě zmrazené poznámky `two-word-zeroing-obstruction.md`
a `zeroing-io-bridge.md` a přímo porovnal originály136,142,143,508.
Přijímáme tři slova jako minimum v následujícím standardním modelu:
počítají se všechny buňky používané za běhu pro kód a pomocná data;
program nepředpokládá zařízení nebo připravené médium, které zadání
neposkytuje. Nejde o měření pouhé délky počátečního zaváděče.

Pro vstup N=2 jsou potřeba tři výstupní nuly. Dvě kódové buňky
s počátkem3000 mohou opakovaně zapisovat pouze ve tvaru sousední
zapisující instrukce a zpětného skoku. STORE nemění indexy;
samomodifikace adresy vyžaduje zápis zpět do kódu. Jakmile začne
zapisovat mimo kód, další cíl už nemění. Tím nelze vynulovat tři
různé výstupy. MOVE vyžaduje předchozí nastavení libovolného I1;
po jeho nastavení ve druhé buňce nezbývá žádný vytvořený nulový
zdroj. Překrytí MOVE nenulových slov první nulu nevytvoří.
Poznámka výslovně rozebírá přepis obou instrukcí a kód ve výstupu.

Samostatná omezená věta nepoužívá IN. Pro přenositelný kontrakt
to stačí: na136 je veškeré I/O vybavení volitelné a16/17 žádné
zařízení nepředpokládají. Univerzální dvouslovný program by musel
fungovat i na instalaci bez použitelného IN. Toto je rozšíření
kvantifikátoru přes přípustné instalace, nikoli neprokázaná
transformace libovolného programu s I/O na program bez I/O.
Na pevném vybaveném stroji s jiným měřením prostoru takovou
neomezenou větu netvrdíme. Horní mez je knižní tříslovná smyčka.
Celá17 zůstává partial kvůli času části(b).

## C0083: potvrzená chyba podmínky Wahidova programu

Root přímo zobrazil erratum z28.2.2018 a knižní143,131,134,135,136.
Zadání23 určuje celé slovo včetně znaménka plus. Podmínka rA>=0
však připouští−0. Pro A=−0 a mem[200]=+0 ponechá SLA znaménko
a každé ADD s nulovým součtem ponechá staré znaménko A. Také
HLT nic nenormalizuje. Po všech27 instrukcích je tedy A=−0;
předepsaným výsledkem je+0. Nejde o spor s číselnou interpretací22:
zde je znaménko explicitní součástí výstupního slova.

Root přečetl nový cílený checker, kód úplné stopy, příslušné větve
`mix_machine.py`, souhrn148 případů a všech27 záznamů stopy.
Ruční invariant platí ve všech37 radixech;37 nových protipříkladů
a111 kontrol souhlasí. Žádný úspěšný starý test se neopakoval.
Obecně zde ADD nepřeteče ani pro kladný počáteční A, protože
SLA ponechá velikost nejvýše B−b a další bajt je nejvýše b−1.

Přesná minimální redakční oprava je `if rA has a plus sign`.
Zachová sedm slov i správnou kladnou nulu. Přidané ENTA0 funguje
pro libovolný A za cenu osmého slova. Globální minimalita23 tím
není dokázána. Nález se týká zveřejněné odpovědi2018, nikoli
původního Dixonova programu1997. Staré přijetí podmínky v X0150
je výslovně opraveno; zdrojové zmrazené balíčky se nemění.

Všechny čtyři vrstvy errat byly znovu porovnány; přesné bloky
a otisky jsou v `results/wahid-errata-root-review.json`.
Odpovídající pozdější oprava nebyla nalezena. Místní ASCII návrh
`reports/V1-C0083-wahid-negative-zero-draft.txt` nebyl odeslán;
potvrzení není tvrzením prvenství nebo přijetí autorem.

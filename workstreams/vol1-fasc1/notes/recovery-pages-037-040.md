# Obnova úplného rozsahu: souborové strany 37–40 / tištěné 29–32

Přečteny celé čtyři strany, nikoli pouze začátky položek V0080–V0087.
Uzavřené důkazy se přebírají níže s konkrétními předpoklady; nevykonává
se znovu Maximum, Hello ani Program P. Jediný nový numerický krok je
malý certifikát čtyřiceti vytištěných prvočísel a jejich pořadí.

## Strana 37 / 29: Program M a všechny komentáře a)–e)

V0078–V0081 v `independent-arguments-028-032.md` pokrývají všech jedenáct
instrukcí M. Vstup: `1 ≤ n < 2^60`, přípustná octabyte tabulka signed
hodnot X[1..n], neměnný globální základ x0 a správný rámec volání.
Předpoklad zaručuje `0 < 8n < 2^63`; `kk` tedy funguje zároveň jako
byteový offset a kladný čítač. Na vstupu do Loop je m maximum suffixu
X[k+1..n] a j jeho nejpravější výskyt. CMP neprovádí přetékající rozdíl;
PBNP zachová m,j při X[k]≤m a obě změny se provedou právě při X[k]>m.
SUB snižuje k až na nulu. Případ n=1 nemá vstup do Loop. Všechny
adresy, opcode a operandová pole v levém sloupci jsou v převzatém
V0081 jednotlivě vyčísleny, včetně backward PBP −6 a SET jako ORI s 0.

V0080 odvozuje každý profilový počet i obě předpovědi větví. PBNP stojí
`(n−1+2A)υ`, PBP `n+2` υ, celkem `nμ+(5n+4A+5)υ`; pro n=1 je to
`μ+10υ`. Jde přesně o deklarovanou cenu instrukcí tabulky 1, nikoli
o měření libovolného hardware nebo dalšího přerušovacího kódu.

V odstavci a) jsou tři sloupce právě syntaxe symbolického programu;
b) jeho numeric ekvivalent je doložen výše. Obecné tvrzení o assembleru
je popis jazyka a existence jeho překladače, ne časová mez. Skutečný
`mmixal-20250620.w` obsahuje definici všech opcode, výrazů, labelů a
pseudooperací; výroky „easily“ a „virtually all“ jsou kvalitativní
redakční popis, nikoli tvrzení s nevysloveným numerickým prahem.
c) Čísla řádků stojí mimo LABEL/OP/EXPR; nejsou operandem ani kódem.
d) §1.2.10M je skutečně na tištěné straně 96 svazku 1, kde M1 nastavuje
k=n−1 a M2 testuje konec před porovnáním. Zde inicializace k=n a první
skok na DecrK přesune tutéž kontrolu za dekrement. Stejný suffixový
invariant a všechny případy shod proto platí. Tato vazba nevyžaduje
opakovat pravděpodobnostní analýzu A; počet změn je v obou programech
totožný. Převzatý úplný argument je též ve
`../../vol1/notes/analysis-records.md`, úvodní oddíl. e) Profil byl
pokryt samostatně, včetně n=1.

Poslední tři odstavce: `j IS $0`, `kk IS $2` dávají SR `3d000203`;
LOC #100 a čtyřbytové instrukce dávají Maximum=#100 a Loop=#10c.
IS a LOC se při sestavení větví na `bypass`, LOC pouze mění `cur_loc`
(`mmixal` 3103–3105). Doporučení #100 má konkrétní zdůvodnění:
TRIP vstupuje na 0 a osm aritmetických tripů na #10,…,#80
(`mmix-doc` 2169–2185); volitelná inicializace knihovny používá #f0
(`mmix-sim` 452–461). Tvrzení nezakazuje jiné platné umístění.

## Strana 38 / 30: pseudooperace, volání M a celý Hello

První tři odstavce jsou pokryty právě výše uvedenými IS/LOC pravidly,
bezpečným 8k a výpočty relativních offsetů. JMP v #108 na #120 má 6,
PBNP v #114 na #120 má 3 a PBP v #124 na #10c má −6 tetrabytes.

V0082 se přebírá z **uzavřeného** V0124 v
`independent-arguments-052-065.md`, nikoli z historického partial
odstavce V0082. `SET $2,100; PUSHJ $1,Maximum` dává callee $0=100.
POP 2 přesune callee $1=m na odkazové místo caller $1 a ponechá
callee $0=j jako caller $2. Návrat je přesně k následujícímu STO.
Přípustný rámec a platná tabulka jsou explicitní, fyzický SAVE/UNSAVE
ani správnost libovolného zásobníkového prostředí se znovu nedokazují.

V0083–V0084 pokrývají všech pět instrukcí H a devět datových bytů.
NNIX argumenty dávají první pointer na řetězec Hello; LDOU jej načte,
Fputs vypíše přesně znaky před prvním nulovým bytem. Vrácená hodnota
prvního Fputs v $255 nevadí: GETA ji nahradí adresou String. Druhý
Fputs připojí sedm znaků `, world` a LF; Halt ukončí běh. Platí obvyklý
kontrakt úspěšného standardního výstupu. Kód nevyžaduje nezměněnou
návratovou hodnotu Fputs. `mmix-sim` 359–369 a 425–430 určují přesně
čtený řetězec, handle i použití $255; hodnoty Fputs=7 a StdOut=1 jsou
přímo v tabulce `mmixal` 2055/2083. GETA #108→#114 má 3; všechny
numeric instrukce a bytes jsou vyčísleny ve V0084.

Poslední odstavec má také skutečný podklad: `mmixal` 3140–3150,
3215–3226 přijímá soubor Hello.mms a bez −o nahradí poslední s znakem o,
tedy vytvoří Hello.mmo. `mmix-sim` 851–865 nejprve zkouší přesné jméno
Hello a při jeho neexistenci Hello.mmo. Předpoklad příkladu je, že není
jiný objektový soubor se samotným jménem Hello. Tyto názvy a významy
mms/mmo stanoví také `mmixal` 693–696. Není tvrzen nový assembler run.

## Strana 39 / 31: celý NNIX argumentový kontrakt

`mmix-sim` 55–59 a 2930–2935 přesně rozlišují options před jménem
programu a předané argumenty od jména programu dále. `−P` nastaví
profiling (2967); fetch zvýší frekvenci aktuální adresy (1415–1420)
a konec simulace volá tisk všech frekvencí (2914). Rekurze print_freqs
1223–1237 projde paměťový strom a 512 pozic každého uzlu právě jednou,
ve vzestupném pořadí. Jde o počty v mezích hostitelského čítače;
kniha zde neslibuje neomezený celočíselný profil libovolně dlouhého běhu.

Main je předepsaný vstup **uživatelského programu** (`mmixal` 671–675,
`mmix-sim` 433–449). Toto není tvrzení o první vykonané instrukci
celého loaderu a knihoven: primární zdroj výslovně dovoluje prelude
na #f0, které pak předá řízení Main. Pro ukázku H žádné takové prelude
není sestaveno. Uchovávám tento přesný význam běhové konvence, nikoli
skryté tvrzení, že skutečný simulator nikdy nemůže nejprve vykonat #f0.

V0085 ověřuje všechny vytištěné adresy a ASCII slova. Skutečná konstrukce
v `mmix-sim` 3365–3384 začíná s x=Pool+8 a loc=Pool+8(argc+2).
Na začátku průchodu k je x adresa k-tého pointeru a loc první volná
octabyte adresa řetězce. Zapíše se pointer a přesně délka d nenulových
bytů. Posun `8+(d & -8) = 8 ceil((d+1)/8)` rezervuje celý řetězec
včetně terminátoru. Nenapsaná paměť pochází z nulovaného calloc
(sim 747), takže poslední NUL i nulový pointer za argc argumenty
zůstávají nulové. Indukce dává nesousedící řetězce, sousední pointery
a octabyte zarovnání každého začátku. Pro argc=3 a délky 3,3,5 jsou
loc přesně #28,#30,#38 v Pool segmentu, nulový pointer na #20.
Počáteční $0=argc a $1=Pool+8 určuje postamble 1049–1053.
Přípustná paměť příkladu neobsahuje kolidující ručně sestavená data
v Pool segmentu, jak vyžaduje obecná MMIXAL načítací konvence.

Navazující odstavce o H jsou přesně již doložené dvě Fputs, Halt a
BYTE. BYTE vytváří jeden byte pro každý výraz a posune lokaci o počet
bytů (`mmixal` 513–527); sedmiznakový řetězec expanduje na sedm
jednoznakových konstant. Obecný řetězec nemusí být zarovnán: Fputs
kontrakt čte znaky od zadané byteové adresy a nemá podmínku zarovnání.

## Strana 40 / 32: data H, úplný Algorithm P a 40 čísel

Pokračování H je přesně `2c 20 77 6f 72 6c 64 0a 00`:
sedm znaků, ASCII LF a NUL. Význam LF je textová výstupní konvence,
nikoli požadavek na libovolné binární zařízení. Úplná ASCII tabulka
již má vlastní přijatý certifikát, není znovu přepočítána.

V0086 v `independent-arguments-028-032.md` se přebírá **včetně dodatku**.
Je doložen invariant postupně uložených prvočísel, obě větve r=0 / r>0,
neobvyklá podmínka q≤p a dostupnost již uloženého divisora. Důkaz
`C(8192,4096)>2^8178` a omezení každého prvočíselného příspěvku
na 2^13 zaručují více než 500 prvočísel pod 8192. Pomocné divisory
3,5,11,97 pokrývají všechny kandidáty do této meze. Tím je ukončení,
správný pořádek, žádná duplikace a bezpečný rozsah vyřešen nezávisle
na následujícím malém číselném certifikátu. P9–P11 pak projdou všechny
indexy `50c+m`, 0≤c≤9, 1≤m≤50; dělení indexu−1 číslem 50 dokazuje
bijekci. Nadpis a čtyřmístný zápis jsou přesná specifikace formátu;
instrukční realizace je až na dalších stranách.

Dosavadní V0087 postrádal numerické pořadí čtyřiceti uvedených hodnot.
Originální sazba `images/file-040-p032.png` znovu zobrazena a přepsány
všechny řádky m=1,2,3,50. `verify_printed_prime_indices.py` provedl
jednou při nice 15 síto na **2..3571**. Každé označené n má uložený
vlastní dělitel p, 2≤p<n. Neoznačené n je prvočíslo: kdyby bylo
složené, nejmenší prvočíselný dělitel p by byl ≤sqrt(n)<60 a při
zpracování p by n≥p² bylo označeno. Takové p samo zůstává neoznačené,
protože prvočíslo není násobkem menšího čísla. To dokazuje úplnost
nezávisle na Algorithm P a bez náhodného testování primality.

Výsledek `results/printed-prime-indices.json` obsahuje všech 500
prvočísel, 3070 vlastních dělitelů zbývajících čísel a všech 40
rovností na příslušných indexech. Vše souhlasí včetně p_500=3571.
Pevná konečná doména je dána posledním vytištěným číslem; nejde
o opakování Program P, jeho počtu DIV ani historického benchmarku.
V0087 tedy přechází z partial na argument_recorded. Poznámka autora
o záměrné neobratnosti příštího programu není optimalitní tvrzení.

## Rozsah a provenance

Všechny věcné matematické, kódové a běhové výroky těchto čtyř stran
mají výše samostatný argument nebo přesné převzetí. Nezůstal nový
finding ani nevyřešená technická věta na těchto stranách. V0096
(historické počty a čas Program P na straně 45) zůstává samostatně
partial; tímto blokem se nijak neuzavírá.

Nový primární soubor `sources/mmixal-20250620.w` je jediný vytažený
člen již uloženého autorova archivu `sources/mmix-20250620.tar.gz`.
SHA256 assembleru je
`1335621eb854fc6d34689b5812cbdf2fc4aaead59e30d4f2bd7acf32d7cd5071`.
Archiv má dříve uloženou provenance v `sources/fp-primary-metadata.json`;
neproběhlo nové stahování. Dokumentace a simulator 2013 jsou tytéž
primární zdroje již použité v ostatních důkazech, nikoli nový build.

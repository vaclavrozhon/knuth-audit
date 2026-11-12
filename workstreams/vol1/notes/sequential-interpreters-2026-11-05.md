# Souvislý průchod §1.4.3 — 5. listopadu 2026

Přímo přečteny všechny původní strany200–214 a530–531, celé
`parallel/interpretive/NOTES.md`, `SELFTRACE.md` a předchozí kořenová
revize `notes/interpretive-root-review.md`. Uložené výsledky simulátoru,
I/O, GO/SPEC, trasování a samotrasování porovnány s uvedeným rozsahem;
úspěšné běhy nebyly opakovány. Současná čtyři errata porovnána podle
stran i tématu, přímo zobrazeny all1-prepre17/39 a all1 8. Výpis
s otisky: `sources/sequential-2026-11-05/interpreters-errata-extract.json`.

## Simulátor a jeho devět úloh

Oddělená velikost a znaménko±1 představují i zápornou nulu. CYCLE
nejprve přičte odložený TIME; stav těsně před CYCLE nelze popsat
samotným CLOCK jako celým již spotřebovaným časem. MOVE přičítá
další2u za slovo průběžně. Platí konečný reprezentovatelný čítač,
nikoli neomezený čas. Fyzické časy hostitelského I/O nejsou
simulovaným časem.

Dekódování počítá M s podepsaným indexem a ověřuje dvoubajtovou
mez; OPTABLE indexované C−63 skutečně končí položkou63. Pole
F=8L+R se rozloží dělením8, ověří L≤R≤5 a zpracuje včetně samotného
znaménka. GETV/GETAV zarovnají vybrané byty vpravo; STORE složí
nezměněné pravé/levé části a zvolí správné znaménko. ADD/SUB při
opačných znaménkách zachovají původní znaménko přesné nuly; MUL/DIV
zvlášť nastaví znaménka součinu, podílu a zbytku. Neurčený výsledek
DIV při přetečení není vydáván za chybu. JOV/JNOV vždy vypnou
simulované přetečení, JSJ nemění JREG a ostatní uskutečněné skoky
uloží následující PC. Registr−0 pro skok není záporný. ENT/ENN při
nulové efektivní adrese znovu převezmou znaménko instrukce.

FCHECK lze sloučit se vstupem MEMORY při zachování samostatného
vstupu bez kontroly F. SHIFT opakuje jednotkový posun nebo rotaci,
tedy souhlasí i pro velké M a M=0; znaménka neposouvá. MOVE kopíruje
sekvenčně, takže zachovává nativní překryv; F=0 nemění I1 ani
jeho znaménko. GO načítá kartu a čeká před vstupem do programu.
Součet časů34+52+11=97u pro LDA,34+21=55u pro ENTA, příplatky
15u indexace,5u vynechaného znaménka,2u nulové adresy souhlasí.
Neurčený historický test8422/178 nebyl rekonstruován: chybí program.
Jeho podíl≈47.3146 a obecný odhad50:1 jsou aritmeticky správně.

I/O zadání výslovně omezuje jednotky na16/18. Přijaté úplné MIX
řešení sleduje READY a DUE, provede každý odložený přenos právě
jednou a vyřídí splatné události i při vynuceném čekání a HLT.
JBUS* může přeskočit neproduktivní čekání, ale zachová JREG po
alespoň jednom provedeném skoku a čas posledního neprovedeného
testu. Paměťový buffer musí celý ležet v0..3499; konec celé
implementace3965 je legální. U neurčeného konfliktního I/O se
neslibuje jediný hardwarový výsledek. Falešné tvrzení úlohy8 má
správnou odpověď: pád z3499 načte BEGIN=3500 a následné STZ TIME
vyvolá MEMERROR. Doplněk9 z1.1.2025 je samostatně řešen pro
NUM/CHAR/HLT, včetně opravené doby10u pro první dvě operace.

## Trasovač a sedm úloh

Kopie instrukce bez skoku může běžet na INST, protože MIX zde
nemá adresování relativní k PC. STJ se virtualizuje pomocí A;
podmínky skoků vyhodnotí původní hardware a pouze adresy se
přesměrují. Pomocná aritmetika nemění CI ani overflow. Obnova J
přes dočasný skok na j−1 funguje pro výslovně předpokládané j≠0;
základní LEAVE naopak J nezachovává, jak kniha upozorňuje.

Páskový záznam má10slov, buffer100slov. Kombinace JNOV a ADD(B−8)
zachová původní overflow a zakóduje požadovaný byt; JL/JE doplní
CI, aniž jej změní. **Známá oprava2008 na531 je podstatná:** I1 se
musí obnovit před větví STJ, jinak ji tato větev přeskočí a použije
index bufferu. Původní chyba i oprava mají přijatou reprodukci.

Při prostém samotrasování se zničí PREG; správná první posloupnost
je3500,3501,3502,3503,3504,3505,3501,… . Dvě sdílející kopie také
ničí kontext; konkrétní perioda82 kroků je dokázána rovností celého
stavu pro konkrétní inicializaci, nikoli pro všechny možné vstupy.
Vlastní samotrasovač odděluje každou logickou paměť slovníkem nad
neměnným obrazem. Všechny fetch/store/MOVE přístupy jsou logické;
indukce proto dává oddělené stroje. Paměť roste alespoň
U(d+1)≥2(U(d)+1), tedy U(d)≥2^(d+1)−2. Konečná kapacita se
vyčerpá. Plné běhy128slov a test hranice2000slov jsou různé
doklady; dlouhý úplný běh2000slov se podle pokynu uživatele nedělá.
Třetí úroveň má doklad z výslovně dosažitelného mezistavu.
Skokový tracer rekonstruuje intervaly mezi skoky, pokud zná
začátek/konec; omezení samomodifikace je v odpovědi výslovné.

**C0039 ponecháno jako kandidát, nikoli potvrzeno.** Na214 stojí
„only three restrictions“ a bod(a) zakazuje pouze zápisy. LDA AREG
při AREG=0 a A=1 pod tracerem vrátí1 místo0. V běžném výkladu je
však pracovní oblast implicitně vyhrazená; nejde o selhání programu
v jeho jasně zamýšleném použití. V UI přesná lokace214, oranžová.
Tato významová nejistota drží hlavní §1.4.3.2 ve stavu partial.

## Prameny, výjimky a stav

Přijata konkrétní pramenná kontrola Randell–Russell1964 s.34–36,
tex.web modulů545/583, dokumentace dvips a druhého vydání
PostScript1990 v později elektronicky revidované podobě. Úplné
články Knuth1963/Evans1964 a přesná sazba TeX1986/1997 jsou
bibliograficky přeskočeny, nikoli ověřeny z metadat. Osobní příhody
na203 jsou autorské svědectví; nevydávají se za nezávisle změřená
zrychlení. Tvrzení o nejstarších interpretech201 je ponecháno
otevřené do související historické části§1.4.5, hlavní§1.4.3 partial.

X0224 se červeně mapuje na205 (SPEC),211 (chybějící uvozovka),213
(neexistující mnemotechnika JXL v komentáři) a531 (obnova I1).
Změny loga/kurzívy202, závorek204 a zpřesnění správného komentáře208
nejsou obsahové vady. Oprava odkazu211 platí pro3.–5. dotisk;
náš první dotisk už má správné1.3.1–26. Nová úloha212 není chyba
původní knihy. Všech8+1 a7 úloh je matematicky uzavřeno. Nové
neznámé chyby0. Další průchod začíná I/O na215.

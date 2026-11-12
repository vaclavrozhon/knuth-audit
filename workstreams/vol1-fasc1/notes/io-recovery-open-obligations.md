# Pracovní přesné I/O povinnosti při obnově file 46–51

Tento soubor není uzavřený důkaz ani ledger nález. Přečteny celé knižní
file 46–51, dosavadní V0098–V0107 a celý primární
`sources/mmix-io-20250620.w` (403 řádků). Další práce nejprve rozhodne
konkrétní chování Fwrite; celé nové stránky ještě nejsou hotové.

## Fwrite — jednoznačný kontrakt a přesná chyba aktuálního bloku

Kniha p42 a MMIX-SIM 348–357 oba vyžadují návrat `n-size`, kde n je
počet úspěšně zapsaných bytů. Primární text dodává přímo C ekvivalent
`fwrite(buffer,1,size,file)-size`, takže při hostitelském short write
zde není prostor vykládat návrat jako počet pouze zahájených bytů.
Dispatcher MMIX-SIM 2395–2406 výsledek uloží do rBB a odtud bez změny
do $255.

MMIX-IO `mmix_fwrite` (řádky přibližně 274–294) načte blok n≤256,
nejprve `size=incr(size,-n)` a potom při `fwrite(...,n,...)!=n` vrací
`-size`. Je-li na vstupu smyčky zbytek R a skutečně se z bloku podaří
zapsat k<n, správně je k−R; původní kód vrátí n−R. Rozdíl je n−k>0.
Pro R=n=1,k=0 vrací dokonce úspěch 0 místo −1. Všechny dřívější
bloky v tomto stavu byly úspěšné, proto je toto současně správná
globální odchylka od celkového původního požadavku.

Plánovaná auditní oprava: udržet R do zjištění hostitelského výsledku,
zachytit `written=fwrite(...)`, při written<n vrátit written−R,
teprve při úspěchu odečíst n. Protože 0≤written≤n≤256, převod
size_t→int je přesný. Beze změny zůstanou režimy, úspěšný přenos,
adresní posuny a dosavadní aritmetika. Vlastní proof-domain pro
znaménkový návrat: 0≤S<2^63 a platný zapisovatelný handle/buffer.

Dokončeno jako samostatný programový nález **MMIX-S0005**; viz
`MMIX-S0005-fwrite-short-count.md` pro úplný invariant, patch, 22 uložených
volání, původní sazbu a deset vrstev errat. První nový pokus selhal při
CWEB buildu opravy po 11 neuložených původních voláních; následný krátký
rerun a tato okolnost jsou výslovně doloženy, žádné starší běhy se neopakovaly.

**Samostatná neuzavřená větev:** ignored `fflush` failure. Patch pro
short fwrite ji nesmí vydávat za opravenou; pokud fwrite n vrátí celé,
ale flush selže, aktuální kód výsledek flush vůbec nečte. Fputs/Fputws
mají podobné ignored fflush. Je nutné stanovit přesný kontrakt počtu
bytů přijatých streamem proti úspěšnému fyzickému vyprázdnění.

## Ostatní skutečně přečtené větve, zatím neuzavřené

* Fgets: knižní a MMIX-SIM próza říká EOF před size−1 nebo newline →−1,
  ale týž primární odstavec uvádí C fgets/strlen ekvivalenci při absenci
  vnitřních NUL, která u krátkého posledního řádku vrací délku. Tuto
  dvojznačnost nelze uzavřít jen tvrzením, že host C je normativní.
  Skutečný kód při neúplném EOF a vnitřním NUL navíc zastaví count na
  prvním NUL; odstavec přitom výslovně říká, že NUL se počítá jako
  ostatní znak. Příklad soubor 00 41 EOF, size=4, dá podle větve 0,
  nikoli 2 ani požadované −1. Nebyl spuštěn.
* Fgetws: při EOF před prvním wyde fread vrátí 0, eof=true, smyčka
  uloží terminátor a vrátí o=0; próza i C fgetws ekvivalence pro prázdný
  vstup vyžadují −1. Tento případ je nyní uzavřen samostatným S0006 (18 uložených
  volání, úzký patch a invariant v MMIX-S0006-fgetws-empty-eof.md).
  Neprázdný unterminated EOF a současné sticky EOF/error flags zůstávají
  mimo potvrzený svědek. Odd buffer se
  navíc zarovná dolů, což vyžaduje vyjasnit předpoklad adresy wyde.
* Fread: pro normální (ne stdin) větev rozlišuje ferror a EOF a vrací
  správný n−size; stdin jde přes `stdin_chr` a neřeší konvenční EOF
  stejně. `size.h!=0` vrací serious error. Převod size.l do signed n
  nad INT_MAX nemá zatím obecný důkaz; není třeba takový přenos spouštět.
* Ftell: na LP64 hostu uloží `long x` pouze do nízkého tetra a horní
  nastaví na 0. Pro pozice ≥2^32 tak hrozí truncation; reachability
  přes dovolované MMIX I/O a odpovídající podporu hosta není dosud
  rozepsána. Fseek sám připouští jen signed32 offsety a jinak vrací
  −1. Žádný multi-gigabyte soubor ani přenos nevytvářet.
* Fclose standardních handles pouze deaktivuje mode a hostitelský
  stream nezavírá, což je zdokumentovaná ochrana stdio; nelze to
  automaticky označit za chybu, když MMIX handle je skutečně uzavřen.
* Fopen režimy r/w/rb/wb/w+b a inicializace 0,1,2 souhlasí s deklarací;
  chybové větve a obnovování dřívějšího handle ještě nemají plný rozbor.

## Další jazykové doplnění v rozpracovaném bloku

Figure15 komentáře po prázdném EXPR mají skutečnou větev: neznámý
první opening token (`/` u /* či //) změní celý operand list na 0
(`mmixal` 2351–2375); dvojité ;; zahájí druhý „instruction“ s prvním
znakem ;, a label scanner jej přeskočí jako comment. Není chybné
tvrzení, že by /* nebo // musely být běžnými C komentáři parseru.

Relativní adresování má nyní přesnější zjištění po přečtení helperu:
`shift_right(...,2,0)` je aritmetický, takže původní pracovní podezření
#fffffffffffffffc→0 se **nepotvrdilo** (−1→0 dává rozdíl +1).
Skutečná hranice je #7ffffffffffffffc→#8000000000000000. Zde jsou
adresy matematicky vzdáleny 4 bez modulo wrap, ale samostatné signed
posuny dávají 2^61−1 a −2^61, rozdíl −2^62+1 a range error.
Předem definovaný target tak selže; future fixup téhož targetu nejprve
odečte adresy a potom posune +4/4=1, tedy uspěje. Primární smlouva
MMIXAL:410–420 výslovně předepisuje odečíst current location a výsledek
dělit čtyřmi; obě eventual values mají mít stejná omezení. To je
konkrétní implementační mezera, nikoli důkaz hardwarové ochrany stran.
Zatím není nový confirmed nález ani běh: zbývají originální sazba,
opravné vrstvy a krátké ověření, pokud bude nutné. Jazykový kontrakt
v knize samotné je správný. Zarovnání adres je modulo 2^64 a u horního
konce se další násobek může stát adresou 0.


### Uzavření R0006

Výše uvedená pracovní programová povinnost je nyní uzavřena v MMIX-S0007-relative-address-boundary.md: úplný důkaz, obě původní větve, původní sazba,11vrstev a39malých sestavení. File47 má po tomto doplnění úplné argumentové pokrytí; správná knižní definice nemá error.


Ftell high-tetra obligation is now resolved separately as MMIX-S0008
(notes/MMIX-S0008-ftell-high-tetra.md). Scope is successful LP64 binary
positions, with explicit host-state-model reproduction. No large file
was created and no limitation on Fseek offsets was silently removed.

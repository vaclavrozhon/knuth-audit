# MMIX-S0008 — Ftell ztrácí horních 32 bitů úspěšné pozice

**Confirmed, medium, doprovodný program; podmíněno hostem LP64.**
V obou distribucích MMIX-IO úspěšné hostitelské `ftell` vrátí hodnotu
typu `long`, ale převod do MMIX octa uloží pouze dolní tetra. Pro
úspěšnou pozici 2^32 proto MMIX vrátí 0 místo #0000000100000000.
Knižní definice je správná; tento nález je pouze v software-ledger.

## 1. Normativní kontrakt a přípustné stavy

Fascikl p43/file51 říká, že Ftell vrací polohu v bytech od začátku
souboru, nebo −1 při chybě. Primární MMIX-SIM:396–407 má tentýž text
a výslovně dodává, že C `ftell(file[handle])` má přesně stejný význam.
Povoleny jsou BinaryRead, BinaryWrite a BinaryReadWrite. Zde nejde
o nevyjasněnou textovou pozici ani o žádost za hranicí hostitelského
typu: host již úspěšně vrátil nezáporné číslo reprezentovatelné v long.

C11 N1570 §7.21.9.4, p337–338/file355–356, definuje pro binary stream
počet znaků od začátku souboru; nemožnost získat pozici vrací −1L.
Na hostu LP64 je 2^32 reprezentovatelné nezáporné long. Není třeba
předpokládat, že každý souborový systém dovoluje takový soubor. Obor
nálezu výslovně vyžaduje host a stream, na němž daná pozice existuje
a hostitelské ftell uspěje. Selhání ftell je jiná, správná větev.

MMIX-IO:44–49 požaduje 32bitové unsigned int pro tetra. To LP64
splňuje. Celá README obou distribucí byla přečtena; nepožaduje
32bitový long. Popis MMIX-ARITH jako aritmetiky pro 32bitový počítač
určuje použitý stavební blok, nikoli zákaz širšího hostitelského long.
Samotný MMIX-IO pro výsledek ftell vědomě deklaruje `register long x`.
Pro host s 32bitovým long tento konkrétní rozpor nenastává.

## 2. Dosažitelnost bez nepovoleného velkého offsetu Fseek

Fseek má v implementaci vlastní omezení offsetu na signed32. To
neomezuje všechny dosažitelné **polohy** na signed32. Uvažujme již
existující binary soubor délky L=2^32 na podporujícím hostu:

1. Fopen v režimu BinaryRead otevře `rb`, tedy soubor nezkrátí.
2. Fseek(−1) prochází testy offset.h=ffffffff a sign bitu offset.l.
   Na zkoumaném GCC hostu se `(int)0xffffffffu` rovná −1, takže
   předá `fseek(fp,0,SEEK_END)`. Předpokládáme jeho úspěch.
3. Ftell nyní obdrží hostitelské long L a musí vrátit MMIX octa L.

Předpoklad převodu unsigned do signed je v této cestě výslovný;
test jej ověřuje assert, nikoli obecnou přenositelností C. Nulový
offset SEEK_END je povolený a není odmítnut omezením signed32.
Samotný Fopen/SEEK_END důkaz nevyžaduje přenos 2^32 bytů ani výpočet
tohoto počtu jednotlivých kroků. Uložená reprodukce modeluje tento
legální stav a nevytváří skutečný velký ani sparse soubor.

## 3. Přesná příčina, propagace a celá rodina rozporu

MMIX-IO:364–375 (§22, původní veřejná sazba p9) obsahuje:

    if (!(sfile[handle].mode&0x4)) return neg_one;
    x=ftell(sfile[handle].fp);
    if (x<0) return neg_one;
    o.h=0, o.l=x;
    return o;

Nechť B=2^32. Při x≥0 unsigned konverze do tetra přesně dává
o.l=x mod B, avšak o.h se nastaví na0. Výsledek je tedy x mod B,
nikoli x. Pro každé úspěšné x v [B,LONG_MAX] na LP64 se liší o
B floor(x/B)>0. Pro 0≤x<B je správný. Tento důkaz pokrývá i
nenulové dolní bity a maximální signed64 hodnotu; neodvozuje celou
rodinu pouze z příkladu B.

Skutečný dispatcher MMIX-SIM:2403–2406 uloží návrat mmix_ftell
přímo do rBB a poté do globálního $255. Nic zde horní bity
neobnoví ani netestuje původní hostitelskou pozici. Instrukce
`TRAP 0,Ftell,3`, strojově #00000a03, proto pozoruje právě chybný
výsledek. Pro předchozí Fseek se $255 nastaví na −1 a vykoná
`TRAP 0,Fseek,3`, #00000903. Důkaz je o zavedených simulátorových
službách; žádná vlastnost libovolného OS či jiného trap handleru
se z něj nevyvozuje.

## 4. Oprava, všechny větve, meze a náklady

Samostatný change file `sources/audit-ftell-high-tetra.ch` mění
pouze poslední převod:

    o.h=(unsigned long)x>>16>>16, o.l=x;

Obor důkazu opravy: tetra má32 bitů a unsigned long32 nebo64 bitů;
x je po původním testu v [0,LONG_MAX]. Převod do unsigned long je
proto přesný. Dva unsigned posuny po16 dávají floor(x/B), aniž by
se kdy posouvalo o celou šířku slova. Na 32bitovém hostu jsou oba
posuny definovány a výsledek druhého je0. Na 64bitovém je výsledné
horní tetra nejvýše #7fffffff a převod do tetra je přesný. Dolní
tetra zůstává x mod B. Rekonstrukce B floor(x/B)+(x mod B)=x
prokazuje správný návrat pro celý obor, včetně0, B−1, B a LONG_MAX.

Pokud režim není binary, první větev dál vrací −1 bez volání hosta.
Jestliže host vrátí záporný error, druhá větev dál vrací −1 a nový
výraz se nevyhodnotí. Všechny úspěchy pod B jsou beze změny; nad B
se obnoví přesně chybějící bity. Žádná smyčka, čtení nebo zápis
souboru se nepřidává, poloha streamu se nemění, práce i paměť jsou
O(1). Nejde o opravu omezeného offsetu Fseek, podporu 128bitového
long ani příslib úspěchu všech hostitelských souborových operací.

## 5. Původní znění, errata a malá reprodukce

Oba celé MMIX-IO zdroje2013/2025 jsou byte-identické, SHA-256
`d6732108356986956f4e4a5a883d210a1e4e69216e1f8d614c456fd3126496e5`.
Veřejné původní PDF [MMIX-IO §22](https://mmix.cs.hm.edu/doc/mmix-io.pdf#page=9)
má drobně odlišnou unsigned deklaraci handle, ale přesně stejný long,
oba guardy a `o.h=0,o.l=x`. Sazba p9, knižní p43 a obě strany
C standardu byly zobrazeny; nejde jen o OCR. Metadata a přímé zdroje
jsou součástí evidence. Fyzický výtisk MMIXware nebyl kontrolován.

Deset dosavadních vrstev oprav je uloženo v `results/errata-S0008.json`
s hashi a kontexty. Nalezená MMIXware oprava p43 se týká privilegovaných
trapů a uloženého rK; zdejší normativní i implementační části Ftell
jsou jiné. Ostatní výskyty long jsou dlouhá forma errat, věta o stacku
a délka názvu. Cílené hledání v obou primárních veřejných doménách
nenalezlo odpovídající opravu. Nejde o tvrzení světového prvenství.

Jeden `nice -n 15` běh `verify_ftell_high_tetra.py` už je uložen:
**16 volání, 4 úspěšné build kroky**. Osm případů se provede na
společném originálu obou verzí a osm na auditní opravě. Originál
selže pro B, B+17 a 2^63−1; oprava souhlasí ve všech osmi. Kontroly
jsou0, 2^31−1, B−1, hostitelský ftell error a nebinární režim.
V každém vhodném režimu se opravdu provede zdrojový mmix_fseek(−1)
před mmix_ftell; zaznamenány jsou oba hostitelské call counts i poloha.

Hostitelské fseek/ftell v driveru jsou **model legálního LP64 stavu**:
seek s0/SEEK_END nastaví model_position=model_length, ftell vrátí
tuto long hodnotu nebo explicitní−1. Skutečný prázdný tmpfile slouží
jen jako validní neprůhledný FILE pointer. Modelovaná délka není
délkou tohoto skutečného souboru. Žádná velká data se nepřenášela;
není tvrzen empirický test souborového systému na 4GiB souboru.
Pomocné octa operace jsou přesné uint64 modulo operace a oracle
je modelovaná nezáporná poloha, nikoli návrat testované funkce.

Driver výslovně kontroluje sizeof(tetra)=sizeof(int)=4, sizeof(long)=8
a potřebný převod pro −1. Příklady dokládají konkrétní původní C větev;
obecný rozpor a úplná oprava jsou samostatně prokázány výše. Uložené
výsledky stačí k revizi a nemají se znovu spouštět.

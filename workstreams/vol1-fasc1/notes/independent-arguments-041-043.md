# §1.3.2′ — I/O kontrakty p.41–43

Jde o ověření číselných vztahů a konkrétních calling sequences v popsaném kontraktu. Nejde o test všech hostitelských chybových stavů či o důkaz shody externího MMIXware s tímto popisem. Používá se platný buffer a kladná velikost, která se vejde do popsaných signed návratových počtů; nulové/obrovské nevalidní parametry nejsou dodatečně specifikovány.

**V0102 — Fopen/Fclose (p.41).** Byte handle má256možných hodnot, takže handle5 je platný. Arg obsahuje pointer a mode ve dvou8bytových slotech; forward1F smí být vOCTA podleassemblerového pravidla. NásledujícíBYTEfoo,0 uloží66,6f,6f,00 a1H dá adresuprvníhoznaku, kterou prvníArgslot dostane. LDA$255,Arg předáadresustruktury, nikoli přímopointerfoo. BinaryWrite je jedna ze tříWritevariant, které podledefinice zahazujístarádata. Fclose nemá dalšíargument, tudíž stačíTRAP bezpředchozíhoSET. Return0/−1 rozlišuje oba stavy přesně znaménkem. Počátečníhandles0,1,2 majídeklarovanéread/writekontrakty; nejde o nové matematickétvrzení o skutečnémOS.

**V0103 — Fread/Fwrite (p.42).** Při požadavkus a n úspěšnýchbytech,0≤n≤s, leží návrat n−s v[−s,0]. Nulaznamenáúplnýpřenos, záporné číslo velikostchybějícíčásti. Freadseriouserror−1−s leží těsněmimo tentointerval, takže je odlišitelný odkrátkéhočtení včetněn=0. Obaargumentybuffer,size zabírají dvěOCTA stejnějakoFopenArg. Dvojice$255=Arg aTRAPsodpovídajícímfunctiontudíž předává všechny potřebnéúdaje. Vysvětlení „negative ifferror“ zahrnujeneúplnýpřenos; nevyvozuji, že obyčejnýEOFmusí být závažnáhostitelskáchyba.

**V0104 — Fgets/Fgetws (p.42).** Při s≥1 se uloží nejvýšes−1jednotek aterminátor, tedynejvýšesjednotekcelkem. Uwydes jde o2sbytůa newline000a. Zastavovacípodmínkou jsou délka neboLF, nikoli vloženýNULbyte; ztráta takovýchdat vNextChar již má hotovýdůkazC0004 a zde se neopakuje. PravidloEOF/error aundefinedbuffer je vknizeexplicitní kontrakt, nelze si jeho chování zaměnit za automatickouplatnost hostitelskéhoC fgets. Okrajevelikostis=0 a implementačnívolbyvšechhostů nejsou zde ověřeny.

**V0105 — Fputs/Fputws (p.42).** Řetězec jesekvence nenulovýchjednotek následovanáprvnínulou; výstup končí právěpřed ní, takže nullterminator není součástvýstupu ani počtun. Předává se přímýstringpointer v$255, nikoliadresa dvouslotovéhoArg. ProgramH/P používají tuto správnouvariantukontraktu. Uwydes jejednotka2byty a0jednotka0000; fyzickáhostitelskátextováreprezentace není ztoho vyvozena.

**V0106 — Fseek/Ftell (p.42–43).** Pro délkuL aoffseto<0 je výchozípoziceL−(−o−1)=L+o+1. Protoo=−1vybereL(end),o=−2posledníbyteL−1 a o=−L−1začátek0. Proo≥0 je poziceo, zvláště0rewind. Návrat0/−1jenpotvrdí, zda je pozice provedena. Ftellvracíadresovýpočetbytů odzačátku; přepnutísměruBinaryReadWrite vyžadujeFseek podlepředepsanéhoAPI, i když se aktuálnípozice nemění. To je kontraktnípodmínka, ne vyvozenánezbytnostprokaždýOS.

**V0107 — čísla funkcí a módů (p.43).** DesetjmenFopen,Fclose,Fread,Fgets,Fgetws,Fwrite,Fputs,Fputws,Fseek,Ftell odpovídá jednou každémučíslu1..10; Halt=0 stojímimo tuto desetici. Pětmodečísel0..4 odpovídá dvěmatextovým a třembinárnímvariantám. Fputs=7 aStdOut=1 tak souhlasí svšemi dříve zakódovanýmiTRAP00000701. Jde o jediné explicitnípřiřazení, ne výsledek odvozovaný zejmen.


## Whole-page recovery correction

The complete scope is now in recovery-pages-049-051.md. V0104 is reopened
for R0008: nonempty EOF is inconsistent between primary prose and its C
analogue. R0007 separately records the exact unstated domain of the global
sign test. The older bounded numerical and calling-sequence arguments
remain valid but never prove these broader statements. Page51, including
all parts of exercises1–3, has a complete explicit argument.

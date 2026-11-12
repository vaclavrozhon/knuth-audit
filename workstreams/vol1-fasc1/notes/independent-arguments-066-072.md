# MMIX — korutiny, p. 66–72

**V0131 — symetrická vazba (p. 66–67).** GO a,b,0 uloží následující
adresu A do a a přejde na poslední pokračování B v b. GO b,a,0 provede
opačný krok. Indukčně se každá korutina obnoví přesně za svým posledním
GO; každý přenos má podle tabulky 1 cenu 3υ. Počáteční adresy musí být
nastaveny před prvním přenosem. Není potřebná adresa návratu na zásobníku.

**V0132 — gramatika a příklad (p. 67).** Po odstranění whitespace se
čte nondigit jako jediný znak, digit n spolu s následujícím znakem jako
n+1 kopií. Konkrétní tokenizace je `a,2b,5e,34,26,f,g,0z,y,w,32,10,p,q,89,r,.`.
Spojení dává a, tři b, šest e, čtyři 4, tři 6, fgzyw, čtyři 2,
dvě 0, pq, devět 9, r a period. Rozdělení po třech dává přesně
vytištěných třináct plných skupin a poslední `r.`. `1.` vytvoří první
period a tím skončí výstup, takže druhá kopie se už nevydá.

**V0133 — layout bufferů (p. 68).** TETRA s patnácti mezerami uloží
15 tetrabytes 00000020, následované 0000000a a 00000000. Má tedy
68 bajtů: tři pozice na znaky na offsetech 4j až 4j+2, mezery za prvními
15 skupinami a LF za šestnáctou. Period je na offsetu 68; OCTA InArgs
se zarovná na 72 a dvě octabytes končí na 88, kde je InBuf. LOC #100
pak přesune kód do textu, ne samotnou adresu návěští InBuf. Počáteční
nulová paměť zajišťuje první doplnění vstupního bufferu.

**V0134 — NextChar (p. 68), převzatý potvrzený C0004.** Pro vstup bez
vložených NUL instrukce POP vrací první znak >#20 a inptr ukazuje za
něj; nula terminátoru Fgets vyvolá nové čtení, záporný návrat Fgets
přepne ukazatel na Period. Obecný slíbený kontrakt pro libovolné 8bitové
znaky však neplatí: datový NUL se zamění za konec bufferu. Konkrétní
protipříklad, ověřená sazba a kontrakt Fgets jsou již v
`notes/MMIX-C0004.md`; nic se znovu netestuje ani nepotvrzuje pod novým ID.
Proto i celý níže uvedený program potřebuje při čtení této verze podmínku
bez vloženého NUL; chyba samotné transformace/Out se tím nepředstírá.

**V0135 — In (p. 69).** Po NextChar jsou hodnoty >'9' nebo <'0'
vydány jednou a pokračování leží před dalším NextChar. Pro digit n se
načte druhý znak, count=n a nejprve se jednou vydá. Po každém vydání
se count sníží; další proběhne právě pokud count≥0. Celkem tedy n+1
vydání včetně n=0. Coroutine Out musí zachovat $0, což její kód dělá.
Globální count přežije GO i pomocná volání; lokální $0 je předaný znak.

**V0136 — Out (p. 69–70).** outptr=OutBuf+4j, 0≤j<16, vždy míří na
první ze tří znakových pozic. Tři oddělené GO umožňují ukončit po period
na kterékoli pozici. Po plné neukončené skupině +=4; shoda s OutBuf+64
spustí Fputs a obnoví ukazatel. Původní mezery/LF se nikdy nezmění těmito
zápisy. Při period na pozici 0,1,2 kaskáda návěští 1H/2H/3H posune
outptr právě na její pozici; STBU +1,+2 přidají LF a NUL. Nejzazší
použité offsety jsou 63 a 64, uvnitř bufferu. Vstupní whitespace nebyl
vydáván, takže Fputs nezastaví před vlastním terminátorem.

**V0137 — inicializace (p. 70).** inptr začíná na nulové InBuf; první
NextChar ji tedy naplní. GETA in,In1 nastaví první aktivaci In, ale Out1
se spustí první: nastaví outptr a teprve pak požádá GO o první znak.
Tím je první $0 skutečně zachycen na první znakové pozici.

**V0138 — zřetězení průchodů (p. 70–71).** Pokud každý stupeň čte jen
svůj příchozí proud v pořadí a může další výstup určit z dosud načteného
prefixu a svého lokálního stavu, lze jeho write spojit s předáním položky
a read s vyžádáním další. Indukce podle vydaných položek zachová přesně
proud na každém rozhraní; mezilehlé soubory se nahradí předáním hodnot.
Na příkladu In/Out jde právě o takový případ. Obrázek 22 mění rozvrh,
nikoli pořadí položek mezi A,B,C,D. Text netvrdí převod každého algoritmu.

**V0139 — čas a paměť (p. 71–72), partial kvantifikace.** Vynechané
pack/write/read/unpack operace jsou konkrétní úspora; současně se místo
největšího jednotlivého programu mohou v paměti vyžadovat všechny čtyři
programy a jejich živé stavy. Text výslovně připouští, že menší fast
memory může celkovou rychlost obrátit. Nejde proto o doloženou obecnou
nerovnost celkových časů bez modelu cache a vazby. Psychologické a
projektové přínosy nejsou matematický slib ani měřená statistika.

**V0140 — hranice převodu (p. 72), partial přesné podmínky.** Při
zpětné vazbě B→A není možné nejprve dokončit původní A, pokud jeho další
krok závisí na ještě neprovedeném B. Stejně online stupeň nemůže vydat
položku závisející na celkovém počtu pozdějších výskytů ze samotného
aktuálního prefixu: dvě pokračování se stejným prefixem vyžadují různé
výsledky. To vysvětluje konkrétní překážky i autobusový příklad. Při
povolení neomezeného bufferu a odložení celého výstupu lze data nejdříve
uložit; obecná věta o nemožnosti jakéhokoli coroutine přepisu by tedy
potřebovala další prostorové/online předpoklady. Zde se za takovou větu
text nevydává a nevzniká potvrzený nový nález. Odkazy na plánované
kapitoly 8/10 nejsou důkazem jejich již vydaného obsahu.

# Kořenová revize §1.4.3

Technické předání bylo přečteno v celém rozsahu: obecné invarianty
simulátoru, obsluhy I/O, trasovač, vzájemné trasování a samotrasovač.
Úspěšné běhy se bez nové pochybnosti neopakovaly. Časový invariant
výslovně zahrnuje odloženou instrukci TIME; samotný CLOCK na vstupu do
CYCLE proto není vždy úplný dosavadní čas. Rozlišení fyzického času
hostitele od simulovaného času je v I/O doplňku dodrženo.

Originál s.211 skutečně omezuje cvičení 6 na jednotky 16 a 18; totéž
platí pro navazující cvičení 7. Jejich úplná MIX implementace tedy není
neúplná kvůli absenci dalších jednotek. Zadané doby 10000u a 7500u,
poloviční přenos a zvláštní čekací případ JBUS* jsou pokryté. Celý
simulátor s doplňky končí na adrese3965, při zachování původního
simulovaného prostoru0–3499. Přetečení časového čítače není řešeno jako
neomezená aritmetika; není to nově tvrzená vlastnost.

Samotrasovač má skutečný MIX kód, soukromé logické zápisy každé úrovně
a neměnnou počáteční paměť. Indukce po vykonaných instrukcích dokazuje
shodu jednotlivých úrovní s oddělenými stroji. Růst velikosti kontextu
vysvětluje konec při vyčerpání paměti. Plné běhy s kapacitou128 slov a
samostatná kontrola hranice2000 slov jsou výslovně odlišené; nepíše se,
že proběhl celý běh při maximální kapacitě. Třetí úroveň je ověřena
z dosažitelného mezistavu, nikoli vydávána za pokračování plného běhu.

Původní s.214 byla znovu prohlédnuta. Bod6(a) doslova zakazuje jen
zápisy do paměti trasovače. Příklad LDA AREG v předání je správný:
uložení vstupního A do AREG mění hodnotu pozdějšího čtení. Evidujeme jej
jako C0039, redakčního kandidáta s nejistým významem implicitní rezervace
paměti, nikoli jako potvrzenou chybu běžného použití. Ostatní omezení
včetně nezachování J při základním návratu jsou v knize výslovná.

Původní inventář má 8+7 cvičení; nové cvičení1.4.3.1-9 z1.1.2025
je vedeno samostatně. Všechny technické úlohy mají řešení a důkaz
v agentových NOTES.md a SELFTRACE.md. Doklad výkonnosti historického
neurčeného programu8422/178 nelze rekonstruovat; jeho podíl a vlastní
časové vzorce ověřeny. V historické části chybějí plné články Knuth1963
a Evans1964 a dokumentace některých prvenství. Tyto mezery zůstávají
partial, přestože technické úlohy jsou checked.

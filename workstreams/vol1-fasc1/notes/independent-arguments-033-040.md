# §1.3.2′ — argumenty p.33–40 / file41–48

Matematický generátorP je již uzavřen v doplněníV0086 (bez census prvočísel); tato poznámka ověřuje jeho konkrétní offsety, decimal output a numerické příklady jazyka. Definice assembleru se berou jako definice; netvrdí se test každé možnosti externí implementace.

**V0088 — data a global registryP (p.33,35).** L=500, PRIME1=D=2^61,ptop=D+2L=D+1000,j0=D+2−ptop=−998 modulo2^64. LOC rezervuje1000bytů pro500wydes,BUF začíná naD+1000, což už je násobek8. GREG nepřidává bajty do paměti. Šest proměnlivýchGREG získáregistry254..249, tedy n254,q253,r252,jj251,kk250,pk249;mm jealias250 a používá se až po skončení divisorského kk. Další konstantyptop,j0,base,stringpattern dostanou248,247,246,245. Proměnné a konstanty se tak nepřekrývají.

**V0089 — P1–P8 instrukce (p.33).** Při aktuálním logickém j počtu uloženýchprimes je jj=2(j−L). Před uložením nového n adresa ptop+jj=D+2j přesně odpovídáPRIME[j+1]. INCLjj,2 zvýší logickéj o1 aBZ pozná j=L právě podlejj=0. Inicializace j0 odpovídá j=1, první vložené n=3 se uloží do druhého wyde. Pro testdivisorů je kk=2(k−1−L), a k=2 tedy také j0; LDWU čtePRIME[k]. Kladné n,pk<8192 se bezpečně dělí signedDIV, rR je správný nonnegative remainder. BZr vrací naP4, BNP(CMPq,pk) naP2 odpovídá právě q≤pk a k se jinak zvýšípo1 přesINCLkk,2. V0086 zaručuje, že potřebnýpk už existuje a zůstane v tabulce. Všechny hodnoty j,k,n,offsetů jsou malé, signed overflow ani wyde truncation proto nemohou změnit tento invariant.

**V0090 — decimal konverze (p.34).** Před každým číslem seBUF nastaví na byte pattern20,30,30,30,30,00,00,00, tedyspace+čtyřiASCIIzeros+terminator. t=BUF+4 ukazuje naunits. Po d průchodech je pk=floor(N/10^d), posledních d míst obsahuje d nejnižších decimaldigitsN a t=BUF+4−d. DIV s aliasemX=Y používá starý operand aGET přečte jeho remainder0..9; INCLr,'0' vytvoříASCII48..57. Další průchod tedy invariant zachová. Protože0<N<8192, skončí za1..4průchody, nezasáhne leading space ani terminator a nevynuluje nepatřičný byte. Zbylé vyšší cifry zůstanouASCII0. Fputs pak vypíše přesněspace+a4digits. Nejde o kopírování numerických0 do textu.

**V0091 — oba výstupní cykly (p.34,37).** Před prvním řádkemmm=−2 a přičteníj0 dává−1000. Obecně řádek m začne s mm=2(m−1)−1000; po c sloupcích je adresa ptop+mm=D+2(m−1)+100c, tedyPRIME[m+50c]. Přičtení2L/10=100 po10.sloupci dá mm=2(m−1)∈0..98, takžePBN skončí; po méně než10sloupcích je mm≤−2 a pokračuje. CMP proti2(L/10−1)=98 ukončí přesně řádek50. V ostatních řádcích přičteníj0 nastaví počátek dalšího m+1. To dokazuje50×10položekbezneomezeného cyklu či přístupuPRIME501.

**V0092 — formátovacídata (p.34–35).** Title má25znaků, následujeLF+NUL; Blanks jsou tři mezery+NUL (ověřena původní sazba images/block2-pdf-042.png). Každý řádek má3úvodnímezery a deset výstupůspace+4digits, tedy53znaků aLF. JedinéNewLn lze použít zaTitle i jako samostatnýřetězec. S base na začátkuTitle jsou offsetyTitle0,NewLn25,Blanks27, všechny≤255. BUF+4 je zase ptop+4. Všechny zmiňované dvouoperandovéLDA tedy splňují assemblerové omezeníbase+byteoffset.

**V0093 — localsymbols (p.35).** Nejbližšíforward2H odřádku23 je38; backwardod31 je21; backwardod57 je44. U trojice `2H IS $10; 2H BZ 2B,2F; 2H IS 2B-4` označme adresu jediné instrukce p. Její prvníoperandbere předchozíreg10; její2F bere třetídefinici, která použije předchozílabelp aodečte4. Výsledkem jeBZ $10,p−4. Vlastní řádek se do2B/2F nepočítá, takže není samo-referenčního kruhu. Deset lokálních čísel0..9 je přesná syntaktická konvence. Historické připsáníM.E.Conwayovi1958 nebylo nezávisle ověřeno.

**V0094 — segmenty (p.36).** Userhalf má2^63adres0..2^63−1 a kernelhalf dalších2^63adres s horním bitem1, tedy záporných při signed interpretaci. Čtyři stejněvelké usersegments mají4·2^61=2^63bytů a počátky0,2^61,2·2^61,3·2^61, tedy0,2000…,4000…,6000…hex. Stacksegment končí7fff…; uvedenéintervaly se neprotínají a přesně pokrývajíuserhalf. Table+BUF programuP spotřebují1008bytů odData_Segment; nepřekračujísegment a nekolidují s textem. Závislostrychlosti na blízkosti hranice je pouze možnostkonkrétníimplementace, nikoli zde měřená matematickázáruka.

**V0095 — loader a arithmeticexpressions (p.36).** Nulová počátečnípaměť aXOR slučováníoverlapů jsou definovanéloaderem; XOR je asociativní/komutativní, takže pořadí překrývajícíchbytepříspěvků nehrajeroli. PRIME1+2L a2(L/10−1) dávají zde D+1000 a98, konzistentní s V0088/V0091. Nejde o důkaz chovánínepřečtenéhohostitelského loaderkódu.

**V0096 — benchmarky (p.37), partial.** Údaje9538dělení,10036μ+641543υ a2804μ+124559υ jsou konkrétní pozorováníhistorického běhu. Nebyly znovu reprodukovány ani odvozeny; **zůstávajíexplicitněpartial**. Žádnýbinomický důkazani kontrolainvariantů je neděláověřenými. Závěry o algoritmické správnosti nejsou na těchto číslech závislé.

**V0097 — constants aUnicode (p.37).** Decimal65=hex41=ASCIIA;decimal39=hex27=apostrophe, takže tripleapostropheconstant má logikuopenquote/character/closequote. Decimal31639=7·4096+11·256+9·16+7=hex7b97, Unicode算, již nezávisle ověřený veV0008. Pravidlo, že všechny codevalues>126 smí býtletter v symbolu, je specifická syntaktická definice, ne tvrzení oUnicodecategory. Stringexpansion je seznamjednotlivýchcharconstants, jehož délka rovná sepočtuznaků.

**V0098 — precedence příklad (p.38).** Strong<< a& jsou uvnitřtermů, weak+ dělí výraz na(#ab<<32) +(k&~(k−1)). Prok=cdef00 má nejnižšíjedničku na bitu8: spodníbyte00 a následujícíef lichý. Identita k&~(k−1) proto dá100hex (ostatní vyššíbity se v k−1 nezmění, nižšízískají1). #ab<<32=ab00000000, součet=ab00000100. Příklady$1+2=$3 a$3−$1=2 odpovídají uvedenétypovéaritmetice, nikoli sčítání obsahůregistrů.

**V0099 — fractionaldivision aexpression grammar (p.38).** Prounsigned0≤x<y je y>0 a0≤2^64x/y<2^64, tedyfloor se vždy vejde dooctabyte. Při x≥y by výsledeknebyl unsigned64, což vysvětlujedefinovanéomezení//. Equal-strength left-association přesnědává(a/b)/c a(a−b)+c. Future-reference+1 je zakázanápodoba grammar, ne neřešitelná matematickárovnice. Jednotlivé parserovévýjimky nemajítest externíhoassembleru.

**V0100 — alignment, fields aGREG/LOC (p.39).** Zarovnánína t∈{2,4,8} převádíp na t·ceil(p/t), tedyvždy nejbližšívyhovujícíadresu≥p; label se definuje ažpotom. Instructionposun4 je kompatibilní s relativnímoffsetemvjednotkách4. Bytovýimmediate má0..255,wyde0..65535 a16bitovýforward/backwardbranch mák∈[−65536,65535], což souhlasí s V0064. Dvouoperandovémemoryformy vyžadujínezměněnoubase aoffset0..255. GREG s opakovanoustejnounenulovoubase může sdíletregister; nula vyžadujeproměnlivýsamostatnýregister. TLOC@+1000 nejprve pojmenujepůvodní@ a potomposune@ o1000, takžeT je začátekvynechaných1000bytů. To ověřujekonkrétnípříklad, zbylápravidla jsou definicejazyka.

**V0101 — forwardreferences aI/O callshape (p.39–40).** Při povolenífuture pouze v relativníminstructionfieldu neboOCTA můžeassemblerzaznamenatjednofixupmísto a doplnitdřívedanouadresu, anižby musel vyhodnocovatobecný budoucí výraz. To vysvětlujemotivaciomezení, ale nedokazujeimplementačníčas celéhoassembleru. BlankEXPR odpovídá0, takžeGREGbezexpr má stejnou počátečníhodnotujakoGREG0. GETA$255,String;TRAP0,Fputs,StdOut z ProgramH splňuje I/O kontrakt: pointer se vloží do$255 a handle/functionjsou konstantnífieldy. Host-errorhandling není v tomto příkladuřešeno.

Dalšíkurzor file49/p41, primitiveI/O contracts. Novýnálezv tomto bloku žádný; knownbenchmarksnebyly plošněpočítány.


## Úplná obnova 6. listopadu 2026

Rozsah všech odstavců file41–45 doplňuje recovery-pages-041-045.md. Dřívější V0096 partial je vyřešeno úplným odvozením profilů a nálezem C0016 (10037μ/2803μ, správné υ); žádný historický běh se neopakoval. Omitted globální LABEL tvrzení vedle V0093 vyvrací C0017; místní příklady zůstávají správné. Conwayova dobová atribuce je doložena původním CASE SOAP III, přesný UNISAP údaj zůstává bibliografickou výjimkou.


## Doplnění file46–48

Celý rozsah a přesné omezení zarovnání na modular address space jsou v recovery-pages-046-048.md. V0101 one-pass motivace má úplný fixup invariant. Předchozí V0100 formulace „vždy adresa≥p“ platí jen bez překročení 2^64; na horním okraji se zarovná na0. Samostatný actual-assembler gap přes bit63 je R0006, takže file47 není uzavřena jako celek.

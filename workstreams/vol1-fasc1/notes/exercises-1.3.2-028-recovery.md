# §1.3.2′, úloha28 — úplný MMIX čtverec19×19 s výstupem

Zadání začíná file55/p47 a pokračuje celou horní částí file56/p48.
Originální file56 byla zobrazena v `images/recovery-magic-josephus-056.png`.
Kniha nedodává MMIX odpověď28. Nyní ji obsahuje `sources/magic28.mms`;
nejde o automatické převzetí dřívějšího MIX programu.

## 1. Přesně převzatý obecný důkaz a obrázek

Celé `workstreams/vol1/notes/mixal-magic-square.md` i
`mixal-magic-sources.md` byly přečteny. Matematický důkaz má přesně stejné
kladné liché n, souřadnice shora/zleva a pravidlo posunu jako MMIX zadání.
Pro n=2h+1 leží číslo k=nq+s+1,0≤q,s<n, v souřadnicích

    row=h+1+q+s mod n,  col=h−q+s mod n.                (1)

Shoda dvou souřadnic dává2(q−q′)≡0; invertibilita2 modulo liché n
vynutí q=q′ a s=s′. Proto jde o bijekci všech n² čísel a buněk.
Uvnitř bloku s<n−1 je posun dolů/vpravo; další diagonální krok po
s=n−1 by se vrátil na první buňku bloku. Posun o dva dolů ze staré
buňky místo toho dá první buňku q+1. Bijekce vyloučí všechny jiné kolize.
Po posledním čísle už není nutno hledat další volnou buňku.

V pevném řádku i sloupci probíhají q i s všechny zbytky, takže součet
je n·n(n−1)/2+n(n−1)/2+n=n(n²+1)/2. Hlavní diagonála má q=h a
vedlejší s=h; součet je znovu stejný. To zahrnuje všechny liché řády,
nikoli pouze předložených7 nebo19. Pro n=1 se počátek vyhodnotí modulo1.
Požadovaná implementace níže má výslovně pevný n=19.

Všech49 buněk originálního MMIX obrázku16 souhlasí s totožným již
uzavřeným obrázkem v převzaté poznámce:

    22 47 16 41 10 35 04
    05 23 48 17 42 11 29
    30 06 24 49 18 36 12
    13 31 07 25 43 19 37
    38 14 32 01 26 44 20
    21 39 08 33 02 27 45
    46 15 40 09 34 03 28

Zejména pozice1 je pod středem a na řádku3/sloupci6 je36. Vnější
přetisk s38 se nezaměňuje za původní knihu. Obecný argument dává
součet175 pro n7 a **3439 pro n19**. Pro hodnoty1...361 stačí tři cifry.

## 2. Úplné rozmístění, přípustný stav a inicializace

Program má N=19, Half=9. X je Data_Segment a zabírá4N²=1444 bajtů,
po řádcích N tetrabytes. Buf začíná hned za X a má4N²+1=1445 bajtů.
Všechny adresy jsou kladné user adresy hluboko pod2^63, bez wrapu,
X je čtyřbajtově zarovnané. Buf potřebuje pouze bajtové přístupy.
Kód je od#100; oblasti jsou disjunktní. Tabulka ani buffer nepotřebují
počáteční nulový obsah. GREG inicializuje dvě báze; hlavní program
explicitně nastaví všechny další hodnoty před použitím.

Lokální registry$0...$13 jsou pracovní, $255 slouží jen výstupu a Halt.
Nevolá se žádný vlastní podprogram ani nepotřebný zásobníkový rámec;
TRAP používá běžné dokumentované rozhraní. Standardní výstup musí
přijímat text, aby se požadovaný výstup fyzicky provedl. Při návratové
chybě Fputs program přejde na Halt se stavem1; při úspěchu se stavem0.
Žádný obecný předpoklad o libovolném OS handleru se nevkládá.

Clear uloží nulu do všech tetrabytes X+1440,X+1436,...,X. Po každém
SUB je off o4 menší; poslední off=−4 ukončí PBNN. Zápisy jsou přesně
celé X, nepřesáhnou do Buf. zero zůstává0 po celý běh.

## 3. Stavový důkaz celé generace

Na vstupu do Place:1≤val≤361, row/col jsou souřadnice(1) pro val,
právě čísla1...val−1 jsou ve svých různých buňkách, všechny ostatní
buňky jsou0. Počátek(row,col,val)=(10,9,1) odpovídá(1).

MUL/ADD/SLU vytvoří offset4(19row+col)≤1440; STTU zapíše právě val.
CMP/BZ odejde po361, kdy je matice celá. Jinak se val zvýší a rr/cc
dostanou row+1,col+1. Obě hodnoty jsou nejvýše19, takže CMP/CSZ stačí
k přesnému modulo19 bez dělení. LDTU načte kandidátní buňku.

Při nule PBZ přejde do Free: podle(1) jde o příští dosud nepoužitou
pozici. Při nenule zůstaly původní row/col zachované. ADD rr,row,2,
SUB t,rr,19 a CSNN rr,t,t provedou modulo19 jedním odečtením, protože
2≤row+2≤20. SET cc,col zachová starý sloupec. Převzatý důkaz kolizí
zaručí, že tato opravená buňka je právě volná příští pozice.
SET row/col a JMP zachovají celý invariant, nikoli jen počítadlo val.

Celkem je361 uložení a360 kandidátních čtení. Kolize nastanou přesně
po19,38,...,342, tedy18krát; po361 už žádné čtení následující buňky
není. Všechny produkty/indexy jsou malé nezáporné signed octabytes;
val≤361 se do STTU vejde. Snižující se počet nezapsaných buněk dokazuje
ukončení a rovnice(1) následně všechny požadované magické součty.

## 4. Celý formatter a obě návratové větve I/O

Na vstupu Format je off=4i pro i-tou buňku v řádkovém pořadí a col
je počet dosud nevypsaných polí v aktuálním řádku (počátečně19).
LDTU načte1≤val≤361. DIV100 a GET rR rozdělí val na stovky q∈[0,3]
a zbytek0...99; DIV tohoto zbytku10 dává desítky0...9 a jednotky0...9.
Přičtení ASCII'0' a tři STB tedy vytvoří přesně tři desetinné cifry,
včetně úvodních nul pro malá čísla. Dělení je vždy kladné a bez overflow.

Čtvrtý bajt je mezera, dokud SUB col nezíská0; CSZ pak vloží LF10
a obnoví col=19. Po čtyřech INCL je off znovu násobek4. CMP/PBN
prochází přesně361 buňkami. Poslední pole každého z19 řádků má newline,
tedy každý řádek76 bajtů a celý text1444 bajtů. STB zero na offset1444
přidá jediný terminátor. Všechny potřebné bajty Buf byly přepsány.

SET$255,Buf a TRAP Fputs,StdOut vydají tento nulou ukončený text.
Vytvořený obsah nemá vnitřní nulový bajt. Běžný úspěšný návrat je
nezáporný, takže BN neodbočí a Halt dostane0. Při záporném návratu BN
odbočí, nastaví1 a rovněž skončí; po I/O se už žádný výstupní bajt ani
matice nepřepisuje. Důkaz neslibuje úspěšný zápis na nefunkční výstup.

## 5. Přesný nominální profil, nezamlčené čtení a formátování

Tabulka1 účtuje MUL10υ,DIV60υ, běžné instrukce1υ, chybně predikované
větve+2υ a TRAP5υ. Cena následující je cena instrukcí hlavního programu;
práce a čekání hostitelského Fputs uvnitř OS nejsou údaj o wall-clock čase.

Clear má dvě SET a361 trojiceSTTU/SUB/PBNN s posledním+2υ; generace
má čtyři SET. Dohromady361μ+1091υ. Place má361 bloků MUL/ADD/SLU/
STTU/CMP/BZ za15υ každý a poslední BZ+2:361μ+5417υ.

Každý ze360 přechodů do další buňky má základní24υ a1 LDTU.
Kolizních18 přechodů přidá2υ za PBZ a čtyři korekční instrukce:
360μ+(24·360+6·18)υ=360μ+8748υ. Celá generace tedy

    1082μ+15256υ.

Format má tři SET a361 dvaadvacetiprvkových těl, v každém dvě DIV;
tedy140υ na buňku,5mems na buňku a poslední PBN+2υ. Terminátor,
SET$255, Fputs, úspěšný BN, SET0 a Halt přidají1mem a14υ.
Celé formátování/vydání je1806μ+50559υ. Celkem při úspěchu

    **2888μ+65815υ**.                                   (2)

Při návratové chybě Fputs je call-site profil o2υ vyšší kvůli BN;
obě větve mají stejný počet ostatních instrukcí. Rozsah programu je
pevný19; obecná složitost tohoto způsobu tvorby a fixed-width tisku je
Θ(n²) operací a Θ(n²) prostoru, bez tvrzení globálního minima.

## 6. Jediná nová malá kontrola skutečného MMIX

`verify_magic28_program.py` pod nice15 z archivního MMIXware20250620
sestavil pouze assembler a jednoduchý simulator, nikoli pipeline
meta-simulator. Pak jednou sestavil a jednou spustil nový magic28.mms.
Celý krok včetně sestavení nástrojů trval1.479s; samotná simulace0.00482s.
Starý MIX checker, jeho census ani žádný dřívější MMIX verifier neběžel.

Nezávislá očekávaná matice vznikla přímo rovnicí(1), nikoli simulací
stejného chůzového algoritmu. Kontrola porovnala KAŽDÝ z1444 výstupních
bajtů, všech361 čísel, všechny řádkové/sloupcové součty i obě diagonály.
Native profil má16678 instrukcí,2888mems a65815oops, přesně(2).
Úspěšné návraty všech tří kroků i úplné logy jsou zachované; sestavení
starého C zdroje mělo diagnostické warnings, které se neskrývají a nejsou
nálezy v této úloze. Assembly i simulace skončily bez diagnostiky.

Evidence: `results/magic28-program.json`, `magic28-build-and-run.json`,
`magic28-listing.txt`, `magic28-simulator-profile.txt`, `magic28-output.txt`.
Zdrojový SHA256 jecd723c785f5e6381c23f241a403dd1748b678d880e10e5d9e42cbcb26915e553;
výstupní SHA2561359cabf31fa2475a1378b4540654e7d6358145c490803c571e34c036f11cc5f.
Úspěšný běh neopakovat. Konečný test potvrzuje nový konkrétní program;
obecný matematický důkaz je samostatný§1 a strojový invariant§§2–4.

## 7. Historie a přesný stav

Převzatý úplný `mixal-magic-sources.md` dokládá Ibn al-Haythamův postup
v přečteném překladu a jeho shodu až na90° rotaci pro každý lichý řád,
ne pouze jeden obrázek. Přečtené biografické části dokládají Basru965
a Káhiru přibližně1040. Dobové recenze potvrzují konkrétní Ball–Coxeter
1939, kapitolu7. Neauditujeme všechny metody celé této kapitoly ani
prvenství rukopisu; tyto širší úkoly zadání netvrdí. Známé původní MIX
erratum připsání Moschopoulovi se nevydává za nový MMIX nález.

**E28 je argument_recorded v celém požadovaném rozsahu.** Požadované
MMIX tělo a tisk už nechybějí. Vzor úplného stavového důkazu vyžaduje
Clear, všechny kolize a mezní poslední buňku; nákladový vzor zahrnuje
formatter i I/O větve; vzor nezávislého potvrzení odděluje souřadnicový
certifikát od skutečně sestaveného chůzového programu.

## 8. Úplná mapa zadání na file55

Každý odstavec této stránky je přiřazen, ne jen začátky položek:

| Výrok nebo podčást | Argument / přesná zbývající mez |
|---|---|
|21 definice, celý n7 seznam, počátky/rekurence|021–023-recovery§1|
|21 počet≈3n²/π² a n<2^32|021–023-recovery§2, včetně konečné paměťové meze|
|21 celý MMIX/tetrabytes|sources/farey21.mms a021–023-recovery§3|
|22(a) determinant a(b) úplnost|021–023-recovery§1, obě samostatné části|
|23 n≥0, celý Zero, velká data|021–023-recovery§§4–5; konkrétní požadované pipeline měření stálepartial|
|24 neoverlap/NUL/osmibajtové bloky a triviální přesná cena|024-recovery§§1–5; kandidátC0019 je zvlášť na odpovědi114|
|25 všech255četností a efektivita|025-recovery celý kód/profil; neurčený autorův komparátor z odpovědi zůstávápartial|
|26 konkrétní pipeline optimalizace|026-recovery celé obě rutiny a podmíněný rozvrh; požadované měření stálepartial|
|27(a) přesná identita, floating program a první index|027-recovery§§1–3,5|
|27(b) přesná identita, high/low program a overflow mez|027-recovery§§1,4–5|
|28 definice, všechny číselné hodnoty a společný součet|zde§1 a celé pokračování§§2–7|

File55 zůstává partial kvůli přesně vypsaným23/25/26 závazkům.
Uzavření28 ani jeden úspěšný malý běh tedy neobarví celou stránku zeleně.

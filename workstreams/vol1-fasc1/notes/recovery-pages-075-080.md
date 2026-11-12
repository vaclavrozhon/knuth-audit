# Celé korutiny: file75–80/p67–72

7. listopadu2026. Každý odstavec, řádek programu01–72,
obr22 a úlohy1–4 na80 jsou přiřazeny níže. Staré
`independent-arguments-066-072.md` se přebírá jen v uvedeném
rozsahu. Všech7úloh má nyní vlastní argument; nové úplné
6/7 jsou v `exercises-1.4.2-006-007-recovery.md`. Tři první
testy nového encoderu ani starý NUL protipříklad se neopakovaly.

## File75: pokračování vazby, gramatika, celý příklad

Indukce GO a,b,0 / GO b,a,0 je úplně rozepsaná na konci
`recovery-pages-071-074.md`: každé pokračování je adresa
následující po posledním GO dané korutiny, každé předání3υ.
U obyčejného podprogramu zůstává jeho vstup pevný, zatímco
callerovy návraty se mění. To je zde definovaný rozdíl,
nikoli zákaz jiných návrhových konvencí.

Odstraníme všechny vstupní byty≤32. Zbytek má jednoznačné
parsování zleva: nondigit je samostatný token; digit n
spotřebuje ještě jeden významný znak c a vydá n+1 kopií c.
První vyprodukovaná period ukončí výstup. Proto34 znamená
čtyři4,26 tři6, nikoli vícemístné číslo3426. Digit jako
opakovaný znak se již znovu neparsuje jako nový prefix.
Token1. skončí po první period, nikoli po obou kopiích.

Celá tokenizace příkladu je
`a,2b,5e,34,26,f,g,0z,y,w,32,10,p,q,89,r,.`.
Osm nondigit tokenů před period a osm dvojznakových tokenů
vydá celkem40 znaků; konečná period je41. Rozdělení do
trojic dává přesně13 plných skupin a konečné r., tedy
vytištěné(2). Prefix0z je správný, ale nikoli nejkratší,
jak explicitně požaduje pozdější úloha7.

Popis vstupního a výstupního partnera je rozhraní proudu:
consumer žádá další položku, producer ji vydává a uchovává
svůj lokální stav. Několik možných pokračování obou stran
motivuje coroutine. Tvrzení, že nejpřirozenější aplikace
jsou I/O a nejužitečnější aplikace bývají dlouhé, jsou
zkušenostní zobecnění bez zde provedeného empirického
průzkumu. Všechen technický obsah75 je doložen, ale tyto
dvě faktografické výjimky brání úplné zelené stránce.

## File76: přesný layout a celý NextChar

Označme D=Data_Segment. Patnáct znaků stringu v TETRA
znamená15 samostatných tetrabytes00000020, ne15 slepených
bytů. Následují0000000a a00000000. OutBuf tedy zabírá
68 bajtů: znaky skupiny j patří na4j…4j+2, pro0≤j<16;
separator je32 na4j+3 pro j<15 a LF na63. Terminátor je
na64. Period je na68, zarovnané InArgs na72/80 a InBuf
na88. LOC#100 přesune adresu **dalšího kódu**, ale label
InBuf je adresa před touto LOC. Fgets velikosti1000 smí
měnit D+88…D+1087; žádná data předtím se nepřekrývají.

GREG0 pro in,out,inptr,count,outptr a nulový výstupní
konstantní registr přidělují různá čísla. Nenulové GREG
bází D,Period,OutBuf+64 a10 mají navzájem různé hodnoty.
Celkem desetGREG tedy dáváG245. Lokální$0 je k dispozici,
t=$255 je scratch. Tím se nepřenáší chybný obecný počet
GREG z C0021 na tento konkrétní seznam bez sloučení.

NextChar čte LDBU do0 a inkrementuje inptr. Pro nulový
byte přejde na14, obnovíFgets buffer, nastavíinptr na jeho
počátek; pokud t<0, CSN jej přesměruje na skutečný Period
byte. Pro nenulové bytes1…32 CMPU/BNP opakuje smyčku.
Pro33…255 POP1 vrací přesný byte do callerR; inptr je
za tímto bytem. Při platném řádku bez vloženéhoNUL jde
o první významný znak. S konečným množstvím whitespace
před dalším významným znakem helper skončí. Nekonečný
whitespace stream nemá další položku a terminace není
slibována. Po zápornémFgets vrátí syntetickou period;
nejde o důkaz zotavení či zachování nenačtených dat při error.

**C0004 je beze změny:** vložený datovýNUL je dovolený
whitespace, ale BZ jej považuje za terminátor a přeskočí
nepřečtený suffix bufferu. Celý protipříklad, sazba a errata
jsou v `MMIX-C0004.md`; původní úspěšný důkaz se nepřezkouší
pod jiným ID. Syntaktická správnost In/Out tuto chybu
NextChar nezachrání. Náprava sleduje délku odděleně od
hodnotyNUL, jak uskutečňuje nový encoder ve své jiné úloze.

**Přesná zbývající I/O závislost:** V0104/R0008 z dřívějšího
úplného I/O rozboru ponechává rozdíl mezi doslovným knižním
Fgets pravidlem pro neprázdný řádek ukončenýEOF a primární
deklarovanou C-fgets ekvivalencí. Zde není tato mezera
přejmenována na vyřešenou: pro takový poslední neúplný řádek
se bez volby kontraktu může lišit rozhodnutíCSN. Všechny
mechanické větve helperu jsou doložené, ale file76 zůstává
partial pro tento konkrétní zdrojový závazek. Pro další
kladný důkaz je explicitní předpoklad, že Fgets před první
period uspěje a použitý prefix neobsahuje datovýNUL.

## File77: každý stav In a Out

In1 zavolá NextChar pomocíPUSHJ0; POP1 vrátí znak do0.
Pro byte>'9' CMPU/PBP přejde přímo naGO27. Pro byte<'0'
je SUB count,0,'0' záporná a BN provede totéž. Obě
nondigit větve tedy vydají jeden znak a jejich pokračování
leží před novým čtením. Pro'0'…'9' je count n∈[0,9],
načte se další významný znak a prvníGO34 jej hned vydá.
Po j-tém návratu z předání je count n−j. Smyčka pokračuje
právě pro j≤n a skončí po n+1 předáních; count je nejméně−1,
takže žádná SUB nepřeteče. JMP pak čte nový token. Je-li
předaným znakem period, Out skončí a nikdy se nevrátí;
zbylé kopie period se proto správně nevydají.

Count je soukromý global In; NextChar ani Out jej nepřepisují.
Shared0 musí Out zachovat při návratu do In. Out pouze
STBU čte0, CMP zapisuje t, GO zapisuje out, pomocné address
operace zapisujíoutptr/t; Fputs mění jen deklarované t.
Tím je druhá polovina rozhraní In doložena instrukci po
instrukci. Vstupní$1 z původního Main není potřeba;
po prvnímPUSHJ0/POP1 je živý lokál jen0. Další volání
NextChar má jeden marker a jeden callee lokál, které se
při návratu opět zruší.

Na vstupu Out do43 je outptr=D+4j,0≤j<16, všechny
předchozí skupiny jsou plné a neterminující. GO43 žádá
první znak, STBU44 jej uloží a CMP/BZ zpracuje period.
Totéž dělají47–50 pro druhou a51–54 pro třetí pozici.
Po třech neperiod znacích INCL posune outptr o4. CMP
s D+64 a PBNZ vrací přesně pro j+1<16; pro16 se přejde
přesJMP59 naFputs40–41. Před Fputs jsou všechny znaky
nenulové,15 oddělovacích mezer iLF zůstaly nedotčené,
terminátor64 je0. Vytiskne se tedy přesně64 bytů:
48 znaků+15 mezer+LF. Out1 obnovíoutptr=D pro další řádek.

Žádné STBU nezasahuje do separatorů při běžném vyplňování.
Všechna digit/count rozhodnutí používají hodnoty v bezpečných
signed64 mezích; pointery se pohybují pouze D…D+64.
Výstupní I/O předpokládá úspěch: původní program jeho
chyby nekontroluje aHalt0 není důkaz úspěšného fyzického
zápisu při vadném externím streamu.

## File78: všechny tři konce, init a vztah k průchodům

Je-li period na pozici k=0,1,2 skupinyj, příslušný skok
vstoupí na63,61,60. Kaskáda INCL proběhne právě k-krát,
takže outptr ukazuje přímo na periodp=D+4j+k.
STBU63 uložíLF na p+1 aSTBU65 NUL na p+2. Konstanty
0B znamenají v prvním případě předchozíGREG10, v druhém
novýGREG0; nejsou záměnou s OutBuf+64. Největší p jeD+62,
LF pakD+63,NUL D+64. Vše je uvnitř68bytového bufferu.
Tím se odstraní i případné stale znaky z předchozího řádku.
Pokud period následuje po přesně48 neterminujících znacích,
plný řádek už byl vytištěn a poslední řádek je pouze period+LF;
to splňuje deklarovanou výjimku délky posledního řádku.

Main nastaví inptr=D+88 a in=In1, pak vstoupí do Out1.
První Out tedy nastavíoutptr před žádostí o znak. Počáteční
byte na InBuf je0 za explicitním načteným objektem; tento
předpoklad inicializace je doložen standardním MMIX loader/
MMIX-SIM memory pravidlem z `exercises-1.3.2-030-031-recovery.md`,
oddíl4: `sources/mmix-sim-20250620.w`, new_mem744–751
a mem_find770ff. Nový blok je calloc a nulový stav se
do něj nemění před prvnímLDBU. To je konkrétní loader
předpoklad, nikoli fyzická záruka každého hypotetického OS.
První nula vyvolá refill. Out nastaví svůj continuation
doout při prvnímGO, takže jeho původníGREG0 hodnota nikdy
není použita jako cíl. Každý dalšíGO respektuje společný
continuation invariant. Init je tak doložen, nejen spárován
s podobným vzorem.

SrovnáníPUSH/POP sGO pro obyčejná volání přebírá přesný
nominální rozdíl4υ versus6υ ze60–70. Pro korutiny je
jednoGO3υ a případné nezávislé lokální rámce potřebují
protokol: celý příklad bezpečného sdílení a plné oddělené
kontexty jsou již v novém důkazu úlohy6. Slovo„entangled“
tedy odkazuje na konkrétní nepárované markery, ne na
nemožnost libovolného bezpečnéhoPUSH řešení (úloha5 je dává).

Dva oddělené průchody příkladu nejprve vytvoří rozbalený
proud a poté jej formátují. Pro bezchybný vstup dává
indukce podle vydaných znaků shodný proud a shodný
formát jako dvě korutiny. Přesná výjimkaNUL se týká
původního readeru, ne abstraktní kompozice transformací.
„Pass“ je výslovně intuitivní pojem; nepřebírá se jako
formálně definovaná jednotka libovolného paměťového přístupu.

## Úplná nominální cena správné větve programu01–72

W počítá skutečně zpracované kladné whitespace bytes,
C návratyNextChar aB refilly včetně počátečního nulového
byte. Jeden whitespace stojíμ+7υ, jeden významný znak
včetněcallerPUSHJ aPOPμ+9υ, jedna nula následovaná refill
μ+13υ. To pokrývá všechny větve19–24 i14–18, včetně
vyšší ceny vzatých ordinary větví a konečnéhoPOP.

H/L jsou počty nedigitových tokenů nad'9'/pod'0', včetně
literal period vL. D je počet dokončených digitových
tokenů s neperiod znakem, A celkový počet jejich kopií.
P∈{0,1} je indikátor závěrečného digit+period. Pak
C=H+L+2D+2P a počet výstupních znaků včetněperiod je
M=H+L+A+P. Vlastní větvení/předáváníIn stojí
(5H+11L+5A+9D+9P)υ: poslední neúspěšnáPBNN je za3υ,
zatímco po předáníperiod se žádná decrement větev neprovede.

Out aMain dohromady stojí(M+2)μ+
(6M+19+k+3g+10q)υ, kde k=(M−1)mod3,
g=floor((M−1)/3) a q=floor((M−1)/48).
Každá plná neterminující skupina přidává3υ a každá
vytištěná plná řádka dalších10υ včetně poslední chyby
predikce,JMP,obouLDA aFputs. Period má ordinary taken
branch za3υ a k kaskádovýchINCL; závěr obsahuje oběSTBU,
LDA,Fputs iHalt. Žádná další skrytá cena3υ zaGo není
vynechána: směryIn→Out aOut→In jsou počítány zvlášť.

Součet těchto tří výrazů je úplná cena pro přesně uvedenou
správnouI/O/NUL-free větev. Pro kompaktní(1) sFgets newline
je W0,C25,B1,H8,L1,D8,A32,P0,M41,k1,g13,q0,
tedy69μ+826υ. Jde o odvození z instrukcí, nikoli o nový
native běh tohoto starého programu. Hostitelské fyzickéI/O
náklady nejsou v tabulkovém modelu skrytě považovány za0.

## File79: celý obr22, všechny tři srovnávací body

Originál `images/recovery-coroutines-079.png` byl přímo
zobrazen. Vlevo jsou čtyři dvojicevstup→pass→výstup,
se stejnýmiFile1/2/3 mezi sousedními kroky; vpravo je
jediná cestaInput→A→B→C→D→Output. Šipky značí pořadí
dat, nikoli úplný směr každého požadavku/řízení.

Pro každý deterministický stupeň s lokálním stavem a
pořadovým čtením prefixu může write předat příští položku
consumeru, read si ji vyžádá od produceru. Indukce podle
počtu položek na každé hraně dává tentýž stav po témže
prefixu a tentýž další výstup. Konečnost jednotlivých
kroků a řádná signalizace konce proudu jsou předpoklady.
Nejvýše jeden právě předávaný prvek může být na hraně;
lokální pracovní paměť každého stupně tím není omezena
na konstantu. Tato konstrukce dokazuje právě popsaný
převod, nikoli libovolný další algoritmus mimo tyto podmínky.

Označení PassA|PassB|PassC|PassD odpovídá primárnímu
lokálnímu Bash manuálu, oddílPipelines: stdout předchozího
příkazu je spojen se stdin následujícího. Úplný tento oddíl
byl přečten a uložen s otiskem; předchozí pokus otevřít
oficiálníGNU web timeoutoval. OS pipe může mít buffer a
samostatné procesy, takže jde o analogii datového spojení,
ne o tvrzení, že shell používáMMIXGO ani stejný scheduling.
Termínfilter označuje takto čtoucí/zapisující prostřední
transformaci. Obrácený převod na soubory funguje při
stejném odděleném feed-forward kontraktu, proto text říká
„often“, nikoli vždy.

(a) Oddělené kontrakty umožňují napsat a posoudit jednotlivé
části zvlášť a rozdělit implementaci mezi pracovníky. To je
konkrétní organizační možnost. Tvrzení o obecné snadnosti
porozumění je zkušenostní, nikoli prokázaná psychologická
statistika; zůstává výslovná faktografická výjimka.

(b) Neprovedené pack/write/read/unpack jsou skutečně
odstraněné operace. Označme jejich cenuS a dodatečnou
vazbu, scheduling či práciH. Při stejných ostatních
instrukcích a paměťových nákladech je rozdílS−H; zrychlení
vyžadujeS>H. Věta„a one-pass algorithm will be faster“
nemá zde vymezenýI/O/batching/linkage model, který tuto
nerovnost zaručí. **V0139 proto zůstávápartial právě pro
toto obecné srovnání**, ne pro nevytvořený hardware.

(c) Velikosti kódu/stavů s_i potřebují při residentní
jednoprůchodové realizaci součetΣs_i místo postupného
maxs_i; sdílený kód/data a další buffery se musí skutečně
započíst zvlášť. Převýšení kapacity rychlé paměti může
přidat cenuK, takže rozdíl jeS−H−K. To dokazuje možnost
obrácení rychlosti a vysvětluje návaznost80; není určena
univerzální hodnotaK ani kvantifikované„considerably“.

## File80: každý další odstavec a úlohy1–4

Při etapách, které jednotlivě zaplní fast memory, ale
současně se nevejdou, může větší počet pomalých přístupů
či swapping převážitI/O úsporu právě kdyžK>S−H.
Historická rozšířenost konkrétních paměťových konfigurací
není nově změřena. Sloučení jen několika sousedních etap
do jedné residentní skupiny a záměna krajníchwrite/read
za souborové operace zachová předchozí indukční stream
kontrakt. Proto lze pod stejnými předpoklady volit počet
skupin/průchodů podle skutečné paměťové kapacity.

Zpětná vazba: jestliže další akceA potřebuje výsledekB,
nelze **tentýž rozvrh a nezměněná těla** provést jako
celéA a teprve pakB. Dvě různé možné odpovědiB po stejném
prefixuA dávají různá pokračování;A nemá bezB potřebnou
informaci. Příklad šachových tahů to splňuje. Je to důkaz
konkrétní kauzální překážky, ne nemožnost všech teoretických
přepisů s předpočítáním či kopírováním stavů.

Podobně požadovaný online výstup obsahující celkový počet
určitého slova nemůže být určen z prefixu, pokud má být
vydán dříve než dočtení proudu: dva vstupy se stejným
prefixem a různým pozdějším počtem vyžadují různý výstup.
Bez omezení odkladu a pracovního uložení lze ovšem celý
vstup nejprve uložit a spočítat; takové korutiny definice
nevylučuje. **V0140 zůstávápartial přesně pro formulaci
„some multipass algorithms cannot be converted to coroutines“
bez těchto resource/online podmínek.** Neuzavírá ji malý
příklad ani nepřidáváme confirmed nález z nejasného významu
intuitivně definovaného„pass“.

Autobusový příklad má stejný informační problém: nelze
poznat nynější zastávku jako dvě před budoucím vystoupením
chlapce jen tím, že sledujeme dosud neuskutečněné vystoupení.
Při předchozí znalosti trasy/výstupu by potřebná informace
existovala. Vtip tedy ilustrativně odpovídá dvěma průchodům.
Označení masterem řízených coroutine jako threads je
terminologická konvence v tomto textu; netvrdí se ekvivalence
se všemi OS preemptive thread implementacemi. Odkazy2.2.5
a plánovaných kapitol8/10 neurčují nynější stav vydání
ani nenahrazují audit odkazovaných algoritmů.

Úloha1 má úplný argument v `recovery-pages-071-074.md`
včetně odpovědi na123/124. Úloha2: při obráceném init
první InGO dorazí naOut1, které nastavíoutptr a hned
žádá další znak, než vykoná prvníSTBU. První předaná
hodnota tedy nebyla zapsána. Vstup a.+LF proto dává
jenperiod+LF. Je-li první hodnotou period, program navíc
může pokračovat za původním terminátorem; odpověď„first
character…lost“ je mechanismus, nikoli slib stejného
obecného fallback výstupu pro každý další vstup.

Úloha3 je přesný layoutTETRA na76 výše, včetně všech
15 mezer a rozlišeníjednoho stringového znaku/čtyřbytového
prvku. Není vynechána implicitní nulová trojice.

Úloha4: přiA→wrapperB GOa,B uloží continuationA doa.
B pomocíGET rR_A,rR uložíA remainder, PUT rR,rR_B
obnovíB remainder aGOt,b,0 skočí doB. WrapperA provede
přesně opačné operace. Indukcí má každý člen při pokračování
své poslednírR. První neaktivní continuation a počáteční
soukromérR musejí být nastaveny; nováGREG0 dává jednu
konkrétní počáteční volbu0. Cena je3+1+1+3=8υ,
t je deklarovanýscratch, ostatní specials nejsou tímto
rozhraním prohlášeny za soukromé. Žádné dělení se nevyvolá
samotnýmGET/PUT, takže protokol nepřidává aritmetickou výjimku.

## Úloha5, odpověď124: úplnéPUSH/POP předání

PUSHJ255,B vytvoří marker původníhoL a prázdné lokály,
rJ=continuationA. GETa,rJ zachová toto pokračování;
PUT rJ,b nastavíB pokračování. POP0 zruší **právě tento**
pomocný rámec, obnoví původní logickou register view
a skočí doB. WrapperA je symetrický. a,b jsou odlišné
globals s vhodně inicializovaným prvním cílem. Cena
1+1+1+3=6υ je dvakrát jednoGO, bez změny velikosti
původního živého stacku. Neobnovuje nějakou druhou
soupravu soukromých B lokálů; zde je sdílená sada a
nezávislé stacky již řeší úplná úloha6. To pokrývá
výslovnou poslední větu odpovědi5 i všechny její instrukce.

## Stav celých stran

75: úplná gramatika/příklad/GO argument, přesně uvedené
empirické výjimky.76: všechny instrukce, layout aC0004
doložené, konkrétní zdrojová EOF závislostR0008 zůstává.
77/78: celý kód obou korutin, každý konec ainit má argument
pod výslovným reader/I/O kontraktem; nesprávnost obecného
readeru je oddělenýC0004, nikoli vydávaná za správný program.
79: celý obrázek a podmíněná kompozice, přesný chybějící
obecný časový modelV0139.80: všechny metody/hranice/úlohy,
ale nevysvětlený obecný streaming rozsahV0140 a navazující
nákladové zkušenostní tvrzení zůstávajípartial.

Vzory: všechny stavy a meze jako binomický rozbor, každý
směr předávání a deklarovaný počet instrukcí jakoAlgorithmR,
oddělení korektní podmíněné konstrukce od neuzavřené
silnější věty jako kografové rozbory. Žádný nový nález
ani native běh původního programu v tomto bloku.

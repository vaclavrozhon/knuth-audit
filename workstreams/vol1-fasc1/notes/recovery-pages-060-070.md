# Celý výklad podprogramů: file60–70 / p52–62

7. listopadu 2026. Každý odstavec, varianta kódu(1)–(18), rovnice
a deklarace v tomto rozsahu byly znovu přiřazeny ke konkrétnímu
argumentu. Starý `independent-arguments-052-065.md` je převzat pouze
v přesně popsaných případech. Níže jsou doplněny vstupní meze,
všechny větve, úplné nominální náklady a dříve chybějící BSPEC.
Nebyly spuštěny žádné programy ani zopakovány SAVE/UNSAVE/PutL důkazy.

## File60: význam podprogramu a celý Max100, V0108

Definice podprogramu, vazby, jednoho deklarovaného vstupu a výstupu
jsou terminologie. Vynechání opakovaných kopií je doloženo přesným
počtem kódu níže. Tvrzení o dodatečném čase se týká stejného těla
a konkrétní vazby; následující strany výslovně připouštějí změnu
cache chování i přizpůsobení těla. Není to věta, že libovolný
refaktoring nikdy nezrychlí program. Strukturní přehlednost, snazší
ladění a užitečnost sdílených/specializovaných rutin jsou důvody
návrhového doporučení, bez matematické garance výsledku.

Historický údaj, že **většina počítačových instalací** již vybudovala
velkou knihovnu užitečných rutin, není v auditu podložen statistikou
pro dobu vzniku textu. Je výslovně přeskočen; sám nepřidává chybu.
Proto celá60 není vykázána jako úplně faktograficky ověřená.

Max100 potřebuje čitelných100 osmibajtových prvků, globální x0
s adresou X[0] a t=$255; názvy jsou různé. Kód nemění pole ani
x0. Hodnoty X[k] jsou libovolná signed64 čísla, včetně obou konců
rozsahu. Použití CMP namísto odečítání zajišťuje správnost i při
takových mezních hodnotách.

Po SETL/LDO/JMP/SR má kk800,m=X[100],j100. Na vstupu do každého
SUB platí kk=8k, m=max X[k…100] a j je největší index v tomto
suffixu s hodnotou m. Po SUB je buď kk0 a rutina vrací, nebo
kk=8(k−1)>0. LDO a CMP načtou následující prvek. PBNP při≤
přeskočí obě změny; při> se nastaví m i j. Všechny tři výsledky
CMP jsou tím pokryty a při rovnosti zůstane větší index. Sto
snížení ukončí smyčku. Žádné byteové adresy mimo X[1…100] se nečtou.

Při PUSHJ $1 se starý caller $0 zachová, $1 je výsledková díra,
callee si vytvoří potřebné lokály0…3. POP2 vloží callee m=$1
do caller $1 a callee j=$0 do caller $2. rJ se uvnitř listové
rutiny nemění; POP2,0 se proto vrátí bez dalšího ukládání adresy.
Tím je doložena i úvodní vazba pokračující na61.

Pro obecné n a a striktních nových maxim mezi n−1 porovnáními má
stejné jedenáctiinstrukční tělo s inicializací kk=8n a závěrečným
POP/GO celkem

**nμ+(5n+6+4a)υ**.

Inicializace včetně prvního SR dává4υ+μ, porovnání3(n−1)υ+(n−1)μ,
striktní zlepšení dodávají4aυ, n dvojic SUB/PBP má2n+2υ a návrat3υ.
Pro100 tedy100μ+(506+4a)υ, před volající instrukcí. Žádný vstupní
rozdíl či chybná konečná predikce nebyly z ceny vynechány.

## File61: GO a rovnice(3), V0109–V0110

V(2) jsou j,m,kk,xk rozdílné globální registry, odlišné od x0
a t. GO $0,GoMax100 zapíše následující adresu do$0. Tělo do$0
nezapisuje, protože pracovní j je nyní globální. Koncové GO
kk,$0,0 používá tento původní operand jako cíl a zapíše vlastní
link pouze do již nepotřebného kk. m/j zůstanou globální výsledky.
GREG @ bezprostředně před vstupem poskytuje přesnou globální bázi
pro jedno GO; není potřebný žádný offset větší než8 bitů.
Bez dostupné vhodné báze funguje GETA následované GO a GO si
přečte starou hodnotu zdroje i při shodě cíle/zdroje$0.
Výrok o běžném používání tohoto stylu na jiných počítačích je
historické zobecnění, které nebylo statisticky ověřeno;61 zůstává
reconciled_with_exclusions, nikoli úplně zelená.

Při k tetrabytech stejného těla na m místech je mk nahrazeno
mc+k+r, kde c je délka každého volání a r pevná režie návratu
uvnitř společné rutiny. Pro c=r=1 je rozdíl
mk−m−k−1=(m−1)(k−1)−2. Při k1 nebo m1 je záporný;
při k2 je m−3, kladný právě pro m>3. Jde o délku instrukčního
kódu, nikoli objektového souboru se symboly a inicializací GREG.

## File62: vazba a obě předání n, V0111–V0113

Tabulková aproximace dává PUSHJ1υ, POP3υ, GO3υ. T uskutečněných
volání proto přidává4Tυ nebo6Tυ ke stejnému tělu. Skutečný
register spilling, příprava argumentů, cache a odlišně
specializované kopie nejsou v této aproximaci; kniha je sama
výslovně odděluje. Následující pojmy parameter/argument/calling
sequence jsou definice, ne další měřené tvrzení.

V(4) GO zapíše do$0 adresu následujícího datového TETRA n.
LDT je **signed**, takže přípustný celočíselný rozsah tohoto
konkrétního zápisu je1≤n≤2^31−1. Násobení8 má pak bezpečný
signed64 výsledek. Tělo nahradí100 obecným n a přesně zachovává
suffixový invariant výše. Koncové GO kk,$0,4 přeskočí právě čtyři
datové bajty; TETRA se nikdy neprovede jako instrukce.

V(6)–(7) se n připraví v$1. Samotné SET je jednoinstrukční,
jestliže n označuje registr s hodnotou nebo přímo kódovatelnou
konstantu; inicializace širší konstanty má svou další calling
režii. Obecný bezpečný obor tohoto těla je1≤n<2^60, čitelný
osmibajtový vektor a vhodná odlišná globální x0. Pak0<8n<2^63,
každý kk je kladný až do posledního SUB a signed SR vrátí správné j.
Tyto strojové reprezentace a platnost pole jsou implicitní
předpoklady matematického rozhraní n≥1 na63; nepřenášíme je na
arbitrární64bitovou značku n nebo vadnou paměť.

Pro stejný vstup v obou rozsazích stojí(4)–(5) včetně GO
(n+1)μ+(5n+10+4a)υ; (6)–(7) včetně SET/GO stojí
nμ+(5n+10+4a)υ. Úspora je přesně jedenμ: odstraněné LDT mělo
μ+υ, ale SET volajícího přidaloυ. Dynamická změna argumentového
registru nevyžaduje změnu instrukčních bajtů. Vrací se hned za GO,
protože v druhé variantě žádné vložené datum není.

## File63: obecná úspora a kompletní uchování kk/xk, V0114–V0115

Změna x0 je přípravou dalšího argumentu, jak požaduje indexový
invariant. Pro pevné c,r platí
mk−(mc+k+r)=(m−1)(k−c)−(c+r), takže constant v(8) je c+r,
nezávislé na m. Změní-li se kvůli obecnosti samo tělo k, musí se
použít skutečné délky; text netvrdí opak.

Varianta(9) má kk=$2,xk=$3, jiné globální j,m,x0 a t. Tempkk
a Tempxk jsou dvě různé platně adresovatelné osmibajtové buňky,
mimo pole a kód; žádný současně aktivní rámec je nepoužívá.
Oba STO uloží původní hodnoty dřív, než SL/LDO začnou práci.
Tělo nikam jinam nezapisuje. Dvě LDO před návratem obnoví přesně
oba původní64bitové vzory. Návrat musí použít GO $0,$0,0,
protože zápis linku do kk by právě obnovenou hodnotu zničil.
Režie proti(7) je4μ+4υ. Argument$1 zůstane, výsledky jsou j/m;
$0 a konvenčně dočasné t se mění. U původně marginal $2/$3
se jejich nulové hodnoty obnoví, nikoli původní rL: text slibuje
uchování **obsahů registrů**, ne všechno metadatové pozorování stavu.

Specifikace(10) a její pokračování na64 správně uvádějí maximum
a jeho index. Naše dokazované rozhraní navíc výslovně uvádí
strojový obor n, platnou paměť, j největší při shodě a clobbery.
Vynechání t je deklarovaná konvence pro$255, nikoli tvrzení,
že se t fyzicky nezmění. Doporučení specifikovat rozhraní je
normativní a nevytváří další neověřenou statistiku.

## File64: všechny vstupy a výstupy, V0116–V0117

GoMax100 nastaví$1=100 a propadne do stejného GoMax; oddělený
GoMax50 nastaví50 a JMP rovněž přejde na týž vstup. Požadované
hodnoty se vejdou do SET immediate. Obě varianty splní vstupní
invariant. V předchozí variantě(9) se kk/xk ukládají až uvnitř
společného vstupu, takže ani přidaný vstup jejich hodnoty nezničí.

V(12) je b další odlišný globální signed64 argument. Jestliže
m≤0, BNP jde na první GO. Jinak m>0 a CMP kk,m,b bez odečítacího
overflow rozdělí všechny případy na m<b a m≥b. První vede na
GO kk,$0,4 a druhý na GO kk,$0,0. Platí to pro b≤0 i pro oba
signed64 krajní b; druhý výstup je prázdný, když není0<m<b možné.
Jádro až po maximum je již doložené. Dodatečný test stojí3υ
v první výstupní větvi a5υ ve druhé, nad jeden původní návrat GO.
První tvrzení zahrnuje jak m≤0, tak m>0,m≥b. Entry GoMax100
přidává jednuυ proti přímému GoMax. Zápis do pracovního kk
nepřepisuje žádný potřebný výsledek m/j.

## File65: vnoření a paměťový zásobník, V0118–V0119

Dvě adresy návratu jsou další argumenty; při pevném rozložení
dvou instrukcí za call stačí sdílený link plusoffset0/4. Doporučení
držet často používaný argument v registru a vzácný pevný argument
v proudu jsou místní úspory známých load/SET, nikoli globální
optimizační věta pro všechny cache a všechny počítače.

Ve schématu(13) má první GO $0,A v$0 adresu v Main. Volání
A→B používá$1, B→C používá$2; pokud C znovu provede GO $0,A,
původní main link se nahradí novým C linkem. Žádná instrukce
schématu starou hodnotu neuložila. Návrat GO $0,$0,0 ji tudíž
nemůže obnovit. Zákaz rekurze platí pro **tento pevný linkovací
protokol s neuloženými dočasnými místy**, nikoli pro GO obecně.
Historická frekvence více než pěti úrovní v komplikovaných
programech nebyla samostatně statisticky ověřena;65 zůstává
reconciled_with_exclusions.

Pro(14) nechť vstupní sp=S je zarovnaný, globální a odlišný od$0;
odS nahoru je dostatečný volný zásobníkový prostor mimo ostatní
živá data, bez wraparound a bez signed pointer overflow.
STO uloží vlastní link R do M[S], ADD nastaví sp=S+8. Před a po
každém řádně ukončeném vnořeném volání zůstane sp=S+8; vnořený
callee používá vyšší místa. SUB/LDO pak načtou právě R zM[S],
GO vrátí řízení kR. Indukce podle hloubky a pořadí návratů
zahrnuje přímou i nepřímou rekurzi. Není to důkaz pro přetečený
stack nebo tělo úmyslně přepisující cizí rámec.

List může STO/ADD/SUB/LDO vynechat, pokud sám zachovává link$0;
neexistuje vnořený GO, který by jej povinně zničil. Paměťový
protokol stojí2μ+7υ bez volajícího GO,2μ+10υ s ním; listová
vazba6υ. Tak je doložena i přesná místní úspora.

## File66: všechny22 rámcové položky a třídy registrů, V0120–V0121

Při vstupních sp=S,fp=F,link=R ukládá(15) F naM[S], nastaví
fp=S,sp=S+176 a uloží R naM[S+8]. Lokální k∈1…20 má adresu
S+8k+8, tedy S+16…S+168. Tato místa jsou přesně20 dalších
octabytů, nezasahují do linku, starého fp ani příštího rámce.
Platí stejné paměťové a aliasové předpoklady jako(14), fp je
další odlišný global. Libovolně vnořený stejný protokol po návratu
obnoví naše fp/sp. Epilog nejprve čte vlastní R přes současné fp,
pak obnoví sp=S a nakonec fp=F zM[S]. Výsledek má oba ukazatele
jako před call a vrací se kR. Prolog/epilog stojí4μ+10υ,
s volajícím GO4μ+13υ. Dvacet lokálních míst je rezervováno,
**není automaticky inicializováno**; tělo je před čtením musí naplnit.

Register-stack model rozděluje všech256 jmen na [0,L),[L,G),
[G,256), kde0≤L≤G≤255 aG≥32. Jen první interval odpovídá
horním L položkám S; globals nejsou jeho částí. Počáteční L=τ=2
se vztahuje k běžnému zavedení hlavního programu a jeho argc/argv,
již doloženému v recovery-pages-037-040.md, nikoli k libovolnému
stavu po přerušení nebo SAVE.

Zdroj v marginal intervalu čte0. Zápis do k v tomto intervalu
zvětší L nak+1≤G a mezilehlé pozice nastaví0. V příkladu L8,
k10 se tedy vytvoří$8,$9,$10; G≥32 zajišťuje, že zdroj$20
zůstává marginal. ADD proto dává$10=0+5,$8=$9=0,L11. Žádný
neurčený starý obsah fyzického registru neovlivní výsledek.

## File67: každý PUSH/POP případ a všechny číselné příklady, V0122–V0123

Použijeme logický index o první current-local položky a celkový
vrchol o+L; tím se vyhneme odlišné konvenci symboluτ v různých
primárních textech. `mmix-doc-20131017.w`1663–1789 dává tři případy:

* X<L: místo o+X se stane markerem X, nový základ je o+X+1 a
  nové L je L−X−1. Staré lokály X+1…L−1 mají nová čísla0…L−X−2.
* L≤X<G: nejprve se nulově přidělí lokály až doX a nastane
  předchozí případ sL=X+1. Nový rámec máL0.
* X≥G: za všechny L lokály se přidá marker L; nový základ je
  o+L+1, nový rámecL0. Globals se nemění.

V první větvi tedy zůstávají všechny **zachovávané hodnoty** na
svých místech; rezervovaná výsledková díra obsahuje marker,
nikoli její dřívější uživatelskou hodnotu. To zpřesňuje textové
„stack remains unchanged“. Nedostupnost pushed částí znamená
nedostupnost pod current-local čísly, ne bezpečnost před svévolným
zápisem do cizí zásobníkové paměti nebo před změnou rG.

Při POP s původním callee L, markerem p a návratovým počtem X
je k=min(X,L+1), nový základ o−p−1 a nové L=min(G,p+k).
Je-li0<X≤L, hlavní výsledek je staré$(X−1); jinak0. Vloží se
do díry pouze tehdy, když je p<novéL. Pomocné výsledky jsou
původní callee$0…$(k−2), na nezměněných zásobníkových adresách.
ProX0 se díra i celý callee rámec zahodí. ProX>L zůstanou
všechny L callee hodnoty pomocnými výsledky a díra dostane0;
případné přebývající horní položky se oříznou naG.

Za pevnéhoG a p5 jsou tři předané argumenty ve starých caller
$6,$7,$8, v callee$0,$1,$2. X0 dáváL5; X1 vrací hlavní do$5,
L6; X2 dává hlavní zcallee$1 do$5, pomocný zcallee$0 do$6,L7.
X10 dává hlavní$9 do$5 a dalších devět do$6…$14,L15. G≥32
zde žádný výsledek neořízne. PřiX4 a ponechaných prvních třech
callee lokálech se přesně obnoví arg0/1/2 v$6/$7/$8, jak pokračuje68.
Fyzické ring/load/store případy těchto přechodů jsou již uzavřeny
v exercises-1.4.3-001-014.md, úloha10; zde se nepřepočítávají.

## File68: rJ, lokální Max a velikost/čas obou variant, V0124

PUSHJ na adrese P nastaví rJ=P+4. POP X,YZ jde na rJ+4YZ,
tedy naP+4(YZ+1), a proto dvě odpovědi0/1 přesně znamenají
dvě sousední instrukce za call. To vyžaduje správně zachované rJ;
nevrací se libovolně změněný special register automaticky.

V(16) se n zcaller$(R+1) stane callee$0. SL musí proběhnout
dřív, než je$0 přepsáno indexem j; tisk to splňuje. Celý Max
invariant i tři signed porovnávací větve jsou shodné s(12).
POP2 vrátí m do$R a j do$(R+1); právě první dvě callee lokály
jsou dva výsledky. „Local argument register“ zde výslovně
znamenáR+1<G, tedyR≤G−2. Pro další argumenty/pomocné výsledky
musí být míst podobně dost; tvrzení o libovolném lokálním R
se nepřenáší přes hranici, za níž by A již nebylo lokální.

Obě varianty(12)/(16) mají16 instrukcí včetně Max100 vstupu
a obou návratů, tedy64 bajtů instrukčního kódu. Čtyři pracovní
GREG a globální báze GO už v(16) nejsou potřeba. GO3υ je o2υ
dražší než PUSHJ1υ, oba návraty mají tabulkově3υ; nejde o
univerzální měření reálného procesoru. Možnost rychlejšího POP
je implementační námět, nikoli slib pro každé zařízení.

## File69: nelineární rámce a přesné převzetí spill/SAVE, V0125–V0126

GET retadd,rJ před prvním dalším call uloží vlastní link.
Každé vnořené PUSH musí mít výsledkovou díru R>retadd, takže
retadd patří mezi skutečně chráněné lokály. PUT před závěrečným
POP obnoví správné rJ. Je-li retadd≥počet výsledků X, tento
pracovní registr při návratu nepatří mezi výsledky. Formule
nechrání speciální registry bez příslušného GET/PUT protokolu.
Režie GET/PUT/POP a caller PUSHJ je6υ v tabulkovém modelu,
proti2μ+10υ ve schématu(14), pokud nevznikne další spilling.

Pole vyžadující adresový výpočet nemůže používat přímé číslo
registru jako adresovatelnou paměť: běžné register operandy mají
pevná čísla v instrukci. Pro taková pole se použije disjunktní
paměťový rámec(15), scalars se ponechají ve správně chráněných
lokálech. Dva invarianty se skládají, protože paměťový fp/sp
a register-stack origin nejsou jedna datová struktura.

V0126 už bylo po původní poznámce uzavřeno. Přesně se přebírá
ring invariant v independent-arguments-073-082.md,V0149–V0153,
logické/fyzické POP v exercises-1.4.3-001-014.md,úloha10,
a celý valid-image inverse SAVE/UNSAVE vúlohách11–12 s již
potvrzenou opravou C0007. Zachovává se jejich obor:ρ≥256,
platný push marker a image vytvořený SAVE; ne libovolná vadná
UNSAVE paměť. Dno se při potřebě místa ukládá, POP je zpět
načítá a SAVE zapisuje celý vymezený kontext; počátek běžného
stack segmentu je#6000000000000000. Není důvod znovu otevírat
pouhou architekturní definici kvůli hypotetickému jinému hardwaru.

Pokud se právě používaný úsek vejde do fyzického ringu, změna
o/L a markeru skutečně nepotřebuje přenosy celé řady registrů.
Empirická frekvence „in most cases“ pro neurčené pracovní zátěže
se však nepovažuje za změřenou;69 je reconciled_with_exclusions.
Odkazy na další kapitoly jsou mapa plánované knihy, nikoli důkaz
jejího budoucího dokončení. Konec stránky zavádí PREFIX níže.

## File69–70: celý PREFIX/LOCAL/BSPEC, V0127–V0129

Primární MMIXAL183–199 definuje plně kvalifikované jméno úvodní
dvojtečkou. Neplnému jménu se **jednou** připojí aktuální prefix;
PREFIX sám dostává takto kvalifikované jméno. Ze startu`:`
plyne řetězec`:`,`:Foo:`,`:Foo:Bar:`,`:`. Čtyři ADD v knize
proto mají přesně vytištěná jména včetně vnějších`:x` a`:z`.
V(18) je vnitřní x0 alias na`:x0`, podobně b/t; j/m/kk/xk
patří do`:Max:`, veřejné`:Max` a`:Max100` zůstávají v kořeni.
Reset PREFIX: uvolní běžná lokální symbolická jména pro další
blok. Číselné lokální1F atd. se nepletou s těmito slovními
jmény. Toto je lexikální přepis, ne runtime zásobníková operace.

LOCAL$40 znamená požadavekG>40 při konci sestavení, nikoli
okamžitou alokaci všech registrů do40. Dokumentace629–640 a
kód3111/3253 drží lreg=max deklarací a odmítnou lreg≥greg.
Architekturní minimumG32 zajišťuje implicitní požadavekLOCAL$31.
Tím je přesně ověřen vytištěný assemblerový kontrakt, ne mylné
tvrzení, že$0…$31 jsou za všech rL okamžitě lokální.

Dřívější V0129partial bylo způsobeno chybějícím primárním
dokumentem. Ten je nyní přímo přečten v uloženém
`sources/mmixal-20250620.w`646–669,877–881,1400–1425,3117–3123:

* BSPEC přijímá typ0…65535, zapsaný doYZ záznamu lop_spec;
  nastaví special mode. ESPEC jej ukončí a vyprázdní buffer.
* Datové pseudooperace zapisují své bajty big endian do výstupu.
  Ve special mode se posouvá spec_mode_loc, nikoli adresa
  načítaného programu cur_loc. Běžné instrukce režim odmítá.
* Formát zahrnuje všechny následující tetrabyty do další loader
  operace mimo lop_quote; quote dovoluje i datový escape byte.
* Reference k calling conventions nebo řádkům zdroje jsou
  příklady významu type, nikoli povinný formát konkrétního
  debuggeru. Primární MMIX-SIM1030–1040 taková data přesně
  přeskočí místo jejich uložení do programové paměti.

Knižní věta slibuje **přenos informací k nástrojům**, ne hotový
interpret každého možného type. Tím je její celá skutečná
povinnost uzavřena; důkaz libovolného cizího debuggeru by byl
nový úkol navíc. V0129 přechází naargument_recorded.

Závěrečné strategic considerations jsou doporučení. Faktická
mez je224 globálních jmen přiG32, přičemž$255 má zavedenou
dočasnou roli; počet pevně rezervovaných globals je konečný.
Proto stovky nezávisle načítaných rutin nemohou každá spotřebovat
velký disjunktní globální blok. Naproti tomu lokální rámce lze
opakovaně využívat s uvedenými volacími invarianty. Text neslibuje
globální optimum ani zaručený čas pro každou knihovnu.

## Výsledný rozsah a použití vzorů

Všech11 stránek je plně zmapováno.62,63,64,66,67,68,70 mají
úplné argumentové pokrytí.60,61,65,69 zachovávají výslovné
historické či empirické výjimky, bez nové matematické mezery.
Úlohy na73–74 a odpovědi121–123 tím ještě nejsou nově uzavřeny.

Binomický vzor vedl k přesnému rozlišení signed32 vloženého
argumentu a signed64 byteových mezí; SAT vzor k celým nákladům
včetně chybných predikcí a skutečného rozdíluμ mezi dvěma
předáními; kografový vzor k uzavření všech disjunktních PUSH/POP
případů a k oddělení formálního kontraktu od neprokázaných
empirických slov „většina“. Nové nálezy žádné, nové běhy žádné.

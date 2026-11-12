# Obnova §3.6: závěr188–189 a celé1–4,6–7

Originály188–193 a599 přečteny, program RANDI vizuálně po všech
instrukcích. Celé `summary-applications.md`, `truncated-lcg.md` a
`verify_summary_applications.py` přečteny. Přebírá se existující
výsledek `summary-applications.json` a všech deset uložených her;
žádný matematický test ani simulace nebyly spuštěny. Nově zobrazeny
uložené originály Lovelace722, titul1843 a Turing450; celý uchovaný
výňatek449–451 přečten. Úloha5 má samostatný následující blok.

## Závěrečný text a přesný rozsah zdrojů

Vada RANDU má krátký nezávislý důkaz. Pro a=65539=2^16+3 a m=2^31
je a²−6a+9=2^32≡0modm. Tedy X_(n+2)−6X_(n+1)+9X_n≡0modm.
Normalizované trojice leží na rovinách9u−6v+w=j, kde −6<j<10,
a tak nejvýše na15 rovinách. To je konkrétní důvod kritiky tohoto
generátoru. Údaj o převaze RANDU na světových počítačích na konci60.let
je historická zpráva, nikoli výsledek tohoto algebraického důkazu;
bez dobového soupisu instalací **partial**.

Ferrenberg–Landau–Wong1992: uložený záznam obsahuje vydavatelská
metadata/rozsah abstraktu, plný článek nebyl získán. Konkrétní
přechod ze3D na2D, páté desetinné místo a úspěch16807 nejsou v tomto
bloku nezávisle potvrzeny: **skip bibliography** v těchto přesných
historických detailech. Celý fyzikální experiment se neprovádí.
Doporučení porovnávat dvě různé rodiny generátorů může odhalit
neshody, ale sama shoda dvou simulací nedokazuje správnost obou;
text zde dává praktickou radu bez kvantifikované míry spolehlivosti.

Tvrzení o aplikaci, v níž generátor selže, má přesný obsah pro
konečný deterministický generátor s konečným množstvím seedů. Je-li
seedů S a abeceda má q≥2 symbolů, zvolme N s q^N>S. Množina všech
možných N-prefixů má nejvýše S prvků. Test příslušnosti do této
množiny přijme generátor vždy, iid rovnoměrný zdroj s pravděpodobností
nejvýše S/q^N<1. Opakováním/blokovým rozšířením lze rozlišení zesílit.
Není tvrzena efektivita tohoto testu ani taková chyba ideálního
skutečně náhodného zdroje; kontext tvoří konečné pseudonáhodné metody.

Myšlenka, že účelově volené kvazináhodné body někdy pomohou numerické
metodě, má vlastní příklad: pro integrál f(x)=x na[0,1] dává průměr
N středů rovnoměrných podintervalů přesně1/2; iid průměr má rozptyl
1/(12N). Pravidelná množina ovšem není iid posloupnost. Tento příklad
prokazuje existenční tvrzení, nikoli veškerý obsah citované knihy.

Každý přehled na189 má samostatnou zdrojovou hranici: Nance/Overstreet
1972; Sowey1972; Sowey1978; Sowey1986; Tezuka1995; celá Hammersley/
Handscomb1964 jsou **skip bibliography**, nikoli označené jako přečtené.
U Metropolise/Eckhardta1987 je převzata známá oprava125–136 na125–137.
Uložený Eckhardtův výňatek131–136 sám nedokazuje celý rozsah ani celý
historický výklad; ten je také skip. Citát přidaný známým erratem2013
je autorská nadsázka o programech, ne číselná statistika „almost all“.
Výzva pracovat na6 nemění rozsah auditu v oprávnění měnit cizí instalace.

## 1: každá instrukce RANDI

Nechť B je počet hodnot jednoho bytu a M=B^5. Instrukční důkaz platí
pro inicializovaný0≤X<M a uložený násobitel a jako slovo. K je kladné
celé číslo k<5000. Kniha požaduje správný rozsah1≤Y≤k, neurčené rX,
vypnuté přetečení a návrat po `JMP RANDI`.

| Instrukce | Přesný účinek a důvod |
|---|---|
|STJ9F|Uloží kladnou návratovou adresu z rJ do adresního pole budoucího JMP; kód instrukce zůstane.|
|STA8F|Uloží celé vstupní k; k=4999 se nemusí vejít do dvou bytů, ale do celého slova se vejde.|
|LDA XRAND|Nahraje nezáporný uložený stav; na začátku je1.|
|MUL7F|Přesný desetibytový součin aX leží v A:X; spodních5 bytů je aXmodM, obě znaménka jsou kladná.|
|INCX1009|Přičte1009 ke spodní polovině; při přetečení ponechá zbytek modulo M a zapne příznak. Adresní konstanta1009 se vejde do2 bytů.|
|JOV*+1|S vypnutým příznakem pokračuje; se zapnutým ho vypne a skočí na tutéž následující instrukci. Změněné rJ už nevadí uloženému návratu.|
|SLAX5|Přesune spodní polovinu součinu do A; zachované kladné znaménko dává nový nezáporný stav.|
|STA XRAND|Uloží X'=(aX+1009)modM.|
|MUL8F|Součin kX'<M² je přesný; horní slovo A je floor(kX'/M).|
|INCA1|Dá1≤Y≤k; protože k<M, nemůže znovu nastat přetečení. Pro k1 vrací vždy1.|
|9H JMP*|Adresní pole změněné prvním STJ vrací řízení na uložené místo; pozdější JOV ho nezměnil.|

MUL ani posuny nenastavují přetečení. JOV tudíž odstraní i příznak,
který byl zapnut již při vstupu, a další operace jej nezapnou.
Ručně uchovaný návrat je nutný právě kvůli JOV. rX smí být změněno,
jak zadání dovoluje. Globální XRAND a měněná návratová instrukce
nejsou rozhraním pro souběžná/reentrantní volání; taková vlastnost
se v zadání nepožaduje. Jeden výstup používá11 instrukcí, tedy O(1)
slovních operací, konstantní pomocnou paměť.

Pro B64 je redukovaný násobitel994108973; pro B100 je3141592621.
V obou případech gcd(1009,M)=1; a−1 je dělitelné4 a při desetinném
M i5. Věta o plné periodě dává periodu M. Za celou periodu X' projde
všechny zbytky, takže pro j=1..k jsou počty výstupů
`ceil(jM/k)−ceil((j−1)M/k)`: interval pro Y=j je
[(j−1)M/k,jM/k). Počty se liší nejvýše o1; přesná uniformita nastane
při k|M. To je přesný doložený význam „about equally probable“
v tomto jednorozměrném celoperiodovém modelu.

**Partial rozsahu překladu:** ve V1/125 je požadavek pracovat pro
všechny64≤B≤100, ne pouze64 a100. Pravidla MIXAL153–155 připouštějí
1–10ciferné atomy, aritmetiku definují nad MIX slovy a CON jako W-value;
v přečteném úseku jsme nenašli explicitní pravidlo, jak příliš velký
samostatný číselný atom převede do slova. Starý byte-model záměrně
odřezává vyšší cifry3141592621; není certifikátem chování assembleru.
Rovněž není doložena plná perioda téže konstanty pro všechny ostatní
hypotetické B. Proto instrukční matematika pro uvedené dvě soustavy
je uzavřena, ale celá1 zůstává **partial** v těchto kontextových mezích.
Samotná absence uzavření není nový nález.1400 archivních hraničních
případů se nepoužívá jako náhrada obecného důkazu nebo překladu.

## 2: překvapení, determinismus a přesný zdroj

Pevný program, seed a ostatní vstupy určují výstup; z toho neplyne,
že jej programátor zná bez provedení potřebného výpočtu. Náhodné
vstupy přidávají další pravděpodobnostní nejistotu, ale nepředvídatelnost
v běžném jazyce není automaticky kryptografická bezpečnost.
Odpověď599 se čte jako tento epistemický argument a nadsázka; například
známý seed a jednoduchý generátor nelze vydávat za univerzálně
nepředvídatelný. Úloha je diskusní, nikoli věta o převzetí světa stroji.

Původní Turing449–451 je celý v uloženém výňatku;450 nyní znovu
vizuálně. Rozlišení znalosti zadání od znalosti všech jeho důsledků
na451 a výslovná zkušenost překvapení na450 podporují připsaný
komentář. Zbytek článku ani citovaná Hartreeho kniha se tím neoznačují
za přečtené. Srovnání citace: Turing i TAOCP vynechávají zesilující
„whatever“ z prvního souvětí původní NoteG; význam zůstává stejný,
netvrdíme doslovnou totožnost každého slova všech tří verzí.

Celý C0078 je převzat: původní NoteG722 i titulScientificMemoirsIII
s rokem1843 jsou opět vizuálně ověřeny. Nemůže tedy jít o první
napsání již publikovaného výroku teprve1844, jak uvádí zadání.
Nález se týká roku, nikoli filozofického závěru nebo data jiných
částí rukopisu. Všechny vrstvy errat tento rok neopravují; datum
nového fyzického tisku a prvenství se netvrdí.

## 3: program, všechny přechody a deset her

Přebíraný `craps_step` má stav0 pro první hod;7/11 vede na výhru,
2/3/12 na prohru a zbývajících4/5/6/8/9/10 je uložený bod.
Potom rovnost bodu znamená výhru,7 prohru a jiný součet stav zachová.
Tyto větve jsou úplné a disjunktní; bod nikdy není7, takže pořadí
závěrečných dvou testů není konfliktní. Řetězce win/loss ukončí
smyčku testující číselný stav. Pro spravedlivé nezávislé kostky je
ukončovací pravděpodobnost po bodu alespoň9/36=1/4, takže počet
zbývajících hodů má ocas≤(3/4)^r a program skončí skoro jistě.
Není tvrzen konečný nejhorší počet hodů pro každou nekonečnou sekvenci.

Každá kostka se volí na1..6; dvě volání mají být v ideálním modelu
nezávislá. Pseudonáhodný příklad neprokazuje takovou nezávislost.
Formát tvoří dvě číslice m,n a komentář;11 dostane „snake eyes“,
ostatní dvojice stejných cifer obecný komentář o dvojici, zbytek
„roll“. Není požadován vyčerpávající slovník kasinových pojmů.

Každý z36 uložených hodů byl přečten; stručný kontrolní přepis:

| Hra | První součet/bod | Další součty | Výsledek |
|---|---|---|---|
|1|6|10,8,5,7|prohra na7|
|2|6|10,6|výhra na6|
|3|7|žádné|okamžitá výhra|
|4|11|žádné|okamžitá výhra|
|5|9|9|výhra na9|
|6|5|11,6,7|prohra na7|
|7|7|žádné|okamžitá výhra|
|8|6|11,2,7|prohra na7;2 není pozdější okamžitá prohra|
|9|10|5,12,6,8,11,6,8,10|výhra na10;12 po prvním hodu neukončí hru|
|10|5|9,11,8,6,5|výhra na5|

Úplné dvojice a komentáře jsou v `results/craps-ten-games.txt`;
požadovaných deset her se neopakuje. Všechny252 přechody uložené
matice byly již porovnány. Obecný výpočet je uzavřený nezávisle:
w_s počítá uspořádané hody s bodem s, s∈{4,5,6,8,9,10},
w=(3,4,5,5,4,3). Po bodu je P_s=w_s/(w_s+6), E_s=36/(w_s+6)
z rovnic P_s=w_s/36+(1−(w_s+6)/36)P_s a analogické rovnice času.
Přidání prvního hodu dává244/495 a557/165, jak obsahuje přesná
archivní matice. Tyto hodnoty nejsou odhady z deseti her.

## 4: všechny tři požadované části a obecný důkaz

(i) Shuffle pro i=N−1..1 volí j rovnoměrně z0..i a vymění prvky.
Indukčně vybírá z dosud nefixovaných karet právě kartu pro poslední
volnou pozici; každá permutace má pravděpodobnost1/N!. Rozlišitelné
karty0..51 se převedou na hodnosti floor(id/4), takže mají přesně
čtyři kopie každé hodnosti. Žádná karta se výměnou neztratí/nezdvojí.

(ii) Zvolený běžný hodinový pasiáns rozdělí52 karet do13 čtyřčlenných
hromádek a začne ve středu. Každé pop odebere právě jednu dosud
nehranou kartu; její hodnost určí další hromádku. Pro mimostředovou
hromádku by pokus o páté odebrání vyžadoval pátou kartu její hodnosti,
která není. Střed má jednu dodatečnou počáteční návštěvu. Zastavení
je tedy přesně po odkrytí čtvrtého krále a nejpozději po52 krocích.
Invariant `odehráno+součet zbývajících=52` platí po každém kroku.

(iii) Výstup obsahuje počet tahů, výhru právě při52 a zbývající počet
v každé hromádce. Histogram délek a kumulativní počet výher splňují
požadavek průběžných statistik. Tři úplné uložené příklady mají40,
42,41 odehraných karet a zbytky12,10,11. Sto ukázkových her s13
výhrami je ilustrace, nikoli tvrzení o empirické přesnosti. Volitelné
podvádění zadání nevyžaduje a nebylo implementováno.

Pro obecné r hodností a c kopií, N=rc, je zbytek rovnoměrně zamíchaný
podmíněně na dosavadní odkryté karty. Volba další pozice podle minulosti
nezvýhodňuje žádnou kartu v dosud neodkrytých pozicích. Doplňme po
skončení pevné pořadí zbývajících pozic; celý odhalený sled má rozdělení
rovnoměrné permutace. Pozice c králů jsou proto rovnoměrná c-podmnožina
zN. Její maximum T má pravděpodobnost C(t−1,c−1)/C(N,c), c≤t≤N.
Výhra T=N má pravděpodobnost C(N−1,c−1)/C(N,c)=c/N=1/r,
tedy1/13. Normalizaci dává hokejková identita součtu přes t.
Platí i c1 nebo r1 (v posledním případě deterministická výhra).
Archivních4296 malých rozdání podporuje celý zákon; obecný důkaz
na tomto výčtu nezávisí. Shuffle i hra mají O(N) čas a O(N) paměť.

## 6: rozsah organizačního projektu

Jde o otevřený úkol pro instalace čtenáře, nikoli konkrétní tištěný
algoritmus s univerzálním výsledkem. Konstrukční postup je inventář
používaných funkcí a jejich seed/state rozhraní, ověření známých
nároků generátoru, srovnání bitové reprodukovatelnosti a testů aplikace,
poté cílená náhrada podle potřeb. „Good“ nemá jeden matematický práh;
stejný generátor nemusí vyhovět všem aplikacím, viz výše. Audit
prověřuje tuto specifikaci a všechny skutečně otištěné implementace;
žádné organizační prostředí se neprohledává a žádné cizí knihovny se
nemění. Není tvrzeno dokončení tohoto projektu v nějaké organizaci.

## 7: oba nesplnitelné požadavky a celý zdrojový rozsah

Celý `truncated-lcg.md` je znovu přečten, oba uzavřené protipříklady
C0076/C0077 se přebírají bez nových10500 porovnání. První používá
X_0=0,a=1,c=1 nebo3: pro n<150 je X_n=n nebo3n<2^16, takže horních16
bitů je v obou případech0, ale první rozdíl1 versus3. Lichost c dává
periodu2^32. Úloha nepožaduje a≡5mod8, proto toto obecné doporučení
nelze dodatečně přidat k hypotézám. Rekonstrukce obou požadovaných
hodnot není z těchto totožných vstupů zaručitelná ani neomezeným časem.

Ve druhém příkladu závisí floor(X_n/2^16)mod4 jen na X_nmod2^18.
Indukcí redukovaná rekurence závisí pouze na a,c,X_0 modulo2^18.
Všech a=5+u2^18,c=1+v2^18,X_0=0,0≤u,v<2^14 má periodu2^32,
protože a≡1mod4 a c liché; dokonce a≡5mod8. Všech2^28 dvojic dává
stejná dvoubitová pozorování navždy, ale jiné vyšší bity a/c.
Proto tvrzení odpovědi599 neplatí ani pro nekonečné množství údajů.
Tento informační limit neobhajuje bezpečnost jednoduché XOR šifry;
odlišuje určování parametrů od předvídání výstupu.

Dva konkrétní řádky původní poznámky jsou také přesné: pro a5 versus
262149, c1, X0=0 je X2=6 versus262150, tedy horní polovina0 versus4,
ale stejné2 spodní bity; změna c na262145 se projeví v H1, nikoli
H1mod4. Parametry jsou vždy v0..2^32−1. Známé odstranění citace BBS
z2009 oba rozpory neodstraňuje. Původní193/599 a všechny vrstvy errat
jsou součástí již uzavřených důkazů.

IEEE Knuth1985/jeho starší předtisk, oba Reedsovy články1977/1979,
Boyar1989 a Frieze–Håstad–Kannan–Lagarias–Shamir1988 nebyly v tomto
bloku přečteny celé: **skip bibliography** zvlášť pro každý odkaz.
Nedovozujeme jejich algoritmy ani přesné složitosti z titulů nebo
z citace. Nálezy vyvracejí neomezené znění knihy vlastním argumentem;
neslibujeme neexistující univerzální rekonstrukční algoritmus.

Žádný nový nález, žádný výpočet. Další: samostatně všechny kroky
úlohy5, oba původní/upravené scénáře, ilustrace a historie190–193;
potom194/file206, stále v obnově celého nedostatečného rozsahu.

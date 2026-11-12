# §1.3.2′, úlohy32–33 — celé MMIX programy a přesný kalendářní rozsah

Zadání file57–58/p49–50, odpovědi file119/p111. Originální119 byla
znovu zobrazena (`images/file-119-p111.png`). Nové kompletní programy
jsou `sources/easter32-table.mms` a `sources/easter33-search.mms`.
`generate_easter32_33.py` sestavuje oba z jednoho textu EasterCore;
vygenerované soubory jsou celé samostatné MMIXAL vstupy, ne fragmenty.

## 1. Přesně převzatá matematika všech E1–E8

Celé `workstreams/vol1/notes/mixal-easter.md`, nová recovery poznámka
`quality-recovery-section-1.3.2-crypt-calendar-2026-11-06.md`,
`mixal-easter-sources.md` a `calendar-primary-root-review.md` byly přečteny.
Jejich matematický obor1583≤Y<100000 a nezáporné modulo jsou shodné
s MMIX zadáním. Dřívější MIX běhy ani žádný průchod5700000 let se
neopakovaly. Přijatý důkaz zde není pouhé podobné datum jednoho roku.

G=Y mod19+1 vybere jednu z19 fází. C=floor(Y/100)+1 je skutečné
století kromě výslovné výjimky roku dělitelného100; pro1984 dává20.
Při c=floor(Y/100) identita floor(3(c+1)/4)=c−floor(c/4) ve všech
čtyřech třídách c mod4 dokazuje X=c−floor(c/4)−12. To počítá vynechané
stoletní přestupné dny od gregoriánské reformy. Z je tabulková lunární
korekce; výrok netvrdí přesnou astronomickou polohu Měsíce.

Pro D=floor(5Y/4)−X−10 platí

    D=Y+floor(Y/4)−floor(Y/100)+floor(Y/400)+2.

Absolutní gregoriánský den před1.březnem při pondělí1.1.1 jako dni1
je365Y−306+floor(Y/4)−floor(Y/100)+floor(Y/400). Rozdíl od D je
364Y−308, násobek7. Proto (D+N) mod7 je den týdne březnového
pořadového dne N, neděle0, a E4 včetně normalizovaných březnových
záporných či nulových dnů má správný význam.

E0=(11G+20+Z−X) mod30 a obě výjimky dávají přesně následující úplňky:

| E0 | Podmínka | N po E6 |
|---|---|---|
| 0…23 | všechny G | 44−E0, tedy21…44 |
| 24 | všechny G | 49 |
| 25 | G≤11 | 49 |
| 25 | G>11 | 48 |
| 26…29 | všechny G | 74−E0, tedy45…48 |

E7 přičte7−((D+N) mod7), tedy nejmenší **kladný** počet dnů na
neděli. Při nedělním úplňku správně přidá7, ne0. Meze21≤N≤49
dávají22≤výsledný březnový den≤56, tedy22.března až25.dubna.
Převod E8 odečte31 právě pro duben.

Nezávislost na předpokladu správnosti samotného knižního algoritmu
zajišťuje již přijatá algebraická shoda s Dershowitz–Reingold1990,
904–906 a919–920: shifted-epact=(E0+6) mod30 a jejich výjimky0/1,
Y mod19>10 jsou přesně tyto dvě epaktové výjimky. Jejich absolutní
neděle po tabulkovém úplňku odpovídá E7 ve všech pěti řádcích tabulky.
Příslušné celé primární formule byly nyní znovu přečteny v místním
`vol1/sources/dershowitz-reingold1990-calendrical.txt`,1048–1128.

## 2. Celý kontrakt EasterCore a každá jeho větev

Vstup y=$0 je celé1583…99999, mode=$1 je0 pro správný algoritmus
nebo1 pro úmyslně chybný zbytek pouze v E5. Výstup date=$2 je výsledný
březnový den. y,good=$19,pret a všechny konstantní báze se zachovávají;
ostatní pracovní lokály$2…$18 a$255 jsou scratch. ret je GO návratový
globál. Podprogram není reentrantní a během volání jej nesmí znovu
použít handler sdílející tytéž registry; úloha takové souběžné volání
nevyžaduje. Každý caller nejprve GETA a GO uloží skutečný návrat do ret.

DIV q,y,19 / GET gold,rR / INCL gold,1 realizuje E1. DIV cent,y,100
/ INCL cent,1 realizuje E2. MUL/SR/SUB tvoří floor(3C/4)−12;
SL/ADD/DIV/SUB tvoří floor((8C+5)/25)−5. MUL/SR/SUB/SUB dávají D.
MUL/ADD/ADD/SUB vytvoří raw=11G+20+Z−X a signed DIV30 vrátí vždy
nezáporný epact=rR. Všechny tyto instrukce mají právě vstupy z§1.

PBZ mode jde při správném módu rovnou k epaktovým výjimkám. V chybném
módu BNN raw přeskočí úpravu nezáporných vstupů; BZ epact ponechá
nulový zbytek záporného násobku30. Jinak SUB epact,epact,30 nahradí
kladný podlahový zbytek e právě záporným zbytkem e−30. To je přesná
emulace truncace k nule, včetně záporných násobků, ne pouze test raw<0.

CMP/BZ zvýší24 vždy. Jestliže nebylo24, CMP/PBNZ přeskočí vše kromě25;
u25 další CMP/BNP ponechá G≤11 a zvýší jen G>11. I chybné záporné
epakty tyto testy správně přeskočí. SET44/SUB vytvoří první N;
CMP/PBNN přidá30 právě při N<21. ADD/DIV7/GET/INCL7/SUB pak
provedou E7 a GO $255,ret,0 se vrátí za právě provedený call.
Žádná druhá cesta ani výjimka nepoužívá nezapsaný scratch registr.

## 3. Všechny aritmetické a paměťové meze

16≤C≤1000,1≤G≤19,0≤X≤738,0≤Z≤315. Hrubá bezpečná mez
−707≤raw≤544 stačí i pro chybný mód. Před výjimkou je epact0…29
nebo−29…0; po výjimce stále nejvýše29. V E4 je5Y≤499995 a všechny
ostatní celočíselné mezivýsledky jsou velikostí menší než500000.
I chybný březnový den je kladný a nejvýše80. Žádný signed64 výsledek
nepřeteče, DIV má vždy kladný d19/100/25/30/7 a k výjimce nedojde.

Všechny lokály jsou$0…$20, globálů je nejvýše6 a jsou od nich
oddělené. Mutable ret/pret jsou různé GREG0, nikoli dvě měněné stejné
nenulové GREG báze. Kód od#100 má méně než120 instrukcí; GETA a všechny
relativní větve jsou v rozsahu a na tetrabyte hranicích. Data od
Data_Segment jsou disjunktní, Line je zarovnaná pro STTU Line,4.
Nejde o neplatné STTU na adrese3: první znak měsíce zapisuje STB3,
zbývající čtyři znaky zapisuje STTU4 v big-endian pořadí.

## 4. Celé vypočti-a-vytiskni32, všech51 řádků a I/O návraty

EasterPrint přijímá y, nastaví mode0 a zavolá EasterCore. Před jeho
voláním caller uloží návrat do pret; vnitřní call používá jiný ret,
takže se návraty nemohou zaměnit. CMP date,31 rozliší měsíce a CSP
vybere day=date nebo date−31. DvojiceARCH=#41524348 aPRIL=#5052494c
jsou ASCII „ARCH“ a „PRIL“. CSP spolu s prvním znakem M/A vybere
právě MARCH/APRIL. day je1…31; DIV10 vytvoří dvě číslice včetně nuly
na začátku a oba STB je zapíší na pozice0,1.

Původní Line je přesně `00 MARCH, 00000\n\0`, tedy17bajtů:
mezery2/9, čárka8, LF15 a NUL16 jsou výslovně zapsané literálem.
V YearDigit je po j dokončených kolech value=floor(Y/10^j), left=5−j,
pos=14−j; pozice15−j…14 obsahují posledních j desetinných cifer Y.
DIV/GET/ADD/STB obnoví invariant pro j+1. Provede se přesně5 kol,
takže i rok1583 má správných pět cifer01583. Horní mez99999 zajišťuje,
že se neztrácí žádná šestá cifra. Všechny pozice řádku jsou inicializované;
po předchozím volání se přepisují všechny měnící se pozice.

Fputs je synchronní dle jeho dokumentovaného kontraktu; buffer se znovu
mění až po návratu. BN zachytí záporný návrat a vrátí status1, jinak
status0. Obě cesty se vracejí přes pret a zachovají y. Driver začíná1950,
po každém úspěchu zvýší y a pokračuje právě při y<2001. Tím vytiskne
všechny roky1950…2000 jednou a skončí kódem0. Při chybě výstupu ihned
skončí kódem1; netvrdí, že neúspěšné zařízení obdrželo celou tabulku.

## 5. Hledání33: proč stačí dvanáct kandidátů a proč žádný nechybí

Přebírá se celý obecný důkaz v recovery kalendářní poznámce§4:
h(C)=27+floor((8C+5)/25)−floor(3C/4), raw=11G+h(C).
Do C98 je h≥−15; pro C99/100/101 je−16. Záporný raw do roku10099
tedy vyžaduje G1 a může být jen−1…−5. Obě modulo větve pak dávají
stejný úplněk44−raw; epakt25 při G1 nemá zvláštní zvýšení.

Pro C102/103 je h=−17. První potenciálně jiný úplněk vyžaduje G1
a raw−6, tedy právě Y=10108+19k,k0…10. Správný/chybný úplněk jsou
49/50 a neděle se liší jen při (D+50) mod7=0. Uzavřený výraz

    (4+2k+floor(3k/4)−[k≥5]) mod7

má pro všech jedenáct k hodnoty4,6,2,5,1,2,5,1,4,6,2. Pro C104
je h−18; roky10300…10316 mají G≥2 a raw≥4. První G1 je10317,
raw−7,D12820. Správný epakt23 dává N21 a neděli25; chybný−7
dává N51 a neděli53, tedy22.dubna. Tím je prokázaná minimalita,
nikoli jen nalezen jeden špatný rok. Vytištěný příklad14250 má
G1,X95,Z40,raw−24,D17707; správně14.dubna, chybně42.dubna.

Nový program proto začne10108 a postupuje po19. V každém kole
zavolá stejné EasterCore s mode0, uloží date do good a zavolá mode1.
Core good nemění. CMP/BNZ rozpozná první rozdíl, jinak se y zvýší19.
Předchozí argument dovoluje přeskočit všechny nekandidáty, prokazuje
prvních11 shod a ukončení dvanáctým kolem. Číslo10317 není zakódovaný
konec smyčky ani přímo vytištěná konstanta: pochází z prvního porovnání
s různými výsledky. Všechny calls zůstávají uvnitř dokázaného oboru.

YearDigit je stejný pěticiferný postup, pouze pos začíná4. Line je
výslovně `00000\n\0`; výstup je přesně `10317\n`. Obě větve Fputs
vedou k Halt0/1 a žádná nevypíše nedefinovanou další paměť.

## 6. Přesný profil obou celých programů

EasterCore před PBZ mode stojí285υ. Správný mode přidá1υ;
epaktové větvení stojí4υ běžně,5υ pro E0=24,10υ pro E0=25,G≤11,
9υ pro E0=25,G>11. Vytvoření úplňku stojí4υ a další3υ při přidání30.
Posun na neděli včetně GO návratu stojí67υ. Správný core tedy stojí

    C(Y)=361+[E0=24]+6[E0=25,G≤11]+5[E0=25,G>11]+3[E0≥24].

Není zde žádná datová paměť. U mode1 přidají modulo větve5υ,
nebo6υ, pokud raw<0 a jeho podlahový zbytek je0; zbývající epaktové
indikátory se hodnotí už na změněném epaktu. V hledání má každé
chybné volání366υ. Správných jedenáct kandidátů má365υ a poslední361υ.

EasterPrint nad rámec C(Y): mode/GETA/GO5υ, výběr měsíce10υ+2μ,
dvě cifry dne65υ+2μ, příprava roku3υ, pět cifer332υ+5μ,
Fputs s testem7υ a úspěšný návrat4υ. Celkem C(Y)+426υ+9μ.
Neúspěšný návrat má navíc2υ. Driver při všech51 úspěších přidá417υ:
počátek1, každý caller průchod8, poslední predikce navíc2 a Halt cesta6.

V nové51řádkové tabulce jsou počty nákladů core361/369/364/365
právě40/3/5/3, tedy součet18462. Kompletní program proto stojí
**459μ+40605υ**. Při selhání až při L-tém volání je přesný náklad
9Lμ+[Σ(j=1…L)C(Y_j)+434L+8]υ; při výstupní chybě se nepokračuje.

V hledání stojí callers včetně obou GETA15υ za každé kolo:
u posledního se dvě vynechané instrukce vyruší s chybnou predikcí BNZ.
Počáteční SET1υ a celý formatter/I/O/Halt348υ dávají nad24 cores
529υ. Proto celkem

    5μ+[11·365+361+12·366+529]υ =5μ+9297υ.

Při neúspěšném Fputs je9299υ. Tyto jsou nominální knižní náklady,
nikoli hostitelská latence souboru nebo důkaz nejrychlejšího programu.

## 7. Jediné nové provedení a nezávislý výstupní certifikát

`verify_easter32_33.py` byl spuštěn jednou pod nice15. V jediném
novém buildu sestavil a jednou spustil každý z těchto dvou programů.
První816bajtový výstup byl porovnán s51 buňkami již matematicky
přijaté shifted-epact/absolute-day formule, nikoli s přepisem MMIX E1–E8.
To je malá nová kontrola chybějící implementace, ne opakování starého
MIX checkeru či celého kalendářního censu. Hledání převezme10317 a
jedenáct near-miss let ze starého uloženého výsledku, znovu je neenumeruje.

Všechny bajty souhlasí. Native tabulka:5375 instrukcí/459mem/40605oops;
hledání:1098 instrukcí/5mem/9297oops. Časy samotných simulací byly
0.002506 a0.001530s; celý nový build a obě kontroly1.437382s.
Zdrojové hashe jsou a06fac95721d64f58f09589f34434be4a880b4faf07106fee3a80c633356cddd
a 70b6ee5769d52dbfee21669652005198547f11a42e731f4c15bc8cf8486d08b0.
Obě assembly i simulace neměly diagnostiku; staré C build warningy jsou
uchované odděleně v `results/easter32-33-build-and-run.json`.
Výsledky, oba listingy, oba profily a oba celé výstupy jsou v results.
Úspěšný běh se nemá opakovat.

## 8. Všechny další matematické věty odpovědi33 jsou přesně převzaté

Recovery poznámka svazku1§5 dává skutečný obecný důkaz periody
P5700000: ΔG0,ΔC57000,ΔX42750,ΔZ18240,Δraw−817·30,
ΔD7·1011750. Minimalita je doložena pro všechny prvočinitele2/3/5/19:
při Y1583 vyjdou N41 a pro posuny P/p postupně27/48/55/34.
Argument gcd period platí i pro jednostrannou posloupnost posunem oP.

Celá četnostní tabulka je doložena uzavřeným vzorcem, nikoli pouhým
převzetím tří čísel z enumerace. Lunární váhy jsou l_N19 pro21…47,
l_48=27,l_49=30; týdenní váhy w=(56,58,56,58,57,57,58). Rozklad
Y=100(100k+s)+y a čínská věta o zbytcích pro19/30 dokazují jejich
nezávislou kombinaci a faktor25. Pro každý S22…56 přesně platí

    H(S)=25 w_(-S mod7) Σ(N=max(21,S−7)…min(49,S−1))l_N.

Převzatý úplný důkaz vah a všech35 oken dává H22=27550,H50=220400,
H56=42000 a dělitelnost všech četností25. Pro vnitřní dny je dolní
mez53200>42000; mimo49/50 je horní mez192850 a H49=197400.
To dokazuje i jedinečnost všech tří knižních extrémů. Jejich rozsah je
matematický algoritmus pro všechny roky, nikoli pouze nový podprogram
omezený na99999. Ani staré5700000 let, ani nových dříve provedených
35 oken se znovu nepočítalo.

## 9. Přesný obsah rychlostních rad32 a zbývající partial

Násobicí rada pro dělení100 je úplně doložená: B=2^64,
K=floor(B/100)+1,0<δ=K−B/100≤1. Horní slovo YK je
floor(Y/100+Yδ/B). Protože100Y<B pro všechna Y≤99999, přídavek
nepřekročí další celou hranici. `MULU t,y,K; GET cent,rH` tak dává
přesně floor(Y/100) v11υ místo DIV60υ. Konstantu je třeba připravit
mimo měřené opakování; není to univerzální dělení všech64bitových Y.

Také FREM rada je realizovatelná: pro zdejší celé vstupy a d7/19/30
jsou FLOT, přesný IEEE remainder a FIX přesné. Při připraveném
floating d a celočíselném d dává následující úplný převod modulo:

    FLOT f,a; FREM f,f,fd; FIX r,ROUND_OFF,f
    ADD t,r,d; CSN r,r,t

Nearest-quotient remainder leží v[−d/2,d/2]; jediné přičtení d při
záporném r vytvoří právě nezáporné modulo. To platí i pro záporné a,
půlku při d30 a signed zero. Všechny vstupy mají velikost<2^19 a
zbytky jsou celá čísla≤15, takže žádná konverze ani FREM nezaokrouhluje.
Úplný primární FREM důkaz je už přijatý v `fp-remainder-recovery.md`.
Nominálně jde o14υ proti DIV/GET61υ, plus jednorázové připravení fd.
Je-li hodnota už floating, první FLOT odpadne. Lze také nahradit
3C pomocí2ADDU a5Y pomocí4ADDU; každá tato konkrétní náhrada šetří9υ.

**Zbývající technický partial32 je přesný vytištěný superlativ „most
rapidly computed by FREM“.** Uvedené realizace dokazují rychlost proti
přímému DIV za stanovených reprezentací a cen. Nedokazují globální
minimum mezi všemi MMIX programy, tabulkami, jejich předvýpočty a
různými dostupnými registry. Kniha tento porovnávací prostor nevymezuje.
Nový úplný podprogram, tisk ani rada s reciprokým násobením už mezeru
nemají. Nezakládá se nález pouze z nedoloženého superlativu.

## 10. Historie, celáfile57 a opakovaný C0026

Konkrétní primární kalendářní formule podporuje Claviovu korekci a
gregoriánské pravidlo. Přesné životopisné přívlastky a osobní připsání
Liliovi/Claviovi v první větě zadání, jakož i množstevní „most Western
churches“, zde nejsou samostatně historicky doložené; jsou výslovně
vymezená faktická/bibliografická výjimka. Nemění důkaz normativně
zadaného algoritmu. Program pro roky≤1582 není naším řešením32 slíben.
Úplné Knuth/Williams1962 a O'Beirne1965 nejsou dostupné ve zjištěném
rozsahu; osobní atribuce O'Beirneovi/Robertu Hillovi zůstávají vynechány.
Bibliografie Reingold/Dershowitz2001 a její algoritmický obsah jsou
převzaté v přesném rozsahu pramenné poznámky, nikoli jako audit celé knihy.

Původní status opakovaného V1-C0026 na119 byl candidate. Nová již
uzavřená root revize `vol1/notes/calendar-primary-root-review.md` jej
mění na confirmed: skutečné tabulky staršího112letého kánonu mají
konečný návod použití a Victorius sám rozlišuje předchozí84/95/112leté
cykly. Převzatý závěr se týká nekvalifikovaného prvenství při zahrnutí
tabulkových postupů stejně jako u Victoria; nedokazuje jiného prvního
autora ani neprovádí novou rekonstrukci všech poškozených znaků.
Zdejší původní119 má tutéž větu. MMIX errata stále opravují jen
Aquitania→Aquitaine, ne prvenství; relevantní původní zdroj a obě
textové vrstvy byly přečteny. V1-C0025 zůstává druhý převzatý confirmed
pro středověkou výlučnost, s konkrétním Liber abaci protipříkladem.
Nevzniká nové MMIX ID ani se nezvyšuje počet našich knižních nálezů.

File57 je celá zmapovaná: příklad133333 členů a celé H1–H4 i31 mají
030–031-recovery; všechny věty E1–E8, stoletní příklad, typ úplňku,
celý podprogram a51řádková tabulka mají§1–4 zde; úvod33 o znaménku
zbytku a všechny konstanty14250 mají§2/5. Zůstává partial pro přesně
vypsaný superlativ související odpovědi32 a faktické výjimky. File58
a119 zde mají jen části32/33; další semaforová/křížovková tvrzení
se neuzavírají. E33 je nyní argument_recorded s explicitními pramennými
výjimkami; E32 partial jen v§9/10, nikoli pro chybějící MMIX program.

Binomický vzor byl použit na přesný rok, záporné násobky30 a meze;
Algorithm R na všechny návraty/skoky a náklady obou celých programů;
kografový vzor na rozdíl mezi správným kalendářem, chybným modulo
a nezávislou historickou formulací. Samotné51řádkové ověření není
důkazem celé periody ani nejrychlejší implementace.

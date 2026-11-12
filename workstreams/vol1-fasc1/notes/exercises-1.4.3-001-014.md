# MMIX — §1.4.3′, úlohy 1–14

## 1 — čtyři položky Info

(a) SRUI má cíl X, zdroj Y a immediate Z: #29, host SRU x,y,z,
čas υ. (b) PBPB testuje původní X, relativní adresu již normalizuje
hlavní cyklus: #50, host PBP x,PBTaken+@−O, základ 3υ.
(c) MUXI potřebuje navíc special source rM, ale nezmění flag #29;
příprava PUT rM,x před host MUX zachová masku. (d) INCML potřebuje
starý X a cíl X: #30; instalace wyde dá z=YZ<<16 a ADDU x,x,z
provede právě požadované modulo přičtení. Všechny čtyři odpovědi sedí.

## 2 — přesný profil tří instrukcí

Přebírá se kompletní rozklad MemFind z C0009 a GetReg z C0012,
neopakují se. Pro normální Fetch jsou časy úseků následující:

| Úsek | ADDU | STHT | PBNZ |
|---|---:|---:|---:|
| Fetch 105–115 | μ+17υ | μ+17υ | μ+17υ |
| Unpack 141–153 | μ+12υ | μ+12υ | μ+12υ |
| Relative 154–164 | 2υ | 2υ | 9υ |
| 165 a X 174–182 | 6υ | μ+17υ | μ+17υ |
| Z 183–197 | μ+14υ | 6υ | 6υ |
| Y 198–207 | μ+13υ | μ+13υ | 6υ |
| Dest/memory 208–231 | 8υ | 23υ | 6υ |
| Resume 232–242 | 14υ | μ+14υ | 16υ−π |
| Done/special path | μ+10υ | 11υ | 11υ−4π |
| Update | 5υ | 5υ | 5υ |

Zde π=2υ při taken, jinak 0, **jak je definováno pod tabulkou
na p. 20**, nikoli indikátor 0/1. Běžný nepřímý call stojí
PUSHJ 1υ plus samotný dříve doložený GetReg/MemFind; POP je zahrnut
v pomocné rutině. V ADDU větvi X: 165,174,175,179,180,181 jsou
šest vykonaných instrukcí po υ. Z: 183,184,185,186+GetReg,187,188
má náklady 1+3+1+(1+6)+1+1=14υ plus μ. Kniha přesouvá jednu υ
mezi těmito dvěma řádky (7 a 13), **celkový čas tím není dotčen**;
tuto drobnou rozkladovou nepřesnost ponecháváme v důkazové poznámce,
bez další samostatné karty.

Součty jsou přesně knižních 5μ+101υ, 5μ+120υ,
3μ+105υ−5π za hypotézy C=U=A=0 a globálních zdrojů.
V branch taken se host PBNZ zlevní o 2υ a postprocessing
se z 11υ změní na tři instrukce SUBU/SET/JMP, tedy o dalších 8υ.
Každý nonglobal zdroj, včetně marginal, přidá 6υ (C0012).
Data store a následující Fetch nemohou oba zachovat stejný cached
chunk; korekce dvou misses C=U=2,A=0 je 10μ+28υ (C0009).
Empirické dlouhé běhy nebyly zopakovány a jejich indikátorový rozpor
je již zahrnut v C0009.

## 3 — γ≠α a přechodová výjimka

Převzít V0153. Z β=γ a 0<L≤ρ plyne α=γ právě při L=ρ.
Pro ρ≥256 a běžné L≤255 to není možné. Global PUSH/SAVE však
přechodně vytvoří L=256 při ρ=256; hned potom se celé pole stane
pushed a L=0. Odpověď výslovně opravuje příliš kategorický předpoklad
v otázce. Hodnota uložená StackStore se neztrácí.

## 4 — kapacita alokace

V0145/46 dávají pevný prostor 4112 bajtů a 4120 bajtů na node.
Počet plných uzlů je floor((2^61−4112)/4120)=559670633304293,
zůstane 2680 bajtů. Vypsaný konzervativní čitatel odečítá 4120
namísto 4112, ale dává **stejné celé číslo**. Jeden cílený přesný
podíl je uložen v results/node-capacity4.json; žádné procházení uzlů.

Dokud alloc+nodesize nepřekročí Pool_Segment a program nepoškodí
jiné interní pole, přidělovaná paměť je dosud nulová. Za touto
hranicí již nulovost zaručena není kvůli argv v poolu. Výrok o
praktické délce lidského života je nečíselný komentář, ne dokázaná
univerzální hardwarová časová mez. Odhad rekurzivní simulace v úloze
21 je samostatný otevřený problém C0010.

## 5 — počet skutečně pushed registrů, partial globální meze

C0013 dává úplný protiargument ke konkrétní vypsané cestě:
3+3+3+2=11, nikoli 3+2+3+2. Marginal $2 se před PUSHJ stane
local, i když před instrukcí rL=1. Přebírá se bez dalšího běhu.

Call graph má větve root→MemFind/GetReg, root→StackLoad→MemFind,
root→StackRoom→StackStore→MemFind a root→GetArgs→MemFind.
Nejdelší strukturální cesta je uvedená StackRoom větev, s prvním
PUSHJ res=2, následně res=2, res=2 a lokály MemFind 0,1.
To dokládá horní součet 11 pro vypsané routine frames. Samostatná
konstrukce dosažitelného úplného vstupu, který na této nejhlubší
cestě zároveň narazí na Error z MemFind, nebyla zapsána; globální
maximum tedy zůstává partial. Second-exit/unwind technika je už
ověřena v §1.4.1′–16.

## 6 — DIV a DIVU

Signed větev provede DIV x,y,z se zakázanými hostitelskými D/V trips,
takže výsledek i event bits zůstanou dostupné. Unsigned větev nejprve
vloží původní simulated rD z x do host rD a pak provede DIVU.
Obě mají právě jedno společné GET rR/STO g[rR] a JMP XDone.
Případy signed divisor 0 a overflow i unsigned high≥divisor již
mají argumenty v aritmetickém bloku; delegování zachová i je.

## 7 — CSWAP

res ukazuje na správný octabyte. Přečte se staré g[rP] do z a
staré M do y. CMPU t,y,z uchová rovnost až do ZSZ. Při shodě se
původní x uloží do M a nový x je 1; při neshodě M zůstane,
g[rP] dostane y a nový x je 0. XDone uloží výsledek až potom.
V sériovém modelu interpretu se mezi porovnání a změnu nevkládá
jiná simulovaná instrukce. Fyzická víceprocesorová atomicita sem
nepatří a není tímto prohlašována za dokázanou.

## 8 — GET

YZ<32 současně znamená Y=0 a Z∈[0,31]. Sedm special registers
ss,oo,ll,gg,aa,ii,uu uchovávaných v hostitelských registrech se
nejprve synchronizuje do g. ll/8 a gg/8 jsou přesná malá celá čísla.
Ostatní sloty g již mají poslední hodnotu nebo deklarovanou konstantu.
Get potom čte g[Z], XDone zapíše výsledek. Pokud cíl byl marginal,
XDest předtím oprávněně zvýšil L; GET rL proto vrací nové L,
jak vyžaduje předinstrukční alokace cíle. Známé odstranění STOU cc
z roku 2011 je v tomto vydání již zohledněno.

## 9 — PUT a konkrétní oprava

První testy odmítnou Y≠0 či X≥32. Kódy 0…7 a 22…31 lze uložit
přímo; 8…18 vedou Error a 19/20/21 jsou rG/rL/rA. rA musí být
menší než 2^18. rG musí být v [32,255] a alespoň L; při snížení
G se každý nový global slot k=z…oldG−1 vynuluje, ostatní zachovají.
Jde o sestupnou smyčku s k před STO sníženým o jedna.

PutL je chybné pro velká z: převzít C0014. Správná krátká varianta
je porovnat celé z s ll/8, při z≥ll/8 skončit a pouze jinak
nastavit ll=z<<3. V té druhé větvi je z≤254, tedy posun bezpečný.
Známé erratum komentáře PutG z 15. 3. 2024 je oddělené a není nález.

## 10 — POP v logických i fyzických indexech

Označme původní O,L a marker p. Nejprve oo−=8 ukáže na marker;
pro 0<X≤L se uloží starý $(X−1) do y, jinak y zůstane počáteční 0.
Je-li marker pod ss, StackLoad jej připojí. Marker je čten modulo
256 a další smyčka posune ss až na požadovaný začátek starého rámce
O−8(p+1). Posléze platí

`Lnew=min(G,p+min(X,L+1))`, `Onew=O−8(p+1)`.

Toto je stejná logická transformace jako V0123. Je-li p<Lnew,
uložené y nahradí marker a tvoří návratovou hodnotu; jinak se zahodí.
Adresu pokračování dává g[rJ]+4YZ; real rJ pomocných calls zůstává
oddělený od tohoto simulated g[rJ].

Při loadu do plného ringu se přepíše nejvyšší stará lokální položka.
Pokud by byla nutná spolu se všemi nově připojovanými p+1 položkami,
nový interval by měl nejméně ρ≥256 položek. Ale Lnew≤G≤255,
takže taková horní položka musí být v části právě zahazované POPem.
Jediná potenciální výjimka, návratová hodnota, již byla uchována v y.
Tím je odůvodněna poznámka k full-ring případu na p. 120.

## 11 — SAVE, po již doložené opravě C0007

Povinné X≥G zajistí přežití výsledného pointeru. Marker L se uloží
za poslední local; po přírůstku a StackRoom se všechny L+1 položky
pushnou, L=0 a Store smyčka vypíše cached interval až do S=O.
Tím zůstává celý předchozí pushed stack i původní current locals
souvisle v paměti, ukončené markerem původního L.

Následující indexová posloupnost je G,G+1,…,255,0,1,…,6,23,…,27,28.
Poslední 28 není g[28], ale (G<<56)+A. Seznam tedy obsahuje přesně
12 jmenovaných special registers a jeden packed word. Větvení po
INCL ss musí být **BZ** podle C0007; s vytištěným BNZ se inverse
vůbec nevytvoří. Po opravené smyčce O=S, x=O−8 a XDone vrátí
adresu packed word do globálního X. Původní hodnota tohoto X byla
uložena před přepsáním, a může být UNSAVE obnovena.

## 12 — UNSAVE, uzavřená inverse pro platný SAVE image; partial obecné vstupy

Po srovnání z dolů na octabyte začíná S=z+8. První decrement čte
packed word; gg=x>>53 dává 8G a maskování spodních 18 bitů vrátí A.
Pak se projde opačná posloupnost 27…23,6…0,255…G. Každé načtení
předchází decrement S o osm, a tak přesně obrací V11.

Následující StackLoad přečte marker původního L. Dalších L loads
obnoví lokály v opačném pořadí, nastaví O=S na původní začátek a
L=min(marker,G). Platný SAVE image má marker≤G≤255<ρ, takže se
všechny current locals do ringu vejdou; pushed stack zůstává v paměti.
Tím je obecně dokázána inverznost pro kontext vytvořený SAVE, včetně
G=255 a L=0. To uzavírá V0067, saved flags ve V0074 a ring/SAVE
závislost V0126 bez opakování jejich ostatních důkazů.

Pro úvodní bootstrap platí uu=0,resuming=1; skok AllDone vynechá
počítání umělého UNSAVE. Normální první UNSAVE s resuming=0 naopak
projde Update. Jakmile uu≠0, běží obyčejná aktualizace.

**Omezení:** úplná sémantika ručně vytvořeného neplatného headeru
nebyla uzavřena. Primární MMIXware například clampingem zvedá G<32
na 32; vypsaný knižní kód takový clamp nemá. Kniha na p. 16
popisuje UNSAVE jako obnovu kontextu předchozího SAVE, proto bez
vyjasnění domény tuto odlišnost nevydáváme za potvrzenou chybu.
Úloha jako úplná implementace všech vstupů zůstává partial.

## 13 — trip priority; partial floating loads

Je-li průnik enabled events t nenulový, posun o 55 a smyčka
1…8 najdou `xx=8−floor(log2(t))`. Event bit #100>>xx je právě
nejvyšší původní bit; target=16xx odpovídá tabulce DVWIOUZX.
ANDN odstraní pouze obslouženou událost, ostatní se posléze zaznamenají.
Explicitní TRIP vstupuje přímo s xx=0. inst má jen spodních 32 bitů,
takže INCH #8000 nastaví přesně příznak 2^63. rW je již následující
adresa, rB původní $255, nové $255 je g[rJ].

Pro běžnou aritmetiku se uloží připravené y,z; pro store se uloží
y+z a původní x, jak požaduje definice. Rozlišení v kódu však
používá obecný Mem_bit: úplné posouzení možných trips při floating
loads (LDSF, NaN) a jejich operandového kontextu závisí na dosud
otevřené IEEE kontrole. Nevydáváme tuto mezeru za nalezenou chybu.

## 14 — RESUME a protipříklad k ropcode 1, partial úplné opravy

XYZ=0 se ověří posunem inst<<40. Negative rX nastaví pouze next
address; pro rX≥0 jsou přijaty ropcodes 0…2. Bitová maska #70cf
má právě bity 0,1,2,3,6,7,c,d,e, tedy povolené vedoucí číslice
pro ropcode1. Extrakce `(rX>>13)&(8*255)` dává 8X a dvojice
porovnání vyloučí marginal X pro ropcodes1/2. Byte opcode se
kontroluje proti #f9. NEG+CSNN vytvoří z ropcodes0,1,2 stav1,−1,−2.

Ropcode2 vymění f za host `ORI x,z,0` s dest flag a cenou υ,
Q vybere MOR maskou #20 z třetího byte zleva. Potom XDest a Done
zapíší rZ a zpracuji požadované Q. Ropcode0 použije běžnou instalaci.

Ropcode1 je **prokazatelně chybné**: C0015 ukazuje ADDU 102 místo3.
Převzít jeho úplný krátký důkaz. Správný obecný převod všech povolených
instrukcí (zejména immediate Y a implicitních operandů) nebyl vytvořen;
úloha tedy zůstává partial i po potvrzení konkrétního selhání.
V0177 lze uzavřít pouze pro řízení stavu mimo tuto chybu; úplná
RESUME/OS závislost V0071 zůstává otevřená.


### Obnova7.11.2026: úplná úloha14

Dřívější partial úplné opravy14 je nahrazeno `exercises-1.4.3-014-recovery.md`: všech144 opcodes, všechny Q, konkrétní patch a27nových prvních případů. Nové nezávislé omezení ropcode2 máC0023. Ostatní uvedené partial se tím neuzavírají.


### Obnova7.11.2026: celé12/13

Partial12 pro malformedobrazy je odvolané podle skutečného kontraktu; `exercises-1.4.3-012-recovery.md` řeší validní inverse a skutečnou counter/bootstrap povinnost. Partial13 pro LDSF je vyřešené normativním no-exception pravidlem. Celý helper má argument v `exercises-1.4.3-013-recovery.md`; samostatný storekontrakt širšíhoMMIX zůstává R0009/V0070partial.

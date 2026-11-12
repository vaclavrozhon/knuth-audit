# Korutiny: úplné samostatné kontexty a obrácený překladač

7. listopadu2026. Zadání6/7 na file81/p73, odpověď6 na
file124/p116. Pro7 není vytištěný hotový program. Dřívější
`exercises-1.4.2-001-007.md` správně ponechával obě úlohy partial;
níže jsou doplněny právě chybějící konstrukce, ne nový SAVE inverse.

## 6. Společný zásobník: přesná podmínka rozhraní

Při běžné GO vazbě se nesmí předpokládat, že proběhlo přejmenování
lokálů: není tomu tak. Má-li A při předání určitý aktivní logický
rámec, B jej musí při návratu do A zanechat se stejným rO,
počtem a hodnotami přístupných lokálů i stejnou logickou
posloupností dosud nepopped položek. Přesun položek mezi fyzickým
ringem a backing memory není porušením této podmínky; rS nemusí
být bitově stejné. Jde o správné obnovení A podle jeho rozhraní,
nikoli o obecný zákaz libovolného používání sdíleného stavu.

Řádně vnořené PUSH/POP páry B tuto podmínku splní podle
přijatého obecného důkazu PUSH/POP. Indukce podle hloubky
vnoření chrání prefix A a každý vložený marker se odstraní
právě svým POP. B musí navíc respektovat sdílené current
locals/globals deklarované rozhraním; samotná návratová adresa
GO žádné registry nechrání. Při přechodu do A s neukončeným
nezávislým rámcem B by A četlo jiné přejmenované lokály a jeho
POP by četlo cizí marker. To je konkrétní důvod nebezpečí.
Speciální protokol dovolující A v této době pracovat jen se
sdílenými globals a nejprve vrátit řízení B je možný, ale
nedává dvě nezávislá soukromá call-stack rozhraní.

## 6. Dva nezávislé kontexty: celý přepínací protokol

Předpoklady: dvě disjunktní platné stack oblasti, stejné
G≥32 a tyto odlišné **rezervované globální** role: who,
ss,tmp,$255. Hodnoty who jsou adresy deskriptorů DA/DB v
trvalé sdílené paměti mimo oba zásobníky. Každý deskriptor
má dvě octa: na0 poslední saved-context pointer a na8
adresu druhého deskriptoru. $255 je deklarovaný scratch/link,
nikoli živý soukromý aplikační údaj. Ostatní globals, lokály,
rJ a ukládané specials patří právě aktivnímu kontextu.

Každá korutina předá řízení instrukcí GO $255,Switch.
Switch má celé následující tělo:

```text
Switch  SAVE   ss,0
        STO    ss,who,0
        LDO    tmp,who,8
        LDO    ss,tmp,0
        UNSAVE 0,ss
        GO     $255,$255,0
```

Vstupní GO uloží do $255 přesně continuation aktuální
korutiny. SAVE má globální destinaci ss; přijatý důkaz
ukládá **původní** hodnoty všech globals včetně $255 a who,
všechny lokály a příslušné specials, a teprve pak přepíše
ss vrcholovým pointerem. První STO proto uloží správný
pointer do vlastního DA neboDB. Who se při SAVE nemění.
Obě LDO používají sdílený deskriptor a vyzvednou dosud
nepoužitý validní image druhé korutiny.

Mezi SAVE a UNSAVE se pracuje jen s globals a deskriptory;
L zůstává0, takže nový prázdný stack nepřepisuje právě
uložený image. Cílový image leží v jiné stack oblasti.
UNSAVE obnoví přesně jeho původní locals, globals, rJ,
specials a logický zásobník. Obnoví také who cílové korutiny
a její uložené $255, tedy její continuation. Poslední
GO $255,$255,0 používá starý zdroj jako cíl; jeho nový
link zůstává jen v deklarovaném scratch $255. Žádný
registrový či paměťový pointer potřebný po UNSAVE nebyl
ponechán pouze v přepsaném ss/tmp.

Indukce přes předání: neaktivní deskriptor obsahuje validní
nepoužitý image; aktivní tělo má přesně svůj soukromý rámec
a při příštím předání vytvoří nový image a přepíše svůj
deskriptor. Starý image se po UNSAVE **znovu nepoužije**.
To respektuje destruktivnost UNSAVE. Všechny starší aktivní
aplikační rámce mohou být součástí image, takže B nemusí
svá vnořená volání před návratem A ukončit. Stack oblasti
musí pojmout skutečnou hloubku i image; konečná paměť není
prohlášena za neomezenou. Přerušení může být dovoleno pouze
s běžnou architekturní obnovou kontextu; vlastní nesprávný
OS handler není tímto protokolem opraven.

**Inicializace není skrytá.** První image má L0 a žádné
starší pushed rámce. Z přijatého SAVE formátu jde o
marker0, globalsG…255,12 specials a packed(G,A), celkem
270−G octa. Jeho who je vlastní DA/DB a $255 požadovaný
první vstup. Takové počáteční kontexty lze sestavit stejným
bootstrap principem jako MMIX loader, který podle primární
MMIX-DOC2761–2767 používá UNSAVE i k inicializaci rO/rS.
Konkrétní existence bez závislosti na starých rámci: platný
L0 template se může zkopírovat do druhé disjunktní oblasti;
změní se jen dvě deklarované globální hodnoty who a $255.
Image pak má přesně hodnoty, které by SAVE vyprodukovalo
z prázdného kontextu s těmito globals na této bázi. V uloženém
L0 stacku nejsou vnitřní návratové markery ani uložené stack
adresy, které by vyžadovaly další relokaci. Aplikační data
jsou buď společná, nebo jejich globals musí být rovněž
inicializovány podle rozhraní. Použije se již prokázaná inverse
pro tento validní layout, nikoli neprokázaná sémantika
libovolného poškozeného image či headeruG<32.

Nominální přenos stojí caller GO3υ, SAVE20μ+υ,
STO/LDO/LDO3μ+3υ, UNSAVE20μ+υ a závěrečné GO3υ,
tedy **43μ+11υ**. Skutečná práce kopírování závisí na
velikosti kontextu; tabulková konstanta20μ ji nevyjadřuje.
Tato konstrukce a její invariant uzavírají přesně dodatek
„with care“ v odpovědi6. Žádný SAVE/UNSAVE test nebyl opakován.

## 7. Doména a úplný důkaz nejkratšího kódu

Vstup je konečný soubor skupin znaků, z něhož se ignorují
všechny bytes≤32, až po první period. Před ní jsou pouze
bytes33…255 jiné než period. Formát přicházející z původního
překladače je podmnožinou tohoto oboru. Vstupní i výstupní
I/O musí plnit svůj explicitní trap kontrakt. Při předčasném
EOF či I/O error program skončíHalt1, neoznačí částečný
výstup za dokončený. Každý výstupní token má vlastní newline;
úloha newlines výslovně nezapočítává do minimální délky.

Po odstranění whitespace má každý token kódu buď jeden
nondigit c, nebo dva znaky(n,c), kde n je číslice0…9
a vyprodukuje n+1 kopií c. Jeden token nemůže pokrýt dvě
různé hodnoty sousedních maximálních běhů; globální optimum
je proto součtem optim jednotlivých běhů a konečné period.
Ignorovaný ne-newline whitespace by délku jen zvětšil.

Pro nondigit běh délky l=10q+r,0≤r<10, a dvojznakových
tokenů a a literálů s platí l≤10a+s a cena2a+s.
Je-li a≤q, cena≥l−8a≥2q+r. Je-li a≥q+1, cena≥2q+2.
Každý kód tedy stojí alespoň **2q+min(r,2)**. q tokenů9c
a zbytek jako c pro r1 či(r−1)c pro r2…9 tuto mez dosahují.
Pro r0 není zbytek. To pokrývá i l1,9,10,11 a násobky10.

Digit nelze vydat jednoznakovým tokenem, takže každý token
stojí2 a produkuje nejvýše10 znaků. Nutná a dosažitelná
cena je **2 ceil(l/10)**, včetně jednoho digit c kódovaného0c.
Period lze přidat jako jediný literál. Prefix před period
by pouze přidal znak, protože první vyprodukovaná period
výstup ukončí. Celková dolní mez je proto dosažena běh po
běhu; nejde jen o lokálně neprokázanou greedy heuristiku.

## 7. Každý stav nového MMIX programu

Celý zdroj: `sources/coroutine7-inverse.mms`. Čtyři konstantní
globals DataBase,One,TwoBuf,ReadArgs jsou odlišné. Paměť má
24 bajtů: RawByte naD, buffer One naD+1 délky3, TwoBuf naD+4
délky4, dvojice argumentů Fread naD+8/D+16. RawByte je
**adresní label**, nikoli číslo global registru. Obě délky
řetězců mají explicitní newline aNUL; nulová paměť za nimi
není předpokladem výstupu. Kód a data jsou disjunktní.

ReadChar žádá přesně jeden byte pomocí Fread. Návrat0
znamená uložený byte; −1 je žádný byte/EOF, −2 serious
error. BNZ proto pokryje obě chybové větve. LDBU vrátí
0…255, CMPU/BNP přeskočí každou hodnotu≤32 **včetně NUL**.
Nezaměňuje se obsah dat s koncem bufferu. Pro platný vstup
dojde po konečném počtu whitespace k dalšímu významnému
bytu; POP1 jej vrátí do caller2. Velikost1 se vejde do
každého použitého hostitelského signed32 parametru.

Main používá0=znak běhu,1=počet,2=nový znak,3=test.
Na vstupu do Read platí0≤count≤9; již vydaný prefix má
optimální kód dokončených běhů a plných desítek, zbývajících
count kopií cur je zatím nevydaný suffix přečteného vstupu.
Při count0 se cur ještě nemusí používat. Nový nenulový znak
založí count1. Shodný zvýší count o1; přesně při10 se
vydá9cur a count se vrátí0. Odlišný znak nejprve vydá
starý zbytek a založí nový běh. Period nejprve vydá případný
zbytek a poté jediný period token; další bajty se již nečtou.
Každá větev udržuje invariant. Count nikdy nepřesáhne10,
adresa dat se dynamicky nezvyšuje a žádný registr nedrží
celkovou neomezenou délku vstupu. Ukončení plyne z konečné
pozice první period, při úspěšném I/O.

EmitRun přijímá count1…10 a c33…255; period jen s count1.
Při count≥2 volí dvouznakový token. Při count1 spočítá
c−'0' a porovná jej **unsigned** s9: pro c<'0' je výsledek
mod2^64 velký, takže jen skutečné48…57 vyberou prefix0.
Ostatní count1 jsou literál. Prefixcount+47 leží48…57,
STBU ukládá přesně správné byty. One se mění jen v prvním
bytu; TwoBuf jen v prvních dvou, proto se newline/NUL
nikdy nezničí. Fputs vidí celý jeden token s newline.
Záporný výsledek jde naHalt1; běžná větev POP0 vrací.

Read používá PUSHJ2 a chrání main0/1. Emit používá PUSHJ4
a argumenty5/6, takže chrání0…3 včetně **nově přečteného
znaku2** při ukončení předchozího běhu. Po POP0 se tento
znak neztratí. Oba helpery jsou listy, rJ nepřepisují;
I/O trap jej vrátí podle své deklarace. Nejvýše je třeba
8 logických stack položek:5 od PUSHJ4 včetně markeru a
3 lokály EmitRun. G≥32 všechna čísla dovoluje; skutečné
čtyři GREG dajíG251. Maximum hodnot i paměti je konstantní
nezávisle na délce běhů. Čas je lineární v počtu přečtených
bytů plus výstupu, s explicitními I/O předpoklady.

## 7. Přesné nominální náklady

R je počet skutečně přečtených bytů do první period,
W počet whitespace, N=R−W významných znaků včetně period.
Z je počet založení běhu při count0, D počet změn znaku
vyžadujících vydání starého zbytku, S počet shodných
následných znaků, F počet dokončených desítek a H∈{0,1}
indikátor zbytku při period. T=D+F+H+1 je počet tokenů
včetně period, L počet jednoznakových tokenů a U počet
tokenů tvořených samotným digit cíle, tedy prefix0+c.

Read stojí12υ za whitespace,14υ za významný znak včetně
caller PUSHJ a POP; každý byte navíc jedenμ. Emit stojí
17υ a1μ pro literál,20υ a2μ pro count1 digit,17υ a2μ
pro delší běh. Rozdíly zahrnují všechny vzaté obyčejné
větve a poslední netaken PBNZ u desítky. Celý zbytek Main
stojí(2N+6Z+9D+8S+7F+H+15)υ. Včetně všech volání,
inicializace aHalt je tedy přesně

**(R+2T−L)μ + (12W+16N+6Z+9D+8S+7F+H+15+17T+3U)υ**.

Tato formule nezapočítává nevykázaný čas hostitelského
streamu jako strojové instrukce. Všechny použité konstanty
jsou z deklarovaného nominálního MMIX modelu.

## První nové běhy a jejich přesný rozsah

`verify_coroutine7_inverse.py` sestavil tento nový zdroj
a každý ze tří cílených souborů provedl **poprvé jednou**.
Všechny výstupní byty, přímé dekódování, obecná minimální
délka i přesná cena souhlasily hned při prvním úspěšném
build/run. Žádný starý překladač ani úspěšný test se neopakoval.

| Vstup | Minimální délka bez LF | Instrukcí | μ | υ |
|---|---:|---:|---:|---:|
|samotná period|1|28|2|48|
|celý příklad knihy(2)|24|954|78|1450|
|všechny whitespace0…32, délky1/9/10/11/21, digits a byte255|24|4210|556|7678|

Poslední případ má532 skutečně přečtených bytů,448 whitespace
a84 významných znaků; data za period zůstala nepřečtena.
Testy používají MMIX-SIM `-f` s místním vstupním souborem,
tedy doloženou běžnou fread větev. Interaktivní terminálové
bufferování `stdin_chr` se nevydává za tentýž hostitelský
mechanismus. Celý nový build a tři první běhy trvaly1.4333s
při nice15. Evidence je v `results/coroutine7-inverse-program.json`,
`coroutine7-inverse-build-and-run.json`, listingu a původních
binárních vstupech/výstupech/profilech. Neopakovat.

Obě dřívější úlohy6/7 jsou nyní argument_recorded. Obecný
důkaz SAVE inverse byl pouze použit, nikoli znovu spuštěn;
optimální kódování má dolní mez pro celý obor a plný program,
nikoli jen několik úspěšných příkladů. Vzory: přesná doména
a hranice jako binomická nerovnost, všechny nákladové větve
jako Algorithm R a oddělení kontraktu, implementace a
samostatných programových vad jako kografový rozbor.

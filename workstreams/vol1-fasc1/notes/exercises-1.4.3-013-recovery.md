# MMIX — §1.4.3′–13: celý trip helper a oddělený store kontrakt

## Přípustné vstupy a všechny větve517–538

Na vstupu z516 je t=E&exc nenulový byte, E enable byte aa;
exc už prošlo doloženým pravidlem U/X. Všechny ostatní bity
jsou nulové. h=8−floor(log2(t)) je celé číslo1…8. Po počátečním
posunu55 a j průchodech smyčkou je nejvyšší jednička na pozici
floor(log2(t))+55+j. Právě při j=h poprvé dosáhne bitu63,
PBNN přestane větvit a xx=h. Žádný dřívější bit nesmí být
odříznut: nejvyšší pozice je do posledního průchodu nejvýše63.
Tím se smyčka vždy ukončí nejpozději za8 průchodů.

`#100>>h` je právě nejvyšší enable-event bit. ANDN odstraní
jen tento obsloužený event; nižší současné enabled i disabled
events se nadále zaznamenají do aa na539. Hostitelské staré
sticky eventy jsou před operací vynulované a nesmějí vyvolat
další trip; úplný důkaz Done/underflow je v087–097.
xx<<4 dává přesně adresy#10…#80. Explicitní TRIP vstupuje
s xx0 přímo doTakeTrip a vybírá#00, exc zůstává0.

Před začátkem TakeTrip ukazuje inst_ptr na následující
instrukci (pro vložený příkaz na rW). STOU jej zachová v g[rW]
ještě před nastavením cílové adresy. inst má pouze32bit slovo;
INCH#8000 proto přidá přesně2^63 bez jakéhokoli přenosu.
g[rX] má horní polovinu#80000000 a původní dolní instrukci.
Nejde o tvrzení, že se vždy rovná obsahu paměti na rW−4:
vložená instrukce smí být jiná.

Poslední dva load/store páry nejprve uloží původní global$255
do rB, potom zkopírují virtuální rJ do$255. Protože G≤255,
$255 je vždyglobal. Operandy y,z se získaly před touto změnou,
takže případné Y255 či Z255 zachovají původní vstup. Fyzické
hostitelské rJ pomocných volání je jiný stav než g[rJ].
Explicitní TRIP může mít libovolná XYZ: Info používá zdrojové
Y/Z, nemá cílX a žádná jiná služba se zde nevybírá.

## Proč Mem_bit nemůže omylem zachytit floating load

Původní partial z§13 byl konkrétně možný LDSF signalingNaN
trip. Normativní `mmix-doc-20131017.w`1511–1517 říká výslovně,
že **žádný LDSF nevyvolá aritmetickou výjimku**, ani signalingNaN.
Přebírá se úplný2^32 bitový konverzní důkaz
`fp-conversions-recovery.md`§3; nejde o nový vzorkový test.

Ostatní loads jsou bitové načtení/sign extension; CSWAP má
pouze porovnání a výměnu; addressADD je unsigned. Žádná
z těchto cest nemá arithmetic event. Signovaný STO rovněž
ukládá celé64bit bez ztráty; unsigned stores, STHT/STCO/STUNC
žádnou aritmetickou výjimku nevyvolají. Interní přípravné
hostitelské operace nemohou přidat starý event, protože rA se
před delegovanou instrukcí znovu nastaví.

Mem_bit je tedy na skutečné arithmetic-trip cestě1 pouze
pro signed STB/STW/STT a STSF. U těchto instrukcí zůstane
pracovní x původním virtuálním$X, neboť store zdrojový
registr nemění. y,z stále obsahují původní address operandy.
Řádky531/532 vypočtou A=(y+z)mod2^64 a z=x. Ropcode2 má
nové ORI f s Mem_bit0, takže tuto větev neprojde ani tehdy,
když jeho zahazovaný původní opcode vypadá jako store.

U nonstore se uloží skutečná připravená y,z. C0003 už
vyvrátil chybné zobecnění p.18, které u NEG psalo `$Y`
namísto immediateY. Knižní helper v této věci správný je.
Vyjma přesného nižšího store problému se tudíž nevyžaduje
další implementace hypotetického hardwaru.

## Celé deklarované náklady

Od517 kTakeTrip je2υ přípravy,3h+2υ smyčky (poslední
nevzatý pravděpodobný skok stojí3υ) a3υ výběru/odebrání
bitu, celkem(3h+7)υ. Samotné TakeTrip525–538 má8mem
operací. Nonmemory cesta stojí8μ+12υ; store cesta má
nevzatýPBZ navíc2υ aADDU/SET2υ, tedy8μ+16υ.
Celý arithmetic helper proto stojí8μ+(3h+19)υ, respektive
8μ+(3h+23)υ. Explicitní TRIP vstup přidáSETxx/JMP2υ
ke společné nonmemory cestě, tedy8μ+14υ. Tyto ceny končí
na538 a nezahrnují539 ani common Update; žádný host benchmark
se nevydává za obecný časový důkaz.

## MMIX-R0009: knižní store pravidlo versus širší primární specifikace

Samotná úloha13 má podle **výslovného knižního store pravidla
p.18** celou implementaci doloženou: rY=A, rZ=původní$X.
Není správné ji nadále držet partial kvůli již vyřešenému LDSF
nebo kvůli požadavku na nevytištěnou obecnou realizaci hardwaru.
E13 proto dostává argument_recorded v tomto přesném rozsahu.

Zůstává však **jiné konkrétní tvrzení**, totiž obecnost tohoto
store pravidla jako definice MMIX. MMIX-doc2115–2128 žádá
rZ jako celý výsledný octabyte paměti, včetně nezměněných
bajtů. `sources/mmix-pipe-20250620-store-trip-excerpts.txt`
dokládá merge nového pole do data->x.o a následné předání
tohoto x do rZ. Knižní helper i C MMIX-SIM používají raw$X.
C simulátor navíc pracuje v tomto místě s w zaokrouhleným
na octabyte, zatímco kniha i slovní definice používají A.

Nejmenší přesný rozdíl v hodnotě: A=D=2^61, všechny8bytů
M[D] nulové, $X=256 a enabledV. Signed STB uloží nízký
byte0 a vyvolá V. Kniha i C simulátor zachytí rZ256;
širší dokumentace a pipeline merge dávají rZ0. Zvolili jsme
zarovnané A, takže tento svědek nezávisí na druhém adresním
rozdílu. Konečný platný store je v user data segmentu a
žádná FP otázka se ho netýká.

To není nový experiment, ale přímé porovnání tří úplných
větví. Zda má být vytištěná knižní věta výslovně omezená na
autorův jednoduchý model, nebo opravena podle širšího MMIX-doc,
zatím není autoritativně rozhodnuto. Nevytváříme proto další
confirmed kartu. R0009 je přesná interpretace primárních
kontraktů, nikoli chybějící důkaz implementace pro hypotetický
hardware. V0070 a celá26 se znovu otevírají: přijatý NEG
protipříklad pokrývá jinou část souvětí a nemůže uzavřít
samostatnou store klauzuli. Totéž omezení je viditelné u97/130.

## Převzetí a standard obnovy

Originál130 byl nově zobrazen, původní26 je v
`images/file-026-p018.png`. Všechny řádky517–538 a skutečné
obě store větve primárních zdrojů byly přečteny; nový běh
není potřebný. Dřívější úspěšné arithmetic/C0003 kontroly se
neopakují. Vzory1/4B jsou použity na všechny priority a mezní
posuny, každou load/store kategorii, přesné ceny a oddělení
splněné knižní algoritmické povinnosti od samostatné rozporné
normativní věty. Nalezení další mezery znamená její otevření,
nikoli ponechání staré zelené stránky.

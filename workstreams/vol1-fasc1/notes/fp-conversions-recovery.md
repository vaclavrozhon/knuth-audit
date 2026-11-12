# V0054–V0055: konverze a zaokrouhlování, úplné dílčí argumenty

6. listopadu 2026. Navazuje na `fp-comparisons-recovery.md`, nikoli na
předpoklad správnosti celé knihovny. Vstupem do instrukce je libovolné
64bitové slovo, případně libovolný tetrabyte LDSF; stav má platné rA a
Y∈{0,1,2,3,4} u instrukcí s volbou režimu. Y=0 přebírá rA, Y>4 je
neplatná instrukce a nevstupuje do důkazu platné konverze. Zdroje jsou
`mmix-arith-{20131017,20250620}.w`, §31–40, §86–90; dispatcher
`mmix-sim-20131017.w:2018–2033,2143–2144,2160–2162,2586–2592`.
Používají se 32bitové unsigned `tetra` a 64bitové dvojice; kontrolní
driver to staticky ověřuje. Závěry o hodnotách nepředpokládají hostitelské
floating operace ani IEEE chování procesoru, na kterém běží C.

## 1. Zaokrouhlovací invariant se dvěma spodními bity

Pro nezáporné reálné t definujme J(t)=floor(t) s nejnižším bitem
nastaveným na 1, je-li t necelé. Rozepišme t=4q+r, 0≤r<4. Potom
J(t)=4q+j, kde

| Přesný zbytek | j | Význam pro zaokrouhlení t/4 |
|---|---:|---|
| r=0 | 0 | přesný integer q |
| 0<r<2 | 1 | pod půlkou, nenulová chyba |
| r=2 | 2 | přesná půlka |
| 2<r<4 | 3 | nad půlkou |

Tato tabulka plyne přímo z floor(r)∈{0,1,2,3} a případného OR s 1.
Proto `o&3` přesně detekuje inexact. OFF vrátí q; směr od nuly přidá
3 před dělením 4 a vrátí q+[r≠0]. Při NEAR se přidá 2 pro liché q,
jinak 1. Pro j=0/1 nevzniká přenos, pro j=3 vzniká vždy, pro j=2 právě
při lichém q. To je úplný důkaz všech čtyř režimů i obou znamének:
UP zvětšuje absolutní hodnotu jen u kladného čísla, DOWN jen u záporného.

Pravý posun s jamem je kompoziční: J(J(t)/2^k)=J(t/2^k), k≥0.
Horní bity totiž v obou postupech zůstávají stejné a spodní bit pouze
sděluje, zda je některý odhozený bit/tail nenulový. Nenulová informace
se ORem nemůže vymazat ani změnit nulu na jiný horní bit. To ospravedlňuje
opakované jednobitové posuny i pozdější zúžení na short bez dvojího
zaokrouhlení. **J není zaokrouhlení na nejbližší**; rozhodovací tabulka
se provede až jednou, na cílové přesnosti.

## 2. fpack a sfpack: hodnoty, meze, příznaky

Kontrakt rozbalené nenulové hodnoty je |x|=f·2^(e−1076), kde
2^54≤f≤2^55, popřípadě f obsahuje J-informaci o přesném konci mantisy.
Správnost takové informace je povinnost jednotlivého volajícího, nikoli
závěr tohoto lemmatu.

U fpack pro e≥0 a e≤2045 dává dělení 4 cílových 53 významných bitů.
Přičtení e·2^52 spojí exponent s implicitní vedoucí jedničkou, a případný
přenos 2^53 správně zvýší exponent. Při e<0 je cílový subnormální krok
2^−1074, proto se před týmž dělením 4 provede pravý posun o −e.
Pro −54≤e<0 se použije přesný posun s jamem. Pro e<−54 je přesná hodnota
menší než půlka nejmenšího subnormálu: f≤2^55 a e≤−55 dává
|x|≤2^−1076<2^−1075. Náhradní o=1 proto má správný j=1. Znaménko nuly
se připojí až na konci a je zachováno i při zániku nenulového čísla.

sfpack nejprve zvolí J(f/2^29), čímž zbudou 24 významných bitů a dva
rozhodovací bity. Výraz `(f<<3).h` je floor(f/2^29); test spodních
29 bitů dodá právě jam. Rozdíl biasů je 1023−127=896=#380. Pro e<896
je proto potřebný další posun 896−e. Větev e<871 může zvolit o=1:
ještě při maximálním f je přesná hodnota pod půlkou nejmenšího short
subnormálu. Jinak je posun v 1..25 a je proveden s jamem. Konečné
`(e−896)<<23` skládá exponent v binary32 stejně jako fpack.

Všechny posuny v C jsou přípustné: pomocné octa posuny rozdělují k na
32bitové části a nepoužijí nativní posun o 32; přímý tetra posun sfpack
má nejvýše 25. Po clampu jsou exponentové příspěvky nezáporné a pod
2^31. Mezivýsledky zaokrouhlení jsou nejvýše 2^55+3 nebo 2^26+3;
nedojde k unsigned přetečení úložného typu.

Pro konečný výsledek je X právě z j≠0. U indikuje tiny výsledek,
včetně nuly vzniklé z nenulového vstupu; dispatcher potlačí samotné U,
pokud je výsledek exact a U-trip není zapnut. Mez short tininess je
2^23=#800000. Verze 2013 měla #100000; tato **známá** vada je opravena
v autorově verzi 2025 a není zde samostatným nálezem.

Pro přetečení oba původní packery správně zjistí O|X, ale vždy vracejí
nekonečno. Tím selhávají tři directed/sign kombinace; samostatný rozpor
MMIX-S0002 a jeho přesný architektonický kontrakt jsou v sousedních
poznámkách. Auditní oprava po detekci O vybere největší konečnou absolutní
hodnotu právě pro OFF, UP záporného výsledku a DOWN kladného výsledku.
O|X zůstává. Ostatní výsledky i všechny ne-overflow větve jsou totožné.
Obě cesty k O jsou pokryty: velký vstupní exponent i carry z mantisy.
Při O je neznaménkový starý výsledek vždy přesně +∞, nikoli NaN:
velká exponentová větev má o=0 a carry může dosáhnout jen jediné další
mocniny dvou. Volba konečné meze/∞ podle znaménka a režimu je tedy úplná
a konečné větve výše se nemění. Dokazuje se hodnota při vypnutých tripech;
libovolné handlery a exponent dodávaný při zapnutém IEEE trapu nejsou
uzavřeny touto opravou.

## 3. sfunpack a LDSF: všech 2^32 vzorů

Má-li short normál exponent E∈[1,254] a fraction F<2^23, sfunpack dává
f=(2^23+F)2^31, e=E+895 a stejné znaménko. Invariant dává hodnotu
(2^23+F)2^(E−150), přesně definici binary32. Pro subnormál začne
f=F2^31. Po t levých posunech, t=23−floor(log2 F)∈[1,23], má
f=F2^(31+t), e=896−t; součin je F2^−149. Každým posunem se vedoucí
jednička přiblíží o jednu pozici; poslední f∈[2^54,2^55), takže smyčka
končí a žádné bity se neztratí. Nula, infinity a NaN jsou z disjunktních
polí E/F rozlišeny jako v binary64, se znaménkem zachovaným.

Všechny nenulové konečné short hodnoty se v binary64 vejdou přesně:
mají nejvýše 24 významných bitů, exponent v [−149,127], a jsou normální
binary64. fpack proto v LDSF nic nezaokrouhluje ani nepřidá příznak.
Pro normal short má výsledný exponent E+896∈[897,1150]; pro subnormal
je v [874,896]. Tím jsou zahrnuty nejmenší i největší hranice.

Nuly se zkopírují se znaménkem. Infinity se zmapuje na stejné znaménko
binary64 infinity. U NaN se payload posune o 29 bitů vlevo; quiet/signaling
bit se nezmění, protože je stále nejvyšším bitem fraction. Sign se připojí
zvlášť. Žádné volání nevynutí I, což je výslovný kontrakt LDSF.
Dispatcher nepřebírá žádné arithmetic exceptions z LDSF; přesná pomocná
rutina je beztak nulové vrací. Paměťová adresa má už dříve dokázanou
modulární a tetrabytovou sémantiku; předpokládá se povolené čtení.

## 4. FLOT, FLOTU, SFLOT a SFLOTU: všechny vstupy a režimy

Vstup 0 vrací +0. U signed záporného raw slova se vezme jeho unsigned
velikost N=2^64−raw; i pro −2^63 je N přesně reprezentovatelné v octa.
Unsigned má N=raw. Tedy 1≤N≤2^64−1, signed velikost nejvýše 2^63.

`floatit` začne e=1076. Vlevo posouvá pouze při N<2^54; invariant
N_initial=f·2^(e−1076) je přesný a bitová délka roste o 1. Nejvýše
54 posunů končí ve správném intervalu. Pokud je počáteční N≥2^55,
pravá smyčka má invariant `f=J(N_initial/2^d), e=1076+d`; každý posun
o 1 s jamem jej zachová. Nejvýše 9 posunů odstraní nadbytečné horní bity
64bitového N. Obě smyčky na jednom vstupu nemohou být nenulové.
Na konci má e rozsah 1022..1085 a f interval [2^54,2^55).

FLOT/FLOTU pak přímo použijí jedno zaokrouhlení z oddílu 1 na binary64.
Výsledek je v konečném normálním rozsahu 1..2^64, žádné O/U/I nevzniká;
X vznikne právě tehdy, když výsledek není N. Připojení znaménka dává
správný signed výsledek i v directed režimech.

SFLOT/SFLOTU použijí sfpack, tedy stejné nezaokrouhlené N s 24bitovou
přesností. I 2^64 je daleko pod mezí binary32, takže O/U/I nevzniká.
Případné X se uloží do ex, protože sfunpack by je jinak vymazalo.
Přesné rozbalení a fpack neprovedou další zaokrouhlení a uložené X
zůstane. To dokazuje požadované anonymní T a jeho následné bezeztrátové
rozšíření, nikoli neplatnou cestu binary64-round → binary32-round.
Immediate varianty mají N∈[0,255], přesně reprezentovatelné už s 24 bity,
tedy stejný důkaz s nulovým X. Zahrnuty jsou všechny čtyři operace,
jejich immediate varianty, čtyři režimy a Y=0 jako volba rA.

## 5. FINT: úplný důkaz hodnot, oddělený příznak X

Nula se vrátí v původních bitech a zachová znaménko; ±∞ a qNaN také.
sNaN se quietuje nastavením bitu 2^51 a nastaví se právě I. To jsou
všechny nečíselné větve `fintegerize`.

Pro nenulové konečné z má funpack f·2^(e−1076)=|z|. Je-li e≥1074,
číslo je celé: f je násobek 4, a krok f2^(e−1076) je celočíselný.
Vrací se přesné z beze změny. Je-li e≤1020, je 0<|z|<1/2; náhradní
xf=1 je podle tabulky správný guard/sticky vzor pro zaokrouhlení na celé.
V ostatních případech e∈[1021,1073] a xf=J(f/2^(1074−e))=J(4|z|).
Oddíl 1 proto přesně dokazuje všechna zaokrouhlení na celé číslo.

Po zaokrouhlení se dva dolní bity vynulují; xf=4|n|. Pro e≥1022 je
|z|≥1 a vybraný integer má velikost alespoň 1. Normalizace se nezmění
nebo vzroste o jediný carry; `xf<<(1074−e)` je proto v [2^54,2^55].
Přesné zabalení s OFF vrátí n, bez nové chyby. Pro e≤1021 připadá
v úvahu jen velikost 0 nebo 1, přímo sestavená kódem. Vždy se připojí
původní znaménko, včetně −0. Žádný výsledek nemůže způsobit O nebo U.

**Samostatná povinnost uzavřena 6. listopadu:** kód při změně konečné
hodnoty nikde nenastaví X. Tuto skutečnost dokazuje průchod všemi
větvemi: funpack vymaže exceptions a všechna pozdější balení jsou přesná.
`MMIX-S0004-integerization-inexact.md` dokládá přesný normativní řetězec
IEEE 754-1985 §5.5→§4→§7.5 a jeho převzetí v MMIX. Pozdější varianty
round-to-integral se nepodsouvají. Původní program má chybějící X;
samostatný úplný důkaz auditní opravy používá test xf.l&3 před rounding.
Výsledkové tvrzení tohoto oddílu není prohlášení celé IEEE shody.

## 6. FIX a FIXU: hodnota a všechny explicitní I/W větve

Pro NaN nebo ±∞ vrací fixit **původní bity** a nastaví I; signaling
NaN se zde nequietuje. To odpovídá výslovnému MMIX pravidlu FIX.
Obě signed nuly vracejí integer 0. Pro konečné nenulové z se vezme
n z předchozího oddílu. Je-li n=0, výsledek je integer 0.

Po rozbalení n je |n|=f2^(e−1076) s e≥1022. Pro e≤1076 dává přesný
pravý posun integer o=|n|; velikost je pod 2^55, a proto v signed rozsahu.
Pro 1076<e≤1084 dává levý posun rovněž velikost pod 2^63.
Pro e=1085 je velikost v [2^63,2^64); jediná signed přípustná možnost
je −2^63, přesně f=2^54 a záporné znaménko. Kód tento jediný případ
rozlišuje testy obou polovin f a znaménka; ve všech ostatních nastaví W.
Pro e>1085 musí být W vždy, protože velikost je alespoň 2^64.

Levý posun počítá zbytek modulo 2^64. Je-li e≥1140, posun má nejméně
64 a zbytek je nutně 0, což odpovídá přímému návratu. Pro menší e
jej vypočte pomocná octa rutina; záporné znaménko provede modular
negaci. Tím je pro všechna konečná z dokázáno `n mod 2^64`, včetně
velmi velkých normalů a obou signed hranic. FIXU v dispatcheru pouze
odstraní W; zachová hodnotu a I, přesně jako specifikace.

Druhé funpack uvnitř fixit maže příznaky integerizace. Současný
fintegerize pro konečné z nepřidává X. Samostatná normativní vazba FIX
na IEEE §5.4 a MMIX FINT, i úplný důkaz zachování X přes druhý funpack
včetně nulového návratu, jsou nyní v `MMIX-S0004-integerization-inexact.md`.
Z opravy FINT samotné by oprava FIX neplynula. FIXU potlačuje pouze W.

## 7. STSF: všechny typy, s oddělenou chybou overflow

Nula a ±∞ se přenesou se stejným znaménkem, bez arithmetic výjimek.
NaN se rozbalí, sNaN nastaví I a quiet bit; payload se pak zkrátí o
29 spodních bitů. Quiet bit zaručuje, že výsledek není infinity ani když
by původní payload měl ostatní jedničky pouze v odhozeném konci.
qNaN nezpůsobí I. Pro všechny konečné nenulové vstupy je použito jediné
zaokrouhlení sfpack z oddílu 2. Subnormální a nulové výsledky mají
přesné U/X pravidlo se známou opravou roku 2025; directed overflow
původního programu je S0002. Proto plná implementace STSF zůstává
counterexample_recorded, její ne-overflow větve mají úplný argument.

## 8. Ukončení, náklady a význam krátkých kontrol

Nejdelší smyčky těchto konverzí jsou normalizace: funpack nejvýše 52,
sfunpack nejvýše 23 a floatit nejvýše 54 levých nebo 9 pravých posunů.
Zbytek je konečné větvení s uvedenými mezemi. FIX případně provede dvě
další rozbalení, ale žádná smyčka nemá datově neomezený počet kroků.
Nevyvozuje se tím cena stroje z počtu C operací. Tabulka 1 deklaruje
FINT/FIX/FIXU/FLOT/SFLOT jako 4υ, LDSF i STSF jako μ+1υ;
to je použitý architektonický model, nikoli nově naměřená rychlost.

Dvanáct cílených případů v `results/fp-conversion-boundary.json`
obsahuje pět svědků S0002, čtyři sousední/směrové kontroly a tři
konverzní kontroly. Očekávání jsou ručně odvozená: 2^64−1 se při NEAR
zaokrouhlí na 2^64; 2^24+1 je přesná short půlka mezi sudým 2^24 a
2^24+2; nejmenší short subnormál je přesně 2^−149. Tyto kontroly
ověřují reprodukci konkrétních cest a nikdy nenahrazují uvedené důkazy.
Oba originály mají pět neshod, auditní overflow oprava žádnou. Celkem
36 krátkých vyvolání aritmetického modulu při nice 15; žádný simulátor,
benchmark nebo plošný census. S0001 se znovu nespouštěl.

V0054–V0055 stále partial, ale původně otevřené aritmetické rekurence
a FINT/FIX příznaky již mají vlastní úplné argumenty v navazujících
poznámkách. Zbývají přesně vymezené IEEE závazky a epsilon specifikační
okraje, nikoli nově vymyšlená povinnost dokazovat libovolné uživatelské
handlery. Hotové podčásti jsou jednotlivě v `fp-verification-items.json`;
původní programové rozpory jsou oddělené od auditních oprav.

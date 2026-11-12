# §1.3.2′, úloha27 — celý Fibonacci program a přesná vazba na uložený výpočet

Zadání file55/p47, oba celé programy a výsledky file117/p109; původní
sazba zobrazena v `images/recovery-fibonacci-117.png`.
Celé `verify_fibonacci27.py` i `results/fibonacci27-exact.json` byly znovu
přečteny; přijatý malý běh se NEOPAKOVAL. Doplňuji jeho přesné pokrytí
vytištěného toku, mezní stavy a náklady. Nový nice15 statický výpočet
ověřil jen dvě celočíselná znaménka a několik koncových konstant,
`results/fibonacci27-recovery-static.json`; negeneroval znovu posloupnost.

## 1. Obě přesné identity a vstupní aritmetika

Pro φ=(1+√5)/2,ψ=(1−√5)/2 mají obě čísla rovnici x²=x+1.
Proto (φⁿ−ψⁿ)/√5 splňuje Fibonacciovu rekurenci a počátky0,1,
tedy se rovná F_n. Protože |ψ|<1 a1/√5<1/2, je F_n nejbližší celé
k φⁿ/√5 pro všechna n≥0, bez polovičního tie. Dále
F_n−φF_(n−1)=ψ^(n−1). Pro n≥3 je jeho absolutní hodnota nejvýše
ψ²=(3−√5)/2<1/2. Tím jsou obě citované identity samostatně doloženy.

Programy používají běžný počáteční režim round-to-nearest, zakázané
aritmetické tripy a nulu pro GREG bez explicitní hodnoty. Změna rA nebo
libovolný enabled handler není součástí tohoto běhu. Všechny FP operandy
jsou kladné normální hodnoty a výsledky nepřekročí2^49 před zastavením(a).
Nejde o zkoušku NaN, subnormal, overflow nebo ostatních zaokrouhlovacích
režimů. Dříve přijaté úplné důkazy výsledků FSQRT, FADD, FMUL, FDIV a
FIXU mají stejné podmínky; známý programový problém eventu X v S0004
nemění zde používané hodnoty při vypnutých tripech.

## 2. Co přesně ověřuje uložený racionální výpočet

`nearest_integer` dělí kladného čitatele jmenovatelem, porovná dvakrát
zbytek a v rovnosti volí sudé celé. `binary64` nejprve určí e tak, že
2^e≤x<2^(e+1); po škálování2^(52−e) právě toto celočíselné zaokrouhlení
vybere nejbližší53bitovou signifikandu. Výjimečný carry na2^53 představuje
správnou další mocninu2, nikoli chybu exponentu. V daném kladném normálním
rozsahu není potřeba subnormal či overflow větev.

FSQRT5 je odvozeno zvlášť: pro s₀=floor√(5·2^102) se porovná
5·2^104 s(2s₀+1)², tedy přesně čtverec středu dvou sousedních binary64
hodnot. Rovnost nenastane, protože√5 je iracionální. Uložený výsledek
má bity4001e3779b97f4a8, tj. s/2^51, s=#11e3779b97f4a8.
Součet s+2^51 je přesně53bitový p=#19e3779b97f4a8, takže ani FADD1
zde nepřidá zaokrouhlovací chybu. INCH #fff0 přičte −2^52 modulo2^64,
čímž sníží exponent právě o1. Vypočtené φ je p/2^52, bity3ff9e3779b97f4a8.

Přesná celočíselná znaménka jsou

    s²−5·2^102 = p²−p·2^52−2^104 = 2463618876616256 > 0.

Takže uložená odmocnina i φ jsou mírně NAD přesnými hodnotami.
Pro φ stačí monotonie x²−x−1 pro x>1. Neopírám znaménko o desetinný
výpis hostitelského floatu.

## 3. Program(a): každý stav a nejmenší chyba

Po inicializaci n=1,new=F₁=1,old=F₀=0 a acc je přesně zaokrouhlený
podíl vypočteného φ a vypočtené√5. Před iterací pro další index platí
new=F_(n−1),old=F_(n−2). ADDU a INCL vytvoří F_n a nový index;
CMPU s old testuje přetečení a SUBU old,new,old uloží F_(n−1).
FMUL vytvoří zaokrouhlený další člen approximation, FIXU jej zaokrouhlí
na celé, CMP/PBZ pokračuje iff výsledek je F_n.

Pro libovolná nezáporná a,b<2^64 je (a+b) mod2^64<a právě při carry;
při carry je výsledek rovněž<b. Vytištěný CMPU porovnává s dosavadním
old, zatímco převzatý integer checker(b) používá druhý sčítanec.
Tyto testy jsou tedy ekvivalentní; nedochází k záměně významu registrů.
V části(a) se carry před n71 nemůže stát, protože F71<2^49.

Racionální smyčka v přečteném checkeru provede přesně zaokrouhlené
násobení za každou vytištěnou iteraci a přeruší při první nerovnosti.
Předem samostatně kontroluje n=0 a1, které vytištěná smyčka netestuje.
Proto uložené first_floating_failure=71 znamená všechny n≤70, nikoli
pouze tři zobrazené okolní hodnoty. Hranice jsou přesně

| n | F_n | acc−F_n |
|---:|---:|---:|
|69|117669030460994|1/4|
|70|190392490709135|13/32|
|71|308061521170129|11/16|

FIXU tedy v71 dává F71+1. Jeho operand i výsledek jsou<2^49<2^63,
takže ani unsigned integer konverze neskrývá přetečení. CMP je+1,
PBZ se nevykoná, SET t,1 zachová hlášený výsledek a TRAP Halt ukončí.
Knižní „+.7“ je přípustné desetinné přiblížení11/16=.6875.

## 4. Program(b): přesné high/low, tie a overflow

Počátky n=2,old=new=1 jsou F₁,F₂. Smyčka nejdřív tvoří další Fibonacciho
číslo a otestuje carry, teprve poté mění old a testuje aproximaci.
K=#9e3779b97f4a7c16 je již přesně ověřená zaokrouhlená aproximace
2^64(φ−1) z důkazu C0001. Tato konstanta je správná i přes tamní
samostatnou chybu slovní formulace o prvních bitech.

MULU/GET vrací přesný rozklad old·K=hi·2^64+lo. ADDU hi,hi,old
vytvoří dolní celé přiblížení φ·old a hihi=hi+1 připraví horní.
CSN hi,lo,hihi testuje znaménkový bit lo, tedy zvolí horní hodnotu iff
lo≥2^63. Jde o zaokrouhlení poloviny nahoru, přesně tak, jak je v
přečteném checkeru. CMP proti new potřebuje pouze rovnost; signed
interpretace obou stejně kódovaných hodnot nad2^63 ji nemění.

Na skutečném průchodu žádná půlka nenastane. K má v₂(K)=1, takže
K·old≡2^63(mod2^64) iff old≡2^62(mod2^63). Poslední old je F92<2^63;
jediný možný pozitivní kandidát by byl2^62. Ale

    F90=2880067194370816120 < 2^62=4611686018427387904
       < F91=4660046610375530309 < F92=7540113804746346429.

Monotonie F_j od j2 vylučuje rovnost s jiným použitým old.
Všechny potřebné MULU produkty mají přesných128 bitů; hi+old a hihi
se do n93 vejdou do64 bitů, protože jsou nejvýše F93+1.

Převzatý checker má assert pro KAŽDÉ n3,...,93 a zapsaný poslední
úspěch F93=12200160415121876738. V94 je matematický součet
19740274219868223167>2^64 a jeho zabalená hodnota1293530146158671551
je menší než dosavadní old=F92 i new_before=F93. Vytištěný CMPU tedy
dá−1, BN skočí rovnou k Halt a žádná fixed-point aproximace pro94 se
neprovede. To dokládá přesně hlášení v knize: reprezentace přeteče
dříve, než do té doby selže aproximace. Nic se netvrdí o všech větších
matematických n mimo unsigned-octabyte doménu.

## 5. Úplný nominální čas

GREG/LOC deklarace nejsou vykonané instrukce. Použijeme tabulku1,
tedy FLOT/FADD/FMUL/FIXU4υ, FSQRT/FDIV40υ, MULU10υ, TRAP5υ a
správně/nesprávně predikované větve1/3υ. Žádná z obou smyček nemá
load ani store, tedy0mem; čas hostitelského ukončení není benchmark.

Program(a) má prolog4+40+4+4+1+40+1+1=95υ. Každý ze70 průchodů
n2...71 má základní15υ; poslední PBZ navíc2υ, SET t1 stojí1 a Halt5.
Celkem **1153υ**.

Program(b) má tři SET za3υ. Každý z91 úspěšných průchodů n3...93
stojí21υ (pět úvodních obyčejných instrukcí, MULU10 a šest následujících).
Overflow průchod94 má ADDU,INCL,CMPU,BN za1+1+1+3=6υ, Halt5υ.
Celkem **1925υ**. Neúčtují se nikdy nevykonané SUBU či násobení po
zjištěném přetečení; větev úspěšné nerovnosti by naopak obsahovala
SET t1, ale na tomto konkrétním běhu nebyla dosažena.

E27 je v celém zadaném rozsahu argument_recorded. Tento blok neuzavírá
celou file117: následují nedodaná Josephusova implementace a začátek30.
Vzor stavového důkazu vyžaduje správný operand CMPU, nákladový vzor
odděluje okamžik overflow od pozdějšího testu a vzor přesných mezí
nahrazuje desetinný odhad φ dvěma celočíselnými nerovnostmi.

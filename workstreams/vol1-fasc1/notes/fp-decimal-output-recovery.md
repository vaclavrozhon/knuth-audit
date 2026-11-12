# MMIX — úplný matematický rozbor print_float a jeho roundtrip vstupu

7. listopadu2026. Rozsah: celý `print_float`, MMIX-ARITH §§54–67,
zdroj967–1302, a přesný podrozsah scan_const, který přijímá jeho
výstup. Oba output oddíly2013/2025 jsou byteově stejné.
Nejde o úplnou IEEE desítkovou službu: výstup je nejkratší roundtrip
řetězec, vstup je nearest-only a exceptions nejsou přislíbené.
S0009 se týká mnohem delšího integer vstupu a zůstává samostatný.

Níže je důkaz aritmetického CWEB algoritmu v deklarovaném32bitovém
word modelu. Převzaté octa posuny jsou unsigned; unsigned rozdíl
převedený na int v bignum_dec má na použitém GCC hostu běžný signed
dvojkově doplňkový význam. Bitové masky při scan_const se chápou jako
32bitové vzory, včetně bitu31. **Nepřisuzuje se tím všem ISO C
implementacím definovaný význam výrazu `1<<31`.** Všechny zde použité
indexy a ostatní nově vymezené aritmetické meze jsou uvedeny níže.
Přenositelnost C ani obecný parserový obor se tím automaticky nezavírá.

## 1. Všechny vstupní třídy a skutečné intervaly

Znaménko se vytiskne nejprve a dále se pracuje s kladnou magnitudou.
Zero vrátí `0.`, infinity `Inf`; oba případy zachovají původní sign.
Canonical NaN s fraction F=2^51 vrátí `NaN`, rovněž se sign.
Zbývají konečná kladná čísla a NaN payloady1≤F<2^52, F≠2^51.

Označme E uložený exponent a F uloženou52bitovou fraction. Pro
F>0 program vytváří celá L,H a exponent e tak, že skutečné intervalové
hranice jsou L·2^(e−1076), H·2^(e−1076):

* Normální E∈[1,2046]: L=2^53+2F−1, H=L+2, e=E.
* Subnormální E=0: L=2F−1, H=L+2, e=1.
* NaN E=2047: L=2F−1, H=L+2, e=1023; interval se týká payload
  hodnoty F/2^52, nikoli řazení NaN jako reálného čísla.

U konečných F>0 jsou to přesně midpointy k sousedům; u NaN jsou
to midpointy payload mřížky. Oba konce patří k x právě při sudém F,
což je přesně `open=x.l&1`. Pro největší finite je horní otevřený
konec skutečná nearest overflow hranice, která již zaokrouhlí naInf.

Pro normální mocninu dvou F=0 program použije e=E−1,
L=2^54−1, H=2^54+2. Dolní krok sousedního binade je poloviční;
pro E≥2 jsou tyto uzavřené midpointy správné. **Pro E=1 je dolní
interval programu užší než skutečný roundtrip interval:** program
použije x−2^−1076 místo x−2^−1075. Horní konec x+2^−1075 je správný.
Užší interval je podmnožinou skutečného a obsahuje x, takže roundtrip
neohrožuje. Pro tvrzení nejkratšího zápisu musí být tento případ
ověřen zvlášť; viz §3. Není tiše pohlcen vzorovým argumentem pro
ostatní exponenty.

## 2. Multiprecizní invarianty a celé mezní indexy

Pro tisk je radix B=2^28 a hodnota pole je
Σ dat[i]·B^(37−i). Po uložení ve §63 platí přesně

    represented_value = L·2^(e−1076)

a obdobně pro H. Je-li k=floor((2112−e)/28), zbytek r∈[0,27],
tři uložené bloky jsou bity L ve slotech k−1,k,k+1 podle posunů
r+28,r,r−28. Protože L,H mají nejvýše55 bitů, jiné bloky jsou0.
Pro všechny skutečné e∈[0,2046] platí2≤k≤75, takže zapisované
indexy jsou1…76. Vektor dat[157] tedy bohatě stačí.

U tiny subnormálů může počáteční a ukazovat na nulový horní padding
(nejen na origin37, jak zjednodušuje slovní komentář). Platný obecný
invariant zde je: mimo[a,b] jsou logické nuly; b je poslední nenulový
slot a před a jsou nuly. Malá větev nevolá bignum_compare a nulový
horní padding jí nevadí. Když a dosáhne origin z vyššího indexu,
stane se to pouze nenulovým carry. Velká větev má počáteční L,H
normalizované bez tohoto paddingu; její compare tedy smí použít a.

`bignum_times_ten`: při průchodu odzadu je carry přesně horní část
již násobeného suffixu. Platí0≤carry≤9 a
10·(B−1)+9=10B−1<2^32, takže tetra nepřeteče. Nový digit je
výsledek modulo B a carry je quotient. Koncový přenos do a−1
zachová hodnotu10F. Jestliže poslední nenulový digit po násobení
zmizí, musel být B/2 a carry do předchozího slotu je5. Předchozí
výsledek10d+5 je lichý, a proto není0 modulo B: stačí zkrátit b
nejvýše ojednu. To zdůvodňuje konkrétní jediný `b--`.

Na tiskové cestě se nikdy nepíše dat[−1]. Ve velké větvi je
T nejvýše10^309 a každé přechodné10F,10G je nejvýše10T≤10^310.
Protože10^310<2^1036=B^37, jejich nejvyšší možný slot je alespoň1;
násobení může bezpečně zapsat dat[a−1]. V malé větvi jsou F,G
po odstranění integer digit menší než1 a před odstraněním menší
než10, tedy a≥37. Žádný netriviální dolní slot není větší než76.
Zvláštní reprezentace přesné nuly a=b=156 se používá pouze tam,
kde je nula výslovně ošetřena; případné násobení0 zapíše dat155=0
a nemůže překročit pole.

`bignum_compare`: normalizované nezero s menším a je větší. Při
stejném a rozhoduje první odlišný digit. Dojde-li nejprve konec g,
je zbytek f kladný právě když p<pp; dojde-li nejprve konec f, má g
ještě nenulový suffix. Současný konec vrací0. Nula s a156 je menší
než všechny zdejší nenuly. Tím jsou všechny return větve pokryty.

`bignum_dec`: nejprve se doplní implicitní dolní nuly f až k b(g).
Průchod od nejnižšího digit udržuje invariant rozdílu zpracovaného
suffixu s borrow∈{0,1}. Pro radix2^28 i10^9 je skutečný signed
rozdíl v[−radix,radix−1], tedy v rozsahu signed32. Při f≥g>0
nezůstane borrow za nejvyšší nenulový digit f. Odebrání horních
a dolních nul zachová výsledek; rovnost dostane jedinou zero
reprezentaci156. Všechna volání ve velké tiskové větvi splňují
f≥g>0, včetně poslední případné rovnosti. Podmínka není odvozena
z úspěšného příkladu: před odčítáním T od F platí G>F≥T a při
závěrečném odčítání od G je G≥T výslovně testováno.

## 3. Skutečný limit17 a zvláštní smallest-normal případ

V §66 je příliš silná pomocná nerovnost. Pro normální fraction
F=2^52−1 je skutečný poměr

    H/L = (2^54−1)/(2^54−3) = 1 + 2/(2^54−3),

což je **menší** než vytištěné(2^53+3)/(2^53+1). Tento drobný
rozpor v komentáři nepoužívám jako důkaz chybných výstupů a nepřidávám
novou programovou kartu. Nahradím jej správnou univerzální mezí:

    H/L ≥ (2^54−1)/(2^54−3) > 1 + 10^−16.

U normálních F>0 je jmenovatel L nejvýše2^54−3. U subnormálů
a payloadů je ještě menší. U mocnin dvou je H−L=3 a
3/(2^54−1)>2/(2^54−3). Poslední ostrá nerovnost je celé
2·10^16>2^54−3. Tím je pokryt i programem zúžený interval min-normal.

Pro kladnou dolní hranici f zvolme10^(d−1)≤f<10^d a mřížku
Δ=10^(d−17). Potom Δ/f≤10^−16, ale g−f>Δ. Mezi hranicemi
tedy existuje **vnitřní** mřížkový bod s nejvýše17 významnými
číslicemi, dokonce při otevřených koncích. Pokud je to právě10^d,
má jen jednu významnou číslici. Proto algoritmus nesmí potřebovat
osmnáctý digit a `char s[18]` pojme i terminující NUL.

Pro x=2^−1022 zbývá ověřit, že užší dolní interval nezvýší
minimum proti skutečné buňce[x−2^−1075,x+2^−1075]. Sousední
16místné decimal body jsou

    a = 2225073858507201·10^−323,
    a+10^−323 = 2225073858507202·10^−323.

Přesné integer nerovnosti dávají a<x−2^−1075 a a+10^−323>x+2^−1075.
Žádný bod s16 nebo méně významnými číslicemi tedy neleží ani ve
skutečné buňce. Obě buňky mají minimum17 a program vybere platný
17místný bod uvnitř užší buňky. Úplná monotonicita a roundtrip se
tím nemění. Pět těchto přesných nerovností je uloženo v
`results/print-float-boundary-arithmetic.json`; jediný nový nice15
výpočet trval0.000907s. Sazba§66 byla skutečně zobrazena.

## 4. Malý exponent: každý průchod a endpoint

Pro e≤1025 je horní integer digit nejvýše8. Je-li a>origin,
integer část je logicky0. Smyčka odstraňuje leading decimal nuly
snížením výstupního exponentu, dokud G nemá nenulový integer digit.
Pak buď obě hranice mají stejný digit d, nebo mají f_digit<g_digit.

Ve společném případě je každý decimal bod v intervalu nucen mít
digit d. Po jeho výpisu se integer části vynulují a obě frakce se
vynásobí10. Invariant je původní interval po odebrání téhož prefixu,
se stejným pozitivním měřítkem. V rozdílném případě lze skončit
s kterýmkoli digit v[f_digit+1,g_digit]; kód volí prostřední
floor((f_digit+1+g_digit)/2), který do této množiny patří a je0…9.
První vytištěný digit není0: při prvním nenulovém G je buď společný
digit kladný, nebo je vybraný digit alespoň1.

Proč tato větev nepotřebuje test `open`? Každý endpoint je dyadický
s redukovaným jmenovatelem2^t, kde t≥50. Při necelé hodnotě≥2^−t
je počet leading decimal nul menší než ceil(2t/5), protože
log10(2)<2/5. Spolu s nejvýše17 významnými kroky podle§3 nastane
méně než t násobení10: ceil(2t/5)+17<t pro t≥50. Žádný endpoint
proto dosud není integer. Vybraný ukončující decimal bod je tedy
**ostře** mezi endpointy; otevřenost/uzavřenost se v této větvi
nemůže projevit. Totéž vylučuje předčasné F=0. Toto je přesný
chybějící předpoklad za slovním komentářem „t>50“.

## 5. Velký exponent: otevřené i uzavřené konce

T je mocnina10. Po úvodní smyčce platí0<F<G<T pro closed interval
a0<F<G≤T pro open interval. Rozdíl vyplývá z testu
`compare(G,T)>=open`: pro open se pokračuje jen při G>T.
Po případném předchozím stupni je G alespoňT/10 (pro open ostře),
což zajišťuje, že první výstup nemá zbytečný leading zero.

V každém kroku násobíme F,G deseti. Opakované odečtení T od obou
vytvoří j=floor(F/T), 0≤j≤9, a zbytkové0≤F<T<G či F<G<T.
Pokud G nedosáhne dalšího povoleného integer bodu, je j vynuceným
společným digitem. Closed interval může skončit přesně při F=0;
open pokračuje, protože dolní hranice do něj nepatří.

Jestliže se ukončit může, závěrečný loop spočítá největší povolený
digit k. Pro closed je to původní j+floor(G/T); pro open
j+ceil(G/T)−1. Platí j+1≤k≤9. Vytištěné
floor((j+1+k)/2) leží mezi povolenými hodnotami. Proto i horní
integer endpoint je zahrnut právě v closed případě. Již vytištěný
prefix je zachován a vybraný bod leží ve správném intervalu.

Před každým dalším digitem není žádný decimal bod na dosavadní
hrubší mřížce: integer body byly vyčerpávajícím způsobem otestovány.
Proto první možný konec dává minimální počet významných číslic.
To dokazuje globální shortest vlastnost pro celý interval, nikoli
jen vztah ke dvěma vybraným zápisům. Jediná odlišná true-cell hranice
byla samostatně vyřešena u min-normal v§3.

## 6. Formát, NaN payload a monotonicita

Má-li s délku d a exponent e, jeho hodnota je integer(s)·10^(e−d).
Větev se zapsaným exponentem vytiskne první digit, případnou tečku,
zbytek s a exponent e−1; dává tutéž hodnotu. Pro e<0 doplní−e
nul před s; pro0≤e≤d vloží tečku do s; pro e>d doplní e−d nul
a závěrečnou tečku. Každá větev proto vyhoví floating syntaxi.
Rozhodnutí e>17 nebo e<d−17 je přesně test, že pevný formát má
více než18 znaků. Znaménko i případný NaN prefix se přidávají
v obou reprezentacích stejně; nejsou skrytou aritmetickou operací.

NaN výstup nesmí obsahovat exponent, protože NaN grammar dovoluje
jen`NaN.` a digit string. Jeho interval má šířku2^−52>2·10^−16,
takže obsahuje vnitřní bod mřížky10^−16. Algoritmus tedy skončí
s nejvýše16 číslicemi **za tečkou**. Payload je menší než1,
a proto e≤0 a d−e≤16: exponentová formatovací větev se nikdy
nevybere. Krajní payloady se díky otevřeným endpointům nevyberou
jako0 nebo1. Canonical NaN byl obsloužen přímo.

Na scan cestě dostane NaN payload q hodnotu1+q. Její nearest
binary64 mřížka je přesně1+F/2^52; následný OR exponentového bitu
vytvoří původní NaN payload a sign. Není nutné spoléhat na
konvenci saturation nelegálního NaN.0 či NaN.999… za hranicí.

Pro dva různé uspořádané konečné binary64 vstupy jsou jejich
roundtrip buňky disjunktní, s případným společným midpointem
přiřazeným pouze jednomu z nich. Vybrané decimal hodnoty proto
mají stejné ostré pořadí. Užší min-normal buňka je podmnožinou
správné, takže argument platí i tam. Pro záporné hodnoty se pořadí
magnitud obrátí znaménkem. Signed zeros mají stejné reálné číslo0,
ale jejich bitový roundtrip je odděleně zachovaný. NaN se tímto
monotonicitním tvrzením neřadí.

## 7. Přesný scan_const podrozsah pro každý vygenerovaný řetězec

Všechny vytištěné finite řetězce mají nejvýše17 významných číslic,
malou integer část, exponent s|E|≤324 a nepatří do S0009 rodiny.
Pevný formát má nejvýše18 znaků; scientific je kratší než32 znaků
i se sign. NaN doplní při scanu jedinou úvodní1, takže i jeho
číselný koeficient má nejvýše17 číslic. Žádný sticky truncation
v input bufferu není aktivní a všechny bufferové pointery zůstávají
v jeho fyzickém rozsahu. Literal exponents se načtou přesně.

Nechť K je počet významných integer číslic, Z počet odstraněných
leading fractional nul, E exponent a D počet uchovaných číslic.
Přesná hodnota je M·10^(K−Z+E−D). Kód dává

    x=333+Z−K−E,

proto první digit M dostane váhu10^(332−x)=10^(K−Z+E−1).
Prefix padding x mod9 a následné devítimístné bloky jsou přesný
radix10^9 rozvoj. Stopping pointer je poslední devítiblok začínající
před posledním vstupním digitem; osm trailing nul pokrývá jeho
zbytek. V tomto oboru se žádný nenulový digit nedostane za index156.
Čísla leží mezi přibližně10^−324 a2^1024; potřebné sloty jsou
daleko od záporné horní hranice i156. `ff.dat[156]+=0` není čteným
logickým digitem a toto místo se nevyužije jako zdroj hodnoty.

`bignum_double` má tentýž suffix invariant jako times_ten, nyní
radix R=10^9. 2(R−1)+1<2^31, carry∈{0,1}. Pokud poslední
digit zmizí, musel být R/2; předchozí2d+1 je lichý, a proto
nezmizí zároveň. Jediný `b--` je opět dostatečný. Žádný zdejší
mezivýsledek nepřekročí2^1025, takže a zůstává bezpečně kladné.

Při hodnotě v≥1 vytvoří T nejmenší mocninu2 ostře větší než v,
tedy2^h≤v<T=2^(h+1), a raw exponent1022+h. Iterace k=54…1
zdvojují zbytek a při zbytku≥T odčítají T. V invariantní rovnici
jsou již získané bity přesným prefixem v·2^(54−h); zbytek je
v[0,T). Nulový zbytek smyčku ukončí s přesnými trailing nulami,
jinak bit0 zaznamená nenulový suffix. Pro0<v<1 úvodní doubling
zvolí m tak, že1≤2^m v<2, raw exponent1022−m, a obdobné
odstraňování integer bitu dává stejný invariant s v·2^(54+m).
Nula je zpracována zvlášť v make_it_zero.

Výsledný55bitový prefix s jedním sticky bitem je přesně vstup,
pro který již úplný pack důkaz dává jediné správné nearest-even
binary64 zaokrouhlení, včetně subnormálů, signed zero a infinity.
Žádný nepovolený druhý rounding se nepřidává. Jelikož výstupní
decimal hodnota leží v příslušné rounding buňce, vrátí scan_const
právě původní bity. Speciální Inf/zero/canonical-NaN větve dávají
stejný výsledek přímo. Příznaky zde stále nejsou součástí kontraktu.

## 8. Náklady a nezavřené zbytky

Výstup má konstantní pomocnou paměť: tři pole157 tetra, několik
octa a18znakový buffer. Nontrivial tiskové digity leží v rozsahu1…76,
takže jedno multiprecizní volání projde nejvýše77 slotů. Malá větev
má nejvýše ceil(2·1076/5)+17=448 násobení každé hranice;
velká úvodní smyčka nejvýše308 násobení T a pak nejvýše17 digitů.
Každý velký digit má nejvýše9 společných odčtení a závěrečný
digit nejvýše9 dalších; žádná skrytá neomezená smyčka nezůstává.
Jde o horní meze skalární práce, nikoli nový benchmark či MMIX μ/υ.

Dokázáno: matematické hodnoty celého print_float, nejkratší počet
významných číslic,17místný limit, oba endpoint režimy, všechny
speciální třídy, syntaktická použitelnost výstupu, monotonicita finite
výstupu a jeho přesný bitový roundtrip přes omezený scan obor.
Samostatné příklady nejsou použity místo těchto invariantů.

Neprohlášeno za uzavřené: celý libovolně dlouhý scan vstup, jeho
širší exponentové meze, obecná C přenositelnost, uživatelsky volitelná
decimal přesnost/režimy, kompletní decimal exception/trap interface
a přímé single-format decimal rozhraní. Tvrzení full IEEE proto
zůstává partial. Malé chyby příliš silné pomocné nerovnosti a
zjednodušeného komentáře o normalizaci jsou doloženy zde; správné
výsledky programu se kvůli nim nebarví jako nový programový nález.

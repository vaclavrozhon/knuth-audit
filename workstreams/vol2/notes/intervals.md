# §4.2.2C a úloha24: směrované intervaly včetně nuly a nekonečen

Původní strany240–241,244–245 a616–617 byly vizuálně přečteny.
Zapracována oprava2007 zavádějící skutečnou0 mezi−0 a+0.
Všechny čtyři vrstvy errat zkontrolovány. Opravený fyzikální příklad
obsahuje nový nálezC0089; interval součinu je správně.

## 1. Význam mezí a směrovaného zaokrouhlení

IntervalI=[l..r] má za konce nenulová reprezentovatelná čísla nebo
symboly−∞,−0,+0,+∞. Pořadí je−∞<z<−0<0<+0<x<+∞ pro z<0<x.
Skutečná0 není koncovým symbolem. Nerovnost l<r je povinná,
s výjimkou povolené rovnosti u konečného nenulového konce.
Nekonečna nejsou hodnoty obsažené v intervalu; značí neomezenost.

Úloha interval popisuje pomocí plovoucích vstupních hodnot. Pro
ověření spolehlivosti používáme i silnější obvyklou interpretaci
reálného obalu: nenulové konečné konce se zahrnují, dolní+0 znamená
striktní kladnost, dolní−0 připouští nulu; horní−0 znamená striktní
zápornost a horní+0 připouští nulu. Tedy[−0,+0]={0}, zatímco
[+0,1] nezahrnuje0. Tato interpretace zahrnuje zejména všechny
plovoucí vstupy požadované zadáním.

Horní zaokrouhlení konečného skutečného výsledku volí nejmenší
reprezentovatelnou horní mez, dolní největší dolní mez. Je-li kladný
výsledek menší než nejmenší kladné číslo, meze jsou+0 a toto číslo;
pro záporný výsledek analogicky záporné minimum a−0. Přesná nula
má dolní−0 a horní+0. Při kladném přetečení je horní mez+∞
a dolní největší konečné číslo; záporně symetricky. Tím jsou
odstraněny výjimky rozsahu, aniž by se ztratilo správné znaménko.

## 2. Součet a rozdíl

Monotonicita sčítání dává
I⊕J=[down(l_I+l_J)..up(r_I+r_J)]. Negace intervalu obrací
pořadí konců a jejich znaménka, takže odčítání je sčítání negace.
Při součtu horních konců nikdy nenastane−∞, takže výraz+∞+(−∞)
není třeba definovat. Dolní součet funguje znaménkovou dualitou.

Pravidla odpovědi pro nuly odpovídají zahrnutí skutečné nuly:
horní+0 plus horní+0 dává+0; pokud je aspoň jeden horní konec−0,
oba sčítance jsou nekladné a aspoň jeden je striktně záporný,
takže horní výsledek je−0. Přičtení kteréhokoli nulového konce
ke konečnému nenulovému konci jej může ponechat; případná ostrost
na nenulovém konci se v této reprezentaci neuchovává, ale obal
zůstává bezpečný. Dolní pravidla jsou přesně opačná přes negaci.

## 3. Součin a důvod čtyř krajních dvojic

Pro konečný obdélníkI×J dosahuje funkce xy obou extrémů v rozích.
Nejdříve se každá z obou souřadnic optimalizuje při pevné druhé;
lineární funkce na intervalu má extrém na kraji. Proto stačí minimum
čtyř dolních a maximum čtyř horních součinů. Pro neomezené intervaly
se používají jednostranné limity se stejnými znaménky.

Následující tabulka přesně vybírá aktivní rohy. Písmena l,r vždy
značí dolní a horní konec daného operandu. „Smíšený“ znamená,
že interval obsahuje záporné i kladné skutečné hodnoty; nulový
interval lze řadit zároveň mezi nekladné i nezáporné.

| ZnaménkaI | ZnaménkaJ | Dolní hodnota před zaokrouhlením | Horní hodnota před zaokrouhlením |
|---|---|---|---|
| nezáporné | nezáporné | l_I l_J | r_I r_J |
| nezáporné | nekladné | r_I l_J | l_I r_J |
| nekladné | nezáporné | l_I r_J | r_I l_J |
| nekladné | nekladné | r_I r_J | l_I l_J |
| smíšené | nezáporné | l_I r_J | r_I r_J |
| smíšené | nekladné | r_I l_J | l_I l_J |
| nezáporné | smíšené | r_I l_J | r_I r_J |
| nekladné | smíšené | l_I r_J | l_I l_J |
| smíšené | smíšené | min(l_I r_J,r_I l_J) | max(l_I l_J,r_I r_J) |

To dokazuje komentář odpovědi: většinou dva směrované součiny,
při dvou smíšených intervalech čtyři. Tvrzení v hlavním textu
„about twice“ je orientační nákladový komentář, ne mez přesně
pro každý znaménkový případ nebo konkrétní implementaci.

Pro nulové konce určuje znaménko výsledného±0 součin znamének.
Totéž se používá pro formální rohy0·∞. Nejde o přisouzení hodnoty
neurčitému reálnému limitu0·∞: v tabulce vybere jiný roh skutečnou
nekonečnou mez, pokud má být neomezená. Pokud je celý operand
nulový, výsledek je opravdu{0}. Kontrola každé znaménkové třídy
rovněž ukazuje, že otevřená nula zůstane otevřená přesně tam,
kde všechny možné součiny mají striktně stejné znaménko.
Příklady: {0}·[−∞,+∞]={0} a [+0,1]·[−∞,−0]=[−∞,−0].
Tím jsou odůvodněny i zdánlivě nezvyklé zvláštní případy odpovědi.

## 4. Dělení

Dělení je odmítnuto právě tehdy, když dolní konec dělitele leží
pod skutečnou0 a horní nad ní; jde přesně o případy, kdy interval
obsahuje0. Díky rozšířenému pořadí test zahrnuje i[−0,r] nebo[l,+0],
ale dovoluje[+0,r] a[l,−0].

Na každé polopřímce je funkce1/x klesající. Formální reciproký
interval je proto[1/r_J..1/l_J], kde(±0)^(-1)=±∞
a(±∞)^(-1)=±0. Násobicí tabulka potom určuje všechny potřebné
rohy. Jak zdůrazňuje odpověď, x·y^(-1) se musí vyhodnotit přímo
jako směrované x/y; reciproký konec se nejprve nezaokrouhluje do
samostatného plovoucího čísla. Stejný rozbor znamének a jednostranných
limitů dokazuje obal i při nulových a nekonečných koncích.

Všechny výsledky jsou znovu platné intervaly: nikdy nevznikne
samotný nekonečný či jednostranně nulový bod. Přetečení a podtečení
jsou zpracována koncovými symboly; jedinou vyžadovanou aritmetickou
výjimkou zůstává dělitel obsahující skutečnou nulu.

## 5. Aktualizovaný příkladN/h a závislost hodnot

Pro meze z errata2020 činí správný intervalový součet

```text
[(24,.60221407)..(24,.60221409)],
```

nikoli horní.60221408 uvedenou v erratu. Detail a přesný svědek
jsou vC0089. Součin naopak souhlasí:

```text
[(−9,.39903126)..(−9,.39903128)].
```

Oprava se týká definované operace nad oběma intervaly. Pokud se
mimo intervalový výpočet využije přesná nová definice konstantSI,
původní užší interval může stále obsahovat tento jeden skutečný
součet; to nezachraňuje vytištěnou identitu intervalové operace.

Komentář o závislosti mezivýsledků je správný. Například pro
x∈[1,2] dá prosté intervalové x−x obal[−1,1], ačkoli skutečný
výraz je přesně0. Ztráta informace o shodnosti dvou výskytů
vede k širšímu obalu; neporušuje bezpečnost směrovaného výpočtu.
Obecné historické přehledy a doporučení zdrojů se ověřují zvlášť.

## 6. Reprodukce a rozsah

`interval_model.py` přepisuje směrované koncové operace z odpovědi24;
`verify_intervals.py` porovnává výstupy s přesnými racionálními
výsledky, bez použití těchto pravidel v referenčním výpočtu.
V každém ze dvou formátů b2,p2 a b3,p1 s exponenty−1..1 existuje
132 přípustných intervalů z úplné množiny konců.

Prošly všechny jejich dvojice: celkem122496 definovaných operací,
489984 nezávislých skalárních krajních kontrol a16896 odmítnutých
nulových dělitelů. Referenční body obsahují všechna čísla formátu,
mezilehlé racionální body a hodnoty hluboko mimo rozsah normálních
čísel. Konečné sondy samy nedokazují chování v nekonečnu; to je
obsahem obecného znaménkového důkazu výše. Samostatně přepočten
celý aktualizovaný příkladN/h. Všechny tři bloky dokončeny s exit0.

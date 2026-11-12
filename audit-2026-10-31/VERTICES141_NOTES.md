# DLX141: čtverce s barevnými vrcholy

Kontrola 2. listopadu 2026. Zadání je na straně 141, odpověď na 454
(PDF 161 a 474). **Nová chyba zatím nenalezena.** Všechny matematické
počty jsme reprodukovali úplným geometrickým výčtem. Druhý úplný výčet
původním DLX2 stále běží, proto zatím netvrdíme shodu celých množin obou
řešičů. Celá úloha je `partial` také kvůli historickým mezerám níže.

## Úplný geometrický výčet

Sada je všech 24 cyklických čtveřic tří barev; Burnside dává
`(3⁴ + 3² + 2·3)/4 = 24`. Každý čtverec musí použít jiný cyklický typ
a všechny výskyty společného geometrického vrcholu mají tutéž barvu.

Nezávislý C++ program postupuje v pevném pořadí buněk. Každou z dosud
nepřiřazených rohových barev zkouší s omezením pořadím prvního výskytu.
Označí použitý typ v bitové masce a odmítne opakování. Větev lze také
odmítnout, když některá další buňka nepřipouští žádný nepoužitý typ.
To je nutná podmínka, nikoli dodatečné omezení řešení. Pořadí buněk
a zavádění barev zachovává právě jednoho zástupce každého přejmenování.

Sedm malých případů bylo před spuštěním porovnáno s úplným výčtem
barev všech vrcholů, původním DLX2 a DLX2 s normalizací z úlohy 122.
Shodují se celé množiny. Součástí je i úplná sada šesti dvoubarevných
dílků na obdélníku 2 × 3. Úspěšné výpočty neopakujeme.

Úplný geometrický běh skončil **20:09:13 UTC**, návratový kód nula.
Přijímací program ověřil otisky vstupu, zdrojů, binárky a obou výstupů,
pak přímo ověřil **všech 335 292 modelů**, jejich různost a všechny orbity.

| Deska | Po přejmenování barev | Symetrie desky | Podstatně různá řešení |
|---|---:|---:|---:|
| 5 × 5 s prostřední dírou | 138 248 | 8 | 17 281 |
| 4 × 6 | 49 336 | 4 | 12 334 |
| 3 × 8 | 147 708 | 4 | 36 927 |

Každá geometrická orbita má skutečně velikost 8, resp. 4: kontrolujeme
celé obrazy a jejich přítomnost v úplné množině. Dělení tedy není pouhý
předpoklad o nesouměrnosti. Zrcadlení permutuje úplnou sadu cyklických
typů opět na sebe. Všechny tři původní obrázky jsou mezi řešeními.

[Přijatý výčet](results/vertices141/independent-accepted.json),
[zástupci všech orbit](results/vertices141/geometric-representatives.json),
[reprodukovatelná kontrola](accept_vertices141_independent.py).

## Vedlejší počty a válce

- U 5 × 5 má otvor jednobarevný okraj v **209** třídách. Přesně **šest**
  z nich má shodnou dvojici protějších stran.
- U 4 × 6 je **180** řešení se shodným levým a pravým okrajem; cyklickým
  přesouváním sloupců vzniká **30 rodin po šesti**.
- U 3 × 8 je analogicky **1536** řešení, **192 rodin po osmi**.
  V **42** třídách mají oba svislé okraje tutéž jedinou barvu.
- Vytištěný obdélník 4 × 6 je opravdu **jediná třída**, kde obě dvojice
  protějších stran určují shodné rozklady podle barev.

Při každém posunutí válce se znovu kontroluje příslušnost k úplnému
výčtu. Rodiny mají uvedené velikosti i po zrcadleních, půlobratu a
přejmenování barev. [Konkrétní zástupci](results/vertices141/special-models.json).

Navíc jsme z původního [Gottfriedova programu s válci](https://www.gottfriedville.net/puzzles/squares/sqdisp.shtml)
dekódovali všech **30 zveřejněných zástupců**. Každý je platný a dohromady
představují přesně všech 30 našich rodin. První pomocný záznam programu
je výslovně označený rámeček; nepočítá se jako řešení.
[Strojová kontrola](results/vertices141/sources-checked.json).

## Původní obrázky a pokrytí roviny

Z původního PDF bylo získáno všech **288 barevných rohů 72 čtverců**.
V každém obrázku souhlasí společné vrcholy i úplná sada 24 typů.
Všech 288 rohů odpovídá také autorovu draftu, strana 77.
[Porovnání a certifikáty okrajů](results/vertices141/geometry-checked.json).

Souřadnice mají počátek vlevo dole. Pro libovolné řešení na obdélníku
šířky `w` a výšky `h` označme jeho vrcholové barvy `P(x,y)` a položme
`f_n(t) = n − |(t mod 2n) − n|`. Pak
`C(x,y) = P(f_w(x), f_h(y))` je periodické obarvení celé celočíselné
mřížky. Každá jednotková buňka je původní buňkou, jejím zrcadlením nebo
půlobratem. Společné vrcholy mají jedinou definici, takže všechny švy
souhlasí. U děravé desky nejprve doplníme prostřední jednotkovou buňku
dílkem určeným jejími čtyřmi rohovými barvami; tento typ je vždy v sadě.
Pokrytí používá další kopie jednotlivých dílků. Samotné celé děravé
bloky by ponechávaly nepokryté dutiny.

Vytištěné příklady dovolují i popsané zvláštní konstrukce. Nechť `S`
zaměňuje `b ↔ c` a ponechává `a`.

U 5 × 5 jsou spodní i horní okraj `aaabba`; levý je `aababa`, pravý
`acacaa`, otvor má `cccc`. Přímá kontrola dává
`P(5,y) = S(P(0,(y+1) mod 5))`. Sousední sloupec bloků je proto nutné
**posunout o jednu buňku dolů**. Pro `q,r = divmod(x,5)` funguje
`C(x,y) = S^q(P(r,(y+q) mod 5))`. Periody jsou `(10,−2)` a `(0,5)`.
Díry se doplní dílkem `cccc`, resp. `bbbb` v přebarvených kopiích.

U 4 × 6 je spodní okraj `abcbbca`, horní `acbccba`, levý zdola
`abbca`, pravý zdola `accba`. Protilehlé okraje jsou navzájem obrazy
pod `S`. Kopie v bloku `(qx,qy)` proto přebarvíme právě tehdy, když
`qx+qy` je liché. Fungují například periody `(12,0)` a `(0,8)`.
Vodorovné rozklady mají RGS **0121120**. Svislé čtené **shora dolů**
mají **01220**, přesně jako v knize; při čtení zdola je to 01120.
První pomocná kontrola měla směr svislého čtení obrácený; nejde o chybu
knihy a oprava směru je zachycena v kontrolním programu.

U 3 × 8 jsou oba svislé okraje `aaaa`. Opakování po osmi sloupcích a
střídání svislého zrcadlení dává periody `(8,0)` a `(0,6)`.

## Druhý výčet a historické náklady

Nativní DLX2 má 24 primárních položek buněk a 24 typů, sekundární
barvené položky vrcholů a **1944 možností**. Běží původní algoritmus
s úpravou z úlohy 122 a počáteční další barvou `a`. Primární položka
typu je přípustná pro větvení až po zavedení všech barev v jejím názvu
(`CTH = největší písmeno + 1`). Taková položka je pevná při permutacích
dosud nepoužitých barev; položky buněk jsou pevné vždy. To odůvodňuje
konkrétní redukci barevné symetrie, nikoli neomezené obecné tvrzení C031.

Fronta **1147292** běží od 19:59:59 UTC, postupně hole5, rect4x6,
rect3x8. Každý případ má limit 48 hodin a ukládá všechna řešení.
Čeká přijetí dokončených terminálů, shoda celých množin a porovnání
knižních **1390/330/720 Gmems**. Průběžný počet se za výsledek nepovažuje.
Zmrazené zdroje se během běhu neupravují. Stav a příkaz jsou
v [launch.json](results/vertices141/launch.json).

## Historické prameny a zbývající mezery

[Gottfriedův vlastní přehled](https://www.gottfriedville.net/puzzles/squares/sqinfo.shtml)
uvádí všechny tři podstatně různé počty;
[jeho stránka zvláštních řešení](https://www.gottfriedville.net/puzzles/squares/sqspcl.shtml)
potvrzuje oba válcové počty. Archivy HTML jsou v `sources/vertices141/`.
Současné stránky však neprokazují přesné roky prvních výpočtů
**1998/1999/2002** ani prvenství.

[Výrobce Kadon](https://www.gamepuzzles.com/moredge.htm) potvrzuje spojení
Gottfrieda, rohově barvených čtverců a Skor-Morova názvu **Nitty Gritty**.
Zmiňuje jeho práci z roku 1972 a pozdější počítač z roku 1999. Původní
datovaný doklad přesného uvedení hlavolamu v **roce 1970** zatím chybí.
Sekundární data bazarových nabídek takový doklad nenahrazují.

Originály patentů [US487797](sources/vertices141/us487797.pdf) a
[US490689](sources/vertices141/us490689.pdf) byly staženy a prohlédnuty
včetně kreseb a původních specifikací. Potvrzují Edwina L. Thurstona,
data **13. prosince 1892** a **31. ledna 1893** a vrcholové skládání
neúplných sad. Absolutní historické prvenství tím samostatně nedokazujeme.

Třetí konkrétní mezera je tvrzení o Langfordově neúspěšném ručním
řešení 3 × 8. Metadata článku z roku 1959 známe z předchozí úlohy,
plný původní text stále chybí; metadata toto tvrzení neověřují.

V šesti relevantních vrstvách errat 4B/Fascicle 5 odpovídající oprava
nenalezena. Použitá oficiální data byla ověřena 2. listopadu v 19:14 UTC
při předchozí úloze; netvrdíme nové opakované stažení.
[Konkrétní vrstvy, otisky a mapování stran](results/vertices141/errata-check.json).

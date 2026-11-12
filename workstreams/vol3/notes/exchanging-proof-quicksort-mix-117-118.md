# Quicksort MIX: všechny instrukce, frekvence a přesná cena

2026-11-07. Tištěné 117–118 / files 128–129 zobrazeny. Správnost
abstraktního Q1–Q9 přebírám z P1034–1039. Tento blok kontroluje skutečný
převod do MIX, ne jinou implementaci. Žádný matematický běh.

## P1048 — reprezentace, mezníky a přesný strojový rozsah

R je jednoslovný záznam totožný se svým klíčem, takže LDA uchová současně
pivot i celý R. INPUT..INPUT+N+1 a kód/STACK leží v paměti, nesmějí se
nevhodně překrývat. N>M≥1, indexové mezníky a jejich paměťové adresy
se vejdou do dvou bajtů. Pro následující důkaz navíc výslovně požadujeme
M+N≤b²−1 pro MIX s bajtovou bází b; postačí b=64 a M+N≤4095. Proč
tato podmínka nevyplyne jen z N>M a běžného uložení pole, je P1055.

Pár je uložen do polí A=(2:3), B=(4:5) jednoho slova. STi zapisuje dva
nejnižší bajty, STA rovněž vybere pravé dva. Proto se každá mez uloží
přesně. LD2/LD3 vyberou dvoubajtové pole a protože nezahrnuje signum,
načtou nezáporný index; libovolné zbylé bajty/slovní signum nevadí.
Každá skutečně uložená mez je kladná a ≤N.

Na konci se při prázdném zásobníku čte také STACK+0; tato adresa musí
být platná, ale její hodnota nemusí být inicializovaná. Načtené hodnoty
se v tomto případě nepoužijí. Paměť zásobníku nad bází je přesně
kapacita z C0011, nikoli jeho chybné tištěné N+2.

## P1049 — instrukce 01–23, partition beze změny invariantů

01–03 nastaví I6=0,I2=1,I3=N. 04 nastaví I5=r+1, 05 A=R[l],
06 I4=l+1. 07 skočí na 13, takže se první zvýšení i vykonané již 06
neprovede podruhé. Každé další zvýšení i je 12. 13 porovná pivot s
R[i]; 14 vrací na 12 právě při K>K[i]. 15 sníží j, 16 porovná
pivot s R[j] a 17 vrací na 15 při K<K[j]. P1035 zaručuje všechny
čtené adresy. Zarážky jsou nejnižší/nejvyšší celé MIX hodnoty a přitom
rovnost není problém. Obě reprezentace nuly se při porovnání chovají
jako stejný klíč; jejich bitový záznam se přesuny neztrácí.

18 nastaví X=j, 19 odečte i, 20 skočí na 08 právě při j−i>0.
08 načte R[i] do X, 09 nastaví I1=INPUT+i. MOVE v 10 má implicitní
F=1: přenese jediné R[j] na adresu I1 a zvýší I1; 11 uloží původní
R[i] na j. Změněný I1 není až do 26 potřeba. A zůstává pivotem.
Po 11 se pokračuje na 12, tedy přesně Q6→Q3.

Když j≤i, 21–23 načtou R[j] do X, uloží jej na l a uloží pivot A na j.
Pro j=l jsou to identická čtení/zápisy téhož slova, bez poškození.
Na rozdíl od abstraktního prohození program správně využívá pivot
uložený v A. Ostatní registr, který bude Q7 potřebovat, zůstává zachován.

## P1050 — instrukce 24–46 a všechny čtyři velikostní kombinace

Pišme a=j−l,b=r−j. 24–25 dají I4=r−(M+j)=b−M; 26–27 dají
I1=j−(M+l)=a−M. 28–29 nastaví A=(b−M)−(a−M)=b−a. Výsledek je
v rozsahu ±N; nulová hodnota má pro JANN vždy nezáporný význam.
30 skočí na 39 právě při b≥a. Jinak a>b:

* 31: jestliže I1≤0, i větší a≤M, takže obě části jsou krátké a jde
  se na 47. Jinak a>M.
* 32: jestliže I4≤0, b≤M, jde se na 45, kde se pouze r nastaví na j−1.
* Jinak a>b>M. 33 zvětší zásobník, 34 uloží l do A pole, 35–36
  vloží j−1 do B pole. 37 nastaví l=j+1 a 38 začne menší pravou část.

Při b≥a se vykoná 39:

* 39 při b≤M přeskočí na 47, protože obě části jsou krátké.
* 40 při a≤M přeskočí zpět na 37 a začne jedinou dlouhou pravou část.
* Jinak b≥a>M. 41–44 uloží (j+1,r) po zvětšení zásobníku, 45 nastaví
  r=j−1 a 46 začne menší či stejně velkou levou část.

Každá větev tedy přesně odpovídá Q7, včetně b=a a rovnosti s M.
Nové hodnoty j±1 se používají jako mezníky pouze tehdy, když příslušná
část není prázdná. Průchod 37 nebo 45 nemusí předcházet vložení, což
vysvětluje smíšené četnosti u těchto řádků.

## P1051 — instrukce 47–50, pop a prázdný zásobník

Při velikosti q>0 načtou 47/48 právě obě meze položky q, 49 nastaví
q−1≥0 a 50 skočí na 04. Zarážkový invariant této části již platí.
Při q=0 se načtou libovolné hodnoty ze STACK, pak I6=−1 a 50 neskočí.
Tím se bezpečně přejde k insertion; I2 a I3 už nebudou použity.
Snížení z 1 na nulu i test nezápornosti fungují pro obě MIX nuly.
Každý push je někdy popnut, a existuje právě jeden dodatečný prázdný
pop na závěr. To vyplývá z konečnosti Q, nikoli z předpokladu, že se
žádná větev nikdy nepoužije.

## P1052 — instrukce 51–63, negativně posunutý index j

51 nastaví I5=2−N. V celé vnější smyčce je I5=j−N. Proto 52 čte
INPUT+N+I5=INPUT+j a 53 porovná A=K[j] s INPUT+j−1. 54 přejde
na 62 právě při K[j]≥K[j−1]. Jinak 55 dá I4=N−1+I5=j−1.
56/57 zkopírují R[i] na i+1, 58 sníží i a 59/60 opakují právě
při K<K[i]. A drží původní R[j], takže 61 vloží tento záznam do díry.
P1039 dokládá zastavení na K[0], bez zápisu do něj.

62 zvýší I5 a 63 vrací na 52, dokud I5≤0, tedy včetně iterace j=N.
Po ní se zvýší na 1 a skončí. N>M≥1 zajišťuje N≥2, takže první
iterace j=2 existuje. Platný indexový rozsah je 2−N..1; efektivní
adresy v této smyčce jsou skutečné indexy pole, bez skrytého velkého
kladného mezisoučtu. Tím jsou doloženy všechny skutečné paměťové zápisy.

## P1053 — každá tištěná četnost a rovnice (15)

A je počet fází, B počet Q6, C' počet levých scan porovnání, C−C'
pravých. S je počet push, S' počet push levé delší části. A' je počet
fází s a>b. A'' počítá případ a>M≥b, A''' případ b>M≥a. D je počet
insertion iterací, které skutečně posouvají, E součet počtů posunů.
Každý takový posun odstraní právě jednu původní inverzi, takže E má
význam v (16). Tyto počty platí i pro shodné klíče.

| Řádky | Četnost každého řádku | Důvod |
|---|---|---|
| 01–03 | 1 | inicializace |
| 04–07 | A | začátek fáze |
| 08–11 | B | Q6 |
| 12 | C'−A | první posun už udělal 06 |
| 13–14 | C' | všechna levá porovnání |
| 15–17 | C−C' | všechna pravá porovnání |
| 18–20 | B+A | jeden test na Q6 a jeden koncový na fázi |
| 21–30 | A | závěrečná výměna a velikosti |
| 31 | A' | a>b |
| 32 | S'+A'' | a>M v této větvi |
| 33–36 | S' | oba dlouhé, a>b |
| 37–38 | S'+A''' | nová pravá část |
| 39 | A−A' | b≥a |
| 40 | S−S'+A''' | b>M v této větvi |
| 41–44 | S−S' | oba dlouhé, b≥a |
| 45–46 | S−S'+A'' | nová levá část |
| 47–50 | S+1 | všechny pop plus poslední prázdný |
| 51 | 1 | začátek insertion |
| 52–54,62–63 | N−1 | každé j=2..N |
| 55,61 | D | insertion s neprázdným posunem |
| 56–60 | E | každý jeden posun |

Do 04 se vstupuje jednou inicializací, S'+A'''krát z 38,
S−S'+A''krát z 46 a S-krát úspěšným pop. Proto

    A=1+(S'+A''')+(S−S'+A'')+S=1+2S+A''+A'''.

To je (15) s přesnou identifikací všech symbolů. Alternativně je to
rovnost pro binární strom: počet všech vnitřních uzlů se rovná jedné
plus dvojnásobku uzlů se dvěma dlouhými dětmi plus počtu uzlů s jedním.

## P1054 — celá cena (16), včetně konstant a prázdného pop

MIX load/store/compare stojí 2u, MOVE jednoho slova 3u, ostatní zdejší
instrukce 1u. Z předchozí úplné tabulky dostáváme:

| Řádky | Cena |
|---|---|
| 01–03 | 3 |
| 04–07 | 5A |
| 08–11 | 8B |
| 12–17 | 4C−A |
| 18–20 | 3(B+A) |
| 21–23 | 6A |
| 24–30 | 7A |
| 31,39 | A |
| 32,40 | S+A''+A''' |
| 33–36,41–44 | 6S |
| 37–38,45–46 | 2S+2(A''+A''') |
| 47–50 | 6(S+1) |
| 51–63 | 1+7(N−1)+3D+8E |

Součet je 21A+11B+4C+3(A''+A''')+15S+3D+8E+7N+3.
Dosazením A''+A'''=A−2S−1 dostáváme přesně

    24A+11B+4C+3D+8E+7N+9S.

Konstanty se zruší, nejde o opomenutí vstupní nebo výstupní režie.
Vzorec je pro tištěný program včetně Q9, i při M=1; doporučené
vynechání Q9 je jiný program a ušetří 7(N−1)+1. Případ N≤M se
v programu nepředpokládá, takže zde nesmíme dosadit A=S=0 jako cenu
jazykově jiného vstupu přes Q1→Q9. Žádná enumerace není potřeba.

## P1055 — otevřený rozsah pro velmi velké M (partial/C0031)

Podmínka M+N≤b²−1 v P1048 stačí pro oba sčítané operandy M+j a M+l.
Bez ní může již první 25 selhat, ačkoli výsledný rozdíl se vejde.
Na binárním MIX je příklad N=3000,M=2000, INPUT=0,
R=(3000,1,2,...,2999), krajní minimální/maximální slova na 0/3001,
kód třeba od 3100 a zásobník od 3200. Kód i pole leží v 4000 buňkách.
První pivot je maximum, takže j=3000. Efektivní adresa instrukce
`DEC4 M,5` je 2000+3000=5000>4095. Svazek 1, tištěná 127/file142,
výslovně označuje indexovaný výsledek mimo dva bajty za nedefinovaný.
Výsledné I4=−2000 by samo bylo reprezentovatelné; závada je mezikrok.

Podobná podmínka se týká řádku 27. Rozdělení 25 na `DEC4 0,5` a
`DEC4 M`, a 27 na `DEC1 0,2` a `DEC1 M`, pracuje s a,b a a−M,b−M,
které se vždy vejdou, ale přidá 2A jednotek do ceny programu. Alternativní
oprava je uvést dostatečné omezení M+N≤b²−1. Pro doporučené M=9 jsou
oba součty bezpečné pro každé pole, které se vejde do paměti MIX.

Přesný protipříklad literalnímu rozsahu N>M je doložen, ale „M should
be chosen as described below“ na 115 může znamenat zamýšlený malý práh.
Proto jde o candidate/low, nikoli potvrzenou algoritmickou chybu.
Neskrývám tento předpoklad do univerzálního uzavření programu.
Doklad a pět vrstev jsou v `V3-C0031-quicksort-threshold-address.md`
a `sources/quicksort-threshold-address-errata-review.json`.

Známé erratum 118/53 z roku 1998 pouze doplní interpunkci komentáře
I5=j−N. Historické opravy 117–118 prvního vydání odstraňují redundantní
R a opravují šipku. Žádná nemění zde kontrolované větvení či náklady.

# D106 — celá MPR3: kostky nad průměrem

6. listopadu 2026. Celé zadání12/file32 a odpověď371/file391
přímo zobrazeny, obě také ve vyšším rozlišení kvůli jednotlivým
tečkám. Celá odpověď porovnána s autorovým Pre-Fascicle5A,
28/file34. Kontrola zahrnuje osm řešení, každý diagram, všechny
pravděpodobnosti a jedinečnost rozšířené varianty.

## Model, všechny stěny a první přesné pravděpodobnosti

Pokračujeme s nezávislými hody šestistěnnými kostkami; každá
fyzická stěna má pravděpodobnost1/6. Opakované hodnoty na různých
stěnách vytvářejí nerovnoměrnou distribuci počtu teček. Zadání
omezuje jednotlivé hodnoty na1,…,6. Podmínka nadprůměrnosti
A>(A+B+C)/3 je přesně2A>B+C, tedy ostrá nerovnost.
Rovnost průměru se nezapočítává jako výhra.

První diagram, v pořadí horního a dolního řádku, obsahuje

```
A=(3,3,3,3,3,5),
B=C=(4,1,4,4,1,4).
```

Tím jsou uvedeny všechny stěny, včetně samostatné kostky C
výslovně ztotožněné distribucí s B. Hody B a C jsou přesto
nezávislé; B=C zde neznamená tutéž náhodnou hodnotu při hodu.

Pro každou z pěti stěn A=3 musí platit B+C<6. Dvojice B,C
dají součet2 ve2·2=4 případech a součet5 ve2·4+4·2=16
případech; součet8 ve zbývajících16 nevyhoví. Každá nízká
stěna A tedy vyhraje20krát. Pro A=5 vyhovuje všech36 dvojic.
Celkem je100+36=136 výher z216, tedy17/27.

Při B=1 žádná dvojice A,C nevyhovuje2B>A+C. Při B=4
vyhoví všech5·6=30 dvojic s A=3 a dvě další s A=5,C=1.
Čtyři vysoké stěny B tak dávají4·32=128 výher, tedy16/27.
Stejný počet platí pro C díky skutečné symetrii nezávislých
distribucí B,C. Zadáním požadované pořadí pravděpodobností
a spodní mez16/27 jsou tedy splněny.

## Proč je seznam osmi řešení úplný

Pořadí šesti fyzických stěn nemění pravděpodobnosti, proto
každou kostku reprezentujeme neklesající šesticí z1,…,6.
Těch je C(11,6)=462, ekvivalentně šest nezáporných četností
se součtem6. Tři kostky lze pro účely výčtu libovolně
přejmenovat; teprve potom je podle pravděpodobnosti označíme
A,B,C v pořadí požadovaném zadáním. Při stejných
pravděpodobnostech nepovažujeme záměnu názvů B,C za nové
řešení. To je přirozený rozsah tištěného počtu osm; nepočítá
uspořádání sítí ani přejmenování stejných rolí.

`verify_mpr003_six.cpp` projde všechny trojice indexů
0≤a≤b≤c<462, včetně opakovaných kostek. Je jich přesně
C(464,3)=16 542 064. Každá neuspořádaná trojice rozdělení
má právě jeden takový zápis, takže nic není vynecháno ani
započítáno dvakrát.

Pro každou dvojici kostek B,C a každou hodnotu v si program
spočítá

```
K(B,C;v)=#{(b,c): b je stěna B, c je stěna C, b+c<2v}.
```

Všech36 uspořádaných dvojic fyzických stěn se započítává
samostatně. Je-li h_A(v) četnost hodnoty v na A, přesný počet
nadprůměrných výsledků pro A je Σ_v h_A(v)K(B,C;v).
Jednotlivé členy rozdělují všech216 hodů podle hodnoty A;
žádný hod nemá dvojí příspěvek. Analogicky se počítá B a C.
Podmínka pravděpodobnosti≥16/27 je přesně počet≥128,
takže se nikde nezaokrouhluje a nemusí se používat plovoucí
aritmetika. Zamítnutí při prvním počtu pod128 nemůže odstranit
řešení. Pro každé přijaté řešení následuje ještě přímý výčet
216 hodů s původními třemi nerovnostmi3x>x+y+z; ten nezávisle
souhlasí s histogramovým skóre.

Úplný seznam je následující. Řetězec zapisuje šest hodnot
kostky v neklesajícím pořadí; poslední sloupec je počet
nadprůměrných hodů z216 pro A,B,C.

| A | B | C | Počty |
|---|---|---|---|
|333335|114444|114444|136,128,128|
|333336|114444|114444|136,128,128|
|444446|115555|115555|136,128,128|
|444446|115555|125555|136,128,128|
|444446|115555|225555|136,128,128|
|444446|125555|125555|136,128,128|
|444446|125555|225555|136,128,128|
|444446|225555|225555|136,128,128|

Osm tříd tedy skutečně má vytištěné pravděpodobnosti
17/27,16/27,16/27. V každé je40 hodů s právě jednou
nadprůměrnou hodnotou a176 se dvěma. Program používá
v jádrech počty nejvýše36 a ve skóre nejvýše216, takže
nenastane přetečení použitých celočíselných typů.
Rekurze pro kostky má pevnou hloubku6, všechny zbývající
smyčky jsou výše vymezené konečné prostory. Celá kontrola
trvala0.220512s s nice15; proces měl pevný limit10s.
Výsledek i SHA256 zdroje jsou v `results/sequential/mpr-003-six.json`.
Žádný předchozí test se neopakoval.

## Rozšířený diagram a každý možný druh hodu

Sedmitečkový dovětek dovoluje hodnoty1,…,7. Druhý diagram má
všechny stěny přesně

```
A=(6,6,6,6,6,6),
B=(7,1,7,7,1,7),
C=(4,4,4,7,7,7).
```

Protože A je konstantní, existují jen čtyři různé hodnotové
trojice. Zde je každá z nich, její pravděpodobnost a přesný průměr:

| A,B,C | Pravděpodobnost | Průměr | Pod průměrem | Nad průměrem |
|---|---|---|---|---|
|6,1,4|1/6|11/3|B|A,C|
|6,1,7|1/6|14/3|B|A,C|
|6,7,4|1/3|17/3|C|A,B|
|6,7,7|1/3|20/3|A|B,C|

V žádném případě není rovnost průměru. Každý hod má právě
jednu kostku pod průměrem a dvě nad ním; každá z A,B,C je
pod průměrem s pravděpodobností1/3, tedy nad ním s2/3.
Přímý malý výčet216 fyzických hodů potvrzuje144 výher,
72 proher a0 rovností pro každou kostku.

## Proč je sedmitečkové optimální řešení jediné

Pro libovolná tři reálná čísla mohou být nad jejich aritmetickým
průměrem nejvýše dvě. Kdyby všechny tři byly větší, sečtením
by jejich součet byl větší než sám sebe. Proto je součet tří
pravděpodobností nadprůměrnosti nejvýše2. Jsou-li všechny
alespoň2/3, musí být všechny přesně2/3 a počet nadprůměrných
kostek musí být2 v každém hodu s kladnou pravděpodobností.
Každá fyzická kombinace stěn má kladnou pravděpodobnost1/216,
takže zde nelze skrýt výjimku na nulové události.

Seřaďme hodnoty jednoho hodu jako l≤m≤h. Dvě hodnoty jsou
nad průměrem právě tehdy, když

```
m>(l+m+h)/3, tedy2m>l+h.
```

Pak je l jedinou hodnotou pod průměrem, m i h jsou nad ním.
Rovnost vysokých hodnot je přípustná, rovnost dvou nejnižších
by však podmínku znemožnila. Tak jsme dostali přesnou
podmínku jen na množiny hodnot, nezávislou na jejich četnostech.

Možných šestistěnných kostek nad1,…,7 je C(12,6)=924.
Jejich neprázdná podpora může být libovolná podmnožina1,…,7
o nejvýše6 prvcích, celkem126 podpor. Pro podporu velikosti k
existuje C(5,k−1) kladných rozdělení šesti stěn mezi její hodnoty;
to je počet kompozic6 na k kladných částí. Program je vytváří
jednou z úplného seznamu neklesajících šestic.

`verify_mpr003_seven.py` používá úplný následující postup:

1. Pro každou dvojici hodnot a,b z1,…,7 určí sedmibitovou
   množinu L(a,b) všech c, pro něž2median(a,b,c)>min(a,b,c)+max(a,b,c).
   Je to přímé vyzkoušení sedmi možností, nikoli odhad.
2. Pro každou dvojici podpor S_A,S_B vytvoří
   L=průnik_{a∈S_A,b∈S_B}L(a,b). Podpora S_C vyhovuje
   pro všechny hody právě tehdy, když S_C⊆L. Oba směry této
   ekvivalence jsou přímo významem průniku.
3. Projde všechny neprázdné podmnožiny L, ponechá jen skutečné
   podpory a pořadí bitových masek S_A≤S_B≤S_C. Operace
   c←(c−1)&L dává vždy největší menší podmasku: binární
   odečtení vymaže poslední jedničku a nastaví nižší bity,
   průnik ponechá právě povolené z nich. Od L do0 tím
   navštíví každou neprázdnou podmasku právě jednou.
4. V každé takové trojici podpor projde všechna jejich
   rozdělení šesti stěn. Při stejných podporách se navíc
   seřadí indexy rozdělení, takže i opakovaná kostka je
   zahrnuta a žádná neuspořádaná trojice není zdvojena.
5. Na přijatých podporách je pod průměrem právě jediné minimum.
   Počet takových hodů pro A je tedy přesně

```
Σ_{a je fyzická stěna A} #{b>a}·#{c>a}.
```

   Přijmou se jen trojice, kde je tento počet72 pro každou
   kostku. To je ekvivalentní třem nadprůměrným pravděpodobnostem2/3.
   Každý přijatý výsledek se ještě ověřuje původními
   nerovnostmi ve všech216 hodech.

Úplný podporový průchod dal367 slučitelných trojic podpor.
Podle počtů kompozic představují celkem jen8 025 trojic
distribucí; ty byly všechny posouzeny. Vyšla právě jedna
neuspořádaná trojice, totožná s vytištěným druhým diagramem.
Tím je prověřena tištěná jedinečnost při optimálních2/3,
nikoli nesprávný výklad, že přidání hodnoty7 odstraní původních
osm řešení s nižšími pravděpodobnostmi.

Podporový předvýpočet trval0.053039s a je zachován v
`results/sequential/mpr-003-seven-supports.json`. Byl pořízen
jednou jako malá velikostní/prostorová kontrola při běžné
prioritě0; nebyl následně opakován. Navazující kontrola8 025
trojic tento soubor převzala pomocí `--resume-supports`,
trvala0.028045s s nice15 a měla limit10s. Přesná existence
a počet řešení jsou v `results/sequential/mpr-003-seven.json`.
Zdroj obsahuje i původní podporový postup, aby byl certifikát
reprodukovatelný; žádný z obou dokončených průchodů znovu
nespouštíme. Všechny smyčky jsou explicitně omezené126
podporami, nejvýše127 podmaskami a konečným seznamem četností.
Žádný dlouhý census ani náhodné hledání nebyl zahájen.

## Errata, výjimky a rozsah

Všech šest místních vrstev errat a dostupné původní TeXy byly
porovnány pro zadání12, odpověď371 a odpovídající Fascicle5
str.183. Žádná matematická ani diagramová oprava MPR3 nebyla
nalezena. Sousední doplnění Komisarski k odpovědi2 je již E118,
nikoli další změna úlohy3. J. Moraleda a D. G. Stork,
College Mathematics Journal43(2012),152–159, jsou výslovně
bibliograficky vynecháni; potřebná matematika a úplné konečné
počty byly dokázány zde, bez převzetí jejich neviděného textu.

D106 uzavírá celé zadání3 i všechny věty a diagramy odpovědi3.
File32 zůstává partial kvůli úloze4 a file391 partial kvůli
odpovědím4 a následujícím. D105 ani starší dokončené výpočty
se neopakovaly. Žádný nový nález nebo kandidát.

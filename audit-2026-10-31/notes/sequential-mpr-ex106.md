# MPR106: úplné fáze d-ární koalescence

7. listopadu 2026. Zadání p22/file42, odpověď p386/file406,
autorský PS11.9.2019 p22/file28 a p43/file49 přímo zobrazeny.
Všech šest vrstev errat a tři TeX zdroje bez použitelné opravy.
Celá105/D203 je převzata přesně pro rozdělení času absorpce
férové procházky v intervalu[0,t]; žádný starý běh se neopakuje.

## Stav a všechny přechody

Počet číslic d je kladný. Pro d1 je pole už konstantní, N0;
prázdný součin GF je1 a obě finální binomické formule dávají0.
Dále d≥2. Označme pole A_0,…,A_(d−1), aby se nepletlo s jeho
nejmenší hodnotou a. V103(b) se skládá zprava, takže bit0 vytvoří

```
(A_0,A_0,A_1,…,A_(d−2)),
```

a bit1 vytvoří

```
(A_1,A_2,…,A_(d−1),A_(d−1)).
```

První krok tedy duplikuje první položku a zahodí poslední, druhý
zahodí první a duplikuje poslední. Jde o současné aktualizace.

Před koalescencí má pole přesně tvar

```
a^r (a+1)(a+2)…(b−1) b^s,
0≤a<b<d, r,s≥1, r+s+b−a=d+1.
```

Počet položek je r+(b−a−1)+s=d, i když prostřední úsek je
prázdný. Počáteční pole0,1,…,d−1 má a0,b=d−1,r=s1.
Následující úplná tabulka ověřuje invariant i všechny hrany:

|Bit a podmínka|Nové hodnoty před koalescencí|Změna|
|---|---|---|
|0, s>1|a,b,r+1,s−1|Rozsah b−a beze změny|
|0, s=1, b−a>1|a,b−1,r+1,1|Rozsah se zmenší o1|
|0, s=1, b−a=1|Celé pole má hodnotu a|Koalescence|
|1, r>1|a,b,r−1,s+1|Rozsah b−a beze změny|
|1, r=1, b−a>1|a+1,b,1,s+1|Rozsah se zmenší o1|
|1, r=1, b−a=1|Celé pole má hodnotu b|Koalescence|

Každý řádek plyne z právě zapsané duplikace a odstranění krajní
položky. Zahrnuje všechny možnosti, udržuje počet d i meze hodnot.
Indukce proto dokazuje invariant po celou dobu, nikoli pouze jeho
platnost v prvním kroku.

## Přesné fáze a jejich podmíněné zákony

Položme t=r+s=d+1−(b−a). Před koalescencí t nabývá postupně
hodnot2,3,…,d. Uvnitř jedné fáze t zůstává pevné a
r∈{1,…,t−1} provádí férovou procházku: bit0 zvyšuje r o1,
bit1 jej snižuje o1. První dosažení r=t nebo r=0 ukončí fázi.
Pokud t<d, přechod do další fáze t+1 má vstupní r=t nebo r=1;
to jsou právě dva sousedé absorpčních hranic nového intervalu.
Pokud t=d, tento přechod znamená koalescenci. Žádnou fázi nelze
přeskočit a žádná se po opuštění znovu nevrací.

V počáteční fázi2 je r1. Při vstupu do každé další fáze může být
r1 nebo t−1. Oba starty mají stejný čas absorpce podle explicitní
reflexe v105. Proto každá fáze t má GF G_t času zásahu0/t při
startu1, přesně jak tvrdí odpověď. Označme její délku H_t.

Je třeba ještě odůvodnit nezávislost, kterou součin GF vyžaduje.
Po jakémkoli konečném zastavovacím čase S má následující konečné
slovo k bitů pravděpodobnost2^−k podmíněně každou konkrétní
historií do S: událost dané historie je určena prvních S bity
a další bity jsou nezávislé. Sečtením přes disjunktní hodnoty S
a historie to platí pro celé informace do S. Každá fáze skončí
skoro jistě s exponenciálním ocasem podle105; konečná indukce
tedy dovoluje tento argument použít ve všech fázích.

Zákon H_t podmíněný celou minulostí je vždy G_t, protože obě
možné vstupní orientace dávají stejný zákon. Postupné podmiňování
proto dává nezávislost H_2,…,H_d a

```
N=H_2+…+H_d,
E z^N=G_2(z)G_3(z)…G_d(z).
```

To dokládá přesně tištěný součin, včetně jeho probabilistického
předpokladu. Každý faktor je v105 explicitní:

```
G_(2m)=z t_(m−1)/t_m,
G_(2m−1)=z u_(m−1)/u_m pro m≥2.
```

Polynomy t,u a všechny odstranitelné hodnoty poměrů jsou úplně
doloženy v105. Součin konečně mnoha těchto GF je platný v okolí1,
kde žádný jmenovatel není nula. Celkové N je konečné skoro jistě
a má oba konečné momenty.

## Každý momentový součet a náklady

Z105 při a1,n=t je EH_t=t−1 a

```
VarH_t=(((t−1)²+1−2)(t−1))/3
      =t(t−1)(t−2)/3=2 binom(t,3).
```

Průměry se sčítají vždy; variance se sčítají díky právě dokázané
nezávislosti. Proto

```
EN=Σ_(t=2)^d(t−1)=d(d−1)/2=binom(d,2),
VarN=2Σ_(t=2)^d binom(t,3)=2 binom(d+1,4).
```

Poslední rovnost je součet Pascalových rozdílů
binom(t,3)=binom(t+1,4)−binom(t,4); dolní člen binom(2,4)=0.
Vzorce tedy zahrnují i t2, kdy je délka1 deterministická, d2,
kdy je N1, i výše oddělené d1. Pro d3 dávají EN3 a VarN2,
ve shodě s103. Žádné numerické dosazování není místo důkazu.

Doslovná pole algoritmu vyžadují d přiřazení na jeden krok
a O(d) slov paměti; celkový počet těchto přiřazení je dN,
v průměru d·binom(d,2), plus inicializace. Počet náhodných bitů
je právě N. Ukončení nastane až po poslední fázi, kdy tabulka
ověřuje společnou hodnotu všech položek. Není předpokládán
jiný zastavovací test ani neprovedená simulace.

Celá106 checked. Žádný nález, bibliografická výjimka, nový výpočet
či restart. Ostatní úlohy na p22/p386 tím nejsou uzavřeny.

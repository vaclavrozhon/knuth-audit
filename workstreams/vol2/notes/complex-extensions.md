# §4.1: další komplexní základy na stranách 205 a 607

## Rozsah

Zde jsou obecné důkazy tvrzení o základech `−d±i`, `2+i` a `i sqrt(2)`.
Gaussovská celá čísla jsou čísla `x+iy` s celými souřadnicemi; `|z|`
označuje eukleidovskou délku. Zápis má konečný nejvyšší exponent, ale
záporné exponenty mohou pokračovat do nekonečna. Jednoznačnost se níže
vztahuje pouze na **konečné celočíselné zápisy**, s ignorováním úvodních nul.
Obecné komplexní zlomky jednoznačné být nemusí.

Originály knihy 205 a 607 byly přečteny vizuálně. Článek I. Kátai,
J. Szabó, *Canonical number systems for complex integers*, Acta Sci. Math.
37 (1975), 255–260, byl získán z
[univerzitního archivu](https://acta.bibl.u-szeged.hu/14536/1/math_037_fasc_003_004_255-260.pdf)
a všech šest původních stran bylo přečteno vizuálně.
[PDF](../sources/katai-szabo-1975.pdf), [metadata](../sources/katai-szabo-1975.json).
Jeho Theorem 1 odpovídá §1 níže, Theorem 2 přechodu na všechna komplexní
čísla v §3. Nortonův článek citovaný knihou, Math. Mag. 57 (1984), 250–251,
nebyl získán; matematická část je doložena vlastním krátkým důkazem v §2.
Prvenství ani úplnost historického seznamu tím ověřena není.

[Program](../verify_complex_extensions.py) porovnává nezávislou polynomiální
normalizaci s nuceným dělením a rekonstruuje hodnoty Hornerovým schématem.
Dva bloky [výsledků](../results/complex-extensions.json) prošly s exit 0:
3185 vstupů pro první rodinu, 9088 normalizačních kroků a 4225 Nortonových
vstupů s 21804 přísnými poklesy čtverce délky. Neopakovaly se úspěšné
kontroly předchozího programu pro základ `−1+i`.

## 1. Kátaiova–Szabóova rodina

Pro kladné celé `d` položme `β=−d+i`, `N=d²+1` a použijme cifry
`0,1,...,N−1`. Zbytkovou třídou čísla `x+iy` při dělení β je
`x+d y mod N`: dosazení `i=d` do `i²+1` dává právě násobek N.
Přesněji má `(z−r)/β` celé souřadnice právě tehdy, když
`r=x+d y mod N`. Jeho souřadnice jsou

```
q = ((−d(x−r)+y)/N) + i (−(x−r)−d y)/N.          (1)
```

Cifra r i podíl q jsou tedy nucené. Zbývá dokázat, že opakované dělení
někdy dorazí do nuly. Pouhé zmenšování délky mimo konečný disk by ještě
nevyloučilo cyklus v disku.

Použijeme polynom s nezápornými celočíselnými koeficienty. Nejdříve
`z=(x+d y)+yβ`. Každý záporný koeficient lze nahradit pomocí identity

```
−1 = β²+2dβ+d².                                   (2)
```

Získáme `z=P(β)`, kde P má nezáporné koeficienty a stupeň nejvýše 3.
Druhá přesná identita je

```
N = β³+(2d−1)β²+(d−1)²β.                          (3)
```

Váha W polynomu znamená **součet jeho koeficientů**, nikoli absolutní
hodnotu P(β). Je-li konstantní koeficient `c0=tN+r`, `0<=r<N`, nahradíme
`tN` pravou stranou (3). Všechny koeficienty zůstanou nezáporné a W se
nezmění, protože `1+(2d−1)+(d−1)²=N`. Odebrání r a dělení polynomu
proměnnou sníží W právě o r. Hodnota nového polynomu je podíl (1).

Předpokládejme pro spor, že nenulový zbytek nikdy nedorazí do nuly.
Nezáporné celé W může klesnout jen konečněkrát, takže od jistého okamžiku
jsou všechny další r nulové. Nenulové Gaussovské celé číslo v tomto
okamžiku by pak bylo dělitelné β^k pro každé k. Jeho kladný celočíselný
čtverec délky by byl dělitelný `N^k` pro každé k, což není možné.
Existence konečného zápisu je dokázána. Nucenost (1) dokazuje jednoznačnost.
Komplexní sdružení dává totéž pro `−d−i`.

**Ukončovací podmínka se týká hodnoty P(β).** Nenulový polynom s nezápornými
koeficienty může mít hodnotu nula, například `P(X)=X²+2dX+N`. Jeho
normalizace může cyklit. Algoritmus proto zastaví při nulovém zbytku,
nikoli až při prázdném seznamu koeficientů. Ve zkoušených vstupech se tento
rozdíl projevil 1674krát; nenarušuje důkaz konečné ciferné reprezentace.
Na straně 257 externího článku je navíc v jedné pomocné řádce vytištěno
`−t(A+1)²`; odpovídající odečtený násobek je `−t(A²+1)`. Zde se používají
přímé identity (2)–(3). Nejde o nález v Knuthově knize.

Pro úplnost ověřujeme i nutnost klasifikace z Theorem 1. Je-li
`β=A+iB` Gaussovské celé a cifry jsou `0,...,A²+B²−1`, pak při `|B|>1`
je imaginární souřadnice každého konečného zápisu dělitelná B; číslo i
nemá zápis. Pro `B=0` jsou všechny hodnoty reálné. Pro `B=±1,A>=1`
je nenulové `z=1−conj(β)` pevný zbytek, neboť

```
z = βz+r,       r=A²+B²−2A+1,       0<=r<A²+B².
```

Nucené dělení nikdy neskončí. Pro `A=0,B=±1` je jediná cifra nula.
Zbylé možnosti jsou právě `A<0,B=±1`, dokázané výše.

## 2. Nortonův základ 2+i

Položme `β=2+i` a `D={0,1,−1,i,−i}`. Zbytková mapa
`x+iy -> x−2y mod 5` zobrazuje těchto pět cifer na různé třídy
`0,1,4,3,2`. Každé z tedy má jedinou cifru δ takovou, že
`q=(z−δ)/β` je Gaussovské celé číslo.

Pro každé nenulové Gaussovské celé z platí `|z|>=1` a `|δ|<=1`, takže

```
|q| <= (|z|+1)/sqrt(5) < |z|,
```

protože `1/(sqrt(5)−1)<1`. Nezáporný celočíselný čtverec délky přísně
klesá; dělení tedy skončí v nule. Existence i jednoznačnost konečných
zápisů jsou dokázány bez konečného vyhledávání cyklů.

## 3. Přechod od Gaussovských celých čísel ke všem komplexním číslům

Následující argument platí pro obě předchozí rodiny. Předpokládejme
Gaussovský celočíselný základ β s `|β|>1`, konečnou cifernou množinu D
obsahující nulu a konečný zápis každého Gaussovského celého čísla.
Označme `M=max(δ in D)|δ|`.

Pro libovolné `z in C` zvolme Gaussovské celé `w_n` nejbližší `β^n z`.
Pak `z_n=β^(−n)w_n -> z`. Po odebrání n nejnižších cifer w_n zbude
Gaussovské celé `r_n` a geometrická řada dává

```
|r_n| <= |z_n| + M/(|β|−1).
```

Posloupnost r_n je omezená, a tedy nabývá jen konečně mnoha mřížových
hodnot. Jejich konečné zápisy mají jednotně omezený nejvyšší exponent,
řekněme nejvýše `L−1`, s `L>=1`. Stejnou mez mají zápisy všech z_n,
protože odebraná část po posunu čárky obsahuje pouze záporné exponenty.

Množina S všech ryze zlomkových zápisů je kompaktní: z každé posloupnosti
lze diagonálně ustálit jednotlivé cifry a zbytek řady je jednotně omezen
`M |β|^(−k)/(|β|−1)` po k cifrách. Všechna z_n patří do uzavřené
množiny `β^L S`; jejich limita z tam patří také. To dokazuje existenci
zápisu každého komplexního čísla. Netvrdí to jednoznačnost jeho
nekonečné zlomkové části ani to, že samotná omezená S pokrývá celou rovinu.

## 4. Základ i sqrt(2) a Grünwaldova úprava

Pro `γ=i sqrt(2)` platí `γ²=−2`. Rozdělení sudých a lichých pozic dává
každý zápis s ciframi 0,1 ve tvaru `E+i sqrt(2) O`, kde E i O mají
negabinární zápis (základ −2). Každé reálné číslo takový zápis má,
proto se tím reprezentuje každé komplexní číslo.

Kdyby zápis čísla i byl nakonec periodický, byly by nakonec periodické
i obě podposloupnosti sudých a lichých cifer. Součet každé je racionální,
protože periodický ocas je geometrická řada. Muselo by však platit
`O=1/sqrt(2)`, což je iracionální. Zápis i proto nemůže být nakonec
periodický, ani konečný. Tvrzení knihy odpovídá tomuto důkazu.

Grünwaldova úprava připouští na lichých pozicích cifry `0,1/sqrt(2)`.
Hodnoty pak mají tvar `E+i O`, a pokrytí celé roviny tím **nezaniká**.
Nevýhoda je ztráta stejné ciferné abecedy na všech pozicích a obvyklého
významu posunu o jednu pozici. Například každý konečný takový zápis má
obě souřadnice dyadicky racionální (celá čísla dělená mocninou 2), ale
posunutí zápisu 1 o jednu pozici by mělo představovat `i sqrt(2)`, které
konečný zápis tohoto typu nemá. Hodnotící větu knihy o pokažení systému
proto nevykládáme jako nepravdivé tvrzení o ztrátě reprezentovatelnosti.

Všechny relevantní vrstvy errat jsou zachyceny v
[positional-errata-excerpts.txt](../sources/positional-errata-excerpts.txt).
Z tohoto doplňkového matematického bloku nevzešel nový nález.

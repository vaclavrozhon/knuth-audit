# §1.2.6, s. 64–65: rozsah algoritmického sčítání

Audit 1. listopadu 2026. Knižní stránky byly zobrazeny.
Citovaná kniha Petkovšek–Wilf–Zeilberger, *A=B* (1996),
je získána z Rutgersovy univerzity; dostupný PDF soubor má
vlastní datum 27. dubna 1997. Přečteny a zobrazeny tištěné
s. 17–19 a 88–89 (strany souboru 28–30,98–99).

## Co znamená uzavřený tvar

Posloupnost t(k) je zde hypergeometrická, jestliže poměr
t(k+1)/t(k) je racionální funkce k. Případné další
parametry se ponechávají jako symboly v koeficientech.
Racionální funkce je podíl dvou polynomů. Antidiference
t je posloupnost H s `H(k+1)−H(k)=t(k)`.

Gosperův algoritmus rozhoduje o hypergeometrické
antidiferenci. Zeilbergerova metoda konstruuje rekurence
pro určité součty; další algoritmy z *A=B* rozhodují
o jejich řešeních ve vymezené třídě. Na s. 19 zdroj
výslovně omezuje „closed form“ v zásadě na lineární
kombinaci pevného počtu hypergeometrických členů, za
dalších předpokladů na vstup. Na s. 88 rozlišuje obecný
prefix binomického součtu od speciálního součtu celého řádku.
To podporuje kvalifikaci „in many important cases“
v TAOCP; nejde o algoritmus pro libovolné významy slova
„jednoduchý“ nebo pro libovolné elementární funkce.

Tato kontrola uzavírá správnost odkazu a rozsahu tvrzení.
Není auditem všech algoritmů v externí knize, které TAOCP
výslovně odkazuje mimo svůj rozsah.

## Definice (39)

Rostoucí mocnina `a^[k]=a(a+1)...(a+k−1)` má při k=0
hodnotu 1. Koeficient uvedené zobecněné hypergeometrické
řady je `c_k=product_i a_i^[k]/(k! product_j b_j^[k])`.
Při nesingulárních parametrech je
`c_(k+1)/c_k=product_i(a_i+k)/((k+1)product_j(b_j+k))`,
tedy skutečně racionální funkce k. Dolní parametry
0,−1,... vyžadují zvláštní limitní či ukončovací konvenci;
základní definice se na ně bez dalšího nevztahuje.

Pro neukončenou řadu s m horními a n dolními parametry
poměrové kritérium dává poloměr konvergence infinity pro
m<=n, 1 pro m=n+1 a 0 pro m>n+1. V posledním případě
jde bez dalšího pokračování jen o formální řadu. Ukončení
nastane při nekladném celém horním parametru, pokud mu
nepředchází nula ve jmenovateli. TAOCP v (39) vypisuje
definici a odkazuje další teorii; netvrdí zde konvergenci
pro všechny parametry a z.

## Vlastní důkaz pro obecný binomický prefix

Nechť m je neurčitá, tedy nikoli předem zvolené celé číslo,
a `t(k)=C(m,k)`. Pracujeme nad polem racionálních funkcí
v m. Předpokládejme, že má t hypergeometrickou antidiferenci H.
Z `t(k)=H(k)(H(k+1)/H(k)−1)` plyne, že H(k)/t(k) je
racionální funkce k. Zapíšeme ji jako k x(k), kde x
je také racionální. Protože
`t(k+1)/t(k)=(m−k)/(k+1)`, musí platit

```text
(m−k)x(k+1)−k x(k)=1.                                   (G1)
```

Předpokládejme nejprve, že x má konečný pól. Rozdělíme
jeho konečně mnoho pólů do tříd, v nichž se liší o celé
číslo. V jedné třídě zvolme nejnižší pól alpha a nejvyšší
pól beta podle tohoto celočíselného posunu. V bodě
k=alpha−1 nemá x(k) pól; pól x(k+1) se proto v (G1)
může odstranit jedině nulou m−k, takže alpha=m+1.
V bodě k=beta nemá x(k+1) pól; nutně beta=0.
To by znamenalo `beta−alpha=−m−1` nezáporné celé číslo,
což je pro neurčitou m nemožné. Póly bereme v algebraickém
uzávěru koeficientového pole, takže argument nevylučuje
jen racionální kořeny jmenovatele, ale všechny.

x tedy nemá konečné póly a musí být polynom. Je-li nenulový
stupně d s vedoucím koeficientem a, levá strana (G1)
má vedoucí člen `−2a k^(d+1)`, a nemůže být rovna 1.
Nulový polynom také nevyhovuje. Hypergeometrická antidiference
tedy neexistuje. Důkaz nevylučuje speciální dosazení m:
například pevné záporné celé m mají v TAOCP popsané
prefixové formule a konečný celý řádek dává 2^m.

Neprohlašujeme tím neexistenci reprezentace pomocí
neúplné beta funkce či jiných nově zavedených funkcí;
takové tvrzení by mělo jiný, zde nestanovený význam.

Zdroj: [autorský PDF soubor A=B](https://sites.math.rutgers.edu/~zeilberg/AeqB.pdf).
Hash, datum získání a přesné stránky jsou v sousedních
metadatech `sources/petkovsek-wilf-zeilberger1996-aeqb.metadata.json`.


## Recovery supplement, 6 November 2026

The full sufficient algorithmic proof chain is now recorded in
`quality-recovery-hypergeometric-decision-2026-11-06.md`, with finite
searches, invariants, degree bounds and termination. Its source manifest
records the additional exact A=B pages read. This extends the older
source-scope-only discussion above without claiming a whole-book audit.

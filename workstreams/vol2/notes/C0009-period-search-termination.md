# V2-C0009: chybějící růst period v §3.2.2-11(c) a 26

**Stav: confirmed, 1. listopadu 2026; rozšířen o neplatnou mez discrepancy.**
Původně jsme nález hodnotili jako drobnou chybějící podmínku návodu.
Tentýž příklad však splňuje i předpoklady poznámky v úloze 26 a vyvrací
její odhad discrepancy, tedy odchylky četností bodů od objemu obdélníků.
Přesná definice a výpočet jsou níže v oddílu „Úloha 26“.
Obě místa evidujeme pod jedním ID, protože chybí stejný předpoklad růstu.

Samotné tvrzení 11(c) o dalším růstu periody je správné. První část nálezu
se vztahuje na parentetický předpis na [str. 37](../images/vol2-p037.png):
počítat periody modulo 4,8,16,... až do prvního rozdílu od periody modulo 4.
Takový první rozdíl nemusí existovat za dovolených předpokladů úlohy.

## Přesný příklad

Zvolme k=2, a_1=1, a_2=-1. Potom f(z)=1-z+z^2 a univerzální
posloupnost A_n definovaná koeficienty 1/f má tvar

```
A_0,A_1,... = 1,1,0,-1,-1,0,1,1,0,-1,-1,0,... .
```

Identita f(z)(1+z)=1+z^3 dává přesně

```
1/f(z) = (1+z)(1-z^3)/(1-z^6).
```

Perioda je tedy 6 už nad celými čísly. Modulo 2^e pro každé e>=2
zůstává **nejmenší** periodou 6: periodu 1 a 2 vylučuje A_0!=A_2,
periodu 3 vylučuje A_0=1 != -1=A_3 modulo 4. Každá nejmenší perioda
musí dělit 6, takže menší možnost nezbývá. V předepsaném hledání proto
lambda(4)=lambda(8)=lambda(16)=...=6 a zastavovací podmínka nikdy nenastane.
Příklad má nenulový poslední koeficient a neobsahuje přechodný úvod.

## Přesný rozsah opravy

Stačí návod podmínit existencí e s lambda(2^e)!=lambda(4), například
požadavkem, že tyto periody nejsou omezené. Jakmile první rozdíl nastane,
část (c) správně určí všechny další periody. Samotný postup postupného
testování však neumí po konečném počtu stejných hodnot rozhodnout,
že ke změně nikdy nedojde. Tento nález nedoplňuje obecný rozhodovací
algoritmus pro druhou větev a nezpochybňuje hlavní větu.

Nejde o tvrzení o běžně voleném náhodném generátoru: jde o univerzální
návod uvnitř úlohy, která výslovně připouští libovolné celočíselné
koeficienty.

[verify_period_lifting.py](../verify_period_lifting.py) potvrzuje konstantní
periodu pro e=2,...,16; algebraická identita výše pokrývá všechna e.
[Výsledky](../results/period-lifting.json).

## Úloha 26: nesplněná mez discrepancy

Poznámka na [str. 39](../images/vol2-p039.png) tvrdí: je-li perioda
modulo p maximální, lambda_1=p^k-1, a platí-li domněnka o počtu nul,
pak k-rozměrná discrepancy je O(alpha^k p^(-alpha/(k-1))) pro alpha→∞.
Zde lambda_alpha označuje nejmenší periodu modulo p^alpha a N_alpha
počet nul v jednom jejím opakování. Domněnka požaduje konstantu c
nezávislou na alpha a počátečních hodnotách, pro niž
N_alpha<=c p^(alpha(k-2)/(k-1)).

Položme p=2, k=2 a X_n=X_(n-1)-X_(n-2) modulo 2^alpha.
Charakteristický polynom t²-t+1 je modulo 2 primitivní: jeho kořen
v tělese se čtyřmi prvky má multiplikativní řád 3. Počáteční dvojice
(1,1) dává modulo 2 periodu 3=2²-1, jak poznámka vyžaduje.
Dokonce i primitivita, chybějící v samotné domněnce (C0010), zde platí.

Přechod dvojic má celočíselnou matici

```
T = [ 0  1 ],    T³=-I,    T⁶=I.
    [-1  1 ]
```

Každá počáteční dvojice má proto modulo libovolné 2^alpha periodu
dělící 6; N_alpha<=6 pro **všechny** počáteční hodnoty i alpha.
Domněnka je pro tuto pevnou rekurenci splněna s c=6, neboť k=2
a její exponent je nula. Neověřujeme ji pouze pro vybranou dvojici.

Discrepancy množiny s četnostmi definujme jako supremum absolutního
rozdílu mezi relativním počtem bodů v obdélníku a objemem obdélníku.
Pro m=2^alpha, alpha>=2, má dvojice (1,1) periodu 6. Její sousední
normalizované dvojice jsou

```
(1/m,1/m), (1/m,0), (0,1-1/m),
(1-1/m,1-1/m), (1-1/m,0), (0,1/m).
```

Obdélník [0,1/2)×[0,1/2) obsahuje právě tři ze šesti bodů, ale jeho
obsah je 1/4. Discrepancy je tedy nejméně |3/6-1/4|=1/4 pro každé
alpha>=2. Platí to i pro variantu používající jen obdélníky ukotvené
v počátku. Tvrzená horní mez O(alpha² 2^(-alpha)) by naopak šla k nule.

Předpoklad neomezeného, posléze p-násobného růstu period je proto
podstatný i pro tento závěr. Tento protipříklad nevyvrací zamýšlenou
verzi s rostoucími periodami; její úplné obecné znění zde nedokazujeme.
Kontext primárního Reiserova pramene je v [samostatné poznámce](reiser-conjecture.md).

[verify_reiser_hypotheses.py](../verify_reiser_hypotheses.py) ověřil všech
21 844 počátečních dvojic modulo 2,...,128 a přesnou odchylku v 19
obdélnících pro alpha=2,...,20. [Výstup](../results/reiser-hypotheses.json).
Obecný důkaz je maticová identita a počítání výše, nikoli konečný test.

## Zdroje a errata

Prohledány all2-prepre, all2-pre, all2, err2 i err2.textxt z 1. 11. 2026
podle str. 37,39,553–557, jména Reiser a obsahu tvrzení. Opravy 18. 2. 2004 a 28. 4. 2017
mění indexy v důkazech, nikoli tento předpis; jiná oprava nenalezena.
Zásahy na str.39 z let 2001,2016,2024 patří úlohám 21,19,27.

Navíc byly vizuálně zkontrolovány [str.37](../images/publisher-preview-p037.png)
a [str.39](../images/publisher-preview-p039.png) v distribučním náhledu,
jehož [tiráž](../images/publisher-preview-copyright.png) uvádí osmé
digitální vydání, červenec 2026. Obě formulace přetrvávají.
[Metadata a původ](../sources/publisher-preview-9780133488791.json).
Novější fyzický dotisk ani prvenství neověřeny.
[ASCII draft](../reports/C0009-period-search-termination-draft.txt) nebyl odeslán.

Dodatečný primární doklad: Brentův článek o periodách (1994),
[str.4 autorské verze](../images/brent-fibonacci-p04.png), výslovně
uvádí f=1-x+x² s periodou3 modulo2 a6 modulo všech vyšších mocnin2.
Tento jev tedy není nový; nález se týká chybných aplikací v knize.
[Zdroj a metadata](../sources/brent-1994-fibonacci.json).

# Self-dualizace a úplný optimalizační postup102–103

7. listopadu 2026. §7.1.1–102/103, p92/file109 a p552/file569;
také dopředná povinnost P1065 z p76/file93. P1084–P1091, X0116.
Původní sazba zadání i odpovědi zobrazena. Žádné LP, větvení,
enumerace ani jiný matematický program se nespouštěly.

## 1. Oba výrazy102 a jejich self-dualita

Pišme Df(x)=1−f(¬x). Oba vytištěné výrazy pro f̂ mají při
x_0=1 hodnotu f(x) a při x_0=0 hodnotu Df(x):

    f̂=(x_0∧f)∨(¬x_0∧Df)
      =(¬x_0∨f)∧(x_0∨Df).

Tím je jejich rovnost dokázána pro všechny funkce, včetně
konstant. Při současné komplementaci x_0,x se větve vymění
a jejich výsledky se komplementují, protože Df(¬x)=1−f(x).
Proto f̂(¬x_0,¬x)=1−f̂(x_0,x), přesně část(a).
Je-li f samo self-duální, obě větve jsou stejné a x_0 je
nepodstatná. Nulární konstantní f=0/1 dává ¬x_0/x_0;
žádná okrajová větev se neztrácí.

Známé erratum ze17.7.2011 mění v odpovědi102 odkaz(1)/(2)
na(11)/(12), tedy De Morganovy zákony. Jejich přesné důkazy
P0521/P0522 jsou v proof-028; zde se nepovažuje chybný starý
odkaz za nový nález a výpočet větví funguje nezávisle na něm.

## 2. Přesný váhový převod102(b), oba směry

Nechť f(x)=[S≥t], S=Σw_jx_j, W=Σw_j, se všemi parametry
celočíselnými. Vytištěný nový threshold je

    [(W+1−2t)x_0+S ≥ W+1−t].

Při x_0=1 se zkrátí na S≥t. Při x_0=0 je podmínka
S≥W+1−t. Díky integrálnosti je to přesně negace W−S≥t,
tedy Df(x), neboť W−S=Σw_j(1−x_j). Převod proto platí
pro libovolná znaménka vah, nulové váhy i konstanty.
Opačně je f=f̂(1,x) cofactor prahové funkce; dosazení1 do
jejího prahu jen odečte váhu x_0. Obě implikace jsou dokázány.
Součet W a nové dva parametry se vypočtou v O(n) aritmetických
operacích, bez růstu počtu původních proměnných kromě x_0.

## 3. Úloha103: přesná vstupní doména a nutnost LP

Vstup je **úplný seznam** minimálních pravdivých podpor B
monotónní self-duální funkce f. Pro n=0 taková funkce neexistuje;
pro n≥1 není konstantní, seznam není prázdný a neobsahuje
prázdnou podporu. Původní otázka nedává pouze neúplný vzorek
implikantů. Matice má pro každé B řádek a_B s položkou+1 na B
a−1 mimo B. Posuzovaný program je přesně

    minimalizuj W=Σw_j,
    w_j≥0,       a_B·w≥1 pro všechny prime podpory B.       (LP)

Nejprve nutnost. Je-li f monotónní a prahová, případná záporná
váha může patřit pouze nepodstatné proměnné: prahový test by
při jejím zvýšení jinak klesl, proti monotónnosti. Váhu takové
proměnné lze nahradit0, protože cofactor x_j=0 je již celé f.
Tím získáme nezáporné váhy bez změny funkce. Self-dualita podle
proof-085, §2, vylučuje dosažitelnou polovinu jejich součtu
a určuje funkci jako ostrou většinu. Po případném převodu
na celočíselnou lichou reprezentaci z téhož důkazu mají všechny
pravdivé podpory podepsanou mezeru nejméně1. Zvláště všechny
prime podpory splňují(LP). Nulové váhy jsou přípustné.

## 4. Postačitelnost všech omezení pro každý vstup

Nechť naopak reálné nezáporné w splňuje(LP). Každý pravdivý
vstup x obsahuje některou prime podporu B, takže z w≥0 plyne

    2w·x−W ≥ 2w·1_B−W = a_B·w ≥1.

Je-li f(x)=0, self-dualita dává f(¬x)=1 a z již dokázaného
plyne2w·x−W≤−1. Máme tedy přesnou real-valued threshold
reprezentaci, bez vázaných výsledků na polovině součtu.
Proof-083 dovoluje převod na celá čísla; samostatný přímý
převod vhodný pro optimalizaci je níže. Úplnost seznamu prime
podpor i self-dualita byly použity na přesně uvedených místech.

Takže prázdná přípustná množina skutečně znamená, že f není
prahová. Zápis minimum=+∞ v odpovědi je standardní hodnota
pro nepřípustnou minimalizaci; neomezenost dolů je vyloučena
podmínkou w≥0.

## 5. Minimum existuje a má racionální reprezentaci

Máme-li nějaké přípustné u s U=Σu_j, omezme se na uzavřenou
množinu0≤w_j, Σw_j≤U a ostatní nerovnosti. Je neprázdná
a kompaktní, takže lineární minimum existuje. Není to pouze
nedosažené infimum.

V optimálním bodě zvolme nenulový směr d kolmý ke všem
aktivním řádkům, pokud ještě nemají hodnost n. Malé posuny
v obou směrech zachovají přípustnost, protože neaktivních
omezení je konečně mnoho a mají kladné rezervy. Z optimality
nutně Σd_j=0. Posuňme se tedy bez změny cíle až k prvnímu
novému aktivnímu omezení. Konečný bod existuje: vhodné znaménko
d snižuje některou souřadnici a nezápornost ji ohraničuje.
Nový řádek zvyšuje hodnost, protože jeho součin s d není0.
Po nejvýše n zvýšeních dostaneme n nezávislých aktivních
celočíselných rovnic s celočíselnými pravými stranami.
Cramerovo pravidlo dává racionální optimální bod.

Tento argument určuje potřebný výstup přesného racionálního
LP řešiče. Nevydáváme běžné zaokrouhlené floating-point řešení
za důkaz splnění všech omezení.

## 6. Celočíselnost, parita a skutečná délka většiny

Z jakéhokoli racionálního přípustného bodu lze kladným společným
jmenovatelem získat nezáporný celočíselný přípustný bod: všechny
mezery≥1 se tím jen zvětší. Je-li jeho součet W lichý, jde
přímo o většinu délky W, podle §4. Je-li W sudý, všechny
celočíselné hodnoty a_B·w=2Σ_{j∈B}w_j−W jsou sudé, tedy≥2.
Proto lze libovolnou kladnou váhu zmenšit o1: žádná mezera
neklesne pod1 a nezápornost se zachová. Taková váha existuje,
protože nulový vektor nesplní žádné prime omezení. Nový součet
je kladný a lichý a dává tutéž funkci.

Zvláště **celočíselný optimální bod původního LP nemůže mít
sudý součet**, jinak by právě uvedená změna zlepšila cíl.
Je-li tedy optimum LP celočíselné, jeho součet je opravdu
minimální délka dovolené liché většinové reprezentace. Stejný
argument dokazuje, že globální optimum celočíselného programu
má lichý součet. Podmínku lichosti není nutné dodatečně přidávat;
plyne z optimality, nikoli z libovolné integrální přípustnosti.

## 7. Co přesně znamená „přidávat další omezení“

Při necelém optimu nestačí zaokrouhlit váhy ani zvolit jednu
libovolnou větev. Následující konečné větvení dává obecný úplný
postup, který větu v odpovědi zpřesňuje bez změny jejího závěru.

1. Z racionálního přípustného bodu vytvoříme podle §6 platnou
   celočíselnou lichou reprezentaci délky U_0. Průběžnou nejlepší
   horní mez U inicializujeme na U_0.
2. Hledáme jen v0≤w_j≤U_0; každé lepší celočíselné řešení tam
   musí ležet. V každém uzlu řešíme(LP) se zděděnými omezeními.
   Nepřípustný uzel nebo uzel s dolní mezí≥U lze vypustit.
3. Je-li optimální bod necelý v souřadnici j s hodnotou v_j,
   rozdělíme uzel na obě větve w_j≤floor(v_j) a
   w_j≥ceil(v_j). Každé celočíselné řešení patří právě do
   jedné z nich. Nesmíme zapomenout druhou větev.
4. Je-li bod celočíselný, máme nové řešení. Jeho případný
   sudý součet lze zmenšit podle §6, i kdyby výsledný bod
   patřil mimo pomocné větvené omezení; původní(LP) stále
   splňuje a dává korektní globální horní mez. Tento uzel
   nepotřebuje další dělení.

Invariant: nejlepší dosud uložená reprezentace je vždy platná
a žádné lepší celočíselné řešení neleží mimo zbývající uzly.
Po jejich vyprázdnění je nalezené řešení optimální. Ukončení
není založeno na numerické toleranci: každé větvení zmenší
celočíselný interval některé souřadnice. V boxu je nejvýše
(U_0+1)^n celočíselných bodů; dělící boxy jsou disjunktní a
mají celočíselné neprázdné rozsahy. Strom má tedy nejvýše
2(U_0+1)^n−1 uzlů a každá větev hloubku nejvýše nU_0.
To je hrubá konečná mez, ne příslib polynomiální doby.

Při m prime termů sestavení husté matice stojí O(mn) operací
a uložení položek±1/0. Každá další podúloha je přesné racionální
LP s n proměnnými a těmito m základními podmínkami plus mezemi.
Kniha zde netvrdí konkrétní polynomiální mez integer optimalizace.
Výše uvedený postup je důkaz algoritmické úplnosti, nikoli
spuštěný census nebo doporučení jej na velkých instancích spouštět.

## 8. Vytištěný příklad, dřívější protipříklad a p76

Pro n=6 a prime podporu{2,5,6} je řádek přesně

    −w_1+w_2−w_3−w_4+w_5+w_6≥1,

jak stojí v odpovědi. Šestiproměnná mediánová funkce z odpovědi84
má již obecný vyvážený trade certifikát neprahovosti v proof-079;
nepřepočítává se. Podle obou právě dokázaných implikací její(LP)
skutečně nemůže být přípustné. Tento odkaz tedy nepředpokládá
nezopakovaný census šesti proměnných.

Obecný postup103 je nyní uzavřen, takže P1065 je checked a spolu
s proof-084 uzavírá celý matematický obsah p76. To neprohlašuje
konkrétní data a další algoritmusK z úlohy104 za zkontrolované;
ty následují zvlášť. Rovněž P1056, dopředné asymptotické srovnání
s112 na p552, zůstává partial.

## 9. Bibliografie a známá oprava

Primární článek Goto/Takahasi je uložen jako
`sources/goto-takahasi1962.pdf` ze
https://plouffe.fr/OEIS/OEISpdf/a000371_1.pdf. Je to **neúplný sken**
se stránkami747,748,750,751, nikoli ověření celého rozsahu747–752.
P747 má oba autory, název a přesnou mux definici self-dualizace;
originál této stránky byl zobrazen. Nepřebírá se z něj žádný
nezkontrolovaný census ani další věty. Přesný konec citovaného
rozsahu a celý historický článek zůstávají bibliografickou výjimkou.

Minnickův DOI10.1109/TEC.1961.5219146 nebyl dostupný přes primární
rozhraní; přesné historické místo a priorita LP metody se výslovně
přeskakují. Všechny potřebné matematické argumenty jsou výše.
Pět vrstev4A/F0 prohledáno podle stran a self-dualization/answer102/103;
známá oprava odkazů(11)/(12) je zohledněna bez karty či nového nálezu.

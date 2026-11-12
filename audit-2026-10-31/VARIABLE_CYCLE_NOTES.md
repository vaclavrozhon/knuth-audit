# Čtyři události z nezávislých proměnných: SAT 322

Kontrola 31. 10. 2026. A závisí na (W,X), B na (X,Y), C na (Y,Z)
a D na (Z,W); W,X,Y,Z jsou nezávislé. Obecná hranice z úlohy 321
je θ≈0.292893, zatímco v tomto proměnném modelu je hranice přesně 1/3.
Níže je nezávislé odvození včetně klasifikace kritických řešení.

## Podmínění a význam obrázku v části (a)

Při X=j,Z=l zůstávají W a Y nezávislé. Označme podmíněné pravděpodobnosti
a_j,b_j,c_l,d_l stejně jako kniha. Fréchetova mez dává

```
Pr(žádná událost | X=j,Z=l)
 = Pr(¬A_j∩¬D_l) Pr(¬B_j∩¬C_l)
 ≥ max(0,1−a_j−d_l) max(0,1−b_j−c_l).
```

Je-li pravděpodobnost vyhnutí nula, musí být pro každý j,l s kladnou
hmotností alespoň jedna z dvojic a_j+d_l nebo b_j+c_l ≥1.

Knižní rovnost čteme v kontextu „best way to allocate the events“:
jako hodnotu po extremálním přeuspořádání, nikoli jako identitu pro
libovolnou předem danou soustavu událostí. Při použití dvou nezávislých
rovnoměrných souřadnic můžeme umístit A_j,B_j k horním a D_l,C_l
k dolním koncům odpovídajících souřadnic a dosáhnout dolní meze
současně pro všechna j,l. Pro nutnou podmínku však stačí samotná
nerovnost; změna diskrétního pravděpodobnostního prostoru není potřebná.

Všechny **65 536** soustavy událostí na dvojicích čtyř férových bitů
potvrdily dolní mez přesným výčtem. V mnoha je ostrá, proto by čtení
jako obecné rovnosti bylo nesprávné. Tento rozdíl interpretace nevedeme
jako další nález, protože text výslovně zavádí nejlepší rozmístění.

### F032: v pravém obrázku jsou prohozené osy W a Y

Definice c_l používá jen Y a Z, definice d_l jen Z a W.
Po fixaci Z=l tedy C smí záviset jen na Y a D jen na W.
Pravý obrázek ale zobrazuje C jako svislý pruh podél vodorovné osy W
a D jako vodorovný pruh podél svislé osy Y. Prohodit popisky **W a Y
pouze v pravém obrázku** opraví tuto záměnu a sjednotí obrázek se
správným součinem (1−a_j−d_l)_+ (1−b_j−c_l)_+ pod ním.
Jde o grafický překlep, nikoli neplatnost hlavního výsledku.

## Redukce (b) na dvě hodnoty

Bod (p,p) je konvexní kombinací bodů (a_j,b_j). Dolní levý čtverec
[0,p]^2 proto protíná jejich konvexní obal. V rovině stačí najít
úsečku mezi dvěma původními body, která čtverec protíná: z trojúhelníku
v Carathéodoryho vyjádření lze přejít na jeho spodní nebo levý okraj;
nebo minimalizovat druhou souřadnici při první ≤p. Jediný vyhovující
bod lze použít dvakrát, takže váhu lze zvolit přísně mezi 0 a 1.
Stejně pro (c_l,d_l). Pro spočetné rozdělení argument platí také:
barycentrum omezené množiny v konečné dimenzi leží v jejím konvexním
obalu; na podpůrné přímce se všechny body s kladnou hmotností musí
nacházet rovněž a dimenze se sníží.

Dostaneme čtyři průměry nejvýše p,

```
μa+(1−μ)a′, μb+(1−μ)b′,
νc+(1−ν)c′, νd+(1−ν)d′,
```

a čtyři disjunkce `a_i+d_j≥1 nebo b_i+c_j≥1`, i,j∈{0,1}.
Každé políčko tabulky 2×2 obarvěme červeně, platí-li první možnost,
a modře, platí-li druhá. Pokud platí obě, můžeme si barvu vybrat.
To dává jen 16 vzorů; záměny řádků, sloupců, barev a transpozice
redukují kontrolu na následující čtyři typy.

## Úplná klasifikace při p=1/3

### Jediná barva ve všech čtyřech políčkách

Čtyři červené podmínky po váženém zprůměrování dávají
E a_i + E d_j≥1, což odporuje horní mezi 2/3. Modrá symetricky.

### Dvě sousední červená políčka

Zvolme červený první řádek a modrý druhý. Potom
`d,d′≥1−a` a `c,c′≥1−b′`. Jejich průměry ≤1/3 vynucují
`a,b′≥2/3`. Průměry v řádcích současně dávají
`μa≤1/3`, `(1−μ)b′≤1/3`, tedy μ=1/2 a a=b′=2/3.
Všechny zbývající nerovnosti jsou pak těsné:

```
a=b′=2/3, a′=b=0,
c=d=c′=d′=1/3, μ=1/2, libovolné 0<ν<1.
```

To je první knižní rodina řešení, včetně volné váhy ν.

### Dvě protilehlá červená políčka

Záměnami řádků, sloupců a případně barev lze současně dosáhnout
`0<μ,ν≤1/2` a červené hlavní diagonály. Pišme r=μ,s=ν.
První červená podmínka a+d≥1 a druhá a′+d′≥1 dávají

`sa+(1−s)a′≥2/3`, zatímco `ra+(1−r)a′≤1/3`.

To je nemožné pro 0<r,s≤1/2:

- Pokud s<r, maximum levého výrazu je
  `(1−s)/(3(1−r))<2/3`, protože je výhodnější nejdřív zvyšovat a′.
- Pokud r≤s a r≥1/3, maximum je s/(3r)≤1/2.
- Pokud r≤s a r<1/3, maximum je
  `s+(1−s)(1/3−r)/(1−r)<2/3`.

Žádné kritické řešení tohoto typu tedy neexistuje.

### Tři červená políčka a jedno modré

Nechť je modré (1,1); červené podmínky jsou
`a+d≥1`, `a+d′≥1`, `a′+d≥1`. Zvolme r=μ≤s=ν, což dovoluje
transpozice. Pro minimální průměry stačí a′=1−d,d′=1−a.
Každé takové řešení je konvexní kombinací tří pokrytí:

```
(a,a′,d,d′)=(1,1,0,0), (0,0,1,1), (1,0,1,0),
```

s vahami 1−d,1−a,a+d−1. Dvojice průměrných nákladů je tedy
v konvexním obalu `(1,0),(0,1),(r,s)`.
Pokud r+s≥1, alespoň jeden náklad je ≥1/2. Jinak jejich minimum
maxima je `s/(1+s−r)`; plyne to buď průsečíkem úsečky s diagonálou,
nebo nerovností `s*náklad_řádku+(1−r)*náklad_sloupce≥s`.
Aby oba náklady byly ≤1/3, nutně

`r+2s≤1`.

Jediná modrá podmínka je b′+c′≥1. Z průměrů dostaneme
`b′≤1/(3(1−r))` a `c′≤1/(3(1−s))`, tedy

`3(1−r)(1−s)≤(1−r)+(1−s)`.

Ale při r≤s a r+2s≤1 je

```
3(1−r)(1−s)−(1−r)−(1−s)
 = 1−2r−2s+3rs
 ≥ r(1−3r)/2 ≥0.
```

Protože 0<r≤1/3, rovnost je možná jedině při r=s=1/3.
Rovnosti ve všech nákladech pak jednoznačně vynucují druhé řešení

```
a=d=1, a′=b=c=d′=0, b′=c′=1/2, μ=ν=1/3.
```

Čtvrtý typ a jeho barevně obrácená varianta uzavírají všech 16 vzorů.
V obou rodinách jsou všechny čtyři průměry přesně 1/3, takže při
p<1/3 žádná nevyhnutelná soustava nemůže existovat. Tím je dokázán
hlavní výsledek úlohy, nikoli jen nutná podmínka nebo výčet na mřížce.

### F031: druhé řešení má mít ν=1/3

Kniha v posledním řádku (c) uvádí stejných osm hodnot jako výše,
ale **ν=2/3**. Potom jsou čtyři průměry

`(1/3,1/3,1/6,2/3)`.

Poslední z nich porušuje podmínku ≤p=1/3. Jediná oprava váhy na
ν=1/3 při zachování uvedených souřadnic dává všechny čtyři průměry 1/3
(a všechny disjunkce platí). Chyba je viditelná v PDF str. 612 i
v autorově Pre-Fascicle 6A str. 248. V úplných erratech 4B a Fascicle 6
není odpovídající oprava.

## Část (d) a nezávislé kontroly

První fyzická konstrukce uvedená v knize prošla všech 18 ohodnocení:
W,Y jsou rovnoměrné na {0,1,2}, X na {0,1}, Z=0;
A={(1,0),(2,0)}, B={(1,1),(1,2)}, C=D={(0,0)}.
Každá událost má pravděpodobnost 1/3 a žádná konfigurace se nevyhne
všem čtyřem. Protože Z je konstantní, C a D nemusejí sousedit v grafu
závislostí; konstrukce funguje už pro cestu D−A−B−C, jejíž hranice je 1/3.
Druhé řešení dostaneme cyklickým přejmenováním proměnných a událostí.

`check_variable_cycle.py` úplně prochází osm souřadnic i obě váhy na
mřížce s jmenovatelem 6, po předfiltrování čtyř průměrových podmínek.
Všechna řešení přesně odpovídají orbitám obou opravených rodin pod
16 symetriemi. Pro obecné reálné hodnoty slouží důkaz výše.
Dále kontroluje dolní mez na všech 65 536 soustavách událostí čtyř
férových bitů; 625 z nich má všechny pravděpodobnosti ≤1/3 a každá
má kladnou pravděpodobnost vyhnutí.

Výsledky: `results/variable_cycle.json`. Doklady F031 a F032:
`images/local-lemma-631.png`, `images/local-lemma-632.png`,
`images/fasc6a-local-lemma-255.png`, `images/fasc6a-local-lemma-256.png`.
Oba nálezy jsou drobné chyby zápisu; výsledek 1/3 je správný.
Fyzický výtisk dosud neověřen. Nic nebylo odesláno.

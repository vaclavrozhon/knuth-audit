# Appendix A: tabulky a racionální harmonická čísla

Audit 1. listopadu 2026, třetí vydání, první dotisk 1997. Původní
strany 619–622 byly přímo zobrazeny; doklady jsou v images/vol1-file634-p619.png
až vol1-file637-p622.png. Vstupní přepis všech položek je samostatný
results/appendix-a-transcription.json, nikoli výstup numerického algoritmu.
Tři opravy OCR na straně 620 byly odečteny z originálu a jsou tam vypsány.

## Certifikace tabulek 1 a 2

Tabulka 1 obsahuje 34 konstant na 40 desetinných míst, tabulka 2 obsahuje
týchž 34 konstant a deset záporných mocnin deseti na 45 osmičkových míst.
Znaménko za číslem vyjadřuje, zda je přesná hodnota větší (+), nebo
menší (−) než vytištěné zaokrouhlení. Například první řádek sqrt(2)
má v desítkové tabulce poslední číslici 7 a znaménko −.

Pro každou vytištěnou hodnotu t se z celých číslic vytvoří přesné
racionální číslo. Je-li b základ soustavy a d počet míst, program
check_appendix_a.py ověřuje striktní intervalovou nerovnost

```text
0 < sign * (v − t) < 1/(2 b^d),
```

kde v je uzavřený interval obsahující přesnou hodnotu konstanty
a sign je +1 nebo −1 podle tisku. Striktní porovnání vyžaduje,
aby celá intervalová obálka byla na správné straně obou mezí.
Tím se certifikuje současně všechna zaokrouhlená místa i znaménko.

Použit python-flint 0.9.0, Arb se 100 desetinnými místy pracovní
přesnosti. Derivace zeta v bodě 2 se počítá jako lineární koeficient
Taylorovy řady zeta(2+t), nikoli numerickým rozdílem blízkých hodnot.
Všechny konstanty mají navíc nezávislé srovnání s mpmath 1.3.0 na
90 místech; odchylka je menší než 10^−80. Toto srovnání je doplněk,
certifikát poskytují intervalové meze.

Obálky čísel a význam přesnosti popisuje
[oficiální dokumentace Arb](https://python-flint.readthedocs.io/en/latest/arb.html);
pro derivaci je použita
[aritmetika mocninných řad](https://python-flint.readthedocs.io/en/latest/arb_series.html).
Konkrétní verze je pevně uvedena v requirements-appendix.txt a výsledku.
Balíček byl instalován do vlastního dočasného adresáře, nikoli do systému.

**Výsledek: všech 78 hodnot i všech 78 znamének je správně.** Úspěšný
běh se neopakoval; results/appendix-a.json obsahuje jednotlivé obálky.

## Tabulka 3 a změna Bernoulliho konvence

H_n znamená součet převrácených hodnot 1,...,n, s H_0=0. F_n je
Fibonacciho posloupnost s F_0=0, F_1=1 a F_(n+2)=F_(n+1)+F_n.
B_n je v původním tisku určen mocninnou řadou

```text
sum B_n z^n/n! = z/(exp(z)−1).
```

Vynásobení exp(z)−1 a porovnání koeficientu z^(n+1) dává B_0=1 a
pro n>=1 rekurenci

```text
B_n = −1/(n+1) sum_(k=0)^(n−1) binom(n+1,k) B_k.
```

Všechny tři posloupnosti byly počítány přesně pomocí celých čísel
a zlomků. **Všech 93 vytištěných hodnot pro 0<=n<=30 souhlasí.**
Nejde o test pouhé desetinné aproximace zlomků.

Veřejná změna z 21. března 2021 mění B_1 na +1/2 a zároveň
v Appendix B mění jmenovatel generující funkce na 1−exp(−z).
Obě konvence jsou správné a souvisejí identitou

```text
z/(1−exp(−z)) = z + z/(exp(z)−1).
```

Mění se právě koeficient B_1; původní tabulka tedy není chybná
v rámci své původní definice. Známá změna je aplikována jako celek.

## Strana 622

Pro reálné x mimo záporná celá čísla definujme

```text
H_x = sum_(n>=1) (1/n − 1/(n+x)).
```

Konečně mnoho počátečních členů je definováno a zbývající členy
jsou O(n^−2), takže řada absolutně konverguje. V záporných celých
bodech má pól; úvodní „for any x“ čteme v definičním oboru výrazu,
nikoli jako přiřazení konečné hodnoty pólům. Všechna následná
tabulková použití mají 0<x<1. Není zde evidována nová chyba.

Pro celá 0<p<q dává obecný důkaz v gauss-harmonic-formula.md,
rovnice H2–H7, přesně poslední vzorec strany 622. Nesoudělnost
p,q není potřebná. Ve vzorci chybí prostřední člen při sudém q
oprávněně: log sin(pi/2)=0. Historická otázka původního Gaussova
důkazu zůstává u §1.2.9-19 oddělená od tohoto vlastního důkazu.

Jedenáct vytištěných zvláštních hodnot vyplývá přímým dosazením
q=2,3,4,5,6. Pro q=2,3,4,6 stačí obvyklé hodnoty sinu,
kosinu a kotangenty v násobcích pi/6 a pi/4. Pro pětiny položme
phi=(1+sqrt(5))/2. Přesné algebraické vztahy jsou

```text
sin(pi/5)^2   = (5−sqrt(5))/8,
sin(2pi/5)^2  = (5+sqrt(5))/8,
sin(pi/5) sin(2pi/5) = sqrt(5)/4,
sin(2pi/5) / sin(pi/5) = phi,
cot(pi/5)  = phi^(3/2) 5^(−1/4),
cot(2pi/5) = phi^(−3/2) 5^(−1/4).
```

Logaritmy obou sinů jsou proto ln(5)/4−ln(2)∓ln(phi)/2.
Dosazení do H2 dává přesně čtyři výrazy pro pětiny včetně
znamének sqrt(5) ln(phi)/2. To je obecná algebraická kontrola,
nikoli jen shoda čísel. Doplňkový intervalový výpočet porovnal
všech 11 specializací s psi(1+p/q)+gamma, kde psi je logaritmická
derivace gamma funkce; všech 11 rozdílů obsahuje nulu a leží
v intervalu (−10^−85,10^−85).

## Odkazy, errata a přesná zbývající mez

Odkaz na §1.2.9-19 je správný a byl porovnán s již přečteným
zadáním a odpovědí i vlastním úplným důkazem. Odkaz ze strany 621
na §1.3.3-23 rovněž vede na deklarovanou 40místnou konstantu
nejdelšího cyklu; původní strana 525 byla znovu přímo zobrazena.
Tato kontrola cíle odkazu není novou certifikací integrálu konstanty;
přesný stav jejího auditu je X0207/X0209.

Všechny čtyři vrstvy errat byly prohledány. Výpis je v
results/appendices-ab-errata.json. Přímo přečteny odpovídající
originály all1-prepre47 a all1-pre18. Vedle výše uvedené změny
B_1 je k Appendix A pouze plán z 6. května 1999 nahradit v příštím
vydání osmičkovou tabulku šestnáctkovou. Není to oprava její hodnoty
ani tvrzení, že takové vydání již vyšlo.

Technická část Appendix A je dokončena bez nového nálezu.
Historická věta na straně 621 o Wrenchových ručních výpočtech pro
první vydání a jejich potvrzení v sedmdesátých letech zatím nemá
nezávisle přečtený primární doklad. Proto je celkový Appendix A
veden jako partial pouze pro tuto konkrétní historii. Původní
fyzický výtisk nebyl ověřen.

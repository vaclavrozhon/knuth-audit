# Úlohy 7.1.1–60/64: mediány, univerzální podprogram a doplnění funkce

Checkpoint X0091, P0850–P0863. Původní zadání p87/file104 a
odpovědi p546/file563 jsou v `proof-file104/563.png`. Operátory
v 60 znovu přesně rozlišeny na renderu `proof-exercise60-original.png`:
v (d) jsou **XOR**, v (e)/(f) jsou NAND. Žádný matematický program.
Theorem P a jeho doména se přesně přebírají z proof-059, P0826–P0828.

## Všech šest výrazů úlohy 60 — P0850–P0855

Označme M(x,y,z) booleovský medián, tedy práh alespoň dvou
jedniček, a k=x+y+z. Následují jednotlivé argumenty, nikoli
jen porovnání odpovědi s vytištěnou tabulkou.

**(a), P0850.** Ze tří součinů xy,yz,xz je právě C(k,2)
rovno 1. Jejich XOR má pro k=0,1,2,3 postupně parity
0,0,1,1. Je to tedy M.

**(b), P0851.** Ze tří disjunkcí x∨y,y∨z,x∨z je právě
3−C(3−k,2) rovno 1, protože nula vzniká přesně na páru nul.
Tyto počty jsou 0,2,3,3 a jejich parity opět 0,0,1,1. Je to M.

**(c), P0852.** Ze tří booleovských hodnot jsou alespoň dvě
stejné. Příslušný jeden ze všech tří párových XOR je 0, takže
jejich konjunkce je vždy 0. Například 111 odlišuje tento výraz od M.

**(d), P0853.** Ekvivalence x≡y je 1⊕x⊕y. XOR tří
ekvivalencí je tedy

    (1⊕x⊕y)⊕(1⊕y⊕z)⊕(1⊕x⊕z)=1,

protože každá proměnná vystoupí dvakrát. Například 000
odlišuje výraz od M. Nezaměňujeme vytištěné XOR za OR.

**(e), P0854.** NAND je ¬(xy), proto konjunkce tří NAND
je podle de Morgana ¬(xy∨yz∨xz)=¬M. Zahrnuje i opakované
hodnoty; nejde o medián, ale jeho komplement.

**(f), P0855.** Disjunkce tří NAND je

    ¬(xy)∨¬(yz)∨¬(xz)=¬((xy)(yz)(xz))=¬(xyz)
                              =¬x∨¬y∨¬z.

V 000 má hodnotu 1, kdežto M má 0. Všech šest výsledků
souhlasí s odpovědí; právě (a)/(b) počítají medián.

## Všech šestnáct binárních operací v 61 — P0856

Fixujme w. Výraz h(t)=w◦t je některá funkce {0,1}→{0,1},
bez jakéhokoli předpokladu monotónnosti. Ze vstupů x,y,z jsou
alespoň dva rovny jejich mediánu a. Po aplikaci h jsou alespoň
dva výsledky rovny h(a), a proto

    h(M(x,y,z))=M(h(x),h(y),h(z)).

Platí to pro obě w a libovolnou tabulku ◦, takže pro všech
šestnáct binárních operací. Tím je doplněno celé tvrzení skryté
za větou odpovědi „when w=0, and when w=1“.

## Schenstedův rozvoj 62 a přesný rozsah monotónnosti — P0857

Fixujme všechny proměnné od x₄ dál. Označme

    A=f(x₁,x₁,x₃), B=f(x₁,x₂,x₂), C=f(x₃,x₂,x₃),
    F=f(x₁,x₂,x₃).

V každé z následujících vyčerpávajících možností je jeden
z A,B,C roven F a zbývající dvě hodnoty jej sevřou:

| rovné souřadnice | člen rovný F | ostatní argumenty f |
|---|---|---|
| x₁=x₂=a, x₃=b | A | (a,a,a), (b,a,b) |
| x₂=x₃=a, x₁=b | B | (b,b,a), (a,a,a) |
| x₁=x₃=a, x₂=b | C | (a,a,a), (a,b,b) |

V první řádce je (a,a,a)≤(a,a,b)≤(b,a,b), pokud a≤b;
při a≥b se všechny nerovnosti obrátí. Ve druhé řádce je
(a,a,a)≤(b,a,a)≤(b,b,a) pro a≤b a opačně pro a≥b.
Ve třetí je (a,a,a)≤(a,b,a)≤(a,b,b), opět s obrácením
pro a≥b. Monotónnost proto v každé řádce sevře F mezi
zbývající dvě hodnoty, a M(A,B,C)=F.

Pigeonhole princip pro tři bity zaručuje alespoň jednu řádku;
při všech stejných bitech jsou všechny členy F. Stačí skutečně
monotónnost **jen v prvních třech souřadnicích**, jak tvrdí
dodatek odpovědi. Žádná symetrie samotné funkce f se nepředpokládá.

## Medián tří jedním mediánem pěti — P0858

Vytištěná identita je M₃(x,y,z)=M₅(x,x,y,y,z). Platí dokonce
na libovolném úplně uspořádaném oboru. Vzhledem k symetrii x/y
předpokládejme x≤y. Při z≤x je prostřední ze seznamu
z,x,x,y,y rovno x; při x≤z≤y je prostřední x,x,z,y,y rovno z;
při y≤z je prostřední x,x,y,y,z rovno y. Ve všech případech
je to M₃(x,y,z), včetně všech rovností a krajních prvků oboru.

Jedno volání daného podprogramu tedy stačí, pouze s opakovanými
vstupy. Na booleovském oboru totéž říká: pro x=y rozhodují
čtyři stejné bity; pro x≠y jsou mezi nimi dvě nuly a dvě jedničky,
takže rozhoduje z.

## Obecný Postův dodatek v 63 — P0859

Nechť f je libovolná monotónní selfduální booleovská funkce,
která není projekcí. „Netriviální“ má právě tento význam;
konstanty selfduální nejsou. Ukážeme explicitně, jak jediné
volání f s identifikovanými vstupy vypočte M₃. Výběr proměnných
není omezen na symetrické nebo prahové funkce.

Píšeme f(S) pro hodnotu na charakteristickém vektoru S⊆[n].
Kdyby f({i})=1, monotónnost dává hodnotu 1 všem množinám
obsahujícím i; selfdualita dává hodnotu 0 všem ostatním.
Pak by f byla právě projekcí x_i. Proto f({i})=0 pro každé i,
a selfdualita dává f([n]\{i})=1.

Vyberme inkluzně minimální pravdivou množinu A uvnitř některé
[n]\{i}. Potom 2≤|A|≤n−1. Pro a∈A tvoří

    A\{a},  {a},  [n]\A

tři neprázdné bloky. Do vstupů f na těchto blocích přiveďme
postupně x,y,z. Vzniklá ternární funkce g je monotónní a
selfduální. Přitom

    g(1,0,0)=f(A\{a})=0       (minimalita A),
    g(0,1,0)=f({a})=0         (f není projekce),
    g(0,0,1)=f([n]\A)=0      (selfdualita a f(A)=1).

Monotónnost dává g(0,0,0)=0, selfdualita pak všechny čtyři
opačné hodnoty: na dvojicích jedniček a na 111 je g=1.
Tedy g=M₃. Případy arity menší než 3 žádnou netriviální f
nemají, přesně jak bylo dokázáno v P0823.

Theorem P, obecně dokázaný v proof-059, realizuje každou
monotónní selfduální funkci pomocí M₃ a projekcí. Nahrazení
každého mediánu právě uvedeným jediným voláním f dokazuje
celý dodatek odpovědi „compute them all“. Nezávislá rekonstrukce
historického Postova článku se tím netvrdí.

## 64(a): obě implikace párové podmínky — P0860/P0861

Označme podmínku

    pro každé x,y existuje k: f(x)=x_k a f(y)=y_k.       (*)

**P0860, nutnost.** Projekce podmínku splňuje. Jestliže ji
splňují f₁,f₂,f₃ a f=M(f₁,f₂,f₃), pro pevné x se alespoň
dvě f_i(x) rovnají f(x) a pro pevné y se alespoň dvě f_i(y)
rovnají f(y). Tyto dvě podmnožiny tří indexů se protínají.
Společný index i a jeho svědek k pro (*) tedy funguje i pro f.
Indukce po konečném mediánovém výrazu z Theorem P dokazuje
vytištěný argument pro všechny monotónní selfduální funkce.

**P0861, dostatečnost.** Kdyby x≤y, ale f(x)=1 a f(y)=0,
svědek k by dal x_k=1>0=y_k, spor. Funkce je monotónní.
Položme y=¬x; každý svědek k dává f(y)=1−f(x), takže je
selfduální. To dokazuje ekvivalenci bez předpokladu, že x/y
jsou různé; případy x=y jsou součástí (*) a budou důležité dále.
Pro n=0 neexistuje svědek k ani selfduální úplná funkce,
takže ekvivalence 64(a) zůstává platná i v tomto okraji.

## 64(b): invariant a přesné lexikografické volby — P0862

Zde dokazujeme obvyklou doménu **n≥1**; nulární rozsah je
oddělen v P0863. Nechť D je dosud definovaná část tabulky,
splňující (*) pro všechny x,y∈D. Pro y∈D definujme

    A_y = { i : y_i=f(y) }.

Podmínka (*) přesně říká A_u∩A_v≠∅ pro všechny u,v∈D.
Zahrnuje A_y≠∅, protože dovoluje u=v. Zápis je ekvivalence,
nikoli jen nutná podmínka. Při doplnění nové hodnoty f(x)=a
se tedy musí nová množina {i:x_i=a} protínat se všemi A_y
a musí být sama neprázdná.

Zvolme lexikograficky nejmenší nedefinované x, jak žádá kniha.

1. **¬x je definováno.** Zvolíme f(x)=1−f(¬x). Pak A_x=A_{¬x},
   takže všechny průniky včetně průniku se sebou jsou zachovány.
2. **¬x není definováno a existuje z≤x s f(z)=1.** Zvolíme
   f(x)=1. Množina A_z je přesně množina jedničkových pozic z,
   je neprázdná a je podmnožinou jedničkových pozic x. Proto
   každý průnik A_z∩A_y svědčí také pro nový průnik A_x∩A_y.
3. **¬x není definováno a takové z neexistuje.** Zvolíme f(x)=0.
   Protože x je nejmenší nedefinované a ¬x je také nedefinované,
   máme x<lex¬x. Pro n≥1 to znamená x₁=0, takže A_x je neprázdná.
   Kdyby A_x∩A_y=∅ pro nějaké definované y, pak A_y leží
   v jedničkových pozicích x. Je-li f(y)=1, znamená to y≤x,
   spor s absencí pravdivého z≤x. Je-li f(y)=0, znamená to
   ¬y≤x. Rovnost by dala y=¬x, které není definováno. Při
   ostré nerovnosti je ¬y lexikograficky menší než x a musí
   být již definováno. Podmínka (*) pro y,¬y vynutí f(¬y)=1,
   opět spor s absencí pravdivého z≤x.

Ve všech třech větvích zůstává zachován úplný invariant (*).
Postup mění vždy jen jedno nedefinované místo, žádnou původní
hodnotu, a skončí nejvýše po 2ⁿ−|D| krocích. Úplná funkce g
splňuje (*) a podle právě dokázané části (a) je monotónní
a selfduální. Prázdné počáteční D je pro n≥1 rovněž pokryto:
první x=00…0 přejde do třetí větve a dostane hodnotu 0.
Není zde tvrzena polynomiální cena vzhledem k n; úplná tabulka
sama může mít 2ⁿ položek a úloha takový nákladový slib nedává.

## Pouze nulární doména 64(b) — P0863, partial

Pokud by 64(b) zahrnovala n=0 a prázdnou počáteční tabulku,
párová podmínka je vakuózní, ale úplná selfduální nulární funkce
neexistuje. Důkaz výše proto výslovně vyžaduje n≥1. Vztah
implicitní domény úlohy k nulárním funkcím zůstává stejně jako
P0580 samostatný drobný doménový limit; žádná karta ani nové
confirmed se tím nevytváří. Pozitivní arity jsou úplně dokázány.

## Errata, bibliografie a stránkový rozsah

Dne 2026-11-07 prohledány `all4a-pre`, `all4a`, `err4a`,
`all4f0`, `all4f1` podle stran 87/546, odpovědí 60–64
a témat Post/Akers/selfdual. Relevantní matematická oprava
tohoto bloku nenalezena. F0 p142/answer60 patří úvodu a mění
„Set A“ na „Let A“; all4a-pre p546 nahrazuje až 67(a).

Primární odkaz Akersova článku
[DOI 10.1109/FOCS.1962.16](https://doi.org/10.1109/FOCS.1962.16)
nebyl dostupný; přesná historická atribuce a bibliografie
FOCS 3 (1962),149–157 zůstává výslovně přeskočena. Totéž
platí pro historické přisouzení 62 Schenstedovi a dodatku 63
Postovi. Matematika nepoužívá žádný z těchto článků jako
neprokázaný vstup.

P87 obsahuje navíc začátek 65 a starší limity P0816/P0840;
p546 obsahuje také 65–67. Ani jedna stránka se tímto
checkpointem neoznačuje jako celá argumentově uzavřená.

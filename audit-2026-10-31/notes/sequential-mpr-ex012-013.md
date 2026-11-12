# D115–D116 — celé MPR12 a MPR13

6. listopadu 2026. Celá zadání p13/file33 a odpovědi
p372/file392 přímo zobrazeny, také autorův Pre-Fascicle
5A, p13/file19 a p29/file35. Pro přesné negace úlohy13
navíc zobrazen větší render file392-detail. Žádný
numerický běh; všechny výpočty jsou níže přesné.

## D115: čtyři atomy a společný determinant

Zaveďme přesně jako odpověď

    w=P(A∩B), x=P(A∩B̄),
    y=P(Ā∩B), z=P(Ā∩B̄).

Jsou nezáporné a w+x+y+z=1. Pišme s=P(A)=w+x,
t=P(B)=w+y a Δ=w−st. Přímým roznásobením

    Δ=w−(w+x)(w+y)
      =w(1−w−x−y)−xy=wz−xy.

Proto Δ je právě determinant vytištěné matice
s řádky (w,x), (y,z). Nejde o absolutní hodnotu
čísla wz−xy: svislé čáry zde značí determinant.

## D115: všech pět rozdílů ve vnitřním případě

Při 0<s<1 a 0<t<1 jsou všechny potřebné jmenovatele
kladné. Z podílové definice podmínění vycházejí:

| Tvrzení | Levá strana minus pravá strana |
|---|---|
| původní P(A\|B)>P(A) | w/t−s=Δ/t |
| (i) P(B\|A)>P(B) | w/s−t=Δ/s |
| (ii) P(A\|B)>P(A\|B̄) | w/t−x/(1−t)=Δ/[t(1−t)] |
| (iii) P(B\|A)>P(B\|Ā) | w/s−y/(1−s)=Δ/[s(1−s)] |
| (iv) P(Ā\|B̄)>P(Ā\|B) | z/(1−t)−y/t=Δ/[t(1−t)] |

Pro (ii) je čitatel w(1−t)−xt=w−(w+x)t=Δ.
Pro (iii) je w(1−s)−ys=w−(w+y)s=Δ.
Pro (iv) je zt−y(1−t)=t(y+z)−y
=t(1−s)−y=w−st=Δ. Tím je ověřen každý převod,
nejen společná závěrečná věta.

Jmenovatele jsou v této větvi kladné, proto všech
pět striktních nerovností platí právě když Δ>0,
tedy právě když wz>xy. Rovnost Δ=0 dává rovnost
ve všech porovnáních, záporné Δ obrácený směr.

## D115: nulové a jisté události bez dělení nulou

Původní p2 výslovně definuje P(E|F)=P(E), když
P(F)=0. Úplný důkaz této větve a pravidla celkové
pravděpodobnosti je převzat z D093,
`notes/sequential-mpr-001-003.md`, §D093.
Nezavádíme jinou konvenci a nedosazujeme do
předchozí tabulky nulový jmenovatel.

Je-li s=0 nebo s=1, indikátor A je téměř jistě
konstantní. Pro každé B s kladnou hmotností má
P(A|B)=s, a totéž platí při nulové hmotnosti
podle konvence. Stejně P(A|B̄)=s. Navíc podmínění
B na A či Ā vrací vždy t: nenulová větev má
hmotnost 1 a nulová větev používá konvenci.
Všech pět porovnání se tedy stane rovností,
včetně doplňků v (iv). Současně w=st, takže Δ=0.

Je-li t=0 nebo t=1, zaměněný argument dává
P(B|A)=P(B|Ā)=t a P(A|B)=P(A|B̄)=s.
Rovněž P(Ā|B)=P(Ā|B̄)=1−s. Opět jsou všechna
striktní tvrzení nepravdivá a Δ=0. Tento argument
zahrnuje i společné okraje s,t∈{0,1}.

Proto je odpověď správná pro všechny pravděpodobnosti,
ne pouze po nevysloveném vyloučení nul a jedniček.
Při Δ>0 navíc žádný z uvedených krajů nemůže nastat;
tabulka tedy pokrývá obě implikace striktního tvrzení.

## D115: „strictly positively correlated“ a odkaz61

Pro indikátory I=[A], J=[B] jsou EI=s, EJ=t
a E(IJ)=w. Definice kovariance tak dává
covar(I,J)=w−st=Δ. Všechny hodnoty jsou omezené,
o existenci očekávání není pochybnost.

Přímo zobrazen původní odkaz61(a) na p17/file37,
pouze odstavec definující pozitivní korelaci jako
covar(f,g)≥0. Výslovné „strictly“ v odpovědi12
znamená >0, tedy právě Δ>0. Není třeba předpoklad
kladných rozptylů jako u normalizovaného Pearsonova
koeficientu. Matematická terminologie odpovědi je
správná. Vlastní důkaz FKG a další části61 se tímto
odkazem neuzavírají; celá úloha61 nadále pending.

Atribuce návrhu úlohy E. Georgiadisovi nemá uvedený
pramen a je výslovně bibliograficky vynechána.

## D116: přesně všech osm atomů odpovědi13

Negace v obou originálech určují nuly pro
(A,B,C)=(0,0,0) a (0,1,0), tedy v obou je Ā∩C̄;
B je jednou doplněné a jednou nedoplněné.
Nenulový dvojitý atom je (1,1,1). Celá tabulka:

| A | B | C | Pravděpodobnost |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1/7 |
| 0 | 1 | 0 | 0 |
| 0 | 1 | 1 | 1/7 |
| 1 | 0 | 0 | 1/7 |
| 1 | 0 | 1 | 1/7 |
| 1 | 1 | 0 | 1/7 |
| 1 | 1 | 1 | 2/7 |

Všechny hmotnosti jsou nezáporné, součet je
(0+1+0+1+1+1+1+2)/7=1. Přímé sečtení dává

    P(A)=P(C)=5/7, P(B)=4/7,
    P(A∩B)=P(B∩C)=P(A∩C)=3/7.

Všechny podmiňovací události jsou kladné.
Oba předpoklady otázky jsou pravdivé:

    P(A|B)=3/4>5/7=P(A), rozdíl 1/28;
    P(B|C)=3/5>4/7=P(B), rozdíl 1/35.

Navržený závěr však neplatí, dokonce má opačný směr:

    P(A|C)=3/5<5/7=P(A), rozdíl −4/35.

Odpověď „False“ i její konkrétní vytištěný svědek
jsou tedy správné. Párové kovariance indikátorů
jsou 1/49 pro A,B a B,C, ale −4/49 pro A,C;
to také přímo souhlasí s determinantovým kritériem12.

## D116: proč nejde o ojedinělý nulový okraj

Věta odpovědi „in many cases“ má i konkrétní
obecnou oporu. Smíchejme předchozí zákon P₀
s rovnoměrným zákonem U na všech osmi bitech:

    P_ε=(1−ε)P₀+εU, 0≤ε<1.

Jde o platné pravděpodobnosti; pro ε>0 jsou všechny
atomy kladné. Při tomto zákonu jsou

    s_A=s_C=(10−3ε)/14, s_B=(8−ε)/14,
    P(A∩B)=P(B∩C)=P(A∩C)=(12−5ε)/28.

Proto po převedení na společný jmenovatel196

    covar([A],[B])=covar([B],[C])
       =(4−ε−3ε²)/196=(1−ε)(4+3ε)/196>0,
    covar([A],[C])
       =(−16+25ε−9ε²)/196
       =−(1−ε)(16−9ε)/196<0.

Pro každý 0≤ε<1 zůstávají oba předpoklady pravdivé
a závěr nepravdivý. Rovnoměrný mezní zákon ε=1 má
všechny kovariance0 a už není striktním svědkem.
Tato rodina navíc ukazuje, že původní dvě nulové
hmotnosti nejsou příčinou selhání implikace.
Není k tomu potřeba numerický test ani vyhledávání.

## Úplnost a errata

D115 uzavírá celé12 včetně všech čtyř podotázek,
determinantu, terminologie a okrajových konvencí.
D116 uzavírá celé13 včetně každé vytištěné hmotnosti,
normalizace, všech tří relevantních podmíněných
pravděpodobností a významu „many cases“. Bez nálezu.

Převzaty nezměněné šestivrstvé stránkové záznamy
z D109/D114 a navíc cíleně hledány odpovědi12/13,
Georgiadis, korelace a determinantové výrazy.
Tři TeX zdroje rovněž zkontrolovány. Žádná oprava
MPR12 nebo13 nenalezena; změny odpovědí12/13 ve
Fascicle5 p207/p226 a Fascicle6 p186 jsou jiné
sekce. Podrobnosti a hashe:
`results/sequential/mpr-012-013-correlation-errata.json`.

Na původní p13 je tím každý matematický obsah
posouzen. Stránka přesto zůstává partial kvůli
interpretačnímu C046 u8; dokončení12–13 kandidáta
neuzavírá. P372 zůstává partial pro14–19 a C046.
P17/file37 má posouzen pouze korelační definiční
odstavec61(a), nikoli celou stránku.

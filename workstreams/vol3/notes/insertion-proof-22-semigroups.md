# Úloha22: obě rodiny, všechny mezery a tabulka

7. listopadu 2026. Originály103/file114 a622/file633 jsou
zobrazené. Celou úlohu odvozujeme obecně; vzorek s=4 v odpovědi
není náhradou důkazu. Žádný program ani enumerace se nespouští.
Pět vrstev errat je doplněno v
`sources/insertion-semigroup-boundary-errata-review.json`.

Minusová rodina má popsanou největší mezeru pro s≥2;
plusová pro s≥1. Knižní s=1 v minusové rodině je zvlášť
zaznamenaný candidate/low V3-C0021: možná implicitní podmínka
netriviálnosti, nikoli automaticky potvrzený nález.
Zásada vzorů1/4B: dokládáme celou reprezentovatelnost, nemožnost
i krajní podmínky; tabulku kontrolujeme přes minimální zástupce,
nikoli jen přes existenci uvedených rozkladů.

## P0791: počet sčítanců v binárním rozkladu

Označ b(v) počet jedniček v binárním zápisu v≥0.
Při rozkladu v=∑_(j≥0)c_j2^j, c_j≥0, může celkový počet
sčítanců C=∑c_j nabývat **právě všech celých hodnot**

    b(v)≤C≤v.

Horní mez plyne z2^j≥1. Opakované sloučení dvou stejných
mocnin na následující mocninu snižuje počet o1, až zbude
jedinečný binární rozklad s b(v) členy; to dokazuje dolní mez.
Naopak od binárního rozkladu vždy rozštěp nějaký člen2^j,
j≥1, na dvě poloviny. Počet členů se zvedne právě o1 a tento
proces skončí až při v jedničkách. Dosáhneme tedy všech hodnot
mezi oběma krajními počty, bez mezery. Pro v=0 je pouze C=0.

Dále d(v)=v−b(v) neklesá: při přechodu v→v+1 nechť t je
počet koncových jedniček v. Pak b(v+1)−b(v)=1−t, takže
d(v+1)−d(v)=t≥0. Tato monotonicita bude bránit neověřenému
přeskočení pozdějších mezer.

## P0792: minusová rodina, všechny intervaly a poslední mezera

Polož Q=2^s, m=Q−1, s≥1. Libovolný rozklad do generátorů
Q2^j−1 má hodnotu

    n=Qv−C,  v=∑c_j2^j, C=∑c_j.

Podle P0791 je množina reprezentovatelných n přesně sjednocením
celých intervalů

    I_v=[mv, Qv−b(v)],   v≥0.                       (M)

Je zde dokázán i opačný směr: každé celé číslo uvnitř intervalu
určuje počet C v povoleném rozsahu a tedy skutečné nezáporné
koeficienty c_j. Levé i pravé konce intervalů přísně rostou;
pravý konec při dalším v roste o Q−1+t≥1.

Mezera mezi I_v a I_(v+1) má délku

    max(0,m−1−v+b(v))=max(0,m−1−d(v)).

Pro0≤v≤Q−1 je výraz nezáporný. Pro v=Q−1 je právě s−1;
pro v=Q je d(v)=Q−1=m a výraz je záporný. Monotonicita d
zaručuje, že odtud už žádná mezera nepřijde.

Pro s≥2 je poslední mezera skutečně neprázdná, neboť s−1>0.
Leží těsně před levým koncem I_Q=mQ. Její poslední číslo je

    F_−=Q(Q−1)−1=2^s(2^s−1)−1.

Všechna n≥Q(Q−1) jsou reprezentovatelná a F_− nikoli,
přesně jak je požadováno. Pro s=1 mají všechny mezery délku0:
první generátor je1 a **každé n≥0 je reprezentovatelné**.
V tomto okraji největší negenerovatelné celé číslo je−1,
nikoli hodnota1 z uvedené formule; tento rozsah se nezamlčuje.

## P0793: přesný počet mezer a celá rekurence odpovědi

Protože všechny mezery byly v(M) vyčerpány, jejich počet je

    x_s=∑_(v=0)^(Q−1)(Q−2−v+b(v)).

V binárních zápisech0,…,2^s−1 je každý z s bitů jedničkou
právě Q/2krát. Proto ∑b(v)=sQ/2. Součet aritmetické části
dává

    x_s=Q(Q−2)−Q(Q−1)/2+sQ/2
       =2^(s−1)(2^s+s−3).

To platí i pro s=1 a správně dává0. Přímé odečtení tohoto
obecně dokázaného výrazu pro dvě po sobě jdoucí hodnoty s dává

    x_s−2x_(s−1)=2^(s−1)(2^(s−1)+1),  s≥2.

Je tedy doložena celá rekurence odpovědi622, nikoli extrapolace
ze samotného příkladu x_4.

## P0794: všech patnáct minimálních reziduálních zástupců

Pro s=4 je m=15 a generátory15,31,63,127,… . Následující
tabulka ověřuje všechny uvedené nejmenší reprezentovatelné
hodnoty n_k≡k modulo15. q_k=(n_k−k)/15 a poslední sloupec
je δ_k=k−q_k+1+b(q_k−1).

|k|n_k|rozklad|q_k|δ_k|
|---:|---:|---|---:|---:|
|0|0|prázdný|0|—|
|1|31|31|2|1|
|2|62|31+31|4|1|
|3|63|63|4|2|
|4|94|63+31|6|1|
|5|125|63+31+31|8|1|
|6|126|63+63|8|2|
|7|127|127|8|3|
|8|158|127+31|10|1|
|9|189|127+31+31|12|1|
|10|190|127+63|12|2|
|11|221|127+63+31|14|1|
|12|252|63+63+63+63|16|1|
|13|253|127+63+63|16|2|
|14|254|127+127|16|3|

Rozklad dokazuje reprezentovatelnost, ale sám by nestačil
k minimalitě. Pro n_k−15=15(q_k−1)+k je každý možný index
intervalu(M) nejvýše q_k−1, neboť levý konec I_v=15v.
Největší pravý konec těchto intervalů je16(q_k−1)−b(q_k−1),
od něhož n_k−15 leží právě o δ_k výše. Každé δ_k>0,
takže n_k−15 reprezentovatelné není. Kdyby byl reprezentovatelný
nějaký ještě menší nezáporný zástupce stejného zbytku, přičtení
několika generátorů15 by reprezentovalo n_k−15; spor.
Tím je u každé položky tabulky prokázáno skutečné minimum.

V každém nenulovém zbytku je přesně q_k kladných mezer,
a v nultém žádná. Jejich součet je

    (2+4+4+6+8+8)+8+(10+12+12+14+16+16)+16
    =136=2·32+8·9.

To potvrzuje všechny zobrazené součty622 i x_3=32.
Největší mezera je max n_k−15=254−15=239;
souhlasí s obecným F_− a nikoli jen s existencí n_14.

## P0795: plusová rodina, poslední mezera a úplné pokrytí

Při generátorech Q2^j+1, Q=2^s, s≥1, je místo toho n=Qv+C.
Stejný obousměrný argument P0791 dává celé intervaly

    J_v=[Qv+b(v),(Q+1)v].                         (P)

Mezi J_v a J_(v+1), pro0≤v≤Q, je mezera délky

    Q−1−v+b(v+1)=Q−w+b(w),  w=v+1.

Pro1≤w≤Q je kladná a pro w=Q+1 má délku1. Tyto intervaly
jsou proto v tomto rozsahu disjunktní a seřazené. Poslední
jednoprvková mezera leží mezi koncem J_Q=Q(Q+1) a začátkem
J_(Q+1)=Q(Q+1)+2. Je tedy

    F_+=Q²+Q+1,
    conductor=F_++1=2^(2s)+2^s+2.

Pro všechny další dvojice se intervaly dotýkají nebo překrývají:
podmínka J_(v+1) začíná nejvýše o1 nad koncem J_v je
d(v+1)≥Q. Již d(Q+2)≥Q (pro Q=2 přímo3; pro Q≥4 je
b(Q+2)=2) a dál platí monotonicita P0791. Rostoucí pravé
konce proto pokryjí všechna čísla od conductor výše, i kdyby
se některé vzdálené levé konce nechovaly monotónně.

Žádný pozdější interval nemohl vyplnit F_+ ani dřívější mezery:
pro v≥Q+2 je jeho levý konec nejméně Q(Q+2)+1>F_+.
Předchozí intervaly mají konce≤Q(Q+1). Dokázány jsou tedy
oba směry, žádný skrytý překryv ani pozdější reprezentace se
nevynechávají. Pro s=1 to dává generátory3,5,9,…, F_+=7
a conductor8, jak lze přímo zkontrolovat.

## P0796: přesný počet plusových mezer

Všechny mezery už byly vyčerpány. Jejich počet je

    y_s=∑_(w=1)^(Q+1)(Q−w+b(w)).

Součet bitů0,…,Q−1 je sQ/2, navíc b(Q)=1 a b(Q+1)=2.
Proto

    y_s=Q(Q+1)−(Q+1)(Q+2)/2+sQ/2+3
       =2^(s−1)(2^s+s−1)+2.

To je druhá požadovaná plusová formule. Pro s=1 dostáváme4
mezery1,2,4,7; nulový součet je reprezentovatelný a nepřičítá
se k počtu kladných mezer. Celá plusová varianta je tím uzavřená.

## P0797 — partial: rozsah s v původním zadání

Matematické výsledky jsou výše prokázány ve skutečných doménách.
Původní zadání103 však výslovně neuvádí s≥2. Při kladném s=1
je údajně nereprezentovatelné číslo2^1(2^1−1)−1=1 rovno
prvnímu generátoru, s koeficienty a_0=1 a všemi ostatními0.
Je to konkrétní rozpor při zahrnutí s=1; oprava je přidat s≥2
do minusové části a triviální případ s=1 ošetřit odděleně.

Možný výklad, že s už znamená netriviální přírůstek≥2, nebyl
v zadání doložen; proto je veden V3-C0021 jako candidate/low,
nikoli confirmed. Veškeré obecné důkazy, tabulka i aplikace pro
s≥2 zůstávají platné. Tato jediná formulace drží celou22
v přesně vymezeném partial stavu. Další kurzor je TheoremP
na91 a dolní konstrukce24 na104/622–623.

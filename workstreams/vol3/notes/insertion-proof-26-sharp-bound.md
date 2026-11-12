# Celá úloha26: ostrá mez, konstrukce a nejkratší příklad

7. listopadu 2026. Zadání104/file115 a odpověď623/file634
jsou zobrazeny; pětivrstvá evidence `sources/insertion-errata-review.json`
pro26 neuvádí opravu. Převzata je již dokázaná skutečnost P0776,
že v3-,5-,7-ordered permutaci mohou být inverse jen v mezerách1,2,4.
Následující šestistavový argument je obecný důkaz všech délek,
nikoli výpočetní enumerace permutací nebo převzetí ostrého tvrzení
z odpovědi. Žádný program se nespouští.

## P0786: úplná konstrukce a její přípustnost

Pro pozice i≥1 definuj surové různé hodnoty

    a_i=i+δ_i,   δ_i=3 pro i≡1, −3 pro i≡2, 0 pro i≡0 mod3.

To je přesně a_(3k+s)=3k+4s pro−1≤s≤1 z odpovědi.
Hodnoty různých zbytkových tříd se liší modulo3; v jedné třídě
rostou po3, takže všechny jsou různé, i když se pro malé i
objeví záporná hodnota nebo hodnota>N. Následné přeznačení
pořadím mezi prvními N hodnotami dá permutaci1,…,N a zachová
veškeré nerovnosti i inverse.

Přípustnost dokážeme pro všechny i, nikoli několika příklady:

| mezera d | a_(i+d)−a_i pro i≡1,2,0 mod3 |
|---|---|
|3|3,3,3|
|5|2,11,2|
|7|1,10,10|

Všechny rozdíly jsou kladné. První N hodnot je tedy současně
3-,5-,7-ordered a totéž platí po přeznačení.

## P0787: všechny inverse konstrukce a devět konkrétních párů

Rozdíly pro zbývající mezery říkají, že inverse nastane přesně
takto: pro d=1 při i≡1; pro d=2 při i≡1 nebo0; pro d=4 při i≡1.
Jiné mezery inverse nemají podle P0776. Je-li N=3k+2, k≥0,
počty přípustných začátků jsou postupně k+1,2k,k, tedy

    I=4k+1=(4N−5)/3.

Platí i k=0, kdy žádná mezera2 či4 neexistuje. Pro N=8 dostaneme
po přeznačení přesně4,1,3,7,2,6,8,5. Všech devět inversí je

    d=1: (1,2),(4,5),(7,8);
    d=2: (1,3),(3,5),(4,6),(6,8);
    d=4: (1,5),(4,8).

To ověřuje konkrétní9>N i původ tištěného příkladu. Nejkratší
možnou délku teprve dokáže obecná horní mez níže.

## P0788: úplný šestistavový model všech přípustných permutací

Čti **pozice** permutace v pořadí rostoucích hodnot. Již přečtené
pozice tvoří ideál pozičního uspořádání: je-li pozice j vybraná,
musely být vybrány její existující předchůdci j−3,j−5,j−7
a tedy i předchůdci se všemi generovatelnými vzdálenostmi.
Nechť m je nejmenší dosud nevybraná pozice. Protože jedinými
kladnými negenerovatelnými vzdálenostmi jsou1,2,4, vybrané
pozice nad m mohou být pouze m+1,m+2,m+4. Výběr m+4 navíc
vyžaduje již vybrané m+1 kvůli rozdílu3. Stav je proto právě
jedna z těchto šesti množin vybraných posunů:

    A=∅, B={1}, C={2}, D={1,2}, E={1,4}, F={1,2,4}.

Naopak každá z nich splňuje všechny požadavky na předchůdce;
žádná další skrytá podmínka není potřeba. Jako další lze vybrat m,
dále m+1 či m+2, pokud ještě nejsou vybrané, a m+4 právě tehdy,
když je vybrané m+1. Pozice nad m+4 nejsou dostupné, dokud m
zůstává nevybrané. U konečného N se samozřejmě vybírají pouze
existující pozice≤N.

Po výběru m posuň základ na nové minimum. Například E→C:
po výběru m jsou m i m+1 vybrané, nové minimum je m+2 a
zbývající vybrané m+4 má nový posun2. Pro F→B je nové minimum
m+3 a vybrané m+4 má posun1. Ostatní normalizace jsou v tabulce.

Při výběru m+d vznikne právě tolik inversí, kolik dosud
nevybraných pozic je menších než m+d. Jejich hodnoty budou
pozdější, tedy větší než právě přidělovaná hodnota. Cena je

    w=d−|S∩{1,…,d−1}|  (a pro d=0 je0).

Každou inversi tak počítáme právě při výběru jejího menšího,
pravého prvku. Úplný seznam přechodů a cen je:

| stav | vybraný posun d | nový stav | w |
|---|---:|---|---:|
|A|0|A|0|
|A|1|B|1|
|A|2|C|2|
|B|0|A|0|
|B|2|D|1|
|B|4|E|3|
|C|0|B|0|
|C|1|D|1|
|D|0|A|0|
|D|4|F|2|
|E|0|C|0|
|E|2|F|1|
|F|0|B|0|

Každá přípustná permutace délky N dává cestu N přechodů A→A
a součet w je její počet inversí. I obráceně každá taková cesta
vybírá pokaždé povolenou pozici a při návratu A po N krocích
má vybraný přesně prefix1,…,N. Nikdy nemohla vybrat pozici>N,
protože výběry se nemažou. Dává tedy platnou permutaci přesně
této délky, nikoli jen přibližný model.

## P0789: obecná horní mez pomocí potenciálu

Každému přechodu přiřaď deficit4−3w a potenciály

    p(A)=0, p(B)=1, p(C)=−2, p(D)=−1, p(E)=−4, p(F)=−3.

Upravený deficit je ρ(u→v)=4−3w+p(u)−p(v).
Pro řádky předchozí tabulky jsou jeho hodnoty postupně

    4,0,0,5,3,0,1,0,3,0,2,0,0.

Každá je nezáporná; lze je ověřit přímým odečtením uvedených
šesti potenciálů. Na cestě A→A se potenciály teleskopicky zruší,
takže přesně

    4N−3I=∑ρ≥0.

Tím již máme univerzální I≤4N/3. Potřebujeme však i ostrou
konstantu pro N≡2 a nejkratší příklad; pouhý sklon nestačí.

Rozlož cestu podle návratů do A na neprázdné exkurze. Exkurze
bez B může být jen smyčka A→A nebo trojúhelník A→C→D→A:
E není dostupné bez B a z F lze pokračovat jen do B. Tyto dvě
exkurze mají délky1,3 a deficity4,3.

Exkurze obsahující B má deficit nejméně5. Uvažuj její poslední B.
Vrátí-li se do A hranou B→A, tato hrana sama máρ=5.
Vrátí-li se přes D→A, ta máρ=3 a od posledního B do D lze
bez dalšího B jít jen přímo B→D (ρ=3), nebo B→E→C→D
(ρ=2). V obou případech je celkový deficit nejméně5.
Ostatní přechody jsou nezáporné a nic z této meze neodečtou.

Každá neprázdná cesta A→A tedy má deficit nejméně3. Pro N≡2
mod3 je celý deficit4N−3I kongruentní2 modulo3, takže nemůže
být3 ani4 a musí být nejméně5. Dostáváme přesně

    I≤(4N−5)/3  pro N≡2 mod3.

P0787 této meze dosahuje; tvrzení o nejlepší možné konstrukci
v této zbytkové třídě je tím dokázáno bez hledání permutací.

## P0790: nejkratší příklad a asymptotika pro všechny délky

Pokud cesta vůbec nenavštíví B, skládá se pouze z exkurzí délky1
s0 inversemi a délky3 se3 inversemi. Má tedy I≤N.
Pokud B navštíví, celkový deficit je nejméně5, a tedy

    I≤⌊(4N−5)/3⌋.

Pro všechna N≤7 je tato mez≤N. Žádná permutace kratší než8
tak nemůže mít více inversí než prvků; výše uvedená osmiprvková
permutace má9. Pojem „shortest“ v odpovědi je tím ověřen obecně,
nikoli jen kontrolou jednoho příkladu.

Pro libovolné velké N vezmi největší M≤N s M≡2 mod3.
Konstrukci délky M doplň vzestupně N−M největšími hodnotami.
Přes hranici přibývají jen správně uspořádané dvojice, takže
3-,5-,7-uspořádání zůstává a počet inversí je
(4M−5)/3=4N/3+O(1). Spolu s univerzální horní mezí P0789
to dává maximum4N/3+O(1) pro všechny N, jak úloha požaduje.

Celá26 včetně všech vět odpovědi je uzavřená. Samostatné
P0785 o algoritmických průměrech v25 se tím nemění. Další
kurzor je22 na103/622 a TheoremP/24 na91/104/622–623.

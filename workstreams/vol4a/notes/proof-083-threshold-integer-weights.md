# Prahové funkce: definice, celočíselnost a velikost vah

7. listopadu 2026. §7.1.1, celá p75/file92; úloha96 na p91/file108,
odpověď p551–552/file568–569. P1049–P1056, checkpoint X0112.
Původní sazba p75, zadání a obou stran odpovědi zobrazena. OCR slouží
jen k navigaci; rozdělení společného OCR souboru podle formfeed není
spolehlivou mapou file pages, proto nyní používám `djvutxt -page`.
Žádný matematický program ani enumerace.

## 1. Všechny příklady a převody na p75

V (75) je nerovnost **≥**, váhy i práh jsou celá čísla. Pro bitové
vstupy je součet n jednotkových vah mezi0 a n. Dosáhne n právě při
samých jedničkách a dosáhne1 právě při alespoň jedné jedničce. Tím
jsou (76)/(77) dokázány. Při obvyklé prázdné konjunkci/disjunkci
fungují i pro n=0: [0≥0]=1, [0≥1]=0. V (78) je t≥1; z 2t−1
hlasů převažují jedničky právě při jejich počtu alespoň t.
Pro (79) jsou hodnoty −x rovny0,−1, takže [−x≥0]=1−x.

V (80) se číselné a lexikografické porovnání stejně dlouhých
bitových řetězců shodují: při prvním rozdílu má jeho váha2^k
větší velikost než součet všech nižších vah2^k−1. Rovnost všech
bitů dává rovnost čísel. U knapsack interpretace jsou velikosti
nezáporná celá čísla, x_j je indikátor přítomnosti předmětu;
negace součtu≥t je přesně součet≤t−1. Nic se nezaokrouhluje.

Při záporné váze w_j=−c, c>0, položme y_j=1−x_j. Potom
−c x_j=c y_j−c. Přechod na kladnou váhu proto vyžaduje právě
posun prahu t→t+c, jak uvádí text. Jednotlivé substituce se
skládají nezávisle; nulové váhy se nemění. Jde o změnu polarity
vstupu, nikoli o tvrzení, že původní funkce byla monotónní.

Pro (81)–(84) označme W=Σw_j≥0 a d=2t−1−W. Vytištěné hodnoty
a=max(0,d), b=max(0,−d) splňují a−b=d a ab=0. Délka mediánu je

    L=W+a+b=2(b+t)−1.

Je kladná a lichá: při W≥1 je L≥1; při W=0 je |2t−1|≥1.
Jeho práh T=(L+1)/2=b+t je tedy kladné celé číslo a současně
T=max(t,W+1−t), přesně (84). Počet jedniček je b+Σw_j x_j,
takže medián je1 právě při Σw_j x_j≥t. Důkaz zahrnuje i libovolný
celočíselný t mimo interval1..W a všechny nulové váhy. Zejména
W=0,t=0 dává jedinou konstantu1 a W=0,t=1 jedinou konstantu0.
Pro n≥1, w_j=1 a t=n nebo t=1 dostáváme přesně (83); zápis
s exponentem n−1 se pro n=0 nepoužívá.

Tím je pokryt celý matematický obsah p75, nejen názvy příkladů.

## 2. Úloha96: všechny větve celočíselného převodu

Nechť f(x)=[w·x≥t] s reálnými parametry. Je-li f identicky1,
stačí w=0,t=0; je-li identicky0, stačí w=0,t=1. Tím je také
ošetřen nulární případ. Vytištěné maximum přes f(x)=0 jinak
existuje a je menší než t, protože jde o neprázdnou konečnou
množinu. Jeho rozdíl od t označme ε>0. Podmínky jsou právě

    w·x−t≥0       pro f(x)=1,
    t−w·x−ε≥0     pro f(x)=0.

Koeficienty tohoto homogenního systému v proměnných(w,t,ε)
jsou celé. Doplním celou indukci, na kterou odpověď odkazuje.

**Lemma.** Má-li celočíselný systém A v≥0 reálné řešení s
v_N>0, má i celočíselné řešení se stejnou přísnou podmínkou.

Pro N=1 musí být všechny koeficienty nezáporné, a v_1=1 vyhoví.
Pro N>1 eliminujeme v_1. Řádky s kladným prvním koeficientem
určují dolní racionální lineární meze L_i(v_2,…,v_N), záporné
horní meze U_j. Nulové řádky se ponechají. Na zbývající proměnné
klademe všechny podmínky L_i≤U_j a původní nulové řádky;
kladnými společnými jmenovateli převedeme koeficienty na celá
čísla. Jde opět o homogenní systém. Původní řešení jej splňuje
a má v_N>0, takže indukce dává celočíselné zbývající souřadnice.
Všechny meze pro v_1 jsou pak racionální. Je-li interval oboustranně
omezen, vezmeme libovolný racionální bod mezi největší dolní
a nejmenší horní mezí, včetně případu jejich rovnosti. Při chybějící
jedné nebo obou stranách existuje racionální bod také. Vynásobení
celého vektoru kladným jmenovatelem v_1 dokončí důkaz a zachová
v_N>0. Prázdný soubor podmínek nepůsobí výjimku.

Aplikace s poslední souřadnicí ε dává celočíselné w,t,ε a ε≥1.
Nulové vstupy tedy mají w·x≤t−1, jedničkové w·x≥t. Funkce je
beze změny. Opačný směr je okamžitý, protože celá čísla jsou
reálná. Kniha netvrdí polynomiální algoritmus tohoto převodu;
eliminace může vytvářet součin počtů dolních a horních mezí.
Konstantní větev vynechaná při zavedení maxima je zde výslovně
doplněna; nejde o nález chybného závěru.

## 3. Dodatek96: přesná Hadamardova mez má vlastní důkaz

Pro n≥1 normalizujme předchozí reálné řešení dělením ε, takže
máme neprázdný polyedr v prostoru z=(w_1,…,w_n,t):

    w·x−t≥0       pro f(x)=1,
    w·x−t≤−1      pro f(x)=0.

Koeficientové řádky jsou, až na změnu znaménka, (x,−1) pro
všechna x∈{0,1}^n. Mají plnou hodnost n+1: řádek x=0 určí
poslední souřadnici a rozdíly řádků x=e_j a x=0 první n.

**Existence aktivní báze bez předpokladu omezenosti polyedru.**
Začněme libovolným přípustným bodem. Není-li hodnost aktivních
řádků plná, vezměme nenulový směr d v jejich společném jádře.
Plná hodnost všech řádků zaručí řádek s nenulovým skalárním
součinem s d. Zvolme znaménko d tak, aby se jeho přípustná
rezerva zmenšovala. Po konečně velkém kladném posunu narazíme
na první neaktivní omezení; existuje minimum kladných poměrů
rezerv k rychlostem jejich poklesu. Staré aktivní řádky zůstanou
aktivní a nový je na nich nezávislý, neboť jeho součin s d není0.
Po nejvýše n+1 zvýšeních hodnosti získáme bod s n+1 nezávislými
aktivními řádky. Nepotřebujeme optimum neomezeného lineárního
funkcionálu ani předpokládat předem existenci vrcholu.

Vybrané rovnosti zapíšeme bez znaménkové orientace jako

    M z=b,   M_i=(x^(i),−1),   b_i=f(x^(i))−1 ∈{0,−1}.

Determinant D=det M je nenulové celé číslo. Cramerovo pravidlo
dává |D|z celočíselné; kladné násobení zachová všechna jedničková
omezení a u nulových zvětší mezeru z1 na |D|≥1. Dostáváme tedy
platnou celočíselnou reprezentaci. Její j-tá váha má velikost
|det M_j|, kde se j-tý sloupec M nahradí b.

Matice M_j má jeden konstantní sloupec−1 a n ostatních sloupců,
z nichž n−1 obsahuje bity a poslední obsahuje0,−1. Změnou
znamének konstantního a posledního sloupce dostaneme matici
s jedním sloupcem samých1 a n bitovými sloupci. Nahraďme každý
bitový sloupec c sloupcem2c−1. Determinant se v absolutní hodnotě
vynásobí2^n a všechny položky nové matice jsou±1.

Hadamardova nerovnost zde plyne přímo z Gramova–Schmidtova
procesu: absolutní determinant je součin délek ortogonálních
zbytků řádků, z nichž žádný není delší než původní řádek;
singulární případ má determinant0. Každý původní řádek má
délku sqrt(n+1). Proto pro každou váhu platí přesně

    |w'_j|=|det M_j| ≤ (n+1)^((n+1)/2) / 2^n.

To je vytištěná mez. Neklade tutéž mez na práh t; důkaz ani kniha
to zde netvrdí. Konstantní funkce mají nulové váhy, a n=0 nemá
žádnou váhu k omezení. Žádný externí determinantový odhad ani
numerické LP jsme nepoužili. Takto je matematický horní dodatek
úlohy96 uzavřen nezávisle na dostupnosti citované věty16.

## 4. Přesné meze, bibliografie a errata

P1056 byla v tomto checkpointu ponechána partial: samotná horní mez
nedokazuje poslední větu odkazující na 112. Nyní ji uzavírá X0124,
notes/proof-098-threshold-weight-lower-bound.md, úplným důkazem dolní
meze a přesným porovnáním exponentů. Zdejší hotový horní argument
se neopakoval. Aktuálně je tedy uzavřeno i toto dopředné srovnání.

[Primární Springer záznam](https://doi.org/10.1007/BF02478259)
potvrzuje McCullocha/Pittse, název, rok1943, svazek5 a strany115–133;
abstrakt popisuje logické modely neuronových sítí. Počet navazujících
prací „thousands“, prioritu a celý neurofyziologický model znovu
nehodnotím. [Primární IBM záznam](https://research.ibm.com/publications/theory-of-majority-decision-elements)
potvrzuje autory Muroga/Toda/Takasu, název, časopis a rok1961.
Odkaz DOI10.1016/0016-0032(61)90702-5 nešlo otevřít; přesné
strany376–418 a číslování Theorem16 zůstávají bibliografickou
výjimkou. Matematická mez je doložena výše vlastním důkazem.

Všechny relevantní vrstvy `all4a-pre`, `all4a`, `err4a`, `all4f0`,
`err4f0` byly prohledány podle stran a threshold/Hadamard/answer96.
F0 oprava jména McCullough→McCulloch z2.3.2009 je v prvním tisku
4A již zapracována. Žádný nový nález. P75 může přejít na plnou
argumentovou kontrolu; p91 a p551 zůstávají partial kvůli přesně
vymezeným starším výzkumným/addendovým mezerám. Pozdější X0124 dokládá
celou p552 přes hotové úlohy97–103 a nově uzavřenou P1056.

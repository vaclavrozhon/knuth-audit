# Zachování uspořádání, generovatelné mezery a dvě sousední třídy

7. listopadu 2026. Sazba90/file101,103–104/file114–115 a
622–623/file633–634 zobrazená. Rozsah: celé L/K a úloha20,
celá21 včetně počtu mezer, odvozená mez23 a hlavní matematické
části25. Dvě dodatečné průměrové konstanty25 závisející na42
zůstávají výslovně otevřené. U26 zde dokazujeme pouze tvrzení
z hlavního textu90, nikoli ještě ostré maximum či nejkratší příklad.

Pět vrstev `sources/insertion-errata-review.json` převzato:
známá oprava1998 na90 mění rozsah přírůstků na h_(t−1),…,h_0.
Pro právě dokazované L/K/20/21/23/25 není v evidenci změna vzorců.
Historická prvenství Sylvestera/Manna ani formulaci o stavu výzkumu
v době vydání zde nezávisle nedohledáváme; nejsou tvrzením o stavu2026.

Zásada vzorů1/4B: celý indexový přenos a rozdíl mezi rovnoměrnou
třídou výsledků a skutečným výstupem algoritmu mají vlastní důkaz.
Zkontrolované přechody Table4 z P0715 se neopakují.

## P0774: Lemma L včetně rovností a prázdných případů

Máme m,n,r≥0, posloupnost x délky m+r, posloupnost y délky n+r
a r různých párů y_j≤x_(m+j). Pro1≤j≤r označ T j-tou
posuzovanou hodnotu po seřazení x, totiž x_(m+j).
Nejméně m+j původních výskytů x je≤T. Nejvýše m z nich patří
k nespárovaným pozicím1,…,m; nejméně j jsou tedy spárované.
Jejich **různé výskyty** y jsou≤svému x≤T. Nejméně j hodnot
y je≤T, a proto jejich j-tá pořadová statistika y_j≤T.

To platí současně pro všechna j. Výskyty, nikoli rozdílné číselné
hodnoty, zajišťují počítání při shodných klíčích. Žádný předpoklad
nezávislosti, různosti hodnot ani m=n není potřeba. Pro r=0
je závěr prázdný; m=0 či n=0 týž početní argument neporušují.

## P0775: Theorem K a úplný indexový překlad úlohy20

Nechť původní pole délky N je k-ordered a h,k≥1. Chceme po
uspořádání každé h-třídy dokázat K_i≤K_(i+k) pro1≤i≤N−k.
Polož u,v∈{1,…,h}, i≡u, i+k≡v modulo h, a

    m=(u+k−v)/h≥0.

Původní dvě posloupnosti jsou
y_j=K_(u+(j−1)h), x_j=K_(v+(j−1)h).
Nechť L_u,L_v jsou jejich skutečné délky. Počet existujících
párů posunutých o k je

    r=L_v−m=⌊(N−u−k)/h⌋+1.

Pro právě zvolené i je r≥1; z i=u+ℓh≤N−k plyne ℓ+1≤r.
Máme L_u≥r, takže n=L_u−r≥0, a délky jsou přesně n+r,m+r.
Původní k-uspořádání dává

    y_j=K_(u+(j−1)h)≤K_(u+k+(j−1)h)=x_(m+j),
    1≤j≤r.

Lemma L zachová tyto nerovnosti po nezávislém uspořádání obou
tříd. Pro j=ℓ+1 je levá pozice i a pravá i+k: požadovaný závěr.
Pokud u=v, jde prostě o dvě pozice téže nyní uspořádané třídy
a závěr je okamžitý; není třeba předstírat dvě disjunktní pole.
Pro k≥N žádný pár není. Pro h≥N se žádná třída nemění.
Shodné klíče jsou přípustné a stabilita uvnitř třídy není potřeba.

To doplňuje všechny m,n,r a všechna posunutí, které odpověď20
jen slovně naznačuje. Nezaměňujeme původní hodnoty v hypotéze
za již uspořádané hodnoty v závěru.

## P0776: konkrétní důsledky90 a mez2N

Indukcí K zachovává každý nový průchod všechna dříve získaná
uspořádání. Po7,5,3 je tedy pole současně7-,5- a3-ordered;
totéž platí pro jednotlivé již doložené řádky Table4. Naproti
tomu8,4,2 nikdy nepřesunou prvek mezi paritami; poslední2-sort
uspořádá právě původní parity. U náhodného vstupu je výsledek
rovnoměrný2-ordered podle P0757. Převzatý P0737 tak dává
právě Θ(N^(3/2)) inversí před posledním průchodem.

Pro libovolné3-,5-,7-ordered pole jsou všechny mezery≥5
generovatelné z3,5,7: máme5,6,7 a pak přidáváme3.
Monotónní řetězení uspořádání vylučuje inverse s těmito mezerami
i s mezerou3. Zůstávají jen mezery1,2,4. Označ jejich počty
I_1,I_2,I_4. Každá inverse K_i>K_(i+4) vynutí

    K_(i+1)≤K_(i+4)<K_i≤K_(i+3).

Mezera2 mezi pozicemi i+1,i+3 je proto neinverse. Různá i
dávají různé takové mezery, takže I_2+I_4≤N−2. Dále I_1≤N−1.
Pro N≥2 tudíž celkem I≤2N−3<2N; pro N≤1 je I=0.
Je tím doloženo přesné tvrzení90. Ostré přibližně4N/3 z26
z této injekce **nevyvozujeme** a zatím je ponecháváme ke kontrole.

## P0777: úloha21, kanonický rozklad a oba směry

Nechť h,k jsou nesoudělná kladná celá čísla. Násobení h
permuuje zbytky modulo k, takže každé celé n má právě jeden tvar

    n=xh+yk,  0≤x<k,  y∈Z.

Jednoznačnost plyne z k|(x−x')h a nesoudělnosti; existence
z Bézoutova vztahu nebo přímo z této permutace zbytků.
Všechny ostatní celočíselné rozklady jsou x+tk, y−th.
Je-li nějaký rozklad x_0h+y_0k nezáporný, potom x_0=x+tk
s t≥0, protože0≤x<k a x_0≥0. Kanonické y=y_0+th je tedy≥0.
Naopak y≥0 již dává nezáporný kanonický rozklad. Generovatelnost
je proto ekvivalentní právě y≥0, nikoli pouhé existenci rozkladu v Z.

Polož F=hk−h−k. Kanonický rozklad F−n má

    x'=k−1−x,  y'=−1−y.

Přímé sečtení dává F, a0≤x'<k. Právě jedno z celých y,y'
je nezáporné. Dokazujeme tak pro **všechna celá n**, i záporná,
ekvivalenci „n je generovatelné právě když F−n není“.

## P0778: největší mezera a přesný počet

Nula je generovatelná a žádné záporné číslo není. Symetrie P0777
proto říká, že F generovatelné není a všechna n>F jsou.
Pro h,k≥2 je F≥1 a F+1=(h−1)(k−1) je sudé: obě h,k
nemohou být sudé. Interval0,…,F se rozpadá na(F+1)/2 různých
dvojic {n,F−n}; v každé je právě jedna mezera. Protože0 není
mezera a nad F žádné nejsou, počet kladných mezer je přesně

    (h−1)(k−1)/2.

Je-li h=1 nebo k=1, všechna nezáporná čísla jsou generovatelná,
kladných mezer je0 a největší negenerovatelný **celý** počet je
F=−1. I tento okraj odpovídá formulaci; netvrdíme existenci
nezáporné mezery v tomto případě.

## P0779: přenos na pole, úloha23 a související tvrzení91

Je-li d=xh+yk≥0 generovatelné, cesta z i do i+d nejprve xkrát
o h a pak ykrát o k zůstává mezi oběma konci. V h- a k-ordered
poli proto K_i≤K_(i+d). Zvlášť to platí pro
d≥F+1=(h−1)(k−1), přesně jak požaduje závorka v21.

Při g-sortu pole, které je gh- a gk-ordered, se každá g-třída
stane h- a k-ordered podposloupností. Pro vložení zvolené položky
mohou být předchozí větší položky pouze v negenerovatelných
vzdálenostech uvnitř této podposloupnosti. Těch je nejvýše
(h−1)(k−1)/2, což je počet přesunů připadající na danou položku
v tvrzení91. Neměníme to na neodvozené tvrzení o součtu obou
směrů incidentních inversí.

V úloze23 jsou a=h_(s+2), b=h_(s+1) nesoudělné. Podle K je
pole před dalším průchodem současně a- i b-ordered. Každá jeho
inverse má skutečnou poziční vzdálenost≤ab−a−b. V jedné třídě
modulo h_s jsou takové vzdálenosti ℓh_s; pro každý pravý konec
jich je nejvýše⌊(ab−a−b)/h_s⌋. Počítáme počáteční inverse
podposloupností, jejichž součet se přesně rovná B_s; nemusíme
udržovat tento odhad na dočasných polohách při přesouvání.
Dostáváme

    B_s≤N⌊(ab−a−b)/h_s⌋=O(Nab/h_s).

To je dokonce o něco ostřejší než zaokrouhlená horní mez
v odpovědi23. Pokud a nebo b je1, je pole již seřazené a B_s=0;
zápornou podlahu v tomto okraji nepoužíváme.

## P0780: úplná struktura úlohy25

Každá celá mezera d≥2 je2x+3y s x,y≥0. V současně2- a
3-ordered permutaci jsou tedy možné pouze inverse mezi sousedy.
Dvě sousední inverse nemohou sdílet vrchol: K_i>K_(i+1)>K_(i+2)
by odporovalo2-uspořádání. Množina inversí je proto matching
hran cesty1,…,N.

Naopak libovolný takový matching realizujeme záměnou příslušných
disjunktních sousedních párů v1,…,N; žádné jiné inverse nevzniknou,
takže výsledek je2- i3-ordered. Je to i jediná realizace: hodnota
na pozici i se rovná

    i+[inverse(i,i+1)]−[inverse(i−1,i)],

protože její pořadí mezi všemi hodnotami je i plus počet pozdějších
menších minus počet dřívějších větších. To zároveň dokazuje
rozklad na jedničkové bloky a prohozené dvojice: permutace začíná
1 nebo21 a po odebrání tohoto bloku dostaneme stejnou úlohu.

## P0781: počet, maximum a Morseův popis

Pro počet A_N dostáváme A_0=A_1=1 a A_N=A_(N−1)+A_(N−2).
S konvencí F_0=0,F_1=1 je tedy A_N=F_(N+1). Matching má
nejvýše⌊N/2⌋ hran a disjunktní páry(1,2),(3,4),… této meze
dosahují. To je přesné maximum inversí.

Jedničkový blok označíme tečkou, dvojici čárkou. Jejich délky
jsou1 a2, nikoli počet značek; počet čárek je přesně počet inversí.
Tím je uvedená „Morse code“ interpretace úplnou bijekcí.
Pro přesně j čárek stačí po zkrácení každé dvojice o jednu pozici
vybrat jejich j míst mezi N−j bloky, takže váhový polynom je
∑_j binom(N−j,j)y^j. Jeho bivariátní GF je1/(1−z−yz²).

## P0782: celý součet inversí a uzavřená Fibonacciho formule

Derivací podle y při y=1 získáme GF všech inversí

    ∑_(N≥0)T_N z^N=z²/(1−z−z²)².

Pro úplnou kontrolu tištěného uzavřeného tvaru polož
D=1−z−z², A(z)=z/D=∑F_Nz^N a B(z)=z²/D=∑_(N≥1)F_(N−1)z^N.
Pak

    zA'−A=(z²+2z³)/D²,
    2zB'=(4z²−2z³)/D².

Jejich součet dělený5 je právě z²/D². Koeficienty pro N≥1 jsou
tudíž

    T_N=((N−1)F_N+2N F_(N−1))/5,

přesně odpověď623; pro N=0 je T_0=0 samostatně, bez nutnosti
zavádět F_(−1). Tím je ověřen i odkaz na součet čárek.

## P0783: rovnoměrný průměr a konstanta

Řešení Fibonacciho rekurence z jejích kořenů
φ=(1+√5)/2, ψ=(1−√5)/2 dává F_N=(φ^N−ψ^N)/√5.
Proto F_N/F_(N+1)=φ^(−1)+O(φ^(−2N)) a analogicky pro N−1.
V rovnoměrné třídě všech F_(N+1) výsledků tedy

    E I=T_N/F_(N+1)
       =N(φ^(−1)+2φ^(−2))/5+O(1)
       =N φ^(−1)/√5+O(1)≈0.276393N+O(1).

Poslední rovnost používá φ²=φ+1 a √5=2φ−1; žádná nová
pravděpodobnostní nezávislost se zde nepředpokládá.

## P0784: konkrétní nerovnoměrnost výstupu algoritmu

Pro N=4 je právě pět2- a3-ordered permutací:
1234,2134,1324,1243,2143. Tento seznam plyne ze všech matchingů
čtyřvrcholové cesty, nikoli z výpočetní enumerace vstupů.
Každá je pevným bodem obou průchodů, takže každá je dosažitelná
při pořadí3,2 i2,3. Theorem K zároveň říká, že jiný výstup není.
Rovnoměrných vstupů je4!=24, avšak24 není dělitelné5.
Počty vzorů proto nemohou být stejné. To je úplný důkaz tvrzení
na90 o nemožnosti jednoduše převzít rovnoměrnou distribuci všech
h- a k-ordered výsledků pro obecné přírůstky.

## P0785 — partial: dva skutečné algoritmické průměry

Odpověď25 dodává N/4 pro3-sort následovaný2-sortem a N/3 pro
opačné pořadí, s odkazem na42. Tyto konstanty neplynou z právě
dokázaného rovnoměrného průměru0.276393N; P0784 naopak vysvětluje,
proč takový přenos není platný. Jejich samostatné odvození dosud
chybí a bude připojeno při celé42. Tři otázky samotného zadání25
jsou vyřešeny, ale tyto dvě další věty odpovědi se neoznačují checked.

Další souvislý kurzor: ostrá část26 (obecná konstrukce, mez a
nejkratší příklad), potom22 a TheoremP s dolní konstrukcí24.
Věta o stavu obecné analýzy v době vydání je výslovně přeskočený
historický údaj; nevydáváme ji za nové zjištění o současné literatuře.

# Úloha104(c): přesné minimum61 a celočíselné minimum63

7. listopadu 2026. Zadání p92/file109, odpověď p553/file570.
Checkpoint X0117, P1103–P1110; vymezené limity P1114–P1120.
Originály i zvětšený detail zadání přečteny. Poslední proměnná
je x_10 s **jediným** výskytem, nikoli s exponentem10; index
a exponent v OCR se nesmějí zaměnit. Větev odpovědi je w_8≥2.
Žádný program, LP řešič, průchod512 vstupů ani census nebyl spuštěn.
Všechny certifikáty níže jsou racionální a ručně odvozené.

## 1. Nepodstatnost x_10 a přípustnost racionálního bodu

Prvních devět vah tvoří vektor

    a=(29,25,19,15,12,8,8,3,3),       Σa=122.

Včetně poslední váhy1 je délka123 a práh62. Dokážeme, že součet
S=Σ_{j=1}^9a_jx_j nikdy není61. Sudé váhy12,8,8 dávají přesně
možné součty E∈{0,8,12,16,20,28}. Liché váhy jsou29,25,19,15,3,3.
Pro S=61 by jejich vybraná lichá suma musela být některá z

    61,53,49,45,41,33.

Musela by použít lichý počet vah. Jediná váha je nejvýše29;
pět vah má sumu nejméně94−29=65. Tři váhy dávají právě

    {21,25,31,35,37,43,47,51,57,59,63,69,73}.

Tento seznam vznikne po rozdělení podle největší vybrané váhy
29/25/19/15; zahrnuje obě stejné váhy3 jako dvě dostupné pozice.
Žádná z požadovaných šesti sum v něm není. Hodnota61 tedy
nenastane. Proto [S+x_10≥62]=[S≥62], takže x_10 je opravdu
nepodstatná, na všech vstupech.

Racionální vektor w*=(a/2,0) má součet61. Na každé pravdivé
podpoře má podepsanou mezeru S−61≥1; na nepravdivé≤−1.
Je tedy přípustný v přesném LP103 a představuje danou funkci.
Tím je dokázána horní mez61 pro reálné optimum; samotná
přípustnost ještě jeho minimálnost nedokazuje.

## 2. Úplný seznam všech podpor se S=62

Stejné rozdělení dovoluje vypsat všechny těsné podpory bez
procházení všech bitových vstupů. Lichá část musí mít sudý
počet členů a sumu v{62,54,50,46,42,34}. Nula členů ani všech
šest (suma94) nevyhoví. Ze dvojic připadají v úvahu jen sumy
54=29+25 a34=19+15. Ze čtveřic použijeme komplement páru
v celkové sumě94; jeho suma může být32,40,44 nebo48:

    32=29+3 (dvě volby), 40=25+15,
    44=29+15=25+19,      48=29+19.

Každou možnost doplníme příslušným E. Dostaneme přesně deset
podpor, všechny uvedené v následující tabulce. Jejich prvky jsou
indexy proměnných; všechny mají původní sumu62. Každá je také
prime, protože odstraněním kteréhokoliv jejího prvku ztratíme
alespoň3 a práh62 již nedosáhneme.

| Řádek | Podpora B | λ pro původní LP | μ pro větev w_8≥2 |
|---|---|---:|---:|
|A|126|15/2|7|
|B|127|15/2|7|
|C|34567|14|13|
|D|246789|6|5|
|E|23589|8|7|
|F|2348|1|0|
|G|2349|1|2|
|H|14589|9|8|
|I|13689|7/2|3|
|J|13789|7/2|3|

## 3. Duální certifikát reálného minima61, i pro deset vah

Pro každý řádek B platí nutná podmínka103:

    2Σ_{j∈B}w_j−Σ_{j=1}^{10}w_j≥1.

Multiplikátory λ v tabulce jsou nezáporné a mají součet61.
Každý z prvních devíti indexů má váženou incidenci31:

    1: A+B+H+I+J,
    2: A+B+D+E+F+G,
    3: C+E+F+G+I+J,
    4: C+D+F+G+H,
    5: C+E+H,
    6: A+C+D+I,       7: B+C+D+J,
    8: D+E+F+H+I+J,   9: D+E+G+H+I+J.

Dosazení λ dává u každého řádku tohoto seznamu přesně31.
Index10 se nevyskytuje nikde. Sečtení nutných nerovností proto
dává

    Σ_{j=1}^9w_j−61w_10≥61,
    tedy Σ_{j=1}^{10}w_j≥61+62w_10≥61.

Vektor w* tuto mez dosahuje, takže reálné optimum je přesně61.
Tento certifikát nevyžaduje úplný seznam všech prime implikantů;
použité podmínky jsou nutné a horní přípustnost již byla dokázána
na všech vstupech v §1.

## 4. Jednoznačnost optimálního bodu

U libovolného optima61 musí předchozí nerovnost vynutit w_10=0.
Všechny λ jsou kladné, takže všechny deset řádků musí mít
mezeru právě1. Každá uvedená podpora má proto novou váhu31.
Rozdíly A/B a F/G dávají w_6=w_7=p a w_8=w_9=q.
Označme zbývající váhy a,b,c,d,e v pořadí1..5.
Z rozdílů I−A, E−F, D−F a H−E dostáváme postupně

    b=c+2q,  d=e+q,  c=2p+q,  a=b+c−d.

Rovnosti A,C,F pak říkají

    7p+6q−e=31,
    4p+2q+2e=31,
    4p+6q+e=31.

První minus třetí dává e=3p/2. Zbývají
7p+2q=31 a11p/2+6q=31, tedy p=4, q=3/2, e=6.
Zpětné dosazení dává přesně

    (a,b,c,d,e,p,p,q,q)=(29,25,19,15,12,8,8,3,3)/2.

Reálné optimum je tedy nejen necelé, ale **jediné**. Tím je
vyloučena možnost jiné celočíselné reprezentace se stejnou
délkou61; pouhé nalezení jednoho necelého optimálního bodu
by samo tuto možnost nevylučovalo.

## 5. Platnost vytištěných celočíselných vah na všech vstupech

Vytištěný vektor je

    v=(15,13,10,8,6,4,4,2,1,0),       Σv=63.

Označme δ=x_1+x_2+x_3+x_4+x_8−x_9. Pak pro prvních devět
proměnných platí2v·x=S+δ. Jestliže S≥62, musí být δ≥1:
při x_9=0 a δ≤0 by S≤12+8+8=28; při x_9=1 a δ≤0 je
vybrán nejvýše jeden z indexů1,2,3,4,8, a tedy
S≤3+29+12+8+8=60. Pro S≥63 tudíž máme S+δ≥64.

Zbývá S=62. Jeho všech deset podpor je v §2; na devíti z nich
je δ=2 a na F=2348 je δ=4. Také zde S+δ≥64, tedy v·x≥32.
Každý pravdivý původní vstup je pravdivý v nové většině délky63.
Obě funkce jsou self-duální, proto stejná inkluze na komplementu
vstupu dává opačnou implikaci i pro nepravdivé hodnoty.
Vektor v přesně reprezentuje původní funkci na všech vstupech.

## 6. Přesná LP větev w_8≥2 a celočíselné minimum

Multiplikátory μ ve čtvrtém sloupci mají součet55. Podle téže
incidenční tabulky mají indexy1..7 a9 váženou incidenci28,
index8 incidenci26 a index10 nulu. Jejich součet nutných
nerovností je proto

    Σ_{j=1}^9w_j−4w_8−55w_10≥55.

Přidáme4 násobky podmínky w_8≥2 a56 násobků w_10≥0:

    Σ_{j=1}^{10}w_j≥63.

Vektor v má w_8=2 a tuto mez dosahuje. Proto omezené **reálné**
LP skutečně dává vytištěné celočíselné optimum63, jak tvrdí
odpověď; nejde pouze o nalezený celočíselný bod v této větvi.

Pro globální celočíselnou většinu je délka lichá. Dolní mez61
je pro celočíselné váhy nedosažitelná podle §4, takže každá
celočíselná lichá reprezentace má délku nejméně63. Bod v ji
dosahuje, a tedy je globálně optimální. Pokud bychom optimalizovali
všechna celočíselná řešení LP bez podmínky lichosti, nemůže existovat
ani součet62: zmenšení některé kladné váhy podle proof-087 by
vytvořilo zakázané celočíselné řešení se součtem61.

Ani konstanty či opačné literály nevytvoří kratší plochou většinu:
po zrušení opačných párů a zafixování nepodstatných proměnných
se použije argument self-duality a nezáporných vah z proof-086.
Proměnné váhy stále splňují nutné nerovnosti výše. Pro délku≤61
by musely mít součet61 bez konstant a rovnat se necelému w*,
což není možné.

## 7. Co z dodatku104(c) zůstává otevřené

Tato poznámka uzavírá konkrétní zadání104(c), odstranění x_10,
reálné optimum, přesnou větev w_8≥2 a globální celočíselné
optimum. Neuzavírá následující vytištěný census:

* vytištěný počet175428 self-duálních devítiproměnných prahových
  funkcí, jehož přesná konvence normalizace ještě není ověřena;
* tvrzení, že právě dva typy mají necelé reálné minimum;
* necelé minimum druhého explicitního příkladu s vahami
  (17,15,11,9,7,5,4,2,1);
* globální maximum první minimální váhy u příkladu
  (42,22,18,15,13,10,8,4,3);
* globální a jednoznačné maximum celkové délky u příkladu
  (34,32,28,27,24,20,18,15,11);
* globální maximum poslední váhy u téhož příkladu.

Úplná doména normalizace/ekvivalence těchto censů i příslušné
certifikáty dosud nejsou ověřeny. Žádný z těchto rozsáhlých
censů se znovu nespouští. Číselné globální výroky se nezaměňují
s právě dokázanou jednou konkrétní funkcí. Žádný nový nález.

Všech pět relevantních vrstev4A/F0 bylo prohledáno podle
stran92/553, úlohy104, K a čísel v dodatku. Oprava104 na p147
fasciklu se týká jiného algoritmu s řádky a sloupci; tato místa
neopravuje. Primární článek Muroga/Tsuboi/Baugh z roku1970 se
v rychlé rešerši nepodařilo zpřístupnit. Přesné bibliografické
údaje a historické okolnosti jsou výslovná výjimka; jeho census
a globální extrémy zůstávají matematicky partial, neuzavírají
se pouhou bibliografickou citací.

# Rozšířené testy prvočíselnosti: strany 394 a 396

Audit 3. listopadu 2026, třetí vydání, první dotisk 1997.
Strany [394](../images/vol2-p394.png) a [396](../images/vol2-p396.png)
byly prohlédnuty v původní sazbě. Symboly v OCR nejsou použity jako
samostatný důkaz.

**Výsledek:** podmínka Brillharta–Lehmera–Selfridgea na straně 394 je
správná. Níže je vlastní důkaz včetně pomocných podmínek, které kniha
odkazuje do původního článku. Dva velké příklady mají přesné certifikáty.
Teoretické výsledky APR a Adleman–Huang na straně 396 souhlasí s
primárními zdroji. Dobová měření a jejich rozsah jsou oddělena od
zaručených časových mezí. Bibliografický rok článku Selfridge–Wunderlich
je řešen samostatně v C0165.

## 1. Co je vstup a co se musí ještě ověřit

N je liché celé číslo větší než 1. Rozložíme

    N - 1 = F- R-,    N + 1 = F+ R+.

F- a F+ jsou části se známým úplným prvočíselným rozkladem.
Zbývající části R-, R+ mají všechny prvočíselné dělitele alespoň b.
V následujícím důkazu jsou F-, F+ sudé a

    gcd(F-,R-) = gcd(F+,R+) = 1,    R-,R+ > 1.

Těchto podmínek dosáhneme převedením celých mocnin známých prvočísel
do F- a F+. F- ani F+ se tím nezmenší, takže se nezhorší knižní
nerovnost. Je-li R- nebo R+ rovno 1, lze místo kombinovaného testu
použít úplný test z [dřívější kontroly](primality-lucas.md),
respektive základní Lucasův test pro N-1. Sudé N se vyřeší předem.
Protože zbývající prvočinitelé jsou liché, můžeme bez újmy brát b >= 2.

U_k(P,Q) označuje Lucasovu posloupnost

    U_0 = 0, U_1 = 1, U_(k+1) = P U_k - Q U_(k-1).
    D = P^2 - 4Q

je její diskriminant. Jacobiho symbol (D/N) zobecňuje znaménko
kvadratického zbytku na lichý složený jmenovatel; přesná definice
a pravidla jsou v [primality-jacobi.md](primality-jacobi.md).

Pomocné podmínky certifikátu jsou následující.

1. Pro každé prvočíslo q dělící F- je k dispozici báze a s
   a^(N-1) = 1 mod N a gcd(a^((N-1)/q)-1,N) = 1.
2. Pro nějakou bázi a platí a^(N-1) = 1 mod N a gcd(a^F- - 1,N) = 1.
3. Zvolíme jeden diskriminant D s (D/N) = -1. Pro každé prvočíslo q
   dělící F+ je k dispozici posloupnost s tímto D, s gcd(Q,N)=1,
   U_(N+1) = 0 mod N a gcd(U_((N+1)/q),N) = 1.
4. Pro nějakou posloupnost se stejným D, opět s gcd(Q,N)=1, platí
   U_(N+1) = 0 mod N a gcd(U_F+,N) = 1.

Báze a mohou být různé. Také dvojice P,Q mohou být různé, ale
diskriminant v bodech 3 a 4 musí zůstat společný. Nesoudělnost Q,N
uvádíme explicitně; za ostatních podmínek ji lze také odvodit.

Samotná velikost F-,F+,b žádný certifikát prvočíselnosti netvoří.
Kniha to netvrdí: výslovně vyžaduje další výpočet popsaný v citaci.
Výsledek gcd=N při hledání svědka také sám nedokazuje složenost.

## 2. Vlastní důkaz knižní meze

Pro prvočíslo l dělící N je řád a modulo l nejmenší kladný exponent,
pro nějž je a umocněné na tento exponent rovno 1. Dělí l-1.
Podmínka 1 proto nutí každou úplnou mocninu q obsaženou ve F-
dělit l-1. Podmínka 2 nutí řád své báze obsahovat alespoň jeden
prvočinitel a0 zbývající části R-. Jelikož gcd(F-,R-)=1,

    l = 1 mod a0 F-,    a0 | R-,    a0 >= b.                 (1)

Pro Lucasovu posloupnost definujeme její hodnost modulo l jako
nejmenší kladné k s U_k=0 mod l. Při gcd(l,QD)=1 tato hodnost
dělí l-epsilon, kde epsilon=(D/l) je Legendreův symbol, tedy
+1 nebo -1 podle toho, zda D má druhou odmocninu modulo l.
Důkaz pomocí podílu kořenů kvadratického polynomu je v
[primality-lucas.md](primality-lucas.md). Stejný argument jako
pro řády a podmínky 3 a 4 dávají

    l = epsilon mod c0 F+,    c0 | R+,    c0 >= b.           (2)

Důležité je společné epsilon v obou Lucasových podmínkách.
Prvočísla a0 a c0 jsou různá lichá prvočísla: případný společný
dělitel by dělil současně N-1 a N+1. Proto

    a0 c0 >= b(b+2),    gcd(a0 F-, c0 F+) = 2.             (3)

Předpokládejme, že N je složené, a položme w=N/l>1. Z rovností
N=1 mod a0F- a N=-1 mod c0F+ dostáváme

    w = 1 mod a0F-,    w = -epsilon mod c0F+.

Z dvojice l,w tedy jeden člen, označme jej y, je současně 1
modulo a0F- a c0F+. Druhý člen z je 1 modulo a0F- a -1
modulo c0F+. Oba členy jsou větší než 1, a proto

    y >= a0 c0 F- F+ / 2 + 1,
    z >= max(a0 F- + 1, c0 F+ - 1).                       (4)

Položme A=F- * F+. Je-li F- >= F+, pak (4) dává

    N = yz >= (b^2 A/2 + 1)(b F- + 1) > b^3 A F-/2.      (5)

Je-li F+ >= F-, použijeme i rozdíl alespoň 2 mezi a0,c0:

    N >= (b(b+2) A/2 + 1)(b F+ - 1) > b^3 A F+/2.        (6)

Poslední ostrá nerovnost není zanedbání záporného členu. Rozdíl
jejích dvou stran je přesně

    (b A/2)(2b F+ - b - 2) + b F+ - 1 > 0,

protože b>=2 a F+>=2. Z (5) a (6) plyne spor s knižní podmínkou

    b^3 F- F+ max(F-,F+) > 2N.

Tedy N je prvočíslo. Důkaz nezávisí na tom, zda případný složený N
má opakované prvočinitele; potřebuje jen jedno prvočíslo l|N a w>1.

Pro prvočíselné N potřební svědci existují: pro body 1 a 2 lze
použít primitivní kořen modulo N, tedy prvek řádu N-1. F_N zde
označuje těleso zbytkových tříd modulo prvočíslo N. Pro body
3 a 4 použijeme prvek řádu N+1 v cyklické grupě prvků normy 1
kvadratického tělesa nad F_N. Norma zobrazuje z na z*zbar,
kde zbar je konjugovaný prvek. Při zvoleném nezbytkovém D
lze každý prvek gamma této grupy kromě 1 vyjádřit jako
(P+sqrt(D))/(P-sqrt(D)); vyřešením pro P dostaneme prvek F_N.
Celé P se zvolí se správnou paritou, aby Q=(P^2-D)/4 bylo celé.
Pak hodnost posloupnosti odpovídající primitivnímu gamma je N+1.

Tento existenční argument není nový časový odhad pro hledání svědků.
Knižní slovní údaj o malém dodatečném výpočtu nezaměňujeme za
dokázanou uniformní mez pro každý způsob jejich výběru.

## 3. Dva samostatné velké certifikáty

[Program](../verify_primality_extended.py) a
[výsledky](../results/primality-extended.json) dokazují prvočíselnost:

| Zdrojový tvar | Počet číslic | F- | F+ | b |
|---|---:|---:|---:|---:|
| (2^167-1)/2349023 | 44 | 2175008 | 5904396450 | 2000000 |
| (2^241-1)/22000409 | 66 | 10228522 | 45993638617007146424985960 | 21221 |

V obou případech jsou F- i F+ menší než sqrt(N), takže nejjednodušší
samostatný test s faktorizovanou částí nad sqrt(N) nestačí.

Všechny prvočinitele F-,F+ ověřuje prosté dělení až do odmocniny.
Dolní mez prvočinitelů R-,R+ kontrolují dvě enumerace:
151 318 prvočísel ze síta celkem a nezávisle 1 010 608 lichých
kladných dělitelů menších než příslušné b. U každého dělitele se
kontrolují oba zbytky R-,R+.

Devět podmínek pro N-1 a patnáct pro N+1 splnilo příslušné gcd=1.
Každé použité modulární umocnění se porovnává s vlastním algoritmem
zleva doprava. Lucasovy hodnoty se porovnávají mezi mocninou
matice [[P,-Q],[1,0]] a násobením dvojic v algebře t^2=P*t-Q.
Nejde o dvě spuštění téhož programu.

Pro první N jsou P=1,Q=-13,D=53; pro druhé P=1,Q=-5,D=21.
Nejasné OCR vedlo nejprve k volbám Q=13 a Q=5, které validátor
odmítl. Finální záporné hodnoty Q jsou součástí přesně ověřených
certifikátů; shodu jejich znamének s původní sazbou článku netvrdíme.
První příklad používá bázi 13 kromě podmínky q=37, kde funguje
báze 3. Báze 13 i 2 tam dávají gcd=N a nejsou svědky.
Druhý příklad používá bázi 13 ve všech čtyřech podmínkách N-1.

Při vývoji validátoru byly odhaleny tři neúspěšné předpoklady:
jedna společná báze 13, potom Q=13 v prvním příkladu a Q=5
ve druhém. Logy jsou zachovány. Jde o chyby našeho přepisu či
volby svědků, nikoli o nálezy v Knuthově knize. První hotový
certifikát byl uložen a při posledním pokračování nebyl opakován.
Úspěšné checkpointy trvaly přibližně 0.777 a 0.078 sekundy;
limit jednotlivých běhů byl 120 sekund, poslední návratový kód 0.

## 4. APR: původní odstavec na straně 396

Primární článek Adleman–Pomerance–Rumely, Annals of Mathematics 117
(1983), 173–206, byl získán z Pomeranceovy stránky. Vizuálně
přečtené strany 173–174 výslovně rozlišují deterministickou
a náhodnou variantu. Pro velké N uvádějí mez

    (log N)^(c log log log N)

s absolutní konstantou c. To je knižní zápis
(log N)^O(log log log N). Označíme-li L počet bitů N, je
stejný řád L^O(log log L), nikoli L^O(log L).
Náhodná varianta nikdy nevrátí chybný výsledek; náhodnost
ovlivňuje dobu získání výsledku. Deterministická varianta
nepředpokládá rozšířenou Riemannovu hypotézu.

Jde o kontrolu shody tvrzení a jeho citace. Celý 34stránkový
důkaz z algebraické teorie čísel zde není znovu dokázán ani
označen za kompletně přečtený.

Cohen a H. W. Lenstra, Math. Comp. 42 (1984), 297–330,
na stranách 299–300 popisují zjednodušení a implementaci.
Výslovně odlišují praktický algoritmus od deterministické
verze s dokázaným nejhorším časem. Pro praktickou variantu
není rigorózní analýza automaticky tatáž.

Cohen a A. K. Lenstra, Math. Comp. 48 (1987), 103–121,
uvádějí rutinní rozsah do 213 číslic a konkrétní 247ciferné N
ověřené za méně než 15 minut na CDC 170/750.
Právě u něj ale píší, že použitá tabulka sama nezaručovala
předem úspěch mimo základní rozsah. Takový příklad dokládá
praktickou velikost úloh, nikoli větu o každém N do 250 číslic.

Knižní „up to, say, 250 digits, in a few hours at most“ proto
zůstává dobovým orientačním tvrzením s neověřeným univerzálním
kvantifikátorem; neděláme z něj ani dokázaný worst-case, ani
potvrzenou chybu. Neprováděli jsme měření původního programu
na původním hardwaru.

## 5. Adleman–Huang a pravděpodobnost doby běhu

Oficiální náhled úvodu knihy Lecture Notes in Mathematics 1512
(1992), strany 1–2, obsahuje hlavní větu a přesně rozlišuje
chybu výsledku od neúspěchu pokusu. Pro každé prvočíslo N
uspěje alespoň polovina pomocných náhodných řetězců délky
polynomiální v počtu bitů N; pro složené N nevznikne
falešný důkaz prvočíselnosti.

Kombinací s testem složenosti vznikne pokus s výstupy
„prvočíslo“, „složené“ nebo „nevím“. První dva výstupy jsou
vždy správné, třetí má pravděpodobnost nejvýše 1/2.
Při k nezávislých pokusech je pravděpodobnost dosavadního
neúspěchu nejvýše 2^-k a očekávaný počet pokusů nejvýše 2.
To přímo vysvětluje knižní formulaci o polynomiálním čase
s vysokou pravděpodobností.

Celý důkaz přes abelovské variety z monografie nepřezkoumáváme.
Získaný soubor nazvaný adleman-huang-1992.pdf obsahuje jen
úvodní listy a obsah, nikoli 142 stran knihy. Samostatný
oficiální náhled skutečně obsahuje uvedené věty na stranách 1–2.

## 6. Kontext a hranice tohoto bloku

Původní BLS je dostupný v indexovaném primárním OCR, zejména
strany 623–626, 631–636 a příklady na 645. Pokusy stáhnout
originální PDF z AMS a kopii ze SciSpace skončily HTTP403;
webový index SciSpace text zpřístupnil, místní PDF však nemáme.
Netvrdíme vizuální kontrolu jeho znamének Q. Správnost
našich certifikátů na jejich přepisu nezávisí.

Williams–Judd 1976, 157–172: přečten abstrakt a úvod z kopie
vložené samotným Williamsem. Potvrzuje využití N^2+1 spolu
s N±1. Jejich konferenční abstrakt z října 1975, indexovaný
v Notices AMS z ledna 1976, výslovně uvádí také N^2±N+1.
Celé dva citované články a jejich numerické tabulky zde
nejsou auditovány.

Plný článek Selfridge–Wunderlich 109–120 nebyl získán.
Lenstrův dobový přehled popisuje hranici 35 číslic a 30030
pro rekurzivní postup. Přesné tvrzení o zlomku sekundy
a původní empirický soubor zůstávají otevřené.

Všechny čtyři řady errat a zdrojový TeX byly prohledány podle
stran, autorů, mezí a výrazů. Relevantní známé změny jsou:
394, prime na nonprime (2000); 396, doplnění Selfridgea (2005);
nahrazení celého odstavce APR/Adleman–Huang textem o AKS
(28. dubna 2005). AKS je samostatně auditováno v
[primality-aks.md](primality-aks.md).

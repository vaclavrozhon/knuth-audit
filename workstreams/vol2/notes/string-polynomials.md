# §4.6.1: nekomutativní dělení, úlohy 17–19

Kontrola 4. listopadu 2026, původní sazba 436–438 a 675–677.
Úlohy mají vlastní obecné důkazy a přesnou implementaci, která
kontroluje pořadí každého součinu. Nové C0200 je interpretační
kandidát k nulovým svědkům; C0201 je potvrzený konstantní okraj
požadavku na největší stupeň. Známé opravy jsou od nich odděleny.

## 1. Řetězcové polynomy a stupeň

Pracujeme v Q<A>, tedy s konečnými racionálními lineárními
kombinacemi slov nad abecedou A. Prázdné slovo je jednotka 1;
násobení slov je zřetězení. Součiny ab a ba se obecně liší.
Stupeň nenulového polynomu je největší délka slova v jeho podpoře;
stupeň nuly je -infinity. Homogenní polynom má všechna nenulová
slova stejné délky.

Pro nenulové U,V platí deg(UV)=deg(U)+deg(V). V nejvyšší části
součinu se každé slovo jednoznačně rozřízne po deg(U) písmenech,
takže koeficient zvoleného součinu dvou nejvyšších slov je součin
jejich nenulových koeficientů. V této algebře tedy nejsou dělitelé
nuly a lze krátit nenulové činitele. Pravidla pro stupeň součtu
na 436 jsou přímo důsledkem definice; i uvedený příklad V^2-U
dává aa+bb+1. Známá oprava z roku 2000 mění deg(u) na deg(U).

## 2. Cohnova slabá redukce, 17(a)

Předpokládejme deg(U)>=deg(V) a
deg(Q_1 U-Q_2 V)<deg(Q_1 U). Tato přísná nerovnost sama zaručuje
nenulovost Q_1,U,Q_2,V a rovnost stupňů obou součinů. Zejména
deg(Q_1)<=deg(Q_2). Je-li Q_1 konstantní, podíl Q=Q_2/Q_1
splňuje požadavek, protože racionální koeficienty komutují.

Jinak rozepišme Q_i=r_i+sum_a a Q_(i,a) podle prvního písmene
slov; r_i je konstantní člen a součet je konečný i pro nekonečnou
abecedu. Vyberme a s deg(Q_(1,a))=deg(Q_1)-1. V nejvyšší
homogenní části součinu Q_1 U-Q_2 V musí vymizet všechna slova
začínající a. Konstantní části r_1 U a r_2 V mají menší stupeň.
Po odstranění prvního a tedy

```
deg(Q_(1,a) U-Q_(2,a) V)<deg(Q_(1,a) U).
```

Nahradíme Q_1,Q_2 těmito dvěma zkrácenými polynomy. Stupeň Q_1
klesne o jednu, takže nakonec dosáhneme již vyřešené konstantní
větve. Toto je algoritmus odpovědi, rozšířený na libovolnou abecedu.

## 3. Úplné dělení a homogenní činitele, 17(b),(c)

Pro (b) je potřebná podmínka Q_1!=0. Je-li
deg(Q_1 U-Q_2 V)<deg(V), pak V!=0. Při deg(U)<deg(V) stačí
Q=0,R=U. Jinak použijeme §2. Po libovolném dosavadním dělení
U=QV+R platí přesná identita

```
Q_1 R-(Q_2-Q_1 Q)V=Q_1 U-Q_2 V.
```

Dokud deg(R)>=deg(V), je pravá strana stupně menšího než
deg(Q_1 R); další slabá redukce sníží stupeň R. Celý proces
tedy skončí s deg(R)<deg(V). Máme-li dvě taková dělení, jejich
rozdíl splňuje (Q-Q')V=R'-R. Nenulová levá strana by měla
stupeň alespoň deg(V), pravá menší. Dělení je proto jednoznačné.

V části (c) nejprve předpokládáme nenulové homogenní činitele
U_1 V_1=U_2 V_2 a deg(V_1)>=deg(V_2). Použijeme (b) na V_1,V_2.
Jestliže d=deg(V_1)-deg(V_2), v nejvyšší homogenní části platí
V_1=Q_d V_2: součin QV_2 má právě jednu homogenní část každého
stupně a R nemůže mít stupeň deg(V_1). Po odečtení této identity
jednoznačnost dělení dává Q=Q_d a R=0. Z
U_1 V_1=U_2 V_2 pak krácením V_2 dostáváme U_2=U_1 Q.

**C0200, candidate:** Doslovně napsané předpoklady (b) dovolují
Q_1=Q_2=0, U=a, V=b. Pak jejich nerovnost platí, ale a=Qb+R,
deg(R)<1 nemá řešení. Stupně by nutily Q být konstantní a
koeficient slova a na pravé straně je nula. Část (b) však může
být čtena jako zesílení předpokladů (a), odkud Q_1!=0 již plyne.
Proto tento bod není označen confirmed. Obdobně v (c) volba
U_1=U_2=0,V_1=a,V_2=b selže, pokud nulový polynom považujeme
za homogenní. Zde záleží na konvenci. Bezpečná formulace výslovně
požaduje Q_1!=0 v (b) a nenulový součin v (c).

## 4. Komutující homogenní polynomy, 17(d)

Nechť nejprve U,V jsou nenulové, homogenní, UV=VU a alespoň
jeden z nich má kladný stupeň. Uspořádáme je tak, aby
deg(U)>=deg(V). Pro deg(V)=0 vrátíme W=U. Jinak (c), použité
na VU=UV, dává U=QV s homogenním Q. Z QVV=VQV krácením V
plyne QV=VQ. Nahradíme dvojici (U,V) dvojicí (V,Q) a opět ji
uspořádáme podle stupňů. Součet stupňů se snížil o deg(V)>0.
Algoritmus skončí u dvojice nenulového homogenního W a konstanty.

Zpětným dosazováním U=QV se oba původní polynomy vyjádří
jako rW^m a sW^n s r,s v Q a m,n nezápornými celými čísly.
Stupně se mění pravidlem (a,b)->(b,a-b), takže konečný kladný
stupeň W je gcd(deg(U),deg(V)). Žádné jiné řešení nemůže mít
větší stupeň: jeho kladný stupeň by musel dělit oba počáteční.
Je-li právě jeden vstup nulový a druhý nekonstantní, lze vzít
W rovný nenulovému vstupu a u nuly použít nulový racionální násobek.

**C0201, confirmed:** Pro U=V=1 může být W=a^k pro libovolné
k>=1, s r=s=1 a m=n=0. Žádný největší stupeň W proto neexistuje.
Konstanty jsou nenulové homogenní polynomy, takže nejde o spor
o definici homogenní nuly. Nulové exponenty jsou přípustné a
jsou potřebné i pro vytištěnou větev s právě jedním konstantním
vstupem. Oprava: požadavek největšího stupně omezit na případ,
kdy alespoň jeden vstup je nekonstantní; dvě konstanty ošetřit
zvlášť libovolnou dohodnutou volbou W. Zde není zpochybněna
existence společného základu, pouze požadované maximum.

## 5. Rozšířený algoritmus, úloha 18

Máme V_1,V_2 ne oba nulové a U_1,U_2 ne oba nulové takové, že
U_1 V_1=U_2 V_2. Pravý společný dělitel D znamená rozklady
V_i=P_i D. Největší pravý společný dělitel (gcrd) je takový,
že každý jiný pravý společný dělitel dělí zprava také D.
Analogicky nejmenší levý společný násobek L (lclm) má splňovat,
že každý levý společný násobek má tvar cL. Výsledky určujeme
až na vhodný nenulový konstantní násobek.

Opravený algoritmus S z odpovědi (původně C, přejmenováno 2010)
má dvě pomocné matice řetězcových polynomů

```
W=[w_1 w'_1; w_2 w'_2],  Z=[z_1 z_2; z'_1 z'_2],
J=[1 0;0 -1].
```

Na začátku W=Z=I. Píšeme u=(u_1,u_2), v=(v_1,v_2)^T,
U=(U_1,U_2), V=(V_1,V_2)^T. Všech osm vytištěných invariantů
je obsaženo ve třech maticových rovnostech

```
u=UW,  v=ZV,  WJZ=(-1)^n J.
```

Při dělení v_1=Qv_2+R se současně použijí matice

```
A=[0 1;1 -Q],  B=[-Q 1;1 0],
Z_new=AZ, W_new=WB, v_new=Av, u_new=uB.
```

Přímé násobení dává BJA=-J. Tři rovnosti, a tedy všech osm
skalárních invariantů, se tím zachovají se změněným znaménkem.
Zvlášť uJv=0, tedy u_1v_1=u_2v_2, přetrvává. Matice A,B
jsou invertibilní i nad nekomutativní algebrou, proto u ani v
nemohou být nulové dvojice. Z rovnosti součinů a absence dělitelů
nuly potom plyne u_1=0 právě tehdy, když v_2=0. Dokud v_2!=0,
existuje potřebné dělení podle §3 a deg(v_2) přísně klesá.

Na konci v=(D,0)^T, D!=0. Rovnost v=ZV dává Bézoutův vztah
D=z_1V_1+z_2V_2 a rovnost V=Z^(-1)(D,0)^T dává, že D je
pravý společný dělitel. Každý jiný pravý společný dělitel dělí
uvedenou Bézoutovu kombinaci, tedy D.

Položme L=z'_1V_1=-z'_2V_2. Pro libovolný společný násobek
M=A_1V_1=A_2V_2 je řádek t=(A_1,-A_2) v levém jádře V.
Řádek t Z^(-1) pak anuluje (D,0)^T. Jeho první složka musí
být nula, takže t=c(z'_1,z'_2) a M=cL. Tím je obecně dokázána
nejmenší vlastnost L, včetně případu právě jednoho nulového V_i,
kdy L=0. Toto zdůvodnění nevyžaduje výměnu vstupního svědka U.

Stejný argument z u=(0,u_2)=UW, nebo prostá výměna pravé a levé
strany, dokazuje duální závěr: u_2 je gcld(U_1,U_2) a
U_1w_1=-U_2w_2 je lcrm(U_1,U_2). Nulové vstupy jsou zahrnuty.

Původní příklad se čtyřmi polynomy na 437 dává přesně vytištěný
součin se 17 členy a D=ab+1. Konkrétní běh vrátí L se záporným
znaménkem vůči vytištěnému součinu, což je ekvivalentní lclm.
Šest matic na 676 je součin tří matic [a,1;1,0] a jejich inverzí
v obráceném pořadí. Jeho výsledek I i uvedená nekomutativní
identita (abc+a+c)(1+ba)=(ab+1)(cba+a+c) jsou správné.

## 6. Celočíselné matice, úloha 19

Pro n x n celočíselné matice A,B vytvoříme C=[A;B], tedy
matici s 2n řádky. Stačí nalézt celočíselné D,R,Z s C=RD,D=ZC.
Rozdělením R na dva bloky P,Q a Z na dva bloky X,Y získáme
A=PD,B=QD,D=XA+YB. Pro libovolný společný pravý maticový
dělitel E, A=A'E,B=B'E, pak D=(XA'+YB')E. Žádná invertibilita
A,B,D ani E není potřebná; důkaz platí i pro nulové matice.

Algoritmus T provádí celočíselné řádkové operace na obecné m x n
matici C a souběžně udržuje T=VC, UV=I. Výměna řádků j,k
v T,V znamená výměnu sloupců j,k v U. Odečtení q-násobku řádku j
od řádku i v T,V odpovídá přičtení q-násobku sloupce i ke sloupci
j v U. Jde o násobení navzájem inverzními elementárními maticemi.

Při zpracování sloupce j zvolíme nenulový pivot mezi řádky j,...,m
a přeneseme jej na j. Dolní řádky redukujeme podílem
q=floor(T_ij/T_jj). Zbytky mají absolutní hodnotu menší než
|T_jj| i pro záporný pivot. Pokud ještě zbývá nenulový dolní
prvek, další nejmenší nenulový pivot má menší absolutní hodnotu.
Celý vnitřní cyklus skončí. Je-li sloupec dole nulový, žádné
dělení se neprovádí, ani když je T_jj=0. Dříve vytvořené nuly
se zachovají, protože dotčené řádky mají v předchozích sloupcích nuly.

Pro m=2n jsou poslední n řádky hotového T nulové. Nechť D je
prvních n řádků T, Z prvních n řádků V a R prvních n sloupců U.
Pak D=ZC a C=UT=RD. Tím je algoritmus i požadovaný gcrd dokázán.

Pro vytištěný příklad platí přesně

```
A=[1 2;3 4], B=[4 3;2 1], D=[1 2;0 -1],
P=[1 0;3 2], Q=[4 5;2 3],
X=[1 0;2 -2], Y=[0 0;1 0].
```

Součiny A=PD,B=QD a součet D=XA+YB souhlasí. Jelikož D má
determinant -1, společný pravý dělitel všech těchto vstupů je
jednotka; i závěrečná poznámka o libovolné unimodulární matici
(celočíselné matici s determinantem +1 nebo -1) je správná.

## 7. Výpočty a známé opravy

`verify_string_polynomials.py` používá přesné zlomky a slovníky
slov. Dělení pomocí ořezávání prvních písmen je porovnáno s
nezávislým výpočtem nejvyšších koeficientů podle posledních písmen.
Testy zahrnují 160 dělení, 80 homogenních faktorizací, 80 dvojic
komutujících mocnin, 90 zpětně sestavených Eukleidových řetězců,
vytištěný příklad a dva nulové vstupy. Celkem bylo ověřeno všech
osm invariantů v 332 stavech, z toho 239 skutečných iterací.
Zpětné řetězce se konstruují součinem matic nezávisle od S.

Dalších 240 dvojic celočíselných matic velikostí 1 až 5 kontroluje
přímo certifikáty C=RD,D=ZC. Zahrnuty jsou nulové matice, nulové
sloupce i záporné pivoty; 49 výsledků D má zcela nulový řádek.
Celkem 1517 řádkových průchodů. Správnost univerzální vlastnosti
plyne již z přesně kontrolovaných certifikátů, ne ze shody dvou
podobných redukčních algoritmů.

Čtyři bloky v `results/string-polynomials.json` prošly za celkem
2.963022 s; PID 1325894, session 56816, limit 180 s, exit 0.
Nebyl opakován žádný úspěšný blok. C0200 a C0201 mají vlastní
krátké důkazy; konečné testy nejsou důkazem neomezenosti v C0201.

Všechny vrstvy errat jsou v `sources/string-polynomials-errata.txt`.
Známé opravy: deg(u)->deg(U) v 17 (2000), u_1v_1=u_2v_2 v S2
(2000), C1–C4->S1–S4 (2010), UV=I a index v T3 (2001/2002).
Původní stránka 42 all2-prepre byla zobrazena. Pro jednoznačnost
náš algoritmus T výslovně vybírá pivot z řádků j,...,m; volný
index i v zápisu původní množiny ani jeho změnu z roku 2002
nevydáváme za nový matematický protipříklad. Pro C0200/201 nebyla
odpovídající oprava nalezena. Aktuální fyzický dotisk a prvenství
nejsou ověřeny; hlášení se neodesílá.

## 8. Prameny a rozsah externí kontroly

[Cohn 1963, původní článek](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/cohnweak.pdf):
vizuálně čteny 332–334,339–342 a bibliografie na 356. Zejména
§4 obsahuje oboustranné dělení a Theorem 4.1 včetně důkazu
principálnosti součtu a průniku. Bibliografie přímo potvrzuje
Cohnovu práci z roku 1961, 57,18–30. Její
[vydavatelský výtah](https://doi.org/10.1017/S0305004100034812)
a metadata byly dostupné, celý PDF obsah nikoli. Celý obecnější
Cohnův článek 1963 nebyl znovu dokazován; speciální případ potřebný
pro úlohy má úplný vlastní důkaz výše.

Bergmanův obecný výsledek o komutujících nehomogenních prvcích
zůstává externí větou z literatury: centralizátor, množina všech
prvků komutujících s pevným nekonstantním prvkem, je polynomiální
algebra v jedné proměnné. Jeho
[vlastní bibliografie](https://math.berkeley.edu/~gbergman/papers/)
a vydavatelská metadata potvrzují článek v Trans. AMS137(1969),327–344.
Původní dizertace 1967 ani plný článek (AMS vrací403) nebyly přečteny;
to není zaměněno za vlastní důkaz tohoto výrazně silnějšího výsledku.
Pro homogenní úlohu 17(d) se tato externí věta nepoužívá.

[Cahen 1914, původní svazek](https://archive.org/details/thoriedesnombr01caheuoft):
vizuálně čten titul (PDF 11) a strany 336–338 (PDF 356–358).
Titul potvrzuje rok 1914 a Tome premier, Le premier degré. §376
definuje největšího společného maticového dělitele univerzální
vlastností a konstruuje jej z vodorovně spojených matic redukcí
na kanonický tvar. Po transpozici jde o konstrukci z §6 výše.
Sken je velmi vybledlý; pro čtení byla navíc použita dočasná
kontrastní kopie. Uložené obrázky zachovávají původní vykreslení.
Kontrola zahrnuje definici a obecnou konstrukci, nikoli úplný
přepis všech špatně čitelných položek číselného příkladu.

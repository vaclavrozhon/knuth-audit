# Rychlý resultant a kompaktní Sturmovy posloupnosti

Kontrola 4. listopadu 2026: dovětek odpovědi §4.6.1–12 na tištěné
straně 674. Závěr: mez O(n log² n) má správnou realizaci v modelu
přesné reálné/komplexní aritmetiky, s kompaktním výstupem.
Nevzniká nový nález. Poloviční Eukleidův algoritmus používá jen
horní části vstupů k nalezení části podílů; jeho specifikace je v §2
a důkaz v §3. Resultant a Sturmovy údaje získáme podle §§5–6.

**Rozsah pramenů.** Schwartzův článek JACM 27 (1980), 701–717,
má ověřenou bibliografii, ale jeho originální PDF nebylo získáno.
Veřejný přepis není autoritativní doklad sazby. Nepřipisujeme proto
tomuto článku podrobnosti níže uvedeného algoritmu ani nepředstíráme
kontrolu všech jeho důkazů. Matematické existenční tvrzení knihy
ověřujeme vlastním úplným rozpisem standardní konstrukce, porovnaným
s primárním Yapovým textem z roku 1999, tištěné strany 58–62.
Přečtena i jeho titulní 43 a van der Hoevenův autorský článek z roku
2022, vybrané strany 1,6–7,15–17. Jeho optimalizované konstanty ani
všechny pomocné algoritmy zde neauditujeme. Moderní dokumentace FLINT
posloužila jako další navigace; sama upozorňuje na části vytvořené
LLM a samotný její text zde není důkazem.

## 1. Podíly jako přesný stručný zápis

Nechť K je těleso a a,b jsou polynomy nad K, zpočátku
n=deg(a)>deg(b). Stupeň nuly značíme -infinity. Označme r_0=a,
r_1=b a zapisujme běžné eukleidovské dělení jako

    r_(i-1) = q_i r_i + r_(i+1),       deg(r_(i+1)) < deg(r_i).

Poslední nenulový zbytek je g=r_t a r_(t+1)=0. Seznam podílů
obsahuje i q_t z posledního přesného dělení. Pro d_i=deg(r_i)
platí deg(q_i)=d_(i-1)-d_i>=1, takže

    sum_i deg(q_i) = n-deg(g),
    sum_i (deg(q_i)+1) + deg(g)+1 <= 2n-deg(g)+1.

Podíly a g tedy mají dohromady O(n) koeficientů. Přesně určují celou
posloupnost: začneme dvojicí (g,0) a postupujeme pozpátku rovnicemi
r_(i-1)=q_i r_i+r_(i+1). Toto je kompaktní reprezentace; její
rozvinutí do všech koeficientů může zabrat kvadratickou práci.

Při deg(a)=deg(b) provedeme nejprve jedno dělení s konstantním
podílem. Při deg(a)<deg(b) vstupy prohodíme; u resultantu zároveň
použijeme znaménko (-1)^(deg(a)deg(b)). Nulové vstupy a konstanty
vyřídíme samostatně. Dále jsou počáteční stupně přísně klesající.

Definujme matice

    Q(q) = [[q,1],[1,0]],
    M_j = Q(q_1) ... Q(q_j),
    (a,b)^T = M_j (r_j,r_(j+1))^T.

Determinant M_j je (-1)^j. Inverze je tedy podepsaná adjungovaná
matice, bez polynomiálního jmenovatele. Stupně jejích prvků,
stejně jako prvků M_j, jsou nejvýše
sum_(i<=j) deg(q_i)=n-deg(r_j).

Platí i obrácený směr: jestliže součin Q(q_1)...Q(q_j) s deg(q_i)>=1
převádí (A,B), deg(A)>deg(B), na (a,b), pak jde o počáteční
eukleidovské podíly a zbytky. Důkaz jde odzadu: z (u,v) vznikne
(qu+v,u), kde deg(qu+v)=deg(q)+deg(u)>deg(u). V každém kroku je
v jednoznačným zbytkem při dělení qu+v polynomem u.

## 2. Lemma o odříznutí nízkých koeficientů

Poloviční algoritmus H(a,b) má vrátit M_j, příslušné podíly a dvojici
(A,B)=(r_j,r_(j+1)) tak, aby

    deg(A) >= ceil(n/2) > deg(B).                         (1)

Položme a=x^s a_1+a_0, b=x^s b_1+b_0, kde deg(a_0),deg(b_0)<s,
a n'=deg(a_1). Předpokládejme, že H(a_1,b_1) vrátí M,A_1,B_1.
Pak pro (A,B)^T=M^(-1)(a,b)^T platí

    (A,B)^T = x^s(A_1,B_1)^T + M^(-1)(a_0,b_0)^T,
    deg(A) = s+deg(A_1),
    deg(B) < s+ceil(n'/2).                              (2)

Důkaz: prvky M^(-1) mají stupeň nejvýše n'-deg(A_1).
Každá souřadnice opravného členu má tedy stupeň ostře menší než
s+n'-deg(A_1). Protože deg(A_1)>=ceil(n'/2), tato mez je nejvýše
s+floor(n'/2) a zároveň nejvýše s+deg(A_1). Vedoucí člen A
se nezmění. U B je jak x^s B_1, tak opravný člen stupně menšího
než s+ceil(n'/2). Dostáváme i deg(A)>deg(B), takže obrácený směr
z §1 potvrzuje správnost převzatých podílů.

**Poslední B_1 nemusí mít správný stupeň ani vedoucí koeficient
po pouhém posunu.** Nízké části mohou skutečné B změnit.
Proto po rekurzi obnovujeme skutečnou dvojici maticovým násobením;
netvoříme další podíl z neopraveného B_1.

## 3. Algoritmus pro libovolné poklesy stupně

Pro n=deg(a)>deg(b) a m=ceil(n/2):

    1. Je-li deg(b)<m, vrať I, prázdný seznam, (a,b).
    2. Spočti R = H(a div x^m, b div x^m).
       Obnov (A,B)^T = R^(-1)(a,b)^T.
    3. Je-li deg(B)<m, vrať R a jeho podíly, (A,B).
    4. Proveď A=qB+D, deg(D)<deg(B).
       Polož l=deg(B), k=2m-l.
    5. Spočti S = H(B div x^k, D div x^k).
       Obnov (C,E)^T = S^(-1)(B,D)^T.
    6. Vrať R Q(q) S, podíly R, potom q a podíly S, (C,E).

Zápis div x^s znamená odstranění s nejnižších koeficientů, nikoli
test dělitelnosti. H je definováno i pro nenulovou konstantu a a b=0:
krok 1 skončí s m=0. Tím jsou pokryty krajní rekurzivní vstupy.

V kroku 2 má první vstup stupeň n'=floor(n/2). Z (2) plyne
deg(A)>=m+ceil(n'/2) a deg(B)<m+ceil(n'/2). Pokud krok 3 skončí,
platí (1). Jinak m<=l<m+ceil(n'/2), takže 0<=k<=l a

    deg(B div x^k) = l-k = 2(l-m) < n'.                 (3)

Práh druhého volání je l-m. Po obnovení podle (2) máme
deg(C)>=k+(l-m)=m a deg(E)<k+(l-m)=m. Pořadí podílů je správné
podle §1. To dokazuje indukci i ukončení algoritmu. Volba k=2m-l
je podstatná; předpoklad poklesu stupně vždy právě o jedna
nebyl použit.

## 4. Cena výpočtu

Označme M(n) cenu násobení polynomů stupně nejvýše n. U obvyklých
metod lze volit neklesající M(n)/n a M(2n)=O(M(n)).
Sčítání stojí O(n). Dělení stojí O(M(n)): obrátíme pořadí
koeficientů dělitele, invertujeme jeho nenulový konstantní člen
a potřebnou část převrácené řady zdvojujeme Newtonovým krokem
h <- h(2-fh). Je-li fh=1 mod x^k, pak 1-fh_new=(1-fh)^2,
tedy chyba je nulová mod x^(2k). Součet nákladů pro geometricky
rostoucí přesnosti je O(M(n)). Podíl určí násobení obráceného
dělence touto řadou a zbytek jedno další násobení.

H má dvě rekurze na stupních nejvýše floor(n/2), podle (3),
a konstantní počet násobení/dělení velikosti O(n). Proto

    T(n) <= 2T(floor(n/2)) + O(M(n)) = O(M(n) log n).

Podíly lze spojovat jako seznamy. Jejich případné kopírování na
O(log n) úrovních stojí O(n log n), zahrnuté v uvedené mezi.
Všechny zbytkové polynomy se přitom nevytvářejí.

Pro úplnou posloupnost použijeme H, pak jedno další dělení
obnovené dvojice (A,B), a pokračujeme na (B,A mod B). Nový první
stupeň je <ceil(n/2). Součet nákladů na geometricky klesajících
vstupech zůstává O(M(n) log n).

V přesném aritmetickém modelu nad komplexními čísly s dostupnými
kořeny jednotky dává rychlá Fourierova transformace M(n)=O(n log n).
Komplexní operaci lze simulovat konstantním počtem reálných operací.
Dostáváme O(n log² n). To není bitová složitost velkých racionálních
čitatelů a jmenovatelů ani tvrzení o numerické stabilitě.
Nad obecným tělesem jsme odvodili O(M(n) log n); dosazení FFT ceny
vyžaduje odpovídající aritmetický model.

## 5. Stupně, vedoucí koeficienty a resultant

Označme lc(f) vedoucí koeficient nenulového f. Z podílů získáme
d_i a c_i=lc(r_i) pomocí

    d_i = d_(i-1)-deg(q_i),
    c_i = c_(i-1)/lc(q_i).                              (4)

To stojí O(n) operací bez znalosti všech mezilehlých zbytků.
Je-li deg(g)>0, resultant je nula. Je-li g nenulová konstanta,

    Res(a,b) = c_t^d_(t-1)
               product_(i=1,...,t-1)
               [(-1)^(d_(i-1)d_i) c_i^(d_(i-1)-d_(i+1))].       (5)

Vzorec plyne z hodnot polynomů v kořenech dělitele: pro A=qB+D,
D nenulové, máme

    Res(A,B) = (-1)^(deg(A)deg(B))
               lc(B)^(deg(A)-deg(D)) Res(B,D).

Konec je Res(A,c)=c^deg(A) pro nenulovou konstantu c. Součet
nezáporných exponentů v (5) je d_0+d_1, protože d_t=0; i prosté
opakované násobení proto přidá jen O(n) operací. Rychlý resultant
je tím doložen i při chybějících stupních a nekonstantním gcd.

## 6. Sturmovy údaje a vyhodnocení v bodech

Pro reálný nekonstantní P použijeme a=P, b=P', kde P' je derivace.
Běžné zbytky převedeme na záporné Sturmovy zbytky předpisem

    s_i = epsilon_i r_i,
    epsilon_0=epsilon_1=1, epsilon_(i+1)=-epsilon_(i-1).

Znaménka epsilon jsou 1,1,-1,-1,1,1,... . Zbytek po dělení
epsilon_(i-1)r_(i-1) polynomem epsilon_i r_i je
epsilon_(i-1)r_(i+1); jeho negace dává uvedenou rekurzi.
Podíly, g a tento předpis tedy určují přesnou Sturmovu posloupnost.

Na +infinity má s_i znaménko epsilon_i c_i, na -infinity navíc
faktor (-1)^d_i. Počet změn znamének s vynecháním nul získáme
v O(n) operacích z (4). Rozdíl počtu změn na levém a pravém
konci dává počet kořenů podle již dokázané Sturmovy věty.

Pro konečný bod z vyhodnotíme všechny q_i(z) a g(z) Hornerovým
schématem, poté zpětně hodnoty r_i(z) stejně jako v §1. Celková
cena je O(sum deg(q_i)+deg(g)+t)=O(n). Funguje to i při nulovém
mezilehlém zbytku v bodě z: zpětný výpočet nedělí jeho hodnotou.
Krajní kořeny P se ošetří konvencí intervalů ze
[sturm-cf.md](sturm-cf.md), nikoli novou domněnkou o znaménkách.

Celá znaménková posloupnost v zadaném bodě je tedy dostupná
z lineárně velkého zápisu. Doslovné vypsání všech koeficientů
všech s_i tento algoritmus neslibuje. Kniha detail reprezentace
neuvádí; bez doložení silnějšího významu slova „evaluate“ to
nepovažujeme za chybu.

## 7. Přesné kontroly a závěr pro pokrytí

Program verify_fast_sturm.py používá přesné zlomky nebo konečná
tělesa. Násobí školsky; jeho běh není měřením FFT složitosti.
Každé rekurzivní volání kontroluje maticovou identitu, práh stupňů
a mez stupňů matice. Úplné podíly srovnává se samostatným dělením
v SymPy; každý vstup navíc rekonstruuje z podílů a g. Resultant
porovnává s původním Sylvesterovým determinantem.

Úspěšné bloky byly uloženy odděleně a neopakovaly se:

- 916 dvojic nad F_2,F_3,F_5,F_101; 4278 rekurzivních certifikátů,
  1003 podílů stupně >1 a 460 Sylvesterových determinantů.
- 30 racionálních dvojic včetně konstant, nuly, stejných počátečních
  stupňů a společných faktorů; dalších 111 certifikátů a 28 determinantů.
- 70 polynomů se známými reálnými kořeny, i násobnými, a přidanými
  faktory bez reálných kořenů; 1420 shod všech hodnot se samostatnou
  znaménkovou rekurzí a 13766 kontrol intervalů.
- Náhodný Sturmův blok neměl větší poklesy stupně. Následoval proto
  nový cílený blok, bez opakování předchozích: x^n-1, x^n+1, x^n-x
  a (x^n-1)^2, včetně n=31,32,63,64. Celkem 76 polynomů,
  71 podílů stupně >1, 6441 intervalů; ověřena i ±infinity.

Čtyři bloky prošly; časy a PID jsou v results/fast-sturm.json
a RUN_STATE.json. Součet vlastních měřených časů je 2.631267 s.
Testy nenahrazují obecný důkaz; ten poskytují §§1–6.
Všech šest vrstev errat bylo prohledáno, viz
sources/fast-sturm-errata.txt; oprava tohoto dovětku nenalezena.
Dosavadní potvrzené nálezy a kandidáti se nemění.

Tím se uzavírá poslední otevřený matematický dovětek §4.6.1.
Nedostupný Schwartzův originál zůstává výslovným limitem
bibliografického průzkumu, nikoli neprokázanou matematickou
závislostí tohoto ověření. Celý svazek tím dokončen není.
Žádné hlášení nebylo odesláno; fyzický nejnovější dotisk neověřen.

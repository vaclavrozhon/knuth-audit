# Úloha55: obecné meze a všechny tištěné mezikroky

Zadání p118/file133 a úplná odpověď p170/file185 byly zobrazeny.
Použita oprava z20.8.2026 v primárním `err4f7-2026-11-06.textxt`:
první věta(c) má „M or XMX“ a v posledních třech řádcích je
všech pět n nahrazeno q. Obě změny jsou známá errata, nikoli
naše nálezy. Připsání řešení D. M. Kaneovi se zde dále
bibliograficky neověřuje. Každý matematický krok je níže
odvozen samostatně.

## E55-0 — obor a Fibonacciho/Lucasovy identity

Obvod složený pouze z V junctions je jednoduchý geometrický
cyklus: každý bod má právě dvě incidentní čáry, takže žádná
další větev ani most nejsou možné. Přímé čáry mezi odlišnými
body nedovolují jednochodý ani dvouchodý cyklus, tedy q≥3.
Následující maticové důkazy ve skutečnosti platí i pro všechny
abstraktní řetězce V/Λ příslušných délek, a nevyžadují, aby
každý takový řetězec šel geometricky realizovat.

Definujeme F0=0,F1=1 a L0=2,L1=1 se stejnou rekurencí
u_(k+2)=u_(k+1)+u_k. Pro φ=(1+√5)/2, ψ=(1−√5)/2=−1/φ
platí φ²=φ+1 a ψ²=ψ+1. Z těchto rovnic a počátečních hodnot
indukcí plynou F_k=(φ^k−ψ^k)/√5 a L_k=φ^k+ψ^k.
Rozšíření rekurence dozadu dává F_(−k)=(−1)^(k+1)F_k
a L_(−k)=(−1)^kL_k; zvláště F_(−1)=1. Tím jsou určeny
i záporné indexy, které se v tištěných vzorcích objeví
pro p=0 či p=q. Z definic také L_q=F_(q+1)+F_(q−1).

## E55-a — obě invariantní části a každá tištěná rovnost

Pořadí čtyř stavů je >,<,−,+. Pišme I pro jednotkovou2×2
matici a J pro matici, která dva stavy prohazuje. Z již
odvozených položek50 máme

    V = [ I I ; I 0 ],    Λ = [ I J ; J 0 ],    J²=I.

Každý2×2 blok součinu P má tvar uI+vJ, protože takové bloky
jsou uzavřeny na sčítání i násobení. To je přesný indukční
invariant: P_ij=P_(i xor1,j xor1) pro každé i,j. Dosazení
J→1 a J→−1 jsou homomorfismy, neboť obě hodnoty splňují
J²=1. Kladné dosazení dá pro V iΛ matici A; záporné dá
pro V matici A a proΛ matici B. Proto pro každý blok r,s

    P_(2r,2s)+P_(2r,2s+1) = (A^q)_(r,s),
    P_(2r,2s)−P_(2r,2s+1) = M_(r,s).

Indukce násobením A dává
A^q=[[F_(q+1),F_q],[F_q,F_(q−1)]]. To dokazuje jednotlivě
všechny vytištěné součty: P00+P01=F_(q+1),
P02+P03=P20+P21=F_q a P22+P23=F_(q−1), stejně jako
všechny čtyři vytištěné rozdíly pro M.

P11=P00 a P33=P22, tedy traceP=2P00+2P22. Přesně podle
dalšího tištěného mezikroku

    traceM = P00−P01+P22−P23
           = P00−(F_(q+1)−P00)+P22−(F_(q−1)−P22)
           = traceP−L_q.

Indukční význam součinu50 je zde bez dalších předpokladových
mezer: každá čára jednoduchého cyklu má jeden stav a každá
V/Λ přípustná dvojice má násobnost1. Stopa tedy počítá
každý labeling jednou a výsledný počet je traceM+L_q.

## E55-b1 — všechny uzavřené tvary, včetně nulových exponentů

Označme X=diag(1,−1). B=XAX a X²=I; pro každý b≥0 proto
B^b=XA^bX. Z předchozí indukce dostaneme přesně obě tištěné
matice A^a a B^b. Pro a=0 či b=0 díky F_(−1)=1 dávají I.
Přímé vynásobení jejich čtyř položek dává

    A^a B^b = [ Δ_(a,b),       −Δ_(a,b−1) ;
                Δ_(a−1,b),     −Δ_(a−1,b−1) ],
    Δ_(a,b)=F_(a+1)F_(b+1)−F_aF_b.

Pro úplnost vložme Binetovy vzorce. Po odečtení se členy
φ^(a+b+2)−φ^(a+b) a jejich ψ protějšek změní v
L_(a+b+1), zatímco smíšené členy jsou dvakrát
φ^aψ^b+ψ^aφ^b= (−1)^bL_(a−b). Tedy přesně

    Δ_(a,b)=[L_(a+b+1)+2(−1)^bL_(a−b)]/5.

Odečtení stejného vzorce s a−1,b−1 využije
L_(s+1)−L_(s−1)=L_s a opačné znaménko(−1)^(b−1):

    trace(A^aB^b)=Δ_(a,b)−Δ_(a−1,b−1)
                 =[L_(a+b)+4(−1)^bL_(a−b)]/5.

Odvození platí i pro potřebné indexy−1 a neopomíjí krajní
případy identity či čisté mocniny.

## E55-b2 — pořadí všech hodnot a přesná rovnost v mezích

Pro t_p=trace(A^pB^(q−p)) dává poslední vzorec symetrii
t_p=t_(q−p). Pro 0≤p≤floor(q/2) jej lze psát jako

    t_p=[L_q+4(−1)^pL_(q−2p)]/5.

Lucasova čísla stejné parity jsou přísně rostoucí pro
nezáporné indexy: sudá začínají2,3 a lichá1,4; další krok
o2 je u_(k+2)=u_(k+1)+u_k>u_k. Proto liché p v tomto
polovičním intervalu dávají přísně rostoucí záporné odchylky
od L_q/5, kdežto sudé p dávají přísně klesající kladné
odchylky. Všechna lichá ramena tedy leží pod všemi sudými;
lichá p se čtou vzestupně, sudá sestupně, a zbytek určuje
symetrie p↔q−p. To je přesný význam tištěného pořadí
se dvěma prostředními symetrickými indexy. U malých q se
prázdná ramena ellipsy vypustí; nepřidávají se indexy
mimo polovinu intervalu.

Minimum nastane právě při p∈{1,q−1}. Dosazením nebo
Fibonacciho rekurencí 3L_q−2L_(q−2)=5F_q dostáváme
t_1+L_q=2F_q. Maximum nastane právě pro p∈{0,q}, kdy
t_p=L_q a výsledný počet je2L_q. Všechny ostatní hodnoty
jsou přísně uvnitř, s již uvedenou symetrií. Platí i q=3:
vnitřní p jsou právě1,2 a obě dávají minimum.

## E55-c1 — horní mez pro libovolné slovo a počet přepnutí

Po položkách |A|=|B|=A. Trojúhelníková nerovnost pro každý
prvek maticového násobení proto indukcí dává |M|≤A^q
po položkách. Zvláště traceM≤traceA^q=L_q, a tedy počet
labelingů≤2L_q. Tím se uzavírá i horní mez, na niž se
zbývající tištěný důkaz již nezaměřuje.

Počet m přepnutí V↔Λ na cyklu je sudý. V případě m=0
jde o čistou mocninu, v případě m=2 o A^aB^b až na
cyklický posun či záměnu A↔B; obě situace uzavírá(b).
V ostatních případech nahradíme každý B za XAX a sousední
X zrušíme. Přesně m X zůstává mezi běhy A. Je-li na
zvoleném začátku běh B, je třeba vzít XMX; to je právě
známá oprava a zachovává stopu i determinant.

Po vhodném cyklickém posunu má reprezentant stejné stopy tvar

    M=(AXA)A^p1 (AXA)A^p2 … (AXA)A^pm,   p_k≥−1.

Každý p_k+2 je délka odpovídajícího neprázdného běhu A
mezi X; proto q=Σ(p_k+2). Záporný exponent−1 je zde jen
zápis překrývajících se sousedních A, nikoli záporný počet
původních písmen. Cyklické posuny součinů invertibilních
matic zachovávají stopu i determinant (a jsou podobností).

Pro C=AXA=[[0,1],[1,1]] jsou C a A po položkách nezáporné.
Pokud jsou všechna p_k≥0, je i celý M nezáporný a traceM≥0.
To splňuje požadovanou dolní mez, protože
2F_q−L_q=−F_(q−3)≤0 pro q≥3.

## E55-c2 — každá rovnost v redukci a její ukončení

**Rozlišení výsledku a sazby:** závěrečný tištěný člen této
redukce má `B^(p3+1)`. Následující vlastní odvození dává
`B^(p3+3)`. Původní rovnost proto nezavíráme jako správnou;
jde o candidate/low C0009 s přesným rozporem stop−5 versus0
a úplnou kontrolou errat v `notes/F7-C0009.md`. Opravená
redukce a celá závěrečná mez mají níže nezávislý důkaz.

Máme-li dva sousední p=−1, posuneme je do p1=pm=−1.
Přepsání XAX=B pak dává právě tištěné střídavé slovo

    A B A^(p2+2) B^(p3+2) … B^(p_(m−1)+2).

Všechny zobrazené exponenty jsou kladné. Přímé násobení
dává ABA=BAB=diag(−1,1). Pišme počátek jako ABA^rB^sR,
kde r=p2+2≥1,s=p3+2≥1; pro m=4 je R prázdné, jinak
začíná A a končí kladnou mocninou B. První tištěný krok je

    trace(ABA^rB^sR)=trace(BABA^(r−1)B^sR)
                   =trace(ABA^(r−1)B^sRB).

První rovnost nahrazuje ABA, druhá přesouvá první B na
konec. To je přesně snížení exponentu p2+2 o1 a zvýšení
posledního exponentu o1, jak uvádí sazba. Opakujeme r-krát:

    trace(ABA^rB^sR)=trace(AB^(s+1)RB^r).

Pro m≥6 se poslední exponent zvětší o r, tedy na
p_(m−1)+p2+4; první exponent B je p3+3 a počet běhů
klesne o2. Pro m=4 se obě koncové mocniny B sloučí:
výsledek je AB^(s+r+1), také s2běhy. Tento malý konec
ellipsis je třeba sloučit, ne počítat dvakrát. Celkový
počet q písmen se nezmění a všechny nové běhy jsou kladné.

Každá vnější redukce sníží nezáporné celé m o2; vnitřní
posouvání spotřebuje kladné r≤q. Postup tedy skončí.
Nakonec jsme buď v m=0,2, nebo se všemi p≥0, již hotovo;
jinak je alespoň jedno p=−1, ale žádná dvě nejsou sousední
ani přes cyklický spoj. Tím je oprávněno přesně tištěné
„therefore we can assume“, včetně jeho krajních případů.

## E55-c3 — všechny tři normy a přesný ušetřený exponent

Používáme eukleidovskou operátorovou normu. Symetrické A
i C mají vlastní čísla φ a−1/φ, takže ||A||=||C||=φ.
Přímé násobení D=AXAXA=diag(−1,1)=−X dává ||D||=1.

Nechť r≥1 exponentů p je−1 a P je součet nezáporných
exponentů. Protože záporné exponenty nesousedí, každý
z nich spáruje dvě různé kopie C do
CA^(−1)C=AXAXA=D; žádná kopie C není spárována dvakrát.
Po případném cyklickém posunu zbývá m−2r samostatných C,
r kopií D a P obyčejných A. Submultiplikativita normy dává

    ||M||≤φ^(m−2r+P)=φ^(q−m−r),   q=2m−r+P.

Úspora proti φ^q je m+r: po jednom faktoruφ pro každé
p≥0 a po dvou pro každé p=−1, přesně jak uvádí závorka
v sazbě. Pro m≥4 a r≥1 je m+r≥5, tedy ||M||≤φ^(q−5).
Norma je použita na reprezentanta téže stopy a determinantu;
nikde se netvrdí, že obecný cyklický posun sám zachovává normu.

## E55-c4 — vlastní čísla, poslední Fibonacciho nerovnost a malé q

Každý původní A iB má determinant−1, tedy detM=(−1)^q.
Pro vlastní čísla λ,λ̂ s |λ|≥|λ̂| proto |λ|≥1 a
|λ̂|=1/|λ|. I pro komplexní vlastní čísla platí
|λ|≤||M||: rozšíření reálné normy na komplexní vektor
plyne součtem čtvercových odhadů pro reálnou a imaginární
část. Trojúhelníková nerovnost a monotonie x+1/x pro x≥1
pak pro q>6 dávají každý vytištěný krok

    |traceM|≤|λ|+1/|λ|≤φ^(q−5)+φ^(5−q).

Položme s=q−5≥2. Z Binetova vzorce a φ²−√5=φ^(−2)
dostáváme přesnou identitu

    F_(s+2)−(φ^s+φ^(−s))
      = φ^(−s)[φ^(2s−2)−√5−(−1)^sφ^(−2)]/√5 ≥0.

Poslední znaménko plyne z φ^(2s−2)≥φ²=√5+φ^(−2);
v s=2 nastává rovnost. Tím je pro všechna q>6 prokázáno
|traceM|≤F_(q−3), tedy požadovaná dolní mez. Každý mezikrok
funguje bez domněnky, že vlastní čísla musejí být reálná.

Závěrečný tištěný odhad nezahrnuje q=3,4,5,6. Tyto přesně
čtyři malé konečné případy doplňuje úplný certifikát
`check_boundary_matrix_bounds55.py`, nikoli několik vzorků:
vyhodnotí všech8+16+32+64=120 slov, uloží každou přesnou
2×2 matici, determinant, stopu a počet do
`results/boundary-matrix-bounds55.json`. Výsledné intervaly
stop jsou [0,4],[−1,7],[−1,11],[−2,18], intervaly počtů
[4,8],[6,14],[10,22],[16,36]. Všechny splňují právě
[2F_q,2L_q]. Běh nice15 trval zlomek sekundy; žádný delší
census se nespouštěl. Toto konečné doplnění spolu s výše
uvedeným obecným důkazem uzavírá výslednou mez55(c) v celém
oboru q≥3. Chybný tištěný exponent zůstává odděleně C0009;
správný výsledek se nevydává za kontrolu vadného mezikroku.

# §1.2.3: součty, součiny a jejich meze

V1-X0036; 1. listopadu 2026. Zobrazen hlavní text s. 27–34,
zadání 34–39 a odpovědi 471–475. Tato poznámka pokrývá hlavní
matematiku a první sadu úloh 1–35. Matice 36–47 budou v samostatné
poznámce. První dotisk má 47 úloh. Změna 2010 nahrazuje 1–3
novými 1–3; počet nezvyšuje. Obě podoby jsou rozlišeny níže.

## 1. Co se sčítá a kdy lze měnit pořadí

Pro množinu celých indexů T značí sum_(j in T) a_j součet členů
s indexy v T. Při konečném počtu nenulových členů jej určuje
asociativita a komutativita sčítání; prázdný součet je 0.
Pro nekonečné T se zvlášť požaduje konečná limita na záporné
poloose a na nezáporné poloose. Jejich součet je hodnota řady.
Nejde pouze o limitu symetrických částečných součtů.

První dotisk v (3) započítává index 0 dvakrát. Už a_0=1 a ostatní
členy 0 dávají na pravé straně 2 místo 1. Oprava 16. července 1997
rozděluje indexy na −N<=j<0 a 0<=j<N; ta je správná. V dalších
důkazech používáme právě tuto opravenou definici.

Pravidlo (a), distribuce, je konečné roznásobení. Je platné i pro
dvě konvergentní řady (úloha 5): označíme jejich součty A,B;
pro každé i je vnitřní řada sum_j a_i b_j rovna a_i B a součet
po i je AB. Není potřeba absolutní konvergence, protože výsledek
je iterovaný součet. Libovolné přeuspořádání všech součinů do
jediné řady z toho bez dalšího neplyne.

Pravidlo (b) požaduje právě jeden vzor j pro každý relevantní index
i=p(j). Pro konečné množiny pouze přejmenuje sčítance. Pro nekonečné
řady posun p(j)=c+j a obrácení p(j)=c−j zachovají součet: přesunou
jen konečně mnoho členů přes index 0; zbylé změny konců jsou ocasy
konvergentních jednostranných řad, a tedy jdou k nule. Obrácení navíc
prohodí obě poloosy. To dokazuje úlohu 7 i obecné tvrzení textu.

Absolutní konvergence znamená sum_j |a_j|<infinity. Ke každému
eta>0 pak existuje konečná množina F, mimo niž je součet absolutních
hodnot menší než eta. Každá bijekce indexů nakonec zahrne F,
a zbývající příspěvky mají absolutní hodnotu nejvýše eta. Tím je
dokázána nezávislost na pořadí. Stejný argument na dvojicích (i,j)
dokazuje záměnu dvou součtů v (7),(9), je-li sum_i sum_j |a_ij|
konečné. Konečné vnější podmínky stačí spolu s konvergencí všech
vnitřních řad; jde o konečnou linearitu limit. To pokrývá výjimky
uvedené pod (10), nikoli obecné podmíněně konvergentní dvojné řady.

Pravidlo (c) pro konečné součty sčítá stejnou množinu dvojic.
V (9) je S'(j) její projekce na j a R'(i,j) podmínka členství
v původní množině dvojic. Změna z 2019 pouze vyjasňuje vázaný index.
Pro trojúhelník 1<=j<=i<=n dostáváme vnější 1<=j<=n a vnitřní
j<=i<=n. Tím je (10) dokázáno.

Závorka [P] je indikátor pravdivosti výroku P, tedy 1 či 0.
Bodová identita [R]+[S]=[R or S]+[R and S] dokazuje pravidlo (d)
i cvičení 21 (ve znění opraveném 2004). Pokud tři ze čtyř řad
konvergují, vyjádříme částečný součet čtvrté jako lineární kombinaci
ostatních tří, zvlášť na každé poloose. Limity proto existují a
identita platí; to je požadavek cvičení 6.

V (17) musí být a_j definováno pro všechny indexy, jak text výslovně
říká. V (18) má každý a_i násobnost počtu řešení p(j)=i. Důkaz
záměnou součtů je platný v konečném či absolutně konvergentním
rozsahu popsaném výše. V následujícím trojúhelníkovém příkladu na
s. 33 má první dotisk chybně [1<=j<=n] místo [1<=j<=i]; pro n=2,
i=1,j=2 se liší. Známá oprava 29. července 1997.

## 2. Čtyři příklady a násobné indexy

Rozklad na sudé a liché indexy je disjunktní rozklad množiny;
substituce j->2j a j->2j+1 jsou bijekce příslušných částí.
Mez 0<=j<n/2 v liché části je správně ostrá. Pro n>=0 celočíselné
součet a_i a_j přes 0<=j<=i<=n počítá každý mimodiagonální pár
jednou a každý diagonální pár jednou. Čtverec sum a_i počítá
mimodiagonální páry dvakrát, diagonální jednou. Proto výsledek je
((sum a_i)^2+sum a_i^2)/2, tedy (13).

Pro G=sum_(j=0)^n ax^j, n>=0, odečtení xG od G ruší prostřední
členy a dává (1−x)G=a−ax^(n+1). Pro x!=1 dostáváme (14).
Pro aritmetický součet A=sum_(j=0)^n(a+bj) obrácení indexů dává
2A=(n+1)(2a+bn), tedy (15). Důkazy nevyžadují indukční odhadnutí
výsledku. V obou případech platí i n=0.

Násobné indexy značí součet přes všechny celé n-tice splňující
podmínky. Rovnice (21) je přímo rovnost dvou indikátorů téže množiny.
V (22) jde o rozklady n do nerostoucích nezáporných částí. Pro n=5
jsou právě 11111,21110,22100,31100,32000,41000,50000; souhlasí
i s již prověřeným seznamem rozkladů z §1.2.1.

## 3. Úlohy 1–25 včetně změněných mezí

1.–3. V prvním dotisku je pro n=3,14 součet a_1+a_2+a_3.
Další dva součty jsou 1+1/3+1/5+1/7+1/9+1/11 a
1/9+1/3+1+1/3+1/9. Substituce n->n^2 nepokrývá 3 ani 5
a má dva vzory pro 1 i 4, takže není požadovanou bijekcí.
V novém znění 2010 se toto přesouvá do úloh 2 a 3. Nová úloha 1
je o orientovaných mezích; samostatný rozbor je v oddílu 6.

4. Při n=3 je levá strana a_11+(a_21+a_22)+(a_31+a_32+a_33),
pravá (a_11+a_21+a_31)+(a_22+a_32)+a_33. Členy souhlasí.
5.–7. Obecné důkazy jsou v oddílu 1.
8. Položme a_(i+1,i)=1, a_(i,i+1)=−1 pro i>=0, jinde 0.
Řádek 0 má součet −1, každý další 0; sloupec 0 má součet 1,
každý další 0. Oba iterované součty existují a jsou různé.
Tento přesný celočíselný příklad splňuje i upřesněné zadání 2022.
9.–10. Při n=−1 ani n=−2 není odvození (14) platné: oddělení
členu a z prázdné množiny není dovoleno. Výsledek pro n=−1
náhodou vychází 0; při n=−2 je pravá strana −a/x pro x!=0,1,
ale množinový součet vlevo je 0. Kniha tento rozdíl správně uvádí.
11. Pro x=1 je výsledek (n+1)a, n>=0.
12. Geometrický součet je (7/6)(1−7^(−n−1)).
13. Pro celá m<=n je součet (n(n+1)−m(m−1))/2, včetně
záporných m. Originál dovoluje m=n, pomocný Markdown chybně píše m<n.
14. Dvojitý součet jk je součin obou jednorozměrných součtů:
(n(n+1)−m(m−1))(s(s+1)−r(r−1))/4 pro m<=n,r<=s.
15.–16. Pro T=sum_(j=0)^n jx^j platí
(1−x)T=sum_(j=1)^n x^j−nx^(n+1). Dosazení geometrického součtu
dává [nx^(n+2)−(n+1)x^(n+1)+x]/(x−1)^2.
Pro x=2 dostáváme (n−1)2^(n+1)+2, počáteční hodnoty
0,2,10,34,98,258. Výraz je v úloze 15 součin n·2^n, jak upřesnila
oprava 2002; indukce nebyla použita.
17. Pro konečné S je součet 1 roven |S|, počtu prvků S.
Původní zadání nemělo konečnost; při nekonečném S nejde o konečně
konvergentní řadu podle zdejší definice. To je známá oprava 5. srpna 2025.
18. Pro kladné celé n se dvojice skládají z kladného dělitele i čísla n
a 1<=j<i. Projekce je 1<=j<n, protože i=n je přípustné; po volbě j
zbývá i|n a i>j. Tento obvyklý obor n je nutný: pro n=0 nebo n<0
by se projekce musela upravit. Úloha zkouší především určení vázaného indexu.
19. Při m<=n členy teleskopují na a_n−a_(m−1). Při množinové
konvenci pro všechny meze je výsledek (a_n−a_(m−1))[m<=n], jak
uvádí oprava 2007. Její vztah k nové konvenci 2022 zůstává kandidátem
V1-C0004; viz oddíl 6. Neoznačujeme proto celé cvičení za uzavřené.
20. Pro n>=0 položme U=sum_(k=0)^n(n−k)b^k. Odečtení posunutých
součtů dává (b−1)U=sum_(k=1)^n b^k−n. Proto
(b−1)U+n+1=sum_(k=0)^n b^k. Platí jako polynomiální identita i
pro b=1; výklad číslic v soustavě vyžaduje přirozeně b>=2 a číslice<b.
21. Důkaz indikátory je v oddílu 1. Původní odkaz pouze na pravidlo
(a) byl opraven na (8) a (17) roku 2004.
22. Pro konečné produkty změníme v (5),(7) součty na součiny.
Dále product(b_i c_i)=product b_i · product c_i a
product_R a · product_S a=product_(R union S) a · product_(R intersect S) a.
Každý faktor má na obou stranách stejnou násobnost, i když je nulový.
Tím se netvrdí bezpodmínečná záměna nedefinovaných nekonečných součinů.
23. Prázdné množiny potřebují neutrální prvky 0 pro součet, 1 pro
součin, aby platilo slučování disjunktních rozsahů i na hranici.
24. Pro a_j>0 a b>0,b!=1 je log_b 1=0 počáteční případ.
Připojení jednoho kladného faktoru použije log_b(uv)=log_b u+log_b v;
indukce tedy pokrývá libovolnou konečnou množinu indexů.
25. Vnitřní j nelze přejmenovat na již vázané vnější i tak, aby se
proměnné ztotožnily. Pro n=2 a oba členy 1 je levá strana 4,
konečná pravá strana 2. Druhý krok je vadný; po doslovném zastínění
by další krok obsahoval sum_(i=1)^n n=n^2. Poznámka 2025 vazbu indexu
vyjasňuje, ale původní odpověď rozpoznává chybu správně.

## 4. Úlohy 26–35

26. Ve spodním trojúhelníkovém součinu P1=product_(0<=j<=i<=n)a_i a_j
se a_r vyskytuje r+1krát jako první faktor a n−r+1krát jako druhý.
Celkový exponent je n+2, proto P1=(product_(r=0)^n a_r)^(n+2).
To platí pro záporná, nulová i komplexní a_r. Horní trojúhelník P2
je roven P1 záměnou indexů; celý čtverec má exponent 2n+2.
P1 P2 se od celého čtverce liší diagonálou product a_r^2,
a je tedy (product a_r)^(2n+4). Samotné odmocnění je však bez
kontroly znaménka nedostatečné. V1-C0003 je rozebrán v oddílu 5.

27. Nechť Q_k=product_(j=1)^k(1−a_j), Q_0=1. Pak
1−Q_n=sum_(j=1)^n (Q_(j−1)−Q_j)=sum_(j=1)^n a_j Q_(j−1).
Pro 0<=a_j<=1 je 0<=Q_(j−1)<=1; tedy 1−Q_n<=sum a_j.
To dokazuje i o něco širší verzi požadované nerovnosti.
28. Rozklad 1−1/j^2=((j−1)/j)((j+1)/j) dává teleskopováním
product_(j=2)^n(1−1/j^2)=(n+1)/(2n) pro n>=1; n=1 je prázdný součin.
29. Pro S_r=sum_(i=0)^n a_i^r je trojnásobný součet přes
0<=k<=j<=i<=n roven (S_1^3+3S_1 S_2+2S_3)/6. V čitateli má
monom s třemi různými indexy koeficient 6; monom s právě dvěma
stejnými indexy 3+3=6; monom a_i^3 koeficient 1+3+2=6.
To dokazuje identitu pro libovolná komplexní čísla bez dělení jejich hodnotami.
30. Odečtení obou součinů součtů dává
sum_(j,k) a_j b_k (x_j y_k−x_k y_j). Diagonála mizí;
spojení dvojic (j,k),(k,j) dává vytištěnou Binetovu identitu.
Při a=w,b=conjugate(z),x=conjugate(w),y=z vznikne
(sum|w|^2)(sum|z|^2)=|sum w_j z_j|^2+
sum_(j<k)|w_j conjugate(z_k)−w_k conjugate(z_j)|^2.
To je **přesné znění originálu**. Součet w_j z_j nemá conjugate(z_j).
Obvyklou seskvilineární podobu Cauchyho–Schwarzovy nerovnosti získáme
náhradou z za conjugate(z). Pomocný Markdown míchá obě podoby; originál nikoli.
31. Dosazení a=u,b=1,x=v,y=1 dává
sum_(j<k)(u_j−u_k)(v_j−v_k)=n sum u_j v_j−(sum u_j)(sum v_j).
Pro obě neklesající reálné posloupnosti jsou všechny sčítance vlevo
nezáporné; tím je dokázána i monotónní nerovnost přidaná 2011.
32. Opakovaná distribuce vybírá v každém z n sloupců právě jeden
řádek i_j z 1,...,m. Výběry jsou právě n-tice na pravé straně.
Pro n=0 zůstane prázdný součin 1 a jedna prázdná n-tice.

33. Definujme Q(t)=product_(k=1)^n(t−x_k) a
D_j=product_(k!=j)(x_j−x_k), kde x_k jsou navzájem různá.
Polynom L_j(t)=product_(k!=j)(t−x_k)/D_j má v uzlech hodnoty
L_j(x_i)=[i=j]. Pro polynom f stupně nejvýše n−1 proto
f(t)=sum_j f(x_j)L_j(t): rozdíl má stupeň nejvýše n−1 a n kořenů.
Porovnání koeficientu t^(n−1) dává sum_j x_j^r/D_j=0 pro
0<=r<n−1 a 1 pro r=n−1. Pro r=n použijeme t^n−Q(t),
jehož vedoucí koeficient je sum x_k; výsledek je sum x_k.
Vše platí i pro n=1. Indukční důkaz knihy má stejný závěr;
opravou 2009 se vyjasňuje, že koeficienty pomocného polynomu P
jsou symetrické ve všech uzlech a nezávisí na zvoleném j.

Pro obecné celé r>=0 je výsledek úplný homogenní polynom
h_(r−n+1)(x_1,...,x_n)=sum_(e_1+...+e_n=r−n+1, e_k>=0)
product x_k^e_k, s h_0=1 a h_s=0 pro s<0. Odvodíme jej
z částečných zlomků t^r/Q(t), případně z vytištěného integrálu:
pro R>max|x_k| geometrické řady pro 1/(1−x_k/z) konvergují
absolutně a stejnoměrně na |z|=R. Člen po členu integruje na 0
každá celočíselná mocnina kromě z^(−1), která dává 2pi i.
Rezidua v jednoduchých pólech jsou x_j^r/D_j. Ekvivalence zápisu
pomocí slabě rostoucích indexů (dodatek 2009) jen přepíše násobnosti
e_k; pro s=0 jde o prázdnou n-tici.

34. Pro libovolný monický polynom f stupně n−1 dává předchozí
porovnání koeficientů sum_k f(y_k)/product_(r!=k)(y_k−y_r)=1.
Zvolíme y_k=k a f(t)=product_(r!=m)(x+t−r). Je monický v t,
ať je x jakékoli komplexní číslo. Tím je dokázána úloha i obecnější
verze odpovědi se z_r; není nutné řešit polynom v parametru x.

35. Supremum je nejmenší horní mez. Pro neprázdné množiny reálných
čísel A,B s konečnými supremy platí sup(A+B)=sup A+sup B:
horní mez je zřejmá a prvky v eta-blízkosti obou suprem dají opačný
odhad s chybou 2eta. Stejně pro nezáporná čísla platí
sup{ab:a in A,b in B}=(sup A)(sup B) v rozsahu, kde je pravá
strana definována. Přejmenování a záměna dvou suprem vybírají
stejnou množinu hodnot. Sjednocení má supremum max(sup A,sup B).
Prázdné množině přiřadíme −infinity; pro sčítání pak pravidla
rozšíříme všude, kde nevzniká neurčitý výraz (+infinity)+(−infinity).
Výrok o součinu nezáporných množin nelze slepě použít na prázdnou
množinu se supremem −infinity. Toto je upřesnění oborů, nikoli
protipříklad k pravidlu pro neprázdné, reálně omezené množiny.
Zápis vnějšího sup dvou hodnot byl roku 2024 změněn na max.

## 5. V1-C0003: znaménko ve vysvětlení přidaném roku 2020

Původní odpověď 26 uvádí správný výsledný vzorec. Dodatek
z 12. června 2020 výslovně vkládá P1=(P1 P2)^(1/2) a zdůvodňuje
to rovností P1=P2. Zadání přitom neomezuje a_i na kladná čísla.

Pro n=1,a_0=−1,a_1=1 je P1=a_0^2(a_1 a_0)a_1^2=−1,
rovněž P2=−1, ale (P1 P2)^(1/2)=1. Všechny výrazy jsou reálně
definovány a odmocňovaný základ je kladný; nejde o volbu větve
komplexní mocniny. Odmocnění proto není platný obecný krok.
Přímé spočtení exponentů z oddílu 4 je krátká oprava bez omezení
vstupů. Alternativně lze nejprve důkaz provést pro kladné hodnoty
a výsledek rozšířit jako polynomiální identitu; tento krok však
v doplněné odpovědi uveden není.

Prohledány all1-prepre,all1-pre,all1,err1 i aktuální err1.textxt,
pod číslem stránky, úlohy, výrazem P1/P2 a odmocňováním. Přesná
sazba dodatku byla zobrazena: images/errata-all1-pre-file014.png.
Další oprava této rovnosti nenalezena. Veřejná rešerše s hesly
TAOCP 1.2.3 26 negative a Knuth 472 square root nepřinesla relevantní
dřívější rozbor; to není důkaz prvenství. Novější tištěný exemplář
s dodatkem 2020 nemáme. Závěr míří přímo na doložený autorův dodatek.

## 6. V1-C0004: dvě konvence obrácených mezí

Množinový součet sum_(p<=j<=q) a_j je pro p>q roven 0.
Orientovaný součet S(p,q) je místo toho určen rozdílem diskrétní
primitivní funkce: zvolme F s F(k)−F(k−1)=a_k a položme
S(p,q)=F(q)−F(p−1). Pro p<=q je to běžný součet, pro p=q+1
je to 0 a pro p>q+1 záporný součet od q+1 do p−1.
Má vlastnost S(p,q)+S(q+1,r)=S(p,r) pro libovolná celá p,q,r.

Nová odpověď 1 z 2010 přiřazuje právě tuto konvenci zápisu s třemi
tečkami. Dodatek 1. března 2022 ji výslovně nabízí také pro sumu
s horní a dolní mezí, tedy levý zápis v (1), a varuje, že pravý
zápis přes podmínku na indexu je jiný. Proto nyní součty (1)
jsou označeny jako jen „essentially equivalent“.

Naproti tomu odpověď 19 byla 1. května 2007 změněna na
(a_n−a_(m−1))[m<=n], což používá množinovou konvenci. Zadání má
horní a dolní mez, nikoli podmínku m<=j<=n pod symbolem sumy.
Pro a_j=j,m=2,n=0 jsou sčítance všechny 1. Orientovaná konvence
vyžaduje S(2,0)=−1, ale odpověď 2007 vrací 0. Původní odpověď
1997, a_n−a_(m−1), je naopak správná pro orientovanou konvenci.

Matematický rozpor při současném univerzálním použití obou konvencí
je přesný. **Stav je zatím candidate:** slova „We might also say“
v poznámce 2022 mohou být zamýšlena jako lokální alternativní návrh,
nikoli jako změna konvence ve všech ostatních cvičeních. K uzavření
redakčního výkladu by pomohl aktuální dotisk či další autorovo
vyjasnění. Žádný z obou matematických výkladů se nesmí zaměnit
za druhý; úloha 19 zůstává v mapě partial.

## 7. Zdroje a zbývající rozsah

[Knuthův původní text Two Notes on Notation](https://www-cs-faculty.stanford.edu/~knuth/papers/tnn.tex)
byl stažen z autorovy stránky, rozbalen z gzip a přečten v relevantní
části o Iversonově konvenci. Podporuje zdejší indikátorové důkazy,
připisuje Iversonovi relační výroky a rozlišuje vlastní rozšíření na
libovolné výroky. Konkrétně odkazuje na Iversonovu knihu 1962, s. 11,
a na Kroneckerovy původní práce. Je to primární zdroj pro Knuthův
výklad; přesné ověření tvrzeného historického prvenství Fourier/Kronecker
ještě vyžaduje uvedené starší prameny.

Apostolův odkaz na kapitolu o řadách, historické poznámky k Binetovi,
Čebyševovi, Eulerovi, Waringovi a Sylvesterovi nejsou pouhým vlastním
důkazem rovnic bibliograficky uzavřeny. Jsou evidovány zvlášť.

`check_sums.py` doplňuje důkazy přesnými celými čísly a zlomky:
19 530 podepsaných trojúhelníkových součinů a symetrických součtů,
21 845 nerovností, 945 interpolačních identit, 612 případů úlohy 34
a další kontroly v `results/sums.json`. První běh prošel; poté byl
počáteční prázdný součin u úlohy 34 změněn na Fraction(1), aby se
ani triviální n=1 nevyhodnocovalo typem float. Po této změně prošel
celý program znovu. Oba běhy jsou stejná metoda, nikoli dva nezávislé důkazy.

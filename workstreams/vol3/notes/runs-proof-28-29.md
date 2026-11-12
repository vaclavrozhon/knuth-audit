# Runs: přidané úlohy28–29 v aktualizovaném znění

Koordinátor výslovně rozšířil uzavření sekce také na přidané úlohy.
Zadání jsou v `images/runs-errata-new28-29.png` (all3-prepre PDF6),
odpovědi v `runs-errata-answer11.png` (PDF28) a
`runs-errata-answers28-29.png` (PDF29). Převzatá rešerše pěti vrstev:
`sources/runs-errata-review.json`. Žádný výpočtový běh.

## 28. Kořeny a jejich reciproký součet

V3-P0273–0281 již dokazují úplnou klasifikaci kořenů, růst,
Hadamardovu faktorizaci a identitu L(z)+P(z)=cz, kde
`P(z)=2z/(z−1)+Σ_m≥1[z/(z−z_m)+z/(z−conj(z_m))]`.
Tyto důkazy se neopakují. Rovnice kořenů z=e^(z−1) je přímo
rovnice stromové funkce T(1/e); označení nevyžaduje další teorii.

Pro asymptotiku pišme M=2πm, h=log(eM), z_m=a+ib. Z již doložených
rovnic `a=1+log|z_m|`, `b=M+π/2−arctan(a/b)` a a=O(log m)
dostáváme nejprve b=M+π/2+O(log m/m). Dosazení do první rovnice dává
`a=h+π/(2M)+O((log m)²/m²)`. Druhá pak dává
`b=M+π/2−h/M+O((log m)²/m²)`, přesně tištěný dvoučlenný rozvoj.

Také uvedenou konvergentní řadu lze ověřit přímo. Pro pevné m≥1
pišme σ=−1−(2m+1)πi, l=Log σ v hlavní větvi, t=1/σ.
Hledejme z=−σ+v, kde `v=l+log(1−tv)`.
Po q=tv je to Lagrangeova rovnice `q=t(l+log(1−q))`.
Lagrangeova inverze dává

`[t^n]v=1/(n+1) [q^n](l+log(1−q))^(n+1)
       =Σ_j (−1)^j [n;j] l^(n+1−j)/(n+1−j)!`,

kde [n;j] jsou neoznačená Stirlingova čísla prvního druhu; poslední
krok používá `(-log(1−q))^j/j!=Σ_n[n;j]q^n/n!`.
To je přesně tištěná dvojitá řada.

Konvergence v požadovaném bodě: R=|σ|≥sqrt(1+9π²) a
`|l|≤log R+π/2+1/(3π)`. Na |q|=1/2 máme |log(1−q)|≤log2.
Platí `2(log R+π/2+1/(3π)+log2)<R` pro toto R i všechna větší
(levá strana roste derivací2/R<1, základ splňuje přísnou nerovnost).
Pro |t|≤1/R je tedy |t(l+log(1−q))|<1/2. Rouchéova věta dává jediný
kořen v tomto kruhu; derivace1+t/(1−q) se tam nerovná0.
Kořen je holomorfní i na o něco větším t-kruhu, takže řada konverguje
v t=1/σ. Z rovnice plyne e^(z−1)=z. Jeho imaginární část leží mezi
2πm a2π(m+1), a proto jde podle uzavřené klasifikace právě o z_m.

Zbývá určit c. Pro reálné x→∞ je
`P(x)−P(−x)=4x/(x²−1)+Σ_m≥1 4Re(x z_m/(x²−z_m²))`.
Pro a_m=O(log(m+1)), b_m asymptotické2πm má jeden člen absolutní
hodnotu `O(x log(m+1)/(x²+m²))`. Plyne to přímo z reálné části
`z_m/(x²−z_m²)`, jejíž čitatel je
`a_m(x²−a_m²−b_m²)` a jmenovatel
`(x²−a_m²+b_m²)²+4a_m²b_m²`.
Rozdělení součtu na m≤x a m>x dává O(log x), stejně jako v odpovědi.
Přitom přímo z25 `L(x)=−x+o(1)` a `L(−x)=−1+o(1)`.
V identitě2cx=L(x)−L(−x)+P(x)−P(−x) proto vyjde c=−1/2.
Koeficient z v L+P=−z/2 a L_1=e−1 pak dává
`Σ_m≥1(1/z_m+1/conj(z_m))=e−5/2`, jak požaduje zadání.

## 29(a). Vrcholy a střídavé běhy

Pro n≥2, k vrcholů a v údolí má slovo1+k+v střídavých běhů.
Vrcholů a údolí může být stejně, nebo se liší o1. Při2k+1 bězích je
vrcholů vždy k. Při2k bězích mají poloviny permutací k nebo k−1
vrcholů; při2k+2 bězích k nebo k+1. Záměna a_i→n+1−a_i tyto
poloviny páruje. Tím je(a) pro n≥2 dokázána včetně koeficientů1/2.
Pro n1 je návaznost na výslovnou konvenci úlohy16 nejasná; samostatný
candidate/low C0018 dokládá1 proti1/2. Nejde o potvrzenou chybu.

## 29(b,c). Důkaz přes binární kartézský strom

Ke slovu různých hodnot přiřaď binární strom: kořenem je maximum,
levým a pravým podstromem stejná konstrukce pro příslušné části slova.
Inorder je inverze, takže jde o bijekci. Doplníme na oba konce slova
sentinel∞. Vrchol s oběma dětmi odpovídá vnitřnímu vrcholu permutace;
list údolí; vrchol s jediným levým dítětem dvojitému vzestupu a s jediným
pravým dítětem dvojitému sestupu. Platí to, protože podstrom daného x
tvoří maximální souvislý blok menších hodnot kolem x; mimo něj jsou
sousedé větší nebo sentinel.

Zachovejme strom kromě volby strany jeho jediných dětí. Má-li k
vrcholů se dvěma dětmi, má k+1 listů a a=n−1−2k vrcholů s jedním
dítětem. Jejich levé/pravé volby jsou nezávislé a dávají2^a různých
permutací; počet vrcholů k se nemění. Každý vrchol se dvěma dětmi
přispívá jedním sestupem, každé jediné pravé dítě přidá jeden další
sestup. Listy ani jediné levé děti sestup nepřidávají.

V každé třídě je tedy právě jedna permutace se k vrcholy a k sestupy:
ta se všemi jedinými dětmi vlevo. Počet tříd je t_nk. Každá má
velikost2^(n−1−2k), což dokazuje(b), a její sestupový polynom je
`x^k(1+x)^(n−1−2k)`, což po součtu dokazuje(c). Tento argument
zahrnuje i n1. Nepotřebuje převzít odkazovaný externí článek.

Bibliografické atribuce Corless et al., Janson a Shapiro–Woan–Getu
nebyly přezkoumány; všechny zde potřebné matematické argumenty jsou
výše doloženy. Aktualizovaný oddíl má jedinou novou otevřenou otázku:
singletonovou konvenci C0018 v29(a).

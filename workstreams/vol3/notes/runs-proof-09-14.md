# Runs: úlohy9–14, zadání45–46, odpovědi603–604

Sazba v `images/runs-file-056.png`, `runs-file-057.png`,
`multisets-file-614.png`, `multisets-file-615.png`. Opravená odpověď11
je zobrazena v `images/runs-errata-answer11.png`; všech pět vrstev
je v `sources/runs-errata-review.json`. Bez nového nálezu a bez běhu.

## 9. Celková délka prvních k běhů

Převzato q_km=Pr(S_k≥m) z V3-P0265; doplňme q_k0=1, k≥1.
Pro Q_k(z)=Σ_m≥0 q_km z^m je
`h_k=(1−1/z)Q_k+1/z` rozdílem sousedních ocasů. Součet podle k dává
`Σ_k≥1 x^k Q_k(z)=x g(x,z)/(1−x)`; každé Eulerovo číslo s j sestupy
vstupuje do všech k≥j+1. Proto

`h(z,x)=(1−1/z)x/(e^((x−1)z)−x)+x/(z(1−x))`.

Zdánlivá singularita v z0 se krátí. Výběr x a x² dává přesně
`h_1=e^z−(e^z−1)/z` a
`h_2=e^(2z)−z e^z+e^z−(e^(2z)−1)/z`.

## 10. Střední hodnota a rozptyl

Derivováním9 v z1 dostaneme
`M(x)=Σ_n≥1 E(S_n)x^n=x/(e^(x−1)−x)−x/(1−x)`;
je to zároveň L(x)/(1−x). Pišme D=e^(x−1)−x, u=x−1. Pak
`M=2/u²+7/(3u)+O(1)`. Reziduum M(z)z^(−n−1) v1 je
`−2(n+1)+7/3=−2(n+1/3)+1`, a v z_j je `z_j^(−n)/(z_j−1)`.
Tím sedí tištěná konturová rovnice i Cauchyho odhad O(r^(−n)).

Přesná konvergentní řada nepotřebuje nový limit kontur: převzatá
V3-P0280 a H(1)=−1/3 z V3-P0281 dávají pro n≥1

`E S_n=2n−1/3−Σ_{j>n}(L_j−2)
      =2n−1/3+2Σ_{k≥1}Re(1/(z_k^n(1−z_k)))`.

Výměna součtů je absolutně konvergentní, protože nejnižší mocnina
v ocasu je j=n+1≥2 a |z_k| roste lineárně s k.

Druhá derivace9 je
`h_zz(1,x)=−2M(x)−2x(x−1)e^(x−1)/D²`.
Druhý člen má Laurentův rozvoj
`−8/u³−32/(3u²)−8/(3u)+O(1)`.
Jeho koeficient x^n je proto `4n²+4n/3+O(R^(−n))` pro libovolné
1<R<|z_1|. Vzorec Var S_n=h_n''(1)+M_n−M_n² a
M_n=2n−1/3+exponenciální zbytek dává
`Var S_n=2n/3+2/9+O(R^(−n))`, po případném zmenšení R.
Tím jsou doloženy i oba mezikroky odpovědi.

## 11. Délka samotného k-tého běhu

P_k0=0. Pro n≥1 rozložme událost podle kladných prvních k−1 délek:
`P_kn=Σ_{t_1,..,t_(k−1)≥1}D(t_1,..,t_(k−1),n,1)`.
Je to opravený rozsah sumace1999. Determinant z úlohy8 nutí přesnou
délku n prostřednictvím posledního dalšího prvku.

Rozvoj prvním řádkem pro prvních j sloučených délek,1≤j≤k−1,
dává koeficient
`c_(j−1)=(−1)^(j−1)Σ_{t_1,..,t_j≥1}1/(t_1+...+t_j)!`.
Počítáním kompozic a binomickou identitou máme

`c_j=(−1)^j Σ_{m≥0}choose(m,j)/(m+1)!
    =−1+e Σ_{r=0}^j(−1)^r/r!`.

Poslední dva členy rozvoje se rovnají−E_k(n), kde pro n≥1

`E_k(n)=(−1)^k Σ_{t_1,..,t_(k−1)≥1}
 [1/(n+T)!−1/(n+T+1)!]`, T=Σt_i.

Pro k1 je to `1/(n+1)!−1/n!`; pro k2 součet teleskopuje na1/(n+1)!.
Pro k≥3 posunutí T ve druhém součtu a Pascalova identita dává
`E_k(n)=(−1)^k Σ_{m≥0}choose(m,k−3)/(n+2+m)!`.
Pro n0 musí být všechny E_k(0)=0, neboť všechny P_k0=0.
E_1(0) už je0 a ostatní proto potřebují opravený faktor[n>0].
Jde přesně o známé opravy2006, nikoli nové chyby.

Z c_j plyne `C(x)=(e^(1−x)−1)/(1−x)`. Rekurence
`P_kn=Σ_{j=0}^{k−2}c_jP_(k−j−1),n−E_k(n)` je po součtu přes k
ekvivalentní `C(x)H=H/x+E(z,x)`. Proto platí tištěný tvar
`H=x(1−x)E/(x e^(1−x)−1)`.

Uzavřený výraz E lze doložit i bez dalších determinantových součtů.
Použijme již dokázané přechodové jádro začátků běhů z V3-P0271.
Hustoty f_k splňují
`f_(k+1)(y)=L_k−e^y∫_0^y e^(−t)f_k(t)dt`.
Pro F(y,x)=Σ_k≥1f_k(y)x^(k−1) pak
`F_y=(1−x)F−1−L(x)`, `F(0,x)=1+L(x)`, takže

`F(y,x)=(1−x e^((1−x)y))/(1−x e^(1−x))`.

Při počáteční hodnotě y je GF délky
`1+(z−1)e^(z(1−y))`, což plyne z ocasů
`(1−y)^(m−1)/(m−1)!`. Integrací tedy vychází

`H=x/(1−x)+x(z−1)/(1−x e^(1−x))
 ·[(e^z−1)/z−x(e^(1−x)−e^z)/(1−x−z)]`.

Dosadíme E=(xC−1)H/x. Se zkratkami a=1−x, d=z+x−1 je čitatel
nad jmenovatelem z d a² roven
`e^(1−x)x²z²−(a+xz)d−e^z(z−1)²a²`.
Po vynásobení e^x je to přesně opravený vzorec v obrázku errat:

`E=[e z²x²−e^x(1−x+zx)(z+x−1)
    −e^(z+x)(1−z)²(1−x)²]
   /[e^x z(z+x−1)(1−x)²]`.

Výběr prvních dvou koeficientů dává H_1=h_1 a
`H_2=e h_1+1−e^z`. Integrací stejného jádra s
`A_k(z)=∫e^(z(1−y))f_k(y)dy` dostaneme
`A_(k+1)=(A_k−L_k h_1)/(1−z)`, tedy i vzorec na604:
`1−H_(k+1)=(1−H_k)/(1−z)−L_k h_1`.

Sousední běhy opravdu nejsou nezávislé:
Pr(T_1=1,T_2=1)=Pr(U_1>U_2>U_3)=1/6, ale součin marginál
je `(1/2)(e/2−1)=e/4−1/2`, což není1/6.

## 12. MacMahonův vzorec pro multiset

N_t=∏_j choose(t+n_j−1,n_j) plyne z nezávislých slabých kompozic
četností do t rozlišitelných krabic. Inkluze–exkluze vynechaných
krabic dává tištěné M_t. Pro slovo s r běhy musíme oddělit jeho
r−1 sestupů; dalších t−r různých hran lze vybrat n−r způsobilých míst.
Proto `M_t=Σ_r P_r choose(n−r,t−r)`, trojúhelníková soustava
s jednotkovou diagonálou, jak stojí v odpovědi.

Přímý důkaz požadovaného vzorce: dovolme prázdné krabice. Po vložení
r−1 povinných oddělovačů zbývá t−r oddělovačů libovolně rozdělit
do n+1 mezer včetně obou konců. Dostaneme
`N_t=Σ_r P_r choose(n+t−r,n)`. Obě strany počítají totéž, neboť
v každé krabici je její multiset seřazen jednoznačně. Po součtu podle t

`Σ_t≥0 N_t z^t=(Σ_r P_r z^r)/(1−z)^(n+1)`.

Výběr z^k po vynásobení(1−z)^(n+1) dává přesně konečný součet zadání12.

## 13–14. Dva konkrétní příklady

13. Čtyři barvy mají každá13 karet. Převzatá symetrie a průměr z
    V3-P0283 dávají `1+13·(4−1)/2=20.5`.
14. Slovo3111231423342244 má kanonické závorky
    `(31)(1)(1)(231)(42)(3342)(2)(4)(4)`.
    Jejich interkalační součin má fronty
    `Q_1=3112,Q_2=3432,Q_3=1134,Q_4=2244`, přesně první tištěný biword.
    Komplement5−x a pořadí bloků1,4,3,2 dají
    `Q_1=2443,Q_2=3311,Q_3=4421,Q_4=2123`, druhý tištěný biword.
    Postupným prvním návratem do minima1 dostáváme cykly
    `(2342341)(421)(4321)(31)`: jejich hrany postupně vyčerpají právě
    uvedené čtyři fronty. Smazání závorek dává2342341421432131.
    Jeho běhy jsou `234|234|14|2|14|3|2|13|1`, tedy9;
    původní `3|11123|14|2334|2244` má5. Žádná enumerace ani test.

Historické atribuce a obsah externích článků603–604 nebyly přezkoumány.
Všechny zde použité matematické výroky mají vlastní argument výše
nebo výslovný odkaz na uzavřený argument.

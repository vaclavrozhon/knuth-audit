# Úloha 7.2.2–70: částečně orientované cesty

Kontrola 1. listopadu 2026. Kniha 4B, první vydání, druhý dotisk,
strana 60 a odpověď na straně 411. Autorův `fasc5b.ps` z 11. září 2019
má stejné zadání na straně 32 a odpověď na straně 49.

**F096: v posledním řádku zadání je nesprávné `ρ_m = 2^m + O(1)`.**
Správně platí

\[
\rho_m=2^m+3m-\frac{15}{2}+O(m^2 2^{-m}).
\]

Stačí tedy změnit `O(1)` na `O(m)`. Zbytek zadání a polynomové
rekurence v odpovědi jsou správné. Jde o asymptotiku pro rostoucí m;
v tvrzení o druhém momentu pro rostoucí n je m pevné.

## Nezávislý model cest

Řádky číslujeme 0 až m−1. Cestu jednoznačně určují výšky jejích n−1
kroků doprava. V každém sloupci jde svisle monotónně, takže existuje
přesně m^(n−1) cest. Poslední sloupec už jen dokončí cestu do cíle.
Volíme pouze kroky, po nichž ještě existuje dokončení; toto je i
konvence citovaného článku a knižního příkladu.

Je-li p pravděpodobnost konkrétní cesty, její příspěvek k E D² je 1/p.
Položme h_i=2 na krajních řádcích, jinak 3; b_j=1 na krajích, jinak 2.
Matice vah jednoho nefinálního sloupce je

\[
T_{ii}=h_i,\qquad T_{ij}=h_i b_j 2^{|i-j|-1}\quad(i\ne j).
\]

První faktor je počet voleb po vstupu do nového sloupce; každý další
svislý krok uvnitř má dvě možnosti, na hranici zůstane jen krok doprava.
Proto E D_mn² = e₀ᵀ T^(n−1) 1 a G_m(z)=z e₀ᵀ(I−zT)⁻¹1.

`check_nes.py` obsahuje jiný, doslovný výčet po jednotlivých krocích:
sám kontroluje navštívené vrcholy, pomocí prohledání grafu testuje
dosažitelnost cíle a násobí skutečné počty nabízených kroků. Na všech
25 mřížkách 2≤m≤6, 1≤n≤5 souhlasí počet cest, celková pravděpodobnost
1 a druhý moment s maticí. Pro m=3 dostaneme 1,10,96,924,8892.

## Racionální funkce a kořeny

Odraz řádků dovoluje matici zmenšit na r=ceil(m/2):
C_ij=Σ T_ik přes k∈{j,m−1−j}, bez opakování prostředního řádku.
Pak Q_m=det(I−zC); P_m je determinant téže matice s prvním sloupcem
nahrazeným jedničkami. Tento Cramerův vzorec dává požadované G_m=zP_m/Q_m.

Přesné charakteristické polynomy a čitatele byly porovnány pro
2≤m≤22, první malé případy i přímo Cramerovým determinantem.
Všechna počáteční data a rekurence z knihy souhlasí.

Pro obecnou rekurenci jmenovatele lze použít třídiagonální C⁻¹.
Pro m≥5 začíná řádky s diagonálou −1/2,−7/9 a prvními
protějšími mimodiagonálními prvky 2/3,1/2. Uvnitř má diagonálu
−5/9 a oba sousední prvky 2/9. Poslední diagonála je −1/3 pro
sudé m; pro liché m je −5/9 a poslední dolní prvek 4/9.
Determinant při přidání dalšího vnitřního řádku má rekurenci
H_r=(−5/9−z)H_(r−1)−(4/81)H_(r−2).
Přechod m→m+2 mění det(C⁻¹) faktorem −1/9, takže po normalizaci
vznikne přesně Q_m=(5+9z)Q_(m−2)−4Q_(m−4).
Malé krajní případy jsou ověřené samostatně.

Rekurence čitatele také plyne z výpočtu v citovaném primárním článku:
jeho k=m−1, ℓ=n−1 a M_k=2zN_k/G_k. Knižní funkce je
z(1+M_(m−1)), tedy Q_m=G_(m−1), P_m=G_(m−1)+2zN_(m−1).
Prošel jsem rozklad svislých úseků, funkcionální rovnice i jejich
řešení kernelovou metodou v §2, strany 4–9 veřejného preprintu.
N i G splňují tutéž lineární rekurenci, takže ji splňuje i P.
Počáteční N=(2,5+3z,11+9z,23+54z+27z²) dávají přesně knižní P.

T je diagonálně podobná symetrické matici
S=(1/2) D L D, kde D_ii=√(h_i b_i) a
L_ij=2^|i−j|+[i=j∈{0,m−1}]. Matice L má pro m≥3 LDLᵀ pivoty
2,−1,−3,…,−3,−2. To lze odvodit z determinantů matice
K_ij=2^|i−j|, jejíž determinant velikosti j je (−3)^(j−1):
po přidání prvního krajního členu jsou vedoucí determinanty
(2/3)(−3)^(j−1) pro 2≤j<m; po přidání obou krajů je plný
determinant (4/9)(−3)^(m−1). Inverze K je třídiagonální, takže
tyto vztahy vyplývají také přímo z lemmatu o změně determinantu.

T tedy má právě jedno kladné vlastní číslo a všechna ostatní záporná.
Perronův kladný vlastní vektor je invariantní vůči odrazu; omezení
na symetrický podprostor má právě jedno kladné vlastní číslo.
To dokazuje knižní tvrzení o kořenech Q_m. Pro m=2 je Q_2=1−4z.
Protože T je striktně kladná, její Perronův kořen ρ_m je jednoduchý
a ostatní vlastní čísla mají menší absolutní hodnotu. Kladné počáteční
a koncové váhy nemohou jeho příspěvek vyrušit. Tím je dokázáno
E D_mn²=Θ(ρ_m^n) pro pevné m.

## Obecný důkaz opravené asymptotiky

Položme k=m−1 a definujme s blízko 1/2 vztahem
z=−(2s−1)(2/s−1)/9, tedy s+1/s=(5+9z)/2.
Dále p(s)=1+2z−2s(1−z). Rekurence a její čtyři počáteční
hodnoty dávají tyto přesné výrazy:

\[
Q_{2r+1}=-\frac{2^r}{3}\bigl(p(1/s)s^r+p(s)s^{-r}\bigr),
\]
\[
Q_{2r+2}=-\frac{2^r}{1+s}\bigl(p(1/s)s^{r+1}+p(s)s^{-r}\bigr).
\]

Ověření počátečních hodnot je v programu symbolické. Obecný krok
plyne z (2s)(2/s)=4 a 2s+2/s=5+9z. Kladný kořen Q_m proto splňuje

\[
s^{m-2}=R(s)=
-\frac{(2s-1)(2s^2-11s-4)}{(2-s)(2-11s-4s^2)}.
\]

Perronův kořen roste do nekonečna: už minimum řádkových součtů T
roste nejméně jako 2^ceil((m−1)/2), což plyne z nejvzdálenějšího
krajního sloupce matice. Proto kladný pól z=1/ρ_m klesá k nule,
s se blíží 1/2 zdola a lze položit δ=1/2−s, ε=2^(−m).

Přímé Taylorovy rozvoje dávají

\[
R(1/2-\delta)=\tfrac83\delta+\tfrac{40}9\delta^2+O(\delta^3),
\qquad z=\tfrac23\delta+\tfrac{16}9\delta^2+O(\delta^3).
\]

Rovnice pro kořen zní R=4ε(1−2δ)^(m−2). Její pravá strana
je nejvýše 4ε, takže nejprve δ=O(ε). Rozvoj s jednotným zbytkem
O(m²δ²) pak dává

\[
\delta=\tfrac32\varepsilon+
 (\tfrac{21}4-\tfrac92m)\varepsilon^2+O(m^2\varepsilon^3).
\]

Po dosazení a převrácení:

\[
\frac1{\rho_m}=\varepsilon+
 (\tfrac{15}2-3m)\varepsilon^2+O(m^2\varepsilon^3),
\qquad \rho_m=2^m+3m-\tfrac{15}2+O(m^2 2^{-m}).
\]

Tento důkaz nevyužívá nesprávný asymptotický rozvoj článku.
Všechny symbolické koeficienty nezávisle přepočítává program.
Čtrnáct číselných kořenů do m=100 má intervaly délky 3·10⁻²⁰
ověřené přesnou racionální aritmetikou a změnou znaménka Q_m(1/ρ).
Unicita kladného kořene je dokázaná výše, nejde jen o plovoucí výpočet.

| m | ρ_m − 2^m |
|---:|---:|
| 10 | 22.2144800247044 |
| 20 | 52.4985679196223 |
| 40 | 112.499999993996 |
| 80 | 232.499999999999999999977… |
| 100 | 292.499999999999999999999999966… |

## Prameny a errata

Primární článek: Mireille Bousquet-Mélou, *On the Importance Sampling
of Self-Avoiding Walks*, CPC 23 (2014), 725–748,
DOI 10.1017/S0963548313000643. Veřejný
[preprint arXiv:1106.1876v2](https://arxiv.org/abs/1106.1876v2)
je z 31. srpna 2012. Stažené PDF a metadata jsou v
`sources/estimation/bousquet-melou-2014.*`.
Název souboru označuje rok citované publikace, nikoli rok verze PDF.

Preprint má v Proposition 5 nesprávný rozvoj svého pólu ρ_k:
již koeficient u 4^(−k−1) se neshoduje s jeho vlastní rekurencí.
Původní sazba byla zobrazena a je uložena jako
`images/bousquet-melou-prop5.png`. Náš pól v jeho indexaci má druhý
koeficient 9/2−3k, nikoli konstantu 9/2. Číselná označení ρ v článku
a knize jsou navzájem převrácená! To není příčina rozporu.
Zda je stejná chyba i ve finální časopisecké sazbě, netvrdíme:
vydavatel nabídl pouze abstrakt a autorův server byl nedostupný.
Bibliografické údaje jsou ověřené na stránce vydavatele.

1. listopadu 2026 byly prohledány `all4b.txt`, `err4b.txt`,
`all4f5.txt`, `err4f5.txt` i oba aktuální zdroje `.textxt`,
včetně hesel, čísla úlohy a posunutého číslování stran.
V historickém Fascicle 5 odpovídá zadání straně 58; jeho známá
změna na této straně upravuje hodnocení úlohy 69. Oprava odpovědi
69 na straně 411 svazku 4B z 14. března 2023 je rovněž jiná věc.
Oprava úlohy 70 nalezena nebyla. Poslední kontrola úplnosti stažených
oficiálních souborů proběhla téhož dne; zůstává 55 souborů.

Znění potvrzují zobrazené `images/vol4b-factor-080.png` a
`images/fasc5b-ex70.png`; odpověď `images/vol4b-estimation-431.png`.
Fyzický výtisk ani celý nejnovější dotisk nemáme ověřený.
Nález neznamená tvrzení o prvenství. Nic nebylo odesláno.

Reprodukce: `python3 audit-2026-10-31/check_nes.py`.
Výstupy: `results/estimation/nes-verified.json` a `nes.log`.

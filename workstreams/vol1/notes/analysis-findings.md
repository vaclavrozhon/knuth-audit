# §1.2.10: tři nesrovnalosti v odpovědích

Kontrola 1. listopadu 2026. Základ je třetí vydání, první dotisk 1997,
tištěné s. 501–502 = strany souboru 516–517. Originály byly zobrazeny.
Všechny čtyři PDF řady errat a zdroj `err1.textxt` byly prohledány;
aktualizace z dneška je doložena v `sources/errata-refresh-2026-11-01.json`.
Příslušné záznamy shrnuje `sources/analysis-errata-extract.json`.
Potvrzení níže se týká dostupných podkladů, nikoli prvenství nebo fyzické knihy.

## V1-C0013: konstanta v exponenciálním odhadu

V odpovědi 13 je X_n počet aktualizací dosavadního maxima v náhodné
permutaci délky n; μ_n a σ_n jsou jeho střední hodnota a směrodatná odchylka.
Kniha tvrdí existenci a>0 tak, že
`Pr(|(X_n−μ_n)/σ_n| > x) < exp(−a x)` pro všechna n a x.
Smysluplný obor standardizace je n≥2, x≥0. Ani na tomto oboru výrok neplatí.

Pro n=2 je X_n rovnoměrný na {0,1}, takže μ_n=σ_n=1/2 a absolutní
hodnota standardizované veličiny je vždy 1. Pro x=1/2 by tedy muselo platit
`1 < exp(−a/2) < 1`. Záměna ostré nerovnosti za neostrou nepomůže.

Správný tvar je `Pr(|(X_n−μ_n)/σ_n| > x) ≤ C exp(−a x)` s konstantou C.
Přímo pro tento příklad lze vzít a=1/2 a C=2 exp(1/4):

1. X_n má stejné rozdělení jako součet nezávislých Bernoulliho veličin B_j
   s pravděpodobnostmi `Pr(B_j=1)=1/j`, j=2,…,n. Plyne to z rozkladu
   pravděpodobnostní vytvořující funkce na součin `(1−1/j)+z/j`.
2. Označme Y_j=B_j−1/j, v_j=E(Y_j²). Platí |Y_j|≤1, E(Y_j)=0.
   Pro |t|≤1 dává exponenciální řada
   `E exp(tY_j) ≤ 1+v_j ∑_{k≥2}|t|^k/k! ≤ 1+v_j t² ≤ exp(v_j t²)`.
   Prostřední krok používá `∑_{k≥2}1/k!=e−2<1`.
3. Protože σ_n²=∑v_j≥v_2=1/4, lze dosadit t=±1/(2σ_n).
   Nezávislost dává `E exp(±(X_n−μ_n)/(2σ_n)) ≤ exp(1/4)`.
4. Markovova nerovnost pro obě znaménka a součet pravděpodobností dávají
   požadovaný odhad. Platí jednotně pro n≥2 a x≥0.

**Primární citace.** Flajolet–Soria, *Discrete Mathematics* 114 (1993),
159–180, Definition 4.1 na s. 171 výslovně obsahuje konstantu C před
geometricky klesajícím členem. Theorem 4.4 na s. 173 se týká množinové
konstrukce; permutace jsou popsány na s. 174 a 176. Jde o kvalitativní
shodu s opravou, nikoli o zdroj našich explicitních konstant.
[PDF autorů](https://algo.inria.fr/flajolet/Publications/FlSo93.pdf),
lokálně `sources/flajolet-soria1993-gaussian.pdf`; obrázky stran souboru
13–15 a 18. Definition 4.1 a důkaz zde neopravujeme ani nepřebíráme jeho
číselné konstanty. Z našich podkladů nelze tvrdit, že chyba vznikla u autorů článku.

Historická oprava 1. srpna 1997 odstraňuje jen přebytečnou hranatou závorku
na konci odpovědi 13. V ostatních vrstvách nebyla nalezena změna tohoto odhadu.

## V1-C0014: složení pravděpodobnostních funkcí

Pravděpodobnostní vytvořující funkce (PGF) zde znamená řadu
`f(z)=∑_{i≥0}p_i z^i` s p_i≥0 a ∑p_i=1; obdobně `g(z)=∑_{j≥0}q_j z^j`.
Odpověď 17(a) správně tvrdí, že h=g∘f je PGF, ale nesprávně zdůvodňuje
nezápornost koeficientů tím, že jsou polynomy v koeficientech f a g.
Polynom obsahuje jen konečně mnoho členů a proměnných.

Například pro `f(z)=(1+z)/2` je konstantní koeficient
`h_0=∑_{j≥0}q_j 2^(−j)`. Není univerzálním polynomem v koeficientech g:
libovolný takový polynom by používal pouze konečně mnoho q_j. Zvolme N
větší než všechny jejich indexy a porovnejme g(z)=z^(N+1) s g(z)=z^(N+2).
Všechny použité koeficienty g se shodují (jsou nulové), ale h_0 je jednou
2^(−N−1), podruhé 2^(−N−2).

Konkrétní nekonečnou řadu poskytuje g(z)=1/(2−z): potom
`h(z)=2/(3−z)` a `h_0=∑_{j≥0}2^(−2j−1)=2/3`.
Pokud f(0)=0, polynomiální argument funguje pro každý pevný koeficient,
avšak zadání takový předpoklad nemá.

Stačí nahradit „polynomy“ **konvergentními součty součinů**. Přesněji,
označme a_{j,k}=[z^k]f(z)^j. Pak a_{j,k}≥0 a ∑_k a_{j,k}=1. Tudíž
`h_k=∑_j q_j a_{j,k}≥0` a záměna nezáporných součtů dává
`∑_k h_k=∑_j q_j ∑_k a_{j,k}=1`.
Součet definuje h=g(f(z)) také analyticky pro |z|≤1 absolutní konvergencí.
Vzorce pro střední hodnotu a rozptyl v odpovědi zůstávají správné,
jsou-li příslušné druhé momenty konečné. Jde o malou chybu v důkazu,
nikoli o protipříklad k výsledku. Oprava v dostupných erratech nenalezena.

## V1-C0015: dodatek k binomickému odhadu z 25. dubna 2023

Nechť X má binomické rozdělení s n pokusy a pravděpodobností úspěchu p,
q=1−p, ε≥0. Dodatek k odpovědi 21 na s. 502 uvádí jako horní odhad pro
`Pr(X≥n(p+ε))` řetězec `exp(−S(ε)) ≤ exp(−2ε² n)`, platný pro všechna p,
kde `S(ε)=∑_{k≥1}2^(2k−1) ε^(2k)/(2k²−k)`.
Znění je vidět v `images/errata-all1-file013.png` i
`images/errata-err1-file012.png` a souhlasí se zdrojovým TeXem.

**První vada: chybějící n.** Pro n=2 a ε=1/4 platí
`S(1/4)=(1/2)∑_{k≥1}(1/4)^k/[k(2k−1)] ≤ 1/6 < 1/4=2ε² n`.
Proto `exp(−S(ε)) > exp(−2ε² n)`, tedy přesný opak uvedené nerovnosti.
Například p=1/2 splňuje i přirozenou podmínku ε≤q.

**Druhá vada: ani exp(−nS(ε)) není odhad pro všechna p.** Z derivací
nebo integrací geometrické řady plyne pro 0≤ε≤1/2 (v krajním bodě limitou)

`S(ε)=(1/2+ε)ln(1+2ε)+(1/2−ε)ln(1−2ε)`,

kde 0 ln 0 znamená 0. Tedy S(1/2)=ln 2. Pro n=8, p=1/4, ε=1/2 je

`Pr(X≥6) = (28·9+8·3+1)/4^8 = 277/65536 > 256/65536 = 2^(−8)`.

To vyvrací i opravený první odhad na oboru, kde řada konverguje.
Pro ε>1/2 navíc řada diverguje. Takové ε je pro p<1/2 přípustné:
například n=1, p=1/4, ε=2/3 dává pravděpodobnost 1/4, nikoli 0.

**Bezpečná oprava.** Pro všechna 0<p<1 zůstává správný Hoeffdingův odhad
`Pr(X≥n(p+ε)) ≤ exp(−2nε²)`. Silnější prostřední člen lze ponechat pro
`p≥1/2, 0≤ε≤q` a doplnit faktor n:
`Pr(X≥n(p+ε)) ≤ exp(−nS(ε)) ≤ exp(−2nε²)`.

Důkaz obou tvrzení: pro 0≤ε<q položme
`D_p(ε)=(p+ε)ln((p+ε)/p)+(q−ε)ln((q−ε)/q)`.
Minimalizace binomické PGF dává horní odhad exp(−nD_p(ε)).
Platí D_p(0)=D_p'(0)=0 a `D_p''(ε)=1/[(p+ε)(q−ε)]≥4`;
dvojí integrace dává D_p(ε)≥2ε². Je-li navíc p≥1/2, potom
`(p+ε)(q−ε)≤1/4−ε²`, takže `D_p''(ε)≥S''(ε)=1/(1/4−ε²)`.
Opět dvojí integrace dává D_p≥S≥2ε². Krajní bod ε=q se získá limitou.
Pro ε>q je sledovaná událost prázdná; při p=0 nebo 1 se příslušné
deterministické rozdělení posoudí přímo. Prostřední řadu pro ε>1/2
nevyhodnocujeme jako konečný výraz.

Obě vady jsou jedním nálezem k témuž novému vzorci. Starší oprava z roku
1999 doplňuje lineární člen ε v jiné expanzi odpovědi 21 a tuto vadu
neřeší. V podkladech aktuálních k 1. listopadu 2026 pozdější oprava není.

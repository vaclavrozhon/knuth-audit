# D175–D178 — MPR73–76: celý argument a přesně oddělený výklad73

7. listopadu 2026. Přímo prohlédnuto původní zadání p19/file39,
celá odpověď p381/file401, PS p19/file25 a p38/file44.
Definice Eulerových čísel v odkazované §5.1.3 byla zobrazena
ve svazku3 p35–36/file46–47. Převzata pouze tato definice
a ověřená vkládací rekurence, nikoli celý externí oddíl.
Šest vrstev errat a tři TeX zdroje jsou v hashovaném manifestu.
Žádný výčet, numerický běh ani restart.

## 73: všechny hodnoty určené urnovou historií

Položme R_n rovno počtu červených míčků na úrovni n,
takže 1≤R_n≤n+1 a černých je n+2−R_n. Nejprve dokazujeme
klasifikaci martingalů f(R_n,n) vzhledem k celé historii urny.
Pro tento přesný význam je nutná a dostačující rekurence

    (n+2)f(r,n)=r f(r+1,n+1)+(n+2−r)f(r,n+1).        (1)

Nutnost plyne z podmíněných pravděpodobností červeného
a černého přidání; všechny stavy mají kladnou pravděpodobnost.
Dostatečnost plyne stejným výpočtem pro každou historii.
V každém konečném čase jde o konečně mnoho konečných reálných
hodnot, takže integrabilita je automatická. Přechod k vlastní
historii hodnot f je přesně již doložená věžová vlastnost D098.

Definujme kladný normalizační faktor

    B(r,n)=r binom(n+1,r)
          =(n+1)!/((r−1)!(n+1−r)!),
    h(r,n)=f(r,n)/B(r,n).

Pro všechny1≤r≤n+1 platí přesné identity
r B(r+1,n+1)=(n+2)B(r,n) a
(n+2−r)B(r,n+1)=(n+2)B(r,n). Dělením(1) proto dostáváme

    h(r+1,n+1)=h(r,n)−h(r,n+1).                       (2)

Okraj f(1,k)=a_k znamená h(1,k)=q_k=a_k/(k+1).
Indukce podle r v(2) dává pro n≥r−1

    h(r,n)=Σ_{k=0}^{r−1} (−1)^k binom(r−1,k) q_{n+1−r+k}.  (3)

Základ r=1 je q_n. Pro přechod odečteme dvě sumy(3)
s posunutým dolním indexem q; koeficient vnitřního q je
(−1)^k[binom(r−1,k)+binom(r−1,k−1)]
=(−1)^k binom(r,k), konce mají koeficienty1 a(−1)^r.
To je přesně(3) pro(r+1,n+1). Násobení B vrací tištěný
vzorec. Každý index q je mezi0 a n; nejsou potřeba
záporné indexy ani konvergence nekonečného součtu.

Existence: libovolná posloupnost konečných reálných a_k
definuje konečné hodnoty(3); Pascalova identita zpětně dává(2),
a tedy(1). Jednoznačnost: (2) určuje další řadu r+1 ze
známé řady r. Pro každou hledanou hodnotu se provede
jen r−1 takových konečných kroků. Žádná rovnoměrná
omezenost posloupnosti a_k není potřebná.

**Všechny tři příklady ze zadání.** Pro f=r/(n+2) přímý
podmíněný průměr je
[r(r+1)+(n+2−r)r]/((n+2)(n+3))=r/(n+2).
Pro f=r[n=r−1] mají všechny vnitřní uzly i oba jejich
potomci hodnotu0. Na pravém okraji r=n+1 má jen červený
potomek hodnotu n+2 a jeho váha je(n+1)/(n+2), takže
průměr je n+1. Základ n=0 je1. Tento příklad odpovídá
a₀=1,a_k=0 pro k>0 v(3).
Pro f=B(r,n)/2^n je h=2^{-n}; oba pravé členy rovnice
h(r,n)=h(r+1,n+1)+h(r,n+1) jsou2^{-n−1}.
Také přímo q_k=2^{-k} a binomická suma v(3) dává
2^{-(n+1−r)}(1−1/2)^{r−1}=2^{-n}. Všechny příklady platí.

### 73: rozdíl mezi úplnou a vlastní historií — kandidát C047

Výše uvedená klasifikace je úplná právě při podmínění
historií urny. Definice(26) v hlavním textu však zavádí
martingale pomocí vlastní historie Z₀,…,Z_n; širší podmínění
je v(28) výslovně zvláštní vlastnost. Zadání73 říká „for this
model“ a požaduje f(r,n), aniž zde podmínění znovu upřesňuje.
Následující přesný příklad odděluje oba významy. Neslouží
k tvrzení, že standardní urnový výklad musí být chybný.

Položme f(r,0)=f(r,1)=0 na všech platných uzlech a pro n≥2

    f(r,n)=c_n([r=n]−[r=n+1]),    c_n=n(n+1)/6.       (4)

Všechny levé okraje f(1,k) jsou0, stejně jako u identicky
nulové funkce. Na úrovni2 má R₂ hodnoty1,2,3 každou
s pravděpodobností1/3 podle D173, takže Z₂=f(R₂,2)
má hodnoty0,1,−1 a střední hodnotu0. Z₀=Z₁=0; proto
martingalová rovnost vůči vlastní historii platí pro n=0,1.

Pro n≥2 zkontrolujeme všechny stavy. Pokud r≤n−1,
oba následující stavy mají hodnotu0. Při r=n je
podmíněný průměr n c_{n+1}/(n+2)=c_n. Při r=n+1 je

    [(n+1)(−c_{n+1})+c_{n+1}]/(n+2)=−c_n.

Použili jsme c_{n+1}=(n+1)(n+2)/6. Tedy od n=2
je proces martingale i vůči celé urnové historii,
a tím také vůči vlastní historii. Je integrabilní
v každém konečném čase, protože |Z_n|≤c_n.
Spolu s prvními dvěma kroky jde o celý martingale(26).

Přesto není vůči historii urny martingalem v n=1:
při R₁=1 dává následující průměr1/3, při R₁=2 hodnotu−1/3,
zatímco Z₁=0. Vlastní historie tyto dvě stejně pravděpodobné
možnosti nerozlišuje a jejich průměr je0. Funkce(4)
a nulová funkce jsou tak dva různé přirozené martingaly
se stejnými a_k=0.

C047 je pouze interpretační kandidát: při zamýšleném podmínění
celou urnovou historií se uzavře jako kontextová poznámka;
při doslovném použití samotné(26) je jednoznačnost nepravdivá
a stačí doplnit „with respect to the urn history“. Tištěný
vzorec pro harmonickou klasifikaci je sám správný. Dokud
není tento rozsah rozhodnut, celá73 zůstává partial.

## 74: celý Friedmanův diagram a pravděpodobnosti

Při vytažení červeného přidáváme černý míček, a obráceně.
Z uzlu(r,b) je proto přechod do(r,b+1) s vahou r/(r+b)
a do(r+1,b) s vahou b/(r+b). Všechny zobrazené hrany
včetně spodních hran za poslední vykreslenou úroveň jsou:

| Výchozí uzel | Doleva: přidán černý | Doprava: přidán červený |
|---|---:|---:|
| (1,1) | 1/2 | 1/2 |
| (1,2) | 1/3 | 2/3 |
| (2,1) | 2/3 | 1/3 |
| (1,3) | 1/4 | 3/4 |
| (2,2) | 2/4 | 2/4 |
| (3,1) | 3/4 | 1/4 |
| (1,4) | 1/5 | 4/5 |
| (2,3) | 2/5 | 3/5 |
| (3,2) | 3/5 | 2/5 |
| (4,1) | 4/5 | 1/5 |

Všech20štítků souhlasí s tiskem. Děti mění právě odpovídající
souřadnici o1; uzly úrovně n mají r+b=n+2. Oba krajní
přechody i všechny součty vah1 jsou zahrnuty.

**Permutační bijekce.** Na úrovni n použijeme permutace
n+1 prvků a r rovno počtu vzestupných běhů. Základ(1)
má jediný běh a odpovídá kořenu. Počet běhů je počet
sestupů plus1, přesně podle zobrazené definice §5.1.3.

Vložme maximum n+2 do jednoho z n+2 slotů. Počet běhů
se nezmění právě při vložení za konec některého z r běhů:
na konci celé permutace nevznikne sestup; ve starém sestupu
a>b se nahradí jediný sestup novým sestupem n+2>b.
Ostatní sloty přidají jeden sestup: na úplném začátku
vznikne sestup do prvního prvku; uvnitř vzestupu a<b
vznikne místo žádného sestupu jeden. Je tedy r možností
zachovat r a n+2−r=b možností přejít na r+1.
To jsou přesně dvě Friedmanovy pravděpodobnosti.

D171 již dokazuje úplnost Metody1, jediného předchůdce
a rovnoměrnost každé permutace délky n+1 s vahou1/(n+1)!;
tento přesný obecný důkaz přebíráme bez výpočtu.
Označíme-li A(N,k) Eulerovo číslo, tedy počet permutací
N prvků s k sestupy, dostáváme

    P(R_n=r)=A(n+1,r−1)/(n+1)!,    1≤r≤n+1.          (5)

Platí i pro n=0. Jako druhou kontrolu rozložme poslední
přechod: p_{n+1}(r)=[r p_n(r)+(n+3−r)p_n(r−1)]/(n+2).
Vkládací argument dává stejnou rekurenci
A(N,k)=(k+1)A(N−1,k)+(N−k)A(N−1,k−1), přímo ověřenou
i na původní p36 svazku3. Dosazením N=n+2,k=r−1
se(5) řídí přesně touto pravděpodobnostní rekurencí.
Vně přípustného rozsahu jsou pravděpodobnosti i počty0;
kořen je1. Počet všech permutací dává součet vah1.

První čtyři celé řady pravděpodobností jsou

    n=0: (1),
    n=1: (1,1)/2,
    n=2: (1,4,1)/6,
    n=3: (1,11,11,1)/24.

Druhá řada plyne ze dvou kořenových hran. Ve třetí jsou
krajní součiny(1/2)(1/3)=1/6 a prostřední součet dvou
příspěvků(1/2)(2/3)=2/3. Ve čtvrté jsou kraje1/24;
druhý uzel má(2/4)(4/6)+(3/4)(1/6)=11/24 a třetí
stejnou hodnotu výměnou obou barev. Symetrie platí,
protože počáteční stav i pravidlo jsou invariantní
při záměně barev. Nejde o empirický výčet.

**F166.** Tisk však má A(n,r−1)/n!, tedy chybějící +1
v horním parametru i faktoriálu. Pro n=1,r=1 dává1
a pro r=2 dává0, ačkoli oba skutečné výsledky mají1/2.
Pro každý n≥1 by dokonce pravý kraj r=n+1 měl vytištěnou
váhu A(n,n)/n!=0, ale skutečná kladná váha je
(1/2)(1/3)···(1/(n+1))=1/(n+1)!.
Rovnoměrné přiřazení n+1 prvků v následující tištěné
větě je správné a přímo vede k opravě(5).
Chybná je pouze hlavní distribuční formule odpovědi
p381/file401; diagram a zadání nafile39 jsou správné.

## 75: každý krok navrženého martingalu

Zde používejme X_j jako indikátor červeného přidání,
aby R_n=X₀+…+X_n byl, jak odpověď výslovně požaduje,
počet červených míčků; X₀=1. V opačném urnovém modelu
je červené přidání vyvoláno černým tahem. Kontext rovnosti
pro R_n tedy určuje význam indikátoru v této odpovědi;
nesměšujeme jej s indikátorem červeného výběru ze starého
modelu. Není potřeba z toho vytvářet další kandidát.

Pro úplnou historii H_n platí
E(X_{n+1}|H_n)=1−R_n/(n+2). Proto

    E(R_{n+1}|H_n)=R_n+1−R_n/(n+2)
                 =(n+1)R_n/(n+2)+1.

Pravá strana závisí jen na R_n; podmínění ještě jednou
na R_n dává přesně tištěnou mezivětu E(R_{n+1}|R_n).
Navržená veličina Z_n=(n+1)R_n−(n+2)(n+1)/2 splňuje

    E(Z_{n+1}|H_n)
      =(n+2)[(n+1)R_n/(n+2)+1]−(n+3)(n+2)/2
      =(n+1)R_n−(n+2)(n+1)/2=Z_n.

Je adaptovaná a |Z_n|≤n(n+1)/2, protože1≤R_n≤n+1.
Základ Z₀=0 souhlasí. Věžová vlastnost D098 dokazuje
také martingale vzhledem k vlastní historii. Všechny
koeficienty a indexy v odpovědi75 jsou správné.

## 76: celý nekonečný protipříklad a kladná varianta

Vezměme nezávislé férové X,Y∈{−1,1}. Definujme
Z₀=X,Z′₀=Y a Z_n=Z′_n=X+Y pro každé n≥1.
Takto je tištěný dvoučasový příklad výslovně doplněn
na celé posloupnosti. Nezávislost a nulové střední
hodnoty dávají E(Z₁|Z₀)=X=Z₀ a E(Z′₁|Z′₀)=Y=Z′₀.
Pro n≥1 jsou posloupnosti konstantní, takže jejich
martingalová rovnost vůči celým vlastním historiím
platí přímo. Všechny veličiny jsou omezené.

Součet má W₀=X+Y a W_n=2(X+Y) pro n≥1.
Proto E(W₁|W₀)=2W₀. Na událostech X=Y=1 a X=Y=−1,
každé s pravděpodobností1/4, se liší od W₀; celkem
má rozpor pravděpodobnost1/2. Neopíráme protipříklad
o případně degenerované libovolné proměnné s nulovým
průměrem, které by rozpor nemusely dát.

Pokud jsou obě posloupnosti naopak martingaly vzhledem
ke stejné pomocné historii H_n, je jejich součet známý
z H_n a integrabilní a linearita dává
E(Z_{n+1}+Z′_{n+1}|H_n)=Z_n+Z′_n.
Přechod k vlastní historii součtu opět plyne z D098.
Žádná nezávislost se pro tuto kladnou variantu nevyžaduje.

## Bibliografie, errata a stav

[Vydavatel Wiley](https://onlinelibrary.wiley.com/doi/10.1002/cpa.3160020103)
potvrzuje Bernard Friedman, A simple urn model, CPAM2(1),
březen1949, pp59–70. Přímo stažen a zobrazen první list
článku: definuje návrat1+α míčků vybrané barvy a β míčků
opačné barvy. Volba α=0,β=1,a=b=1 je přesně tento model.
Ověřena je definice a bibliografie, nikoli celý článek;
na jeho dalších výsledcích žádný důkaz nezávisí.

Všechny zobrazené shody v šesti erratech a třech TeX
zdrojích byly posouzeny. Sousední známé změny72,
jiné sekce73–76, bibliografické heslo Friedman pro jiný
problém a stránkově posunuté položky nemění73–76.
Pro F166 ani případný rozsah73 není známa použitelná
oprava v uložených vrstvách. Není tvrzen fyzický výtisk,
živá aktualizace, prvenství ani nezávislá revize koordinátora.

74–76 jsou celé posouzeny, s opravou F166 v odpovědi74.
73 má úplný důkaz při urnovém podmínění a přesný opačný
příklad pro slabší definici; interpretační C047 zatím
brání uzavření celé úlohy. Staré mezery a censy zachovány.


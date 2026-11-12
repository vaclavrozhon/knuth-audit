# Úloha 116 — rozpracováno při výslovném zastavení uživatelem

7. listopadu 2026. Poslední konzistentní checkpoint je X0125,
1212 položek. Tato poznámka není uzavřený checkpoint ani důvod
k povýšení stránky. Další kroky vyžadují nové obnovení auditu.

Originály zadání p94/file111 a odpovědí p556–557/file573–574
zobrazeny. Nové sources/proof-file574.pdf a images/proof-file574.png.
Pět vrstev all4a-pre, all4a, err4a, all4f0, err4f0 prohledáno pro
116/557/Dunham/Fridshal/Vikulin/Igarashi; žádná relevantní změna.
Bibliografie této úlohy dosud nebyla nezávisle ověřena.

## Již odvozený obsah, dosud bez finální položkové evidence

(a) Term s j kladnými a k−j zápornými literály dovoluje přesně váhy
[j,n−k+j], všechny dosažitelné. Je implikantem právě při jedničkách
f na celém intervalu. Je prime právě když sousední dosažitelné váhy
j−1 a n−k+j+1 jsou nulové: vypuštění kladného/záporného literálu
rozšíří právě příslušný konec. Neexistující vnější váhy −1,n+1
nedávají omezení. Prázdný term je jediný prime konstanty 1;
konstanta 0 nemá žádný.

Každému maximálnímu běhu jedniček v_0…v_n na vahách [a,a+b]
odpovídají všechny prime termy s a kladnými, b volnými a
c=n−a−b zápornými souřadnicemi. Počet je
W_n(a,b,c)=n!/(a!b!c!). Příspěvky různých běhů se sčítají.
(b) S_{3,4,5,6} pro n=9 má (a,b,c)=(3,3,3), tedy 84·20=1680.

Obecná úplná dynamická rekurence pro (c): F_n(t) je maximum nad
všemi slovy s v_j=0 pro j>t. F_n(−2)=F_n(−1)=0 a

    F_n(t)=max(F_n(t−1),
      max_(0≤k≤t) [C(n,t)C(t,k)+F_n(k−2)]).

První větev je v_t=0; jinak poslední běh jedniček je [k,t],
oddělený od staršího optimálního prefixu nulou na k−1. To dokazuje
obě nerovnosti rekurence i konstrukci svědka. F_n(n) je hledané
maximum. Jde o O(n²) celočíselných aritmetických operací po přípravě
binomických koeficientů; jednotková bitová cena se nepředpokládá.

Jediný malý cílený běh nice 15 vyčíslil pouze deset řádků pro n=9:
verify/symmetric116_n9_dp.py → results/symmetric116-n9-dp.json.
Žádná enumerace funkcí. Výsledky F_9(t), t=0,…,9:

    1,9,72,253,757,1269,1689,1689,1698,1698.

Svědek je přesně 1101111011. JSON uchovává všech 55 kandidátů,
jejich rozklad a vítězné prefixy; běh skončil s exit 0. Znovu jej
nespouštět. Finální vazba důkaz→každá číselná položka ještě nezapsána.

## Další odvozené argumenty k dopracování

V globálním maximu nejsou dvě sousední nuly. U okraje lze při dvou
nulách přidat izolovanou jedničku. Pro vnitřní mezeru mezi běhy
[a,r] a [l,u], l≥r+3, prodloužení levého běhu zvyšuje počet,
pokud n−r>r−a+1; prodloužení pravého dole jej zvyšuje, pokud
l>u−l+1. Kdyby neplatilo ani jedno, 2r≥n−1 a 2l≤n+1,
což odporuje l−r≥3. Ostatní běhy zůstanou oddělené.

Prefixová vytištěná rekurence H_n(m), v_m=1 a m≤n/2, má maximum
v k=ceil(m/2). Připravený důkaz, ještě neuzavřený v evidenci:
posun všech běhů doprava o 1 násobí každý příspěvek c/(a+1)>1,
takže H je v této doméně rostoucí a prefixové maximum končí na
posledním povoleném bitu. Pro k≤ceil(m/2) stačí unimodalita C(m,k)
a monotónnost H. Pro k>ceil(m/2) lze simultánní indukcí použít
H_n(t)<2 C(n,t)C(t,ceil(t/2)). Potřebná mez je

    C(m,ceil(m/2))−C(m,k) ≥ 2 C(k−2,ceil((k−2)/2))  (m≥3).

Pro pevné k je levá strana neklesající při k≤m≤2k−2:
přírůstek centrálního koeficientu je C(m,floor(m/2)+1), alespoň
C(m,k−1). V m=k je rozdíl C(k,ceil(k/2))−1; poměr centrálních
koeficientů pro k a k−2 je ≥3. Základy m=0,1,2 a dokončení
simultánní indukce ještě formálně zapsat. Globální uzavřený vzorec
s n_j=floor((n+j)/3) tím dosud prokázán není.

(d) Připraven vlastní důkaz i ostré asymptotiky bez globálního
uzavřeného vzorce. Je-li a,b,c≥n/4, interval [a,n−c] obsahuje
n/2, takže nejvýše jeden běh může mít všechny tři takové parametry.
Každý jiný má některou souřadnici ≤n/4 a jeho koeficient je
nejvýše rho^n, kde rho=(8/3)(3/2)^(1/4)<3. Plyne to z
C(n,a)2^(n−a)≤(2+t)^n/t^(n/4) pro t=2/3; ostatní souřadnice
symetricky. Tedy maximum je mezi největším vyváženým trinomiálem
a tímto trinomiálem plus (n+1)rho^n. Stirling pro tři vyvážené
části dává 3^(n+3/2)/(2πn)+O(3^n/n²). Přesný Stirlingův
zdroj/rozpis a jednotlivé okraje ještě začlenit.

(e) Pro samotné existenční zadání lze použít m=ceil(n/2)−1,
a přibližně m/2 a funkci s jedničkovými běhy [a,m] a [n−a+1,n].
Její střední prime příspěvek je W_n(a,m−a,n−m), komplement má
střední běh [m+1,n−a] s příspěvkem W_n(m+1,n−a−m−1,a).
Oba mají podíly přibližně (1/4,1/4,1/2), tedy potřebnou velikost
Θ(2^(3n/2)/n). Tento směr ještě rozepsat včetně parit a malých n.
Vytištěná přesná optimalita minima obou počtů, její rekurence,
13 čísel a ostrá paritní konstanta zatím NEJSOU prokázány.

## Přesný další krok

Při novém obnovení převést hotové (a),(b), obecnou DP a certifikát
n=9 do jednotlivých položek od P1213; dopracovat prefixovou indukci
a ostrou asymptotiku. Globální uzavřený vzorec (c) a optimalizační
dodatky (e) ponechat partial, dokud nebude odpovídající argument.
Dosud žádné nové ID X0126 nebylo vytvořeno, žádná stránka povýšena.
Main text zůstává p78/file95 od canalizing, reading p218/file235.

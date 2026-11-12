# Inverze: jednotlivé argumenty úloh16–24

S.20–21, odpovědi594–596. Sazba594/595 znovu zobrazena pouze kvůli
konkrétním vzorcům. Známá errata převzata ze
sources/inversions-errata-review.json. Bez výpočetního běhu a bez nálezu.
Úloha20 zůstává částečná: identita dokázána, požadovaná explicitní
kombinatorická involuce dosud není doložena. Historické atribuce a
bibliografie přeskočeny, nikoli vydávány za matematické důkazy.

## 16: Eulerovy identity a q-exponenciála

Koeficient z^n q^m v ∏_(k≥0)(1−q^k z)^−1 vybírá n nezáporných
částí součtu m, tedy rozklad m na nejvýše n kladných částí. Úloha15,
již dokázaná, dává koeficient z^n rovný1/(q;q)_n, kde
(q;q)_n=∏_(k=1)^n(1−q^k). Ve ∏(1+q^k z) musí být části různé.
Odečtení schodiště n−1,n−2,…,0 je bijekce na slabě klesající
nezáporné části; součet se sníží o binom(n,2). To dokazuje obě identity.

Konečná verze: koeficient x^k v ∏_(j=0)^(r−1)(1+q^j x) je
q^binom(k,2) [r choose k]_q. Indukce plyne z přidání posledního
faktoru a q-Pascalovy identity, kterou ověří společný jmenovatel
(q;q)_k(q;q)_(r−k). Duální koeficient v
∏_(j=0)^r(1−q^j x)^−1 je [n+r choose n]_q: odečítání nejmenší
části, případně její odstranění, dává stejnou rekurenci pro rozklady
do obdélníku n×r. Při r→∞ se obě konečné identity koeficientově
mění na právě dokázané nekonečné identity.

n!_q=(q;q)_n/(1−q)^n a
n!_(q^−1)=q^−binom(n,2)n!_q. Dosazení z(1−q) do první identity
dává první produkt pro exp_q; nahrazení q za q^−1 ve druhé dává
druhý produkt. Pro |q|<1 rovnost Taylorových řad platí v oblasti
|z(1−q)|<1, pro |q|>1 druhý produkt i řada konvergují pro všechna z.
Formální rovnosti se chápou nad racionálními funkcemi generického q.

Koeficient z^n v exp_q(z)exp_(q^−1)(−z) je (1−q)^n krát
Σ_(k=0)^n (−1)^k q^binom(k,2)/((q;q)_k(q;q)_(n−k)). Po vynásobení
(q;q)_n je to konečný součin ∏_(j=0)^(n−1)(1−q^j), jenž pro n>0
obsahuje nulový faktor. Pro n=0 je1. Tím je dokázána i poslední
formální identita v odpovědi16; podmínka n≥0 v sazbě je správná.

## 17: všech24 čtveřic

Použije se již dokázaná MacMahonova bijekce: stabilně seřadíme indexy
podle klesajících q_i a ověříme q_(a_i)=počet sestupů a od i doprava.
Čtveřice v šesti vytištěných řádcích dávají postupně tyto permutace:

1234,2134,3124,4123;
1243,2143,3142,4132;
1324,2314,3214,4213;
1342,2341,3241,4231;
1423,2413,3412,4312;
1432,2431,3421,4321.

Přímé odečtení suffixových počtů sestupů dává ve všech případech p=0.
Permutace jsou různé a je jich4!=24, proto je tabulka úplná.
Jde o ruční kontrolu tištěné tabulky, nikoli hledání enumerací.

## 18: nezávisle zkreslené bity

Pro pevnou hodnotu v je pravděpodobnost Y_i=X_i XOR i=v rovna
p^d q^(n−d), kde d je Hammingova vzdálenost i,v. Přes všechna i
má každá hodnota d násobnost binom(n,d). Nezávislé indikátory výskytu
v proto dávají pro každé v stejné rozdělení počtu výskytů; jeho
střední hodnota jeΣ binom(n,d)p^d q^(n−d)=1. To je přesný význam
uniformity celého souboru uvedený v zadání, nikoli uniformita Y_i.

Nechť F_n je očekávaný počet inverzí, q=1−p, r=p²+q² a M=2^(n−1).
V každé ze dvou polovin vstupních indexů rozhodne nejvyšší bit
o inverzi s pravděpodobností pq; při shodě s pravděpodobností r
rozhodují dolní bity. Obě poloviny přispějí pq M(M−1)+2rF_(n−1).
U dvojice z různých polovin dá nejvyšší bit inverzi s pravděpodobností
p², tedy příspěvek p²M². Při shodě nejvyšších výstupních bitů,
s pravděpodobností2pq, je přes všechny M² dolní vstupní dvojice
očekávaný počet sestupných dolních výstupů M(M−1)/2: součet jejich
pravděpodobností je pro každou dolní hodnotu1. Další příspěvek je
pq M(M−1). Tedy

F_0=0,
F_n=2rF_(n−1)+p²M²+2pq M(M−1).

Rozvinutí rekurence je přesně tištěný konečný součet na594. Dvě
geometrické řady a1−r=2pq dají
F_n=2^(n−1){p(2−p)(2^n−r^n)/(2−r)+r^n−1}.
Krajní p=0/1 se získají přímo, bez dělení1−r; pro p=1/2 vyjde
(2^n−1)²/4, jak také plyne z nezávislých uniformních hodnot.

## 19: Dedekindův součet

Známé erratum mění poslední mod m na mod n. Položme
F_r=floor(mr/n), R_r=mr−nF_r. Nesoudělnost zaručuje, že R_r pro
1≤r<n jsou právě1,…,n−1. Pro i<j je
F_j−F_i−F_(j−i)=[R_j<R_i]. Po sečtení má F_r koeficient
(r−1)−(n−r−1)−(n−r−1)=3r−2n+1, shodný s odpovědí.

ΣF_r=(m−1)(n−1)/2 a ΣrF_r=(m/n)Σr²−(1/n)ΣrR_r, proto
inv=(n−1)(2n−1)/2−(3/n)ΣrR_r.
Definice svazku2, s.83 rovnice16 (sazba workstreams/vol2/images/vol2-p083.png)
má normalizaci σ(m,n,0)=12Σ(r/n−1/2)(R_r/n−1/2), nikoli běžnou
nenormalizovanou s. Roznásobení dává
ΣrR_r/n²=σ/12+(n−1)/4, a tedy
inv=(n−1)(n−2)/4−nσ(m,n,0)/4, správný tištěný výsledek.

## 20: Jacobiho identita; přesná mezera

Označme q=uv. Vyjmutí záporných mocnin z prvního součinu dává
∏_(k=1)^n(1−u^k v^(k−1))(1−u^(k−1)v^k)
=(−1)^n u^binom(n+1,2)v^binom(n,2)
  ∏_(k=−n+1)^n(1−u^(k−1)v^k).
Konečná q-binomická identita z16, se substitucí−u^−n v^(1−n),
a následné přeznačení indexu o n dají
Σ_j [2n choose n+j]_q (−1)^j u^binom(j,2)v^binom(j+1,2).
Původní směs j/k v mezikroku opravilo erratum18.5.2000.

Po vynásobení(q;q)_n je pro pevné j koeficient
(q;q)_(2n)(q;q)_n/((q;q)_(n+j)(q;q)_(n−j))
=1+O(q^(n+1−|j|)). Každý pevný celkový stupeň obsahuje jen konečně
mnoho j, takže koeficientový limit je přesně Jacobiho součin v zadání.
Dosazení u=z,v=z² dává exponent j(3j+1)/2 a po j→−j Eulerovu
pentagonální identitu. Dosazení u=qz,v=q/z dává q^(j²)z^−j;
součet je invariantní vůči j→−j, a má tedy uvedený obvyklý tvar.

Tři produktové faktory odpovídají různým povoleným dílům
(k,k−1),(k−1,k),(k,k); výběr každého nese znaménko−1.
Pravá strana proto opravdu vyjadřuje podepsané počty popsaných
komplexních rozkladů, včetně prázdného při(0,0). Explicitní
involuce párující tyto rozklady ani obsah citovaných kombinatorických
prací však dosud ověřeny nejsou. Úloha20 proto zůstává partial;
otevřená otázka dalších vlastností se nevydává za vyřešenou.

## 21: zásobníkové permutace

Po výstupu a_j z rostoucího vstupu zásobník obsahuje právě menší
prvky, které vystoupí později: všechny už dorazily a větší vložené
prvky musely před a_j opustit vrchol. Jeho velikost je tedy C_j.
Mezi výstupy se vloží r≥0 prvků a jeden odebere, takže
C_(j+1)=C_j+r−1, nutná nerovnost C_j≤C_(j+1)+1.

Obráceně vložme před prvním výstupem C_1+1 prvků a mezi j-tým
a(j+1)-ním výstupem C_(j+1)−C_j+1≥0 prvků. C_n=0 zaručuje
celkem n vložení; nezáporné zbývající velikosti zaručují platnost
operací. Výsledná permutace má právě zadanou tabulku C, která podle
již dokázané úlohy7 určuje permutaci jednoznačně. Podmínka je postačující.

## 22: kruhová tabulka h

V příkladu591826473 vyberou příslušné kruhové intervaly z předchozích
hodnot postupně ∅,∅,{5},{9,1},{5},{9,1,8,2},{5,6},{9,1,8,2},
{5,9,8,6,4,7}. Počty001214246 souhlasí; součet20 je2+4+6+8,
součet poloh sestupů.

Vždy0≤h_j<j. Při zpětné rekonstrukci zůstávají hodnoty a_1,…,a_j.
Pohyb proti směru hodin od mezery po a_(j+1) potká nejprve právě
h_j přeživších hodnot na oblouku(a_j,a_(j+1)] a pak a_j.
Počáteční mezera před1 odpovídá koncovému intervalu(a_n,n].
Odebrání(h_j+1)-ní hodnoty proto rekonstruuje přesně a_j; zároveň
funguje pro libovolnou tabulku v uvedených mezích, tedy jde o bijekci.

Pevné a_i je započítáno při průchodech oblouků
a_i→a_(i+1)→…→a_n→n přes svou hodnotu. Počet těchto průchodů
je počet oběhů kruhu, tedy počet sestupů od polohy i doprava.
První oblouk startovní hodnotu nepočítá, poslední končí nejvýše n;
nevzniká dodatečný oběh. Sečtení přes i dá každému sestupu na j
právě j příspěvků. ProtoΣh_j=ind(a).

## 23: ruská ruleta

Nechť a je pořadí úmrtí a b jeho duál. Před j-tou smrtí zbývá
r=n−j+1 lidí. Po zrcadlení hodnot a obrácení pořadí je počet
neúspěšných pokusů před prvním dosažením a_j právě h_r(b), podle
kruhového intervalu z22. Další plné oběhy přidávají r pokusů.
Proto příspěvek j-té fáze jeΣ_(k≥0)p_j q_j^(h_r+rk)
=p_j q_j^h_r/(1−q_j^r), pro0<p_j≤1.
Součin nezávislých fází je vzorec v odpovědi, s již známou opravou
posledního k_1 na k_n.

U31425 jsou nejmenší počty neúspěchů2,2,1,1,0; duál14253 má
h=01122. Násobky5,4,3,2,1 souhlasí. Chybu k_2 místo k_4 ve
čtvrté fázi opravilo erratum31.3.2019.
Při konstantním p=1−q je jmenovatel∏_(r=1)^n(1−q^r)/(1−q)=G_n(q)
a čitatel q^ind(b). Pro0<p<1 je minimum právě u maximálního indexu,
tedy u sestupného b i a. Při p=1 má každý neidentický pořádek nulovou
pravděpodobnost; sestupné pořadí je nadále jedním z minim, nikoli
jedinečným minimem. Odpověď jedinečnost netvrdí.

## 24: zobecněný index

Položme m=n−1, d_i=[a_i>t(a_(i+1))] pro1≤i<m a d_0=d_m=0.
Pro1≤j≤m dejme e_j=[t(a_j)<n], e_n=0. Protože a_i<n,
d_(j−1)≤e_j. Značka c_j=e_j−d_(j−1) je0 nebo1 a je1 právě
tehdy, když vložení n před a_j přidá nový zobecněný sestup.

Vložením n na j se příspěvek sestupů změní o
j e_j−(j−1)d_(j−1)+Σ_(i=j)^(m−1)d_i.
Nové započtené inverze s n přidajíΣ_(l=j)^m(1−e_l).
Při C_j=Σ_(l=j)^n c_l se součet zjednoduší na
Δ(j)=n−j+j c_j−C_j.

Seřaďme místa s c_j=1 sestupně j_1>…>j_k; potom C_(j_r)=r
a Δ(j_r)=n−r. Ostatní místa seřaďme j_n>…>j_(k+1).
Počet těchto míst alespoň j_r je n−r+1, a tedy také zde
Δ(j_r)=n−r. Krajní místo j_n=n má přírůstek0. Všechna vložení
proto dávají právě0,…,n−1; indukce násobí GF faktorem1+…+z^(n−1).
Počáteční n=0/1 je zřejmé, takže GF je G_n.

Při t(j)=j je druhý člen definice nulový a první obyčejný index.
Při t(j)≥n je první nulový a druhý počítá všechny inverze.
Odstavec tvrdící n! různých statistik a jeho pokračování na596
byly celé odstraněny známým erratem22.9.2024; nepoužíváme je
jako další tvrzení platného textu ani jako nový nález.

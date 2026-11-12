# MPR107–108: každá konstrukce a všechny okraje couplingů

7. listopadu 2026. Celá zadání p22/file42 a odpovědi p386/file406
zobrazeny; totéž v autorském PS11.9.2019 p22/file28 a p43/file49.
Všech šest vrstev errat a tři TeX zdroje bez použitelné opravy.
Z D092 se přebírá pouze výslovný diskrétní model s konečnými či
spočetnými atomy a nezápornými vahami, nikoli dosud chybějící
důkaz některé podčásti. Žádný nový běh nebo opakovaný výpočet.

##107, celý úvod a dvouatomové příklady

V diskrétním prostoru určuje zákon X jeho všechny váhy P(X=x).
Rovnost těchto vah zachovává pravděpodobnost každé množiny hodnot
X, rozdělení každé funkce X a všechny existující momenty. Totéž
platí samostatně pro Y. To je přesný rozsah tištěného tvrzení
o závěrech týkajících se X nebo Y; nová společná konstrukce
nestanovuje jejich nezávislost, pokud ji zvlášť nezvolíme.

Pro Ω=Ω′×Ω″ položíme w_(α,β)=p′_α p″_β. Součet nezáporných
vah je(Σ_α p′_α)(Σ_β p″_β)=1 i pro spočetné prostory.
Definujeme X(α,β)=X′(α),Y(α,β)=Y″(β). Součet po β dává
původní X-marginálu, součet po α původní Y-marginálu. Produkty
uvedené v zadání tedy opravdu definují coupling a jeho atomy.

Pro oba binární prostory jsou p,q∈[0,1]. Produktová tabulka

```
       ♣           ♠
Q      pq          p(1−q)
K      (1−p)q      (1−p)(1−q)
```

je nezáporná, její řádkové součty jsou p,1−p a sloupcové q,1−q.
Pro p<q má alternativní tabulka nenulové možné položky
Q♣:p,K♣:q−p,K♠:1−q. Pro p>q lze použít
Q♣:q,Q♠:p−q,K♠:1−p, čímž se skutečně vynechá K♣, jak
uvádí text. Pro p=q stačí Q♣:p,K♠:1−p. V každém případě
jsou všechny váhy nezáporné a oba součty marginál přesně odpovídají
zadání. Nulové atomy lze vypustit nebo ponechat s nulovou vahou;
všechny výroky o dvou/třech/čtyřech atomech jsou horní meze,
nikoli tvrzení minimálního počtu při p0 nebo p1.

##107(a): obě tištěné větve a úplná volba označení

Označme atomy prvního prostoru řádky1,2,3 a druhého sloupci1,2,3.
Coupling je nezáporná matice s řádkovými součty p_i a sloupcovými
q_j; každý její kladný prvek je jeden atom. Jsou-li po přeznačení
p1≤q1 a p2≤q2, použijeme

```
[ p1      0       0 ]
[ 0       p2      0 ]
[ q1−p1   q2−p2   q3].
```

To jsou právě první tištěné pěti váhy. Poslední řádek má součet
q1+q2+q3−p1−p2=1−p1−p2=p3; ostatní řádky a všechny sloupce
sedí přímo. Všechny položky jsou nezáporné.

Pro úplnost rozepíšeme redukci na případy, včetně možnosti zaměnit
role obou prostorů. Seřaďme každou trojici vzestupně. Dvě různá
p lze přiřadit ke dvěma různým q s p≤q právě tehdy, když
p1≤q2 a p2≤q3. Dostatečnost: přiřadíme p1→q2,p2→q3.
Nutnost: menší ze dvou použitých q je nejvýše q2 a druhé
p je nejméně p2. Pokud p1>q2, vyměníme oba prostory: nyní
q1≤q2<p1≤p2 zajišťuje první konstrukci pro opačné řádky/sloupce;
transpozice výsledku je požadovaný coupling. Výměna prostorů
nic nemění na samotné úloze.

V ostatní větvi neúspěchu musí p2>q3. Pak i p3>q3 a
p2+p3>q2+q3, takže z rovnosti celkových součtů p1<q1.
Dostáváme právě tištěné pořadí

```
p1<q1≤q2≤q3<p2≤p3.
```

Nyní použijeme matici

```
[ p1       0             0 ]
[ q1−p1   p1+p2−q1      0 ]
[ 0        p3−q3         q3].
```

Její možné kladné váhy jsou právě druhý tištěný seznam.
q1−p1>0,p1+p2−q1≥0 (protože p2>q3≥q1),p3−q3>0 a
p1,q3≥0. Řádkové součty jsou p1,p2,p3; první a třetí
sloupec mají součet q1,q3, druhý
p1+p2−q1+p3−q3=1−q1−q3=q2. Součet všech vah je1.
Tím jsou všechny tištěné přeznačovací větve úplně doloženy.
Při rovnostech a nulových pravděpodobnostech funguje první
konstrukce nebo transpozice; výsledný počet atomů je nejvýše5.

##107(b,c): přesné čtyři atomy a ostrá dolní mez pěti

Pro(b) řádky mají součty(1,5,6)/12, sloupce(2,3,7)/12.
Konkrétní coupling je

```
(1/12)[0 0 1; 2 3 0; 0 0 6].
```

Čtyři kladné váhy jsou1/12,2/12,3/12,6/12, přesně odpověď.
První marginála sčítá1,2+3,6; druhá2,3,1+6. Není potřebná
žádná enumerace couplingů.

Pro(c) zvolíme tištěné p=(1,4,4)/9,q=(3,3,3)/9. Každý
jednotlivý atom couplingu přispívá do jednoho sloupce, a proto
má váhu nejvýše3/9. Každý z řádků s hmotností4/9 tedy
potřebuje nejméně dva atomy; zbývající kladný řádek alespoň
jeden. Proto je nutných nejméně2+2+1=5 atomů, i kdyby se
více atomů promítalo na stejnou dvojici hodnot. Pět také stačí:

```
(1/9)[1 0 0; 2 2 0; 0 1 3].
```

Obě marginály jsou přesně předepsané. Tím je skutečně dokázána
nemožnost méně než pěti, nikoli pouze neúspěch určité konstrukce.

##108: všechny celočíselné podpory, včetně obou nekonečných konců

Položme p_k=P′(X=k),q_k=P″(Y=k) pro k∈Z a
F(n)=Σ_(k≤n)p_k,H(n)=Σ_(k≤n)q_k. Předpoklad ocasů je
ekvivalentní F(n)≥H(n) pro každé celé n: použijeme
P(X≥n+1)=1−F(n) a stejnou identitu pro Y.
Obě kumulativní funkce jsou neklesající, mají limity0 v−∞
a1 v+∞, protože všechny nezáporné váhy se sčítají na1.

Vezměme intervaly I_n=[F(n−1),F(n)) a J_m=[H(m−1),H(m)).
Mají délky p_n,q_m. Pro každý u∈(0,1) existuje nejmenší celé
n s F(n)>u: existence plyne z limity1, dolní omezenost z limity0.
Toto n je jednoznačné a u∈I_n. Analogicky pro J_m. Prázdné
intervaly odpovídají nulovým vahám. Tím je rozklad na intervaly
validní i při podpůře neomezené směrem dolů, kdy bod0 nemusí
ležet v žádném neprázdném I_n. Jednotlivý nulově dlouhý koncový
bod nebudeme používat jako atom nového diskrétního prostoru.

Přesná realizace tištěného společného rozdělení intervalu je
Ω={(n,m):w_nm>0}, kde

```
w_nm=max(0,min(F(n),H(m))−max(F(n−1),H(m−1))).
```

Jde o délku I_n∩J_m. Ω je konečná či spočetná a atomy mají
kladné váhy, nikoli neurčitě definované kvantily v nule. Pro pevné
n je konečný součet po m=−M,…,M přesně délka
I_n∩[H(−M−1),H(M)). Jak M roste, krajní hodnoty konvergují
k0 a1 a délka konverguje k p_n. Proto Σ_m w_nm=p_n.
Obráceným argumentem Σ_n w_nm=q_m. Nezáporné součty pak dávají
Σ_(n,m)w_nm=Σ_n p_n=1. Celá konstrukce tedy zůstává v autorově
diskrétním modelu, bez nutnosti zavádět spojitou náhodnou proměnnou.

Definujeme X(n,m)=n,Y(n,m)=m. Předchozí součty dokazují obě
přesné marginály a odpovídají intervalové definici z odpovědi.
Pokud n>m, potom n−1≥m a

```
F(n−1)≥F(m)≥H(m).
```

Levý kraj I_n je tedy nejméně pravý kraj J_m; jejich průnik
má nulovou délku a w_nm=0. V Ω taková dvojice vůbec není.
Proto X≤Y platí pro každý atom, jak zadání požaduje, nikoli
jen po nevysvětleném zanedbání výjimek. Když jsou některé původní
hmotnosti nulové, příslušné řádky či sloupce se prostě nevyskytují;
jejich marginální pravděpodobnost zůstává0. Rovné distribuční
funkce, konstantní proměnné i jednostranné podpory jsou zahrnuty.

Kniha tedy může popisovat atomy jako společné subintervaly
vymezené oběma sadami kumulativních součtů. Pokud se chce ponechat
i izolovaný nulově dlouhý koncový atom, lze jej vypustit bez změny
prostoru s kladnou hmotností; konstrukce výše už jej neobsahuje.
Každá použitá hodnota X,Y je konečné celé číslo.

Celé107(a–c) včetně úvodu a celé108 jsou checked. Bez nového
nálezu, kandidáta, bibliografické výjimky nebo matematického běhu.

# Pomocný bod k §1.3.3-31: uniformní ocas

Tento zápis je cílená pomoc koordinátorovi, nikoli převzetí auditu
cv. 31. Vychází z jeho odvození v
`workstreams/vol1/notes/permutation-remaining-working.md`, oddíl 31.
Uzavírá jediný chybějící přechod od hustoty pro pevný počet kroků
k průměru celkového počtu pevných bodů. Nejde o nový nález.

## Parametr, který odstraní n z iterace

Fixujme celé m>1, položme q=m−1, α=m/q>1 a r=1/α=q/m<1.
Pro permutaci velikosti n a hledaný pevný bod j, kde 1≤j≤n, začíná
zpětná iterace v x_0=mj a dokud x_i>n, počítá

```
x_(i+1) = floor((m(x_i−n)−1)/q).
```

Pevný bod po právě k krocích znamená x_k=j. Protože m>1 a j≥1,
musí být k≥1. Zaveďme h=n−j≥0 a y_i=mn−x_i. Pak y_0=mh a
elementární úprava podlahy dává

```
y_(i+1) = T(y_i),
T(y) = floor(my/q)+1.
```

Tato iterace už **nezávisí na n**. Nutná podmínka pevného bodu je

```
T^k(mh) = qn+h.                                  (1)
```

Pro pevné k a h určuje (1) nejvýše jedno celé n a potom i j=n−h.
Zde pro horní odhad nemusíme dokazovat obrácenou implikaci ani
kontrolovat podmínky předchozího nezastavení. Každý skutečný pevný
bod se injektivně zobrazí na svůj h.

## Počet možných h a počet možných k

Pro každé nezáporné celé y platí T(y)≥αy. Je-li n≤N a (1) platí,
pak

```
qn+h ≥ α^k mh,
h ≤ qN/(mα^k−1) ≤ Nα^(−k) = Nr^k.               (2)
```

Poslední nerovnost je ekvivalentní α^k≥1. Označme A_k(N) počet
skutečných dvojic (n,j) s 1≤j≤n≤N, které dávají pevný bod po právě
k krocích. Injektivita podle h a (2) dávají

```
A_k(N) ≤ floor(Nr^k)+1 ≤ Nr^k+1.                 (3)
```

Hodnota h=0 (tedy j=n) se nesmí vynechat: právě její možné zahrnutí
v počtu celých h=0,…,floor(Nr^k) vysvětluje přídavek +1 pro každé k.

Navíc pro celočíselné y má zlomek my/q zlomkovou část nejvýše
(q−1)/q. Tedy T(y)≥αy+1/q. Iterováním a použitím
(1/q)/(α−1)=1 získáme

```
T^k(y) ≥ α^k(y+1)−1.
```

Na skutečném pevném bodu je y_k=mn−j≤mN, zatímco y_0≥0.
Proto α^k−1≤mN, čili

```
k ≤ L_N := floor(log_α(mN+1)).                    (4)
```

Jde o analytický odhad; není nutné numericky vyhodnocovat logaritmus
v implementaci. m je v celém tvrzení pevné.

## Uniformní odhad a záměna limity

Sečtení (3) pro K<k≤L_N dává přímo

```
(1/N) sum_{k>K} A_k(N)
  ≤ r^(K+1)/(1−r) + L_N/N
  = m r^(K+1) + O_m(log N/N).                    (5)
```

Proto

```
lim_{K→∞} limsup_{N→∞} (1/N) sum_{k>K} A_k(N)=0.
```

Koordinátor už pro každé pevné k≥1 odvodil limitní hustotu

```
lim_{N→∞} A_k(N)/N
  = q^k/[m^(k+1)−q^k] =: d_k.
```

Číslo d_k je nezáporné a d_k=r^k/(m−r^k)≤r^k/q, takže jeho řada
konverguje. Pro konečný součet k≤K lze limitu zaměnit automaticky;
(5) potom dovolí nechat K→∞. Je-li F(n) počet pevných bodů Josefovy
permutace při parametru m, máme tak rigorózně

```
lim_{N→∞} (1/N) sum_{n=1}^N F(n)
  = sum_{k=1}^∞ (m−1)^k/[m^(k+1)−(m−1)^k].
```

Pro k≥1 navíc r^k/m < d_k < r^k/q. Sečtením geometrických řad
dostaneme ostré meze pro tento průměr: (m−1)/m < sum d_k < 1.

Výhoda parametru h=n−j je přesná: místo až q^k reziduálních tříd
počítáme jedno celé h pro každý skutečný pevný bod a pevné k.
Zaokrouhlovací chyba je proto pouze 1 na k, a celkem O_m(log N),
což stačí pro všechna pevná m>1, nejen pro m=2.

# §3.4.2-19: vážené vzorkování podle priorit

Kontrola 1. listopadu 2026. Doplněná úloha19 byla vizuálně přečtena
v all2-prepre, souborová strana9, a porovnána s ostatními vrstvami errat.
Níže je úplný vlastní důkaz všech čtyř částí. Žádný nový nález.

## Definice a součinový odhad

Máme N záznamů s kladnými váhami w_i. Nezávislé veličiny U_i jsou
rovnoměrné na [0,1); **priorita** q_i=U_i/w_i určuje pořadí výběru.
Pro 2<=n<=N označíme r n-tou nejmenší prioritu a ponecháme n−1 záznamů
s q_i<r. Odhad váhy je

```text
W_i(r) = max(w_i,1/r), pokud q_i<r; jinak 0.
```

Zápis W_i(s+) znamená stejný předpis s q_i<=s. S pravděpodobností1 jsou
všechny priority kladné a navzájem různé; rovnosti na nulové množině
výsledky očekávání nemění. E označuje střední hodnotu.

Nechť I je libovolná množina k různých indexů, kde 1<=k<n. Podmíníme
všemi prioritami mimo I a jako s označíme (n−k)-tou nejmenší z nich.
Tato priorita existuje, protože n<=N. Platí skoro jistě identita

```text
product_{i in I} W_i(r) = product_{i in I} W_i(s+).             (1)
```

Jsou-li všechny priority z I menší než s, má s mezi všemi prioritami
pořadí n a obě strany jsou stejné. Jinak je pravá strana0. Kdyby levá
byla kladná, všechny k priorit z I by byly mezi prvními n−1, takže
n-tá celková priorita by opět musela být (n−k)-tá z ostatních, tedy s;
to by ovšem vyžadovalo všechny priority z I menší než s. Spor.

Při tomto podmínění je s pevné a priority z I zůstávají nezávislé.
Pro každý i∈I máme

```text
Pr(q_i<=s) = min(w_i*s,1),
E[W_i(s+) | priority mimo I] = min(w_i*s,1)*max(w_i,1/s) = w_i.
```

Podmíněné očekávání součinu(1) je proto součin w_i. Nezápornost dovoluje
použít Tonelliho větu (záměnu integrálů nezáporných funkcí), aniž bychom
předem předpokládali konečné momenty. Po odstranění podmínění dostaneme

```text
E[product_{i in I} W_i(r)] = product_{i in I} w_i.             (2)
```

To současně dokazuje(a) pro prvních k indexů a(b) pro libovolné různé
indexy. Nestrannost jednotlivých odhadů je případ k=1.

## Rozptyly a podmínka n>2

Rozptyl Var(X)=E[(X−E X)^2] vyžaduje pro obvyklou konečnou identitu
konečný druhý moment. Pro i nechť s_i je (n−1)-tá nejmenší priorita
ostatních záznamů. Stejné podmínění dává

```text
E[W_i(r)^2 | priority mimo i] = w_i*max(w_i,1/s_i).             (3)
```

Pro malé t>0 je Pr(s_i<=t)<=C*t^(n−1), kde C je součet součinů vah
přes všechny (n−1)-prvkové podmnožiny ostatních indexů. Důvod: pokud
s_i<=t, alespoň taková podmnožina má všechny priority nejvýše t;
sjednocovací mez a nezávislost dávají uvedený součet. Integrací ocasu
Pr(1/s_i>x)<=C/x^(n−1) pro velká x vidíme, že E[1/s_i]<∞, pokud n>2.
Rovnice(3) pak zaručuje konečné druhé momenty.

Pro n>2 lze v(2) použít k=2, tedy E[W_i W_j]=w_i w_j. Kovariance,
definovaná jako E[W_i W_j]−E[W_i]E[W_j], je0 pro i!=j. Rozvinutí
čtverce tudíž dokazuje(c): rozptyl odhadu součtu libovolné skupiny
záznamů je součtem jejich jednotlivých rozptylů.

Podmínka n>2 má skutečný význam: při N=n=2 a jednotkových vahách je
E[W_1^2]=integral_0^1 (1/s) ds=∞. Pro kontrolní případ N=n=3,
w_i=1, je r maximum tří rovnoměrných veličin a odhad celkové váhy2/r;
jeho střední hodnota je3, druhý moment12 a rozptyl3. Obecně pro
jednotkové váhy a n>=3 dává beta integrál
E[W_i^2]=(N−1)/(n−2), Var(W_i)=(N−n+1)/(n−2).

## Jeden průchod

Pro(d) udržujeme **maximovou haldu**, stromovou datovou strukturu,
jejíž kořen obsahuje největší uloženou prioritu. Uchovává n nejmenších
priorit dosud čtených záznamů spolu s jejich váhami a identifikátory.
Po naplnění haldy nový záznam s menší prioritou nahradí kořen a halda
se opraví; ostatní se zahodí. Indukce přímo zachovává uvedený invariant.
Po konci vstupu je kořen r a ostatních n−1 záznamů požadovaný vzorek.
Paměť je O(n), jeden krok nejvýše O(log n); nevydáváme tuto mez za
O(1) na přijatý záznam. Kratší soubor lze poznat před naplněním haldy.

## Primární zdroj a přesný rozsah četby

[Preprint Duffield–Lund–Thorup](https://arxiv.org/pdf/cs/0509026),
arXiv:cs/0509026v1, je uložen s SHA-256 v `sources/`. Přečteny strany1–8,
zejména lemma1 a oddíly2.3–2.5; strana7 také vizuálně. Rovnice(8) v§2.4
je stejný obecný součinový moment. Autoři mají opačnou konvenci:
priorita w_i/alpha_i, k největších priorit a práh tau=(k+1)-tá největší.
Pro převod na knihu je k=n−1 a tau=1/r. Nezaměňovat jejich n (počet
záznamů) s naším n (velikost vzorku plus1).

Jde o preprint z2005, nikoli ověřenou sazbu JACM2007. Publikační údaje
JACM54(6), article32, potvrzuje autorův katalog a institucionální záznam,
ale přímé stažení autorovy kopie časopiseckého PDF neuspělo (vypršelý
certifikát, potéHTTP406); metadata zachovávají tento rozdíl. Vlastní
stručný důkaz výše nepotřebuje přebírat všechny mezikroky preprintu.

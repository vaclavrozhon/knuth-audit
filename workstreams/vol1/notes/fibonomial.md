# §1.2.8-29–30: fibonomické koeficienty a mocniny

Audit 1. listopadu 2026. Zadání s. 85 a odpověď s. 494
zobrazeny. Používáme F_n,phi,psi z `fibonacci-basic.md`.
Pro n,k>=0 definujme

```text
B(n,k)=product_(j=1)^k F_(n−k+j)/F_j.
```

Prázdný součin B(n,0)=1; pro k>n je v čitateli F_0,
tedy B(n,k)=0. Pro záporné k nastavíme B(n,k)=0 jako
okrajovou konvenci rekurence. Všechny jmenovatele F_j
jsou při j>=1 kladné.

## Celočíselnost a tabulka

Pro 1<=k<n jsou podíly
B(n−1,k)/B(n,k)=F_(n−k)/F_n a
B(n−1,k−1)/B(n,k)=F_k/F_n. Sčítací identita (F2)
předchozí poznámky proto dává

```text
B(n,k)=F_(k−1)B(n−1,k)+F_(n−k+1)B(n−1,k−1).            (B1)
```

Pro k=0,n platí rovnost přímo; při k=0 se použije F_(−1)=1.
Indukce podle n z řádku B(0,0)=1 dokazuje celočíselnost.
Není třeba ji odvozovat z číselného krácení zlomků.
Řádky n=0,...,6 jsou přesně

```text
1
1 1
1 1 1
1 2 2 1
1 3 6 3 1
1 5 15 15 5 1
1 8 40 60 40 8 1
```

Doplnění nul do čtverce 0<=n,k<=6 odpovídá změně 2023.
Původní hodnocení úlohy 29 je v obrazu M23, nikoli M25 z OCR.

## Obecný důkaz rekurence mocnin

Položme q=psi/phi=−phi^(−2). Gaussův q-binomický
koeficient značíme [m choose k]_q a definujeme jej jako
product_(j=1)^k (1−q^(m−k+j))/(1−q^j). Jelikož |q|<1,
žádný jmenovatel není nulový. Z uzavřeného vzorce F_j
plyne

```text
B(m,k)=phi^(k(m−k)) [m choose k]_q.                    (B2)
```

Konečná q-binomická věta, dokázaná v binomickém bloku,
je polynomiální identita
product_(j=0)^(m−1)(1+u q^j)
=sum_(r=0)^m q^(r(r−1)/2)[m choose r]_q u^r.
Nevyužíváme zde žádnou problematickou nekonečnou řadu.
Dosadíme A=phi^(m−1), použijeme souměrnost Gaussových
koeficientů a dostaneme

```text
product_(j=0)^(m−1)(t−phi^(m−1−j)psi^j)
 = sum_(k=0)^m B(m,k)(−1)^ceil((m−k)/2)t^k.             (B3)
```

Podrobně: při r=m−k je mocnina phi rovna
r(m−1)−r(r−1)=k(m−k); znaménko je
(−1)^(r+r(r−1)/2)=(−1)^ceil(r/2).
Tím je ověřen i snadno přehlédnutelný zaokrouhlovací
znak v exponentu původní sazby.

Pro m>=1 je F_n^(m−1) binomickým rozvojem (F3)
lineární kombinace m geometrických posloupností
(lambda_j^n), kde lambda_j=phi^(m−1−j)psi^j,
j=0,...,m−1. Posun n na n+1 násobí každou z nich
příslušným lambda_j. Polynomiální identita (B3) proto
anuluje všechny složky, a tedy

```text
sum_(k=0)^m B(m,k)(−1)^ceil((m−k)/2)F_(n+k)^(m−1)=0.    (B4)
```

Platí pro všechna celá n a m>=1. Při m=1 je nultá
mocnina konstantní polynom 1, včetně F_0^0; rovnost
je pak 1−1=0. Pro m=3 vychází přesně
F_n²−2F_(n+1)²−2F_(n+2)²+F_(n+3)²=0.
Pro d-té mocniny má tedy rekurence řád d+1,
jak říká úvod zadání. Hodnocení úlohy 30 je **M38**.

Indukční důkaz v knize lze rovněž přímo zkontrolovat:
B(m,k)F_k=F_m B(m−1,k−1),
B(m,k)F_(m−k)=F_m B(m−1,k).
Posun k v první sumě a parita
k+ceil((m−k)/2)−m−ceil((m−1−k)/2)
dávají řádky (a),(b), v druhém případě sudý rozdíl.
Dále (−1)^k F_(m−k)=F_(k−1)F_m−F_k F_(m−1)
vede na (c), protože F_m!=0. Identita
F_(n+k)=F_(k−1)F_n+F_k F_(n+1) pak dává (d).
Nulové koeficienty mimo konečný rozsah se vynechávají.

Historické citace Lucas 1878, Jarden 1966 a Riordan
1962 jsou samostatná pramenná kontrola.

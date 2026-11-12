# V2-C0020: nesprávná koncentrace při zaokrouhlení počtu intervalů

**Confirmed**, 1.11.2026. §3.3.2-20, odpověď str.564, poslední
odstavec pokračující na565. Třetí vydání, první dotisk1997.
Zdroj `images/vol2-p564.png` přečten včetně zvětšení sazby: skutečně
je zde **m=ceil(1/delta)**. Počáteční pracovní přepis na podlahu byl
chybný a byl opraven; níže uvedený protipříklad používá strop.

## Tvrzení a problém

Kniha volí delta=alpha (log(n)/n)^(1/3), M=alpha³/2+1/3 a
m=ceil(1/delta). Tvrdí, že při rozdělení na m stejně pravděpodobných
částí všechny četnosti leží mezi n delta(1−delta) a
n delta(1+delta) s pravděpodobností alespoň1−O(n^(−M)).

Skutečná střední četnost je n/m, nikoli n delta. Zaokrouhlení může
posunout dolní mez téměř na střední hodnotu. Následující posloupnost
velikostí vzorku dává pravděpodobnost porušení dolní meze v jediné
buňce blížící se1/2, což uvedené tvrzení vyvrací.

## Obecný protipříklad se stálým alpha=1

Pro každé dostatečně velké celé k nechť x_k>e je jediné řešení
x_k/log(x_k)=k³; jednoznačnost plyne z růstu x/log(x) pro x>e.
Zvolme celé n_k=ceil(x_k). Je-li náhodou x_k celé, vezměme x_k+1;
v obou případech 0<n_k−x_k<=1. Položme
delta_k=(log(n_k)/n_k)^(1/3).

Funkce (log(x)/x)^(1/3) je pro x>e klesající. Derivací a větou
o střední hodnotě dostaneme

```text
delta_k = 1/k − O(1/(k n_k)),   delta_k < 1/k,
m_k = ceil(1/delta_k) = k+1
```

pro všechna dostatečně velká k. Dále n_k ~ 3 k³ log(k).
Jedna z m_k buněk má četnost X_k s binomickým rozdělením
Bin(n_k,p_k), p_k=1/(k+1). Dolní mez je
L_k=n_k delta_k(1−delta_k). Rozdíl skutečného průměru a dolní meze je

```text
n_k p_k − L_k
 = n_k [1/(k+1)−1/k+1/k²] + O(1/k)
 = n_k/[k²(k+1)] + O(1/k).
```

Směrodatná odchylka X_k je sqrt(n_k p_k(1−p_k)) ~ sqrt(n_k/k).
Po dělení touto odchylkou je rozdíl
O(sqrt(log(k))/k) -> 0. Současně n_k p_k(1−p_k) -> infinity.
Centrální limitní věta pro binomické veličiny s těmito parametry
proto dává

```text
Pr(X_k < L_k) -> 1/2.
```

Lze ji použít i pro tuto trojúhelníkovou posloupnost: součet třetích
absolutních momentů centrovaných Bernoulliho členů dělený třetí
mocninou celkové směrodatné odchylky je nejvýše
1/sqrt(n_k p_k(1−p_k)), a tedy splňuje Ljapunovovu podmínku.
Zaokrouhlení reálné meze L_k na celé číslo v limitě nehraje roli.

Událost, že všechny buňky vyhoví, má tudíž limsup nejvýše1/2.
Tištěná dolní mez1−O(n_k^(−5/6)) by naopak směřovala k1.
Jde o rozpor pro pevné alpha, nikoli o změnu konstanty s n.
Tentýž důkaz funguje pro každé pevné alpha>0: stačí definovat x_k
rovnicí x_k/log(x_k)=(alpha k)³. Ani volba velkého alpha tedy
problém zaokrouhlení neodstraní.

## Přesně certifikované ilustrace

`verify_serial_correlation.py` našel následující celá n. Správné
zaokrouhlení x_k a hodnoty m jsou ověřeny racionálními intervaly
pro log(n), odvozenými z řady log(y)=2 atanh((y−1)/(y+1)).
Také delta má racionální dolní a horní mez; výpočet nestojí jen
na plovoucí čárce. Poslední sloupec je informativní desetinný výstup.

| k | n_k | m_k | (n_k p_k−L_k)/sd(X_k) |
|---:|---:|---:|---:|
| 10 | 9 119 | 11 | 0.302836104508 |
| 100 | 16 626 509 | 101 | 0.040776366529 |
| 1000 | 23 897 019 585 | 1001 | 0.004888488360 |

Důkaz je obecná argumentace výše; tři ilustrace ji nenahrazují.

## Hlavní závěr úlohy lze opravit

Pro rovnoměrné vstupy má jmenovatel D tvar
D/n²=(sum U_i²)/n−((sum U_i)/n)². Přímá koncentrace obou průměrů
omezených veličin dává

```text
D/n² = 1/12 + O(sqrt(log(n)/n))
```

mimo událost pravděpodobnosti O(n^(−B)), kde libovolného pevného B
dosáhneme dostatečnou konstantou v odchylce. Na dobré události lze
invertovat D². Na špatné použijeme (U_0−U_1)^4/D²<=1, protože
D=sum_(i<j)(U_i−U_j)². Jelikož E(U_0−U_1)^4=1/15, dostáváme

```text
E[(U_0−U_1)^4/D²]
 = (48/5)n^(−4) [1+O(sqrt(log(n)/n))] + O(n^(−B)).
```

Pro B dostatečně velké tento odhad dokazuje i tištěný hlavní člen
a jeho slabší zbytek. Vzorec pro rozptyl v úloze20 a asymptotická
oprava24/(5n²) v textu73 tedy zůstávají správné.

## Errata a stav

Všechny vrstvy `all2-prepre`, `all2-pre`, `all2`, `err2` a aktuální
TeX prohledány1.11.2026: str.564–565, odpověď20, intervalové četnosti
a související formulace. Oprava nenalezena; jediná změna na564 se
týká bibliografického odkazu odpovědi15. Nejnovější fyzický tisk ani
prvenství neověřeny. Náhled vydavatele tuto stranu neobsahuje.
Draft `reports/C0020-correlation-concentration-draft.txt` neodeslán.

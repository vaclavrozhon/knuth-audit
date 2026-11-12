# D108 — celá MPR5: délka hry a střídání vítěze

6. listopadu 2026. Celé zadání13/file33 a odpověď371/file391
přímo zobrazeny; rovněž autorův Pre-Fascicle5A,13/file19
a28/file34. Kontrola pokrývá(a,b,c), všechny tištěné
mezikroky a čísla, nezávislost, normalizaci a okraje.
E119 je známé upřesnění zadání5(b), již zapracované v4B.

## Model a část(a), včetně nejmenší možné hodnoty

Skóre A₁,…,A_n jsou nezávislá se stejným rozdělením;
totéž platí pro B₁,…,B_n a obě celé rodiny jsou nezávislé.
Proto jsou také dvojice(A_i,B_i), jejich rozdíly a události
A_i>B_i nezávislé pro různá i. Výhra Alice je ostrá nerovnost
součtů; rovnost se za její výhru nepočítá.

Tištěný příklad má A_i=1001 s pravděpodobností99/100,
jinak0, a B_i=1000 vždy. V jedné hře je tedy P₁=.99.
Po1000 kolech Bob dosáhne1 000 000. Alice ho překoná,
pokud všech1000 jejích skóre je1001, a tehdy má1 001 000.
Pokud se objeví alespoň jedna nula, má nejvýše
999·1001=999 999 a prohraje. Proto přesně

```
P₁₀₀₀=(99/100)^1000
       ∈[0.000043171247410658250988,
          0.000043171247410658250989]
       <0.0001.
```

Obě krajní desetinná čísla jsou rigorózní vnější meze,
nikoli zaokrouhlení používané jako důkaz nerovnosti.
Přímo celočíselně bylo porovnáno99^1000·10000<100^1000.

Pro libovolný model splňující předpoklady platí inkluze
{A₁>B₁,…,A_n>B_n}⊆{Σ_i(A_i−B_i)>0}. Pravděpodobnost
levé události je nezávislostí P₁^n. Tím je přesně dokázána
tištěná obecná dolní mez P_n≥P₁^n. Uvedený příklad ji
pro n=1000 dosahuje, a proto dává nejmenší možnou hodnotu
P₁₀₀₀ při P₁=.99. Nejde jen o nalezení nějakého příkladu.

## Část(b): rozdělení a všechny nekonečné součty

Definujme, přesně podle zadání, pro k≥0

```
m_k=2^{k³}, n_k=2^{k²+k}, w_k=2^{−k²},
D=Σ_{k≥0}w_k, q_k=w_k/D.
```

Máme3/2<D<2: první dvě váhy jsou1 a1/2 a další jsou
kladné; zároveň k²≥k a pro k≥2 je nerovnost ostrá,
takže součet je menší nežΣ2^{−k}=2. D je konečné a kladné,
q_k>0 aΣq_k=1. Čísla m_k jsou kladná a přísně rostoucí,
počínaje m₀=1, m₁=2.

Položme E=Σ_{j≥0}q_{2j}; zde je E označením konkrétní
pravděpodobnosti, nikoli operátorem střední hodnoty.
Rozdělení A má kladné hodnoty m₀,m₂,… s těmito sudými
pravděpodobnostmi a zbývající hmotnost1−E v0.
Nezávislé B má kladné hodnoty m₁,m₃,… s lichými
pravděpodobnostmi a zbývající hmotnost E v0. Každé
rozdělení je tedy normalizované; žádné skóre není nekonečné.
Předpoklad konečné střední hodnoty zadání nemá a důkaz jej
nepoužívá. Ve skutečnosti kladné členy m_k q_k v každé
paritě nerostou k0, takže příslušné střední hodnoty jsou
nekonečné; to uvedeným pravděpodobnostním tvrzením nevadí.

Je-li A=m_{2k}, vyhraje právě při B=0 nebo B=m_{2j+1}
s j<k. Tyto případy jsou disjunktní a nezávislost dává

```
P(A>B)=Σ_{k≥0}q_{2k}(E+Σ_{j=0}^{k−1}q_{2j+1}).
```

Prázdný vnitřní součet pro k=0 je0. Obdobně při
B=m_{2k+1} nastane výhra B právě proti A=0 nebo
A=m_{2j},j≤k, tedy

```
P(A<B)=Σ_{k≥0}q_{2k+1}(1−E+Σ_{j=0}^{k}q_{2j}).
```

Sudé a liché kladné hodnoty se nikdy nerovnají, protože
m_k jsou přísně rostoucí. Jedinou remízou je proto A=B=0,
jejíž pravděpodobnost je(1−E)E. Naproti tomu AB>0
znamená, že obě skóre jsou kladná, s pravděpodobností
E(1−E). Jde o dvě různé události se stejnou pravděpodobností,
nikoli o jejich ztotožnění.

Všechny součty mají nezáporné členy a jsou součty
disjunktních událostí, takže jejich uspořádání nepotřebuje
žádný nedoložený předpoklad absolutní konvergence.
Tři případy A>B,A<B,A=B jsou úplné a disjunktní,
tedy jejich pravděpodobnosti mají součet1.

## Každé tištěné desetinné číslo, s odhadem zbytku

Pro kontrolu čísel není třeba simulovat hry ani vytvářet
velká m_k. Poměr po sobě jdoucích vah je
w_{j+1}/w_j=2^{−(2j+1)}. Za libovolným K≥0 proto platí

```
Σ_{j>K} w_j
 ≤ τ_K=2^{−(K+1)²}/(1−2^{−(2K+3)}).
```

Jde o geometrickou majorantu: první vynechaná váha je
2^{−(K+1)²} a všechny další poměry jsou nejvýše
2^{−(2K+3)}. Položme D_L=Σ_{j=0}^K w_j,
D_U=D_L+τ_K. Pak D_L≤D≤D_U. Je-li E_L součet
ponechaných sudých vah, máme

```
E_L/D_U ≤ E ≤ (E_L+τ_K)/D_L.
```

Pro párové pravděpodobnosti lze použít dvě nezávislé
pomocné indexové veličiny J,K s pravděpodobnostmi q_j,q_k:
A=m_J pro sudé J, jinak0; B=m_K pro liché K, jinak0.
Tento model má právě požadované rozdělení a nezávislost.
Každá událost je tedy součtem některých párů vah w_j w_k
děleným D². Pokud N_L je součet jejích ponechaných párů,
všechny vynechané páry dohromady mají hmotnost nejvýše
D_U²−D_L². Proto rigorózně

```
N_L/D_U² ≤ P ≤ (N_L+D_U²−D_L²)/D_L².
```

`verify_mpr005_probabilities.py` počítá jen13 vah (K=12)
a169 párů, všechny jako přesné zlomky. Ověřuje také, že
tři základní součty ponechaných párů dávají přesně D_L².
Výsledné vnější intervaly jsou:

| Veličina | Dolní mez | Horní mez | Tisk |
|---|---|---|---|
|D|1.564468413605938579334729|1.564468413605938579334730|1.56447|
|E|0.679154177587149979592571|0.679154177587149979592572|0.67915|
|P(A>B)|0.474021336606877382545717|0.474021336606877382545718|.47402|
|P(A<B)|0.308074882740050689537975|0.308074882740050689537976|.30807|
|P(A=B)|0.217903780653071927916306|0.217903780653071927916307|.21790|
|P(AB>0)|0.217903780653071927916306|0.217903780653071927916307|.21790|

Každý interval leží celý uvnitř intervalu zaokrouhlení
vytištěného čísla; totéž bylo přesně ověřeno pro .000043
v(a). Certifikát ukládá i původní racionální meze a meze
zaokrouhlení, nikoli jen desetinné zobrazení.
Celá kontrola trvala0.001923s s nice15, žádné staré výsledky
ani rozsáhlé součty nebyly přepočítávány.

## Část(c): všechny mezikroky a uniformní chyba

Označme G_k událost, že během prvních n_k kol nikdo
nedosáhne skóre většího než m_k. V jednom kole má A
takovou hodnotu s pravděpodobností součtu příslušných
sudých q_j,j>k, zatímco B se součtem lichých. Sjednocení
přes obě rodiny a přes všech n_k kol proto dává

```
P(G_k^c) ≤ n_k Σ_{j>k}q_j
 ≤ 2^{k²+k} 2^{−(k+1)²}/[D(1−2^{−(2k+3)})]
 = 2^{−k−1}/[D(1−2^{−(2k+3)})]
 ≤ (4/7)2^{−k}.
```

Poslední nerovnost používá D>1 a k≥0. Není zapotřebí
nadbytečný faktor2: dvě parity dohromady tvoří právě
jeden celý součetΣ_{j>k}q_j. Nezávislost není pro tento
horní odhad sjednocení potřeba.

Označme H_k událost, že se během těchto kol objeví
přesně hodnota m_k. Ta je možná pouze u jednoho hráče,
podle parity k, v každém jeho kole s pravděpodobností q_k.
Nezávislost mezi koly proto dává přesně

```
P(H_k^c)=(1−q_k)^{n_k}
 < exp(−q_k n_k)=exp(−2^k/D).
```

Máme0<q_k<1, takže ostrá nerovnost plyne z1−u<e^{−u}
pro u>0. Například rozdíl e^{−u}−1+u je v0 nulový
a jeho derivace1−e^{−u} je pro u>0 kladná.

Zbývá ověřit tištěnou dominanci skóre. Pro k≥2 je

```
log₂(m_k/(n_k m_{k−1}))
 = k³−(k²+k)−(k−1)³
 = 2k²−4k+1=2(k−1)²−1 ≥1>0.
```

Tedy m_k>n_k m_{k−1}, přesně pro rozsah k>1 použitý
v odpovědi. Pro k=1 tato pomocná nerovnost neplatí,
ale konečný počáteční úsek není součástí asymptotického
důkazu a není zde neprávem zahrnut.

Na G_k∩H_k hráč s paritou k získá alespoň jednou m_k,
a má tedy celkové nezáporné skóre alespoň m_k. Druhý
hráč nemůže získat m_k a na G_k nemá ani nic vyššího;
každé jeho skóre je tedy nejvýše m_{k−1}. Jeho součet
je nejvýše n_k m_{k−1}<m_k. Na této události tak Alice
striktně vyhraje pro sudé k a striktně prohraje pro liché k.
Žádná remíza zde není vynechána.

Sjednocením obou chyb dostáváme pro všechna k≥2 konkrétní
horní mez

```
|P_{n_k}−[k sudé]|
 ≤ (4/7)2^{−k}+exp(−2^k/D) →0.
```

To dokazuje celé požadované(c). Současně opravňuje tištěné
„quite surely … as k→∞“. Parametrem tohoto asymptotického
výroku je k. Pro každé pevné R>0 a celé h>R platí
e^{ak}≥(ak)^h/h! pro a>0, tedy e^{−ak}=O(k^{−R}).
První chybový člen je tohoto tvaru s a=ln2. Pro druhý
použijeme2^k≥k a exp(−2^k/D)≤exp(−k/D), takže i on je
superpolynomiálně malý v k. Netvrdíme odlišný odhad
O(n_k^{−R}), který by z uvedeného důkazu neplynul.

## Errata, bibliografie a rozsah

E119 eviduje známé upřesnění z8.2.2021: ve Fascicle5,
str.13, úloha5(b), je rozdělení A a B rozepsáno samostatně
a výslovně nezávisle. Původní TeX a sazba all4f5/file3
byly přímo přečteny; právě toto znění již obsahuje4B.
Starší autorův PS má stručnější formulaci. Jeho matematické
vzorce a odpověď jsou stejné; známé upřesnění není nový nález.
V ostatních pěti místních vrstvách errat nebyla nalezena
další oprava MPR5. Sousední změny nejsou duplicitně evidovány.

Historická atribuce T. M. Coverovi a citovaný článek
The American Statistician43(1989),277–278 jsou výslovně
bibliograficky vynechány. Všechny potřebné matematické
argumenty, čísla a okraje mají samostatné důkazy výše.
D108 uzavírá celou MPR5 i odpověď. File33 zůstává partial
kvůli úlohám6–13 a file391 kvůli odpovědi6 a dalším
neuzavřeným rozsahům. Žádný nový nález, kandidát nebo restart.

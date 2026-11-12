# V2-C0025: dva nesprávné členy Eulerovy derivace

**Confirmed**, 1.11.2026. §3.3.2-30, str.569, druhý zobrazený
vzorec. Třetí vydání, první dotisk1997; původní sazba i zvětšení
`images/vol2-p569.png` přečteny. Zahrnuty všechny opravy2021,
včetně globálního přechodu na B_1=+1/2 na728/731.

## Definice a správný vzorec

Kniha definuje f(z)=−m log(z)−sum_(k=1)^n log(1−z^k)
a Eulerovu derivaci theta=z d/dz. Pro rho>0 je theta při
z=exp(−rho) operátorem−d/d rho. Současná Bernoulliho konvence
je x/(1−exp(−x))=sum B_l x^l/l!, tedy B_1=+1/2.
Při0<rho<2pi/n platí konvergentní rozvoj

```text
f(exp(−rho)) = m rho−n log(rho)−log(n!)
              −sum_(k=1)^n sum_(l>=1) B_l (−k)^l rho^l/(l l!).
```

Proto pro j>=1 musí být

```text
theta^j f(exp(−rho))
 = −m[j=1] + (j−1)! n/rho^j
   − (−1)^j sum_(k=1)^n sum_(l>=j)
       (l)_j B_l (−k)^l rho^(l−j)/(l l!).
```

Zápis(l)_j je klesající součin, [j=1] je indikátor rovnosti.
Kniha má **j!** místo(j−1)! a před posledním součtem **plus**
místo minus. Změna k^l na(−k)^l z22.3.2021 je správná při
současném přechodu konvence B_1; obě zde popsané vady ale ponechává.

## Nejkratší kontroly

U n=1 není druhá Eulerova derivace závislá na m a přesně platí

```text
theta² f(exp(−rho)) = exp(−rho)/(1−exp(−rho))²
                    = 1/rho²−1/12+rho²/240+O(rho^4).
```

Tištěný rozvoj po všech opravách2021 dává
2/rho²+1/12−rho²/240+O(rho^4). Liší se už vedoucí pól,
nikoli zanedbaný zbytek. Pro n=m=1,rho=1 je skutečná hodnota
A=1/[4sinh²(1/2)]<1, kdežto tištěná nekonečná řada má hodnotu
3−A>2. Jde tedy i o konkrétní konečný vstup splňující rho=n/m.

Znaménko se projeví i při j=1, kdy jsou oba faktoriály stejné:
pro n=m=1 je správný konstantní člen−3/2, tištěný−1/2.
Program nezávisle derivuje racionální funkci v z a porovnal
Laurentovy rozvoje pro j=1..6; všechny potvrzují obě opravy.

Hlavní asymptotické vzorce pro p_n a q_n jsou správné;
vlastní důkaz a numerický certifikát má `partition-certificate.md`.
Všechny vrstvy errat a TeX prohledány1.11.2026. Opravy1999,
2004,2021 prohlédnuty také obrazově; tyto dva členy neopravují.
Novější fyzický tisk a prvenství neověřeny, draft neodeslán.

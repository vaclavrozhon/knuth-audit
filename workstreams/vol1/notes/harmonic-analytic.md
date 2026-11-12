# §1.2.7: analytické odhady a necelé argumenty

Audit 1. listopadu 2026. Zobrazeny s. 75–79 a odpovědi
492–493. Značíme `H_n=sum_{k=1}^n 1/k` a
`H_n^(r)=sum_{k=1}^n k^(−r)` pro celé n>=0. Eulerova
konstanta je `gamma=lim_{n→infinity}(H_n−log n)`;
existence byla dokázána v `harmonic-finite.md`, části
„Definice a růst“. Symbol O(g(n)) znamená absolutní
omezení konstantou krát g(n) pro dost velké n.

## Zeta funkce a (5)–(7)

Pro reálné r>1 je `zeta(r)=sum_{k>=1} k^(−r)` konečná
podle blokové meze (H2) v konečné poznámce. Integrální
porovnání klesající funkce x^(−r) dává pro n>=1

```text
0 < zeta(r)−H_n^(r) < n^(1−r)/(r−1).                   (A1)
```

To zpřesňuje větu, že pro r>=2 je zbytek rychle malý.

Bernoulliho polynomy B_j(t) definujeme formální řadou
`s exp(ts)/(exp(s)−1)=sum_{j>=0} B_j(t)s^j/j!`;
Bernoulliho čísla jsou B_j=B_j(0). Jejich odvození
Fourierovými koeficienty je v `gamma-functions.md`, části
„Divergence Stirlingovy řady a historické prameny“:
pro nenulové celé l je koeficient B_j(t) roven
`−j!/(2pi i l)^j`, získaný opakovanou integrací po částech.
Pro sudé j>=2 je řada absolutně konvergentní. Dosazení
t=0 tedy dává

```text
zeta(2m)=|B_(2m)|(2pi)^(2m)/(2(2m)!),   m>=1.            (A2)
```

Koeficientová rekurence z definice dává
B_2=1/6,B_4=−1/30,B_6=1/42,B_8=−1/30. V (A2)
tak vyjdou přesně pi²/6,pi⁴/90,pi⁶/945,pi⁸/9450
z (7). Historická atribuce Eulerovi vyžaduje pramen,
nikoli nový numerický výpočet těchto hodnot.

## Přesný integrál a zbytek v (3)

Pro t>0 položme `phi(t)=1/t−1/(exp(t)−1)`.
Funkce je kladná, u 0 má limitu 1/2 a na [0,infinity)
je omezená. Pro celé n>=1 definujme
`D_n=integral_0^infinity exp(−nt)phi(t)dt`.
Integrál absolutně konverguje a D_n→0.
Odečtení dvou sousedních integrálů dává

```text
D_n−D_(n+1)=log((n+1)/n)−1/(n+1).
```

Pro první člen lze použít
`(exp(−nt)−exp(−(n+1)t))/t=integral_n^(n+1) exp(−ut)du`
a prohodit nezáporné integrály. Druhý člen je integrál
exp(−(n+1)t). Stejný rozdíl má H_n−log n−gamma,
který také jde k 0. Teleskopování proto dokazuje

```text
H_n−log n−gamma = D_n.                                 (A3)
```

Eulerův sinusový součin z `gamma-functions.md`, části
„Součiny a reflexe“, po dosazení z=it/(2pi) a
logaritmickém derivování dává

```text
1/(exp(t)−1)−1/t+1/2
 = 2t sum_{l>=1} 1/(t²+4pi² l²).                       (A4)
```

Derivace součinu je oprávněna lokální stejnoměrnou
konvergencí řady logaritmických derivací; pro reálné
t>0 žádný faktor nemá nulu. Pro a>0 platí přesně

```text
1/(a²+t²)=1/a²−t²/a⁴+t⁴/(a⁴(a²+t²)).
```

Dosazením a=2pi l do (A4), s (A2) pro m=1,2,3,
dostáváme

```text
phi(t)=1/2−t/12+t³/720−R(t),
0<R(t)<t⁵/30240.                                      (A5)
```

Integrace proti exp(−nt) v (A3), s
`integral_0^infinity exp(−nt)t^j dt=j!/n^(j+1)`, dává

```text
H_n=log n+gamma+1/(2n)−1/(12n²)+1/(120n⁴)−epsilon,
0<epsilon<1/(252n⁶), n>=1.                             (A6)
```

To je přesně (3). Dodatek z 19. března 2025 správně
uvádí n>0; při n=0 by pravá strana neměla smysl.
Stejné rozvinutí 1/(a²+t²) do libovolné konečné délky
ukazuje obecný odhad: zbytek po Bernoulliho členech má
znaménko prvního vynechaného členu a je menší než jeho
absolutní hodnota. Tento důkaz ospravedlňuje i konečné
rozvoje použité v číselném certifikátu této sekce.

## Úlohy 5,8,12: číselné údaje a asymptotická velikost

Úloha 5 žádá 15 desetinných míst H_10000. Přesný součet
racionálních čísel lze zaokrouhlit bez binárních floatů;
výsledek v odpovědi je 9.787606036044382. Výpočet a
intervaly jsou zaznamenány samostatným kontrolním programem.
Jeho úspěšný výsledek `results/harmonic.json` dává
`9.787606036044382264178477904851 < H_10000
 < 9.787606036044382264178477904852`.
Eulerových deset míst 0.5772156649... lze certifikovat
z (A6), nebo z delšího Bernoulliho rozvoje s výslovným
zbytkem. Porovnání celé tabulky v dodatku A tím ještě
není prohlášeno za dokončené.

V úloze 8 porovnáváme (n+1)H_n−n s log(n!). Rozvoj (A6)
a již ověřený Stirlingův odhad dávají

```text
sum_{k=1}^n H_k−log(n!)
 = gamma n + (1/2)log n + c + O(1/n),
c=gamma+1/2−(1/2)log(2pi)=0.158277... .                  (A7)
```

Tedy knižní hodnota .158 je správná na uvedená tři
desetinná místa. Další člen je 1/(3n), pokud použijeme
o jeden řád přesnější zbytky. Odpověď netvrdí uniformní
malou absolutní chybu pro všechna malá n.

Úloha 12 nepotřebuje počítat tisící mocninu pi.
Integrální porovnání ocasu od 3 dává

```text
0<zeta(1000)−1 < 2^(−1000)(1+2/999) < 10^(−301).         (A8)
```

Poslední nerovnost je přesná celočíselná kontrola
`1001*10^301 < 999*2^1000`. Hodnota 1 je tím bezpochyby
správná při zaokrouhlení na požadovaných 100 míst a má
301 shodných úvodních číslic za desetinnou tečkou.
To je význam tvrzení odpovědi o více než 300 místech;
netvrdíme, že se 1 získá nejbližším zaokrouhlením na
301 míst (to by požadovalo chybu menší než 0.5*10^−301).

## Úlohy 23–24: digama a necelý argument

Gama funkce Gamma byla definována a její nekonečný součin
dokázán v `gamma-functions.md`, (G1). Logaritmická derivace
je `psi(z)=Gamma'(z)/Gamma(z)`, zvaná digama funkce,
definovaná mimo póly Gamma. Z Gamma(z+1)=z Gamma(z) plyne
`psi(z+1)=psi(z)+1/z`.

Součin (G1) znamená, přesně jak tvrdí úloha 24,

```text
1/Gamma(z)=z exp(gamma z)
             product_{k>=1}(1+z/k)exp(−z/k).             (A9)
```

Pro z na kompaktní množině a k>2|z| mají logaritmy
faktorů odhad O(|z|²/k²); součin proto konverguje
lokálně stejnoměrně v celé komplexní rovině. V bodech
0,−1,−2,... má výsledek nulu. Nejde o zákaz nulových
hodnot konvergentního součinu. U z=0 je ocas součinu
1+O(z²), a proto
`Gamma(1+z)=exp(−gamma z)(1+O(z²))`; dostáváme
Gamma'(1)=−gamma, použitou v úloze 23.

Přirozené meromorfní pokračování harmonických čísel je

```text
H_z=gamma+psi(z+1)
   =sum_{k>=1}(1/k−1/(k+z)),                            (A10)
```

pro z mimo záporná celá čísla. Druhá rovnost plyne
logaritmickým derivováním (A9); její řada konverguje
lokálně stejnoměrně mimo póly díky členu z/(k(k+z)).
Rekurence a H_0=0 vracejí původní H_n na nezáporných
celých argumentech. Nejde o tvrzení, že je to jediné
možné pokračování hodnot posloupnosti bez dalších podmínek.

Poznámka odpovědi 24 o vyšších řádech je rovněž správná:
pro reálné r>1 a reálné z>−1 lze definovat
`H_z^(r)=sum_{k>=1}(k^(−r)−(k+z)^(−r))`.
Rozdíl je O(k^(−r−1)) a pro celé z=n>=0 součet
teleskopuje na H_n^(r). Pro komplexní z se zvolí
větev mocnin na oblasti vyhýbající se jejich řezům;
při celém r není větvová nejednoznačnost a zbývají póly.
Původní tvrzení o konvergenci **součinu** (A9) pro všechna
komplexní z se nepřenáší jako tvrzení o absenci těchto pólů.

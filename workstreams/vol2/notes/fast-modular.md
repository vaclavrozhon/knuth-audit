# §4.3.3B: modulární metoda a úlohy 6/7

Kontrola 2.11.2026. Vizuálně přečteny strany302–305, zadání316 a
odpovědi633. Kontrolovány všechny čtyři vrstvy errat. Matematiku
tohoto bloku uzavíráme s hraniční opravou C0103; historické srovnání
obecné Schönhageovy varianty z roku1966 patří do samostatného kontextu.

## Šest modulů a úloha 6

Definujme q_0=1, q_(k+1)=3q_k−1 a p_k=18q_k+8. Indukcí
`q_k=(3^k+1)/2`, `p_k=3^(k+2)+17`. Exponenty modulů jsou
`e_i=6q_k+d_i`, kde d_i postupně nabývá hodnot −1,1,2,3,5,7;
moduly jsou m_i=2^e_i−1. Krok k>0 násobí dvě p_k-bitová čísla.

Každý společný prvočíselný dělitel dvou exponentů dělí také rozdíl
jejich d_i. Všech patnáct rozdílů má prvočíselné dělitele jen2,3,5.
Pouze exponent s d=2 je sudý a pouze ten s d=3 je dělitelný3.
Modulo5 mají dvě shodná d právě hodnoty2 a7. Oba příslušné exponenty
by byly dělitelné5 pouze pro q_k≡3; posloupnost q_k modulo5 však
cyklí 1,2,0,4. Tím je dokázána párová nesoudělnost exponentů.
Identita `gcd(2^a−1,2^b−1)=2^gcd(a,b)−1` z §4.3.2 pak dává
párovou nesoudělnost modulů.

Součet exponentů je 36q_k+17=2p_k+1. Každý exponent je nejméně5,
a proto

```
product_i m_i
 = 2^(2p_k+1) product_i(1−2^(−e_i))
 >= 2^(2p_k+1) (1−sum_i 2^(−e_i))
 >= 2^(2p_k+1) * 13/16 > 2^(2p_k).
```

Součin vstupů je tedy jednoznačně určen svými šesti zbytky.
Každý zbytek má nejvýše `6q_k+7=18q_(k−1)+1<p_(k−1)` bitů,
takže rekurzivní násobení má požadovanou menší délku. Převod do
zbytků a redukce součinů stojí O(p_k): počet modulů i poměr jejich
délky k délce operandu jsou omezené konstantou.

## Inverzní násobení s pravidelnými bity

Pro nesoudělná 0<e<f položme M=2^f−1 a b=e^(−1) mod f,
1<=b<f. Označme

```
c[h] = sum_(0<=j<h) 2^(je) mod M.
```

Protože be≡1 modulo f a 2^f≡1 modulo M, platí
`(2^e−1)c[b] ≡ 2^(be)−1 ≡ 1 (mod M)`.
Číslo c[b] je tedy požadovaná inverze modulu 2^e−1.

Rovnice (32) staví současně součin u*c[2^k] a součin u*c[B_k],
kde B_k je celé číslo určené nejnižšími k+1 bity čísla b. Stavové
proměnné a_k,d_k jsou příslušné exponenty posunů modulo f. Přesně:

```
a_k = 2^k e mod f,        u_k = u c[2^k] mod M,
d_k = B_k e mod f,        v_k = u c[B_k] mod M.
```

Identita `c[A+B] ≡ c[A]+2^(Ae)c[B] (mod M)` dokazuje krok pro v_k;
její případ A=B=2^(k−1) dokazuje krok pro u_k. Aktualizace v_k
používá **nové** u_k a **staré** d_(k−1), jak je správně vytištěno.
Při inicializaci musí být u normalizované modulo M; přesný nedostatek
deklarovaného vstupního rozsahu je samostatný
[C0103](C0103-modular-zero-endpoint.md).

Násobení 2^a modulo M je cyklický posun f bitů, se záměnou reprezentace
samých jedniček za0. Stojí O(f). Jeden krok čtyř posloupností má tedy
cenu O(f), kroků je O(log b)=O(log f). Inverzi b lze nalézt rozšířeným
Eukleidovým algoritmem v O((log f)^3) jednoduchých bitových operací,
což je O(f log f). I postupné zkoušení b stačí, pokud se be modulo f
aktualizuje **přičtením e**; není třeba každý pokus od začátku násobit.
Výsledná cena je O(f log f), bez předpokladu rychlého obecného násobení
f-bitových čísel.

## Rekonstrukce a úloha 7

Rovnice (28) je Garnerův převod již dokázaný v §4.3.2. Zde každé
násobení inverzí c_ij provedeme předchozím postupem, přičemž rozdíl
předem zredukujeme modulo m_j. Je jich binom(r,2). Hornerova
rekonstrukce (29) má r−1 sčítání a r−1 násobení; násobení m_j
se provede posunem a odečtením. Postupně rostoucí délky jsou nejvýše
r e_r, takže celá konverze stojí O(r^2 e_r log e_r).

Pro šest modulů je r konstantní a e_r=O(p_k). Celková rekurence je
`t_k <= 6t_(k−1)+c k 3^k` s vhodnou konstantou c a upraveným
konečným počátkem. Po dělení6^k a sečtení dostaneme

```
t_k/6^k <= t_0+c sum_(j=1..k) j/2^j <= t_0+2c.
```

Pro nejmenší k s n<=p_k máme při k>0
`p_k=3p_(k−1)−34<3n`. Doplnění na tabulkovou délku tedy stojí jen
konstantní faktor a dostáváme `T(n)=O(n^(log_3 6))`.
Zde `log_3 6≈1.63093`: desetinný horní odhad musí být1.631,
nikoli1.63. To je již zveřejněné erratum ze7.2.1999.

Další známé opravy: nesoudělnost e,f (7.2.2000) a na str.304
`w_j<m_j`, `w'_1=w_1`, počet operací r−1 (6.10.2025).

## Reprodukce

`verify_fast_modular.py` má samostatné checkpointy pro speciální
inverzní součiny, parametry, Garnerovu rekonstrukci a celou rekurzivní
metodu. Orákulem je nezávislé obecné násobení Pythonu, případně jeho
modulární inverze; ve zkoumané rekonstrukci se dlouhé násobení
inverzí nahrazuje přímo rovnicí (32). Výsledky a dokončení běhu jsou
zaznamenány v `results/fast-modular.json` a `RUN_STATE.json`.

Běh31517 skončil exit0; všechny čtyři checkpointy prošly. Celkem46132
malých inverzních součinů,108 velkých do16384 bitů,224 celých kontrol
invariantů,4324 rekonstrukcí a72 plných násobení do6578 bitů
(345252 základních součinů,69036 rekonstrukcí). Tabulky ověřeny
v15 úrovních; obecné důkazy výše nejsou nahrazeny konečnými testy.

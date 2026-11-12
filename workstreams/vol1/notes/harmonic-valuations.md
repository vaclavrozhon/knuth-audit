# §1.2.7-17–19: přesná dělitelnost harmonických čísel

Audit 1. listopadu 2026. Zobrazeno zadání s. 78 a odpovědi
s. 492. Pro prvočíslo p a nenulové racionální q definujeme
`v_p(q)` jako exponent p v čitateli minus exponent p ve
jmenovateli po krácení. Například v_2(12/5)=2 a
v_2(3/4)=−2. Součet zlomků s lichými jmenovateli lze
redukovat modulo 2^a pomocí inverzí jejich jmenovatelů;
obdobně pro jmenovatele nedělitelné p modulo p^a.

## Úloha 17 a silnější doplněk odpovědi

Pro liché prvočíslo p je každý jmenovatel 1,...,p−1
jednotkou modulo p. Inverze permutují nenulové zbytky,
proto

```text
H_(p−1) = sum_{j=1}^{p−1} j^−1
        ≡ sum_{j=1}^{p−1} j = p(p−1)/2 ≡ 0 (mod p).      (V1)
```

Společný jmenovatel (p−1)! není dělitelný p; při krácení
se tedy faktor p z čitatele neztratí. Tím je dokázáno
zadání i první knižní důkaz.

Druhý důkaz používá polynomy nad polem zbytků modulo p.
Monický polynom `product_{j=0}^{p−1}(x+j)` má všechny
prvky tohoto pole za kořeny, a tedy se rovná x^p−x.
Koeficient x² je pro liché p nulový; současně jde
o c(p,2)=(p−1)!H_(p−1) podle úlohy 6. To znovu dává (V1).

Pro p>3 platí i tvrzená dělitelnost p². Spárujeme j a p−j:

```text
H_(p−1) = sum_{j=1}^{(p−1)/2} p/(j(p−j))
         ≡ −p sum_{j=1}^{(p−1)/2} j^−2  (mod p²).        (V2)
```

Inverze opět permutují nenulové zbytky, takže
`sum_{j=1}^{p−1} j^−2 ≡ sum j² ≡ 0 (mod p)`;
poslední rovnost plyne ze vzorce p(p−1)(2p−1)/6,
kde 6 je pro p>3 invertibilní. Členy j a p−j mají
stejné čtverce, takže poloviční součet ve (V2) je také
0 modulo p. Dostáváme v_p(H_(p−1))>=2. p=3 se správně
vylučuje: H_2=3/2 má v_3=1. Waringova atribuce a odkaz
Hardy–Wright jsou historické/pramenné otázky mimo tento důkaz.

## Lemma o součtu převrácených lichých čtverců

Pro liché kladné a a celé b>=0 platí

```text
sum_{j=0}^{2^b−1} 1/(a+2j)² ≡ 2^b (mod 2^(b+1)).        (V3)
```

Při b=0 jde o lichý zlomek modulo 2. V indukčním kroku
spárujeme j a j+2^(b−1); jejich liché jmenovatele se
liší o 2^b. Pro liché d máme
`(d+2^b)^−2−d^−2 ≡ 0 (mod 2^(b+1))`, protože čitatel
rozdílu je −2^(b+1)d−2^(2b), dělitelný 2^(b+1) pro b>=1.
Součet je tedy modulo 2^(b+1) dvakrát kratší součet;
indukční předpoklad dává (V3).

Rozdělení N=2^b m po m blocích délky 2^b, kde m je liché,
proto dává

```text
v_2(sum_{j=0}^{N−1} 1/(a+2j)²) = b = v_2(N).            (V4)
```

Každý blok začíná lichým a, takže (V3) platí pro všechny.

## Úloha 18: přesný exponent v lichém harmonickém součtu

Nechť `A_n=sum_{j=1}^n 1/(2j−1)`, n>=1, a n=2^a m,
kde m je liché. Pro a=0 je A_n součtem lichého počtu
lichých zlomků, tedy v_2(A_n)=0.

Pro a>=1 spárujeme lichý jmenovatel d s 2n−d:

```text
A_n=2n sum_{j=1}^{n/2} 1/((2j−1)(2n−2j+1)).            (V5)
```

Protože 2n je dělitelné 2^(a+1), je každý člen vnitřního
součtu modulo 2^(a+1) roven −1/(2j−1)². Podle (V4)
má součet těchto čtverců přesnou valuaci
v_2(n/2)=a−1. Přičtení násobku 2^(a+1) ji nemůže změnit.
Součin ve (V5) tedy má

```text
v_2(A_n)=(a+1)+(a−1)=2a.                               (V6)
```

Všechny původní jmenovatele jsou liché, takže i výsledný
zkrácený jmenovatel je lichý. Rovnost (V6) je přesně
tvrzení odpovědi: čitatel je dělitelný 2^(2a), ale nikoli 2^(2a+1).
Úloha n=0 nepoužívá; nejvyšší mocnina dělící čitatel 0
by nebyla konečná. Jde o vlastní důkaz, který nevyžaduje
znalost citovaného Selfridgeova–Silvermanova řešení.

## Úloha 19: celé harmonické hodnoty

Pro n>=1 zvolme a=floor(log_2 n), tedy 2^a<=n<2^(a+1).
Mezi 1,...,n má přesně jeden jmenovatel valuaci a:
j=2^a. Po vynásobení H_n číslem 2^a má tento člen
hodnotu 1, ostatní jsou sudé zlomky s lichým jmenovatelem.
Proto `v_2(H_n)=−a`. Pro n>=2 je to záporné, což
vylučuje celočíselnou hodnotu. Jediné možnosti jsou tedy
n=0 a n=1, s hodnotami 0 a 1. Tento argument zároveň
ospravedlňuje krok knižního důkazu o jediném maximálním
mocninném jmenovateli; pouhá přítomnost sudého jmenovatele
bez vyloučení krácení by sama nestačila.

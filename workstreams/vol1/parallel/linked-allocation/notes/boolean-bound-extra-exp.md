# Nadbytečné exp v náhradní odpovědi §2.2.3-13

Stav: **confirmed v elektronických podkladech**, bez tvrzení o prvenství
či fyzicky ověřeném dotisku. Globální identifikátor přidělí koordinátor.

## Přesné znění a zdroje

Nejde o původní stranu 547 z roku 1997. Jde o její platnou náhradní
odpověď 13 datovanou **15. 3. 2018**, `errata/pdf/all1-pre.pdf`,
strana souboru 16. Zobrazen celý originál i detail vzorce:
`images/all1-pre-file16.png`, `images/errata-answer13-detail.png`.
Vzorec je zřetelně

```
exp( (2 e n 2^n / r)^r * product_{k=0}^n binom(n,k)! ),
r = (2^(n+1)-2)/(n+1).
```

Vnější exp není artefakt OCR. Naopak primární článek
G. R. Brightwell a P. Tetali, *The Number of Linear Extensions
of the Boolean Lattice*, Order 20 (2003), 333–345, Theorem 1.3,
rovnice (1), má pouze mocninu násobenou součinem faktoriálů.
Přečten originál autorské kopie, strana souboru 3:
`images/brightwell-tetali-file3.png`,
[soubor autora](https://tetali.math.gatech.edu/PUBLIS/linextn_cube.pdf).

Pro rozlišení zápisů označme d rozměr Booleovy mřížky a N=2^d
počet jejích prvků. Má d+1 vrstev o velikostech b_i=binom(d,i).
Vrchol vrstvy i má i bezprostředních předchůdců. Parametr věty je

```
r = sum_{i=1}^d binom(d,i-1)/i
  = (1/(d+1)) sum_{i=1}^d binom(d+1,i)
  = (2^(d+1)-2)/(d+1).
```

Dosazení do Theorem 1.3 dává horní mez

```
B_d = (2 e d 2^d / r)^r * L_d,
L_d = product_{i=0}^d binom(d,i)!.
```

Přesně B_d se má nacházet v erratu. Tištěná náhrada uvádí exp(B_d).
Všechny čtyři vrstvy byly prohledány podle stran i výrazů Brightwell,
Tetali, subset/linear extensions, answer13 a exp. `all1-prepre` obsahuje
starší opravu asymptotiky z 13. 5. 2001, `all1-pre` uvedenou náhradu;
`all1` a `err1` nemají následnou opravu tohoto výrazu (stav podkladů
ověřený koordinátorem 1. 11. 2026). Relevantní originály vrstev byly
zobrazeny; nejsou jiné korekce stejného matematického tvrzení.

## Co je a není nepravdivé

Původní Sha–Kleitmanovu horní mez označme
`U_d = product b_i^(b_i)`. Jelikož B_d≥1, nerovnost
`number_of_extensions ≤ exp(B_d)` je stále pravdivá. Chyba spočívá
v nesprávné reprodukci citované věty a v tvrzení, že tento výraz
**zlepšuje** U_d. Vnější exp navíc znemožní z těchto mezí odvodit
požadovanou ostrou logaritmickou asymptotiku.

Konkrétně d=2 dává r=2, L_d=2, U_d=4, B_d=128e².
Vytištěná náhrada je exp(128e²)>4. Ani samotný B_d ještě nemusí
být ostřejší pro malé d; citované zlepšení je asymptotické.
Následující obecné porovnání není založeno na konečném testování.

Pro d≥4 platí

```
L_d ≥ 2^(sum_i (b_i-1)) = 2^(2^d-d-1),
ln U_d ≤ d 2^d ln 2.
```

První nerovnost využívá j!≥2^(j−1) pro j≥1, druhá b_i≤2^d.
Již při d=4 máme 2^(2^d-d-1)=2048 > 4·16·ln2. Poměr levé
strany k d2^d je při zvýšení d o 1 násoben
`2^(2^d-1) * d/(2(d+1)) > 1`, takže nerovnost trvá.
Proto B_d≥L_d>ln U_d a exp(B_d)>U_d pro všechna d≥4.
Případy d=1,2,3 se ověří přímo: U=1,4,729 a L=1,2,36;
B_1=4e a u d=2 je již L>ln U, u d=3 také.
Tištěné exp(B_d) tedy není zlepšením pro **žádné d≥1**.

Že odstranění exp obnoví skutečně silnější mez pro konkrétní
rozměr, lze doložit například d=16, N=65536 a r=131070/17.
Integrální odhad `ln(j!) ≤ j ln j − j + 1 + ln j` dává

```
ln(U_d/L_d) ≥ N − (d+1) − sum_i ln b_i
            ≥ N − (d+1)(1+d ln2)
            > 65247              [d=16, ln2<1].
```

Naproti tomu r<2N/17<7711 a
`2 e d N/r = e·272/(1−1/N) < 1024`, protože e<3 a N=65536.
Proto

```
ln(B_d/L_d) = r ln(2 e d N/r)
           < 7711 ln1024
           < 7711·7 = 53977 < 65000,
```

kde ln1024=10ln2<7. Poslední standardní odhad ln2<0.7
plyne např. z e^0.7>1+0.7+0.7²/2+0.7³/6+0.7⁴/24>2.
Tedy B_16<U_16, zatímco exp(B_16)>U_16.

## Návrh hlášení (English ASCII)

In the replacement answer to exercise 2.2.3-13 (page 547), dated
15 March 2018 in all1-pre, the outer `exp(...)` should be deleted.
Brightwell and Tetali's Theorem 1.3 gives

    (2 e n 2^n / r)^r * product_{k=0}^n binom(n,k)!,
    r = (2^(n+1)-2)/(n+1),

without the outer exponential. The displayed expression remains an
upper bound, but it exceeds the earlier Sha--Kleitman bound for every
n >= 1 and therefore does not give the stated improvement. For example,
at n=2 the old bound is 4 and the displayed replacement is exp(128 e^2).
The author-hosted paper states the required bound explicitly in (1).

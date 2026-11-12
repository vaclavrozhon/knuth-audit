# V2-C0033: Fibonacciho řádek obsahuje ocas místo přesné délky

**Confirmed**,1.11.2026. §3.3.3-27, tabulka na tištěné
str.576 (soubor588), [sken](../images/vol2-p576.png)
i zvětšený detail přečteny vizuálně.

Nechť L je délka vzestupného běhu začínajícího U1,
podmíněno U0>U1. Fibonacciho čísla mají F0=0,F1=1
a `F_(n+2)=F_(n+1)+F_n`. Pro generátor
`U_(n+1)=(U_n+U_(n−1)) mod 1` je vytištěný obecný
vzorec pravděpodobnosti přesné délky **správný**:

```text
Pr(L=1)=1/2,
Pr(L=k)=1/(F_(k−1)F_(k+1))−1/(F_k F_(k+2)), k>1.
```

Fibonacciho řádek tabulky však obsahuje `Pr(L>k)`.
Správné srovnání pro délku přesně k je:

| k | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Vytištěno | 1/2 | 1/3 | 1/10 | 1/24 | 1/65 |
| Správně | 1/2 | 1/6 | 7/30 | 7/120 | 41/1560 |

Řádek nezávislých náhodných čísel pod ním je správný
a používá přesné délky, takže nejde pouze o jiný popisek.

Přímý geometrický důkaz: pišme x=U0,y=U1. Podmíněné
rozdělení má hustotu2 na trojúhelníku `0<y<x<1`.
Dokud běh roste, nedošlo k přetečení přes1, takže
`U_k=F_(k−1)x+F_k y`. Pro k>=2 má oblast L>=k
vrcholy `(0,0),(1/F_(k−1),0),(1/F_(k+1),1/F_(k+1))`.
Její dvojnásobná plocha je `1/(F_(k−1)F_(k+1))`.
Rozdíl sousedních ocasů dokazuje vzorec i opravený řádek.
Pro k2 jde konkrétně o pás `x+y<1<x+2y` s plochou1/12,
tedy podmíněnou pravděpodobností1/6.

Nezávislé racionální ořezávání polygonů přímo podle
rekurence ověřilo prvních15 délek bez použití Fibonacciho
vzorce při konstrukci oblastí; [výsledky](../results/theoretical-tests.json).
Fig.A-2 a obecný vzorec není třeba měnit.

Všechny čtyři vrstvy errat i aktuální TeX prohledány1.11.2026
podle576, answer27, Fibonacci, run a permutation. Oprava
tohoto řádku nebyla nalezena. Fyzický poslední dotisk ani
prvenství neověřeny; ASCII draft neodeslán.

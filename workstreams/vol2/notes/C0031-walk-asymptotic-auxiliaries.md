# V2-C0031: pomocné chyby v asymptotice procházek

**Confirmed**, 1.11.2026. §3.3.2-33, odpověď str.571;
celá původní strana i zvětšený detail byly vizuálně přečteny.
Hlavní asymptotický výsledek je správný, ale odvození obsahuje
následující chyby. Sdružujeme je pod jedním ID téhož důkazu.

Položme m=k−2l, n=l a L=m+3n=k+l. Před vyloučením nulového
počátečního stavu má počet jedniček W generující funkci

```text
F(z)=((1+z)/2)^m ((1+3z²)/4)^n.
```

1. Pro liché L koeficient `[z^((L−1)/2)] F(z)/(1−z)` je
   Pr(W<L/2), tedy pravděpodobnost převahy nul. Pro požadovanou
   převahu jedniček je nutný jeho komplement. Například k4,l1
   má primitivní rekurenci s periodou15: koeficient je7/16,
   požadovaná pravděpodobnost před podmíněním je9/16, po něm9/15.
   Toto není rozdíl způsobený zanedbáním nulového stavu.
2. Pro vytištěné `g(z)=log F(z)−(L−1)log(z)/2` platí
   `(d/dx)g(exp(x))` v x=0 rovno1/2. Lineární člen rozvoje
   g(exp(epsilon u)) je tedy **+epsilon u/2**, nikoli záporný.
3. Druhý integrální vzorec s faktorem1/(2pi i) má vpravo
   **1/sqrt(2pi)** místo sqrt(2pi):

```text
(1/(2pi i)) integral_(a−i infinity)^(a+i infinity)
    exp(u²/2) u^(2j) du
 = (−1)^j (2j−1)!! / sqrt(2pi).
```

   Zde a je libovolné pevné reálné číslo a dvojitý faktoriál
   znamená součin kladných lichých čísel do2j−1, pro j0 hodnotu1.
   Pro a0,j0 stačí u=it a obyčejný Gaussův integrál. První
   vytištěný integrál, jehož cesta vede přes **+1**, je správný;
   nezaměňovat jej s cestou přes−1 použitou dříve v textu.
4. Zbytek v posledním vzorci pro centrální koeficient má mít
   `O((m+3n)^(-3/2))`, nikoli `O((m−3n)^(-3/2))`. Platná
   primitivní volba k7,l3 dává m1,n3, tedy m−3n=−8, zatímco
   L=10 je sudé. Přesný počet i uniformní odhad závisí na L.

[Vlastní Fourierův důkaz](lfsr-walks.md) potvrzuje hlavní
asymptotiku i opravený centrální odhad rovnoměrně pro m>=1,n>=0.
Přímé počty fází a18 přesných binomických modelů
poskytují další kontrolu; hlavní výsledek nezávisí na opravách
výše. Rozvoj1/(1−exp(epsilon u)) naopak správně používá B_2;
na tomto místě není problém s globální změnou B_1 z2021.

Všechny čtyři vrstvy errat i aktuální TeX prohledány1.11.2026
podle571, answer33, asymptotic a random walk. Oprava odpovědi32
z2005 je jiný odstavec; pro uvedené řádky oprava nenalezena.
Fyzický dotisk a prvenství neověřeny; draft neodeslán.

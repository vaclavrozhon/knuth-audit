# V2-C0028: nesprávný posun lineárního členu pro různé partice

**Confirmed**, 1.11.2026. §3.3.2-30, odpověď str.569, odstavec
začínající „With q_n(m)“. Původní obraz569 vizuálně přečten;
zvětšený detail potvrzuje tištěný přírůstek
`alpha(n^(1/2)−n^(−1/2))/2` ke koeficientu c_1.

Zde p_n(m) počítá partice na nejvýše n částí, q_n(m) partice
na n různých kladných částí a N=n(n+1)/2. Platí q_n(m)=p_n(m−N).
Integrand pro p je exp(f(z)), kde
f(z)=−m log(z)−sum_(k=1)^n log(1−z^k). Přechod ke q proto
znamená přesnou náhradu f(z) -> f(z)+N log(z).

Na integrační cestě z=exp(−rho+i delta t), rho=n/m a
delta=sqrt(n)/m, přibude do exponentu přesně

```text
−N rho + i N delta t.
```

Konstantní faktor exp(−N rho) je v knize správný. Koeficient
c_1, definovaný exponentem i c_1 t, však musí vzrůst o

```text
N delta = alpha/2 · (n^(−1/2)+n^(−3/2)),   m=n³/alpha.
```

Například n=2,m=8,alpha=1 dává přírůstek3sqrt(2)/8, zatímco
tištěný výraz dává sqrt(2)/4. Pro velká n je správný přírůstek
řádu n^(−1/2), tištěný řádu n^(1/2). Rozpor nezávisí na
Bernoulliho konvenci ani chybě C0025. Výsledný vzorec pro q_n
je přesto správný; vlastní důkaz je v `partition-certificate.md`.

Všechny čtyři vrstvy errat i aktuální TeX prohledány1.11.2026
podle569, c_1, linear coefficient a partition. Oprava nenalezena.
Nejnovější fyzický tisk ani prvenství neověřeny; draft neodeslán.

# V2-C0126 — derivace patří do bodu -1, ne +1

Stav: **confirmed**. §4.5.2-30, str.645, první dva rozvoje.
Originál644–645 i zvětšené body derivací byly vizuálně přečteny.
V obou vzorcích je vytištěno a'(1), resp. b'(1). Správně má být
a'(-1), resp. b'(-1).

Pro h=a nebo b je Mellinův integrand
`pi*h(s)*x^(-s)/((2^(s+1)-1)*sin(pi*s))`. Při e=s+1 jsou
rozhodující členy

```text
h(s)=h(-1)+e*h'(-1)+O(e²),
pi/sin(pi*s)=-1/e+O(e),
1/(2^e-1)=1/(e*ln2)-1/2+O(e),
x^(-s)=x(1-e*ln x+O(e²)).
```

Reziduum dvojpólu je tedy
`x*(h(-1)*(lg x+1/2)-h'(-1)/ln2)`, přímo určující opravu.
Definice a,b na644 i ostatní členy rozvoje jsou tím respektovány.

Tištěné hodnoty nemohou být alternativním správným zápisem.
Funkce b(s) má v s=1 pól s hlavní částí -1/((s-1)ln2), takže
b'(1) není konečná. U a přímé kladné součty dávají a'(1)>a'(-1)>0.
Numericky jsou a'(-1)=0.05567376764497...,
a'(1)=0.11742430247488..., b'(-1)=0.22798291450244....
Numerika je pouze doplněk přesného důkazu.

Všechny opravené rozvoje nezávisle porovnány s přímými součty
v `gcd-second.md` a `results/gcd-second.json`;46419 exit0.
Čtyři vrstvy errat prohledány2026-11-02 podle644/645, úlohy30,
Mellinových rozvojů a derivací; oprava nenalezena. Poslední
fyzický dotisk/priorita neověřeny, návrh neodeslán.

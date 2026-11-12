# §1.2.9-21: integrační konstanta a V1-C0012

Audit 1. listopadu 2026. Zadání s. 95 (strana souboru 110)
a odpověď s. 498 (513) byly zobrazeny. Pro formální řadu
`G(z)=sum_{n>=0} n! z^n` odpověď správně dostává diferenciální
rovnici

```text
z^2 G'(z)+zG(z)=G(z)-1.                                (A1)
```

Formální řada znamená posloupnost koeficientů s algebraickými
operacemi po koeficientech; její použití zde nepředpokládá
konvergenci pro nenulové z. Analytické řešení (A1) na z<0 je

```text
G_C(z)=(-1/z) exp(-1/z) (E1(-1/z)+C),                  (A2)
E1(u)=integral_u^infinity exp(-t)/t dt,  u>0,
```

kde C je libovolná konstanta. Odpověď následně označuje řadu
za asymptotický rozvoj uvedené funkce pro z<0. Asymptotický
rozvoj zde znamená, že po odečtení prvních N členů je zbytek
O(|z|^N) pro každé pevné N při z->0-. Toto tvrzení vyžaduje C=0.

## Protipříklad a správná normalizace

Položme u=-1/z, takže z->0- odpovídá u->infinity. Substituce
t=u+v dává

```text
G_0(-1/u)=u exp(u) E1(u)
         =integral_0^infinity exp(-v)/(1+v/u) dv -> 1.  (A3)
```

Limitní přechod plyne z majoranty exp(-v), jejíž integrál je 1.
Naproti tomu pro C=1 platí `G_1(-1/u)=G_0(-1/u)+u exp(u)`
a tato funkce roste do nekonečna. Nesplňuje ani první člen
požadovaného rozvoje, tj. limitu 1. Pro každé komplexní C!=0
roste velikost přidaného členu a stejný závěr zůstává v platnosti.

Pro C=0 máme dokonce přesný zbytek. Pro celé N>=1 použijme
konečnou geometrickou identitu v integrálu (A3):

```text
G_0(z)=integral_0^infinity exp(-v)/(1-zv) dv
      =sum_{j=0}^{N-1} j! z^j
        +z^N integral_0^infinity exp(-v) v^N/(1-zv) dv,
                                                     z<0. (A4)
```

Protože 1-zv>=1, má zbytek velikost nejvýše N!|z|^N.
Navíc po vydělení z^N konverguje k N!, takže souhlasí i
následující koeficient. Integrály `integral exp(-v)v^j=j!`
plynou opakovanou integrací per partes. To je úplný důkaz
rozvoje bez odvolání na Stirlingův vzorec či numeriku.

Rovnici (A1) lze ověřit derivováním (A2); homogenní řešení
je `(-1/z)exp(-1/z)`. Porovnání koeficientů (A1) dává a_0=1
a a_n=n a_(n-1), tedy a_n=n!. Pro n>=2 je
`n! >= (n/2)^(n/2)` (alespoň n/2 horních faktorů), takže
`(n!)^(1/n) >= sqrt(n/2) -> infinity`. Poloměr konvergence
formální řady je proto nula. Divergence řady nebrání
asymptotickému rozvoji jediné normalizované funkce G_0.

## Errata, primární kontrola a závažnost

Ve všech pěti vrstvách errat byly hledány strana 498,
odpověď 21, E1, asymptotický rozvoj a Knopp. Známá oprava
z 15. dubna 2002 sjednocuje argument E1(x) na E1(z).
Opravy z 9. května 2021 a 29. března 2023 opravují bibliografii
Knoppovy knihy. Žádná z nich nevybírá C=0. Originály příslušných
stran errat byly zobrazeny v tomto a předchozích blocích.

Nezávislý primární zdroj
[DLMF 6.2.1–6.2.2](https://dlmf.nist.gov/6.2#E1)
potvrzuje definici a posunutý integrál E1;
[DLMF 6.12.1](https://dlmf.nist.gov/6.12#E1)
udává odpovídající rozvoj a mez prvním vynechaným členem
na kladné reálné ose. Tyto části byly přečteny online;
Knoppova citovaná §66 zatím přečtena nebyla.

**V1-C0012 je confirmed, drobné chybějící upřesnění:**
v asymptotické větě má být uvedeno „with C=0“.
Rovnice i obecné řešení jsou správné; závěr o rozvoji nemá
platnost pro celou uvedenou rodinu. Prvenství ani fyzický
exemplář nejsou ověřeny. Nic nebylo odesláno.

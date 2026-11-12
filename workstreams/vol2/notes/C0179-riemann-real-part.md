# V2-C0179: nepárovaná řada v Riemannově formuli

Stav **confirmed**, zadání§4.5.4-25,str414.
Součet je omezen na nuly rho=sigma+i*tau s tau>0,
ale integrál není nahrazen reálnou částí. Faktor2
sám konjugované příspěvky nenahradí.

Označme I_rho(x) právě vytištěný horizontální integrál
od−infty do sigma. Pro každé pevné x=p^k platí

```
sum_(0<tau<=T) I_rho(x)
 = i/(2*pi*k)*log T+K_x+o(1).
```

Nepárovaná řada tedy diverguje, už při x=2. Nejde jen
o možnost nepatrné imaginární numerické chyby. Důkaz v
[riemann-explicit.md](riemann-explicit.md), (R8)–(R9),
používá Landauovu nepodmíněnou formuli, vlastní integraci
per partes a parciální sumaci s absolutně konvergentním zbytkem.

Oprava: sčítat **reálné části jednotlivých integrálů**, s nulami
uspořádanými podle tau a s násobnostmi. Ekvivalentně lze
vynechat2 a sčítat obě poloroviny v symetrickém pořadí.
Reálnou část je nutné vzít před limitou nepárovaného součtu.

Originál414 vizuálně včetně zvětšeného výřezu; vlastní
komplexní integrály jsou ověřeny36intervalovými kvadraturami.
Mangoldtův originál300–301 výslovně zachovává obě větve.
Gonekova první strana uvádí použitou Landauovu formuli.
Celé čtyři vrstvy errat a aktuální TeX neobsahují nalezenou
opravu této části zadání. Změna2011 n→x v odpovědi je jiná.
Fyzický poslední dotisk a priorita neověřeny, návrh neodeslán.

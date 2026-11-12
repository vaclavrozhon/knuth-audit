# V2-C0134: empirická formule není celkový součet podílů

Stav: **confirmed**, chybná slovní normalizace v odpovědi
§4.5.3-35, strana654, první řádek. Toto místo označuje
následující výraz za „the sum of all partial quotients“.
Zadání na378 přitom výslovně sčítá přes všechny zlomky m/n,
1<=m<n. Pro tento celkový součet nemůže uvedená formule
platit, ani jako domněnka s uvedeným zbytkem.

Označme Q(n)=sum_(1<=m<n) A(m,n), kde A(m,n) je součet
podílů kanonického rozvoje m/n. T_n v knize znamená
průměr počtu dělení v Eukleidově algoritmu při pevném
větším argumentu n a druhém argumentu z0,...,n-1.
Není to součet počtů dělení. Označme R(n) hlavní výraz
na654, bez posledního O(n^-1/2).

## Důkaz nezávislý na zamýšlené domněnce

Nechť p je prvočíslo. Zlomek1/p má jediný podíl p, tedy
Q(p)>=p. Každé dva eukleidovské kroky zmenší kladný
zbytek alespoň na polovinu, takže T_p<=2 log_2 p+2.
Prvočíselná suma v tištěném výrazu má při n=p jediný člen:

```
(4/p - (p+1)/p^2 * (p-1)/(p-1)) (ln p)^2
       =(3/p-1/p^2)(ln p)^2.
```

Proto R(p)=O((log p)^2). Jelikož prvočísel je nekonečně
mnoho, Q(p)-R(p)>=p-O((log p)^2) nemůže být O(p^-1/2).
Žádná volba konstanty v tištěném O tento rozpor neodstraní.
Argument nevyžaduje důkaz hlubší asymptotiky z úlohy35,
ani přesné určení konstanty2.542875.

Vlastní důkaz v euclid-subtractive.md, oddíly1–5, navíc
dává Q(n)~(6/pi^2)n(log n)^2. Tištěný hlavní výraz má
velikost průměru, tedy o faktor n menší. Z textu musí být
zřejmé, jaký průměr a jaká konvence posledního odečtení
jsou zamýšleny. Pouhé přidání slova „average“ zde
neprohlašujeme za ověřenou úplnou opravu všech konstant.

## Konečná ilustrace a hranice závěru

Pro n=10007 dává přesný výpočet Q(n)=655938 a
nT_n=92364. Intervalová aritmetika dává

```
64.56709510834198 < R(10007) < 64.56709510834200.
```

Tento jediný příklad by sám asymptotické O nevyvracel;
důkazem je rodina všech prvočísel výše. Číselná kontrola
jen názorně ukazuje nesoulad měřítek. Program a úplné
intervaly pro tři prvočíselné vstupy jsou v
verify_euclid_subtractive.py a results/euclid-subtractive.json.

Průměr odečítání do rovnosti je
S(n)=(Q(n)-(n-1))/n. Průměr do nulového zbytku se od něj
liší o1. V auditovaných podkladech nebyl získán původní
Pittewayův a Castleův článek z roku1988; jeho přesnou
konvenci ani pravdivost normalizované domněnky netvrdíme.
Hlavní zadání35 a jeho dokázaná asymptotika jsou správné.

## Doklady a errata

Vizuálně přečteny původní strany378,653 a654, poslední také
ve vyšším rozlišení. Prohledány all2-prepre, all2-pre,
all2 a err2 dne2026-11-03 podle stránek, autorů, slov
„partial quotients“ a konstanty. Oprava z2003-07-12 mění
pouze „its“ na „Its“ v názvu časopisu na653. Žádná
normalizační oprava není v našich čtyřech řadách uvedena.
Zkontrolován také původ dodatku: starší errata druhého
vydání, oprava1995-10-07 k odpovědi35 na606, už obsahují
stejnou formulaci. To není oprava zjištěného problému.

Neověřen poslední fyzický dotisk, priorita ani nárok na
odměnu. Anglický ASCII návrh hlášení zůstává neodeslaný.

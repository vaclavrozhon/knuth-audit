# V2-C0208: sx+t versus x+s v opravě odmocnin

Stav: **confirmed**. Oprava §4.6.2–15, 7. srpna 2001, `all2-prepre`,
strana souboru 43; nahrazuje řádky 4–9 příslušného odstavce na 681.
Původní oprava byla vizuálně zobrazena, není to závěr pouze z OCR.

První vzorec používá gcd(x²−u,(sx+t)^((p−1)/2)−1), ale dále uvádí
počet hodnot s nejméně (p−1)/2 a algoritmus s posuny x+s. Pro p=5,
u=1,t=0 žádná hodnota s nerozdělí kořeny ±1: s a −s jsou současně
čtverce nebo nečtverce. Nezachrání to ani podmínka t≠0: pro p=7,
u=1,t=3 uspějí právě s=2,5, tedy jen 2 hodnoty místo nejméně 3.

Oprava: sx+t → x+s. Pro posuny platí přesný počet
(p+1+χ(2a)+χ(−2a))/2, kde a²=u a χ je kvadratický charakter;
to je právě (p−1)/2 plus 0,1 nebo 2, jak správně říká zbytek errata.
Důkaz a nezávislá kontrola gcd proti hodnotám na kořenech jsou v
[sqrt-mod-prime.md](sqrt-mod-prime.md), §2, a výsledkovém JSON.

Všech šest vrstev errat prohledáno 4. listopadu 2026. Nález je chyba
vzorce v historické opravě, nikoli nově prokázané selhání posunového
algoritmu. Nejnovější fyzický dotisk a prvenství neověřeny, neodesláno.

# V2-C0035: spojité testy potřebují výjimku a=1

**Confirmed**,1.11.2026. §3.3.3-22 až24, zadání str.92
a odpovědi575–576. [Zadání](../images/vol2-p092.png)
a obě odpovědi byly přečteny vizuálně;22 říká pouze,
že a je celé a `0<=theta<1`. V kontextu násobitelů
generátoru není a=1 vyloučeno a může dát plnou periodu.

Pro `s(x)=(ax+theta) mod 1`, a=1 a rovnoměrné x na[0,1)
nastává s(x)<x právě pro `1−theta<=x<1`. Pravděpodobnost
je tedy **theta**, nikoli vytištěná1/2. Například theta1/4
dává1/4. Zvláště pro theta0 je s(x)=x, takže pravděpodobnost
libovolného přísného poklesu je0. Úloha24 však pro t2
dává1/2 i při a1.

Stačí v úlohách22–24 vyžadovat a>1, nebo přidat zvláštní
odpovědi pro a1. Vzorce odpovědí22 a23 dělí výrazem a−1
a nelze je na tento případ používat. Hlavní spojitý vzorec
korelace21 naopak při a1 funguje; nejde o chybu v něm.

Známá oprava22 z3.2.2005 přidává rovnoměrné rozdělení x;
výjimku a1 neřeší. Čtyři vrstvy errat i aktuální TeX
prohledány1.11.2026 podle92,575,576, answer22, answer24,
descending. Další relevantní oprava nenalezena.
Fyzický nejnovější dotisk ani prvenství neověřeny.

Oddělená interpretační poznámka: komentář za odpovědí23
o nemožnosti dosáhnout1/6 je podložen pro velké a.
Pro a2,theta1/3 nebo2/3 a a3,theta1/2 je přesná hodnota
naopak1/6. To nevyvrací vytištěnou asymptotiku; v auditu
ji neinterpretujeme jako tvrzení bez omezení na velké a.

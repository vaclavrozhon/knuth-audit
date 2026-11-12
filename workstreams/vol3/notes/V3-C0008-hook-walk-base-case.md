# V3-C0008 — počáteční případ indukce hook walk

Potvrzená drobná chyba v odpovědi §5.1.4-38(a), s.613 / file624:
„k=l=1“ má být „k=l=0“. Úloha na70 definuje I={i0,…,ik}, J={j0,…,jl};
jediný rohový vrchol tedy odpovídá k=l=0 a má pravděpodobnost1/n.

Protipříklad k vytištěné větě: čtvercový tvar3×3, n=9, roh(3,3),
I=J={1,3}. Zde k=l=1. Existují dvě přípustné cesty:
(1,1)→(1,3)→(3,3) a(1,1)→(3,1)→(3,3). Stupně jsou4,2,0.
Každá cesta má pravděpodobnost(1/9)(1/4)(1/2)=1/72, dohromady1/36,
nikoli1/9. To souhlasí s dokazovaným součinem1/(n*d13*d31)=1/36.
Samotný vzorec úlohy a hook-walk konstrukce nejsou zpochybněny.

Sazba images/tableaux-file-081.png a624.png prohlédnuta. V all3-prepre,
all3-pre,all3,err3 není oprava tohoto počátku indukce. Dodatek odpovědi38
na staré s.594 v err3-1e z21.5.1995 už opakuje k=l=1, neopravuje jej.
Výřezy sources/tableaux-errata-review.json. Prvenství/fyzický výtisk
neověřeny; ruční výpočet dvou cest, žádná enumerace.

# V2-C0115: nulová oblast nejmenších slash formátů

**confirmed**, 2. listopadu 2026. §4.5.1-12, zadání na str. 333,
odpověď na str. 639, pravidlo při shodě na str. 332. Všechny tři
strany přečteny v původní sazbě třetího vydání, prvního tisku 1997.

Odpověď tvrdí bez kvalifikace q, že round(x)=0 právě tehdy,
když |x|<=2^(1-q). Pro q=1 jsou však reprezentovatelné pouze
0/1 a +/-1/0. Vstup x=1 leží přesně na mediánu 0/1 a 1/0.
Pravidlo menšího jmenovatele vybere 1/0, nikoli nulu.
Tento protipříklad používá pouze kladný vstup a jednoznačnou
první větev pravidla pro shodu.

Pro q=1 je nulová oblast (-1,1). Při doslovné volbě menšího
podepsaného čitatele je pro q=2 nulová oblast (-1/2,1/2]; bod
-1/2 totiž zaokrouhlí na -1/1. Pro q>=3 je tištěná formule správná.
Stačí proto připojit předpoklad q>=3, případně vypsat oba malé
případy. Praktické formáty q=27/58 nejsou dotčeny.

Důkaz a nezávislé úplné mřížky jsou v
[rational-slash.md](rational-slash.md) a `results/rational-slash.json`.
Čtyři vrstvy errat prohledány, oprava nenalezena. Poslední fyzický
dotisk ani priorita neověřeny; návrh hlášení neodeslán.

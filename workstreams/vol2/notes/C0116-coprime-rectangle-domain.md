# V2-C0116: chybějící obor platnosti počtu nesoudělných dvojic

**confirmed**, 2. listopadu 2026. §4.5.1-14, zadání na str. 333,
odpověď na str. 640. Obě stránky přečteny v původní sazbě třetího
vydání, prvního tisku 1997. Zadání říká celé dvojice a neomezuje
dolní meze M1,N1 na nezáporná čísla.

Tištěná Möbiova suma končící na min(M2,N2) předpokládá kladné
souřadnice. Pro M1=-1,M2=1,N1=0,N2=2 jsou přípustné nesoudělné
dvojice právě (0,1),(1,1),(1,2). Tištěná suma má jediný člen
mu(1)*(1-(-1))*(2-0)=4, zatímco správný počet je 3. Chybně
započte (0,2). Zlomky s nulovým čitatelem přitom patří přímo
do motivujícího kontextu úlohy.

Jednoduchá oprava je doplnit 0<=M1 a 0<=N1. Pro obecné celé
intervaly je třeba upravit mez sumy a zvlášť vyloučit (0,0);
úplný vzorec i důkaz jsou v [rational-slash.md](rational-slash.md).
Implementace ověřena na 3025 obecných a 2025 kladných obdélnících
proti přímému výčtu. Velké počty hodnot v odpovědi 13 jsou správné,
protože se počítají pouze kladné čitatele a nula se přidává zvlášť.

Čtyři vrstvy errat prohledány, odpovídající oprava nenalezena.
Poslední fyzický dotisk a priorita neověřeny; hlášení neodesláno.

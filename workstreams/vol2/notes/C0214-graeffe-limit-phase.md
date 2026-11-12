# V2-C0214: znaménko limity Gräffeho iterace

Stav: **confirmed**. Odpověď §4.6.2–20, strana 683, odstavec pod tabulkou c_t.
Věta o limitě normalizovaného polynomu x^m vynechává fázi.

Pro reálný u=2x-1 je jediný kořen 1/2, tedy m=1. Při transformaci
hat(u)=u(sqrt(x))*u(-sqrt(x)) je t-tý nenormalizovaný iterát
1-2^(2^t)x pro t>=1. Normalizace kladnou eukleidovskou normou dává
limitu -x, nikoli x. V reálném případě je opravená limita (-1)^m*x^m.
Pro obecné komplexní koeficienty je třeba odstranit jednotkovou fázi;
ta nemusí konvergovat. Odhady M(u) a rychlost jejich sbližování
zůstávají platné. Jde o doprovodné tvrzení, ne o selhání metody.

Obecný důkaz: [integer-factorization.md](integer-factorization.md), §3.
Sazba683 zobrazena, šest vrstev errat prohledáno 4.11.2026;
oprava nenalezena. Novější fyzický dotisk/prvenství neověřeny. Neodesláno.

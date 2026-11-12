# C0163: erratum přidává složený exponent 77232017

**Stav:** confirmed v původním PDF all2-pre, str. 11,
dodatek z 24. dubna 2019 ke str. 409, seznam (26).

Tištěné 77232017 má být **77232917**. Číslo s chybným
exponentem nemůže být prvočíslem, neboť

    77232017 = 19 * 29 * 140167 = 19 * 4064843,
    2^19−1 = 524287 dělí 2^77232017−1.

Druhý vztah plyne z rozkladu x^b−1 na (x−1) krát
geometrický součet, s x=2^19 a b=4064843. Dělitel je
vlastní. Přímé modulární ověření souhlasí.

Správnou hodnotu potvrzuje oficiální GIMPS zpráva o
Paceově objevu z 26. prosince 2017. Podrobnosti, výsledek
a odkazy jsou v [mersenne-context.md](mersenne-context.md).
PDF strana byla zobrazena; není to OCR chyba. Další
vrstvy errat ani aktuální TeX opravu neobsahují.
Novější fyzický tisk a prvenství neověřeny. Nic neodesláno.

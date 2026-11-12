# V2-C0199: Brownova úprava při stejných stupních

Stav: **confirmed**. §4.6.1–25, odpověď na straně 678.

Pro primitivní u=2x^3+x+1,v=2x^3+x^2+1 má první pseudodělení
2u=2v+(-2x^2+2x). První stupeňový rozdíl je delta=0, společný
vedoucí faktor c=2. Větev C3 proto vrátí nový polynom -x^2+x,
ale současně vyžaduje h=2^0/2=1/2, který nepatří do Z.

Nález se týká příslibu algoritmu pracovat nad původním UFD; netvrdí,
že při povolení zlomků vznikne nesprávný gcd. Stačí omezit optimalizaci
na přísně různé vstupní stupně, nebo provést při rovnosti jeden
primitivní krok E a poté úpravu znovu inicializovat. Obecný důkaz
opravy je v `polynomial-c-extensions.md`.

Původní sazba `images/vol2-p678.png` přečtena. Relevantní historické
vrstvy, aktuální errata a TeX prohledány; odpovídající oprava nenalezena.
Nejnovější fyzický dotisk a prvenství neověřeny. Přesný protipříklad
je v `results/polynomial-c-extensions.json`; hlášení neodesláno.

# V2-C0117 — jednobitová výjimka v přesném nejhorším čase

Stav: **confirmed**, drobný okrajový případ. §4.5.2, str. 340, odstavec
o nejhorším čase programu B; související poslední věta odpovědi 37 na 645.

Originál na 340 tvrdí dosažení maxima `13N+8` pro `1<=u,v<2^N`, s B=1.
Při N=1 existuje pouze (1,1). Její počty jsou A=B=D=E=0, C=1, tedy
`6+13=19`, nikoli 21. Vzorec zůstává správnou horní mezí. Pro N>=2 je
dosažené maximum 13N+8 obecně dokázáno v `gcd-basic.md`.

Odpověď 37 udává nejmenší příklad s n odečteními jako
`(2^(n-1)+1,2^(n-1)-1)`. Při n=1 vyjde nepovolená dvojice (2,0).
Správná nejmenší kladná dvojice je (1,1); obecný příklad platí pro n>=2.

Oprava: u prvního tvrzení doplnit N>=2 a případ N=1 uvést zvlášť;
u druhého doplnit n>=2. Algoritmus ani hlavní asymptotika nejsou vadné.

Doloženo zobrazením `images/vol2-p340.png`, `images/vol2-p645.png`;
čas nezávisle potvrzen instrukčním interpretem i součtem vytištěných cen.
Čtyři vrstvy errat (`all2-prepre`, `all2-pre`, `all2`, `err2`) prohledány
2026-11-02 podle stran, úlohy a obsahu; odpovídající oprava nenalezena.
Neověřeno v aktuálním fyzickém dotisku, prvenství neověřeno, neodesláno.

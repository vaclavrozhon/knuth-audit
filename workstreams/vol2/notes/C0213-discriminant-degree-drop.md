# V2-C0213: diskriminant při poklesu stupně

Stav: **confirmed**. Odpověď §4.6.2–23, strana 686, první odstavec.
Vytištěná ekvivalence mezi násobným faktorem modulo p a dělitelností
diskriminantu potřebuje předpoklad p nedělící vedoucí koeficient.

Primitivní u=2x^2+2x+1 má diskriminant -4, ale modulo 2 je u=1.
Také u=2x^3+2x^2+x+1 má diskriminant -72, zatímco modulo 2 je x+1.
Oba polynomy jsou nad Q bez násobných faktorů. Druhý příklad ukazuje
problém i s nekonstantním zbytkem. U neprimitivního vstupu je navíc
třeba vyřadit prvočísla dělící obsah.

Konečnost výjimečných prvočísel i vytištěný seznam pro monický polynom
(22) zůstávají správné. Obecný opravený důkaz a nezávislý determinant
jsou v [integer-factorization.md](integer-factorization.md), §6.

Sazba686 zobrazena; všech šest vrstev errat prohledáno 4.11.2026,
odpovídající oprava nenalezena. Fyzický dotisk/prvenství neověřeny.
Nic neodesláno.

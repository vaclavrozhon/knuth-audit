# V2-C0118 — chybějící absolutní hodnota v odpovědi 15

Stav: **confirmed**. §4.5.2-15, str. 641, dovětek v hranaté závorce.
Algoritmus X je na 342, zadání na 354; originály byly zobrazeny.

Pro u=1,v=2 má X po inicializaci vektory (1,0,1), (0,1,2).
Po kvocientu 0 jsou to (0,1,2), (1,0,1); po kvocientu 2 pak
(1,0,1), (-2,1,0). Koncové v1=-2, tedy v1*u=-2, zatímco lcm(1,2)=2.

Správně platí `|v1*u|=lcm(u,v)`. První věta odpovědi sama správně uvádí
`v1=±v/u3`; znaménko se ztratí až v dovětku. Tabulka vlastního příkladu
na str. 343 má rovněž záporné koncové v1, totiž -710.

Ještě výjimka u=v=0: je v povoleném nezáporném oboru algoritmu X,
který skončí okamžitě s (v1,v2)=(0,1). Úvodní podílový vzorec odpovědi
15 zde dělí nulou, takže má být omezen na u3>0 a nulový vstup vyřízen zvlášť.
Opravená rovnost s absolutní hodnotou sama platí i pro oba nulové vstupy.

Obecný důkaz přes unimodulární matici (celočíselnou matici s determinantem
±1) a reprodukce jsou v `gcd-basic.md`, `verify_gcd_basic.py`,
`results/gcd-basic.json`. Čtyři vrstvy errat byly prohledány 2026-11-02;
obsahují jiné opravy odpovědí 10 a 14 na této straně, ale tuto nikoli.
Aktuální fyzický dotisk ani prvenství neověřeny. Neodesláno.
